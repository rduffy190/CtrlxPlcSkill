# ctrlX Motion App — index

Generated from `R911430551_01_EN_Motion App Version 4_ApplicationManual.pdf` by `scripts/pdf_to_libref.py`. Search this index (or grep the files) for a name, then read just that section.

## 4.1 General information  →  `04-01_General_information.md` (55 KB, p. 14–40)

Real axes, Virtual axes, Disabling axes (maximal project), Motion global state machine, Axis objects, Encoder axis objects, Kinematic objects, Motion System Configuration, Saving Motion data, Motion kernel state via Data Layer, Units, Scalings, Motion-synchronous commanding

## 4.2 Licenses  →  `04-02_Licenses.md` (3 KB, p. 40–41)

_(single section)_

## 4.3 System performance  →  `04-03_System_performance.md` (2 KB, p. 41–42)

_(single section)_

## 5.1 Overview  →  `05-01_Overview.md` (2 KB, p. 42–45)

_(single section)_

## 5.2 Position control  →  `05-02_Position_control.md` (1 KB, p. 45–45)

_Not documented in this book: open the FB's Documentation tab in the ctrlX PLC Engineering Library Manager._

## 5.3 Velocity control  →  `05-03_Velocity_control.md` (3 KB, p. 45–49)

_(single section)_

## 5.4 Torque/force control  →  `05-04_Torque_force_control.md` (3 KB, p. 49–53)

_(single section)_

## 5.5 Multiple braking dynamics and diagnostic number  →  `05-05_Multiple_braking_dynamics_and_diagnostic_number.md` (1 KB, p. 53–53)

_Not documented in this book: open the FB's Documentation tab in the ctrlX PLC Engineering Library Manager._

## 5.6 Homing status  →  `05-06_Homing_status.md` (1 KB, p. 53–54)

_Not documented in this book: open the FB's Documentation tab in the ctrlX PLC Engineering Library Manager._

## 5.7 Gantry axes  →  `05-07_Gantry_axes.md` (1 KB, p. 54–55)

_Not documented in this book: open the FB's Documentation tab in the ctrlX PLC Engineering Library Manager._

## 5.8 Using an encoder axis with ctrlX I/O position data  →  `05-08_Using_an_encoder_axis_with_ctrlX_I_O_position_data.md` (2 KB, p. 55–56)

_Not documented in this book: open the FB's Documentation tab in the ctrlX PLC Engineering Library Manager._

## 5.9 Touch probe  →  `05-09_Touch_probe.md` (4 KB, p. 56–61)

_(single section)_

## 5.10 Special features of the CoE profile  →  `05-10_Special_features_of_the_CoE_profile.md` (6 KB, p. 61–68)

_(single section)_

## 5.11 Overview of drive parameters  →  `05-11_Overview_of_drive_parameters.md` (4 KB, p. 68–71)

_(single section)_

## 6.1 General functions  →  `06-01_General_functions.md` (23 KB, p. 71–84)

Extrapolation of actual values, Extrapolation for operating mode switching in motion, Measuring probe, Restrictions, Synchronizing a Motion object with an external instance, Synchronizing an external instance with a Motion object and waiting for acknowledgment

## 6.2 Axis functions  →  `06-02_Axis_functions.md` (188 KB, p. 84–176)

Synchronized execution of Motion commands, Calculation pipeline, Calculation steps, Change parameters in real time, Handling Modulo axes, Synchronized command function, Dynamic synchronization, Dynamic synchronization limits, Error reaction, Cam tables for Flexprofiles and CamIn, Basic structure of the “Flexprofile" synchronous operating modes, Configuring the profile, Time master, Standard motion laws, Extended motion laws, Flexstep, Motion law boundary conditions, Selecting the coordinate system, Switching and synchronizing, Processing type, Characteristics of the event control, Mapping of events, States, Storage in the file system, ctrlX Cam Designer, Validation, Commanding, CamIn - Cam with scaling factor, Torque/force control, ctrlX DRIVE Parameter, Motion parameters, Error classification and reaction principles, Delay time of the drive in case of emergency stop, Dynamic break parameter settings, Axis profile setting, Empiric parameter values, CXA_GantryAlignment, Axis status information, Measuring the maximum axis dynamics, Command value decoupling, Supporting devices in "Open Loop" mode with ctrlX, Axis decoupling from the axis profile, Axis checksum

