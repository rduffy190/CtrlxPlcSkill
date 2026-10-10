// Enum with attributes and explicit base type, a struct, and a struct that nests it.
{attribute 'qualified_only'}
{attribute 'strict'}
TYPE E_TestState :
(
    Idle := 0,
    Running,
    Done := 5,
    Faulted
) UINT;
END_TYPE

TYPE ST_Pair :
STRUCT
    rA      : REAL;     // first
    rB      : REAL := 1.5;
END_STRUCT
END_TYPE

TYPE ST_Nested :
STRUCT
    stPair  : ST_Pair;
    aiVals  : ARRAY[0..3] OF INT;
    sName   : STRING(15);
END_STRUCT
END_TYPE
