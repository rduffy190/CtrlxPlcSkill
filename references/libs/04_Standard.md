# 4 Standard

## 4.1 Introduction and overview

The "Standard" library contains all functions and function blocks required by
IEC61131-3 as standard function blocks for an IEC programming system. The
difference between a standard function and an operator is that the operator
is implicitly known to the programming system, whereas the standard function
blocks have to be bound to the project as library.

## 4.2 String Functions

### 4.2.1 CONCAT

Function block of the "Standard" library.
Function of type STRING; returns the concatenation of two strings.

Inputs:
STR1 : STRING;          Character strings to be concatenated.
STR2 : STRING;          Character strings to be concatenated.

Return value: STRING, resulting character string.
CONCAT(STR1,STR2) means: Concatenate STR1 and STR2 to form a single
string STR1STR2.

Example in IL: (Result is "SUSIWILLI")

Example in FBD:

Beispiel in ST:
VarSTRING1 := CONCAT ('SUSI','WILLI');

### 4.2.2 DELETE

Function block of the "Standard" library.
Function of type STRING; deletes a substring from a larger string starting at a
given position.

Inputs:
STR : STRING;        Character string from which a substring is to be
                     removed.
LEN : INT;           Length of the substring to be removed (number of char‐
                     acters).
POS : INT;           Position in STR from which a substring of LEN characters
                     is to be deleted; POS is specified in number of charac‐
                     ters, counting from the left.

Return value: STRING, character string remaining after deletion.
DELETE(STR, L, P) means: Delete L-characters from STR, starting with the
character at position POS.

Example in IL: (Result is "SUSI")

Example in FBD:

Beispiel in ST:
Var1 := DELETE ('SUXYSI',2,3);

### 4.2.3 FIND

Function block of the "Standard" library.
Function of type INT; browses for the position of a specific substring in a
string.

Inputs:
STR1 : STRING;          Character string in which to browse for string STR2.
STR2 : STRING;          Substring whose position is to be browsed for in
                        STR1.

Return value: INT, start position of STR2 in STR1; "0" if STR2 is not found in
STR1
FIND(STR1, STR2) means: Find the position of the first character of the first
occurrence of STR2 in STR1. If STR2 does not occur in STR1, OUT := 0.

Example in IL: (Result is "4")

Example in FBD:

Beispiel in ST:
VarINT1 := FIND ('abcdef','de');

### 4.2.4 INSERT

Function block of the "Standard" library.
Function of type STRING; inserts one string into another from a certain posi‐
tion.

Inputs:
STR1 : STRING;          Caracter string into which STR2 is to be inserted.
STR2 : STRING;          Character string to be inserted into STR1.
POS : INT;              Position in STR1 at which STR2 is to be inserted;
                        number of characters counted from the left.

Return value: STRING, result string.
INSERT(STR1, STR2, POS) means: Insert STR2 into STR1 at position POS.

Example in IL: (Result is "SUXYSI")

Example in FBD:

Beispiel in ST:
VarSTRING1 := INSERT ('SUSI','XY',2);

### 4.2.5 LEFT

Function block of the "Standard" library.
Function of type STRING; returns a left-hand start string of a character string.

Inputs:
STR : STRING;           STRING; string to be analyzed.
SIZE : INT;             Length of the left-hand start string (number of charac‐
                        ters).

Return value: STRING; start string.
LEFT (STR, SIZE) means: Take the first SIZE characters from the left in the
STR string.

Example in IL: (Result is "SUS")

Example in FBD:

Beispiel in ST:
VarSTRING1 := LEFT ('SUSI',3);

### 4.2.6 LEN

Function block of the "Standard" library.
Function of type STRING; returns the length of a string.

Input:
STR : STRING;           String to be analyzed.

Return value: INT, length of the character string (number of characters).

Example in IL: (Result is "4")

Example in FBD:

Beispiel in ST:
VarINT1 := LEN ('SUSI');

### 4.2.7 MID

Function block of the "Standard" library.
Function of type STRING; returns a substring of a string.

Inputs:
STR : STRING;           String to be analyzed.
LEN : INT;              Length of the substring (number of characters).
POS : INT;              Start position of the substring; results when the
                        number of characters given here in STR is moved from
                        left to right.