## 6.3 Kinematic functions  →  `06-03_Kinematic_functions.md` (255 KB, p. 176–317)

Relevant parameters, Orientation & rotation, Substitute function for kinematic axes, Substitute function axis transformations of a kinematic system, SLERP, Differentiating between axes, kinematics and axis transformations, Functional principle of an axis transformation, Variant, Robot structure, Robot parameters, Robot structure, Robot dimensions, Axis coupling, Singularities of a 6-axis robot with a spherical hand, Solution selection, Robot structure, Robot parameters, Solution selection, Singularities of a 3-axis twisting crane robot, Robot structure, Variant, Robot parameters, Singularities of a SCARA robot, Solution selection, Robot structure, Robot parameters, Axis coupling, Singularities of a 4-axis SCARA robot with a crank, Solution selection, Robot structure, Robot parameters, Forward transformation, Inverse position kinematics, Singularities at the lower edge of the working area, Singularities at the upper edge of the working area, Robot structure, Robot parameters, Forward transformation, Inverse position kinematics, Singularities of a 3-axis delta robot with linear axes, Robot structure, Robot parameters, Forward transformation, Inverse position kinematics, Singularities at the lower edge of the working area, Singularities at the upper edge of the working area, Structure, Parameterization, Solution selection, Restrictions on the workspace, Singularities, Structure, Parameterization, Solution selection, Restrictions on the workspace, Singularities, Structure, Parameterization, Solution selection, Singularities, Structure, Parameterization, Solution selection, Restrictions on the working area, Singularities, Structure, Variant, Parameterization, Solution selection, Structure, Variant, Parameterization, Singularities, Solution selection, Structure, Variant, Parameterization, Structure, Variant, Parameterization, Motion commands, Moving on a straight line - MoveLinear, Points management, General information, Lengths and levels on the belt, State machine, Typical workflows and use cases, Belt synchronization for MoveJump and MoveHalfJump, Configuring the coordinate systems, Axis configuration, Kinematic configuration, Prerequisites, Configuration rule, On-site monitoring, Belt jitter and belt jumps, Value range of belt value, Status display, Example, Restrictions, Belt-synchronous with blending, Frequently Asked Questions (FAQ), Working areas and safe zones, Reduced motion velocity depending on the safe axis states, Switching on the path

## 6.4 Troubleshooting  →  `06-04_Troubleshooting.md` (18 KB, p. 317–325)

Basic principles of error reaction, Error reaction in a distributed system, Error types and associated error reactions, Axis/kinematic error in detail, Error causes, Forwarding errors, Interaction with other components, Configurable error reaction of specific functions, After the error reaction, Drive does not follow the command values of the control, Extended diagnostic options

## 7.1 General information  →  `07-01_General_information.md` (16 KB, p. 325–332)

_(single section)_

## 7.2 Axis commands  →  `07-02_Axis_commands.md` (474 KB, p. 332–519)

