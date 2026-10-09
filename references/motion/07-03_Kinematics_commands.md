# 7.3 Kinematics commands

### 7.3.1 Overview

Processing kinematic commands
Kinematic commands are typically processed as buffered. This means that
the commands are written to a command buffer after commanding. They are
prepared by a lower-priority task and finally they are executed in the order of
commanding. Furthermore, certain motion commands can also be commanded
as unbuffered. The command becomes active almost immediately and the
command buffer is discarded. For more details about buffered and unbuffered
kinematic commands, see ⮫ Chapter 7.1 General information on page 325.
There are exceptions for particular commands which can be processed
directly (additional commands) or as unbuffered. This includes, for example:
●   Override
●   KinInterrupt
●   KinContinue
●   KinAbort
●   KinReset

Motion commands
A motion command issued for a kinematics causes the Tool Center Point
(TCP) to move in the space.
The TCP refers to the top of the kinematics. The user sets the new TCP target
position. The type of motion command determines the path used to reach the
new TCP position.

The new target position can be set in any coordinate system.
The coordinate system has no impact on the path used to reach the point.
If the target position is commanded during a path motion in the axis coordi‐
nate system ACS, the target pose is calculated internally from the axis values
in the product coordinate system PCS and the path is then interpolated in the
PCS. The axis positions reached at the end of the motion can deviate from
the commanded axis values in the case of an active axis transformation with
ambiguities, as the transformation branch is not changed within a motion.
Refer to ⮫ Chapter 7.1 General information on page 325
The TCP position can be determined using the function ML_KinGetIpoValues
or under the ctrlX Data Layer under motion/kin/<kin-name>state/values/ipo.

A motion command consists of the following:
● Endpoint: Point on the motion path
● Maximum values: Maximum values for the velocity profile, such as max‐
   imum velocity and maximum acceleration
● Motion type: The type of path on which the endpoint is to be reached
In case of kinematic commands, the limit values of the participating axes
are taken into consideration apart from the programmed path dynamic limit
values.

Overview of kinematic commands
The following kinematic commands are implemented. Further kinematic com‐
mands with more complex operations can be found at ⮫ Chapter 7.4.1 Over‐
view on page 603.
● ⮫ Chapter 7.3.2 KinEnable - Enabling kinematics on page 521
● ⮫ Chapter 7.3.3 KinDisable - Disabling kinematics on page 523
● ⮫ Chapter 7.3.4 KinMoveLinAbs - Absolute traversing of kinematics
  on page 524
● ⮫ Chapter 7.3.5 KinMoveLinRel - Relative traversing of kinematics
  on page 528
● ⮫ Chapter 7.3.6 KinMoveDirectAbs - Direct absolute traversing of kine‐
  matics on page 532
● ⮫ Chapter 7.3.7 KinMoveDirectRel - Direct relative traversing of kinematics
  on page 535
● ⮫ Chapter 7.3.8 KinMoveDirectAsyncAbs - Direct asynchronous absolute tra‐
  versing of kinematics on page 538
● ⮫ Chapter 7.3.9 KinMoveDirectAsyncRel - Direct asynchronous relative tra‐
  versing of kinematics on page 543
● ⮫ Chapter 7.3.10 KinMoveJump - Jump motion to the target point
  on page 549
● ⮫ Chapter 7.3.11 KinMoveHalfJump - Half-jump motion to the target point
  on page 556
● ⮫ Chapter 7.3.12 KinCyclicSetPointPCS - Cyclic command value input
  on page 563
● ⮫ Chapter 7.3.13 KinJogCont - Continuous kinematic jogging on page 569
● ⮫ Chapter 7.3.14 KinJogIncr - Incremental kinematic jogging on page 573
● ⮫ Chapter 7.3.15 KinInterrupt, KinInterrupt2 - Interrupting the kinematic
  command on page 577
● ⮫ Chapter 7.3.16 KinContinue - Continuing the kinematic command
  on page 583
● ⮫ Chapter 7.3.17 KinAbort, KinAbort2 - Canceling the kinematic command
  on page 585

● ⮫ Chapter 7.3.18 KinReset - Resetting the kinematics on page 590
● ⮫ Chapter 7.3.19 KinContour - Specifying the contour area on page 594

### 7.3.2 KinEnable - Enabling kinematics

Basics
This command enables the kinematics. Thus, this command directly influences
the state machine of the kinematics. The state of the kinematics is set to
STANDBY after the command. After the kinematics has been enabled, it is
ready to move.
All kinematic axes have to be in status STANDSTILL.
Configured axes have to be added to the kinematics before the kinematics is
enabled.

PLC:

ML_KinEnable
Name         Data type       Inherited   Address      Initial value   Comment
                             from
  Data      ML_KinEna‐                                                InOut: Command parame‐
            bleData                                                   ters
  ML_KinEn‐ BOOL                                                      Returns, whether it was
able                                                                  possible to add the com‐
                                                                      mand to the kinematic
                                                                      object.
                                                                      ● TRUE: The command
                                                                        could be added success‐
                                                                        fully
                                                                      ● FALSE: An error
                                                                        occurred. Details in
                                                                        ML_oCmdResult
STRUCT ML_KinEnableData
Name       Data type    Inherited        Address      Initial value   Comment
                        from
  In       ML_iKinCmd‐                                                Input: Command data of
           Base                                                       the command
  Out      ML_oCmdRe‐                                                 Output: Command parame‐
           sult                                                       ters
STRUCT ML_iKinCmdBase
Name        Data type        Inherited   Address      Initial value   Comment
                             from
  KinName    STRING(63)                                               Name of the kinematics
                                                                      used to execute the com‐
                                                                      mand

STRUCT ML_iKinCmdBase
  Source    STRING(50)                                                   Specifies the command
                                                  source, e.g PlcApplication1
                                                  is displayed in the diag‐
                                                  nostic messages
   SourceLine ULINT                                                      Specifies the source line of
                                                  the command; is displayed
                                                  in the diagnostic messages
STRUCT ML_oCmdResult
Name       Data type             Inherited   Address     Initial value   Comment
                                 from
   CmdID           ULINT                                                 Command ID (is set to
                                                                         18446744073709551615 in
                                                                         the event of an error)
   Error           BOOL                                                  Error ID TRUE indicates
                                                                         that an error occurred
   ErrorID         UDINT                                                 Specifies the type of
                                                                         occurred error: The upper
                                                                         4 bytes reflect the main
                                                                         diagnostics, the lower 4
                                                                         bytes reflect the detailed
                                                                         diagnostics, 0 means no
                                                                         error

Data Layer:
Method: POST
URL:               https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/group-ena
Payload: (blank)

Python:
<cmdID> = motion.kin_cmd_enable( kin=<kinName> )

Generates an Enable kinematics command (object has to be "attached"), see
documentation Python Runtime App ⮫ Python functions.
● <kinName> - string, kinematic name

BundleIF:
The required command type is:

cmd::kin::KinCmdType::KIN_CMD_GROUP_ENA

//! Create a motion command for a kinematic (KIN_CMD_GROUP_*)
//!
//! @param[in]   sourceInfo Command source information
//! @param[in]   kinName     Name of the motion object
//! @param[in]   cmdType     Type of the command
//! @param[out] cmdID        The ID of the added command
//! @return                  Was everything okay?
virtual MotionResult kinGroupCmd(const cmd::CmdSourceInfo&
sourceInfo, const char* kinName, cmd::kin::KinCmdType cmdType,
uint64_t &cmdID ) const = 0;

### 7.3.3 KinDisable - Disabling kinematics

Basics
This command disables the kinematics. Thus, this command directly influ‐
ences the state machine of the kinematics. The state of the kinematics is set
to DISABLED after the command. This command does not switch the power of
the axis added to the kinematics off. The kinematics cannot be used anymore
after it has been disabled.

PLC:

ML_KinDisable
Name         Data type       Inherited   Address       Initial value   Comment
                             from
  Data       ML_KinDisa‐                                               InOut: Command parame‐
             bleData                                                   ters
  ML_KinDis‐ BOOL                                                      Returns, whether it was
able                                                                   possible to add the com‐
                                                                       mand to the kinematic
                                                                       object.
                                                                       ● TRUE: The command
                                                                         could be added success‐
                                                                         fully
                                                                       ● FALSE: An error
                                                                         occurred. Details in
                                                                         ML_oCmdResult
STRUCT ML_KinDisableData
Name       Data type     Inherited       Address       Initial value   Comment
                         from
  In       ML_iKinCmd‐                                                 Input: Command data of
           Base                                                        the command
  Out      ML_oCmdRe‐                                                  Output: Command parame‐
           sult                                                        ters
STRUCT ML_iKinCmdBase
Name        Data type        Inherited   Address       Initial value   Comment
                             from
  KinName    STRING(63)                                                Name of the kinematics
                                                                       used to execute the com‐
                                                                       mand
  Source     STRING(50)                                                Specifies the command
                                                                       source, e.g PlcApplication1
                                                                       is displayed in the diag‐
                                                                       nostic messages
  SourceLine ULINT                                                     Specifies the source line of
                                                                       the command; is displayed
                                                                       in the diagnostic messages

STRUCT ML_oCmdResult
Name       Data type             Inherited   Address      Initial value   Comment
                                 from
   CmdID           ULINT                                                  Command ID (is set to
                                                                          18446744073709551615 in
                                                                          the event of an error)
   Error           BOOL                                                   Error ID TRUE indicates
                                                                          that an error occurred
   ErrorID         UDINT                                                  Specifies the type of
                                                                          occurred error: The upper
                                                                          4 bytes reflect the main
                                                                          diagnostics, the lower 4
                                                                          bytes reflect the detailed
                                                                          diagnostics, 0 means no
                                                                          error

Data Layer:
Method: POST
URL:               https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/group-dis
Payload: (blank)

Python:
<cmdID> = motion.kin_cmd_disable( kin=<kinName> )

Generates a disable kinematic command (object has to be "attached"), see
documentation Python Runtime App ⮫ Python Functions.
● <kinName> - string, kinematic name

BundleIF:
To disable the kinematics, the command type has to be as follows:

cmd::kin::KinCmdType::KIN_CMD_GROUP_DIS

//! Create a motion command for a kinematic (KIN_CMD_GROUP_*)
//!
//! @param[in]   sourceInfo Command source information
//! @param[in]   kinName     Name of the motion object
//! @param[in]   cmdType     Type of the command
//! @param[out] cmdID        The ID of the added command
//! @return                  Was everything okay?
virtual MotionResult kinGroupCmd(const cmd::CmdSourceInfo&
sourceInfo, const char* kinName, cmd::kin::KinCmdType cmdType,
uint64_t &cmdID ) const = 0;

### 7.3.4 KinMoveLinAbs - Absolute traversing of kinematics

Basics
This command moves the kinematics in the PCS in a linear way from the last
commanded TCP position to a specified absolute target position. Select the
coordinate system of the absolute target position.
It is ensured that the defined limit values are complied with.

The kinematics is in state "MOVING” during the motion. After reaching the
end position, the command is set to DONE and the kinematics goes to state
STANDBY.
The programming limit values for velocity, acceleration, deceleration as well
as both jerk limits have to be positive (greater than zero), as otherwise the
parameters would be inconsistent.
Exception: If both jerk limit values are exactly zero, the motion is executed
without jerk limit (trapezoid velocity profile).
                     If the motion passes through a singularity or close to
        WARNING      a singularity, unexpectedly large accelerations and high
                     axis velocities may occur. For further information, refer
                     to ⮫ Dealing with singularities on page 194

The motion can be generated as buffered or unbuffered command. The buf‐
fered commands are stored in a command buffer and executed sequentially.
Unbuffered commands are prepared in a high-priority task. They cancel the
currently active command once it is ready to be executed. The remaining com‐
mand buffer is deleted (all commands are assigned the state ABORTED, when
querying the status with GetCmdState, see ⮫ Chapter 7.8.7 GetCmdState -
Command states on page 787). It is recommended to use buffered commands
when possible. The unbuffered commands have a major impact on the tem‐
poral behavior of the system and can result in considerable delays of other
tasks. Additionally, a sequence of commands can be executed faster if it is
commanded as a sequence of buffered commands.
If an error occurred during the execution (e.g. unknown coordinate system
of target position), the command was not added to the kinematics object. If
an error occurred during the execution, the kinematic status is set to ERROR‐
STOP.

PLC:

ML_KinMoveLinAbs
Name        Data type        Inherited   Address       Initial value   Comment
                             from
  Data      ML_KinMove‐                                                InOut: Command parame‐
            LinAbs                                                     ters
  ML_KinMo‐ BOOL                                                       Returns, whether it was
veLinAbs                                                               possible to add the com‐
                                                                       mand to the kinematic
                                                                       object.
                                                                       ● TRUE: The ML_KinMove‐
                                                                         LinAbs command could
                                                                         be added successfully
                                                                       ● FALSE: An error
                                                                         occurred. Details in
                                                                         ML_oCmdResult
STRUCT ML_KinMoveLinData
Name       Data type    Inherited        Address       Initial value   Comment
                        from

STRUCT ML_KinMoveLinData
  In       ML_iKinMo‐                                                     Input: Command data of
veLin                                                          the command
  Out      ML_oCmdRe‐                                                     Output: Command parame‐
