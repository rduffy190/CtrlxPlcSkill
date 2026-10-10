// FB_All: every var block in house order, plus an ST body with IF/CASE.
FUNCTION_BLOCK FB_All
VAR_INPUT
    bIn         : BOOL;             // input
    stCfg       : ST_Pair;          // struct input
END_VAR
VAR_OUTPUT
    eState      : E_TestState;      // enum output
    rOut        : REAL;
END_VAR
VAR_IN_OUT
    aiData      : ARRAY[1..10] OF INT;
END_VAR
VAR_IN_OUT CONSTANT
    stLimits    : ST_Pair;
END_VAR
VAR
    _eState     : E_TestState;
    _fbTimer    : TON;
END_VAR
VAR CONSTANT
    DELAY       : TIME := T#2S;
END_VAR

CASE _eState OF
    E_TestState.Idle:
        IF bIn THEN
            _eState := E_TestState.Running;
        END_IF
    E_TestState.Running:
        IF _fbTimer.Q THEN
            _eState := E_TestState.Done;
        END_IF
END_CASE
_fbTimer(IN := _eState = E_TestState.Running, PT := DELAY);
rOut := stCfg.rA + stLimits.rB;
eState := _eState;
END_FUNCTION_BLOCK

// Fn_Add: a function with a return type.
FUNCTION Fn_Add : REAL
VAR_INPUT
    rA          : REAL;
    rB          : REAL;
END_VAR
Fn_Add := rA + rB;
END_FUNCTION

// PRG_Test: a program calling the FB and the function, using the GVLs.
PROGRAM PRG_Test
VAR
    fbAll       : FB_All;
    rSum        : REAL;
END_VAR
fbAll(bIn := GVL_Test.bFlag, stCfg := GVL_Test.stPair, aiData := GVL_Test.aiBuf, stLimits := GVL_Test.stPair);
rSum := Fn_Add(rA := fbAll.rOut, rB := LREAL_TO_REAL(GVL_Retain.lrOffset));
END_PROGRAM