AxsPower - Axis power, AxsReset - AxsReset - Resetting the axis, AxsAbort - Canceling the axis command, AxsStop - Stop axis command, AxsEmergencyStop - Axis Emergency Stop, AxsInterrupt - Interrupting the axis command, AxsContinue - Continuing the axis command, AxsVelocity - Axis velocity, AxsTorque - Torque axis, AxsPosAbs, AxsPosAbsEx - Absolute positioning of the axis, AxsPosRel - Relative positioning of the axis, AxsPosAdd - Additive positioning of the axis, AxsJogIncr - Incremental axis jogging, AxsJogCont - Continuous axis jogging, Interface, AxsSetIpoPosFromActPos - Setting the interpolator position to the actual axis value, AxsGetSyncMotionState - Synchronization state, AxsGearInPos - Synchronizing to position, AxsGearInPosEx - Synchronizing to position, AxsGearInPos2 - Synchronizing to position, AxsGearInPos2Ex - Synchronizing to position, AxsGearInVel - Synchronizing to velocity, AxsCamIn, AxsCamInEx - Controlling a cam with a scaling factor, AxsCamIn2, AxsCamInEx2 - Commanding a cam with a scaling factor, AxsGetCamInState - Reading the points table status, AxsGetCamInActivePointTable - Points table, AxsFlexprofile, AxsFlexprofile2, AxsFlexprofileEx, AxsFlexprofileEx2 - Commanding an electronic cam (FlexProfile), AxsSetFlexProfileConfiguration, AxsFlexProfileValidate - Configuring and validating the electronic cam (FlexProfile), AxsSetAbsPos - Set axis to absolute position, AxsProbe - Axis probe, GetAxisProbeValues - Read axis probe, AxsProbeAbort - Axis probe, abort measurement, AxsProbeEx - Axis extended probe, AxsProbeAbortEx - Abort axis extended probe measurement, AxsHoming - Homing command, AxsFixedStop - Traveling the axis to a fixed stop, AxsResetFixedStop - Reset the axis to fixed stop, AxsAddToGantry - Adding the axis to the gantry, AxsRemoveFromGantry - Removing the axis from the gantry, Interface, AxsAddToKin - Adding the axis to the kinematics, AxsRemoveFromKin - Removing the axis from the kinematics, AxsSetDriveFollowsMonitoring - Turning "Drive follows command values" monitoring on or off

PLC: `ML_AxsAbort`, `ML_AxsAddToGantry`, `ML_AxsAddToKin`, `ML_AxsCamIn`, `ML_AxsCamIn2`, `ML_AxsCamInActivePointTable`, `ML_AxsCamInEx`, `ML_AxsCamInEx2`, `ML_AxsContinue`, `ML_AxsCtrlBasedGantryHoming`, `ML_AxsCyclicSetPoint`, `ML_AxsEmergencyStop`, `ML_AxsFixedStop`, `ML_AxsFlexprofile`, `ML_AxsFlexprofileEx`, `ML_AxsFlexprofileEx2`, `ML_AxsGearInPos`, `ML_AxsGearInPos2`, `ML_AxsGearInPosEx`, `ML_AxsGearInPosEx2`, `ML_AxsGetCamInState`, `ML_AxsGetSyncMotionState`, `ML_AxsHoming`, `ML_AxsInterrupt`, `ML_AxsJogCont`, `ML_AxsJogIncr`, `ML_AxsPosAbs`, `ML_AxsPosAbsEx`, `ML_AxsPosAdd`, `ML_AxsPosRel`, `ML_AxsPower`, `ML_AxsProbe`, `ML_AxsProbeAbort`, `ML_AxsProbeAbortEx`, `ML_AxsProbeEx`, `ML_AxsRemoveFromGantry`, `ML_AxsRemoveFromKin`, `ML_AxsReset`, `ML_AxsResetFixedStop`, `ML_AxsSetAbsPos`, `ML_AxsSetDriveFollowsMonitoring`, `ML_AxsSetFlexProfileConfiguration`, `ML_AxsSetIpoPosFromActPos`, `ML_AxsStop`, `ML_AxsTorque`, `ML_AxsVelocity`, `ML_GetAxisProbeValues`, `ML_SetCyclicSetPoint`

## 7.3 Kinematics commands  →  `07-03_Kinematics_commands.md` (220 KB, p. 519–603)

