# 20 CXA_MotionPrinting

## 20.1 MB_CAMTABLE

Type definitions
The structure contains the "CamTable" array, which holds the calculated cam
points, and the "NumberOfElements" variable, which indicates the number of
valid cam points in the "CamTable" array.
Table 473: Min, max, and default values for the MB_CAMTABLE structure
Name       Type        Min. value Max.      Default      Effective Descrip‐
                                  value     value                  tion
lrCamT‐    ARRAY                                         Rising    Array con‐
able       [0..1023]                                     edge at   taining
           OF LREAL                                      "Execute" the calcu‐
                                                                   lated cam
                                                                   points
uiNumber‐ UINT         3           1024                  Rising    Number of
OfEle‐                                                   edge at   valid cam
ments                                                    "Execute" points in
                                                                   the CamT‐
                                                                   able array

## 20.2 MB_CAMPROF

Type definitions
The enumeration is used to select between different cam profiles. The CAM‐
PROF_STANDARD and CAMPROF_ADDITIVE options use the old format, in
which the last element of the cam table is the interpolation point φ = 360°
- dφ. The CAMPROF_ADDITIVE_SEGMENTABLE option uses the new format, in
which the last element of the cam profile table is the interpolation point φ =
360°.w
For cam tables in the control, only the new format is available.
Table 474: Elements of the MB_CAMPROF enumeration type
Element                    Value                      Description
CAMPROF_STANDARD           0                          Cam profile without gear
                                                      ratio, non-segmentable
                                                      (old format)
CAMPROF_ADDITIVE           1                          Overlay profile with gear
                                                      ratio, non-segmentable
                                                      (old format)
CAMPROF_ADDI‐              2                          Overlay profile with gear
TIVE_SEGMENTABLE                                      ratio, segmentable (new
                                                      format)

## 20.3 MB_PilgrimStepCalcType01

     Brief description
     The function block calculates a cam table with up to 1,024 data points,
     as well as the stroke lengths for forward and reverse motion and the stop
     positions for step-feed operation. In doing so, it takes into account that the
     synchronous range of the printing cylinder may be longer than the length of
     the format to be printed. For example, in offset printing units, the plate length
     is fixed by the mechanical clamping device and is therefore always constant.
     However, the print format on the printing plate can be shorter.
     The cam calculated by the function block operates the infeed and outfeed
     rollers of the printing machine.

     Interface description

                                                 MB_PilgrimStepCalcType01
                               BOOL    Execute                                Done    BOOL
                               REAL    FormatLength                          Active   BOOL
                               REAL    SyncRange                              Error   BOOL
                               REAL    CircPrintUnit                        ErrorID   ERROR_CODE
                               REAL    CircInfeed                        ErrorIdent   ERROR_STRUCT
                               REAL    FineAdjust                   CamStrokeHigh     REAL
                         MB_CAMPROF    CamProf                       CamStrokeLow     REAL
                                                                          StopPos1    REAL
                                                                          StopPos2    REAL
                         MB_CAMTABLE   CamTable                          CamTable     MB_CAMTABLE

Table 475: Interface variables for the MB_PilgrimStepCalcType01 function block
I/O type           Name                     Type                       Comment
VAR_INPUT          Execute                  BOOL                       Function block processing enabled (once,
                                                                       edge-controlled)
                   FormatLength             REAL                       Length of the format to be printed [mm]
                   SyncRange                REAL                       If TRUE, the current actual value of the web
                                                                       tension is used as the command value for
                                                                       web tension control
                   CircPrintUnit            REAL                       If TRUE, the "PresetValue" is used as the
                                                                       command value for the closed-loop tension
                                                                       control
                   CircInfeed               REAL                       Value for the default web tension setting
                   FineAdjust               REAL                       If TRUE, the correction value is calculated
                                                                       with a negative sign

I/O type        Name                    Type           Comment
CamProf                 ⮫ Chapter      Selecting the cam profile
                        20.2 MB_CAM‐
                        PROF
                        on page 557
VAR_OUTPUT Done                         BOOL         Processing completed without errors, output
                                     data valid
Active                  BOOL         Processing active. Output data invalid
Error                   BOOL         Indicates that an error occurred
ErrorID                 ⮫ ERROR_COD Brief error description

                        E
ErrorIdent              ⮫ ERROR_STR Detailed error description
                        UCT
CamStrokeHigh           BOOL         Stroke outfeed/infeed
CamStrokeLow            BOOL         Stroke infeed/outfeed
                                     Acceleration applied relative to the "MaxAcc"
                                     input, in [%]
StopPos1                BOOL         Turning point 1 [°] with velocity = 0
StopPos2                BOOL         Turning point 2 [°] with velocity = 0
VAR_IN_OUT      CamTable                ⮫ AXIS_REF   Structure containing the calculated cam table
                                     elements and information about the number
                                     of elements

Min/max and default values
Table 476: Min., max., and default values for the inputs of the MB_PilgrimStepCalcType01 function
block
Name                   Type      Min. value       Max. value     Default      Effective
                                                                 value
Execute                BOOL                                      FALSE     Continuous
FormatLength           REAL      >0.0             n. def.        100.0     Rising edge at "Exe‐
                                                                           cute"
SyncRange              REAL      >0.0             n. def.        100.0     Rising edge at "Exe‐
                                                                           cute"
CircPrintUnit          REAL      >0.0             n. def.        100.0     Rising edge at "Exe‐
                                                                           cute"
CircInfeed             REAL      >0.0             n. def.        100.0     Rising edge at "Exe‐
                                                                           cute"
FineAdjust             REAL      0-0              100.0          1.0       Rising edge at "Exe‐
                                                                           cute"
CamProf                MB_CAM‐                                   CAM_PROF_ Rising edge at "Exe‐
                       PROF                                      STANDARD cute"

     Functional description
     If the entire circumference of a printing cylinder is not covered by a printing
     plate or printing cylinder, printed and unprinted areas alternate during contin‐
     uous operation. To prevent these gaps in printing, the material web is slowed
     down by the transport rollers, retracted a specified distance, and then accel‐
     erated back to synchronous velocity so that the new print immediately follows
     the old one.
     This compensating motion is calculated by the function block and is character‐
     ized by continuity up to the point of acceleration.