Return value: STRING, substring.
MID (STR, LEN, POS) means: Remove LEN characters from string STR, starting
with the character at position POS.

Example in IL: (Result is "US")

Example in FBD:

Beispiel in ST:
VarSTRING1 := MID ('SUSI',2,2);

### 4.2.8 REPLACE

Function block of the "Standard" library.
Function of type STRING; replaces a substring of a string with another string.

Inputs:
STR1 : STRING;          Character string, part of which is to be replaced by
                        string STR2.
STR2 : STRING;          Character string to replace part of STR1.
L : INT;                Length of the substring in STR1 to be replaced.
P : INT;                Position in STR1 from which STR2 is to be inserted
                        instead of the existing L-characters.

Return value: STRING, resulting character string.
REPLACE(STR1, STR2, L, P) means: Replace L-characters from STR1 with
STR2, starting with the Pth character in STR1.

Example in IL: (Result is "SKYSI")

Example in FBD:

Beispiel in ST:
VarSTRING1 := REPLACE ('SUXYSI','K',2,2);

### 4.2.9 RIGHT

Function block of the "Standard" library.
Function of type STRING; returns a right-hand start string of a character
string.

Inputs:
STR : STRING;           String to be analyzed.
SIZE : INT;             Length of the right-hand start string (number of char‐
                        acters).

Return value: STRING; start string.
RIGHT(STR, SIZE) means: Take the first SIZE characters from the right in the
STR string.

Example in IL: (Result is "USI")

Example in FBD:

Beispiel in ST:
VarSTRING1 := RIGHT ('SUSI',3);

## 4.3 Bistable function blocks

### 4.3.1 RS

Function block of the "Standard" library.
Function block resets bistable function block.

Inputs:
SET : BOOL;             Setting: If this input is TRUE, output Q1 is set to 1.
RESET1 : BOOL;          Reset: If this input is TRUE, output Q1 is reset to 0.

Output:
Q1 : BOOL;              Is TRUE when SET1 becomes TRUE.

Q1 = RS (SET, RESET1) means: Q1 = NOT RESET1 AND (Q1 OR SET)

Deklarationsbeispiel:
RSInst : RS;

Example in IL:

Example in FBD:

Beispiel in ST:
RSInst(SET:= VarBOOL1 , RESET1:=VarBOOL2 );              VarBOOL3 :=
RSInst.Q1;

### 4.3.2 SR

Function block of the "Standard" library.
Function block sets bistable function blocks to dominant.

Inputs:
SET1 : BOOL;            Setting: If this input is TRUE, output Q1 is set to 1.
RESET : BOOL;           Reset: If this input is TRUE, output Q1 is reset to 0.

Output:
Q1 : BOOL;              Is TRUE when SET1 becomes TRUE.

Q1 = SR (SET1, RESET) means: Q1 = (NOT RESET AND Q1) OR SET1

Deklarationsbeispiel:
SRInst : SR;

Example in IL:

Example in FBD:

Beispiel in ST:
SRInst(SET1:= VarBOOL1 , RESET:=VarBOOL2 ); VarBOOL3 :=
SRInst.Q1;

## 4.4 Edge detection

### 4.4.1 F_TRIG

Function block of the "Standard" library.
Function block detects a falling edge.

Input:
CLK : BOOL;             Boolean input signal checked for a falling edge.

Output:
Q : BOOL;               Is TRUE when a falling edge is detected at CLK.

When the input variable CLK returns TRUE, the output Q and the auxiliary
variable M are FALSE. When CLK returns FALSE, Q first returns TRUE and then
M is set to TRUE, i.e. each time the function block instance is called again, Q
is first set to TRUE and then returns FALSE, followed by a falling edge in CLK.

Q := NOT CLK AND NOT M;
M := NOT CLK;

Declaration example:

FTRIGInst : F_TRIG ;

Example in IL:

Example in FBD:

Beispiel in ST:
  FTRIGInst(CLK:= VarBOOL1);        VarBOOL2 := FTRIGInst.Q;

### 4.4.2 R_TRIG

Function block of the "Standard" library.
Function block detects a rising edge.

 Input:
 CLK : BOOL;            Boolean input signal checked for a rising edge.

 Output:
 Q : BOOL;              Is TRUE when a rising edge is present at CLK.