sult                                                           ters
STRUCT ML_iKinMoveLin EXTENDS ML_iKinCmdBase
Name        Data type   Inherited   Address               Initial value   Comment
                        from
  KinName STRING(63) ML_iKinCmd‐                                          Name of the kinematics
                        Base                                              used to execute the com‐
                                                                          mand
   Source          STRING(50)     ML_iKinCmd‐                             Specifies the command
                                  Base                                    source, e.g PlcApplication1
                                                                          is displayed in the diag‐
                                                                          nostic messages
   SourceLine ULINT               ML_iKinCmd‐                             Specifies the source line of
                                  Base                                    the command; is displayed
                                                                          in the diagnostic messages
   Position        ARRAY[0..15]                                           Commanded absolute
                   OF LREAL                                               target position
   CoordSys        STRING(15)                                             Coordinate system of the
                                                                          commanded target position
                                                                          (PCS, WCS, MCS or ACS
   Buffered        BOOL                                   TRUE            TRUE, if the command
                                                                          is to be executed as buf‐
                                                                          fered command, otherwise
                                                                          FALSE
   DynLimits ML_iDynLi‐                                                   Limit values of the position
             mits                                                         command
STRUCT ML_iDynLimits
Name        Data type             Inherited     Address   Initial value   Comment
                                  from
   Velocity        LREAL                                                  Velocity limit value
   Accelera‐       LREAL                                                  Acceleration limit value
tion
   Decelera‐       LREAL                                                  Deceleration limit value
tion
   JerkAcc         LREAL                                  0               Jerk limit value for acceler‐
                                                                          ation phase
   JerkDec         LREAL                                  0               Jerk limit value for deceler‐
                                                                          ation phase
STRUCT ML_oCmdResult
Name       Data type              Inherited     Address   Initial value   Comment
                                  from
   CmdID           ULINT                                                  Command ID (is set to
                                                                          18446744073709551615 in
                                                                          the event of an error)
   Error           BOOL                                                   Error ID TRUE indicates
                                                                          that an error occurred

STRUCT ML_oCmdResult
  ErrorID  UDINT                                                      Specifies the type of
                                                  occurred error: The upper
                                                  4 bytes reflect the main
                                                  diagnostics, the lower 4
                                                  bytes reflect the detailed
                                                  diagnostics, 0 means no
                                                  error

Data Layer:
Method: POST
URL:               https://<ip-addr>/automation/api/v2/nodes/motion/kin/

<kin_name>/cmd/move-abs
Payload:

{
"type":"object","value":
{
"kinPos":
[10,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
],
"coordSys":"WCS",

"lim":{
                     "vel":800,
                     "acc":3,
                     "dec":3,
                     "jrkAcc":0,
                     "jrkDec":0
                 }
}
}

Python
<cmdID> = motion.kin_cmd_move_lin_abs( kin=<kinName>,
pos=<targetPos> [,coord_sys=<coordSys>] [,vel=<velocity>]
[,acc=<acceleration>] [,dec=<deceleration>]
[,jrkacc=<jerkAcceleration>] [,jrk_dec=<jerkDeceleration>]
[,buffered=<buffered>] )

Creates a MoveLinAbs command for a kinematics (object has to be
"attached"), see documentation Python Runtime App ⮫ Python functions.
● <kinName> - string, kinematic name
● <pos> - tuple of double or list of double (16 values max.), target position
  of the command
● <coordSys> - string ("PCS", "WCS", "MCS" or "ACS")
● <velocity> - double, velocity limit value of the command (the last pro‐
  grammed velocity limit value is used if this parameter is not programmed)
● <acceleration> - double, acceleration limit value of the command (the last
  programmed acceleration limit value is used if this parameter is not pro‐
  grammed)
● <deceleration> - double, deceleration limit value of the command (the last
  programmed deceleration limit value is used if this parameter is not pro‐
  grammed)

● <jerkAcceleration> - double, jerk limit value for the acceleration of the com‐
  mand (the last programmed jerk limit value for the acceleration is used if
  this parameter is not programmed)
● <jerkDeceleration> - double, jerk limit value for the deceleration of the
  command (the last programmed jerk limit value for the deceleration is used
  if this parameter is not programmed)
● <buffered> - bool, use TRUE if the command is to be buffered (TRUE by
  default)

BundleIF:
Command type for a linear motion with absolute target position:

cmd::kin::KinCmdType::KIN_CMD_MOVE_ABS
//! Create a motion command for a kinematic (KIN_CMD_MOVE_*)
//!
//! @param[in]   sourceInfo Command source information
//! @param[in]   kinName     Name of the motion object
//! @param[in]   cmdType     Type of the command
//! @param[in]   targetPos   Target position of the command
//! @param[in]   targetCOS   Target coordinate system for the
targetPos
//! @param[in]   dynLim      Dynamic limits of the command
//! @param[in]   buffered    Create as a buffered command
//! @param[out] cmdID        The ID of the added command
//! @return                  Was everything okay?
virtual MotionResult kinMoveCmd(const cmd::CmdSourceInfo&
sourceInfo, const char* kinName, cmd::kin::KinCmdType cmdType,
double *targetPos, cmd::kin::CmdTargetCOS targetCOS, const
cmd::DynamicLimitsT &dynLim, bool buffered, uint64_t &cmdID )
const = 0;

### 7.3.5 KinMoveLinRel - Relative traversing of kinematics

Basics
This command moves the kinematics in the PCS in a linear way from the last
commanded TCP position to a specified relative target position. Select the
coordinate system of the relative position.
It is ensured that the defined limits are complied with.
The kinematics is in state "MOVING” during the motion. After reaching the end
position, the command is set to DONE and the kinematics goes to STANDBY
mode.
The programming limit values for velocity, acceleration, deceleration as well
as both jerk limits have to be positive (greater than zero), as otherwise the
parameters would be inconsistent.
Exception: If both jerk limit values are exactly zero, the motion is executed
without jerk limit (trapezoid velocity profile).
                      If the motion passes through a singularity or close to
         WARNING      a singularity, unexpectedly large accelerations and high
                      axis velocities may occur. For further information, refer
                      to ⮫ Dealing with singularities on page 194
The motion can be generated as buffered or unbuffered command. The buf‐
fered commands are stored in a command buffer and executed sequentially.
Unbuffered commands are prepared in a high-priority task. They cancel the
currently active command once it is ready to be executed. The remaining com‐

mand buffer is deleted (all commands are assigned the state ABORTED, when
querying the status with GetCmdState, see ⮫ Chapter 7.8.7 GetCmdState -
Command states on page 787). It is recommended to use buffered commands
when possible. The unbuffered commands have a major impact on the tem‐
poral behavior of the system and can result in considerable delays of other
tasks. Additionally, a sequence of commands can be executed faster if it is
commanded as a sequence of buffered commands.
If an error occurred during the execution (e.g. unknown coordinate system
of target position), the command was not added to the kinematics object. If
an error occurred during the execution, the kinematic status is set to ERROR‐
STOP.

PLC:

ML_KinMoveLinRel
Name        Data type       Inherited     Address      Initial value   Comment
                            from
  Data      ML_KinMove‐                                                InOut: Command parame‐
            LinRel                                                     ters
  ML_KinMo‐ BOOL                                                       Returns, whether it was
veLinRel                                                               possible to add the com‐
                                                                       mand to the kinematic
                                                                       object.
                                                                       ● TRUE: The ML_KinMove‐
                                                                         LinREL command could
                                                                         be added successfully
                                                                       ● FALSE: An error
                                                                         occurred. Details in
                                                                         ML_oCmdResult
STRUCT ML_KinMoveLinData
Name       Data type    Inherited         Address      Initial value   Comment
                        from
  In       ML_iKinMo‐                                                  Input: Command data of
           veLin                                                       the command
  Out      ML_oCmdRe‐                                                  Output: Command parame‐
           sult                                                        ters
STRUCT ML_iKinMoveLin EXTENDS ML_iKinCmdBase
Name        Data type   Inherited   Address            Initial value   Comment
                        from
  KinName STRING(63) ML_iKinCmd‐                                       Name of the kinematics
                        Base                                           used to execute the com‐
                                                                       mand
  Source     STRING(50)     ML_iKinCmd‐                                Specifies the command
                            Base                                       source, e.g PlcApplication1
                                                                       is displayed in the diag‐
                                                                       nostic messages

STRUCT ML_iKinMoveLin EXTENDS ML_iKinCmdBase
  SourceLine ULINT      ML_iKinCmd‐                                      Specifies the source line of
Base                                             the command; is displayed
                                                 in the diagnostic messages
   Position        ARRAY[0..15]                                          Commanded relative target
OF LREAL                                              position
   CoordSys        STRING(15)                                            Coordinate system of the
                                                 commanded target position
                                                 (PCS, WCS, MCS or ACS
   Buffered        BOOL                                  TRUE            TRUE, if the command
                                                 is to be executed as buf‐
                                                 fered command, otherwise
                                                 FALSE
   DynLimits ML_iDynLi‐                                                  Limit values of the position
mits                                                        command
STRUCT ML_iDynLimits
Name        Data type             Inherited   Address    Initial value   Comment
                                  from
   Velocity        LREAL                                                 Velocity limit value
   Accelera‐       LREAL                                                 Acceleration limit value
tion
   Decelera‐       LREAL                                                 Deceleration limit value
tion
   JerkAcc         LREAL                                 0               Jerk limit value for acceler‐
                                                                         ation phase
   JerkDec         LREAL                                 0               Jerk limit value for deceler‐
                                                                         ation phase
STRUCT ML_oCmdResult
Name       Data type              Inherited   Address    Initial value   Comment
                                  from
   CmdID           ULINT                                                 Command ID (is set to
                                                                         18446744073709551615 in
                                                                         the event of an error)
   Error           BOOL                                                  Error ID TRUE indicates
                                                                         that an error occurred
   ErrorID         UDINT                                                 Specifies the type of
                                                                         occurred error: The upper
                                                                         4 bytes reflect the main
                                                                         diagnostics, the lower 4
                                                                         bytes reflect the detailed
                                                                         diagnostics, 0 means no
                                                                         error

Data Layer:
Method: POST
URL:               https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/move-rel
Payload:

{
"type":"object","value":
{

"kinPos":[10, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
"coordSys":"WCS",
"lim":{
                "vel":800,
                "acc":3,
                "dec":3,
                "jrkAcc":0,
                "jrkDec":0
              }
}
}

Python:
<cmdID> = motion.kin_cmd_move_lin_rel( kin=<kinName>,
pos=<targetPos> [,coord_sys=<coordSys>] [,vel=<velocity>]
[,acc=<acceleration>] [,dec=<deceleration>]
[,jrk_acc=<jerkAcceleration>] [,jrkdec=<jerkDeceleration>]
[,buffered=<buffered>] )

Creates a MoveLinRel command for a kinematics (object has to be
"attached"), see documentation Python Runtime App ⮫ Python functions.
● <kinName> - string, kinematic name
● <pos> - tuple of double or list of double (16 values max.), target position
  of the command
● <coordSys> - string ("PCS", "WCS", "MCS" or "ACS")
● <velocity> - double, velocity limit value of the command (the last pro‐
  grammed velocity limit value is used if this parameter is not programmed)
● <acceleration> - double, acceleration limit value of the command (the last
  programmed acceleration limit value is used if this parameter is not pro‐
  grammed)
● <deceleration> - double, deceleration limit value of the command (the last
  programmed deceleration limit value is used if this parameter is not pro‐
  grammed)
● <jerkAcceleration> - double, jerk limit value for the acceleration of the com‐
  mand (the last programmed jerk limit value for the acceleration is used if
  this parameter is not programmed)
● <jerkDeceleration> - double, jerk limit value for the deceleration of the
  command (the last programmed jerk limit value for the deceleration is used
  if this parameter is not programmed)
● <buffered> - bool, use TRUE if the command is to be buffered (TRUE by
  default)

BundleIF:
To move the kinematics linear relative, the command type has to be as fol‐
lows:

cmd::kin::KinCmdType::KIN_CMD_MOVE_REL
//! Create a motion command for a kinematic (KIN_CMD_MOVE_*)
//!
//! @param[in]   sourceInfo Command source information
//! @param[in]   kinName     Name of the motion object
//! @param[in]   cmdType     Type of the command
//! @param[in]   targetPos   Target position of the command
//! @param[in]   targetCOS   Target coordinate system for the

targetPos
//! @param[in]   dynLim      Dynamic limits of the command
//! @param[in]   buffered    Create as a buffered command
//! @param[out] cmdID        The ID of the added command
//! @return                  Was everything okay?
virtual MotionResult kinMoveCmd(const cmd::CmdSourceInfo&
sourceInfo, const char* kinName, cmd::kin::KinCmdType cmdType,
double *targetPos, cmd::kin::CmdTargetCOS targetCOS, const
cmd::DynamicLimitsT &dynLim, bool buffered, uint64_t &cmdID )
const = 0;

### 7.3.6 KinMoveDirectAbs - Direct absolute traversing of kinematics

Basics
This command commands a kinematic motion to the specified absolute posi‐
tion in the specified coordinate system to which the actuator path is not
relevant to.
Prerequisite: The kinematics has to be enabled.
During the motion, the PLCopen state of the kinematics is set to MOVING. It
is ensured that the configured dynamic limits of all axes are complied with.
No path dynamics is taken into consideration, thus, a very fast motion can
take place. All axis motion phases are synchronous. This means that the time
sections for acceleration and motion with constant velocity and deceleration
are identical for all axes. In such a phase, at least one axis moves along one of
its dynamic limits.
The target position can be specified in any existing coordinate system. The
motion ends with velocity and with velocity or acceleration equal to zero.
If the commanded target position is reached, the command is set to state
DONE and the PLCopen state of the kinematics is set to STANDBY.
Use|ML_KinGetPLCOpenState| or |ML_GetCmdState| to determine the current
state.
The motion can be generated as buffered or unbuffered command. The buf‐
fered commands are stored in a command buffer and executed sequentially.
Unbuffered commands are prepared in a high-priority task. They cancel the
currently active command once it is ready to be executed. The remaining com‐
mand buffer is deleted (all commands are assigned the state ABORTED, when
querying the status with GetCmdState, see ⮫ Chapter 7.8.7 GetCmdState -
Command states on page 787). It is recommended to use buffered commands
when possible. The unbuffered commands have a major impact on the tem‐
poral behavior of the system and can result in considerable delays of other
tasks. Additionally, a sequence of commands can be executed faster if it is
commanded as a sequence of buffered commands.
If an error occurred during the execution (e.g. unknown coordinate system
of target position), the command was not added to the kinematics object. If
an error occurred during the execution, the kinematic status is set to ERROR‐
STOP.
The programming limit values for velocity, acceleration, deceleration as well
as both jerk limits have to be positive (greater than zero), as otherwise the
parameters would be inconsistent.
Exception: If both jerk limit values are exactly zero, the motion is executed
without jerk limit (trapezoid velocity profile).

PLC:

ML_KinMoveDirectAbs
Name       Data type        Inherited     Address   Initial value   Comment
                            from
  Data      ML_KinMove‐                                             InOut: Command parame‐

DirectAbs                                               ters
  ML_KinMo‐ BOOL                                                    Returns, whether it was
veDirectAbs                                                         possible to add the com‐
mand to the kinematic
object.
● TRUE: The ML_KinMo‐
  veDirectAbs command
  could be added success‐
  fully
● FALSE: An error
  occurred. Details in
  ML_oCmdResult
STRUCT ML_KinMoveDirectData
Name       Data type    Inherited         Address   Initial value   Comment
                        from
  In       ML_iKinMo‐                                               Input: Command data of
           veDirect                                                 the command
  Out      ML_oCmdRe‐                                               Output: Command parame‐
           sult                                                     ters
STRUCT ML_iKinMoveDirect EXTENDS ML_iKinCmdBase
Name        Data type    Inherited  Address     Initial value       Comment
                         from
  KinName STRING(15) ML_iKinCmd‐                                    Name of the kinematics
                         Base                                       used to execute the com‐
                                                                    mand
  Source     STRING(50)     ML_iKinCmd‐                             Specifies the command
                            Base                                    source, e.g PlcApplication1
                                                                    is displayed in the diag‐
                                                                    nostic messages
  SourceLine ULINT          ML_iKinCmd‐                             Specifies the source line of
                            Base                                    the command; is displayed
                                                                    in the diagnostic messages
  Position   ARRAY[0..15]                                           Commanded absolute
             OF LREAL                                               target position
  CoordSys   STRING(15)                                             Relevant coordinate system
                                                                    of the commanded target
                                                                    position (PCS, WCS, MCS
                                                                    or ACS

STRUCT ML_iKinMoveDirect EXTENDS ML_iKinCmdBase
  Buffered  BOOL                                TRUE                       TRUE, if the command
                                                    is to be executed as buf‐
                                                    fered command, otherwise
                                                    FALSE
STRUCT ML_oCmdResult
Name       Data type             Inherited   Address       Initial value   Comment
                                 from
   CmdID           ULINT                                                   Command ID (is set to
                                                                           18446744073709551615 in
                                                                           the event of an error)
   Error           BOOL                                                    Error ID TRUE indicates
                                                                           that an error occurred
   ErrorID         ULINT                                                   Specifies the type of
                                                                           occurred error: The upper
                                                                           4 bytes refer to the main
                                                                           diagnostics, the lower 4
                                                                           bytes refer to the detailed
                                                                           diagnostics, 0 means no
                                                                           error

Data Layer:
Method: POST
URL:               https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/move-direct-abs
Payload:

{
"type":"object","value":
{
"kinPos":[10.0, 10.0, 5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
"coordSys":"WCS",
"buffered":false
}
}

Python:
<cmdID> = motion.kin_cmd_move_direct_abs( kin=<kinName>,
pos=<targetPos> [,coord_sys=<targetCoordinateSystem>]
[,buffered=<buffered>])

Creates a MoveDirectAbs command for a kinematics (object has to be
"attached"), see documentation Python Runtime App ⮫ Python functions.
● <kinName> - string, kinematic name
● <pos> - tuple of double or list of double (16 values max.), target position
  of the command
● <targetCoordinateSystem> - Coordinate system in which <pos> is defined
  (coordinate system is "PCS”, if not programmed
● <buffered> - boolean, is this command supposed to be a buffered com‐
  mand?

BundleIF:
Command type for a linear motion with absolute target position:

cmd::kin::KinCmdType::KIN_CMD_MOVE_DIRECT_ABS
//! Create a motion command for a kinematic
(KIN_CMD_MOVE_DIRECT_*)
//!
//! @param[in]   sourceInfo Command source information
//! @param[in]   kinName     Name of the motion object
//! @param[in]   cmdType     Type of the command
//! @param[in]   targetPos   Target position of the command
//! @param[in]   targetCOS   Target coordinate system for the
targetPos

//! @param[in]   buffered    Create as a buffered command?
//! @param[out] cmdID        The ID of the added command
//! @return                  Was everything okay?
MotionResult kinMoveDirectCmd(const dia::CmdSourceInfo&
sourceInfo, const char* kinName, cmd::kin::KinCmdType cmdType,
const double *targetPos, cmd::kin::CmdTargetCOS targetCOS,
bool buffered, uint64_t &cmdID ) const;

### 7.3.7 KinMoveDirectRel - Direct relative traversing of kinematics

Basics
This function commands a kinematic motion to the specified relative position
in the specified coordinate system to which the actuator path is not relevant
to.
Prerequisite: The kinematics has to be enabled.
During the motion, the PLCopen state of the kinematics is set to MOVING. It
is ensured that the configured dynamic limits of all axes are complied with.
No path dynamics is taken into consideration, thus, a very fast motion can
take place. All axis motion phases are synchronous. This means that the time
sections for acceleration and motion with constant velocity and deceleration
are identical for all axes. In such a phase, at least one axis moves along one of
its dynamic limits.
The target position can be specified in any existing coordinate system. The
motion ends with velocity and with velocity or acceleration equal to zero.
If the commanded target position is reached, the command is set to state
DONE and the PLCopen state of the kinematics is set to STANDBY. Use|
ML_KinGetPLCOpenState| or |ML_GetCmdState| to determine the current
state.
The motion can be generated as buffered or unbuffered command. The buf‐
fered commands are stored in a command buffer and executed sequentially.
Unbuffered commands are prepared in a high-priority task. They cancel the
currently active command once it is ready to be executed. The remaining com‐
mand buffer is deleted (all commands are assigned the state ABORTED, when
querying the status with GetCmdState, see ⮫ Chapter 7.8.7 GetCmdState -
Command states on page 787). It is recommended to use buffered commands
when possible. The unbuffered commands have a major impact on the tem‐
poral behavior of the system and can result in considerable delays of other
tasks. Additionally, a sequence of commands can be executed faster if it is
commanded as a sequence of buffered commands.

If an error occurred during the execution (e.g. unknown coordinate system
of target position), the command was not added to the kinematics object. If
an error occurred during the execution, the kinematic status is set to ERROR‐
STOP.
The programming limit values for velocity, acceleration, deceleration as well
as both jerk limits have to be positive (greater than zero), as otherwise the
parameters would be inconsistent.
Exception: If both jerk limit values are exactly zero, the motion is executed
without jerk limit (trapezoid velocity profile).

PLC:

ML_KinMoveDirectRel
Name       Data type            Inherited     Address     Initial value   Comment
                                from
   Data     ML_KinMove‐                                                   InOut: Command parame‐
            DirectRel                                                     ters
  ML_KinMo‐ BOOL                                                          Returns, whether it was
veDirectRel                                                               possible to add the com‐
                                                                          mand to the kinematic
                                                                          object.
                                                                          ● TRUE: The ML_KinMo‐
                                                                            veDirectRel command
                                                                            could be added success‐
                                                                            fully
                                                                          ● FALSE: An error
                                                                            occurred. Details in
                                                                            ML_oCmdResult
STRUCT ML_KinMoveDirectData
Name       Data type    Inherited             Address     Initial value   Comment
                        from
  In       ML_iKinMo‐                                                     Input: Command data of
           veDirect                                                       the command
  Out      ML_oCmdRe‐                                                     Output: Command parame‐
           sult                                                           ters
STRUCT ML_iKinMoveDirect EXTENDS ML_iKinCmdBase
Name        Data type    Inherited  Address     Initial value             Comment
                         from
  KinName STRING(15) ML_iKinCmd‐                                          Name of the kinematics
                         Base                                             used to execute the com‐
                                                                          mand
   Source          STRING(50)   ML_iKinCmd‐                               Specifies the command
                                Base                                      source, e.g PlcApplication1
                                                                          is displayed in the diag‐
                                                                          nostic messages

STRUCT ML_iKinMoveDirect EXTENDS ML_iKinCmdBase
  SourceLine ULINT       ML_iKinCmd‐                                 Specifies the source line of
     Base                                        the command; is displayed
                                                 in the diagnostic messages
 Position    ARRAY[0..15]                                            Commanded absolute
OF LREAL                                                target position
 CoordSys    STRING(15)                                              Relevant coordinate system
                                                 of the commanded target
                                                 position (PCS, WCS, MCS
                                                 or ACS
 Buffered    BOOL                                    TRUE            True, if the command is
                                                 to be executed as buf‐

                                                 fered command, otherwise
                                                 FALSE
STRUCT ML_oCmdResult
Name       Data type          Inherited   Address    Initial value   Comment
                              from
 CmdID       ULINT                                                   Command ID (is set to
                                                                     18446744073709551615 in
                                                                     the event of an error)
 Error       BOOL                                                    Error ID TRUE indicates
                                                                     that an error occurred
 ErrorID     ULINT                                                   Specifies the type of
                                                                     occurred error: The upper
                                                                     4 bytes reflect the main
                                                                     diagnostics, the lower 4
                                                                     bytes reflect the detailed
                                                                     diagnostics, 0 means no
                                                                     error

Data Layer:
Method: POST
URL:               https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/move-direct-rel
Payload:

{
"type":"object","value":
{
"kinPos":[10.0, 10.0, 5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
"coordSys":"WCS",
"buffered":false
}
}

Python:
<cmdID> = motion.kin_cmd_move_direct_rel( kin=<kinName>,
pos=<targetPos> [,coord_sys=<targetCoordinateSystem>]
[,buffered=<buffered>])

Creates a MoveDirectAbs command for a kinematics (object has to be
"attached"), see documentation Python Runtime App ⮫ Python functions.

● <kinName> - string, kinematic name
● <pos> - tuple of double or list of double (16 values max.), target position
  of the command
● <targetCoordinateSystem> - Coordinate system in which <pos> is defined
  (coordinate system is "PCS”, if not programmed
● <buffered> - boolean, is this command supposed to be a buffered com‐
  mand?

BundleIF:
For commanding with relative target position, the following command type is
used:

cmd::kin::KinCmdType::KIN_CMD_MOVE_DIRECT_REL
//! Create a motion command for a kinematic
(KIN_CMD_MOVE_DIRECT_*)
//!
//! @param[in]   sourceInfo Command source information
//! @param[in]   kinName     Name of the motion object
//! @param[in]   cmdType     Type of the command
//! @param[in]   targetPos   Target position of the command
//! @param[in]   targetCOS   Target coordinate system for the
targetPos
//! @param[in]   buffered    Create as a buffered command
//! @param[out] cmdID        The ID of the added command
//! @return                  Was everything okay?
MotionResult kinMoveDirectCmd(const dia::CmdSourceInfo&
sourceInfo, const char* kinName, cmd::kin::KinCmdType cmdType,
const double *targetPos, cmd::kin::CmdTargetCOS targetCOS,
bool buffered, uint64_t &cmdID ) const;

### 7.3.8 KinMoveDirectAsyncAbs - Direct asynchronous absolute tra‐

versing of kinematics
Basics
This function commands a kinematic motion to the specified absolute position
in the specified coordinate system to which the actuator path is not relevant
to.
The axes move asynchronously.
Prerequisite: The kinematics has to be enabled.

During the motion, the PLCopen state of the kinematics is set to MOVING. It
is ensured that the configured dynamic limits of all axes are complied with.
No path dynamics is taken into consideration, thus, a very fast motion can
take place. All motion phases of the axes are asynchronous. This means that
the axes simultaneously start the interpolation but that the motion is not
synchronous. Each axis reaches the target position as fast as it is possible
with the dynamic limits specified by the given factors.
The target position can be specified in any existing coordinate system. The
motion ends with velocity and with velocity or acceleration equal to zero.
Factors impact the dynamic motion limit values:
● The following applies to the velocity factor:
  – No factors specified - no reduction takes place
  – 0.0/1.0 – no reduction
  – < 0.001 – not permitted

   – >= 0.001 – the configured maximum axis velocities apply as reduced
     (0.1% ... 100%)
   – > 1 - not permitted
● The following applies to acceleration, deceleration, acceleration jerk and
   deceleration jerk:
   – 0 – the previous factor is used for reduction.
     The following order applies:
     Velocity, acceleration, deceleration, acceleration jerk, deceleration jerk
   – > 0 – the specified factor applies
   – > 1 – not permitted
Examples:
● All factors 0 or 1 → the configured, dynamic axis limit values apply

● Velocity factor = 0.75, other factors = 0.0 → Axes must be moved at a
    maximum of 75 % of the configured dynamic axis limit values. The factor
    applies to all axis limit values
● All factors 0.0, except the acceleration jerk factor = 0.5 → Axes can move
    with the configured dynamic axis limit value. The jerks for acceleration and
    deceleration are reduced by 50 %
● Velocity factor = 0.8, acceleration factor = 1.0, other factors = 0.0 → Axes
    must be moved at a maximum of 80 % of the configured velocity, all other
    limit values apply according to the configuration
If the commanded target position is reached, the command is set to state
DONE and the PLCopen state of the kinematics is set to STANDBY. Use|
ML_KinGetPLCOpenState| or |ML_GetCmdState| to determine the current
state.
The motion can be generated as buffered or unbuffered command. The buf‐
fered commands are stored in a command buffer and executed sequentially.
Unbuffered commands are prepared in a high-priority task. They cancel the
currently active command once it is ready to be executed. The remaining com‐
mand buffer is deleted (all commands are assigned the state ABORTED, when
querying the status with GetCmdState, see ⮫ Chapter 7.8.7 GetCmdState -
Command states on page 787). It is recommended to use buffered commands
when possible. The unbuffered commands have a major impact on the tem‐
poral behavior of the system and can result in considerable delays of other
tasks. Additionally, a sequence of commands can be executed faster if it is
commanded as a sequence of buffered commands.
No axis assigned
If a motion is commanded for a kinematics in which a coordinate index is
moved and no axis is assigned to the index, this coordinate is interpolated
synchronously to the slowest axis. If the no coordinate is part of the com‐
manded motion to which an axis is assigned, the coordinates reach their
target point within one cycle.
Example 1:
● The axes "X" and "Y" are assigned to the kinematics to the indices 0 and 1
● A motion is commanded to (1, 2, 3) → No axis is assigned to the third
  index
● In this example, the "X" axis should require 1.5 s for the motion and the "Y"
  axis should require 1.9 s.
  – The third coordinate is moved synchronously to "Y" and reaches its
     target position from 3 to 1.9 s (identical to axis "Y")

Example 2:
● The axes "X" and "Y" are assigned to the kinematics to the indices 0 and 1
● A relative motion is commanded to (0, 0, 1) → No axis is assigned to the
   third index and no other axis is part of the process.
   – After one cycle, the coordinate reaches its target position of 1
Restriction regarding safe zones and working ranges
The TCP path is not defined in this command. Additionally, asynchronous
input (in particular overrides, see ⮫ Chapter 7.7.3 SetOverride - Override
on page 739 and ⮫ Chapter 7.7.2 GetOverride - Reading out the override
on page 737) directly influence the traveled path. Therefore, a more detailed
check of the protection zones and working areas is not possible. This com‐
mand only checks the straight line between start point and target point. Thus,
range violations are reported even though no violations would occur or viola‐
tions are not detected. It is recommended not to use this command in close
proximity to a safe zone or a working area, see ⮫ Chapter 7.5.9 KinSafeAreaP -
Working areas/safe zones on page 672.
If an error occurred during the execution (e.g. unknown coordinate system
of target position), the command was not added to the kinematics object. If
an error occurred during the execution, the kinematic status is set to ERROR‐
STOP.

PLC:

ML_KinMoveDirectAsyncAbs
Name          Data type   Inherited          Address       Initial value   Comment
                          from
  Data        ML_KinMove‐                                                  InOut: Command parame‐
              DirectAsyn‐                                                  ters
              cAbs
  ML_KinMo‐ BOOL                                                           Returns, whether it was
veDirectAsyn‐                                                              possible to add the com‐
cAbs                                                                       mand to the kinematic
                                                                           object.
                                                                           ● TRUE: The ML_KinMo‐
                                                                             veDirectAsyncAbs com‐
                                                                             mand could be added
                                                                             successfully
                                                                           ● FALSE: An error
                                                                             occurred. Details in
                                                                             ML_oCmdResult
STRUCT ML_KinMoveDirectAsyncData
Name       Data type    Inherited            Address       Initial value   Comment
                        from
  In       ML_iKinMo‐                                                      Input: Command data of
           veDirectA‐                                                      the command
           sync

STRUCT ML_KinMoveDirectAsyncData
  Out      ML_oCmdRe‐                                                 Output: Command parame‐
sult                                                       ters
STRUCT ML_iKinMoveDirectAsync EXTENDS ML_iKinCmdBase
Name        Data type   Inherited   Address     Initial value         Comment
                        from
  KinName STRING(15) ML_iKinCmd‐                                      Name of the kinematics
                        Base                                          used to execute the com‐
                                                                      mand
  Source       STRING(50)     ML_iKinCmd‐                             Specifies the command
                              Base                                    source, e.g PlcApplication1
                                                                      is displayed in the diag‐

nostic messages
  SourceLine ULINT            ML_iKinCmd‐                             Specifies the source line of
Base                                    the command; is displayed
in the diagnostic messages
  Position     ARRAY[0..15]                                           Commands absolute target
OF LREAL                                               position (absolute or rel‐
ative), depending on the
command type
  CoordSys     STRING(15)                                             Relevant coordinate system
of the commanded target
position (PCS, WCS, MCS
or ACS
  Buffered     BOOL                                   TRUE            TRUE, if the command
is to be executed as buf‐
fered command, otherwise
FALSE
  DynLim‐      ML_iDynLi‐                                             Factors (0 ... 1) for
Factors        mits                                                   dynamic motion limits
(velocity, acceleration,
deceleration, jerkAcc,
jerkDec)
STRUCT ML_iDynLimits
Name        Data type         Inherited     Address   Initial value   Comment
                              from
   Velocity    LREAL                                                  Velocity limit value
   Accelera‐   LREAL                                                  Acceleration limit value
tion
   Decelera‐   LREAL                                                  Deceleration limit value
tion
   JerkAcc     LREAL                                  0               Jerk limit value for acceler‐
                                                                      ation phase
  JerkDec      LREAL                                  0               Jerk limit value for deceler‐
                                                                      ation phase
STRUCT ML_oCmdResult
Name       Data type          Inherited     Address   Initial value   Comment
                              from
  CmdID        ULINT                                                  Command ID (is set to
                                                                      18446744073709551615 in
                                                                      the event of an error)

STRUCT ML_oCmdResult
  Error    BOOL                                                           Error ID TRUE indicates
                                                   that an error occurred
   ErrorID         ULINT                                                  Specifies the type of
                                                   occurred error: The upper
                                                   4 bytes reflect the main
                                                   diagnostics, the lower 4
                                                   bytes reflect the detailed
                                                   diagnostics, 0 means no
                                                   error

Data Layer:
Method: POST
URL:               https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/move-direct-async-abs
Payload:

{
"type":"object","value":
{
"kinPos":[10.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
"coordSys":WCS,
"dynLimFactors": {
                 "vel":1,
                 "acc":1,
                 "dec":1,
                 "jrkAcc":1,
                 "jrkDec":1
              },
"buffered":false
}
}

Python:
<cmdID> = motion.kin_cmd_move_direct_async_abs( kin=<kinName>,
pos=<targetPos> [,coord_sys=<targetCoordinateSystem>]
[,vel_factor=<velocityFactor>]
[,acc_factor=<accelerationFactor>]
[,dec_factor=<decelerationFactor>]
[,jrk_acc_factor=<jerkAccelerationFactor>]
[,jrk_dec_factor=<jerkDecelerationFactor>]
[,buffered=<buffered>])

Creates a MoveDirectAsyncAbs command for a kinematics (object has to be
"attached"), see documentation Python Runtime App ⮫ Python functions.
● <kinName> - string, kinematic name
● <targetPos> - tuple of double or list of double (max. 16 values), target
  position of command
● <targetCoordinateSystem> - Coordinate system in which <pos> is defined
  (coordinate system is "PCS”, if not programmed)
● <velocityFactor> - double, velocity limit factor of the command (set velocity
  limit factor for this kinematics to "1", for "0" or not programmed → no
  limit)

● <accelerationFactor> - double, acceleration limit factor of the command
  (the last programmed acceleration limit factor is used (if this factor is
  unequal to “0”), if this parameter is not programmed or if the value “0” is
  specified)
● <decelerationFactor> - double, deceleration limit factor of the command
  (the last programmed deceleration limit factor is used (if this factor is
  unequal to “0”), if this parameter is not programmed or if the value “0” is
  specified)
● <jerkAccelerationFactor> - double, factor for the jerk limit of the accelera‐
  tion of the command (the last programmed factor is used for the jerk limit
  of the acceleration (if this factor is unequal to “0”), if this parameter is not
  programmed or if the value “0” is specified)
● <jerkDecelerationFactor> - double, factor for jerk limit of the deceleration

  of the command (the last programmed factor for the jerk limit of the decel‐
  eration is used (if this factor is unequal to “0”), if this parameter is not
  programmed or if the value “0” is specified)
● <buffered> - bool, use TRUE if the command is to be buffered (TRUE by
  default)

BundleIF:
For commanding with absolute target position, the following command type is
used:

cmd::kin::KinCmdType::KIN_CMD_MOVE_DIRECT_ASYNC_ABS
//! @brief Create a motion command for a kinematic
(KIN_CMD_MOVE_DIRECT_ASYNC_*)
//!
//! @param[in]   sourceInfo    Command source information
//! @param[in]   kinName       Name of the motion object
//! @param[in]   cmdType       Type of the command
//! @param[in]   targetPos     Target position of the command
//! @param[in]   targetCOS     Target coordinate system for
the targetPos
//! @param[in]   dynLimFactors Dynamic limits factors of the
command
//! @param[in]   buffered      Create as a buffered command
//! @param[out] cmdID          The ID of the added command
//! @return                    Was everything okay?
MotionResult kinMoveDirectAsyncCmd(const dia::CmdSourceInfo&
sourceInfo, const char* kinName, cmd::kin::KinCmdType cmdType,
const double *targetPos, cmd::kin::CmdTargetCOS targetCOS,
const cmd::DynamicLimitsT &dynLimFactors, bool buffered,
uint64_t &cmdID ) const;

### 7.3.9 KinMoveDirectAsyncRel - Direct asynchronous relative traversing

of kinematics
Basics
This function commands a kinematic motion to the specified relative position
in the specified coordinate system to which the actuator path is not relevant
to.
The axes move asynchronously.
Prerequisite: The kinematics has to be enabled.

During the motion, the PLCopen state of the kinematics is set to MOVING. It
is ensured that the configured dynamic limits of all axes are complied with.
No path dynamics is taken into consideration, thus, a very fast motion can
take place. All motion phases of the axes are asynchronous. This means that
the axes simultaneously start the interpolation but that the motion is not
synchronous. Each axis reaches the target position as fast as it is possible
with the dynamic limits specified by the given factors.
The target position can be specified in any existing coordinate system. The
motion ends with velocity and with velocity or acceleration equal to zero.
By means of the factors, the dynamic motion limit values can be influenced:
● The following applies to the velocity factor:
   – No factors specified - no reduction takes place
   – 0.0/1.0 – no reduction
   – < 0.001 – not permitted
   – >= 0.001 – the configured maximum axis velocities apply as reduced
     (0.1% ... 100%)
   – > 1 - not permitted
● The following applies to acceleration, deceleration, acceleration jerk and
   deceleration jerk:
   – 0 – the previous factor is used for reduction.
     The following order applies:
     Velocity, acceleration, deceleration, acceleration jerk, deceleration jerk
   – > 0 – the specified factor applies
   – > 1 – not permitted
Examples:
● All factors 0 or 1 → the configured, dynamic axis limit values apply
● Velocity factor = 0.75, other factors = 0.0 → Axes must be moved at a
    maximum of 75 % of the configured dynamic axis limit values. The factor
    applies to all axis limit values
● All factors 0.0, except the acceleration jerk factor = 0.5 → Axes can move
    with the configured dynamic axis limit value. The jerks for acceleration and
    deceleration are reduced by 50 %
● Velocity factor = 0.8, acceleration factor = 1.0, other factors = 0.0 → Axes
    must be moved at a maximum of 80 % of the configured velocity, all other
    limit values apply according to the configuration
If the commanded target position is reached, the command is set to state
DONE and the PLCopen state of the kinematics is set to STANDBY. Use|
ML_KinGetPLCOpenState| or |ML_GetCmdState| to determine the current
state.
The motion can be generated as buffered or unbuffered command. The buf‐
fered commands are stored in a command buffer and executed sequentially.
Unbuffered commands are prepared in a high-priority task. They cancel the
currently active command once it is ready to be executed. The remaining com‐
mand buffer is deleted (all commands are assigned the state ABORTED, when
querying the status with GetCmdState, see ⮫ Chapter 7.8.7 GetCmdState -
Command states on page 787). It is recommended to use buffered commands
when possible. The unbuffered commands have a major impact on the tem‐
poral behavior of the system and can result in considerable delays of other
tasks. Additionally, a sequence of commands can be executed faster if it is
commanded as a sequence of buffered commands.

No axis assigned
If a motion is commanded for a kinematics in which a coordinate index is
moved and no axis is assigned to the index, this coordinate is interpolated
synchronously to the slowest axis. If the no coordinate is part of the com‐
manded motion to which an axis is assigned, the coordinates reach their
target point within one cycle.
Example 1:
● The axes "X" and "Y" are assigned to the kinematics to the indices 0 and 1
● A motion is commanded to (1, 2, 3) → No axis is assigned to the third
   index
● In this example, the "X" axis should require 1.5 s for the motion and the "Y"
   axis should require 1.9 s.

   – The third coordinate is moved synchronously to "Y" and reaches its
      target position from 3 to 1.9 s (identical to axis "Y")
Example 2:
● The axes "X" and "Y" are assigned to the kinematics to the indices 0 and 1
● A relative motion is commanded to (0, 0, 1) → No axis is assigned to the
   third index and no other axis is part of the process.
   – After one cycle, the coordinate reaches its target position of 1
Restriction regarding safe zones and working ranges
The TCP path is not defined in this command. Additionally, asynchronous
input (in particular overrides, see ⮫ Chapter 7.7.3 SetOverride - Override
on page 739 and ⮫ Chapter 7.7.2 GetOverride - Reading out the override
on page 737) directly influence the traveled path. Therefore, a more detailed
check of the protection zones and working areas is not possible. This com‐
mand only checks the straight line between start point and target point. Thus,
range violations are reported even though no violations would occur or viola‐
tions are not detected. It is recommended not to use this command in close
proximity to a safe zone or a working area, see ⮫ Chapter 7.5.9 KinSafeAreaP -
Working areas/safe zones on page 672.
If an error occurred during the execution (e.g. unknown coordinate system
of target position), the command was not added to the kinematics object. If
an error occurred during the execution, the kinematic status is set to ERROR‐
STOP.

PLC:

ML_KinMoveDirectAsyncRel
Name          Data type   Inherited        Address      Initial value   Comment
                          from
  Data        ML_KinMove‐                                               InOut: Command parame‐
              DirectAsyn‐                                               ters
              cRel
  ML_KinMo‐ BOOL                                                        Returns, whether it was
veDirectAsyn‐                                                           possible to add the com‐
cRel                                                                    mand to the kinematic
                                                                        object.
                                                                        ● TRUE: The ML_KinMo‐
                                                                          veDirectAsyncRel com‐
                                                                          mand could be added
                                                                          successfully
                                                                        ● FALSE: An error
                                                                          occurred. Details in
                                                                          ML_oCmdResult
STRUCT ML_KinMoveDirectAsyncData
Name       Data type    Inherited          Address      Initial value   Comment
                        from
  In       ML_iKinMo‐                                                   Input: Command data of
           veDirectA‐                                                   the command
           sync
  Out      ML_oCmdRe‐                                                   Output: Command parame‐
           sult                                                         ters

STRUCT ML_iKinMoveDirectAsync EXTENDS ML_iKinCmdBase
Name        Data type   Inherited   Address     Initial value         Comment
                        from
  KinName STRING(15) ML_iKinCmd‐                                      Name of the kinematics
                        Base                                          used to execute the com‐
                                                                      mand
  Source       STRING(50)     ML_iKinCmd‐                             Specifies the command
                              Base                                    source, e.g PlcApplication1
                                                                      is displayed in the diag‐
                                                                      nostic messages
  SourceLine ULINT            ML_iKinCmd‐                             Specifies the source line of
                              Base                                    the command; is displayed

in the diagnostic messages
  Position     ARRAY[0..15]                                           Commands absolute target
OF LREAL                                               position (absolute or rel‐
ative), depending on the
command type
  CoordSys     STRING(15)                                             Relevant coordinate system
of the commanded target
position (PCS, WCS, MCS
or ACS
  Buffered     BOOL                                   TRUE            TRUE, if the command
is to be executed as buf‐
fered command, otherwise
FALSE
  DynLim‐      ML_iDynLi‐                                             Factors (0 ... 1) for
Factors        mits                                                   dynamic motion limits
(velocity, acceleration,
deceleration, jerkAcc,
jerkDec)
STRUCT ML_iDynLimits
Name        Data type         Inherited     Address   Initial value   Comment
                              from
   Velocity    LREAL                                                  Velocity limit value
   Accelera‐   LREAL                                                  Acceleration limit value
tion
   Decelera‐   LREAL                                                  Deceleration limit value
tion
   JerkAcc     LREAL                                  0               Jerk limit value for acceler‐
                                                                      ation phase
  JerkDec      LREAL                                  0               Jerk limit value for deceler‐
                                                                      ation phase

STRUCT ML_oCmdResult
Name       Data type             Inherited   Address       Initial value   Comment
                                 from
   CmdID           ULINT                                                   Command ID (is set to
                                                                           18446744073709551615 in
                                                                           the event of an error)
   Error           BOOL                                                    Error ID TRUE indicates
                                                                           that an error occurred
   ErrorID         ULINT                                                   Specifies the type of
                                                                           occurred error: The upper
                                                                           4 bytes reflect the main
                                                                           diagnostics, the lower 4
                                                                           bytes reflect the detailed
                                                                           diagnostics, 0 means no
                                                                           error

Data Layer:
Method: POST
URL:               https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/move-direct-async-rel
Payload:

{
"type":"object","value":
{
"kinPos":[10.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
"coordSys":"WCS",
"dynLimFactors": {
                 "vel":1,
                 "acc":1,
                 "dec":1,
                 "jrkAcc":1,
                 "jrkDec":1
              },
"buffered":false
}
}

Python:
<cmdID> = motion.kin_cmd_move_direct_async_rel( kin=<kinName>,
pos=<targetPos> [,coord_sys=<targetCoordinateSystem>]
[,vel_factor=<velocityFactor>]
[,acc_factor=<accelerationFactor>]
[,dec_factor=<decelerationFactor>]
[,jrk_acc_factor=<jerkAccelerationFactor>]
[,jrk_dec_factor=<jerkDecelerationFactor>]
[,buffered=<buffered>])

Creates a MoveDirectAsyncRel command for a kinematics (object has to be
"attached"), see documentation Python Runtime App ⮫ Python functions.
● <kinName> - string, kinematic name
● <pos> - tuple of double or list of double (16 values max.), target position
  of the command

● <targetCoordinateSystem> - Coordinate system in which <pos> is defined
  (coordinate system is "PCS”, if not programmed)
● <velocityFactor> - double, velocity limit factor of the command (set velocity
  limit factor for this kinematics to "1", for "0" or not programmed → no
  limit)
● <accelerationFactor> - double, acceleration limit factor of the command
  (the last programmed acceleration limit factor is used (if this factor is
  unequal to “0”), if this parameter is not programmed or if the value “0” is
  specified)
● <decelerationFactor> - double, deceleration limit factor of the command
  (the last programmed deceleration limit factor is used (if this factor is
  unequal to “0”), if this parameter is not programmed or if the value “0” is
  specified)

● <jerkAccelerationFactor> - double, factor for the jerk limit of the accelera‐
  tion of the command (the last programmed factor is used for the jerk limit
  of the acceleration (if this factor is unequal to “0”), if this parameter is not
  programmed or if the value “0” is specified)
● <jerkDecelerationFactor> - double, factor for jerk limit of the deceleration
  of the command (the last programmed factor for the jerk limit of the decel‐
  eration is used (if this factor is unequal to “0”), if this parameter is not
  programmed or if the value “0” is specified)
● <buffered> - bool, use TRUE if the command is to be buffered (TRUE by
  default)

BundleIF:
For commanding with relative target position, the following command type is
used:

cmd::kin::KinCmdType::KIN_CMD_MOVE_DIRECT_ASYNC_REL
//! @brief Create a motion command for a kinematic
(KIN_CMD_MOVE_DIRECT_ASYNC_*)
//!
//! @param[in]   sourceInfo    Command source information
//! @param[in]   kinName       Name of the motion object
//! @param[in]   cmdType       Type of the command
//! @param[in]   targetPos     Target position of the command
//! @param[in]   targetCOS     Target coordinate system for
the targetPos
//! @param[in]   dynLimFactors Dynamic limits factors of the
command
//! @param[in]   buffered      Create as a buffered command?
//! @param[out] cmdID          The ID of the added command
//! @return                    Was everything okay?
MotionResult kinMoveDirectAsyncCmd(const dia::CmdSourceInfo&
sourceInfo, const char* kinName, cmd::kin::KinCmdType cmdType,
const double *targetPos, cmd::kin::CmdTargetCOS targetCOS,
const cmd::DynamicLimitsT &dynLimFactors, bool buffered,
uint64_t &cmdID ) const;

### 7.3.10 KinMoveJump - Jump motion to the target point

Basics
The command performs a jump motion to the target point, reaching a speci‐
fied maximum height in the z-direction at the latest when half the distance is
reached.

One possible application is picking up parts at their current position and
placing them at the target position (Pick & Place). The entire motion is div‐
ided into five separate motions: Two vertical segments at the start and end,
whose lengths can be set independently of one another, as well as two poly‐
nomial segments that serve as a transition to the specified maximum height
and are connected by a linear segment in the middle. Changes in orientation
occur exclusively within the horizontal segments.
The command is always executed in a buffered manner.

Functional description

(bottom)
This figure shows two possible motion paths with different height parameters
(S, M, E) for a jump from the current position (P1) to the target position (P2).
All three parameters are interpreted in the unit of length configured for the
kinematics. For a jump in the positive z-direction, all height parameters must
be positive. To perform a jump in the negative z-direction, all parameters must
be negative. For this reason, mixing different signs is not permitted. The start
height S and the end height E are always relative to the respective starting
and ending points, respectively, and may also be zero. For a positive jump, the
maximum height M is calculated based on the lower of the two points, while
for a negative jump, the higher point is used as the reference. Unlike the start
and end heights, the maximum height must always be a unequal to zero. In
addition, the maximum height must not be absolutely less than the height of
the points above the start or end point (C1/C2). Therefore, this value must
always be greater than the start/end height.
As with the other commands providing ⮫ advanced programming options, the
target position is specified as a sequence of value pairs and the desired coor‐
dinate system (see KinMoveLinEx), with the exception that commands in the
axis coordinate system (ACS) are not supported. If a command is issued in
a coordinate system other than PCS, it has to be ensured that the Z-axis of
the specified coordinate system matches the Z-axis of the active PCS. In this

case, only rotation around the Z-axis is permitted (e.g., in a PCS set or WCS
transformation). In addition, the target position must not be the same as the
starting position or be shifted only vertically.

Compatibility with other command options
To move without having to stop repeatedly at the segment transitions, first
enable the command option for continuous motion (see KinContMotionP). In
addition, using the contour command (see KinContour) ensures that all indi‐
vidual motions are completely prepared before the first motion is executed;
otherwise, errors may occur at runtime when using ContMotion in connection
with a short initial jump height.
Using the PolyTrans (KinPolyTransP) or Blend (KinBlendP) command options,
it is possible to create a transition to another motion command at the start

or end of a MoveJump. To prevent this, the relevant command option must be
disabled before using MoveJump.
If the command option for belt-synchronous motion (see KinBeltSync) is ena‐
bled at the time of the jump, the vertical motions at the start and end are
synchronized with the respective belt. Any desynchronization and resynchroni‐
zation with a belt occurs only during the horizontal motion.

Jump in case of active safe zones

If one or more active safe zones are crossed along a line between the end
of the first segment (C1) and the start of the last segment (C2), the hori‐
zontal segment is extended far enough to include at least all areas of the
safe zones (see figure above). Otherwise, they could be crossed within the
polynomial segments. If a safe zone does not obstruct horizontal motions
(S2), it is ignored, and the start and end points of the middle segment remain
unchanged. The maximum height must be selected so that the horizontal seg‐
ment does not pass through a safe zone.

PLC:

ML_KinMoveJump
Name       Data type        Inherited     Address       Initial value   Comment
                            from

ML_KinMoveJump
  Data      ML_KinMove‐                                                 InOut: Command parame‐
JumpData                                                    ters
  ML_KinMo‐ BOOL                                                        Returns, whether it was
veJump                                                                  possible to add the com‐
mand to the kinematic
object.
● TRUE: The ML_KinMove‐
  Jump command was
  successfully added
● FALSE: An error
  occurred. Details in
  ML_oCmdResult
STRUCT ML_KinMoveJumpData
Name       Data type  Inherited               Address   Initial value   Comment
                      from
  In       ML_iKinMo‐                                                   Input: Command data of
           veJump                                                       the command
  Out      ML_oCmdRe‐                                                   Output: Command parame‐
           sult                                                         ters
STRUCT ML_iKinMoveJump EXTENDS ML_iKinCmdBase
Name        Data type  Inherited  Address     Initial value             Comment
                       from
  KinName STRING(15) ML_iKinCmd‐                                        Name of the kinematics
                       Base                                             used to execute the com‐
                                                                        mand
   Source          STRING(50)   ML_iKinCmd‐                             Specifies the command
                                Base                                    source, e.g PlcApplication1
                                                                        is displayed in the diag‐
                                                                        nostic messages
   SourceLine ULINT             ML_iKinCmd‐                             Specifies the source line of
                                Base                                    the command; is displayed
                                                                        in the diagnostic messages
  CmdKin‐          ML_KinMo‐                                            Commanded absolute
Pose               tionCmd‐                                             target position with mean‐
                   Target                                               ings
   CoordSys        STRING(15)                                           Coordinate system refer‐
                                                                        enced for the commanded
                                                                        target position (PCS, WCS,
                                                                        or MCS)
  Star‐            LREAL                                0               Length of the first ver‐
tHeight                                                                 tical motion relative to the
                                                                        starting point
   MaxHeight LREAL                                      0               Maximum jump height
   EndHeight LREAL                                      0               Length of the last ver‐
                                                                        tical motion relative to the
                                                                        target point
   DynLimits ML_iDynLi‐                                                 Dynamic limit values
             mits                                                       during the motion com‐
                                                                        mand

STRUCT ML_KinMotionCmdTarget
Name       Data type   Inherited               Address   Initial value   Comment
                       from
  CmdKin‐  ARRAY                                                         Commanded target posi‐
Target     [0..24] OF                                                    tion with meanings
           ML_KinCmd‐
           PosePair
  CmdKin‐  UINT                                                          Number of entries in
TargetSize                                                               CmdKinTarget
STRUCT ML_KinCmdPosePair
Name       Data type   Inherited               Address   Initial value   Comment
                       from

  Value    LREAL                                                         A value of the cmdKinPose
  Meaning  ML_Meaning                                                    Associated meaning of the
                                                     value
Attribute     ML_Attrib‐                           UNDEF           Additional attribute of the
utes                                                 meaning
ENUM ML_Meaning
Name      Data type                Inherited   Address   Initial value   Comment
                                   from
      UNDEF         INT                                  0               Error or undefined
      X             INT                                                  Absolute position of the x-
                                                                         axis
      Y             INT                                                  Absolute position of the y-
                                                                         axis
      Z             INT                                                  Absolute position of the z-
                                                                         axis
      AX1           INT                                                  Absolute position of axis 1
      AX2           INT                                                  Absolute position of axis 2
      AX3           INT                                                  Absolute position of axis 3
...
ENUM ML_MeaningAttribute
Name      Data type      Inherited             Address   Initial value   Comment
                         from
  UNDEF   INT                                            0               Error, undefined or not
                                                                         used
                    INT                                                  IC(): Incremental value
 INCR_VALUE
                    INT                                                  AC(): Absolute value
 ABS_VALUE
                    INT                                                  DC(): Shortest route
 SHORT_WAY
                    INT                                                  ACP(): Positive direction of
POS_ROT_DI                                                               rotation
R
                    INT                                                  ACN(): Negative direction
NEG_ROT_DI                                                               of rotation
R

STRUCT ML_iDynLimits
Name        Data type      Inherited   Address   Initial value   Comment
                           from
   Velocity        LREAL                                         Velocity limit value
   Accelera‐       LREAL                                         Acceleration limit value
tion
   Decelera‐       LREAL                                         Deceleration limit value
tion
   JerkAcc         LREAL                         0               Jerk limit value for acceler‐
                                                                 ation phase
   JerkDec         LREAL                         0               Jerk limit value for deceler‐
                                                                 ation phase
STRUCT ML_oCmdResult
Name       Data type       Inherited   Address   Initial value   Comment
                           from
   CmdID           ULINT                                         Command ID (is set to
                                                                 18446744073709551615 in
                                                                 the event of an error)
   Error           BOOL                                          Error ID TRUE indicates
                                                                 that an error occurred
   ErrorID         ULINT                                         Specifies the type of
                                                                 occurred error: The upper
                                                                 4 bytes reflect the main
                                                                 diagnostics, the lower 4
                                                                 bytes reflect the detailed
                                                                 diagnostics, 0 means no
                                                                 error

Data Layer:
Method: POST
URL:               https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/move-jump
Payload:
{"type":"object", "value": {
    "cmdKinPose": [
      {"value":500, "extMeaning": {"meaning":"X",
      "addAttributes":"INCR_VALUE"}},
      {"value":0, "extMeaning": {"meaning":"Y",
      "addAttributes":"ABS_VALUE"}},
      {"value":10, "extMeaning": {"meaning":"Z",

      "addAttributes":"ABS_VALUE"}}
   ],
    "startHeight":150,
    "maxHeight":200,
    "endHeight":50,
    "coordSys":"MCS",
    "lim": {
      "vel":6000,
      "acc":2,
      "dec":2,
      "jrkAcc":0,
      "jrkDec":0
    }
}}

Python
<cmdID> = motion.kin_cmd_move_jump(kin=<kinName>,
kin_pose_pair=<targetPose>
[, start_height=<startHeight>][, max_height=<maxHeight>][,
end_height=<endHeight>]
[, coord_sys=<targetCoordSys>][, vel=<velocity>][,
acc=<acceleration>]
[, dec=<deceleration>][, jrk_acc=<jerkAcceleration>][,
jrk_dec=<jerkDeceleration>]

Example:
motion.kin_cmd_move_jump("Robot", {"X":40.0, "Y":-100.0,
"Z":42.0}, 10.0, 17.0, 5.0, "MCS", vel=800.0, acc=2.0, dec=2.0)
Generates a MoveJump command for a kinematic (the object has to be
"attached"); see the documentation for Python Runtime App ⮫ Python
functions.
● <kinName> - string, kinematic name
● <targetPose> - Specify a target position of the command by pairing
  a meaning and a corresponding value for the coordinates to be
  offset. The pairs are collected in a dictionary data type { <meaning
  string>:<position>, ... ,<meaning string>:<position>}. <position> can be
  an <float>, <long> or a <sub-dictionary> with {<attribute string>:<float|
  long>}. Example: kin_pose_pair={ "X":3.0, "Y":2, "Z":{"INCR_VALUE":-10},
  "AX5":{"POS_ROT_DIR":20}}
● <startHeight> - double, length of the start segment (S in the image above)
● <maxHeight> - double, maximum height (M in the image above)
● <endHeight> - double, length of the end segment (E in the image above)

● <targetCoordSys> - string ("PCS", "WCS", "MCS"), coordinate system in
  which <targetPose> is defined (the coordinate system is "PCS" if not speci‐
  fied)
● <velocity> - double, velocity limit value of the command (the last pro‐
  grammed velocity limit value is used if this parameter is not programmed)
● <acceleration> - double, acceleration limit value of the command (the last
  programmed acceleration limit value is used if this parameter is not pro‐
  grammed)
● <deceleration> - double, deceleration limit value of the command (the last
  programmed deceleration limit value is used if this parameter is not pro‐
  grammed)
● <jerkAcceleration> - double, jerk limit value for the acceleration of the com‐
  mand (the last programmed jerk limit value for the acceleration is used if
  this parameter is not programmed)
● <jerkDeceleration> - double, jerk limit value for the deceleration of the
  command (the last programmed jerk limit value for the deceleration is used
  if this parameter is not programmed)

BundleIF:
/// @brief Create a motion command for a kinematics in which
    the target position is reached by moving on an arch
///
/// @param[in]    sourceInfo    Command source information
/// @param[in]    kinName       Name of the motion object
/// @param[in]    targetKinPosePair   Target position of the
    command with meanings
/// @param[in]    sizeKinPose   Size of the targetKinPosePair
    array
/// @param[in]    parameters    MoveJump parameters
    (startHeight, maxHeight, endHeight)
/// @param[in]    targetCOS     Target coordinate system for
    the targetPos
/// @param[in]    dynLim        Dynamic limits
/// @param[out] cmdID           The ID of the added command
/// @return                     Status of the function call:
    STS_OK or an error code on failure.
MotionResult kinMoveJumpCmd(const dia::CmdSourceInfo&
sourceInfo, const char* kinName,
cmd::CmdKinPosePair* targetKinPosePair, uint32_t sizeKinPose,
const cmd::MoveJumpParameters& parameters,
cmd::kin::CmdTargetCOS targetCOS,
const cmd::DynamicLimitsT& dynLim, uint64_t& cmdID);

### 7.3.11 KinMoveHalfJump - Half-jump motion to the target point

Basics
The command performs a half-jump toward the target point. Depending on the
selection of the start and end points and the variant parameter, an upward or
downward motion is possible.
One possible application is picking up parts at their current position and
placing them at the target position (Pick & Place). The entire motion is div‐
ided into five separate motions: Two vertical segments at the start and end,
whose lengths can be set independently of one another, as well as two poly‐
nomial segments that serve as a transition to the specified maximum height
and are connected by a linear segment in the middle. Changes in orientation
occur exclusively within the horizontal segments.

The command is always executed in a buffered manner.

Functional description

                                   P2       P1
                    C                                         C

                H                                                 H

                    P1                                      P2
            Z
                    P1                                      P2

                H                                                 H

                    C                                        C

                                   P2       P1

Fig. 318 shows the four possible motion paths with the various variant param‐
eters (UP and DOWN) and the height parameter (H) for a half jump from
the current position (P1) to the target position (P2). The height parameter is
interpreted in the unit of length configured for the kinematics. A half jump in
an upward motion (UP) (see the left side of Fig. 318) can occur in either a
positive or negative direction. In this context, the height parameter refers to
the starting point. A positive, vertical segment is executed at the beginning if
the z-coordinate of P2 is greater than that of P1 and the height parameter is
set to a positive value. A half jump downward motion (DOWN) (see the right
side of Fig. 318) can also occur in both the positive and negative direction.
Here, the height parameter refers to the target point. A positive, vertical seg‐
ment is executed at the end if the z-coordinate of P1 is greater than that of P2
and the height parameter is set to a positive value.
The height parameter can also be zero. The maximum height of the start and
end point must be greater than the absolute value of the height parameter.
The length of the polynomial segment in the vertical direction is mirrored
symmetrically across the horizontal length, if the horizontal length allows it.
Otherwise, the polynomial segment is shortened to the available horizontal
length.
As with the other commands providing ⮫ advanced programming options, the
target position is specified as a sequence of value pairs and the desired
coordinate system (see ⮫ Chapter 7.4.2 KinMoveLinEx - Moving on a straight
line in space on page 605), with the exception that commands in the axis
coordinate system (ACS) are not supported. If a command is issued in a
coordinate system other than PCS, it has to be ensured that the Z-axis of
the specified coordinate system matches the Z-axis of the active PCS. In this
case, only rotation around the Z-axis is permitted (e.g., in a PCS set or WCS
transformation). In addition, the target position must not be the same as the
starting position.

Compatibility with other command options
To move the object without stopping repeatedly at the segment junctions,
you must first enable the command option for continuous motion (see
⮫ Chapter 7.5.7 KinContMotionP - Continuous motion across several com‐
mands on page 664 ). In addition, using the "Contour" command (see

⮫ Chapter 7.3.19 KinContour - Specifying the contour area on page 594)
ensures that all individual motions are completely prepared before the first
motion is executed; otherwise, errors may occur at runtime when using Con‐
tMotion in conjunction with a short initial jump height.
It is possible to use the PolyTrans (⮫ Chapter 7.5.8 KinPolyTransP - Com‐
mand options for kinematics - Path rounding with polynomial on page 667)
or blendng (⮫ Chapter 7.5.2 KinBlend, KinBlendP - Blending/permanent kin‐
ematic option on page 640) command options to generate a transition to
another motion command at the start or end of the MoveHalfJump. To prevent
this, the relevant command option must be disabled before the MoveHalf‐
Jump.
If the command option for belt-synchronous motion (see ⮫ Chapter 7.5.14 Kin‐
BeltSyncP - Belt-synchronous on page 692) is enabled at the time of the jump,
the vertical motions at the start and end are synchronized with the respec‐
tive belt. Any desynchronization and resynchronization with a belt occurs only
during the horizontal motion.

Jump in case of active safe zones

                                                          P2

                 C1                                      C2
                            S1

                                                 S2

                  P1

If one or more active safe zones are crossed along a line between the end of
the vertical segment (C1) and the virtual point C2, the horizontal segment is
extended far enough to enclose at least all areas of the safe zones (see Figure
2). Otherwise, they could be crossed within the polynomial segments. Point
C2 is calculated using the x and y coordinates of the end point (start point
for MoveHalfJump DOWN) (P2) and the z-coordinate of point C1, which is cal‐
culated by adding the height to the start point (end point for MoveHalfJump
DOWN). If a safe zone does not obstruct the horizontal motion (S2), it is
ignored, and the start point (end point for MoveHalfJump DOWN) of the hori‐
zontal segment remains unchanged. The height of the end point (start point
for MoveHalfJump DOWN) has to be set high enough so that the horizontal
segment does not pass through a safe zone.

PLC:

ML_KinMoveHalfJump
Name       Data type        Inherited     Address   Initial value   Comment
                            from
  Data      ML_KinMove‐                                             InOut: Command parame‐
            HalfJump‐                                               ters
            Data
  ML_KinMo‐ BOOL                                                    Returns, whether it was
veHalfJump                                                          possible to add the com‐
                                                                    mand to the kinematic
                                                                    object.
                                                                    ● TRUE: The ML_KinMove‐
                                                                      HalfJump command was

                                          successfully added
                                        ● FALSE: An error
                                          occurred. Details in
                                          ML_oCmdResult
STRUCT ML_KinMoveHalfJumpData
Name       Data type   Inherited          Address   Initial value   Comment
                       from
  In       ML_iKinMo‐                                               Input: Command data of
           veHalfJump                                               the command
  Out      ML_oCmdRe‐                                               Output: Command parame‐
           sult                                                     ters
STRUCT ML_iKinMoveHalfJump EXTENDS ML_iKinCmdBase
Name        Data type   Inherited  Address    Initial value         Comment
                        from
  KinName STRING(15) ML_iKinCmd‐                               Name of the kinematics
                        Base                                   used to execute the com‐
                                                               mand
  Source     STRING(50)     ML_iKinCmd‐                        Specifies the command
                            Base                               source, e.g PlcApplication1
                                                               is displayed in the diag‐
                                                               nostic messages
  SourceLine ULINT          ML_iKinCmd‐                        Specifies the source line of
                            Base                               the command; is displayed
                                                               in the diagnostic messages
  CmdKin‐    ML_KinMo‐                                         Commanded absolute
Pose         tionCmd‐                                          target position with mean‐
             Target                                            ings
  CoordSys   STRING(15)                                        Coordinate system refer‐
                                                               enced for the commanded
                                                               target position (PCS, WCS,
                                                               or MCS)
  Height    LREAL                                   0          Height of the HalfJump
  Variant   ML_Move‐                                HALF_JUMP_ A variation of the Half‐
            HalfJumpVar‐                            UP         Jump. First, the vertical
            iant                                               motion, or second
  DynLimits ML_iDynLi‐                                         Dynamic limit values
            mits                                               during the motion com‐
                                                               mand

STRUCT ML_KinMotionCmdTarget
Name       Data type   Inherited            Address   Initial value   Comment
                       from
  CmdKin‐  ARRAY                                                      Commanded target posi‐
Target     [0..24] OF                                                 tion with meanings
           ML_KinCmd‐
           PosePair
  CmdKin‐  UINT                                                       Number of entries in
TargetSize                                                            CmdKinTarget
STRUCT ML_KinCmdPosePair
Name       Data type   Inherited            Address   Initial value   Comment
                       from
  Value    LREAL                                                      A value of the cmdKinPose
  Meaning  ML_Meaning                                                 Associated meaning of the
                                                                      value
      Attribute    ML_Attrib‐                         UNDEF           Additional attribute of the
                   utes                                               meaning
ENUM ML_MoveHalfJumpVariant
Name       Data type  Inherited             Address   Initial value   Comment
                      from
           INT                                        0               HalfJump with vertical
 HALF_JUMP                                                            motion first, followed by
_UP                                                                   horizontal motion
           INT                                                        HalfJump with horizontal
 HALF_JUMP                                                            motion first, followed by
_DOWN                                                                 vertical motion
ENUM ML_Meaning
Name      Data type             Inherited   Address   Initial value   Comment
                                from
      UNDEF        INT                                0               Error or undefined
      X            INT                                                Absolute position of the x-
                                                                      axis
      Y            INT                                                Absolute position of the y-
                                                                      axis
      Z            INT                                                Absolute position of the z-
                                                                      axis
      AX1          INT                                                Absolute position of axis 1
      AX2          INT                                                Absolute position of axis 2
      AX3          INT                                                Absolute position of axis 3
...
ENUM ML_MeaningAttribute
Name      Data type      Inherited          Address   Initial value   Comment
                         from
  UNDEF   INT                                         0               Error, undefined or not
                                                                      used
                   INT                                                IC(): Incremental value
 INCR_VALUE
                   INT                                                AC(): Absolute value
 ABS_VALUE

ENUM ML_MeaningAttribute
INT                                                    DC(): Shortest route
 SHORT_WAY
INT                                                    ACP(): Positive direction of
 POS_ROT_DI                                                        rotation
R
INT                                                    ACN(): Negative direction
 NEG_ROT_DI                                                        of rotation
R
STRUCT ML_iDynLimits
Name        Data type        Inherited   Address   Initial value   Comment
                             from

   Velocity    LREAL                                               Velocity limit value
   Accelera‐   LREAL                                               Acceleration limit value
tion
   Decelera‐   LREAL                                               Deceleration limit value
tion
   JerkAcc     LREAL                               0               Jerk limit value for acceler‐
ation phase
  JerkDec      LREAL                               0               Jerk limit value for deceler‐
ation phase
STRUCT ML_oCmdResult
Name       Data type         Inherited   Address   Initial value   Comment
                             from
  CmdID        ULINT                                               Command ID (is set to
                                                                   18446744073709551615 in
                                                                   the event of an error)
  Error        BOOL                                                Error ID TRUE indicates
                                                                   that an error occurred
  ErrorID      ULINT                                               Specifies the type of
                                                                   occurred error: The upper
                                                                   4 bytes reflect the main
                                                                   diagnostics, the lower 4
                                                                   bytes reflect the detailed
                                                                   diagnostics, 0 means no
                                                                   error

Data Layer:
Method: POST
URL:               https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/move-half-jump
Payload:
{"type":"object", "value": {
    "cmdKinPose": [
        {"value":40, "extMeaning":
{"meaning":"X","addAttributes":"INCR_VALUE"}},
        {"value":10, "extMeaning":
{"meaning":"Y","addAttributes":"ABS_VALUE"}},
        {"value":30, "extMeaning":
{"meaning":"Z","addAttributes":"ABS_VALUE"}}
    ],
    "height":20,
    "variant":"HALF_JUMP_UP",
    "coordSys":"MCS",
    "lim": {
        "vel":6000,
        "acc":2,
        "dec":2,
        "jrkAcc":0,
        "jrkDec":0
    }
}}

Python
<cmdID> = motion.kin_cmd_move_half_jump(kin=<kinName>,
kin_pose_pair=<targetPose>
[, height=<height>][, variant=<variant>][,
coord_sys=<coord_sys>][, vel=<vel>][, acc=<acc>]
[, dec=<dec>][, jrk_acc=<jrkAcc>][, jrk_dec=<jrkDec>]

Example:
motion.kin_cmd_move_half_jump("Robot", {"X":40.0, "Y":-100.0,
"Z":42.0}, 10.0, True, "MCS", vel=800.0, acc=2.0, dec=2.0)
Creates a MoveHalfJump command for a kinematic (the object has to
be "attached"); see the documentation for Python Runtime App ⮫ Python
Functions.
● <kinName> - string, kinematic name
● <targetPose> - Specify a target position of the command by pairing
  a meaning and a corresponding value for the coordinates to be
  offset. The pairs are collected in a dictionary data type { <meaning
  string>:<position>, ... ,<meaning string>:<position>}. <position> can be
  an <float>, <long> or a <sub-dictionary> with {<attribute string>:<float|
  long>}. Example: kin_pose_pair={ "X":3.0, "Y":2, "Z":{"INCR_VALUE":-10},
  "AX5":{"POS_ROT_DIR":20}}
● <height> - double, vertical height of the start/end segment
● <variant> —bool; set the value to "True" to perform the horizontal motion
  first and then the vertical motion, and to "False" to perform the vertical
  motion first and then the horizontal motion.

● <coordSys> - string ("PCS", "WCS", "MCS"), coordinate system in which
  <targetPose> is defined (the coordinate system is "PCS" if not otherwise
  specified)
● <vel> - double, velocity limit value for the command (if this parameter is
  not set, the last programmed velocity limit value is used)
● <acc> - double, acceleration limit value of the command (if this parameter
  is not set, the last programmed acceleration limit value is used)
● <dec> —double, deceleration limit value of the command (if this parameter
  is not set, the last programmed deceleration limit value is used)
● <jrkAcc> - double, jerk limit value for the command's acceleration (if this
  parameter is not set, the last programmed jerk limit value for acceleration
  is used)
● <jrkDec> - double, jerk limit value for the target deceleration (if this param‐

  eter is not set, the most recently programmed jerk limit value for the decel‐
  eration is used)

BundleIF:
/// @brief Create a motion command for a kinematics in which
the target position is reached by moving on a half arch
///
/// @param[in]   sourceInfo       Command source information
/// @param[in]   kinName          Name of the motion object
/// @param[in]   targetKinPosePair Target position of the
                                  command with meanings
/// @param[in]   sizeKinPose      Size of the targetKinPosePair
                                  array
/// @param[in]   height           Height of the MoveHalfJump
/// @param[in]   variant          Variant of the MoveHalfJump
                                  (HALF_JUMP_UP or
                                  HALF_JUMP_DOWN)
/// @param[in]   targetCOS        Target coordinate system for
                                  the targetPos
/// @param[in]   dynLim           Dynamic limits
/// @param[out] cmdID             The ID of the added command
/// @return                       Status of the function call:
                                  STS_OK or an error code on
                                  failure.
MotionResult kinMoveHalfJumpCmd(const dia::CmdSourceInfo&
sourceInfo, const char* kinName, cmd::CmdKinPosePair*
targetKinPosePair, uint32_t sizeKinPose,
const double height, cmd::MoveHalfJumpVariant variant,
cmd::kin::CmdTargetCOS targetCOS, const cmd::DynamicLimitsT&
dynLim, uint64_t& cmdID);

### 7.3.12 KinCyclicSetPointPCS - Cyclic command value input

Basics
The KinCyclicSetPointPCSCmd command configures the kinematics so that
PCS positions and orientations are calculated cyclically using a backward
transformation and passed on to the axes as command values. The motion
is defined exclusively by this cyclic channel, which is populated with values by
the "setKinCyclicSetPointPCS" function.
The command values have to be reset cyclically at each execution cycle. Fur‐
thermore, the command values must comply with the axis limits. Kinematic
limits are not checked. However, axis limit values are monitored.

When one of the "Abort," "velocity Override = 0," or "Interrupt" motion com‐
mands is detected, the motion is brought to a stop at velocity 0—if neces‐
sary—using an internally determined deceleration ramp, and the command
is terminated. The deceleration ramp for this time is calculated using the
"time_sync_out" parameter of the KinCyclicSetPointPCSCmd command. The
time has to be set to a value that ensures the axis limits are not exceeded.
If "time_sync_out=0.0," the configured kinematic path limits are used to calcu‐
late the deceleration ramp.
The KinCyclicSetPointPCSCmd command can also be executed in non-buf‐
fered mode. This command, like any other motion command, can be termi‐
nated by a non-buffered command. If the command is aborted, a deceleration
ramp is automatically generated.
The command's execution is not real-time capable. It takes a few cycles to
prepare.

Restrictions
● The command does not work with the KinBlendP command option
  (⮫ Chapter 7.5.2 KinBlend, KinBlendP - Blending/permanent kinematic
  option on page 640).
● Synchronization with a subsequent command is only possible for unbuf‐
  fered commands.
● If the subsequent command is sent from the buffer, the velocity is ramped
  down to 0 before the new command takes effect.
● The command terminates when one of the following events occurs:
  – kinOverride = 0
  – kinAbort command
  – kinInterrupt command

Use case
An important use case for a cyclic channel is specifying cyclic Cartesian X/Y/Z
positions for a robot, in which case the kinematics should only perform the
inverse transformation to calculate the target positions of the axes.

PLC:

ML_KinCyclicSetPointPCS
Name         Data type          Inherited     Address       Initial value   Comment
                                from
   Data            ML_KinCy‐                                                InOut: Command parame‐
                   clicSet‐                                                 ters
                   PointPCS

ML_KinCyclicSetPointPCS
   ML_KinCy‐ BOOL                                                   Returns, whether it was
clicSet‐                                                            possible to add the com‐
PointPCS                                                            mand to the kinematic
object.
● TRUE: The ML_KinCyclic‐
  SetPointPCS command
  was successfully added
● FALSE: An error
  occurred. Details in
  ML_oCmdResult
STRUCT ML_KinCyclicSetPointPCS

Name       Data type     Inherited        Address   Initial value   Comment
                         from
  In       ML_iKinCy‐                                               Input: Command data of
           clicSet‐                                                 the command
           PointPCS
  Out      ML_oCmdRe‐                                               Output: Command parame‐
           sult                                                     ters
STRUCT ML_iKinCyclicSetPointPCS EXTENDS ML_iKinCmdBase
Name        Data type    Inherited   Address     Initial value      Comment
                         from
  KinName STRING(15) ML_iKinCmd‐                                    Name of the kinematics
                         Base                                       used to execute the com‐
                                                                    mand
  Source     STRING(50)     ML_iKinCmd‐                             Specifies the command
                            Base                                    source, e.g PlcApplication1
                                                                    is displayed in the diag‐
                                                                    nostic messages
  SourceLine ULINT          ML_iKinCmd‐                             Specifies the source line of
                            Base                                    the command; is displayed
                                                                    in the diagnostic messages
  Time‐      LREAL                                  0               Time interval until the start
SyncIn                                                              of the CyclicSetPointPCS
                                                                    trajectory. timeSyncIn is
                                                                    interpreted in the config‐
                                                                    ured unit.
  Time‐      LREAL                                  0               Optional time interval at
SyncOut                                                             the end of the CyclicSet‐
                                                                    PointPCS trajectory. time‐
                                                                    SyncOut is interpreted in
                                                                    the configured unit.
  Buffered   BOOL                                   TRUE            TRUE, if the command
                                                                    is to be executed as buf‐
                                                                    fered command, otherwise
                                                                    FALSE
STRUCT ML_oCmdResult
Name       Data type        Inherited     Address   Initial value   Comment
                            from
  CmdID      ULINT                                                  Command ID (is set to
                                                                    18446744073709551615 in
                                                                    the event of an error)

STRUCT ML_oCmdResult
  Error    BOOL                                                            Error ID TRUE indicates
                                                  that an error occurred
   ErrorID         ULINT                                                   Specifies the type of
                                                  occurred error: The upper
                                                  4 bytes refer to the main
                                                  diagnostics, the lower 4
                                                  bytes refer to the detailed
                                                  diagnostics, 0 means no
                                                  error

ML_KinSetCyclicSetPointPCS
Name         Data type   Inherited            Address      Initial value   Comment
                         from
   Data      ML_SetKin‐                                                    InOut: Command parame‐
             CyclicSet‐                                                    ters
             PointPCS
   ML_KinCy‐ BOOL                                                          Returns, whether it was
clicSet‐                                                                   possible to add the com‐
PointPCS                                                                   mand to the kinematic
                                                                           object.
                                                                           ● TRUE: The ML_KinSet‐
                                                                             CyclicSetPointPCS com‐
                                                                             mand was successfully
                                                                             added
                                                                           ● FALSE: An error
                                                                             occurred. Details in
                                                                             ML_oCmdResult
STRUCT ML_KinSetCyclicSetPointPCS
Name       Data type     Inherited            Address      Initial value   Comment
                         from
  In       ML_iSetKin‐                                                     Input: Command data of
           CyclicSet‐                                                      the command
           PointPCS
  Out      ML_oCmdRe‐                                                      Output: Command parame‐
           sult                                                            ters
STRUCT ML_iKinSetCyclicSetPointPCS EXTENDS ML_iKinCmdBase
Name        Data type    Inherited   Address     Initial value             Comment
                         from
  KinName STRING(15) ML_iKinCmd‐                                           Name of the kinematics
                         Base                                              used to execute the com‐
                                                                           mand
   Source          STRING(50)   ML_iKinCmd‐                                Specifies the command
                                Base                                       source, e.g PlcApplication1
                                                                           is displayed in the diag‐
                                                                           nostic messages

STRUCT ML_iKinSetCyclicSetPointPCS EXTENDS ML_iKinCmdBase
  SourceLine ULINT       ML_iKinCmd‐                                    Specifies the source line of
     Base                                           the command; is displayed
                                                    in the diagnostic messages
  setPoint   ARRAY                                                      New target value; see
[0..15] OF                                                 ML_SetCyclicSetPointPCS
LREAL
STRUCT ML_oCmdResult
Name       Data type          Inherited   Address       Initial value   Comment
                              from
  CmdID      ULINT                                                      Command ID (is set to
                                                                        18446744073709551615 in

                                                    the event of an error)
  Error      BOOL                                                       Error ID TRUE indicates
                                                    that an error occurred
  ErrorID    ULINT                                                      Specifies the type of
                                                    occurred error: The upper
                                                    4 bytes refer to the main
                                                    diagnostics, the lower 4
                                                    bytes refer to the detailed
                                                    diagnostics, 0 means no
                                                    error

Data Layer:
Method: POST
URL:                https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/cyclic-set-point-pcs
Payload:

{
"type":"object","value":
{
"timeSyncIn":10.0,
"timeSyncOut":10.0,
"buffered":false
}
}

Python:
<cmdID> = motion.kin_cmd_cyclic_set_point_pcs(kin:
str,time_sync_in: Optional[float] = 0.0, time_sync_out:
Optional[float] = 0.0, buffered: Optional[bool] = True)

Generates a CyclicSetPointPCS command for a kinematics configuration (the
object has to be "attached"); see the documentation for Python Runtime App
⮫ Python Functions.
● <kin> - string, kinematic name
● <time_sync_in> - Time interval upon start of the CyclicSetPointPCS trajec‐
  tory; interpreted in the configured units.

● <time_sync_out> - Time interval upon end of the CyclicSetPointPCS trajec‐
  tory; interpreted in the configured units. This time indicates the duration of
  the deceleration process. If the interval is set to 0, the deceleration ramp is
  automatically calculated within the specified limits.
● <buffered> - boolean, is this command supposed to be a buffered com‐
  mand?

BundleIF:

cmd::kin::KinCmdType::KIN_CMD_CYCLIC_SET_POINT_PCS
/// @brief Create a motion command for a kinematics for cyclic
set point commanding PCS (Cyclic setpoint)
///
/// Use setKinCyclicSetPointPCS to give the motion kernel the
new setpoint in every cycle.
///
/// @param[in]     handle       Handle of the interface
/// @param[in]     sourceInfo   Command source information
/// @param[in]     kinName      Name of the kinematics
/// @param[in]     timeSyncIn   Time interval at the beginning
of the CyclicSetPointPCS trajectory. timeSyncIn is interpreted
as in configured units.
///                             Synchronisation with the
CyclicSetPointPCS trajectory or if blending is activated,
blending with the predecessor command.
/// @param[in]     timeSyncOut Optional time interval at
the end of the CyclicSetPointPCS trajectory. timeSyncOut is
interpreted as in configured units.
///                             If an end of the command is
detected, this time specifies the length of the braking process
///                             If this time interval is
specified as 0, it is calculated internally using the
kinematic dynamic limits
///                             If blending is activated, this
time is used for the blending to the following command.
/// @param[in]     buffered     Is buffered mode?
/// @param[out]    cmdID        The ID of the added command
/// @return                     Status of the function call:
STS_OK or an error code on failure.
MotionResult KinCyclicSetPointPCSCmd(void* handle, const
dia::CmdSourceInfo& sourceInfo, const char* kinName, double
timeSyncIn, double timeSyncOut, bool buffered, uint64_t&
cmdID);

cmd::kin::KinCmdType::KIN_CMD_SET_CYCLIC_SET_POINT_PCS
/// @brief This method sets the external set point of the
kinematics.
///
/// To let the given set points affect the kinematics,
kinCyclicSetPointPCSCmd must be active in the kinematics. Its
assumed,
/// that you call this function cyclic to provide new set
points for the kinematics.
///
/// There is no explicit check, if the given setpoint and
orientation can be achieved by the kinematics. When you

provide a
/// position outside the reachable space (e.g. due to length
of arms) the motion kernel will create an error in the
kinematics.
/// When you move to a position, that is outside the axis
limits, you will also get an error in the kinematics.
/// When you have a kinematics with limited capabilities (e.g.
no orientation supported or only motion in X and Y allowed),
/// all the "unused" values are simply ignored - you won't get
an error.
///
/// Don't command setpoints near singularities. There is no
automatic singularity handling available.

///
/// The position and orientation is always in PCS, when you
have a PCS active. Its interpreted in MCS, when you don't have
a PCS active.
///
/// The coordinates X, Y, Z, the Euler angles and additional
axes are interpreted as in configured units.
///
/// The function is optimized for speed and can be used in
a real-time context (lock- and wait-free), when the motion
kernel is in state RUNNING.
/// If the motion kernel is not in state RUNNING, the function
call is not real-time capable.
///
/// @param[in]    handle            Handle of the interface
/// @param[in]    kinName           Name of the kinematics
/// @param[in]    setPoint          External setpoint
coordinates; must be an array of 16 double values (X, Y, Z,
EUL1_XYZ_E, EUL2_XYZ_E, EUL3_XYZ_E, ..additional axis values)
/// @return                         Status of the function
call: STS_OK or an error code on failure.
MotionResult setKinCyclicSetPointPCS(void* handle, const char*
kinName, const double* setPoint);

### 7.3.13 KinJogCont - Continuous kinematic jogging

Basics
There are two commands for jogging a kinematics: KinJogIncr and KinJog‐
Cont. This command continuously jogs a kinematics. The command can be
aborted with the KinAbort command.
Both commands move the kinematics along a certain vector. The length for
possible motions is always limited by the configured permissible axis ranges
of the kinematic axes. If the current position is outside the configured, per‐
missible kinematic axis range, the axes can move towards the permitted range
but cannot move away from the range.
The kinematics is in state "MOVING” during the motion. After reaching the end
position, the command is set to DONE and the kinematics goes to STANDBY
mode.
Jogging of the kinematics is only allowed if the kinematic is in state STANDBY,
the velocity is zero and no other command is active.
The programming limit values for velocity, acceleration, deceleration as well
as both jerk limits have to be positive (greater than zero), as otherwise the
parameters would be inconsistent.

Exception: If both jerk limit values are exactly zero, the motion is executed
without jerk limit (trapezoid velocity profile).
                     If the motion passes through a singularity or close to
        WARNING      a singularity, unexpectedly large accelerations and high
                     axis velocities may occur. For further information, refer
                     to ⮫ Dealing with singularities on page 194
The command supports the following coordinate systems:
● WCS (World Coordinate System)
● MCS (Machine Coordinate System)
● PCS (Product Coordinate System)
● TCS (Tool Coordinate System)
  The TCS coordinate system only serves as an input aid, i.e. the commanded
  lengths and directions are transformed from the TCS into the PCS and then
  interpolated in the latter. This also means that the jog direction always
  refers to the initial TCS orientation of the command. When position and
  orientation are tapped at the same time, a straight line is traversed in
  space on which the orientation changes, i.e. no arc. Also refer to ⮫ Chapter
  6.3.1 Position and orientation in space on page 176
● ACS (Axis Coordinate System)
  The ACS coordinate system allows you to jog a single kinematic axis
  without having to ungroup or regroup the kinematics. If multiple kinematic
  axes are moved incrementally, a vector is calculated whose length corre‐
  sponds to the increment.

PLC:

ML_KinJogCont
Name        Data type            Inherited    Address       Initial value   Comment
                                 from
   Data            ML_KinJog‐                                               InOut: Command parame‐
                   ContData                                                 ters
  ML_Kin‐          BOOL                                                     Returns, whether it was
JogCont                                                                     possible to add the com‐
                                                                            mand to the kinematic
                                                                            object.
                                                                            ● TRUE: The command
                                                                              could be added success‐
                                                                              fully
                                                                            ● FALSE: An error
                                                                              occurred. Details in
                                                                              ML_oCmdResult
STRUCT ML_KinJogContData
Name       Data type    Inherited             Address       Initial value   Comment
                        from
  In       ML_iKinJog‐                                                      Input: Command data of
           Cont                                                             the command

STRUCT ML_KinJogContData
  Out      ML_oCmdRe‐                                                Output: Command parame‐
sult                                                      ters
STRUCT ML_iKinJogCont EXTENDS ML_iKinCmdBase
Name        Data type   Inherited   Address          Initial value   Comment
                        from
  KinName STRING(15) ML_iKinCmd‐                                     Name of the kinematics
                        Base                                         used to execute the com‐
                                                                     mand
 Source      STRING(50)     ML_iKinCmd‐                              Specifies the command
                            Base                                     source, e.g PlcApplication1
                                                                     is displayed in the diag‐

                                                 nostic messages
 SourceLine ULINT           ML_iKinCmd‐                              Specifies the source line of
        Base                                     the command; is displayed
                                                 in the diagnostic messages
 Direction   ARRAY                                                   Direction vector
[0..15] OF
LREAL
 CoordSys    STRING(15)                                              Coordinate system of the
                                                 direction vector (WCS,
                                                 MCS, PCS, TCS, ACS)
 DynLimits ML_iDynLi‐                                                Limit values for the jog
mits                                                      command
STRUCT ML_oCmdResult
Name       Data type        Inherited     Address    Initial value   Comment
                            from
 CmdID       ULINT                                                   Command ID (is set to
                                                                     18446744073709551615 in
                                                                     the event of an error)
 Error       BOOL                                                    Error ID TRUE indicates
                                                                     that an error occurred
 ErrorID     UDINT                                                   Specifies the type of
                                                                     occurred error: The upper
                                                                     4 bytes reflect the main
                                                                     diagnostics, the lower 4
                                                                     bytes reflect the detailed
                                                                     diagnostics, 0 means no
                                                                     error

Data Layer:
Method: POST
URL:                https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/jog-cont
Payload:

{
"type":"object","value":
{
"jogDir" : [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
"jogIncrement":0.0,
"coordSys":"WCS",

"lim":{
          "vel":10,
          "acc":10,
          "dec":10,
          "jrkAcc":1,
          "jrkDec":1
       }
}
}

Python:
<cmdID> = motion.kin_cmd_jog_cont( kin=<kinName>,
dir=<direction>, coord_sys=<coordSys>, [,vel=<velocity>]
[,acc=<acceleration>] [,dec=<deceleration>]
[,jrk_acc=<jerkAcceleration>] [,jrk_dec=<jerkDeceleration>] )

Generates a continuous jogging command for a kinematic (object has to be
"attached"), see documentation Python Runtime App ⮫ Python functions.
● <kinName> - string, kinematic object name
● <dir> - tuple of double or list of double (16 values max.), jogging direction
● <coordSys> - string, the coordinate system of the jog direction ("WCS",
  “MCS”, “PCS”, “TCS”, “ACS”)
● <velocity> - double, velocity limit value of the command (the last pro‐
  grammed velocity limit value is used if this parameter is not programmed)
● <acceleration> - double, acceleration limit value of the command (the last
  programmed acceleration limit value is used if this parameter is not pro‐
  grammed)
● <deceleration> - double, deceleration limit value of the command (the last
  programmed deceleration limit value is used if this parameter is not pro‐
  grammed)
● <jerkAcceleration> - double, jerk limit value for the acceleration of the com‐
  mand (the last programmed jerk limit value for the acceleration is used if
  this parameter is not programmed)
● <jerkDeceleration> - double, jerk limit value for the deceleration of the
  command (the last programmed jerk limit value for the deceleration is used
  if this parameter is not programmed)

BundleIF:
/// @brief Create a nonbuffered jog command for a kinematics
(KIN_CMD_JOG_*)
///
/// @param[in]   sourceInfo Command source
                             information
/// @param[in]   kinName     Name of the motion
                             object
/// @param[in]   cmdType     Type of the command
                             (KIN_CMD_JOG_ABS/
                             KIN_CMD_JOG_REL)
/// @param[in]   jogDir      Direction vector
/// @param[in]   targetCOS   Target coordinate
                             system for the
                             jogDir
/// @param[in]   jogIncrement Positive
                               incremental jog
                               distance (only
                               KIN_CMD_JOG_REL)

/// @param[in]       dynLim  Dynamic limits
                             of the command
/// @param[out] cmdID        The ID of the added
                             command
/// @return                  Status of the
                             function call:
                             STS_OK or an
                             error code on failure.
virtual MotionResult kinJogCmd( const cmd::CmdSourceInfo&
sourceInfo, const char* kinName, cmd::kin::KinCmdType cmdType,
double *jogDir , cmd::kin:: CmdTargetCOS targetCOS, double
jogIncrement, const cmd::DynamicLimitsT &dynLim, uint64_t
&cmdID ) const = 0;

with the following data types:

//! @brief Data container for dynamic limits
 struct DynamicLimitsT
 {
   double m_vel = 0.0;     //!<velocity limit
   double m_acc = 0.0;     //!<acceleration limit
   double m_dec = 0.0;     //!<deceleration limit
   double m_jrkAcc = 0.0; //!<jerk limit while accelerating
  double m_jrkDec = 0.0; //!<jerk limit while decelerating
  double m_jrkAcc2 = 0.0; //!<second jerk limit while
accelerating (not used)
   double m_jrkDec2 = 0.0; //!<second jerk limit while
decelerating (not used)
 };

Required command type for continuous jogging:

KinCmdType::KIN_CMD_JOG_ABS

Please note: m_jrkAcc2 and m_jrkDec2 are currently not supported and have
to be set to 0.

### 7.3.14 KinJogIncr - Incremental kinematic jogging

Basics
There are two commands for jogging a kinematics: KinJogIncr and KinJog‐
Cont. This command jogs the kinematics incrementally with the specified dis‐
tance and the commanded dynamic limits. The command can be aborted with
the "KinAbort" command.
Both commands move the kinematics along a certain vector. The length for
possible motions is always limited by the configured permissible axis ranges
of the kinematic axes. If the current position is outside the configured, per‐
missible kinematic axis range, the axes can move towards the permitted range
but cannot move away from the range.
The kinematics is in state "MOVING” during the motion. After reaching the end
position, the command is set to DONE and the kinematics goes to STANDBY
mode.
Jogging of the kinematics is only allowed if the kinematic is in state STANDBY,
the velocity is zero and no other command is active.

The programming limit values for velocity, acceleration, deceleration as well
as both jerk limits have to be positive (greater than zero), as otherwise the
parameters would be inconsistent.
Exception: If both jerk limit values are exactly zero, the motion is executed
without jerk limit (trapezoid velocity profile).
                     If the motion passes through a singularity or close to
       WARNING       a singularity, unexpectedly large accelerations and high
                     axis velocities may occur. For further information, refer
                     to ⮫ Dealing with singularities on page 194
The command supports the following coordinate systems:
● WCS (World Coordinate System)
● MCS (Machine Coordinate System)
● PCS (Product Coordinate System)
● TCS (Tool Coordinate System)
  The TCS coordinate system only serves as an input aid, i.e. the commanded
  lengths and directions are transformed from the TCS into the PCS and then
  interpolated in the latter. This also means that the jog direction always
  refers to the initial TCS orientation of the command. When position and
  orientation are tapped at the same time, a straight line is traversed in
  space on which the orientation changes, i.e. no arc. Also refer to ⮫ Chapter
  6.3.1 Position and orientation in space on page 176
● ACS (Axis Coordinate System)
  The ACS coordinate system allows you to jog a single kinematic axis
  without having to ungroup or regroup the kinematics. If multiple kinematic
  axes are moved incrementally, a vector is calculated whose length corre‐
  sponds to the increment.

PLC:

ML_KinJogIncr
Name        Data type          Inherited     Address       Initial value   Comment
                               from
   Data     ML_KinJo‐                                                      InOut: Command parame‐
            gIncrData                                                      ters
  ML_KinJo‐ BOOL                                                           Returns, whether it was
gIncr                                                                      possible to add the com‐
                                                                           mand to the kinematic
                                                                           object.
                                                                           ● TRUE: The command
                                                                             could be added success‐
                                                                             fully
                                                                           ● FALSE: An error
                                                                             occurred. Details in
                                                                             ML_oCmdResult
STRUCT ML_KinJogIncrData
Name       Data type     Inherited           Address       Initial value   Comment
                         from

STRUCT ML_KinJogIncrData
  In       ML_iKinJo‐                                                Input: Command data of
gIncr                                                     the command
  Out      ML_oCmdRe‐                                                Output: Command parame‐
sult                                                      ters
STRUCT ML_iKinJogIncr EXTENDS ML_iKinCmdBase
Name        Data type    Inherited   Address         Initial value   Comment
                         from
  KinName STRING(63) ML_iKinCmd‐                                     Name of the kinematics
                         Base                                        used to execute the com‐
                                                                     mand

  Source     STRING(50)     ML_iKinCmd‐                              Specifies the command
        Base                                     source, e.g PlcApplication1
                                                 is displayed in the diag‐
                                                 nostic messages
  SourceLine ULINT          ML_iKinCmd‐                              Specifies the source line of
        Base                                     the command; is displayed
                                                 in the diagnostic messages
  Increment LREAL                                                    Jog distance increment
  Direction ARRAY                                                    Direction vector
[0..15] OF
LREAL
  CoordSys STRING(15)                                                Coordinate system of the
                                                 direction vector (WCS,
                                                 MCS, PCS, TCS, ACS)
  DynLimits ML_iDynLi‐                                               Limit values for the jog
mits                                                     command
STRUCT ML_oCmdResult
Name       Data type        Inherited     Address    Initial value   Comment
                            from
  CmdID      ULINT                                                   Command ID (is set to
                                                                     18446744073709551615 in
                                                                     the event of an error)
  Error      BOOL                                                    Error ID TRUE indicates
                                                                     that an error occurred
  ErrorID    UDINT                                                   Specifies the type of
                                                                     occurred error: The upper
                                                                     4 bytes reflect the main
                                                                     diagnostics, the lower 4
                                                                     bytes reflect the detailed
                                                                     diagnostics, 0 means no
                                                                     error

Data Layer:
Method: POST
URL:                https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/jog-incr
Payload:

{
"type":"object","value":
{

"jogDir" : [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
"jogIncrement":1,
"coordSys":"WCS",
"lim":{
        "vel":1000,
        "acc":1000,
        "dec":10,
        "jrkAcc":1,
        "jrkDec":1
      }
}
}

Python:
<cmdID> = motion.kin_cmd_jog_incr( kin=<kinName>,
dir=<direction>, incr=<increment>, coord_sys=<coordSys>,
[,vel=<velocity>] [,acc=<acceleration>] [,dec=<deceleration>]
[,jrk_acc=<jerkAcceleration>] [,jrk_dec=<jerkDeceleration>] )

Creates an incremental jog command for a kinematics (object has to be
"attached"), see documentation Python Runtime App ⮫ Python functions.
●   <kinName> - string, kinematic object name
●   <dir> - tuple of double or list of double (16 values max.), jogging direction
●   <incr> - double, increment to be moved
●   <coordSys> - string, the coordinate system of the jog direction ("WCS",
    “MCS”, “PCS”, “TCS”, “ACS”)
●   <velocity> - double, velocity limit value of the command (the last pro‐
    grammed velocity limit value is used if this parameter is not programmed)
●   <acceleration> - double, acceleration limit value of the command (the last
    programmed acceleration limit value is used if this parameter is not pro‐
    grammed)
●   <deceleration> - double, deceleration limit value of the command (the last
    programmed deceleration limit value is used if this parameter is not pro‐
    grammed)
●   <jerkAcceleration> - double, jerk limit value for the acceleration of the com‐
    mand (the last programmed jerk limit value for the acceleration is used if
    this parameter is not programmed)
●   <jerkDeceleration> - double, jerk limit value for the deceleration of the
    command (the last programmed jerk limit value for the deceleration is used
    if this parameter is not programmed)

BundleIF:
// @brief Create a nonbuffered jog command for a kinematics
(KIN_CMD_JOG_*)
///
// @param[in]    sourceInfo Command source
                             information
/// @param[in]   kinName     Name of the motion
                             object
/// @param[in]   cmdType     Type of the command
                             (KIN_CMD_JOG_ABS/
                             KIN_CMD_JOG_REL)
/// @param[in]   jogDir      Direction vector
/// @param[in]   targetCOS   Target coordinate
                             system for the

                             jogDir
/// @param[in]       jogIncrement
                               Positive
                               incremental
                               jog distance
                               (only
                               KIN_CMD_JOG_REL)
/// @param[in]   dynLim      Dynamic limits of
                             the command
/// @param[out] cmdID        The ID of the added
                             command
/// @return                  Status of the
                             function call:
                             STS_OK or an error

                             code on failure.
virtual MotionResult kinJogCmd( const cmd::CmdSourceInfo&
sourceInfo, const char* kinName, cmd::kin::KinCmdType cmdType,
double *jogDir , cmd::kin:: CmdTargetCOS targetCOS, double
jogIncrement, const cmd::DynamicLimitsT &dynLim, uint64_t
&cmdID ) const = 0;

with the following data types:

//! data container for dynamic limits
 struct DynamicLimitsT
 {
   double m_vel = 0.0;     //!<velocity limit
  double m_acc = 0.0;      //!<acceleration limit
  double m_dec = 0.0;      //!<deceleration limit
  double m_jrkAcc = 0.0;   //!<jerk limit while accelerating
  double m_jrkDec = 0.0;   //!<jerk limit while decelerating
  double m_jrkAcc2 = 0.0; //!<second jerk limit while
accelerating (not used)
  double m_jrkDec2 = 0.0; //!<second jerk limit while
decelerating (not used)
 };

Required command type for incremental jogging:

KinCmdType::KIN_CMD_JOG_REL

Please note: m_jrkAcc2 and m_jrkDec2 are currently not supported and have
to be set to 0.

### 7.3.15 KinInterrupt, KinInterrupt2 - Interrupting the kinematic command

Basics
This command interrupts the current kinematic motion with the current,
dynamic limit values. Deceleration can be performed with the last com‐
manded limits, with reduced axis limits or with the configured axis limits. The
behavior is identical to setting of the kinematic override to 0%. Continue the
motion with the “KinContinue” command. This command is effective immedi‐
ately, it does not change the command buffer (so all buffered commands are
still available).
Restriction: When moving the kinematics with KinMoveDirectAsync, the kine‐
matic will always decelerate on a deceleration ramp with the last commanded
limits, irrespective of the specified braking limit.

States of the Interrupt/Continue command
The Interrupt and Continue commands are active together with the regular
command processing. Thus, there are the following command states:
Commanding sequence       Response of the kine‐    Command state
                          matics
Motion command            Kinematics starts moving Move: ACTIVE
becomes active
Interrupt is commanded    Kinematics decelerates    Move: ACTIVE; Interrupt:
                          with the currently com‐   ACTIVE
                          manded dynamics
-                         Kinematics stopped        Move: ACTIVE; Interrupt:
                                                    DONE
Continue is commanded Kinematics accelerates        Move: ACTIVE; Interrupt:
                      again (continues the          DONE; Continue: DONE
                      motion command)
-                     Target position of motion Move: DONE; Interrupt:
                      command is reached,       DONE; Continue: DONE
                      motion is stopped
The Continue command can also be commanded before a complete kinematic
stop. In this case, the third table line is not applicable.

States of the Interrupt/Continue command
The Abort command also aborts an Interrupt command.
Thus, there are the following kinematic command states:
Commanding sequence       Response of the kine‐    Command state
                          matics
Motion command            Kinematics starts moving Move: ACTIVE
becomes active
Interrupt is commanded    Kinematics decelerates    Move: ACTIVE; Interrupt:
                          with the currently com‐   ACTIVE
                          manded dynamics
Abort is commanded        Kinematics continues to   Move: ABORTED; Inter‐
before it is stopped      decelerate with the       rupt: ABORTED; Abort:
                          currently commanded       ACTIVE
                          dynamics
-                         Motion is stopped         Move: ABORTED; Inter‐
                                                    rupt: ABORTED; Abort:
                                                    DONE
In case of buffered commands that do not stop until the end of the motion
(as e.g. during blending with splines), it can sporadically happen that several
commands become active after an abort until the kinematics is stopped.
Therefore, the active command is not immediately set to ABORTED (as it
might not have been processed completely and thus reached state DONE).

PLC:

ML_KinInterrupt
Name         Data type       Inherited     Address   Initial value   Comment
                             from
  Data       ML_KinInter‐                                            InOut: Command parame‐

ruptData                                                ters
   ML_KinIn‐ BOOL                                                    Returns, whether it was
terrupt                                                              possible to add the com‐
mand to the kinematic
object.
● TRUE: The command
  could be added success‐
  fully
● FALSE: An error
  occurred. Details in
  ML_oCmdResult
STRUCT ML_KinInterruptData
Name       Data type     Inherited         Address   Initial value   Comment
                         from
  In       ML_iKinCmd‐                                               Input: Command data of
           Base                                                      the command
  Out      ML_oCmdRe‐                                                Output: Command parame‐
           sult                                                      ters
STRUCT ML_iKinCmdBase
Name        Data type        Inherited     Address   Initial value   Comment
                             from
  KinName     STRING(63)                                             Name of the kinematics
                                                                     used to execute the com‐
                                                                     mand
  Source      STRING(50)                                             Specifies the command
                                                                     source, e.g PlcApplication1
                                                                     is displayed in the diag‐
                                                                     nostic messages
  SourceLine ULINT                                                   Specifies the source line of
                                                                     the command; is displayed
                                                                     in the diagnostic messages

STRUCT ML_oCmdResult
Name       Data type           Inherited    Address   Initial value   Comment
                               from
   CmdID           ULINT                                              Command ID (is set to
                                                                      18446744073709551615 in
                                                                      the event of an error)
   Error           BOOL                                               Error ID TRUE indicates
                                                                      that an error occurred
   ErrorID         UDINT                                              Specifies the type of
                                                                      occurred error: The upper
                                                                      4 bytes reflect the main
                                                                      diagnostics, the lower 4
                                                                      bytes reflect the detailed
                                                                      diagnostics, 0 means no
                                                                      error

PLC:

ML_KinInterrupt2
Name         Data type         Inherited    Address   Initial value   Comment
                               from
   Data      ML_KinInter‐                                             InOut: Command parame‐
             rupt2Data                                                ters
   ML_KinIn‐ BOOL                                                     Returns, whether it was
terrupt2                                                              possible to add the com‐
                                                                      mand to the kinematic
                                                                      object.
                                                                      ● TRUE: The command
                                                                        could be added success‐
                                                                        fully
                                                                      ● FALSE: An error
                                                                        occurred. Details in
                                                                        ML_oCmdResult
STRUCT ML_KinInterruptData2
Name       Data type     Inherited          Address   Initial value   Comment
                         from
  In       ML_iKinInter‐                                              Input: Command data of
           rupt                                                       the command
  Out      ML_oCmdRe‐                                                 Output: Command parame‐
           sult                                                       ters

STRUCT ML_iKinInterrupt EXTENDS ML_iKinCmdBase
Name        Data type     Inherited   Address       Initial value   Comment
                          from
  KinName STRING(63) ML_iKinCmd‐                               Name of the kinematics
                          Base                                 used to execute the com‐
                                                               mand
  Source      STRING(50)    ML_iKinCmd‐                        Specifies the command
                            Base                               source, e.g PlcApplication1
                                                               is displayed in the diag‐
                                                               nostic messages
  SourceLine ULINT          ML_iKinCmd‐                        Specifies the source line of
                            Base                               the command; is displayed

                                   in the diagnostic messages
  brakeType ML_BrakeDy‐                             BRAKE_WITH Dynamic limit type selec‐
namicLimits                             _COM‐      tion (is not yet supported)
                        MANDED_LI
                        MITS
STRUCT ML_iKinCmdBase
Name        Data type       Inherited     Address   Initial value   Comment
                            from
  KinName     STRING(63)                                            Name of the kinematics
                                                                    used to execute the com‐
                                                                    mand
  Source      STRING(50)                                            Specifies the command
                                                                    source, e.g PlcApplication1
                                                                    is displayed in the diag‐
                                                                    nostic messages
  SourceLine ULINT                                                  Specifies the source line of
                                                                    the command; is displayed
                                                                    in the diagnostic messages
ENUM ML_BrakeDynamicLimits
Name       Data type   Inherited          Address   Initial value   Comment
                       from
           INT                                                      Decelerating with the cur‐
BRAKE_WITH                                                          rently commanded dynamic
_COM‐                                                               limits (soft stop)
MANDED_LI
MITS
           INT                                                      Decelerate with axis limits,
BRAKE_WITH                                                          reduced using ML_KinAxs‐
_AXS_REDUC                                                          DynLimP or with the
ED_LIMITS                                                           configured axis limits if
                                                                    ML_KinAxsDynLimP is not
                                                                    active
              INT                                                   Decelerate with the config‐
BRAKE_WITH                                                          ured dynamic limit values
_AXS_CFG_LI                                                         (hard stop)
MITS

STRUCT ML_oCmdResult
Name       Data type             Inherited   Address      Initial value   Comment
                                 from
   CmdID           ULINT                                                  Command ID (is set to
                                                                          18446744073709551615 in
                                                                          the event of an error)
   Error           BOOL                                                   Error ID TRUE indicates
                                                                          that an error occurred
   ErrorID         ULINT                                                  Specifies the type of
                                                                          occurred error: The upper
                                                                          4 bytes reflect the main
                                                                          diagnostics, the lower 4
                                                                          bytes reflect the detailed
                                                                          diagnostics, 0 means no
                                                                          error

Data Layer:
Method: POST
URL:                https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/interrupt
Payload: (blank)

Python:
<cmdID> = motion.kin_cmd_interrupt( obj=<kinName>, str=<type> )

Generates an interrupt command for a kinematic (object has to be "attached"),
see documentation Python Runtime App ⮫ Python functions.
● <kinName> - string, kinematic name
● <type> - string, type of braking limit
  – BRAKE_WITH_COMMANDED_LIMITS (default, if type = none)
  – BRAKE_WITH_AXS_REDUCED_LIMITS
  – BRAKE_WITH_AXS_CFG_LIMITS

BundleIF:
//! Create an interrupt command for a kinematic
(KIN_CMD_INTERRUPT)
//!
//! @param[in]   handle      Handle of the interface
//! @param[in]   sourceInfo Command source information
//! @param[in]   kinName     Name of the motion object
//! @param[out] cmdID        The ID of the added command
//! @return                  Was everything okay?
extern "C" MotionResult MOTION_CORE_KinInterruptCmd(void
*handle, const dia::CmdSourceInfo& sourceInfo, const char*
kinName, uint64_t &cmdID);

/// @brief Selector for the brake dynamic limits to be used by
the ipo IVAJ
enum class IVAJBrakeLimit
{
BRAKE_WITH_COMMANDED_LIMITS,   ///< do a brake ramp (on path)
                                    until vel=0 with the
                                    commanded limits (same as

                                    setting override to zero)
BRAKE_WITH_AXS_REDUCED_LIMITS, ///< do a brake ramp (on path)
                                    until vel=0 with the
                                    reduced axis limits
                                    (ignore the commanded and
                                    configured kinematics
                                    limits)
BRAKE_WITH_AXS_CFG_LIMITS,     ///< do a brake ramp (on path)
                                    until vel=0 with the
                                    configured axis limits
                                    (ignore all other limits)
};

//! @brief Create an interrupt command for a kinematic
(KIN_CMD_INTERRUPT)
//!
//! @param[in]   handle      Handle of the interface
//! @param[in]   sourceInfo Command source information
//! @param[in]   kinName     Name of the motion object
//! @param[in]   brakeLimit Use the given brake dynamic
limits for the downslope
//! @param[out] cmdID        The ID of the added command
//! @return                  Was everything okay?
extern "C" MotionResult MOTION_CORE_KinInterruptCmdEx(void
*handle, const dia::CmdSourceInfo& sourceInfo, const
char* kinName, ::motion::core::ipo::IVAJBrakeLimit brakeLimit,
uint64_t &cmdID)

### 7.3.16 KinContinue - Continuing the kinematic command

Basics
This command continues the current kinematic motion that has been inter‐
rupted by the “KinInterrupt" command, using the current dynamic limit values.
The behavior is identical to setting the kinematic override to the previous
value. This command is effective immediately, it does not change the com‐
mand buffer (so all buffered commands are still available, overrides from 0 to
the previous value).

PLC:

ML_KinContinue
Name        Data type             Inherited   Address   Initial value   Comment
                                  from
   Data            ML_KinConti‐                                         InOut: Command parame‐
                   nueData                                              ters
  ML_Kin‐          BOOL                                                 Returns, whether it was
Continue                                                                possible to add the com‐
                                                                        mand to the kinematic
                                                                        object.
                                                                        ● TRUE: The command
                                                                          could be added success‐
                                                                          fully
                                                                        ● FALSE: An error
                                                                          occurred. Details in
                                                                          ML_oCmdResult
STRUCT ML_KinContinueData
Name       Data type    Inherited             Address   Initial value   Comment
                        from
  In       ML_iKinCmd‐                                                  Input: Command data of
           Base                                                         the command
  Out      ML_oCmdRe‐                                                   Output: Command parame‐
           sult                                                         ters
STRUCT ML_iKinCmdBase
Name        Data type             Inherited   Address   Initial value   Comment
                                  from
   KinName         STRING(63)                                           Name of the kinematics
                                                                        used to execute the com‐
                                                                        mand
   Source          STRING(50)                                           Specifies the command
                                                                        source, e.g PlcApplication1
                                                                        is displayed in the diag‐
                                                                        nostic messages
   SourceLine ULINT                                                     Specifies the source line of
                                                                        the command; is displayed
                                                                        in the diagnostic messages

STRUCT ML_oCmdResult
Name       Data type          Inherited   Address      Initial value   Comment
                              from
 CmdID       ULINT                                                     Command ID (is set to
                                                                       18446744073709551615 in
                                                                       the event of an error)
 Error       BOOL                                                      Error ID TRUE indicates
                                                                       that an error occurred
 ErrorID     UDINT                                                     Specifies the type of
                                                                       occurred error: The upper
                                                                       4 bytes reflect the main
                                                                       diagnostics, the lower 4

                                                   bytes reflect the detailed
                                                   diagnostics, 0 means no
                                                   error

Data Layer:
Method: POST
URL:                https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/continue
Payload: (blank)

Python:
<cmdID> = motion.kin_cmd_continue( obj=<kinName> )

Removes an active interrupt command of a kinematic (object has to be
"attached"), see documentation Python Runtime App ⮫ Python functions.
The command is active immediately, getCmdState( ) with the specified com‐
mand ID always returns a DONE.
● <kinName> - string, kinematic name

BundleIF:
//! Create an continue command for a kinematic removes an
active interrupt command (KIN_CMD_CONTINUE)
//!
//! @param[in]   handle      Pointer to the interface
//! @param[in]   sourceInfo Command source information
//! @param[in]   kinName     Name of the motion object
//! @param[out] cmdID        The ID of the added command
//! @return                  Was everything okay?
extern "C" MotionResult MOTION_CORE_KinContinueCmd(void
*handle, const dia::CmdSourceInfo& sourceInfo, const char*
kinName, uint64_t &cmdID);

### 7.3.17 KinAbort, KinAbort2 - Canceling the kinematic command

Basics
This command cancels the current motion for a kinematics. During the com‐
mand, the kinematic is in state ABORTING. Deceleration can be performed
with the last commanded limits, with reduced axis limits or with the config‐
ured axis limits to zero velocity on the programmed path. If the motion has

stopped, the command is set to state DONE, the PLC Open state of the kin‐
ematics is set to STANDBY and all commands in the preparation buffer are
removed. KinAbort can be commanded in state MOVING or STANDBY.
Restriction: When moving the kinematics with KinMoveDirectAsync, the kine‐
matic will always decelerate on a deceleration ramp with the last commanded
limits, irrespective of the specified braking limit.
This command is an unbuffered command, i.e. all previously active commands
and the commands of the preparation buffer are discarded. These commands
are assigned the command state ABORTED.

PLC:

ML_KinAbort
Name        Data type             Inherited     Address   Initial value   Comment
                                  from
   Data            ML_KinAbort‐                                           InOut: Command parame‐
                   Data                                                   ters
  ML_KinA‐         BOOL                                                   Returns, whether it was
bort                                                                      possible to add the com‐
                                                                          mand to the kinematic
                                                                          object.
                                                                          ● TRUE: The command
                                                                            could be added success‐
                                                                            fully
                                                                          ● FALSE: An error
                                                                            occurred. Details in
                                                                            ML_oCmdResult
STRUCT ML_KinAbortData
Name       Data type              Inherited     Address   Initial value   Comment
                                  from
   In              ML_iKinCmd‐                                            Input: Command data of
                   Base                                                   the command
   Out             ML_oCmdRe‐                                             Output: Command parame‐
                   sult                                                   ters
STRUCT ML_iKinAbort EXTENDS ML_iKinCmdBase
Name        Data type   Inherited   Address               Initial value   Comment
                        from
  KinName STRING(63) ML_iKinCmd‐                                          Name of the kinematics
                        Base                                              used to execute the com‐
                                                                          mand
   Source          STRING(50)     ML_iKinCmd‐                             Specifies the command
                                  Base                                    source, e.g PlcApplication1
                                                                          is displayed in the diag‐
                                                                          nostic messages
   SourceLine ULINT               ML_iKinCmd‐                             Specifies the source line of
                                  Base                                    the command; is displayed
                                                                          in the diagnostic messages

STRUCT ML_oCmdResult
Name       Data type        Inherited    Address   Initial value   Comment
                            from
  CmdID      ULINT                                                 Command ID (is set to
                                                                   18446744073709551615 in
                                                                   the event of an error)
  Error      BOOL                                                  Error ID TRUE indicates
                                                                   that an error occurred
  ErrorID    UDINT                                                 Specifies the type of
                                                                   occurred error: The upper
                                                                   4 bytes reflect the main
                                                                   diagnostics, the lower 4

bytes reflect the detailed
diagnostics, 0 means no
error

PLC:

ML_KinAbort2
Name         Data type      Inherited    Address   Initial value   Comment
                            from
  Data       ML_KinA‐                                              InOut: Command parame‐
             bort2Data                                             ters
  ML_KinA‐   BOOL                                                  Returns, whether it was
bort2                                                              possible to add the com‐
                                                                   mand to the kinematic
                                                                   object.
                                                                   ● TRUE: The command
                                                                     could be added success‐
                                                                     fully
                                                                   ● FALSE: An error
                                                                     occurred. Details in
                                                                     ML_oCmdResult
STRUCT ML_KinAbortData2
Name       Data type    Inherited        Address   Initial value   Comment
                        from
  In       ML_iKinAbort                                            Input: Command data of
                                                                   the command
  Out        ML_oCmdRe‐                                            Output: Command parame‐
             sult                                                  ters
STRUCT ML_iKinAbort EXTENDS iKinCmdBase
Name        Data type   Inherited   Address        Initial value   Comment
                        from
  KinName STRING(63) ML_iKinCmd‐                                   Name of the kinematics
                        Base                                       used to execute the com‐
                                                                   mand

STRUCT ML_iKinAbort EXTENDS iKinCmdBase
  Source    STRING(50) ML_iKinCmd‐                                 Specifies the command
Base                                       source, e.g PlcApplication1
                                   is displayed in the diag‐
                                   nostic messages
   SourceLine ULINT             ML_iKinCmd‐                        Specifies the source line of
Base                               the command; is displayed
                                   in the diagnostic messages
   brakeType ML_BrakeDy‐                                BRAKE_WITH Dynamic limit type selec‐
namicLimits                                _COM‐      tion (is not yet supported)
                        MANDED_LI
                        MITS
STRUCT ML_iKinCmdBase
Name        Data type           Inherited   Address     Initial value   Comment
                                from
   KinName         STRING(63)   ML_iKinCmd‐                             Name of the kinematics
                                Base                                    used to execute the com‐
                                                                        mand
   Source          STRING(50)   ML_iKinCmd‐                             Specifies the command
                                Base                                    source, e.g PlcApplication1
                                                                        is displayed in the diag‐
                                                                        nostic messages
ENUM ML_BrakeDynamicLimits
Name       Data type   Inherited              Address   Initial value   Comment
                       from
           INT                                                          Decelerating with the cur‐
BRAKE_WITH                                                              rently commanded dynamic
_COM‐                                                                   limits (soft stop)
MANDED_LI
MITS
           INT                                                          Decelerate with axis limits,
BRAKE_WITH                                                              reduced using ML_KinAxs‐
_AXS_REDUC                                                              DynLimP or with the
ED_LIMITS                                                               configured axis limits if
                                                                        ML_KinAxsDynLimP is not
                                                                        active
                   INT                                                  Decelerate with the config‐
BRAKE_WITH                                                              ured dynamic limit values
_AXS_CFG_LI                                                             (hard stop)
MITS
STRUCT ML_oCmdResult
Name       Data type            Inherited     Address   Initial value   Comment
                                from
   CmdID           ULINT                                                Command ID (is set to
                                                                        18446744073709551615 in
                                                                        the event of an error)
   Error           BOOL                                                 Error ID TRUE indicates
                                                                        that an error occurred

STRUCT ML_oCmdResult
  ErrorID  UDINT                                                  Specifies the type of
                                              occurred error: The upper
                                              4 bytes reflect the main
                                              diagnostics, the lower 4
                                              bytes reflect the detailed
                                              diagnostics, 0 means no
                                              error

Data Layer:
Method: POST
URL:               https://<ip-addr>/automation/api/v2/nodes/motion/kin/

<kin_name>/cmd/abort
Payload: (blank)

Python:
<cmdID> =     motion.kin_cmd_abort( kin=<kinName>>, str=<type> )

Generates an abort command for a kinematic (object has to be "attached"),
see documentation Python Runtime App ⮫ Python functions.
● <kinName> - string, kinematic object name
● <type> - string, type of braking limit
  – BRAKE_WITH_COMMANDED_LIMITS (default, if type = none)
  – BRAKE_WITH_AXS_REDUCED_LIMITS
  – BRAKE_WITH_AXS_CFG_LIMITS

BundleIF:
//! Create a abort command for a kinematic (KIN_CMD_ABORT)
//!
//! @param[in]   sourceInfo Command source information
//! @param[in]   kinName     Name of the motion object
//! @param[out] cmdID        The ID of the added command
//! @return                  Was everything okay?
virtual MotionResult kinAbortCmd(const cmd::Cmd-SourceInfo&
sourceInfo, const char* kinName, uint64_t&cmdID) const = 0;

/// @brief Selector for the brake dynamic limits to be used by
the ipo IVAJ
enum class IVAJBrakeLimit
{
BRAKE_WITH_COMMANDED_LIMITS,   ///< do a brake ramp (on path)
                                    until vel=0 with the
                                    commanded limits (same as
                                    setting override to zero)
BRAKE_WITH_AXS_REDUCED_LIMITS, ///< do a brake ramp (on path)
                                    until vel=0 with the
                                    reduced axis limits
                                    (ignore the commanded and
                                    configured kinematics
                                    limits)
BRAKE_WITH_AXS_CFG_LIMITS,     ///< do a brake ramp (on path)
                                    until vel=0 with the
                                    configured axis limits
                                    (ignore all other limits)

};

/// @brief Create a abort command for a kinematics
(KIN_CMD_ABORT)
///
/// @param[in] sourceInfo Command source information
/// @param[in] kinName      Name of the motion object
/// @param[in] brakeLimit Use the given brake dynamic
                            limits for the downslope
/// @param[out] cmdID       The ID of the added command
/// @return                 Was everything okay?
virtual MotionResult kinAbortCmdEx(const
dia::CmdSourceInfo& sourceInfo, const char*
kinName, ::motion::core::ipo::IVAJBrakeLimit brakeLimit,
uint64_t& cmdID) const = 0;

### 7.3.18 KinReset - Resetting the kinematics

Basics
This command resets all reported kinematic errors and in case of minor
errors, the command also resets the subordinate axes. The command sets the
kinematics into a defined state. After resetting a minor error, the kinematic is
in STANDBY state. The kinematics is ready for a new command. After resetting
of a fatal error, the kinematics is in state DISABLED without axis. The axis
remains unchanged when resetting a severe kinematic error.
The reset is only permitted if the kinematics is in an error state or in one of
the GROUP STANDSTILL or GROUP DISABLED states.
This command is an unbuffered command, i.e. all previously active commands
and the commands of the preparation buffer are discarded.
The following diagrams show the kinematic and the axis state machine
behavior during and after a reset.

     PLC:

ML_KinReset
Name        Data type             Inherited     Address   Initial value   Comment
                                  from
   Data            ML_KinReset‐                                           InOut: Command parame‐
                   Data                                                   ters
  ML_Kin‐          BOOL                                                   Returns, whether it was
Reset                                                                     possible to add the com‐
                                                                          mand to the kinematic
                                                                          object.
                                                                          ● TRUE: The command
                                                                            could be added success‐
                                                                            fully
                                                                          ● FALSE: An error
                                                                            occurred. Details in
                                                                            ML_oCmdResult
STRUCT ML_KinResetData
Name       Data type              Inherited     Address   Initial value   Comment
                                  from
   In              ML_iKinCmd‐                                            Input: Command data of
                   Base                                                   the command
   Out             ML_oCmdRe‐                                             Output: Command parame‐
                   sult                                                   ters

STRUCT ML_iKinCmdBase
Name        Data type         Inherited   Address      Initial value   Comment
                              from
 KinName     STRING(63)                                                Name of the kinematics
                                                                       used to execute the com‐
                                                                       mand
 Source      STRING(50)                                                Specifies the command
                                                                       source, e.g PlcApplication1
                                                                       is displayed in the diag‐
                                                                       nostic messages
 SourceLine ULINT                                                      Specifies the source line of
                                                                       the command; is displayed

                                                   in the diagnostic messages
STRUCT ML_oCmdResult
Name       Data type          Inherited   Address      Initial value   Comment
                              from
 CmdID       ULINT                                                     Command ID (is set to
                                                                       18446744073709551615 in
                                                                       the event of an error)
 Error       BOOL                                                      Error ID TRUE indicates
                                                                       that an error occurred
 ErrorID     UDINT                                                     Specifies the type of
                                                                       occurred error: The upper
                                                                       4 bytes reflect the main
                                                                       diagnostics, the lower 4
                                                                       bytes reflect the detailed
                                                                       diagnostics, 0 means no
                                                                       error

Data Layer:
Method: POST
URL:                https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/reset
Payload: (blank)

Python:
<cmdID> = motion.kin_cmd_reset( kin=<kinName> )

Generates a reset command for a kinematic (object has to be "attached"), see
documentation Python Runtime App ⮫ Python Functions.
● <kinName> - string, kinematic name

BundleIF:
//! Create a reset command for a kinematic (KIN_CMD_RESET)
//!
//! @param[in]   sourceInfo Command source information
//! @param[in]   kinName     Name of the motion object
//! @param[out] cmdID        The ID of the added command
//! @return                  Was everything okay?
virtual MotionResult kinResetCmd(const cmd::CmdSourceInfo&
sourceInfo, const char* kinName, uint64_t &cmdID ) const = 0;

### 7.3.19 KinContour - Specifying the contour area

Basics
The KinContourCmd command can be used in the ctrlX MOTION to define the
area of a contour from kinematic motions. For each parameter, it is specified
whether it is the beginning or the end of the contour. By defining the contour
area, ctrlX MOTION can ensure that the contour movements are processed
in the desired manner (see ⮫ Backgrounds/details on page 595 for more
information). Additionally, it is possible, by using a parameter, to control that
at the start of the contour the program waits until a specified number of
subsequent commands are completely prepared.

Functional description
Contour
A contour (in the sense of ctrlX MOTION) is a sequence of motions that are
to be executed one after the other (without interruptions). The course of the
contour is known in advance (at the time of commanding). Influences on exe‐
cution (e.g. ⮫ Chapter 7.7.3 SetOverride - Override on page 739) only affect
the dynamics of the motion, but not the geometric progression.

Command KinContourCmd
The KinContourCmd command can be used in the ctrlX MOTION to define the
area of a contour from kinematic motions. The command is called once at the
beginning of the contour and once at the end of the contour. By means of a
parameter it is specified whether it is the beginning or the end of the contour.
The contour itself may consist of any kinematic commands (especially motion
commands). Command options may also be toggled. By defining the contour,
the ctrlX MOTION can ensure that it is processed in the desired way (see
⮫ Backgrounds/details on page 595 for more information).
Waiting for preparation
When commanding the contour start, it can be additionally specified that
the execution at the start of the contour waits until a specified number of
following commands (i.e. commands of the contour) are completely prepared.
This can be used to build up a buffer that prevents a runtime error if the
execution of the command is faster than the preparation. The number of
commands to be prepared is limited by the contour end. So if you want to
wait until all commands of a contour are completely prepared, you can simply
specify a very large number. In that case, the end of the contour limits the
waiting time.
Command state
If you do not want to wait at the start of the contour (number of com‐
mands to be prepared is zero), the KinContour command is executed imme‐
diately (similar to a SetOverride, see ⮫ Chapter 7.7.3 SetOverride - Over‐
ride on page 739). If the command state is queried via GetCmdState (see
⮫ Chapter 7.8.7 GetCmdState - Command states on page 787) for this com‐
mand, a DONE is always returned. If, on the other hand, it has to be waited,
the command ACTIVE (if waiting) and only then DONE is set. The command at
the end of the contour is always executed immediately. If the command state
is queried via GetCmdState (see ⮫ Chapter 7.8.7 GetCmdState - Command
states on page 787) for this command, a DONE is always returned.
Unbuffered commands, KinAbort and KinReset

Unbuffered commands (see ⮫ Chapter 7.1 General information on page 325)
cause the command buffer to be discarded. The same applies to the KinAbort
command (see ⮫ Chapter 7.3.17 KinAbort, KinAbort2 - Canceling the kine‐
matic command on page 585). This implicitly terminates a contour definition.
This means that no contour end must be commanded in these cases.
With a KinReset (see ⮫ Chapter 7.3.18 KinReset - Resetting the kinematics
on page 590) all internal states are reset to the initial value. This also applies
to the contour area. This means that no contour end may be commanded even
after a KinReset.

Restrictions
Contour start and contour end

Contours must neither enclose nor overlap. Exactly one contour end must be
commanded for each contour start. If a contour end is commanded without
a contour start having occurred beforehand, the ctrlX MOTION generates a
runtime error in the kinematics and this goes into the ERROR state. The same
happens if another contour start is commanded after a contour start without a
contour end coming in between.
Deceleration ramp at contour start
If a number of commands is specified for the contour start for which prepa‐
ration is to be waited for, this necessarily results in a deceleration ramp at
contour start. In this case, the contour start command is active for at least
one cycle, even if sufficient commands have already been prepared. If zero is
specified as the number, this does not result in a deceleration ramp at the
contour start. The end of the contour never results in a deceleration ramp
(unless it results from other commands).

Backgrounds/details
Preparation and execution
In ctrlX MOTION, buffered commands are prepared in a background process
to such an extent that the execution of these commands can take place in a
time-optimized manner. In principle, as much data as possible is precalculated
so that the execution can interpolate optimally in terms of runtime on the
basis of this data. Prepared commands are labeled accordingly, so that the
execution is allowed to process these commands. Whenever a buffered com‐
mand is specified in ctrlX MOTION, the preparation becomes active internally
and prepares all commands in the command buffer up to that point for execu‐
tion.
Execution faster than preparation - runtime error
Typically, preparation is faster than execution. Thus, there are a lot of pre‐
pared commands that can be executed. However, if the execution is faster
than the preparation (in case of very short motions and high web velocity),
sporadically, the execution wants to switch a new command active, but there
are no prepared commands. This is not a problem if the last command ends
with a standstill. However, it results in a runtime error if the last command
has a continuous velocity profile and does not end with velocity zero. The
Wait for preparation function can be used to wait until a specified set of
subsequent commands is ready to be prepared before processing the contour.
This can be used to build up a buffer of prepared commands to work around
the runtime error problem.
LookAhead function
There are a number of functions in the ctrlX MOTION requiring data of the
following commands. Typical examples: PolyTrans (see ⮫ Chapter 7.5.8 KinPo‐
lyTransP - Command options for kinematics - Path rounding with polynomial
on page 667), which inserts a fillet between two motion commands using

a spline path, and ContMotion (see ⮫ Chapter 7.5.7 KinContMotionP - Con‐
tinuous motion across several commands on page 664), which generates a
continuous velocity profile. With PolyTrans, data of the individual command
as well as data of the successive command have to be accessed, with ContMo‐
tion, data of many successive commands (up to several hundred) are required.
For this purpose, the ctrlX MOTION LookAhead functionality is implemented.
If a command option requires data from subsequent commands, it can call the
LookAhead function. This prepares the subsequent commands for the required
level (so that the required data is also calculated) and provides the data. The
command option can then work with it.
End of command buffer
If the LookAhead function is to supply data from subsequent commands, but
there are no further commands in the command buffer, it returns this informa‐
tion to the calling command option. The command option interprets this as
“end of motion”. In the case of PolyTrans, this results in no rounding being
inserted (since there is no second command). In the case of ContMotion,
a deceleration ramp is generated until standstill at the end of the last com‐
mand.
Late commanding:
When the commands are prepared at the end of the command buffer, they are
marked as "prepared". When new commands are subsequently commanded,
the completed commands are not modified anymore. This can lead to the
contour not being processed as expected.
Example:
In the example, the PolyTrans command option (see ⮫ Chapter 7.5.8 KinPoly‐
TransP - Command options for kinematics - Path rounding with polynomial
on page 667) should be active. If PolyTrans does not find a successive com‐
mand in the preparation of LookAhead, no rounding is inserted as the end of
the contour is assumed. If now commanding is slower than the preparation,
it can sporadically occur that a command is prepared (without rounding) and
only afterwards the successive command is inserted into the command buffer.
This results in a motion without roundings, although PolyTrans is active.
The detailed flow in this example would then be: 1. Command n is specified
2. Preparation becomes active and prepares the command 3. PolyTrans com‐
mand option uses the LookAhead to find the successive command 4. Since
there is no other command in the command buffer yet, PolyTrans starts from
the end of the command sequence and does not create a rounding. 5. Com‐
mand n is marked as "ready for execution" 6. Command n+1 is specified. Thus,
no rounding has been inserted between command n and command n+1. Note:
At point 4, the ctrlX MOTION does not know whether the command sequence
has been completed or whether there was only a delay in the command. Even
with script processing, it is impossible to determine whether the relevant
contour sequence has been completed.
The detailed flow in this example would then be:
1.   Command n is specified
2.   Preparation becomes active and prepares the command
3.   PolyTrans command option uses the LookAhead to find the successive
     command
4.   Since there is no other command in the command buffer, PolyTrans
     starts from the end of the command sequence and does not create a
     rounding
5.   Command n is marked as "ready for execution”

6.   Command n+1 is specified
     🡆 Thus, no rounding has been inserted between command n and com‐
        mand n+1
At point 4, the ctrlX MOTION does not know whether the command sequence
has been completed or whether there was only a delay in the command. Even
with script processing, it is impossible to determine whether the relevant
contour sequence has been completed.
Contour definition
The KinContourCmd is used to specify to the ctrlX MOTION which commands
belong to a contour. This affects the behavior of the LookAhead in such a
way that the preparation of a command is delayed until successive commands
of the contour are available, even if they are commanded late. This allows

the LookAhead to always provide data from successive commands within the
contour, and the active command options work as expected.

PLC:

STRUCT ML_KinContourData
Name       Data type    Inherited          Address     Initial value   Comment
                        from
  In       ML_iKinCon‐                                                 Input: Command data of
           tour                                                        the command
  Out      ML_oCm‐                                                     Output: Command parame‐
           dOptResult                                                  ters
STRUCT ML_KinContour EXTENDS ML_iKinCmdBase
Name       Data type    Inherited   Address            Initial value   Comment
                        from
  KinName STRING(15) ML_iKinCmd‐                                       Name of the kinematics
                        Base                                           used to execute the com‐
                                                                       mand
  Source      STRING(50)     ML_iKinCmd‐                               Specifies the command
                             Base                                      source, e.g PlcApplication1
                                                                       is displayed in the diag‐
                                                                       nostic messages
  SourceLine ULINT           ML_iKinCmd‐                               Specifies the source line of
                             Base                                      the command; is displayed
                                                                       in the diagnostic messages
  IsStart     BOOL                                     TRUE            TRUE if this is the start of
                                                                       the contour, FALSE for the
                                                                       end of the contour
  PrepCmds UDINT                                       0               How many of the following
                                                                       commands should be com‐
                                                                       pletely prepared

STRUCT ML_oCmdResult
Name       Data type             Inherited   Address     Initial value   Comment
                                 from
   CmdID           ULINT                                                 Command ID (is set to
                                                                         18446744073709551615 in
                                                                         the event of an error)
   Error           BOOL                                                  Error ID TRUE indicates
                                                                         that an error occurred
   ErrorID         ULINT                                                 Specifies the type of
                                                                         occurred error: The upper
                                                                         4 bytes reflect the main
                                                                         diagnostics, the lower 4
                                                                         bytes reflect the detailed
                                                                         diagnostics, 0 means no
                                                                         error

Data Layer:
Method: POST
URL:               https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/contour
Payload:

{
"type":"object","value":
{
isStart:bool = true;
prepCmds:uint = 0;
}
}
{
"type":"object","value":
{
“isStart”: true,
“prepCmds”: 20
}
}

Python:
<cmdID> = motion.kin_cmd_contour( kin=<kinName>
[,is_start=<isStart>] [,prep_cmds=<prepCmds>])

Creates a kinematics command to specify the start and end of a contour
(object has to be "attached"), see documentation Python Runtime App
⮫ Python functions.
● <kinName> - string, kinematic name
● <isStart> -Boolean, is this the start of the contour? (Default: true)
● <prepCmds> - unsigned int, how many commands should be completely
  prepared? Has to be >= 0. Default value is 0.

BundleIF:

/// @brief Define start and end of a contour. Optional block
the execution at the begin of the contour until a given number
of following commands are completely prepared.
/// @param[in] handle        Handle of the interface
/// @param[in] sourceInfo    Command source information
/// @param[in] kinName       Name of the kinematics object
/// @param[in] contourStart Is this the start of the contour?
(set to false for the end of the contour)
/// @param[in] prepCmds      Number of following commands,
that should be completely prepared. Set to 0 for zero overhead
variant.
/// @param[out] cmdID        The ID of the added command
/// @return                  Status of the function call:

STS_OK or an error code on failure.
extern "C" MotionResult MOTION_CORE_KinContourCmd(void*
handle, const dia::CmdSourceInfo & sourceInfo, const char*
kinName, bool contourStart, std::uint32_t prepCmds, uint64_t &
cmdID)

### 7.3.20 KinPathSmooth - Smooth path rounding and continuous velocity

across multiple commands
Basics
The KinPathSmooth command facilitates a smooth motion across multiple
commands for one kinematics. The command internally switches three sub-
commands (options) simultaneously. The three sub-commands are KinCon‐
tour, the command option KinContMotionP and the option for corner rounding
(e.g. KinPolyTransP, corresponding to the parameter RoundingType).

Functional description
If this command is enabled, all sub-commands are enabled and the parame‐
ters are assigned to them. The "eps" parameter have to be greater than 0.
Here, "eps" measures the maximum distance of the generated polynomial path
from the corner. Further details can be found in the KinPolyTransP Motion
command (see ⮫ Chapter 7.5.8 KinPolyTransP - Command options for kine‐
matics - Path rounding with polynomial on page 667).
If this command is disabled, all three sub-commands (options) are disabled.
If this command is enabled, KinContour, KinContMotion and KinPolyTrans
cannot be commanded separately and if one of the sub-commands (Kin‐
Contour, KinContMotionP and KinPolyTransP) is already active, the KinPathS‐
mooth command cannot be enabled.
The "eps" parameter can be updated with different eps values by repeatedly
calling the KinPathSmooth command. However, the values of PrepCmds and
RoundingType must remain the same. Both parameters are explained in the
InOut table of the ML_iKinPathSmooth structure

Command status

● If there is to be no waiting time at the start of the contour, the number of
   commands to be prepared have to be zero. The command is then executed
   immediately (similar to ML_SetOverride). In this case, DONE is always
   returned if the user queries this command via ML_GetCmdState
● If a wait is required at the start of the contour, the command status is
   set to ACTIVE during the waiting time and finally to DONE following the
   execution
● The command at the end of the contour is always executed immediately.
   If the user queries this command via ML_GetCmdState, DONE is always
   returned
In the event of an error (e.g. invalid command parameters), the command
is not added to the kinematics object and the kinematics status is set to
ERRORSTOP.

PLC:

STRUCT ML_KinPathSmooth
Name       Data type    Inherited            Address       Initial value   Comment
                        from
  In       ML_iKinKin‐                                                     Input: Command data of
           PathSmooth                                                      the command

STRUCT ML_KinPathSmooth
  Out      ML_oCm‐                                                    Output: Command parame‐
dOptResult                                                 ters
STRUCT ML_iKinPathSmooth EXTENDS ML_iKinCmdBase
Name        Data type   Inherited  Address     Initial value          Comment
                        from
  KinName STRING(63) ML_iKinCmd‐                                      Name of the kinematics
                        Base                                          used to execute the com‐
                                                                      mand
  Source      STRING(50)     ML_iKinCmd‐                              Specifies the command
                             Base                                     source, e.g PlcApplication1
                                                                      is displayed in the diag‐

nostic messages
  SourceLine ULINT           ML_iKinCmd‐                              Specifies the source line of
Base                                     the command; is displayed
in the diagnostic messages
  IsStart     BOOL                                    TRUE            TRUE if this is the start of
the contour, FALSE for the
end of the contour
  Eps         LREAL                                                   Maximum permissible tol‐
erance eps
  PrepCmds UDINT                                      0               How many of the following
commands should be com‐
pletely prepared
ML_Round‐                                               Rounding type for enabling
Rounding‐     ingType                                                 a command option for
Type                                                                  the transition of motion
commands, e.g. (PolyTrans
command option)
STRUCT ML_oCmdResult
Name       Data type         Inherited     Address    Initial value   Comment
                             from
  CmdID       ULINT                                                   Command ID (set to
                                                                      18446744073709551615 in
                                                                      case of error)
  Error       BOOL                                                    Error ID TRUE indicates
                                                                      that an error occurred
  ErrorID     ULINT                                                   Specifies the type of
                                                                      occurred error: The upper
                                                                      4 bytes reflect the main
                                                                      diagnostics, the lower 4
                                                                      bytes reflect the detailed
                                                                      diagnostics, 0 means no
                                                                      error

Data Layer:
Method: POST
URL: https://<ip-addr>/automation/api/v2/nodes/motion/kin/[kin name]/cmd/
path-smooth
Payload:

{
    "isStart": true,
    "eps": 0.5,
    "prepCmds": 20,
    "roundingType": "POLY_TRANS"
}
{
    "isStart": false,
    "eps": 0,
    "prepCmds": 0,
    "roundingType": "POLY_TRANS"
}
The command id of the KinPathSmooth command is always 0.

Python:
<cmdID> =
motion.kin_cmd_path_smooth( kin=<kinName>[,is_start=<isStart>]
[eps=<Eps>][,prep_cmds=<prepCmds>] [,])

Creates a kinematics command to specify the start and end of a contour
(object has to be "attached"), see documentation Python Runtime App
⮫ Python functions.
● <kinName> - string, kinematic name
● <isStart> -Boolean, is this the start of the contour? (default is FALSE)
● <Eps> - double; max. distance of the generated polynomial path from the
  corner
● <prepCmds> - unsigned int, how many commands should be completely
  prepared? Has to be >= 0. Default value is 0

Python example:
python example:

motion.kin_cmd_path_smooth(kin="Robot", is_start=True,
eps=0.5, prep_cmds=20, rounding_type = "POLY_TRANS")
#... // kin movement commands
#motion.kin_move_kin_cmd_move_lin_abs(…)
motion.kin_cmd_path_smooth("Robot")

# update parameter eps
motion.kin_cmd_path_smooth("Robot", True, 0.5, 20,
"POLY_TRANS") # path smooth on
motion.kin_move_kin_cmd_move_lin_abs(…)
motion.kin_move_kin_cmd_move_lin_abs(…)
motion.kin_cmd_path_smooth("Robot", True, 0.3, 20,
"POLY_TRANS") # # path smooth update parameter ‘eps’
motion.kin_move_kin_cmd_move_lin_abs(…)
motion.kin_move_kin_cmd_move_lin_abs(…)
motion.kin_cmd_path_smooth("Robot") # path smooth off

BundleIF:

/// @brief Create a motion command for a kinematics for
activation of smooth path over multiple commands
///
/// @param[in]   handle        Handle of the interface
/// @param[in]   sourceInfo    Command source information

/// @param[in]        kinName  Name of the kinematics object
/// @param[in]        isStart  Is this the start of the
                               contour?
                               (set to false for the end of
                               the contour)
/// @param[in]    eps          Maximum permissible tolerance
                               eps
/// @param[in]    prepCmds     Number of following commands,
                               that should be completely
                               prepared. Set to 0 for zero
                               overhead variant.
/// @param[in]    roundingType Rounding type to active a
                               command option for transition

                               of movement commands, e.g.
                               (PolyTrans command option)
/// @param[out] cmdID          The ID of the added command
/// @return                    Status of the function call:
                               STS_OK or an error code on
                               failure.
::motion::core::MotionResult(*kinPathSmoothCmd)(void* handle,
const ::motion::core::dia::CmdSourceInfo& sourceInfo, const
char* kinName, bool isStart, double eps, std::uint32_t
prepCmds, ::motion::core::cmd::kin::RoundingType roundingType,
uint64_t& cmdID);