Based on the mechanical specifications for the circumference of the infeed or
outfeed roller ("CircInfeed"), the circumference of the printing cylinder ("Circ‐
PrintUnit"), the plate length “FormatLength” on the printing cylinder, and the
total length of the synchronous range “SyncRange,” the function block MB_Pil‐
grimStepCalcType01 calculates—after processing is authorized via "Execute,” a
cam table with up to 1,024 control points, as well as the two stroke factors
"CamStrokeHigh" and "CamStrokeLow" and the stop positions "StopPos1" and
"StopPos2." The number of cam elements in a cam table is set by the "Num‐
berOfElements" element of the "CamTable" structure.
It is assumed that the circumference of the infeed roller and the circumfer‐
ence of the outfeed roller are identical (CircInfeed).
Based on the lead specified by the "FineAdjust" fine-tuning function, two
strokes are calculated to maintain constant web tension. The larger stroke is
always assigned to the roller at the front in the direction of travel. The block
uses the following formulas to calculate the strokes:
CamStrokeLow = 360° * FormatLength / CircInfeed
CamStrokeLow = 360° * FormatLength / CircInfeed * (1 + FineAdjust / 100)
The "StopPos1" and "StopPos2" outputs contain the reference positions at
which the cam disc has a reversal point, for example, to perform a format
change at one of these positions during a control cycle or to change the
stroke using a register controller.
The cam table to be calculated is stored in the "CamTable" structure with scal‐
ings stored as percentages. The validity of the cam elements is indicated by
the "Done" output. The cam table can be launched using the ML_AxsCamIn2
function block.
If an error occurs while processing the function block, it is signaled by the
"Error" output. The elements of the "CamTable" structure, as well as the out‐
puts "CamStrokeHigh," "CamStrokeLow," "StopPos1," and "StopPos2," are not
updated in the event of an error.

                                Printing-Unit 1          Printing-Unit 2

                                          FormatLength
                                                                  CircPrintUnit = π * dP
                  SyncRange

          CircInfeed = π * dI                                dP

                   dI

                   Infeed                                                                  Outfeed

Cam properties
The cam table for the MB_PilgrimStepCalcTyp01 function block has the fol‐
lowing properties:
● This function block is based on the MSV_CamTableType04 function block
   and also covers cases in which the synchronization range of the printing
   cylinder has to be greater than the printing zone.
● The compensating motion, as characterized by the cam table, for returning
   the carriage is continuous up to the acceleration (s, v, a) and exhibits a
   step in the jerk (j)
● The compensating motion starts at the first table element, followed by a
   linear rise that is synchronized with the angle of the printing cylinder
● The algorithm for calculating the cam points is distributed across multiple
   cycles, i.e. instance calls, to avoid a noticeable impact on the cycle time of
   the PLC.
● The calculated strokes of the function block have the following characteris‐
   tics:
   – The strokes depend on the print format and the circumference of the
      infeed roller
   – The CamStrokeHigh stroke is intended for parameter P-0-0093 of the
      infeed roller and parameter P-0-0073 of the outfeed roller, while the
      CamStrokeLow stroke is intended for parameter P-0-0073 of the infeed
      roller and parameter P-0-0093 of the outfeed roller
To generate the web tension, the stroke for the forward movement of the out‐
feed roller and the stroke for the backward movement of the infeed roller are,
by the amount of the fine adjustment, greater than the stroke for the forward
movement of the infeed roller and the stroke for the backward movement of
the outfeed roller.

Cam types
There are three cam types:
FormatLength = SyncRange = CircPrintUnit
The printing plate or printing cylinder covers the entire synchronous zone of
the cylinder, and the synchronous zone extends around the entire circumfer‐
ence of the printing cylinder. In this case, no adjusting motion is executed.
SyncRange equals CircPrintUnit; FormatLength also has to have this value in
any case, since no compensating motion can be performed. If FormatLength
is less than SyncRange in this case, the function block terminates processing
with an error.

                                                                                                                           Linear Zone
                                                                                                                           Backward Zone
                                                                                                                           Print plate

        Electric Drives and Controls
        © All rights reserved by Bosch Rexroth AG, even and especially in cases of proprietary rights applications.
        We also retain sole power of disposal, including all rights relating to copying, transmission and dissemination.

CircPrintUnit

        200

        150

        100

         50

          0

         -50

        -100

        -150

        -200
               0                      512                                1024

                        s                   v                a

FormatLength = 2000.0
SyncRange      = 2000.0
CircPrintUnit = 2000.0
CircInFeed     = 2000.0
FormatLength = SyncRange
The printing plate or printing cylinder covers the entire synchronous zone of
the cylinder. The entire remaining cylinder area can be used for the compen‐
sating motion.

                                                                                                                            Linear Zone
                                                                                                                            Backward Zone
                                                                                                                            Print plate

         Electric Drives and Controls
         © All rights reserved by Bosch Rexroth AG, even and especially in cases of proprietary rights applications.
         We also retain sole power of disposal, including all rights relating to copying, transmission and dissemination.

        200

        150

        100

         50

          0

         -50

        -100

        -150

        -200
               0                                                                              512                                           1024

                                                        s                                           v                       a

FormatLength = 500.0
SyncRange     = 500.0
CircPrintUnit = 600.0
CircInFeed    = 600.0

        200

        150

        100

         50

          0

         -50

        -100

        -150

        -200
               0                               512                                  1024

                                      s              v                a

FormatLength = 200.0
SyncRange      = 200.0
CircPrintUnit = 2500.0
CircInFeed     = 2500.0
FormatLength < SyncRange
The printing plate or printing cylinder covers only part of the synchronous
zone of the cylinder. It has to continue to move at synchronous velocity until
the end of the synchronous range. Only when the cylinder is no longer in
contact with the web can the web be decelerated, retracted, and accelerated
again. Here, the additional path of the non-printing synchronous area has to
be removed.

                                  e
                             Z on
                           r
                         ea
                   Lin

                                           d
                                        ar
                                    c kw e
                                  Ba Zon
                                                                      Linear Zone
                                                                      Backward Zone
                                                                      Print plate

        200

        150

        100

         50

          0

         -50

        -100

        -150

        -200
               0                    512                   1024

                       s                  v         a

FormatLength = 500.0
SyncRange     = 1200.0
CircPrintUnit = 2000.0
CircInFeed    = 3000.0

        200

        150

        100

         50

          0

         -50

        -100

        -150

        -200
               0                    512                   1024

                       s                  v         a

FormatLength = 1000.0
SyncRange     = 1500.0
CircPrintUnit = 2000.0
CircInFeed    = 3000.0
FormatLength > SyncRange

For certain production runs, the format length may also exceed the sync range
of a printing cylinder.

        200

        150

        100

         50

          0

         -50

        -100

        -150

        -200
               0                      512                                1024

                         s                  v                a

Use case: Special product printed using two printing units:

Standard product (format length 350 mm):

Special product (format length 700 mm):

Troubleshooting
ErrorID        Additional1               Additional2   Description
INPUT_RANGE_ER 16#0A0F0118               16#0C230041   The "NumberO‐
ROR                                                    fElements" input is
                                                       < minimum or >
                                                       maximum
INPUT_RANGE_ER 16#0A0F0118               16#0C230042   The "Format‐
ROR                                                    Length" input is <
                                                       minimum
INPUT_RANGE_ER 16#0A0F0118               16#0C230043   The "SyncRange"
ROR                                                    input is < min‐
                                                       imum
INPUT_RANGE_ER 16#0A0F0118               16#0C230044   The "CircPrintUnit"
ROR                                                    input is < min‐
                                                       imum
INPUT_RANGE_ER 16#0A0F0118               16#0C230045   The "CircInfeed"
ROR                                                    input is < min‐
                                                       imum
INPUT_RANGE_ER 16#0A0F0118               16#0C230046   The "FineAdjust"
ROR                                                    input is < min‐
                                                       imum or > max‐
                                                       imum
INPUT_INVALID_ER 16#0A0F0118             16#0C230047   The address of the
ROR                                                    "CamTable" field is
                                                       null
INPUT_INVALID_ER 16#0A0F0118             16#0C230048   The "SyncRange"
ROR                                                    input is > "Circ‐
                                                       PrintUnit"

## 20.4 MB_FlexLockPrepareType01

Brief description
The function block prepares four different slave axis profiles for the LockOn/
LockOff functionality in advance.

Interface description

Table 477: Interface variables of the MB_FlexLockPrepareType01 function block
I/O type   Name                           Type        Comment
VAR_INPUT  Execute                        BOOL        If this input is set, the function block is active
VAR_OUTPUT Done                           BOOL        Function finished
           Active                         BOOL        Function active
           Error                          BOOL        Indicates that an error occurred during the
                                                      function block operation
               ErrorID                    ⮫ ERROR_COD Brief error description
                                          E
               ErrorIdent                 ⮫ ERROR_STR Detailed error description
                                          UCT
VAR_IN_OUT     FlexLockParameter          ⮫ MB_FLEX‐  Additional parameter
                                          LOCK_PARAM‐
                                          ETER
               Axis                       ⮫ AXIS_REF  Reference to slave axis

Table 478: Min./max. and default values of the MB_FlexLockPrepareType01
function block inputs
Name        Min. value      Max. value Default value Unit       Effective
Exe‐        FALSE            FALSE     FALSE         /          /
cute
StartDis‐   0         Maximum 90                       Degrss   Rising edge at
tance                 modulo                                    "Execute"
                      value of
                      the axis
StopDis‐   0          Maximum 90                       Degrss   Rising edge at
tance                 modulo                                    "Execute"
                      value of
                      the axis
SyncType Valid struc‐ Valid struc‐ SHORTEST_           /        Rising edge at
           ture       ture         WAY                          "Execute"
RatioNum‐ 0           MaxDint‐     1                   /        Rising edge at
erator                Value                                     "Execute"
RatioDeno‐ 0          MaxDint‐     1                   /        Rising edge at
minator               Value                                     "Execute"

Name          Min. value   Max. value Default value Unit    Effective
MasterFi‐     0            100        0.0           %       Rising edge at
neAdjust                                                    "Execute"
SyncVel    MinLreal‐        MaxLreal‐   0.0         rpm     Rising edge at
           Value           Value                            "Execute"
SyncAcc    MinLreal‐        MaxLreal‐   0.0         rad/s^2 Rising edge at
           Value           Value                            "Execute"
MasterOff‐ MinLreal‐        MaxLreal‐   100.0       rpm     Rising edge at
setVel     Value           Value                            "Execute"
MasterOff‐ MinLreal‐        MaxLreal‐   2.0         rad/s^2 Rising edge at
setAcc     Value           Value                            "Execute"

Functional description
MB_FlexLockPrepareType01 is called before MB_FlexLockType01 is executed.
After changing FlexLockParameter.Startdistance or Stopdistance, compute the
profiles again.
MB_FlexLockPrepareType01 executes the following steps:
● a) Compute the profile FLEX_LOCK_DWELL and save it in profile 0 of the
  slave axis
● b) Compute the FLEX_LOCK_START profile and save it in profile 1 of the
  slave axis
● c) Compute the FLEX_LOCK_RUN profile and save it in profile 2 of the slave
  axis
● d) Compute the FLEX_LOCK_STOP profile and save it in profile 3 of the
  slave axis
Refer to the enumeration type ⮫ MB_FLEXLOCK_PROFILETYPE.
In the following Data Layer node, check whether the profiles have been
created successfully after executing the function block MB_FlexLockPrepare‐
Type01:
motion/axs/SlaveAxis/cfg/functions/coupling/sync-motion/flexprofile/profiles

Error codes
The function block can generate the following error messages:

ErrorID       Additional1        Additional2   Description
INPUT_RANGE_E 16#0A0F011         16#0C23002    The stop distance is too short
RROR          8                  C
INPUT_RANGE_E 16#0A0F011         16#0C23002    The start distance is too short
RROR          8                  D
INPUT_RANGE_E 16#0A0F011         16#0C23002    Start distance and stop dis‐
RROR          8                  E             tance are too long

## 20.5 MB_FlexLockType01

Brief description
The function block MB_FlexLockType01 selects slave profiles ("Dwell" (profile
0), "Start" (profile 1), "Run" (profile 2) or "Stop" (profile 3)) from MB_Flex‐
LockPrepare and enables them, depending on the "LockOn" input for the
LockOn/LockOff functionality.

Interface description

Table 479: Interface variables of the MB_FlexLockType01 function block
I/O type Name                 Type              Comment
VAR_INPU Enable               BOOL              Function block processing
T                                               enabled
         LockOn               BOOL              Enabling or disabling
         InitProfile          ⮫ MB_FLEX‐        Profile synchronized for the
                              LOCK_PROFILE‐     first time
                              TYPE
              StopPosition    LREAL             Position at which the slave
                                                axis stops. Becomes active if
                                                LockOn is set to FALSE
              MasterOffset    LREAL             Offset of the RUN profile
                                                between master and slave
VAR_OUT ActProfile            ⮫ MB_FLEX‐        Profile is currently active
PUT                           LOCK_PROFILE‐
                              TYPE
              SwitchingMas‐   LREAL             Master position in which the
              terPosStart                       profile is switched to LockOn
                                                profile
              SwitchingMas‐   LREAL             Master position in which the
              terPosStop                        profile is switched to LockOff
                                                profile

I/O type   Name            Type                   Comment
           InOperation     BOOL                   The function is operating
                                                  without errors. The outputs
                                                  are valid
           CommandA‐       BOOL                   Function block is aborted by
           borted                                 another function block
           Error           BOOL                   Indicates that an error
                                                  occurred during the function
                                                  block operation
           ErrorID         ⮫ ERROR_CODE           Brief error description

           ErrorIdent      ⮫ ERROR_STRUCT         Detailed error description
VAR_IN_O FlexLockPara‐     ⮫ MB_FLEX‐     Additional parameter
UT       meter             LOCK_PARAMETER
           Master          ⮫ AXIS_REF     Reference to master axis
           Slave           ⮫ AXIS_REF             Reference to slave axis

Table 480: Min./max. and default values of the MB_FlexLockType01 function
block inputs
Name         Min. value   Max. value    Default       Unit         Effective
                                        value
Enable       FALSE        TRUE           FALSE        /     /
LockOn       FALSE        TRUE          FALSE         FALSE When the
                                                            "Enable"
                                                            input is set
                                                            to TRUE
InitProfile Valid struc‐ Valid struc‐ ⮫ MB_FLEX‐ FLEX_LOCK_ When the
            ture         ture         LOCK_PARA DWELL       "Enable"
                                      METER                 input is set
                                                            to TRUE
StopPosi‐   0            Maximum      0          0          Realtime
tion                     modulo
                         value of the
                         axis
Master‐     Negative     Maximum      0          0          Realtime
Offset      modulo       modulo
            value of the value of the
            axis         axis
StartDis‐     0          Maximum      90         Degrss     When the
tance                    modulo                             "Enable"
                         value of the                       input is set
                         axis                               to TRUE
StopDis‐      0          Maximum      90         Degrss     When the
tance                    modulo                             "Enable"
                         value of the                       input is set
                         axis                               to TRUE
SyncType    Valid struc‐ Valid struc‐ SHORTEST_ /           When the
            ture         ture         WAY                   "Enable"
                                                            input is set
                                                            to TRUE
RatioNumer‐ 0            MaxDint‐     1          /          When the
ator                     Value                              "Enable"
                                                            input is set
                                                            to TRUE

Name            Min. value   Max. value   Default   Unit         Effective
                                          value
RatioDeno‐      0            MaxDint‐     1         /            When the
minator                      Value                               "Enable"
                                                                 input is set
                                                                 to TRUE
MasterFi‐       0            100          0.0       %            When the
neAdjust                                                         "Enable"
                                                                 input is set
                                                                 to TRUE
SyncVel         MinLreal‐     MaxLreal‐   0.0       rpm          When the
                Value        Value                               "Enable"
                                                                 input is set
                                                                 to TRUE
SyncAcc         MinLreal‐     MaxLreal‐   0.0       rad/s^2      When the
                Value        Value                               "Enable"
                                                                 input is set
                                                                 to TRUE
MasterOff‐      MinLreal‐     MaxLreal‐   100.0     rpm          When the
setVel          Value        Value                               "Enable"
                                                                 input is set
                                                                 to TRUE
MasterOff‐      MinLreal‐     MaxLreal‐   2.0       rad/s^2      When the
setAcc          Value        Value                               "Enable"
                                                                 input is set
                                                                 to TRUE

Functional description
The function block starts with the status specified by the "InitProfile" input
and then selects the corresponding profiles for the LockOn/LockOff function‐
ality depending on the "LockOn" input and enables them.
The "StopPosition" and "MasterOffset" inputs can be changed when the Flex‐
Profile is in the "active" state.
The computation of the LockOn/LockOff position is based on the adjustment
of:
● Access phase (for MLC A-0-2656/P-0-0227)
● Effective master axis velocity (for MLC A-0-2652/P-0-0777)

Prerequisites
● Master and slave axes should be set to modulo format and to the modulo
  value of 360 degrees.
● The function block MB_FlexLockPrepare should be executed to compute
  and save the profiles.
● The master and slave axes are switched on.
● The function block should be executed on the Motion task of the PLC task
  type.
● The master axis should move in positive direction.
● The drive should be homed before using this function block (absolute
  homing preferred).

Error codes
The function block can generate the following error messages:

ErrorID       Additional1 Additional2 Description
STATE_MACHINE 16#0A0F01 16#0C230021 Invalid state machine of the
_ERROR        18                      master axis
RESOURCE_ERR 16#0A0F01 16#0C230022 Invalid access to actual IEC task
OR            18
RESOURCE_ERR 16#0A0F01 16#0C230023 An error occurred while
OR            18                      retrieving information on the
                                      current IEC task
OTHER_ERROR 16#0A0F01 16#0C230024 Invalid task type
              18

OTHER_ERROR 16#0A0F01 16#0C230025 Invalid external event
              18
OTHER_ERROR 16#0A0F01 16#0C230026 The axis is not a modulo axis
              18
OTHER_ERROR 16#0A0F01 16#0C230027 The modulo axis value is not
              18                      360
ACCESS_ERROR 16#0A0F01 16#0C230028 An error occurred while
              18                      retrieving the provider handle
ACCESS_ERROR 16#0A0F01 16#0C230029 An error occurred while
              18                      retrieving the provider type
OTHER_ERROR 16#0A0F01 16#0C23002A Invalid provider type
              18
ACCESS_ERROR 16#0A0F01 16#0C23002B An error occurred while
              18                      retrieving the duplicate value of
                                      the provider

Note
Due to the direct change between the profiles, dynamic synchronization
requires re-synchronized axes; overshooting cannot be avoided in the stop and
start phase.

## 20.6 MB_PositionMonitoring_GantryCant

Brief description
The function block MB_PositionMonitoring_GantryCant monitors the relative
position of two the axes with regard to tilting. The retract motion is possible
using the tolerance band functionality. The direction of motion out of the
tilting is continuously monitored.
The function block can be used to monitor:
● Infeed axes of printing units
● Gantry axes with mechanically parallel travel distances, etc.

Interface description

Table 481: Interface variables of the MB_PositionMonitoring_GantryCant function block
I/O type           Name                    Type         Comment
VAR_INPUT          Enable                  BOOL         Function block processing enabled
                   MachineSet              ⮫ MB_POS_MON Machine-specific characteristics
                                           _GANTRY_CANT
           PosDrv1                         LREAL        Current position of axis 1
           PosDrv2                         LREAL        Current position of axis 2
VAR_OUTPUT InOperation                     BOOL         Monitoring the axes completed without
                                                        errors; output signals valid
                   Error                   BOOL         Monitoring the axes completed with errors,
                                                        output variable "ErrorIdent" valid
                   ErrorID                 ⮫ ERROR_CODE Diagnostic description in case of error
                   ErrorIdent              ⮫ ERROR_STRUC Diagnostic description in case of error
                                           T
                   OutOfRange              BOOL          Permissible range is exceeded
                   OutOfRangePos           BOOL          Permissible range is exceeded. Axis posi‐
                                                         tion of axis 1 is higher than or equal to the
                                                         axis position of axis 2
                   OutOfRangeNeg           BOOL          Permissible range is exceeded. Axis posi‐
                                                         tion of axis 1 is lower than the axis position
                                                         of axis 2

        Functional description

        The function block MB_PositionMonitoring_GantryCant cyclically monitors the
        positions of two axes with regard to tilting after enabling the process via
        "Enable". If the distance of the axes exceeds the maximum range "Range"
        allowed, this is signaled via the outputs "OutOfRange" and "OutOfRangePos"
        or "OutOfRangeNeg".
        In the following cycle, the output "OutOfRange" is reset. The outputs "OutO‐
        fRangePos" or "OutOfRangeNeg" continue to signal the requirement of a posi‐
        tion adjustment until reaching the admissible distance minus the tolerance.
        If the maximum distance reached plus the tolerance is exceeded again or even
        more during this position adjustment in this period, this is signaled by setting
        the output "OutOfRange" again.
        If an error occurs during the function block processing, this is signaled via
        the output "Error" and, in this case, specified by the updated elements of the
        output structure "ErrorIdent". The other outputs are not updated in the event
        of an error.

## 20.7 MB_TensionControlLoadCellType01

        Brief description
        Depending on the measured value of a load cell, the tension controller con‐
        trols the tension to the command value.

      Interface description

Table 482: Interface variables of the MB_TensionControlLoadCellType01 function block
I/O type       Name                   Type        Comment
VAR_INPUT      Enable                 BOOL        If this input is set, the function block oper‐
                                                  ates
               Pause                  BOOL        Controller paused (control difference is set to
                                                  0)
               Preset                 BOOL        Set controller to a preset value
               PresetValue            LREAL       Value for default setting
               SetpointLock           BOOL        Use the actual value as command value for
                                                  the closed-loop tension control
               NegPolarity            BOOL        The direction is determined by changing Addi‐
                                                  tivePosDeg.
               Feedback               LREAL       Current actual value of the tension
               HighLimit              LREAL       Maximum value for the controller output
               LowLimit               LREAL       Minimum value for the controller output
               Adaptive               BOOL        If TRUE, adaptive P-gain is enabled.
                                                  If FALSE, P-gain is equal to KpLowVel

I/O type           Name                 Type          Comment
PControlLowVel       LREAL         P-gain at low master axis velocities, if Adap‐
                                   tive=TRUE, otherwise value for constant P-
                                   gain
MasterVelocityLow    LREAL         Master axis velocity up to which KpLowVel is
                                   used
PControlHighVel      LREAL         P-gain at high master axis velocities
MasterVelocityHigh   LREAL         Master axis velocity at which KpHighVel is
                                   used
IControl             LTIME         Integral action time in ms
WindowValue          LREAL         Value in % that statistically fulfills the condi‐
                                   tion:
                                   [Setpoint - (Setpoint * WindowValue)] <
                                   Feedback < [Setpoint + (Setpoint * Window‐
                                   Value)]
WindowMaxValue       LREAL         Maximum value in % at which the actual
                                   value can be greater than the command
                                   value.
                                   Feedback < (Setpoint * WindowMaxValue)
WindowMinValue       LREAL         Minimum value in % by which the actual
                                   value can be less than the command value.
                                   Feedback > (Setpoint * WindowMinValue)
StandstillEnable     BOOL          Enabling the standstill control
StandstillVel        LREAL         Additive velocity for standstill control
StandstillVelDead‐   LREAL         Value in units of Setpoint/Feedback below
band                               which the standstill velocity is reduced
ResponseCurve        ARRAY [0..3]  Characteristic curve to scale the deviation if
                     OF            the InVelocity path is active
                     IL_COORD_TY
                     PE01
VAR_OUTPUT InOperation                  BOOL         Side register controller is operating
Error                        BOOL         Indicates that an error occurred during the
                                  function block operation
ErrorID              ⮫ ERROR_COD Brief error description
                     E
ErrorIdent           ⮫ ERROR_STR Detailed error description
                     UCT
InPause              BOOL         "Pause" is active. The "ControlValue" and
                                  "ParameterControlValue" outputs maintain
                                  their values
PresetAck            BOOL         "Preset" is executed. The "Preset" value is
                                  copied to the "ControlValue" and "Parameter‐
                                  ControlValue" outputs
HighLimitActive      BOOL         Upper limit value is active. "ControlValue"
                                  would be higher, but is limited to "HighLimit"
LowLimitActive       BOOL         Lower limit value is active. "ControlValue"
                                  would be lower, but is limited to "LowLimit"
WindowIn             BOOL         TRUE if Feedback is within the window (see
                                  input values)
WindowMax            BOOL         TRUE if Feedback is greater than the max‐
                                  imum value (see input values)

I/O type       Name                  Type          Comment
WindowMin             BOOL          TRUE if Feedback is greater than the min‐
                                    imum value (see input values)
GearRatioFineAdjust LREAL           The FineAdjust value for the gear ratio in %
                                    for use in ProcessCtrl.FineAdjust
AdditivePosDeg        LREAL         Additive position in degrees for use in Proc‐
                                    essCtrl.Master.Offset
VAR_IN_OUT     Setpoint              LREAL         Tension value Setpoint
Master                ⮫ AXIS_REF    Reference to master axis
Slave                 ⮫ AXIS_REF    Reference to slave axis

Table 483: Min./max. and default values of the MB_TensionControlLoadCellType01 function block
inputs
Name                   Type     Min. value    Max. value       Default       Effective
                                                               value
Enable                 BOOL                                    FALSE         Continuous
Pause                  BOOL                                    FALSE         Continuous
Preset                 BOOL                                    FALSE         Continuous
SetPointLock           BOOL                                    FALSE         Continuous
NegPolarity            BOOL                                    FALSE         Continuous
Feedback               LREAL    n. def.       n. def.          0.0           Continuous
PresetValue            LREAL    n. def.       n. def.          0.0           Rising edge at
                                                                             "Preset"
HighLimit              LREAL    >LowLimit     n. def.       200.0            Continuous
LowLimit               LREAL    -95.0         <HighLimit    -50              Continuous
Adaptive               BOOL                                 FALSE            Continuous
PControlLowVel         LREAL    >0.0          n. def.       1.0              Continuous
MasterVelocityLow      LREAL    >0.0          <=MasterVelo‐ 1.0              Continuous
                                              cityHigh
PControlHighVel        LREAL    >0.0          n. def.       1.0              Continuous
MasterVelocityHigh     LREAL    >=MasterVelo‐ n. def.       1.0              Continuous
                                cityLow
IControl               LTIME    0s            n. def.       0s               Continuous
WindowValue            LREAL    0.0           100.0         0.0              Continuous
WindowMaxValue         LREAL    >=WindowMin‐ 100.0          0.0              Continuous
                                Value
WindowMinValue         LREAL    0.0           <=Window‐     0.0              Continuous
                                              MaxValue
StandstillEnable   BOOL                                     FALSE            Continuous
StandstillVel      LREAL        0.0           n. def.       0.0              Continuous
StandstillDeadband LREAL        0.0           n. def.       1.0              Continuous

Functional description

Depending on the measured value of a load cell, the tension controllers
(MB_TensionControlLoadCellType01) control the tension to the command
value.
The tension controller is designed as PI controller. The controller output
affects the gear fine adjustment of the slave axis (draw roll).
For the standstill control, an additional P-controller is integrated. The con‐
troller output in standstill acts on the additive master axis position of the
slave axis (draw roll).
StandstillVel determines the additional gain of the P-controller. This means
that the greater the standstill, the greater the oscillation. The range of Addi‐
tivePosDeg is -360~360. This range is important for the standstill control.
When the function block is enabled, AdditivePosDeg always changes from 0.
If AdditivePosDeg is greater than 360, AdditivePosDeg immediately changes
to -360. This can cause a reversal of the axis. Normally, the standstill control
should be used to fine-tune situations.
With the MB_TensionControlLoadCellType01 tension controller, the dynamic
control loop response can be parameterized by specifying the controller
parameters.
The slave axis can either be operated in the velocity-synchronous or in the
phase-synchronous operation mode.

branch

standstill (Standstill Control)

Preset/PresetValid
A positive edge at the "Preset" input specifies an initial value for the control
variable using the "PresetValue" variable. At the same time, the internal var‐
iables of the controller are set in a way that the controller is approached
without any jerk. "Preset" acts only on the gear fine adjustment in the path
"InVelocity Control".

Adaptive, PControlLowVel, PControlHighVel, MasterVelocityLow, MasterVeloci‐
tyHigh
The P-gain can either be specified as constant or adaptive P-gain. Via the
"Adaptive" input, either an adaptive or a constant P-gain is selected. Setting
"Adaptive" to TRUE selects the adaptive P-gain.
If a constant P-gain is selected, only the value in "PControlLowVel" is effective
for the P-gain.
If an adaptive P-gain is selected, the "PControlLowVel", "PControlHighVel",
"MasterVelocityLow" and "MasterVelocityHigh" inputs have to be assigned. The
characteristic curve looks as follows:

The individual inputs describe the characteristic curve for positive master axis
velocities. The characteristic curve for negative master axis velocities results
from the mirroring at the axis of the P-gain. This means that only symmetric
characteristics are possible. The P-gain between the master axis velocities
"MasterVelocityLow" and "MasterVelocityHigh" is linearly interpolated.
This results in some conditions for the value ranges of the inputs:
● The values for "MasterVelocityLow" and "MasterVelocityHigh" have to be
  positive
● The values for "MasterVelocityLow" and "MasterVelocityHigh" may not be
  identical
● The "MasterVelocityLow" value has to be lower than the "MasterVelocity‐
  High" value

If one of these conditions is not met, an error is generated at the function
block output.

SetpointLock
Setting the "SetpointLock" input applies the current actual tension value as
the new command value for the tension controller. For example, the function
allows the command value of the tension to obtain a reasonable initial value
that reflects the current state of the machine.

Pause
The "Pause" input allows the tension controller to pause. If this input is set to
TRUE, the control deviation is set to "0", i.e. the controller output is frozen at
the current I-value. If "Pause" is active, the "InPause" output is set.

