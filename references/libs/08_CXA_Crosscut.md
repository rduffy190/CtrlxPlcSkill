# 8 CXA_Crosscut

## 8.1 Introduction and overview

Paper, plastic and metal webs are cut to length in a CrossCutter using a
rotating knife system. The web moves independently and the knife is synchron‐
ized on the web so that it moves at the same linear velocity as the material
web during the cutting interval. After the cutting, the knife is moved by a
further web distance that results in the intended cutting length.
The Fig. 57 shows a typical CrossCutter application.

This function is generally used with the synchronized Motion function Flex‐
Profile described in the documentation ⮫ "Motion App, Motion Runtime
Environment for ctrlX OS", Application Manual.

Table 44: Function blocks of the CXA_Crosscut library
Name                                   Description
⮫ MB_CrossCutType01                    The function block MB_CrossCutSealType01 calculates, loads
                                       and activates a FlexProfile for CrossSealer or CrossCutter
                                       applications.
⮫ MB_CrossCutCalc‐                     The MB_CrossCutCalcType01 function block provides all
Type01MB_CrossCutCalcType01            required data at its outputs which have to be loaded into
                                       the FlexProfile of an axis to operate a CrossCutter or a Cross‐
                                       Sealer with the functions selected in the parameters of the
                                       function block.
⮫ MB_WriteCrossCutPro‐                 The function block MB_WriteCrossCutProfile can write Cross‐
fileMB_CrossCutCalcType01              Cutter profiles in point tables and the FlexProfile from the
                                       Data Layer.

## 8.2 Data types

### 8.2.1 MB_CORR_PROFILE (ENUM)

Brief description
The enumeration type MB_CORR_PROFILE is used by the ⮫ MB_CrossCutCalc‐
Type01 function block to define a correcting motion in the cutting area.

Table 45: MB_CORR_PROFILE enumeration type
Element                                    Value       Description
CORR_PROFILE_NONE                          0           No correction in the cutting zone
                                                       The CrossCutter axis velocity corresponds to the master axis
                                                       velocity
CORR_PROFILE_OVERSPEED                     1           Constant overspeed or reduction of the CrossCutter axis velocity
                                                       in the cutting area
                                                       The CrossCutter axis velocity is faster or slower than the master
                                                       axis velocity by the value parameterized at the "Overspeed" input
                                                       of the MB_CrossCutCalcType01 function block.
CORR_PROFILE_COS_COMP                      2           Correction of the CrossCutter axis velocity

                                The velocity is changed in a way that the CrossCutter axis rotates
                                in material direction (the x-component of the velocity vector) at
                                a constant velocity. The speed of the CrossCutter axis has to be
                                adapted depending on the current position in the cut.
CORR_PROFILE_PUSH_OUT                      3           Executing a PushOut motion at the end of the cut
                                Parameterization via the "PushOut" input of the MB_CrossCut‐
                                CalcType01 function block. The speed of the CrossCutter axis
                                has to be adapted depending on the current position in the cut.
                                ⮫ MB_PUSH_OUT_CONFIG
CORR_PROFILE_COS_COMP_AND_PUSH_OUT 4                   Combination of the corrections CORR_PROFILE_COS_COMP and
                                CORR_PROFILE_PUSH_OUT. Parameterization via the "PushOut"
                                input of the MB_CrossCutCalcType01 function block
                                ⮫ MB_PUSH_OUT_CONFIG

### 8.2.2 MB_POINT_TABLE_DATA (STRUCT)

Brief description
The MB_POINT_TABLE_DATA structure is used to generate the point tables
using the ⮫ MB_CrossCutCalcType01 function block.

Table 46: MB_POINT_TABLE_DATA structure
Structural element     Type                            Min. Max.       Default Description
                                                       value value     value
PointTableName         STRING                                                  Point table name
NumberOfElements       UINT                                                    Number of elements in the point table
PointTable             ARRAY[0..1023] OF LREAL                                 Array with the value of the table

### 8.2.3 MB_PUSH_OUT_CONFIG (STRUCT)

Brief description
The MB_PUSH_OUT_CONFIG structure is used by the ⮫ MB_CrossCutCalc‐
Type01 function block.
This structure can parameterize a defined PushOut at the end of the cut.

Table 47: MB_PUSH_OUT_CONFIG structure
Name                 Type     Min. value       Max. value      Default value Description
PushOutBegin         LREAL                                     -5.0%          Beginning of the PushOut area (parameter
                                                                              A)
                                                                              The value must not be equal to 0, unit in
                                                                              [%]

Name                  Type         Min. value           Max. value       Default value Description
Overspeed_At_Cut      LREAL        -100.0%              100.0%           5.0%         Overspeed during a cut (parameter B)
                                                        The value must not be equal to 0, unit in
                                                        [%]
Overspeed_Max         LREAL        > 0.0%               100.0%           10%          Maximum overspeed (parameter C)
                                                        Unit in [%]

