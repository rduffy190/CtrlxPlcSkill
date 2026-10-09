# 6 Util

## 6.1 Introduction and overview

The "Util" library contains an additional collection of different function blocks
for BCD conversion, bit/byte functions, mathematical auxiliary functions, as
controllers, signal generators, function manipulators and for analog value
processing.

## 6.2 BCD conversion

### 6.2.1 Introduction and overview

A byte in BCD format contains integer values between 0 and 99. Four bits
are used for each decimal place. The decimal place is stored in the bits 4-7.
The BCD format is therefore similar to the hexadecimal representation, except
that only values between 0 and 99 can be stored in the BCD byte, whereas a
hexadecimal byte ranges from 0 to FF.

Example:
The integer number 51 is to be converted into BCD format. 5 is binary 0101,
1 is binary 0001, thus the BCD byte 01010001 that corresponds to the value
$51=81.

Also refer to:
● ⮫ Chapter 6.2.2 BCD_TO_INT on page 57
● ⮫ Chapter 6.2.3 INT_TO_BCD on page 58

### 6.2.2 BCD_TO_INT

This function converts a byte in BCD format into an INT value.
The input value of the function is of type BYTE and the output is of type INT.
If a byte should be transferred and it does not correspond to the BCD format,
the output is -1.

Example in ST:

i:=BCD_TO_INT(73); (* Result is 49 *)
k:=BCD_TO_INT(151); (* Result is 97 *)
l:=BCD_TO_INT(15); (* Output -1, because it is not in BCD
format *)

### 6.2.3 INT_TO_BCD

This function converts an INTEGER value into a byte in BCD format.
The input value of the function is of type INT, the output is of type BYTE.
If an INTEGER value is transferred which cannot be converted into a BCD byte,
255 is output.

Example in ST:

i:=INT_TO_BCD(49); (* Result is 73 *)
k:=BCD_TO_INT(97); (* Result is 151 *)
l:=BCD_TO_INT(100); (* Error! Output: 255 *)

## 6.3 Bit/byte functions

### 6.3.1 EXTRACT

The inputs of this function are a DWORD X and a BYTE N. The output is a
BOOL value that contains the content of the Nth bit of the input X, whereby
counting starts with the zeroth bit.

Example in ST:

FLAG:=EXTRACT(X:=81, N:=4);
  (* Result : TRUE, because 81 is binary 1010001, so the 4th
bit is 1 *)
FLAG:=EXTRACT(X:=33, N:=0);
  (* Result : TRUE, because 33 is binary 100001, so the bit
'0' is 1 *)

### 6.3.2 PACK

This function can return eight input bits B0, B1,..., B7 of type BOOL as one
BYTE.

Example in CFC:

### 6.3.3 PUTBIT

The input of this function consists of a DWORD X, a BYTE N and a Boolean
value B.
PUTBIT sets the Nth bit of X to the value B, whereby counting starts with the
zeroth bit

Example in ST:

var1:=38;   (* binary 100110 *)
var2:=PUTBIT(A,4,TRUE); (* Result: 54 = 2#110110 *)
var3:=PUTBIT(A,1,FALSE); (* Result: 36 = 2#100100*)

### 6.3.4 UNPACK

The function block UNPACK converts input B of type BYTE into 8 output varia‐
bles B0,...,B7 of type BOOL, and is therefore the counterpart to the function
PACK.

Example in CFC:

## 6.4 Mathematical auxiliary functions

### 6.4.1 DERIVATIVE

The DERIVATIVE function block approximately determines the local time deriv‐
ative.
The function value is transferred as REAL variable via IN. TM contains the
elapsed time in ms in a DWORD and the RESET input of type BOOL can be
used to restart the function block by transferring the value TRUE.
The OUT output is of type REAL.
For the best possible result, DERIVATIVE approximates over the last four
values to minimize errors caused by (e.g. measurement) inaccuracies in the
input variables.

Function block in CFC:

### 6.4.2 INTEGRAL

The INTEGRAL function block approximately determines the integral of a func‐
tion over time.
As for DERIVATIVE, the function value is transferred as REAL variable via IN.
TM contains the elapsed time in ms in a DWORD and the RESET input of type
BOOL can be used to restart the function block with TRUE.
The OUT output is of type REAL.
The integral is approximated by a step function.
If the integral value reaches the end of the value range of a REAL variable
(approx. ±1038), the Boolean output variable OVERFLOW is set to TRUE and
the function block is disabled until it is reinitialized with RESET.

Function block in CFC:
Example: Integral over a linear function:

### 6.4.3 LIN_TRAFO

The LIN_TRAFO function block transforms a real value within a range defined
by lower and upper limits into a real value within the corresponding ratio in
another range, also defined by lower and upper limits.

It is based on the following equation:
(IN - IN_MIN) : (IN_MAX - IN) = (OUT - OUT_MIN) : (OUT_MAX - OUT)

Table 13: Inputs LIN_TRAFO
Variable                     Data type     Description
IN                           REAL          Input value
IN_MIN                       REAL          Smallest input value
IN_MAX                       REAL          Largest input value
OUT_MIN                      REAL          Smallest output value
OUT_MAX                      REAL          Largest output value

Table 14: Outputs LIN_TRAFO
Variable                     Data type     Description
OUT                          REAL          Output value
ERROR                        BOOL          Error output: TRUE if IN_MIN = IN_MAX, or if IN is
                                           beyond the given input range

Use case:
A temperature sensor supplies volt values to input IN. These are to be
changed into temperature values in degree Celsius and output in OUT.
The input (volt) range is defined as IN_MIN=0 and IN_MAX=10. The output
(degree Celsius) range is defined with OUT_MIN=-20 and OUT_MAX=40.
Accordingly, a temperature of 10 degrees Celsius is output for an input of 5
volts.

### 6.4.4 STATISTICS_INT

The STATISTICS_INT function block computes some default statistical values.
STATISTICS_INT corresponds to STATISTICS_REAL, except that the input IN
and the outputs MN, MX, AVG are of type INT.
The IN input is of type INT.
If the Boolean input RESET is TRUE, all values are reinitialized.
The output MN contains the minimum and MX the maximum value of IN. AVG
describes the average, i.e. the expected value of IN. All three outputs are of
type INT.

### 6.4.5 STATISTICS_REAL

The STATISTICS_REAL function block computes some statistical default
values.
STATISTICS_REAL corresponds to STATISTICS_INT, except that the input IN
and the outputs MN, MX, AVG are of type REAL.
The IN input is of type REAL.
If the Boolean input RESET is TRUE, all values are reinitialized.
The output MN contains the minimum and MX the maximum value of IN.
AVG describes the average, i.e. the expected value of IN. All three outputs are
of type REAL.

### 6.4.6 VARIANCE

The VARIANCE function block computes the variance of entered values.
The input IN is of type REAL, RESET is of type BOOL and the output OUT is
again of type REAL.
This function block computes the statistical variance from the values entered.
VARIANCE can be reinitialized with RESET=TRUE.

The standard deviation can easily be computed from the square root of VAR‐
IANCE.

## 6.5 Controller

### 6.5.1 PD

The "Util" library provides the PD controller function block.

Table 15: Inputs PD

Variable         Data type       Description
ACTUAL           REAL            Actual value of the control variable
SET_POINT        REAL            Command value, reference variable
KP               REAL            Proportionality coefficient, amplification factor of the P-term
TV               REAL            Lead time, amplification factor of the D-term;
           Specified in seconds, e.g. "0.5" for 500 ms
Y_MANUAL         REAL            Manual output value; is output to Y if MANUAL = TRUE
Y_OFFSET         REAL            Offset for control variable Y
Y_MIN, Y_MAX     REAL            Lower or upper limit for control variable Y. If Y falls below or
           exceeds these limits, the LIMITS_ACTIVE output is set to TRUE
           and Y is kept within the limits. This monitoring is only active if
           Y_MIN<Y_MAX.
MANUAL           BOOL            Switches manual control variable specification via Y_MANUAL on
           (TRUE) or off (FALSE)
RESET            BOOL            TRUE reinitializes the controller. During initialization, Y = Y_OFFSET.

Table 16: Outputs PD
Variable                     Data type        Description
Y                            REAL             Control variable computed by the function block (see
                                              in the following)
LIMITS_ACTIVE                BOOL             Indicates with TRUE that Y exceeded the permitted
                                              range (Y_MIN, Y_MAX).

Y_OFFSET, Y_MIN and Y_MAX are used to transform the control variable into a
specified range.
MANUAL can be used to switch to manual mode and RESET can be used to
reinitialize the controller.
In normal mode (MANUAL = RESET = LIMITS_ACTIVE = FALSE), the controller
computes the control error e as difference between SET_POINT - ACTUAL,
forms its derivative according to the time δe/δt and saves these values inter‐
nally.
The output, the control variable (Y), is computed as follows:

where Δ=SET_POINT-ACTUAL.
In addition to the P-term, the current change in the control error (D-term) is
also included in the control variable.
In addition, Y is limited to the permitted range between Y_MIN and Y_MAX.
If Y exceeds this range, LIMITS_ACTIVE becomes TRUE. To avoid limiting the
control variable, set Y_MIN and Y_MAX to 0.
When MANUAL is TRUE, Y_MANUAL is output.
A P-controller can easily be created by setting TV to 0.

### 6.5.2 PID

The "Util" library provides the PID controller function block.

In contrast to the PD controller, this function block contains an additional
REAL input TN for the integral action time in seconds (e.g. "0.5" for 500 ms).

Table 17: Inputs PID
Variable                     Data type        Description
ACTUAL                       REAL             Actual value of the control variable
SET_POINT                    REAL             Command value, reference variable
KP                           REAL             Proportionality coefficient, amplification factor of the
                                              P-term
TN                           REAL             Integral action time, amplification factor of the P-term;
                                              Specified in seconds, e.g. "0.5" for 500 ms
TV                           REAL             Lead time, amplification factor of the D-term;
                                              Specified in seconds
Y_MANUAL                     REAL             Manual output value; output to Y if MANUAL = TRUE
Y_OFFSET                     REAL             Offset for control variable
Y_MIN, Y_MAX                 REAL             Lower or upper limit for control variable Y. If Y falls
                                              below or exceeds these limits, the LIMITS_ACTIVE
                                              output is set to TRUE and Y is kept within the limits.
                                              This monitoring is only active if Y_MIN<Y_MAX.
MANUAL                       BOOL             Switches manual control variable specification via
                                              Y_MANUAL on (TRUE) or off (FALSE)
RESET                        BOOL             TRUE reinitializes the controller. During initialization, Y
                                              = Y_OFFSET.

Table 18: Outputs PID
Variable                     Data type     Description
Y                            REAL          Control variable computed by the function block (see
                                           in the following)
LIMITS_ACTIVE                BOOL          Indicates with TRUE that Y exceeded the permitted
                                           range (Y_MIN, Y_MAX).
OVERFLOW                     BOOL          Indicates an overflow with TRUE (see in the following)

Y_OFFSET, Y_MIN and Y_MAX are used to transform the control variable into a
specified range.
MANUAL can be used to switch to manual mode and RESET can be used to
reinitialize the controller.
In normal mode (MANUAL = RESET = LIMITS_ACTIVE = FALSE), the controller

calculates the control error e as difference between SET_POINT - ACTUAL,
forms its derivative according to the time δe/δt and saves these values inter‐
nally.
In contrast to the PD controller, the output, the control variable (Y), contains
an additional integral value and is computed as follows:

In addition to the P-term, the current change in the control error (D-term)
and the history of the control error (I-term) are also included in the control
variable.
The PID controller can easily be converted into a PI controller by setting TV=0.

The additional I-term can cause an overflow if the integral over the error Δ is
too large due to incorrect controller parameterization.
To be on safe side, a Boolean output OVERFLOW is therefore available, which
- in this case - becomes TRUE. This takes only place if the control system is
unstable due to incorrect parameterization. At the same time, the controller
pauses and is not enabled again until it is reinitialized.

### 6.5.3 PID_FIXCYCLE

The "Util" library provides the PID_FIXCYCLE controller function block.

This function block corresponds functionally to the ⮫ PID controller except
that the cycle time is not automatically measured internally, but specified in
seconds via the CYCLE input.

## 6.6 Signal generator

### 6.6.1 BLINK

The BLINK function block generates a pulsating signal. The input consists of
ENABLE of type BOOL, as well as TIMELOW and TIMEHIGH of type TIME. The
OUT output is of type BOOL.
If ENABLE is set to TRUE, BLINK starts to alternately set the output to TRUE
for the TIMEHIGH period and then to FALSE for the TIMELOW period.
If ENABLE is set to FALSE again, the OUT output is no longer changed, i.e. no
further pulses are generated. If OUT should also become FALSE when ENABLE
is reset, use "OUT AND ENABLE" (i.e. by inserting an AND block with the
parameter ENABLE) at the output.

Example in CFC:

### 6.6.2 FREQ_MEASURE

The FREQ_MEASURE function block measures the (average) frequency (Hz) of
a Boolean input signal.
The number of measurement periods to be averaged can be defined.
A measurement period is the period between two rising edges of the input
signal.

Table 19: FREQ_MEASURE inputs
Variable                     Data type     Description
IN                           BOOL          Input signal
PERIODS                      INT           Number of measurement periods, i.e. the periods
                                           between the rising edges used to determine the
                                           average frequency of the input signal.
                                           Possible values: 1 to 10
RESET                        BOOL          Reset all parameters to 0

Table 20: FREQ_MEASURE outputs
Variable                     Data type     Description
OUT                          REAL          Determined frequency in [Hz]
VALID                        BOOL          FALSE,
                                           when the measurement is not yet completed,
                                           or if PERIODS > 3*OUT, which indicates an error
                                           regarding the input signal.

### 6.6.3 GEN

The function generator creates typical periodic functions.
The inputs consist of MODE of the predefined enumeration type GEN_MODE,
BASE of type BOOL, PERIOD of type TIME, two INT values CYCLES and
AMPLITUDE and the Boolean RESET input. An INT with the name OUT is

output.
The MODE describes the function to be generated, whereby the enumera‐
tion values TRIANGLE and TRIANGLE_POS provide two triangular functions,
SAWTOOTH_RISE a rising, SAWTOOTH_FALL a falling sawtooth, RECTANGLE a
square wave signal and SINUS and COSINUS the sine and cosine:

BASE specifies whether the period duration actually refers to a specified time
(then BASE=TRUE) or to a certain number of cycles, i.e. calls of the function
block (BASE=FALSE).
PERIOD or CYCLES then define the corresponding period duration.
AMPLITUDE defines the amplitude of the function to be generated.
The function generator is reset to 0 when RESET=TRUE.

Example in CFC:

## 6.7 Function manipulators

### 6.7.1 CHARCURVE

The CHARCURVE function block is used to map values to a piecewise linear
function.

IN of type INT is fed with the value to be manipulated.
The BYTE N indicates the number of points defining the mapping function.
In the ARRAY CC: ARRAY[0..10] OF POINT, with POINT, a structure consisting
of two INT values (X and Y), this characteristic curve is then defined.
The OUT output of type INT contains the manipulated value. ERR of type BYTE
might indicate errors.

Errors
● The points P[0]..P[N-1] in the ARRAY have to be sorted according to their
  X-values, otherwise ERR receives the value 1.
● If the input IN is not between P[0].X and P[N-1].X, ERR=2 and OUT gets
  the corresponding limit value P[0].Y or P[N-1].Y.
● If N is beyond the permitted value range from 2 to 11, ERR=4.

Example in ST:
First, the instance CharCurve01, the ARRAY CC and the variable Count have
to be defined in the declaration part:

Declaration:

VAR
 ...
 CharCurve01:CHARCURVE;
 CC:ARRAY[0..10] OF POINT:=(X:=0,Y:=0),(X:=250,Y:=50),

   (X:=500,Y:=150),(X:=750,Y:=400),7((X:=1000,Y:=1000));
 Count:INT;
 ...
END_VAR

The variable Count is incremented with each processing and thus the input
value for CharCurve01 increases.

Example in ST:

Count:=Count+10;
CharCurve01(IN:=Count,N:=5,P:=CC);

This is shown with the subsequent tracing:

### 6.7.2 RAMP_INT

The RAMP_INT function block is used to limit the rise or fall of the fed-in
function.
RAMP_INT works exactly like RAMP_REAL, except that the inputs IN, ASCEND,
DESCEND and the output OUT are of type INT.
The input consists of three INT values: IN, the function input, and ASCEND
and DESCEND, the maximum increase or decrease per time interval defined
by TIMEBASE of type TIME. If RESET is set to TRUE, RAMP_INT is reinitialized.
The OUT output of the INT type contains the function value limited in terms of
increase and decrease.
Note that problems may arise if the TIMEBASE set is less than the duration of
one cycle.
If TIMEBASE is set to t#0s, the increase or decrease limit refers to one cycle,
i.e. one call of the function block.

Example in CFC:

### 6.7.3 RAMP_REAL

The RAMP_REAL function block is used to limit the rise or fall of the fed-in
function.
RAMP_REAL works exactly like RAMP_INT, except that the inputs IN, ASCEND,
DESCEND and the output OUT are of type REAL.
The input consists of three REAL values: IN, the function input, and ASCEND
and DESCEND, the maximum increase or decrease per time interval defined
by TIMEBASE of type TIME.
If RESET is set to TRUE, RAMP_REAL is reinitialized.
The OUT output of the REAL type contains the function value limited in terms
of increase and decrease.
Note that problems may arise if the TIMEBASE set is less than the duration of
one cycle.
If TIMEBASE is set to t#0s, the increase or decrease limit refers to one cycle,
i.e. one call of the function block.

Example in CFC:

## 6.8 Analog value processing

### 6.8.1 HYSTERESIS

The input of this function block consists of the three INT values IN, HIGH and
LOW. The OUT output is of type BOOL.

If IN falls below the LOW limit value, OUT becomes TRUE. If IN exceeds the
upper limit HIGH, FALSE is output.

Example:

### 6.8.2 LIMITALARM

The LIMITALARM function block indicates whether the input value is within a
specified interval and which limit it could exceed.
The input values IN, HIGH and LOW are each of type INT, the output values O,
U and IL are of type BOOL.
If the upper limit HIGH of IN is exceeded, O becomes TRUE; if it falls below
LOW, U becomes TRUE.

However, if IN is between LOW and HIGH, IL becomes TRUE.

Example in CFC:
