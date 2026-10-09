# 37 CXA_Winder

## 37.1 Introduction and overview

The CXA_Winder library provides functionalities to wind and unwind webs
(winders).

Function blocks of the CXA_Winder library
Function block                   Description
⮫ MB_WinderSpeedAdapter          Component function block
⮫ MB_CalculateInertiaLimit       Component function block
⮫ MB_DiameterCalculator          Component function block
⮫ MB_DiameterMeasurement         Component function block
⮫ MB_DancerControl               Component function block
⮫ MB_WinderDancerCtrlType01 Main function block
⮫ MB_WinderTensionCtrlType01 Main function block
⮫ MB_WinderTensionCtrlType02 Main function block

                                                                               Data types                1344

## 37.2 Data types

### 37.2.1 MB_PIDCONTROL_DATA (STRUCT)

Brief description
The MB_PIDCONTROL_DATA data structure describes the data of the PID con‐
troller.

Table 1206: MB_PIDCONTROL_DATA data structure
Name         Type            Min. value Max. value        Default       Effective              Description
                                                          value
PControl     LREAL           0.0          n. def.         0.0           Continuous             Kp gain of the tension controller

IControl     LTIME           0.0          n. def.         0.0           Continuous             Tn integral lagging time of the ten‐
                                                                    sion controller
DControl     LREAL           0.0          n. def.         0.0           Continuous             Offset gain

### 37.2.2 MB_WIND_CTRL_TYPE (ENUM)

Brief description
The enumeration type MB_WIND_CTRL_TYPE allows to select the open tension
control (sensorless) or closed tension control (load cell).

Table 1207: MB_WIND_CTRL_TYPE enumeration type
Name                        Value        Effective                                  Description
OPEN_LOOP                  16#0000       At a rising edge at "Enable"               Winding type "open-loop", without sensor
CLOSED_LOOP                16#0001       At a rising edge at "Enable"               Winding type "closed-loop", with load cell

### 37.2.3 MB_WIND_DANCER_LIMITS (STRUCT)

Brief description
The MB_WIND_DANCER_LIMITS data structure describes the limiter of the
controller control variable in the diagram.

Table 1208: MB_WIND_DANCER_LIMITS data structure
Name                Type           Min. value   Max. value Default          Effective             Description
                                                           value
