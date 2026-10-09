# Reading (and writing) Data Layer RT memory maps

Read this before writing PLC code that accesses a ctrlX Data Layer **real-time (RT) node** through its memory map. Examples:
- `motion/realtime/cyclicStatusData` (cyclic axis status),
- `fieldbuses/ethercat/master/instances/<master>/realtime_data/input|output` (EtherCAT process image),
- `plc/admin/retain`,
- `motion/axs/<ax>/cmd-input/double`.

`datalayer/nodesrt` lists them all.

It replaces tedious I/O mapping: the PLC finds each value by **name** at runtime, so a changed configuration doesn't need remapping by hand.

## What an RT node is

- It's a **packed byte buffer** in shared memory. Its children are `info` (type, `sizeBytes`), `map` and `data`.
- The **map** lists the variables. Each has a `name`, a `bitoffset` (**in bits**), a `bitsize` and a `type` (`types/datalayer/float64`, `bool8`, `uint16`, ...). The map also has a `revision`, which changes when the variable list changes.
- **Packed** means an LREAL can start on any byte. Never overlay a struct or dereference a `POINTER TO LREAL` into the buffer. Copy byte by byte.
- `bool8` is one byte (0/1). All values are little-endian, the same as the PLC.
- Map names are paths. In motion they look like `Ax1/ActualPos` (`<axis>/<field>`). EtherCAT names are dotted (`<device>.<signal>`, see the example).

**Look at the real map first.** Use the `ctrlx-rest` skill: `dl.py rtmap <node>` lists the variables sorted by offset, and `dl.py rtdata <node>` decodes the live buffer. Write down the exact names before you write the lookup table.

## PLC API

Libraries: **`CXA_Datalayer`** (`DL_MemUser`, `DL_NODEVALUE`, `DL_RESULT`) and **`CXA_AutomationCore_fbs`** (`comm_datalayer_MemoryMap`, `comm_datalayer_Variable`).

The calls below come from a working user example (`datalayer-rt/example-fbOpenIO-ethercat.txt`) and from the `DL_MemUser` section of `libs/10_CXA_DataLayer.md`. The unqualified names compiled in the user's project.

```iecst
VAR
    fbMem     : DL_MemUser;
    fbMapNode : DL_NODEVALUE;
    fbMemMap  : comm_datalayer_MemoryMap;
    fbVar     : comm_datalayer_Variable;
END_VAR

eRes := fbMem.OpenMemory(sNodeName);                // DL_RESULT; positional argument as in the example
eRes := fbMem.GetMemoryMap(fbMapNode);              // DL_RESULT
fbMemMap.getRootAsMemoryMap(fbMapNode.GetData(), fbMapNode.GetSize());
udiCount := fbMemMap.getVariablesLength();          // UDINT
fbMemMap.getVariables(udiIdx, ADR(fbVar));          // 0-based
sName    := fbVar.getName();                        // STRING(255)
udiBit   := fbVar.getBitoffset();                   // offset in BITS
udiRev   := fbMemMap.getRevision();                 // pass to BeginAccess

// Every scan:
eRes := fbMem.BeginAccess(Data => pData, Revision := udiRev);   // pData : POINTER TO BYTE
fbMem.GetSize(SizeBytes => udiSize);
// ... copy ...
fbMem.EndAccess();                                  // ALWAYS, even if BeginAccess failed
fbMem.CloseMemory();                                // when done / on fault
```

