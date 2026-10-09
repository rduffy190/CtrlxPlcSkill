# 36 CXA_Utilities

## 36.1 Introduction and overview

General information
The "CXA_Utilities" library extends the basic functionality of the system and
provides common basic functionalities. The library includes basic functionali‐
ties for several applications or as standalone functionality.

Table 986: Areas of application and functions/function blocks of CXA_Utilities
Area of application (folder in library)
Function blocks                                    Description
Jogging variables (Adjustment)
⮫ Chapter 36.2.2 IL_ContinuousAdjustType01         Continuous adjustment of a REAL variable via
on page 1141                                       binary inputs
⮫ Chapter 36.2.3 IL_ContinuousAdjustType02         Continuous adjustment of a DINT variable via
on page 1145                                       binary inputs.
⮫ Chapter 36.2.4 IL_IncrementalAdjustType01        Incremental adjustment of a REAL variable via
on page 1148                                       binary inputs

1134 /    ctrlX PLC Engineering
1344      Introduction and overview

Basic classes for the function block development (Base FB)
⮫ Chapter 36.3.2 IL_EnableDoneBase               Implements the interface of a function block
on page 1155                                     with an "Enable" input and "Done", "Active" and
"Standard" error outputs
⮫ Chapter 36.3.3 IL_EnableInOpBase               Implements the interface of a function block
on page 1158                                     with an "Enable" input and "InOperation" and
"Standard" error outputs
⮫ Chapter 36.3.4 IL_EnableInOpShutdownBase Implements the interface of a function block
on page 1161                                     with an "Enable" input and "InOperation", "Shut‐
down" and "Standard" error outputs.
⮫ Chapter 36.3.7 IL_ExecuteDoneAbortedBase       Implements the interface of a function block
on page 1170                                     with an "Execute" input and the "Done", "Com‐
mandAborted", "Active" and "Standard" error
outputs
⮫ Chapter 36.3.8 IL_ExecuteDoneAbortedShut‐ Implements the interface of a function block
downBase on page 1173                            with an "Execute" input and "Done", “Active”,
“Shutdown“, CommandAborted” output and
"Standard" error outputs
⮫ Chapter 36.3.5 IL_ExecuteDoneBase              Implements the interface of a function block
on page 1165                                     with an "Execute" input and "Done", "Active" and
"Standard" error outputs
⮫ Chapter 36.3.6 IL_ExecuteInOpBase              Implements the interface of a function block
on page 1167                                     with an "Execute" input and "InOperation",
"Active" and "Standard" error outputs
Conversion (Bit-Stream Connect)
⮫ Chapter 36.4.2 IL_BoolToByte on page 1179      8 individual bits (BOOL) are converted into one
BYTE (FUN)
⮫ Chapter 36.4.3 IL_BoolToDWord on page 1180 32 individual bits (BOOL) are converted into one
DWORD (FUN)
⮫ Chapter 36.4.4 IL_BoolToWord on page 1183 16 individual bits (BOOL) are converted into one
WORD (FUN)
⮫ Chapter 36.4.5 IL_ByteToDWord on page 1184 4 BYTEs are converted into one DWORD (FUN)
⮫ Chapter 36.4.6 IL_ConcatByte on page 1185     2 BYTEs are summarized to one WORD (FUN)
⮫ Chapter 36.4.7 IL_ConcatWord on page 1186     2 WORDs are summarized to one DWORD
Conversion (Bit-Stream Split)
⮫ Chapter 36.5.2 IL_ByteToBool on page 1187  Function block extracts 8 bits (BOOL) from one
BYTE
⮫ Chapter 36.5.3 IL_DWordToBool on page 1188 Function block extracts 32 bits (BOOL) from
one DWORD
⮫ Chapter 36.5.4 IL_DWordToByte on page 1191 Function block extracts 4 BYTEs from one
DWORD
⮫ Chapter 36.5.5 IL_HighByte on page 1191    FUN extracts a high-order BYTE from one WORD
⮫ Chapter 36.5.7 IL_HighWord on page 1193       FUN extracts a high-order WORD from one
DWORD
⮫ Chapter 36.5.6 IL_LowByte on page 1192        FUN extracts a low-order BYTE from one WORD
⮫ Chapter 36.5.8 IL_LowWord on page 1193        FUN extracts a low-order WORD from one
DWORD
⮫ Chapter 36.5.9 IL_WordToBool on page 1194     Function block extracts 16 bits (BOOL) from
one WORD
Conversion (ByteSwap)

              Introduction and overview        1344

⮫ Chapter 36.6.2 IL_SwapDWord on page 1196        FUN exchanges BYTEs of a DWORDs ( 3 2 1 0 ->
0 1 2 3)
Attention: Not PLC-compatible!
⮫ Chapter 36.6.3 IL_SwapWord on page 1196         FUN exchanges BYTEs of a WORD (1 0 -> 0 1)
Checksums (CRC16)
⮫ Chapter 36.7.2 IL_CRC16 on page 1197            Function block computes CRC16 checksum
using a date
Conversion (Datatype Change)
⮫ Chapter 36.8.2 IL_AsciiToByte on page 1199      FUN converts any ASCII character into a byte
code
⮫ Chapter 36.8.3 IL_ByteToAscii on page 1200      FUN converts any byte code into an ASCII char‐

acter
⮫ Chapter 36.8.4 IL_RealToString on page 1200     FUN converts REAL value into a STRING
⮫ Chapter 36.8.5 IL_LRealToString on page 1201 FUN converts (L)REAL value format-controlled
into a STRING
High-resolution time support (Debugging)
⮫ Chapter 36.9.2 IL_HighResTimeDiff            Calculates the time difference of two high-reso‐
on page 1203                                   lution time cycles of the system in microseconds
(before and after a code section)
⮫ Chapter 36.9.3 IL_HighResTimeTick            Reads the high-resolution time cycle of the
on page 1203                                   system
Trigger (FlipFlops)
⮫ Chapter 36.10.2 IL_Toggle on page 1205       Settable and resettable FlipFlop
Mathematical functions (Mathematical Functions)
⮫ Chapter 36.11.2 IL_InterpolationLinear       Calculates intermediate points and linearizations
on page 1207                                   for example
⮫ Chapter 36.11.3 IL_MaxValue on page 1209         Indicates the maximum value of all occurred
 values
Character strings without length limitation (StringFun_NoLimitStrLength)
⮫ Chapter 36.12.2 IL_StrLower on page 1213         Function converts character string into lower
 case letters
⮫ Chapter 36.12.3 IL_StrUpper on page 1214         Function converts character string into upper
 case letters
⮫ Chapter 36.12.4 IL_StrCompare on page 1214 Function compares two character strings and
 returns the difference. Upper and lower case let‐
 ters considered
⮫ Chapter 36.12.5 IL_StrCompareNoCase              Function compares two character strings and
on page 1215                                       returns the difference. Upper and lower case let‐
 ters not considered
⮫ Chapter 36.12.6 IL_StrNCompare                   Function compares the entered number of char‐
on page 1215                                       acters of two character strings and returns the
 difference. Upper and lower case letters consid‐
 ered
⮫ Chapter 36.12.7 IL_StrNCompareNoCase             Function compares the entered number of char‐
on page 1216                                       acters of two character strings and returns the
 difference. Upper and lower case letters not con‐
 sidered
⮫ Chapter 36.12.8 IL_AsciiStreamToBase64           Function converts a character string, saved in
on page 1217                                       ASCII format, into the BASE64 format
⮫ Chapter 36.12.9 IL_Base64ToAsciiStream          Function converts a character string, saved in
on page 1218                                      BASE64 format, into the ASCII format

1136 /    ctrlX PLC Engineering
1344      Introduction and overview

⮫ Chapter 36.12.12 IL_StrCopy on page 1224      Function copies character string from the source
to the destination address
⮫ Chapter 36.12.13 IL_StrNCopy on page 1224     Function copies partial character string from a
character string to a target character string.
Length of the target character string is specified.
If the source character string is shorter than the
requested length, the target character string is
supplemented by fill characters
⮫ Chapter 36.12.14 IL_CONCAT on page 1225       Function adds character string 2 behind char‐
acter string 1
⮫ Chapter 36.12.15 IL_DELETE on page 1226       Function deletes a partial character string from
the character string of a specified position
⮫ Chapter 36.12.16 IL_FIND on page 1227         Function searches for position of entered partial
character string in a character string
⮫ Chapter 36.12.17 IL_INSERT on page 1228       Function inserts a partial character string to a
character string starting from the entered posi‐
tion
⮫ Chapter 36.12.18 IL_LEFT on page 1229         Function provides the left part of a character
string with a length of x characters
⮫ Chapter 36.12.19 IL_LEN on page 1230          Function provides the character string length
⮫ Chapter 36.12.20 IL_MID on page 1230          Function provides a partial character string to
a character string starting from the entered posi‐
tion
⮫ Chapter 36.12.21 IL_REPLACE on page 1231      Function replaces a partial character string of
a character string by another partial character
string
⮫ Chapter 36.12.22 IL_RIGHT on page 1232        Function provides the right part of a character
string with a length of x characters
⮫ Chapter 36.12.23 IL_Ascii_To_Char             Function converts ASCII code into a character
on page 1233
⮫ Chapter 36.12.24 IL_Char_To_Ascii             Function converts a character into ASCII code
on page 1233
⮫ Chapter 36.12.25 IL_Int_To_Str on page 1234  Function converts (depending on format) an
integer into a character string
⮫ Chapter 36.12.27 IL_Real_To_Str on page 1234 Function converts (depending on format) a REAL
number into a character string
⮫ Chapter 36.12.29 IL_String_To_Unicode        Function converts a character string according
on page 1235                                   to the specified option (utf8/utf16) into Unicode
and stores the values in a DWORD array
⮫ Chapter 36.12.31 IL_Unicode_To_String        Function converts a Unicode character string
on page 1236                                   into a STRING according to the specified option
(utf8/utf16)
⮫ Chapter 36.12.34 IL_StrInverse on page 1239 Function inverts a character string
⮫ Chapter 36.12.35 IL_StrSetEndOfString         Functions sets the end of a character string
on page 1240
⮫ Chapter 36.12.36 IL_StrGetElement             The character string is split into multiple ele‐
on page 1241                                    ments by the entered separator string. The func‐
tion calls one of the elements
⮫ Chapter 36.12.37 IL_StrLChr on page 1242      Function isolates a partial character string from
the character string up to the first occurrence of
the entered separator

              Introduction and overview        1344

⮫ Chapter 36.12.38 IL_StrRChr on page 1242      Function isolates a partial character string from
the character string up to the last occurrence of
the entered separator
⮫ Chapter 36.12.39 IL_StrSetElement             Character string separated into elements by the
on page 1243                                    entered separator order. The function positions
a new element to the desired position in the
character string
⮫ Chapter 36.12.40 IL_StrSplit on page 1244     Character string separated by specified sepa‐
rator. The function stores the address of each
partial character string in an array
⮫ Chapter 36.12.41 IL_StrTrimAll on page 1245   Function deletes all specified characters in a
character string

⮫ Chapter 36.12.42 IL_StrTrimSpace              Depending on the option, the function deletes
on page 1246                                    spaces in a character string
Time functions (TIME)
⮫ Chapter 36.13.2 IL_Date on page 1248          Reads the current system date
⮫ Chapter 36.13.3 IL_DateAndTime                Reads current system date and time
on page 1249
⮫ Chapter 36.13.5 IL_ExtSysTimeDate             Reads current system date and time in the
on page 1250                                    extended system format
⮫ Chapter 36.13.6 IL_LocalTime on page 1251  Converts control-internal UTC time into local
time
⮫ Chapter 36.13.7 IL_SysTime64 on page 1253 Reads current system date and time in microsec‐
onds since 01.01.1970
⮫ Chapter 36.13.10 IL_SysTime64ToSysTimeDate Converts the format of system date and system
on page 1255                                 time
⮫ Chapter 36.13.9 IL_SysTimeDate on page 1254 Reads current system date and time
⮫ Chapter 36.13.8 IL_SysTimeDateToSysTime64 Converts the format of system date and system
on page 1253                                  time
⮫ Chapter 36.13.4 IL_TimeOfDay on page 1249     FUN reads the current system time
Double-linked lists (Utilities/Logic)
⮫ Chapter 36.14.2 IL_LinkedList on page 1259    Manages double-linked lists (used for ring
buffer, FIFOs and LIFOs)
Modulo value calculation (Utilities/Logic)
⮫ Chapter 36.15.4 IL_GetModuloType01            Calculates a modulo value. Value range between
on page 1266                                    0.0 and + modulo value (REAL)
⮫ Chapter 36.15.5 IL_GetModuloType02            Calculates a modulo value. Value range between
on page 1268                                    0 and + modulo value (DINT)
⮫ Chapter 36.15.6 IL_GetModuloType03            Calculates a modulo value. Value range between
on page 1269                                    - modulo value and + modulo value (REAL)
⮫ Chapter 36.15.7 IL_GetModuloType04              Calculates a modulo value. Value range between
on page 1270                                      - modulo/2 and + modulo value/2 (REAL)
Trigonometric functions (Utilities/Trigonometric Functions)
⮫ Chapter 36.15.2 IL_DegToRad on page 1265        Converts angle in degree into angle in radian
  measure incl. modulo
⮫ Chapter 36.15.3 IL_RadToDeg on page 1266        Converts an angle in radian measure into the
  corresponding angle in degree incl. modulo

1138 /    ctrlX PLC Engineering
1344      Jogging variables (adjustment)

## 36.2 Jogging variables (adjustment)

### 36.2.1 Introduction and overview

Adjust (jog) the PLC variables continuously or incrementally via binary inputs
using the following function blocks:

Table 987: CXA_Utilities, Adjustment
Area of application (folder in library)
Function blocks                                   Description
Jogging variables (adjustment)
⮫ Chapter 36.2.2 IL_ContinuousAdjustType01        Continuous adjustment of a REAL variable via
on page 1141                                      binary inputs
⮫ Chapter 36.2.3 IL_ContinuousAdjustType02        Continuous adjustment of a DINT variable via
on page 1145                                      binary inputs.
⮫ Chapter 36.2.4 IL_IncrementalAdjustType01       Incremental adjustment of a REAL variable via
on page 1148                                      binary inputs
                     When using the above mentioned function blocks to jog PLC variables, con‐
                     sider the following requirements:
                     ● Stop the operation via a binary input ("Enable")
                     ● The variable to be affected can be continuously adjusted using the function
                       blocks IL_ContinuousAdjustType01 and IL_ContinuousAdjustType02.
                     ● The variable to be affected can be incrementally adjusted using the func‐
                       tion block IL_IncrementalAdjustType01.
                     ● The selected variable can either be changed in incremented or decre‐
                       mented steps within the limit values.
                     ● When reaching a limit value ("HighLimitActive" = TRUE or "LowLimitActive"
                       = TRUE), the continuous adjustment is disabled and thus, the function
                       block does no longer affect the variable. In this case, the respective limit
                       value is displayed at the "HighLimit" input or at the "LowLimit" input

General basics
If the limits “HighLimit" and "LowLimit" have the same value for a specified
modulo value, "LowLimit" is set to zero and "HighLimit" is set to the modulo
value. Thus, it is possible to adjust the limit values in the entire modulo
range.
The change rate describes the rate the affected variable changes during
adjustment. This rate depends on the step width and the number of steps per
second. The change rate is calculated as follows, for example, when changing
a position:

If, for example, the speed of the virtual master axis is changed, the change
rate is calculated as follows:

                                         Jogging variables (adjustment)        1344

As long as the control signal is present, the affected variable is changed with
the defined velocity.

Adjustment limits
The variable can only be adjusted via the corresponding inputs within the
determined limit values.
Exception:
If the initial value of the variable to be adjusted is not in the specified limits,
the affected variable can only be adjusted in the direction of the target range.
If a modulo value is specified, the affected variable can be adjusted in both
directions. After reaching the target range, it is no longer possible to leave
this range.

Preset
The output variable can be pre-assigned to a definite value using the inputs
"Preset" and "PresetValue". The "PresetAck” output is set as soon as the "Pre‐
setValue" was applied. The output variable remains on the "PresetValue" as
long as the "Preset" input is set.

Basic rules
● If both control signals ("Inc"/"Dec") are TRUE at the same time, they are
   evaluated as FALSE
● A control signal changes the polarity and causes an immediate change of
   direction. The current adjustment is also not completed
● If the adjustment velocity is changed during a motion, the behavior of the
   following function blocks differ:
   IL_ContinuousAdjustType01/IL_ContinuousAdjustType02 and
   IL_IncrementalAdjustType01
   The change becomes immediately effective for IL_ContinuousAdjustType01
   and IL_ContinuousAdjustType02. In contrast, the motion for IL_Incrementa‐
   lAdjustType01 is finished before the new step velocity is accepted. A subse‐
   quent adjustment is performed with the adjusted variables.
Furthermore, the following rules apply to the function block IL_IncrementalAd‐
justType01:
● The inputs "Inc" and "Dec" are evaluated with regard to the edges. A rising
  edge causes an adjustment by the specified step width ("StepWidth")
● A new control signal (positive edge) with the same polarity detected during
  a running motion causes another motion following the current motion

1140 /    ctrlX PLC Engineering
1344      Jogging variables (adjustment)

incremental change

During the first activation ("Enable" = TRUE), the function blocks IL_Con‐
tinuousAdjustType01, IL_ContinuousAdjustType02 and IL_IncrementalAdjust‐
Type01 initialize the variables required to determine the cycle time (irrespec‐
tive of the present inputs). In the second cycle, a calculated cycle time is
available required to calculate the correct change rate. Subsequently, the
cycle time is updated continuously.
By specifying a modulo value, the function block provides an output variable
between zero and the specified modulo value. When exceeding the modulo
value, the output variable is reset to zero. However, the adjustment continues.
The specified valid range can thus be between zero and the modulo value. The
range can be adjusted by the zero value.

                                       Jogging variables (adjustment)      1344

of 360°
In addition, the function block IL_ContinuousAdjustType01 or IL_Continu‐
ousAdjustType02 provides the possibility to adjust the change velocity
depending on the time by specifying scaling factors and time intervals.

### 36.2.2 IL_ContinuousAdjustType01

Brief description
The IL_ContinuousAdjustType01 function block allows a continuous adjust‐
ment of a REAL variable via binary inputs.

Table 988: Reference table of the IL_ContinuousAdjustType01
Library
CXA_Utilities

Interface description

1142 /    ctrlX PLC Engineering
1344      Jogging variables (adjustment)

Table 989: Interface variables of the IL_ContinuousAdjustType01 function block
I/O type           Name               Data type         Description
VAR_INPUT          Enable             BOOL              Enabling the function block (cyclic, state-
                                                        controlled)
                   Inc                BOOL              Increase affected variable
                   Dec                BOOL              Decrease affected variable
                   Preset             BOOL              Set the preset value (PresetValue)
                   PresetValue        REAL              Specified value for the preset value
                   ModuloValue        REAL              Modulo value (if 0, then absolute proc‐
                                                        essing)
                   HighLimit          REAL              Maximum output value of the variable to be
                                                        affected
                   LowLimit           REAL              Minimum output value of the variable to be
                                                        affected
                   StepWidth          REAL              Step width
                   StepsPerSecond     REAL              Number of steps per second
                   AdjTimeIntervals   ARRAY [1..4] OF   Time intervals in seconds to scale the
                                      REAL              change rate
                   AdjWeightFactors   ARRAY [1..5] OF   Scaling factors of the change rate
                                      REAL
VAR_OUTPUT InOperation                BOOL              Function block enabled. The outputs "High‐
                                                        LimitActive" and "LowLimitActive" are valid
                   Error              BOOL              Calculation of the variable "Value" to be
                                                        affected was completed with an error. The
                                                        output variable "ErrorIdent" is valid
                   ErrorID            ⮫ ERROR_CODE      Brief error description
                   ErrorIdent         ⮫ ERROR_STRUCT Detailed description of the diagnostics in
                                                     the event of an error
                                                        ⮫ Troubleshooting on page 1144
                   PresetAck          BOOL              The value of the "PresetValue" input was
                                                        applied
                   Changing           BOOL              The variable to be affected was calculated.
                                                        Output variable "Value" is valid
                   HighLimitActive    BOOL              Maximum output value of the variable to be
                                                        affected was reached
                   LowLimitActive     BOOL              Minimum output value of the variable to be
                                                        affected was reached
VAR_IN_OUT         Value              REAL              Variable to be affected

                                       Jogging variables (adjustment)       1344

Signal-time diagram

Functional description
The affected variable "Value" can be adjusted either in positive or negative
direction. A valid range is specified to affect the variable using the limit
values. The modulo value specification allows the adjustment in the reference
system of the axis. Specify the step width and the number of steps per
second to determine the change rate of the affected variable. Additionally,
a specified value ("PresetValue") in the permissible operating range can be
directly written to the affected variable.
After processing enabled via "Enable, the variable to be affected can be
changed via the inputs "Inc" (in positive direction) and "Dec" (in negative
direction). As long the “Inc” input or the “Dec” input is set, the adjustable
variable can be continuously increased or decreased (“StepsPerSecond” *
“StepWidth”).
When initializing the function block, ensure that the input variables "Modulo‐
Value", "HighLimit" and "LowLimit" are provided with valid values.
Specify the scaling factors ("AdjWeightFactors[ ]") and their respective time
intervals ("AdjTimeIntervals[ ]") to modify the change rate with regard to time.
The scaling factors and the time intervals have to be set in addition to the
inputs "StepsPerSecond" and "StepWidth". Depending on the current time
interval, the change rate is multiplied with the respective scaling factor. The
figure below shows the behavior of the function block using an example
configuration: The "AdjTimeIntervals" input variables ([T1; T2; T3; T4]) are
specified in seconds. T5 is the time interval between the completion of the
time interval T4 and the adjustment abort. The "AdjWeightFactors" input var‐
iables ([0.5; 1; 1.5; 2; 4]) determine the scaling of the change rate. The
last "AdjWeightFactors" value ("AdjWeightFactors [5]") is assigned to the time
interval T5.

1144 /    ctrlX PLC Engineering
1344      Jogging variables (adjustment)

If a time interval of 0 is selected, the following scaling factor is retained until
the adjustment is aborted.
Example:
If "AdjTimeIntervals[2]" = 0, the scaling factor of "AdjWeightFactors[3]" is
retained until the process is aborted.
The calculation of the elapsed time to define the correct time interval of the
scaling factors is reset with each new adjustment. If the inputs "AdjWeightFac‐
tors" and "AdjTimeIntervals" are not set, it is continuously adjusted with the
change rate specified in the inputs "StepsPerSecond" and "StepWidth".
Positive values have to be specified for the input values of the time intervals
("AdjTimeIntervals"). The scaling factors can also contain negative values.
The variable to be affected can only be set to the specified preset value if it is
in the valid range specified by "HighLimit" and "LowLimit".
The "InOperation" output signals that the function block is operating. How‐
ever, there is no adjustment. The "Changing" output indicates that the adjust‐
ment was processed without errors. The value of the adjusted variable "Value"
is valid.
The "Error" output indicates if an error occurs during the adjustment. For
detailed information on the error, refer to the "ErrorIdent" structure.

Troubleshooting
The function block generates the following error messages in Addi‐
tional1/Additional2 of the table CXA_TABLE, 16#0001:
Additional2 contains the target-dependent value CXA_PLC_DETAIL‐
DIAG_ERROR in the upper word, e.g. 16#0C230000 for die ctrlX CORE or
16#01230000 for the ctrlX DRIVE Technology Function.

Table 990: Error codes of the IL_ContinuousAdjustType01 function block
ErrorID           Additional1              Additional2                       Description
INPUT_RANGE_ERROR 16#A0F00100              CXA_PLC_DETAILDIAG_ERROR          Inputs are not in the
                                           + 16#00000001                     valid range
STATE_MACHINE_ERROR16#A0F00100             CXA_PLC_DETAILDIAG_ERROR          Invalid function block
                                           + 16#00000011                     state

                                              Jogging variables (adjustment)      1344

### 36.2.3 IL_ContinuousAdjustType02

        Brief description
        The IL_ContinuousAdjustType02 function block allows a continuous adjust‐
        ment of a DINT variable to be affected via binary inputs.

        Table 991: Reference table of the IL_ContinuousAdjustType02
        Library
        CXA_Utilities

        Interface description

Table 992: Interface variables of the IL_ContinuousAdjustType02 function block
I/O type       Name                    Data type         Description
VAR_INPUT      Enable                  BOOL              Enabling the function block (cyclic, state-
                                                         controlled)
               Inc                     BOOL              Increase affected variable
               Dec                     BOOL              Decrease affected variable
               Preset                  BOOL              Set the preset value (PresetValue)
               PresetValue             DINT              Specified value for the preset value
               ModuloValue             DINT              Modulo value (if 0, then absolute proc‐
                                                         essing)
               HighLimit               DINT              Maximum output value of the variable to be
                                                         affected
               LowLimit                DINT              Minimum output value of the variable to be
                                                         affected
               StepWidth               REAL              Step width
               StepsPerSecond          REAL              Steps per second
               AdjTimeIntervals        ARRAY [1..4] OF   Time intervals in seconds to scale the
                                       REAL              change rate
               AdjWeightFactors        ARRAY [1..5] OF   Scaling factors of the change rate
                                       REAL
VAR_OUTPUT InOperation                 BOOL              Function block enabled. The outputs High‐
                                                         LimitActive and LowLimitActive are valid
               Error                   BOOL              Calculation of the variable "Value" to be
                                                         affected was completed with an error. The
                                                         output variable "ErrorIdent" is valid

1146 /     ctrlX PLC Engineering
1344       Jogging variables (adjustment)

I/O type           Name               Data type           Description
ErrorID            ⮫ ERROR_CODE        Brief error description
ErrorIdent         ⮫ ERROR_STRUCT Detailed description of the diagnostics in
                             the event of an error
                                  ⮫ Troubleshooting on page 1147
PresetAck          BOOL                The value of the "PresetValue" input was
                                  applied
Changing           BOOL                The variable to be affected was calculated.
                                  The output variable "Value” is valid
HighLimitActive    BOOL                Maximum output value of the variable to be
                                  affected was reached
LowLimitActive     BOOL                Minimum output value of the variable to be
                                  affected was reached
VAR_IN_OUT         Value              DINT                Variable to be affected

Signal-time diagram

Functional description
The affected variable "Value" can be adjusted either in positive or negative
direction. A valid range is specified to affect the variable using the limit
values. The modulo value specification allows the adjustment in the reference
system of the axis. Specify the step width and the number of steps per
second to determine the change rate of the affected variable. Additionally,
a specified value (PresetValue) in the permissible operating range can be
directly written to the affected variable.
After processing enabled via "Enable, the variable to be affected can be
changed via the inputs "Inc" (in positive direction) and "Dec" (in negative
direction). As long the “Inc” input or the “Dec” input is set, the adjustable
variable can be continuously increased or decreased (“StepsPerSecond” *
“StepWidth”).
When initializing the function block, ensure that the input variables "Modulo‐
Value", "HighLimit" and "LowLimit" are provided with valid values.
Specify the scaling factors ("AdjWeightFactors[ ]") and their respective time
intervals ("AdjTimeIntervals[ ]") to modify the change rate with regard to time.
The scaling factors and the time intervals have to be set in addition to the
inputs "StepsPerSecond" and "StepWidth". Depending on the current time
interval, the change rate is multiplied with the respective scaling factor. The
figure below shows the behavior of the function block using an example
configuration: The "AdjTimeIntervals" input variables ([T1; T2; T3; T4]) are
specified in seconds. T5 is the time interval between the completion of the
time interval T4 and the adjustment abort. The "AdjWeightFactors" input var‐

                                         Jogging variables (adjustment)        1344

