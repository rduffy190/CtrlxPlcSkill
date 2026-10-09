# 19 CXA_MotionInterface

## 19.1 Introduction and overview

General information
The PLC libraries CXA_MotionInterface, CXA_MotionInterfaceUser and the
respective programming template provide functions to control axes and kine‐
matics.
Alternatively to the individual functions of the PLC libraries CXA_Motion or
CXA_PLCopen, the MotionInterface is a ready program frame and an easy-to-
operate interface for the axis or kinematic functionality.
To use the library, install the app rexroth-motion.

Components of the MotionInterface
● CXA_MotionInterface.compiled-library:
  Basic library with the basic function blocks and basic structures
● CXA_MotionInterfaceUser.library:
  Open source library with extended function blocks, extended structures,
  programs and visualizations
  The global variables of the interfaces are also instantiated. The user can
  adapt and extend the interfaces.
● Programming template "MotionInterface":
  Includes the call of required programs and example code
  There are the following two variants of the template in the context menu
  of the “Application” node in the ctrlX PLC Engineering: "AxisInterface" and
  "KinematicInterface and AxisInterface"

AxisInterface
In the control structure, the AxisInterface includes control signals and param‐
eters for the various operation modes of the axes. In the status structure,
actual values, diagnostic information and acknowledgements are provided for
the operation modes.
The structures are provided as arrays. It allows FOR loops across all axes.
The axes are addressed via the index in the structures. The axis index is
either assigned automatically to the axis name or by the user (see ⮫ Chapter
Adjusting the assignment AxisName <>AxisIndex on page 507).
Table 382: Assignment: User interface to the AxisInterface data structure
User interface               Type                                 Description
arAxisCtrl_gb[ ]             TE_AXIS_CONTROL_TYPE01               Control structure, including command
                                                                  values and variables to activate the
                                                                  operation modes
arAxisStatus_gb[ ]           TE_AXIS_STATUS_TYPE01                Status structure including diagnostic
                                                                  information, acknowledgements for the
                                                                  operation modes, actual values and
                                                                  status bits

  KinematicInterface
In the control structure, the KinematicInterface includes control signals and
parameters for the various operation modes of the kinematics. In the status
structure, actual values, diagnostic information and acknowledgements are
provided for the operation modes.
The structures are provided as arrays It allows FOR loops across all kine‐
matics. The kinematics are addressed via the index in the structures. The
kinematic index is either assigned automatically to the kinematic name or by
the user (see ⮫ Chapter Adjusting the assignment KinematicName <>Kinemati‐
cIndex on page 554).
The KinematicInterface uses the AxisInterface internally. It is thus required to

call the AxisInterface as well.
Table 383: Assignment: User interface to the KinematicInterface data structure
User interface               Type                        Description
arKinCtrl_gb[ ]              TE_KINEMATICS_CON‐          Control structure, including command
                             TROL_TYPE01                 values and variables to activate the
                                                         operation modes
arKinStatus_gb[ ]            TE_KINE‐                    Status structure including diagnostic
                             MATICS_STATUS_TYPE01        information, acknowledgements for the
                                                         operation modes, actual values and
                                                         status bits

  IMC Interface
The IMC Interface (Interface-Motion-Control) includes control signals for the
app rexroth-motion in the control structure. Status bits and diagnostic infor‐
mation of the rexroth-motion app are provided in the status structure.
The AxisInterface and the KinematicInterface use the IMC Interface internally
to start the initialization when the “Running” state is reached.
The AxisInterface already calls the program MB_ImcInterface internally. An
additional call is only required if the IMC Interface is used without AxisInter‐
face.
Table 384: Assignment: User interface to the IMC Interface data structure
User interface               Type                        Description
ImcCtrl                      MB_IMC_CONTROL_TYPE01       Control structure to specify the Motion
                                                         mode and to clear errors
ImcStatus                    MB_IMC_STATUS_TYPE01        Status structure with the current Motion
                                                         mode and diagnostic information

## 19.2 MotionInterface - Initial configuration

  Before the functionality of the MotionInterface can be used initialize this
  MotionInterface first.
  The following steps activate the AxisInterface and the KinematicInterface in
  the ctrlX PLC Engineering.
  It is recommended to use the programming template "MotionInterface”. This
  template can be imported into the ctrlX PLC Engineering and used as style
  guide for new projects. When using either the template “AxisInterface” or
  “KinematicInterface and AxisInterface”, the handling of the AxisInterface and
  the KinematicInterface including all possible user extensions has been com‐
  pletely executably programmed.

  First steps when using the “MotionInterface” template:

1.   Create a new project in the ctrlX PLC Engineering or open an existing
project. Go to the context menu of the node and select the menu item
“Insert template” under “Logic 🠂 application”
Refer to Fig. 287
2.   Select the “MotionInterface“ tab and then the respective variant - either
“AxisInterface“ or “KinematicInterface and AxisInterface“.
   The additional tasks "MainTaskMotif" and "MotionTask" are inserted
into the task configuration when opening the MotionInterface.
The “MainTaskMotif” settings match the default settings of the “Main‐
Task” created when generating a project.
It is recommended to merge the calling of both tasks in the “MainTask”
and to delete “MainTaskMotif”, as it is not required anymore.
Refer to Fig. 288
3.   Log into and start the PLC application and test the function via the
visualizations "OverviewAxes" or "OverviewKinematics”.
AxisName<>AxisIndex or KinName<>KinIndex are assigned automatically
by default.
4.   Select the library CXA_MotionInterfaceUser in the library manager
and open the library parameters MOTIF_CONFIG. The arrays can be
adjusted to the number of your axes or kinematics. Select another con‐
figuration mode to define the assignment AxisName<>AxisIndex or Kin‐
Name<>KinIndex.
5.   Use arAxisCtrl_gb[ ], arAxisStatus_gb[ ], arKinCtrl_gb[ ], arKin‐
Status_gb[ ] to program your application. There are also demo programs
in the "MotionInterface" folder. Calling the demo programs in the Main‐
Task are not required for the function and can thus be removed.

## 19.3 AxisInterface

### 19.3.1 Introduction and overview

The AxisInterface pools and extends PLCopen motion function blocks and
provides an easy-to-operate interface for the drive functionality.
The AxisInterface includes control signals and parameters for the various
operation modes of the axes as well as the setting options for selected
process values.
Table 385: Program organization units of the AxisInterface in the CXA_MotionInterface library
Field of application (folder in the library CXA_MotionInterface)
POUs                                              Description
AxisInterface/POUs
⮫ Chapter MB_AxisInit on page 459                 Used to initialize the AxisInterface for a single
                                                  axis. The function block has to be called only
                                                  once upon program start or each time the mode
                                                  is switched from "Configuration" to "Running"
⮫ Chapter MB_AxisInterfaceBase on page 461        Configuration of the AxisInterface for a single
                                                  axis. The function block has to be called cycli‐
                                                  cally (in the Motion cycle or slower than the
                                                  Motion cycle) as long as the user is in the oper‐
                                                  ating mode
AxisInterface/DUTs

                               For information on the data structures, refer to
                               the ctrlX PLC Engineering library manager in
                               the CXA_MotionInterface library in the AxisInter‐
                               face/DUTs folder
AxisInterface/GlobalVariables
                               For information on the global variables, refer
                               to the ctrlX PLC Engineering library manager in
                               the CXA_MotionInterface library in the AxisInter‐
                               face/GlobalVariables folder
The AxisInterface is provided as programming template or as standalone inter‐
face for the axis functionality.
If it is used with the programming template "MotionInterface" as AxisInterface
or as "KinematicInterface and AxisInterface", the user does not have to deal
with instance calls of the function blocks in the project. This functionality is
completely integrated into the template - the user just needs to write a few
lines of code.
If the AxisInterface is used as standalone functionality, create the instances of
both function blocks for each axis.
Table 386: Program organization units of the AxisInterface in the CXA_MotionInterfaceUser library
Field of application (folder in the library CXA_MotionInterfaceUser)
POUs                                              Description
AxisInterfaceUser/POUs
TE_AxisInitAllAxes                                AxisInterface initialization for all axes. Calls the
                                                  ⮫ MB_AxisInit internally for each axis
TE_AxisInterface extended ⮫ MB_AxisInterface‐     The user can extend the AxisInterface for a
Base                                              single axis (⮫ AxisInterface - User extension).
                                                  The function block has to be called cyclically
                                                  (in the Motion cycle or slower than the Motion
                                                  cycle) as long as the user is in the operating
                                                  mode
TE_AxisInterfaceMainProg                          When the "Running" mode is reached, the main
                                                  program executes the initialization. After a suc‐
                                                  cessful initialization, TE_AxisInterface is called
                                                  for all axes
TE_GetAxisInterfaceIndex                          Provides the index of an axis using the axis
                                                  name
                                                  For more information, refer to the ctrlX
                                                  PLC Engineering library manager in the
                                                  CXA_MotionInterfaceUser library in the "AxisIn‐
                                                  terfaceUser/POUs" folder
AxisInterfaceUser/DUTs
                                                  For information on the data structures, refer to
                                                  the ctrlX PLC Engineering library manager in the
                                                  CXA_MotionInterfaceUser library in the AxisInter‐
                                                  faceUser/DUTs folder
AxisInterfaceUser/GlobalVariables
Global_AxisInterface                              The actual AxisInterface with the arrays arA‐
                                                  xisCtrl_gb and arAxisStatus_gb can be found
                                                  here. The other variables are used internally and
                                                  by visualizations.
                                                  Also refer to ⮫ Chapter 19.3.4 AxisInterface -
                                                  Global variables on page 492
AxisInterfaceUser/Visualizations

⮫ Chapter Introduction and overview                 Commission visualizations, e.g. to jog axes
on page 498
AxisInterfaceUser/_AxifDebug
If problems arise, use the POUs to record           For information on this debug feature, refer
the sequence of the Motion commands in this         to the ctrlX PLC Engineering library manager
folder.                                             in the library CXA_MotionInterfaceUser in the
                               folder AxisInterfaceUser/_AxifDebug. For a "How
                               To", refer to the documentation of the program
                               TE_AxIfDebugProg
AxisInterfaceUser/_Examples

PROGRAM Example_AxIfApplicationPart                 Example code to apply the AxisInterface. This
                               example code is also included in the program‐
                               ming template "KinematicInterface and AxisInter‐
                               face"
Utilities/ConfigFileRead
TE_ConfigFileRead                                   Auxiliary function block to analyze the JSON file
                               when MOTIF_CONFIG.CFG_MODE_AXS = FILE is
                               set. Internally used by TE_AxisInitAllAxes.

Project planning note/runtime requirement
The AxisInterface function block is called for each axis in the AxisInterface.
This call requires PLC runtime. This runtime varies depending on the axis type
and axis mode.

Table 387: Assignment: User interface to the AxisInterface data structure
User interface       Type                           Description
arAxisCtrl_gb[ ]     TE_AXIS_CONTROL_TYPE01         Control structure, including command values
                                                    and variables to activate operation modes
arAxisStatus_gb[ ] TE_AXIS_STATUS_TYPE01            Status structure including diagnostic informa‐
                                                    tion, acknowledgements for the operation
                                                    modes, actual values and status information on
                                                    the rexroth-motion app.

Use the AxisNo of the MB_AXISIF_REF structure as an index for the array, e.g.
arAxisCtrl_gb[MyVirtualAxis.AxisNo].Admin. etc.

EnableCyclicScanning
The element arAxisCtrl_gb[ ].Admin.Config.EnableCyclicScanning can control
the internal handling of certain command values.
If EnableCyclicScanning is set to TRUE, some command values of the
arAxisCtrl_gb[ ] structure are scanned cyclically and applied immediately
when a value changes.

EnableExtClearError
If the element arAxisCtrl_gb[ ].Admin.Config.EnableExtClearError is TRUE, this
means that error outputs are deleted and the selected operating mode is
restarted if the error is deleted from outside the AxisInterface. The default
value is FALSE.
If the last axis command was enabled via the MotionInterface and EnableExt‐
ClearError is set to FALSE, the PLCopenState error is cleared if the error was
cleared from outside the AxisInterface. However, the error status of the PLC
function also has to be reset via MotionInterface.
After resetting all errors, the selected operating mode is not restarted.
If the last axis command was enabled via MotionInterface and EnableExtClear‐
Error is TRUE, the selected operating mode is automatically restarted when
the error was fixed from outside the AxisInterface.
If the last axis command was not enabled via the MotionInterface, the
selected operating mode is not automatically restarted after fixing the error
irrespective of whether EnableExtClearError is set to FALSE or TRUE.

UpdateEveryInput
Data, which is not cyclically scanned, is also applied when a cyclically
scanned element changes if the UpdateEveryInput input was set.

Example:
The "Relative positioning" operation mode was started with the values shown
above before, Velocity = 10 and JerkAcc = 0.
To start the next positioning with a different acceleration, the input
PosMode.DynValues.JerkAcc is changed from 0 to 100. Then, the next "Dis‐
tance" is written.
The jerk is also applied when "Distance" is changed.

−   When activating an operation mode (.Admin._OpMode), all input data is
    read irrespective of the setting of the "EnableCyclicScanning" input
− If EnableCyclicScanning = TRUE, all input data highlighted in green is read
    cyclically. Thus, any value change is read immediately after activating an
    operation mode
− In contrast to that, all input data highlighted in blue is not scanned cycli‐
    cally. Thus, the values are only read if an operation mode is activated
− If UpdateEveryInput = TRUE, all input data highlighted in blue is also
    applied if one of the cyclically scanned elements of the operation mode
    is changed
− Data becomes consistent when EnableCyclicScanning (FALSE→Write
    data→TRUE) is used
For commissioning purposes, various visualizations are provided in the
library CXA_MotioninterfaceUser. They are based on the structural elements
described in this section.

AxisCyclicStatusData
The cyclic status data functionality retrieves axis data in the Data Layer RT on
request. The arAxisCtrl_gb[ ].Admin.Config.AxisCyclicStatusData element can
enable the cyclic status data functionality. The default value is TRUE.
Data can be available in the fields arAxisStatus_gb[].Data.DeviceStatus.xxx
and arAxisStatus_gb[].Diag.HasError / HasWarning.

Table 388: Elements of “arAxisStatus_gb[].Data.DeviceStatus.PlcOpenState”
DeviceStatus.PlcO‐ PLCopen state      Description
penState
0                  DISABLED           The axis is not supplied with power.
1                  STAND‐             Transient state when power supply
                   STILL_PENDING      was requested for the axis.
2                  STANDSTILL         The axis is powered and ready to
                                      receive motion commands.
3                  HOMING             The axis moves to its reference point.
4                  DIS‐               The axis is currently moving in accord‐
                   CRETE_MOTION       ance with a position command.
5                  CONTIN‐            The axis is currently controlled by the
                   UOUS_MOTION        velocity.
6                  COORDI‐            The axis is part of a kinematic system
                   NATED_MOTION       and can be controlled only via the kin‐
                                      ematics.
7                  SYNCHRON‐          The axis is assigned to another axis
                   IZED_MOTION        and follows it.
8                  STOPPING           Transitional state after a stop com‐
                                      mand (including "Drive Stop") has
                                      been issued and the axis has come to
                                      a stop.
9                  ABORTING           Transitional state after an abort com‐
                                      mand has been issued and the axis
                                      has been stopped.
10                 ERRORSTOP          Status after an error has occurred and
                                      the axis is shut down.
                                      In this state, the axis has to be reset
                                      in order to be activated again.

 DeviceStatus.PlcO‐ PLCopen state      Description
 penState
 11                 OUTDATED           If the Motion Core's status is not in
                                       state RUNNING, the axis object always
                                       returns this state.
 12                 GANTRY_SLAVE       The axis is the slave axis of a gantry
                                       coupling.
 13                 STOPPED            The axis is stopped, and the “Drive
                                       Halt” (AH) function is active.

arAxisStatus_gb[].Data.ActValues
The current position, velocity, torque and acceleration can be read via the
global variable arAxisStatus_gb[].Data.ActValues.

For arAxisStatus_gb[].Data.ActValues.Velocity, the actual value of the velocity
has to be assigned in the axis profile, otherwise the output value remains 0.
Only after "Encoder actual values ENC_1: Velocity" has been assigned to the
"Velocity" input in the axis profile, arAxisStatus_gb[].Data.ActValues.Velocity
outputs the value.
For the correct configuration in the axis profile, follow the steps described
in the Motion app, Application Manual, chapter ⮫ Window - "Axis profiles" ®
"Axis profile operating mode speed (SoE)".

The cycle time of the PLC depends on the number of configured axes. The
more axes are configured, the higher the cycle time of the PLC, see ⮫ Table
389 Measured values of the average cycle time on page 454.
Table 389: Measured values of the average cycle time
 Number of configured axes             Average cycle time (us)
 4                                     219
 6                                     281
 8                                     350

Changes and new information compared to the version for MLC/MLD?
● Parts of the event-controlled AxisInterface were applied (MB_AxisIn‐
  terfaceType11 function block). The structural elements are partially
  implemented as properties. The substructures are then implemented
  as function blocks instead of structures to use properties. The
  arAxisCtrl_gb[].Admin.mTriggerMoveCmd() method is implemented into a
  structure
● The operation mode selection arAxisCtrl_gb[].Admin._OpMode is not
  implemented as UNION anymore, but as properties. When controlling using
  bits (_OpModeBits), a multiple selection is not possible anymore
● Rarely used elements of arAxisCtrl_gb[].Admin were moved to

  arAxisCtrl_gb[].Admin.Config (see table below)
● Values of the type REAL are generally defined in the structures as LREAL
● There is no AxisData[] structure. For the current actual values and some
  status bits, go to arAxisStatus_gb[].Data .

The following list is intended to help porting MLC/MLD to ctrlX. New struc‐
tural elements added to the ctrlX platform are not taken into account.
Table 390: Required code changes when porting MLC/MLD (Search/Replace)
Code MLC/MLD                                     Replace by (ctrlX)

Control structure

arAxisCtrl_gb[].Admin._OpMode.en                 arAxisCtrl_gb[].Admin._OpMode1, 2

(Operation mode) ModeSyncPhase                   (Operation mode) ModeSyncPos

(Operation mode) ModeCyclicPosition              (Operation mode) ModeCyclicSetPoint

(Operation mode) ModeStopping                    (Operation mode) ModeStop2

(Operation mode) ModeInterrupted                 (Operation mode) ModeInterrupt2

arAxisCtrl_gb[].Admin._OpMode.b                  arAxisCtrl_gb[].Admin._OpModeBits1, 2, 3

arAxisCtrl_gb[].Admin.Axis                       arAxisCtrl_gb[].Admin.Config.Axis

arAxisCtrl_gb[].Admin.DiagNbrRefreshTime         arAxisCtrl_gb[].Admin.Config.DiagNbrRefreshTime

arAxisCtrl_gb[].Admin.StopDeceleration           arAxisCtrl_gb[].StopMode.StopDeceleration

arAxisCtrl_gb[].WaitTimePowerReset               Not required/integrated anymore

arAxisCtrl_gb[].Admin.EnableExtClearError        arAxisCtrl_gb[].Admin.Config.EnableExtClearError

arAxisCtrl_gb[].Admin.EnableCyclicScanning       arAxisCtrl_gb[].Admin.Config.EnableCyclicScanning

arAxisCtrl_gb[].Admin.UpdateEveryInput           arAxisCtrl_gb[].Admin.Config.UpdateEveryInput

arAxisCtrl_gb[].DriveInterruptReaction           Not required/integrated anymore

arAxisCtrl_gb[].Admin.PowerOn                    arAxisCtrl_gb[].Admin.Config.PowerOn

arAxisCtrl_gb[].ParameterLevel                   Not required/integrated anymore

arAxisCtrl_gb[].PosMode.Acceleration             arAxisCtrl_gb[].PosMode.DynValues.Acceleration

arAxisCtrl_gb[].PosMode.Deceleration             arAxisCtrl_gb[].PosMode.DynValues.Deceleration

arAxisCtrl_gb[].PosMode.Adjust                   Not required/integrated anymore

arAxisCtrl_gb[].VelMode.Acceleration             arAxisCtrl_gb[].VelMode. DynValues.Acceleration

arAxisCtrl_gb[].VelMode.Deceleration             arAxisCtrl_gb[].VelMode. DynValues.Deceleration

arAxisCtrl_gb[].VelMode.Adjust                   Not required/integrated anymore

arAxisCtrl_gb[].SyncMode.AdjCamShaftDistance     No integrated anymore

arAxisCtrl_gb[].SyncMode.AdjFineAdjust

arAxisCtrl_gb[].SyncMode.AdjPhaseOffset

arAxisCtrl_gb[].SyncMode.AngleOffset             arAxisCtrl_gb[].SyncMode.Offsets.AngleAdjust.Position

arAxisCtrl_gb[].SyncMode.CamShaftDistance        arAxisCtrl_gb[].SyncMode.CamIn.GainFactor

arAxisCtrl_gb[].SyncMode.CamTableID              arAxisCtrl_gb[].SyncMode.CamIn.PointTable4

Code MLC/MLD                                            Replace by (ctrlX)

arAxisCtrl_gb[].SyncMode.InputRevolution                arAxisCtrl_gb[].SyncMode.RatioNumerator5

arAxisCtrl_gb[].SyncMode.OutputRevolution               arAxisCtrl_gb[].SyncMode.RatioDenominator5

arAxisCtrl_gb[].SyncMode.PhaseOffset                    arAxisCtrl_gb[].SyncMode.Offsets.Slave.Position6

arAxisCtrl_gb[].SyncMode.PhaseOffsetVel                 arAxisCtrl_gb[].SyncMode.Offsets.Slave.Velocity

arAxisCtrl_gb[].SyncMode.PhaseOffsetAcc                 arAxisCtrl_gb[].SyncMode.Offsets.Slave.Acceleration

arAxisCtrl_gb[].SyncMode.PhaseShift                     arAxisCtrl_gb[].SyncMode.Offsets.Master.Position6

arAxisCtrl_gb[].SyncMode.PhaseShiftVel                  arAxisCtrl_gb[].SyncMode.Offsets.Master.Velocity

arAxisCtrl_gb[].SyncMode.PhaseShiftAcc                  arAxisCtrl_gb[].SyncMode.Offsets.Master.Acceleration

arAxisCtrl_gb[].SyncMode.StartMode                      arAxisCtrl_gb[].SyncMode.SyncMode7

arAxisCtrl_gb[].SyncMode.SyncDirection                  arAxisCtrl_gb[].SyncMode.SyncDirection8

arAxisCtrl_gb[].SyncMode.SyncVelocity                   arAxisCtrl_gb[].SyncMode.SyncDynValues.VelNeg

arAxisCtrl_gb[].SyncMode.SyncDynValues.VelPos

arAxisCtrl_gb[].SyncMode.SyncAcceleration               arAxisCtrl_gb[].SyncMode.SyncDynValues.Acc

arAxisCtrl_gb[].SyncMode.SyncDynValues.Dec

arAxisCtrl_gb[].SyncMode.Profile.ExecutionMode          arAxisCtrl_gb[].SyncMode.FlexProfile.ProfileExecutionMode7

arAxisCtrl_gb[].SyncMode.Profile.ProfileEntry           arAxisCtrl_gb[].SyncMode.FlexProfile.ProfileEntry

arAxisCtrl_gb[].SyncMode.Profile.RelativePositioning    Not required/integrated anymore

arAxisCtrl_gb[].SyncMode.Profile.MasterOffset           arAxisCtrl_gb[].SyncMode.FlexProfile.AngleAdjust

arAxisCtrl_gb[].SyncMode.Profile.SetSelection           arAxisCtrl_gb[].SyncMode.FlexProfile.Profile9

arAxisCtrl_gb[].SyncMode.Profile.SlaveOffset            arAxisCtrl_gb[].SyncMode.FlexProfile.SlaveAdjust

arAxisCtrl_gb[].SyncMode.Profile.SwitchingPosition      arAxisCtrl_gb[].SyncMode.FlexProfile.SwitchPosition

arAxisCtrl_gb[].SyncMode.Profile.UseSwitchingPosition   arAxisCtrl_gb[].SyncMode.FlexProfile.SwitchProfileOnPos

arAxisCtrl_gb[].SyncMode.Profile.SyncType               arAxisCtrl_gb[].SyncMode.SyncDirection7

arAxisCtrl_gb[].SetupMode.Enable                        arAxisCtrl_gb[].Admin._OpModeBits.MODE_SETUP

arAxisCtrl_gb[].SetupMode.Accel                         arAxisCtrl_gb[].SetupMode.DynValues.Acceleration

arAxisCtrl_gb[].SetupMode.DynValues.Deceleration

arAxisCtrl_gb[].SetupMode.Homing                        arAxisCtrl_gb[].SetupMode.Home

arAxisCtrl_gb[].SetupMode.JogPosControl                 arAxisCtrl_gb[].SetupMode.JogIncr9

Status structure

arAxisStatus_gb[].Admin.MODE_AH etc.                    arAxisStatus_gb[].Admin._OpModeAckBits. MODE_AH etc.

arAxisStatus_gb[].Admin.Name                            arAxisStatus_gb[].Admin.Name10

arAxisStatus_gb[].Admin.AbsRefCmdStatus                 arAxisStatus_gb[].Admin.SetAbsRefDone11

arAxisStatus_gb[].Admin.AxisFeatures.PARAM_LEVEL        No integrated anymore

arAxisStatus_gb[].Admin.AxisFeatures.PACK_PROFILE

arAxisStatus_gb[].Admin.AxisFeatures.LINK_AXIS

arAxisStatus_gb[].Admin.AxisFeatures.IPO_CONTROL

arAxisStatus_gb[].Admin.AxisFeatures.HYDRAULIc

arAxisStatus_gb[].Admin.AxisFeatures.ENCODER_AXIS

arAxisStatus_gb[].Admin.AxisFeatures.CONTROLLER_AXIS

arAxisStatus_gb[].Admin.InternalFlags                   No integrated anymore

arAxisStatus_gb[].Admin.ParamLevelAck                   No integrated anymore

arAxisStatus_gb[].PosMode.Adjust….                      No integrated anymore

arAxisStatus_gb[].VelMode.Adjust….                      No integrated anymore

Code MLC/MLD                                      Replace by (ctrlX)

arAxisStatus_gb[].SyncMode.AdjCamShaftDistance    No integrated anymore

arAxisStatus_gb[].SyncMode.AdjFineAdjust

arAxisStatus_gb[].SyncMode.AdjPhaseOffset

arAxisStatus_gb[].SyncMode.AngleOffsetDone        Currently not yet integrated

arAxisStatus_gb[].SyncMode.CamActiveID            arAxisStatus_gb[].Data.SyncMode.CamIn.ActiveCamTable4

arAxisStatus_gb[].SyncMode.PhasingMasterDone      Currently not yet integrated

arAxisStatus_gb[].SyncMode.PhasingSlaveDone       Currently not yet integrated

arAxisStatus_gb[].SyncMode.ProfileActiveSet       arAxisStatus_gb[].Data.SyncMode.FlexProfile.ActiveProfile9

arAxisStatus_gb[].SyncMode.SyncVelocityDone       Not integrated

arAxisStatus_gb[].SyncMode.SyncAccelerationDone

arAxisStatus_gb[].SetupMode.….                    No integrated anymore

arAxisStatus_gb[].Diag.Number                     arAxisStatus_gb[].Diag.NumberMain

arAxisStatus_gb[].Diag.NumberDetail

arAxisStatus_gb[].Diag.Warning                    No integrated anymore

AxisData[]12.Axis_Power                           arAxisStatus_gb[].Data.DeviceStatus13.PowerOn

AxisData[].Axis_CamTab_0                          arAxisCtrl_gb[].SyncMode.CamIn.PointTable14

AxisData[].Axis_CamTab_1

AxisData[].Axis_CamTab_2

AxisData[].Axis_CmdActive                         No integrated anymore

AxisData[].Axis_CyclicAnaChannelOpen              No integrated anymore

AxisData[].Axis_CyclicPosChannelOpen

AxisData[].Axis_CyclicTrqChannelOpen

AxisData[].Axis_CyclicVelChannelOpen

AxisData[].Axis_ErrInProgress                     No integrated anymore

AxisData[].Axis_Error                             arAxisStatus_gb[].Data.DeviceStatus.HasError

AxisData[].Axis_Homed                             arAxisStatus_gb[].Data.DeviceStatus.Homed15

AxisData[].Axis_InAb                              arAxisStatus_gb[].Data.DeviceStatus.PowerReady

AxisData[].Axis_Inbb                              No integrated anymore

AxisData[].Axis_InMasterPhaseOffset               No integrated anymore

AxisData[].Axis_InPosition                        arAxisStatus_gb[].Data.DeviceStatus.InPosition16

AxisData[].Axis_InSynchron                        No integrated anymore

AxisData[].Axis_InTorque                          arAxisStatus_gb[].Data.DeviceStatus.InTorque2

AxisData[].Axis_InVelocity                        arAxisStatus_gb[].Data.DeviceStatus.InVelocity2

AxisData[].Axis_OperationMode                     No integrated anymore

AxisData[].Axis_Power                             arAxisStatus_gb[].Data.DeviceStatus.Power

AxisData[].Axis_Standstill                        arAxisStatus_gb[].Data.DeviceStatus.Standstill2

AxisData[].Axis_Warnung                           No integrated anymore

AxisData[].ContinuousMotion                       arAxisStatus_gb[].Data.PLCOpenState.ContinuousMotion

AxisData[].ControlledMotion                       No integrated anymore

AxisData[].CoordinatedMotion

AxisData[].DiscreteMotion                         arAxisStatus_gb[].Data.PLCOpenState.DiscreteMotion

AxisData[].dwAxisCondition_i                      No integrated anymore

AxisData[].dwFlexProfileEventStatusBits_i         arAxisStatus_gb[].Data.SyncMode.FlexProfile.EventConditionStatus

AxisData[].dwMotionProfileStatusBits_i            No integrated anymore

Code MLC/MLD                             Replace by (ctrlX)

AxisData[].dwUserActualDataA_i           No integrated anymore17

AxisData[].dwUserActualDataB_i

AxisData[].dwUserActualDataC_i

AxisData[].dwUserActualDataD_i

AxisData[].dwUserActualDataE_i

AxisData[].dwUserActualDataF_i

AxisData[].ErrorStop                     arAxisStatus_gb[].Data.PLCOpenState.ErrorStop

AxisData[].FlexProfil_Set0_Checked       arAxisStatus_gb[].Data.SyncMode.FlexProfile.AccessState0 = Not UNVALIDATED

AxisData[].FlexProfil_Set0_OK            arAxisStatus_gb[].Data.SyncMode.FlexProfile.AccessState0 = VALID

AxisData[].FlexProfil_Set1_Checked       arAxisStatus_gb[].Data.SyncMode.FlexProfile.AccessState1 = Not UNVALIDATED

AxisData[].FlexProfil_Set1_OK            arAxisStatus_gb[].Data.SyncMode.FlexProfile.AccessState1 =VALID

AxisData[].FlexProfil_Set2_Checked       arAxisStatus_gb[].Data.SyncMode.FlexProfile.AccessState2 = Not UNVALIDATED

AxisData[].FlexProfil_Set2_OK            arAxisStatus_gb[].Data.SyncMode.FlexProfile.AccessState2 =VALID

AxisData[].FlexProfil_Set3_Checked       arAxisStatus_gb[].Data.SyncMode.FlexProfile.AccessState3 = Not UNVALIDATED

AxisData[].FlexProfil_Set3_OK            arAxisStatus_gb[].Data.SyncMode.FlexProfile.AccessState3 =VALID

AxisData[].FlexProfil_EvtSet0_Checked    arAxisStatus_gb[].Data.SyncMode.FlexProfile.AccessState0 = Not UNVALIDATED

AxisData[].FlexProfil_EvtSet0_Ok         arAxisStatus_gb[].Data.SyncMode.FlexProfile.AccessState0 =VALID

AxisData[].FlexProfil_EvtSet1_Checked    arAxisStatus_gb[].Data.SyncMode.FlexProfile.AccessState1 = Not UNVALIDATED

AxisData[].FlexProfil_EvtSet1_Ok         arAxisStatus_gb[].Data.SyncMode.FlexProfile.AccessState1 =VALID

AxisData[].FlexProfil_EvtSet2_Checked    arAxisStatus_gb[].Data.SyncMode.FlexProfile.AccessState2 = Not UNVALIDATED

AxisData[].FlexProfil_EvtSet2_Ok         arAxisStatus_gb[].Data.SyncMode.FlexProfile.AccessState2 =VALID

AxisData[].FlexProfil_EvtSet3_Checked    arAxisStatus_gb[].Data.SyncMode.FlexProfile.AccessState3 = Not UNVALIDATED

AxisData[].FlexProfil_EvtSet3_Ok         arAxisStatus_gb[].Data.SyncMode.FlexProfile.AccessState3 =VALID

AxisData[].FlexProfil_Active             arAxisStatus_gb[].Data.PLCOpenState.SynchronizedMotion AND arA‐
xisCtrl_gb[].Admin._OpModeBits.MODE_SYNC_FLEXPROFILE

AxisData[].FlexProfil_Sync               arAxisStatus _gb[].SyncMode.InSync

AxisData[].FlexProfil_WaitForSwitching   arAxisStatus _gb[].SyncMode.FlexProfile.WaitForSwitch.

AxisData[].Homing                        arAxisStatus_gb[].Data.PLCOpenState.Homing

AxisData[].PowerOn                       arAxisStatus_gb[].Data.DeviceStatus.Power

AxisData[].rActualPosition_i             arAxisStatus_gb[].Data.DeviceStatus.ActualPos

arAxisStatus_gb[].Data.ActValues.Position

AxisData[].rActualTorqueForce_i          arAxisStatus_gb[].Data.DeviceStatus.ActualTRQ

arAxisStatus_gb[].Data.ActValues.Torque

AxisData[].rActualVelocity_i _i          arAxisStatus_gb[].Data.DeviceStatus.ActualVel

arAxisStatus_gb[].Data.ActValues.Velocity

AxisData[].Standstill                    arAxisStatus_gb[].Data.PLCOpenState.Standstill

AxisData[].Stopping                      arAxisStatus_gb[].Data.PLCOpenState.Stopping

AxisData[].SynchronizedMotion            arAxisStatus_gb[].Data.PLCOpenState.SynchronizedMotion

AxisData[].wUserActualDataBitA_i         No integrated anymore18

AxisData[].wUserActualDataBitB_i

AxisData[].wUserActualDataBitC_i

AxisData[].wUserActualDataBitD_i

1    The values of the enumeration elements changed.

The operation modes ModeSyncProfile, ModeCyclicVelocity, ModeCyclicTorque, ModePosAbs2, ModeValveControl and ModePosSX
are no longer available.

2    Functional differences in the operation modes ModeAH, ModeStop, ModeInterrupt

3    Functional change, active bits are automatically reset by the system when a bit is selected

4    Data type for Cam/PointTable changed

5    Data type changed from UINT to DINT, which means that a reversal of direction can now also be configured

6    Functional change, in case of modulo configuration (master/slave), the corresponding offset in synchronicity is not corrected in the
modulo area

7    Names and functions of the enumeration components changed in some cases

8    Names of the enumeration components changed

9    Data type changed from UINT to STRING

10   String length reduced from 40 to 15

11   Functional difference, status is now binary instead of Command status

12   AxisData[] is identical to arAxisStatus_gb[].PtrAxisData^ and arAxisStatus_gb[].AxisData_HMI

13   For the DeviceStatus to be displayed, enable it via arAxisCtrl_gb[].Admin.Config.AxisCyclicStatus Data

14   Data type for PointTable is not identical

15   Status is currently (V 3.6) only updated when power is added

16   Status is generated in the control based on received actual values and status of the drive is not used

17   Has to be implemented via Data Layer Realtime Channel

18   Has to be implemented via Data Layer Realtime Channel

This list of code changes is incomplete. The program code has to be checked
while porting.

### 19.3.2 AxisInterface - Function blocks

MB_AxisInit
Brief description
The MB_AxisInit function block is used to initialize the AxisInterface
(⮫ Chapter MB_AxisInterfaceBase on page 461) for a single axis.
The function block has to be called only once upon program start or each
time the mode is switched from “Configuration” to “Running”. It is already
implemented into the template “KinematicInterface and AxisInterface“.

Interface description

Table 391: Interface variables of the MB_AxisInit function block
I/O type           Name                  Data type            Comment
VAR_INPUT          Execute               BOOL                 A positive edge at “Execute” starts the initi‐
                                                              alization
           AxisName                      STRING(15)           Axis name
           AxisIndex                     UINT                 Index in the AxisInterface structures
VAR_OUTPUT Done                          BOOL                 Set when the function block has completed
                                                              the processing
                   Active                BOOL                 Set when the function block is active (not
                                                              in idle mode)
                   Error                 BOOL                 It indicates that an error has occurred in
                                                              the function block instance
                   ErrorID               ⮫ ERROR_CODE         Short note on the error cause
                   ErrorIdent            ⮫ ERROR_STRUCT Detailed error information
VAR_IN_OUT         AdminCtrl             MB_AXIS_ADMIN‐ Axis management
                                         ISTRATION       connect arAxisCtrl_gb[i].Admin
                   AdminStatus           MB_AXIS_ADMIN_S Status of the axis management
                                         TATUS           connect arAxisStatus_gb[i].Admin
                   DataStatus            MB_AXIS_DATA    State information of the axis
                                                         connect arAxisStatus_gb[i].Data
                   DiagStatus            MB_AXIS_DIAG‐   Diagnostic information on the axis
                                         NOSIS           connect arAxisStatus_gb[i].Diag

        It is not possible to transfer the entire instance of the structures (e.g.
        arAxisCtrl_gb[ ]/arAxisStatus_gb[ ]) to the function block via an input.
        This allows to make special extensions to the existing code for the user appli‐
        cation. For more details, refer to the ⮫ AxisInterface - User extension.
        Thus,    the   required     elements     of   TE_AXIS_CONTROL_TYPE01       and
        TE_AXIS_STATUS_TYPE01 are transferred as separate inputs.

        Functional description
   The MB_AxisInit function block initializes the following structural elements
   with default values:
Table 392: Initialized structural elements of the MB_AxisInit function block
Structural element                                  Default
AdminCtrl._OpMode                                   ModeAB
AdminCtrl.Config.Axis.AxisNo                        AxisIndex
AdminCtrl.Config.Axis.AxisName                      AxisName
AdminStatus.Name                                    AxisName
AdminStatus.Active                                  TRUE for active axis
AdminStatus.AxisFeatures                            Depending on the axis type, refer to MB_AXIS_FEA‐
                                                    TURES in the library
DataStatus.Units                                    Units are only read out once during the initialization

        Troubleshooting
        The error codes of the internally used function block DL_ReadNode are trans‐
        ferred to read the Data Layer nodes.
        The function block can generate the following error codes:

Table 393: Error codes of the MB_AxisInit function block
ErrorID                      Additional1          Additional2               Description
INPUT_RANGE_ERROR            16#0A0F0107          16#0C230101               String “AxisName” is
                                                                            too short or too long
STATE_MACHINE_ERRO 16#0A0F0107                    16#0C230103               Errors while processing
R                                                                           the function block

MB_AxisInterfaceBase
Brief description
The MB_AxisInterfaceBase function block is used to configure the AxisInter‐

face for a single axis.
This function block has to be called cyclically (in the Motion cycle or slower
than the Motion cycle) when the user is in “Running” mode. It is already
implemented into the template “KinematicInterface and AxisInterface“.

Interface description

Table 394: Interface variables of the MB_AxisInterfaceBase function block
I/O type      Name                 Data type        Comment
VAR_INPUT     AdminCtrl            REFERENCE TO     Axis management,
                                   MB_AXIS_ADMIN‐ Connect arAxisCtrl_gb[i].Admin
                                   ISTRATION
              StopModeCtrl         REFERENCE TO     Stopping the axis,
                                   MB_AXIS_STOP_M Connect arAxisCtrl_gb[i].StopMode
                                   ODE
              PosModeCtrl          REFERENCE        Positioning modes,
                                   TO MB_AXIS_POSI‐ Connect arAxisCtrl_gb[i].PosMode
                                   TIONING
              CoordModeCtrl        REFERENCE TO     Kinematic mode,
                                   MB_AXIS_COORDI‐ Connect arAxisCtrl_gb[i].CoordMode
                                   NATED
              GantryModeCtrl       REFERENCE TO     Operation mode Gantry,
                                   MB_AXIS_GANTRY Connect arAxisCtrl_gb[i].GantryMode
              SyncModeCtrl         REFERENCE        Sync operation mode,
                                   TO MB_AXIS_SYN‐ Connect arAxisCtrl_gb[i].SyncModeCtrl
                                   CHRONISATION

I/O type           Name               Data type           Comment
VelModeCtrl        REFERENCE TO        Velocity operation mode,
             MB_AXIS_VELOCIT     Connect arAxisCtrl_gb[i].VelModeCtrl
             Y
TorqueModeCtrl     REFERENCE TO     Torque operation mode,
             MB_AXIS_TORQUE   Connect arAxisCtrl_gb[i].TorqueModeCtrl
AdminStatus        REFERENCE TO     Status of the axis management,
             MB_AXIS_ADMIN_S Connect arAxisStatus_gb[i].Admin
             TATUS
DataStatus         REFERENCE TO     Actual values of the axis status,
             MB_AXIS_DATA     Connect arAxisStatus_gb[i].Data
DiagStatus         REFERENCE        Status of the axis diagnostics,
             TO MB_AXIS_DIAG‐ Connect arAxisStatus_gb[i].Diag
             NOSIS
It is not possible to transfer the entire instance of the structures (e.g.
arAxisCtrl_gb[ ]/arAxisStatus_gb[ ]) to the function block via an input.
This allows to make special extensions to the existing code for the user appli‐
cation. For more details, refer to the ⮫ AxisInterface - User extension.
Thus,     the   required    elements    of   TE_AXIS_CONTROL_TYPE01           and
TE_AXIS_STATUS_TYPE01 are transferred as separate inputs.
To optimize the performance, the structures are connected to REFERENCE TO
as VAR_INPUT instead of as VAR_IN_OUT. Thus, the inputs only have to be
initialized once. Thus, if the function block is called cyclically, the structures
do not have to be transferred.
The function block checks the inputs of arAxisCtrl_gb[ ] and internally gener‐
ates the requested commands for the axis. The outputs of arAxisStatus_gb[ ]
are updated depending on the result of this command.
For example, the setting of the arAxisCtrl_gb[ ].Admin._OpMode from ModeAb
to ModePosAbs causes the following:
● Check the required states to activate a motion command such as "Axis in
  Ab"
● Enabling the function ML_AxsPower (if
  arAxisCtrl_gb.Admin.Config.PowerOn = TRUE)
● Wait for the acknowledgement that the power of the axis is added (AH/AF)
● Enabling the function ML_AxsPosAbs with the command values of PosMo‐
  deCtrl
● Acknowledging the arAxisStatus_gb[ ].Admin._OpModeAck to ModePosAbs
  (Bit MODE_POS_ABS)
● Scanning the values PosModeCtrl.Position,
  PosModeCtrl.Velocity, PosModeCtrl.DynValues.Acceleration and
  PosModeCtrl.DynValues.Deceleration and re-enabling the ML_AxsPosAbs in
  the case of modifications

Troubleshooting
The error codes of the internally used function blocks (e.g. DL_ReadNode
to read the Data Layer node) and the internally used functions (e.g. ML_Axs‐
Power) are transferred.
The function block can generate the following error codes:

Table 395: Error codes of the MB_AxisInterfaceBase function block
ErrorID                      Additional1        Additional2               Description
INPUT_RANGE_ERROR            16#0A0F0107        16#0C230110               At least one of the func‐
                                                                          tion block inputs is not
                                                                          initialized
DEVICE_ERROR       16#0A0F0107                  16#0C230111               Axis is in ErrorStop
STATE_MACHINE_ERRO 16#0A0F0107                  16#0C230113               Errors while processing
R                                                                         the function block
RESOURCE_ERROR     16#0A0F0107                  16#0C230115               Ctrl.Admin.PowerOn is
                                                                          set to FALSE, an

operation mode was
selected, but the drive
is not in AH/AF.
In this case, switch the
drive to AH/AF mode or
set the axis input
parameter “arA‐
xisCtrl_gb.Admin.Config
.PowerOn” to “TRUE.”
RESOURCE_ERROR               16#0A0F0107        16#0C230116               An operation mode was
selected in ModeAb
using the method
Ctrl.Admin.mTriggerMo‐
veCmd()
INPUT_RANGE_ERROR            16#0A0F0107        16#0C230117               In this variant, the func‐
tion block does not
support the OpMode
STATE_MACHINE_ERRO 16#0A0F0107                  16#0C230118               Errors while processing
R                                                                         the function block -
Power
STATE_MACHINE_ERRO 16#0A0F0107                  16#0C230119               Errors while processing
R                                                                         the function block -
Reset
STATE_MACHINE_ERRO 16#0A0F0107                  16#0C23011A               Errors while processing
R                                                                         the function block -
Stop

### 19.3.3 AxisInterface - Operation modes

Introduction and overview
There are three methods to activate an operation mode:
● Selection via ENUM values
   Assigning a value of the TYPE MB_AXIS_MODE
   arAxisCtrl_gb[ ].Admin._OpMode:
   arAxisCtrl_gb[].Admin._OpMode:= ModePosAbs;
   - or -
   arAxisCtrl_gb[].Admin._OpMode:= ModeAB;
● Using the bit access
   Setting a bit using the bit access functionality.
   arAxisCtrl_gb[].Admin._OpModeBits.MODE_POS_ABS:= TRUE;
   Deleting the “_OpMode” is also possible using the bit access functionality.
   arAxisCtrl_gb[].Admin._OpModeBits.MODE_POS_ABS := FALSE;
   MODE_AB is enabled by bit deletion.
   Also possible: arAxisCtrl_gb[].Admin._OpModeBits.MODE_AB :=
   TRUE;
● Using the Ctrl.Admin.mTriggerMoveCmd() method
   Also refer to "DemoBufferedAxisCommands” in the template "KinematicIn‐
   terface and AxisInterface”
   This method issues the command to the Motion firmware in this call. To
   ensure a proper function, the axis has to be enabled, e.g. query ModeAH
   and CmdDone.
   Call:
   arAxisCtrl_gb[uiAxisIndex].Admin.mTriggerMoveCmd(_OpMode:=
   ModePosAbs, Buffered:=TRUE, UserID:='my text');
   – Transfer parameter "_Opmode" = Value of TYPE MB_AXIS_MODE
   – Transfer parameter "Buffered" = TRUE: The previous command becomes
       active after the previous command has been completed
   – Transfer parameter "Buffered" = FALSE (Default): The previous command
       is aborted
   – Transfer parameter "UserID" = string (max. 25 bytes). Transferred as
       “Source” when calling the Motion commands. In case of errors, the
       source of the command can thus be identified.
   – Return value of the method: cmdID of the issued Motion command. If
       there is an error, 16#FFFFFFFFFFFFFFFF is returned.
The commands issued in the AxisInterface are not buffered by default. In con‐
trast, the commands issued in the KinematicInterface are buffered by default.
Buffered        commands        can     also     be     issued    with      the
arAxisCtrl_gb[uiAxisIndex].Admin.mTriggerMoveCmd() method. It is thus also
possible to issue multiple commands in one cycle (Buffered = TRUE).
Before an operation mode can be activated, assign values to every attribute
first. All attributes are provided with default values. Some are provided with
values unequal to zero while others are defined as 0. Due to the special
demands, a value has to be assigned to them.
Only attributes (e.g. position, velocity) that are used or whose default values
were changed have to be declared before the current operation mode is
changed.

The status acknowledgement (arAxisStatus_gb[].Admin.) for an operation
mode is implemented as follows.
Example:
−  The status acknowledgement only returns TRUE if the command to switch
   the axis to the absolute positioning mode was executed:
   arAxisStatus_gb[].Admin.MODE_POS_ABS
− The status acknowledgement is immediately reset when issuing a new
   command:
   arAxisStatus_gb[].Admin.CmdDone
   The positioning mode is activated:

   arAxisCtrl_gb[].Admin._OpMode.b.MODE_POS_ABS
   The output is set to TRUE if the drive switches to the positioning mode
   and starts to turn:
   arAxisStatus_gb[].Admin.MODE_POS_ABS
   If the drive reached the target position, the status acknowledgement is set:
   arAxisStatus_gb[].Admin.CmdDone
The input arAxisCtrl_gb.Admin.Config.PowerOn controls the internal use of
the ML_AxsPower (CXA_Motion library) in the AxisInterface:
● PowerOn = TRUE (default): The AxisInterface controls the ML_AxsPower.
   When an operation mode is enabled, first ML_AxsPower is called internally
   and only after a ready signal, the actual operation mode selected is ena‐
   bled. If switched off (ModeAb), ML_AxsPower is removed after the drive
   has been stopped
● PowerOn = FALSE: The AxisInterface does not control ML_AxsPower, the
   application program has to operate ML_AxsPower. If an operation mode is
   selected and ML_AxsPower was not previously controlled, the AxisInterface
   outputs the error 0A0F0107/0C230115
The following section describes the operation modes supported by the AxisIn‐
terface basic type and the attributes that can be assigned.
In the following, it is assumed that the default value of the “PowerOn” input
is TRUE.

Operation mode “Drive ready”
Activating this operation mode switches the drive to AB (“Drive ready”) and
switches off the torque.
The following command activates the operation mode:
arAxisCtrl_gb[].Admin._OpMode:= ModeAB;
or
arAxisCtrl_gb[].Admin._OpModeBits.MODE_AB:= TRUE;
The AxisInterface uses the functions ML_AxsPower and             ML_AxsAbort
(CXA_Motion library) for switching.

Table 396: Attributes of the operation mode “Drive ready”
Element           Name                          Type                     Default          Cycli‐
                                                                                          cally
                                                                                          scanned
arAxisCtrl[ ]     StopMode.StopDeceleration LREAL                        99.0             Yes
                  StopMode.StopJerk         LREAL                        0.0              No
arAxis‐           Admin._OpModeAck‐         BOOL                                          Omitted
Status_gb[]       Bits.MODE_AB

Operation mode “Drive Halt”
Activating this operation mode switches the drive to AH (“Drive Halt”) and
maintains the torque. The ModeAH mode interrupts running motion com‐
mands and causes a deceleration within the specified dynamic limits until the
axis reaches a velocity of zero and the drive switches to AH. While braking,
the PLCopen state of the axis is STOPPING. When the velocity reaches zero,
the axis goes into the PLCopen state STOPPED.
Once ModeAH is enabled, only a stop-related motion command is permitted
for the target axis. If the operating mode is switched to another mode, the
axis is first automatically switched from STOPPED to StandStill.

The following command activates the operation mode:
arAxisCtrl_gb[].Admin._OpMode := ModeAH;
or
arAxisCtrl_gb[].Admin._OpModeBits.MODE_AH := TRUE;
The AxisInterface uses the function ML_AxsStop (CXA_Motion library) for
switching.

Table 397: Attributes of the operation mode “Drive Halt”
Element            Name                         Type                     Standard         Cycli‐
                                                                                          cally
                                                                                          scanned
arAxisCtrl[ ]      StopMode.StopDeceleration LREAL                       99.0             Yes
                   StopMode.StopJerk         LREAL                       0.0              No
arAxis‐            Admin._OpModeAck‐         BOOL                                         Not
Status_gb[]        Bits.MODE_AH                                                           appli‐
                                                                                          cable
                   Admin.CmdDone                BOOL                                      Not
                                                                                          appli‐
                                                                                          cable

Operation mode "Setup"
Use the "Setup" mode to select whether an individual axis is homed or
whether the axes are moved in steps (specified distance) or continuously
within the specified dynamic limits.
During axis homing in "Setup" mode, the axis moves until the home posi‐
tion is reached. During the motion, the PLCopen status of the axis is set to
HOMING.
In axis jog mode in the "Setup" mode, the maximum traversing length is
always limited by the configured permissible ranges of the axis. If the current
position is beyond the configured, permissible axis ranges, the axis can move
towards the permitted range, but cannot move away from the range.
The following command activates the operation mode:
arAxisCtrl_gb[].Admin._OpMode := ModeSetup;
or
arAxisCtrl_gb[].Admin._OpModeBits. MODE_SETUP:= TRUE;
The following acknowledgement has to follow the operation mode command.
It returns the respective commanded operation mode or TRUE:
arAxisStatus_gb[].Admin._OpModeAck = MB_AXIS_MODE.ModeSetup;
arAxisStatus_gb[].Admin._OpModeAckBits.MODE_SETUP;
The AxisInterface uses the functions ML_AxsHoming, ML_AxsJogIncr and
ML_AxsJogCont (CXA_Motion library) for switching.

Table 398: Attributes of the "Setup" mode
Element              Name                                      Type            Standard Cyclically
                                                                                        scanned
arAxisCtrl_gb[ ]    SetupMode.Home                             BOOL                     No
                    SetupMode.HomeRefPos                       LREAL           0.0      No
                    SetupMode. JogPlus                         BOOL                     No
                    SetupMode. JogMinus                        BOOL                     No
                    SetupMode.Vel                              LREAL           10.0     No
                    SetupMode.DynValues.JerkAcc                LREAL           2.0      No
                    SetupMode.DynValues.JerkDec                LREAL           2.0      No

 SetupMode.JogIncr                          BOOL                     No
 SetupMode. StepWidth                       LREAL           1.0      No
arAxisStatus_gb [ ] Admin._OpModeAckBits. MODE_SETUP           BOOL                     Not appli‐
                                                                     cable

  If "SetupMode. JogPlus" or "SetupMode. JogMinus" are set to TRUE, jogging is
  triggered either in positive or negative direction. "SetupMode.Vel" and "Setup‐
  Mode.DynValues" are used as dynamic limits during jogging.
  If the "SetupMode.JogIncr" attribute is set to TRUE, the incremental jog mode
  is selected. Otherwise, the continuous jog mode is selected by default. The
  incremental jog mode uses "SetupMode. StepWidth" as increment.
  The "SetupMode.Home" attribute triggers the homing mode and uses "Setup‐
  Mode.HomeRefPos" as a parameter.

Operation mode “Absolute positioning”
  Activating this operation mode causes an absolute motion to a previously
  specified target position.
  The following command activates the operation mode:
  arAxisCtrl_gb[].Admin._OpMode := ModePosAbs;
  or
  arAxisCtrl_gb[].Admin._OpModeBits.MODE_POS_ABS := TRUE;
  The following acknowledgement has to follow the operation mode command.
  It returns TRUE, when the drive reached its target position:
  arAxisStatus_gb[].Admin.CmdDone
  The AxisInterface uses the functions ML_AxsPower and ML_AxsPosAbs
  (CXA_Motion library) for switching.

Table 399: Attributes of the operation mode “Absolute positioning”
Element            Name                         Type                     Default           Cycli‐
arAxisCtrl_gb[ ]   PosMode.Position           LREAL                      0.0               Yes
                   PosMode.Velocity           LREAL                      10.0              Yes
                   PosMode.DynValues.Acceler‐ LREAL                      10.0              Yes
                   ation
                   PosMode.DynValues.Deceler‐ LREAL                      10.0              Yes
                   ation
                   PosMode.DynValues.JerkAcc LREAL                       0.0               No
                   PosMode.DynValues.JerkDec LREAL                       0.0               No

Element            Name                         Type                     Default          Cycli‐
                                                                       cally
                                                                       scanned
arAxis‐            Admin._OpModeAck‐            BOOL                                      Omitted
Status_gb[ ]       Bits.MODE_POS_ABS
Admin.CmdDone                BOOL                                      Omitted

“Relative positioning” operation mode
   Activating this operation mode causes a relative motion to a previously speci‐
   fied target position by adding the PosMode.Distance to the current actual
   position.

  The following command activates the operation mode:
  arAxisCtrl_gb[].Admin._OpMode := ModePosRel;
  or
  arAxisCtrl_gb[].Admin._OpModeBits.MODE_POS_REL := TRUE;
  The following acknowledgement has to follow the operation mode command.
  It returns TRUE when the drive reached its target position:
  arAxisStatus_gb[].Admin.CmdDone
  The AxisInterface uses the functions ML_AxsPower and ML_AxsPosRel
  (CXA_Motion library) for switching.
  If the same ModePosRel motion needs to be repeated multiple times, mTrig‐
  gerMoveCmd can be used.

Table 400: Attributes of the operation mode “Relative positioning”
Element            Name                         Type                     Standard         Cycli‐
                                                                                          cally
                                                                                          scanned
arAxisCtrl_gb[ ]   PosMode.Distance           LREAL                      0.0              Yes
                   PosMode.Velocity           LREAL                      10.0             Yes
                   PosMode.DynValues.Acceler‐ LREAL                      10.0             Yes
                   ation
                   PosMode.DynValues.Deceler‐ LREAL                      10.0             Yes
                   ation
                   PosMode.DynValues.JerkAcc LREAL                       0.0              No
                   PosMode.DynValues.JerkDec LREAL                       0.0              No
arAxis‐            Admin._OpModeAck‐          BOOL                                        Not
Status_gb[ ]       Bits.MODE_POS_REL                                                      appli‐
                                                                                          cable
                   Admin.CmdDone                BOOL                                      Not
                                                                                          appli‐
                                                                                          cable

Operation modes “Additive positioning”
  Activating this operation mode causes a relative motion to a previously speci‐
  fied target position by adding the PosMode.Distance to the current target
  position.

  The following command activates the operation mode:
  arAxisCtrl_gb[].Admin._OpMode := ModePosAdd;
  or
  arAxisCtrl_gb[].Admin._OpModeBits.MODE_POS_ADD:= TRUE;

  The following acknowledgement has to follow the operation mode command.
  It returns TRUE when the drive reached its target position:
  arAxisStatus_gb[].Admin.CmdDone
  The AxisInterface uses the functions ML_AxsPower and ML_AxsPosAdd
  (CXA_Motion library) for switching.

Table 401: Attributes of the operation mode “Additive positioning”
Element            Name                        Type                     Default           Cycli‐
                                                                                          cally
                                                                                          scanned
arAxisCtrl_gb[ ]   PosMode.Distance           LREAL                     0.0               Yes

PosMode.Velocity           LREAL                     10.0              Yes
PosMode.DynValues.Acceler‐ LREAL                     10.0              Yes
ation
PosMode.DynValues.Deceler‐ LREAL                     10.0              Yes
ation
PosMode.DynValues.JerkAcc LREAL                      0.0               No
PosMode.DynValues.JerkDec LREAL                      0.0               No
arAxis‐            Admin._OpModeAck‐          BOOL                                        Omitted
Status_gb[ ]       Bits.MODE_POS_ADD
Admin.CmdDone              BOOL                                        Omitted

Operation mode “Robot Control”
  Activating this operation mode switches the corresponding drive into cyclic
  position control (drive-controlled). Furthermore, the corresponding axis is
  automatically grouped to a kinematics. The grouped axes can execute a coor‐
  dinated motion.
  The following command activates the operation mode:
  arAxisCtrl_gb[].Admin._OpMode := ModeCoordinated;
  or
  arAxisCtrl_gb[].Admin._OpModeBits.MODE_COORDINATED:= TRUE;
  This operation mode returns TRUE in the axis status structure:
  arAxisStatus_gb[].Admin._OpModeAckBits.MODE_COORDINATED;
  The AxisInterface uses the functions ML_AxsPower, ML_AxsAddToKin and
  ML_AxsRemoveFromKin (CXA_Motion library) for switching.

Table 402: Attributes of the operation mode “Robot Control”
Element            Name                        Type                     Default           Cycli‐
                                                                                          cally
                                                                                          scanned
arAxisCtrl_gb[ ]   CoordMode.KinName           STRING(15)                                 No

  Declaration:
  E.g.: Kin1: MB_AXESGROUPIF_REF :=(KinName:='Kin1',GroupNo:=0);

  Assignment:
  E.g. arAxisCtrl_gb[uiAxisIndex].CoordMode.KinName := Kin1.KinName;

Operation mode “Gantry”
Activating this operation mode switches the corresponding drive into cyclic
position control (drive-controlled). Furthermore, the corresponding axis is
automatically coupled to a Gantry master. The axis follows the Gantry master
in the PLCopen state SYNCHRONIZED_MOTION.
This operation mode can only be enabled and disabled if the gantry master is
in the PLCopen status “StandStill”, i.e. either ModeAH or ModeExternalFB is
selected for the gantry master.
The following command activates the operation mode:
arAxisCtrl_gb[].Admin._OpMode := ModeGantry
or
arAxisCtrl_gb[].Admin._OpModeBits.MODE_GANTRY:= TRUE;
This operation mode returns TRUE in the axis status structure:
arAxisStatus_gb[].Admin._OpModeAckBits.MODE_GANTRY;
The AxisInterface uses the functions ML_AxsPower, ML_AxsAddToGantry and
ML_AxsRemoveFromGantry (CXA_Motion library) for switching.

Table 403: Attributes of the operation mode “Gantry”
Element            Name                         Type                   Default          Cycli‐
                                                                                        cally
                                                                                        scanned
arAxisCtrl_gb[ ]   GantryMode.Master            AXIS_REF                                No

Declaration:
E.g.: Master1: AXIS_REF :=(AxisName:='Axis1');

Assignment:
e.g. arAxisCtrl_gb[uiAxisIndex].GantryMode.Master := Master1;

Operation mode “Interrupt"
When enabling this operation in DISCRETE_MOTION, the current command
is interrupted and the axis is stopped with the configured limit values. The
PLCopen state of the axis remains in the DISCRETE_MOTION state until the
interruption is canceled with ModeContinue. Use ModeContinue to continue
the interrupted command and other commands.

If the operation mode is changed from ModeAb to ModeInterrupt, the AxisIn‐
terface switches the drive to AH.
The following command activates the operation mode:
arAxisCtrl_gb[].Admin._OpMode := ModeInterrupt;
or
arAxisCtrl_gb[].Admin._OpModeBits.MODE_INTERRUPT:= TRUE;
The AxisInterface uses the function ML_AxsInterrupt (CXA_Motion library) for
switching.

Table 404: Attributes of the “Interrupt” mode
Element            Name                                    Type        Default        Cyclically
                                                                                      scanned
arAxis‐            Admin._OpModeAckBits.MODE_INTER‐        BOOL                       Omitted
Status_gb[ ]       RUPT
                   Admin.CmdDone                           BOOL                       Omitted

Operation mode “Continue”
When activating this operation mode, an interruption is canceled with ModeIn‐
terrupt.
If ModeCoordInterrupt is selected, an error is issued if there was an interrup‐
tion before.
The following command activates the operation mode:
arAxisCtrl_gb[].Admin._OpMode := ModeContinue;
or
arAxisCtrl_gb[].Admin._OpModeBits.MODE_CONTINUE:= TRUE;
The AxisInterface uses the function ML_AxsContinue (CXA_Motion library) for

switching.

Table 405: Attributes of the operation mode “Continue”
Element            Name                                Type             Default        Cyclically
                                                                                       scanned
arAxis‐            Admin._OpModeAck‐                   BOOL                            Omitted
Status_gb[ ]       Bits.MODE_CONTINUE
                   Admin.CmdDone                       BOOL                            Omitted
                     The Admin.CmdDone output shows that the ModeContinue command was
                     issued successfully. Admin.CmdDone cannot be used to check whether the
                     previously interrupted command was completed successfully, as the output is
                     already TRUE.
                     The interrupted command is completed if arAxisStatus_gb[].Admin.Active‐
                     CmdStatus = 'DONE';.

Operation mode "AxsHoming"
Activating this operation mode switches the axis to the operating mode
"AxsHoming". The axis moves until the homed position is reached. During the
motion, the PLCOpen status of the axis is set to HOMING.
The following command activates the operation mode:
arAxisCtrl_gb[].Admin._OpMode := ModeHoming;
or
arAxisCtrl_gb[].Admin._OpModeBits.MODE_AXS_HOMING;
The following acknowledgement has to follow the operation mode command.
It returns the respective commanded operation mode or TRUE if the drive
reached its target position:
arAxisStatus_gb[].Admin._OpModeAck = MB_AXIS_MODE.ModeHoming;
arAxisStatus_gb[].Admin._OpModeAckBits.MODE_AXS_HOMING;
arAxisStatus_gb[].Admin.CmdDone;
The AxisInterface uses the functions ML_AxsHoming and ML_GetCmdState
(CXA_Motion library) for switching.

Table 406: Attributes of the “AxsHoming” mode
Element            Name                                Type             Standard       Cyclically
                                                                                       scanned
arAxisCtrl_gb[]    PosMode.HomingNewRefPos             LREAL        0                  No
arAxis‐            Admin._OpModeAck                    MB_AXIS_MODE ModeAB             Not appli‐
Status_gb[]                                                                            cable
                   Admin._OpModeAck‐                   BOOL                            Not appli‐
                   Bits.MODE_AXS_HOMING                                                cable

Element            Name                                Type              Standard       Cyclically
                                                                     scanned
Admin.CmdDone                       BOOL                             Not appli‐
                                                                     cable

Operation mode "MoveVelocity"
  Activating this operation mode switches the axis to the velocity mode.
  The axis travels constantly with the target velocity. During the motion, the
  PLCOpen status of the axis is set to CONTINUOUS_MOTION.
  The following command activates the operation mode:
  arAxisCtrl_gb[].Admin._OpMode := MB_AXIS_MODE.ModeVel;
  or
  arAxisCtrl_gb[].Admin._OpModeBits.MODE_AXS_VELOCITY ;
  The following acknowledgement has to follow the operation mode command.
  It returns the respective commanded operation mode or TRUE:
  arAxisStatus_gb[].Admin._OpModeAck = MB_AXIS_MODE.ModeVel;
  arAxisStatus_gb[].Admin._OpModeAckBits.MODE_AXS_VELOCITY;
  arAxisStatus_gb[].Admin.CmdDone;
  The AxisInterface uses the functions ML_AxsVelocity and ML_GetCmdState
  (CXA_Motion library) for switching.

Table 407: Attributes of the “MoveVelocity” mode
Element            Name                               Type             Standard        Cyclically
                                                                                       scanned
arAxisCtrl_gb   VelMode.Velocity                      LREAL        0                   Yes
                VelMode.DriveVelControl               BOOL         FALSE               No
                VelMode.DynValues.Acceleration        LREAL        2                   Yes
                VelMode.DynValues.Deceleration        LREAL        2                   Yes
                VelMode.DynValues.JerkAcc             LREAL        0                   No
                VelMode.DynValues.JerkDec             LREAL        0                   No
arAxisStatus_gb Admin._OpModeAck                      MB_AXIS_MODE ModeAB              Not appli‐
                                                                                       cable
                   Admin._OpModeAck‐                  BOOL             FALSE           Not appli‐
                   Bits.MODE_AXS_VELOCITY                                              cable
                   Data.VelMode.InVel                 BOOL             FALSE           Not appli‐
                                                                                       cable
                   Admin.CmdDone                      BOOL             FALSE           Not appli‐
                                                                                       cable
                   Data.PLCOpenState.Continuous‐      BOOL             FALSE           Not appli‐
                   Motion                                                              cable

Operation mode "ModeStop"
  Enabling this operation mode cancels the current axis motion. During the
  deceleration, the PLCOpen status of the axis is set to ABORTING.
  As soon as the axis reaches a velocity of zero, the PLCopen state of the axis is
  switched to StandStill, i.e. a PLCopen function block that is called outside the
  AxisInterface is accepted and the AxisInterface reports ModeExternalFB.
  The following command activates the operation mode:
  arAxisCtrl_gb[].Admin._OpMode := MB_AXIS_MODE.ModeStop;
  or

   arAxisCtrl_gb[].Admin._OpModeBits.MODE_AXS_STOP
   The following acknowledgement has to follow the operation mode command.
   It returns the respective commanded operation mode or TRUE:
   arAxisStatus_gb[].Admin._OpModeAck = MB_AXIS_MODE. ModeStop;
   arAxisStatus_gb[].Admin._OpModeAckBits.MODE_AXS_STOP;
   arAxisStatus_gb[].Admin.CmdDone;
   The AxisInterface uses the functions ML_AxsAbort and ML_GetCmdState
   (CXA_Motion library) for switching.

Table 408: Attributes of the “ModeStop” mode

Element           Name                               Type             Standard       Cyclically
                                                                   scanned
arAxisCtrl_gb[]   StopMode.StopDeceleration          LREAL        0                  Yes
StopMode.StopJerk                  LREAL        0                  No
arAxis‐           Admin._OpModeAck                   MB_AXIS_MODE ModeAB             Not appli‐
Status_gb[]                                                                          cable
Admin._OpModeAck‐                  BOOL                            Not appli‐
Bits.MODE_AXS_STOP                                                 cable
Admin.CmdDone                      BOOL                            Not appli‐
                                                                   cable

Operation mode "ModeFixedStop"
   Activating this operation mode switches the axis to ModeFixedStop. The com‐
   mand positions an axis absolutely to the commanded position in a limited
   force value.
   The following command activates the operation mode:
   arAxisCtrl_gb[].Admin._OpMode := MB_AXIS_MODE. ModeFixedStop;
   or
   arAxisCtrl_gb[].Admin._OpModeBits. MODE_FIXED_STOP
   The following acknowledgement has to follow the operation mode command.
   It returns the respective commanded operation mode or TRUE:
   arAxisStatus_gb[].Admin._OpModeAck                =         MB_AXIS_MODE.
   ModeFixedStop;
   arAxisStatus_gb[].Admin._OpModeAckBits. MODE_FIXED_STOP;
   arAxisStatus_gb[].Admin.CmdDone;
   The AxisInterface uses the functions ML_AxsFixedStop, ML_AxsResetFixedStop
   and ML_GetCmdState (CXA_Motion library) for switching.

Table 409: Attributes of the “ModeFixedStop” mode
Element           Name                               Type             Standard       Cyclically
                                                                                     scanned
arAxisCtrl_gb[]   PosMode.Position                   LREAL            0              No
                  PosMode.Velocity                   LREAL            0              No
                  PosMode.MaxTorque                  LREAL            0              No
                  PosMode.DynValues.Velocity         LREAL            0              No
                  PosMode.DynValues.Acceleration     LREAL            2              No
                  PosMode.DynValues.Deceleration     LREAL            2              No
                  PosMode.DynValues.JerkAcc          LREAL            0              No
                  PosMode.DynValues.JerkDec          LREAL            0              No

Element            Name                              Type            Standard       Cyclically
                                                                 scanned
arAxis‐            Admin._OpModeAck                  MB_AXIS_MODE ModeAB            Not appli‐
Status_gb[]                                                                         cable
Admin._OpModeAck‐                 BOOL                           Not appli‐
Bits.MODE_FIXED_STOP                                             cable
Admin.CmdDone                     BOOL                           Not appli‐
                                                                 cable

Operation mode "ModeCyclicSetPoint"
  Enabling this operation mode switches to the ModeCyclicSetPoint. The com‐
  mand sends the command value directly to traverse the axis cyclically.
  The following command activates the operation mode:
  arAxisCtrl_gb[].Admin._OpMode                                            :=
  MB_AXIS_MODE.ModeCyclicSetPoint
  or
  arAxisCtrl_gb[].Admin._OpModeBits.MODE_CYCLIC_SET_POINT
  The following acknowledgement has to follow the operation mode command.
  It returns the respective commanded operation mode or TRUE:
  arAxisStatus_gb[].Admin._OpModeAck               =          MB_AXIS_MODE.
  ModeCyclicSetPoint;
  arAxisStatus_gb[].Admin._OpModeAckBits.MODE_CYCLIC_SET_POINT;
  arAxisStatus_gb[].Admin.CmdDone;
  The AxisInterface uses the functions ML_AxsCyclicSetPoint, ML_SetCyclicSet‐
  Point and ML_GetCmdState (CXA_Motion library) for switching.

Table 410: Attributes of the “ModeCyclicSetPoint” mode
Element            Name                              Type            Standard       Cyclically
                                                                                    scanned
arAxisCtrl_gb[]    PosMode.CyclicSetPointValue       LREAL        0                 No
arAxis‐            Admin._OpModeAck                  MB_AXIS_MODE ModeAB            Not appli‐
Status_gb[]                                                                         cable
                   Admin._OpModeAck‐                 BOOL                           Not appli‐
                   Bits.MODE_CYCLIC_SET_POINT                                       cable
                   Admin.CmdDone                     BOOL                           Not appli‐
                                                                                    cable

"ModeSyncPos" operation mode
After enabling this operation mode, the corresponding axis is automatically
coupled to a master axis. The slave axis is set to the SYNCHRONIZED_MOTION
status.
Use the following command to enable the operation mode:
  arAxisCtrl_gb[].Admin._OpModeBits.MODE_SYNC_POS :=TRUE;
  or
  arAxisCtrl_gb[].Admin._OpMode := MB_AXIS_MODE.ModeSyncPos;
  This operation mode provides an acknowledgement of the operation mode or
  "TRUE" in the status structure of the axis:
  IF             arAxisStatus_gb[].Admin._OpModeAck                           =
  MB_AXIS_MODE.ModeSyncPos THEN
  //user code
  END_IF

or
arAxisStatus_gb[].Admin._OpModeAckBits;
The AxisInterface uses the function ML_AxsGearInPosEx (CXA_Motion library)
to implement the function "GearInPos" in the synchronized motion type "Mod‐
eSyncPos". The "Synchronized Motion" license is required for this operation
mode.
If the cyclically scanned parameter (e.g. SyncMode.RatioNumerator) is
changed, it is applied to the current or next cycle. If the non-cyclically
scanned parameter is changed, it is applied to the next (re-)trigger of the
opMode.

Table 411: Attributes of the "ModeFixedStop" operation mode
Element        Name             Type           Standard       Cyclically
                                                              scanned
arA‐            SyncDyn‐        LREAL          0.0            No
xisCtrl_gb[].Sy Values.Acc
ncMode          SyncDyn‐        LREAL          0.0            No
                Values.Dec
                SyncDyn‐        LREAL          0.0            No
                Values.JrkAcc
                SyncDyn‐        LREAL          0.0            No
                Values.JrkDec
                SyncDyn‐        LREAL          0.0            No
                Values.VelNeg
                SyncDyn‐        LREAL          0.0            No
                Values.VelPos
                Master.Axis‐    STRING（15） ‘’                 Yes
                Name
                SyncSource      ⮫ ML_Syn‐      SYNC_SET‐      Yes
                                cSource        POINT
               SyncMode         ⮫ ML_Syn‐      SYNC_RELA‐     No
                                cMode          TIVE
               SyncDirection ⮫ ML_Dyn‐         SYNC_SHORTE Yes
                               SyncDirection   ST_PATH
               RatioDenomi‐ DINT               1              Yes
               nator
               RatioNumer‐     DINT            1              Yes
               ator
               FineAdjust      LREAL           0.0            No
               BufferMode      BOOL            FALSE          No
               Off‐            LREAL           0.0            Yes
               sets.Master.Po
               sition
               Off‐            LREAL           0.0            Yes
               sets.Master.Vel
               ocity
               Off‐            LREAL           0.0            Yes
               sets.Master.Ac
               celeration
               Off‐            LREAL           0.0            Yes
               sets.Slave.Posi
               tion

Element      Name         Type         Standard      Cyclically
                                        scanned
Offsets.Slave. LREAL       0.0          Yes
Velocity
Offsets.Slave. LREAL       0.0         Yes
Acceleration
Proc‐           LREAL      0.0         Yes
essCtrl.Master.
Offset
Proc‐           LREAL      0.0         Yes
essCtrl.Master.
TConstant
Proc‐           LREAL      0.0         Yes
essCtrl.Slave.
Offset
Proc‐           LREAL      0.0         Yes
essCtrl.Slave.T
Constant
Proc‐           LREAL      0.0         Yes
essCtrl.FineAd
just
Gear‐           LREAL      0.0         No
InPos.Master‐
StartDist
Gear‐           LREAL      0.0         No
InPos.Master‐
SyncPos
arAxis‐      Admin._OpMo‐ MB_AXIS_MOD ModeAB        Not applicable
Status_gb    deAck           E
Admin._OpMo‐ BOOL          FALSE       Not applicable
deAckBits
Data.Syn‐       LREAL      0.0         Not applicable
cMode.Actua‐
lOffset
Data.Syn‐       BOOL       FALSE       Not applicable
cMode.InSync
Data.Syn‐       LREAL      0.0         Not applicable
cMode.Offset‐
ToTarget
Data.Syn‐       ML_SyncMo‐ NO_SYNC_MOT Not applicable
cMode.Syn‐      tionState  ION
cState
Data.PLCOpen BOOL          FALSE       Not applicable
.Synchronized‐
Motion
Data. ActSyn‐ BOOL         FALSE       Not applicable
cOffsets.
Master.Done
Data. ActSyn‐ LREAL        0.0         Not applicable
cOffsets.
Master.Posi‐
tion

Element        Name             Type         Standard        Cyclically
                                                             scanned
               Data. ActSyn‐ LREAL           0.0             Not applicable
               cOffsets.
               Master.Remain
               Time
               Data. ActSyn‐ BOOL            FALSE           Not applicable
               cOffsets.
               Slave.Done
               Data. ActSyn‐ LREAL           0.0             Not applicable
               cOffsets.

               Slave.Position
               Data. ActSyn‐ LREAL           0.0             Not applicable
               cOffsets.
               Slave.Remain‐
               Time

    "ModeSyncVel" operation mode
After enabling this operation mode, the corresponding axis is automatically
coupled to a master axis. The slave axis is set to the SYNCHRONIZED_MOTION
status.
Use the following command to enable the operation mode:
arAxisCtrl_gb[].Admin._OpModeBits.MODE_SYNC_VEL :=TRUE;
or
arAxisCtrl_gb[].Admin._OpMode := MB_AXIS_MODE.ModeSyncVel;
This operation mode provides an acknowledgement of the operation mode or
"TRUE" in the status structure of the axis:
IF             arAxisStatus_gb[].Admin._OpModeAck                          =
MB_AXIS_MODE.ModeSyncVel THEN
//user code
END_IF
or
arAxisStatus_gb[].Admin._OpModeAckBits;
The AxisInterface uses the function ML_AxsGearInVelEx (CXA_Motion library)
to implement the function "GearInVel" in the synchronized motion type "Mod‐
eSyncVel". The "Synchronized Motion" license is required for this operation
mode.

Table 412: Attributes of the "ModeSyncVel" operation mode
Element        Name             Type         Standard        Cyclically
                                                             scanned
arA‐            SyncDyn‐        LREAL        0.0             No
xisCtrl_gb[].Sy Values.Acc
ncMode          SyncDyn‐        LREAL        0.0             No
                Values.Dec
                SyncDyn‐        LREAL        0.0             No
                Values.JrkAcc
                SyncDyn‐        LREAL        0.0             No
                Values.JrkDec
                SyncDyn‐        LREAL        0.0             No
                Values.VelNeg

Element      Name         Type         Standard     Cyclically
                                       scanned
SyncDyn‐        LREAL      0.0         No
Values.VelPos
Master.Axis‐    STRING（15） ‘’          Yes
Name
SyncSource      ML_Syn‐    SYNC_SET‐   Yes
                cSource    POINT
RatioDenomi‐ DINT          1           Yes
nator
RatioNumer‐     DINT       1           Yes
ator
FineAdjust      LREAL      0.0         Yes
BufferMode      BOOL       FALSE       No
Off‐            LREAL      0.0         Yes
sets.Master.Po
sition
Off‐            LREAL      0.0         Yes
sets.Master.Vel
ocity
Off‐            LREAL      0.0         Yes
sets.Master.Ac
celeration
Off‐            LREAL      0.0         Yes
sets.Slave.Velo
city
Offsets.Slave. LREAL       0.0         Yes
Acceleration
Proc‐           LREAL      0.0         Yes
essCtrl.Master.
Offset
Proc‐           LREAL      0.0         Yes
essCtrl.Master.
TConstant
Proc‐           LREAL      0.0         Yes
essCtrl.Slave.
Offset
Proc‐           LREAL      0.0         Yes
essCtrl.FineAd
just
arAxis‐      Admin._OpMo‐ MB_AXIS_MOD ModeAB        Not applicable
Status_gb    deAck           E
Admin._OpMo‐ BOOL          FALSE       Not applicable
deAckBits
Data.Syn‐       LREAL      0.0         Not applicable
cMode.Actua‐
lOffset
Data.Syn‐       BOOL       FALSE       Not applicable
cMode.InSync
Data.Syn‐       LREAL      0.0         Not applicable
cMode.Offset‐
ToTarget

Element        Name            Type           Standard    Cyclically
                                                          scanned
               Data.Syn‐      ML_SyncMo‐      NO_SYNC_MOT Not applicable
               cMode.Syn‐     tionState       ION
               cState
               Data.PLCOpen BOOL              FALSE           Not applicable
               .Synchronized‐
               Motion
               Data. ActSyn‐ BOOL             FALSE           Not applicable
               cOffsets.
               Master.Done

               Data. ActSyn‐ LREAL            0.0             Not applicable
               cOffsets.
               Master.Posi‐
               tion
               Data. ActSyn‐ LREAL            0.0             Not applicable
               cOffsets.
               Master.Remain
               Time
               Data. ActSyn‐ BOOL             FALSE           Not applicable
               cOffsets.
               Slave.Done
               Data. ActSyn‐ LREAL            0.0             Not applicable
               cOffsets.
               Slave.Velocity

    "ModeFlexProfile" operation mode
This command sets the axis related to a master axis via electronic cams
or profiles. All profiles of the axis have to be configured in the ctrlX Data
Layer. After enabling this operation mode, the respective axis is automati‐
cally coupled to a master axis. The slave axis is switched to the SYNCHRON‐
IZED_MOTION state.
Use the following command to enable the operation mode:
arAxisCtrl_gb[].Admin._OpMode := MB_AXIS_MODE.FlexProfile ;
//OR
arAxisCtrl_gb[].Admin._OpModeBits.MODE_SYNC_FlexProfile :=TRUE;
This operation mode provides an acknowledgement of the operation mode or
"TRUE" in the status structure of the axis:
IF             arAxisStatus_gb[].Admin._OpModeAck                           =
MB_AXIS_MODE.ModeFlexProfile THEN
//user code
END_IF
or
arAxisStatus_gb[].Admin._OpModeAckBits.MODE_SYNC_FlexProfile;
The AxisInterface uses the function ML_AxsFlexprofileEx (CXA_Motion library)
to implement the "FlexProfile" function. The "Synchronized Motion" license is
required for this operation mode.

Table 413: Attributes of the "ModeFlexProfile” operation mode
Element       Name           Type            Standard          Cyclically
                                               scanned
arAxisCtrl_gb[] Syn‐            AXIS_REF                       Yes
cMode.Master
Admin.Config. AXIS_REF                         No
Axis
Syn‐            ⮫ ML_Syn‐    SYNC_SET‐         Yes
cMode.Syn‐      cSource      POINT
cSource
Syn‐            ⮫ ML_Dyn‐    SYNC_SHORTE Yes
cMode.Direc‐ SyncDirection   ST_PATH
tion
SyncMode.Buf‐ BOOL           FALSE             No
ferMode
Syn‐            LREAL        0.0               No
cMode.Syn‐
cDyn‐
Values.Acc
Syn‐            LREAL        0.0               No
cMode.Syn‐
cDyn‐
Values.Dec
Syn‐            LREAL        0.0               No
cMode.Syn‐
cDyn‐
Values.JrkAcc
Syn‐            LREAL        0.0               No
cMode.Syn‐
cDyn‐
Values.JrkDec
Syn‐            LREAL        0.0               No
cMode.Syn‐
cDyn‐
Values.VelNeg
Syn‐            LREAL        0.0               No
cMode.Syn‐
cDyn‐
Values.VelPos
SyncMode.Off‐ LREAL          0.0               Yes
sets.Master.Po
sition
SyncMode.Off‐ LREAL          0.0               Yes
sets.Master.Vel
ocity
SyncMode.Off‐ LREAL          0.0               Yes
sets.Master.Ac
celeration
SyncMode.Off‐ LREAL          0.0               Yes
sets.Slave.Posi
tion
SyncMode.Off‐ LREAL          0.0               Yes
sets.Slave.
Velocity

Element   Name          Type      Standard       Cyclically
                                       scanned
SyncMode.Off‐ LREAL     0.0            Yes
sets.Slave.
Acceleration
Syn‐            LREAL   0.0            Yes
cMode.Proc‐
essCtrl.AngleA
djust.Offset
Syn‐            LREAL   0.0            Yes
cMode.Proc‐

                                                           CXA_MotionInterface
essCtrl.AngleA
djust.TConstan
t
Syn‐            LREAL   0.0            Yes
cMode.Proc‐
essCtrl.Master.
Offset
Syn‐            LREAL   0.0            Yes
cMode.Proc‐
essCtrl.Master.
TConstant
Syn‐            LREAL   0.0            Yes
cMode.Proc‐
essCtrl.Slave.
Offset
Syn‐            LREAL   0.0            Yes
cMode.Proc‐
essCtrl.Slave.T
Constant
Syn‐            LREAL   0.0            Yes
cMode.Proc‐
essCtrl.FineAd
just
SyncMode.Off‐ LREAL     0.0            Yes
sets.AngleAd‐
just.Position
SyncMode.Off‐ LREAL     0.0            Yes
sets.AngleAd‐
just.Velocity
SyncMode.Off‐ LREAL     0.0            Yes
sets.AngleAd‐
just.Accelera‐
tion
Syn‐            DINT    1              Yes
cMode.RatioN‐
umerator
Syn‐            DINT    1              Yes
cMode.Ratio‐
Denominator
Syn‐            LREAL   0.0            Yes
cMode.FineAd‐
just

Element      Name          Type           Standard      Cyclically
                                           scanned
Syn‐            LREAL          0.0         No
cMode.Flex‐
Profile.Master‐
Offset
Syn‐            LREAL          0.0         No
cMode.Flex‐
Profile.Slave‐
Offset
Syn‐            ML_Profi‐      SLAVE_CUR‐  No
cMode.Flex‐     leEntry        RENT_MASTER
Profile.Profi‐                 _CURRENT
leEntry
Syn‐            ML_ProfileExe‐ PRO‐        No
cMode.Flex‐     cutionMode     FILE_MODE_C
Profile.Profi‐                 YCLIC
leExecution‐
Mode
Syn‐            LREAL          0.0         No
cMode.Flex‐
Profile.Switch‐
Position
Syn‐            BOOL           FALSE       No
cMode.Flex‐
Profile.Switch‐
ProfileOnPos
Syn‐            BOOL           FALSE       No
cMode.Flex‐
Profile.Switch‐
GearOnPos
Syn‐            LREAL          0.0         No
cMode.Flex‐
Pro‐
file.AngleAd‐
just
Syn‐            ULINT          0           Yes
cMode.Flex‐
Profile.Even‐
tCondition‐
Control
Syn‐            STRING(50)     ‘’          Yes
cMode.Flex‐
Profile.Profile
Syn‐            LREAL          0.0         No
cMode.Flex‐
Profile.Slave‐
Adjust
arAxis‐      Admin._OpMo‐ MB_AXIS_MOD ModeAB            Not applicable
Status_gb    deAck           E
Admin.OpMo‐ BOOL               FALSE       Not applicable
deAck‐
Bits.MODE_SY
NC_FlexProfile

Element   Name           Type             Standard       Cyclically
                                               scanned
Data.Syn‐       LREAL           0.0            Not applicable
cMode.Actua‐
lOffset
Data.Syn‐       BOOL            FALSE          Not applicable
cMode.InSync
Data.Syn‐       LREAL           0.0            Not applicable
cMode.Offset‐
ToTarget

Data.Syn‐       ML_SyncMo‐      NO_SYNC_MOT Not applicable
cMode.Syn‐      tionState       ION
cState
Data.Syn‐       ML_FlexProfi‐   LOCKED_FOR_ Not applicable
cMode.Flex‐     leAccess        EDIT
Profile.Access‐
State_0
Data.Syn‐       ML_FlexProfi‐   LOCKED_FOR_ Not applicable
cMode.Flex‐     leAccess        EDIT
Profile.Access‐
State_1
Data.Syn‐       ML_FlexProfi‐   LOCKED_FOR_ Not applicable
cMode.Flex‐     leAccess        EDIT
Profile.Access‐
State_2
Data.Syn‐       ML_FlexProfi‐   LOCKED_FOR_ Not applicable
cMode.Flex‐     leAccess        EDIT
Profile.Access‐
State_3
Data.Syn‐       STRING          ‘0’            Not applicable
cMode.Flex‐
Profile.Active‐
Profile
Data.Syn‐       UDINT           0              Not applicable
cMode.Flex‐
Profile.Active‐
Segment
Data.Syn‐       ULINT           0              Not applicable
cMode.Flex‐
Profile.Even‐
tCondition‐
Status
Data.PLCO‐      BOOL            FALSE          Not applicable
penState.Syn‐
chronizedMo‐
tion
Data.Syn‐       BOOL            FALSE          Not applicable
cMode.Flex‐
Profile.Single‐
ExecutionDone
Data.Syn‐       BOOL            FALSE          Not applicable
cMode.Flex‐
Profile.Wait‐
ForSwitch

 Element       Name            Type          Standard        Cyclically
                                                             scanned
               Data. ActSyn‐   BOOL          FALSE           Not applicable
               cOffsets.
               Master.Done
               Data. ActSyn‐   LREAL         0.0             Not applicable
               cOffsets.
               Master.Done
               Data. ActSyn‐   LREAL         0.0             Not applicable
               cOffsets.
               Master.Done
               Data. ActSyn‐   BOOL          FALSE           Not applicable
               cOffsets.
               Slave.Done
               Data. ActSyn‐   LREAL         0.0             Not applicable
               cOffsets.
               Slave.Done
               Data. ActSyn‐   LREAL         0.0             Not applicable
               cOffsets.
               Slave.Done
               Data. ActSyn‐   BOOL          FALSE           Not applicable
               cOffsets.
               AngleAd‐
               just.Done
               Data. ActSyn‐   LREAL         0.0             Not applicable
               cOffsets.
               AngleAd‐
               just.Done
               Data. ActSyn‐   LREAL         0.0             Not applicable
               cOffsets.
               AngleAd‐
               just.Done

"ModeCamIn" operation mode
This command sets the axis connected to a master axis via electronic cams.
The cam has to be configured in the ctrlX Data Layer, refer to ⮫ "Motion App -
Motion Runtime Environment for ctrlX OS", Application Manual. After enabling
this operation mode, the respective axis is automatically coupled to a master
axis. The slave axis is switched to the SYNCHRONIZED_MOTION state.
Use the following command to enable the operation mode:
arAxisCtrl_gb[].Admin._OpMode := MB_AXIS_MODE.ModeSyncCam ;
//OR
arAxisCtrl_gb[].Admin._OpModeBits.MODE_SYNC_CamIn :=TRUE;
This operation mode provides an acknowledgement of the operation mode or
"TRUE" in the status structure of the axis:
IF     arAxisStatus_gb[].Admin._OpModeAck            =      MB_AXIS_MODE.
ModeSyncCam THEN
//user code
END_IF
or
arAxisStatus_gb[].Admin._OpModeAckBits.MODE_SYNC_ CamIn;

