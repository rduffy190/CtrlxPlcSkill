// Example from the PressSystem project (2026-10-09). Built to PLCopenXML and schema-valid; NOT yet compiled
// in ctrlX PLC Engineering. If MC_Halt's axis pin fails to compile, the manual also names it 'Axes'.
// FB_AxisCtrl: one ctrlX axis through CXA_PLCopen: power, absolute move, halt, reset and status.
// Latches the first error with its ctrlX diagnosis until reset. Not a sequence; the caller drives it.
FUNCTION_BLOCK FB_AxisCtrl
VAR_INPUT
    bPower          : BOOL;         // power on (level)
    bMove           : BOOL;         // absolute move (Execute): needs a FALSE->TRUE edge per move
    lrPosition      : LREAL;        // target position, taken at the edge of bMove
    stDyn           : ST_Dynamics;  // move dynamics, taken at the edge of bMove
    bHalt           : BOOL;         // halt (Execute, level)
    lrHaltDec       : LREAL;        // halt deceleration
    bReset          : BOOL;         // reset latched error and drive ErrorStop (level)
END_VAR
VAR_OUTPUT
    bPowered        : BOOL;         // power on and confirmed
    bStandstill     : BOOL;         // powered, not moving, no error
    bInPos          : BOOL;         // current move done (held while bMove is TRUE)
    bHalted         : BOOL;         // halt done (held while bHalt is TRUE)
    bError          : BOOL;         // latched error (FB error or axis ErrorStop)
    lrActPos        : LREAL;        // actual position (valid while powered)
    eErrorID        : ERROR_CODE;   // latched error class
    dwDiagMain      : DWORD;        // latched ctrlX main diagnosis (0 for a drive ErrorStop: see ctrlX diagnostics)
    dwDiagDetail    : DWORD;        // latched ctrlX detail diagnosis
END_VAR
VAR_IN_OUT
    stAxis          : AXIS_REF;     // axis to control
END_VAR
VAR
    _bError         : BOOL;
    _eErrorID       : ERROR_CODE;
    _dwDiagMain     : DWORD;
    _dwDiagDetail   : DWORD;
    _fbPower        : MC_Power;
    _fbReset        : MC_Reset;
    _fbStatus       : MC_ReadStatus;
    _fbActPos       : MC_ReadActualPosition;
    _fbMove         : MC_MoveAbsolute;
    _fbHalt         : MC_Halt;
END_VAR

// Latch the first error. Sub-FB results are from the previous scan, the same as a timer's Q.
IF NOT _bError THEN
    IF _fbPower.Error THEN
        _bError := TRUE;  _eErrorID := _fbPower.ErrorID;
        _dwDiagMain := _fbPower.ErrorIdent.Additional1;  _dwDiagDetail := _fbPower.ErrorIdent.Additional2;
    ELSIF _fbMove.Error THEN
        _bError := TRUE;  _eErrorID := _fbMove.ErrorID;
        _dwDiagMain := _fbMove.ErrorIdent.Additional1;   _dwDiagDetail := _fbMove.ErrorIdent.Additional2;
    ELSIF _fbHalt.Error THEN
        _bError := TRUE;  _eErrorID := _fbHalt.ErrorID;
        _dwDiagMain := _fbHalt.ErrorIdent.Additional1;   _dwDiagDetail := _fbHalt.ErrorIdent.Additional2;
    ELSIF _fbReset.Error THEN
        _bError := TRUE;  _eErrorID := _fbReset.ErrorID;
        _dwDiagMain := _fbReset.ErrorIdent.Additional1;  _dwDiagDetail := _fbReset.ErrorIdent.Additional2;
    ELSIF _fbStatus.Error THEN
        _bError := TRUE;  _eErrorID := _fbStatus.ErrorID;
        _dwDiagMain := _fbStatus.ErrorIdent.Additional1; _dwDiagDetail := _fbStatus.ErrorIdent.Additional2;
    ELSIF _fbStatus.Valid AND _fbStatus.ErrorStop THEN
        // Error raised in the drive/motion kernel while moving; the detail is in the ctrlX diagnostics log
        _bError := TRUE;  _eErrorID := ERROR_CODE.DEVICE_ERROR;
        _dwDiagMain := 0;  _dwDiagDetail := 0;
    END_IF
ELSIF bReset AND NOT _fbStatus.ErrorStop AND NOT _fbReset.Active THEN
    _bError      := FALSE;
    _eErrorID    := ERROR_CODE.NONE_ERROR;
    _dwDiagMain  := 0;
    _dwDiagDetail:= 0;
END_IF

// Sub-FBs, every scan.
// A failed Power/ReadStatus (e.g. motion not RUNNING yet) needs a new edge: reset drops Enable for one scan.
_fbPower(Enable := bPower AND NOT (_fbPower.Error AND bReset), Axis := stAxis);
_fbStatus(Enable := bPower AND NOT (_fbStatus.Error AND bReset), Axis := stAxis);
_fbActPos(Enable := bPower AND NOT (_fbActPos.Error AND bReset), Axis := stAxis);
_fbReset(Execute := bReset AND _fbStatus.ErrorStop, Axis := stAxis);
_fbMove(Execute      := bMove AND NOT _bError,
        Position     := lrPosition,
        Velocity     := stDyn.lrVel,
        Acceleration := stDyn.lrAcc,
        Deceleration := stDyn.lrDec,
        Jerk         := stDyn.lrJerk,
        BufferMode   := MC_BUFFER_MODE.mcAborting,
        Axis         := stAxis);
// No halt on an unpowered axis or one in ErrorStop: the drive has already stopped it
_fbHalt(Execute      := bHalt AND _fbPower.Status AND NOT _fbStatus.ErrorStop,
        Deceleration := lrHaltDec,
        Jerk         := 0.0,
        Axis         := stAxis);

// Outputs, last
bPowered     := _fbPower.Status;
bStandstill  := _fbStatus.Valid AND _fbStatus.Standstill;
// Gated by the command so a Done can never outlive the step that asked for it
bInPos       := _fbMove.Done AND bMove;
bHalted      := _fbHalt.Done AND bHalt;
bError       := _bError;
lrActPos     := _fbActPos.Position;
eErrorID     := _eErrorID;
dwDiagMain   := _dwDiagMain;
dwDiagDetail := _dwDiagDetail;
END_FUNCTION_BLOCK
