VAR_GLOBAL
    bFlag       : BOOL;                         // plain
    iCount      : INT := 3;                     // simple initial value
    stPair      : ST_Pair := (rA := 2.0);       // structured initial value: kept as raw text (warning)
    aiBuf       : ARRAY[1..10] OF INT;
END_VAR