The AxisInterface uses the function ML_AxsCamInEx (CXA_Motion library)
to implement the "CamIn" function. The "Synchronized Motion" license is
required for this operation mode.

Table 414: Attributes of the "ModeCamIn" operation mode
Element        Name          Type           Standard        Cyclically
                                            scanned
arAxisCtrl_gb[] Syn‐            AXIS_REF                    Yes
cMode.Master
Admin.Config. AXIS_REF                    No
Axis

Syn‐            ML_Syn‐       SYNC_SET‐   Yes
cMode.Syn‐      cSource       POINT
cSource
SyncMode.       ML_SyncDirec‐ SYNC_SHORTE Yes
SyncDirection tion            ST_PATH
Syn‐            LREAL         0.0         No
cMode.Syn‐
cDyn‐
Values.Acc
Syn‐            LREAL         0.0         No
cMode.Syn‐
cDyn‐
Values.Dec
Syn‐            LREAL         0.0         No
cMode.Syn‐
cDyn‐
Values.JrkAcc
Syn‐            LREAL         0.0         No
cMode.Syn‐
cDyn‐
Values.JrkDec
Syn‐            LREAL         0.0         No
cMode.Syn‐
cDyn‐
Values.VelNeg
Syn‐            LREAL         0.0         No
cMode.Syn‐
cDyn‐
Values.VelPos
SyncMode.Off‐ LREAL           0.0         Yes
sets.Master.Po
sition
SyncMode.Off‐ LREAL           0.0         Yes
sets.Master.Vel
ocity
SyncMode.Off‐ LREAL           0.0         Yes
sets.Master.Ac
celeration
SyncMode.Off‐ LREAL           0.0         Yes
sets.Slave.Posi
tion

Element      Name          Type          Standard       Cyclically
                                           scanned
SyncMode.Off‐ LREAL            0.0         Yes
sets.Slave.
Velocity
SyncMode.Off‐ LREAL            0.0         Yes
sets.Slave.
Acceleration
Syn‐            LREAL          0.0         Yes
cMode.Proc‐
essCtrl.Master.
Offset
Syn‐            LREAL          0.0         Yes
cMode.Proc‐
essCtrl.Master.
TConstant
Syn‐            LREAL          0.0         Yes
cMode.Proc‐
essCtrl.Slave.
Offset
Syn‐            LREAL          0.0         Yes
cMode.Proc‐
essCtrl.Slave.T
Constant
Syn‐            LREAL          0.0         Yes
cMode.Proc‐
essCtrl.FineAd
just
Syn‐            DINT           1           Yes
cMode.RatioN‐
umerator
Syn‐            DINT           1           Yes
cMode.Ratio‐
Denominator
Syn‐            LREAL          0.0         Yes
cMode.FineAd‐
just
Syn‐            LREAL          0.0         No
cMode.CamIn.
MasterOffset
SyncMode.       LREAL          0.0         No
CamIn.Slave‐
Offset
SyncMode.       ML_Profi‐      SLAVE_CUR‐  No
CamIn.Profi‐    leEntry        RENT_MASTER
leEntry                        _CURRENT
SyncMode.       ML_ProfileExe‐ PRO‐        No
CamIn.Profi‐    cutionMode     FILE_MODE_C
leExecution‐                   YCLIC
Mode
SyncMode.       LREAL          0.0         No
CamIn.Switch‐
Position

Element     Name         Type         Standard        Cyclically
                                          scanned
SyncMode.      BOOL       FALSE           No
CamIn.Switch‐
ProfileOnPos
SyncMode.      BOOL       FALSE       No
CamIn.Switch‐
GearOnPos
Syn‐           LREAL      0.0         Yes
cMode.CamIn.
SwitchPosi‐

tionGainFactor
Syn‐           BOOL       FALSE       No
cMode.CamIn.
SwitchGain‐
FactorOnPos
SyncMode.      LREAL      1.0         Yes
CamIn. Gain‐
Factor
SyncMode.      LREAL      0.0         No
CamIn.AngleA
djust
SyncMode.      STRING(50) ‘’          Yes
CamIn. Point‐
Table
Syn‐           DINT       0           Yes
cMode.CamIn.
GearReduction
Syn‐           BOOL       FALSE       Yes
cMode.CamIn.
ActiveStateRe‐
fresh
arAxis‐     Admin._OpMo‐ MB_AXIS_MOD ModeAB       Not applicable
Status_gb   deAck          E
Admin.OpMo‐ BOOL          FALSE       Not applicable
deAck‐
Bits.MODE_SY
NC_CamIn
Data.Syn‐      BOOL       FALSE       Not applicable
cMode.InSync
Data.Syn‐      ML_SyncMo‐ NO_SYNC_MOT Not applicable
cMode.Syn‐     tionState  ION
cState
Data.PLCO‐     BOOL       BOOL        Not applicable
penState.Syn‐
chronizedMo‐
tion
Data.Syn‐      STRING(31) ‘’          Not applicable
cMode.CamIn.
ActiveCamT‐
able

Element      Name         Type     Standard   Cyclically
                                 scanned
Data.Syn‐      BOOL   FALSE      Not applicable
cMode.CamIn.
SingleExecu‐
tionDone
Data.Syn‐      BOOL   FALSE      Not applicable
cMode.CamIn.
WaitForSwitch
Data.Syn‐      BOOL   FALSE      Not applicable
cMode.CamIn.
WaitForSwitch‐
Gain
Data. ActSyn‐ BOOL    FALSE      Not applicable
cOffsets.
Master.Done
Data. ActSyn‐ LREAL   0.0        Not applicable
cOffsets.
Master.Done
Data. ActSyn‐ LREAL   0.0        Not applicable
cOffsets.
Master.Done
Data. ActSyn‐ BOOL    FALSE      Not applicable
cOffsets.
Slave.Done
Data. ActSyn‐ LREAL   0.0        Not applicable
cOffsets.
Slave.Done
Data. ActSyn‐ LREAL   0.0        Not applicable
cOffsets.
Slave.Done
Data. ActSyn‐ BOOL    FALSE      Not applicable
cOffsets.
AngleAd‐
just.Done
Data. ActSyn‐ LREAL   0.0        Not applicable
cOffsets.
AngleAd‐
just.Done
Data. ActSyn‐ LREAL   0.0        Not applicable
cOffsets.
AngleAd‐
just.Done
Data. ActSyn‐ BOOL    FALSE      Not applicable
cOffsets.
Master.Done
Data. ActSyn‐ LREAL   0.0        Not applicable
cOffsets.
Master.Done
Data. ActSyn‐ LREAL   0.0        Not applicable
cOffsets.
Master.Done

Element       Name           Type           Standard        Cyclically
                                                            scanned
              Data. ActSyn‐ BOOL            FALSE           Not applicable
              cOffsets.
              Slave.Done
              Data. ActSyn‐ LREAL           0.0             Not applicable
              cOffsets.
              Slave.Done
              Data. ActSyn‐ LREAL           0.0             Not applicable
              cOffsets.
              Slave.Done

              Data. ActSyn‐ BOOL            FALSE           Not applicable
              cOffsets
              Data. ActSyn‐ LREAL           0.0             Not applicable
              cOffsets
              Data. ActSyn‐ LREAL           0.0             Not applicable
              cOffsets
              Data.Syn‐     BOOL            FALSE           Not applicable
              cMode.CamIn.
              StateRefre‐
              shActive
              Data.Syn‐     BOOL            FALSE           Not applicable
              cMode.CamIn.
              StateRefresh‐
              Done
              Data.Syn‐     ARRAY [0..3]                    Not applicable
              cMode.CamIn. OF
              Profiles      MB_SYNC_STA
                            TE_CAMIN_PR
                            OFILES

Table 415: Attributes of the “MB_SYNC_STATE_CAMIN_PROFILES” function
Name              Type              Standard            Description
ProfileName       STRING (63)       0                   Profile name
PointTableName                      ‘’                  Name of the "Point
                                                        Table"
AccessState       ML_FlexProfileAc‐ UNVALIDATED         The access status
                  cess                                  of the specified
                                                        axis profile

    Operation mode “External function block”
If the axis is already in an operation mode, a motion command is not executed
from the AxisInterface when this operation mode is activated.

If the operation mode is changed from ModeAb to ModeExternalFB, the Axi‐
sInterface switches the drive to AH and waits for an external motion com‐
mand, e.g. from a technology function.
The following command activates the operation mode:
arAxisCtrl_gb[].Admin._OpMode := ModeExternalFB;
or
arAxisCtrl_gb[].Admin._OpModeBits.MODE_EXTERNAL_FB:= TRUE;
The AxisInterface uses the function ML_AxsPower (CXA_Motion library) for
switching.

Table 416: Attributes of the operation mode “External function block”
Element            Name                        Type                     Default        Cycli‐
                                                                                       cally
                                                                                       scanned
arAxis‐            Admin._OpModeAck‐           BOOL                                    Omitted
Status_gb[ ]       Bits.MODE_EXTERNAL_FB

"ModeTorque" operation mode
Enabling this operating mode, switches the drive to torque mode and interpo‐
lates to the target torque. This command can only be unbuffered (buffering is
not useful). POSITION, VELOCITY and TORQUE can switch from one operating
mode to another. If torque mode is enabled, the PLCopen state of the axis is
CONTINUOUS_MOTION.
The user can enable the torque mode as follows:
 arAxisCtrl_gb[].Admin._OpMode := MB_AXIS_MODE. ModeTorque;
 or
 arAxisCtrl_gb[].Admin._OpModeBits. MODE_AXS_TORQUE;
 The following acknowledgement has to follow the command for the operating
 mode.
 Returns the requested operating mode or TRUE:
 arAxisStatus_gb[].Admin._OpModeAck = MB_AXIS_MODE. ModeTorque;
 arAxisStatus_gb[].Admin._OpModeAckBits. MODE_AXS_TORQUE;
 arAxisStatus_gb[].Data.TorqueMode.InTorque
 arAxisStatus_gb[].Data.TorqueMode. TorqueCtrlPosVelLim
 arAxisStatus_gb[].Data.TorqueMode. TorqueCtrlNegVelLim
 The AxisInterface uses the ML_AxsTorque and ML_GetCmdState functions
 (CXA_Motion library) for switching purposes.

 Table 417: Attributes of the "ModeTorque" mode
  Element       Name                  Type    Standard    Cyclically scanned
  arAxisCtrl_gb TorqueMode.Torque     LREAL   0.0         Yes
                TorqueMode.TrqRamp    LREAL   0.0         Yes
                TorqueMode.Velocity   LREAL   0.0         Yes
                TorqueMode.Dyn‐       LREAL   2           No
                Values.Acceleration
                TorqueMode.Dyn‐       LREAL   2           No
                Values.Deceleration
                TorqueMode.Dyn‐       LREAL   0.0         No
                Values.JerkAcc
                TorqueMode.Dyn‐       LREAL   0.0         No
                Values.JerkDec
  arAxis‐       TorqueMode.InTorque   BOOL    FALSE       Not applicable
  Status_gb
                TorqueMode.Tor‐       BOOL    FALSE       Not applicable
                queCtrlPosVelLim
                TorqueMode.Tor‐       BOOL    FALSE       Not applicable
                queCtrlNegVelLim

If the global configuration parameter "EnableCyclicScanning" is set to TRUE,
the input parameters "Torque"/"TorqueRamp"/"Velocity"/"DynValues.Accelera‐
tion"/"DynValues.Deceleration" should be checked and refreshed every cycle.
If the global configuration parameter "UpdateEveryInput" is set to TRUE at the
same time, "DynValues.JerkAcc"/"DynValues.JerkDec" should also be checked
and refreshed. If the global configuration parameter "EnableCyclicScanning" is
set to FALSE, they are only locked when "ModeTorque" is active.

Prerequisite for torque control in the Data Layer node:
The axis has to be supplied with power.
● The unit of the "Torque" and "TorqueRamp" parameters can be configured

  in the following Data Layer node:
    motion/axs/<Axis>/cfg/units
    By default, the unit for "Torque" is Nm and for "TorqueRamp" Nm/s.
● The window for "InTorque" can be configured in the following Data Layer
    node:
    motion/axs/<Axis name>/cfg/functions/cyclic-status-data/windows/in-trq
● The torque limitation in negative direction can be configured in the fol‐
    lowing Data Layer node:
    motion/axs/<Axis name>/cfg/lim/trq-neg
● The torque limitation in positive direction can be configured in the fol‐
    lowing Data Layer node:
    motion/axs/<Axis name>/cfg/lim/trq-pos
Drives that only support the torque mode are not permitted. This means that
it always has to be possible to switch from torque to POSITION or VELOCITY.

Functions for multiple operation modes
Some functions are enabled in multiple operation modes and described in
this section.

VelocityOverride
With the VelocityOverride input, the velocity of the running motion can be
reduced.
Values between 0.0% (axis in standstill) and 100.0% (motion executed with
specified velocity) are permitted.
The VelocityOverride input is enabled in the following operation modes:
● ModePosAbs
● ModePosRel
● ModePosAdd
The AxisInterface uses the function ML_SetOverride (CXA_Motion library) for
switching.
Table 418: Attributes of the function "VelocityOverride"
Element             Name                              Type           Default      Cyclically
                                                                                  scanned
arAxisCtrl_gb[ ]    Admin.VelocityOverride            LREAL          100.0        Yes

Setting absolute position
The actual position value at any position can be set to a new value (new
reference system) via the SetAbsRef input. The input RefPosition specifies the
new value.

If an AxisProfile of type "Servodrive over Ethercat" is connected to an axis,
the command “S-0-0447, C0300 Set absolute position procedure command”
is executed in the connected drive.
The successful completion is shown via the SetAbsRefDone output. In case of
error, diagnostic outputs are set.
SetAbsRefDone is reset if the input SetAbsRef is deleted.
The SetAbsRef input is preferably used in the following operation modes:
● ModeAB
● ModeAH
The AxisInterface uses the function ML_AxsSetAbsPos (CXA_Motion library)
for switching.
Table 419: Attributes of the function “Set absolute position"
Element             Name                                Type          Default           Cyclically
                                                                                        scanned
arAxisCtrl_gb[ ]   Admin.SetAbsRef                      BOOL          FALSE             Yes
                   Admin.RefPosition                    LREAL         0.0               No
arAxisStatus_gb[ ] Admin.SetAbsRefDone                  BOOL                            Omitted

User-defined operation modes
In case of customizable operation modes, the Motion commands are specified
in the user-specific extension of the library CXA_MotionInterfaceUser. Thus,
users can implement own operation modes and their motion commands.
In total, 10 user-defined modes (ModeUserXx_User_0...ModeUserXx_User_9)
are available. An exemplary implementation is already available for ModeU‐
serXx_User_0.
If the axis is already in an operation mode, the AxisInterface does not execute
any motion command when this operation mode is activated.
If the operation mode is changed from ModeAb to ModeUserXx_User_0...Mod‐
eUserXx_User_9, the AxisInterface switches the drive to AH and waits for a
motion command, e.g. from the extension in the application part.
The following command activates the first user-defined operation mode:
arAxisCtrl_gb[].Admin._OpMode := ModeUserXx_User_0;
or
arAxisCtrl_gb[].Admin._OpModeBits.MODE_XX_USER_0:= TRUE;
The AxisInterface uses the function ML_AxsPower (CXA_Motion library) for
switching.

Table 420: Attributes of the user-defined operation modes
Element            Name                          Type                         Default           Cycli‐
arAxis‐            Admin._OpModeAck‐             BOOL                                           Omitted
Status_gb[ ]       Bits.MODE_XX_USER_0...9

### 19.3.4 AxisInterface - Global variables

The library CXA_MotionInterfaceUser includes the Global Variable List
Global_AxisInterface in the folder AxisInterfaceUser/GlobalVariables.

This list includes the following structures/variables:

Name                   Type                                        Description
arAxisCtrl_gb[ ]       ARRAY [] OF TE_AXIS_CONTROL_TYPE01          Control structure of the AxisIn‐
                                                terface
arAxisStatus_gb[ ]     ARRAY [] OF TE_AXIS_STATUS_TYPE01           Status structure of the AxisInter‐
                                                face
arAxisIdx_gb           ARRAY [] OF UINT                            Continuous list of axes
uiNofAxis_gb           UINT                                        Number of active axes
VisuAxisNo             INT                                         Switching the axis index in the
                                                visualizations
bRemoteOn_gb           BOOL                                        TRUE: Visualization is active

  uiNofAxis_gb      should       be        in       the                       range
  [MOTIF_CONFIG.MIN_AXIS_INDEX..MOTIF_CONFIG.MAX_AXIS_INDEX].

### 19.3.5 AxisInterface - Structures

Introduction and overview
The AxisInterface provides a data interface for easy axis control.
For information on the data structures, refer to the ctrlX PLC Engineering
library manager in the CXA_MotionInterface library in the AxisInterface/DUTs
folder or in the CXA_MotionInterfaceUser library in the AxisInterfaceUser/DUTs
folder.

  The programming template “MotionInterface" can either be extended by the
  user or some extensions have already been integrated. To enable these exten‐
  sions, define own structures in the user project that extend the library struc‐
  tures.
  The extended structures have the prefix “TE_”. If there is a structure called
  TE_AXIS_ADMIN_STATUS for example in the programming template “MotionIn‐
  terface”, it is an extended structure of MB_AXIS_ADMIN_STATUS.
  For information on the structure, refer to the ctrlX PLC Engineering library
  manager with the name MB_AXIS_ADMIN_STATUS in the library CXA_MotionIn‐
  terface and with the name TE_AXIS_ADMIN_STATUS in the library CXA_Motio‐
  nInterfaceUser.

### 19.3.6 AxisInterface - Example program

Introduction and overview
This chapter provides an overview on the AxisInterface parts available as
open-source code.
The open-source program parts are provided with the following elements:
  ● The programming template “AxisInterface” is used as an example applica‐
    tion for the AxisInterface (also refer to ⮫ Chapter 19.2 MotionInterface -
    Initial configuration on page 445).
  ● The user can change the CXA_MotionInterfaceUser.library to adapt the Axi‐
    sInterface to the respective application (also refer to ⮫ AxisInterface - User
    extension).

Programming template "AxisInterface"
The programming template “AxisInterface" covers the following points of the
AxisInterface:
● AxisIfPlcProg:
  Calling the TE_AxisInterfaceMainProg() - Initialization and cyclic call of the
  AxisInterface.
● AxisIfMotionProg:
  The method TE_AxisInterfaceMainProg.mMotionTask() is called. In this
  cycle, the actual values are refreshed in arAxisStatus_gb[].Data. If the
  method is not called, the actual values are refreshed in the PlcProg cycle.
● GlobalAxisDefines:
  Only required if MOTIF_CONFIG.CONFIG_MODE_AXS is set to GLOB_VAR.
  The axes are defined as constants of the type MB_AXISIF_REF and trans‐
  ferred in a list to TE_AxisInterfaceMainProg(). This constants have to be
  adapted for the own project.
● DemoAxisCommands:
  Example code to use the AxisInterface. This code has to be adapted for the
  own project.
● DemoBufferedAxisCommands:
  Example code with a sequence programming and the issuing of buffered
  axis commands. This code has to be adapted for the own project.
● OverViewAxes:
  Visualization to operate the AxisInterface during the commissioning phase.
  Click on the fields with "<<" to go down further into the screens.
● Version_AxisInterface:
  Change history and disclaimer

CXA_MotionInterfaceUser.library:

Introduction and overview
This open library extends the function blocks and structures of the basic
library CXA_MotionInterface. Programs and visualizations are provided. The
global variables of the interfaces are instantiated. The user can adapt and
extend the interfaces with this library.
To make the adaptations, refer to ⮫ AxisInterface - User extension.
This chapter describes the POUs of the AxisInterface from the AxisInterfa‐
ceUser/POUs folder.

TE_AxisInterfaceMainProg
Brief description
The program TE_AxisInterfaceMainProg covers the following:
● Initialization of the AxisInterface :
  When reaching the "Running" mode, the AxisInterface is initialized using
  the function block TE_AxisInitAllAxis. If the initialization was completed
  successfully, the “InitDone” output is set. In case of errors, the “Error”
  output is set.
● Cyclic call of the AxisInterface:
  After a successful initialization, the function block TE_AxisInterface is

  called cyclically.
● TE_AxisInterfaceMainProg.mMotionTask() method:
  If the method is called from a faster MotionTask, the elements in
  arAxisStatus_gb[].Data are updated in a faster cycle. The call of the func‐
  tion block TE_AxisInterface can be moved to the faster task using the con‐
  trol variable “arAxisCtrl_gb[].Admin.Config.MotionSync“.
  If the method is not called, all updates are made in the cycle of the PLC
  task.

Table 421: Interface variables of TE_AxisInterfaceMainProg
I/O type       Name                   Data type           Comment
VAR_INPUT      ClearError             BOOL                Clearing the error is started at a positive
                                                          edge at ClearError
               AxisCfgIdx             POINTER TO          Configuration list for the indices of the
                                      ARRAY [] OF         axes (only for the configuration mode
                                      MB_AXISIF_REF       GLOB_VAR)
VAR_OUTPUT InitDone                   BOOL                It is set if the program completed the initi‐
                                                          alization successfully
               Error                  BOOL                Indicates that an error occurred in the pro‐
                                                          gram
               ErrorID                ⮫ ERROR_CODE        Short note on the error cause
               ErrorIdent             ⮫ ERROR_STRUCT Detailed error information

Troubleshooting:
The error codes of the internally used function block TE_AxisInitAllAxes are
transferred.
The program can generate the following error codes:
Table 422: Error codes of the program TE_AxisInterfaceMainProg
ErrorID            Additional1                       Additional2               Description
STATE_MACHINE_ERRO 16#0A0F0107                       16#0C230190               Errors during the pro‐
R                                                                              gram processing

The program TE_AxisInterfaceMainProg is useful when integrating the AxisIn‐
terface into an existing program.
See also Example_AxIfApplicationPart in the folder AxisInterfaceUser/_Exam‐
ples.

TE_AxisInitAllAxes
Brief description
The function block TE_AxisInitAllAxes initializes the AxisInterface structures.
Use the parameter list MOTIF_CONFIG to control the initialization.

        There are the following options:
        ● AUTO = MOTIF_CONFIG.CONFIG_MODE:
          If the Datalayer node motion/axs/ is read out and the axes are positioned
          in the AxisInterface structures in the sequence found.
        ● GLOB_VAR = MOTIF_CONFIG.CONFIG_MODE:
          The axes are positioned using the global array AXIF_CONFIG_INDEXES in
          the AxisInterface structures.
        ● FILE = MOTIF_CONFIG.CONFIG_MODE:
          A list of axes and the respective axis number are defined in a JSON file.

Table 423: Interface variables of TE_AxisInitAllAxes
I/O type           Name                  Data type            Comment
VAR_INPUT          Execute               BOOL                 A positive edge at “Execute” starts the initi‐
                                                              alization
                   AxisCfgIdx            POINTER TO           Configuration list for the indices of the
                                         ARRAY [] OF          axes (only for the configuration mode
                                         MB_AXISIF_REF        GLOB_VAR)
VAR_OUTPUT Done                          BOOL                 Set when the function block has completed
                                                              the processing
                   Active                BOOL                 Set when the function block is active (not
                                                              in idle mode)
                   Error                 BOOL                 Indicates that an error occurred in the pro‐
                                                              gram
                   ErrorID               ERROR_CODE           Short note on the error cause
                   ErrorIdent            ERROR_STRUCT         Detailed error information

        Troubleshooting:
 The error codes of the internally used function block MB_AxisInit are trans‐
 ferred.
 The function block can generate the following error codes:
Table 424: Error codes of the TE_AxisInitAllAxes function block
ErrorID                        Additional1              Additional2               Description
INPUT_RANGE_ERROR              16#0A0F0107              16#0C230180               The number of actually
                                                                                  created axes (uiNo‐
                                                                                  fAxis_gb) exceeds the
                                                                                  maximum number of
                                                                                  axes configured in
                                                                                  CXA_MotionInterfa‐
                                                                                  ceUser that may be cre‐
                                                                                  ated
                                                                                  (MOTIF_CONFIG.MAX_A
                                                                                  XIS_INDEX)
INPUT_RANGE_ERROR              16#0A0F0107              16#0C230181               Unknown configuration
                                                                                  mode
                                                                                  (MOTIF_CONFIG.CFG_
                                                                                  MODE_AXS)
INPUT_RANGE_ERROR              16#0A0F0107              16#0C230182               Pointer AxisCfgIdx to
                                                                                  the global variable is 0
                                                                                  (MOTIF_CONFIG.CFG_
                                                                                  MODE_AXS =
                                                                                  GLOB_VAR)

ErrorID                      Additional1             Additional2          Description
INPUT_RANGE_ERROR            16#0A0F0107             16#0C230183          Axis index is beyond
                                                     the valid range
                                                     (MOTIF_CONFIG.CFG_
                                                     MODE_AXS =
                                                     GLOB_VAR)
INPUT_RANGE_ERROR            16#0A0F0107             16#0C230184          Axis index double
                                                     (MOTIF_CONFIG.CFG_
                                                     MODE_AXS =
                                                     GLOB_VAR)
INPUT_RANGE_ERROR            16#0A0F0107             16#0C230185          Axis name double

                                                     (MOTIF_CONFIG.CFG_
                                                     MODE_AXS =
                                                     GLOB_VAR)
INPUT_RANGE_ERROR            16#0A0F0107             16#0C230186          Configuration file not
                                                     found
                                                     (MOTIF_CONFIG.CFG_
                                                     MODE_AXS = FILE)
INPUT_RANGE_ERROR            16#0A0F0107             16#0C230187          Configuration file incor‐
                                                     rect
                                                     (MOTIF_CONFIG.CFG_
                                                     MODE_AXS = FILE)
STATE_MACHINE_ERRO 16#0A0F0107                       16#0C230188          Errors while processing
R                                                                         the function block

The program TE_AxisInterfaceMainProg already calls this function block
TE_AxisInitAllAxes.

TE_AxisInterface
Brief description
The function block TE_AxisInterface extends the MB_AxisInterfaceBase and
processes the AxisInterface structures in cyclic mode.
To optimize the performance, the structures are connected to REFERENCE TO
as VAR_INPUT instead of as VAR_IN_OUT. Thus, the inputs only have to be
initialized once. The mInitExtension method is used. If the function block is
called cyclically, the structures do not have to be transferred.

Table 425: Interface variables of TE_AxisInterface
I/O type       Name                 Data type        Comment
VAR_INPUT      AdminCtrlExt         REFERENCE TO     Reference to the control structure “Admin”
control struc‐                      TE_AXIS_ADMINIS‐
ture                                TRATION
               StopModeCtrlExt      REFERENCE TO     Reference to the control structure “Stop
                                    TE_AXIS_STOP_MO Mode”
                                    DE
               PosModeCtrlExt       REFERENCE        Reference to the control structure "Posi‐
                                    TO TE_AXIS_POSI‐ tioning"
                                    TIONING
               SetupMode            REFERENCE TO     Reference to the control structure “Setup‐
                                    TE_AXIS_SETUP_M Mode”
                                    ODE
               VelModeCtrlExt       REFERENCE TO     Reference to the control structure Velocity
                                    TE_AXIS_VELOCITY Mode

I/O type           Name              Data type           Comment
SyncModeExt       REFERENCE           Reference to the control structure "Sync
                  TO TE_AXIS_SYN‐     Mode"
                  CHRONISATION
TrqModeCtrlExt    REFERENCE TO        Reference to the control structure "Torque
                  TE_AXIS_TORQUE      Mode"
VAR_INPUT          AdminStatusExt    REFERENCE TO        Reference to the status structure “Admin”
status struc‐                        TE_AXIS_ADMIN_S
ture                                 TATUS
DataStatusExt     REFERENCE TO        Reference to the status structure “Data”
                  TE_AXIS_DATA
DiagStatusExt     REFERENCE           Reference to the status structure “Diag”
                  TO TE_AXIS_DIAG‐
                  NOSIS

    Troubleshooting:
 The error codes of the internally used function blocks are transferred.
 The function block can generate the following error codes:
Table 426: Error codes of the TE_AxisInterface function block
ErrorID            Additional1                      Additional2              Description
STATE_MACHINE_ERRO 16#0A0F0107                      16#0C2301A0              Errors while processing
R                                                                            the function block

    The program TE_AxisInterfaceMainProg already calls the function block
    TE_AxisInterface.

TE_GetAxisInterfaceIndex
    Brief description
    The function TE_GetAxisInterfaceIndex provides the index of an axis in the
    AxisInterface structures defined by axis names.

Table 427: Interface variables of TE_GetAxisInterfaceIndex
I/O type           Name               Data type          Comment
VAR_INPUT          AxisName           STRING(15)         Name of the searched axis
Return             TE_GetAxisInterfa‐ UINT               Index of the searched axis
                   ceIndex                               16#FFFF (-1) if the axis was not found

    Troubleshooting:
    The function returns 16#FFFF (-1) if the axis was not found.

### 19.3.7 AxisInterface - Visualizations

Introduction and overview
   Visualization masks are included in the AxisInterface upon delivery to provide
   a simple template interface to set and control the system axes.

    The following visualizations are included in the programming template "Kine‐
    maticInterface and AxisInterface" and in the CXA_MotionInterfaceUser.library:

Table 428: Example project visualizations
Visualization                 Description
OverviewAxes (in the tem‐     Complete overview on all defined axes, including simple diagnos‐
plate project)                tics, status and jog operating elements
Axis_Overview                 It indicates the current command and current values for position
                              and velocity, together with the navigation for the position display of
                              the current axis. The axes can also be homed and switched off.
Position_mode                 Monitoring the positioning mode
                     The following global variables are used to control and access system informa‐
                     tion in the visualizations:

● arAxisCtrl_gb[ ]
● arAxisStatus_gb[ ]
● VisuAxisNo

System overview - Visualization
The OverviewAxes visualization allows to quickly connect each axis that is
configured in the project. Additional axes can be added for display in offline
mode.

This display provides an overall system status and allows to delete errors.
Individual axis operating elements provide the axis name, diagnostics, the cur‐
rent position and velocity together with the operation mode status displays.
With the SetupMode section, the user can jog and position individual axes as
well as start and stop axes.