iables ([0.5; 1; 1.5; 2; 4]) determine the scaling of the change rate. The
last "AdjWeightFactors" value ("AdjWeightFactors [5])" is assigned to the time
interval T5.

If a time interval of 0 is selected, the following scaling factor is retained until
the adjustment is aborted.
Example:
If "AdjTimeIntervals[2]" = 0, the scaling factor of "AdjWeightFactors[3]" is
retained until the process is aborted.
The calculation of the elapsed time to define the correct time interval of the
scaling factors is reset with each new adjustment. If the inputs "AdjWeightFac‐
tors" and "AdjTimeIntervals" are not set, it is continuously adjusted with the
change rate specified in the inputs "StepsPerSecond" and "StepWidth".
Positive values have to be specified for the input values of the time intervals
(AdjTimeIntervals). The scaling factors can also contain negative values.
The variable to be affected can only be set to the specified preset value if it is
in the valid range specified by "HighLimit" and "LowLimit".
The "InOperation" output signals that the function block is operating. How‐
ever, there is no adjustment. The "Changing" output indicates that the adjust‐
ment was processed without errors. The value of the adjusted variable "Value"
is valid.
The "Error" output indicates if an error occurs during the adjustment. For
detailed information on the error, refer to the "ErrorIdent" structure.

Troubleshooting
The function block generates the following error messages in Addi‐
tional1/Additional2 of the table CXA_TABLE, 16#0001:
Additional2 contains the target-dependent value CXA_PLC_DETAIL‐
DIAG_ERROR in the upper word, e.g. 16#0C230000 for die ctrlX CORE or
16#01230000 for the ctrlX DRIVE Technology Function.
Table 993: Error codes of the IL_ContinuousAdjustType02
ErrorID                      Additional1       Additional2                Description
INPUT_RANGE_ERROR            16#A0F00100       CXA_PLC_DETAILDIAG_ERROR + Inputs are not in
                                               16#00000001                the valid range

1148 /    ctrlX PLC Engineering
1344      Jogging variables (adjustment)

ErrorID                           Additional1          Additional2                Description
STATE_MACHINE_ERROR               16#A0F00100          CXA_PLC_DETAILDIAG_ERROR + Invalid function
                                    16#00000011                block state

### 36.2.4 IL_IncrementalAdjustType01

        Brief description
        The IL_IncrementalAdjustType01 function block allows an incremental adjust‐
        ment of a REAL variable via binary inputs.

        Table 994: Reference table of the IL_IncrementalAdjustType01 function block
        Library
        CXA_Utilities

        Interface description

Table 995: Interface variables of the IL_IncrementalAdjustType01 function block
I/O type           Name                    Data type           Description
VAR_INPUT          Enable                  BOOL                Enabling the function block (cyclic, state-
                                                               controlled)
                   Inc                     BOOL                Increase affected variable
                   Dec                     BOOL                Decrease affected variable
                   Preset                  BOOL                Set the preset value (PresetValue)
                   PresetValue             REAL                Specified value for the preset value
                   ModuloValue             REAL                Modulo value for rotary calculation
                   HighLimit               REAL                Maximum output value of the variable to be
                                                               affected
                   LowLimit                REAL                Minimum output value of the variable to be
                                                               affected
           StepWidth                       REAL                Step width
           StepsPerSecond                  REAL                Steps per second
VAR_OUTPUT InOperation                     BOOL                Function block enabled. The outputs "High‐
                                                               LimitActive" and "LowLimitActive" are valid
                   Error                   BOOL                Calculation of the variable "Value" to be
                                                               affected was completed with an error. The
                                                               output variable "ErrorIdent" is valid
                   ErrorID                 ⮫ ERROR_CODE        Brief error description

                                        Jogging variables (adjustment)        1344

I/O type       Name                 Data type      Description
ErrorIdent           ⮫ ERROR_STRUCT Detailed  description of the diagnostics in
                              the event of an error
PresetAck            BOOL           The value of the "PresetValue" input was
                              applied
Changing             BOOL           The variable to be affected was calculated.
                              Output variable "Value" is valid
HighLimitActive      BOOL           Maximum output value of the variable to be
                              affected was reached
LowLimitActive       BOOL           Minimum output value of the variable to be
                              affected was reached

VAR_IN_OUT     Value                REAL           Variable to be affected

Signal-time diagram

Functional description
The affected variable "Value" can be adjusted either in positive or negative
direction. A valid range is specified to affect the variable using the limit
values. The modulo value specification allows the adjustment in the reference
system of the axis. Specify the step width and the number of steps per
second to determine the change rate of the affected variable. Additionally,
a specified value ("PresetValue") in the permissible operating range can be
directly written to the affected variable.
After processing enabled via "Enable, the variable to be affected can be
changed via the inputs "Inc" (in positive direction) and "Dec" (in negative
direction). As long the “Inc” input or the “Dec” input is set, the adjustable
variable can be continuously increased or decreased (“StepsPerSecond” *
“StepWidth”).
The variable to be affected can only be set to the specified preset value if it is
in the valid range specified by "HighLimit" and "LowLimit".
The "InOperation" output signals that the function block is operating. How‐
ever, there is no adjustment. The "Changing" output indicates that the adjust‐
ment was processed without errors. The value of the adjusted variable "Value"
is valid.
If an error occurs during the function block processing, this is signaled by
the output "Error" = TRUE. For detailed information on the error, refer to the
"ErrorIdent" output structure.

1150 /    ctrlX PLC Engineering
1344      Basic classes for the function block development (Base FB)

Troubleshooting
The function block generates the following error messages in Addi‐
tional1/Additional2 of the table CXA_TABLE, 16#0001:
Additional2 contains the target-dependent value CXA_PLC_DETAIL‐
DIAG_ERROR in the upper word, e.g. 16#0C230000 for die ctrlX CORE or
16#01230000 for the ctrlX DRIVE Technology Function.

Table 996: Error codes of the IL_IncrementalAdjustType01
ErrorID                     Additional1     Additional2                          Description
INPUT_RANGE_ERROR           16#A0F00100     CXA_PLC_DETAILDIAG_ERROR +           Inputs are not in
                                            16#00000001                          the valid range
STATE_MACHINE_ERROR         16#A0F00100     CXA_PLC_DETAILDIAG_ERROR +           Invalid function
                                            16#00000011                          block state

## 36.3 Basic classes for the function block development (Base

FB)

### 36.3.1 Introduction and overview

Table 997: Areas of application and functions/function blocks of CXA_Utilities
Area of application (folder in library)
Function blocks                                  Description
Basic classes for the function block development (Base FB)
⮫ Chapter 36.3.2 IL_EnableDoneBase               Implements the interface of a function block
on page 1155                                     with an "Enable" input and "Done", "Active" and
                                                 "Standard" error outputs
⮫ Chapter 36.3.3 IL_EnableInOpBase               Implements the interface of a function block
on page 1158                                     with an "Enable" input and "InOperation" and
                                                 "Standard" error outputs
⮫ Chapter 36.3.4 IL_EnableInOpShutdownBase Implements the interface of a function block
on page 1161                                     with an "Enable" input and "InOperation", "Shut‐
                                                 down" and "Standard" error outputs.
⮫ Chapter 36.3.5 IL_ExecuteDoneBase              Implements the interface of a function block
on page 1165                                     with an "Execute" input and "Done", "Active" and
                                                 "Standard" error outputs
⮫ Chapter 36.3.6 IL_ExecuteInOpBase              Implements the interface of a function block
on page 1167                                     with an "Execute" input and "InOperation",
                                                 "Active" and "Standard" error outputs
⮫ Chapter 36.3.7 IL_ExecuteDoneAbortedBase       Implements the interface of a function block
on page 1170                                     with an "Execute" input and "Done", “Active”,
                                                 “CommandAborted” and "Standard" error out‐
                                                 puts
⮫ Chapter 36.3.8 IL_ExecuteDoneAbortedShut‐ Implements the interface of a function block
downBase on page 1173                            with an "Execute" input and "Done", “Active”,
                                                 “Shutdown“, CommandAborted” and "Standard"
                                                 error outputs
                     The basic function blocks
                     ● IL_EnableDoneBase
                     ● IL_EnableInOpBase
                     ● IL_EnableInOpShutdownBase

● IL_ExecuteDoneBase

          Basic classes for the function block development (Base FB)         1344

● IL_ExecuteInOpBase
● IL_ExecuteDoneAbortedBase
● IL_ExecuteDoneAbortedShutdownBase
facilitate the development of function blocks. They implement the basic struc‐
ture of the function block and the behavior of the standard inputs and out‐
puts.
A state machine is specified for each of the two function block types which
updates the standard inputs and outputs. The user code can be added to the
respective state machine by implementing namely specified methods. Auxiliary
methods are implemented facilitating the setting of error codes.
To use a basic function block, it has to be referenced via the keyword
“EXTENDS” when defining the own function block. This procedure is also

called “deriving a function block”. The user-specific function block then con‐
tains the inputs and outputs of the basic function block and, subsequently,
all inputs and outputs of the user-specific function block. All methods imple‐
mented in the basic function block can be used in the own (derived) function
block. This is also called inheritance of methods.

Methods that can be overwritten
The basic function blocks define their own methods called by the internal
state machine. These methods can be redefined to implement a user-specific
functionality. This is also called overwriting of methods.
All methods of the basic function blocks that can be overwritten, are listed in
the following.
Method                            Description
mReset()                          This method allows resetting of internal function blocks and
              self-defined outputs.
              It is called upon transition to the STATE_IDLE state. The out‐
              puts “Active", "InOperation" and "Error" are reset internally.
              This method is to be implemented optionally.
mInit(Reset: BOOL): BOOL          Using this method, the preparations for the actual task of the
              function block are implemented.
              This method is called in or at the transition to the STATE_INIT
              state. "Reset" is TRUE during transition. The function block
              is initialized in mInit(). Until the initialization is completed,
              mInit() has to return TRUE. Once initialization is completed,
              mInit() has to return with FALSE. A subordinate state machine
              can be implemented in mInit().
              This method is to be implemented optionally.
mInOp(Reset: BOOL): BOOL          The actual task of the function block is implemented in this
              method.
              This method is called in or at the transition to the
              STATE_INOP state. Argument "Reset" is TRUE during transition
              into STATE_INOP.
              For a function block with an "Execute" input, mInOp(FALSE) is
              called until FALSE is returned. Subsequently, STATE_DONE is
              automatically enabled if the function block is a derivation of a
              function block with a "Done" output.
mError()                          If an error occurs, this method is called by mSetError().
              Boolean outputs can be reset here. "Active", "InOperation" and
              the error outputs are already provided by mSetError().
              This method is to be implemented optionally.

1152 /    ctrlX PLC Engineering
1344      Basic classes for the function block development (Base FB)

Method                       Description
mIdle()                      This method is called in the states STATE_IDLE, STATE_INIT and
        STATE_DONE and STATE_ERROR, but not in the STATE_INOP
        state.
        Function blocks provided with a continuous time measurement
        always have to be called. They can be called here.
mShutdown(Reset: BOOL): BOOL Using this method, the end process of the function block is
        implemented.
        This method is called in or at the transition to the
        STATE_SHUTDOWN or STATE_ERROR state. The argument
        "Reset" is TRUE during the transition.
        As long as the end process is not completed, mShutdown() has
        to be called and TRUE returned.
        Once the end process is completed, mShutdown() has to
        return FALSE.

Auxiliary functions
Auxiliary functions are methods that are provided by the basic function blocks
and can be used in user-specific implementations. They may not be over‐
written by user-specific implementations. Presently, two methods are imple‐
mented to set the error state.

Method                              Description
mSetError(enErrorID:                This method sets the specified error code at the outputs
ERROR_CODE,                         "ErrorID" and "ErrorIdent" and activates the output "Error".
enTable: ERROR_TABLE,               Subsequently, mError() is called. The function block changes
               to STATE_ERROR.
dwAdditional1: DWORD,
               After calling mSetError(), a return jump should be performed
dwAdditional2: DWORD)
               using RETURN to impede further code processing after an error.
mSetErrorIdent(enErrorID:           This method sets the specified error code at the outputs
ERROR_CODE,                         "ErrorID" and "ErrorIdent" and activates the output "Error".
stErrorIdent: ERROR_STRUCT)         Subsequently, mError() is called. The function block changes to
               STATE_ERROR. This function is suitable for applying the error
               code from another function block.
               After calling mSetErrorIdent(), a return jump should be per‐
               formed using RETURN to impede further code processing after
               an error.
mSetErrorCode(enErrorID:            This method generates a PLC error with the specified library
ERROR_CODE,                         error code in the main diagnostics ("Additional1") and the error
wLibraryCode: WORD,                 code in the detailed diagnostics ("Additional2").
wErrorCode: WORD)
mSetErrorCode64(enErrorID:          This method sets the error code transferred from a subordi‐
ERROR_CODE,                         nate firmware function. The main diagnostics is stored in "Addi‐
lwErrorCode: LWORD)                 tional1". The detailed diagnostics is stored in "Additional2".
mSetCommandAborted()                This method is only available for the basic function block
               IL_ExecuteDoneAbortedBase. Calling this method sets the
               "CommandAborted" output and switches the function blocks to
               the "CommandAborted" state.

          Basic classes for the function block development (Base FB)       1344

Using the basic function blocks
Basic function blocks can be extended to derive user-specific function blocks.
Therefore, the "Extended:" checkbox has to be selected and the basic function
block has to be entered into the text box when the new function block is
created.

Inheritance is the basic principle. The new function block contains all varia‐
bles and methods already implemented in the basic function block. User-spe‐
cific functionality can be added by re-implementing existing methods. The
newly declared inputs and outputs in the function block derived from the
basic block are displayed below the interfaces already defined in the basic
function block. It is therefore only necessary to define the new inputs and
outputs.
It is mandatory to call "FB_Main()" in the implementation section of the
derived function block. Other implementations are not allowed at this point.

1154 /    ctrlX PLC Engineering
1344      Basic classes for the function block development (Base FB)

block IL_EnableInOpBase
Interface of the created function block:

The actual function is implemented in the rewritable methods "mInit()" and
"mInOp()". Methods that are not required, do not have to be implemented.
The following figure shows the implementation of mInit() method. The state
machine shown in the example is optional.

          Basic classes for the function block development (Base FB)       1344

### 36.3.2 IL_EnableDoneBase

Brief description
This basic function block (basic class) implements the interface of a function
block with "Enable" input and "Done" and "Active" outputs. In addition, the
default error outputs are created. The function block implements a state
machine that is suitable for the default inputs and outputs.
Function blocks of this type are mainly used for cyclic processes, such as the
cyclic polling of an external device.
This function block serves as a basic class for user-specific implementations.
It has to be implemented using the keyword "EXTENDS".

1156 /    ctrlX PLC Engineering
1344      Basic classes for the function block development (Base FB)

Interface description

Table 998: Interface variables of the IL_EnableDoneBase function block
           Name                     Type          Comment
VAR_INPUT  Enable                   BOOL          Processing enabled (cyclic, state-controlled)
VAR_OUTPUT Done                     BOOL          The function block has output a result
           Active                   BOOL          The function block is active
           Error                    BOOL          Indicates that an error occurred
           ErrorID                  ⮫ ERROR_CODE Error cause
                   ErrorIdent       ⮫ ERROR_STRUC Detailed error cause
                                    T

Functional description
This basic class implements the interface of a function block with "Enable"
input and "Done" and "Active" outputs. In addition, the default error outputs
are created. The function block implements a state machine that is suitable
for the default inputs and outputs.
This function block serves as a basic class for user-specific implementations.
It has to be implemented using the keyword "EXTENDS".
Function blocks with Enable input are mainly used for tasks that are cyclically
repeated.
This basic function block implements the "Enable" input and the "Done",
"Active", "Error", "ErrorID" and "ErrorIdent" outputs. Processing starts at a
rising edge at "Enable" and runs after the initialization phase until either
"Enable" is reset or an error occurs. After the initialization phase, "Active" is
set to indicate that the function block is performing its task. After completion
of the task, "Done" is set for one cycle. Subsequently, a new processing proce‐
dure is started.

          Basic classes for the function block development (Base FB)        1344

output
Function blocks of this type have five internal states (see also ⮫ Chapter
36.3.9 IL_FB_STATES on page 1178 ):
STATE_IDLE         This state represents the starting state of the function
                   block. It is activated when "Enable" is FALSE. mReset()
                   is executed at the beginning of the state. mIdle() is exe‐
                   cuted in the state.
                   If "Enable" is set, the STATE_INIT state is entered.

STATE_INIT         This state is used to start the function block. It
                   runs through before the actual cyclic operation. When
                   the state is entered, mInit(Reset:=TRUE) is called.
                   mInit(Reset:=FALSE) and mIdle() are called in the state.
                   If mInit() returns False, it is changed to STATE_INOP. If
                   mSetError() or mSetErrorIdent() are called, it is changed
                   to STATE_ERROR. If “Enable” is reset, it is changed to
                   STATE_IDLE.

STATE_INOP         The cyclic task is performed here. The "Active" output
                   is TRUE as long as this state is active. When
                   the state is entered, mInOp(Reset:=TRUE) is called.
                   mInOp(Reset:=FALSE) is called in the state.
                   If mSetError() or mSetErrorIdent() is called, it is changed
                   to STATE_ERROR. If “Enable” is reset, it is changed to
                   STATE_IDLE.

1158 /    ctrlX PLC Engineering
1344      Basic classes for the function block development (Base FB)

 STATE_DONE            State active after successful task processing. It is left after
                       another cycle. Subsequently, STATE_INOP will become
                       active again.

 STATE_ERROR           This is the error state of the function block. Error output
                       "Error" is active in this state and the error code is dis‐
                       played at "ErrorID" or "ErrorIdent". When the state is
                       entered, mError() is called. mIdle() is called in the state.
                       If "Enable" is reset, the STATE_IDLE state is entered.

 Signal-time diagram
 The following time response results from the state machine described above:

 Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:
Additional2 contains the target-dependent value CXA_PLC_DETAIL‐
DIAG_ERROR in the upper word, e.g. 16#0C230000 for die ctrlX CORE or
16#01230000 for the ctrlX DRIVE Technology Function.
Table 999: Error codes of the IL_EnableDoneBase
ErrorID                    Additional1         Additional2                Description
STATE_MACHINE_ERROR        16#A0F00100         CXA_PLC_DETAILDIAG_ERROR + Invalid state of the
                                               16#00000011                state machine

### 36.3.3 IL_EnableInOpBase

 Brief description
 This basic function block (basic class) implements the interface of a function
 block with "Enable" input and "InOperation" output. In addition, the default
 error outputs are created. The function block implements a state machine that
 is suitable for the default inputs and outputs.
 Function blocks of this type are mainly used for continuous processes, such
 as controllers.
 This function block serves as a basic class for user-specific implementations.
 It has to be implemented using the keyword "EXTENDS".

          Basic classes for the function block development (Base FB)         1344

Interface description

Table 1000: Interface variables of the IL_EnableInOpBase function block
           Name                  Type          Comment

VAR_INPUT  Enable                BOOL          Processing enabled (cyclic, state-controlled)
VAR_OUTPUT InOperation           BOOL          The function blocks is busy with its actual task
Error                 BOOL          Indicates that an error occurred
ErrorID               ⮫ ERROR_CODE Error cause
ErrorIdent        ⮫ ERROR_STRUC Detailed error cause
            T

Functional description
This basic class implements the interface of a function block with "Enable"
input and "InOperation" output. In addition, the default error outputs are
created. The function block implements a state machine that is suitable for
the default inputs and outputs.
This function block serves as a basic class for user-specific implementations.
It has to be implemented using the keyword "EXTENDS".
This basic function block implements the "Enable" input and the "InOpera‐
tion", "Error", "ErrorID" and "ErrorIdent" outputs. Processing starts at a rising
edge at "Enable" and runs after the initialization phase until either "Enable" is
reset or an error occurs. After the initialization phase, "InOperation" is set to
indicate that the function block performs its cyclic task.
Function blocks with an “Enable” input and “InOperation” output are pref‐
erably used in cyclical, repeating tasks, e.g. closed-loop control.

output
Function blocks of this type have four internal states (see also ⮫ Chapter
36.3.9 IL_FB_STATES on page 1178):

1160 /    ctrlX PLC Engineering
1344      Basic classes for the function block development (Base FB)

STATE_IDLE            This state represents the starting state of the function
                      block. It is activated when "Enable" is FALSE. mReset()
                      is executed at the beginning of the state. mIdle() is exe‐
                      cuted in the state.
                      If "Enable" is set, the STATE_INIT state is entered.

STATE_INIT            This state is used to start the function block. It
                      runs through before the actual cyclic operation. When
                      the state is entered, mInit(Reset:=TRUE) is called.
                      mInit(Reset:=FALSE) and mIdle() are called in the state.
                      If mInit() returns False, it is changed to STATE_INOP. If
                      mSetError() or mSetErrorIdent() are called, it is changed
                      to STATE_ERROR. If “Enable” is reset, it is changed to
                      STATE_IDLE.

STATE_INOP            The cyclic task is performed here. The "InOperation"
                      output is TRUE as long as this state is active. When
                      the state is entered, mInOp(Reset:=TRUE) is called.
                      mInOp(Reset:=FALSE) is called in the state.
                      If mSetError() or mSetErrorIdent() is called, it is changed
                      to STATE_ERROR. If “Enable” is reset, it is changed to
                      STATE_IDLE.

STATE_ERROR           This is the error state of the function block. Error output
                      "Error" is active in this state and the error code is dis‐
                      played at "ErrorID" or "ErrorIdent". When the state is
                      entered, mError() is called. mIdle() is called in the state.
                      If "Enable" is reset, the STATE_IDLE state is entered.

Signal-time diagram
The following time response results from the state machine described above:

Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:
Additional2 contains the target-dependent value CXA_PLC_DETAIL‐
DIAG_ERROR in the upper word, e.g. 16#0C230000 for die ctrlX CORE or
16#01230000 for the ctrlX DRIVE Technology Function.

          Basic classes for the function block development (Base FB)         1344

Table 1001: Error codes of the IL_EnableInOpBase
ErrorID                      Additional1      Additional2                       Description
STATE_MACHINE_ERROR          16#A0F00100      CXA_PLC_DETAILDIAG_ERROR +        Invalid state of the
                                              16#00000011                       state machine

### 36.3.4 IL_EnableInOpShutdownBase

Brief description
This basic function block (basic class) implements the interface of a function
block with the "Enable" input and the "InOperation" and “Shutdown” outputs
In addition, the default error outputs are created. The function block imple‐
ments a state machine that is suitable for the default inputs and outputs.

Function blocks of this type are mainly used for continuous processes, such
as controllers.
This function block serves as a basic class for user-specific implementations.
It has to be implemented using the keyword "EXTENDS".

Interface description

Table 1002: Interface variables of the IL_EnableInOpShutdownBase function block
           Name                  Type          Comment
VAR_INPUT  Enable                BOOL          Processing enabled (cyclic, state-controlled)
VAR_OUTPUT InOperation           BOOL          The function blocks is busy with its actual task
           Shutdown              BOOL          Indicates that the function block is currently in
                                               a defined final state
               Error             BOOL          Indicates that an error occurred
               ErrorID           ⮫ ERROR_CODE Error cause
               ErrorIdent        ⮫ ERROR_STRUC Detailed error cause
                                 T

Functional description
This basic class implements the interface of a function block with the
"Enable" input and the "InOperation" and “Shutdown” outputs In addition,
the default error outputs are created. The function block implements a state
machine that is suitable for the default inputs and outputs.
This function block serves as a basic class for user-specific implementations.
It has to be implemented using the keyword "EXTENDS".
This basic function block implements the "Enable" input and the "InOpera‐
tion", "Shutdown", "Error", "ErrorID" and "ErrorIdent" outputs.
Processing starts at a rising edge at "Enable" and runs after the initialization
phase until either "Enable" is reset or an error occurs. After the initialization
phase, "InOperation" is set to indicate that the function block performs its
cyclic task.

1162 /    ctrlX PLC Engineering
1344      Basic classes for the function block development (Base FB)

The “Shutdown” signals that the function block changes to the state “SHUT‐
DOWN”. When the “Shutdown” output is set, the function block has to be
called.
Function blocks with an “Enable” input and “InOperation” output are pref‐
erably used in cyclical, repeating tasks, e.g. closed-loop control.

InOperation/shutdown output
Red/top         State switching conditions
Green/bottom Called methods during state switching
Function blocks of this type have six internal states (see also ⮫ Chapter 36.3.9
IL_FB_STATES on page 1178):
STATE_IDLE          This state represents the starting state of the function
                    block. It is activated when "Enable" is FALSE. mReset()
                    is executed at the beginning of the state. mIdle() is exe‐
                    cuted in the state.
                    If "Enable" is set, the STATE_INIT state is entered.

STATE_INIT          This state is used to start the function block. It
                    runs through before the actual cyclic operation. When
                    the state is entered, mInit(Reset:=TRUE) is called.
                    mInit(Reset:=FALSE) and mIdle() are called in the state.
                    If mInit() returns False, it is changed to STATE_INOP. If
                    mSetError() or mSetErrorIdent() are called, it is changed
                    to STATE_ERROR. If “Enable” is reset, it is changed to
                    STATE_SHUTDOWN.

STATE_INOP          The cyclic task is performed here.
                    The "InOperation" output is TRUE as long as this state is
                    active. When the state is entered, mInOp(Reset:=TRUE) is
                    called. mInOp(Reset:=FALSE) is called in the state.
                    If mSetError() or mSetErrorIdent() is called, it is changed
                    to STATE_ERROR. If “Enable” is reset, it is changed to
                    STATE_SHUTDOWN.

Basic classes for the function block development (Base FB)           1344

STATE_SHUT‐           This is the final state of the function block.
DOWN                  The "Shutdown" output is TRUE as long as this state is
active.
mShutDown(Reset:=TRUE) is called upon entry in the
state. mShutDown(Reset:=FALSE) is called in the state.
If mShutDown() is False, the STATE_IDLE state is entered.
STATE_ERROR           This is the error state of the function block.
Error output "Error" is active in this state and the error
code is displayed at "ErrorID" or "ErrorIdent".
The shutdown process is executed in this state. mError()
and mShutDown(Reset := TRUE) is called upon entry in

the state. mIdle() and mShutDown(Reset := FALSE) is
called in the state. As long as mShutDown() returns
"TRUE", the output "Shutdown" remains "TRUE".
If an error occurs during the shutdown process, the shut‐
down process is canceled and the "ShutDown" output is
reset.
If "Enable" is reset, the STATE_ERROR_SHUTDOWN state
is entered.
STATE_ERROR_          The prerequisite to enter this state is that the previous
SHUTDOWN              state was "STATE_ERROR" and a falling edge at "Enable".
If the shutdown is not yet completed, the program
remains in this state and is called with mShutDown
(reset := FALSE).
The "ShutDown" output is "TRUE" as long as this state is
active.
If mShutDown() is False, the STATE_IDLE state is entered.
If an error occurs during the shutdown operation, the
operation is canceled.
The "Error" output is set for one cycle. The "Shut‐
Down" output is reset. The state machine changes to
STATE_IDLE.
If it was already shut down in STATE_ERROR, mShut‐
Down() is not called in this state. It is immediately
changed to STATE_IDLE.

Signal-time diagram
The following time response results from the state machine described above:

1164 /    ctrlX PLC Engineering
1344      Basic classes for the function block development (Base FB)

(I)

(II)

(III)

Error codes
The function block uses the error table CXA_TABLE, 16#0001. It can generate
the following error messages in Additional1/Additional2.
Additional2 contains the target-dependent value CXA_PLC_DETAIL‐
DIAG_ERROR in the upper word, e.g. 16#0C230000 for die ctrlX CORE or
16#01230000 for the ctrlX DRIVE Technology Function.

          Basic classes for the function block development (Base FB)         1344

Table 1003: Error codes of the IL_EnableInOpShutdownBase
ErrorID                      Additional1      Additional2                Description
STATE_MACHINE_ERROR          16#A0F00100      CXA_PLC_DETAILDIAG_ERROR + Invalid state of the
                                              16#00000011                state machine

### 36.3.5 IL_ExecuteDoneBase

Brief description
This basic function block (basic class) implements the interface of a function
block with “Execute" input and "Done" and "Active" outputs. In addition,
the default error outputs are created. The function block implements a state
machine that is suitable for the default inputs and outputs.

Function blocks of this type are used for nonrecurring tasks requiring a proc‐
essing time of multiple cycles. for example, the initialization of an external
hardware.
This function block serves as a basic class for user-specific implementations.
It has to be implemented using the keyword "EXTENDS".

Interface description

Table 1004: Interface variables of the IL_ExecuteDoneBase function block
           Name                  Type                  Comment
VAR_INPUT  Execute               BOOL                  Processing enabled (cyclic, edge-controlled)
VAR_OUTPUT Done                  BOOL                  Processing completed by the function block
                                                       without error
               Active            BOOL                  The function block was started
               Error             BOOL                  Indicates that an error occurred
               ErrorID           ⮫ ERROR_CODE          Error cause
               ErrorIdent        ⮫ ERROR_STRUCT        Detailed error cause

Functional description
This basic class implements the interface of a function block with “Execute"
input and "Done" and "Active" outputs. In addition, the default error outputs
are created. The function block implements a state machine that is suitable
for the default inputs and outputs.
This function block serves as a basic class for user-specific implementations.
It has to be implemented using the keyword "EXTENDS".
This basic function block implements the "Execute" input and the "Done",
"Active", "Error", "ErrorID" and "ErrorIdent" outputs.
Processing starts at a rising edge at "Execute" and runs after the initialization
phase until either STATE_DONE is reached or an error occurs.
A new rising edge at "Execute" causes a reset and a restart of the function
block.

1166 /    ctrlX PLC Engineering
1344      Basic classes for the function block development (Base FB)

Function blocks with an “Execute” input and a “Done” output are preferably
used in nonrecurring tasks with a defined conclusion, e.g., initialization of
external hardware.

well as Active outputs
Function blocks of this type have five internal states (see also ⮫ Chapter
36.3.9 IL_FB_STATES on page 1178 ):
STATE_IDLE         This state represents the starting state of the function
                   block. It is enabled if "Execute" is FALSE and if the func‐
                   tion block is either in STATE_DONE or STATE_ERROR.
                   mReset() is executed at the beginning of the state.
                   mIdle() is executed in the state.
                   If "Execute" is set, it is changed to STATE_INIT.

STATE_INIT         This state is used to start the function block. It
                   runs through before the actual cyclic operation. The
                   "Active" output is TRUE as long as this state is active.
                   When the state is entered, mInit(Reset:=TRUE) is called.
                   mInit(Reset:=FALSE) and mIdle() are called in the state.
                   If mInit() returns False, it is changed to STATE_INOP. If
                   either mSetError() or mSetErrorIdent() is called, it is
                   changed to STATE_ERROR.

           Basic classes for the function block development (Base FB)            1344

 STATE_INOP            The cyclic task is performed here. The "Active" output
                       is TRUE as long as this state is active. When
                       the state is entered, mInOp(Reset:=TRUE) is called.
                       mInOp(Reset:=FALSE) is called in the state.
                       If mInOp() returns FALSE, the task is completed and the
                       function block changes to the STATE_DONE state.
                       If mSetError() or mSetErrorIdent() is called, the
                       STATE_ERROR state is entered.

 STATE_DONE            State active after successful task processing. It is exited
                       if "Execute" is FALSE, but remains active for at least one
                       cycle. mIdle() is called in the state.

 STATE_ERROR           This is the error state of the function block. Error output
                       "Error" is active in this state and the error code is dis‐
                       played at "ErrorID" or "ErrorIdent". When the state is
                       entered, mError() is called. mIdle() is called in the state.
                       If "Execute" is reset, the STATE_IDLE state is entered.

 Signal-time diagram
 The following time response results from the state machine described above:

 Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:
Additional2 contains the target-dependent value CXA_PLC_DETAIL‐
DIAG_ERROR in the upper word, e.g. 16#0C230000 for die ctrlX CORE or
16#01230000 for the ctrlX DRIVE Technology Function.
Table 1005: Error codes of the IL_ExecuteDoneBase
ErrorID                      Additional1     Additional2                Description
STATE_MACHINE_ERROR          16#A0F00100     CXA_PLC_DETAILDIAG_ERROR + Invalid state of the
                                             16#00000011                state machine

### 36.3.6 IL_ExecuteInOpBase

 Brief description
 This basic function block (basic class) implements the interface of a function
 block with “Execute" input and “InOperation" and "Active" outputs. In addi‐
 tion, the default error outputs are created. The function block implements a
 state machine that is suitable for the default inputs and outputs.

1168 /    ctrlX PLC Engineering
1344      Basic classes for the function block development (Base FB)

Function blocks of this type are used for constant tasks without defined termi‐
nation.
This function block serves as a basic class for user-specific implementations.
It has to be implemented using the keyword "EXTENDS".

Interface description

Table 1006: Interface variables of the IL_ExecuteInOpBase function block
           Name                     Type                  Comment
VAR_INPUT  Execute                  BOOL                  Processing enabled (cyclic, edge-controlled)
VAR_OUTPUT InOperation              BOOL                  The function block processes its task
           Active                   BOOL                  The function block was started
           Error                    BOOL                  Indicates that an error occurred
           ErrorID                  ⮫ ERROR_CODE          Error cause
                   ErrorIdent       ⮫ ERROR_STRUCT        Detailed error cause

Functional description
This basic class implements the interface of a function block with “Execute"
input and “InOperation" and "Active" outputs. In addition, the default error
outputs are created. The function block implements a state machine that is
suitable for the default inputs and outputs.
This function block serves as a basic class for user-specific implementations.
It has to be implemented using the keyword "EXTENDS".
This basic function block implements the "Execute" input and the "InOpera‐
tion", "Active", "Error", "ErrorID" and "ErrorIdent" outputs. Processing starts
with a rising edge at "Execute" and runs after the initialization phase until an
error occurs. A new rising edge at "Execute" causes a reset and a restart of the
function block.
Function blocks with "Execute" input "InOperation" output are preferably used
for continuous tasks without defined completion such as closed-loop velocity
control.

          Basic classes for the function block development (Base FB)            1344

InOperation as well as Active outputs
Function blocks of this type have four internal states (see also ⮫ Chapter
36.3.9 IL_FB_STATES on page 1178):
STATE_IDLE            State represents the starting state of the function block. It
                      is enabled if "Execute" is FALSE and if the function block
                      is in STATE_DONE. mReset() is executed at the beginning
                      of the state. mIdle() is executed in the state.
                      If "Execute" is set, it is changed to STATE_INIT.

STATE_INIT            This state is used to start the function block. It
                      runs through before the actual cyclic operation. The
                      "Active" output is TRUE as long as this state is active.
                      When the state is entered, mInit(Reset:=TRUE) is called.
                      mInit(Reset:=FALSE) and mIdle() are called in the state.
                      If mInit() returns False, it is changed to STATE_INOP. If
                      either mSetError() or mSetErrorIdent() is called, it is
                      changed to STATE_ERROR.

STATE_INOP            The cyclic task is performed here. The "Active" output
                      is TRUE as long as this state is active. When
                      the state is entered, mInOp(Reset:=TRUE) is called.
                      mInOp(Reset:=FALSE) is called in the state.
                      If mSetError() or mSetErrorIdent() is called, the
                      STATE_ERROR state is entered.

STATE_ERROR           This is the error state of the function block. Error output
                      "Error" is active in this state and the error code is dis‐
                      played at "ErrorID" or "ErrorIdent". When the state is
                      entered, mError() is called. mIdle() is called in the state.
                      If "Execute" is reset, the STATE_IDLE state is entered.

Signal-time diagram
The following time response results from the state machine described above:

1170 /    ctrlX PLC Engineering
1344      Basic classes for the function block development (Base FB)

Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:
Additional2 contains the target-dependent value CXA_PLC_DETAIL‐
DIAG_ERROR in the upper word, e.g. 16#0C230000 for die ctrlX CORE or
16#01230000 for the ctrlX DRIVE Technology Function.
Table 1007: Error codes of the IL_ExecuteInOpBase
ErrorID             Additional1                   Additional2                    Description
STATE_MACHINE_ERROR 16#A0F00100                   CXA_PLC_DETAILDIAG_ERROR +     Invalid state of the
                                                  16#00000011                    state machine

### 36.3.7 IL_ExecuteDoneAbortedBase

Brief description
This basic class implements the interface of a function block with “Execute"
input and “Done”, "CommandAborted" and "Active" outputs. In addition, the
default error outputs are created. The function block implements a state
machine that is suitable for the default inputs and outputs.
Function blocks of this type are used for nonrecurring tasks requiring a proc‐
essing time of multiple cycles. for example, the initialization of an external
hardware.
This function block serves as a basic class for user-specific implementations.
It has to be implemented using the keyword "EXTENDS".

Interface description

Table 1008: Interface variables of the IL_ExecuteDoneAbortedBase function block
                   Name                    Type               Comment
VAR_INPUT          Execute                 BOOL               Processing enabled (cyclic, edge-con‐
                                                              trolled)

          Basic classes for the function block development (Base FB)        1344

Name                      Type                   Comment
VAR_OUTPUT Done                      BOOL                   Processing completed by the function
                                        block without error
Active                 BOOL                   The function block was started
CommandAborted         BOOL                   The processing was aborted by
                                        another function block
Error                  BOOL                   Indicates that an error occurred
ErrorID                ⮫ ERROR_CODE           Error cause
ErrorIdent             ⮫ ERROR_STRUCT         Detailed error cause

Functional description

This basic class implements the interface of a function block with “Execute"
input and “Done”, "CommandAborted" and "Active" outputs. In addition, the
default error outputs are created. The function block implements a state
machine that is suitable for the default inputs and outputs.
This function block serves as a basic class for user-specific implementations.
It has to be implemented using the keyword "EXTENDS".
Function blocks with an “Execute” input are preferably used in nonrecurring
tasks with a defined conclusion, e.g., initialization of external hardware. This
basic function block implements the "Execute" input and the "Done", "Active",
"Error", "ErrorID" and "ErrorIdent" outputs. Processing starts at a rising edge
at "Execute" and runs after the initialization phase until either STATE_DONE
is reached, an error occurs or the processing is aborted by another function
block.

outputs "Done", "CommandAborted" as well as "Active"
Function blocks of this type have six internal states (see also ⮫ Chapter 36.3.9
IL_FB_STATES on page 1178):

1172 /    ctrlX PLC Engineering
1344      Basic classes for the function block development (Base FB)

STATE_IDLE            State represents the starting state of the function block.
It is enabled if "Execute" is FALSE and if the function
block is either in STATE_DONE or STATE_ERROR. mReset()
is executed at the beginning of the state. mIdle() is exe‐
cuted in the state.
If "Execute" is set, it is changed to STATE_INIT.

STATE_INIT            This state is used to start the function block. It
runs through before the actual cyclic operation. The
"Active" output is TRUE as long as this state is active.
When the state is entered, mInit(Reset:=TRUE) is called.
mInit(Reset:=FALSE) and mIndle() are called in the state.
If mInit() returns False, it is changed to STATE_INOP. If
mSetError() or mSetErrorIdent() are called, it is changed
to STATE_ERROR. If “Execute” is reset, it is changed to
STATE_IDLE.

STATE_INOP            The cyclic task is performed here. The "Active" output
is TRUE as long as this state is active. When
the state is entered, mInOp(Reset:=TRUE) is called.
mInOp(Reset:=FALSE) is called in the state.
If mInOp() returns FALSE, the task is completed and the
function block changes to the STATE_DONE state.
If mSetError() or mSetErrorIdent() is called, the
STATE_ERROR state is entered.

STATE_DONE            State active after successful task processing. It is exited
if "Execute" is FALSE, but remains active for at least one
cycle. mIdle() is called in the state.

STATE_COAB            State becomes active after the auxiliary method "mSet‐
CommandAborted" was completely processed. It is exited
if "Execute" is FALSE, but remains active for at least one
cycle. mIdle() is called in the state.

STATE_ERROR           This is the error state of the function block. Error output
"Error" is active in this state and the error code is dis‐
played at "ErrorID" or "ErrorIdent". When the state is
entered, mError() is called. mIdle() is called in the state.
If "Execute" is reset, the STATE_IDLE state is entered.

Signal-time diagram
The following time response results from the state machine described above:

           Basic classes for the function block development (Base FB)       1344

 IL_ExecuteDoneAbortedBase

 Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:
Additional2 contains the target-dependent value CXA_PLC_DETAIL‐
DIAG_ERROR in the upper word, e.g. 16#0C230000 for die ctrlX CORE or
16#01230000 for the ctrlX DRIVE Technology Function.
Table 1009: Error codes of the IL_ExecuteDoneAbortedBase
ErrorID                      Additional1     Additional2                Description
STATE_MACHINE_ERROR          16#A0F00100     CXA_PLC_DETAILDIAG_ERROR + Invalid state of the
                                             16#00000011                state machine

### 36.3.8 IL_ExecuteDoneAbortedShutdownBase

 Brief description
 This basic function block (basic class) implements the interface of a function
 block with the "Execute" input and the "Done", "Active", "Shutdown" and
 "CommandAborted" outputs. In addition, the default error outputs are cre‐
 ated. The function block implements a state machine suitable for the default
 inputs and outputs.
 Function blocks of this type are used for nonrecurring tasks requiring a proc‐
 essing time of multiple cycles. for example, the initialization of an external
 hardware.
 This function block serves as a basic class for user-specific implementations.
 It has to be implemented using the keyword "EXTENDS".

 Interface description

Table 1010: Interface variables of the IL_ExecuteDoneAbortedShutdownBase function block
               Name                 Type                  Comment
VAR_INPUT      Execute              BOOL                  Processing enabled (cyclic, edge-con‐
                                                          trolled)

1174 /    ctrlX PLC Engineering
1344      Basic classes for the function block development (Base FB)

Name                        Type                   Comment
VAR_OUTPUT Done                        BOOL                   Processing completed by the function
                                           block without error
Active              BOOL                   The function block was started
Shutdown            BOOL                   Processing is completed.
                                           It was either aborted by the user
                                           (mAbort()) or due to an error (mSe‐
                                           tError() or mSetErrorIdent()). However,
                                           the function block has to successfully
                                           complete its activities
CommandAborted      BOOL                   The processing was aborted by another
                                           function block
Error               BOOL                   Indicates that an error occurred
ErrorID             ⮫ ERROR_CODE           Error cause
ErrorIdent          ⮫ ERROR_STRUCT         Detailed error cause

     Functional description
     This basic class implements the interface of a function block with the "Exe‐
     cute" input and the "Done", "Active", "Shutdown" and "CommandAborted" out‐
     puts. In addition, the default error outputs are created.
     The function block implements a state machine suitable for the default inputs
     and outputs.
     This function block serves as a basic class for user-specific implementations.
     It has to be implemented using the keyword "EXTENDS".
     Processing starts at a rising edge at "Execute" and runs after the initialization
     phase until either STATE_DONE is reached, an error occurs or the processing
     is aborted by another function block.

  Basic classes for the function block development (Base FB)           1344

and “CommandAborted” outputs.
Function blocks of this type are provided with seven internal states (see also
⮫ Chapter 36.3.9 IL_FB_STATES on page 1178):
STATE_IDLE                   This state represents the starting state of the function block.
It is active upon first call and it is enabled if "Execute" is set
to FALSE and if the function block is in the states STATE_DONE,
STATE_ABORT_SHUTDOWN or STATE_ERROR_SHUTDOWN.
When the state is entered (again), mReset() is executed. mIdle() is
executed in the state.
If "Execute" is set, it is changed to STATE_INIT.

STATE_INIT                   This state is used to start the function block. It runs through before
the actual cyclic operation.
The "Active" output is TRUE as long as this state is active. When the
state is entered, mInit(Reset:=TRUE) is called. mInit(Reset:=FALSE)
and mIdle() are called in the state.
If mInit() returns FALSE, it is changed to the STATE_INOP state.
If mSetError() or mSetErrorIdent() is called, it is switched to the
STATE_ERROR_SHUTDOWN state.

1176 /    ctrlX PLC Engineering
1344      Basic classes for the function block development (Base FB)

STATE_INOP                  The cyclic task is performed here.
       The "Active" output is TRUE as long as this state is active.
       When the state is entered, mInOp(Reset:=TRUE) is called.
       mInOp(Reset:=FALSE) is called in the state.
       If mInOp() returns FALSE, the task is completed and the function
       block changes to the STATE_DONE state.
       If mSetError() or mSetErrorIdent() is called, it is switched to the
       STATE_ERROR_SHUTDOWN state.

STATE_DONE                  State active after successful task processing.
       It is exited if "Execute" is FALSE, but remains active for at least one
       cycle. mIdle() is called in the state.

STATE_RESTART               If a positive edge at the "Execute" input is detected upon execution,
       the current processing is stopped and the function is started again.
       Therefore, the method mShutDown(TRUE) is called, when the state is
       entered state. The method mShutDown(FALSE) is called in the state.
       The outputs "Active" and "Shutdown" are enabled during execution.
       If the method returns mShutDown() = FALSE, it is changed to
       STATE_INIT.

STATE_ABORT_SHUTDOWN This is the abort state of the function block.
The outputs "Shutdown" and "CommandAborted" are active in this
state.
When the state is entered, mShutDown(TRUE) is called. mShut‐
Down(FALSE) and mIdle() are called in the state. Returns the method
mShutDown() = FALSE and if "Execute" is reset, it is changed to the
"STATE_IDLE" state.

STATE_ERROR_                This is the error state of the function block.
SHUTDOWN                    In this state, the outputs “Shutdown” and “Error” are enabled and the
       error code is displayed at “ErrorID” or “ErrorIdent”.
       When the state is entered, mError() is called. mShutDown(TRUE) is
       called in the state. mShutDown(FALSE) and mIdle() are called in the
       state. Returns the method mShutDown() = FALSE and if "Execute" is
       reset, it is changed to "STATE_IDLE". The “Error” output remains set.

Methods
The following methods are available for the user:
Table 1011: Public methods of the IL_ExecuteDoneAbortedShutdownBase function block
Method                  Function
midle()                 Idle code as long as the function block is not in INOP
BOOL:= mInit(Reset)     Initialization code of the function block.
                        Is processed until mInit returns FALSE. Reset at first call TRUE
BOOL:= mInOp(Reset)     Operation code of the function block.
                        Is processed until mInOp returns FALSE. Reset at first call TRUE
BOOL:= mShutDown(Reset) Shutdown code of the function block by abort/error/reset.
                        Is processed until mShutDown returns FALSE. Reset at first call
                        TRUE
mAbort()                Canceling the current task → Transition to shutdown

          Basic classes for the function block development (Base FB)          1344

Method                        Function
mSetError()                   Called by the user when an error was detected
nSetErrorIdent()              Alternative call by the user when an error was detected
Additionally, the following methods are available:
Table 1012: Internal methods of the IL_ExecuteDoneAbortedShutdownBase function block
Method                        Function
mError()                      One-time execution when entering the ERROR state
mReset()                      One-time execution when entering the states IDLE or INIT after
                              restart
mSetOutputs()                 Setting the outputs depends on the current state

Signal-time diagram
The following time response results from the state machine described above:

IL_ExecuteDoneAbortedShutdownBase

IL_ExecuteDoneAbortedShutdownBase

1178 /    ctrlX PLC Engineering
1344      Conversion (bit-stream “connect”)

 Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:
Additional2 contains the target-dependent value CXA_PLC_DETAIL‐
DIAG_ERROR in the upper word, e.g. 16#0C230000 for die ctrlX CORE or
16#01230000 for the ctrlX DRIVE Technology Function.
Table 1013: Error codes of the IL_ExecuteDoneAbortedShutdownBase
ErrorID                     Additional1       Additional2                Description
STATE_MACHINE_ERROR         16#A0F00100       CXA_PLC_DETAILDIAG_ERROR + Invalid state of the
                                              16#00000011                state machine

### 36.3.9 IL_FB_STATES

 IL_FB_STATES defines an enumeration type that contains the states of the
 standard state machine. The states used depend on the type of function
 block. STATE_IDLE is set as the starting state.

Table 1014: IL_FB_STATES enumeration type
State                     Description
STATE_IDLE            0   Starting state of a function block
STATE_INIT            1   Initialization of the function block
                          State runs after the function block starts. All preparations required for
                          the actual operations are made here. A sub-state machine is possible.
STATE_INOP            2   Working state of the function block
                          In this state, the actual task of the function block is executed.
STATE_SHUTDOWN        3   Processing end
                          State exists only for function blocks with a "Shutdown” output. Here, the
                          running processes are completed in order to move the function block
                          back to the STATE_IDLE state.
STATE_DONE            4   Processing completed
                          State indicates that task processing was successfully completed.
STATE_ERROR           5   Error state
                          State is active after an error occurs. It is exited by resetting “Enable” or
                          “Execute”.
STATE_COAB            6   Command canceled by another function block ("CommandAborted"
                          output is TRUE).
STATE_ERROR_SH        7   Completing processes before entering into the error state.
UTDOWN

## 36.4 Conversion (bit-stream “connect”)

### 36.4.1 Introduction and overview

Table 1015: Areas of application and functions/function blocks of CXA_Utilities
Area of application (folder in library)
Function blocks                                  Description
Conversion function and function blocks (bit-stream connect)
⮫ Chapter 36.4.2 IL_BoolToByte on page 1179      8 individual bits (BOOL) are converted to one
                                                 BYTE (FUN)
⮫ Chapter 36.4.3 IL_BoolToDWord on page 1180 32 individual bits (BOOL) are converted to one
                                                 DWORD (FUN)

                                           Conversion (bit-stream “connect”)         1344

⮫ Chapter 36.4.4 IL_BoolToWord on page 1183  16 individual bits (BOOL) are converted to one
                              WORD (FUN)
⮫ Chapter 36.4.5 IL_ByteToDWord on page 1184 4 BYTEs are converted to one DWORD (FUN)
⮫ Chapter 36.4.6 IL_ConcatByte on page 1185        2 BYTEs are summarized to one WORD (FUN)
⮫ Chapter 36.4.7 IL_ConcatWord on page 1186        2 WORDs are summarized to one DWORD
      Bit-stream connect: Smaller data types are summarized to bigger ones.
      An example is the function IL_BoolToByte, which converts 8 bits to one byte.

### 36.4.2 IL_BoolToByte

      Brief description
      This function describes the individual bits of a byte. 8 individual bits are

      converted to a byte.

      Interface description

Table 1016: Interface variables of the IL_BoolToByte function
               Name          Data type        Description
VAR_INPUT      Bit0          BOOL             Describes the position of bit 0 in the output byte
               Bit1          BOOL             Describes the position of bit 1 in the output byte
               Bit2          BOOL             Describes the position of bit 2 in the output byte
               Bit3          BOOL             Describes the position of bit 3 in the output byte
               Bit4          BOOL             Describes the position of bit 4 in the output byte
               Bit5          BOOL             Describes the position of bit 5 in the output byte
               Bit6          BOOL             Describes the position of bit 6 in the output byte
               Bit7          BOOL             Describes the position of bit 7 in the output byte
RETURN         IL_BoolToByte BYTE             Output byte

      Functional description
      This function writes the bits of the inputs to the output byte according to
      their significance. The byte is written in accordance with the state of all bits
      at the input of the function. That means that the state of the input "Bit0" is
      copied to bit 0 of the output byte, the state of the input "Bit1" is copied to bit
      1 of the output byte, etc.

1180 /    ctrlX PLC Engineering
1344      Conversion (bit-stream “connect”)

Troubleshooting
No troubleshooting available for this function.

### 36.4.3 IL_BoolToDWord

Brief description
This function describes the individual bits of a DWord. 32 individual bits are
converted to a double word.

Interface description

                                       Conversion (bit-stream “connect”)       1344

Table 1017: Interface variables of the IL_BoolToDWord function
               Name               Data type     Description
VAR_INPUT      Bit0               BOOL          Describes the position of bit 0 in the output
                                                double word
               Bit1               BOOL          Describes the position of bit 1 in the output
                                                double word
               Bit2               BOOL          Describes the position of bit 2 in the output
                                                double word
               Bit3               BOOL          Describes the position of bit 3 in the output
                                                double word
               Bit4               BOOL          Describes the position of bit 4 in the output
                                                double word

Bit5               BOOL          Describes the position of bit 5 in the output
                                 double word
Bit6               BOOL          Describes the position of bit 6 in the output
                                 double word
Bit7               BOOL          Describes the position of bit 7 in the output
                                 double word
Bit8               BOOL          Describes the position of bit 8 in the output
                                 double word
Bit9               BOOL          Describes the position of bit 9 in the output
                                 double word
Bit10              BOOL          Describes the position of bit 10 in the output
                                 double word
Bit11              BOOL          Describes the position of bit 11 in the output
                                 double word
Bit12              BOOL          Describes the position of bit 12 in the output
                                 double word
Bit13              BOOL          Describes the position of bit 13 in the output
                                 double word
Bit14              BOOL          Describes the position of bit 14 in the output
                                 double word
Bit15              BOOL          Describes the position of bit 15 in the output
                                 double word
Bit16              BOOL          Describes the position of bit 16 in the output
                                 double word
Bit17              BOOL          Describes the position of bit 17 in the output
                                 double word
Bit18              BOOL          Describes the position of bit 18 in the output
                                 double word
Bit19              BOOL          Describes the position of bit 19 in the output
                                 double word
Bit20              BOOL          Describes the position of bit 20 in the output
                                 double word
Bit21              BOOL          Describes the position of bit 21 in the output
                                 double word
Bit22              BOOL          Describes the position of bit 22 in the output
                                 double word
Bit23              BOOL          Describes the position of bit 23 in the output
                                 double word

1182 /    ctrlX PLC Engineering
1344      Conversion (bit-stream “connect”)

Name              Data type      Description
Bit24             BOOL           Describes the position of bit 24 in the output
                                 double word
Bit25             BOOL           Describes the position of bit 25 in the output
                                 double word
Bit26             BOOL           Describes the position of bit 26 in the output
                                 double word
Bit27             BOOL           Describes the position of bit 27 in the output
                                 double word
Bit28             BOOL           Describes the position of bit 28 in the output
                                 double word
Bit29             BOOL           Describes the position of bit 29 in the output
                                 double word
Bit30             BOOL           Describes the position of bit 30 in the output
                                 double word
Bit31             BOOL           Describes the position of bit 31 in the output
                                 double word
RETURN             IL_BoolToDWord    DWORD          Output double word

    Functional description
    This function writes the bits of the inputs to the output double word
    according to their significance. The DWord is written in accordance with the
    state of all bits at the input of the function. That means that the state of the
    input "Bit0" is copied to bit 0 of the output double word, the state of the
    input "Bit1" is copied to bit 1 of the output double word, etc.

                                    Conversion (bit-stream “connect”)      1344

Troubleshooting
No troubleshooting available for this function.

### 36.4.4 IL_BoolToWord

Brief description
This function describes the individual bits of a Word. 16 individual bits are
converted to a word.

Interface description

Table 1018: Interface variables of the IL_BoolToWord function
              Name           Data type        Description
