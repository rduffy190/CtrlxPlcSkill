# Common patterns

These are reference implementations that show structure and house style. Adapt the names, faults and features to the request, but keep the **sequence structure** in section 1, because it exists to avoid a whole class of easy bugs.

## Contents
1. Sequence structure (jumps → transitions → on change → cyclic)
2. Motor with run-feedback fault
3. Analog scaling
4. Latched alarm with reset

---

## 1. Sequence structure

Every sequence is written in the same four sections, in this order:

| # | Section | Contains | Must not contain |
|---|---|---|---|
| 1 | **Jumps** | Overriding transitions that apply in many states: fault, step timeout, abort request. They go to `Faulted` / `Aborting` and record the fault. | Outputs, normal step-to-step logic |
| 2 | **Transitions** | A `CASE` with **only** state changes: `IF <condition> THEN _eState := ...`. | Outputs, actions, FB calls |
| 3 | **On change** | `IF _eState <> _eLastState THEN`. Inside: first the actions common to *every* change (restart the step timer, clear the timeout), then a `CASE` of one-shot **entry actions** for the state just entered (set its timeout, latch a recipe value, issue an `ML_` command…). It ends with `_eLastState := _eState`. | State changes, cyclic outputs |
| 4 | **Cyclic** | First every sub-FB call, with its inputs (`IN`, `Execute` bits, setpoints) driven from the current state. Then, **last**, every output: command values as expressions of the state, and copies of internal values. | State changes, reading outputs, any output write before a sub-FB call |

