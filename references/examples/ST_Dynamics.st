// Type needed by FB_AxisCtrl.st (ST here, ladder in codesys-lad) (AXIS_REF, MC_* and ERROR_CODE come from libraries).
TYPE ST_Dynamics :
STRUCT
    lrVel   : LREAL;
    lrAcc   : LREAL;
    lrDec   : LREAL;
    lrJerk  : LREAL;
END_STRUCT
END_TYPE