Adding an axis to the system overview
An axis is added to the system overview display like a new visualization:
Select the relevant element and specify the axis number.
The following steps describe the procedure briefly:
1.   Double-click on the visualization “OverviewAllAxes” with ctrlX PLC Engi‐
     neering in offline mode.

2.   In the “Visualization Tools” window, select the button “Frame” and,
     under the last line in the axis table, generate an outline with the correct
     line height and width.
3.   Right-click on the “Frame” and enable the “Frame selection”. Select
     the element OverviewOneAxis from the selection window of the visuali‐
     zation in the folder CXA_MotionInterfaceUser/AxisInterfaceUser/Visualiza‐
     tions/SystemOverview.
     🡆 An entirely new system overview "Axis line" is displayed.
4.   Click into the new visualization, enter the index of the defined axis into
     the "Properties" window as value for m_Input_AxisIndex.
5.   The new AxisInterface for the system overview can now be resized and
     positioned.
6.   Recompile the PLC project and go online.

Repeat the steps for all axes added to the project.

Navigation system overview
To open an overview display of the individual axis, click on the button with
the two arrows “<<” located below the "Details" column in the axis table.
From the axis overview display, it can be navigated to the operation mode
display for the position.

### 19.3.8 AxisInterface - User extension

    Introduction and overview
The user can extend the structures arAxisCtrl_gb[ ] and arAxisStatus_gb[ ] to
adapt the AxisInterface to special applications.

The structures arAxisCtrl_gb[ ] and arAxisStatus_gb[ ] of the user are defined
as basic types with the prefix “MB_” in the closed CXA_MotionInterface.com‐
piled-library and can thus not be accessed by the user.
To allow extensions, own structures are required that extend the “MB_” struc‐
tures. The extended structures have the prefix “TE_” and are located in the
open library CXA_MotionInterfaceUser.library.

Recommended procedure
To execute the user extensions, adjust the CXA_MotionInterfaceUser.library.
For understanding purposes, it is required and strongly recommended to
specify a new name for the modified library, e.g. CXA_MotionInterfaceMyCom‐
pany.library.
CXA_MotionInterfaceMyCompany.library is used as library name in the fol‐
lowing.
Operating sequence
1.      Select the CXA_MotionInterfaceUser.library in the library manager. Right-
        click on “Export library”. Specify a storage location and a new name, e.g.
        "CXA_MotionInterfaceMyCompany.library". Subsequent renaming is also
        possible.

2.    Use a second instance of the ctrlX PLC Engineering to open the
      CXA_MotionInterfaceMyCompany.library. In the project information,
      select the field “released”, modify further fields and delete the “Place‐
      holder” key in the properties.
3.    Remove the CXA_MotionInterfaceUser.library in the library manager of
      the user program (first instance of the ctrlX PLC Engineering) and inte‐
      grate the CXA_MotionInterfaceMyCompany.library instead.
4.    Make the respective changes in the library and execute the following
      command: “File 🠂 Save project and install in library repository”.
5.    Test the adaptations in the user program (first instance of PLC Engi‐
      neering). Debugging in the code from the library is also possible.
6.    Repeat the steps 4 and 5 until the function runs without errors.
When an update of the CXA_MotionInterfaceUser.library is available, changes
can be applied with “Project 🠂 Compare” in the CXA_MotionInterfaceMyCom‐
pany.library.
CXA_MotionInterfaceUser.library uses error codes from "CXA_TABLE". Refer to
the product documentation.
If more error codes are required in the user extensions, they can be defined
freely, but have to be reported with "USER1_TABLE..USER10_TABLE

ML_AxsGetBrakingDistance
This section shows how the AxisInterface is extended by adding the ML_Axs‐
GetBrakingDistance functionality. The function ML_AxsGetBrakingDistance
allows to request the current deceleration path of an axis.

The following new inputs and outputs are defined:
● arAxisCtrl_gb[ ].Admin.EnableReadBreakDistance
● arAxisStatus_gb[ ].Data.BrakingDistance
The following customized extensions are implemented into the programming
template “AxisInterface".
● Jog functionality as SetupMode
● RetriggerOpMode to trigger an operation mode again, e.g. MoveRelative
    with the same distance
● A user-defined operation mode MODE_XX_USER_0
It is assumed that the structure already prepared in the program template
“AxisInterface” is used. The following describes the required changes in the
POUs specified there.

Notes on the implementation of user extensions
The user extensions were implemented using the object-oriented extensions
from PLC Engineering.
Please note the following particularities:

  ● The function block TE_AxisInterface is derived from the basic function
    block MB_AxisInterfaceBase. Use the keyword SUPER to call the basic func‐
    tion block or its methods/actions of the basic function block. At various
    locations, the method mSetError of the function block MB_AxisInterface‐
    Base is called via SUPER^.mSetError(...); to enter errors into the diagnostic
    system
  ● Within the function block TE_AxisInterface, the data of arAxisCtrl_gb can be
    accessed using the inputs AdminCtrlExt, PosModeCtrlExt, etc. and the data
    of arAxisStatus_gb can be accessed using AdminStatusExt, DiagStatusExt,
    etc.
    The inputs AdminCtrl (without Ext), etc. belong to the basic function block

    and are not to be used.
  ● The inputs of the TE_AxisInterface function block are defined as REFER‐
    ENCE TO. In the method mInitExtension, the references are initialized once
    and do not have to be transferred again during the cyclic call of the func‐
    tion block
  ● To extend the basic structures TE_AXIS_CONTROL_TYPE01 and
    TE_AXIS_STATUS_TYPE01 with additional substructures, the following addi‐
    tional steps are required (see SetupMode and SetupModeAck as exam‐
    ples):
    – Enter new elements into TE_AXIS_CONTROL_TYPE01 or
       TE_AXIS_STATUS_TYPE01
    – Add the additional inputs as REFERENCE TO to the TE_AxisInterface
       function block
    – Initialize the references in the method mInitExtension of the TE_AxisIn‐
       terface function block

    Extending the arAxisCtrl_gb[ ] structure
To add the additional functionality of the arAxisCtrl_gb[ ] structure, the user
has to create a new structure, derive the substructures from the existing struc‐
ture and then add the new elements. In the programming template "Kinemati‐
cInterface and AxisInterface", a structure TE_AXIS_CONTROL_TYPE01 and the
substructures TE_AXIS_ADMINISTRATION, etc. are already prepared.

  Proceed the following steps to extend the functionality of the TE_AXIS_ADMIN‐
  ISTRATION structure:
  1.   Open the CXA_MotionInterfaceMyCompany.library with the ctrlX PLC
       Engineering
  2.   Open the TE_AXIS_ADMINISTRATION structure, folder AxisInterfa‐
       ceUser/DUTs/Control.
  3.      Declare the following variable
          ● EnableReadBreakingDistance: BOOL:=TRUE;

    Extending the arAxisStatus_gb[ ] structure
  Extend the arAxisStatus_gb[ ] structure as described in the steps in ⮫ Chapter
  Extending the arAxisCtrl_gb[ ] structure on page 503.
  The following steps describe the procedure briefly:
  1.   Open the TE_AXIS_DATA structure, folder AxisInterfaceUser/DUTs/Status.
  2.   Declare the following variable
          ● BrakingDistance: LREAL;

    Extending the function block
The last step in the user extension is to extend the function block so that the
new elements can be used.

1.   Declare the following variable in the TE_AxisInterface function block:
     stML_AxsGetBrakingDistanceData:
     ML_AxsGetBrakingDistanceData;
2.   The function could be programmed as follows in the TE_AxisInterface
     function block:
     IF AdminCtrlExt.EnableReadBreakingDistance = TRUE THEN
     stML_AxsGetBrakingDistanceData.In.AxisName :=
     AdminCtrlExt.Config.Axis.AxisName;
     ML_AxsGetBrakingDistance(stML_AxsGetBrakingDistanceData); /
     / call motion function
     DataStatusExt.BrakingDistance :=
     stML_AxsGetBrakingDistanceData.Out.BrakingDistance;
     END_IF
3.   Compile the project again and check it for programming errors.
4.   Load the project to the control.
The new input and output elements are now part of the AxisInterface struc‐
ture and can be viewed using the variables in the Global_AxisInterface.

Using the user-defined operation mode
In case of user-defined operation modes, the Motion commands are imple‐
mented in the user-specific extension of the CXA_MotionInterfaceMyCom‐
pany.library.
The following steps show how to use the user-defined operation modes:
1.    Insert a new data structure for the command values of the user-defined
      operation mode (name, e.g. TE_AXIS_USERMODE1) below the AxisInter‐
      face/Type/Control folder.
2.    Define the data structure elements (e.g. Vel: REAL, Acc:REAL, DEC:
      REAL).
3.    Insert a new element of the type of the above mentioned data struc‐
      ture (example: UserMode1: TE_AXIS_USERMODE1;) at the end of the
      TE_AXIS_CONTROL_TYPE01 or TE_AXIS_CONTROL_TYPE02 data struc‐
      ture.
4.    Insert a new input at the end of the VAR_INPUT declaration in the TE_Axi‐
      sInterface function block (example: MyModeUser1Ext: REFERENCE TO
      TE_AXIS_USERMODE1;).
5.    Initialize the reference of the newly created input in the mInitExtension
      method of the TE_AxisInterface (example: MyModeUser1Ext REF= arA‐
      xisCtrl_gb[index].UserMode1;).
6.    Program the Motion command in the mUserModes method. The mUserM‐
      odes method of the TE_AxisInterface overwrites the method of the basic
      function block MB_AxisInterfaceBase. It is called by this function block.
7.    Compile the project again and check it for programming errors.
8.    Load the project to the control and start the PLC.
9.    The new user-defined operation mode can be selected and the Motion
      command with the transmitted command values is applied.

### 19.3.9 How To - Typical user activities

Accessing axis data
The following data is available (name = corresponding axis name):
● arAxisCtrl_gb[Name.AxisNo] => Control structure of the AxisInterface
● arAxisStatus_gb[Name.AxisNo] => Status structure of the AxisInterface
● arAxisStatus_gb[Name.AxisNo].Data => Actual values and status informa‐
  tion

Axis data can be accessed acyclically via the ctrlX Data Layer using the func‐
tion blocks DL_ReadNode and DL_WriteNode.

Adjusting the maximum number of axes
 The axis structures can be adjusted to the actual existing number of axes.
 The library CXA_MotionInterfaceUser allows adjustments using the library
 parameter MOTIF_CONFIG.
 The size of the structures can be selected with regard to the application using
 the constants MIN_AXIS_INDEX and MAX_AXIS_INDEX.
 MOTIF_CONFIG.MAX_AXIS_INDEX is limited by the maximum number of axes
 permitted by the Motion kernel.
 If the KinematicInterface is used, the constant MAX_AXIS_INDEX selected may
 not be higher than Global_MB_KinInterfaceVars.MB_KINIF_MAX_AXIS_INDEX.
 Otherwise, an initialization error results when the PLC program is started.

    Adjusting the assignment AxisName <>AxisIndex
 The AxisInterface uses an AxisIndex for the addressing in the axis structures.
 The Motion firmware works with this axis name. There are different methods
 to assign AxisName<>AxisIndex.
 The library CXA_MotionInterfaceUser allows to select the method using the
 library parameter MOTIF_CONFIG.
 Assignment: AxisName<>AxisIndex in MOTIF_CONFIG.CFG_MODE_AXS
  ● AUTO: Reading out the Data Layer node motion/axs and assigning the Axi‐
    sIndex in the found sequence
  ● GLOB_VAR: In the application, a list of MB_AXISIF_REF is defined and

    transferred to the program TE_AxisInterfaceMainProg. Refer to GlobalAx‐
    isDefines in the programming template "KinematicInterface and AxisInter‐
    face”.
  ● FILE: A list of axes and the respective axis number are defined in a JSON
    file.
    Exemplary JSON file section belonging to the axes:
    "axes": { "vAxis1": 4, "X_Axis": 1, "Y_Axis": 2, "Z_Axis": 3,
    "MoverX": 5, "MoverY": 6, "MoverZ": 7 }
    The example file "AxesKinematicsDefines.json" is in the "Utilities" folder in
    the CXA_MotionInterfaceUser library.
    Note the following:
    – The section starts with the keyword “axes”
    – Use quotes for the axis name. Note the case sensitivity
    – The axis index follows the colon
    – Recommendation: To check the syntax, use a JSON Validator from the
        Internet

    Adding an axis
An axis can be created in the user interface in the Motion section or created
from the PLC program for example.
Defined structural elements of the AxisInterface have to be initialized for an
added axis if required. This results automatically when using the programming
template "KinematicInterface and AxisInterface” once the “Running” state has
been reached. The assignment AxisName<>AxisIndex has to be supplemented
if MOTIF_CONFIG.CFG_MODE_AXS = GLOB_VAR or FILE is configured.
  Also refer to ⮫ Further information on page 507.

    Removing/renaming an axis
An existing axis can be deleted or renamed in the user interface in the
“Motion” section or via different interfaces.

  <If an axis is renamed, modify the access via the control and status structures
  “arAxisCtrl_gb[ChangedAxisName.AxisNo]" and "arAxisStatus_gb[ChangedAxis‐
  Name.AxisNo]" within the PLC program.
  The     assignment    AxisName<>AxisIndex      has    to    be    adjusted    if
  MOTIF_CONFIG.CFG_MODE_AXS = GLOB_VAR or FILE is configured.
  Also refer to ⮫ Further information on page 507.

    AxisInterface - Extensions
 The AxisInterface allows almost any AxisInterface extensions. Additional sub‐
 structures can also be added and existing substructures extended.

As an example, the following structural elements are programmed as user
extensions in the AxisCtrl structure:
● Admin: Extension of the existing substructure in the AxisCtrl structure
   – ReTriggerOpMode: Restart the operation mode set, e.g. start MoveRela‐
      tive with the same “Distance”
● SetupMode: Additional substructure in the AxisCtrl structure
   – JogPlus: Jog +
   – JogMinus: Jog -
   – Vel: Jog velocity
   – DynValues: Jog (deceleration) acceleration and jerk
   – JogIncr: TRUE ->Incremental jogging. A positive edge at JogPlus or Jog‐
      Minus jogs a step width
   – StepWidth: Step width for incremental jogging
The code for these extensions is in the actions of the TE_AxisInterface() func‐
tion block in the AxisInterfaceUser/POUS folder.
The related structures are in the AxisInterfaceUser/DUTs/Control and AxisIn‐
terfaceUser/DUTs/Status folders.
Own extensions can be added (refer to ⮫ AxisInterface - User extension).

## 19.4 KinematicInterface

### 19.4.1 Introduction and overview

The KinematicInterface pools and extends PLCopen motion function blocks
and provides an easy-to-operate interface for the kinematic functionality.
The KinematicInterface includes control signals and parameters for the var‐
ious operation modes of the kinematics.

Table 429: Program organization units of the KinematicInterface in the CXA_MotionInterface library
Field of application (folder in the library CXA_MotionInterface)
POUs                                              Description
KinInterface/POUs
⮫ Chapter MB_KinematicsInit on page 514           Used to initialize the KinematicInterface for each
                                                  kinematics. The function block has to be called
                                                  only once when the program is started or each
                                                  time the phase is switched from parameteriza‐
                                                  tion mode to the operating mode
⮫ Chapter MB_KinematicsInterfaceBase              Used to configure the KinematicInterface for
on page 516                                       each kinematics. The function block has to be
                                                  called cyclically (in the Motion cycle or slower
                                                  than the Motion cycle) as long as the user is in
                                                  the operating mode
KinInterface/DUTs
                                                  For information on the data structures, refer to
                                                  the ctrlX PLC Engineering library manager in
                                                  the CXA_MotionInterface library in the KinInter‐
                                                  face/DUTs folder
KinInterface/GlobalVariables
                                                  For information on the global variables, refer
                                                  to the ctrlX PLC Engineering library manager in
                                                  the CXA_MotionInterface library in the KinInter‐
                                                  face/GlobalVariables folder

The KinematicInterface is provided as programming template or as a stand‐
alone interface for the kinematic functionality.
If it is used with the programming template “MotionInterface” as “Kinemati‐
cInterface and AxisInterface”, the user does not have to deal with instance
calls of the function blocks in the project. This functionality is completely
integrated into the template - the user just needs to write a few lines of code.
If the KinematicInterface is used as standalone functionality, the instances of
both function blocks have to be created for each kinematics.
The KinematicInterface uses the AxisInterface internally. It is thus required to
call the AxisInterface as well.

Table 430: Program organization units of the KinematicInterface in the CXA_MotionInterfaceUser
library
Field of application (folder in the library CXA_MotionInterfaceUser)
POUs                                              Description
KinInterfaceUser/POUs
TE_KinematicsInitAllKinematics               KinematicInterface initialization for all kine‐
                                             matics. Calls ⮫ MB_KinematicsInit internally for
                                             each kinematics
TE_KinematicsInterface extended ⮫ MB_Kinema‐ The user can extend the KinematicInterface for
ticsInterfaceBase                            a single kinematics (⮫ KinematicInterface - User
                                             extension). The function block has to be called
                                             cyclically (in the Motion cycle or slower than the
                                             Motion cycle) as long as the user is in the oper‐
                                             ating mode
TE_KinInterfaceMainProg                      When the “Running” mode is reached, the main
                                             program executes the initialization. After a suc‐
                                             cessful initialization, TE_KinematicsInterface is
                                             called for all kinematics
                                             For more information, refer to the ctrlX
                                             PLC Engineering library manager in the
                                             CXA_MotionInterfaceUser library in the KinInter‐
                                             faceUser/POUs folder
KinInterfaceUser/DUTs
                                                  For information on the data structures, refer to
                                                  the ctrlX PLC Engineering library manager in the
                                                  CXA_MotionInterfaceUser library in the KinInter‐
                                                  faceUser/DUTs folder
KinInterfaceUser/GlobalVariables
Global_Kinematics_Interface                       The actual KinematicInterface with the arrays
                                                  arKinCtrl_gb and arKinStatus_gb can be found
                                                  here. The other variables are used internally and
                                                  by visualizations.
                                                  Also refer to ⮫ Chapter 19.4.4 KinematicInterface
                                                  - Global variables on page 543
KinInterfaceUser/Visualizations
⮫ Chapter Introduction and overview               Commission visualizations, e.g. to jog axes
on page 548
KinInterfaceUser/_KinifDebug

If problems arise, use the POUs to record         For information on this debug feature, refer
the sequence of the Motion commands in this       to the ctrlX PLC Engineering library manager
folder.                                           in the library CXA_MotionInterfaceUser in the
                             folder KinInterfaceUser/_KinifDebug. For a “How
                             To”, refer to the documentation of the program
                             "TE_KinIfDebugProg"
KinInterfaceUser/_Examples
PROGRAM Example_KinIfApplicationPart              Example code to apply the KinematicInterface.
                             This example code is also included in the pro‐
                             gramming template "KinematicInterface and Axi‐
                             sInterface"
Utilities/ConfigFileRead
TE_ConfigFileRead                                 Auxiliary function block to analyze the JSON file
                             when MOTIF_CONFIG.CFG_MODE_KIN = FILE is
                             set. Internally used by TE_KinematicsInitAllKine‐
                             matics.

Project planning note/runtime requirement
The KinematicInterface function block is called for each kinematics of the Kin‐
ematicInterface. This call requires PLC runtime. This runtime varies depending
on the kinematic type and the kinematic mode. Additionally, the function
block of the AxisInterface has to be called for each axis.

Table 431: Assignment: User interface to the KinematicInterface data structure:
User interface       Type                         Description
arKinCtrl_gb[ ]      TE_KINEMATICS_CON‐           Control structure, including command values
                     TROL_TYPE01                  and variables to activate operation modes
arKinStatus_gb[ ]    TE_KINE‐                     Status structure including diagnostic informa‐
                     MATICS_STATUS_TYPE01         tion, acknowledgements for the operation
                                                  modes, actual values and status information on
                                                  the rexroth-motion app.

Use the GroupNo of the MB_AXESGROUPIF_REF structure as an index for the
array, e.g. arKinCtrl_gb[Mover.GroupNo].Admin. etc.

EnableCyclicScanning
The element arKinCtrl_gb[ ].Admin.Config.EnableCyclicScanning can control
the internal handling of certain command values.
If EnableCyclicScanning is set to TRUE, some command values of the
arKinCtrl_gb[ ] structure are scanned cyclically and applied immediately when
a value changes.

−   While activating an operation mode (.Admin._OpMode), all input data is
    read regardless of the setting of the "EnableCyclicScanning" input
− If EnableCyclicScanning = TRUE, all input data highlighted in green is read
    cyclically. Thus, any value change is read immediately after activating an
    operation mode
− In contrast to that, all input data highlighted in blue is not scanned cycli‐
    cally. Thus, the values are only read if an operation mode is activated
− Data becomes consistent when EnableCyclicScanning (FALSE→Write
    data→TRUE) is used
For commissioning purposes, various IndraLogic visualizations are provided
in the library CXA_MotioninterfaceUser. They are based on the structural ele‐
ments described in this section.

Required changes in the user code compared to the previous versions
Changes in the version 1.8
● The SetupMode is now implemented as own operation mode called "Mode‐
  CoordSetup".
  Thus, "arKinCtrl_gb[].SetupMode.Enable" and "arKinStatus_gb[].Setup‐
  Mode.EnableAck” are omitted

Table 432: Required code changes when updating to the current version
From version       Previous code version                     Replace by
                   arKinCtrl_gb[] control structure
1.8                SetupMode.Enable                          Admin._OpMode‐
                                                             Bits.MODE_COORD_SETUP
                   arKinStatus_gb[] control structure
1.8                SetupMode.EnableAck                       Admin._OpModeAck‐
                                                             Bits.MODE_COORD_SETUP

Changes and new information compared to the version for MLC

● Parts of the event-controlled KinematicInterface were applied (MB_Kine‐
  maticsInterfaceType12 function block). The structural elements are par‐
  tially implemented as properties. The substructures are then imple‐
  mented as function blocks instead of structures to use properties. The
  arKinCtrl_gb[].Admin.mTriggerMoveCmd() method is implemented into a
  structure
● The operation mode selection arKinCtrl_gb[].Admin._OpMode is not imple‐
  mented as UNION anymore, but as properties. When controlling using bits
  (_OpModeBits), a multiple selection is not possible anymore
● Rarely used elements of arKinCtrl_gb[].Admin were moved to
  arKinCtrl_gb[].Admin.Config (see table below)
● Values of the type REAL are generally defined in the structures as LREAL
● There is no KinData[] structure. For the current actual values and some
  status bits, go to arKinStatus_gb[].Data
Table 433: Required code changes when porting MLC (Search/Replace).
Code MLC                                              Replace by
Control structure arKinCtrl_gb[]
_OpMode.en                                            _OpMode
ModeCoordInterrupted                                  ModeCoordInterrupt
ModeCoordStopping                                     ModeCoordStandby
_OpMode.b                                             _OpModeBits
MODE_COORD_INTERRUPTED                                MODE_COORD_INTERRUPT
MODE_COORD_STOPPING                                   MODE_COORD_STANDBY
Admin.Group                                           Admin.Config.Group
Admin.DiagNbrRefreshTime                              Admin.Config.DiagNbrRefreshTime
Admin.EnableCyclicScanning                            Admin.Config.EnableCyclicScanning
CoordMode.Velocity                                    CoordMode.DynValues.Velocity
CoordMode.Acceleration                                CoordMode.DynValues.Acceleration
CoordMode.Deceleration                                CoordMode.DynValues.Deceleration
CoordMode.Jerk                                        CoordMode.DynValues.JerkAcc
                                                      CoordMode.DynValues.JerkDec
CoordMode.BlendingRadius                              CoordMode.BlendingStartD1
                                                      CoordMode.BlendingEndD2
SetupMode.Enable                                      Admin._OpModeBits.MODE_COORD_SETUP
SetupMode.Velocity[]                                  SetupMode.DynValues.Velocity
SetupMode.Acceleration[]                              SetupMode.DynValues.Acceleration
SetupMode.Deceleration[]                              SetupMode.DynValues.Deceleration
SetupMode.Jerk[]                                      SetupMode.DynValues.JerkAcc
                                                      SetupMode.DynValues.JerkDec

Code MLC                                            Replace by
SetupMode.Distance[]                                SetupMode.Increment
Control structure arKinStatus_gb[]
Admin.MODE_COORD_UNGROUPED                          Admin._OpModeAck‐
                             Bits.MODE_COORD_UNGROUPED
Admin.MODE_COORD_CONTINUE                           Admin._OpModeAckBits.MODE_COORD_CON‐
                             TINUE
Admin.MODE_COORD_INTERRUPTED                        Admin._OpModeAckBits.MODE_COORD_INTER‐
                             RUPT
Admin.MODE_COORD_EXTERNAL_FB                        Admin._OpModeAck‐
                             Bits.MODE_COORD_EXTERNAL_FB
Admin.MODE_COORD_POS_LIN_ABS                        Admin._OpModeAck‐
                             Bits.MODE_COORD_POS_LIN_ABS
Admin.MODE_COORD_POS_LIN_REL                        Admin._OpModeAck‐
                             Bits.MODE_COORD_POS_LIN_REL
Admin.MODE_COORD_STOPPING                           Admin._OpModeAck‐
                             Bits.MODE_COORD_STANDBY
SetupMode.EnableAck                                 Admin._OpModeAckBits.MODE_COORD_SETUP

This list of code changes is incomplete. The program code has to be checked
while porting.

### 19.4.2 KinematicInterface - Function blocks

MB_KinematicsInit
Brief description
The function block MB_KinematicsInit is used to initialize the KinematicInter‐
face for each kinematics.
The function block has to be called only once upon program start or each
time the mode is switched from “Configuration” to “Running”. It is already
implemented into the template “KinematicInterface and AxisInterface“.

Interface description

Table 434: Interface variables of the MB_KinematicsInit function block
I/O type           Name              Data type           Comment
VAR_INPUT          Execute           BOOL                Initialization start using a positive edge
                   KinName           STRING(15)          Name of the kinematics to be initialized
                   KinIndex          UINT                Index in the KinematicInterface structures

I/O type   Name                     Data type       Comment
VAR_OUTPUT Done                     BOOL            Set when the function block has completed
                              the processing
Active                BOOL            Set when the function block is active (not
                              in idle mode)
Error                 BOOL            It indicates that an error has occurred in
                              the function block instance
ErrorID               ERROR_CODE      Short note on the error cause
ErrorIdent            ERROR_STRUCT    Detailed error information
VAR_IN_OUT    AdminCtrl             MB_KINE‐        Kinematic management

              MATICS_ADMINIS‐ arKinCtrl_gb[ ].Admin
              TRATION
AdminStatus           MB_KINE‐        Status of the kinematic management
              MATICS_ADMIN_ST arKinStatus_gb[ ].Admin
              ATUS
DataStatus            MB_KINE‐        State information of the kinematics
              MATICS_DATA     connect arKinStatus_gb[i].Data
DiagStatus            MB_KINE‐        Diagnostic information on the kinematics
              MATICS_DIAG‐    arKinStatus_gb[ ].Diag
              NOSIS
It is not possible to transfer the complete structures MB_Kinematics_Con‐
trol_Type01 and MB_Kinematics_Status_Type01 to the function block instead
of the individual structural elements AdminCtrl, AdminStatus, etc,.
This allows to make special extensions to the existing code for the user appli‐
cation.
Thus, the required elements of TE_KINEMATICS_CONTROL_TYPE01 and
TE_KINEMATICS_STATUS_TYPE01 are transferred as separate inputs.

Functional description
Table 435: Initialized structural elements of the MB_KinematicsInit function
block
Administration Control
AdminCtrl._OpMode           ModeCoordAB
AdminCtrl.Config.Group.Gro KinIndex
upNo
AdminCtrl.Config.Group.Kin‐ KinName
Name
Administration Status
AdminStatus.Active          TRUE for active kinematics
AdminStatus.Name            KinName
DataStatus.Units            Units are only read out once during the initiali‐
                            zation

Troubleshooting
The error codes of the internally used function blocks DL_ReadNode and
DL_BrowseNode are transferred to read Data Layer nodes.
The function block can generate the following error codes:

Table 436: Error codes of the MB_KinematicsInit function block
ErrorID                    Additional1       Additional2    Description
INPUT_RANGE_ERROR          16#0A0F0107       16#0C230140    String length KinName beyond the
                                                            valid range [1..15]
STATE_MACHINE_ERROR 16#0A0F0107              16#0C230141    Errors while processing the function
                                                            block
INPUT_RANGE_ERROR          16#0A0F0107       16#0C230142    Too many axes configured for this kin‐
                                                            ematics
INPUT_RANGE_ERROR          16#0A0F0107       16#0C230143    KinIndex beyond the valid range
                                                            [1..MB_KINIF_MAX_KIN_NUMBER]
INPUT_RANGE_ERROR          16#0A0F0107       16#0C230144    Invalid pointer arpAdminAxisCtrl_gb
                                                            for at least one axis

MB_KinematicsInterfaceBase
      Brief description
      The function block MB_KinematicsInterfaceBase is used to configure the Kine‐
      maticInterface for each kinematics.
      This function block has to be called cyclically (in the Motion cycle or slower
      than the Motion cycle) when the user is in “Running” mode. It is already
      implemented into the template "KinematicInterface and AxisInterface”.

      Interface description

Table 437: Interface variables of the MB_KinematicsInterfaceBase function block
I/O type  Name              Data type                     Comment
VAR_INPUT AdminCtrl         REFERENCE TO MB_KINE‐         Kinematic management
                            MATICS_ADMINISTRATION         arKinCtrl_gb[ ].Admin
               CoordCtrl   REFERENCE TO MB_KINE‐          Operation mode “Coordinated
                           MATICS_COORDINATED             Motion”
                                                          arKinCtrl_gb[ ].CoordMode
               AdminStatus REFERENCE TO MB_KINE‐          Status of the kinematic man‐
                           MATICS_ADMIN_STATUS            agement
                                                          arKinStatus_gb[ ].Admin
               DataStatus REFERENCE TO MB_KINEMATICS_DATA Actual values and status of the
                                                          kinematics
                                                          arKinStatus_gb[ ].Data
               DiagStatus REFERENCE TO MB_KINE‐           Status of the axis diagnostics
                           MATICS_DIAGNOSIS               arKinStatus_gb[ ].Diag

