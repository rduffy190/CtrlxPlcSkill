# PLCopenXML notes (CODESYS flavour)

These notes cover the format produced by `scripts/st_to_plcopenxml.py`. You only need them when extending the script or debugging an import.

- The root is `<project xmlns="http://www.plcopen.org/xml/tc6_0200">` and contains, in this order: `fileHeader`, `contentHeader`, `types` (`dataTypes`, `pous`), `instances`, then an optional `addData`.
- Each POU is `<pou name pouType="program|functionBlock|function">` with an `<interface>` and a `<body><ST><xhtml xmlns="http://www.w3.org/1999/xhtml">code</xhtml></ST></body>`.
- In the interface, `returnType` (functions only) comes first, followed by the var blocks: `inputVars`, `outputVars`, `inOutVars`, `localVars`, `tempVars`, `externalVars`. Attributes are `constant`, `retain` and `persistent`.
- Inside a variable the order is `<type>`, `<initialValue><simpleValue value=".."/>`, then `<documentation>`.
- Types:
  - Elementary types are `<BOOL/>`, `<INT/>` and so on.
  - Strings are `<string length="n"/>`.
  - Arrays are `<array><dimension lower upper/>…<baseType>`.
  - Pointers are `<pointer><baseType>`.
  - Everything else, including FB types, is `<derived name="X"/>`.
- CODESYS addData:
  - `http://www.3s-software.com/plcopenxml/interfaceasplaintext` holds the declaration text, including comments, pragmas and attributes. The script adds it to every POU, DUT and GVL, so anything the structured XML can't express (attributes, mixed `VAR_GLOBAL` / `VAR_GLOBAL CONSTANT` blocks, `ARRAY[*]`, structured initial values) survives there.
  - A GVL file becomes **one** `globalVars`, even if it has several `VAR_GLOBAL` blocks.
  - `ARRAY[*]` has no numeric bounds in PLCopen, so it's written as `<derived name="ARRAY[*] OF T"/>`.
  - `http://www.3s-software.com/plcopenxml/globalvars` holds `<globalVars name="GVL_X">` (GVLs).
  - Methods, properties and actions use further `3s-software` addData entries. The script doesn't generate those, so add such objects by hand after import.
- LD bodies (`<body><LD>`) come from the codesys-lad skill's `scripts/ladder.py`. Its module docstring and that skill's `references/ladder.md` give the mapping, which was taken from real LD exports from CODESYS V3.5 SP15 and ctrlX PLC Engineering 3.6.5. Both exports validate against the PLCopen TC6 v2.01 XSD once its namespace is swapped from `tc6_0200` to `tc6_0201`, and so does the script's output. `scripts/validate_plcopen.py` does that check. `ElementType` / `CallType` / `InputParamTypes` markers are written with `xmlns=""`, as CODESYS does.
- A POU's `InterfaceAsPlainText` goes where ctrlX PLC Engineering exports it: in the POU's own `addData` after `<body>`, and a copy in each var block's `addData`. (`interface/addData` holds only attributes.)
- On import, CODESYS shows a tree of objects to choose from. Existing objects with the same name prompt for replacement.
- ctrlX PLC Engineering is CODESYS-based, so the same import path (Project → Import PLCopenXML) should apply. This hasn't been verified on a real install yet.
