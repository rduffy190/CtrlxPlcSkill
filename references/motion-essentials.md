# ctrlX MOTION from the PLC: essentials

These notes are condensed from the *Motion App* application manual (R911430551). The full text, split by section, is in `references/motion/`, with `references/motion/INDEX.md` listing every command and its `ML_` PLC function. Read the relevant command section before using any command, because the interfaces have many fields and the details matter.

## Three ways to command motion from the PLC

| Interface | Library | Style | Use when |
|---|---|---|---|
| **PLCopen FBs** (`MC_Power`, `MC_MoveAbsolute`, …) | `CXA_PLCopen` (docs: `libs/28_CXA_PLCopen.md`) | Function blocks with Execute/Done/Busy/Error. Call every scan. | This is the default. Engineers know it, and the FB handles the handshake for you. |
| **MotionInterface** (`arAxisCtrl_gb[i]` / `arAxisStatus_gb[i]`) | `CXA_MotionInterface` + template (docs: `libs/19_CXA_MotionInterface.md`) | A ready-made program frame. You set control bits and setpoints per axis index, and it handles the rest. | Use this for many axes handled uniformly, or if the user started from the MotionInterface template. |
| **ML_ functions** (`ML_AxsPosAbs`, `ML_AxsPower`, …) | `CXA_Motion` (docs: `motion/07-*.md`, "PLC:" part of each command) | Plain **functions** that submit a command and return at once. | Use them for features that have no MC_ FB (FlexProfile, kinematics `Kin*`, signals, overrides, probes, gantry…) or when the user asks for them. |

Ask, or follow the existing project, before mixing styles on the same axis. Every interface ends up in the same per-axis command buffer, so two parts of the program commanding one axis will abort each other's commands.

## ML_ functions behave differently from FBs (important)

An `ML_` call is a **one-shot submission**. It is not an FB you call cyclically.

- `ML_AxsPosAbs(Data := stPosAbs)` returns `TRUE` if the command was **accepted** into the axis's command buffer, and `FALSE` (with details in `Data.Out`) if it was rejected, for example because of bad parameters or a violated dynamic limit.
- The call does **not** mean the move finished. `Data.Out.CmdID` identifies the command. To track it, poll `ML_GetCmdState` with `In.ObjName` and `In.CmdID` until `Out.State` is `'DONE'` or `'ABORTED'`.
- **Never call a motion `ML_` function every scan.** Each call queues a new command (buffered) or aborts and replaces the current one (unbuffered). Call it once on the transition into a sequence step, store the CmdID, then wait in the next step.
- Data layout: `stXxx.In.*` holds the parameters (`AxisName`, `Position`, `Buffered`, `DynLimits.{Velocity, Acceleration, Deceleration, JerkAcc, JerkDec}`, …). `stXxx.Out` is an `ML_oCmdResult` with `CmdID`, `Error` and `ErrorID`. In `ErrorID` (UDINT), the upper half is the main diagnosis and the lower half the detail.
- `Source` and `SourceLine` in `In` are free text and a number that show up in the diagnostic log. Fill them in (e.g. `'PRG_Station1'`) so errors can be traced.

### Skeleton (house sequence structure, see `patterns.md` §1; check field names against the command's section)

The `ML_` submission is a one-shot action, so it belongs in the **on-change** section (entry of the move step). The status query runs in the **cyclic** section, and the transitions read its result.