It is not possible to transfer the complete structures to the function block
via the input instead of individual structural elements such as AdminCtrl or
CoordCtrl.
This allows to make special extensions to the existing code for the user appli‐
cation.
Thus, the required elements of TE_Kinematics_Control_Type01 and TE_Kine‐
matics_Status_Type01 are transferred as separate inputs.
To optimize the performance, the structures are connected to REFERENCE TO
as VAR_INPUT instead of as VAR_IN_OUT. Thus, the inputs only have to be
initialized once. Thus, if the function block is called cyclically, the structures
do not have to be transferred.

The function block checks the inputs of arKinCtrl_gb[ ] and internally
generates the requested commands for the kinematics. The outputs of
arKinStatus_gb[ ] are updated depending on the result of this command.
For example, setting arKinCtrl_gb[ ].Admin._OpMode from ModeCoordAb to
ModeCoordPosLinAbs leads to the following sequence:
● All assigned axes are switched in COORDINATED_MOTION via the AxisInter‐
  face
● Enabling the function ML_KinEnable
● Wait for the acknowledgement that the kinematics is ready
● Enabling the function ML_KinMoveLinAbs with the command values of
  CoordModeCtrl
● Acknowledging the arKinStatus_gb[ ].Admin._OpModeAck to ModeCoord‐
  PosLinAbs (bit MODE_COORD_POS_LIN_ABS)
● Scanning the values in CoordModeCtrl.Position[] and re-enabling the
  ML_KinMoveLinAbs in the case of modifications

Troubleshooting
The error codes of the internally used function blocks (e.g. DL_ReadNode to
read the Data Layer node) and the internally used functions (e.g. ML_KinEn‐
able) are transferred.
The function block can generate the following error codes:
Table 438: Error codes of the MB_KinematicsInterfaceBase function block
ErrorID                      Additional1    Additional2      Description
INPUT_RANGE_ERROR            16#0A0F0107    16#0C230150      At least one of the function block
                                                             inputs is not initialized
DEVICE_ERROR                 16#0A0F0107    16#0C230151      Kinematics is in ErrorStop
STATE_MACHINE_ERROR          16#0A0F0107    16#0C230153      Errors while processing the function
                                                             block
INPUT_RANGE_ERROR            16#0A0F0107    16#0C230154      Invalid
                                                             AdminCtrl.Config.Group.GroupNo
                                                             input
OTHER_ERROR                  16#0A0F0107    16#0C230155      Error when grouping the kinematics
RESOURCE_ERROR               16#0A0F0107    16#0C230156      An operation mode was
                                                             selected in ModeCoordUn‐
                                                             grouped using the method
                                                             Ctrl.Admin.mTriggerMoveCmd()
IINPUT_INVALID_ERROR         16#0A0F0107    16#0C230157      In this variant, the function block does
                                                             not support the OpMode
INPUT_RANGE_ERROR            16#0A0F0107    16#0C230158      Global axis pointers are invalid
STATE_MACHINE_ERROR          16#0A0F0107    16#0C230159      Errors while processing the function
                                                             block - Reset

ErrorID                     Additional1    Additional2     Description
STATE_MACHINE_ERROR         16#0A0F0107    16#0C23015A     Errors while processing the function
                                      block - Stop

### 19.4.3 KinematicInterface - Operation modes

Introduction and overview
The following section describes the operation modes supported by the Kine‐
maticInterface basic type and the attributes that can be assigned.

There are three methods to activate an operation mode:
● Selection via ENUM values
  Assigning a value of the TYPE MB_KINEMATICS_MODE
  arKinCtrl_gb[ ].Admin._OpMode:
  arKinCtrl_gb[].Admin._OpMode:= ModeCoordPosLinAbs;
  or
  arKinCtrl_gb[].Admin._OpMode:= ModeCoordAB;
● Using the bit access
  Setting a bit using the bit access functionality.
  arKinCtrl_gb[].Admin._OpModeBits.MODE_COORD_POS_LIN_ABS:=
  TRUE;
  Deleting the “_OpMode” is also possible using the bit access functionality.
  arKinCtrl_gb[].Admin._OpModeBits.MODE_COORD_POS_LIN_ABS :=
  FALSE;
  MODE_COORD_AB is enabled by the bit deletion.
  Also possible: arKinCtrl_gb[].Admin._OpModeBits.MODE_COORD_AB :=
  TRUE;
● Using the Ctrl.Admin.mTriggerMoveCmd() method
  Also refer to "DemoKinematicsCommands” in the template "KinematicInter‐
  face and AxisInterface”.
  This method issues the command to the Motion firmware in this call. To
  ensure a proper function, the kinematics has to be enabled, e.g. query
  ModeCoordStandby and CmdDone.
  Call: arKinCtrl_gb[uiKinIndex].Admin.mTriggerMoveCmd(_OpMode:=
  ModeCoordPosLinAbs, Buffered:=FALSE, UserID:='my text');
  – Transfer parameter "_Opmode" = Value of TYPE MB_KINEMATICS_MODE
  – Transfer parameter "Buffered" = TRUE (Default): The previous command
     becomes active after the previous command has been completed
  – Transfer parameter "Buffered" = FALSE: The previous command is
     aborted
  – Transfer parameter "UserID" = string (max. 25 bytes). Transferred as
     “Source” when calling the Motion commands. In case of errors, the
     source of the command can thus be identified.
  – Return value of the method: cmdID of the issued Motion command. If
     there is an error, 16#FFFFFFFFFFFFFFFF is returned.

The commands issued in the KinematicInterface are buffered by default.
In contrast, the commands issued in the AxisInterface are not buffered by
default.
Non-buffered     commands      can     also  be     issued    with    the
arKinCtrl_gb[uiKinIndex].Admin.mTriggerMoveCmd() method. Thus, a new
motion command (Buffered = FALSE) can cancel the current commands.

Before an operation mode can be activated, assign values to every attribute
first. All attributes are provided with default values. Some are provided with
values unequal to zero while others are defined as 0. Due to the special
demands, a value has to be assigned to them.

Only attributes (e.g. position, velocity) that are used or whose default values
were changed have to be declared before the current operation mode is
changed.