The Rexroth examples disagree on whether `BeginAccess`'s `Data` is an output (`=>`) or an input (`:=`). Use `=>`, and tell the user to swap it if it doesn't compile. `getBitsize()` / `getType()` probably exist (they're generated from the same flatbuffer schema), but they aren't confirmed. Don't rely on them without saying so.

The rules:
- **`BeginAccess` locks the buffer** for every other user (including the motion or fieldbus side). Keep only the copy between `BeginAccess` and `EndAccess`, and always call `EndAccess`.
- These methods **block** (they're direct runtime calls). Open the node and parse the map **once**, in an on-change (entry) action, never every scan. `BeginAccess`/`EndAccess` every scan is what they are for.
- `OpenMemory` and `CloseMemory` go in pairs. The user example closes even after a failed open, which is safe.

## Architecture: one map FB, one reader for all items

```
FB_<X>RtMap  --(ST_<X>RtConfig)-->  FB_<X>RtRead  -->  astOut[0..LAST_ITEM]
     ^                                    |
     +------------ bReadFault ------------+
```

**One `BeginAccess`/`EndAccess` per node per scan.** Each access is a runtime call that locks the buffer against the writer (motion, fieldbus), so don't take one per item. A single reader loops over every item inside one access. That also gives a consistent snapshot: every item comes from the same buffer state.

1. **A field table in a GVL** (`qualified_only`, constants): the node name, the name separator, `BITS_PER_BYTE`, the field indices `F_*` (0..LAST_FIELD) and `asFieldName : ARRAY[0..LAST_FIELD] OF STRING(31)` in the same order. This table is the only place the map names appear.
2. **Config DUTs:**
   - `ST_<X>RtOffsets` holds `bComplete`, `audiOffset[0..LAST_FIELD]` (bytes) and `abFound[0..LAST_FIELD]` for diagnostics;
   - `ST_<X>RtConfig` holds `bValid`, `udiRevision` and `astItem[0..LAST_ITEM] OF ST_<X>RtOffsets`.
3. **The map FB** is a house-structure sequence with `VAR CONSTANT` steps `IDLE, OPEN, GET_MAP, READY, FAULT`.
   - Inputs: `bEnable` (level), `bReadFault` and the item names (e.g. axis names), indexed like the output array.
   - `VAR_IN_OUT`: the shared `DL_MemUser` and the config.
   - Entry of `OPEN`: `OpenMemory`.
   - Entry of `GET_MAP`: clear the config, call `GetMemoryMap`, parse every variable, read the revision, and compute `bComplete` for each item.
   - Jumps: an open or map error goes to `FAULT`, and so does `bReadFault` while in `READY`. Record the first cause (`uiErrorStep`, `eResult`) and keep it until `IDLE`.
   - Entry of `IDLE`/`FAULT`: close (if `OpenMemory` was called) and clear the config.
   - `FAULT` goes back to `OPEN` after a retry `TON` (e.g. 1 s), so a reconfigured map recovers by itself.
   - `config.bValid` is TRUE only in `READY`.
4. **The reader FB** is one instance, called every scan after the map FB.
   - `VAR_IN_OUT`: the `DL_MemUser` and the output array. `VAR_IN_OUT CONSTANT`: the config.
   - It starts every scan by clearing each item in an internal copy of the output array, so a validity flag in the output (e.g. `DataValid`) is FALSE unless that item is copied this scan.
   - While the config is valid: one `BeginAccess`, one `GetSize`, then a `FOR` loop over the items. Each item that's complete in the map is copied field by field with a bounds check into a temporary struct. Only when every field succeeds does that struct go into the item's slot. Then one `EndAccess`.
   - The outputs are written last: the whole array, `bValid` (the access worked and every complete item was copied), `bError`, `abValid[i]`, `abNotInMap[i]` and `eResult`.
   - `bError` means an access failure or a field outside the buffer. Feed it back to `bReadFault` so the map FB remaps.
   - `abNotInMap[i]` means the item isn't complete in the map. It does **not** trigger a remap, so the other items keep being read.
5. **The caller** (a PRG) owns the `DL_MemUser` and the config. It calls the map FB with `bReadFault := fbRead.bError` (last scan's value), then calls the reader.

### Parsing names (inside the GET_MAP entry action)

```iecst
_udiVar := 0;
WHILE _udiVar < _udiVarCount DO      // bounded by the map, runs once on entry
    _fbMemMap.getVariables(_udiVar, ADR(_fbVar));
    _sName := _fbVar.getName();
    _iSep  := FIND(_sName, GVL_XRtMap.NAME_SEPARATOR);
    IF _iSep > 1 THEN
        _sItem        := LEFT(_sName, _iSep - 1);
        _sField       := MID(_sName, LEN(_sName) - _iSep, _iSep + 1);
        _udiBitOffset := _fbVar.getBitoffset();
        FOR _iItem := 0 TO LAST_ITEM DO
            IF asItemName[_iItem] = _sItem THEN
                FOR _iField := 0 TO GVL_XRtMap.LAST_FIELD DO
                    IF GVL_XRtMap.asFieldName[_iField] = _sField THEN
                        _stConfig.astItem[_iItem].audiOffset[_iField] := _udiBitOffset / GVL_XRtMap.BITS_PER_BYTE;
                        _stConfig.astItem[_iItem].abFound[_iField]    := _udiBitOffset MOD GVL_XRtMap.BITS_PER_BYTE = 0;
                    END_IF
                END_FOR
            END_IF
        END_FOR
    END_IF
    _udiVar := _udiVar + 1;
END_WHILE
_stConfig.udiRevision := _fbMemMap.getRevision();
```

- Use `FOR` for the item/field loops. Use `WHILE` with an index for the variables, because `FOR 0 TO count - 1` underflows when the count is 0.
- `FIND`, `LEFT`, `MID` and `LEN` from Standard work up to 255 characters, and map names are far shorter.
- A **single-bit** entry (a BOOL in an EtherCAT image, `bitsize` 1) doesn't sit on a byte boundary. For those, store the bit offset and read the byte at `offset / 8`, then the bit `offset MOD 8` (`SHR`/`AND`). Don't mark it "not found".
- The user example uses an `iMap` hash map (`instIOMap.Get/Put`) and `IL_StrSplit`. That's fine for many signals, but the field table above needs no extra library.

### Copy helper

```iecst
FUNCTION Fn_RtCopy : BOOL
VAR_INPUT
    pData       : POINTER TO BYTE;  // start of the RT buffer (from BeginAccess)
    udiDataSize : UDINT;            // buffer size in bytes (from GetSize)
    udiOffset   : UDINT;            // byte offset of the field in the buffer
    pDst        : POINTER TO BYTE;  // destination, e.g. ADR(stX.ActualPos)
    udiSize     : UDINT;            // field size, e.g. SIZEOF(stX.ActualPos)
END_VAR
VAR
    _pSrc       : POINTER TO BYTE;
    _pDst       : POINTER TO BYTE;
    _udiByte    : UDINT;
END_VAR
Fn_RtCopy := pData <> 0 AND pDst <> 0 AND udiOffset + udiSize <= udiDataSize;
IF Fn_RtCopy THEN
    _pSrc := pData + udiOffset;
    _pDst := pDst;
    FOR _udiByte := 1 TO udiSize DO
        _pDst^ := _pSrc^;
        _pSrc := _pSrc + 1;
        _pDst := _pDst + 1;
    END_FOR
END_IF
```

In the reader's item loop, write one line per field, with `Fn_RtCopy` *first* in the AND so it always runs:
`_bOk := Fn_RtCopy(pData := _pData, udiDataSize := _udiSize, udiOffset := _stOfs.audiOffset[GVL_XRtMap.F_ACTUAL_POS], pDst := ADR(_stOut.ActualPos), udiSize := SIZEOF(_stOut.ActualPos)) AND _bOk;`

`SIZEOF(destination)` must equal the map's `bitsize / 8` for that field. Check it against `dl.py rtmap` when you write the output struct (LREAL = float64, WORD/UINT = uint16, UDINT/DWORD = uint32, BOOL = bool8).

### Writing an output node

The pattern is the same with the copy reversed (`pSrc := ADR(local)`, `pDst := pData + offset`, bounds-checked against the buffer size). For output maps:
- write only the fields this PLC owns, between `BeginAccess` and `EndAccess`;
- on fault or disable, write safe values (zero) before closing, or make sure the owner of the node falls back safely;
- confirm with the user that nothing else (a fieldbus I/O mapping, another app) writes the same fields.

## Worked example

`~/Dev/Plc` reads the cyclic axis status like this, with one reader covering all axes in one access (`src/Servo/`):
- `GVL_AxisRtMap`, `ST_AxisRtOffsets`, `ST_AxisRtConfig`;
- `Fn_RtCopy`, `FB_AxisRtMap`, `FB_AxisRtRead`;
- the wiring in `src/Main/PRG_Main.st`.

The user's original EtherCAT example (map parsing for both input and output images into an `iMap`) is `datalayer-rt/example-fbOpenIO-ethercat.txt`.