KinEnable - Enabling kinematics, KinDisable - Disabling kinematics, KinMoveLinAbs - Absolute traversing of kinematics, KinMoveLinRel - Relative traversing of kinematics, KinMoveDirectAbs - Direct absolute traversing of kinematics, KinMoveDirectRel - Direct relative traversing of kinematics, KinMoveDirectAsyncAbs - Direct asynchronous absolute traversing of kinematics, KinMoveDirectAsyncRel - Direct asynchronous relative traversing of kinematics, KinMoveJump - Jump motion to the target point, KinMoveHalfJump - Half-jump motion to the target point, KinCyclicSetPointPCS - Cyclic command value input, KinJogCont - Continuous kinematic jogging, KinJogIncr - Incremental kinematic jogging, KinInterrupt, KinInterrupt2 - Interrupting the kinematic command, KinContinue - Continuing the kinematic command, KinAbort, KinAbort2 - Canceling the kinematic command, KinReset - Resetting the kinematics, KinContour - Specifying the contour area, KinPathSmooth - Smooth path rounding and continuous velocity across multiple commands

PLC: `ML_KinAbort`, `ML_KinAbort2`, `ML_KinContinue`, `ML_KinContour`, `ML_KinCyclicSetPointPCS`, `ML_KinDisable`, `ML_KinEnable`, `ML_KinInterrupt`, `ML_KinInterrupt2`, `ML_KinJogCont`, `ML_KinJogIncr`, `ML_KinMoveDirectAbs`, `ML_KinMoveDirectAsyncAbs`, `ML_KinMoveDirectAsyncRel`, `ML_KinMoveDirectRel`, `ML_KinMoveHalfJump`, `ML_KinMoveJump`, `ML_KinMoveLinAbs`, `ML_KinMoveLinRel`, `ML_KinPathSmooth`, `ML_KinReset`, `ML_KinReset_GroupAxisErrorState`, `ML_KinReset_PlcOpenGroupStates`

## 7.4 Kinematic commands with extended programming options  →  `07-04_Kinematic_commands_with_extended_programming_options.md` (100 KB, p. 603–640)

KinMoveLinEx - Moving on a straight line in space, KinMoveDirectEx - Point-to-point motion at axis level, KinMoveDirectAsyncExx - Asynchronous point-to-point motion, KinMove2DCircle - Movement on a plane-related circular/helical path, KinMove3DCircle - Moving on a circular path in space, KinMoveToPointLin - Moving the kinematics linearly to a saved point, KinMoveToPointDirect - Moving the kinematics directly to a saved point

PLC: `ML_KinMoveCircle3D`, `ML_KinMoveCircleCcw2D`, `ML_KinMoveCircleCw2D`, `ML_KinMoveDirectAsyncEx`, `ML_KinMoveDirectEx`, `ML_KinMoveLinEx`, `ML_KinMoveToPointDirect`, `ML_KinMoveToPointLin`

## 7.5 Command options  →  `07-05_Command_options.md` (134 KB, p. 640–694)

KinBlend, KinBlendP - Blending/permanent kinematic option, KinMCSP - Command options for kinematics machine coordinate system, KinPCSP, KinPCSToolP - Command option for kinematic product coordinate system, KinToolLengthsP - Non-static tool offset, KinAxsDynLimP - Decreasing dynamic limits of the kinematic axis using a command, KinContMotionP - Continuous motion across several commands, KinPolyTransP - Command options for kinematics - Path rounding with polynomial, KinSafeAreaP - Working areas/safe zones, KinSafeAreaInExecutionP - Working areas/safe zones, KinFeedGroupP - Specifying the feed group, KinActivePlaneP - Selecting the active plane, KinSwitchOnPath, KinSwitchOnPathP, KinSwitchOnPathEx, KinSwitchOnPathExP - Switching on the path, KinBeltSyncP - Belt-synchronous

PLC: `ML_AxsGetBeltValueRT`, `ML_KinActivePlaneP`, `ML_KinAxsDynLimP`, `ML_KinBeltSyncP`, `ML_KinBlend`, `ML_KinBlendP`, `ML_KinContMotionP`, `ML_KinFeedGroupP`, `ML_KinMCSP`, `ML_KinPCSP`, `ML_KinPCSToolP`, `ML_KinPolyTransP`, `ML_KinSafeAreaInExecutionP`, `ML_KinSafeAreaP`, `ML_KinSwitchOnPath`, `ML_KinSwitchOnPathEx`, `ML_KinSwitchOnPathExP`, `ML_KinSwitchOnPathP`, `ML_KinToolLengthsP`