```iecst
VAR
    _eState         : E_MoveState;          // enum: Idle, Moving, Done, Faulted
    _eLastState     : E_MoveState;
    _bAccepted      : BOOL;                 // last ML_ submission was accepted
    _stPosAbs       : ML_AxsPosAbsData;     // CXA_Motion
    _stCmdState     : ML_GetCmdStateData;
END_VAR
VAR CONSTANT
    AXIS_NAME       : STRING := 'Axis_X';
    SOURCE_NAME     : STRING := 'PRG_Station1';
    CMD_DONE        : STRING := 'DONE';
    CMD_ABORTED     : STRING := 'ABORTED';
END_VAR

// ===== 1. Jumps =====
IF _eState = E_MoveState.Moving AND (NOT _bAccepted OR _stCmdState.Out.Error
                                    OR _stCmdState.Out.State = CMD_ABORTED) THEN
    _eState := E_MoveState.Faulted;          // _stPosAbs.Out.ErrorID / _stCmdState.Out.ErrorID hold the reason
END_IF

// ===== 2. Transitions =====
CASE _eState OF
    E_MoveState.Idle:    IF bExecute THEN _eState := E_MoveState.Moving; END_IF
    E_MoveState.Moving:  IF _stCmdState.Out.State = CMD_DONE THEN _eState := E_MoveState.Done; END_IF
    E_MoveState.Done:    IF NOT bExecute THEN _eState := E_MoveState.Idle; END_IF
    E_MoveState.Faulted: IF bReset AND NOT bExecute THEN _eState := E_MoveState.Idle; END_IF
ELSE
    _eState := E_MoveState.Faulted;
END_CASE

// ===== 3. On change =====
IF _eState <> _eLastState THEN
    CASE _eState OF
        E_MoveState.Moving:
            // Submit exactly once, on entry
            _stPosAbs.In.AxisName := AXIS_NAME;
            _stPosAbs.In.Source   := SOURCE_NAME;
            _stPosAbs.In.Position := lrTargetPos;
            _stPosAbs.In.Buffered := TRUE;
            _stPosAbs.In.DynLimits.Velocity     := lrVel;
            _stPosAbs.In.DynLimits.Acceleration := lrAcc;
            _stPosAbs.In.DynLimits.Deceleration := lrAcc;
            // JerkAcc = JerkDec = 0 -> no jerk limit (trapezoid profile)
            _stCmdState.Out.State := '';                    // forget the previous command's result
            _stCmdState.Out.Error := FALSE;
            _bAccepted := ML_AxsPosAbs(Data := _stPosAbs);
    END_CASE
    _eLastState := _eState;
END_IF

// ===== 4. Cyclic =====
bBusy  := _eState = E_MoveState.Moving;
bDone  := _eState = E_MoveState.Done;
bError := _eState = E_MoveState.Faulted;

// Status query: safe to call every scan (unlike the command itself)
_stCmdState.In.ObjName := AXIS_NAME;
_stCmdState.In.CmdID   := _stPosAbs.Out.CmdID;
IF _eState = E_MoveState.Moving THEN
    ML_GetCmdState(Data := _stCmdState);
END_IF
```

The poll is gated on the state because `ML_GetCmdState` is a function, not an FB: it has no internal state to freeze, and skipping it outside `Moving` just avoids pointless calls.

## PLCopen MC_ FBs in practice (CXA_PLCopen)