VAR_INPUT     Bit0           BOOL             Describes the position of bit 0 in the output word
              Bit1           BOOL             Describes the position of bit 1 in the output word
              Bit2           BOOL             Describes the position of bit 2 in the output word
              Bit3           BOOL             Describes the position of bit 3 in the output word
              Bit4           BOOL             Describes the position of bit 4 in the output word
              Bit5           BOOL             Describes the position of bit 5 in the output word
              Bit6           BOOL             Describes the position of bit 6 in the output word
              Bit7           BOOL             Describes the position of bit 7 in the output word
              Bit8           BOOL             Describes the position of bit 8 in the output word
              Bit9           BOOL             Describes the position of bit 9 in the output word
              Bit10          BOOL             Describes the position of bit 10 in the output word
              Bit11          BOOL             Describes the position of bit 11 in the output word
              Bit12          BOOL             Describes the position of bit 12 in the output word
              Bit13          BOOL             Describes the position of bit 13 in the output word
              Bit14          BOOL             Describes the position of bit 14 in the output word
              Bit15          BOOL             Describes the position of bit 15 in the output word
RETURN        IL_BoolTo‐     WORD             Output word
              Word

1184 /    ctrlX PLC Engineering
1344      Conversion (bit-stream “connect”)

    Functional description
    This function writes the bits of the inputs to the output word according to
    their significance. The word is written in accordance with the state of all bits
    at the input of the function. That means that the state of the input "Bit0" is
    copied to bit 0 of the output word, the state of the input "Bit1" is copied to
    bit 1 of the output word, etc.

    Troubleshooting
    No troubleshooting available for this function.

### 36.4.5 IL_ByteToDWord

    Brief description
    This function describes the individual bytes of a DWord. 4 individual bytes are
    converted to a double word.

    Interface description

Table 1019: Interface variables of the IL_ByteToDWord function
                   Name              Data type       Description
VAR_INPUT          Byte0             BYTE            Describes the position of byte 0 in the output
                                                     double word
                   Byte1             BYTE            Describes the position of byte 1 in the output
                                                     double word
                   Byte2             BYTE            Describes the position of byte 2 in the output
                                                     double word
                   Byte3             BYTE            Describes the position of byte 3 in the output
                                                     double word

                                    Conversion (bit-stream “connect”)        1344

Name                 Data type      Description
RETURN         IL_ByteToDWord       DWORD          Output double word

Functional description
This function writes the bytes of the inputs to the output double word
according to their significance. The double word is written in accordance with
the state of all bytes at the input of the function. That means that the state of
the input "Byte0" is copied to byte 0 of the output double word, the state of
the input "Byte1" is copied to byte 1 of the output double word, etc.

Troubleshooting
No troubleshooting available for this function.

### 36.4.6 IL_ConcatByte

Brief description
This function describes the individual bytes of a Word. 2 bytes are consoli‐
dated to a word.

Interface description

Table 1020: Interface variables of the IL_ConcatByte function
               Name                 Data type      Description
VAR_INPUT      HighByte             BYTE           Describes the position of byte 1 in the output
                                                   word
               LowByte              BYTE           Describes the position of byte 0 in the output
                                                   word
RETURN         IL_ConcatByte        WORD           Output word

1186 /    ctrlX PLC Engineering
1344      Conversion (bit-stream “connect”)

Functional description
This function writes the bytes of the inputs to the output word according
to their significance. The word is written in accordance with the state of all
bytes at the input of the function. That means that the state of the input
"HighByte" is copied to byte 1 of the output double word, the state of the
input "LowByte" is copied to byte 0 of the output word, etc.

Troubleshooting
No troubleshooting available for this function.

### 36.4.7 IL_ConcatWord

Brief description
This function describes the individual words of a double word. 2 words are
consolidated to a double word.

Interface description

Table 1021: Interface variables of the IL_ConcatWord function
                   Name              Data type       Description
VAR_INPUT          HighWord          WORD            Describes the position of word 1 in the output
                                                     double word
                   LowWord           WORD            Describes the position of word 0 in the output
                                                     double word
RETURN             IL_ConcatWord     DWORD           Output double word

Functional description
This function writes the words of the inputs to the output double word
according to their significance. The double word is written in accordance with
the state of the words at the input of the function. That means that the state
of the input "HighWord" is copied to word 1 of the output double word, the
state of the input "LowWord" is copied to word 0 of the output double word,
etc.

                                       Conversion (bit stream “split”)       1344

Troubleshooting

No troubleshooting available for this function.

## 36.5 Conversion (bit stream “split”)

### 36.5.1 Introduction and overview

Table 1022: Areas of application and functions/function blocks of CXA_Utilities
Area of application (folder in library)
Function blocks                                  Description
Conversion function and function blocks (bit-stream split)
⮫ Chapter 36.5.2 IL_ByteToBool on page 1187      Function block extracts 8 bits (BOOL) from one
                                                 BYTE
⮫ Chapter 36.5.3 IL_DWordToBool on page 1188 Function block extracts 32 bits (BOOL) from
                                                 one DWORD
⮫ Chapter 36.5.4 IL_DWordToByte on page 1191 Function block extracts 4 BYTEs from one
                                                 DWORD
⮫ Chapter 36.5.5 IL_HighByte on page 1191        FUN extracts a high-order BYTE from one WORD
⮫ Chapter 36.5.7 IL_HighWord on page 1193          FUN extracts a high-order WORD from one
                                                   DWORD
⮫ Chapter 36.5.6 IL_LowByte on page 1192           FUN extracts a low-order BYTE from one WORD
⮫ Chapter 36.5.8 IL_LowWord on page 1193           FUN extracts a low-order WORD from one
                                                   DWORD
⮫ Chapter 36.5.9 IL_WordToBool on page 1194        Function block extracts 16 bits (BOOL) from
                                                   one WORD
                     Bit-Stream Split: One data type is split into smaller data types.
                     An example is the function block IL_DWordToByte, which splits a double word
                     into 4 bytes.

### 36.5.2 IL_ByteToBool

Brief description
This function block extracts individual bits from a byte. 8 individual bits are
extracted from a byte.

1188 /    ctrlX PLC Engineering
1344      Conversion (bit stream “split”)

Interface description

Table 1023: Interface variables of the IL_ByteToBool function
          Name               Data type         Description
VAR_INPUT Input              BYTE              Input byte from which the bits are extracted
VAR_OUPUT Bit0               BOOL              Bit 0 of the input byte
          Bit1               BOOL              Bit 1 of the input byte
          Bit2               BOOL              Bit 2 of the input byte
          Bit3               BOOL              Bit 3 of the input byte
          Bit4               BOOL              Bit 4 of the input byte
          Bit5               BOOL              Bit 5 of the input byte
          Bit6               BOOL              Bit 6 of the input byte
          Bit7               BOOL              Bit 7 of the input byte

Functional description
This function block determines the individual bits of a byte. The state of the
input "Input" is identified and the status of the individual bits is copied to the
output variables "Bit0" .. “Bit7”.

Troubleshooting
No troubleshooting available for this function block.

### 36.5.3 IL_DWordToBool

Brief description
This function block extracts individual bits from a double word. 32 individual
bits are extracted from a DWord.

                                     Conversion (bit stream “split”)     1344

Interface description

Table 1024: Interface variables of the IL_DWordToBool function
          Name               Data type       Description
VAR_INPUT Input              DWORD           Input double word from which the bits are extracted
VAR_OUPUT Bit0               BOOL            Bit 0 of the input double word
          Bit1               BOOL            Bit 1 of the input double word
          Bit2               BOOL            Bit 2 of the input double word
          Bit3               BOOL            Bit 3 of the input double word
          Bit4               BOOL            Bit 4 of the input double word
          Bit5               BOOL            Bit 5 of the input double word
          Bit6               BOOL            Bit 6 of the input double word
          Bit7               BOOL            Bit 7 of the input double word
          Bit8               BOOL            Bit 8 of the input double word
          Bit9               BOOL            Bit 9 of the input double word
          Bit10              BOOL            Bit 10 of the input double word
          Bit11              BOOL            Bit 11 of the input double word
          Bit12              BOOL            Bit 12 of the input double word
          Bit13              BOOL            Bit 13 of the input double word
          Bit14              BOOL            Bit 14 of the input double word

1190 /    ctrlX PLC Engineering
1344      Conversion (bit stream “split”)

Name           Data type          Description
Bit15          BOOL               Bit 15 of the input double word
Bit16          BOOL               Bit 16 of the input double word
Bit17          BOOL               Bit 17 of the input double word
Bit18          BOOL               Bit 18 of the input double word
Bit19          BOOL               Bit 19 of the input double word
Bit20          BOOL               Bit 20 of the input double word
Bit21          BOOL               Bit 21 of the input double word
Bit22          BOOL               Bit 22 of the input double word
Bit23          BOOL               Bit 23 of the input double word
Bit24          BOOL               Bit 24 of the input double word
Bit25          BOOL               Bit 25 of the input double word
Bit26          BOOL               Bit 26 of the input double word
Bit27          BOOL               Bit 27 of the input double word
Bit28          BOOL               Bit 28 of the input double word
Bit29          BOOL               Bit 29 of the input double word
Bit30          BOOL               Bit 30 of the input double word
Bit31          BOOL               Bit 31 of the input double word

        Functional description
        This function block determines the individual bits of a double word. The state
        of the input "Input" is identified and the status of the individual bits is copied
        to the output variables "Bit0" .. “Bit31”.

        Troubleshooting
        No troubleshooting available for this function block.

                                        Conversion (bit stream “split”)       1344

### 36.5.4 IL_DWordToByte

Brief description
This function block extracts individual bytes from a DWord. 4 individual bytes
are extracted from a double word.

Interface description

Table 1025: Interface variables of the IL_DWordToByte function
              Name           Data type          Description
VAR_INPUT     Input          DWORD              Input double word from which the bytes are
                                                extracted
VAR_OUPUT Byte0              BYTE               Byte 0 of the input double word
          Byte1              BYTE               Byte 1 of the input double word
          Byte2              BYTE               Byte 2 of the input double word
          Byte3              BYTE               Byte 3 of the input double word

Functional description
This function block determines the individual bytes of a double word. The
state of the input "Input" is identified and the status of the individual bytes is
copied to the output variables Byte0 .. Byte3.

Troubleshooting
No troubleshooting available for this function block.

### 36.5.5 IL_HighByte

Brief description
This function extracts the high-order byte from a word.

1192 /    ctrlX PLC Engineering
1344      Conversion (bit stream “split”)

Interface description

Table 1026: Interface variables of the IL_HighByte function
                   Name          Data type       Description
VAR_INPUT          Input         WORD            Input word from which the byte is extracted
RETURN             IL_HighByte   BYTE            High-order byte of the input word

Functional description
This function determines the high-order byte of a word. The state of the input
"Input" is identified and the status of the high-order byte is copied to the
function output.

Troubleshooting
No troubleshooting available for this function.

### 36.5.6 IL_LowByte

Brief description
This function extracts the low-order byte from a word.

Interface description

Table 1027: Interface variables of the IL_LowByte function
                   Name          Data type       Description
VAR_INPUT          Input         WORD            Input word from which the byte is extracted
RETURN             IL_LowByte    BYTE            Low-order byte of the input word

Functional description
This function determines the low-order byte of a word. The state of the input
"Input" is identified and the status of the low-order byte is copied to the
function output.

                                         Conversion (bit stream “split”)     1344

Troubleshooting
No troubleshooting available for this function.

### 36.5.7 IL_HighWord

Brief description
This function extracts the high-order word from a double word.

Interface description

Table 1028: Interface variables of the IL_HighWord function
              Name        Data type           Description
VAR_INPUT     Input       DWORD               Input double word from which the word is extracted
RETURN        IL_HighWord WORD                High-order word of the input double word

Functional description
This function determines the high-order word of a double word. The state of
the input "Input" is identified and the status of the high-order word is copied
to the function output.

Troubleshooting
No troubleshooting available for this function.

### 36.5.8 IL_LowWord

Brief description
This function extracts the low-order word from a double word.

1194 /    ctrlX PLC Engineering
1344      Conversion (bit stream “split”)

Interface description

Table 1029: Interface variables of the IL_LowWord function
                   Name       Data type          Description
VAR_INPUT          Input      DWORD              Input double word from which the word is extracted
RETURN             IL_LowWord WORD               Low-order word of the input double word

Functional description
This function determines the low-order word of a double word. The state of
the input "Input" is identified and the status of the low-order word is copied
to the function output.

Troubleshooting
No troubleshooting available for this function.

### 36.5.9 IL_WordToBool

Brief description
This function block extracts individual bits from a word. 16 individual bits are
extracted from a word.

Interface description

                                        Conversion (bit stream “split”)       1344

Table 1030: Interface variables of the IL_WordToBool function
          Name               Data type         Description
VAR_INPUT Input              WORD              Input word from which the bits are extracted
VAR_OUPUT Bit0               BOOL              Bit 0 of the input word
          Bit1               BOOL              Bit 1 of the input word
          Bit2               BOOL              Bit 2 of the input word
          Bit3               BOOL              Bit 3 of the input word
          Bit4               BOOL              Bit 4 of the input word
          Bit5               BOOL              Bit 5 of the input word
          Bit6               BOOL              Bit 6 of the input word
          Bit7               BOOL              Bit 7 of the input word

Bit8               BOOL              Bit 8 of the input word
Bit9               BOOL              Bit 9 of the input word
Bit10              BOOL              Bit 10 of the input word
Bit11              BOOL              Bit 11 of the input word
Bit12              BOOL              Bit 12 of the input word
Bit13              BOOL              Bit 13 of the input word
Bit14              BOOL              Bit 14 of the input word
Bit15              BOOL              Bit 15 of the input word

Functional description
This function block determines the individual bits of a word. The state of the
input "Input" is identified and the status of the individual bits is copied to the
output variables "Bit0" .. "Bit15”.

Troubleshooting
No troubleshooting available for this function block.

1196 /    ctrlX PLC Engineering
1344      Conversion (ByteSwap)

## 36.6 Conversion (ByteSwap)

### 36.6.1 Introduction and overview

CXA_Utilities, ByteSwap
Table 1031: Areas of application and functions/function blocks of CXA_Utilities
Area of application (folder in library)
Function blocks                                Description
Conversion functions and function blocks (ByteSwap)
⮫ Chapter 36.6.2 IL_SwapDWord on page 1196 FUN exchanges BYTEs of a DWORDs ( 3 2 1 0 ->
                                               0 1 2 3)
                                               Note: Not PLC-compatible!
⮫ Chapter 36.6.3 IL_SwapWord on page 1196      FUN exchanges BYTEs of a WORD (1 0 -> 0 1)
                        Byte swap: The lower and the upper half of the data type are swapped.
                        An example is the function IL_SwapWord, which swaps the low-order byte of
                        the input word with the high-order one.

### 36.6.2 IL_SwapDWord

Brief description
This function swaps the bytes of a double word 3 2 1 0 --> 0 1 2 3.

Interface description

Table 1032: Interface IL_SwapDWord
                   Name              Data type         Description
VAR_INPUT          Input             DWORD             Input double word
RETURN             IL_SwapWord       DWORD             Output double word with swapped bytes

Functional description
This function swaps the bytes of a double word in their sequence.
The state of the "Input" input is detected.
The byte sequence changes from 3 2 1 0 to 0 1 2 3.
The result is copied to the function output.
The function name is not according to IEC 61131-3.

Troubleshooting
No troubleshooting available for this function.

### 36.6.3 IL_SwapWord

Brief description
This function swaps the high-order and the low-order byte of a word.

                                                            Checksums        1344

Interface description

Table 1033: Interface IL_SwapWord
              Name             Data type       Description
VAR_INPUT     Input            WORD            Input word
RETURN        IL_SwapWord      WORD            Output word with which the high-order byte was

                          swapped with the low-order byte.

Functional description
With this function, the high-order byte of a word is swapped with the low-
order byte. The state of the input "Input" is registered and the high-order and
the low-order byte are swapped and copied to the function output.

Troubleshooting
No troubleshooting available for this function.

## 36.7 Checksums

### 36.7.1 Introduction and overview

CXA_Utilities, CRC16
Table 1034: Areas of application and functions/function blocks of CXA_Utilities
Area of application (folder in library)
Function blocks                                    Description
Checksums (CRC16)
⮫ Chapter 36.7.2 IL_CRC16 on page 1197             Function block computes CRC16 checksum
                                                   using a date
                     This sections describes functions and function blocks calculating checksums.
                     Currently, there is only function block implemented into this function group.

### 36.7.2 IL_CRC16

Brief description
The function block IL_CRC16 calculates a CRC16 checksum via a date.

1198 /    ctrlX PLC Engineering
1344      Checksums

Interface description

Table 1035: Interface variables of the IL_CRC16 function block
                     Name               Type           Comment
VAR_INPUT            Execute            BOOL           Processing enabled (cyclic, edge-con‐
                                                       trolled)
                     DataAddress       POINTER TO BYTE Address of the date to be used for cal‐
                                                       culating the checksum
                     DataSize          UINT            Size of the date in bytes
                     CalcBytesPerCycle UINT            Size in bytes of the partial data block
                                                       to be calculated per call
VAR_OUTPUT           Done              BOOL            Processing completed by the function
                                                       block
                     Active            BOOL            The function block is active
                     Error             BOOL            Indicates that an error occurred
                     ErrorID           ⮫ ERROR_CODE    Error cause
                     ErrorIdent        ⮫ ERROR_STRUCT Detailed error cause
                     CRC16              WORD                Calculated checksum