When the input variable CLK returns FALSE, the output Q and the auxiliary
variable M are FALSE. When CLK returns TRUE, Q first returns TRUE and then
M is set to TRUE, i.e. each time the function block instance is called again, Q
is first set to TRUE and then returns FALSE, followed by a rising edge in CLK.
Q := CLK AND NOT M;
M := CLK;

Deklarationsbeispiel:
RTRIGInst : R_TRIG ;

Example in IL:

Example in FBD:

Beispiel in ST:
RTRIGInst(CLK:= VarBOOL1);         VarBOOL2 := RTRIGInst.Q;

## 4.5 Counter

### 4.5.1 CTD

Function block of the "Standard" library.
Function block for decrementing.

Inputs:
CD : BOOL;              A rising edge at this input starts decrementing CV.
LOAD : BOOL;            If this input is TRUE, CV is set to the upper limit PV.

PV : WORD;              Upper limit, start value when decrementing CV.

The type WORD used in IndraLogic for PV does not comply with the IEC
standard that specifies type INT.

Outputs:
Q : BOOL;               Is TRUE when CV is 0.
CV : WORD;              Value is decremented by 1 from the start value PV
                        until 0 is reached.

If LOAD is TRUE, the counter variable CV is initialized with the upper limit PV.
If CD has a rising edge from FALSE to TRUE, CV is decreased by 1 as long as
CV is greater than 0 (i.e. if no underflow is caused).
Q returns TRUE if CV is 0.

Deklarationsbeispiel:
CTDInst : CTD;

Example in IL:

Example in FBD:

Beispiel in ST:
CTDInst(CD:= VarBOOL1, LOAD:=VarBOOL2 , PV:= VarWORD1);
VarBOOL3 := CTDInst.Q; VarINT1 := CTDInst.CV;

### 4.5.2 CTU

Function block of the "Standard" library.
Function block for incrementing.

 Inputs:
 CU : BOOL;             A rising edge at this input starts incrementing CV.
 RESET : BOOL;          If this input is TRUE, CV is reset to 0.
 PV : WORD;             Upper limit to increment CV.

The type WORD used in IndraLogic for PV does not comply with the IEC
standard that specifies type INT.

 Outputs:
 Q : BOOL;              Is TRUE when CV reached the upper limit PV.
 CV : WORD;             Counting continues until PV is reached.

If RESET is TRUE, the counter variable CV is initialized with 0. If CU has a
rising edge from FALSE to TRUE, CV is increased by 1.

Declaration example:
CTUInst : CTU;

Example in IL:

Example in FBD:

Beispiel in ST:
CTUInst(CU:= VarBOOL1, RESET:=VarBOOL2 , PV:= VarWORD1);
VarBOOL3 := CTUInst.Q; VarINT1 := CTUInst.CV;

### 4.5.3 CTUD

Function block of the "Standard" library.
Function block that operates as up and down counter.

 Inputs:
 CU : BOOL;             If there is a rising edge at this input, incrementing CV
                        starts.

Inputs:
CD : BOOL;              If there is a rising edge at this input, decrementing CV
                        starts.
RESET : BOOL;           If TRUE, CV is set to 0.
LOAD : BOOL;            If TRUE, CV is set to PV.
PV : WORD;              Upper limit for incrementing/decrementing CV.

The type WORD used in IndraLogic for PV does not comply with the IEC
standard that specifies type INT.

Outputs:
QU : BOOL;              Is TRUE when CV >= PV.

QD : BOOL;              Is TRUE when CV decremented to 0.
CV : WORD;              Value to be incremented or decremented.

If RESET applies, the counting variable CV is initialized with 0. If LOAD
applies, CV is initialized with PV.
If CU has a rising edge from FALSE to TRUE, CV is increased by 1. If CD has a
rising edge from FALSE to TRUE, CV is decreased by 1 as long as CV does not
cause an underflow.
QU returns TRUE if CV is greater than or equal to PV.
QD returns TRUE if CV is 0.

Deklarationsbeispiel:
CTUDInst : CUTD;

Example in IL:

Example in FBD:

Beispiel in ST:
CTUDInst(CU := VarBOOL1, CU:= VarBOOL2, RESET := VarBOOL3,
LOAD:=VarBOOL4 , PV:= VarWORD1); VarBOOL5 := CTUDInst.QU;
VarBOOL6 := CTUDInst.QD; VarINT1 := CTUDInst.CV;

## 4.6 Timer

### 4.6.1 RTC

Function block of the "Standard" library.
RunTimeClock function block; returns the continuous date and time from a
specified start time.

 Inputs:
 EN : BOOL;                     A falling edge at this input starts incrementing
                                the time in CDT.
 PDT : DATE_AND_TIME;           Date and time at which the incrementation
                                should start.

 Outputs:
 Q : BOOL;                      Is TRUE as long as CDT increments.
 CDT : DATE_AND_TIME;           Current state of the incremented time.

VarBOOL2:=RTC(EN, PDT, Q, CDT) means:
When EN changes to TRUE, the time of the PDT is set and incremented in
seconds and output via CDT when EN is TRUE. When EN is set to FALSE again,
CDT jumps to the initial value of DT#1970-01-01-00:00:00.

Example in IL:

Example in FBD:

Beispiel in ST:
RTC(EN:=VarBOOL1, PDT:=DT#2006-03-30-14:00:00, Q=>VarBOOL2,
CDT=>VarTimeCur);

### 4.6.2 TOF

Function block of the "Standard" library.

Function block; implements switch-off delay. If the input changes from TRUE
to FALSE (falling edge), a specific amount of time elapses before the output
also becomes FALSE.

Inputs:
IN : BOOL;              A falling edge at this input starts incrementing the
                        delay time in ET.
PT : TIME;              Upper limit to increment ET (delay time).

Outputs:
Q : BOOL;               Is provided with a falling edge when ET reached the
                        upper limit PV (delay time elapsed).

ET : TIME;              Current delay time.

TON(IN, PT, Q, ET) means: When IN is FALSE, the time in ET is incremented in
milliseconds until the value is the same as in PT. It then remains the same.
Q is FALSE if IN is FALSE and ET is PT. Otherwise it is TRUE.
Q therefore has a falling edge when the time specified in PT in milliseconds
has elapsed.

Deklarationsbeispiel:
TOFInst : TOF ;

Example in IL:

Example in FBD:

Beispiel in ST:
  TOFInst(IN := VarBOOL1, PT:= T#5s);          VarBOOL2 :=TOFInst.Q;

### 4.6.3 TON

Function block of the "Standard" library.
Function block; implements switch-on delay. After the input has become
TRUE, a certain time will elapse before the output also becomes TRUE.

 Inputs:
 IN : BOOL;             A rising edge at this input starts incrementing the
                        time in ET.
 PT : TIME;             Upper limit for the time in ET (delay time).

 Output:
 Q : BOOL;              Is provided with a rising edge when ET reached the
                        upper limit PT (delay time elapsed).
 ET : TIME;             Current delay time.

TON(IN, PT, Q, ET) means: Q is TRUE if IN is TRUE and ET is PT. Otherwise it
is FALSE.
Q therefore has a rising edge when the time specified in PT in milliseconds
has elapsed.

Deklarationsbeispiel:
TONInst : TON ;

Example in IL:

Example in FBD:

Beispiel in ST:
TONInst(IN := VarBOOL1, PT:= T#5s);

### 4.6.4 TP

Function block of the "Standard" library.
Function block operating as pulse generator. A timer is incremented to a given

upper limit. While incrementing, the pulse variable (Q) is TRUE, otherwise
FALSE.

Inputs:
IN : BOOL;              A rising edge at this input starts incrementing the
                        time in ET.
PT : TIME;              Upper limit of time in ET.

Outputs:
Q : BOOL;               Is TRUE when the time is incremented in ET (pulse).
ET : TIME;              Current time.

When IN is TRUE, the time in ET is incremented in milliseconds until the value
is equal to that in PT. The value then remains constant.
Q is TRUE after IN has changed to TRUE and if ET is still less than or equal to
PT. Otherwise it is FALSE.
Q therefore provides a signal for the period specified in PT.

Deklarationsbeispiel:
TPInst : TP ;

Example in IL:

Example in FBD:

Beispiel in ST:
  TPInst(IN := VarBOOL1, PT:= T#5s);           VarBOOL2 :=TPInst.Q;