NegPolarity
The "NegPolarity" input affects the control direction. Depending on the posi‐
tion of the draw roll with regard to the direction, the material moves and the
position of the feed roll, the control direction has to be either positive or
negative. This input determines the direction of the change of AdditivePosDeg.
The input should not be changed when switching the standstill control. This
input is normally changed if the sign of the transmission ratio changed.

Feedback
This input represents the actual value of the tension. It can be read via an
analog input at the drive or at the Inline I/O for example. The user is respon‐
sible for a reasonable scaling.

PresetValue
Setting the "Preset" input specifies an initial value for the control variable
using the "PresetValue" variable. At the same time, the internal variables of
the controller are set in a way that the controller is approached without any
jerk.

HighLimit, HighLimitAct
This input limits the control variable of the controller to a maximum value.
If the limitation occurs, the I-value of the controller is no longer summed up
("Anti-reset-windup"). If a limitation occurs, the "HighLimitAct" output is set.

LowLimit, LowLimitAct
This input limits the control variable of the controller to a minimum value.
If the limitation occurs, the I-value of the controller is no longer summed up
("Anti-reset-windup"). The minimum value is -95. If a limit occurs, the "LowLi‐
mitAct" output is set.

PControlLowVel
This value corresponds to the proportional gain of the tension controller if the
"Adaptive" input is not active. Otherwise, it represents the lower gain of an
adaptive P-gain.

WindowValue, WindowIn
Use this value to define a symmetric window containing the current actual
tension value.
The window is defined as follows:

WindowMaxValue, WindowMax
This value can be used to set the upper value for the actual tension value.
The value is evaluated as follows:

If this condition is met, the "WindowMax" output is set. If this condition is not
met, the output is not set and there is no limitation.

WindowMinValue, WindowMin
This value can be used to specify a lower value for the actual tension value.
The value is evaluated as follows:

If this condition is met, the "WindowMin" output is set. If this condition is not
met, the output is not set and there is no limitation.

StandstillEnable
Set the "StandstillEnable" input to additively add the velocity specified in
"StandstillVel" to the axis to be controlled. This allows a closed-loop tension
control at standstill as well.
At lower velocities, the influence of the gear ratio fine adjustment decreases
continuously. There is also an open control loop at master axis standstill,
since the gear ratio fine adjustment does no influence anymore. Thus, the
"StandstillEnable" input has to be set when reaching the standstill window
in order not to increase the I-value up to the limit in the "InVelocity Control"
path by the open control loop.

ResponseCurve
Using the "ResponseCurve" input, the control deviation can be scaled. Use
this functionality to specify a smaller scaling of the control deviation for
smaller control deviations. This results in a lower proportional gain and thus
causes a smoother control behavior in a steady state.
When parameterizing the input, the controller parameters should first be
set without evaluation. Subsequently, a lower scaling should be specified.
This allows to globally set the controller parameters first using the system
dynamics, and then, a local optimization is ensured (e.g. for the steady state).
The local optimization is parameterized with a characteristic curve with up
to four data points. Negative deviations are processed by point reflection of
the curve at the origin. This results in a total of nine linear sections. The

section s5 passes the origin. The sections s1 and s9 have a slope of 1 and
each run into positive or negative infinity. If the input is not assigned, a 1-to-1
characteristic curve is used as default value. That means that it is not scaled.

Points P1 to P4 are stored in an array of IL_COORD_TYPE01. If less than
four points are required, the x-coordinates of the points that are not required
(beginning with the last point) are set to 0. The x-values have to be positive
and increase in positive direction. The same point can be stored twice.

StandstillEnable, StandstillVel, StandstillVelDeadband
The standstill control can be executed using the "StandstillEnable" and
"StandstillVel" inputs. This adds an additive velocity. To achieve better control
quality, it is reduced by the command value.
This can be executed with a modified signum function provided with the fol‐
lowing transfer function:

The control deviation is relativized in the "Setpoint" range. If the "Feedback"
approaches the "Setpoint", the closed-loop control becomes "more sensitive"
than a simple two-point controller. The value responsible for the limitation
can be set at the "StandstillVelDeadband" input. The values are provided
with the same units as the "Setpoint" input or the "Feedback" input. There
is a linear interpolation between the two extreme values "+StandstillVel" and
-"StandstillVel" so that the transfer function above results for the control devi‐
ation and tension velocity.
Subsequently, the factor determined is multiplied by the specified "Stand‐
stillVel". The velocity is processed as speed with the scaling set in the drive. If
the web velocity should be entered instead of the speed, calculate it before.
To reverse the direction of motion for the standstill control, set the "NegPo‐
larity" input.
Subsequently, the result is multiplied by a correction factor. This correction
factor results from the gear ratio. However, the gear ratio fine adjustment
is not considered. The gear ratio fine adjustment is generally very small and
therefore not important. The gear ratio is only applied at a rising edge at the
"Enable" input.

## 20.8 MB_TensionControlLoadCellMatParType01

Brief description
The function block regulates the web tension to a predefined command value
based on the measured value from a load cell.
Compared to the similarly structured function block "⮫ MB_TensionControl‐
LoadCellType01 The MB_TensionControlLoadCellMatParType01 function block
has the following advantages:
● Configuring the controller based on machine and material data.
● Custom controller configuration (command value or input response) to
  enable a tailored controller design.
● Customizable control loop dynamics (aperiodic or periodic), ensuring flexi‐
  bility in performance optimization.
● Automatic adjustment of controller parameters to achieve optimal response
  characteristics.

     Interface description

Table 484: Interface variables of the MB_TensionControlLoadCellMatParType01 function block
I/O type           Name                  Type     Comment
VAR_INPUT          Enable                BOOL     If TRUE, the function block runs
                   Pause                 BOOL     If TRUE, the controller is stopped (the con‐
                                                  trol difference is set to 0)
                   Feedback              LREAL    Current actual value of the track voltage
                   SetpointLock          BOOL     If TRUE, the current actual value of the web
                                                  tension is used as the command value for
                                                  web tension control
                   Preset                BOOL     If TRUE, the "PresetValue" is used as the
                                                  command value for the closed-loop tension
                                                  control
                   PresetValue           LREAL    Value for the default web tension setting
                   NegPolarity           BOOL     If TRUE, the correction value is calculated
                                                  with a negative sign
                   HighLimit             LREAL    Maximum value for the controller output
                   LowLimit              LREAL    Minimum value for the controller output
                   WindowValue           LREAL    Value in % that statistically fulfills the condi‐
                                                  tion:
                                                  [Setpoint - (Setpoint * WindowValue)] <
                                                  Feedback < [Setpoint + (Setpoint * Window‐
                                                  Value)]
                   WindowMaxValue        LREAL    Maximum value in % at which the actual
                                                  value can be greater than the command
                                                  value.
                                                  Feedback < (Setpoint * WindowMaxValue)

I/O type       Name                 Type          Comment
WindowMinValue       LREAL         Minimum value in % by which the actual
                                   value can be less than the command value.
                                   Feedback > (Setpoint * WindowMinValue)
Circumference        LREAL         Master Axis Diameter [mm]
DistanceRoll1To2     LREAL         Length of the material web to be adjusted
                                   between two rollers [mm]
DelayFeedbackValue   LREAL         Filter delay
StandstillEnable     BOOL          If TRUE, the idle control is enabled
StandstillVelDead‐   LREAL         Value in units of Setpoint/Feedback below