`examples/FB_AxisCtrl.st` is a ready axis wrapper (a ladder version, scan-tested, is in the codesys-lad skill's `references/examples/FB_AxisCtrl.st`): power, absolute move, halt, reset and status, with a latched first error and its ctrlX diagnosis. Copy it instead of re-deriving these points:

- **Axis reference**: `stLift : AXIS_REF := (AxisName := 'BeamLift');` in a GVL (type from CXA_CommonTypes, `AxisName : STRING(15)`). It is passed as `Axis := stLift` (a VAR_IN_OUT), so an FB that wraps axes takes `stAxis : AXIS_REF` in `VAR_IN_OUT`. Create or check the axes on the controller with the ctrlx-rest skill (`motion_axes.py`).
- **Units**: MC_ positions and dynamics are in the axis' **configured default units** (`motion/axs/<ax>/cfg/units`). A new axis defaults to mm, mm/min, m/s² and m/s³, so check them before choosing setpoint units.
- **Back-to-back moves on one MC_MoveAbsolute need a fresh edge.** When two sequence steps both move the same axis (e.g. Approaching → Pressing), `Execute` driven from "state is a move state" never falls, so the second move is never issued. Hold Execute low on the state-change scan: `bMove := NOT _bStateChanged AND (<move states>)`, with `_bStateChanged := _eState <> _eLastState` computed in the on-change section.
- **Gate Done with the command** (`bInPos := _fbMove.Done AND bMove`), so a Done from the previous step can't satisfy the next step's transition on its first scan.
- **Power/ReadStatus errors need a new Enable edge.** If motion isn't RUNNING yet (boot, SETUP), `MC_Power`/`MC_ReadStatus` latch Error until Enable re-edges. Drop Enable for one scan on reset: `Enable := bPower AND NOT (_fbPower.Error AND bReset)`. Enable the readers only while powered, so an unpowered system doesn't fault at boot.
- **Execute errors clear when Execute drops.** Latch the first `ErrorID`/`ErrorIdent.Additional1/2` in the wrapper, or the info is gone once the sequence drops Execute on entering Faulted. Also latch `MC_ReadStatus.ErrorStop` as a fault (drive error during motion; details in the ctrlX diagnostics log).
- **MC_Reset**: `Execute := bReset AND _fbStatus.ErrorStop`. Clear the latched error only when `bReset AND NOT ErrorStop AND NOT _fbReset.Active`.
- **MC_Halt**: don't execute it on an unpowered axis or one in ErrorStop (it errors, and the drive has already stopped). Gate it with `_fbPower.Status AND NOT _fbStatus.ErrorStop`. The manual's interface table names its axis pin `Axes` (InOut Const) while the value table says `Axis`. `Axis` is assumed, so check it at the first compile.
- **BufferMode**: `MC_BUFFER_MODE.mcAborting` (default, single axis) or `mcBuffered`. Blending isn't supported on single axes.
- **Power-off with a vertical axis**: in a sequence, exit Faulted on reset straight to the power-on step when still enabled, rather than through a Disabled step. Otherwise power drops for a scan.

## Command buffering

- **Buffered** commands go into a FIFO per axis or kinematics and run one after another. The limits are 30 commands for axes and 100 for kinematics, configurable at `motion/kin/<name>/cfg/prep-limits/max-cmds-in-buffer`. Preparation runs in a low-priority task, so prefer buffered commands where possible.
- **Unbuffered** commands abort the active command and discard the buffer, so everything there goes to state `ABORTED`. They're prepared in real-time context and are expensive. A burst of them can trip the motion watchdog. Use them only when an external event invalidates the current move, such as new vision coordinates.
- Kinematic commands are always buffered.
- Interrupt, continue and override changes (`AxsInterrupt`/`AxsContinue`, `SetOverride`) act immediately **without** discarding the buffer.
- The command states are `CREATED → INBUFFER → PREPARED → ACTIVE → DONE`, plus `ABORTED` and `OUTDATED` (no info any more). See 7.8.7 `GetCmdState`.

## State machines

- **Motion system** (global): `BOOTING → RUNNING`, with `CONFIGURATION` and `ERROR` as the other states. Commands are only accepted in `RUNNING`, which corresponds to ctrlX OS state "OPERATION". In SETUP or SERVICE, motion switches to CONFIGURATION. Make the PLC check this, and don't treat it as an axis fault.
- **Axis / kinematics**: the PLCopen state machine (`DISABLED`, `STANDSTILL`, `DISCRETE_MOTION`, `CONTINUOUS_MOTION`, `SYNCHRONIZED_MOTION`, `HOMING`, `STOPPING`, `ERRORSTOP`, …). If the motion kernel isn't RUNNING, the state reads `OUTDATED`. Read it with `ML_AxsGetPLCOpenState` / `ML_KinGetPLCOpenState`, or with `MC_ReadStatus` when using CXA_PLCopen.
- Typical start sequence: wait for motion RUNNING, then power (`ML_AxsPower` with `SwitchOn := TRUE`, or `MC_Power`), then wait for `STANDSTILL`, then home or set the absolute position if needed, and only then move.
- Motion commands need `STANDSTILL` (powered, no error). An error during execution puts the axis into `ERRORSTOP`, and leaving it needs a reset (`AxsReset` / `MC_Reset`) **after** the cause is gone.

## Errors

- **F0**: diagnostic only, no reaction.
- **F2**: the affected axis or kinematics is stopped. It has three classes: LIGHT (the axis can still follow and stops gently), SEVERE (it no longer follows) and CRITICAL.
- **F6/F8**: system error, giving a SEVERE reaction on **all** axes and kinematics. These usually come from another app.
- Error reactions are local and as gentle as possible. Design PLC logic to detect `ERRORSTOP`, stop the sequence, show the `ErrorID` (main and detail diagnosis) and require an operator reset.
- See `motion/06-04_Troubleshooting.md`, including "drive does not follow the command values".

## Other useful facts

- **Dynamic limits**: the effective limits are the smaller of the commanded and configured values. ctrlX also caps acceleration and jerk so that the max velocity and acceleration are reachable within one motion cycle. Velocity, acceleration and deceleration must be > 0, and jerk = 0 on both means no jerk limit.
- **Modulo axes**: `PosAbs` takes the shortest way. `PosAbsEx` takes a direction (`SHORTEST_WAY`, `POSITIVE_DIR`, `NEGATIVE_DIR`, `CURRENT_DIR`).
- **Units** are configured per axis and kinematics (Data Layer `.../cfg/units`). Changing the axis type between linear and rotary resets units and limits. See 4.1.9.
- **Data Layer**: axis nodes live under `motion/axs/<name>/...` (state, cfg, cmd-state) and kinematics under `motion/kin/<name>/...`. These are readable from the PLC with CXA_Datalayer, but use the ML_/MC_ calls for commanding, because Data Layer and REST commanding isn't real-time.
- **Motion-synchronous PLC task** (4.1.11): to run PLC logic between actual-value processing and command generation, you need three things: a `plc-external-event` callable in the `ctrlXAutomation` scheduler task, the PLC task on the same CPU core, and the PLC task at higher priority (a lower number). Only suggest this for tight synchronisation needs.