The status acknowledgement (arKinStatus_gb[].Admin. for an operation
mode is implemented as follows.

Example:
−   The status acknowledgement returns TRUE only if the command for
    switching the kinematics to the absolute linear positioning mode was exe‐
    cuted:
    arKinStatus_gb[].Admin.MODE_COORD_POS_LIN_ABS
−   The status acknowledgement is immediately reset when issuing a new
    command:
    arKinStatus_gb[].Admin.CmdDone
    The positioning operation mode is activated:
    arKinCtrl_gb[].Admin._OpMode.b.MODE_COORD_POS_LIN_ABS
    The output is set to TRUE if the kinematics switches to the positioning
    mode and starts to move:
    arKinStatus_gb[].Admin.MODE_COORD_POS_LIN_ABS
    If the kinematics reaches the target coordinates, the status acknowledge‐
    ment is set:
    arKinStatus_gb[].Admin.CmdDone

Operation modes “Kinematic ready”
Activating this operation mode switches the kinematics to GroupDisabled and
switches off the torque at all assigned axes.
The following command activates the operation mode:
arKinCtrl_gb[].Admin._OpMode:= ModeCoordAB;
or
arKinCtrl_gb[].Admin._OpModeBits.MODE_COORD_AB:= TRUE;
The KinematicInterface uses the function ML_KinDisable (CXA_Motion library)
and the operation mode ModeAb of the AxisInterface for switching.

Table 439: Attributes of the operation mode “Kinematic ready”
Element           Name                          Type                     Default          Cycli‐
                                                                                          cally
                                                                                          scanned
arKinStatus_gb[] Admin._OpModeAck‐     BOOL                                               Omitted
                 Bits.MODE_COORD_UNGRO
                 UPED

Operation mode “Kinematic halt"
Activating this operation mode switches the kinematics to GroupDisabled and
switches all assigned axes to AH (drive halt), but maintaining the torque.
The following command activates the operation mode:
arKinCtrl_gb[].Admin._OpMode := ModeCoordAH;
or
arKinCtrl_gb[].Admin._OpModeBits.MODE_COORD_AH := TRUE;

       The KinematicInterface uses the function ML_KinDisable (CXA_Motion library)
       and the operation mode ModeAH of the AxisInterface for switching.

Table 440: Attributes of the operation mode “Kinematic halt”
Element                Name                                    Type                           Default          Cycli‐
arKinStatus_gb[] Admin._OpModeAck‐     BOOL                                                                    Omitted
                 Bits.MODE_COORD_UNGRO
                 UPED
                 Admin.CmdDone         BOOL                                                                    Omitted

Operation mode "Setup"
    In the "Setup" operation mode, select whether the entire kinematics is moved
    along a specified direction vector or whether the individual coordinates are
    moved step by step (over a specific distance) or continuously within the speci‐
    fied dynamic limits.
    The maximum traversing length is always limited by the configured permis‐
    sible ranges of the kinematic axes. If the current position is beyond the config‐
    ured, permissible axis ranges, the axis can move towards the permitted range,
    but not beyond.
    The following command activates the operation mode:
       arKinCtrl_gb[].Admin._OpMode:= ModeCoordSetup;
       or
       arKinCtrl_gb[].Admin._OpModeBits. MODE_COORD_SETUP:= TRUE;
       The following acknowledgement has to follow the operation mode command.
       It returns the respective commanded operation mode or TRUE:
       arKinStatus_gb[].Admin._OpModeAck                                       =
       MB_KINEMATICS_MODE.ModeCoordSetup;
       arKinStatus_gb[].Admin._OpModeAckBits.MODE_COORD_SETUP;
       The KinematicInterface uses the operation mode ModeCoordinated of the Axi‐
       sInterface and the functions ML_KinJogIncr and ML_KinJogCont (CXA_Motion
       library) for switching.

Table 441: Attributes of the "Setup" operation mode
Element            Name                                 Type                                Standard            Cyclically

arKinCtrl_gb [ ]   SetupMode. JogMode                   TE_KINEMATICS_JOGMODE                                   No

SetupMode. JogPlus                   ARRAY [0..(MB_KINIF_NOF_POINT-1)]                       No
                                     OF BOOL

SetupMode. JogMinus                  ARRAY [0..(MB_KINIF_NOF_POINT-1)]                       No
                                     OF BOOL

SetupMode. Increment                 LREAL                               1.0                 No

SetupMode. DirectionVector           ARRAY [0..(MB_KINIF_NOF_POINT-1)] MB_KINIF_NOF_POINT    No
                                     OF LREAL                            (0.0)

SetupMode. JogVectorPlus             BOOL

SetupMode. JogVectorMinus            BOOL

SetupMode. DynValues.Velocity        LREAL                               1.0                 No

SetupMode. DynValues.Acceleration    LREAL                               1.0                 No

SetupMode. DynValues. Deceleration   LREAL                               1.0                 No

SetupMode. JerkAcc                   LREAL                               0.0                 No

Element              Name                           Type                        Standard            Cyclically

SetupMode. JerkDec             LREAL                       0.0

arKinStatus_gb [ ]   Admin._OpModeAckBits.          BOOL                                            Not appli‐
MODE_COORD_SETUP                                                               cable

The attribute "SetupMode. JogMode" selects incremental or continuous jog
mode. The incremental jog mode uses "SetupMode. Increment" step width.
If "SetupMode. JogVectorPlus" or "SetupMode. JogMinus" are set to TRUE,
jogging is triggered along the vector of direction either in positive or negative
direction. "SetupMode. DirectionVector" is the direction vector to be used.

Each element in the input field "SetupMode. JogPlus" or "SetupMode. Jog‐
Minus" has its respective coordinate. If neither "SetupMode.JogVectorPlus"
nor "SetupMode.JogVectorMinus" is set, depending on the value of "Setup‐
Mode. JogPlus" or "SetupMode. "JogMinus": The jog command is triggered at
the selected coordinate with the highest priority (plus before minus, in order
within the same array).
"SetupMode.DynValues" is used as dynamic limit value during jogging.

Operation mode “Absolute linear positioning”
Activating this operation mode causes an absolute linear motion to previously
specified target coordinates.
The following command activates the operation mode:
arKinCtrl_gb[].Admin._OpMode := ModeCoordPosLinAbs;
or
arKinCtrl_gb[].Admin._OpModeBits.MODE_COORD_POS_LIN_ABS              :=
TRUE;
The following acknowledgement has to follow the operation mode command.
It returns TRUE when the kinematics reached the target coordinates:
arKinStatus_gb[].Admin.CmdDone
In the "ModeCoordPosLinAbsl" control mode, the new function "ML_KinMo‐
veLinEx" replaces the function "ML_KinMoveLinAbs". The additional attribute
"ABS_VALUE" is set for all axes; this attribute cannot be selected. In addition,
the parameters arKinCtrl_gb[].CoordMode.KinCmdOption.ActivateKinPosPair
and arKinCtrl_gb[].CoordMode.KinCmdOption.stKineTargetPos are added for
the specified kinematic position. This is supported by the "CXA_MotionInter‐
face 4.6.3.0" library and is also compatible with versions prior to "CXA_Motio‐
nInterface 4.6.3.0."
The KinematicInterface uses the "ModeCoordinated" operating mode of the
AxisInterface and is toggled using the ML_KinEnable and ML_KinMoveLinEx
(or ML_KinMoveLinAbs) functions from the CXA_Motion library.

Table 442: Attributes of the operation mode “Absolute linear positioning”
Element                  Name                              Type                  Standard          Cycli‐
arKinCtrl_gb[ ]          CoordMode.Point[0..15]            LREAL                 0.0               Yes
                         CoordMode.Dyn‐                    LREAL                 1.0               No
                         Values.Velocity
                         CoordMode.Dyn‐                    LREAL                 1.0               No
                         Values.Acceleration
                         CoordMode.Dyn‐                    LREAL                 1.0               No
                         Values.Deceleration

Element            Name                         Type                    Standard         Cycli‐
                                                                      cally
                                                                      scanned
CoordMode.DynValues.Jer‐     LREAL                   0.0              No
kAcc
CoordMode.Dyn‐               LREAL                   0.0              No
Values.JerkDec
CoordMode.CoordSystem        MB_KIN_COORD_SYS        MB_KIN_COOR No
                                                     D_SYS.PCS
CoordMode.PosDirA‐           ML_MEANINGATTRI‐        ABS_VALUE   No
sync.Attribute[0..24]        BUTE
CoordMode.KinCmdOp‐          ML_MEANING              X,Y,Z,AX7...AX1 No
tion.stKineTargetPos.Target‐                         6,X,X...
Meaning[0..24]
CoordMode.KinCmdOp‐          LREAL                   0.0              Yes
tion.stKineTargetPos.Target‐
Value[0..24]
CoordMode.KinCmdOp‐          UINT                    0                No
tion.stKineTargetPos.Target‐
Size
CoordMode.KinCmdOp‐          BOOL                    FALSE            No
tion.ActivateKinPosPair
arKin‐             Admin._OpModeAck bits.       BOOL                                     Not
Status_gb[ ]       MODE_COORD_POS_LIN_AB                                                 appli‐
S                                                                     cable
Admin.CmdDone                BOOL                                     Not
                                                                      appli‐
                                                                      cable

  Parameter description
  arKinCtrl_gb[].CoordMode.KinCmdOption.ActivateKinPosPair
  is           used            to           enable    or    disable
  arKinCtrl_gb[].CoordMode.KinCmdOption.stKineTargetPos in order to
  control the target position with specific meanings.
  If CoordMode.KinCmdOption.ActivateKinPosPair is set to FALSE, the fol‐
  lowing applies:
  ● This mode supports Cartesian kinematics and up to 16 axes within a single
    kinematic group.
  ● The target position can be specified using
    arKinCtrl_gb[].CoordMode.Point[].
  ● arKinCtrl_gb[].CoordMode.KinCmdOption.stKineTargetPos is disa‐
    bled.
  ● The number of entries at the specified target position is automatically
    determined from the kinematics for all grouped axes.
  ● The meaning of the specified target position is based on the default values
    and cannot be selected.
  If CoordMode.KinCmdOption.ActivateKinPosPair is set to TRUE, the fol‐
  lowing applies:
  ● arKinCtrl_gb[].CoordMode.Point[] is disabled.
  ● Position values, their meanings, and the number of
    entries in the specified target position are entered via
    arKinCtrl_gb[].CoordMode.KinCmdOption.stKineTargetPos.

Operation mode “Relative linear positioning”
  Activating this operation mode causes a relative linear motion to previously
  specified target coordinates by adding the CoordMode.Point[] to the current
  target coordinates.
  The following command activates the operation mode:
  arKinCtrl_gb[].Admin._OpMode := ModeCoordPosLinRel;
  or
  arKinCtrl_gb[].Admin._OpModeBits.MODE_COORD_POS_LIN_REL              :=
  TRUE;
  The following acknowledgement has to follow the operation mode command.

  It returns TRUE when the kinematics reached the target coordinates:
  arKinStatus_gb[].Admin.CmdDone
  In the "ModeCoordPosLinRel" control mode, the new function "ML_Kin‐
  MoveLinEx" replaces the function "ML_KinMoveLinRel." The additional
  attribute "INCR_VALUE" is set for all axes; this attribute cannot be
  selected. In addition, for the specified kinematic position, the param‐
  eters “arKinCtrl_gb[].CoordMode.KinCmdOption. ActivateKinPosPair and
  arKinCtrl_gb[].CoordMode.KinCmdOption.stKineTargetPos have been added
  for the specified kinematic position. This is supported by the CXA_Motio‐
  nInterface 4.6.3.0 library and is also compatible with versions earlier than
  CXA_MotionInterface 4.6.3.0.
  The KinematicInterface uses the "ModeCoordinated" operating mode of the
  AxisInterface and is switched on and off using the CXA_Motion library func‐
  tions ML_KinEnable and ML_KinMoveLinEx (version 4.6.3.0 and later) or
  ML_KinMoveLinRel (prior to version 4.6.3.0).

Table 443: Attributes of the operation mode “Relative linear positioning”
Element            Name                           Type                  Standard          Cycli‐
                                                                                          cally
                                                                                          scanned
arKinCtrl_gb[ ]    CoordMode.Point[0..15]         LREAL                 0.0               Yes
                   CoordMode.Dyn‐                 LREAL                 1.0               No
                   Values.Velocity
                   CoordMode.Dyn‐                 LREAL                 1.0               No
                   Values.Acceleration
                   CoordMode.Dyn‐                 LREAL                 1.0               No
                   Values.Deceleration
                   CoordMode.DynValues.Jer‐       LREAL                 0.0               No
                   kAcc
                   CoordMode.Dyn‐                 LREAL                 0.0               No
                   Values.JerkDec
                   CoordMode.CoordSystem          MB_KIN_COORD_SYS      MB_KIN_COOR No
                                                                        D_SYS.PCS
                   CoordMode.PosDirA‐             ML_MEANINGATTRI‐      ABS_VALUE   No
                   sync.Attribute[0..24]          BUTE
                   CoordMode.KinCmdOp‐            ML_MEANING            X,Y,Z,AX7...AX1 No
                   tion.stKineTargetPos.Target‐                         6,X,X...
                   Meaning[0..24]
                   CoordMode.KinCmdOp‐            LREAL                 0.0               Yes
                   tion.stKineTargetPos.Target‐
                   Value[0..24]

Element            Name                         Type                    Standard         Cycli‐
                                                                    cally
                                                                    scanned
CoordMode.KinCmdOp‐          UINT                    0                No
tion.stKineTargetPos.Target‐
Size
CoordMode.KinCmdOp‐          BOOL                    FALSE            No
tion.ActivateKinPosPair
arKin‐             Admin._OpModeAck bits.       BOOL                                     Not
Status_gb[ ]       MODE_COORD_POS_LIN_RE                                                 appli‐
L                                                                     cable
Admin.CmdDone                BOOL                                     Not
                                                                    appli‐
                                                                    cable

Parameter description:
arKinCtrl_gb[].CoordMode.KinCmdOption.ActivateKinPosPair
is           used            to           enable    or    disable
arKinCtrl_gb[].CoordMode.KinCmdOption.stKineTargetPos in order to
control the target position with specific meanings.
If CoordMode.KinCmdOption.ActivateKinPosPair is set to FALSE, the fol‐
lowing applies:
● This mode supports Cartesian kinematics and up to 16 axes within a single
  kinematic group.
● The target position can be specified using
  arKinCtrl_gb[].CoordMode.Point[].
● arKinCtrl_gb[].CoordMode.KinCmdOption.stKineTargetPos is disa‐
  bled.
● The number of entries at the specified target position is automatically
  determined from the kinematics for all grouped axes.
● The meaning of the specified target position is based on the default values
  and cannot be selected.
If CoordMode.KinCmdOption.ActivateKinPosPair is set to TRUE, the fol‐
lowing applies:
● arKinCtrl_gb[].CoordMode.Point[] is disabled.
● Position values, their meanings, and the number of
  entries at the specified target position are entered via
  arKinCtrl_gb[].CoordMode.KinCmdOption.stKineTargetPos.

Operation mode “Absolute direct positioning”
Activating this operation mode causes an absolute motion to previously
specified target coordinates without considering how the target position is
reached.
The following command activates the operation mode:
arKinCtrl_gb[].Admin._OpMode := ModeCoordPosDirAbs;
or
arKinCtrl_gb[].Admin._OpModeBits.MODE_COORD_POS_DIR_ABS               :=
TRUE;
The following confirmation has to follow the operation mode command and
returns TRUE when the kinematics have reached the target coordinates:
arKinStatus_gb[].Admin.CmdDone

   In the "ModeCoordPosDirAbs" control mode, the new "ML_KinMoveDir‐
   ectEx" function replaces the "ML_KinMoveDirectAbs" function. The additional
   attribute "ABS_VALUE" is set for all axes; this attribute cannot be selected.
   For the specified kinematic position, "arKinCtrl_gb[].CoordMode.KinCmdOp‐
   tion.ActivateKinPosPair" and "arKinCtrl_gb[].CoordMode.KinCmdOption.stKi‐
   neTargetPos" are added. This is supported by the "CXA_MotionInterface
   4.6.3.0" library and is also compatible with versions prior to "CXA_MotionIn‐
   terface 4.6.3.0."
   The KinematicInterface uses the "ModeCoordinated" operating mode of the
   AxisInterface and is switched on and off using the CXA_Motion library func‐
   tions ML_KinEnable and ML_KinMoveDirectEx (version 4.6.3.0 and later) or

   ML_KinMoveDirectAbs (prior to version 4.6.3.0).

Table 444: Attributes of the operation mode “Absolute direct positioning”
Element           Name                         Type                     Standard         Cycli‐
                                                                                         cally
                                                                                         scanned
arKinCtrl_gb[ ]   CoordMode.Point[0..15]       LREAL                    0.0              Yes
                  CoordMode.Dyn‐               LREAL                    1.0              No
                  Values.Velocity
                  CoordMode.Dyn‐               LREAL                    1.0              No
                  Values.Acceleration
                  CoordMode.Dyn‐               LREAL                    1.0              No
                  Values.Deceleration
                  CoordMode.DynValues.Jer‐     LREAL                    0.0              No
                  kAcc
                  CoordMode.Dyn‐               LREAL                    0.0              No
                  Values.JerkDec
                  CoordMode.CoordSystem        MB_KIN_COORD_SYS         MB_KIN_COOR No
                                                                        D_SYS.PCS
                  CoordMode.PosDirA‐           ML_MEANINGATTRI‐         ABS_VALUE   No
                  sync.Attribute[0..24]        BUTE
                  CoordMode.KinCmdOp‐          ML_MEANING               X,Y,Z,AX7...AX1 No
                  tion.stKineTargetPos.Target‐                          6,X,X...
                  Meaning[0..24]
                  CoordMode.KinCmdOp‐          LREAL                    0.0              Yes
                  tion.stKineTargetPos.Target‐
                  Value[0..24]
                  CoordMode.KinCmdOp‐          UINT                     0                No
                  tion.stKineTargetPos.Target‐
                  Size
                  CoordMode.KinCmdOp‐          BOOL                     FALSE            No
                  tion.ActivateKinPosPair
arKin‐            Admin._OpModeAck bits.       BOOL                                      Not
Status_gb[ ]      MODE_COORD_POS_DIR_AB                                                  appli‐
                  S                                                                      cable
                  Admin.CmdDone                BOOL                                      Not
                                                                                         appli‐
                                                                                         cable

Parameter description:
arKinCtrl_gb[].CoordMode.KinCmdOption.ActivateKinPosPair
is           used           to   enable           or           disable
arKinCtrl_gb[].CoordMode.KinCmdOption.stKineTargetPos              and
arKinCtrl_gb[].CoordMode.DynValues in order to control the target posi‐
tion using specific meanings.
If CoordMode.DynValues is enabled for the ModeCoordPosDirAbs command,
each value in DynValues has to be between 0.001 and 1.0. A value of 1.0
means that the maximum configured axis dynamics are used for point-to-point
motion. Otherwise, the axes' motion limit values apply, which can result in a
very fast motion.
If CoordMode.KinCmdOption.ActivateKinPosPair is set to FALSE, the fol‐
lowing applies:
● This mode supports Cartesian kinematics and up to 16 axes within a single
  kinematic group.
● The target position can be specified using arKinCtrl_gb[].Coor‐
  dMode.Point[].
● arKinCtrl_gb[].CoordMode.KinCmdOption.stKineTargetPos and
  arKinCtrl_gb[].CoordMode.DynValues are disabled.
● The number of entries at the specified target position is automatically
  determined from the kinematics for all grouped axes.
● The meaning of the specified target position is based on the default values
  and cannot be selected.
● The kinematic system reaches its target position as quickly as possible,
  with the maximum configured dynamics determining the motion.
If CoordMode.KinCmdOption.ActivateKinPosPair is set to TRUE, the fol‐
lowing applies:
● arKinCtrl_gb[].CoordMode.Point[] is disabled.
● Position values, their meanings, and the number of
  entries at the specified target position are entered via
  arKinCtrl_gb[].CoordMode.KinCmdOption.stKineTargetPos.
● arKinCtrl_gb[].CoordMode.DynValues is disabled.

Operation mode “Relative direct positioning”
Enabling this operating mode triggers a relatively linear motion toward prede‐
fined target coordinates by adding the values from CoordMode.Point[] or
CoordMode.KinCmdOption.stKineTargetPos.TargetValue[] to the current
target coordinates. This does not take into account how the target position is
reached.
The following command activates the operation mode:
arKinCtrl_gb[].Admin._OpMode := ModeCoordPosDirRel;
or
arKinCtrl_gb[].Admin._OpModeBits.MODE_COORD_POS_DIR_REL               :=
TRUE;
The following confirmation has to follow the operation mode command and
returns TRUE when the kinematics have reached the target coordinates:
arKinStatus_gb[].Admin.CmdDone

   In the "ModeCoordPosDirRel" control mode, the new "ML_KinMoveDir‐
   ectEx" function replaces the "ML_KinMoveDirectRel" function. The additional
   attribute "INCR_VALUE" is set for all axes; this attribute cannot be selected.
   For the specified kinematic position, "arKinCtrl_gb[].CoordMode.KinCmdOp‐
   tion.ActivateKinPosPair" and "arKinCtrl_gb[].CoordMode.KinCmdOption.stKi‐
   neTargetPos" are added. This is supported by the CXA_MotionInterface 4.6.3.0
   library and is also compatible with versions earlier than CXA_MotionInterface
   4.6.3.0.
   The KinematicInterface uses the "ModeCoordinated" operating mode of the
   AxisInterface and is switched on and off using the CXA_Motion library func‐
   tions ML_KinEnable and ML_KinMoveDirectEx (version 4.6.3.0 and later) or

   ML_KinMoveDirectRel (prior to version 4.6.3.0).

Table 445: Attributes of the operation mode “Relative direct positioning”
Element           Name                          Type                    Standard         Cycli‐
                                                                                         cally
                                                                                         scanned
arKinCtrl_gb[ ]   CoordMode.Point[0..15]        LREAL                   0.0              Yes
                  CoordMode.Dyn‐                LREAL                   1.0              No
                  Values.Velocity
                  CoordMode.Dyn‐                LREAL                   1.0              No
                  Values.Acceleration
                  CoordMode.Dyn‐                LREAL                   1.0              No
                  Values.Deceleration
                  CoordMode.DynValues.Jer‐      LREAL                   0.0              No
                  kAcc
                  CoordMode.Dyn‐                LREAL                   0.0              No
                  Values.JerkDec
                  CoordMode.CoordSystem         MB_KIN_COORD_SYS        MB_KIN_COOR No
                                                                        D_SYS.PCS
                  CoordMode.PosDirA‐           ML_MEANINGATTRI‐         ABS_VALUE   No
                  sync.Attribute[0..24]        BUTE
                  CoordMode.KinCmdOp‐          ML_MEANING               X,Y,Z,AX7...AX1 No
                  tion.stKineTargetPos.Target‐                          6,X,X...
                  Meaning[0..24]
                  CoordMode.KinCmdOp‐          LREAL                    0.0              Yes
                  tion.stKineTargetPos.Target‐
                  Value[0..24]
                  CoordMode.KinCmdOp‐          UINT                     0                No
                  tion.stKineTargetPos.Target‐
                  Size
                  CoordMode.KinCmdOp‐          BOOL                     FALSE            No
                  tion.ActivateKinPosPair
arKin‐            Admin._OpModeAck bits.       BOOL                                      Not
Status_gb[ ]      MODE_COORD_POS_DIR_RE                                                  appli‐
                  L                                                                      cable
                  Admin.CmdDone                BOOL                                      Not
                                                                                         appli‐
                                                                                         cable

Parameter description:
arKinCtrl_gb[].CoordMode.KinCmdOption.ActivateKinPosPair
is           used           to   enable           or           disable
arKinCtrl_gb[].CoordMode.KinCmdOption.stKineTargetPos              and
arKinCtrl_gb[].CoordMode.DynValues in order to control the target posi‐
tion using specific meanings.
If CoordMode.DynValues is enabled for the ModeCoordPosDirRel command,
each value in DynValues has to be between 0.001 and 1.0. A value of 1.0
means that the maximum configured axis dynamics are used for point-to-point
motion. Otherwise, the axes' motion limit values apply, which can result in a
very fast motion.
If CoordMode.KinCmdOption.ActivateKinPosPair is set to FALSE, the fol‐
lowing applies:
● This mode supports Cartesian kinematics and up to 16 axes within a single
  kinematic group.
● The target position can be specified using arKinCtrl_gb[].Coor‐
  dMode.Point[].
● arKinCtrl_gb[].CoordMode.KinCmdOption.stKineTargetPos and
  arKinCtrl_gb[].CoordMode.DynValues are disabled.
● The number of entries at the specified target position is automatically
  determined from the kinematics for all grouped axes.
● The meaning of the specified target position is based on the default values
  and cannot be selected.
● The kinematic system reaches its target position as quickly as possible,
  with the maximum configured dynamics determining the motion.
If CoordMode.KinCmdOption.ActivateKinPosPair is set to TRUE, the fol‐
lowing applies:
● arKinCtrl_gb[].CoordMode.Point[] is disabled.
● Position values, their meanings, and the number of
  entries at the specified target position are entered via
  arKinCtrl_gb[].CoordMode.KinCmdOption.stKineTargetPos.
● arKinCtrl_gb[].CoordMode.DynValues is disabled.

"Asynchronous direct positioning” operation mode
Enabling this operating mode triggers an asynchronous motion to predefined
target coordinates, without taking into account how the target position is
reached. All axes start simultaneously, but the motion is not synchronous.
The following command activates the operation mode:
arKinCtrl_gb[].Admin._OpMode := ModeCoordPosDirAsync;
or
arKinCtrl_gb[].Admin._OpModeBits.MODE_COORD_POS_DIR_ASYNC:=TRUE
;
The following confirmation has to follow the operation mode command and
returns TRUE when the kinematics have reached the target coordinates:
arKinStatus_gb[].Admin.CmdDone
The kinematic interface uses the "ModeCoordinated" operating mode of the
AxisInterface, as well as the ML_KinEnable and ML_KinMoveDirectAsyncEx
functions (CXA_Motion library), to switch modes.

Table 446: Attributes of the "Asynchronous direct positioning" operation mode
Element           Name                          Type                     Standard         Cycli‐
                                                                                          cally
                                                                                          scanned
arKinCtrl_gb[ ]   CoordMode.Point[0..15]        LREAL                    0.0              Yes
                  CoordMode.Dyn‐                LREAL                    1.0              No
                  Values.Velocity
                  CoordMode.Dyn‐                LREAL                    1.0              No
                  Values.Acceleration
                  CoordMode.Dyn‐                LREAL                    1.0              No

Values.Deceleration
CoordMode.DynValues.Jer‐      LREAL                    0.0              No
kAcc
CoordMode.Dyn‐                LREAL                    0.0              No
Values.JerkDec
CoordMode.CoordSystem         MB_KIN_COORD_SYS         MB_KIN_COOR No
                                                       D_SYS.PCS
CoordMode.PosDirA‐           ML_MEANINGATTRI‐          ABS_VALUE   No
sync.Attribute[0..24]        BUTE
CoordMode.KinCmdOp‐          ML_MEANING                X,Y,Z,AX7...AX1 No
tion.stKineTargetPos.Target‐                           6,X,X...
Meaning[0..24]
CoordMode.KinCmdOp‐          LREAL                     0.0              Yes
tion.stKineTargetPos.Target‐
Value[0..24]
CoordMode.KinCmdOp‐          UINT                      0                No
tion.stKineTargetPos.Target‐
Size
CoordMode.KinCmdOp‐          BOOL                      FALSE            No
tion.ActivateKinPosPair
arKin‐            Admin._OpModeAck bits.       BOOL                                       Not
Status_gb[ ]      MODE_COORD_POS_DIR_AS                                                   appli‐
YNC                                                                     cable
Admin.CmdDone                BOOL                                       Not
                                                                        appli‐
                                                                        cable

   Parameter description:
   ● arKinCtrl_gb[ ].CoordMode.PosDirAsync.Attribute defines addi‐
     tional attributes that clarify the meaning of a requested kinematic position.
   ● If DynValues are enabled for the ModeCoordPosDirAsync command, each
     DynValue has to be between 0.001 and 1.0. A value of 1.0 means that the
     maximum value is used.
   ● arKinCtrl_gb[].CoordMode.KinCmdOption.ActivateKinPosPair
     is used to enable or disable
     arKinCtrl_gb[].CoordMode.KinCmdOption.stKineTargetPos and
     arKinCtrl_gb[].CoordMode.DynValues in order to control the target
     position using specific meanings.

       If CoordMode.KinCmdOption.ActivateKinPosPair is set to FALSE, the fol‐
       lowing applies:
       ● This mode supports Cartesian kinematics and up to 16 axes within a single
         kinematic group.
       ● The target position can be specified using
         arKinCtrl_gb[].CoordMode.Point[].
       ● arKinCtrl_gb[].CoordMode.KinCmdOption.stKineTargetPos and
         arKinCtrl_gb[].CoordMode.DynValues are disabled.
       ● The number of entries at the specified target position is automatically
         determined from the kinematics for all grouped axes.
       ● The meaning of the specified target position is based on the default values
         and cannot be selected.
       If CoordMode.KinCmdOption.ActivateKinPosPair is set to TRUE, the fol‐
       lowing applies:
       ● arKinCtrl_gb[].CoordMode.Point[] is disabled.
       ● Position values, their meanings, and the number of
         entries at the specified target position are entered via
         arKinCtrl_gb[].CoordMode.KinCmdOption.stKineTargetPos.
       ● If arKinCtrl_gb[].CoordMode.DynValues is enabled, each value of the
         dynamic limit values has to be between 0.001 and 1.0.

Operation mode "2D Circular moving in clockwise rotation"
  Enabling this operation mode causes a 2D circular movement to the target
  coordinates with clockwise rotation in the selected active plane.
  The arc of a 2D circle is performed in the active plane configured with the
  command option. An active plane is always selected (the XY-plane is the
  default). Either the radius or the center points of the circle should be speci‐
  fied as required circle parameters of the motion.
  The following command activates the operation mode:
       arKinCtrl_gb[].Admin._OpMode := ModeCoordPosCir2DCw;
       or
       arKinCtrl_gb[].Admin._OpModeBits. MODE_COORD_POS_CIR_CW :=TRUE;
       The following acknowledgement has to follow the operation mode command.
       It returns TRUE when the kinematics reached the target coordinates:
       arKinStatus_gb[].Admin.CmdDone
       The KinematicInterface uses the operation mode ModeCoordinated of the
       AxisInterface and the functions ML_KinEnable and ML_KinMoveCircleCw2D
       (CXA_Motion library) for switching.

Table 447: Attributes of the operation mode "2D circular moving in clockwise rotation"
Element             Name                                Type                    Standard       Cyclically

arKinStatus_gb[]    EndPoint                            ⮫ MB_KIN_END_POINT                     No

CircleData                          ⮫ MB_KIN_CIRCLE_PARAM                  No

CoordMode.DynValues.Velocity        LREAL                   1.0            No

CoordMode.DynValues.Acceleration    LREAL                   1.0            No

CoordMode.DynValues. Deceleration   LREAL                   1.0            No

CoordMode.DynValues.JerkAcc         LREAL                   0.0            No

CoordMode.DynValues.JerkDec         LREAL                   0.0            No

arKinStatus_gb[ ]   Admin._OpModeAckBits.               BOOL                                   Not appli‐
MODE_COORD_POS_CIR_CW                                                      cable

Element         Name                            Type                    Standard            Cyclically

Admin.CmdDone                   BOOL                                        Not appli‐

Data types

MB_KIN_END_POINT (STRUCT)
The MB_KIN_END_POINT structure contains the size and the raw data of the
target position.
Structural ele‐   Type                           Description

ment
Size              UINT                         Number of entries in "Data"
Data              ARRAY[0..24] OF ML_KinCmdPo‐ Target end position with
                  sePair                       meanings and attributes

ML_KinCmdPosePair (STRUCT)
Structural ele‐   Type                           Description
ment
Value             LREAL                          Value of the target end
                                                 position
Meaning           ML_Meaning                     Meaning of the value
                                                 (e.g. X, Y, Z, AX1, AX2, AX3,
                                                 AX4, AX5, AX6, AX7...)
Attributes        ML_MeaningAttribute            Additional attribute of the
                                                 meaning
                                                 (e.g. UNDEF, INCR_VALUE,
                                                 ABS_VALUE...)

MB_KIN_CIRCLE_PARAM (STRUCT)
The structure MB_KIN_CIRCLE_PARAM contains the size and the raw data of
the circle-related parameter.
Structural ele‐   Type                           Description
ment
Size              UINT                           Number of entries in "Data"
Data              ARRAY[0..7] OF ML_KinCmdCir‐   Commanded circle data
                  cleDataPair                    with circle meaning

ML_KinCmdCircleDataPair (STRUCT)
Structural ele‐   Type                           Description
ment
Value             LREAL                          Value of the target end
                                                 position
Meaning           ML_Meaning                     Meaning of the value
                                                 (e.g. X, Y, Z, AX1, AX2, AX3,
                                                 AX4, AX5, AX6, AX7...)
Attributes        ML_MeaningAttribute            Additional attribute of the
                                                 meaning
                                                 (e.g. UNDEF, INCR_VALUE,
                                                 ABS_VALUE...)

Operation mode "2D Circular moving in counterclockwise"
  Enabling this operation mode causes a 2D circular movement to the target
  coordinates with counterclockwise rotation in the selected active plane.
  The arc of a 2D circle is performed in the active plane configured with the
  command option. An active plane is always selected (the XY-plane is the
  default). Either the radius or the center points of the circle should be speci‐
  fied as required circle parameters of the motion.
  The following command activates the operation mode:
       arKinCtrl_gb[].Admin._OpMode := ModeCoordPosCir2DCcw;
       or
       arKinCtrl_gb[].Admin._OpModeBits.
       MODE_COORD_POS_CIR_CCW :=TRUE;
       The following acknowledgement has to follow the operation mode command.
       It returns TRUE when the kinematics reached the target coordinates:
       arKinStatus_gb[].Admin.CmdDone
       The KinematicInterface uses the operation mode ModeCoordinated of the
       AxisInterface and the functions ML_KinEnable and ML_KinMoveCircleCcw2D
       (CXA_Motion library) for switching.

Table 448: Attributes of the operation mode "2D circular moving in counterclockwise"
Element             Name                                Type                    Standard      Cyclically

arKinStatus_gb[]    EndPoint                            ⮫ MB_KIN_END_POINT                    No

CircleData                          ⮫ MB_KIN_CIRCLE_PARAM                 No

CoordMode.DynValues.Velocity        LREAL                   1.0           No

CoordMode.DynValues.Acceleration    LREAL                   1.0           No

CoordMode.DynValues. Deceleration   LREAL                   1.0           No

CoordMode.DynValues.JerkAcc         LREAL                   0.0           No

CoordMode.DynValues.JerkDec         LREAL                   0.0           No

arKinStatus_gb[ ]   Admin._OpModeAckBits.               BOOL                                  Not appli‐
MODE_COORD_POS_CIR_CW                                                     cable

Admin.CmdDone                       BOOL                                  Not appli‐

Operation mode “Standby"
  If the operation mode is changed from ModeCoordAb or ModeCoordAH to
  ModeCoordStandby , the KinematicInterface switches all assigned axes to AF
  and groups the axes to a kinematics.
  When enabling this operation mode in GroupMoving, all running commands
  are aborted and the kinematics is stopped with the target state Group‐
  Standby.
  The following command activates the operation mode:
       arKinCtrl_gb[].Admin._OpMode := ModeCoordStandby;
       or
       arKinCtrl_gb[].Admin._OpModeBits.MODE_COORD_STANDBY:= TRUE;
       The KinematicInterface uses the operation mode ModeCoordinated of the
       AxisInterface and the functions ML_KinEnable and ML_KinAbort (CXA_Motion
       library) for switching.

Table 449: Attributes of the operation mode “Standby”
Element            Name                         Type                    Default           Cycli‐
                                                                                          cally
                                                                                          scanned
arAxis‐            Admin._OpModeAck‐      BOOL                                            Omitted
Status_gb[ ]       Bits.MODE_COORD_STANDB
                   Y
                   Admin.CmdDone          BOOL                                            Omitted

Operation mode “Interrupt”

When enabling this operation mode in GroupMoving, all running commands
are interrupted and the kinematics is stopped. The kinematics remains in
the GroupMoving state until the interruption is removed with ModeCoordCon‐
tinue,
If the operation mode is changed from ModeCoordAb or ModeCoordAH to
ModeCoordInterrupt, the KinematicInterface switches all assigned axes to AF
and groups the axes to a kinematics.
The following command activates the operation mode:
arKinCtrl_gb[].Admin._OpMode := ModeCoordInterrupt;
or
arKinCtrl_gb[].Admin._OpModeBits.MODE_COORD_INTERRUPT:= TRUE;
The KinematicInterface uses the function ML_KinInterrupt (CXA_Motion
library) for switching.

Table 450: Attributes of the operation mode “Interrupt”
Element            Name                         Type                    Default           Cycli‐
                                                                                          cally
                                                                                          scanned
arAxis‐            Admin._OpModeAck‐            BOOL                                      Omitted
Status_gb[ ]       Bits.MODE_COORD_INTER‐
                   RUPT
                   Admin.CmdDone                BOOL                                      Omitted

Operation mode “Continue”
When activating this operation mode, an interruption is canceled with Mode‐
CoordInterrupt.
If ModeCoordContinue is selected, an error is issued if there was an interrup‐
tion before.
The following command activates the operation mode:
arKinCtrl_gb[].Admin._OpMode := ModeCoordContinue;
or
arKinCtrl_gb[].Admin._OpModeBits.MODE_COORD_CONTINUE:= TRUE;
The KinematicInterface uses the function ML_KinContinue (CXA_Motion
library) for switching.

Table 451: Attributes of the operation mode “Continue”
Element            Name                         Type                    Default           Cycli‐
                                                                                          cally
                                                                                          scanned
arAxis‐            Admin._OpModeAck‐            BOOL                                      Omitted
Status_gb[ ]       Bits.MODE_COORD_CON‐
                   TINUE

Element            Name                         Type                    Default          Cycli‐
                                                                    cally
                                                                    scanned
Admin.CmdDone                BOOL                                     Omitted

Operation mode "SlopeType"
Activating this operation mode switches the kinematics to the operating mode
SlopeType. This kinematic command option permanently allows a continuous
motion across several commands.
The following command activates the operation mode:
arKinCtrl_gb[].CoordMode.SlopeType           :=     MB_KIN_CONT_MOTION.
ST_CONTINUOUS_SLOPE
The following acknowledgement has to follow the operation mode command.
It returns the respective commanded operation mode:
arKinCtrl_gb[].CoordMode.SlopeType
The AxisInterface uses the functions ML_KinContMotionP (CXA_Motion
library) for switching.

Table 452: Attributes of the “SlopeType” mode
Element            Name                         Type                    StandardCycli‐
                                                                                cally
                                                                                scanned
arKinCtrl_gb[].    CoordMode.SlopeType          MB_KIN_CONT_MOTION ST_BLOCK_SLO Not
                                                                   PE           appli‐
                                                                                cable

"Half jump up" operation mode
When this operating mode is enabled and a positive value is set for
arKinCtrl_gb[].CoordMode.HalfJumpData.Height, it results in a half-
jump upward, allowing the kinematics to be moved from the last commanded
tool center point to a specified target position during a pick-&-place motion.
The following command activates the operation mode:
arKinCtrl_gb[].Admin._OpMode := ModeCoordPosHalfJumpUp
Optional activation via:
arKinCtrl_gb[].Admin._OpModeBits.          MODE_COORD_POS_HALF_JUMP_UP:
=TRUE
When "Half jump up" is enabled, the following steps are performed:
● Step 1: Move up or down, depending on the specified altitude parameter (a
   positive altitude value results in upward motion).
● Step 2: Motion along a polynomial path in the horizontal direction (based
   on the specified altitude parameter).
● Step 3: End the motion with a horizontal motion at the target position.
When      the     kinematics    have    reached   the  target     coordinates,
arKinStatus_gb[].Admin.CmdDone is set to TRUE.
The KinematicInterface uses the "ModeCoordinated" operating mode of the
AxisInterface, as well as the ML_KinEnable and ML_KinMoveHalfJump func‐
tions (CXA_Motion library), to switch modes.

Table 453: Attributes of the "Half jump up" operation mode
Element            Name                         Data type               Standard          Cycli‐
                                                                                          cally
                                                                                          scanned
arKinCtrl_gb[ ]    EndPoint                     ⮫ MB_KIN_END_POINT                        No
                   CoordMode.Dyn‐               LREAL                   1.0               No
                   Values.Velocity
                   CoordMode.Dyn‐           LREAL                       1.0               No
                   Values.Acceleration
                   CoordMode.DynValues.     LREAL                       1.0               No

Deceleration
CoordMode.DynValues.Jer‐ LREAL                       0.0               No
kAcc
CoordMode.Dyn‐           LREAL                       0.0               No
Values.JerkDec
CoordMode.HalfJump‐      REAL                        0.0               No
Data.Height
CoordMode.CoordSystem    MB_KIN_COORD_SYS                              No
arKin-             Admin._OpModeAck bits.   BOOL                                          Not
Status_gb[ ]       MODE_COORD_POS_HALF_J                                                  appli‐
UMP_UP                                                                 cable
Admin.CmdDone            BOOL                                          Not
                                                                       appli‐
                                                                       cable

"Half jump down" operation mode
  When this operating mode is enabled and a positive value is set for
  arKinCtrl_gb[].CoordMode.HalfJumpData.Height, it results in a half-
  jump upward, allowing the kinematics to be moved from the last commanded
  tool center point to a specified target position during a pick-&-place motion.
  The following command activates the operation mode:
  arKinCtrl_gb[].Admin._OpMode := ModeCoordPosHalfJumpDown
  Optional activation via:
  arKinCtrl_gb[].Admin._OpModeBits.
  MODE_COORD_POS_HALF_JUMP_DOWN: =TRUE
  When "Half jump down" is enabled, the following steps occur:
  ● Step 1: Move up or down, depending on the specified altitude parameter (a
     positive altitude value results in upward motion).
  ● Step 2: Motion along a polynomial path in the horizontal direction (based
     on the specified altitude parameter).
  ● Step 3: End the motion with a horizontal motion at the target position.
  When      the     kinematics    have    reached   the  target     coordinates,
  arKinStatus_gb[].Admin.CmdDone is set to TRUE.
  The KinematicInterface uses the "ModeCoordinated" operating mode of the
  AxisInterface, as well as the ML_KinEnable and ML_KinMoveHalfJump func‐
  tions (CXA_Motion library), to switch modes.

Table 454: Attributes of the "Half jump down" operation mode
Element            Name                         Data type               Standard          Cycli‐
                                                                                          cally
                                                                                          scanned
arKinCtrl_gb[ ]    EndPoint                     ⮫ MB_KIN_END_POINT                        No

Element            Name                        Data type               Standard        Cycli‐
                                                                    cally
                                                                    scanned
CoordMode.Dyn‐           LREAL                      1.0             No
Values.Velocity
CoordMode.Dyn‐           LREAL                      1.0             No
Values.Acceleration
CoordMode.DynValues.     LREAL                      1.0             No
Deceleration
CoordMode.DynValues.Jer‐ LREAL                      0.0             No
kAcc
CoordMode.Dyn‐           LREAL                      0.0             No
Values.JerkDec
CoordMode.HalfJump‐      REAL                       0.0             No
Data.Height
CoordMode.CoordSystem    MB_KIN_COORD_SYS                           No
arKin-             Admin._OpModeAck bits.   BOOL                                       Not
Status_gb[ ]       MODE_COORD_POS_HALF_J                                               appli‐
UMP_DOWN                                                            cable
Admin.CmdDone            BOOL                                       Not
                                                                    appli‐
                                                                    cable

Operation mode "AccelerationOverride"
  Activating this operation mode switches the kinematics to the operating mode
  AccelerationOverride. This command is used to specify the current value for
  the acceleration override of a motion object.
  The following command activates the operation mode:
  arKinCtrl_gb[].CoordMode.AccelerationOverride
  The following acknowledgement has to follow the operation mode command.
  It returns the respective commanded operation mode:
  arKinCtrl_gb[].CoordMode.AccelerationOverride
  The AxisInterface uses the functions ML_SetAccOverride and ML_GetAccO‐
  verride (CXA_Motion library) for switching.

Table 455: Attributes of the “AccelerationOverride” mode
Element            Name                        Type                    Standard        Cycli‐
                                                                                       cally
                                                                                       scanned
arKinCtrl_gb[].    CoordMode.AccelerationO‐    LREAL                   100             Not
                   verride                                                             appli‐
                                                                                       cable

Operation mode "ModeCoordStopping"
  Enabling this operation mode pauses the current motion of an axis group.
  During the delay, the PLCOpen status of the axis group is set to ABORTING
  until the velocity decreased to zero. The PLCOpen status then changes to
  STANDBY.
  The following command activates the operation mode:
  arKinCtrl_gb[].Admin._OpMode              :=         MB_KINEMATICS_MODE.
  ModeCoordStopping;
  or

      arKinCtrl_gb[].Admin._OpModeBits.MODE_COORD_STOPPING :=TRUE;
      This operation mode returns the acknowledgement of the operation mode or
      TRUE in the status structure of the kinematics:
      IF     arKinStatus_gb[].Admin._OpModeAck       =    MB_KINEMATICS_MODE.
      ModeCoordStopping THEN
        //user code
      END_IF
      //or
      arKinStatus_gb[].Admin._OpModeAckBits.MODE_COORD_STOPPING;
      This kinematic interface uses the ML_KinAbort function (in the CXA_Motion

      library) to implement the functionality.

Table 456: Attributes of the “ModeCoordStopping” mode
Element              Name                        Type                      Standard            Cyclically

arKinStatus_gb       Admin._OpModeAck            MB_KINEMATICS_MODE        ModeAB              Not appli‐

Admin.OpModeAck‐            BOOL                      FALSE               Not appli‐
Bits.MODE_COORD_STOPPING                                                  cable

Data.PLCOpenState.Standby   BOOL                      FALSE               Not appli‐

Operation mode “External function block”
If the operation mode is changed from ModeCoordAb or ModeCoordAH to
ModeCoordExternalFB, the KinematicInterface switches all assigned axes to
AF, groups the axes to a kinematics and waits for an external motion com‐
mand, e.g. from a technology function.
If the kinematics is already in an operation mode, a motion command is not
executed from the KinematicInterface when this operation mode is activated.
The following command activates the operation mode:
      arKinCtrl_gb[].Admin._OpMode := ModeCoordExternalFB;
      or
      arKinCtrl_gb[].Admin._OpModeBits.MODE_COORD_EXTERNAL_FB:= TRUE;
      The KinematicInterface uses the operation mode ModeCoordinated of the Axi‐
      sInterface and the function ML_KinEnable (CXA_Motion library) for switching.

Table 457: Attributes of the operation mode “External function block”
Element                Name                             Type                  Default          Cycli‐
arKin‐                 Admin._OpModeAck‐      BOOL                                             Omitted
Status_gb[ ]           Bits.MODE_COORD_EXTERN
                       AL_FB

Functions for multiple operation modes
Some functions are enabled in all positioning modes and described in this
section.

BeltSync
   This function enables synchronization with a conveyor belt until it is deac‐
   tivated. The kinematics are synchronized with the conveyor belt's position,
   which is defined by BeltValue.

The KinematicInterface uses the ML_KinBeltSyncP function (CXA_Motion
library) to switch modes.

Set the belt coordinate system (BeltCS)
A belt coordinate system that is independent of the kinematic system is cre‐
ated and defined in the ctrlX DataLayer, as shown in the following example:

Data Layer node: motion/cfg/coord-systems/belt-cs/sets

Set the camera coordinate system (CCS)
The camera coordinate system is created and defined in the ctrlX DataLayer,
as shown in the following example:

Data Layer node: motion/cfg/coord-systems/ccs/sets

Axis belt sync configuration
Create a belt axis independent of a kinematic system and define its proper‐
ties:

● Position in space (offset and rotation relative to the WCS).
● Specification of the transmission ratio, e.g., the distance the belt travels
  during one revolution of the axis.
Data Layer node: motion/axs/[name]/cfg/functions/belt-sync
● Is-belt-axis: Flag used to specify whether the axis is a belt axis.
● belt-coord-sys-name-default: Name of the conveyor belt's default
  coordinate system.
If the axis has been configured as a belt axis, the BeltValue is automatically
adjusted to reflect the state of the axis. The user can retrieve ActBeltValue,
IsBeltAxis, and BeltCoord via the axis user interface or the global variable

arAxisStatus_gb[].Data.BeltStatus from MotionInterfaceUser.

Configuring the kinematic belt synchronization
Configuring a single belt for "kinematic belt synchronization" in the ctrlX Data
Layer.

Data Layer node: motion/kin/Kinematics/cfg/functions/belt-sync/
belts

Belt synchronization and kinematic status
Table 458: Attributes of the "BeltSync" function
Element            Name                            Type                Standard        Cycli‐
                                                                                       cally
                                                                                       scanned
arKinCtrl_gb[ ]    CoordMode.KinCmdOp‐          LREAL                  0.0             No
                   tion.stBeltSync.BeltValue
                   CoordMode.KinCmdOp‐          STRING                                 No
                   tion.stBeltSync.BeltAxis‐
                   Name
                   CoordMode.KinCmdOp‐          BOOL                   FALSE           No
                   tion.ActivateBeltSync
arKin-             Data.BeltSyncState.BeltState STRING                                 Not
Status_gb[ ]                                                                           appli‐
                                                                                       cable
                   Data.BeltSyncState.InBelt‐      BOOL                FALSE           Not
                   Sync                                                                appli‐
                                                                                       cable

  Functional description:
  ● If the value of ActivateBeltSync is changed from FALSE to TRUE, the belt
    synchronization command is activated, and the status of BeltSync changes
    from DESYNCHRONIZED to another status.
  ● If ActivateBeltSync is set to TRUE and the input parameter BeltValue or
    BeltName is changed, the BeltSync function is triggered again.
  ● If ActivateBeltSync is changed from TRUE to FALSE, the command to
    belt synchronization is disabled and the BeltSync status changes to
    DESYNCHRONIZED.
  ● Before belt synchronization is activated, BeltValue and BeltAxisName
    have to be specified, and the position, velocity, and coordinate system of
    the kinematics has to be verified.

VelocityOverride
With the VelocityOverride input, the velocity of the running motion can be
reduced. Values between 0.0% (kinematics in standstill) and 100.0% (motion
executed with specified velocity) are permitted.
The KinematicInterface uses the function ML_SetOverride (CXA_Motion
library) for switching.
Table 459: Attributes of the function "VelocityOverride"
Element           Name                         Type                     Standard         Cycli‐
                                                                                         cally
                                                                                         scanned

arKinCtrl_gb[ ]   CoordMode.VelocityOverride LREAL                      100.0            Yes

PCS
The SetName and ActivatePCS inputs can be used to activate a product coor‐
dinate system (PCS) for all motion commands.
A rising edge on ActivatePCS activates the PCS offsets and orientations speci‐
fied as "Set" or "Group" in SetName.
The PCS is disabled again at a falling edge at ActivatePCS.
The KinematicInterface uses the function ML_KinPCSP (CXA_Motion library)
for switching.
Table 460: Attributes of the function "PCS"
Element           Name                         Type                     Standard         Cycli‐
                                                                                         cally
                                                                                         scanned
arKinCtrl_gb[ ]   CoordMode.KinCmdOp‐          STRING                   ''               No
                  tion.SetName
arKinCtrl_gb[ ]   CoordMode.KinCmdOp‐          BOOL                     FALSE            Yes
                  tion.ActivatePCS

PCSTool
The SetName and ActivatePCSTool inputs can be used to activate a product
coordinate system (PCS) relative to a tool for all motion commands.
A rising edge on ActivatePCSTool activates the PCS offsets and orientations
entered in SetName as "Set" or "Group."
The PCS is disabled again at a falling edge at ActivatePCSTool.
The KinematicInterface uses the function ML_KinPCSToolP (CXA_Motion
library) for switching.
Table 461: Attributes of the function "PCSTool"
Element           Name                         Type                     Standard         Cycli‐
                                                                                         cally
                                                                                         scanned
arKinCtrl_gb[ ]   CoordMode.KinCmdOp‐          STRING                   ''               No
                  tion.SetName
arKinCtrl_gb[ ]   CoordMode.KinCmdOp‐          BOOL                     FALSE            Yes
                  tion.ActivatePCSTool

Blending
The inputs BlendingStartD1, BlendingEndD2 and ActivateBlending can enable
a blending between two motion commands. A basic use case is the corner
rounding between two linear paths.
A rising edge at ActivateBlending enables the blending limits entered into
BlendingStartD1 and BlendingEndD2.

  Blending is disabled again at a falling edge at ActivateBlending.
  The KinematicInterface uses the function ML_KinBlendP (CXA_Motion library)
  for switching.
Table 462: Attributes of the function "Blending"
Element            Name                            Type                   Standard         Cycli‐
arKinCtrl_gb[ ]    CoordMode.BlendingStartD1 LREAL                        0.0              No
arKinCtrl_gb[ ]    CoordMode.BlendingEndD2 LREAL                          0.0              No
arKinCtrl_gb[ ]    CoordMode.ActivateBlending BOOL                        FALSE            Yes

ActivePlane
  The active plane consists of a main coordinate, a secondary coordinate and
  a right-angled coordinate. It defines a rectangular coordinate system in Carte‐
  sian space. The active plane can be switched between the XY-plane, the YZ-
  plane and the ZX-plane. If the ActivePlane function is disabled, the XY-plane is
  used by default.
  The KinematicInterface uses the ML_KinActivePlaneP (CXA_Motion library) for
  switching.
Table 463: Attributes of the "ActivePlane" function
Element            Name                            Type                   Standard         Cycli‐
arKinCtrl_gb[ ]    CoordMode. KinCmdOp‐            BOOL                   FALSE            Yes
                   tion.ActivePlane
arKinCtrl_gb[ ]    CoordMode. KinCmdOp‐            ML_ActivePlaneType     XY_PLANE         Yes
                   tion.Plane

ActivatePathSmooth
  "Active pathSmooth" ensures smooth motion of a kinematic system across
  multiple commands. The command internally toggles three subcommands
  (options) simultaneously. The three subroutines are "KinContour," the "Kin‐
  ContMotionP” command option, and the corner-rounding option (e.g., "KinPo‐
  lyTransP”, corresponding to the "RoundingType" parameter).
  The KinematicInterface uses the ML_KinPathSmooth function to switch
  modes (CXA_Motion library). Also refer to: ⮫ Motion App Documentation,
  "KinPathSmooth" function
Table 464: Attributes of the "ActivatePathSmooth" function
Element            Name                            Type                   Standard         Cycli‐
arKinCtrl_gb[ ]    CoordMode. KinCmdOp‐            BOOL                   FALSE            Yes
                   tion.ActivePathSmooth
arKinCtrl_gb[ ]    CoordMode. KinCmdOp‐            LREAL                  0.0              Yes
                   tion.stPathSmooth.Eps
arKinCtrl_gb[ ]    CoordMode. KinCm‐               UINT                   0                Yes
                   dOption.stPathSmooth.Pre‐
                   pareCmds
arKinCtrl_gb[ ]    CoordMode. KinCmdOp‐            ML_RoundingType        POLY_TRANS       Yes
                   tion.stPathSmooth.Round‐
                   ingType

### 19.4.4 KinematicInterface - Global variables

The library CXA_MotionInterfaceUser includes the Global Variable List
Global_Kinematics_Interface in the folder KinInterfaceUser/GlobalVariables.
This list includes the following structures/variables:
Table 465: VAR_GLOBAL Global_Kinematics_Interface
Name                             Data type                       Comment
arKinCtrl_gb[ ]                  ARRAY [] OF TE_KINE‐            Control structure of the Kinema‐
                                 MATICS_CONTROL_TYPE01           ticInterface
arKinStatus_gb[ ]                ARRAY [] OF TE_KINE‐            Status structure of the Kinemati‐
                                 MATICS_STATUS_TYPE01            cInterface

arKinIdx_gb                      ARRAY [] OF UINT                Continuous list of kinematics
uiNofKinematics_gb               UINT                            Number of active kinematics
VisuKinematicsNo                 INT                             Switching the KinematicIndex in
                                              the visualizations
bClearErrorKin_gb                BOOL                            Global “Clear errors”

### 19.4.5 KinematicInterface - Structures

Introduction and overview
The KinematicInterface provides a data interface for easy kinematic control.
For information on the data structures, refer to the ctrlX PLC Engineering
library manager in the CXA_MotionInterface library in the KinInterface/DUTs
folder or in the CXA_MotionInterfaceUser library in the KinInterfaceUser/DUTs
folder.
The programming template “MotionInterface" can either be extended by the
user or some extensions have already been integrated. To enable these exten‐
sions, define own structures in the user project that extend the library struc‐
tures.
The extended structures have the prefix “TE_”. If there is a struc‐
ture called TE_KINEMATICS_ADMIN_STATUS for example in the program‐
ming template “MotionInterface”, it is an extended structure of MB_KINE‐
MATICS_ADMIN_STATUS.
For information on the structure, refer to the ctrlX PLC Engineering library
manager with the name MB_KINEMATICS_ADMIN_STATUS in the library
CXA_MotionInterface and with the name TE_KINEMATICS_ADMIN_STATUS in
the library CXA_MotionInterfaceUser.

### 19.4.6 KinematicInterface - Example program

Introduction and overview
This chapter provides an overview on the KinematicInterface parts available as
open-source code.
The open-source program parts are provided with the following elements:
  ● The programming template “KinematicInterface and AxisInterface” is used
    as an example application for the KinematicInterface (also refer to
    ⮫ Chapter 19.2 MotionInterface - Initial configuration on page 445).
  ● The user can change the CXA_MotionInterfaceUser.library to adapt the Kin‐
    ematicInterface to the respective application (also refer to ⮫ KinematicIn‐
    terface - User extension).

Programming template "KinematicInterface and AxisInterface"
In the "DemoKinematicsCommands” program, the access to the KinematicIn‐
terface is shown.

The programming template “KinematicInterface and AxisInterface" covers the
following points of the KinematicInterface:
● AxisKinIfPlcProg:
  Calling the TE_AxisInterfaceMainProg() - Initialization and cyclic call of the
  AxisInterface.
  Calling the TE_KinInterfaceMainProg() - Initialization and cyclic call of the
  KinematicInterface.
● AxisKinIfMotionProg:
  The method TE_AxisInterfaceMainProg.mMotionTask() is called. In this
  cycle, the actual values are refreshed in arAxisStatus_gb[].Data. If the
  method is not called, the actual values are refreshed in the PlcProg cycle.
  The method TE_KinInterfaceMainProg.mMotionTask() is called. In this cycle,
  the actual values are refreshed in arKinStatus_gb[].Data. If the method is
  not called, the actual values are refreshed in the PlcProg cycle.
● GlobalAxisDefines:
  Only required if MOTIF_CONFIG.CONFIG_MODE_AXS is set to GLOB_VAR.
  The axes are defined as constants of the type MB_AXISIF_REF and trans‐
  ferred in a list to TE_AxisInterfaceMainProg(). This constants have to be
  adapted for the own project.
● GlobalKinematicsDefines:
  Only required if MOTIF_CONFIG.CONFIG_MODE_KIN is set to GLOB_VAR.
  The kinematics are defined as constants of the type MB_AXES‐
  GROUPIF_REF and transferred in a list to TE_KinInterfaceMainProg(). This
  constants have to be adapted for the own project.
● DemoAxisCommands:
  Example code to use the AxisInterface. This code has to be adapted for the
  own project.
● DemoBufferedAxisCommands:
  Example code with a sequence programming and the issuing of buffered
  axis commands. This code has to be adapted for the own project.
● DemoKinematicsCommands:
  Example code with a sequence programming and the issuing of kinematic
  commands. This code has to be adapted for the own project.
● OverViewAxes:
  Visualization to operate the AxisInterface during the commissioning phase.
  Click on the fields with "<<" to go down further into the screens.
● OverviewKinematics:
  Visualization to operate the KinematicInterface during the commissioning
  phase. Click on the fields with "<<" to go down further into the screens.
● Version_AxisKinInterface:
  Change history and disclaimer

CXA_MotionInterfaceUser.library:

Introduction and overview
This open library extends the function blocks and structures of the basic
library CXA_MotionInterface. Programs and visualizations are provided. The
global variables of the interfaces are instantiated. The user can adapt and
extend the interfaces with this library.
To make the adaptations, refer to ⮫ KinematicInterface - User extension.
This chapter describes the POUs of the KinematicInterface from the KinInter‐
faceUser/POUs folder.

TE_KinInterfaceMainProg
        Brief description
        The program TE_KinInterfaceMainProg covers the following:
      ● Initialization of the KinematicInterface:
         When reaching the "Running" mode, the KinematicInterface is initialized
         using the function block TE_KinematicsInitAllKinematics. If the initialization
         was completed successfully, the “InitDone” output is set. In case of errors,
         the “Error” output is set.
      ● Cyclic call of the KinematicInterface:
         After a successful initialization, the function block TE_KinematicsInitAllKi‐

         nematics is called cyclically.
      ● TE_KinInterfaceMainProg.mMotionTask() method:
         If the method is called from a faster MotionTask, the elements in
         arKinStatus_gb[].Data are updated in a faster cycle. The call of the function
         block TE_KinematicsInterface can be moved to the faster task using the
         control variable arKinCtrl_gb[].Admin.Config.MotionSync“.
         If the method is not called, all updates are made in the cycle of the PLC
         task.
Table 466: Interface variables of TE_KinInterfaceMainProg
I/O type       Name                  Data type           Comment
VAR_INPUT      ClearError            BOOL                Clearing the error is started at a positive
                                                         edge at ClearError
               KinCfgIdx             POINTER TO          Configuration list for the indices of the kin‐
                                     ARRAY []            ematics (only for the configuration mode
                                     OF MB_AXES‐         GLOB_VAR)
                                     GROUPIF_REF
VAR_OUTPUT InitDone                  BOOL                It is set if the program completed the initi‐
                                                         alization successfully
               Error                 BOOL                Indicates that an error occurred in the pro‐
                                                         gram
               ErrorID               ERROR_CODE          Short note on the error cause
               ErrorIdent            ERROR_STRUCT        Detailed error information

        Troubleshooting:
     The error codes of the internally used function block TE_KinematicsInitAllKine‐
     matics are transferred.
     The program can generate the following error codes:
Table 467: Error codes of the program TE_KinInterfaceMainProg
ErrorID            Additional1                      Additional2               Description
STATE_MACHINE_ERRO 16#0A0F0107                      16#0C2301D0               Errors during the pro‐
R                                                                             gram processing
                       The program TE_KinInterfaceMainProg is useful when integrating the Kinemati‐
                       cInterface into an existing program.
                       See also Example_KinIfApplicationPart in the folder KinInterfaceUser/_Exam‐
                       ples.

TE_KinematicsInitAllKinematics
        Brief description
        The function block TE_KinematicsInitAllKinematics initializes the KinematicIn‐
        terface structures.
        Use the parameter list MOTIF_CONFIG to control the initialization.

        There are the following options:
        ● AUTO = MOTIF_CONFIG.CONFIG_MODE:
          If the Data Layer node motion/kin/ is read out and the kinematics are
          positioned in the KinematicInterface structures in the sequence found.
        ● GLOB_VAR = MOTIF_CONFIG.CONFIG_MODE:
          The kinematics are positioned using the global array
          KINIF_CONFIG_INDEXES in the KinematicInterface structures.
        ● FILE = MOTIF_CONFIG.CONFIG_MODE:
          A list of kinematics and the respective kinematic index are defined in a
          JSON file.

Table 468: Interface variables of TE_KinematicsInitAllKinematics
I/O type           Name                  Data type            Comment
VAR_INPUT          Execute               BOOL                 A positive edge at “Execute” starts the initi‐
                                                              alization
                   KinCfgIdx             POINTER TO           Configuration list for the indices of the kin‐
                                         ARRAY []             ematics (only for the configuration mode
                                         OF MB_AXES‐          GLOB_VAR)
                                         GROUPIF_REF
VAR_OUTPUT Done                          BOOL                 Set when the function block has completed
                                                              the processing
                   Active                BOOL                 Set when the function block is active (not
                                                              in idle mode)
                   Error                 BOOL                 Indicates that an error occurred in the pro‐
                                                              gram
                   ErrorID               ERROR_CODE           Short note on the error cause
                   ErrorIdent            ERROR_STRUCT         Detailed error information

        Troubleshooting:
 The error codes of the internally used function block MB_KinematicsInit are
 transferred.
 The function block can generate the following error codes:
Table 469: Error codes of the TE_KinematicsInitAllKinematics function block
ErrorID                        Additional1              Additional2               Description
INPUT_RANGE_ERROR              16#0A0F0107              16#0C2301C0               Input KinIndex beyond
                                                                                  the valid range
                                                                                  [MB_KINIF_MIN_KIN_IN
                                                                                  DEX..MOTIF_CONFIG.M
                                                                                  AX_KIN_INDEX]
INPUT_RANGE_ERROR              16#0A0F0107              16#0C2301C1               Unknown configuration
                                                                                  mode
                                                                                  (MOTIF_CONFIG.CFG_
                                                                                  MODE_KIN)
INPUT_RANGE_ERROR              16#0A0F0107              16#0C2301C2               Pointer KinCfgIdx to the
                                                                                  global variable is 0
                                                                                  (MOTIF_CONFIG.CFG_
                                                                                  MODE_KIN =
                                                                                  GLOB_VAR)
INPUT_RANGE_ERROR              16#0A0F0107              16#0C2301C3               Kinematic index beyond
                                                                                  the valid range
                                                                                  (MOTIF_CONFIG.CFG_
                                                                                  MODE_KIN =
                                                                                  GLOB_VAR)

ErrorID                      Additional1          Additional2             Description
INPUT_RANGE_ERROR            16#0A0F0107          16#0C2301C4             Kinematic index double
                                                     (MOTIF_CONFIG.CFG_
                                                     MODE_KIN =
                                                     GLOB_VAR)
INPUT_RANGE_ERROR            16#0A0F0107          16#0C2301C5             Kinematic name double
                                                     (MOTIF_CONFIG.CFG_
                                                     MODE_KIN =
                                                     GLOB_VAR)
INPUT_RANGE_ERROR            16#0A0F0107          16#0C2301C6             Configuration file not
                                                     found

                                                     (MOTIF_CONFIG.CFG_
                                                     MODE_KIN = FILE)
INPUT_RANGE_ERROR            16#0A0F0107          16#0C2301C7             Configuration file incor‐
                                                     rect
                                                     (MOTIF_CONFIG.CFG_
                                                     MODE_KIN = FILE)
STATE_MACHINE_ERRO 16#0A0F0107                    16#0C2301C8             Errors while processing
R                                                                         the function block
The program TE_KinInterfaceMainProg already calls this function block TE_Kin‐
ematicsInitAllKinematics.

TE_KinematicsInterface
Brief description
The function block TE_KinematicsInterface extends the MB_KinInterfaceBase
and processes the structures of the KinematicInterface in cyclic mode.
To optimize the performance, the structures are connected to REFERENCE
TO as VAR_INPUT instead of as VAR_IN_OUT. Thus, the inputs only have to
be initialized once. The mInitExtension method is used. Thus, if the function
block is called cyclically, the structures do not have to be transferred.

Table 470: Interface variables of TE_KinematicsInterface
I/O type       Name                  Data type       Comment
VAR_INPUT      AdminCtrlExt          REFERENCE       Reference to the control structure “Admin”
control struc‐                       TO TE_KINE‐
ture                                 MATICS_ADMINIS‐
                                     TRATION
                CoordCtrlExt         REFERENCE       Reference to the control structure “Coordi‐
                                     TO TE_KIN‐      nated”
                                     EMATICS_COORDI‐
                                     NATED
                SetupMode            REFERENCE TO    Reference to the control structure “Setup‐
                                     TE_KINE‐        Mode”
                                     MATICS_SETUP_M
                                     ODE
VAR_INPUT       AdminStatusExt       REFERENCE TO    Reference to the status structure “Admin”
status struc‐                        TE_KINE‐
ture:                                MATICS_ADMIN_ST
                                     ATUS
                DataStatusExt        REFERENCE       Reference to the status structure “Data”
                                     TO TE_KINE‐
                                     MATICS_DATA

I/O type           Name                 Data type           Comment
DiagStatusExt        REFERENCE           Reference to the status structure “Diag”
                     TO TE_KIN‐
                     EMATICS_DIAG‐
                     NOSIS
SetupModeAck         REFERENCE TO        Reference to the status structure “Setup‐
                     TE_KINE‐            Mode”
                     MATICS_SETUP_M
                     ODE_STATUS

    Troubleshooting:
 The error codes of the internally used function blocks are transferred.
 The function block can generate the following error codes:
Table 471: Error codes of the TE_KinematicsInterface function block
ErrorID            Additional1                         Additional2              Description
STATE_MACHINE_ERRO 16#0A0F0107                         16#0C2301E0              Errors while processing
R                                                                               the function block
                       The program TE_KinInterfaceMainProg already calls this function block TE_Kin‐
                       ematicsInterface.

### 19.4.7 KinematicInterface - Visualizations

Introduction and overview
Visualization masks are included in the KinematicInterface upon delivery to
provide a simple template interface to set and control the kinematics.
The following visualizations are included in the programming template "Kine‐
maticInterface and AxisInterface" and in the CXA_MotionInterfaceUser.library:
Table 472: Example project visualizations
Visualization                      Description
OverviewKinematics (in the         Overall view on all defined kinematics, including simple diagnostics
template project)                  and status information
Kinematics_Overview                It indicates the current command and current values for coordinates
                                   and velocity, together with the navigation for the position and setup
                                   display for the current kinematics. Switching off axes is also pos‐
                                   sible
KinPosition_mode                   Monitoring the positioning mode
KinSetup_mode                      Monitoring the jog mode
                       The following global variables are used to control and access system informa‐
                       tion in the visualizations:
                       ● arKinCtrl_gb[ ]
                       ● arKinStatus_gb[ ]
                       ● VisuKinematicsNo

System overview - Visualization
   The OverviewKinematics visualization allows to quickly connect all kinematics
   configured in the project. Additional kinematics can be added for display in
   offline mode.
   This display provides an overall system status and allows to delete errors.
   Individual axis operating elements provide the kinematic name, diagnostics,
   the current position and velocity together with the operation mode status
   displays.

Adding a kinematics to the system overview
A kinematics is added to the system overview display like a new visualization:
Select the relevant element and specify the kinematic number.
The following steps describe the procedure briefly:
1.   Double-click on the visualization “OverviewAllKinematics” with ctrlX PLC
     Engineering in offline mode.
2.   In the "Visualization tools" window, select the button “Frame” and,
     under the last line in the kinematic table, generate an outline with the
     correct line height and width.
3.   Right-click on the "Frame" and enable the "Frame selection". Select the
     element OverviewOneKinematics from the selection window of the visu‐
     alization in the folder CXA_MotionInterfaceUser/KinInterfaceUser/Visuali‐
     zations/SystemOverview.
     🡆 An entirely new system overview “Kinematic line" is displayed.
4.   Click into the new visualization, enter the index of the defined kine‐
     matics into the "Properties" window as value for m_Input_KinIndex.
5.   The new KinematicInterface for the system overview can now be resized
     and positioned.
6.   Recompile the PLC project and go online.

Repeat the steps above for all kinematics added to the project.

Navigation system overview
To open an overview display of the individual kinematics, click on the button
with the two arrows "<<" located below the "Details" column in the kinematic
table. From the kinematic overview display, the user can navigate to the opera‐
tion mode display for the position and the setup.

### 19.4.8 KinematicInterface - User extension

Introduction and overview
The user can extend the structures arKinCtrl_gb[ ] and arKinStatus_gb[ ] to
adapt the KinematicInterface to special applications.

The structures arKinCtrl_gb[ ] and arKinStatus_gb[ ] of the user are defined
as basic types with the prefix “MB_” in the closed CXA_MotionInterface.com‐
piled-library and can thus not be accessed by the user.
To allow extensions, own structures are required that extend the “MB_” struc‐
tures. The extended structures have the prefix “TE_” and are located in the
open library CXA_MotionInterfaceUser.library.

Recommended procedure
To execute the user extensions, adjust the CXA_MotionInterfaceUser.library.
For understanding purposes, it is required and strongly recommended to
specify a new name for the modified library, e.g. CXA_MotionInterfaceMyCom‐
pany.library.
CXA_MotionInterfaceMyCompany.library is used as library name in the fol‐
lowing.
Operating sequence
1.   Select the CXA_MotionInterfaceUser.library in the library manager. Right-
     click on “Export library”. Specify a storage location and a new name, e.g.
     "CXA_MotionInterfaceMyCompany.library". Subsequent renaming is also
     possible.

2.   Use a second instance of the ctrlX PLC Engineering to open the
     CXA_MotionInterfaceMyCompany.library. In the project information,
     select the field “released”, modify further fields and delete the “Place‐
     holder” key in the properties.
3.   Remove the CXA_MotionInterfaceUser.library in the library manager of
     the user program (first instance of the ctrlX PLC Engineering) and inte‐
     grate the CXA_MotionInterfaceMyCompany.library instead.
4.   Make the respective changes in the library and execute the following
     command: “File 🠂 Save project and install in library repository”.
5.   Test the adaptations in the user program (first instance of PLC Engi‐
     neering). Debugging in the code from the library is also possible.

6.   Repeat the steps 4 and 5 until the function runs without errors.
When an update of the CXA_MotionInterfaceUser.library is available, changes
can be applied with “Project 🠂 Compare” in the CXA_MotionInterfaceMyCom‐
pany.library.
CXA_MotionInterfaceUser.library uses error codes from "CXA_TABLE". Refer
to the product documentation. If more error codes are required in the
user extensions, they can be defined freely, but have to be reported with
"USER1_TABLE..USER10_TABLE

ML_GetOverride
This section shows how the KinematicInterface is extended by adding the
ML_GetOverride functionality. The function ML_GetOverride allows to query
the current VelocityOverride of a kinematics. The command value is already in
the basic structure as arKinCtrl_gb[].CoordMode.VelocityOverride.

The following new inputs and outputs are defined:
● arKinCtrl_gb[ ].Admin.EnableReadVelocityOverride
● arKinStatus_gb[ ].Data.ActVelocityOverride
The following customized extensions are implemented into the programming
template “KinematicInterface".
● Jog functionality as SetupMode
It is assumed that the structure already prepared in the program template
“KinematicInterface” is used. The following describes the required changes in
the POUs specified there.

Notes on the implementation of user extensions
The user extensions are implemented using the object-oriented extensions
from ctrlX PLC Engineering.
Please note the following particularities:
● The TE_KinematicsInterface function block is derived from the basic func‐
  tion block MB_KinematicsInterfaceBase. Use the keyword SUPER to call the
  basic function block or its methods/actions of the basic function block. At
  various locations, the method mSetError of the function block MB_Kinema‐
  ticsInterfaceBase is called via SUPER^.mSetError(...); to enter errors into
  the diagnostic system
● Within the TE_KinematicsInterfaceBase function block, the data of
  arKinCtrl_gb can be accessed using the inputs AdminCtrlExt, CoordCtrlExt
  etc. or the arKinStatus_gb can be accessed via AdminStatusExt, DiagStatu‐
  sExt, etc.
  The inputs AdminCtrl (without Ext), etc. belong to the basic function block
  and are not to be used

● The inputs of the TE_KinematicsInterfaceBase function block are defined
  as REFERENCE TO. In the method mInitExtension, the references are initial‐
  ized once and do not have to be transferred again during the cyclic call of
  the function block
● To extend the basic structures TE_KINEMATICS_CONTROL_TYPE01 and
  TE_KINEMATICS_STATUS_TYPE01 with additional substructures, the fol‐
  lowing additional steps are required (see SetupMode and SetupModeAck
  as examples):
  – Enter new elements into TE_KINEMATICS_CONTROL_TYPE01 or TE_KINE‐
     MATICS_STATUS_TYPE01
  – Add the additional inputs as REFERENCE TO to the TE_KinematicsInter‐
     faceBase function block
  – Initialize in the method mInitExtension of the TE_KinematicsInterface‐
     Base function block

Extending the arKinCtrl_gb[ ] structure
To add the additional functionality of the arKinCtrl_gb[ ] structure, the user
has to create a new structure, derive the substructures from the existing struc‐
ture and then add the new elements. In the programming template "Kinemati‐
cInterface and AxisInterface", a structure TE_KINEMATICS_CONTROL_TYPE01
and the substructures TE_KINEMATICS_ADMINISTRATION, etc. are already pre‐
pared.

Proceed according to the following steps to extend the functionality of the
TE_KINEMATICS_ADMINISTRATION structure:
1.   Open the CXA_MotionInterfaceMyCompany.library with the ctrlX PLC
     Engineering
2.   Open the TE_KINEMATICS_ADMINISTRATION structure, folder KinInterfa‐
     ceUser/DUTs/Control.
3.   Declare the following variable
     ● EnableReadVelocityOverride: BOOL:=TRUE;

Extending the arKinStatus_gb[ ] structure
Extend the arKinStatus_gb[ ] structure as described in the steps in ⮫ Chapter
Extending the arKinCtrl_gb[ ] structure on page 552.
The following steps describe the procedure briefly:
1.   Open the TE_KINEMATICS_DATA structure, folder KinInterfaceUser/DUTs/
     Status.
2.   Declare the following variable
     ● ActVelocityOverride: LREAL;

Extending the function block
The last step in the user extension sequence is to extend the function block so
that the new elements can be used.
1.    Declare the following variable in the TE_KinematicsInterface function
      block:
     stML_GetOverrideData: ML_GetOverrideData;

2.      The function could be programmed as follows in the TE_KinematicsInter‐
        face function block:
     IF AdminCtrlExt.EnableReadVelocityOverride = TRUE THEN
     stML_GetOverrideData.In.ObjName :=
     AdminCtrlExt.Config.Group.KinName;
     ML_GetOverride(stML_GetOverrideData); // call motion
     function
     DataStatusExt.ActVelocityOverride :=
     stML_GetOverrideData.Out.Value;
     END_IF

3.   Compile the project again and check it for programming errors.
4.   Load the project to the control.
The new input and output elements are now part of the KinematicInter‐
face structure and can be viewed using the variables in the Global_Kine‐
matics_Interface.

### 19.4.9 How To - Typical user activities

Accessing kinematic data
The following data is available (name = corresponding kinematic name):
● arKinCtrl_gb[Name.GroupNo] => Control structure of the KinematicInter‐
  face
● arKinStatus_gb[Name.GroupNo] => Status structure of the KinematicInter‐
  face
● arKinStatus_gb[Name.GroupNo].Data => Actual values and status informa‐
  tion

Kinematic data can be accessed acyclically via the ctrlX Data Layer using the
function blocks DL_ReadNode and DL_WriteNode.

Adjusting the maximum number of kinematics
 The kinematic structures can be adjusted to the actual existing number of
 kinematics.
 The library CXA_MotionInterfaceUser allows adjustments using the library
 parameter MOTIF_CONFIG.
 The size of the structures can be selected with regard to the application using
 the constants MIN_KIN_INDEX and MAX_KIN_INDEX.

Adjusting the assignment KinematicName <>KinematicIndex
 The KinematicInterface uses a KinematicIndex for the addressing in the kine‐
 matic structures. The Motion firmware works with this kinematic name. There
 are different methods to assign KinematicName<>KinematicIndex.
 The library CXA_MotionInterfaceUser allows to select the method using the
 library parameter MOTIF_CONFIG.
 Assignment:         KinematicName         <>       KinematicIndex         in
 MOTIF_CONFIG.CFG_MODE_KIN
● AUTO: Reading out the Data Layer node motion/kin and assigning the Kine‐
  maticIndex in the found sequence
● GLOB_VAR: In the application, a list of MB_AXESGROUPIF_REF is defined
  and transferred to the program TE_KinInterfaceMainProg. Refer to GlobGlo‐
  balKinematicsDefines in the programming template "KinematicInterface and
  AxisInterface”.
● FILE: A list of kinematics and the respective KinematicIndex are defined in
  a JSON file.
  Exemplary JSON file section belonging to the kinematics:
  "kinematics": { "Kin1": 1, "Mover": 3 }
  The example file "AxesKinematicsDefines.json" is in the "Utilities" folder in
  the CXA_MotionInterfaceUser library.
  Note the following:
  – The section starts with the keyword “kinematics”
  – Use quotes for the kinematic name. Note the case sensitivity
  – The kinematic index follows the colon
  – Recommendation: To check the syntax, use a JSON Validator from the
     Internet

Adding a kinematics
A kinematics can be created in the user interface in the Motion section or
created from the PLC program for example.

Defined structural elements of the KinematicInterface have to be ini‐
tialized for an added kinematics if required. This results automati‐
cally when using the programming template "KinematicInterface and
AxisInterface” once the “Running” state has been reached. The
assignment KinematicName<>KinematicIndex has to be supplemented if
MOTIF_CONFIG.CFG_MODE_KIN = GLOB_VAR or FILE is configured.
Also refer to ⮫ Further information on page 554.

    Removing/renaming kinematics
An existing kinematics can be deleted or renamed in the user interface in the
“Motion” section or via different interfaces.

If a kinematics is renamed, modify the access via the control
and status structures “arKinCtrl_gb[ChangedKinematicName.GroupNo]" and
"arKinStatus_gb[ChangedKinematicName.GroupNo]" within the PLC program.
The assignment KinematicName<>KinematicIndex has to be modified if
MOTIF_CONFIG.CFG_MODE_KIN = GLOB_VAR or FILE is configured.
Also refer to ⮫ Further information on page 554.

    KinematicInterface - Extensions
The KinematicInterface allows almost any extension of the KinematicInterface
structures. Additional substructures can also be added and existing substruc‐
tures extended.

As an example, the following structural elements are programmed as user
extensions in the KinCtrl structure:
● SetupMode: Additional substructure in the KinCtrl structure
  – JogMode: Setting either incremental or continuous jogging
  – JogPlus[ ]: Jogging + can be selected for each coordinate
  – JogMinus[ ]: Jogging - can be selected for each coordinate
  – Increment: Step width for incremental jogging
  – DirectionVector[ ]: Direction of motion when jogging on the path
  – JogVectorPlus: Jogging +, for the complete kinematics
  – JogVectorMinus: Jogging -, for the complete kinematics
  – DynValues: Jog (deceleration) acceleration and jerk.

No structural elements are exemplarily programmed as user extensions in the
KinStatus structure: However, this is possible.

The code for these extensions is in the actions of the TE_KinematicsInterface()
function block in the KinInterfaceUser/POUS folder. The related structures
are in the KinInterfaceUser/DUTs/Control and KinInterfaceUser/DUTs/Status
folders.
Own extensions can be added (refer to ⮫ KinematicInterface - User extension).

## 19.5 IMC Interface

### 19.5.1 Introduction and overview

The IMC Interface (Interface-Motion-Control) includes control signals for the
rexroth-motion app in the control structure and status bits and diagnostic
information are provided in the status structure of the rexroth-motion app.

Functions of the IMC Interface
● Mode selection: Either "Configuration" or “Running”. The Motion state and
  the AxisProfile state are switched.
● Executes the "Clear Error" command. The function corresponds to the
  button "Clear Error of control" (e.g. “Automation” site in the web inter‐
  face).
● Executes RetriggerOpMode to allow users to re-execute the selected oper‐
  ating mode.
● If the mode is switched via an external instance (e.g. web interface), the
  IMC Interface sets the output PassiveMode and the selected mode is not
  actuated.
  Use RetriggerOpMode or switch back into the selected mode to exit the
  PassiveMode again.
● The state of the components Motion = MotionModeAck and AxisProfile =
  AxisProfileModeAck is shown separately.
  For a ctrlX CORE Virtual, AxisProfileModeAck is always on the value
  IMC_MODE_UNDEFINED.
  The output _OpModeAck shows MotionModeAck and AxisProfileModeAck
  together. In case of a mismatch, the lower state is shown. This ensures that
  all components are ready for _OpModeAck = RUN.
The following figure shows the user interface with the data structures of the
IMC Interface:

For more information on the data structures, refer to the ctrlX PLC Engi‐
neering library manager in the CXA_MotionInterface library in the ImcInter‐
face/DUTs folder.

To use the IMC Interface, call the program MB_ImcInterface cyclically, e.g.
in the PlcTask. When using the AxisInterface or the KinematicInterface, the
program call is already integrated.
The ctrlX PLC Engineering library manager in the CXA_MotionInterface library,
the ImcInterface/_Examples folder contains an application example for the
IMC interface.
This example shows how ImcStatus and ImcCtrl are used when creating axes.