### 8.2.4 MB_RESOLUTION (ENUM)

Brief description
The enumeration MB_RESOLUTION is used by the function block ⮫ MB_Cross‐
CutCalcType01.
The enumeration can modify the number of cam table data points and thus
the required computation time.

Table 48: MB_RESOLUTION enumeration type
Element                   Value       Description                                                             Number of data
                                                                                                              points (cutting seg‐
                                                                                                              ment + compensating
                                                                                                              segment + cutting
RESOLUTION_LOW            1           Low resolution, short computation time required (faster by              10 + 100 + 10
                                      approx. factor 3 in contrast to medium resolution)
RESOLUTION_MIDDLE 2                   Medium resolution, average computation time required (faster by 25 + 300 + 25
                                      approx. factor 3 in contrast to high resolution)
RESOLUTION_HIGH           3           High resolution, much computation time required                         50 + 1000 + 50

### 8.2.5 MB_STEP_MOTION_LAW (ENUM)

Brief description
The enumeration type MB_STEP_MOTION_LAW specifies the motion step
modes of the generated segments.

Table 49: MB_CORR_PROFILE enumeration type
Element                    Value                            Description
VELOCITY_IN_VELOCITY_LINEA 1                                Velocity-in-velocity, constant velocity
R
POINTS_TABLE_AUTO          50                               Point table with interpolation

### 8.2.6 MB_STOP_CONFIG (STRUCT)

Brief description
The MB_STOP_CONFIG structure is used to define the stop behavior when the
function block ⮫ MB_CrossCutCalcType01 enables FALSE.

Table 50: MB_STOP_CONFIG structure
Structural ele‐    Type                         Min.       Max.      Default value                   Description
ment                                            value      value
StopDeceleration LREAL                          0                    1000                            This ramp stops the slave axis.
EnableStopPos      BOOL                                              FALSE                           Set TRUE if the slave axis is
                                                                                                     to be stopped at a target posi‐

Structural ele‐    Type                   Min.     Max.    Default value                Description
ment                                      value    value
StopPositon        LREAL                  0.0      360.0   0.0                          Stop position of the slave axis,
                                                             only applied if EnableStopPos
                                                             is set to TRUE.
StopDirection      ML_PosAbsExDirection                    ML_PosAbsExDirection.        Stop direction for the slave
                                DIRECTION_CURRENT            axis

## 8.3 Function blocks

### 8.3.1 MB_CrossCutType01

Brief description
The function block MB_CrossCutType01 calculates, loads and activates a Flex‐
Profile for CrossSealer or CrossCutter applications. The function block uses
the MB_CrossCutCalcType01 function block internally for the calculation.
With the calculated FlexProfile, the slave axis moves with product velocity in
the sealing or cutting area. Other functions such as OverSpeed, PushOut or
cosine correction can be optionally added in this area.
Beyond the sealing or cutting area, an almost optimal compensation motion
(in terms of acceleration and energy loss) is performed if the specified format
length does not match the distance of the knife or sealing jaw. Furthermore,
a pendular motion of the CrossSealer or CrossCutter axis in freely selectable
limits can be predefined to optimally use the acceleration capacity of the
drive in case of large format lengths.
At runtime, input variables (such as the format length) can be changed to
automatically calculate a new FlexProfile in the background. The newly calcu‐
lated FlexProfile is then enabled and effective at the switching angle.
At a negative edge at "Enable", the FlexProfile is stopped and the slave
axis switches to the "StandStill" state. The stop motion depends on
MB_STOP_CONFIG.

Interface description

Table 51: Interface variables of the MB_CrossCutType01 function block
               Name               Type               Description

Input          Enable             BOOL               Function block processing enabled

CrossCutter        BOOL               If "CrossCutter" = TRUE, the CrossCutter use case is selected
(see the following detailed description).

In this use case, the master axis has to be standardized so
that the material to be cut covers the distance that corre‐
sponds to the knife distance in one revolution. In this case,
the electronic gearbox of the FlexProfile is set with the trans‐
mission ratio "FormatLength/KnifeDistance". Furthermore, the
input "CutSealArea" functions as cutting angle of the Cross‐
Cutter and the input variables "ProductsPerCut" and "Start‐
Product" are not applied.

If "CrossCutter" = FALSE, the CrossSealer use case is selected
(see the following detailed description).

In this use case, the master axis has to be standardized so
that one revolution corresponds to a foil feed of one product
length. In this case, the electronic gearbox of the FlexProfile
is set with the transmission ratio "1/ProductsPerCut". Further‐
more, the input "CutSealArea" corresponds to the sealing
length and is thus defined in translatory units (e.g. mm or
inch). The inputs "ProductsPerCut" and "StartProduct" are
evaluated in this case.

StartFlexProfile   BOOL               The activation of a new FlexProfile is blocked as long as this
input is set to FALSE.

"StartFlexProfile" = TRUE enables the new FlexProfile if the
output "ProfileReady" = TRUE, otherwise the new FlexProfile
waits for "ProfileReady".

ProductsPerCut     UINT               Input is only effective if "CrossCutter" = FALSE.

Number of products per sealing process.

Corresponds to the number of master revolutions per sealing
or cutting process.

StartProduct       UINT               Input is only effective if "CrossCutter" = FALSE.

If there is more than one product per sealing or cutting
process ("ProductsPerCut" > 1), the start product can be
defined via this input when enabling the function block.

NumberOfKnives     UINT               Number of sealing jaws or knives available on the circumfer‐
ence of the sealing or cutting cylinder. The sealing jaws or
knives are positioned with the same distance from each other.

KnifeDistance      LREAL              Distance of the knives or sealing jaws.

Corresponds to the circumference divided by the number of
knives or sealing jaws [mm or in]

FormatLength       LREAL              Predefined cutting length or sealing distance/package length
[mm or in]

CutSealArea        LREAL              In this area, the knife or the sealing jaw moves with product
velocity. The velocity within this window can be adjusted
using additional inputs, such as "OverSpeed," "PushOut," or
cosine correction.

If the input "CrossCutter" = FALSE, this input corresponds to
the sealing length and is thus defined in translatory units (e.g.
in mm or inch).

If the input "CrossCutter" = TRUE, this input acts rotatorily as
angle in [°].

Name                Type                  Description

PendelumFactor      LREAL                 Maximum pendulum radius in [%]

0%: No pendular motion (standstill at large format length)

100%: Maximum pendular motion (pendular motion up to the
edges of the sealing area or cutting area)

CorrectionProfile   MB_CORR_PROFILE       Special profile selection.

The inputs "OverSpeed" or "PushOut" have to be used for the
parameterization of the special profile.

Overspeed           LREAL                 Constant overspeed or reduction of the master axis velocity in
the cutting area in [%].

0%: No overspeed

100%: Double master axis velocity

-50%: Half master axis velocity

This input is only effective if the option CORR_PRO‐
FILE_OVERSPEED is selected at the input "CorrectionProfile".

PushOut             MB_PUSH_OUT_CONFIG    Structure to define a "PushOut" motion during the cut or the
sealing process.

In the "CorrectionProfile", either the
option CORR_PROFILE_PUSH_OUT or CORR_PRO‐
FILE_COS_COMP_AND_PUSH_OUT has to be selected. Other‐
wise, "PushOut" is disabled and thus ineffective.

Resolution          MB_RESOLUTION         The resolution of the cam calculation is specified by deter‐
mining the number of data points in three stages.

DynSyncDirection    ML_DynSyncDirection   Synchronization direction

StopConfig          MB_STOP_CONFIG        Configuring the stop mode of the slave axis

Output        InOperation         BOOL                  CrossCutter runs without any faults

Error               BOOL                  Processing completed with error

ErrorID             ⮫ ERROR_CODE          Error class

ErrorIdent          ⮫ ERROR_STRUCT        Diagnostic description in case of error

Shutdown            BOOL                  CrossSealer is stopped with "StopConfig" after a negative
edge at "Enable". During this time, the "Shutdown "output is
enabled to display the defined stop.

ChangeProfile       BOOL                  If input variables such as, for example, If "FormatLength" is
changed during operation, a new FlexProfile is calculated and
loaded in the background. Subsequently, the new FlexProfile
is used. Since this process requires several cycles, this output
is enabled for this period. If input values are received again
during this process (e.g., "FormatLength") is changed, the cur‐
rent operation is canceled and rerun using the new data.

The output is reset as soon as the newly calculated FlexProfile
becomes effective and thus the switching phase was passed.

ProfileReady        BOOL                  This output is set as soon as the FlexProfile was calculated,
loaded and enabled. This output is deleted as soon as
the FlexProfile is applied (after having passed the switching
phase).

ActualProduct       UINT                  If there is more than one product per sealing process ("Pro‐
ductsPerCut" > 1), the currently processed product is dis‐
played via this output. At a rising edge at "Enable", this output
is reset to the input variable "StartProduct".

Name                               Type                     Description

CutCounter                         UINT                     The "CutCounter" increases with each modulo overflow (360°
                                                            → 0°) of the slave axis. At a rising edge at "Enable", the "Cut‐
                                                            Counter" is reset to zero

VAR_IN_OUT          Master                             ⮫ AXIS_REF               Reference to master axis

Slave                              ⮫ AXIS_REF               Reference to slave axis

                                                            (= CrossCutter/CrossSealer)

                                                            The modulo value is 360° electrical and is mechanically
                                                            defined as the distance between two knives/sealing jaws.

Table 52: Min./max. and default values of the inputs of the MB_CrossCutType01 function block
Name                  Type                     Min. value             Max. value                Default value            Effective

Enable                BOOL                                                                      FALSE                    Continuous

CrossCutter           BOOL                                                                      FALSE                    Rising edge at

StartFlexProfile      BOOL                                                                      TRUE                     Continuous

ProductsPerCut        UINT                     1                      32                        1                        Rising edge at

StartProduct          UINT                     1                      32                        1                        Rising edge at

NumberOfKnives        UINT                     1                      8                         1                        Rising edge at

KnifeDistance         LREAL                    >0.0 mm/in             n. def.                   100.0mm/in               Rising edge at

FormatLength          LREAL                    >0.2*KnifeDistance         30*knifeDistance      100.0mm/in               Continuous*

CutSealArea           LREAL                    >0 degree              <360.0                    10 degree                Continuous*

                           > 0mm                  <KnifeDistance            10 mm/in

PendelumFactor        LREAL                        0.0%               100 %                     0.0%                     Continuous*

CorrectionProfile     MB_CORR_PROFILE              0                      4                     0                        Continuous*

Overspeed             LREAL                    -50.0%                 +100.0%                   0.0%                     Continuous*

PushOut               MB_PUSH_OUT_CONFIG                                                                                 Continuous*

Resolution            MB_RESOLUTION            RESOLUTION_LOW         RESOLUTION_HIGH           RESOLU‐                  Rising edge at
                                                                            TION_MEDIUM              "Enable"

DynSyncDirection      ML_DynSyncDirection                                                       SHORTEST_WAY             Rising edge at

StopConfig            MB_STOP_CONFIG                                                                                     Continuous

Master                AXIS_REF                                                                                           Rising edge at

Slave                 AXIS_REF                                                                                           Rising edge at

*Applying the inputs takes multiple cycles and is displayed at the "ChangeProfile" output

          Functional description
          After the processing was enabled via "Enable", the function block calculates a
          FlexProfile as well as cam point tables for the CrossSealer/CrossCutter appli‐
          cation according to the specified input data. The function block also supports
          multiple CrossSealers/CrossCutters with equally distributed knives or sealing
          jaws.

Note for multi-use CrossCutters or CrossSealers:
For multi-use CrossCutter or CrossSealer applications, adjust the parameteri‐
zation of the mechanical gearbox (see also ⮫ Necessary boundary conditions
and requirements on page 999).
Therefore, the calculated motion sequence is divided into the following two
sections:
● The cutting or sealing area is defined by the input variable "CutSealArea".
    In this area, the knife or the sealing jaw moves with the product velocity. In
    addition, other functions such as "OverSpeed" for overspeed or a reduction
    of the velocity, "PushOut" for a push out motion or the cosine correction
    can be optionally added.
    In this area, the following input variables become effective:

    – "CorrectionProfile"
       "CorrectionProfile" provides special profiles in the cutting and sealing
       area ("OverSpeed", "PushOut", "cosine correction", "PushOut" + "cosine
       correction").
    – "OverSpeed"
       "OverSpeed" indicates the velocity increase or reduction in "CutSea‐
       lArea" in [%].
    – "PushOut"
       "PushOut" defines a special "PushOut" motion during the cutting or
       sealing process.
● Outside the cutting or sealing area, an optimum ompensation motion with
    regard to jerk and energy is performed if the specified format length
    "FormatLength" does not correspond to the distance of the knives or the
    sealing jaws "KnifeDistance". Furthermore, a pendular motion of the Cross‐
    Sealer axis or CrossCutter axis can be specified in adjustable limits to opti‐
    mally use the acceleration capacity of the drive for large format lengths.
    The following input variable becomes effective in this area:
    – "PendelumFactor"
       "PendelumFactor" specifies the maximum admissible pendulum radius
       in [%].
The FlexProfile and the cam point tables are automatically loaded and ena‐
bled after the calculation. During this period, the output "ChangeProfile" is
set. If the FlexProfile is applied and if the slave axis is synchronized, the
output InOperation is activated. In this state, the slave axis moves synchro‐
nously to the master axis using the previously calculated FlexProfile. In this
state, the cut or seal counter "CutCounter" is increased with each revolution
of the CrossCutter axis or CrossSealer axis.
If input variables such as "FormatLength" are changed at runtime, a new Flex‐
Profile is calculated in the background. Since this process requires several
cycles, the output "ChangeProfile" is set during this period. The output "Pro‐
fileReady" is set if the new FlexProfile has been enabled, but the switching
phase has not yet been passed. If the switching phase is reached subse‐
quently, the calculated FlexProfile is applied and the outputs "ChangeProfile"
and "ProfileReady" are reset. If any input data is changed again during the cur‐
rent change of the FlexProfile, the changes are discarded and the calculation
with the new input data is started.
The data points of the cam point tables used in the FlexProfile can be influ‐
enced via the "Resolution" input. A high resolution results in a maximum
accuracy but requires most of the time during the calculation. The time effort
can be reduced by the factor 3 or 9 using the settings "Medium" and "Low".
The reduction of the resolution is useful if different product lengths are con‐
tinuously processed with high cycle rates (> 500 cycles/min).

A negative edge at "Enable" results in a defined shutdown of the Cross‐
Cutter/CrossSealer. The slave axis is decelerated until standstill with the
adjustable ramp "StopDeceleration". During the defined shutdown, the output
"Shutdown" is set. The output "Shutdown" is reset if the slave axis has
reached its standstill position or if an error occurred.

Scaling notes
The translatory input variables of the function block (e.g. "FormatLength") can
be specified either in [mm] or in inch [in]. However, it has to be considered
that all translatory input variables are specified in the same unit (mm or
inch).

Use case CrossSealer
Via the "CrossCutter" input, the function block generally differentiates
between the CrossCutter application and the CrossSealer use case.
If the input "CrossCutter" is FALSE, a CrossSealer application is assumed.
Triggering a cross sealer cylinder of flow wrappers is a typical example of
this use case. The sealing jaw should move with the product velocity and
with an optimum correction profile during the sealing process. Outside the
sealing range, a ompensation motion is to be performed if the format length
"FormatLength" does not correspond to the distance of the sealing jaws "Kni‐
feDistance".
The CrossSealer use case provides the following characteristics:
● The "CutSealArea" input corresponds to the length of the sealing seam and
  is thus specified in translatory units (mm or inch).
● One master axis revolution (360°) corresponds to the foil feed of one
  product length.

● One sealing process can include several products. The number of products
    per sealing process is specified via the "ProductsPerCut" input. This input
    directly influences the electronic gearbox of the FlexProfile.
● The first product is set via the "StartProduct" input after a positive edge at
    "Enable". This variable is effective internally to position offset of the Flex‐
    Profile used. After a positive edge at "Enable", the output "ActualProduct"
    is set to the input "StartProduct".
Note on starting the function block
If the master axis and the slave axis are at any position at the function block
start, the slave axis performs a dynamic synchronization to synchronize with
the master axis. If this is not intended, the master axis and slave axis have to
be set to the 0° or 180° position before starting the function block.

The following figure shows an example of a signal-time diagram of the master
axis and the CrossSealer axis for one product per package:

process
The following figure shows an example of a signal-time diagram of the master
axis and the CrossSealer axis for 3 products per package:

Use case CrossCutter
Via the "CrossCutter" input, the function block generally differentiates
between the CrossCutter application and the CrossSealer use case.
If the input "CrossCutter" is TRUE, a CrossCutter application is assumed.
During the cutting process, the knife should move with the velocity of the
product and with an optional correction profile. Outside the cutting area, a
ompensation motion is to be performed if the format length "FormatLength"
does not correspond to the distance of the sealing jaws "KnifeDistance".
The CrossCutter use case provides the following characteristics:
● The input "CutSealArea" corresponds to the angular range of the Cross‐
  Cutter in which it is traveling with the velocity of the product and the
  optional correction profile.
● One revolution of the master axis corresponds to the material feed length
  which corresponds to the knife distance "KnifeDistance".
● One cut per product is assumed. The inputs "ProductsPerCut" and "Start‐
  Product" are not effective (these inputs is internally set to 1).
● The output "ActualProduct" is always set to "1".
● The electronic gearbox of the FlexProfile used is set to the transmission
  ratio "FormatLength/KnifeDistance".
  This gear only allows integer values from 1 to 65535 as numerator and
  denominator of the gearbox ratio. Thus, there is a maximum cutting length
  deviation due to quantization.
  If a deviation of the cutting lengths occurs due to quantization, a respective
  gearbox ratio fine adjustment is calculated and specified. In this case, a
  drift between the master and the slave axis results due to the system
  conditions.

          Necessary boundary conditions and requirements
          ● The sealing jaws/knives are symmetrically distributed over the circumfer‐
             ence.
          ● The 0° position of the slave axis is always exactly in the middle of the
             CutSealArea.
          There are two options for the slave axis if "Enable" is set to FALSE, depending
          on the "StopConfig" input:
          ● If "StopConfig.EnableStopPos" = TRUE, the slave axis is stopped at the
            "StopConfig.StopPosition" position via the last velocity.
          ● If "StopConfig.EnableStopPos" = FALSE, the axis is stopped immediately via
            the "StopConfig.StopDeceleration" ramp.

### 8.3.2 MB_CrossCutCalcType01

          Brief description
          The MB_CrossCutCalcType01 function block provides all required data at its
          outputs which have to be loaded into the FlexProfile of an axis to operate a
          CrossCutter or a CrossSealer with the functions selected in the parameters
          of the function block. All inputs of the function block are transferred once at
          a rising edge at "Execute". In addition, the function block writes directly into
          the arrays specified by input/output variable at its runtime. The written data is
          only valid if the function block was processed without errors and if it returns
          "Done".

          Interface description

Table 53: Interface variables of the MB_CrossCutCalcType01 function block
                    Name                     Type                          Description

Input               Execute                  BOOL                          Processing enabled at a rising edge

ModuloValue              LREAL                         Modulo value of the slave axis

KnifeDistance            LREAL                         Distance between the knifes (e.g. mm)

FormatLength             LREAL                         Format length (e.g. mm)

CutAngle                 LREAL                         Length of cutting zone

PendelumFactor           LREAL                         Maximum pendulum radius in [%]

                                                       0%: No pendulum motion

                                                       100%: Maximum pendulum motion (pendulum
                                                       motion up to the cutting range limits)

CorrectionProfile        MB_CORR_PROFILE               Special profile selection.

                                                       To parameterize the special profile, use the
                                                       inputs "Overspeed" or "PushOut".

Name                    Type                                    Description

Overspeed               LREAL                                   Constant overspeed or reduction of the master
                                                                axis velocity in the cutting area in [%].

                                                                0%: No "Overspeed"

                                                                100%: Double master axis velocity

                                                                -50%: Half master axis velocity

                                                                This input is only effective if the option
                                                                CORR_PROFILE_OVERSPEED is selected at the
                                                                input "CorrectionProfile".

                                                                In the "CorrectionProfile", the CORR_PRO‐
                                                                FILE_OVERSPEED option has to be selected.
                                                                Otherwise, "Overspeed" is disabled and thus
                                                                ineffective.

PushOut                 MB_PUSH_OUT_CONFIG                      Structure to define a "PushOut" motion during
                                                                the cut or the sealing process.

                                                                In the "CorrectionProfile", either the option
                                                                CORR_PROFILE_PUSH_OUT or CORR_PRO‐
                                                                FILE_COS_COMP_AND_PUSH_OUT has to be
                                                                selected. Otherwise, "PushOut" is disabled and
                                                                thus ineffective.

Resolution              MB_RESOLUTION                           The resolution of the cam calculation is speci‐
                                                                fied by determining the number of data points
                                                                in three stages

Output             Done                    BOOL                                    Processing completed

Active                  BOOL                                    Processing active

Error                   BOOL                                    Processing completed with error

ErrorID                 ⮫ ERROR_CODE                            Error class

ErrorIdent              ⮫ ERROR_STRUCT                          Diagnostic description in case of error

NumberOfSteps           UINT                                    Number of steps for the profile

NumberOfPointTables     UINT                                    Number of points tables used for the profile

VAR_IN_OUT         RangeStartPos           ARRAY [*] OF LREAL                      Array of the area (master init positions), three
                                                                elements are required

Gain                    ARRAY [*] OF LREAL                      Array of the gain (distances) of the slave axis,
                                                                three elements are required

LawType                 ARRAY [*] OF MB_STEP_MOTION_LAW         Array of step modes "LawType", three elements
                                                                are required

PointTable              ARRAY [*] OF MB_POINT_TABLE_DATA        Array of MB_POINT_TABLE_DATA, three ele‐
                                                                ments are required

Table 54: Min./max. and default values of the inputs of the MB_CrossCutCalcType01 function
block
Name                Type                 Min. value             Max. value           Default value              Effective

Execute             BOOL                                                             FALSE                      Continuous

ModuloValue         LREAL                >0.0                   n. def.              360.0                      Rising edge at "Exe‐

KnifeDistance       LREAL                > 0.0                  n. def               100.0                      Rising edge at "Exe‐

FormatLength        LREAL                >0.2*KnifeDistance     30*KnifeDistance     100.0                      Rising edge at "Exe‐

CutAngle            LREAL                0.0                    < "ModuloValue"      20.0                       Rising edge at "Exe‐

Name                Type                 Min. value      Max. value       Default value       Effective

PendelumFactor      LREAL                0.0%            100.0%           0.0%                Rising edge at "Exe‐

CorrectionProfile   MB_CORR_PROFILE                                       CORR_PROFILE_NONE Rising edge at "Exe‐

Overspeed           LREAL                -50.0%          100.0%           0.0%                Rising edge at "Exe‐

PushOut             MB_PUSH_OUT_CONFI                                                         Rising edge at "Exe‐
G                                                                         cute"

Resolution          MB_RESOLUTION                                         RESOLUTION_HIGH     Rising edge at "Exe‐

Functional description
The function block computes profiles for the CrossCutter application. The
individual segments consist either of analytical segments or point tables. After
processing enabled via "Execute", a result consisting of three segments is
computed once based on the input variables. The parameters describing the
profile are stored in the respective arrays which have to be provided as array
at the inputs of the function block. The arrays have to be large enough to be
able to save the number of calculated motion steps (currently three steps).
Array handling is similar to the MB_WriteCrossCutProfile function block, as
the user has to call the function after computing to write the computed profile
to the free set of the FlexProfile.
The following list describes the meaning of the individual inputs of the
MB_CrossCutCalcType01 function block in detail:
● The "ModuloValue" input specifies the modulo value of the CrossCutter
  axis. 360.0° are specified by default.
● The "FormatLength" and "KnifeDistance" inputs define the "FormatRatio"
  that specifies the product length to be cut. "FormatRatio" describes the
  ratio of the desired product length and the circumference of the Cross‐
  Cutter cylinder.
  This means that if "FormatRatio==1", the length of the cut product cor‐
  responds to the circumference of the CrossCutter cylinder (synchronous
  format).
  If "FormatRatio==5", the length of the product cut is five times the circum‐
  ference of the CrossCutter cylinder.
● The "CutAngle" input specifies the cutting area of the CrossCutter. In the
  cutting area, the CrossCutter either rotates with the material feed velocity
  or with a (selectable) correction motion.
● The "PendelumFactor" input specifies the maximum pendular motion of the
  CrossCutter axis in percent.
  This means that if "PendelumFactor==0%", the CrossCutter axis never
  rotates at a negative velocity (backwards).
  If "PendelumFactor==100%", the CrossCutter axis rotates to the border of
  the cutting area to minimize energy loss and the required acceleration.
  This provides special benefits in case of higher values for "FormatRatio". If
  "PendelumFactor==100%", the CrossCutter does not generally rotate up to
  the border of the cutting area since this is not always advantageous. The
  respective optimum utilization of the available area is always automatically
  calculated by the function block.
● The "CorrectionProfile" input allows different correction motions in the cut‐
  ting zone required for the respective use case.

   The following options are available:
   – "CorrectionProfile==CORR_PROFILE_NONE"
      (No correction: CrossCutter axis rotates with the master axis velocity)
   – "CorrectionProfile==CORR_PROFILE_OVERSPEED"
      (Constant overspeed of the CrossCutter axis in the cutting area)
   – "CorrectionProfile==CORR_PROFILE_COS_COMP"
      (Constant velocity vector in material direction, e. g. for guillotine cut‐
      ters)
   – "CorrectionProfile==CORR_PROFILE_PUSH_OUT"
      (PushOut of the material)
   – "CorrectionProfile==CORR_PROFILE_COS_COMP_AND_PUSH_OUT"
      (Constant velocity vector in material direction as well as simultaneous
      "PushOut", e.g. for guillotine cutters)
● The "Overspeed" input allows the exact setting of the overspeed in [%] in
   the cutting area if
   "CorrectionProfile==CORR_PROFILE_OVERSPEED"
   Thus, entering a value of 10 [%] increases the velocity of the CrossCutter
   axis in the cutting area by 10 % compared to the material velocity.
● The input "PushOut" parameterizes the "PushOut" correction
   The input is only processed if
   "CorrectionProfile==CORR_PROFILE_PUSH_OUT"
   or
   "CorrectionProfile==CORR_PROFILE_COS_COMP_AND_PUSH_OUT"
● The "Resolution" input allows the selection of the resolution of the cam
   tables used in three steps. Selecting a lower resolution saves calculation
   time, but reduces accuracy. High resolution increases the calculation time
   and the accuracy respectively.
The successful calculation of a profile is signaled via the "Done" output. The
parameters are written to the data arrays addressed by the specified array of
variable length. Subsequently, these parameters have to be written to a free
FlexProfile using the MB_WriteCrossCutProfile function block.

Typical output
The typical result of the CrossCutter computation comprises two types, for
example:
(if resolution:=RESOLUTION_HIGH)
                              Type 1                     Type 2
LawType[0]                    VELOCITY_IN_VELOCITY_LINEAR POINTS_TABLE_AUTO
LawType[1]                    POINTS_TABLE_AUTO          POINTS_TABLE_AUTO
LawType[2]                    VELOCITY_IN_VELOCITY_LINEAR POINTS_TABLE_AUTO
PointTable[0].NumberOfElements 0                         51
PointTable[1].NumberOfElements 1001                      1001
PointTable[2].NumberOfElements 0                         51
PointTable[0].PointTable      Empty                      51 points
PointTable[1].PointTable      1001 points                1001 points
PointTable[2].PointTable      Empty                      51 points

Effects of the format ratio on the maximum velocity of the CrossCutter axis in
the compensation range:

             Format ratio                 Ratio between the velocity of the
                                          slave axis and the velocity of the
                                                     master axis
                     1                                    1
                    0.8                                  1.5
                    0.6                                  2.2
                    0.4                                  3.7
                    0.2                                   8

### 8.3.3 MB_WriteCrossCutProfile

Brief description

The MB_WriteCrossCutProfile function block provides the following functions:
● Writing the point table from the PLC to the Data Layer node motion/cfg/
   functions/sync-motion/point-table/tables
● Sending payload of the FlexProfile with the parameters "Range", "Gain" and
   "LawType" in the Data Layer node Motion/axs/AxisName/cfg/functions/cou‐
   pling/sync-motion/flexprofile/profiles
The point table and the parameters can be generated from MB_CrossCutCalc‐
Type01 and saved in IN_OUT variables.
For more details refer to the documentation ⮫ "Motion App, Motion Runtime
Environment for ctrlX OS", Application Manual.
Define the name of the point table in advance and the point table is written to
the Data Layer at a rising edge at "Execute".
The FlexProfile checks whether the "AxisName" and "ProfileName" inputs are
valid. When writing and checking the FlexProfile is complete, the "Done"
output is set to TRUE. If "AxisName" is empty, writing the FlexProfile is
skipped. If "ProfileName" is empty, the function block automatically generates
a profile name, e.g. 0, 1,... and transfers it to the "TargetProfile" output.

Interface description

Table 55: Interface variables of the MB_WriteCrossCutProfile function block
                     Name                      Type                       Description
Input                Execute                   BOOL                       Starting the action at a
                                                                          rising edge
                     AxisName                  STRING                     Axis name to write the
                                                                          FlexProfile
                                                                          If the input is empty,
                                                                          writing the FlexProfile is
                                                                          skipped.

Name                     Type                           Description
ProfileName              STRING                         Name of the FlexProfile,
                                                        can be '0', '1', '2', '3' or ''
                                                        If the entry is empty, it
                                                        is automatically written to
                                                        the next running FlexPro‐
                                                        file.
Output              Done                     BOOL                           Processing completed
Active                   BOOL                           Processing active
Error                    BOOL                           Processing completed
                                                        with error
ErrorID                  ⮫ ERROR_CODE                   Error class
ErrorIdent               ⮫ ERROR_STRUCT                 Diagnostic description in
                                                        case of error
TargetProfile            STRING                         Display of the target Flex‐
                                                        Profile name
VAR_IN_OUT          RangeStartPos            ARRAY [*] OF LREAL             Array of the area (master
                                                        init positions), three ele‐
                                                        ments are required
Gain                     ARRAY [*] OF LREAL             Array of the gain (dis‐
                                                        tances) of the slave
                                                        axis, three elements are
                                                        required
LawType                  ARRAY [*] OF                   Array of step modes "Law‐
                         MB_STEP_MOTION_LAW             Type", three elements are
                                                        required
PointTable               ARRAY [*] OF                   Array of
                         MB_POINT_TABLE_DATA            MB_POINT_TABLE_DATA,
                                                        three elements are
                                                        required

 WriteTarget
 The following table shows the relation between the various inputs and out‐
 puts:
 Input                                 Output
 Axis name Profile       Point table   Target profile Name of the point table
           name          name                         in the Data Layer
 Slave1    (empty)       CrossCut_0    (Automatically CrossCut_0
                         CrossCut_1    generated)     CrossCut_1
                         CrossCut_2                   CrossCut_2
 Slave1        (empty)   (empty)       (Automatically CrossCut_Slave1_FP*_0
                                       generated)     CrossCut_Slave1_FP*_1
                                                      CrossCut_Slave1_FP*_2
 Slave1        ‘2’       CrossCut_A    ‘2’            CrossCut_A
                         CrossCut_B                   CrossCut_B
                         CrossCut_C                   CrossCut_C
 Slave1        ‘2’       ‘’            ‘2’            CrossCut_Slave1_FP2_0
                                                      CrossCut_Slave1_FP2_1
                                                      CrossCut_Slave1_FP2_2

Input                                   Output
‘’               (empty)   CrossCut_3   (Skip writing)   CrossCut_3
                           CrossCut_4                    CrossCut_4
                           CrossCut_5                    CrossCut_5
‘’               ‘2’       CrossCut_0   (Skip writing)   CrossCut_0
                           CrossCut_1                    CrossCut_1
                           CrossCut_2                    CrossCut_2
‘’               (empty)   ‘’           Errors           Errors
Explaining the point table name:
“CrossCut_” + “SlaveAxisName” + “_FP” + “FlexProfileName” + ” _” +
“TableIndex”

Automatically generated target profile "TargetProfile"
The "TargetProfile" output is generated automatically if the "ProfileName"
input is empty.
The rules are shown in the following table.
Every FlexProfile that is not LOCKED_FOR_RUN is treated as EMPTY.
(Example: VALID, EMPTY, INVALID...)
FlexProfile     Case 0           Case 1             Case 2           Case 3             Case 4
0               EMPTY            LOCKED_FOR_RUN     EMPTY            EMPTY              EMPTY
1               EMPTY            EMPTY              LOCKED_FOR_RUN   EMPTY              EMPTY
2               EMPTY            EMPTY              EMPTY            LOCKED_FOR_RUN     EMPTY
3               EMPTY            EMPTY              EMPTY            EMPTY              LOCKED_FOR_RUN
TargetProfile   ‘0’              ‘1’                ‘2’              ‘3’                ‘0’
