# Naming & style conventions

## Object prefixes

| Object | Prefix | Example |
|---|---|---|
| Program | `PRG_` | `PRG_Main` |
| Function block | `FB_` | `FB_Motor` |
| Function | `Fn_` | `F_ScaleAnalog` |
| Struct | `ST_` | `ST_MotorStatus` |
| Enum | `E_` | `E_PumpState` |
| Interface | `I_` | `I_Device` |
| Global variable list | `GVL_` | `GVL_IO` |

## Variable prefixes (by type)

| Type | Prefix | Example |
|---|---|---|
| BOOL | `b` | `bRunning` |
| BYTE / WORD / DWORD | `by` / `w` / `dw` | `wStatusWord` |
| SINT / INT / DINT | `si` / `i` / `di` | `iCount` |
| USINT / UINT / UDINT | `usi` / `ui` / `udi` | `uiRecipeNo` |
| REAL / LREAL | `r` / `lr` | `rPressure` |
| TIME | `t` | `tDelay` |
| STRING | `s` | `sMessage` |
| Enum | `e` | `eState` |
| Struct | `st` | `stStatus` |
| FB instance | `fb` | `fbStartDelay` |
| Array | `a` + element prefix | `arTemps` |
| Pointer / Reference | `p` / `ref` | `refMotor` |

## Scope prefixes

- Inputs and outputs of an FB need no extra prefix (the type prefix is enough).
- Physical I/O in a GVL is grouped by direction, e.g. `GVL_IO.bDI_StartPB` and `GVL_IO.bDO_PumpRun`.
- Constants are `UPPER_SNAKE_CASE` in a `VAR CONSTANT` / `VAR_GLOBAL CONSTANT` block.
- Local Vars have a `_` prefix, e.g `_uiState` for a local uint of state
- Never put global data in an FB or function. No `GVL_x.var` reads or writes inside it. Pass the value in as an input or `VAR_IN_OUT`, and wire it to the GVL in the calling `PRG_`. Global constants are allowed.
- Never read your own `VAR_OUTPUT`s. Work on the internal `_` variable and copy it out (`eState := _eState;`) at the very end, after the sub-FB calls.

## Style

- Indent with 4 spaces.
- Keywords are UPPERCASE.
- Enums use `{attribute 'qualified_only'}` and are always referenced as `E_State.Idle`.
- Comment each interface variable with a trailing `//` comment.
- Declare var blocks in this order, always: `VAR_INPUT`, `VAR_OUTPUT`, `VAR_IN_OUT`, `VAR`, `VAR CONSTANT`. Leave out the blocks a POU doesn't need, but never reorder them. Other blocks (`VAR_TEMP`, `VAR_STAT`) go after `VAR`, before `VAR CONSTANT`.
- Every POU begins with a short header comment that says its purpose, plus its author and date if the user wants them.
- Use constants, no magic numbers, in code. e.g. `PI` should be used instead of `3.14159`
- Use constants for states if the state is not output from the block, Enums if the state is output 