LowLimitControl LREAL              0.0          N. def.         0.0         Continuous            Lower limitation of the controller
                                                                                                  output (at a speed of 0) bipolar
                                                                                                  [min^-1] (the value is internally
                                                                                                  standardized with the diameter
                                                                                                  ratio of ReferenceDiameter and
HighLimitControl LREAL             0.0          N. def.         0.0         Continuous            Upper limitation of the controller
                                                                                                  output (at a speed of Velocity‐
                                                                                                  HighLimit) bipolar [min^-1] (the
                                                                                                  value is internally standardized
                                                                                                  with the diameter ratio of Ref‐
                                                                                                  erenceDiameter and MinRefDia‐
VelocityHighLimit LREAL            0.0          N. def.         0.0         Continuous            Speed of the master for HighLi‐
                                                                                                  mitControl [min^-1]

1274 /      ctrlX PLC Engineering
1344        Data types

### 37.2.4 MB_WIND_DIAM_CALC_MODE (ENUM)

Brief description
The enumeration type MB_WIND_DIAM_CALC_MODE allows to select the type
of diameter computation.

Table 1209: MB_WIND_DIAM_CALC_MODE enumeration type
Name                       Value           Effective                       Description
CALC_DIAM_MANUAL           16#0000         At a rising edge at "Enable"    Diameter computation depending on "CalcRange"
FIRST_REV_AUTO_CALC        16#0001         At a rising edge at "Enable"    Diameter computation is executed after every 3
                                                                           degrees for the first revolution. Thereafter, it
                                                                           depends on the "CalcRange"

### 37.2.5 MB_WIND_DIAMETER (STRUCT)

Brief description
The MB_WIND_DIAMETER data structure describes the data required for the
diameter calculator.

Table 1210: MB_WIND_DIAMETER data structure
Name               Type            Min. value     Max. value      Default value Effective       Description
PresetVal          LREAL           > 0.0          N. def.         100.0          Continuous     Default value for the preset
                                                                                                diameter [mm]
CoreVal            LREAL           > 0.0          N. def.         100.0          Rising edge at Diameter of the core [mm]
                                                                                 "Enable"
CalcRange          LREAL           0.0            N. def.         360.0          Continuous     Range for diameter com‐
                                                                                                putation [degrees] (load-
RepeatLength       LREAL           > 0.0          N. def.         100.0          Rising edge at Format length [mm]
                                                                                 "Enable"       (1 revolution of the refer‐
                                                                                                ence axis unwound)
Webwidth           LREAL           0.0            N. def.         0.0            Rising edge at Web width [mm]
                                                                                 "Enable"       (is required for the moment
                                                                                                of inertia)
Density            LREAL           0.0            N. def.         1.0            Rising edge at Material density [kg/dm3]
                                                                                 "Enable"       (is required for the moment
                                                                                                of inertia)
AverageValue       UINT            0              20              1              Continuous     Number of diameter values
                                                                                                to be averaged [-]
HighLimit          LREAL           LowLimit       N. def.         2000.0         Continuous     Upper limit for the diameter
                                                                                                The diameter is limited to
                                                                                                this value
LowLimit           LREAL           > 0.0          HighLimit       100.0          Continuous     Lower limit for the diameter
                   LREAL                                                                        [mm]
                                                                                                The diameter does not fall
                                                                                                below this value
MinDiameter        LREAL           > 0.0          N. def.         100.0          Continuous     Minimum diameter [mm]
MaxDiameter        LREAL           > 0.0          N. def.         2000.0         Continuous     Maximum diameter [mm]

   Data types               1344

Name                Type          Min. value   Max. value   Default value Effective     Description
MechanicInertia     LREAL         0.0          N. def.      0.0           Continuous    Moment of inertia of the
mechanics [kg m2] based on
the motor side
(is required for the resulting
moment of inertia)
DancerConstant      LREAL         0.0          N. def.      0.0           Continuous    Displacement of the dancer,
(is only required                                                                       based on the unit of dancer
for a winder with                                                                       adjustment [mm/-]
dancer)                                                                                 (is only required for a
winder with dancer)
MeasuredVal         LREAL         0.0          n. def       0.0           Continuous    Measured diameter [mm]

PivotVelocity       LREAL         0.0          N. def.      0.0           Continuous    Pivot velocity (for relative
motion of the winding axis)
[mm/s]
DiamCalcMode        ⮫ MB_WIND_ CALC_DIAM_      FIRST_REV_A CALC_DIAM_     Rising edge at Diameter computation mode
DIAM_CALC_ MANUAL          UTO_CALC    MANUAL         "Enable"       CALC_DIAM_MANUAL
MODE
Diameter computation
depending on CalcRange
FIRST_REV_AUTO_CALC
Diameter computation is
executed after every 5
degrees for the first revolu‐
tion. Thereafter, it depends
on the CalcRange
DiamSource          BOOL                                                  Rising edge at Diameter determination:
"Enable"       FALSE:
Diameter is computed
TRUE:
Diameter is measured
(MeasuredVal)
MinRefDiameter‐     LREAL         0.0          N. def.      100.0         Rising edge at Minimum reference diameter
Dancer                                                                    "Enable"       for winders with dancer

### 37.2.6 MB_WIND_DIRECTION (ENUM)

Brief description
The enumeration type MB_WIND_DIRECTION allows to select the type of
winding direction.

Table 1211: MB_WIND_DIRECTION enumeration type
Name                 Value         Effective                                Description
REWIND              16#0000        At a rising edge at "Enable"             Rewinder
UNWIND              16#0001        At a rising edge at "Enable"             Unwinder

### 37.2.7 MB_WIND_FRICTION (STRUCT)

Brief description
The MB_WIND_FRICTION data structure characterizes the friction torque.

1276 /      ctrlX PLC Engineering
1344        Data types

Table 1212: MB_WIND_FRICTION data structure
Name                 Type        Min.       Max.       Default Effective                Description
                                 value      value       value
StandstillTorque     LREAL        0.0      N. def.          0.0     Continuous          Friction torque at standstill
MaxTorque            LREAL        0.0      N. def.          0.0     Continuous          Friction torque at S-0-0091, Velocity limit
                                                                                        value, bipolar
MinTorque            LREAL        0.0      N. def.          0.0     Continuous          Minimum friction torque
MinTorqueVelocity    LREAL        0.0      N. def.          0.0     Continuous          Velocity at minimum friction torque

### 37.2.8 MB_WIND_TENS_DIAG (STRUCT)

Brief description
The MB_WIND_TENS_DIAG data structure describes individual components of
the torque limit value as well as the current actual tension value for diagnostic
purposes.

Table 1213: MB_WIND_TENS_DIAG data structure
Structural element    Type      Min. value Max.             Default      Effective           Description
                                           value            value
TensionCtrlOutput     LREAL     N. def.     N. def.         0.0          Continuous          Output of the tension controller [N]
TorqueLimit           LREAL     n. def.     N. def.         0.0          Continuous          Signed torque limit [%]
AccelerationTorque    LREAL     N. def.     N. def.         0.0          Continuous          Current acceleration torque [%]
FrictionTorque        LREAL     n. def      n. def          0.0          Continuous          Current friction torque [%]
CurrentTension        LREAL     0.0         N. def.         0.0          Continuous          Current actual tension value [N]

### 37.2.9 MB_WIND_TENSION (STRUCT)

Brief description
The MB_WIND_TENSION data structure describes the data of the tension con‐
troller.

Table 1214: MB_WIND_TENSION data structure
Name                 Type       Min.      Max.      Default Effective                Description
                                value     value      value
PControl             LREAL        0.0     N. def.     0.0         Continuous         Kp gain of the tension controller
IControl             LTIME        0.0     N. def.     0.0         Continuous         Tn integral action time of the tension con‐
                                                                                     troller
FeedbackVal          LREAL        0.0     N. def.     0.0         Continuous         Actual value of the tension
PreControl‐          LREAL        0.0     N. def.     1.0         Continuous         Scaling of the command value addition
Weighting
HighLimit            LREAL        0.0     N. def.     0.0         Continuous         Upper limit of the tension controller
LowLimit             LREAL        0.0     N. def.     0.0         Continuous         Lower limit of the tension controller

### 37.2.10 MB_WIND_TENSION_MODE (ENUM)

Brief description
The enumeration type MB_WIND_TENSION_MODE allows to select the mode
to tension the material web.

Table 1215: MB_WIND_TENSION_MODE enumeration type
Name                    Value     Effective                                    Description
CONST_SPEED            16#0000    At a rising edge at "Enable"                 Tensioning method: Constant tensioning speed
CONST_WEB_VEL          16#0001    At a rising edge at "Enable"                 Tensioning method: Constant path velocity

                                                                     Function blocks           1344

### 37.2.11 MB_WIND_TOURQUE_LIMITS (STRUCT)

    The structure contains values for bipolar torque limit S-0-0092.

Table 1216: MB_WIND_TOURQUE_LIMITS data structure
Name                  Type       Min. Max.     Default   Effective          Description
                                 value value   value
DefaultTourqeLimit    LREAL      0.0   400.0   100.0     Continuous         Value for the bipolar torque limit after
                                                                            removing "Enable" [%]
TourqeLimitFactor     LREAL      0.0   400.0   50.0      Continuous         Factor by which the computed TorqueLimit is
                                                                            increased [%]
MinTourqueLimit       LREAL      0.0   400.0   10.0      Continuous         Minimum TorqueLimit by which the com‐
                                                                            puted TorqueLimit is increased [%]

## 37.3 Function blocks

### 37.3.1 MB_WinderSpeedAdapter

    Brief description
    The function block executes an adaptation of the Kp-gain of the speed con‐
    troller of the respective winding drive that depends on the current moment of
    inertia of the winder and a minimum and maximum Kp-value.

    Interface description

Table 1217: Interface variables of the MB_WinderSpeedAdapter function block
I/O type            Name                  Data type                  Description
VAR_INPUT           Enable                BOOL                       Function block processing enabled (once,
                                                                     edge-controlled)
                    Pause                 BOOL                       Function block pauses, CurrentPControl
                                                                     remains "frozen"
                    PControlMax           LREAL                      Kp-gain for maximum diameter [Nm/
                                                                     (rad/s)]
                    PControlMin           LREAL                      Kp-gain for minimum diameter [Nm/
                                                                     (rad/s)]
                    InertiaMax            LREAL                      Moment of inertia at maximum diameter or
                                                                     moment of inertia [kg*m2] (related to the
                                                                     motor shaft)

1278 /     ctrlX PLC Engineering
1344       Function blocks

I/O type           Name                Data type             Description
InertiaMin          LREAL                 Moment of inertia at minimum diameter
                                          (core) or moment of inertia [kg*m2]
                                          (related to the motor shaft)
CurrentInertia      LREAL                 Current moment of inertia of the winder
                                          [kg/m2] (related to the motor shaft)
VAR_OUTPUT InOperation                 BOOL                  Processing completed without errors,
                                          output data valid
Error               BOOL                  Processing completed with error
ErrorID             ⮫ ERROR_CODE          Diagnostic description in case of error
ErrorIdent          ⮫ ERROR_STRUCT Detailed diagnostics
InPause             BOOL           Function block pauses (CurrentPControl
                                   "frozen")
CurrentPControl     LREAL          Current Kp-value (speed controller) [Nm/
                                   (rad/s)]
VAR_IN_OUT         Slave               ⮫ AXIS_REF     Axis structure of the winding axis
CONSTANT

Table 1218: Min./max. and default values of the inputs of the MB_WinderSpeedAdapter function
block
Name               Type              Min. value    Max. value        Default value   Effective
Enable             BOOL                                              FALSE           Continuous
Pause              BOOL                                              FALSE           Continuous
DisableCyclic‐     BOOL                                              FALSE           Continuous
Writes
PControlMax        LREAL             PControlMin   n. def.           0.0             Continuous
PControlMin        LREAL             0.0           n. def.           0.0             Continuous
InertiaMax         LREAL             InertiaMin    n. def.           0.0             Continuous
InertiaMin         LREAL             0.0.          n. def.           0.0             Continuous
CurrentInertia     LREAL             0.0           n. def.           0.0             Continuous

     Functional description
     The function block linearly calculates the value for the Kp of the speed con‐
     troller depending on the current moment of inertia. This value is calculated
     between a minimum and maximum value. The minimum and maximum Kp
     have to be determined at empty core and at full winding diameter. Further‐
     more, the values for the minimum and maximum moment of inertia (at the
     core or at full winding diameter) are required. These can be determined using
     the function block ⮫ MB_CalculateInertiaLimit.
     The current Kp-value of the speed controller is calculated from these values
     with regard to the current moment of inertia of the winder.

                                                       Function blocks       1344

### 37.3.2 MB_CalculateInertiaLimit

Brief description
The function block MB_CalculateInertiaLimit represents a non-cyclic function
block in contrast to the other function blocks described in this documenta‐
tion. It is systematically, for example, called for the initialization of another
function block.
In this function block, the material properties and dimensions of the web
of fabric are analyzed and the maximum moment of inertia at the maximum
diameter "MaxDiameter" is calculated for the winding material on the winder.
The calculated maximum moment of inertia "MaxInertia" can be used for the
MB_WinderSpeedAdapter for example. The proportional gain between a min‐
imum value and a maximum value can be adapted. For example, a linear
increase of the proportional gain factor can be set.

Interface description

Table 1219: Interface variables of the MB_CalculateInertiaLimit function block
I/O type       Name                 Data type           Description
VAR_INPUT      Execute              BOOL                Enabling the function block (edge-con‐
                                                        trolled)
               WebWidth             LREAL               Web width [mm]
               Density              LREAL               Material density of the web [kg/dm3]
               MaxDiameter          LREAL               Maximum diameter of the winder [mm]

1280 /     ctrlX PLC Engineering
1344       Function blocks

I/O type   Name                       Data type              Description
CoreDiameter               LREAL                  Core diameter of the winder [mm]
VAR_OUTPUT Done                       BOOL                   Maximum moment of inertia "MaxInertia"
                                          calculated
Active             BOOL                   Processing, function block active
Error              BOOL                   Processing completed with error
ErrorID            ⮫ ERROR_CODE           Diagnostic description in case of error
ErrorIdent         ⮫ ERROR_STRUCT Detailed diagnostics
MaxInertia         LREAL          Maximum moment of inertia [kg/m2] refer‐
                                  ring to the motor side
VAR_IN_OUT         Slave              ⮫ AXIS_REF     Axis structure of the winding axis

Table 1220: Min./max. and default values of the inputs of the MB_CalculateInertiaLimit function
block
Name               Type            Min. value      Max. value        Default value   Effective
Execute            BOOL                                              FALSE           Continuous
Webwidth           LREAL           0.0             N. def.           0.0             Rising edge at
                                                                                     "Execute"
Density            LREAL           0.0             N. def.           1.0             Rising edge at
                                                                                     "Execute"
MaxDiameter        LREAL           > 0.0           n. def            2000.0          Rising edge at
                                                                                     "Execute"
CoreDiameter       LREAL           > 0.0           N. def.           100.0           Rising edge at
                                                                                     "Execute"

     Functional description
     With the core diameter of the winder "CoreDiameter", the web width "Web‐
     Width" and the density of the web of the fabric "Density", the moment of
     inertia "MaxInertia" is calculated for the specified maximum diameter "Max‐
     Diameter".

### 37.3.3 MB_DiameterMeasurement

     Brief description
     The function block MB_DiameterMeasurement calculates and loads a meas‐
     ured diameter and calculates the velocity adaptation for the winding axis and
     the current moment of inertia of the winding material on a winder. The func‐
     tion block is called for every winding axis, where the diameter is measured.
     Cyclic output variables are the resulting gear fine adjustment for the respec‐
     tive winding drive "GearRatioFineAdjust" and the current moment of inertia of
     the winding material "CurrentInertia".
     The gear fine adjustment "GearRatioFineAdjust" has to be set manually to the
     synchronization functionality, e.g. MB_GearInPos/MB_GearInVel.

                                                        Function blocks      1344

      Interface description

Table 1221: Interface variables of the MB_DiameterMeasurement function block
I/O type       Name                Type             Comment
VAR_INPUT      Enable              BOOL             Function block processing enabled (level-
                                                    controlled)
               Pause               BOOL             Function block pauses, gear fine adjust‐
                                                    ment remains "frozen"
               MeasuredDiameter LREAL               Measured diameter [mm]
               FormatLength     LREAL               Format length [mm]
                                                    (1 revolution of the master axis unwound)
               MinDiameter         LREAL            Minimum diameter [mm],
                                                    is only used for display purposes by the
                                                    "MinAvDiamAchieved" output
               MaxDiameter         LREAL            Maximum diameter [mm],
                                                    is only used for display purposes by the
                                                    "MaxAvDiamAchieved" output
               WebWidth            LREAL            Web width [mm]
               Density             LREAL            Material density [kg/dm3]
               AverageValue        UDINT            Number of diameter values to be averaged.
                                                    Input is limited to 30
               HighLimitDiameter LREAL              Upper limit for the diameter [mm]
                                                    The diameter is limited to this value
               LowLimitDiameter LREAL               Lower limit for the diameter [mm]
                                                    The diameter is limited to this value
           CoreDiameter            LREAL            Core diameter of the winder [mm]
VAR_OUTPUT InOperation             BOOL             Function block operating
           Error                   BOOL             Processing completed with error
           ErrorID                 ⮫ ERROR_CODE     Diagnostic description in case of error
               ErrorIdent          ⮫ ERROR_STRUCT Detailed diagnostics
               InPause             BOOL           Dancer controller pausing

1282 /     ctrlX PLC Engineering
1344       Function blocks

I/O type           Name                Type                   Comment
MinAvDiamA‐         BOOL                   Minimum diameter reached
chieved                                    (Refers to the averaged diameter)
MaxAvDiamA‐         BOOL                   Maximum diameter reached
chieved                                    (Refers to the averaged diameter)
HighLimitActive     BOOL                   Currently calculated diameter reached
                                           upper limit
                                           (Diameter value is discarded)
LowLimitActive      BOOL                   Currently calculated diameter reached
                                           lower limit
                                           (Diameter value is discarded)
GearRatioFineAd‐    LREAL                  Gear fine adjustment for speed lagging of
just                                       the drive [%]
CurrentInertia      LREAL                  Current total moment of inertia
                                           (related to the motor side) [kg*m2]
VAR_IN_OUT         Slave               ⮫ AXIS_REF             Reference to slave axis
CONSTANT

Table 1222: Min./max. and default values of the inputs of the MB_DiameterMeasurement function
block
Name               Type              Min. value     Max. value        Default value   Effective
Enable             BOOL                                               FALSE           Continuous
Pause              BOOL                                               FALSE           Continuous
MeasuredDia‐       LREAL             > 0.0          N. def.           100.0           Continuous
meter
FormatLength       LREAL             > 0.0          N. def.           100.0           Rising edge at
                                                                                      "Enable"
MinDiameter        LREAL             > 0.0          N. def.           100.0           Continuous
MaxDiameter        LREAL             > 0.0          N. def.           2000.0          Continuous
Webwidth           LREAL             0.0            N. def.           0.0             Rising edge at
                                                                                      "Enable"
Density            LREAL             0.0            N. def.           1.0             Rising edge at
                                                                                      "Enable"
AverageValue       UDINT             0              30                1               Continuous
HighLimitDia‐      LREAL             0.0            N. def.           2000.0          Continuous
meter
LowLimitDia‐       LREAL             0.0            N. def.           100.0           Continuous
meter
CoreDiameter       LREAL             0.0            N. def.           100.0           Rising edge at
                                                                                      "Enable"

     Functional description
     The function block MB_DiameterMeasurement reads a measured diameter
     value (e.g. with an ultra-sound sensor) and ensures the correct velocity
     adjustment of the respective winding axis based on the diameter measured.
     The function block is used in the function blocks⮫ MB_WinderDancerCtrl‐
     Type01, ⮫ MB_WinderTensionCtrlType01 und ⮫ MB_WinderTensionCtrlType02.
     The ratio "FormatLength"/"CoreDiameter" may not be greater than 25. Other‐
     wise, the gear adjustment via the gear fine adjustment is insufficient.

                                                             Function blocks      1344

### 37.3.4 MB_DiameterCalculator

      Brief description
      The function block MB_DiameterCalculator cyclically calculates the current
      diameter, the velocity adaptation for the winding axis and the current moment
      of inertia of the winding material on a winder. The function block is called for
      each winding axis. Cyclic output variables are the current winding diameter
      "CurrentDiameter", the resulting fine adjustment of the gear for the respective
      winding drive "GearRatioFineAdjust" and the current moment of inertia of the
      winding material "CurrentInertia".

      Interface description

Table 1223: Interface variables of the MB_DiameterCalculator function block
I/O type       Name                Type                Comment
VAR_INPUT      Enable              BOOL                Function block processing enabled (level-
                                                       controlled)
               Preset              BOOL                Preset of the current winding diameter
               Pause               BOOL                Diameter calculator pauses (level-con‐
                                                       trolled)
               PresetDiameter      LREAL               If this input is set, the cyclic data is not
                                                       written directly to the optional cyclic data
                                                       container, but only displayed at the output
               FormatLength        LREAL               Format length [mm]
                                                       (corresponds to an unwound revolution of
                                                       the reference axis)
               MinDiameter         LREAL               Minimum diameter [mm]
                                                       Is only used for display purposes by the
                                                       "MinAvDiamAchieved" output
               MaxDiameter         LREAL               Maximum diameter [mm]
                                                       Is only used for display purposes by the
                                                       "MaxAvDiamAchieved" output

1284 /     ctrlX PLC Engineering
1344       Function blocks

I/O type           Name              Type              Comment
FeedBackDancer    LREAL             Actual dancer position value
                                    (only for the "Winder with dancer" function‐
                                    ality)
DancerConstant    LREAL             Web distance when adjusting the dancer
                                    roll related to the unit of the dancer adjust‐
                                    ment [mm]
                                    Sign has to be set depending on the dancer
                                    design!
                         (only for the "Winder with dancer" function‐
                         ality)
WebWidth          LREAL          Web width [mm]
Density           LREAL          Material density [kg/dm3]
AverageValue      UDINT          Number of diameter values to be averaged.
                         Input is limited to 30
HighLimitDiameter LREAL          Upper limit of the diameter [mm]. The
                         diameter is limited to this value
LowLimitDiameter LREAL           Lower limit of the diameter [mm]. The
                         diameter does not fall below this value
CoreDiameter      LREAL          Core diameter of the winder [mm]
DiamCalcRange     LREAL          Range for the diameter calculation
                         [degrees]. Specifies the number of degrees
                         after which the diameter should be calcu‐
                         lated on a regular basis. Relates to the
                         winding axis (load-sided)
DiamCalcMode      MB_WIND_DIAM_C Diameter calculation mode
          ALC_MODE
PivotVelocity     LREAL          Pivot velocity of the winder (relative
                         velocity to the winder motion) [mm/s]
                         This corrects the diameter calculation if
                         there is a relative motion of the winding
                         axis
VAR_OUTPUT InOperation       BOOL           Function block operating
Error             BOOL           Processing completed with error
ErrorID           ⮫ ERROR_CODE   Diagnostic description in case of error
ErrorIdent        ⮫ ERROR_STRUCT Detailed diagnostics
PresetAck         BOOL           Preset diameter was applied (set as long as
                                 "Preset" is present)
InPause           BOOL           Diameter calculator paused
MinAvDiamA‐       BOOL           Minimum diameter reached
chieved                          (Refers to the averaged diameter)
MaxAvDiamA‐       BOOL           Maximum diameter reached
chieved                          (Refers to the averaged diameter)
HighLimitActive   BOOL           Currently calculated diameter reached
                                 upper limit
                                 (Diameter value is discarded)
LowLimitActive    BOOL           Currently calculated diameter reached
                                 lower limit.
                                 (Diameter value is discarded)
CurrentDiameter   LREAL          Current winding diameter

                                                               Function blocks        1344

I/O type        Name               Type                   Comment
GearRatioFineAd‐   LREAL                  Gear fine adjustment for speed lagging of
just                                      the drive [%]
CurrentInertia     LREAL                  Current total moment of inertia (related to
                                          the motor side) [kg*m2]
VAR_IN_OUT      Master             ⮫ AXIS_REF             Reference to the master axis
Slave              ⮫ AXIS_REF             Reference to slave axis

Table 1224: Min./max. and default values of the inputs of the MB_DiameterCalculator function
block
Name            Type            Min. value      Max. value         Default value    Effective

Enable          BOOL                                               FALSE            Continuous
Preset          BOOL                                               FALSE            Continuous
Pause           BOOL                                               FALSE            Continuous
PresetDia‐      LREAL           > 0.0           N. def.            100.0            Rising edge at
meter                                                                               "Preset"
FormatLength    LREAL           > 0.0           N. def.            100.0            Rising edge at
                                                                    "Enable"
MinDiameter     LREAL           > 0.0           N. def.            100.0            Continuous
MaxDiameter     LREAL           > 0.0           N. def.            2000.0           Continuous
FeedBack‐       LREAL           0.0             N. def.            0.0              Continuous
Dancer
Dancer‐         LREAL           N. def.         N. def.            0.0              Continuous
Constant
WebWidth        LREAL           0.0             N. def.            0.0              Rising edge at
                                                                    "Enable"
Density         LREAL           0.0             N. def.            1.0              Rising edge at
                                                                    "Enable"
AverageValue    UDINT           1               30                 1                Continuous
HighLimitDia‐   LREAL           0.0             N. def.            2000.0           Continuous
meter
LowLimitDia‐    LREAL           0.0             N. def.            100.0            Continuous
meter
CoreDiameter    LREAL           0.0             N. def.            100.0            Rising edge at
                                                                    "Enable"
DiamCal‐     LREAL              0.0             N. def.            360.0            Continuous
cRange
DiamCalcMode ENUM                                                  0                Rising edge at
                                                                    "Enable"
PivotVelocity   LREAL           0.0             N. def.            0.0              Continuous

     Functional description
     Preset of the diameter
     Since the calculated diameter directly affects the winding axis velocity via the
     resulting fine adjustment, a reasonable value has to be preset for the diameter
     at the start of the calculation when activating the diameter calculator. Thus,
     a value for the diameter, which is close to the actual diameter, should be
     specified at the input "PresetDiameter" and a Preset should be performed. For
     a rewinder, the value should be slightly lower and for an unwinder, it should
     be slightly higher. This allows an easier startup in each case.

1286 /    ctrlX PLC Engineering
1344      Function blocks

With each new roll, preset the winding diameter once upon start. Use the
"Preset" input. The diameter is set to the value of the "PresetDiameter" input.
Setting the diameter using "Preset" is always possible without setting the
"Pause" input.
After switching on the control, the winding diameter, the gear fine adjustment
and the moment of inertia are all equal zero. This means that a preset should
be performed each time the control is switched on to preset the respective
variables with reasonable values. If this is not done, no reasonable value can
be calculated for the current winding diameter. This can cause a malfunction
of the diameter calculator and thus lead to a winder stop.
If it is not possible to specify a correct Preset value for the initial winding,
we recommend the use of the "auto-calc mode" to calculate the diameter
(FIRST_REV_AUTO_CALC). In this mode, the range of diameter calculation
(DiamCalcRange) is automatically adjusted for the first winding axis revolu‐
tion after the start to obtain a reasonable starting diameter more quickly.
If the current diameter is to be kept after the control has been switched off,
the "CurrentDiameter" output has to be copied to a remanent variable. After
switching on, use this value for a preset.
Diameter calculation
The calculation of the diameter is proportional to the quotient from the refer‐
ence axis velocity nRef and the winding axis velocity nWinder and to the format
length F (corresponding to an unwound revolution of the reference axis).

The ratio "FormatLength" / "CoreDiameter" may not be greater than 25.
Otherwise, the gear adjustment via the gear fine adjustment is insufficient!
The reference axis has to rotate to calculate the diameter.

Average determination
The calculated current diameter "CurrentDiameter" can be averaged by setting
the "AverageValue" input.
The number of the diameter values to be averaged is applied at "Average‐
Value". Only the current internally calculated diameters within the limits of
"HighLimitDiameter" and "LowLimitDiameter" contribute to the generation of
the average value. Values beyond these limits are discarded. Values between 1
and 10 are appropriate for "AverageValue". Therefore, "AverageValue" is limited
to 30. If a higher value is entered, "AverageValue" is limited to 30. The higher
the number selected, the more precise the calculated diameter. However, the
accuracy of the diameter is reduced by increasing values for "AverageValue",
as it is lagging due to the "filtering". Thus, select a reasonable value for
"AverageValue". With smaller winding diameters, the variation in the diameter
values calculated is higher. Therefore, the value of the filter may not be too
high. Otherwise, the delay of the diameter calculated, caused by averaging,
would result in a distinct "lagging" of the diameter calculated. For a winder
with dancer for example, this can result in an unintended displacement of the
dancer.
Calculation of the moment of inertia

                                                        Function blocks       1344

Using the inputs "WebWidth" and "Density", the moment of inertia of the
winder is calculated internally in the diameter calculator and displayed at
the output "CurrentInertia". Using the moment of inertia that depends on the
diameter, an adaptation of the KP-gain of the speed loop can be implemented
in the PLC project in ctrlX PLC Engineering.
Preparation of a splice
Finally, the inputs "MinDiameter" and "MaxDiameter" can be set. The variables
specified affect the outputs "MinAvDiamAchieved" and "MaxAvDiamAchieved"
and display a message if the currently calculated winding diameter exceeds
the specified limits. The respective values should be within the admissible
diameter range defined by the inputs "HighLimitDiameter" and "LowLimitDia‐
meter". Thus, the time for specific process steps, for example, for a splice or
adjustment of the "DiamCalcRange" input, can be detected and displayed in

the PLC based on the specification of the minimum/maximum diameter.

### 37.3.5 MB_DancerControl

Brief description
The function block MB_DancerControl cyclically calculates a closed-loop
dancer position control for a draw roller with dancer or for a winding axis
with dancer. The cyclic output variable of the dancer position controller is
the speed offset of the respective drive of a draw roller or winding axis. The
current control deviation of the dancer position controller is output.
The control variable limitation is standardized or the P-gain is adapted via a
settable minimum reference diameter (e.g. minimum core diameter). It does
not depend on the format length set at the diameter calculator.
Diagnostic inputs for the control variable limitation are also available.
The control variable limitation of the dancer position controller is dynami‐
cally adjusted according to the reference axis velocity and the diameter ratio
("MinRefDiameter" / Pi * "ReferenceDiameter"). This means that, at a higher
velocity, the limitation of the additive velocity of the dancer position con‐
troller is automatically higher than at a lower velocity. Considering the diam‐
eter ratio results in the limitation for winding applications automatically being
adapted to a changing "ReferenceDiameter" (the limitation reduces automati‐
cally with an increasing diameter).
If the control variable of the dancer position controller is limited, this is dis‐
played via the binary outputs "HighlimitActive" or "LowLimitActive". The binary
outputs "ActHighlimitVal" and "ActLowLimitVal" show the current values for
the limitation.

1288 /    ctrlX PLC Engineering
1344      Function blocks

    Interface description

Table 1225: Interface variables of the MB_DancerControl function block
I/O type           Name              Type          Comment
VAR_INPUT          Enable            BOOL          Function block processing enabled (level-
                                                   controlled)
                   Pause             BOOL          Dancer controller paused, no velocity adap‐
                                                   tation (level-controlled)
                   ControlPolarity   BOOL          Polarity of the closed-loop dancer control
                                                   is inverted (applied at a positive at Enable)
                   SetpointDancer    LREAL         Command value (setpoint) for the closed-
                                                   loop dancer control
                   FeedbackDancer    LREAL         Actual value (feedback) of the dancer posi‐
                                                   tion
                   WindowDancer      LREAL         Windows to monitor the actual dancer posi‐
                                                   tion value [%] with regard to the command
                                                   dancer position value. If the dancer posi‐
                                                   tion deviates from the command value by
                                                   more than the given value, the function
                                                   block reports this deviation by resetting the
                                                   "InWindow" output
                   DancerLimits      MB_WIND_DANCE Structure for the automatic control variable
                                     R_LIMITS      limitation of the dancer
                   PIDControlData    MB_PIDCON‐    Structure for the PID parameters
                                     TROL_DATA
                   ReferenceDiameter LREAL         Reference diameter (value to standardize
                                                   PControl and the control variable limitation
                                                   "DancerLimits". That means that the values
                                                   are internally adapted)
                                                   For a pure dancer position controller:
                                                       ● Draw roller diameter [mm]
                                                       For winders with dancer:
                                                       ● Assigning current winding diameter
                                                         [mm] from the diameter calculator func‐
                                                         tion block

                                                                Function blocks        1344

I/O type       Name                Type                   Comment
MinRefDiameter      LREAL                  Minimum diameter [mm], (value to stand‐
                                           ardize PControl)
                                           For a pure dancer position controller:
                                           ● Identical to the ReferenceDiameter
                                           For winders with dancer:
                                           ● Smallest core diameter possible
MinDancerFeed‐      LREAL                  Lower threshold for the actual dancer value
back                                       (only for a display with binary output)
MaxDancerFeed‐      LREAL                  Upper threshold for the actual dancer value
back                                       (only for a display with binary output)

VAR_OUTPUT InOperation             BOOL                   Function block operating
Error                   BOOL                   Processing completed with error
ErrorID                 ⮫ ERROR_CODE           Diagnostic description in case of error
ErrorIdent        ⮫ ERROR_STRUCT Detailed diagnostics
InPause           BOOL           Dancer controller pausing
InWindow          BOOL           Actual dancer value within the Dancer
                                 window
MinFeedbackA‐     BOOL           Actual value of the dancer position is below
chieved                          the input "MinDancerFeedback"
MaxFeedbackA‐     BOOL           Actual value of the dancer position is above
chieved                          the input "MaxDancerFeedback"
HighLimitActive   BOOL           Limit of speed offset "HighLimit" is active
LowLimitActive    BOOL           Limit of speed offset "LowLimit" is active
ActHighLimitVal   LREAL          Current value for the upper limit of the
                                 speed offset
ActLowLimitVal    LREAL          Current value for the lower limit of the
                                 speed offset
AddVelocityDancer LREAL          Speed offset for the winding drive or draw
                                 roller drive [rpm]
CurrentDancerDe‐ LREAL           Current control deviation of the dancer
viation                          controller
VAR_IN_OUT     Master            ⮫ AXIS_REF     Reference to the master axis
CONSTANT
Slave               ⮫ AXIS_REF             Reference to slave axis

Table 1226: Min./max. and default values of the inputs of the MB_DancerControl function block
Name            Type            Min. value      Max. value         Default value    Effective
Enable          BOOL                                               FALSE            Continuous
Pause           BOOL                                               FALSE            Continuous
DisableCyclic‐ BOOL                                                FALSE            Rising edge at
Writes                                                                              "Enable"
ControlPolarity BOOL                                               FALSE            Rising edge at
                                                                                    "Enable"
Setpoint‐    LREAL              0.0             N. def.            0.0              Continuous
Dancer
Feedback‐    LREAL              N. def.         N. def.            0.0              Continuous
Dancer
WindowDancer LREAL              0.0             N. def.            0.0              Continuous

1290 /    ctrlX PLC Engineering
1344      Function blocks

Name               Type           Min. value      Max. value      Default value   Effective
DancerLimits       STRUCT
PIDControl         STRUCT                                                         Continuous
ReferenceDia‐      LREAL          0.0             N. def.         100             Continuous
meter
MinRefDia‐         LREAL          0.0             N. def.         0.0             Rising edge at
meter                                                                             "Enable"
MinDancer‐         LREAL          0.0             MaxDancer‐      0.0             Continuous
Feedback                                          Feedback
MaxDancer‐         LREAL          MinDancer‐      N. def.         0.0             Continuous
Feedback                          Feedback

Functional description
The function block cyclically calculates a closed-loop dancer position control
for a draw roller with dancer or for a winding axis with dancer.
The ⮫ IL_PIDType01 (CXA_LoopControl library) function block is used as con‐
troller. The controller is a PID-controller. The cyclic output variables of the
dancer position controller are the speed offset of the respective drive for
the draw roller or the winding axis, as well as the current control deviation
of the dancer position controller. The "AddVelocityDancer" output of the func‐
tion block is only a calculated velocity offset value and does not affect the
drive parameters. If required, "AddVelocityDancer" can be set to the input
"MB_GearInVel". The current control deviation "CurrentDancerDeviation" is
available for analysis. The proportional gain (factor KP) and the low and high
values for control variable limitation "DancerLimits" are automatically adjusted
with the "ReferenceDiameter" input based on the "MinRefDiameter" input. The
diameter of the draw roller "ReferenceDiameter" and "MinRefDiameter" has
to be specified for a closed-loop dancer position control for a draw roller.
For a winder with dancer position control, "ReferenceDiameter" is the current
winding diameter (the proportional gain of the dancer position control auto‐
matically reduces with an increasing diameter) and "MinRefDiameter" is the
smallest core diameter possible. If the values for the integral part (integral
action time Tn, "IControl") and the lead element (lead time TD, "DControl") are
zero, the internal memory parameters of the PID controller are deleted. There
has to be a value proportional to the dancer roll adjustment (e.g. an analog
tension value) at the "FeedBackDancer" input. The command value and the
actual value have to have the same unit.
The function block only processes positive command values and actual values.
Negative command values result in an error.
Negative actual values are limited to zero.
Closed-loop dancer position control
To determine the dancer position, a measuring device is required that converts
the dancer position into a proportional signal. The actual position of the
dancer is subtracted from a given command value and specified as a control
deviation on an internally integrated PID-controller. The control variable of the
controller has an effect on the speed command value by addition. Thus, the
winding axis rotates faster or slower than the master axis. The position of the
dancer is thereby controlled.
Under normal conditions (e. g. no high variations of the speed command
values), the approximate adjustment of the circumferential velocity of a
winding axis is performed via the fine adjustment of the gear. The electronic
gear is used for the approximate adjustment of a tension-controlled axis.
Thus, the dancer position controller should thus control only small deviations.

                                                             Function blocks       1344

      Direction of rotation of the tension or winding axis, control direction of the
      closed-loop dancer control
      The direction of rotation of the tension or winding axis can be set by man‐
      ually changing the sign of the transmission ratio to the opposite sign. When
      inverting the direction of rotation of the axis, the control polarity (ControlPo‐
      larity) has to be inverted as well.

### 37.3.6 MB_WinderDancerCtrlType01

      Brief description
      The function block MB_WinderDancerCtrlType01 provides functionalities for a
      winder with dancer and a sensorless winder.

      Interface description

Table 1227: Interface variables of the MB_WinderDancerCtrlType01 function block
I/O type       Name                 Type                Comment
VAR_INPUT      Enable               BOOL                Function block processing enabled (level-
                                                        controlled)
               PauseDiameter        BOOL                Diameter calculator paused; no further
                                                        diameter calculation and velocity adjust‐
                                                        ment (level-controlled)
               PauseDancer          BOOL                Dancer controller paused (level-controlled)
               PresetDiameter       BOOL                CurrentDiameter is set to PresetVal. Gear‐
                                                        RatioFineAdj is adjusted accordingly (edge-
                                                        controlled)
               ControlPolarity      BOOL                Polarity of the closed-loop dancer control
                                                        is inverted (applied at a positive edge at
                                                        "Enable")

1292 /     ctrlX PLC Engineering
1344       Function blocks

I/O type           Name               Type           Comment
SetpointDancer     LREAL          Command value (setpoint) for the closed-
                                  loop dancer control
FeedbackDancer     LREAL          Actual value (feedback) of the dancer posi‐
                                  tion
WindowDancer       LREAL          Window to monitor the actual dancer posi‐
                                  tion value [%] with regard to the command
                                  dancer position value. If the dancer posi‐
                                  tion deviates from the command value by
                                  more than the given value, the function
                                  block reports this deviation by resetting the
                                  "InWindow" output
DancerLimits       ⮫ MB_WIND_DANC Structure for the automatic control variable
                   ER_LIMITS      limitation of the dancer
PIDControlData     ⮫ MB_PIDCON‐      Value for the PID of the dancer control
                   TROL_DATA
MinDancerFeed‐     LREAL           Lower threshold for the actual dancer value
back                               (only for a display with binary output)
MaxDancerFeed‐     LREAL           Upper threshold for the actual dancer value
back                               (only for a display with binary output)
Diameter           ⮫ MB_WIND_DIAM‐ Structure for diameter calculator
                   ETER
VAR_OUTPUT InOperation                BOOL            Function block operating
Error                      BOOL            Processing completed with error
ErrorID                    ⮫ ERROR_CODE    Diagnostic  description in case of error
ErrorIdent         ⮫ ERROR_STRUCT    Detailed diagnostics
InPauseDancer      BOOL              Dancer controller pausing
InPauseDiam        BOOL              Diameter calculator paused
PresetDiamAck      BOOL              Preset diameter was applied
                                     (Set if "Preset" is present)
MinAvDiamA‐        BOOL              Minimum diameter reached
chieved                              (Refers to the averaged diameter)
MaxAvDiamA‐        BOOL              Maximum diameter reached
chieved                              (Refers to the averaged diameter)
HighLimitDiamAc‐   BOOL              Currently calculated diameter reached
tive                                 upper limit
                                     (Diameter value is discarded)
LowLimitDiamAc‐    BOOL              Currently calculated diameter has reached
tive                                 the lower limit (diameter value is dis‐
                                     carded)
InWindowDancer     BOOL              Actual dancer value within the Dancer
                                     window
MinFeedbackA‐      BOOL              Actual value of the dancer position is below
chieved                              the input "MinDancerFeedback"
MaxFeedbackA‐      BOOL              Actual value of the dancer position is above
chieved                              the input "MaxDancerFeedback"
HighLimitDancer‐   BOOL              Limit of the velocity offset "HighLimit" is
Active                               active
LowLimitDancer‐    BOOL              Limit of the velocity offset "LowLimit" is
Active                               active

                                                                Function blocks       1344

I/O type       Name                Type                   Comment
ActHighLimit‐       LREAL                  Current value for the upper limit of the
Dancer                                     velocity offset
ActLowLimit‐        LREAL                  Current value for the lower limit of the
Dancer                                     velocity offset
CurrentDiameter     LREAL                  Current winding diameter
GearRatioFineAd‐    LREAL                  Gear fine adjustment for speed lagging of
just                                       the drive [%]
CurrentInertia      LREAL                  Current moment of inertia of the winding
                                           material + mechanics
                                           (related to the motor side) [kg*m2]

AddVelocityDancer LREAL                    Speed offset for the winding drive [rpm]
CurrentDancerDe‐ LREAL                     Current control deviation of the dancer
viation                                    controller
VAR_IN_OUT     Master            ⮫ AXIS_REF               Reference to the master axis
CONSTANT       Slave               ⮫ AXIS_REF             Reference to the slave axis (winding axis)

Table 1228: Min./max. and default values of the inputs of the MB_WinderDancerCtrlType01
function block
Name            Type            Min. value      Max. value         Default value   Effective
Enable          BOOL                                               FALSE           Continuous
PauseDiameter BOOL                                                 FALSE           Continuous
PauseDancer BOOL                                                   FALSE           Continuous
PresetDia‐      BOOL                                               FALSE           Continuous
meter
ControlPolarity BOOL                                               FALSE           Rising edge at
                                                                                   "Enable"
Setpoint‐    LREAL              0.0             N. def.            0.0             Continuous
Dancer
Feedback‐    LREAL              N. def.         N. def.            0.0             Continuous
Dancer
WindowDancer LREAL              0.0             N. def.            0.0             Continuous
DancerLimits STRUCT
PIDControl‐  STRUCT                                                                Continuous
Data
MinDancer‐   LREAL              0.0             MaxDancer‐         0.0             Continuous
Feedback                                        Feedback
MaxDancer‐   LREAL              MinDancer‐      N. def.            0.0             Continuous
Feedback                        Feedback
Diameter     STRUCT                                                                Depending on the
                                                                                   structure element

      Functional description
      Diameter calculation
      The diameter calculation provides the currently calculated diameter via the
      cyclically called function block ⮫ AXIS_REF. The additive fine adjustment of
      the winding axis is set with regard to the diameter. The axis is moved faster
      or slower in relation to the reference axis to achieve a constant tension of the
      fabric web.
      A relative motion of the dancer roll is taken into account in the diameter
      calculation using the "DancerConstant" input.

1294 /    ctrlX PLC Engineering
1344      Function blocks

For this purpose, determine this dancer constant once.
The following procedure is recommended:
1.    In case of a deflection of the dancer from one end position to the other
      end position, determine the web distance (unit in mm).
2.    Determine the difference between the two actual dancer values of the
      respective end position.
3.    Calculate the quotient of both values.
4.    Determine the sign of the dancer constant by conducting a practical
      test. For this purpose, the diameter calculation is observed at a slowly
      rotating winding axis and reference axis. Command value jumps to the
      dancer command value should not significantly affect the calculation of
      the diameter if the sign is correct.
5.    Subsequently optimize the calculated value for the dancer constant as
      described in step 4.
If the current diameter is to be kept after the control has been switched off,
the "CurrentDiameter" output has to be copied to a remanent variable. After
switching on, use this value for a preset.

Splice
After a splice, the winding diameter generally changes abruptly. The last cal‐
culated internal value for the winding diameter does no longer correspond
to the current diameter. For a correct diameter calculation, a winding diam‐
eter preset is reasonable. The input value for the Preset should correspond
approximately to the actual value of the winding diameter to achieve the most
accurate resulting fine adjustment possible.
If the preset is not performed, malfunctions can occur. Thus, perform the
preset before activating the diameter calculator.
With a flying splice, it has to be ensured that the circumferential velocity of
the new roll corresponds to the current one. This has to be ensured with an
appropriate PLC project in the ctrlX PLC Engineering. The "Pause" input can
be used when activating the diameter calculator for the new roll, for example
"Pause" can be disabled after removing the old roll.

Closed-loop dancer position control
To determine the dancer position, a measuring device is required that converts
the dancer position into a proportional signal. The actual position of the
dancer is subtracted from a given command value and added as a control
deviation to an internal PID controller. The control variable of the controller
has an effect on the speed command value by addition. Thus, the winding axis
rotates faster or slower than the master axis.
Under normal conditions (e. g. no high variations of the speed command value
or abrupt changes in the diameter of the winder), the approximate adjustment
of the circumferential velocity of the winding axis is performed by the fine
adjustment of the gear. Therefore, the diameter calculator described before
is used. Thus, the dancer position controller has to control only small devia‐
tions.

Direction of rotation of the winding axis, control direction of the closed-loop
dancer control
Set the direction of rotation of the tension or winding axis by manually change
the sign of the transmission ratio to the opposite sign. When inverting the
drive direction of rotation, the control direction (ControlPolarity) is also to be
inverted.

                                                       Function blocks      1344

Functional diagram of the dancer position controller
The following functional diagram schematically explains the functions of the
diameter calculator with dancer.

### 37.3.7 MB_WinderTensionCtrlType01

Brief description
The function block MB_WinderTensionCtrlType01 cyclically calculates the
current winding diameter, the current winder moment of inertia, the corre‐
sponding velocity adaptation via fine adjustment of the gear, an additive
speed offset for tensioning the web and a parameterizable torque limit.

1296 /    ctrlX PLC Engineering
1344      Function blocks

Interface description

Table 1229: Interface variables of the MB_WinderTensionCtrlType01 function block
I/O type           Name              Type           Comment
VAR_INPUT          Enable            BOOL           Function block processing enabled (level-
                                                    controlled)
                   Pause             BOOL           Pausing the tension controller and the
                                                    diameter calculator (values are frozen)
                   WindDirection     ⮫ MB_WIND_DIRE Winding direction
                                     CTION          ● Rewinder REWIND (16#0000)
                                                       ● Unwinder UNWIND (16#0001)
                   PauseDiameter     BOOL              Pausing the diameter calculation.
                   PresetDiameter    BOOL              CurrentDiameter is set to PresetVal, Gear‐
                                                       RatioFineAdjust is adjusted accordingly
                                                       (edge-controlled)
                   SetpointStandstill LREAL            Specification of the standstill tension [N]
                                                       (switching between standstill tension and
                                                       operating tension using the standstill mes‐
                                                       sage of the drive)
                   SetpointOpMode    LREAL             Specification of the operating tension [N]
                                                       (Switching between standstill tension and
                                                       operating tension using the standstill mes‐
                                                       sage of the drive)

                                                         Function blocks      1344

I/O type       Name                Type            Comment
ActTensionFilter    LTIME           Filter time constant for actual tension con‐
                                    trol
AccelTorqueFilter   LTIME           Filter time constant for acceleration torque
TorqueLimits        MB_WIND_TORQU Value for the bipolar torque limit after disa‐
                    E_LIMITS        bling "Enable" [%]
WindowTension       LREAL           Window for the actual tension control value
                                    [%] in relation to the tension command
                                    value ("TensionInWindow")
MinTension          LREAL           Lower threshold for the actual tension
                                    value (only for a display with the binary
                                    output "MinTensionAck")

MaxTension          LREAL           Upper threshold for the actual tension con‐
                                    trol value (only for a display with binary
                                    output "MaxTensionAck")
Diameter            ⮫ MB_WIND_DIAM‐ Structure for diameter calculator
                    ETER
TensionCtrl         ⮫ MB_WIND_TEN‐ Structure for tension controller
                    SION
Friction            ⮫ MB_WIND_FRIC‐ Structure for friction torque
                    TION
VAR_OUTPUT InOperation             BOOL            Function block operating
Error                   BOOL            Processing completed with error
ErrorID                 ⮫ ERROR_CODE    Diagnostic description in case of error
ErrorIdent       ⮫ ERROR_STRUCT Detailed diagnostics
InPause          BOOL           Tension controller and diameter calculator
                                pause
PresetDiamAck    BOOL           Preset diameter was applied (set as long as
                                "Preset" is pending)
InPauseDiam      BOOL           Diameter calculator pauses
MinAvDiamAck     BOOL           Minimum diameter reached (refers to the
                                averaged diameter)
MaxAvDiamAck     BOOL           Maximum diameter reached (refers to the
                                averaged diameter)
HighLimitDiamAck BOOL           Currently calculated diameter reached the
                                upper limit (diameter value is discarded)
LowLimitDiamAck BOOL            Currently calculated diameter has reached
                                the lower limit (diameter value is dis‐
                                carded)
DiameterEngaged BOOL            Diameter "engaged"
                                TRUE: engaged
                                FALSE: Disengaged
HighLimitTensAc‐ BOOL           Output of the tension controller reached
tive                            upper limit
LowLimitTensAc‐  BOOL           Output of the tension controller reached
tive                            lower limit
TensionInWindow BOOL            Actual tension value is within the tension
                                window
MinTensionA‐     BOOL           Tension below the "MinTension" input
chieved

1298 /     ctrlX PLC Engineering
1344       Function blocks

I/O type           Name               Type                   Comment
    MaxTensionA‐       BOOL                   Tension above the "MaxTension" input
    chieved
    CurrentDiameter    LREAL           Currently calculated diameter [mm]
    GearRatioFineAd‐   LREAL           Resulting gear fine adjustment for speed
    just                               lagging of the drive [%]
    CurrentInertia     LREAL           Current total moment of inertia (related to
                                       the motor side) [kg*m2]
    SpeedOffset        LREAL           Tensioning speed [rpm]
    TorqueLimitBipolar LREAL           Bipolar torque limit [%]
    AdditionalTorque LREAL             Additive torque [%]
    WindTensDiag       ⮫ MB_WIND_TENS_ Current control deviation of the dancer
                       DIAG            controller
VAR_IN_OUT         Master             ⮫ AXIS_REF             Reference to the master axis
    Slave              ⮫ AXIS_REF             Reference to the slave axis (winding axis)

Table 1230: Min./max. and default values of the inputs of the MB_WinderTensionCtrlType01
function block
Name           Type        Min. value              Max. value         Default value   Effective
Enable         BOOL                                                   FALSE           Continuous
Pause          BOOL                                                   FALSE           Continuous
WindDirection  MB_WIND_DIR                                            FALSE           Rising edge at
               ECTION                                                                 "Enable"
PauseDiameter BOOL                                                    FALSE           Continuous
PresetDia‐     BOOL                                                   FALSE           Continuous
meter
SetpointStand‐ LREAL       0.0                     n. def.            0.0             Continuous
still
SetpointOp‐    LREAL       0.0                     n. def.            0.0             Continuous
Mode
ActTension‐    LTIME       0s                      n. def.            0s              Continuous
Filter
AccelTorque‐   LTIME       0s                      n. def.            0s              Continuous
Filter
TorqueLimits MB_WIND_TOR                                                              Continuous
               QUE_LIMITS
WindowTen‐     LREAL       0.0                     n. def.            0.0             Continuous
sion
MinTension     LREAL       0.0                     n. def.            0.0             Continuous
MaxTension     LREAL       0.0                     n. def.            0.0             Continuous
Diameter       MB_WIND_DIA                                                            Depending on the
               METER                                                                  structure element
TensionCtrl    MB_WIND_TEN                                                            Continuous
               SION
Friction       MB_WIND_FRI                                                            Continuous
               CTION

        Functional description
        The function block is a diameter calculator with open-loop tension control
        that usually does not operate at the torque limit.

                                                       Function blocks      1344

The function block cyclically calculates the current winding diameter, the cur‐
rent moment of inertia of the winder, the corresponding velocity adaptation
via the fine adjustment of the gear, an additive speed offset for tensioning the
web of fabric and the torque command value for feedforward
The function blocks ⮫ MB_DiameterCalculator and ⮫ MB_DiameterMeasure‐
ment are used internally.
The velocity is adapted via the gear fine adjustment due to the changing
winding diameter. The tension controller additively affects the velocity com‐
mand value. The calculated torque (tension torque, friction torque, accelera‐
tion torque) is precontrolled via the additive torque command value.
Due to safety reasons, the torque limit value on the currently calculated
torque command value is multiplied with a scaling factor and is set with an

additional additive value. In the normal winder mode, the torque limitation
should not be effective and the winding drive should be operated in a speed-
controlled way.

Direction of rotation of the winding drive, rewinder/unwinder
With the input of the function block, the winder type is set to a rewinder or
unwinder type. The direction of rotation of the drive has to be set either by
the scaling parameters or by the polarity of the master drive.

1300 /    ctrlX PLC Engineering
1344      Function blocks

The direction of rotation of the master axis of the winding drive (that is the
master axis of the function block MB_GearInVel or the master axis of the Axi‐
sInterface) has to be positive which means a positive speed command value.
The winding drive has to be inverted using the polarity parameters.
Diameter calculation
The torque for the winding drive results from the product of the tension and
the winding radius. Thus, the radius or the diameter of the winder has to be
continuously determined. Thus, an internal diameter calculator is integrated
into the function block (function block ⮫ MB_DiameterCalculator ).
The diameter calculation become active when the winding material is ten‐
sioned and no standstill message of the reference axis is active. It is calcu‐
lated cyclically depending on the speed or the position of the winding axis.
For diagnostic purposes, the current diameter can be retrieved at the function
block.
The calculated winding diameter directly affects the resulting fine adjustment
of the gearbox. If the web tension is too low or negative (formation of loops),
the diameter calculator is interrupted since no useful diameter calculation can
be performed any longer under these circumstances.
If the actual tension control of the drive is more than 25 % below the com‐
mand value, the diameter calculator stops calculating (engaging condition).
If the current diameter is to be kept after the control has been switched off,
the "CurrentDiameter" output has to be copied to a remanent variable. After
switching on, use this value for a preset.
The ratio "FormatLength"/"CoreDiameter" may not be greater than 25.
Otherwise, the gear adjustment via the gear fine adjustment is insufficient.
Tensioning the winding material
When enabling the winding calculator (Enable = TRUE), the winding material
is initially tensioned with the additive speed offset. To avoid the formation of
loops in the winding material, the master axis should not rotate. The winding
material is tensioned if the tension command value of the tension controller
exceeds a defined minimum value and if the relative deviation between the
tension command value and the actual torque value is lower than a defined
limit.
Friction compensation
Different inputs are used for a friction torque compensation.
Approaching the friction behavior is defined as follows.
The friction is initially reduced from the standstill friction torque up to a spe‐
cific speed. The friction torque increases linearly with the winding axis speed
up to the maximum speed.
This behavior also applies to negative speeds. The curve is mirrored at the
y-axis (friction torque). With this friction torque behavior, the effect of the
friction can be counteracted by a compensation.

                                                      Function blocks       1344

Compensation of acceleration torque
An additional acceleration torque is required for the acceleration of the
winding axis. This torque depends on the winding diameter. By specifying
certain material and fabric web data, the inertia of the winder is calculated
according to the diameter. The calculated acceleration torque can also be
filtered.
Torque limit and feedforward
The drive of the winding axis generally DOES NOT operate at its torque limit.
Due to safety reasons, the calculated torque is set as value for the torque
limit in addition to a variable additive value (this value should be above the
required motor torque and should not limit the drive in normal operation).
A torque limit proportional to the tension and the respective diameter of the
winder is calculated cyclically.

This cyclic value for the torque limit is precontrolled as additive torque com‐
mand value.
Furthermore, this value can be increased by a proportional ratio (TorqueLimit‐
Factor) and an additive ratio (MinTorqueLimit) so that the torque limit does
not become active during normal winder operation.

The resulting torque limit corresponds to the TorqueLimitbipolar output. By
default, the calculated torque limit is increased by a TorqueLimitFactor of 50%
and a minimum TorqueLimit of 10%.
During tensioning, it can be practical to set the torque limit lower (e.g. Tor‐
queLimitFactor 10%) if tensioning takes place with too much torque. The Tor‐
queLimitFactor should be increased again after tensioning is completed.
Splice

1302 /    ctrlX PLC Engineering
1344      Function blocks

After a splice, the winding diameter generally changes abruptly. The last calcu‐
lated internal value for the winding diameter does no longer correspond to the
current diameter. A preset of the winding diameter is required to calculate the
diameter correctly. The input value for the preset should correspond approxi‐
mately to the actual value of the winding diameter.
If the preset is not performed, malfunctions can occur. The preset should
therefore be completed before the diameter calculator becomes active again.
The value for the preset should be selected as follows:
● In case of a rewinder, it has to be slightly smaller or equal to the actual
    winding diameter
● In case of an unwinder, it has to be slightly higher or equal to the actual
    winding diameter
With a flying splice, it has to be ensured that the circumferential velocity of
the new roll corresponds to the current one. This should be implemented in
the PLC project of the ctrlX PLC Engineering.
Filtering the actual tension control value
At low tensions, an unfiltered actual tension value can result in a disengaging
diameter calculator. A filtering process should therefore be performed and the
corresponding input should be activated (e.g. 20 ms).

Enabling the torque constant correction for synchronous motors
The torque resulting from a motor is determined at the drive using the motor
current and a so-called torque constant P-0051 "Torque/force constant". How‐
ever, this so-called "Torque or force constant" is not a static value seen from
the physical point of view.
Dependencies
1.   Level of the actual motor current flow
     (the constant reduces at currents higher than INom)
2.   Temperature of motor winding and rotor
     (the constant reduces when the temperature increases)
A corrected torque constant can be used for the synchronous motor.
Thus, the following effects on the torque/force constant are considered:
1.   Magnetic field weakening due to magnetic saturation caused by
     increased motor current compared to nominal current.
2.   Magnetic field weakening due to increased motor winding temperature.
3.   Magnetic field weakening due to increased rotor temperature depending
     on the average speed.
A significant deviation from the torque constant P-0051 is only caused if the
current load increases to 100% (or higher) of the nominal current S-0-0111
"Standstill current motor". That means the higher the motor load, the better
the impact of correction. For a motor loaded at low level, only a minimum or
no correction results.

### 37.3.8 MB_WinderTensionCtrlType02

Brief description
The function block MB_WinderTensionCtrlType02 cyclically calculates the
current winding diameter, the current winder moment of inertia, the corre‐
sponding velocity adaptation via the fine adjustment of the gear, an additive
speed offset for tensioning the web of fabric and the required torque limit.

                                                         Function blocks       1344

Interface description

Table 1231: Interface variables of the MB_WinderTensionCtrlType02 function block
I/O type       Name              Type            Comment
VAR_INPUT      Enable            BOOL            Function block processing enabled (level-
                                                 controlled)
               Pause             BOOL            Pausing the tension controller and the
                                                 diameter calculator (values are frozen)
               WindCtrlType      ⮫ MB_WIND_CTRL_ Winding structure
                                 TYPE            ● Open-loop tension control (without
                                                  sensor): OPEN_LOOP (16#0000)
                                                ● Open-loop tension control (load cell):
                                                  CLOSED_LOOP (16#0001)
               WindDirection     ⮫ MB_WIND_DIRE Winding direction
                                 CTION          ● Rewinder REWIND (16#0000)
                                                    ● Unwinder UNWIND (16#0001)
               PauseDiameter     BOOL               Pausing the diameter calculation
                                                    Closed-loop/open-loop control of the
                                                    torque limit remains active
               PresetDiameter    BOOL               CurrentDiameter is set to PresetVal. Gear‐
                                                    RatioFineAdj is adjusted accordingly (edge-
                                                    controlled)

1304 /     ctrlX PLC Engineering
1344       Function blocks

I/O type           Name               Type              Comment
TensionMode        ⮫ MB_WIND_TEN‐    Mode to tension the material web
                   SION_MODE
                           ● Tensioning at constant speed
                               CONST_SPEED
                           ● Tensioning at constant web velocity
                               CONST_WEB_VEL
SetpointStandstill LREAL           Specification of the standstill tension [N]
                           (Switching between standstill tension and
                           operating tension using the standstill mes‐
                           sage of the drive)
SetpointOpMode LREAL               Specification of the operating tension [N]
                           (Switching between standstill tension and
                           operating tension using the standstill mes‐
                           sage of the drive)
TensionSpeed       LREAL           Tensioning speed at an empty winder
                           [min-1]
ActTorqueFilter    LTIME           Filter time constant for the actual torque
AccelTorqueFilter LTIME            Filter time constant for acceleration torque
DefaultTorqueLimit LREAL           Value for the bipolar torque limit after
                           removing "Enable" [%]
WindowTension      LREAL           Window for the actual tension value [%]
                           related to the tension command value
                           (output "TensionInWindow")
MinTension         LREAL           Lower threshold for the actual tension
                           value (only for a display with the binary
                           output "MinTensionAck")
MaxTension         LREAL           Upper threshold for the actual tension con‐
                           trol value (only for a display with binary
                           output "MaxTensionAck")
Diameter           ⮫ MB_WIND_DIAM‐ Structure for diameter calculator
           ETER
TensionCtrl        ⮫ MB_WIND_TEN‐ Structure for tension controller
           SION
Friction           ⮫ MB_WIND_FRIC‐ Structure for friction torque
           TION
VAR_OUTPUT InOperation        BOOL            Function block operating
Error              BOOL            Processing completed with error
ErrorID            ⮫ ERROR_CODE    Diagnostic description in case of error
ErrorIdent         ⮫ ERROR_STRUCT Detailed diagnostics
InPause            BOOL           Tension controller and diameter calculator
                                  pause
PresetDiamAck      BOOL           Preset diameter was applied (set as long as
                                  "Preset" is pending)
InPauseDiam        BOOL           Diameter calculator pauses
MinAvDiamA‐        BOOL           Minimum diameter reached (refers to the
chieved                           averaged diameter)
MaxAvDiamA‐        BOOL           Maximum diameter reached (refers to the
chieved                           averaged diameter)
HighLimitDiamAc‐   BOOL           Currently calculated diameter reached the
tive                              upper limit (diameter value is discarded)

                                                               Function blocks       1344

I/O type       Name               Type                   Comment
LowLimitDiamAc‐    BOOL                   Currently calculated diameter has reached
tive                                      the lower limit (diameter value is dis‐
                                          carded)
DiameterEngaged    BOOL                   Diameter "engaged"
                                          TRUE: engaged
                                          FALSE: Disengaged
HighLimitTensAc‐   BOOL                   Output of the tension controller reached
tive                                      upper limit
LowLimitTensAc‐    BOOL                   Output of the tension controller reached
tive                                      lower limit

TensionInWindow    BOOL                   Actual tension value is within the tension
                                          window
MinTensionA‐       BOOL                   Tension below the "MinTension" input
chieved
MaxTensionA‐       BOOL                   Tension above the "MaxTension" input
chieved
CurrentDiameter    LREAL           Currently calculated diameter [mm]
GearRatioFineAd‐   LREAL           Resulting gear fine adjustment for speed
just                               lagging of the drive [%]
CurrentInertia     LREAL           Current moment of inertia of the winding
                                   material + mechanics (related to the motor
                                   side) [kg*m2]
SpeedOffset        LREAL           Tensioning speed [rpm]
TorqueLimitBiploar LREAL           Bipolar torque limit [%]
WindTensDiag       ⮫ MB_WIND_TENS_ Current control deviation of the dancer
                   DIAG            controller
VAR_IN_OUT     Master             ⮫ AXIS_REF             Reference to the master axis
Slave              ⮫ AXIS_REF             Reference to the slave axis (winding axis)

Table 1232: Min./max. and default values of the inputs of the MB_WinderTensionCtrlType02
function block
Name            Type        Min. value         Max. value         Default value   Effective
Enable          BOOL                                              FALSE           Continuous
Pause           BOOL                                              FALSE           Continuous
WindCtrlType    MB_WIND_CTR                                                       Rising edge at
                L_TYPE                                                            "Enable"
WindDirection MB_WIND_DIR                                                         Rising edge at
                ECTION                                                            "Enable"
PauseDiameter BOOL                                                FALSE           Continuous
PresetDia‐      REAL                                              FALSE           Rising edge at
meter                                                                             "Preset"
TensionMode MB_WIND_TEN                                                           Rising edge at
                SION_MODE                                                         "Enable"
SetpointStand‐ LREAL        0.0                N. def.            0.0             Continuous
still
SetpointOp‐     LREAL       N. def.            N. def.            0.0             Continuous
Mode
TensionSpeed LREAL          0.0                N. def.            0.0             Continuous
ActTorqueFilter LTIME       0s                 N. def.            0s              Continuous

1306 /    ctrlX PLC Engineering
1344      Function blocks

Name           Type        Min. value          Max. value      Default value   Effective
AccelTorque‐   LTIME       0s                  N. def.         0s              Continuous
Filter
DefaultTorque‐ LREAL       0.0                 N. def.         100.0           Continuous
Limit
WindowTen‐     LREAL       0.0                 N. def.         0.0             Continuous
sion
MinTension     LREAL       0.0                 N. def.         0.0             Continuous
MaxTension     LREAL       0.0                 N. def.         0.0             Continuous
Diameter       MB_WIND_DIA                                                     Depending on the
METER                                                           structure element
TensionCtrl    MB_WIND_TEN                                                     Continuous
SION
Friction       MB_WIND_FRI                                                     Continuous
CTION

Functional description
Diameter calculator with open-loop tension control
The functional scope of the diameter calculator with open-loop tension con‐
trol includes:
●  Tensioning of the untensioned winding material
●  Speed-dependent friction compensation
●  Compensation of acceleration torque
●  Separate parameterization of the operating tension and the standstill ten‐
   sion
● Calculation of diameter-dependent variables (with the function block
   ⮫ MB_DiameterCalculator)
Functional diagram of the winder calculator with open-loop tension control
The following functional diagram schematically explains the functions of the
diameter calculator with open-loop tension control.

                                                     Function blocks      1344

Diameter calculator with closed-loop tension control
The functional scope of the diameter calculator with closed-loop tension con‐
trol includes:
●  Tensioning of the untensioned winding material
●  Speed-dependent friction compensation
●  Compensation of the acceleration torque
●  Separate parameterization of the operating tension and the standstill ten‐
   sion
● PI controller for tension (via IL_PIDType01)
● Calculation of diameter-dependent variables (with the function block
   ⮫ MB_DiameterCalculator)
Functional diagram of the winder calculator with closed-loop tension control
The following functional diagram schematically explains the functions of the
diameter calculator with closed-loop tension control.

1308 /    ctrlX PLC Engineering
1344      Function blocks

Direction of rotation of the winding drive, rewinder/unwinder
With the input of the function block, the winder type is set to a rewinder or
unwinder type. The direction of rotation of the drive has to be set either by
the scaling parameters or by the polarity of the master drive.
The direction of rotation of the master axis of the winding drive (that is the
master axis of the function block MC_GearIn or the master axis of the AxisIn‐
terface) has to be positive, i.e. a positive speed command value. The winding
drive has to be inverted using the polarity parameters.
Diameter calculation
The torque for the winding drive results from the product of the tension and
the winding radius. Thus, the radius or the diameter of the winder has to be
continuously determined. Thus, an internal diameter calculator is integrated
into the function block (function block ⮫ MB_DiameterCalculator ).
The diameter calculation become active when the winding material is ten‐
sioned and no standstill message of the reference axis is active. It is calcu‐
lated cyclically depending on the speed or the position of the winding axis.
For diagnostic purposes, the current diameter can be retrieved at the function
block.
The calculated winding diameter directly affects the resulting fine adjustment
of the gearbox. If the web tension is too low or negative (formation of loops),
the diameter calculator is interrupted since no useful diameter calculation can

                                                     Function blocks       1344

be performed any longer under these circumstances. If the actual torque of
the drive is more than 25% below the command value, the diameter calculator
stops calculating (engaging condition).
If the current diameter is to be kept after the control has been switched off,
the "CurrentDiameter" output has to be copied to a remanent variable. After
switching on, use this value for a preset.
The ratio "FormatLength"/"CoreDiameter" may not be greater than 25.
Otherwise, the gear adjustment via the gear fine adjustment is insufficient.
Tensioning the winding material
When enabling the winding calculator ("Enable" = TRUE), the winding material
is initially tensioned with the tensioning speed. To avoid the formation of
loops in the winding material, the master axis should not rotate. The winding

material is tensioned if the torque command value of the drive exceeds a
predefined limit and if the relative deviation between the torque command
value and the actual torque value is lower than a defined limit.
Two different procedures can be used for tensioning the winding material:
● Tensioning at constant speed
● Tensioning with constant web velocity
When tensioning the winding material with constant speed, the tensioning
speed is maintained on a constant level. Thus, the web velocity increases with
an increasing winding diameter.

When tensioning the winding material at a constant web velocity, the ten‐
sioning speed is reduced reciprocally to the winding diameter. The calculation
of the winding axis speed is based on the tensioning speed of an empty
winder. This calculation has to be transferred to the function block.

1310 /    ctrlX PLC Engineering
1344      Function blocks

Friction compensation
Different inputs are used for a friction torque compensation.
Approaching the friction behavior is defined as follows:
The friction is initially reduced from the standstill friction torque up to a spe‐
cific speed. The friction torque increases linearly with the winding axis speed
up to the maximum speed.
This behavior also applies to negative speeds. The curve is mirrored at the
y-axis (friction torque). With this friction torque behavior, the effect of the
friction can be counteracted by a compensation.

Compensation of acceleration torque
An additional acceleration torque is required for the acceleration of the
winding axis. This torque depends on the winding diameter. By specifying
certain material and fabric web data, the inertia of the winder is calculated
according to the diameter. The calculated acceleration torque can also be
filtered.
Splice

                                                       Function blocks       1344

After a splice, the winding diameter generally changes abruptly. The last calcu‐
lated internal value for the winding diameter does no longer correspond to the
current diameter. A preset of the winding diameter is required to calculate the
diameter correctly. The input value for the preset should correspond approxi‐
mately to the actual value of the winding diameter.
The value for the preset should be selected as follows:
● In case of a rewinder, it has to be slightly smaller or equal to the actual
  winding diameter
● In case of an unwinder, it has to be slightly higher or equal to the actual
  winding diameter
With a flying splice, it has to be ensured that the circumferential velocity of
the new roll corresponds to the current one.

Filtering the actual torque value
At low tensions, an unfiltered actual torque value can result in a disengaging
diameter calculator. A filtering should therefore be performed and the cor‐
responding input should be activated. Therefore, the actual torque and the
target torque of the drive are compared (e.g. 20 ms).
Additional leading and lagging of the winding axis
Set an additional leading or lagging via the gear fine adjustment (presetting
gear fine adjustment "FineAdjust") using the structure variable. A low positive
value (e.g. 5 %) should be set for a rewinder and a low negative value for
an unwinder. This results in an improved startup reaction for the respective
starting direction.

Enabling the torque constant correction for synchronous motors
The torque resulting from a motor is determined at the drive using the motor
current and a so-called torque constant P-0051 "Torque/force constant". How‐
ever, this so-called "Torque or force constant" is not a static value seen from
the physical point of view.
Dependencies
1.    Level of the actual motor current flow
      (the constant reduces at currents higher than INom)
2.    Temperature of motor winding and rotor
      (the constant reduces when the temperature increases)
A corrected torque constant can be used for the synchronous motor. This can
be enabled in the parameter P-0-0556 "Axis controller configuration" bit 11
(set).
Thus, the following effects on the torque/force constant are considered:
1.   Magnetic field weakening due to magnetic saturation caused by
     increased motor current compared to nominal current.
2.   Magnetic field weakening due to increased motor winding temperature.
3.   Magnetic field weakening due to increased rotor temperature depending
     on the average speed.
A significant deviation from the torque constant P-0051 is only caused if the
current load increases to 100% (or higher) of the nominal current S-0-0111
"Standstill current motor". That means the higher the motor load, the better
the impact of correction. For a motor loaded at low level, only a minimum or
no correction results.

1312 /    ctrlX PLC Engineering
1344      Error codes of the CXA_Winder

## 37.4 Error codes of the CXA_Winder

Table 1233: Error codes of the CXA_Winder
ErrorID          Additional1     Additional2 Description
INPUT_INVALID_ER 16#0A0F0117     16#0C230001 Upper limit value < Lower
ROR                                          limit value
INPUT_INVALID_ER 16#0A0F0117     16#0C230002 Format length negative
ROR
INPUT_INVALID_ER 16#0A0F0117     16#0C230003 Reference diameter nega‐
ROR                                          tive
INPUT_INVALID_ER 16#0A0F0117     16#0C230004 Window negative
ROR
INPUT_INVALID_ER 16#0A0F0117     16#0C230005 Upper limit value negative
ROR
INPUT_INVALID_ER 16#0A0F0117     16#0C230006 Lower limit value negative
ROR
INPUT_INVALID_ER 16#0A0F0117     16#0C230007 Upper limit value of the
ROR                                          velocity negative
INPUT_INVALID_ER 16#0A0F0117     16#0C230008 P-gain negative
ROR
INPUT_INVALID_ER 16#0A0F0117     16#0C230009 Setpoint negative
ROR
INPUT_INVALID_ER 16#0A0F0117     16#0C230010 Minimum feedback nega‐
ROR                                          tive
INPUT_INVALID_ER 16#0A0F0117     16#0C230011 Maximum feedback nega‐
ROR                                          tive
INPUT_INVALID_ER 16#0A0F0117     16#0C230012 Maximum/minimum feed‐
ROR                                          back negative
INPUT_INVALID_ER 16#0A0F0117     16#0C230013 HighLimitDiameter < Low‐
ROR                                          LimitDiameter
INPUT_INVALID_ER 16#0A0F0117     16#0C230014 Web width negative
ROR
INPUT_INVALID_ER 16#0A0F0117     16#0C230015 Density negative
ROR
INPUT_INVALID_ER 16#0A0F0117     16#0C230016 Core diameter negative
ROR
INPUT_INVALID_ER 16#0A0F0117     16#0C230017 Area of diameter calcula‐
ROR                                          tion negative
INPUT_INVALID_ER 16#0A0F0117     16#0C230018 Preset value negative
ROR
INPUT_INVALID_ER 16#0A0F0117     16#0C230019 Minimum diameter nega‐
ROR                                          tive
INPUT_INVALID_ER 16#0A0F0117     16#0C230020 Maximum diameter nega‐
ROR                                          tive
INPUT_INVALID_ER 16#0A0F0117     16#0C230021 Calculation mode invalid
ROR
INPUT_INVALID_ER 16#0A0F0117     16#0C230022 Mechanical inertia nega‐
ROR                                          tive
INPUT_INVALID_ER 16#0A0F0117     16#0C230023 Pre-control weighting neg‐
ROR                                          ative
INPUT_INVALID_ER 16#0A0F0117     16#0C230024 Tension high limit value
ROR                                          negative

                                 Error codes of the CXA_Winder       1344

ErrorID          Additional1   Additional2 Description
INPUT_INVALID_ER 16#0A0F0117   16#0C230025 Tension limit values
ROR
INPUT_INVALID_ER 16#0A0F0117   16#0C230026 Friction standstill torque
ROR                                        negative
INPUT_INVALID_ER 16#0A0F0117   16#0C230027 Friction maximum torque
ROR                                        negative
INPUT_INVALID_ER 16#0A0F0117   16#0C230028 Friction minimum torque
ROR                                        negative
INPUT_INVALID_ER 16#0A0F0117   16#0C230029 Friction velocity minimum
ROR                                        torque negative
INPUT_INVALID_ER 16#0A0F0117   16#0C230030 Window tension negative

ROR
INPUT_INVALID_ER 16#0A0F0117   16#0C230031 Minimum tension negative
ROR
INPUT_INVALID_ER 16#0A0F0117   16#0C230032 Maximum tension nega‐
ROR                                        tive
INPUT_INVALID_ER 16#0A0F0117   16#0C230033 Command value (set‐
ROR                                        point) Standstill negative
INPUT_INVALID_ER 16#0A0F0117   16#0C230034 Command value (set‐
ROR                                        point) OpMode negative
INPUT_INVALID_ER 16#0A0F0117   16#0C230035 Standard torque limit
ROR                                        value negative
INPUT_INVALID_ER 16#0A0F0117   16#0C230036 Minimum torque limit
ROR                                        value negative
INPUT_INVALID_ER 16#0A0F0117   16#0C230037 Factor torque limit value
ROR                                        negative
INPUT_INVALID_ER 16#0A0F0117   16#0C230038 Standard torque limit
ROR                                        value maximum exceeded
INPUT_INVALID_ER 16#0A0F0117   16#0C230039 Minimum torque limit
ROR                                        value maximum exceeded
INPUT_INVALID_ER 16#0A0F0117   16#0C230040 Factor torque limit value
ROR                                        maximum exceeded
INPUT_INVALID_ER 16#0A0F0117   16#0C230041 P-gain maximum negative
ROR
INPUT_INVALID_ER 16#0A0F0117   16#0C230042 P-gain minimum negative
ROR
INPUT_INVALID_ER 16#0A0F0117   16#0C230043 InertiaMax negative
ROR
INPUT_INVALID_ER 16#0A0F0117   16#0C230044 Current inertia negative
ROR
INPUT_INVALID_ER 16#0A0F0117   16#0C230045 InertiaMin negative
ROR
INPUT_INVALID_ER 16#0A0F0117   16#0C230046 PGainMax <= PGainMin
ROR
INPUT_INVALID_ER 16#0A0F0117   16#0C230047 InertiaMax <= InertiaMin
ROR
INPUT_INVALID_ER 16#0A0F0117   16#0C230048 Max < Core diameter
ROR
INPUT_INVALID_ER 16#0A0F0117   16#0C230049 Tension speed negative
ROR

1314 /    ctrlX PLC Engineering
1344      Data types

ErrorID          Additional1      Additional2 Description
INPUT_INVALID_ER 16#0A0F0117      16#0C230050 Unit is invalid
ROR