## 7.6 Synchronization commands  →  `07-06_Synchronization_commands.md` (83 KB, p. 694–735)

JoinCmd - Synchronized start of Motion objects, SetSignalCmd - Synchronization by sending signals, SetSignalCmdOpt, ResetSignalCmd - Resetting signals, WaitForSignalCmd - Wait for signal, WaitForSignalResetCmd - Waiting for a signal to be reset, SetSignal - Setting a signal at system level, ResetSignal - Resetting a signal at system level, GetSignal - Retrieving a signal value at system level, KinSetLocalSignal, KinSetLocalSignalCmdOpt, KinResetLocalSignal, KinWaitForLocalSignal, KinWaitForLocalSignalReset, SetKinLocalSignal, ResetKinLocalSignal, GetKinLocalSignal - Synchronization by sending local kinematic signals

PLC: `ML_GetKinLocalSignal`, `ML_GetSignal`, `ML_JoinCmd`, `ML_KinResetLocalSignal`, `ML_KinSetLocalSignal`, `ML_KinSetLocalSignalCmdOpt`, `ML_KinWaitForLocalSignal`, `ML_KinWaitForLocalSignalReset`, `ML_ResetKinLocalSignal`, `ML_ResetSignal`, `ML_ResetSignalCmd`, `ML_SetErrorLevel`, `ML_SetKinLocalSignal`, `ML_SetSignal`, `ML_SetSignalCmd`, `ML_SetSignalCmdOpt`, `ML_WaitForSignalCmd`, `ML_WaitForSignalResetCmd`

## 7.7 General commands  →  `07-07_General_commands.md` (93 KB, p. 735–772)

SetErrorLevel - Setting the error state, GetOverride - Reading out the override, SetOverride - Override, ForceOverride100 - Overriding the override, SetAccOverride, GetAccOverride - Acceleration override, ForceAccOverride100 - Overriding acceleration override, WaitPrepare - Stopping the preparation, WaitExec - Wait command, Definition of terminology, Risk of a head-to-head collision, Risk of a head-to-tail collision, Axis at standstill or when moving away from another axis, C-interface, Data Layer interface, KinSafeAreaInExecutionCheckEnabled - Enabling the working area monitoring, KinSafeAreaInExecutionAddCheckSize - Online modification of the working area size

PLC: `ML_AxsGetIpoAddData`, `ML_CollisionAvoidance`, `ML_ForceAccOverride100`, `ML_ForceOverride100`, `ML_GetAccOverride`, `ML_GetCollisionGuardState`, `ML_GetOverride`, `ML_KinSafeAreaInExecutionAddCheckSize`, `ML_KinSafeAreaInExecutionCheckEnabled`, `ML_SetAccOverride`, `ML_SetOverride`, `ML_WaitExec`, `ML_WaitPrepare`

## 7.8 Additional information  →  `07-08_Additional_information.md` (56 KB, p. 772–794)

AxsGetIpoAddData - Additional axis data, KinGetIpoAddData - Additional kinematic data, KinCoordTransform - Converting the coordinate system, AxsGetExtrapolatedActValues - Extrapolated axis values, AxsSetExtrapolateExternalDynamic - Source for dynamic extrapolation data, AxsGetBrakingDistance, AxsGetBrakingDistanceEx - Determining the current braking distance, GetCmdState - Command states, AxsSetRTStateEnabled - Enabling cyclic axis data

PLC: `ML_AxsGetBrakingDistance`, `ML_AxsGetBrakingDistanceEx`, `ML_AxsSetExtrapolateExternalDynamic`, `ML_AxsSetRTStateEnabled`, `ML_GetCmdState`, `ML_KinCoordTransform`, `ML_KinGetIpoAddData`
