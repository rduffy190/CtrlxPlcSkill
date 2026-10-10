---
name: codesys-st
description: Write PLC code in IEC 61131-3 Structured Text for Bosch Rexroth ctrlX CORE (ctrlX PLC Engineering) and other CODESYS V3-based controllers. Produces paste-ready POUs (programs, function blocks, functions), DUTs and GVLs, and can also produce importable PLCopenXML files (ladder diagram is the codesys-lad skill, which uses this skill's converter). Use this skill whenever the user wants PLC logic written or extended, even if they don't say "Structured Text", "ctrlX" or "CODESYS". That includes sequences, state machines, servo axes and ctrlX MOTION (MC_/ML_ commands, homing, positioning, gearing, cams, kinematics), motor/valve/pump control, conveyors, alarms, interlocks, PID loops, analog scaling, timers/counters, Modbus/IO mapping, reading or writing ctrlX Data Layer real-time (RT) nodes and memory maps (DL_MemUser, cyclic axis status, EtherCAT process image by name), or "write a function block that…". Also use it when someone describes a machine and asks how to program it.
---

# CODESYS Structured Text

Write Structured Text that a controls engineer can paste into CODESYS (or import) and trust. That means code that compiles, behaves correctly within the scan cycle, and is easy to commission and debug at 2 a.m. on a plant floor.

## Before writing code

PLC code controls physical equipment, and wrong assumptions turn into stuck machines or damaged parts. Before writing anything non-trivial, make sure you know:

- **I/O**: what the inputs and outputs are, their types (digital/analog, scaling ranges), and whether any are normally-closed (fail-safe wiring means `xStopOk` is TRUE when healthy).
- **Sequence / behaviour**: the normal flow, plus what happens on stop, fault, power-up, and reset.
- **Target**: the default is ctrlX CORE with ctrlX PLC Engineering. For ctrlX specifics such as the Data Layer, libraries and I/O, see `references/platforms.md`.

If the request is clear enough, make reasonable assumptions and list them at the top of your answer instead of interrogating the user. Ask only when a wrong guess would change the design, such as whether a fault latches until reset or clears on its own.

## Safety boundary

Standard PLC code is not a safety function. Emergency stops, guard interlocks, light curtains and the like belong in hardwired safety circuits or a safety PLC (SIL/PL rated). When a request involves these, still write the standard-PLC side (monitoring the safety relay's status, stopping the sequence, raising alarms), and add one short note saying the actual safety function has to live in the safety system. Don't lecture beyond that.

## Design rules (why they matter)

The PLC runs your code top to bottom every scan, usually every 1–20 ms, forever. Most PLC bugs come from forgetting that.

- **Never block.** No `WHILE` waiting on an input and no long loops. A stuck loop trips the watchdog and stops the whole controller. Wait across scans with state and timers instead.
- **Never read a POU's own outputs.** Keep every value the logic uses (state, fault code, latched bits) in internal `_` variables, and copy them to the `VAR_OUTPUT`s at the very end, **after** the sub-FB calls. Outputs can be written by the caller, so reading them back makes the logic depend on data it doesn't own.
- **Never put global data in an FB.** A function block (or function) never reads or writes a global variable (`GVL_x.var`) and never declares one. Everything it works on comes in through `VAR_INPUT`, `VAR_IN_OUT` or `VAR_IN_OUT CONSTANT`, and goes out through `VAR_OUTPUT` / `VAR_IN_OUT`. Only the program (`PRG_`) that calls the FB connects it to the GVLs. This applies to "convenient" reads too, such as a broadcast machine state or an I/O word. A hidden global dependency can't be seen at the call site. It makes the FB impossible to reuse or to test with other data, and a second instance silently shares the same data. **Global *constants*** (`VAR_GLOBAL CONSTANT`: array bounds, index constants, field tables) are not data and may be used.
- **Call every sub-FB instance every scan, unconditionally, after the logic and before the outputs.** Timers and your own FBs only update when called, so calling `_fbTimer` inside an `IF` or `CASE` freezes it when the condition goes false, which is a classic bug. Drive its inputs from the state (`IN := _eState = E_X.Filling`) and call it once, after the logic.
- **Outputs are written last, after every sub-FB call.** The order at the end of every POU is: sub-FB calls, then all output writes (command values and copies of internal values). Any output that passes on a sub-FB result (a timer's `Q`, a child's `Done`/`Error`/status) then carries this scan's value, not last scan's, and there's exactly one place to look for what a POU drives.
- **Write every sequence in the house structure. This one isn't optional.** The sections run in this order:
  1. **jumps**: fault, timeout and abort go to `Faulted`/`Aborting`;
  2. **transitions**: a `CASE` containing only state changes;
  3. **on change**: `IF eState <> _eLastState`, holding the common actions and then the per-state entry actions;
  4. **cyclic**: all sub-FB calls (inputs driven from the state), then all outputs last (command values as boolean expressions of the state, and copies of internal values).

  `references/patterns.md` §1 has the full template and the reasons for it. Read it before writing any sequence. For a sequence in ladder, use the codesys-lad skill.
- **One writer per output.** Assign each physical output in exactly one place, in the output section at the end of the POU, after the sub-FB calls. If several places write it, the last one wins silently.
- **No rising edges in sequences.** Commands are levels, and the state is the edge detector. A terminal state (`Done`, `Faulted`) holds until the command is removed, like PLCopen Execute/Done. One-shot actions go in the on-change section. An edge is lost if it arrives in the wrong step and can't be seen online. `R_TRIG` is only acceptable outside sequences, e.g. a simple counter on a sensor pulse.
- **Fail safe.** Outputs should be de-energised by default and on fault. Treat broken-wire analog values (out of range) as faults. Clamp setpoints.
- **Watch REAL comparisons.** Don't use `=` on REAL. Compare with a tolerance or use `>=` / `<=`.
- **Make it debuggable.** Expose status (current state, active alarm bits, step timer) as outputs or readable vars, because people commission with the online view. Keep FB interfaces small and meaningful.
- **Avoid unnecessary cleverness.** Pointers, `__NEW` and heavy OOP make online debugging harder. Use `REFERENCE TO`, methods, properties and interfaces when they genuinely simplify things (e.g. a family of similar devices), not by default.

## Naming and style

Follow `references/conventions.md`. Read it before writing code, because it holds the user's house style and overrides any habits you have.

Var blocks are always declared in this order: `VAR_INPUT`, `VAR_OUTPUT`, `VAR_IN_OUT`, `VAR`, `VAR CONSTANT`.

## Output format

The CODESYS editor splits each POU into a **declaration** part (top pane) and an **implementation** part (bottom pane), so present each object that way, in separate code blocks the user can paste straight in:

````
### FB_Pump  (Function Block)

**Declaration**
```iecst
FUNCTION_BLOCK FB_Pump
VAR_INPUT
    ...
END_VAR
```

**Implementation**
```iecst
...
```
````

- Order objects so that dependencies come first: DUTs (enums, structs), then GVLs, then functions and FBs, and finally the `PROGRAM` that uses them.
- Don't put `END_FUNCTION_BLOCK` / `END_PROGRAM` in what the user pastes, because the CODESYS editor doesn't use them. (They are needed for the XML script input; see below.)
- DUTs paste whole (`TYPE ... END_TYPE`) into a DUT object. A GVL pastes as its `VAR_GLOBAL ... END_VAR` block.
- After the code, add a short **Notes** section covering assumptions, what to wire or map, the libraries needed, and anything to verify during commissioning. Keep it brief.
- Comment the *why* in the code, not the obvious. Use a `//` comment on each interface variable, because CODESYS shows it as a tooltip.

## PLCopenXML (when asked for an importable file)

If the user wants a file to import (Project → Import PLCopenXML…), or the answer has many objects and pasting would be tedious, generate one with the bundled script instead of hand-writing XML. Hand-written PLCopenXML is verbose and easy to get subtly wrong.

1. Write each object as full ST source in `.st` files, *with* the `END_...` keywords. For example, use `FUNCTION_BLOCK FB_X ... END_FUNCTION_BLOCK`, `TYPE ... END_TYPE`, or a GVL as `VAR_GLOBAL ... END_VAR` in a file whose name is the GVL's name (e.g. `GVL_IO.st`). One file can hold several objects.
2. Run:
   ```bash
   python3 <skill-dir>/scripts/st_to_plcopenxml.py file1.st file2.st -o Project.xml
   ```
3. Optionally check the file against the PLCopen schema: `python3 <skill-dir>/scripts/validate_plcopen.py Project.xml` (needs lxml; downloads the schema once).
4. Read the script's warnings, because some constructs (methods, properties, attributes on DUTs) aren't converted and must be added by hand. Tell the user about anything that was skipped.

Read `references/plcopenxml.md` if you need to understand or extend the format.

## Ladder (LD)

Ladder is the **codesys-lad** skill, installed next to this one. It holds the ladder text language, its compiler and its examples. Its POUs build with this skill's `st_to_plcopenxml.py`, which loads the compiler from `codesys-lad/scripts/` whenever a POU body starts with `NETWORK`, so ST and LD objects can go in one import file.

## ctrlX library lookups

`references/libs/` contains Rexroth's *PLC Libraries* reference book, split into one file per library: Standard, Util, CXA_DataLayer, CXA_EthercatMaster, CXA_ModbusTCP/RTU, CXA_PLCopen (MC_* motion), CXA_MotionInterface, CXA_FileAsync, CXA_SocketComm, CXA_Utilities and more. Some files are hundreds of KB, so never read one whole. Instead:

1. Search `references/libs/INDEX.md` for the FB, type or function name, or for the topic if you don't know the name yet. It says which file has it.
2. Grep that file for the heading (e.g. `grep -n "^### .*DL_ReadNode$" references/libs/10_CXA_DataLayer.md`) and read just that section. The interface table and example program are usually within 60–120 lines.
3. Use the documented names, types and qualified call (e.g. `CXA_Datalayer.DL_ReadNode`) exactly. Mention which library the user has to add in the Library Manager.

Most CXA function blocks follow the PLCopen **Execute / Done / Busy-or-Active / Error / ErrorID / ErrorIdent** handshake (`IL_ExecuteDoneBase`):
- A rising edge on `Execute` starts the job, which runs over several scans. Keep calling the instance every scan.
- Hold the inputs constant while `Active`.
- When `Done` or `Error` goes TRUE, latch the result or error and drop `Execute`.
- Wrap these FBs in a state or step of your sequence rather than pulsing `Execute` blindly, and surface `ErrorID`/`ErrorIdent` for diagnostics.

## Motion (axes, kinematics)

For anything that moves an axis, including power, homing, positioning, jogging, gearing, cams and kinematics, read `references/motion-essentials.md` first. It explains:
- the three PLC interfaces (`MC_` PLCopen FBs, MotionInterface, `ML_` functions) and which to use;
- why `ML_` functions must be called **once** per command and then tracked by CmdID, never called every scan like an FB;
- buffered vs unbuffered commands, the axis state machine, and how errors are handled.

For MC_ FBs, `references/examples/FB_AxisCtrl.st` is a ready axis wrapper. The "PLCopen MC_ FBs in practice" section explains it: re-edging Execute between consecutive moves, gating Done, error latching, reset and halt.

To create or check the axes themselves on a controller (names, units, limits, virtual vs real, saving), use the ctrlx-rest skill: `scripts/motion_axes.py` and `references/motion-config.md`.

The full Motion App manual (chapters 4–7) is in `references/motion/`. Look up commands and their `ML_` PLC functions in `references/motion/INDEX.md`, then read just that command's section. Each section covers what the command does, its "PLC:" interface structs, and the Data Layer and Python equivalents.

## Data Layer RT memory maps (reading I/O and status by name)

When the user wants values from a ctrlX real-time Data Layer node instead of I/O mapping, read `references/datalayer-rt.md` first. Examples are the cyclic axis status (`motion/realtime/cyclicStatusData`), the EtherCAT process image (`.../realtime_data/input|output`), or any node with a `/map`. It gives:
- the verified `DL_MemUser` / `comm_datalayer_MemoryMap` calls;
- the house architecture: one map FB builds a config struct of offsets, and one reader FB reads every item in a single `BeginAccess`/`EndAccess` into the output array, at the same indices;
- the name parsing, the packed-buffer copy helper and the retry/remap handling.

Inspect the real map with the `ctrlx-rest` skill (`dl.py rtmap <node>`) before writing the field table.

## Regression tests

`tests/run.sh` covers:
- `st_to_plcopenxml.py` on `tests/fixtures/`: enums, structs, every GVL kind, FB/FUNCTION/PROGRAM and all var blocks. The output is checked structurally by `tests/check_st.py`, against the PLCopen schema, and for its expected warnings.
- The shipped example `references/examples/FB_AxisCtrl.st`.
- `pdf_to_libref.py`, which must regenerate `references/libs` and `references/motion` byte-identical from `docs/*.pdf`.

Run it after changing any script here, and add a fixture plus an assertion for every new construct the converter learns. Ladder is tested separately by `../codesys-lad/tests/run.sh`.

## Regenerating the references

`references/libs/` and `references/motion/` are generated from the PDFs in `docs/` by `scripts/pdf_to_libref.py`. If the user provides a newer edition, rerun it:
```bash
python3 <skill-dir>/scripts/pdf_to_libref.py <libraries-book.pdf> -o <skill-dir>/references/libs
python3 <skill-dir>/scripts/pdf_to_libref.py <motion-app-manual.pdf> -o <skill-dir>/references/motion \
    --chapters 4-7 --split-level 2 --title "ctrlX Motion App"
```

## Common building blocks

For patterns that come up often (motor starter with feedback fault, valve with position monitoring, analog scaling with range fault, alarm latching, sequence skeleton), see `references/patterns.md`. Adapt the patterns rather than pasting them blindly, because they illustrate structure and aren't a fixed library.