Why the sections matter:
- **Jumps first and in one place.** "Fault from any state" is written once, so no step can forget to check it. Their priority (fault > timeout > abort) is explicit. The transitions then run as normal on the state the jump set. That's correct by construction, because exits from `Faulted`/`Aborting` are held conditions, so if one fires in the same scan it would have fired a scan later anyway. Don't add a "jumped" flag to skip them.
- **Transitions only in the CASE.** You can read the whole flow chart from one block. A state is never changed from inside an action.
- **On change after the transitions.** Entry actions run on the same scan as the transition, for the state the sequence actually ended up in. A state that's only passed through within one scan (a transition overridden by a jump) never runs its entry actions. One-shot work can't be repeated, because it's fenced off by `_eState <> _eLastState`.
- **Cyclic last.** Outputs are a function of the final state, so they never lag a scan behind a jump to `Faulted`. Writing each command as an expression of the state (`bClampCmd := _eState = Clamping OR _eState = Working`) gives each output exactly one writer. It also can't stay latched after the sequence leaves a step.
- **Never read your own outputs.** The state, fault code and any other value the logic depends on live in internal `_` variables, and the outputs are only copies written at the end of the cyclic section. A caller can write an FB's outputs from outside, so reading them back makes the logic depend on something it doesn't own.
- **Sub-FB calls come first in the cyclic section, every scan**, never inside a CASE or IF. A timer or Execute/Done FB that isn't called stops updating.
- **Outputs come after the sub-FB calls, at the very end of the POU.** An output that passes on a sub-FB result (a child's `Done`/`Error`, a status word) then shows this scan's value instead of lagging one scan, and every output write is in one block at the bottom. Nothing after the output block.
- **The `ELSE` branch.** An unknown state value (e.g. after an online change) goes to `Faulted` instead of hanging.
- **No first-scan logic.** Every state machine starts in `Idle`, and `Idle` does nothing. The variable defaults (state `Idle`, fault code 0, outputs FALSE) are already the correct `Idle` values, so nothing needs to run on the first scan.
- **Steps Should Be CONSTANTS** That way new steps can be added with any number with readability 

### No rising edges: the state is the edge detector

Commands are **levels**, and the sequence detects them with its states, not with `R_TRIG`. A terminal state (`Done`, `Faulted`, end of `Aborting`) **holds until the command is removed**:

```
Idle --bExecute--> ...steps... --> Done --NOT bExecute--> Idle
```

While `Done` holds, a held `bExecute` can't start a second cycle, because the sequence has to see `bExecute` go FALSE (back to `Idle`) and then TRUE again. The handshake is the same one as PLCopen and CXA FBs (Execute/Done), so callers drive this block exactly like an `MC_` FB, and blocks chain naturally.

Edges are avoided because an edge is a one-scan event. If it arrives while the sequence is in another step it's lost for good, and it can't be watched in the online view. A state can be seen, and it waits. The one-shot behaviour an edge would give you comes from the on-change section instead.

State type convention: use an **enum** when the state is an output of the block (as below). Use **`VAR CONSTANT` UINT steps** for internal sub-sequences whose state isn't exposed. The structure is identical either way (`CASE _uiStep OF STEP_CLAMP: ...`).

### Example: clamp → work → unclamp cycle

```iecst
{attribute 'qualified_only'}
{attribute 'strict'}
TYPE E_CycleState :
(
    Idle := 0,
    Clamping,
    Working,
    Unclamping,
    Done,
    Aborting,
    Faulted
) UINT;
END_TYPE
```

```iecst
// FB_Cycle: one clamp/work/unclamp cycle per Execute, with abort, step timeouts and latched faults.
FUNCTION_BLOCK FB_Cycle
VAR_INPUT
    bExecute        : BOOL;     // run one cycle; hold TRUE until Done/Error, then remove
    bAbort          : BOOL;     // abort request (level), e.g. guard opened
    bReset          : BOOL;     // fault reset (level), only acts once Execute is removed
    bExternalFault  : BOOL;     // fault cause from outside, e.g. drive fault
    bClamped        : BOOL;     // feedback: clamp closed
    bUnclamped      : BOOL;     // feedback: clamp open
    bWorkDone       : BOOL;     // feedback: work station finished
END_VAR
VAR_OUTPUT
    eState          : E_CycleState; // current step, for HMI / online view
    bBusy           : BOOL;         // cycle in progress
    bDone           : BOOL;         // cycle finished; held until Execute is removed
    bError          : BOOL;         // faulted; held until reset with Execute removed
    uiFaultCode     : UINT;         // first fault that latched, 0 = none
    eFaultState     : E_CycleState; // step that was active when the fault latched
    bClampCmd       : BOOL;         // valve: close clamp
    bWorkCmd        : BOOL;         // start work station
END_VAR
VAR
    _eState         : E_CycleState; // the state; eState is only a copy for the caller
    _uiFaultCode    : UINT;
    _eFaultState    : E_CycleState;
    _eLastState     : E_CycleState;
    _tStepTimeout   : TIME;         // timeout of the current step, T#0S = none
    _fbStepTimer    : TON;
END_VAR
VAR CONSTANT
    CLAMP_TIMEOUT       : TIME := T#3S;
    WORK_TIMEOUT        : TIME := T#30S;
    UNCLAMP_TIMEOUT     : TIME := T#3S;
    FAULT_NONE          : UINT := 0;
    FAULT_EXTERNAL      : UINT := 1;
    FAULT_STEP_TIMEOUT  : UINT := 2;
    FAULT_INVALID_STATE : UINT := 99;
END_VAR
```

```iecst
// ===== 1. Jumps: highest priority first =====
IF _eState <> E_CycleState.Faulted THEN
    IF bExternalFault THEN
        _uiFaultCode := FAULT_EXTERNAL;
        _eFaultState := _eState;
        _eState := E_CycleState.Faulted;
    ELSIF _fbStepTimer.Q THEN
        // The step timer belongs to the current step, so this one check covers every step's timeout
        _uiFaultCode := FAULT_STEP_TIMEOUT;
        _eFaultState := _eState;
        _eState := E_CycleState.Faulted;
    ELSIF bAbort AND (_eState = E_CycleState.Clamping OR _eState = E_CycleState.Working) THEN
        _eState := E_CycleState.Aborting;
    END_IF
END_IF

// ===== 2. Transitions only =====
CASE _eState OF
    E_CycleState.Idle:
        IF bExecute AND NOT bAbort THEN
            _eState := E_CycleState.Clamping;
        END_IF

    E_CycleState.Clamping:
        IF bClamped THEN
            _eState := E_CycleState.Working;
        END_IF

    E_CycleState.Working:
        IF bWorkDone THEN
            _eState := E_CycleState.Unclamping;
        END_IF

    E_CycleState.Unclamping:
        IF bUnclamped THEN
            _eState := E_CycleState.Done;
        END_IF

    E_CycleState.Done:
        // Hold until the command is removed: this is what replaces an edge on Execute
        IF NOT bExecute THEN
            _eState := E_CycleState.Idle;
        END_IF

    E_CycleState.Aborting:
        IF bUnclamped AND NOT bExecute THEN
            _eState := E_CycleState.Idle;
        END_IF

    E_CycleState.Faulted:
        IF bReset AND NOT bExecute AND NOT bExternalFault THEN
            _eState := E_CycleState.Idle;
        END_IF

ELSE
    _uiFaultCode := FAULT_INVALID_STATE;
    _eFaultState := _eState;
    _eState := E_CycleState.Faulted;
END_CASE

// ===== 3. On change: common actions, then entry actions of the new state =====
IF _eState <> _eLastState THEN
    // Every change: restart the step timer, no timeout unless the new step sets one
    _fbStepTimer(IN := FALSE);
    _tStepTimeout := T#0S;

    CASE _eState OF
        E_CycleState.Idle:
            // Idle means no fault: fault info only exists while the sequence is out of Idle
            _uiFaultCode := FAULT_NONE;
            _eFaultState := E_CycleState.Idle;

        E_CycleState.Clamping:
            _tStepTimeout := CLAMP_TIMEOUT;

        E_CycleState.Working:
            _tStepTimeout := WORK_TIMEOUT;
            // one-shot work goes here, e.g. latch the recipe or issue an ML_ motion command

        E_CycleState.Unclamping, E_CycleState.Aborting:
            _tStepTimeout := UNCLAMP_TIMEOUT;
    END_CASE

    _eLastState := _eState;
END_IF

// ===== 4. Cyclic: every sub-FB call, then every output last =====
_fbStepTimer(IN := _tStepTimeout > T#0S, PT := _tStepTimeout);

// Outputs: command values from the current state
bBusy     := _eState = E_CycleState.Clamping OR _eState = E_CycleState.Working
             OR _eState = E_CycleState.Unclamping OR _eState = E_CycleState.Aborting;
bDone     := _eState = E_CycleState.Done;
bError    := _eState = E_CycleState.Faulted;
bClampCmd := _eState = E_CycleState.Clamping OR _eState = E_CycleState.Working;   // Aborting opens it
bWorkCmd  := _eState = E_CycleState.Working;

// Copy internal values out; the logic above never reads its own outputs
eState      := _eState;
uiFaultCode := _uiFaultCode;
eFaultState := _eFaultState;
```

Notes:
- **A start/stop machine** (not a one-shot cycle) uses the same idea. For example, `Stopped` holds until `bStart` is released, so a start button held through a stop doesn't restart the machine.
- **Re-entering the same step** (e.g. retrying) isn't a change, so its entry actions don't run. Route through a separate retry step instead.
- **The first fault is kept, and `Idle` means no fault.** The jump section skips `Faulted`, so later faults don't overwrite `_uiFaultCode`/`_eFaultState`. Both are cleared on entry to `Idle`. A fault only exists while the command that led to it is still active: `Faulted` can't be left while `bExecute` is TRUE. Once the command is removed and the fault is reset, the sequence is back in `Idle` with nothing wrong, so there's no fault to show.
- **Calling Execute/Done FBs (CXA, `MC_`) from a sequence** is the same handshake from the other side. Set their `Execute` in the cyclic section from the state (`_fbMove.Execute := _eState = E_X.Moving`), call the FB there every scan, and use `Done` in the transition CASE and `Error` in the jumps. Leaving the step drops `Execute`, which re-arms the FB.

---

## 2. Motor with run-feedback fault

```iecst
// FB_Motor: contactor/VFD output with run-feedback supervision.
FUNCTION_BLOCK FB_Motor
VAR_INPUT
    bRunCmd     : BOOL;         // request to run
    bFeedback   : BOOL;         // contactor aux / VFD running
    bReset      : BOOL;         // fault reset (level)
    tFbTimeout  : TIME := T#2S; // max time for feedback to follow command
END_VAR
VAR_OUTPUT
    bRunOut     : BOOL;         // drive output
    bFault      : BOOL;         // latched feedback fault
END_VAR
VAR
    _bRunOut    : BOOL;
    _bFault     : BOOL;
    _fbFbTimer  : TON;
END_VAR
```

```iecst
// Feedback must follow the output within tFbTimeout, in both directions (timer called below, before the outputs)
IF _fbFbTimer.Q THEN
    _bFault := TRUE;
ELSIF bReset AND NOT bRunCmd THEN
    _bFault := FALSE;   // only reset while not commanded, so a reset never restarts the motor
END_IF

_bRunOut := bRunCmd AND NOT _bFault;

// Sub-FBs
_fbFbTimer(IN := (_bRunOut <> bFeedback), PT := tFbTimeout);

// Outputs, last
bRunOut := _bRunOut;
bFault  := _bFault;
```

## 3. Analog scaling

```iecst
// Fn_ScaleAnalog: linear scaling of raw counts to engineering units.
FUNCTION Fn_ScaleAnalog : REAL
VAR_INPUT
    iRaw        : INT;      // raw counts
    iRawMin     : INT;      // counts at eng. min (e.g. 0 for 4 mA)
    iRawMax     : INT;      // counts at eng. max (e.g. 32767 for 20 mA)
    rEngMin     : REAL;     // engineering value at iRawMin
    rEngMax     : REAL;     // engineering value at iRawMax
END_VAR
```

```iecst
IF iRawMax = iRawMin THEN
    Fn_ScaleAnalog := rEngMin;  // avoid divide by zero on bad config
ELSE
    Fn_ScaleAnalog := rEngMin + (INT_TO_REAL(iRaw - iRawMin) * (rEngMax - rEngMin))
                      / INT_TO_REAL(iRawMax - iRawMin);
END_IF
```

Detect a broken wire (e.g. below 3.6 mA) in the calling FB by comparing `iRaw` with a threshold constant, debounced with a TON. Feed the result into the sequence's jumps as a fault cause.

## 4. Latched alarm with reset

```iecst
// Alarm latches on the debounced condition and clears on reset once the condition is gone
IF _fbAlarmDelay.Q THEN
    _bAlarm := TRUE;
ELSIF bReset AND NOT bCondition THEN
    _bAlarm := FALSE;
END_IF

_fbAlarmDelay(IN := bCondition, PT := ALARM_DEBOUNCE);

bAlarm := _bAlarm;      // output copy, last
```