band                               which the standstill velocity is reduced
ResponseCurve        ARRAY [0..3]  Characteristic curve to scale the deviation if
                     OF            the InVelocity path is active
                     IL_COORD_TY
                     PE01
MasterVelocityLow    LREAL        Master axis velocity up to which KpLowVel is
                                  used [1/min]
MaterialParameter    ⮫ MB_TEN‐    Data Structure with Material Elements
                     SION_CON‐
                     TROL_MATE‐
                     RIAL
ControlMode          ⮫ MB_TEN‐    Enumeration that contains the control mode
                     SION_CON‐
                     TROL_MODE
DampingFactor        LREAL        A factor used to fine-tune or regulate the
                                  dynamics of a closed-loop control system
GearIn               DINT         Electric GearIn: Transmission ratio (denomi‐
                                  nator)
GearOut              DINT         Electric GearOut: Transmission ratio (numer‐
                                  ator)
VAR_OUTPUT InOperation              BOOL         The controller is running
Error                    BOOL         Indicates that an error occurred
ErrorID                  ⮫ ERROR_COD Brief error description
                     E
ErrorIdent           ⮫ ERROR_STR Detailed error description
                     UCT
InPause              BOOL         "Pause" is active. The "ControlValue" and
                                  "ParameterControlValue" outputs maintain
                                  their values
PresetAck            BOOL         "Preset" is executed. The "Preset" value is
                                  copied to the "ControlValue" and "Parameter‐
                                  ControlValue" outputs
HighLimitActive      BOOL         Upper limit value is active. "ControlValue"
                                  would be higher, but is limited to "HighLimit"
LowLimitActive       BOOL         Lower limit value is active. "ControlValue"
                                  would be lower, but is limited to "LowLimit"
WindowIn             BOOL         TRUE if Feedback is within the window (see
                                  input values)
WindowMax            BOOL         TRUE if Feedback is greater than the max‐
                                  imum value (see input values)

I/O type           Name                    Type            Comment
WindowMin               BOOL            TRUE if Feedback is greater than the min‐
                                        imum value (see input values)
GearRatioFineAdjust LREAL               The FineAdjust value for the gear ratio in %
                                        for use in ProcessCtrl.FineAdjust
AdditivePosDeg          LREAL           Additive position in degrees for use in Proc‐
                                        essCtrl.Master.Offset
VAR_IN_OUT         Setpoint                LREAL           Tension value Setpoint
Master                  ⮫ AXIS_REF      Reference to the master axis
Slave                   ⮫ AXIS_REF      Reference to slave axis

Table   485:   Min.,   Max.,    and    default    values               for     the      inputs      of     the
MB_TensionControlLoadCellMatParType01 function block
Name                        Type      Min. value      Max. value     Default         Effective
                                                  value
Enable                      BOOL                                     FALSE           Continuous
Pause                       BOOL                                     FALSE           Continuous
Feedback                    LREAL     n. def.         n. def.        0.0             Continuous
SetpointLock                BOOL                                     FALSE           Continuous
Preset                      BOOL                                     FALSE           Continuous
PresetValue                 LREAL     n. def.         n. def.        0.0             Rising edge at
                                                                  "Preset"
NegPolarity                 BOOL                                     FALSE           Continuous
HighLimit                   LREAL     >LowLimit    n. def.           200.0           Continuous
LowLimit                    LREAL     -95.0        <HighLimit        -50             Continuous
WindowValue                 LREAL     0.0          100.0             0.0             Continuous
WindowMaxValue              LREAL     >=WindowMin‐ 100.0             0.0             Continuous
                   Value
WindowMinValue              LREAL     0.0          <=Window‐         0.0             Continuous
                                MaxValue
Circumference               LREAL                                    100.0           Rising edge at
                                                                  "Enable"
DistanceRoll1To2            LREAL                                    100.0           Rising edge at
                                                                  "Enable"
DelayFeedbackValue LREAL                                             100 ms          Continuous
StandstillEnable   BOOL                                              FALSE           Continuous
StandstillVelDead‐ LREAL              0s              n. def.        1.0             Continuous
band
MasterVelocityLow  LREAL                                             1.0             Continuous
DampingFactor      LREAL                                             100.0           Continuous
GearIn             DINT                                              1.0             Rising edge at
                                                                  "Enable"
GearOut                     DINT                                     1.0             Rising edge at
                                                                  "Enable"

        Functional description
        The operation of the traction controller is illustrated in the following flow
        charts. Depending on the "StandstillEnable" input, either the "InVelocity Con‐
        trol" or "Standstill Control" path is active.

standstill/in velocity
The "InVelocity Control" path is active when the "StandstillEnable" input is
not set. The voltage is controlled via the "Gear ratio fine adjustment" or "Addi‐
tivePosDeg" parameter.

To control the system when it is at a standstill, the "Standstill Control" control
path can be activated. This control path takes effect when the "StandstillEn‐
able" input is set. The voltage is controlled via the “additive master axis posi‐
tion.”

Control)
To ensure ease of use, the flow charts do not include information about
the "WindowValue," "WindowMaxValue," or "WindowMinValue" limits or their
status indicators.

Circumference, DistanceRoll1To2
The input values "Circumference" and "DistanceRoll1To2" are used for the
internal calculation of the control parameters. They describe the specific
structural characteristics of the facility. The "Circumference" value describes
the circumference of the "Master" axis, and the "DistanceRoll1To2" value
describes the length of the material web between the "Master" and "Slave"
axes.

DelayFeedbackValue
The input value "DelayFeedbackValue" is used for the internal calculation of
the controller parameters and describes the delay time Tu of the web tension
control loop. So this value corresponds to the total of peripheral time con‐
stants such as motor dynamics, filter times, sensors, motion cycle time.

MasterVelocityLow
The "MasterVelocityLow" input is used to limit the controller parameters.
Due to the speed-dependent controlled system response, speed-dependent
controller parameters result. Depending on the desired control loop response,
either the controller gain and/or the controller reset time is speed-dependent.
The following substitutionally represents the dependency of the controller
gain from the web velocity in a graphical form.

As already explained for "StandstillEnable," the transmission fine-tuning
becomes less and less effective at low velocities. This behavior is directly
reflected in the controller gain. To prevent unreasonably large controller
parameters, the "MasterVelocityLow" input is used to limit the controller
parameters at "low" path speeds. In most cases, the value of this input should
lie below the smallest production speed and above the switchover speed in
the standstill path. This ensures unrestricted control-loop dynamics above
the "MasterVelocityLow" speed, while at the same time limiting the controller
parameters at "low" path speeds

MaterialParameter
The "MaterialParameter" input structure is used for the internal calculation of
the controller parameters. This structure contains information regarding the
individual web material. The individual elements of this structure describe
the type, the width, the thickness and/or the grammage and the mod‐
ulus of elasticity of the web material. For paper web materials, the basis
weight ("WebGrammage") is evaluated, and for other web materials, the
material thickness ("WebThickness") is evaluated. When a predefined track
material ("MaterialParameter.MaterialType") is selected, the modulus of elas‐
ticity is retrieved from the internal database. Accordingly, the "MaterialPara‐

meter.MaterialEModule" input is evaluated only when a user-defined material
type—"CUSTOM_PAPER" or "CUSTOM_NON_PAPER"—is selected. For clarity,
two example circuit configurations are shown below:

Paper from block-internal database
MaterialParameter.MaterialType := OFFSET_PAPER;
MaterialParameter.WebWidth := 500;
MaterialParameter.WebGrammage := 80;

