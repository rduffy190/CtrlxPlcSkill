# Platform differences among CODESYS-based targets

The ST language is nearly identical across these targets. The main differences are libraries, I/O mapping and a few keywords.

## Plain CODESYS V3.5 (CtrlX, WAGO, Festo, Eaton, Raspberry Pi, Control Win, …)
- Libraries: `Standard` (TON, R_TRIG, CTU…), `Util` (hysteresis, PID, BLINK…), `CAA` libraries for files, network and similar tasks.
- I/O is mapped in the device tree's I/O Mapping tab, either to a GVL variable or as "create new variable". `AT %IX0.0` declarations also work but are discouraged.
- Methods and properties are added as child objects in the device tree, not pasted inline.

## Bosch Rexroth ctrlX CORE (default target)
- The engineering tool is **ctrlX PLC Engineering**, which is based on CODESYS V3.5, so standard CODESYS ST, `Standard` and `Util` all apply.
- The PLC runs as an app on ctrlX OS. The **ctrlX Data Layer** is the central data exchange between apps (motion, I/O, other apps, external clients). From the PLC it's accessed through Rexroth's Data Layer library, typically `CXA_Datalayer`. Expose values the HMI or other apps need through the Data Layer instead of inventing ad-hoc comms.
- EtherCAT I/O is configured in the engineering tool and mapped to variables like any CODESYS device.
- Rexroth ships `CXA_...` libraries for the Data Layer, motion, EtherCAT, Modbus, files, sockets and more. Their documentation is in `references/libs/` (see "ctrlX library lookups" in SKILL.md). Never guess an FB's name or interface; look it up.
- Data Layer node paths for PLC variables look like `plc/app/Application/sym/<GVL or POU>/<variable>`, e.g. `plc/app/Application/sym/Gvl/iecString`.
- From library version 1.2.6.0, Data Layer FBs run asynchronously. Keep `NodeName`, `ClientId` and the value buffers constant while the FB is busy, or it raises errors.
- OPC UA client/server libraries (`CXA_OpcUa...`) aren't documented in the reference book. Their docs are on the FB's Documentation tab in the Library Manager, so flag OPC UA calls for the user to verify.

## Things that differ / to check
- `LTIME`, `__NEW`, `__DELETE`, `REFERENCE TO` and `PROPERTY` need a reasonably recent CODESYS 3.5 service pack. ctrlX PLC Engineering is current, so they're fine there. If the user mentions an old install, avoid them.
- `{attribute 'qualified_only'}` and `{attribute 'strict'}` on enums are supported everywhere in V3.
- Implicit enum base type is INT. Specify it with `E_X : (...) UINT;` when it matters for comms.
- Use `TO_INT()`, `REAL_TO_INT()` and similar functions for explicit conversions, because the compiler warns about implicit narrowing.


## Reading a Data Layer RT memory map on the PLC

See `datalayer-rt.md`. It covers the API, the map FB plus single-access reader architecture, name parsing, the packed-buffer copy and output nodes.