Functional description
When there is a rising edge at the Enable input, the input values are applied
and calculation of the checksum is started.
The values of the address ("DataAddress") and its size ("DataSize") of the
date have to be valid values.
If input "CalcBytesPerCycle" is 0, the checksum is completely calculated upon
the first call. Only the number of bytes specified in “CalcBytesPerCycle" is
calculated before the function block returns. This prevents the processing
load from becoming too high.
The value at output "CRC16" is only valid if output "Done" is set.

Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:
Additional2 contains the target-dependent value CXA_PLC_DETAIL‐
DIAG_ERROR in the upper word, e.g. 16#0C230000 for die ctrlX CORE or
16#01230000 for the ctrlX DRIVE Technology Function.
Table 1036: Error codes generated by IL_CRC16
ErrorID                   Additional1        Additional2                Description
INPUT_RANGE_ERROR         16#A0F00100        CXA_PLC_DETAILDIAG_ERROR + The "DataAddress"
                                             16#00000021                input is 0.

                                       Conversion (data type “change")       1344

ErrorID                      Additional1     Additional2                Description
INPUT_RANGE_ERROR            16#A0F00100     CXA_PLC_DETAILDIAG_ERROR + The "DataSize" input is
                        16#00000022                0.

## 36.8 Conversion (data type “change")

### 36.8.1 Introduction and overview

CXA_Utilities, data type change
Table 1037: Areas of application and functions/function blocks of CXA_Utilities
Area of application (folder in library)
Function blocks                                     Description

Conversion (data type “change")
⮫ Chapter 36.8.2 IL_AsciiToByte on page 1199        FUN converts any ASCII character to a byte code
⮫ Chapter 36.8.3 IL_ByteToAscii on page 1200        FUN converts any byte code to an ASCII char‐
                               acter
⮫ Chapter 36.8.4 IL_RealToString on page 1200       FUN converts REAL value to a STRING
⮫ Chapter 36.8.5 IL_LRealToString on page 1201 FUN converts (L)REAL value format-controlled to
                          a STRING
The functions interpret their input data according to the guideline given in the
description.

### 36.8.2 IL_AsciiToByte

Brief description
This function converts an arbitrary ASCII sign to the corresponding byte code.

Interface description

Table 1038: Interface IL_AsciiToByte
              Name                Data type         Description
VAR_INPUT     Input               BYTE              Input byte containing the byte code
RETURN        IL_AsciiToByte      STRING[1]         The function output contains the ASCII sign
                                                    which corresponds to the byte code in the input
                                                    string.

Functional description
With this function, the ASCII character of the byte code in the input byte is
determined. The state of the input "Input" is detected and the corresponding
ASCII character is copied to the function output.

Troubleshooting
No troubleshooting available for this function.

1200 /    ctrlX PLC Engineering
1344      Conversion (data type “change")

### 36.8.3 IL_ByteToAscii

Brief description
This function converts an arbitrary byte code to the corresponding ASCII sign.

Interface description

Table 1039: Interface IL_ByteToAscii
                   Name              Data type         Description
VAR_INPUT          Input             BYTE              Input byte containing the byte code to be con‐
                                                       verted
RETURN             IL_ByteToAscii    STRING[1]         Function output contains the ASCII sign of the
                                                       byte code in the input string

Functional description
With this function, the ASCII character of the byte code in the input string is
determined. The state of the input "Input" is detected and the corresponding
ASCII value of the character is copied to the function output.

Troubleshooting
No troubleshooting available for this function.

### 36.8.4 IL_RealToString

Brief description
This function converts a REAL value to a string.

Interface description

Table 1040: Interface IL_RealToString
                   Name            Data type         Description
VAR_INPUT          Input           REAL              Input byte containing the figure to be converted
RETURN             IL_RealToString STRING            Function output contains the real value as string.

Functional description
With this function, the content of the input "Input" is registered, converted
to a string and copied to the output of the function. As of values lower than
"0.1", IndraLogic automatically uses the exponential notation (e.g. 0.0126 is
written as 1.26e-002). The function "IL_RealToString" ignores this and displays
the real value as string in the decimal notation. The function "IL_RealToString"
only considers values up to the fourth decimal place (e.g. the real 0.0123789
becomes string 0.0124)!

                                      Conversion (data type “change")        1344

Troubleshooting
No troubleshooting available for this function.

### 36.8.5 IL_LRealToString

Brief description
This function converts an (L)REAL value to a STRING. The number is con‐
verted with regard to the content of the format string.
If a REAL number is applied to an LREAL input, it is implicitly converted from
REAL into LREAL.

Interface description

Table 1041: IL_LRealToString interface
             Name                 Data type        Description
VAR_INPUT Format                  STRING(19)       Format string to represent "Value"
             Value                LREAL            Number to be converted
Return value IL_LRealToString     STRING(20)       Function output contains LREAL value as
                                                   STRING

Functional description
This function converts an LREAL value to a STRING. The number is formatted
with regard to the content of the format string.
The format string determines the number of decimal places in front of and
after the comma. It can output leading zeroes or selected between decimal
point and comma.
Syntax of the format string:
  [0|#] [{#}] [.|,] [{#}]
'#': Places(s) to be output in from of and after the comma
'0': Output of leading zeroes
'.': Decimal separator (US)
',': Decimal separator (DE)
Table 1042: Effect of the format string
LREAL number Format             Result            Note
-1.23456789E02 ###.###          -123.457          The last place is rounded
1.23456789E02 ###.###           ␣123.457          Positive numbers are always
                                                  provided with a leading
                                                  space
1.23456789E02 ###,###           ␣123,457          Uses a comma as decimal
                                                  separator
1.2                 ###.###     ␣␣␣1.200          Format is always filled left
                                                  and right
-1.2345678E-06 ###.###          ␣␣-0.000          if a negative value is
                                                  rounded to zero, "-0" is dis‐
                                                  played

1202 /    ctrlX PLC Engineering
1344      Debugging

LREAL number Format            Result           Note
1.23456789E05 ###.###          ␣12345.679       if the number cannot be
                                                output in the format, the
                                                format is extended
-1.23456789E02 #####           ␣␣-123           Output as whole number
1.23456789E02 0####            ␣00123           Output with leading zeroes
-1.23456789E02 0####           -00123           As above
1.2345E02      (blank)         1.2345E02        An empty format
                                                is converted using
                                                the standard function
                                                LREAL_TO_STRING()
1.23456789E02 ##0.##           Format error     If the format string is faulty,
                                                "Format error" is output
Remarks
Values allowed for LREAL:
±(2.2250738585072014e-308 ... 1.7976931348623158e+308)
Values > 9.0007199254741e+15 or <-9.0007199254741e+15 (±(2e+53 -
1)) are only converted using LREAL_TO_STRING().
Table 1043: Conversion examples
                 LREAL                      Format             STRING
      -2.2250738585072014e-308             '###.###'           ␣␣-0.000
            -999999.999999              '0#########'        -0001000000
                  0.1                      '###.###'           ␣␣0.100
               0.0314e+4                  '####.###'          ␣␣314.000
           3.402823466e+38                     ''         3.402823466e+38

Troubleshooting
If a value cannot be output in the specified format, the format is extended
accordingly.
If an incorrect format is specified, "Format Error" is output.

## 36.9 Debugging

### 36.9.1 Introduction and overview

Functions to process high-resolution CPU ticks are available. These functions
can be used to determine the operation time of program modules:

CXA_Utilities, Debugging
Table 1044: Areas of application and functions/function blocks of CXA_Utilities
Area of application (folder in library)
Function blocks                                  Description
Debugging
⮫ Chapter 36.9.2 IL_HighResTimeDiff              Calculates the time difference of two high-reso‐
on page 1203                                     lution time ticks of the system in microseconds
⮫ Chapter 36.9.3 IL_HighResTimeTick              Reads the high-resolution time cycle of the
on page 1203                                     system

                                                             Debugging       1344

### 36.9.2 IL_HighResTimeDiff

Brief description
The function IL_HighResTimeDiff calculates the time difference of two high-
resolution time ticks of the system in microseconds.

Interface description

Table 1045: Interface IL_HighResTimeDiff
          Name             Data type          Description
VAR_INPUT HighResTimeTick1 UDINT              High-resolution time tick of the system before the
                                              code section
             HighResTimeTick2 UDINT           High-resolution time tick of the system after the code
                                              section
RETURN       IL_HighResTime‐     UDINT        Time difference of two high-resolution time ticks of
             Diff                             the system in μs

Specification
The function IL_HighResTimeDiff is used for the determination of the opera‐
tion time of a code section together with the function IL_HighResTimeTick

Depending on the system, the reading of a high-resolution time tick takes ca.
one to two microseconds which can be additionally taken into consideration
for the determination of the time difference by the user, if necessary.

Functional description
The function IL_HighResTimeDiff calculates the time difference of two high-
resolution time ticks of the system in microseconds.

Troubleshooting
No troubleshooting available for this function.

Use case
see ⮫ Use case on page 1204.

### 36.9.3 IL_HighResTimeTick

Brief description
The function IL_HighResTimeTick reads the high-resolution time tick of the
system.

1204 /    ctrlX PLC Engineering
1344      Debugging

Interface description

Table 1046: Interface IL_HighResTimeTick
               Name                  Data type   Description
VAR_INPUT      Enable                BOOL        Processing of function enabled (cyclic, state-con‐
                                                 trolled)
RETURN         IL_HighResTimeTick UDINT          High-resolution time tick of the system

Specification
The function IL_HighResTimeTick is used for the determination of the opera‐
tion time of a code section together with the function IL_HighResTimeDiff

The return value of the function IL_HighResTimeTick should not be directly
used as a time value due to the special system-dependent time base.

Functional description
The function IL_HighResTimeTick cyclically reads the high-resolution time tick
of the system after processing enabled for the function with "Enable".

Troubleshooting
No troubleshooting available for this function.

Use case
In this program example, the operation time of a program block is measured.

                                                            FlipFlops       1344

## 36.10 FlipFlops

### 36.10.1 Introduction and overview

This function block extends the trigger function blocks provided by the default
library.

CXA_Utilities, FlipFlops
Table 1047: Areas of application and functions/function blocks of CXA_Utilities
Area of application (folder in library)
Function blocks                                   Description
FlipFlops

⮫ Chapter 36.10.2 IL_Toggle on page 1205          Settable and resettable FlipFlop

### 36.10.2 IL_Toggle

Brief description
This function block changes the status of its Boolean output with every rising
edge at the "Execute" input. Two additional inputs allow for setting the Boo‐
lean output to TRUE or FALSE.

Interface description

Table 1048: Interface IL_Toggle
          Name               Data type       Description
VAR_INPUT Execute            BOOL            Rising edge changes the status of the output "Toggle"
          Set                BOOL            Sets the output Toggle to TRUE
          Reset              BOOL            Sets the output Toggle to FALSE
VAR_OUPUT Toggle             BOOL            Current state

1206 /    ctrlX PLC Engineering
1344      Mathematical functions

Signal-time diagram

Top: Behavior of "Toggle" when "Set" and "Reset" remain FALSE
Down: Behavior of "Toggle" when "Set", "Reset" and "Execute" interact
●   "Toggle" remains FALSE since "Reset" is TRUE
●   "Toggle" remains TRUE since "Set" is TRUE
●   "Toggle" becomes FALSE since "Reset" dominates
●   "Toggle" becomes "TRUE" since "Set" is "TRUE"

Functional description
The function block IL_Toggle changes the status of its output "Toggle"
between TRUE and FALSE with every rising edge at the input "Execute". The
input "Set" fixes the output "Toggle" to TRUE. The input "Reset" fixes the
output "Toggle" to FALSE. If both inputs "Set" and "Reset" are TRUE, Reset
dominates so that the output "Toggle" is set to FALSE. As long as "Set" or
"Reset" are TRUE, signal changes at Execute do not affect the output "Toggle".

Troubleshooting
No troubleshooting available for this function block.

## 36.11 Mathematical functions

### 36.11.1 Introduction and overview

The following function blocks provide mathematical functions.

                                               Mathematical functions        1344

CXA_Utilities, mathematical functions
Table 1049: Areas of application and functions/function blocks of CXA_Utilities
Area of application (folder in library)
Function blocks                                    Description
Mathematical functions
⮫ Chapter 36.11.2 IL_InterpolationLinear           Calculates intermediate points and linearizations
on page 1207                                       for example. The function block uses the struc‐
                                                   ture ⮫ Chapter 36.11.4 IL_COORD_PAIR_TYPE01
                                                   on page 1210
⮫ Chapter 36.11.3 IL_MaxValue on page 1209         Indicates the maximum value of all occurred
                                                   values

### 36.11.2 IL_InterpolationLinear

Brief description
The function block IL_InterpolationLinear cyclically calculates the y-value asso‐
ciated to a given x-value by linear interpolation based on a defined X-Y node
table.

Interface description

Table 1050: Interface variables of the IL_InterpolationLinear function block
I/O type      Name           Data type                  Description
VAR_INPUT     Enable         BOOL                       Enabling the function block (cyclic, state-
                                                        controlled)
              XValue         LREAL                      X value
              Disable‐       BOOL                       Deactivating copying of the data point table
              Copy
              Disable‐       BOOL                       Deactivating sorting of the data point table
              Sort
              NofPairs       DINT                       Number of the connected value pairs in the
                                                        data point table
           ValueTable POINTER TO ARRAY                  Address of the data point table
                      [0..127] OF
                      ⮫ IL_COORDINATE_PAIR_TYPE01
VAR_OUTPUT InOpera‐   BOOL                    Cyclic calculation of a y-value completed
           tion                               without error, output variable "YValue”
                                              valid
           Active     BOOL                    Calculation of a Y value active, output varia‐
                                              bles invalid
           Error      BOOL                    Calculation of a y-value completed with
                                              error, error outputs "ErrorID" and "ErrorI‐
                                              dent" valid

1208 /     ctrlX PLC Engineering
1344       Mathematical functions

I/O type           Name       Data type                     Description
ErrorID    ⮫ ERROR_CODE                  If the "Error" output is set, it contains a
                                   broad error classification
ErrorIdent ⮫ ERROR_STRUCT                If the "Error" output is set, this output con‐
                                   tains detailed error information
                                   ⮫ Troubleshooting on page 1208
YValue     LREAL                         Y-value

Functional description
The function block IL_InterpolationLinear cyclically calculates the y-value
"YValue" associated with the input value "XValue" via "Enable" based on a
specified data point table after processing enabled for the function block.
The data point table is saved on an internal data array depending on the
inputs "DisableCopy" and "DisableSort" at a rising edge and sorted in an
ascending order afterwards. The time for calculating a respective y-value
"YValue" can be minimized if a data point table already sorted in an ascending
order is used when the function block is enabled for processing and this is
marked by the input "DisableSort". In this case, the data array is not sorted. If
in a new processing of the function block, the internally available and already
used data point table should be used again, the input “DisableCopy" as well
as the input "DisableSort" have to be set to enabled.
The y-value to be calculated is stored on the output "YValue" in case of error-
free processing of the function block. The validity of the value is signaled by
the output "InOperation".
If the y-value to be calculated immediately cannot be provided after the func‐
tion block activation, it is indicated by the output "Active".
If an error occurs while processing the function block, it is signaled by the
"Error" output. The output "YValue" is not updated in case of an error.
Table 1051: Effect of the inputs "DisableCopy" and "DisableSort" on the
runtime behavior of the function block
DisableCopy      DisableSort    Use case
FALSE            FALSE          An unsorted data point table is specified. It
                                was not used like this in the previous calcu‐
                                lation. The data point table is copied and
                                sorted
FALSE            TRUE           A data point table already sorted in an
                                ascending order is specified. It was not used
                                like this in the previous calculation. The data
                                point table is copied but not sorted internally
TRUE             FALSE          This combination is not a reasonable state
TRUE             TRUE           The data point table was used in previous cal‐
                                culations. Therefore, it is already known inter‐
                                nally and sorted in an ascending order
Sorting the data point table after the activation of the function block might
cause that the function block cannot deliver the desired output value in
the first or the following cycle due to the restriction to a maximally admis‐
sible runtime. This duration at the beginning of the activation is signaled by
"Active".

Troubleshooting
The function block uses the error table CXA_TABLE, 16#0030. It can generate
the following error messages in Additional1 and Additional2:

                                                Mathematical functions        1344

Additional2 contains the target-dependent value CXA_PLC_DETAIL‐
DIAG_ERROR in the upper word, e.g. 16#0C230000 for die ctrlX CORE or
16#01230000 for the ctrlX DRIVE Technology Function.
Table 1052: Error codes of the IL_InterpolationLinear function block
ErrorID                      Additional1      Additional2                Description
INPUT_RANGE_ERROR            16#A0F00100      CXA_PLC_DETAILDIAG_ERROR + Inputs invalid
                                              16#00000031                (XValue not within
                                                                         the data points)
STATE_MACHINE_ERROR 16#A0F00100               CXA_PLC_DETAILDIAG_ERROR + Invalid state of the
                                              16#00000032                state machine.

### 36.11.3 IL_MaxValue

Brief description
The function block IL_MaxValue determines the actual maximum value from
the time dependent course of the input signal.

Interface description

Table 1053: Interface variables of the IL_MaxValue function block
I/O type       Name                 Data type           Description
VAR_INPUT      Enable               BOOL                Processing enabled of the function block
                                                        (cyclic, state-controlled)
           ActValue                 LREAL               Current value
           Preset                   BOOL                Activation of preset value
           PresetValue              LREAL               Specified value
VAR_OUTPUT InOperation              BOOL                Determination of maximum value com‐
                                                        pleted
               PresetAck            BOOL                Confirmation to apply "PresetValue" value
               MaxValue             LREAL               Maximum value

Functional description
After the release of the function block, the function block IL_MaxValue uses
"Enable" to compare the current value of the input variable "ActValue" to
the value in "MaxValue". It copies the respectively higher value to the output
variable "MaxValue."
If the input "Preset" is activated at function block runtime, the value of the
input variable "PresetValue" is copied to the output variable "MaxValue". The
input is state-controlled, i.e. as long as the "Preset" input is active, the "Pre‐
setValue" is copied to the "MaxValue" output variable.
If a "PresetValue" value is to be specified when the function is activated, the
"Preset" input has to be set simultaneously with the "Enable" input.

1210 /    ctrlX PLC Engineering
1344      Character strings without length limitation (StringFun_NoLimitStrLength)

Error codes
The function block IL_MaxValue does not generate any errors.

### 36.11.4 IL_COORD_PAIR_TYPE01

This data structure defines a two-dimensional coordinate with X- and Y-LREAL
values.

Type declaration

TYPE IL_COORD_PAIR_TYPE01 :
STRUCT
    X: LREAL := 0.0;                 // X coord
    Y: LREAL := 0.0;                 // Y coord
END_STRUCT
END_TYPE

Used in
● ⮫ Chapter 36.11.2 IL_InterpolationLinear on page 1207

## 36.12 Character strings without length limitation

(StringFun_NoLimitStrLength)

### 36.12.1 Introduction and overview

The following functions allow text processing/character string management
without length limitation.
Address and length of the character string are applied for example. It is proc‐
essed byte-by-byte.
The following applies:

Specification 1
Functions to process character strings, such as ⮫ Chapter 36.12.18 IL_LEFT
on page 1229 obtain the two outputs "SourceStr" and "DstStr".
"SourceStr" is the initial address of the source character string.
"DstStr" is the initial address of the target character string (result).
If "SourceStr" and "DstStr" are identical, the source character string is
changed and no copy is created. The function returns the address. The result
is stored in this address.
Table 1054: Example: IL_LEFT(SourceStr, DstStr, length, MaxLen)
Str1 := 'ABCDE';
L_LEFT(ADR(Str1), ADR(Str2), 3, 5); Return value of the function:
                                     ADR(Str2)
                                     Str1 = 'ABCDE'
                                     Str2 = 'ABC'

Str1 := 'ABCDE';
IL_LEFT(ADR (Str1), ADR (Str1), 3, 5); Return value of the function:
                                       ADR(Str1)
                                       Str1 = 'ABC'

Specification 2
A character string is accessed via pointer.

Character strings without length limitation (StringFun_NoLimitStrLength)       1344

The "MaxLen" input limits the character string length to avoid access to invalid
memory.
If the maximum number of characters "MaxLen" is reached, "DstStr" is com‐
pleted with "NUL". The "DstStr" address is returned by the function.
Table 1055: Example: IL_LEFT(SourceStr, DstStr, length, MaxLen)
Str1 := 'ABCDEFGHIJKLMN';
IL_LEFT(ADR(Str1), ADR(Str2), 10, 5); Return value of the function:
                                       ADR(Str2)
                                       Str1 = 'ABCDEFGHIJKLMN'
                                       Str2 = 'ABCDE'

Str1 := 'ABCDEFGHIJKLMN';
IL_LEFT(ADR (Str1), ADR (Str1), 10,     Return value of the function:
5);                                     ADR(Str1)
                                        Str1 = 'ABCDE'

CXA_Utilities, StringFun_NoLimitStrLength
Table 1056: Areas of application and functions/function blocks of CXA_Utilities
Area of application (folder in library)
Function blocks                                   Description
Capitalization
⮫ Chapter 36.12.2 IL_StrLower on page 1213        Function converts character string to lower case
                                                  letters
⮫ Chapter 36.12.3 IL_StrUpper on page 1214        Function converts character string to upper case
                                                  letters
Compare
⮫ Chapter 36.12.4 IL_StrCompare on page 1214 Function compares two character strings and
                                             returns the difference. Upper and lower case let‐
                                             ters considered
⮫ Chapter 36.12.5 IL_StrCompareNoCase        Function compares two character strings and
on page 1215                                 returns the difference. Upper and lower case let‐
                                             ters not considered
⮫ Chapter 36.12.6 IL_StrNCompare             Function compares the entered number of char‐
on page 1215                                 acters of two character strings and returns the
                                             difference. Upper and lower case letters consid‐
                                             ered
⮫ Chapter 36.12.7 IL_StrNCompareNoCase       Function compares the entered number of char‐
on page 1216                                 acters of two character strings and returns the
                                             difference. Upper and lower case letters not con‐
                                             sidered
Conversions
⮫ Chapter 36.12.8 IL_AsciiStreamToBase64     Function converts a character string, saved in
on page 1217                                 ASCII format, to the BASE64 format
⮫ Chapter 36.12.9 IL_Base64ToAsciiStream     Function converts a character string, saved in
on page 1218                                 BASE64 format, to the ASCII format
Copy
⮫ Chapter 36.12.12 IL_StrCopy on page 1224        Function copies character string from the source
                                                  to the target address

1212 /    ctrlX PLC Engineering
1344      Character strings without length limitation (StringFun_NoLimitStrLength)

⮫ Chapter 36.12.13 IL_StrNCopy on page 1224       Function copies partial character string from a
character string to a target character string.
Length of the target character string is specified.
If the source character string is shorter than the
requested length, the target character string is
supplemented by fill characters
IEC
⮫ Chapter 36.12.14 IL_CONCAT on page 1225         Function adds character string 2 behind char‐
acter string 1
⮫ Chapter 36.12.15 IL_DELETE on page 1226         Function deletes a partial character string from
the character string of a specified position
⮫ Chapter 36.12.16 IL_FIND on page 1227           Function searches for position of entered partial
character string in a character string
⮫ Chapter 36.12.17 IL_INSERT on page 1228         Function inserts a partial character string to a
character string starting from the entered posi‐
tion
⮫ Chapter 36.12.18 IL_LEFT on page 1229           Function provides the left part of a character
string with a length of x characters
⮫ Chapter 36.12.19 IL_LEN on page 1230            Function provides the character string length
⮫ Chapter 36.12.20 IL_MID on page 1230            Function provides a partial character string to
a character string starting from the entered posi‐
tion
⮫ Chapter 36.12.21 IL_REPLACE on page 1231        Function replaces a partial character string of
a character string by another partial character
string
⮫ Chapter 36.12.22 IL_RIGHT on page 1232          Function provides the right part of a character
string with a length of x characters
Numeric conversions (type conversion)
⮫ Chapter 36.12.23 IL_Ascii_To_Char               Function converts ASCII code to a character
on page 1233
⮫ Chapter 36.12.24 IL_Char_To_Ascii               Function converts a character to ASCII code
on page 1233
⮫ Chapter 36.12.25 IL_Int_To_Str on page 1234  Function converts (depending on format) an
integer to a character string
⮫ Chapter 36.12.27 IL_Real_To_Str on page 1234 Function converts (depending on format) a REAL
number to a character string
⮫ Chapter 36.12.29 IL_String_To_Unicode        Function converts a character string according
on page 1235                                   to the specified option (utf8/utf16) into Unicode
and stores the values in a DWORD array
⮫ Chapter 36.12.31 IL_Unicode_To_String        Function converts a Unicode character string
on page 1236                                   to a STRING according to the specified option
(utf8/utf16)
Other
⮫ Chapter 36.12.34 IL_StrInverse on page 1239 Function inverts a character string
⮫ Chapter 36.12.35 IL_StrSetEndOfString           Functions sets the end of a character string
on page 1240
Split
⮫ Chapter 36.12.36 IL_StrGetElement               The function is split into multiple elements by
on page 1241                                      the entered separator string. The function calls
one of the elements

Character strings without length limitation (StringFun_NoLimitStrLength)       1344

⮫ Chapter 36.12.37 IL_StrLChr on page 1242        Function isolates a partial character string from
                             the character string up to the first occurrence of
                             the entered separator
⮫ Chapter 36.12.38 IL_StrRChr on page 1242        Function isolates a partial character string from
                             the character string up to the last occurrence of
                             the entered separator
⮫ Chapter 36.12.39 IL_StrSetElement               Character string separated into elements by the
on page 1243                                      entered separator order. The function positions
                             a new element to the desired position in the
                             character string
⮫ Chapter 36.12.40 IL_StrSplit on page 1244       Character string separated by specified sepa‐
                             rator. The function stores the address of each

                             partial character string in an array
Trim
⮫ Chapter 36.12.41 IL_StrTrimAll on page 1245     Function deletes all specified characters in a
                             character string
⮫ Chapter 36.12.42 IL_StrTrimSpace                Depending on the option, the function deletes
on page 1246                                      spaces in a character string

### 36.12.2 IL_StrLower

Brief description
The IL_StrLower function converts all characters of a character string into
small letters.
Return value: Address of target character string.

Interface description

Table 1057: FUN IL_StrLower interface
Name           Type                          Comment
SourceStr      POINTER TO BYTE               Address of source character string
DstStr         POINTER TO BYTE               Address of target character string
MaxLen         UDINT                         Max. length of target character string (in bytes/Char)
Table 1058: Example 1
Str1: STRING := 'AbCDE';
Str2: STRING;
IL_StrLower(ADR(Str1), ADR(Str2), 5);             Return value: ADR(Str2)
                                                  Str2: 'abcde'
Table 1059: Example 2
Str1: STRING := 'AbCDE';
Str2: STRING;
IL_StrLower(ADR(Str1), ADR(Str2), 2);             Return value: ADR(Str2)
                                                  Str2: 'ab'

1214 /    ctrlX PLC Engineering
1344      Character strings without length limitation (StringFun_NoLimitStrLength)

Table 1060: Example 3
Str1: STRING := 'AbCDE';
Str2: STRING;
IL_StrLower(ADR(Str1), ADR(Str1), 5);               Return value: ADR(Str1)
                                                    Str1: 'abcde'

### 36.12.3 IL_StrUpper

Brief description
The IL_StrUpper function converts all characters of a character string into
capital letters.
Return value: Address of target character string.

Interface description

Table 1061: FUN IL_StrUpper interface
Name               Type                        Comment
SourceStr          POINTER TO BYTE             Address of source character string
DstStr             POINTER TO BYTE             Address of target character string
MaxLen             UDINT                       Max. length of target character string (in bytes/Char)
Table 1062: Example 1
Str1: STRING := 'aBcde';
Str2: STRING;
IL_StrUpper(ADR(Str1), ADR(Str2), 5);               Return value: ADR(Str2)
                                                    Str2: 'ABCDE'
Table 1063: Example 2
Str1: STRING := 'aBcde';
Str2: STRING;
IL_StrUpper(ADR(Str1), ADR(Str2), 2);               Return value: ADR(Str2)
                                                    Str2: 'AB'
Table 1064: Example 3
Str1: STRING := 'aBcde';
IL_StrUpper(ADR(Str1), ADR(Str1), 5);               Return value: ADR(Str1)
                                                    Str1: 'ABCDE'

### 36.12.4 IL_StrCompare

Brief description
The IL_StrCompare function compares two character strings and returns the
difference.
Upper and lower case letters considered. The difference is calculated using
the first non-identical characters.
If the two character strings are identical, 0 is returned.

Character strings without length limitation (StringFun_NoLimitStrLength)      1344

Interface description

Table 1065: FUN IL_StrCompare interface
Name           Type                          Comment
Str1           POINTER TO BYTE               Address of character string 1
Str2           POINTER TO BYTE               Address of character string 2

Table 1066: Example
Str1: STRING := 'abcde';
Str2: STRING := 'abCde';
IL_StrCompare (ADR(Str1), ADR(Str2));             Return value: 32

### 36.12.5 IL_StrCompareNoCase

Brief description
The IL_StrCompare function compares two character strings and returns the
difference.
Upper and lower case letters not considered. The difference is calculated
using the first non-identical characters.
If the two character strings are identical, 0 is returned.

Interface description

Table 1067: FUN IL_StrCompareNoCase interface
Name           Type                          Comment
Str1           POINTER TO BYTE               Address of character string 1
Str2           POINTER TO BYTE               Address of character string 2
Table 1068: Example
Str1: STRING := 'abcde';
Str2: STRING := 'ABEDE'
IL_StrCompareNoCase (ADR(Str1), ADR(Str2)); Return value: -2

### 36.12.6 IL_StrNCompare

Brief description
The IL_StrNCompare function compares partial character strings of two char‐
acter strings and returns the difference.
Upper and lower case letters considered.
The difference is calculated using the first non-identical characters.
If the two character strings are identical, 0 is returned.

1216 /    ctrlX PLC Engineering
1344      Character strings without length limitation (StringFun_NoLimitStrLength)

Interface description

Table 1069: FUN IL_StrNCompare interface
Name               Type                        Comment
Str1               POINTER TO BYTE             Address of character string 1
Str2               POINTER TO BYTE             Address of character string 2
n                  UDINT                       Number of characters to be compared
Table 1070: Example 1
Str1: STRING := 'abcde';
Str2: STRING := 'abCde'
IL_StrNCompare (ADR(Str1), ADR(Str2), 3);          Return value: 32
Table 1071: Example 2
Str1: STRING := 'abcde';
Str2: STRING := 'abCde';
IL_StrNCompare (ADR(Str1), ADR(Str2), 2);          Return value: 0

### 36.12.7 IL_StrNCompareNoCase

Brief description
The IL_StrNCompareNoCase function compares partial character strings of
two character strings and returns the difference.
Upper and lower case letters not considered.
The difference is calculated using the first non-identical characters.
If the two character strings are identical, 0 is returned.

Interface description

Table 1072: FUN IL_StrNCompareNoCase interface
Name               Type                        Comment
Str1               POINTER TO BYTE             Address of character string 1
Str2               POINTER TO BYTE             Address of character string 2
n                  UDINT                       Number of characters to be compared
Table 1073: Example 1
Str1: STRING := 'abcde';
Str2: STRING := 'abEde';
IL_StrNCompareNoCase (ADR(Str1), ADR(Str2), Return value: -2
3);

   Character strings without length limitation (StringFun_NoLimitStrLength)         1344

Table 1074: Example 2
Str1: STRING := 'abcde';
Str2: STRING := 'abCde';
IL_StrNCompareNoCase (ADR(Str1), ADR(Str2), Return value: 0
3);

### 36.12.8 IL_AsciiStreamToBase64

      Brief description
      The IL_AsciiStreamToBase64 function is used to convert a character string
      saved in ASCII format to ⮫ BASE64 format.

      Interface description

Table 1075: IL_AsciiStreamToBase64 function
               Name               Type              Comment
VAR_INPUT      NoOfConvert‐                         Number of bytes to be converted in the
                                  UINT
               Bytes                                "StreamBuffer"
                                                    Pointer to the ASCII character string to be con‐
                                  POINTER        TO verted
               StreamBuffer
                                  BYTE
                                                    Use the ADR ( ) operator
               SizeOfStream‐                        (Maximum) size of the input “StreamBuffer”
                                  UINT
               Buffer                               Use the SIZEOF ( ) operator.
                                                    Pointer to the buffer of the BASE64-converted
                                  POINTER        TO data
               Base64Buffer
                                  BYTE
                                                    Use the ADR ( ) operator
               SizeOf‐                              (Maximum) size of the output BASE64 buffer
                                  UINT
               Base64Buffer                         Use the SIZEOF ( ) operator.
VAR_OUTPUT NoOf‐                                    Number of bytes in the BASE64 buffer output
                                  UINT
           Base64Bytes                              as converted result
RETURN                            BOOL              Processing is executed.

      Functional description
      The IL_AsciiStreamToBase64 function is used to convert a character string
      saved in ASCII format to ⮫ BASE64 format.
      Source data is transferred to the "StreamBuffer" and the converted data is
      saved to the "Base64Buffer".
      "NoOfConvertBytes" contains the number of bytes to be converted provided in
      the "StreamBuffer".
      The (maximum) size of the "StreamBuffer" is specified in "SizeOfStream‐
      Buffer".

      After the conversion, the result is available in "Base64Buffer".

1218 /    ctrlX PLC Engineering
1344      Character strings without length limitation (StringFun_NoLimitStrLength)

The user has to ensure further processing of "Base64Buffer" data before the
next data set is converted.
The (maximum) size of the "Base64Buffer" is specified in "SizeOf‐
Base64Buffer".

The "NoOfBase64Bytes" outputs provides the number of converted and saved
bytes in the "Base64Buffer".

The return value "IL_AsciiStreamToBase64" of type BOOL includes information
on the success of the function call:
TRUE is output if the conversion was successful.
FALSE is output if data was not completely converted or if "SizeOfStream‐
Buffer" and "SizeOfBase64Buffer" do not match one another.
Only compatible data is converted.

Examples
The IL_AsciiStreamToBase64 function is used to convert an ASCII character
string to BASE64 format.
The return value of type BOOL provides information on the success of the
operation.

VAR
 bIL_AsciiStreamToBase64: BOOL;
 uiNoOfConvertBytes: UINT := UINT#3;
 arStreamBuffer: STRING(96) := 'Man';
 uiNoOfBase64Bytes : UINT;
 arBase64Buffer : STRING(128);
END_VAR

bIL_AsciiStreamToBase64 := IL_AsciiStreamToBase64(
 NoOfConvertBytes:= uiNoOfConvertBytes,
 StreamBuffer:= ADR(arStreamBuffer),
 SizeOfStreamBuffer:= SIZEOF(arStreamBuffer),
 Base64Buffer:= ADR(arBase64Buffer),
 SizeOfBase64Buffer:= SIZEOF(arBase64Buffer),
 NoOfBase64Bytes=> uiNoOfBase64Bytes);

The result of the example "IL_AsciiStreamToBase64" is shown in the following:

### 36.12.9 IL_Base64ToAsciiStream

Brief description
The IL_Base64ToAsciiStream function is used to convert a character string
saved in ⮫ BASE64 format to ASCII format.

   Character strings without length limitation (StringFun_NoLimitStrLength)      1344

      Interface description

Table 1076: IL_Base64ToAsciiStream function

Name              Type              Comment
VAR_INPUT      NoOf‐                               Number of bytes to be converted in the
                  UINT
Base64Bytes                         Base64Buffer
                                    Pointer to the BASE64 character string to be
                  POINTER        TO converted
Base64Buffer
                  BYTE
                                    Use the ADR ( ) operator.
SizeOf‐                             (Maximum) size of the output "Base64Buffer"
                  UINT
Base64Buffer                        Use the SIZEOF ( ) operator
                                    Pointer to the buffer of the ASCII-converted
                  POINTER        TO data
OutputBuffer
                  BYTE
                                    Use the ADR ( ) operator.
SizeOfOutput‐                       Size of the OutputBuffer
                  UINT
Buffer                              Use the SIZEOF ( ) operator
VAR_OUTPUT NoOfConvert‐                            Number of bytes in the OutputBuffer output as
                  UINT
Bytes                                   converted result
RETURN                           BOOL              Processing is executed.

      Functional description
      The IL_Base64ToAsciiStream function is used to convert a character string
      saved in ⮫ BASE64 format to ASCII format.
      Source data is transferred to the "Base64Buffer" and the converted data is
      saved to the "OutputBuffer".
      "NoOfBase64Bytes" contains the number of data to be converted provided in
      the "Base64Buffer".
      The (maximum) size of the "Base64Buffer" is specified in "SizeOf‐
      Base64Buffer".

      After the conversion, the result is available in "OutputBuffer".
      The user has to ensure further processing of "OutputBuffer" data before the
      next data set is converted.
      The (maximum) size of the "OutputBuffer" is specified in "SizeOfOutput‐
      Buffer".

      The "NoOfConvertBytes" outputs provides the number of converted and saved
      bytes in the "OutputBuffer".
      The return value "IL_Base64ToAsciiStream" of type BOOL includes information
      on the success of the function call:
      TRUE is output if the conversion was successful.

1220 /    ctrlX PLC Engineering
1344      Character strings without length limitation (StringFun_NoLimitStrLength)

FALSE is output if data was not completely converted or if "SizeOf‐
Base64Buffer" and "SizeOfOutputBuffer" do not match one another.
Only compatible data is converted.

Examples
The IL_Base64ToAsciiStream function is used to convert a character string
saved in ⮫ BASE64 format to ASCII format.
The return value of type BOOL provides information on the success of the
operation.

VAR
 bIL_Base64ToAsciiStream: BOOL;
 uiNoOfBase64Bytes : UINT :=4;
 arBase64Buffer : STRING(128) :='TWFu';
 uiNoOfConvertBytes: UINT;
 arOutputBuffer: STRING(96);
END_VAR

bIL_Base64ToAsciiStream := IL_Base64ToAsciiStream(
        NoOfBase64Bytes:= uiNoOfBase64Bytes,
        Base64Buffer:= ADR(arBase64Buffer),
        SizeOfBase64Buffer:= SIZEOF(arBase64Buffer),
        OutputBuffer:= ADR(arOutputBuffer),
        SizeOfOutputBuffer:= SIZEOF(arOutputBuffer),
        NoOfConvertBytes=> uiNoOfConvertBytes);

The result of the example "IL_Base64ToAsciiStream" is shown in the following:

### 36.12.10 IL_BufferToString

Brief description
The IL_BufferToString function copies an ASCII character string from a byte
array.

Interface description

Character strings without length limitation (StringFun_NoLimitStrLength)        1344

Table 1077: IL_BufferToString function
               Name              Type              Comment
VAR_INPUT      BufferAdr         POINTER        TO (Initial) address of the byte array buffer
                                 BYTE              Use the ADR ( ) operator
               SizeOfBuffer      UINT              Size of the byte array buffer
                                                   Use the SIZEOF ( ) operator
               StartPosition     UINT              Starting position of the character string in the
                                                   byte array buffer
               EndPosition       UINT              End position of the character string in the byte
                                                   array buffer
               StringAdr         POINTER        TO Pointer to copied character string

            STRING            Use the ADR( ) operator
SizeOfString      UINT              Maximum permissible size of the character
                              string
                              Use the SIZEOF ( ) operator
                              SizeOF(StringAdr)
RETURN                           BOOL              Conversion completed

Functional description
The IL_BufferToString function copies an ASCII character string from a byte
array.
"BufferAdr" contains the (starting) address of the provided byte array.
"StartPosition" includes the starting position of the character string in the
array.
"EndPosition" contains the position of the latest character to be read in the
array.

The function queries a character string from a byte array starting at "StartPosi‐
tion" and ending at "EndPosition".
The retrieved character string is saved under "StringAdr".
The maximum length of the retrievable character string is specified under
"SizeOfString".

The return value of the "IL_BufferToString" function of type BOOL confirms
the conversion.
TRUE is output if copying was successful.
FALSE is output if copying was not successful, e.g. if "SizeOfBuffer" and
"SizeOfString" do not match.
Only compatible data is copied.

Examples
The IL_BufferToString function copies an ASCII character string from a byte
array.

VAR
 bIL_BufferToString : BOOL;
 strIL_BufferToString: STRING(300);
 arBufferAdr: ARRAY [0..300] OF BYTE:=
[63,64,65,66,67,68,69,70,71,72,73];
END_VAR

1222 /    ctrlX PLC Engineering
1344      Character strings without length limitation (StringFun_NoLimitStrLength)

     bIL_BufferToString := IL_BufferToString(BufferAdr:=
     ADR(arBufferAdr),
      SizeOfBuffer:=SIZEOF(arBufferAdr), StartPosition:=2,
     EndPosition:=8,
      StringAdr:= ADR(strIL_BufferToString),
      SizeOfString:= SIZEOF(strIL_BufferToString));

     The result of the example "IL_BufferToString" is shown in the following:

### 36.12.11 IL_StringToBuffer

     Brief description
     The IL_StringToBuffer function copies an ASCII character string to a byte array.

     Interface description

Table 1078: IL_StringToBuffer function
                   Name             Type              Comment
VAR_INPUT          InputData        POINTER        TO Pointer to the character string to be converted
                                    STRING            Use the ADR ( ) operator
                   LenOfInputData UDINT               Length of the input character string
                                                      Use IL_Len (InputData)
                   Position         UINT              Starting position of the character string in the
                                                      byte array buffer
                   BufferAdr        POINTER        TO Address of the byte array buffer
                                    BYTE              Use the ADR ( ) operator
                   SizeOfBuffer     UINT              Size of the byte array buffer.
                                                      Use the SIZEOF ( ) operator

Character strings without length limitation (StringFun_NoLimitStrLength)         1344

Name               Type              Comment
RETURN                           UINT              End position of the character string in the byte
                               array buffer

Functional description
The IL_StringToBuffer function copies an ASCII character string to a byte array.
"InputData" contains the pointer to the character string to be copied.
The number of characters is specified in "LenOfInputData". It is to be deter‐
mined using the "IL_Len" function.

The function also retrieves the character string and stores it in the "BufferAdr"

array.
"Position" is the starting position for the storage of the character string in the
"BufferAdr" array.
The first character in the "BufferAdr" array is provided with the position
number 0.

The return value "IL_StringToBuffer" of type UINT returns the position of the
latest copied character.
In case of error, if e.g. "SizeOfBuffer" and "LenOfInputData" do not match,
copying is canceled.
Only compatible data is copied.

Examples
The IL_StringToBuffer function copies an ASCII character string to a byte array.

VAR
 strInputData: STRING(300) :='ABCDEFGH';
 uiIL_StringToBuffer: UINT;
 arBufferAdr: ARRAY [0..300] OF BYTE;
END_VAR

uiIL_StringToBuffer :=
IL_StringToBuffer(InputData:=ADR(strInputData),
 LenofInputData := IL_LEN(ADR(strInputData)), Position:=4,
 BufferAdr:=ADR(arBufferAdr) , SizeOfBuffer:=
SIZEOF(arBufferAdr));

The result of the example "IL_StringToBuffer" is shown in the following:

1224 /    ctrlX PLC Engineering
1344      Character strings without length limitation (StringFun_NoLimitStrLength)

### 36.12.12 IL_StrCopy

Brief description
The IL_StrCopy function copies a character string from source to target
address.
Return value: Address of target character string.

Interface description

Table 1079: FUN IL_StrCopy interface
Name               Type                        Comment
SourceStr          POINTER TO BYTE             Address of source character string
DstStr             POINTER TO BYTE             Address of target character string
MaxLen             UDINT                       Max. length of target character string (in bytes/Char)
Table 1080: Example
Str1: STRING := 'abcde';
Str2: STRING;
IL_StrCopy (ADR(Str1), ADR(Str2), 5);               Return value: ADR(Str2)
                                                    Str2: 'abcde'

### 36.12.13 IL_StrNCopy

Brief description
The IL_StrNCopy function copies a partial character string from a character
string to the target address.
Length of the target character string is specified with "MaxLen".

Character strings without length limitation (StringFun_NoLimitStrLength)        1344

If the source character string is shorter than the entered length, the target
character string is supplemented by fill characters
Return value: Address of target character string.

Interface description

Table 1081: FUN IL_StrNCopy interface
Name           Type                           Comment
SourceStr      POINTER TO BYTE                Address of source character string
DstStr         POINTER TO BYTE                Address of target character string
CharNum        UDINT                          Length of the target character string (in bytes/Char)
strCharFill    STRING[1]                      Fill character
MaxLen         UDINT                          Max. length of target character string (in bytes/Char)
Table 1082: Example 1
Str1: STRING := 'abcde';
Str2: STRING;
IL_StrNCopy (ADR(Str1), ADR(Str2), 7, 'F'，10); Return value: ADR(Str2)
                                               Str2: 'abcdeFF'
Table 1083: Example 2
Str1: STRING := abcde;
Str2: STRING;
IL_StrNCopy (ADR(Str1), ADR(Str2), 7, 'F', 6);     Return value: ADR(Str2)
                                                   Str2: 'abcdeF'
Table 1084: Example 3
Str1: STRING := abcde;
Str2: STRING;
IL_StrNCopy (ADR(Str1), ADR(Str2), 3, 'F',10);     Return value: ADR(Str2)
                                                   Str2: 'abc'

### 36.12.14 IL_CONCAT

Brief description
The IL_CONCAT function adds character string 2 behind character string 1.
The result cannot be saved under the address of character string 2.

Return value: Address of target character string.

1226 /    ctrlX PLC Engineering
1344      Character strings without length limitation (StringFun_NoLimitStrLength)

Interface description

Table 1085: FUN IL_CONCAT interface
Name               Type                        Comment
Str1               POINTER TO BYTE             Address of character string 1
Str2               POINTER TO BYTE             Address of character string 2
DstStr             POINTER TO BYTE             Address of target character string
MaxLen             UDINT                       Max. length of target character string (in bytes/Char)

Table 1086: Example 1
Str1: STRING := 'ABCD';
Str2: STRING := 'EFGH';
Str3: STRING;
IL_CONCAT(ADR(Str1), ADR(Str2), ADR(Str3),          Return value: ADR(Str3)
10);
                                                    Str3: 'ABCDEFGH'
Table 1087: Example 2
Str1: STRING := 'ABCD';
Str2: STRING := 'EFGH';
Str3: STRING;
IL_CONCAT(ADR(Str1), ADR(Str2), ADR(Str3),          Return value: ADR(Str3)
2);
                                                    Str3: 'AB'
Table 1088: Example 3
Str1: STRING := 'ABCD';
Str2: STRING := 'EFGH';
IL_CONCAT(ADR(Str1), ADR(Str2), ADR(Str1),          Return value: ADR(Str1)
10);
                                                    Str1: 'ABCDEFGH'

### 36.12.15 IL_DELETE

Brief description
The IL_DELETE function deletes a partial character string from a character
string from a specified position.
The first character of the character string counted from the left is on position
1.
Return value: Address of target character string.

Character strings without length limitation (StringFun_NoLimitStrLength)        1344

Interface description

Table 1089: FUN IL_DELETE interface
Name           Type                           Comment

SourceStr      POINTER TO BYTE                Address of source character string
DstStr         POINTER TO BYTE                Address of target character string
                         Length of the partial character string to be removed
Length         UDINT                          (in bytes/Char)
                         Position of the source character string to start the
Position       UDINT                          removal of the partial character string
MaxLen         UDINT                          Max. length of target character string (in bytes/Char)
Table 1090: Example 1
Str1: STRING := 'ABCDEFGH';
Str2: STRING;
IL_DELETE (ADR(Str1), ADR(Str2), 4, 3, 5);         Return value: ADR(Str2)
                                                   Str2: 'ABGH'
Table 1091: Example 2
Str1: STRING := 'ABCDEFGH';
Str2: STRING;
IL_DELETE (ADR(Str1), ADR(Str2), 4, 3, 2);         Return value: ADR(Str2)
                                                   Str2: 'AB'
Table 1092: Example 3
Str1: STRING := 'ABCDEFGH';
IL_DELETE (ADR(Str1), ADR(Str1), 4, 3, 5);         Return value: ADR(Str1)
                                                   Str1: 'ABGH'

### 36.12.16 IL_FIND

Brief description
The IL_FIND searches for the initial position of the specified partial character
string in a character string. The first character of the character string counted
from the left is on position 1.
The position is provided as return of the function.

Interface description

1228 /     ctrlX PLC Engineering
1344       Character strings without length limitation (StringFun_NoLimitStrLength)

Table 1093: FUN IL_FIND interface
Name               Type                        Comment
Str1               POINTER TO BYTE             Address of source character string
                                               Address of the partial character string to be searched
Str2               POINTER TO BYTE             for
Table 1094: Example
Str1: STRING := 'ABCDEFGH';
Str2: STRING := 'CDEF';
IL_FIND (ADR(Str1), ADR(Str2));                     Return value: 3

### 36.12.17 IL_INSERT

Brief description
The IL_INSERT inserts a partial character string starting from a specified posi‐
tion in the character string.
The first character of the character string counted from the left is on position
1.
Return value: Address of the target character string.

Interface description

Table 1095: FUN IL_INSERT interface
Name               Type                        Comment
SourceStr          POINTER TO BYTE             Address of source character string
DstStr             POINTER TO BYTE             Address of target character string
InsertStr          POINTER TO BYTE             Address of the partial character string to be inserted
                                               Position of the source character string to start the
Position           UDINT                       insertion of the partial character string from
MaxLen             UDINT                       Max. length of target character string (in bytes/Char)
Table 1096: Example 1
Str1: STRING := 'ABCD';
Str2: STRING;
Str3: STRING := 'EFGH';
IL_INSERT(ADR(Str1), ADR(Str2), ADR(Str3), 3, Return value: ADR(Str2)
10);
                                              Str2: 'ABEFGHCD'

Character strings without length limitation (StringFun_NoLimitStrLength)            1344

Table 1097: Example 2
Str1: STRING := 'ABCD';
Str2: STRING;
Str3: STRING := 'EFGH';
IL_INSERT(ADR(Str1), ADR(Str2), ADR(Str3), 3, Return value: ADR(Str2)
2);
                                              Str2: 'AB'
Table 1098: Example 3
Str1: STRING := 'ABCD';
Str3: STRING := 'EFGH';
IL_INSERT(ADR(Str1), ADR(Str1), ADR(Str3), 3, Return value: ADR(Str1)

10);
                         Str1: 'ABEFGHCD'

### 36.12.18 IL_LEFT

Brief description
The IL_LEFT provides the left partial character string of a character string.
Return value: Address of target character string.

Interface description

Table 1099: FUN IL_LEFT interface
Name           Type                           Comment
SourceStr      POINTER TO BYTE                Address of source character string
DstStr         POINTER TO BYTE                Address of target character string
                                              Length of the left partial character string
Length         UDINT                          (in Byte/Char)
MaxLen         UDINT                          Max. length of target character string (in bytes/Char)
Table 1100: Example 1
Str1: STRING := 'ABCD';
Str2: STRING;
IL_LEFT(ADR(Str1), ADR(Str2), 3, 5);               Return value: ADR(Str2)
                                                   Str2: 'ABC'
Table 1101: Example 2
Str1: STRING := 'ABCD';
Str2: STRING;
IL_LEFT(ADR(Str1), ADR(Str2), 3, 2);               Return value: ADR(Str2)
                                                   Str2: 'AB'

1230 /     ctrlX PLC Engineering
1344       Character strings without length limitation (StringFun_NoLimitStrLength)

Table 1102: Example 3
Str1: STRING := 'ABCD';
IL_LEFT(ADR(Str1), ADR(Str1), 3, 5);                Return value: ADR(Str1)
                                                    Str1: 'ABC'

### 36.12.19 IL_LEN

Brief description
The IL_LEN function provides the length of the character string (number of
characters).

Interface description

Table 1103: FUN IL_LEN interface
Name               Type                        Comment
Str                POINTER TO BYTE             Address of character string
Table 1104: Example
Str1: STRING := 'ABCDEFGH';
IL_LEN(ADR(Str1));                                  Return value: 8

### 36.12.20 IL_MID

Brief description
The IL_MID functions provides a partial character string of specified length
starting from the specified position of a character string.
The position corresponds to the character number. The first character of the
character string counted from the left is on position 1.
Return value: Address of target character string.

Interface description

Table 1105: FUN IL_MID interface
Name               Type                        Comment
SourceStr          POINTER TO BYTE             Address of source character string
DstStr             POINTER TO BYTE             Address of target character string
Length             UDINT                       Length of the partial character string (in bytes/Char)
                                               Position of the source character string to start calling
Position           UDINT                       the partial character string from
MaxLen             UDINT                       Max. length of target character string (in bytes/Char)

Character strings without length limitation (StringFun_NoLimitStrLength)       1344

Table 1106: Example 1
Str1: STRING := 'ABCDEFGH';
Str2: STRING;
IL_MID(ADR(Str1), ADR(Str2), 4, 3, 10);           Return value: ADR(Str2)
                                                  Str2: 'CDEF'
Table 1107: Example 2
Str1: STRING := 'ABCDEFGH';
Str2: STRING;
IL_MID(ADR(Str1), ADR(Str2), 4, 3, 2);            Return value: ADR(Str2)
                                                  Str2: 'CD'

Table 1108: Example 3
Str1: STRING := 'ABCDEFGH';
IL_MID(ADR(Str1), ADR(Str1), 4, 3, 10);           Return value: ADR(Str1)
                                                  Str1: 'CDEF'

### 36.12.21 IL_REPLACE

Brief description
The IL_REPLACE replaces a partial character string of a character string with a
substitute character string.
Return value: Address of target character string.

Interface description

Table 1109: FUN IL_REPLACE interface
Name           Type                          Comment
SourceStr      POINTER TO BYTE               Address of source character string
DstStr         POINTER TO BYTE               Address of target character string
                                             Address of the partial character string to be inserted
ReplaceStr     POINTER TO BYTE               (substitute character string)
                                             Length of the partial character string to be removed
Length         UDINT                         (in bytes/Char)
                                             The position of the source character string from
                                             which the partial character string is to be replaced
Position       UDINT                         by the substitute character string
MaxLen         UDINT                         Max. length of target character string (in bytes/Char)

1232 /    ctrlX PLC Engineering
1344      Character strings without length limitation (StringFun_NoLimitStrLength)

Table 1110: Example 1
Str1: STRING := 'ABCDE';
Str2: STRING;
Str3: STRING := 'XX';
IL_REPLACE(ADR(Str1), ADR(Str2), ADR(Str3),          Return value: ADR(Str2)
3, 2, 5);
                                                     Str3: 'AXXE'
Table 1111: Example 2
Str1: STRING := 'ABCDE';
Str2: STRING;
Str3: STRING := 'XX';
IL_REPLACE(ADR(Str1), ADR(Str2), ADR(Str3),          Return value: ADR(Str2)
3, 2, 2);
                                                     Str3: 'AX'
Table 1112: Example 3
Str1: STRING := 'ABCDE';
Str3: STRING := 'XX';
IL_REPLACE(ADR(Str1), ADR(Str1), ADR(Str3),          Return value: ADR(Str1)
3, 2, 5);
                                                     Str1: 'AXXE'

### 36.12.22 IL_RIGHT

Brief description
The IL_RIGHT provides the right partial character string of a character string.
Return value: Address of target character string.

Interface description

Table 1113: FUN IL_RIGHT interface
Name               Type                         Comment
SourceStr          POINTER TO BYTE              Address of source character string
DstStr             POINTER TO BYTE              Address of target character string
                                                Length of the right partial character string (in bytes/
Length             UDINT                        Char)
MaxLen             UDINT                        Max. length of target character string (in bytes/Char)
Table 1114: Example 1
Str1: STRING := 'ABCD';
Str2: STRING;
IL_RIGHT(ADR(Str1), ADR(Str2), 3, 5);                Return value: ADR(Str2)
                                                     Str2: 'BCD'

Character strings without length limitation (StringFun_NoLimitStrLength)       1344

Table 1115: Example 2
Str1: STRING := 'ABCD';
Str2: STRING;
IL_RIGHT(ADR(Str1), ADR(Str2), 3, 2);              Return value: ADR(Str2)
                                                   Str2: 'BC'
Table 1116: Example 3
Str1: STRING := 'ABCD';
IL_RIGHT(ADR(Str1), ADR(Str1), 3, 5);              Return value: ADR(Str1)
                                                   Str1: 'BCD'

### 36.12.23 IL_Ascii_To_Char

Brief description
The IL_Ascii_To_Char function converts ASCII code to a character.
Return value: Characters

Interface description

Table 1117: FUN IL_Ascii_To_Char interface
Name           Type                           Comment
Ascii          BYTE                           ASCII code to be converted
Table 1118: Example
IL_ Ascii_to_Char (16#63);                         Return value: 'c'
IL_ Ascii_to_Char (99);                            Return value: 'c'

### 36.12.24 IL_Char_To_Ascii

Brief description
The IL_Char_To_Ascii function converts a character to ASCII.
Return value: ASCII code.

Interface description

Table 1119: FUN IL_Char_To_Ascii interface
Name           Type                           Comment
Char           STRING[1]                      Character to be converted
Table 1120: Example
IL_Char_To_Ascii ('c')                             Return value: 16#63
IL_Char_To_Ascii ('c')                             Return value: 99

1234 /    ctrlX PLC Engineering
1344      Character strings without length limitation (StringFun_NoLimitStrLength)

### 36.12.25 IL_Int_To_Str

Brief description
The IL_Int_To_Str functions converts an integer (depending on format) to a
character string.
Return value: Character string.

Interface description

Table 1121: FUN IL_Int_To_Str interface
Name               Type                           Comment
iInt               INT                            Integer to be converted
                                                  Selection of digit representation in the character
Format             ⮫ ENUM_INT_OPTION              string
Table 1122: Example 1
IL_Int_To_Str (10, EN_OPT_BIN);                         Return value: '1010'
Table 1123: Example 2
IL_Int_To_Str (10, EN_OPT_DEZ);                         Return value: '10'
Table 1124: Example 3
IL_Int_To_Str (10, EN_OPT_HEX);                         Return value: 'A'

### 36.12.26 ENUM_INT_OPTION

The enumeration type ENUM_INT_OPTION allows to select the representation
of the integer in the character string.

ENUM_INT_OPTION elements
Table 1125: ENUM_INT_OPTION elements
Name                      Value                      Description
EN_OPT_BIN                0                          Binary number
EN_OPT_DEZ                1                          Decimal number
EN_OPT_HEX                2                          Hexadecimal number

### 36.12.27 IL_Real_To_Str

Brief description
The IL_Real_To_Str function converts (depending on format) a REAL number
(max. seven significant positions) to a character string.
Return value: Address of target character string.

Character strings without length limitation (StringFun_NoLimitStrLength)      1344

Interface description

Table 1126: FUN IL_Real_To_Str interface
Name             Type                          Comment
Value            REAL                          REAL number to be converted

Str              POINTER TO BYTE               Address of target character string
Num              UINT                          Number of decimal places to be displayed
                        Selection of digit representation in the character
Opt              ⮫ ENUM_REAL_OPTION            string
Table 1127: Example 1
IL_Real_To_Str (263.355, 2, EN_OPT_FLOATING); Return value: '263.36'
Table 1128: Example 2
IL_Real_To_Str (263.355, 2, EN_OPT_EXP);             Return value: '2.63E+2'
Table 1129: Example 3
IL_Real_To_Str (263.355, 0, EN_OPT_ENGI‐             Return value: '263*10^0'
NEERING);
IL_Real_To_Str (263.355, 2, EN_OPT_ENGI‐             Return value: '2.63*10^+3'
NEERING);

### 36.12.28 ENUM_REAL_OPTION

The enumeration type ENUM_REAL_OPTION allows to select the representa‐
tion of the REAL number in the character string.

ENUM_REAL_OPTION elements
Table 1130: ENUM_REAL_OPTION elements
Name                      Value                     Description
EN_OPT_FLOATING           0                         Floating point representa‐
                                                    tion
EN_OPT_EXP                1                         Exponential representa‐
                                                    tion
EN_OPT_ENGINEERING        2                         Engineer representation

### 36.12.29 IL_String_To_Unicode

Brief description
The IL_String_To_Unicode function converts a character string according to the
specified option (utf8/utf16) into Unicode and stores the values in a DWORD
array.
Only 1 byte of memory space is reserved for each string character. Thus, the
characters matching ASCII code and Windows 1252 can be identified.

1236 /    ctrlX PLC Engineering
1344      Character strings without length limitation (StringFun_NoLimitStrLength)

Interface description

Table 1131: FUN IL_String_To_Unicode interface
Name               Type                        Comment
Str                POINTER TO BYTE             Address of source character string
pArray             POINTER TO DWORD            Address of target array
SizeOfArray        UDINT                       Max. size of array (in bytes)
Opt                ⮫ ENUM_OPT_UTF              Unicode coding format
Table 1132: Example 1
Str1: STRING := 'ABÝæ';
arArray: Array[0..3] OF DWORD;
IL_String_To_Unicode (ADR(Str1), ADR(arArray), Return value: ADR(arArray)
4, EN_UTF8);
                                               arArray[0]: 16#41
                                               arArray[1]: 16#42
                                               arArray[2]: 16#E6
                                               arArray[3]: 16#DD
Table 1133: Example 2
Str1: STRING := 'ABÝæ';
arArray: Array[0..3] OF DWORD;
IL_String_To_Unicode (ADR(Str1), ADR(arArray), Return value: ADR(arArray)
4, EN_UTF16);
                                               arArray[0]: 16#41
                                               arArray[1]: 16#42
                                               arArray[2]: 16#C39D
                                               arArray[3]: 16#C3A6

### 36.12.30 ENUM_OPT_UTF

The enumeration type ENUM_OPT_UTF, type INT, allows to select the Unicode
coding format.

ENUM_OPT_UTF elements
Table 1134: ENUM_OPT_UTF elements
Name                     Value                     Description
EN_UTF16                 0                         UTF16 code
EN_UTF8                  1                         UTF8 code

### 36.12.31 IL_Unicode_To_String

Brief description
The IL_Unicode_To_String function converts Unicode to STRING.
Unicode is stored in a DWORD array. One array element corresponds to one
Unicode character.

Character strings without length limitation (StringFun_NoLimitStrLength)      1344

Only 1 byte of memory space is reserved for each string character. Thus, the
characters matching ASCII code and Windows 1252 can be identified.
Return value: Address of target character string.

Interface description

Table 1135: FUN IL_Unicode_To_String interface
Name             Type                          Comment
pArray           POINTER TO DWORD              Address of the source array
SizeOfArray      UDINT                         Max. size of array (in bytes)
Str              POINTER TO BYTE               Address of target character string
Opt              ⮫ ENUM_OPT_UTF                Unicode coding format
Table 1136: Example 1
arArray: Array[0..3] of DWORD := [16#41, 16#42, 16#E6, 16#DD];
Str1: STRING;
IL_Unicode_To_String (ADR(arArray), 4,          Return value: ADR(Str1)
ADR(Str1), 4, EN_UTF8);
                                                Str1: 'ABÝæ'
Table 1137: Example 2
arArray: Array[0..3] of DWORD := [16#41, 16#42, 16#C39D, 16#C3A6];
Str1: STRING;
IL_String_To_Unicode (ADR(Str1), ADR(arArray), Return value: ADR(Str1)
4, EN_UTF16);
                                                Str1: 'ABÝæ'

### 36.12.32 IL_BufferGetElementCount

Brief description
The function IL_BufferGetElementCount specifies the number of objects in the
character string separated by a "separator" character.

Interface description

Table 1138: IL_BufferGetElementCount function
                 Name              Type              Comment
VAR_INPUT                                            ASCII separator in the character string to be
                 Separator         BYTE
                                                     analyzed

1238 /    ctrlX PLC Engineering
1344      Character strings without length limitation (StringFun_NoLimitStrLength)

Name            Type              Comment
            POINTER        TO Pointer to the character string to be converted
InputData
            BYTE              Use the ADR( ) operator
                              Total length of the character string
SizeOfInputData UINT              Use the function IL_Len( ) and the operator
                              ADR( ) for the character string to be analyzed
RETURN                             UINT              Number of separated objects

Functional description
The function IL_BufferGetElementCount specifies the number of objects in the
character string separated by a "separator" character.
Example: Character string: '0/123/2/3', separator: /, return value: 4.
If there is only one character in the "InputData" character string, no "sepa‐
rator" is required.
1 is output as return value of the function, e.g. ('X',/) = 1.
If "InputData" is an empty character string, 0 is output as return value of the
function, e.g. ('',/) = 0.

Examples
The function IL_BufferGetElementCount specifies the number of objects in the
character string separated by a "separator" character.

VAR
 strInputString:   STRING(300) ;
 uiNoOfCharacters: UINT;
END_VAR

strInputString := '1/2/333/4/a/b/C/D/!/@/</;/,/{/[';

uiNoOfCharacters := IL_BufferGetElementCount(
 Separator:= IL_AsciiToByte('/'),
 InputData:= ADR(strInputString),
 SizeOfInputData := UDINT_TO_UINT (IL_Len(ADR(strInputStrin

The result of the example "IL_BufferGetElementCount" is shown in the fol‐
lowing:

### 36.12.33 IL_Code

Brief description
The IL_Code function determines the ASCII code of a specified character in a
character string in decimal representation

Character strings without length limitation (StringFun_NoLimitStrLength)        1344

Interface description

Table 1139: IL_Code function
               Name               Type              Comment
VAR_INPUT      InputData          POINTER        TO Pointer to an ASCII character string

             STRING            Use the ADR( ) operator
LenOfInputData UDINT                 String length
                               Use: IL_Len (InputData)
Position           UDINT             Position at which the character is read
RETURN                            BYTE              Code of the character at the "Position"

Functional description
The IL_Code function determines the ASCII code of a specified character in a
character string in decimal representation
The position of the character is specified by the "Position" value. The first
character of the character string has the position 1.
If IL_Code is called with a "position" smaller than 1 or greater that the length
of the "LenOfInputData" character string, 0 returns.
Calculate "LenOfInputData" using the IL_Len function.
Example:
IL_Code ('ABC 123', 4) results in 32 (the blank is coded with the value 32).
The return value of type BYTE returns the character as ASCII value.

Examples
The IL_Code function determines the ASCII code in decimal representation for
the character at the position "Position" of a character string.

VAR
 strCode: STRING(1000) := 'ABCDEF';
 byIL_Code: BYTE;
END_VAR

byIL_Code := IL_Code(InputData:= ADR(strCode),
 LenofInputData := IL_Len(ADR(strCode)), Position:=3 );

The result of the example "IL_Code" is shown in the following:

### 36.12.34 IL_StrInverse

Brief description
The IL_StrInverse function inverts a character string.

1240 /    ctrlX PLC Engineering
1344      Character strings without length limitation (StringFun_NoLimitStrLength)

Return value: Address of target character string.

Interface description

Table 1140: FUN IL_StrInverse interface
Name               Type                         Comment
SourceStr          POINTER TO BYTE              Address of source character string
DstStr             POINTER TO BYTE              Address of target character string
Table 1141: Example 1
Str1: STRING := 'abcde';
Str2: STRING;
IL_StrInverse (ADR(Str1), ADR(Str2));                Return value: ADR(Str2)
                                                     Str2: 'edcba'
Table 1142: Example 2
Str1: STRING := 'abcde';
IL_StrInverse (ADR(Str1), ADR(Str1));                Return value: ADR(Str1)
                                                     Str1: 'edcba'

### 36.12.35 IL_StrSetEndOfString

Brief description
The IL_StrSetEndOfString functions sets the end ID of a character string and
thus limits the length of the target character string.
Return value: Address of target character string.

Interface description

Table 1143: FUN IL_StrSetEndOfString interface
Name               Type                         Comment
Str                POINTER TO BYTE              Address of source character string
Length             UDINT                        Length of the target character string
Table 1144: Example
Str1: STRING := 'abcde';
IL_StrSetEndOfString (ADR(Str1), 3);                 Return value: ADR(Str1)
                                                     Str1: 'abc'

Character strings without length limitation (StringFun_NoLimitStrLength)      1344

### 36.12.36 IL_StrGetElement

Brief description
The source character string is split into elements by separator character
strings.
The IL_StrGetElement function calls the element specified by "ElementNum".
Return value: Address of the element.

Interface description

Table 1145: FUN IL_StrGetElement interface
Name           Type                          Comment
SourceStr      POINTER TO BYTE               Address of source character string
Delimiter      POINTER TO BYTE               Address of the target character string
                                             Number of the element to be called.
ElementNum     UDINT                         The number of the first element is 1
Element        POINTER TO BYTE               Address used to store the called element
MaxLen         UDINT                         Max. length of the element (in bytes/Char)
Table 1146: Example 1
Str1: STRING := 'ab;;cd;;e';
Str2: STRING := ';;' ;
Str3: STRING;
IL_StrGetElement (ADR(Str1), ADR(Str2), 2 ,       Return value: ADR(Str3)
ADR(Str3), 5);
                                                  Str3: 'cd'
Table 1147: Example 2
Str1: STRING := 'ab;;cd;;e';
Str2: STRING := ';;' ;
Str3: STRING;
IL_StrGetElement (ADR(Str1), ADR(Str2), 2 ,       Return value: ADR(Str3)
ADR(Str3), 1);
                                                  Str3: 'cd'
Table 1148: Example 3
Str1: STRING := 'ab;;cd;;e';
Str2: STRING := ';;' ;
IL_StrGetElement (ADR(Str1), ADR(Str2), 2 ,       Return value: ADR(Str1)
ADR(Str1), 5);
                                                  Str1: 'cd'

1242 /    ctrlX PLC Engineering
1344      Character strings without length limitation (StringFun_NoLimitStrLength)

### 36.12.37 IL_StrLChr

Brief description
The IL_StrLChr function applies the partial character string from the beginning
of the source character sequence up to the first occurrence of the entered
character "Char".
Return value: Address of target character string.

Interface description

Table 1149: FUN IL_StrLChr interface
Name               Type                        Comment
SourceStr          POINTER TO BYTE             Address of source character string
DstStr             POINTER TO BYTE             Address of target character string
Char               STRING[1]                   Delimiter of the partial character string
MaxLen             UDINT                       Max. length of the element (in bytes/Char)
Table 1150: Example 1
Str1: STRING := 'This is a string' ;
Str2: STRING;
IL_StrLChr (ADR(Str1), ADR(Str2), 'i', 100);        Return value: ADR(Str2)
                                                    Str2: 'Thi'
Table 1151: Example 2
Str1: STRING := 'This is a string' ;
IL_StrLChr (ADR(Str1), ADR(Str1), 'i', 100);        Return value: ADR(Str1)
                                                    Str1: 'Thi'

### 36.12.38 IL_StrRChr

Brief description
The IL_StrRChr function applies the partial character string from last the
occurrence of the entered character "Char" up to the end of the source char‐
acter string.
Return value: Address of the target string.

Interface description

Character strings without length limitation (StringFun_NoLimitStrLength)         1344

Table 1152: FUN IL_StrRChr interface
Name           Type                            Comment
SourceStr      POINTER TO BYTE                 Address of source character string
DstStr         POINTER TO BYTE                 Address of target character string
Char           STRING[1]                       Delimiter of the partial character string
MaxLen         UDINT                           Max. length of target character string (in bytes/Char)
Table 1153: Example 1
Str1: STRING := 'This is a string' ;
Str2: STRING;
IL_StrRChr (ADR(Str1), ADR(Str2), 'i', 100);        Return value: ADR(Str2)

                               Str2: 'ing'
Table 1154: Example 2
Str1: STRING := 'This is a string' ;
IL_StrRChr (ADR(Str1), ADR(Str1), 'i', 100);        Return value: ADR(Str1)
                                                    Str1: 'ing'

### 36.12.39 IL_StrSetElement

Brief description
The source character string is split into elements by separator character
strings.
The IL_StrSetElement functions inserts the "Element" character string plus
separator character string into the location specified by "ElementNum".
Return value: Address of target character string.

Interface description

Table 1155: FUN IL_StrSetElement interface
Name           Type                            Comment
SourceStr      POINTER TO BYTE                 Address of source character string
DstStr         POINTER TO BYTE                 Address of target character string
Delimiter      POINTER TO BYTE                 Address of the target character string
                                               Number of the element position the element is to be
                                               inserted into.
ElementNum     UDINT                           The number of the first element is 1
Element        POINTER TO BYTE                 Address of the element to be inserted
MaxLen         UDINT                           Max. length of target character string (in bytes/Char)

1244 /    ctrlX PLC Engineering
1344      Character strings without length limitation (StringFun_NoLimitStrLength)

Table 1156: Example 1
Str1: STRING := 'ab;;cd;;e';
Str2: STRING;
Str3: STRING := ';;' ;
Str4: STRING := 'fg';
IL_StrSetElement (ADR(Str1), ADR(Str2),              Return value: ADR(Str2)
ADR(Str3), 2 , ADR(Str4), 15);
                                                     Str2: 'ab;;fg;;cd;;e'
Table 1157: Example 2
Str1: STRING := 'ab;;cd;;e';
Str2: STRING;
Str3: STRING := ';;' ;
Str4: STRING := 'fg';
IL_StrSetElement (ADR(Str1), ADR(Str2),              Return value: ADR(Str2)
ADR(Str3), 2 , ADR(Str4), 2);
                                                     Str2: 'ab'
Table 1158: Example 3
Str1: STRING := 'ab;;cd;;e';
Str3: STRING := ';;' ;
Str4: STRING := 'fg';
IL_StrSetElement (ADR(Str1), ADR(Str1),              Return value: ADR(Str1)
ADR(Str3), 2 , ADR(Str4), 5);
                                                     Str1: 'ab;;fg;;cd;;e'

### 36.12.40 IL_StrSplit

Brief description
The source character string is split into partial character strings by separators.
The address of each partial character string is stored in a specified array.
The data type of an array element is "POINTER TO STRING[255]"
The source characters string is changed when calling the function!

Return value: Number of split partial character strings.

Interface description

Table 1159: FUN IL_StrSplit interface
Name               Type                         Comment
SourceStr          POINTER TO BYTE              Address of source character string
Delimiter          STRING[1]                    Separator

Character strings without length limitation (StringFun_NoLimitStrLength)      1344

Name           Type                  Comment
               Maximum number of partial character strings to be
MaxWord        UDINT                 separated
               TRUE: Ignores multiple immediately following separa‐
               tors
               FALSE: If two or more separators follow each other
SkipMulti‐                           immediately, only empty string "NUL" each is gener‐
pleFS          BOOL                  ated as partial character strings
POINTER TO POINTER TO Address of the array containing the addresses of the
pArray         STRING[255]           partial characters strings
SizeOfArray    UDINT                 Length of the array (in bytes)

Table 1160: Example 1
Str1: STRING := 'ab;;cd;e';
arArray: ARRAY[0..200] OF POINTER TO STRING[255];
IL_StrSplit(ADR(Str), ';', 4, FALSE, ADR(arArray), Return value: 4
SIZEOF(arArray));
                                                   arArray [1]: 'ab'
                                                   arArray [2]: ''
                                                   arArray [3]: 'cd'
                                                   arArray [4]: 'e'
Table 1161: Example 2
Str1: STRING := 'ab;;cd;e';
arArray: ARRAY[0..200] OF POINTER TO STRING[255];
IL_StrSplit(ADR(Str), ';', 3, TRUE, ADR(arArray), Return value: 3
SIZEOF(arArray));
                                                  arArray [1]: 'ab'
                                                  arArray [2]: 'cd'
                                                  arArray [3]: 'e'
Table 1162: Example 3
Str1: STRING := 'ab;;cd;e';
arArray: ARRAY[0..200] OF POINTER TO STRING[255];
IL_StrSplit(ADR(Str), ';', 2, TRUE, ADR(arArray), Return value: 2
SIZEOF(arArray));
                                                  arArray [1]: 'ab'
                                                  arArray [2]: 'cd;e'

### 36.12.41 IL_StrTrimAll

Brief description
The IL_StrTrimAll function removes all "Char" characters in one character
string.
Return value: Address of target character string

1246 /    ctrlX PLC Engineering
1344      Character strings without length limitation (StringFun_NoLimitStrLength)

Interface description

Table 1163: FUN IL_StrTrimAll interface
Name               Type                          Comment
SourceStr          POINTER TO BYTE               Address of source character string
DstStr             POINTER TO BYTE               Address of target character string
Char               STRING[1]                     Characters to be removed in the character string
MaxLen             UDINT                         Max. length of target character string (in bytes/Char)
Table 1164: Example 1
Str1: STRING := ';;;;;ab;;;;;cde;;;;;' ;
Str2: STRING;
IL_ StrTrimAll (ADR(Str1), ADR(Str2), ';',10);        Return value: ADR(Str2)
                                                      Str2: 'abcde'
Table 1165: Example 2
Str1: STRING := ';;;;;ab;;;;;cde;;;;;' ;
Str2: STRING;
IL_ StrTrimAll (ADR(Str1), ADR(Str2), ';',2);         Return value: ADR(Str2)
                                                      Str2: 'ab'
Table 1166: Example 3
Str1: STRING := ';;;;;ab;;;;;cde;;;;;' ;
IL_ StrTrimAll (ADR(Str1), ADR(Str1), ';',10);        Return value: ADR(Str1)
                                                      Str1: 'abcde'

### 36.12.42 IL_StrTrimSpace

Brief description
The IL_StrTrimSpace removes the spaces from a character string depending on
the option specified.
Return value: Address of target character string

Interface description

Table 1167: IL_StrTrimSpace interface
Name               Type                          Comment
SourceStr          POINTER TO BYTE               Address of source character string
DstStr             POINTER TO BYTE               Address of target character string

                          Time and date calculation, version 2 (time)      1344

Name           Type                          Comment
OptNum         ⮫ ENUM_TRIM_OPT               Controls removal of spaces in the character string
MaxLen         UDINT                         Max. length of target character string (in bytes/Char)
Table 1168: Example 1
Str1: STRING := ' This is a string ';
Str2: STRING;
IL_StrTrimSpace (ADR(Str1), ADR(Str2),            Return value: ADR(Str2)
EN_TRIM_BOTH_ENDS, 100);
                                                  Str2: 'This is a string'
Table 1169: Example 2

Str1: STRING := ' This is a string ';
Str2: STRING;
IL_StrTrimSpace (ADR(Str1), ADR(Str2),            Return value: ADR(Str2)
EN_TRIM_BEGINNING, 100);
                            Str2: 'This is a string '
Table 1170: Example 3
Str1: STRING := ' This is a string ';
Str2: STRING;
IL_StrTrimSpace (ADR(Str1), ADR(Str2),            Return value: ADR(Str2)
EN_TRIM_END, 100);
                                                  Str2: ' This is a string'
Table 1171: Example 4
Str1: STRING := ' This is a string ';
Str2: STRING;
IL_StrTrimSpace (ADR(Str1), ADR(Str2),            Return value: ADR(Str2)
EN_TRIM_ALL, 100);
                                                  Str2: 'This is a string'

### 36.12.43 ENUM_TRIM_OPT

The enumeration type ENUM_TRIM_OPT affects how spaces are removed from
the character string.

ENUM_ TRIM_OPT elements
Table 1172: ENUM_ TRIM_OPT elements
Name             Valu Description
                  e
EN_TRIM_BOTH_END  0 Removes all spaces at the beginning and the end of the character
S                     string
EN_TRIM_BEGIN‐    1 Removes all spaces at the beginning of the character string
NING
EN_TRIM_END       2 Removes all spaces at the end of the character string
EN_TRIM_ALL       3 Removes all spaces except for an individual space between two words

## 36.13 Time and date calculation, version 2 (time)

### 36.13.1 Introduction and overview

Time base for all time functions and functions blocks is Unix time (since
1970-01-01). If an earlier date is to be output or converted, the date output
will always be the basic date (1970-01-01).

1248 /    ctrlX PLC Engineering
1344      Time and date calculation, version 2 (time)

The following functions and function blocks provide the system time and/or
the date as a return value:

CXA_Utilities, time and date calculation
Table 1173: Areas of application and functions/function blocks of CXA_Utilities
Area of application (folder in library)
Function blocks                                       Description
Time (time and date calculation)
⮫ Chapter 36.13.2 IL_Date on page 1248                Reads the current system date
⮫ Chapter 36.13.3 IL_DateAndTime                      Reads current system date and time
on page 1249
⮫ Chapter 36.13.5 IL_ExtSysTimeDate                   Reads current system date and time in the
on page 1250                                          extended system format
⮫ Chapter 36.13.6 IL_LocalTime on page 1251           Converts control-internal UTC time to local time
⮫ Chapter 36.13.7 IL_SysTime64 on page 1253  Reads current system date and time in microsec‐
                                             onds since 01.01.1970
⮫ Chapter 36.13.10 IL_SysTime64ToSysTimeDate Converts the format of system date and system
on page 1255                                 time
⮫ Chapter 36.13.9 IL_SysTimeDate on page 1254 Reads current system date and time
⮫ Chapter 36.13.8 IL_SysTimeDateToSysTime64 Converts the format of system date and system
on page 1253                                  time
⮫ Chapter 36.13.4 IL_TimeOfDay on page 1249           FUN reads the current system time

### 36.13.2 IL_Date

Brief description
The function IL_Date reads the current date of the system.

Interface description

Table 1174: Interface IL_Date
                   Name          Data type      Description
VAR_INPUT          Enable        BOOL           Processing of function enabled (cyclic, state-con‐
                                                trolled)
RETURN             IL_Date       DATE           Current system date according to IEC61131-3

Functional Description
The function IL_Date cyclically reads the system date formatted according to
IEC61131-3 after processing enabled for the function via "Enable".

Troubleshooting
No troubleshooting available for this function.

                           Time and date calculation, version 2 (time)         1344

### 36.13.3 IL_DateAndTime

Brief description
The function IL_DateAndTime reads current system date and time.

Interface description

Table 1175: Interface IL_DateAndTime
               Name           Data type       Description
VAR_INPUT      Enable         BOOL            Processing of function enabled (cyclic, state-con‐
                                              trolled)
RETURN         IL_DateAnd‐    DT              Current system date and system time according to
               Time                           IEC61131-3

Functional Description
The function IL_DateAndTime cyclically reads the current system date as well
as the current system time formatted according to IEC61131-3 after proc‐
essing enabled for the function via "Enable".

Troubleshooting
No troubleshooting available for this function.

### 36.13.4 IL_TimeOfDay

Brief description
The function IL_TimeOfDay reads the current time of the system.

Interface description

Table 1176: Interface IL_TimeOfDay
               Name           Data type       Description
VAR_INPUT      Enable         BOOL            Processing of function enabled (cyclic, state-con‐
                                              trolled)
RETURN         IL_TimeOfDay TOD               Current system time according to IEC61131-3

1250 /    ctrlX PLC Engineering
1344      Time and date calculation, version 2 (time)

Functional Description
The function IL_TimeOfDay cyclically reads the system time formatted
according to IEC61131-3 after processing enabled for the function via
"Enable".

Troubleshooting
No troubleshooting available for this function.

### 36.13.5 IL_ExtSysTimeDate

Brief description
The function block IL_ExtSysTimeDate reads current system date and time.

Interface description

Table 1177: Interface IL_ExtSysTimeDate
                   Name         Data type   Description
VAR_INPUT          Enable       BOOL        Processing of function enabled (cyclic, state-con‐
                                            trolled)
VAR_OUTPUT ExtSysTime‐          EXT_SYS_TIM Current system date and system time in the extended
           Date                 E_DATE      system format

Functional Description
The function block IL_ExtSysTimeDate cyclically reads the current system date
as well as the current system time in the extended system format after proc‐
essing enabled for the function block via "Enable".

The extended system format is composed of the system formats SYS_TIME64
and SYS_TIME_DATE.

Troubleshooting
No troubleshooting available for this function block.

                                Time and date calculation, version 2 (time)       1344

### 36.13.6 IL_LocalTime

     Brief description
     The functionality of the "IL_LocalTime" function block is controlled via the
     "CurrentUTCTime" input.
     If the "CurrentUTCTime" input contains the default value (input is not active),
     the function block reads out the system time of the control and converts it to
     local time using the time zone information.
     If the "CurrentUTCTime" input does not contain the default value, the time
     value is converted to local time via the "CurrentUTCTime" and is output at the
     "LocalDateTime" output. In this case, the time is not read out of the control.

     Interface description

Table 1178: Interface variables of the IL_LocalTime function block
                Name             Type                  Description
VAR_INPUT       Enable           BOOL                  Starts at a rising edge.
                                                       Binary outputs are reset at a falling edge.
                Pause          BOOL                    Pauses processing
                CurrentUTCTime DT                      If a time value is specified via the input,
                                                       this time is converted to local time and
                                                       output at the "LocalDateTime" output.
                                                       If the input is not active, the system time of
                                                       the control is converted.
VAR_OUTPUT      Done             BOOL                  Time updated; time outputs valid
                Error            BOOL                  TRUE indicates an error.
                ErrorID          ⮫ ERROR_CODE          Error class
                ErrorIdent       ⮫ ERROR_STRUCT        Detailed error information (see ⮫ Trouble‐
                                                       shooting on page 1252 )
                InPause         BOOL                   Processing paused
                LocalDateTime DT                       Local time as DT data type
                LocalTimeStruct SYS_TIME_DATE          Local time as SYS_TIME_DATE
VAR_IN_OUT      Time zone       ⮫ IL_TIMEZONE          Time zone description

Table 1179: Min./max. and default values of the IL_LocalTime function block inputs
Name           Type                Min. value Max. value Default value     Applied
Enable         BOOL                                      FALSE             Continuous
Pause          BOOL                                      FALSE             Rising edge at “Enable”
CurrentUTCTime DT                                        DT#1970-1-1-      Continuous if Enable =
                                                         0:0:0             TRUE

1252 /    ctrlX PLC Engineering
1344      Time and date calculation, version 2 (time)

Name               Type          Min. value Max. value Default value Applied
Time zone          ⮫ IL_TIMEZONE                                     Rising edge at “Enable”

Functional description
If the CurrentUTCTime input contains the default value (input is not active),
the function block reads out the time zone information from the "Timezone"
input in case of a rising edge at "Enable". The system time is cyclically read
and converted to local time using the time zone information and the result
is set on the outputs "LocalDateTime" and "LocalTimeStruct". The output is
refreshed each second. At each refresh, the "Done" output is set for one PLC
cycle.
If the CurrentUTCTime input does not contain the default value, the time
value is read in via the nCurrentUTCTime input in case of a set "Enable" input.
This time value is converted to local time and output at the "LocalDateTime"
output. In this case, the time is not read out of the control.
The "Pause" input pauses the processing. If this input is set, no time is read
and the outputs "LocalDateTime" and "LocalTimeStruct" are frozen.
If an error occurs while processing, the "Error" output is set. "ErrorID" and
"ErrorIdent" contain detailed information on the error.

Troubleshooting
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:
Additional2 contains the target-dependent value CXA_PLC_DETAIL‐
DIAG_ERROR in the upper word, e.g. 16#0C230000 for die ctrlX CORE or
16#01230000 for the ctrlX DRIVE Technology Function.
Table 1180: Error codes generated by IL_LocalTime
ErrorID               Additional1                  Additional2              Description
INPUT_INVALID_ERROR 16#A0F00100           CXA_PLC_DETAILDIAG_ERROR +        Winter time settings
                                          16#00000041                       inconsistent
INPUT_RANGE_ERROR         16#A0F00100     CXA_PLC_DETAILDIAG_ERROR +        Time in WinterDiffUtc
                                          16#00000042                       bigger than 24 hours
INPUT_RANGE_ERROR         16#A0F00100     CXA_PLC_DETAILDIAG_ERROR +        Value in SwiWinter‐
                                          16#00000043                       Month higher than 12
INPUT_RANGE_ERROR         16#A0F00100     CXA_PLC_DETAILDIAG_ERROR +        Value in SwiWinter‐
                                          16#00000044                       Week higher than 5
INPUT_RANGE_ERROR         16#A0F00100     CXA_PLC_DETAILDIAG_ERROR +        Value in SwiWinter‐
                                          16#00000045                       Weekday higher than 7
INPUT_RANGE_ERROR         16#A0F00100     CXA_PLC_DETAILDIAG_ERROR +        Value in SwiWinterDay‐
                                          16#00000046                       Year higher than 365
INPUT_INVALID_ERROR 16#A0F00100           CXA_PLC_DETAILDIAG_ERROR +        Summer time settings
                                          16#00000047                       inconsistent
INPUT_RANGE_ERROR         16#A0F00100     CXA_PLC_DETAILDIAG_ERROR +        Time in SummerDiffUtc
                                          16#00000048                       bigger than 24 hours
INPUT_RANGE_ERROR         16#A0F00100     CXA_PLC_DETAILDIAG_ERROR +        Value in SwiSummer‐
                                          16#00000049                       Month higher than 12
INPUT_RANGE_ERROR         16#A0F00100     CXA_PLC_DETAILDIAG_ERROR +        Value in SwiSummer‐
                                          16#0000004A                       Week higher than 5
INPUT_RANGE_ERROR         16#A0F00100     CXA_PLC_DETAILDIAG_ERROR +        Value in SwiSummer‐
                                          16#0000004B                       Weekday higher than 7

                             Time and date calculation, version 2 (time)         1344

ErrorID                        Additional1            Additional2       Description
INPUT_RANGE_ERROR            16#A0F00100     CXA_PLC_DETAILDIAG_ERROR + Value in SwiSummer‐
                        16#0000004C                DayYear higher than
                                                   365
INPUT_INVALID_ERROR 16#A0F00100              CXA_PLC_DETAILDIAG_ERROR + Error at time conver‐
                        16#0000004D                sion due to incorrect
                                                   time zone information

### 36.13.7 IL_SysTime64

Brief description
The function block IL_SysTime64 reads current system date and time.

Interface description

Table 1181: Interface IL_SysTime64
               Name              Data type      Description
VAR_INPUT      Enable            BOOL           Processing of function enabled (cyclic, state-con‐
                                                trolled)
VAR_OUTPUT SysTime64             SYS_TIME64     Current system date and system time in microsec‐
                                                onds since 01.01.1970

Functional Description
The function block IL_SysTime64 reads the current system date as well as
the current system time in microseconds since 01.01.1970 after processing
enabled for the function via "Enable".

Troubleshooting
No troubleshooting available for this function block.

### 36.13.8 IL_SysTimeDateToSysTime64

Brief description
The function block IL_SysTimeDateToSysTime64 serves for the format conver‐
sion of the system date and the system time.

1254 /    ctrlX PLC Engineering
1344      Time and date calculation, version 2 (time)

Interface description

Table 1182: Interface IL_SysTimeDateToSysTime64
                   Name        Data type
                                     Description
VAR_INPUT          Enable      BOOL  Processing enabled for function block (cyclic, state-
                                     controlled)
           SysTimeDate SYS_TIME_DATE System date and system time in the system format
VAR_OUTPUT SysTime64   SYS_TIME64    System date and system time in microseconds since
                                     01.01.1970

Functional description
After processing enabled for the function block, the function block IL_Sys‐
TimeDateToSysTime64 uses "Enable" to cyclically convert the system date
including the system time available at the input "SysTimeDate" in microsec‐
onds (basis: 01.01.1970).

Troubleshooting
No troubleshooting available for this function block.

### 36.13.9 IL_SysTimeDate

Brief description
The function block IL_SysTimeDate reads current system date and time.

Interface description

Table 1183: Interface IL_SysTimeDate
                   Name         Data type            Description
VAR_INPUT          Enable       BOOL                 Processing of function enabled (cyclic, state-con‐
                                                     trolled)
VAR_OUTPUT SysTimeDate          SYS_TIME_DATE        Current system date and system time in the
                                                     system format

Functional Description
The function block IL_SysTimeDate cyclically reads the current system date as
well as the current system time in the system format after processing enabled
for the function block via "Enable".

                           Time and date calculation, version 2 (time)     1344

Troubleshooting
No troubleshooting available for this function block.

### 36.13.10 IL_SysTime64ToSysTimeDate

Brief description
The function block IL_SysTime64ToSysTimeDate serves for the conversion of
the system date and the system time.

Interface description

Table 1184: Interface IL_SysTime64ToSysTimeDate
              Name           Data type
                                     Description
VAR_INPUT     Enable         BOOL    Processing enabled for function block (cyclic, state-
                                     controlled)
           SysTime64   SYS_TIME64    System date and system time in microseconds since
                                     01.01.1970
VAR_OUTPUT SysTimeDate SYS_TIME_DATE System date and system time in the system format

Functional description
After processing enabled for the function block, the function block "IL_Sys‐
Time64ToSysTimeDate" uses "Enable" to convert the system date including the
system time available at the input "SysTime64" in microseconds (basis: to the
system date and the system time in the system format (basis: 01.01.1970).

Troubleshooting
No troubleshooting available for this function block.

### 36.13.11 IL_TIMEZONE

The data structure contains information on the time zone.

1256 /    ctrlX PLC Engineering
1344      Time and date calculation, version 2 (time)

IL_TIMEZONE data structure
Table 1185: IL_TIMEZONE data structure
Element               Data      Min.       Max. value   Default value Description
                      type      value
WinterDiffUtc         TIME                              t#0s         Difference from local winter
                                                                     time to UTC
WinterLoc             BOOL                              FALSE        TRUE: East from Greenwich
                                                                     FALSE: West from Green‐
                                                                     wich
SwiWinterMonth        USINT     0          12           0            Month when converting to
                                                                     winter time
                                                                     0: Not used
                                                                     1..12: Month
SwiWinterWeek         USINT     0          5            0            Week in the month of
                                                                     winter time conversion
                                                                     0: Not used
                                                                     1..4 week of the conversion
                                                                     5: Last week in the month
SwiWinterWeekday USINT          0          7            0            Weekday when converting
                                                                     to winter time
                                                                     0: Not used
                                                                     1..7: weekday (1: Mon, 7:
                                                                     Sun)
SwiWinterDayYear      UINT      0          365          0            Day in the year of the con‐
                                                                     version to winter time
                                                                     0: Not used
SwiWinterTime         TOD       t#0s       t#23h59m59s t#0s          Time when converting to
                                                                     winter time
SummerDiffUtc         TIME                              t#0s         Difference from local
                                                                     summer time to UTC
SummerLoc             BOOL                              FALSE        TRUE: East from Greenwich
                                                                     FALSE: West from Green‐
                                                                     wich
SwiSummerMonth        USINT     0          12           0            Month when converting to
                                                                     summer time
                                                                     0: Not used
                                                                     1..12: Month
SwiSummerWeek         USINT     0          5            0            Week in the month of
                                                                     summer time conversion
                                                                     0: Not used
                                                                     1..4 week of the conversion
                                                                     5: Last week in the month
SwiSummer‐            USINT     0          7            0            Weekday when converting
Weekday                                                              to summer time
                                                                     0: Not used
                                                                     1..7: weekday (1: Mon, 7:
                                                                     Sun)

                           Time and date calculation, version 2 (time)      1344

Element          Data          Min.      Max. value     Default value Description
type          value
SwiSummerDayYear UINT          0         365            0             Day in the year of the con‐
                                                  version to summer time
                                                  0: Not used
SwiSummerTime        TOD       t#0s      t#23h59m59s t#0s             Time when converting to
                                                  summer time
South                BOOL                               FALSE         Location south of the
                                                  equator

Predefined time zones

To facilitate the time zone handling, several important time zones are already
predefined. This, the structure has to be filled out only in exceptional cases.
If predefined time zones are used, the "Timezone." prefix has to be used.
Timezone.CEST for "Central European time zone"

Table 1186: Predefined time zones
Constant    Time zone Description
ACST        ACST      UTC+9:30
                      Australia
ACDT        ACST/     UTC+9:30/UTC+10:30
            ACDT      Australia
AEST        AEST      UTC+10
                      Australia
AEDT        AEST/     UTC+10/UTC+11
            AEDT      Australia
AMT         AMT, BOT UTC-4
                      Brazil, Bolivia
AMST        AMT/AMST UTC-4/UTC-3
                      Brazil
ART         ART       UTC-3
                      Argentina
ARST        ART/ARST UTC-3/UTC-2
                      Argentina
AWST        AWST      UTC+8
                      Australia
BRT         BRT       UTC-3
                      Brazil
BRST        BRT/BRST UTC-3/UTC-2
                      Brazil
BST         GMT/BST UTC+0/UTC+1
                      Great Britain
CAT         CAT       UTC+2
                      Botswana, Burundi, Congo, Mozambique, Rwanda,
                      Zambia, Zimbabwe
CET         CET       UTC+1
                      Algeria, Tunisia

1258 /    ctrlX PLC Engineering
1344      Time and date calculation, version 2 (time)

Constant    Time zone Description
CEST        CET/CEST UTC+1/UTC+2
                      Albania, Andorra, Austria, Belgium, Bosnia-Herzego‐
                      vina, Croatia, Czech Republic, Denmark, France,
                      Germany, Gibraltar, Vatican City, Hungary, Italy,
                      Kosovo, Lichtenstein, Luxemburg, Macedonia, Malta,
                      Monaco, Montenegro, Netherlands, Norway, Poland,
                      San Marino, Serbia, Slovakia, Slovenia, Spain - except
                      Canary Islands, Sweden, Switzerland
CCT         CCT, HKT UTC+8
                      China, Macau, Taiwan, Hong Kong
CDT         CST/CDT UTC-6/-5
                      Canada, USA, Mexico
CVT         CVT       UTC-1
                      Cape Verde
EAT         EAT       UTC+3
                      Djibouti, Eritrea, Ethiopia, Kenya, Madagascar,
                      Somalia, Sudan, Tanzania, Uganda
EDT         EST/EDT   UTC-5/UTC-4
                      Canada, USA
EET         EET       UTC+2
                      Libya
EEST        EET/EEST UTC+2/UTC+3
                      Belarus, Bulgaria, Estonia, Finland, Greece, Latvia,
                      Lithuania, Moldova, Romania, Russia (Kaliningrad),
                      Turkey, Ukraine, Egypt
FNT         FNT       UTC-2
                      Brazil
GMT         GMT       UTC+0
                      Iceland, Burkina Faso, Ivory Coast, Gambia, Ghana,
                      Guinea-Bissau, Guinea, Liberia, Mali, Mauritania,
                      Saint Helena, Senegal, Sierra Leone, Togo
ICT         ICT       UTC+7
                      Cambodia, Laos, Thailand, Vietnam
IST         IST       UTC+5:30
                      India
JST         JST       UTC+9
                      Japan
MSK         MSK/MSD UTC+3/UTC+4
                      Russia
MDT         MST/MDT UTC-7/UTC-6
                      USA
PDT         PDT       UTC-8/UTC-7
                      Canada, USA
SAST        SAST      UTC+2
                      Lesotho, South Africa, Swaziland
WAT         WAT       UTC+1
                      Angola, Benin, Central African Republic, Chad, Congo,
                      Equatorial Guinea, Gabon, Niger, Nigeria

                                  Double-linked lists (Utilities/Logic)     1344

Constant     Time zone Description
WAST         WAT/WAST UTC+1/UTC+2
                       Namibia
WEST         WET/WEST UTC+0/UTC+1
                       Faroe Islands, Portugal, Canary Islands, Madeira,
                       Morocco

## 36.14 Double-linked lists (Utilities/Logic)

### 36.14.1 Introduction and overview

The following function block was designed for applications at which a double-

linked list is required. Elements can be added and deleted.

CXA_Utilities, double-linked lists
Table 1187: Areas of application and functions/function blocks of CXA_Utilities
Area of application (folder in library)
Function blocks                                   Description
Double-linked lists (Utilities/Logic)
⮫ Chapter 36.14.2 IL_LinkedList on page 1259      Manages double-linked lists (used for ring
                                                  buffer, FIFOs and LIFOs)
                                                  The function block uses the data types
                                                  ● ⮫ Chapter 36.14.3 IL_LINKED_LIST_MAINTE‐
                                                    NANCE on page 1264
                                                  ● ⮫ Chapter 36.14.4 IL_LINKED_LIST_MODE
                                                    on page 1264

### 36.14.2 IL_LinkedList

Brief description
The function block maintains a double-linked list. The list content can be
specified by the user.

Interface description

Table 1188: Interface variables of the IL_LinkedList function block
I/O type      Name            Data type             Description
VAR_INPUT     Execute         BOOL                  The function block starts its functionality at
                                                    a rising edge
              Link            POINTER TO            Pointer to an array of IL_LINKED_LIST_MAIN‐
                              ⮫ IL_LINKED_LIST_MAIN TENANCE structures required to maintain
                              TENANCE               the list
              Size            UDINT                   Number of list elements to be maintained

1260 /     ctrlX PLC Engineering
1344       Double-linked lists (Utilities/Logic)

I/O type           Name            Data type            Description
Mode            ⮫ IL_LINKED_LIST_MOD Mode that executes the function block, e.g.
                E                    adding or removing an element
Index           DINT                     Index on which the operation is to be
                                         applied
VAR_OUTPUT Done                    BOOL                     If this output is TRUE, the function block
                                         has successfully completed its operation
Error           BOOL                     Indicates that an error occurred in the func‐
                                         tion block. The output data is invalid
ErrorID         ⮫ ERROR_CODE             Error ID
ErrorIdent      ⮫ ERROR_STRUCT           Error structure with further subdivision of
                                         error classes
                                         ⮫ Error codes on page 1263
CurrentIndex DINT                        Current index
NextIndex    DINT                        Next index
Counter      UDINT                       Number of elements in the list

        Min./max. and default values of the inputs
        The following value ranges and default values can be applied at the function
        block:

Table 1189: Min./max. and default values of the IL_LinkedList function block
Name          Type                             Min. value         Max. value          Default value
Link          0                                0                  16#FFFFFFFF         0
Size          UDINT                            0                  16#FFFFFFFF         0
Mode          IL_LINKED_LIST_MODE              ModeInitClear      ModeCheckIndex      ModeInitClear
Index         UDINT                            0                  16#FFFFFFFF         0

        Functional description
        The function block maintains a double-linked list. This list is stored in an
        array in which only the indices have to be maintained. To maintain the
        list, create an array of type IL_LINKED_LIST_MAINTENANCE (see ⮫ Using the
        IL_LINKED_LIST_MAINTENANCE structure on page 1260) that has to be as large
        as its own data.
        The list is manipulated by calling the function block. The manipulation type
        can be defined by the "Mode" input (⮫ IL_LINKED_LIST_MODE).

        Using the IL_LINKED_LIST_MAINTENANCE structure
        The data structure IL_LINKED_LIST_MAINTENANCE is used by the function
        block and may not be overwritten. Since users can determine the length of
        the linked list, they have to create the maintenance structures for the list as
        well.
        Therefore, define an array of the type ⮫ IL_LINKED_LIST_MAINTENANCE.
        The structure can be used for debugging.
        "Prev" is a pointer to the preceding list element
        "Next" is a pointer to the following list element.
        If the value is 0, it is the end or the beginning of the array or an unused
        element.

                                 Double-linked lists (Utilities/Logic)     1344

The inputs "Link" and "Size" of the function block may not be modified after
initialized by "Mode ModeInitClear". This also applies when changing online
e.g. if the length of the data structure is changed.

Examples
Example of the function block use:

Defining variables:

(* Maximum array size *)
uiMAX_ARRAY_SIZE: INT := 10;
(* My data structure array *)

arMyData:     ARRAY [1..uiMAX_ARRAY_SIZE] OF MY_STRUCTURE;
(* List management array*)
arLinkedList: ARRAY [1..uiMAX_ARRAY_SIZE] OF
IL_LINKED_LIST_MAINTEANANCE;
(* Function block instance *)
fbMyList:     IL_LinkedList;
(* Index variable*)
udiIndex:     DINT;

Call for initialization:

fbMyList(Execute:= TRUE,
    Link:= ADR(arLinkedList),
    Size:= uiMAX_ARRAY_SIZE,
    Mode:= ModeInitClear,
    Index:= ,
    Done=> ,
    Error=> ,
    ErrorId =>,
    ErrorIdent=> ,
    CurrentIndex=> ,
    NextIndex=>);

Adding a head to the list:

(* Reset "Execute" input first (value of mode is not
important) *)
fbMyList(Execute:= FALSE,
      Link:= ADR(arLinkedList),
      Size:= uiMAX_ARRAY_SIZE,
      Mode:= ModeInitClear,
      Index:= ,
      Done=> ,
      Error=> ,
      ErrorId =>,
      ErrorIdent=> ,
      CurrentIndex=> ,
      NextIndex=>);

(* Add head *)
fbMyList(Execute:= TRUE,
      Link:= ADR(arLinkedList),
      Size:= uiMAX_ARRAY_SIZE,
      Mode:= ModeAddHead,
      Index:= ,

1262 /    ctrlX PLC Engineering
1344      Double-linked lists (Utilities/Logic)

       Done=> ,
       Error=> ,
       ErrorId =>,
       ErrorIdent=> ,
       CurrentIndex=> udiIndex,
       NextIndex=>);

(* Return value in CurrentIndex contains index for list head
or
   -1 if an error occurred. *)
IF udiIndex <> -1 THEN
    arMyData[udiIndex].StructureMember := MyValue;
END_IF;

Scroll through a list:

(* Reset "Execute" input first (value of mode is not
important) *)
fbMyList(Execute:= FALSE,
      Link:= ADR(arLinkedList),
      Size:= uiMAX_ARRAY_SIZE,
    Mode:= ModeGetHead,
      Index:= ,
      Done=> ,
      Error=> ,
      ErrorId =>,
    ErrorIdent=> ,
      CurrentIndex=> ,
      NextIndex=>);

(* Determine head *)
fbMyList(Execute:= TRUE,
      Link:= ADR(arLinkedList),
    Size:= uiMAX_ARRAY_SIZE,
      Mode:= ModeGetHead,
      Index:= ,
      Done=> ,
      Error=> ,
      ErrorId =>,
      ErrorIdent=> ,
      CurrentIndex=> udiIndex,
    NextIndex=>);

(* Check return value (-1 means error) *)
WHILE (udiIndex > 0) DO
      (* Return value in CurrentIndex contains index in list *)
      arMyData[udiIndex].StructureMember := MyValue;

       (* Reset "Execute" input again *)
       fbMyList(Execute:= FALSE,
             Link:= ADR(arLinkedList),
           Size:= uiMAX_ARRAY_SIZE,
           Mode:= ModeGetNext,
          Index:= ,
             Done=> ,
             Error=> ,
             ErrorId =>,
           ErrorIdent=> ,

                                       Double-linked lists (Utilities/Logic)       1344

                  CurrentIndex=> ,
                NextIndex=>);

        (* Get next element*)
      fbMyList(Execute:= TRUE,
              Link:= ADR(arLinkedList),
            Size:= uiMAX_ARRAY_SIZE,
              Mode:= ModeGetNext,
              Index:= ,
              Done=> ,
            Error=> ,
              ErrorId =>,
              ErrorIdent=> ,

            CurrentIndex=> udiIndex,
              NextIndex=>);
    END_WHILE

 Output assignment depending on the "Mode" input
Depending on the "Mode" input assignment, the "Index" input and the "Cur‐
rentIndex" and "NextIndex" are configured accordingly. The following table
lists the respective values. An X stands for a value that is unchanged with
respect to the previous call. If an error occurs, -1 is returned for "Curren‐
tIndex".
Table 1190: Function block outputs with respect to Mode
Mode                         Index           CurrentIndex                 NextIndex
ModeInitClear                X               -1                           Next free index
ModeAddTail                  X               Tail index                   Next free index
ModeAddHead                  X               Head index                   Next free index
ModeRemoveTail               X               New tail index               Next free index
ModeRemoveHead               X               New head index               Next free index
ModeRemoveIndex              Index for       Previous element index       Next free index
                             removal
ModeGetHead                  X               Head index                   X
ModeGetTail                  X               Tail index                   X
ModeGetNext                  Previous        Subsequent element index     X
                             index
ModeGetPrev                  Next index      Previous element index       X
ModeGetEmptyIndex            X               X                            Next free index
ModeCheckIndex               Testing index   1: Found                     -1
                                             -1: Not found

 Error codes
 The function block uses the error table CXA_TABLE.
 It can generate the following error messages in Additional1/Additional2:
 Additional2 contains the target-dependent value CXA_PLC_DETAIL‐
 DIAG_ERROR in the upper word, e.g. 16#0C230000 for die ctrlX CORE or
 16#01230000 for the ctrlX DRIVE Technology Function.
Table 1191: Error codes of the IL_LinkedList function block
ErrorID                       Additional1        Additional2                Description
INPUT_INVALID_ERROR           16#A0F00100        CXA_PLC_DETAILDIAG_ERROR + "Index" input is not
                                                 16#00000051                in the valid range

1264 /    ctrlX PLC Engineering
1344      Double-linked lists (Utilities/Logic)

ErrorID                     Additional1           Additional2                Description
INPUT_INVALID_ERROR         16#A0F00100           CXA_PLC_DETAILDIAG_ERROR + "Link" input is a null
                            16#00000052                pointer
ACCESS_ERROR                16#A0F00100           CXA_PLC_DETAILDIAG_ERROR + An index is still
                            16#00000053                linked in the list
                                                       although it is empty
                                                       (internal error)
ACCESS_ERROR                16#A0F00100           CXA_PLC_DETAILDIAG_ERROR + An element in the
                            16#00000054                list is to be cleared,
                                                       but the list is
                                                       already empty
RESOURCE_ERROR              16#A0F00100           CXA_PLC_DETAILDIAG_ERROR + List is full
                            16#00000055
STATE_MACHINE_ERROR 16#A0F00100                   CXA_PLC_DETAILDIAG_ERROR + "Mode" input has an
                            16#00000056                invalid value
RESOURCE_ERROR              16#A0F00100           CXA_PLC_DETAILDIAG_ERROR + "Size" input changed
                            16#00000057                again after initializa‐
                                                       tion (e.g. by online
                                                       change).

### 36.14.3 IL_LINKED_LIST_MAINTENANCE

The structure is used by the function block ⮫ IL_LinkedList.
"Prev" is a pointer for the previous list element, "Next" for the subsequent
element. If the value is 0, it is the end or the beginning of the array or an
unused element.
Due to this structure, debugging lists is facilitated.

Type definition

TYPE IL_LINKED_LIST_MAINTENANCE :
STRUCT
    Prev: POINTER TO DINT;
    Next: POINTER TO DINT;
END_STRUCT
END_TYPE

### 36.14.4 IL_LINKED_LIST_MODE

Use the enumeration type to define the action to be executed.
The enumeration is used by the function block ⮫ Chapter 36.14.2 IL_Linked‐
List on page 1259.

Enumerations and their meaning in the function block IL_LinkedList
Table 1192: Enumerations and their meaning in the function block IL_LinkedList
Enumeration     Meaning
ModeInitClear   The linked list is initialized. All entries are deleted
ModeAddTail     An element is inserted at the end of the list. If the list is empty, the first
                element is created
ModeAddHead     An element is inserted at the beginning of the list. If the list is empty, the first
                element is created
ModeRemoveTail The last element in the list is removed
ModeRemoveHead The first element in the list is removed
ModeRemoveIndex The element at the index "Index" is removed

                             Modulo value calculation (Utilities/Logic)         1344

Enumeration          Meaning
ModeGetHead          Returns the index of the head of the list
ModeGetTail          Returns the index of the tail of list
ModeGetNext          Returns the subsequent element in the list
ModeGetPrev          Returns the previous element in the list
ModeGetEmp‐          Returns the next free index in the list
tyIndex
ModeCheckIndex       Checks whether the specified index is used in the linked list. The result is
returned in the "CurrentIndex":
1: Index is used
-1: Index is not used

## 36.15 Modulo value calculation (Utilities/Logic)

### 36.15.1 Introduction and overview

The following functions calculate a modulo value. Depending on the selected
function, different value ranges are used.

CXA_Utilities, Modulo value calculation
Table 1193: Areas of application and functions/function blocks of CXA_Utilities
Area of application (folder in library)
Function blocks                                    Description
Modulo value calculation (Utilities/Logic)
⮫ Chapter 36.15.4 IL_GetModuloType01               Calculates a modulo value. Value range between
on page 1266                                       0.0 and + modulo value (REAL)
⮫ Chapter 36.15.5 IL_GetModuloType02               Calculates a modulo value. Value range between
on page 1268                                       0 and + modulo value (DINT)
⮫ Chapter 36.15.6 IL_GetModuloType03               Calculates a modulo value. Value range between
on page 1269                                       - modulo value and + modulo value (REAL)
⮫ Chapter 36.15.7 IL_GetModuloType04               Calculates a modulo value. Value range between
on page 1270                                       - modulo/2 and + modulo value/2 (REAL)

### 36.15.2 IL_DegToRad

Brief description
The function IL_DegToRad converts a angular value in degrees to the corre‐
sponding radian incl. modulo.

Interface description

Table 1194: Interface variables of the IL_DegToRad function block
I/O type     Name             Data type                Description
VAR_INPUT Deg                 LREAL                    Angle [DEG]
Return value                  LREAL                    Angle [RAD]

1266 /    ctrlX PLC Engineering
1344      Modulo value calculation (Utilities/Logic)

I/O type   Name               Data type                Description
VAR_OUTPUT Modulo             INT                      Modulo

Functional description
At an instance call, the IL_DegToRad function cyclically converts the indicated
angle in degrees to the respective radian incl. modulo. If a value beyond the
valid value range is specified, 0 is returned.

Troubleshooting
The function IL_DegToRad does not generate any errors.

### 36.15.3 IL_RadToDeg

Brief description
The function IL_RadToDeg converts an angular value in radian to the corre‐
sponding degrees incl. Modulo.

Interface description

Table 1195: Interface variables of the IL_RadToDeg function block
I/O type     Name             Data type                Description
VAR_INPUT Rad                 LREAL                    Angle [RAD]
Return value                  LREAL                    Angle [DEG]
VAR_OUTPUT Modulo             INT                      Modulo

Functional description
At an instance call, the function IL_RadToDeg cyclically converts the indicated
angle in radian to the respective degrees incl. Modulo.
If a value beyond the valid value range is specified, 0 is output for "Deg" and
for "Modulo".

Troubleshooting
The function IL_RadToDeg does not generate any errors.

### 36.15.4 IL_GetModuloType01

Brief description
The function returns the modulo value. The value range returned is between
0.0 and + modulo value.

                            Modulo value calculation (Utilities/Logic)         1344

Interface description

Table 1196: Interface variables of the IL_GetModuloType01 function
I/O type       Name                Data type           Description
VAR_INPUT      Value               REAL                Value at which the modulo function is to be

                                  applied
ModuloValue         REAL                Modulo value to be used for the modulo
                                  operation
RETURN                             REAL                Modulo value: The value range returned is
                                  between 0.0 and + modulo value.

Min./max. and default values
The following table lists the min./max. and default values of the function
block inputs:
Table 1197: Min./max. and default values of the IL_GetModuloType01 function
Name            Type            Min. value     Max. value   Default value        Applied
Value           REAL            - 1.175494e-38 3.402823e+38 0.0                  With every call
ModuloValue     REAL            - 1.175494e-38 3.402823e+38 360.0                With every call

Functional description
The function returns the modulo value. The value range returned is between
0.0 and + modulo value. The positive and the negative limit value are not part
of the value range (also see the following diagram which shows the value
transferred to the function on the x-coordinates and the value returned from
the function on the y-coordinates).
If 0.0 is transferred for "ModuloValue", the function returns the value "Value".

Troubleshooting
The function does not generate any errors.

1268 /    ctrlX PLC Engineering
1344      Modulo value calculation (Utilities/Logic)

### 36.15.5 IL_GetModuloType02

Brief description
The function returns the modulo value. The value range returned is between 0
and + modulo value

Interface description

Table 1198: Interface variables of the IL_GetModuloType02 function
I/O type           Name              Data type           Description
VAR_INPUT          Value             DINT                Value at which the modulo function is to be
                                                         applied
                   ModuloValue       DINT                Modulo value to be used for the modulo
                                                         operation
RETURN                               DINT                Modulo value: The value range returned is
                                                         between 0 and + modulo value

Min./max. and default values
The following table lists the min./max. and default values of the function
block inputs:
Table 1199: Min./max. and default values of the IL_GetModuloType02 function
Name               Type           Min. value   Max. value        Default value   Applied
Value              DINT           - 2147483648 2147483647        0               With every call
ModuloValue        DINT           - 2147483648 2147483647        360             With every call

Functional description
The function returns the modulo value. The value range returned is between
0 and + modulo value The positive and the negative limit value are not part
of the value range (also see the following diagram which shows the value
transferred to the function on the x-coordinates and the value returned from
the function on the y-coordinates).
If 0 is transferred for "ModuloValue", the function returns the value "Value".

                            Modulo value calculation (Utilities/Logic)         1344

Troubleshooting
The function does not generate any errors.

### 36.15.6 IL_GetModuloType03

Brief description
The function returns the modulo value. The returned value range is between -
modulo value and + modulo value.

Interface description

Table 1200: Interface variables of the IL_GetModuloType03 function
I/O type       Name                Data type           Description
VAR_INPUT      Value               REAL                Value at which the modulo function is to be
                                                       applied
               ModuloValue         REAL                Modulo value to be used for the modulo
                                                       operation
RETURN                             REAL                Modulo value: The returned value range
                                                       is between - modulo value and + modulo
                                                       value.

Min./max. and default values
The following table lists the min./max. and default values of the function
block inputs:
Table 1201: Min./max. and default values of the IL_GetModuloType03 function
Name            Type            Min. value     Max. value   Default value        Applied
Value           REAL            - 1.175494e-38 3.402823e+38 0.0                  With every call
ModuloValue     REAL            - 1.175494e-38 3.402823e+38 360.0                With every call

Functional description
The function returns the modulo value. The returned value range is between
- modulo value and + modulo value. The positive and the negative limit value
are not part of the value range (also see the following diagram which shows
the value transferred to the function on the x-coordinates and the value
returned from the function on the y-coordinates).
If 0.0 is transferred for "ModuloValue", the function returns the value "Value".

1270 /    ctrlX PLC Engineering
1344      Modulo value calculation (Utilities/Logic)

    Troubleshooting
    The function does not generate any errors.

### 36.15.7 IL_GetModuloType04

    Brief description
    The function returns the modulo value. The returned value range is between -
    modulo / 2 and + modulo / 2.

    Interface description

Table 1202: Interface variables of the IL_GetModuloType04 function
I/O type           Name              Data type           Description
VAR_INPUT          Value             REAL                Value at which the modulo function is to be
                                                         applied
                   ModuloValue       REAL                Modulo value to be used for the modulo
                                                         operation
RETURN                               REAL                Modulo value: The returned value range is
                                                         between - modulo / 2 and + modulo / 2.

    Min./max. and default values
The following table lists the min./max. and default values of the function
block inputs:
Table 1203: Min./max. and default values of the IL_GetModuloType04 function
Name               Type           Min. value     Max. value   Default value      Applied
Value              REAL           - 1.175494e-38 3.402823e+38 0.0                With every call
ModuloValue        REAL           - 1.175494e-38 3.402823e+38 360.0              With every call

           Trigonometric functions (Utilities/Trigonometric Functions)      1344

Functional description
The function returns the modulo value. The returned value range is between -
modulo * 0.5 and + modulo * 0.5. The positive and the negative limit value are
part of the value range (also see the following diagram which shows the value
transferred to the function on the x-coordinates and the value returned from
the function on the y-coordinates).
If 0.0 is transferred for "ModuloValue", the function returns the value "Value".

Troubleshooting
The function does not generate any errors.

## 36.16 Trigonometric functions (Utilities/Trigonometric Func‐

tions)

### 36.16.1 IL_DegToRad

Brief description
The function IL_DegToRad converts a angular value in degrees to the corre‐
sponding radian incl. modulo.

Interface description

Table 1204: Interface variables of the IL_DegToRad function block
I/O type     Name            Data type                Description
VAR_INPUT Deg                LREAL                    Angle [DEG]
Return value                 LREAL                    Angle [RAD]
VAR_OUTPUT Modulo            INT                      Modulo

Functional description
At an instance call, the IL_DegToRad function cyclically converts the indicated
angle in degrees to the respective radian incl. modulo. If a value beyond the
valid value range is specified, 0 is returned.

1272 /    ctrlX PLC Engineering
1344      Introduction and overview

Troubleshooting
The function IL_DegToRad does not generate any errors.

### 36.16.2 IL_RadToDeg

Brief description
The function IL_RadToDeg converts an angular value in radian to the corre‐
sponding degrees incl. Modulo.

Interface description

Table 1205: Interface variables of the IL_RadToDeg function block
I/O type     Name            Data type                Description
VAR_INPUT Rad                LREAL                    Angle [RAD]
Return value                 LREAL                    Angle [DEG]
VAR_OUTPUT Modulo            INT                      Modulo

Functional description
At an instance call, the function IL_RadToDeg cyclically converts the indicated
angle in radian to the respective degrees incl. Modulo.
If a value beyond the valid value range is specified, 0 is output for "Deg" and
for "Modulo".

Troubleshooting
The function IL_RadToDeg does not generate any errors.