User-defined web material (e.g. foil)
MaterialParameter.MaterialType := CUSTOM_NON_PAPER;

MaterialParameter.WebWidth := 500;
MaterialParameter.WebThickness := 200;
MaterialParameter.MaterialEModule := 650;
If the web material used is not listed in the internal database and if there is
no information regarding the modulus of elasticity, it may be determined in a
standstill measurement.

You can see from this Hooke’s formula that by means of a meas‐
ured force difference, due to a given elongation (change in length
due to an additive master axis position), the individual modulus of
elasticity [N/mm²] can be determined at standstill. Furthermore, the
product of the modulus of elasticity [N/mm²] and the cross-sectional
area [mm²] can also be calculated directly, and by normalizing the cross-
sectional area ("MaterialType:=CUSTOM_NON_PAPER", "WebWidth:=1[mm]",
"WebThickness:=1000[µm]") to A=1[mm²], it can be specified as a modified
modulus of elasticity [N].

ControlMode
The "ControlMode" input can be used to define the primary control loop
behavior. The web tension controller may either be optimized for com‐
mand value response or for disturbance response. If the web tension is
controlled using a fixed-value control mode, this input should be set to
"CONTROL_MODE_OPT_DISTURBANCE." As a result, the internal controller
parameters will be determined so that faults are perfectly corrected. Con‐
versely, in a follow-up configuration, this input should be assigned "CON‐
TROL_MODE_OPT_COMMAND." As a result, the internal controller parameters
will be determined so that the controlled variable perfectly follows the com‐
mand variable.

DampingFactor
The "DampingFactor" input can be used to define the control loop dynamics.
It acts on both branches, standstill control and control during web opera‐
tion. The control loop dynamics may either be set aperiodically (without over‐
shoot) or periodically (with overshoot). In this context, a "damping factor"
of 100%—assuming exact path parameters—corresponds exactly to the aperi‐
odic limit case, and a "damping factor" of 120% corresponds to a periodic
oscillation with approximately 20% overshoot. Furthermore, the control loop
response can be slowed down to a "damping factor" of 20% or accelerated

to a "damping factor" of 200%. If track parameters ("Circumference," "Distan‐
ceRoll1To2," "DelayFeedbackValue," "MaterialParameter") or system behavior
(e.g., location- and time-dependent humidity and temperatures) that differ
from actual conditions, this input can also be used to correct the desired
dynamic control loop behavior.

### 20.8.1 Data types

MB_TENSION_CONTROL_MATERIAL (STRUCT)
The following table lists the attributes of the MB_TENSION_CONTROL_MATE‐
RIAL structure:
Name               Type            Min. value            Max. value         Default value    Effective            Description

MaterialType       ⮫ MB_TEN‐       CUSTOM_PAPER          BOPP_FILM          OFFSET_PAPER     Continuous           Type of track mate‐
SION_CON‐                                                                                      rial
TROL_MATE‐
RIAL_TYPE

WebWidth           LREAL           >0.0                  n. def.            500.0            Continuous           Width of the web
                                                                                       material [mm]*

WebThickness       LREAL           >0.0 (if Material‐    n. def.            0.0              Continuous (if       Thickness of the
        Type is not of type                                       MaterialType is not film material [µ]*
        PAPER)                                                    of type PAPER)

WebGrammage        LREAL           >0.0 (if Material‐    n. def.            80               Continuous (if       Weight of the web
        Type is of type                                           MaterialType is of   material [g/m²]
        PAPER)                                                    type PAPER)

MaterialEModules   LREAL           >0.0 (if Material‐    n. def.            0.0              Continuous           Modulus of elas‐
        Type is of type                                                                ticity of the web
        CUSTOM_PAPER)                                                                  material [N/mm²]*

* When using the internal material database (E [N/mm²]), the units [mm] and
[µm] are required. When using a user-defined modulus of elasticity, the basic
unit is [N/mm²]. However, any units may be used, such as [kg/ft²]. Make sure
that the selected units are always used consistently.

MB_TENSION_CONTROL_MATERIAL_TYPE (ENUM)
The following table lists the properties of the MB_TENSION_CONTROL_MATE‐
RIAL_TYPE enumeration.
Enumeration / Element                   Number         Description
CUSTOM_PAPER                            1              Customized paper
PACKING_PAPER                           2              Packaging paper
OFFSET_PAPER                            3              Offset paper (standard)
METALLIZED_PAPER                        4              Metallized paper
CUSTOM_NON_PAPER                        5              Customized (no paper)
PE_FILM                                 6              Polyethylene film (PE film)
PET_FILM                                7              Polyethylene terephthalate film (PET
                                                       film)
PP_FILM                                 8              Polypropylene film (PP film)
OPP_FILM                                9              Oriented polypropylene film (OPP
                                                       film)
BOPP_FILM                               10             Biaxially oriented polypropylene film
                                                       (BOPP film)

    MB_TENSION_CONTROL_MODE (ENUM)
The following table lists the properties of the MB_TENSION_CONTROL_MODE
enumeration.
Enumeration / Element    Number      Description
CON‐                     1           The function block optimizes the dis‐
TROL_MODE_OPT_DIS‐                   turbance response of the "Feedback"
TURBANCE                             value with respect to the "Setpoint"
                                     value (default setting).
CON‐                     2           The function block optimizes the
TROL_MODE_OPT_COM‐                   response of the "Feedback" value to
MAND                                 the "Setpoint" value.

## 20.9 MB_FLEXLOCK_PARAMETER

Elements of the MB_FLEXLOCK_PARAMETER structure
I/O type Name           Type          Comment
VAR_IN_O StartDis‐      LREAL         Removal of the slave motion for
UT       tance                        Lock ON
         StopDis‐       LREAL         Removal of the slave motion for
         tance                        Lock OFF
         SyncType      ML_DynSync‐    Synchronization setting for initial
                       Direction      synchronization
           RatioNumer‐ DINT           Gear setting for ML_FlexProfile
           ator
           RatioDeno‐ DINT            Gear setting for ML_FlexProfile
           minator
           MasterFi‐   LREAL          Gear setting for ML_FlexProfile
           neAdjust
           SyncVel     LREAL          Velocity for initial synchronization
           SyncAcc     LREAL          Acceleration for initial synchroniza‐
                                      tion
           MasterOff‐   LREAL         Velocity to change the offset
           setVel
           MasterOffse‐ LREAL         Acceleration to change the offset
           tAcc

## 20.10 MB_FLEXLOCK_PROFILETYPE

Elements of the enumeration type MB_FLEXLOCK_PROFILETYPE
FLEX_LOCK_DWELL                        0
FLEX_LOCK_START                        1
FLEX_LOCK_RUN                          2
FLEX_LOCK_STOP                         3

## 20.11 MB_POS_MON_GANTRY_CANT

Brief description
The MB_POS_MON_GANTRY_CANT data type maps the machine set of the
MB_PositionMonitoring_GantryCant function block.
The structure includes the following data:

Structural element     Type        Min. value     Max. value     Default      Effective
                                            value
Range                  LREAL        >= 2*Toler‐   n. def.        10.0         Maximum allowed
              ance                                       position difference of
                                                         both axes
Tolerance              LREAL       0.0            n. def.        5.0          Tolerance of the
                                                         limits

The specified tolerance has to meet the following condition:
Range > 2*Tolerance
