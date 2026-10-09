# 7.4 Kinematic commands with extended programming options

options

### 7.4.1 Overview

Description
In the case of kinematic motion commands with extended programming
options, the target position is specified by a sequence of value pairs, each
consisting of a number for the position value and an "extended meaning",
consisting of a meaning that describes what the numerical value refers to
and an attribute with additional information that specifies how the numerical
value is to be interpreted:
(<position value>, (<meaning>, <attribute>))
● Attributes make it possible, for example, to command parts of the kine‐
    matics absolutely and other parts incrementally within a command
● Only those axes/coordinates whose value changes in the current command
    has to be specified
Depending on the command, it is possible to specify the target position in
relation to different coordinate systems: PCS, MCS, ACS.
If a meaning is specified that is not supported by the kinematics (e.g. because
a corresponding axis is not assigned to the kinematics), a diagnostics is gener‐
ated.
Please note that some meanings are only supported if a corresponding axis
transformation is active. This mainly concerns the meanings for orientations,
but also the coordinates X, Y, Z.
There are exceptions for particular commands which can be processed
directly (additional commands) or as unbuffered. This includes, for example:

Meaning
The meaning indicates the axis or coordinate (position or orientation) to
which the specified numerical value refers.
The following meanings are supported:
X                                       X-coordinate
Y                                       Y-coordinate
Z                                       Z-coordinate
AX1                                     Axis 1 of the kinematics
AX2                                     Axis 2 of the kinematics
AX3                                     Axis 3 of the kinematics
...
AX16                                    Axis 16 of the kinematics
EUL1_ZYZ_I                              Euler angle 1 of the intrinsic orienta‐
                                        tion convention Z, Y', Z"
EUL2_ZYZ_I                              Euler angle 2 of the intrinsic orienta‐
                                        tion convention Z, Y', Z"
EUL3_ZYZ_I                              Euler angle 3 of the intrinsic orienta‐
                                        tion convention Z, Y', Z"
EUL1_XYZ_E                              Euler angle 1 of the extrinsic orienta‐
                                        tion convention X, Y, Z
EUL2_XYZ_E                              Euler angle 2 of the extrinsic orienta‐
                                        tion convention X, Y, Z
EUL3_XYZ_E                              Euler angle 3 of the extrinsic orienta‐
                                        tion convention X, Y, Z
EUL1_ZYX_E                              Euler angle 1 of the intrinsic orienta‐
                                        tion convention Z, Y, X
EUL2_ZYX_E                              Euler angle 2 of the intrinsic orienta‐
                                        tion convention Z, Y, X
EUL3_ZYX_E                              Euler angle 3 of the intrinsic orienta‐
                                        tion convention Z, Y, X
With regard to the orientation conventions, see also ⮫ Chapter 6.3.2 Orienta‐
tion & rotation on page 181.

Attribute
The attribute specifies how the numerical value is to be interpreted. Currnetly,
there are only attributes for absolute and relative motion. The attributes are
also used when specifying geometry-specific parameters (e.g. circle radius or
circle center).
The following attributes are supported:
● UNDEF - Default attribute (positions are interpreted as absolute values)
● INCR_VALUE - The specified numerical value is interpreted incrementally
● ABS_VALUE - The specified numerical value is interpreted as absolute

Command overview
The following extended motion commands are supported:
● ⮫ Chapter 7.4.2 KinMoveLinEx - Moving on a straight line in space
  on page 605
● ⮫ Chapter 7.4.3 KinMoveDirectEx - Point-to-point motion at axis level
  on page 609

● ⮫ Chapter 7.4.4 KinMoveDirectAsyncExx - Asynchronous point-to-point
  motion on page 614
● ⮫ Chapter 7.4.5 KinMove2DCircle - Movement on a plane-related cir‐
  cular/helical path on page 619
● ⮫ Chapter 7.4.6 KinMove3DCircle - Moving on a circular path in space
  on page 628
● ⮫ Chapter 7.4.7 KinMoveToPointLin - Moving the kinematics linearly to a
  saved point on page 634
● ⮫ Chapter 7.4.8 KinMoveToPointDirect - Moving the kinematics directly to a
  saved point on page 637

### 7.4.2 KinMoveLinEx - Moving on a straight line in space

Basics
This command is an extension of the commands ⮫ Chapter 7.3.4 KinMoveLi‐
nAbs - Absolute traversing of kinematics on page 524 and ⮫ Chapter 7.3.5
KinMoveLinRel - Relative traversing of kinematics on page 528.
It moves the kinematics in the PCS linearly on a straight line from the last
commanded TCP position to the new target position. Any additional axes
are also interpolated linearly. Changes to the orientation are processed using
parallel SLERP interpolation (see ⮫ Chapter Moving on a straight line - Move‐
Linear on page 279) if available.
You can select the coordinate system of the target position. The specified
target position is always transformed into the current PCS and interpolated
within it.
                      If commanding takes place in the ACS and an axis trans‐
         NOTICE       formation with ambiguities (singular poses) is active, it
                      is not guaranteed that the commanded axis positions
                      are reached at the end of the motion, as the transfor‐
                      mation branch present at the start of the motion is
                      retained within the interpolation. The final pose reached
                      in the PCS, however, is identical to the pose that
                      results for the commanded axis values.
As the target position, enter the position value, the meaning and the desired
attribute for each axis/coordinate of the kinematics to be moved at ⮫ Chapter
7.4.1 Overview on page 603. Depending on the attribute, the position values
are interpreted as absolute or relative values.

PLC:

ML_KinMoveLinEx
Name        Data type         Inherited   Address       Initial value   Comment
                              from
  Data       ML_KinMove‐                                                InOut: Command parame‐
             LinExData                                                  ters

ML_KinMoveLinEx
  ML_KinMo‐ BOOL                                                        Returns, whether it was
veLinEx                                                                 possible to add the com‐
mand to the kinematic
object.
● TRUE: The ML_KinMo‐
  veLinEx command was
  added successfully
● FALSE: An error
  occurred. Details in
  ML_oCmdResult
STRUCT ML_KinMoveLinExData
Name       Data type   Inherited              Address   Initial value   Comment
                       from
  In       ML_iKinMo‐                                                   Input: Command data of
           veLinEx                                                      the command
  Out      ML_oCmdRe‐                                                   Output: Command parame‐
           sult                                                         ters
STRUCT ML_iKinMoveLinEx EXTENDS ML_iKinCmdBase
Name        Data type   Inherited   Address    Initial value            Comment
                        from
  KinName STRING(15) ML_iKinCmd‐                                        Name of the kinematics
                        Base                                            used to execute the com‐
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
   CoordSys        STRING(15)                                           Coordinate system of the
                                                                        commanded target position
                                                                        (PCS, WCS, MCS or ACS
   Buffered        BOOL                                 TRUE            TRUE, if the command
                                                                        is to be executed as buf‐
                                                                        fered command, otherwise
                                                                        FALSE
   DynLimits ML_iDynLi‐                                                 Limit values of the position
             mits                                                       command
STRUCT ML_KinMotionCmdTarget
Name       Data type   Inherited              Address   Initial value   Comment
                       from
  CmdKin‐  ARRAY                                                        Commanded target posi‐
Target     [0..24] OF                                                   tion with meanings
           ML_KinCmd‐
           PosePair
  CmdKin‐  UINT                                                         Number of entries in
TargetSize                                                              CmdKinTarget

STRUCT ML_KinCmdPosePair
Name       Data type   Inherited               Address      Initial value   Comment
                       from
  Value    LREAL                                                            A value of the cmdKinPose
  Meaning  ML_Meaning                                                       Associated meaning of the
                                                                            value
      Attribute     ML_Attrib‐                              UNDEF           Additional attribute of the
                    utes                                                    meaning
ENUM ML_Meaning
Name      Data type                Inherited   Address      Initial value   Comment
                                   from

UNDEF         INT                                     0               Error or undefined
X             INT                                                     Absolute position of the x-
                                                        axis
Y             INT                                                     Absolute position of the y-
                                                        axis
Z             INT                                                     Absolute position of the z-
                                                        axis
AX1           INT                                                     Absolute position of axis 1
AX2           INT                                                     Absolute position of axis 2
AX3           INT                                                     Absolute position of axis 3
...
ENUM ML_MeaningAttribute
Name      Data type      Inherited             Address      Initial value   Comment
                         from
  UNDEF   INT                                               0               Error, undefined or not
                                                                            used
                    INT                                                     IC(): Incremental value
INCR_VALUE
                    INT                                                     AC(): Absolute value
ABS_VALUE
                    INT                                                     DC(): Shortest route
SHORT_WAY
                    INT                                                     ACP(): Positive direction of
POS_ROT_DI                                                                  rotation
R
                    INT                                                     ACN(): Negative direction
NEG_ROT_DI                                                                  of rotation
R
STRUCT ML_iDynLimits
Name        Data type              Inherited   Address      Initial value   Comment
                                   from
   Velocity         LREAL                                                   Velocity limit value
   Accelera‐        LREAL                                                   Acceleration limit value
tion
   Decelera‐        LREAL                                                   Deceleration limit value
tion
   JerkAcc          LREAL                                   0               Jerk limit value for acceler‐
                                                                            ation phase

STRUCT ML_iDynLimits
  JerkDec   LREAL                                          0               Jerk limit value for deceler‐
                                                    ation phase
STRUCT ML_oCmdResult
Name       Data type            Inherited    Address       Initial value   Comment
                                from
   CmdID           ULINT                                                   Command ID (is set to
                                                                           18446744073709551615 in
                                                                           the event of an error)
   Error           BOOL                                                    Error ID TRUE indicates
                                                                           that an error occurred
   ErrorID         UDINT                                                   Specifies the type of
                                                                           occurred error: The upper
                                                                           4 bytes reflect the main
                                                                           diagnostics, the lower 4
                                                                           bytes reflect the detailed
                                                                           diagnostics, 0 means no
                                                                           error

Data Layer
/motion/kin/<kin_name>/cmd/move-ex

Python
<cmdID> = motion.kin_cmd_move_ex( kin=<kinName>,
kin_pose_pair=<targetPose>
 [,coord_sys=<targetCoordSys>] [,vel=<velocity>]
[,acc=<acceleration>]
 [,dec=<deceleration>] [,jrk_acc=<jerkAcceleration>]
 [,jrk_dec=<jerkDeceleration>] [,buffered=<buffered>])

Generates MoveLinEx command for a kinematics (object has to be "attached"),
see documentation Python Runtime App ⮫ Python functions.
● <kinName> - string, kinematic name
● <targetPose> - Specify a target position of the command by pairing a
  meaning and a corresponding value for the coordinates to be offset.
  The pairs are collected in a dictionary data type { <meaning string>:<posi‐
  tion>, ... ,<meaning string>:<position>}.
  <position>can be a <float>, <long> or a <sub dictionary> with {<attribute
  string>:<float|long>}.
  Example:
  kin_pose_pair={ "X":3.0, "Y":2, "Z":{"INCR_VALUE":-10}, "AX5":
  {"POS_ROT_DIR":20}}
● <targetCoordSys> - string ("PCS", "WCS", "MCS" or "ACS"), coordinate
  system, in which <targetPose> is defined (coordinate system is "PCS", if
  not programmed)
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

/// @brief Create a linear motion command for a kinematics in
which the target position is specified by value pairs
///
/// @param[in]   sourceInfo             Command source
information
/// @param[in]   kinName                Name of the motion
object
/// @param[in]   targetPose             Target pose of the
command
/// @param[in]   nofTargetPoseElements Number of target pose
elements
/// @param[in]   targetCOS              Target coordinate
system for the targetPose
/// @param[in]   dynLim                 Dynamic limits of the
command
/// @param[out] cmdID                   The ID of the added
command
/// @param[in]   buffered               is buffered mode?
/// @return                             Status of the function
call: STS_OK or an error code on failure.

virtual MotionResult kinMoveCmdEx(const dia::CmdSourceInfo&
sourceInfo, const char* kinName,
                                  const cmd::CmdKinPosePair*
targetPose, const uint32_t nofTargetPoseElements,
                                  cmd::kin::CmdTargetCOS
targetCOS, const cmd::DynamicLimitsT& dynLim,
                                  uint64_t& cmdID, bool
buffered = true) const = 0;

### 7.4.3 KinMoveDirectEx - Point-to-point motion at axis level

Basics
This command is an extension of the commands ⮫ Chapter 7.3.6 KinMoveDir‐
ectAbs - Direct absolute traversing of kinematics on page 532 and ⮫ Chapter
7.3.7 KinMoveDirectRel - Direct relative traversing of kinematics on page 535.
It moves the axes of the kinematics to the commanded absolute or relative
target positions.
The coordinate system to which the specified target position refers can be
selected as required (PCS, MCS, ACS). The target position is transformed
internally in the ACS and the interpolation is carried out linearly on the axis
plane. The motion is coordinated so that all axes reach their target position
simultaneously.

                      As the interpolation is linear in the axis space, a
       NOTICE         linear spatial motion only results in case of a Cartesian
                      machine structure!
As the target position, enter the position value, the meaning and the desired
attribute for each axis/coordinate of the kinematics to be moved at ⮫ Chapter
7.4.1 Overview on page 603. Depending on the attribute, the position values
are interpreted as absolute or relative values.
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

PLC:

ML_KinMoveDirectEx
Name       Data type              Inherited    Address       Initial value   Comment
                                  from
   Data            ML_KinMove‐                                               InOut: Command parame‐
                   DirectExData                                              ters

ML_KinMoveDirectEx
  ML_KinMo‐ BOOL                                                    Returns, whether it was
veDirectEx                                                          possible to add the com‐
mand to the kinematic
object.
● TRUE: The ML_KinMove‐
  DirectEx command was
  added successfully
● FALSE: An error
  occurred. Details in
  ML_oCmdResult
STRUCT ML_KinMoveDirectExData

Name       Data type    Inherited         Address   Initial value   Comment
                        from
  In       ML_iKinMo‐                                               Input: Command data of
           veDirectEx                                               the command
  Out      ML_oCmdRe‐                                               Output: Command parame‐
           sult                                                     ters
STRUCT ML_iKinMoveDirectEx EXTENDS ML_iKinCmdBase
Name        Data type   Inherited   Address    Initial value        Comment
                        from
  KinName STRING(63) ML_iKinCmd‐                                    Name of the kinematics
                        Base                                        used to execute the com‐
                                                                    mand
  Source     STRING(50)     ML_iKinCmd‐                             Specifies the command
                            Base                                    source, e.g PlcApplication1
                                                                    is displayed in the diag‐
                                                                    nostic messages
  SourceLine ULINT          ML_iKinCmd‐                             Specifies the source line of
                            Base                                    the command; is displayed
                                                                    in the diagnostic messages
  CmdKin‐    ML_KinMo‐                                              Commanded absolute
Pose         tionCmd‐                                               target position with mean‐
             Target                                                 ings
  CoordSys   STRING(15)                                             Coordinate system of the
                                                                    commanded target position
                                                                    (PCS, WCS, MCS or ACS
  Buffered   BOOL                                   TRUE            TRUE, if the command
                                                                    is to be executed as buf‐
                                                                    fered command, otherwise
                                                                    FALSE
  DynLimits ML_iDynLi‐                                              Factors (0 ... 1) for
            mits                                                    dynamic motion limits
                                                                    (velocity, acceleration,
                                                                    deceleration, jerkAcc,
                                                                    jerkDec)
STRUCT ML_KinMotionCmdTarget
Name       Data type   Inherited          Address   Initial value   Comment
                       from

STRUCT ML_KinMotionCmdTarget
  CmdKin‐  ARRAY                                                       Commanded target posi‐
Target     [0..24] OF                                                  tion with meanings
ML_KinCmd‐
PosePair
  CmdKin‐  UINT                                                        Number of entries in
TargetSize                                                             CmdKinTarget
STRUCT ML_KinCmdPosePair
Name       Data type   Inherited            Address    Initial value   Comment
                       from
  Value    LREAL                                                       A value of the cmdKinPose
  Meaning  ML_Meaning                                                  Associated meaning of the
                                                                       value
      Attribute    ML_Attrib‐                          UNDEF           Additional attribute of the
                   utes                                                meaning
ENUM ML_Meaning
Name      Data type             Inherited   Address    Initial value   Comment
                                from
      UNDEF        INT                                 0               Error or undefined
      X            INT                                                 Absolute position of the x-
                                                                       axis
      Y            INT                                                 Absolute position of the y-
                                                                       axis
      Z            INT                                                 Absolute position of the z-
                                                                       axis
      AX1          INT                                                 Absolute position of axis 1
      AX2          INT                                                 Absolute position of axis 2
      AX3          INT                                                 Absolute position of axis 3
...
ENUM ML_MeaningAttribute
Name      Data type      Inherited          Address    Initial value   Comment
                         from
  UNDEF   INT                                          0               Error, undefined or not
                                                                       used
                   INT                                                 IC(): Incremental value
INCR_VALUE
                   INT                                                 AC(): Absolute value
ABS_VALUE
                   INT                                                 DC(): Shortest route
SHORT_WAY
                   INT                                                 ACP(): Positive direction of
POS_ROT_DI                                                             rotation
R
                   INT                                                 ACN(): Negative direction
NEG_ROT_DI                                                             of rotation
R
STRUCT ML_iDynLimits
Name        Data type           Inherited   Address    Initial value   Comment
                                from
      Velocity     LREAL                                               Velocity limit value

STRUCT ML_iDynLimits
   Accelera‐ LREAL                                                      Acceleration limit value
tion
   Decelera‐ LREAL                                                      Deceleration limit value
tion
   JerkAcc   LREAL                                      0               Jerk limit value for acceler‐
                                                    ation phase
  JerkDec    LREAL                                      0               Jerk limit value for deceler‐
                                                    ation phase
STRUCT ML_oCmdResult
Name       Data type         Inherited    Address       Initial value   Comment

         from
  CmdID      ULINT                                                      Command ID (is set to
                                                    18446744073709551615 in
                                                    the event of an error)
  Error      BOOL                                                       Error ID TRUE indicates
                                                    that an error occurred
  ErrorID    UDINT                                                      Specifies the type of
                                                    occurred error: The upper
                                                    4 bytes reflect the main
                                                    diagnostics, the lower 4
                                                    bytes reflect the detailed
                                                    diagnostics, 0 means no
                                                    error

Data Layer
/motion/kin/<kin_name>/cmd/move-direct-ex

Python
<cmdID> = motion.kin_cmd_move_direct_ex( kin=<kinName>,
kin_pose_pair=<targetPose>
 [,coord_sys=<targetCoordSys>] [,vel=<velocity>]
[,acc=<acceleration>]
 [,dec=<deceleration>] [,jrk_acc=<jerkAcceleration>]
 [,jrk_dec=<jerkDeceleration>] [,buffered=<buffered>])

Generates a MoveDirectEx command for a kinematics (object has to be
"attached"), see documentation Python Runtime App ⮫ Python Functions.
● <kinName> - string, kinematic name
● <targetPose> - Specify a target position of the command by pairing a
  meaning and a corresponding value for the coordinates to be offset.
  The pairs are collected in a dictionary data type { <meaning string>:<posi‐
  tion>, ... ,<meaning string>:<position>}.
  <position>can be a <float>, <long> or a <sub dictionary> with {<attribute
  string>:<float|long>}.
  Example:
  kin_pose_pair={ "X":3.0, "Y":2, "Z":{"INCR_VALUE":-10}, "AX5":
  {"POS_ROT_DIR":20}}
● <targetCoordSys> - string ("PCS", "WCS", "MCS" or "ACS"), coordinate
  system, in which <targetPose> is defined (coordinate system is "PCS", if
  not programmed)
● <velocity> - double, double, the velocity limitation factor of the command
  No limit, unless configured, or 0 or 1

● <acceleration> - double, the acceleration limit factor of the command. No
  limit, unless configured, or 0 or 1
● <deceleration> —double, the deceleration limit factor of the command. No
  limit, unless configured, or 0 or 1
● <jerkAcceleration> - double, factor for limiting the jerk of the command's
  acceleration. No limit, unless configured, or 0 or 1
● <jerkDeceleration> - double, factor for limiting the jerk of the command's
  deceleration. No limit, unless configured, or 0 or 1
● <buffered> - bool, use TRUE if the command is to be buffered (TRUE by
  default)

BundleIF:
Command type for a linear motion with absolute target position:

/// @brief Create a point-to-point motion command for a
kinematics in which all axes are moved synchronously and the
target position is specified by value pairs
///
/// @param[in]   sourceInfo   Command source information
/// @param[in]   kinName      Name of the motion object
/// @param[in]   targetPose   Target pose of the command
/// @param[in]   nofTargetPoseElements Number of target pose
                                         elements
/// @param[in]   targetCOS    Target coordinate system for the
                              targetPose
/// @param[in]   dynLimFactors Factors to reduce the
individual dynamic limits
/// @param[out] cmdID         The ID of the added command
/// @param[in]   buffered     is buffered mode?
/// @return                   Status of the function call:
                              STS_OK or an error code on
                              failure.

virtual MotionResult kinMoveCmdDirectEx(const
dia::CmdSourceInfo& sourceInfo, const char* kinName,
const cmd::CmdKinPosePair* targetPose, const uint32_t
nofTargetPoseElements, cmd::kin::CmdTargetCOS targetCOS, const
cmd::DynamicLimitsT& dynLimFactors, uint64_t& cmdID, bool
buffered = true) const = 0;

### 7.4.4 KinMoveDirectAsyncExx - Asynchronous point-to-point motion

Basics
This command is an extension of the commands ⮫ Chapter 7.3.8 KinMo‐
veDirectAsyncAbs - Direct asynchronous absolute traversing of kinematics
on page 538 and ⮫ Chapter 7.3.9 KinMoveDirectAsyncRel - Direct asynchro‐
nous relative traversing of kinematics on page 543.
It moves the axes of the kinematics asynchronously to the commanded abso‐
lute or relative target positions. Asynchronous means that although the axes
start their respective motions at the same time, they reach their target posi‐
tion at different times depending on the travel distance and dynamics.
The coordinate system to which the specified target position refers can be
selected as required (PCS, MCS, ACS). The target position is transformed
internally in the ACS and the interpolation is carried out separately for each
axis.

                       As the interpolation is carried out separately for all axes
        NOTICE         involved at the axis level, the result is a curved path in
                       space!
As the target position, enter the position value, the meaning and the desired
attribute for each axis/coordinate of the kinematics to be moved at ⮫ Chapter
7.4.1 Overview on page 603. Depending on the attribute, the position values
are interpreted as absolute or relative values.

PLC:

ML_KinMoveDirectAsyncEx
Name        Data type   Inherited          Address        Initial value   Comment
                        from
  Data      ML_KinMove‐                                                   InOut: Command parame‐
            DirectAsyn‐                                                   ters
            cExData
  ML_KinMo‐ BOOL                                                          Returns, whether it was
veDirectA‐                                                                possible to add the com‐
syncEx                                                                    mand to the kinematic
                                                                          object.
                                                                          ● TRUE: The ML_KinMove‐
                                                                            DirectAsyncEx command
                                                                            was added successfully
                                                                          ● FALSE: An error
                                                                            occurred. Details in
                                                                            ML_oCmdResult
STRUCT ML_KinMoveDirectAsyncExData
Name       Data type    Inherited          Address        Initial value   Comment
                        from
  In       ML_iKinMo‐                                                     Input: Command data of
           veDirectA‐                                                     the command
           syncEx
  Out      ML_oCmdRe‐                                                     Output: Command parame‐
           sult                                                           ters
STRUCT ML_iKinMoveDirectEx EXTENDS ML_iKinCmdBase
Name        Data type   Inherited   Address    Initial value              Comment
                        from
  KinName STRING(15) ML_iKinCmd‐                                          Name of the kinematics
                        Base                                              used to execute the com‐
                                                                          mand
  Source     STRING(50)      ML_iKinCmd‐                                  Specifies the command
                             Base                                         source, e.g PlcApplication1
                                                                          is displayed in the diag‐
                                                                          nostic messages

STRUCT ML_iKinMoveDirectEx EXTENDS ML_iKinCmdBase
  SourceLine ULINT      ML_iKinCmd‐                                    Specifies the source line of
Base                                           the command; is displayed
in the diagnostic messages
  CmdKin‐          ML_KinMo‐                                           Commanded absolute
Pose               tionCmd‐                                            target position with mean‐
Target                                              ings
CoordSys     STRING(15)                                          Coordinate system of the
commanded target position
(PCS, WCS, MCS or ACS
Buffered     BOOL                                TRUE            TRUE, if the command
is to be executed as buf‐
fered command, otherwise
FALSE
DynLimits ML_iDynLi‐                                             Limit values of the position
mits                                                   command
STRUCT ML_KinMotionCmdTarget
Name       Data type   Inherited            Address    Initial value   Comment
                       from
  CmdKin‐  ARRAY                                                       Commanded target posi‐
Target     [0..24] OF                                                  tion with meanings
           ML_KinCmd‐
           PosePair
  CmdKin‐  UINT                                                        Number of entries in
TargetSize                                                             CmdKinTarget
STRUCT ML_KinCmdPosePair
Name       Data type   Inherited            Address    Initial value   Comment
                       from
  Value    LREAL                                                       A value of the cmdKinPose
  Meaning  ML_Meaning                                                  Associated meaning of the
                                                                       value
      Attribute    ML_Attrib‐                          UNDEF           Additional attribute of the
                   utes                                                meaning
ENUM ML_Meaning
Name      Data type             Inherited   Address    Initial value   Comment
                                from
      UNDEF        INT                                 0               Error or undefined
      X            INT                                                 Absolute position of the x-
                                                                       axis
      Y            INT                                                 Absolute position of the y-
                                                                       axis
      Z            INT                                                 Absolute position of the z-
                                                                       axis
      AX1          INT                                                 Absolute position of axis 1
      AX2          INT                                                 Absolute position of axis 2
      AX3          INT                                                 Absolute position of axis 3
...
ENUM ML_MeaningAttribute
Name      Data type      Inherited          Address    Initial value   Comment
                         from

ENUM ML_MeaningAttribute
  UNDEF   INT                                           0               Error, undefined or not
                                                         used
INT                                                      IC(): Incremental value
INCR_VALUE
INT                                                      AC(): Absolute value
ABS_VALUE
INT                                                      DC(): Shortest route
SHORT_WAY
INT                                                      ACP(): Positive direction of
POS_ROT_DI                                                              rotation
R

INT                                                      ACN(): Negative direction
NEG_ROT_DI                                                              of rotation
R
STRUCT ML_iDynLimits
Name        Data type         Inherited    Address      Initial value   Comment
                              from
   Velocity    LREAL                                                    Velocity limit value
   Accelera‐   LREAL                                                    Acceleration limit value
tion
   Decelera‐   LREAL                                                    Deceleration limit value
tion
   JerkAcc     LREAL                                    0               Jerk limit value for acceler‐
                                                                        ation phase
  JerkDec      LREAL                                    0               Jerk limit value for deceler‐
                                                                        ation phase
STRUCT ML_oCmdResult
Name       Data type          Inherited    Address      Initial value   Comment
                              from
  CmdID        ULINT                                                    Command ID (is set to
                                                                        18446744073709551615 in
                                                                        the event of an error)
  Error        BOOL                                                     Error ID TRUE indicates
                                                                        that an error occurred
  ErrorID      UDINT                                                    Specifies the type of
                                                                        occurred error: The upper
                                                                        4 bytes reflect the main
                                                                        diagnostics, the lower 4
                                                                        bytes reflect the detailed
                                                                        diagnostics, 0 means no
                                                                        error

      Data Layer
      /motion/kin/<kin_name>/cmd/move-direct-async-ex

      Python
      <cmdID> = motion.kin_cmd_move_direct_async_ex( kin=<kinName>,
      kin_pose_pair=<targetPose>
       [,coord_sys=<targetCoordSys>] [,vel=<velocity>]

[,acc=<acceleration>]
 [,dec=<deceleration>] [,jrk_acc=<jerkAcceleration>]
 [,jrk_dec=<jerkDeceleration>] [,buffered=<buffered>])

Generates KinMoveDirectEx command for a kinematics (object has to be
"attached"), see documentation Python Runtime App ⮫ Python functions.
● <kinName> - string, kinematic name
● <targetPose> - Specify a target position of the command by pairing a
  meaning and a corresponding value for the coordinates to be offset.
  The pairs are collected in a dictionary data type { <meaning string>:<posi‐
  tion>, ... ,<meaning string>:<position>}.
  <position>can be a <float>, <long> or a <sub dictionary> with {<attribute
  string>:<float|long>}.
  Example:
  kin_pose_pair={ "X":3.0, "Y":2, "Z":{"INCR_VALUE":-10}, "AX5":
  {"POS_ROT_DIR":20}}
● <targetCoordSys> - string ("PCS", "WCS", "MCS" or "ACS"), coordinate
  system, in which <targetPose> is defined (coordinate system is "PCS", if
  not programmed)
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

/// @brief Create a point-to-point motion command for a
kinematics in which all axes are moved independently and the
target position is specified by value pairs
///
/// @param[in]   sourceInfo             Command source
                                        information
/// @param[in]   kinName                Name of the motion
                                        object
/// @param[in]   targetPose             Target pose of the
                                        command
/// @param[in]   nofTargetPoseElements Number of target
                                        pose elements
/// @param[in]   targetCOS              Target coordinate
                                        system for the
                                        targetPose
/// @param[in]   dynLim                 Dynamic limits of

                                               the command (not
                                               yet supported)
/// @param[out]     cmdID                      The ID of the added
                                               command
/// @param[in]      buffered                   is buffered mode?
/// @return                                    Status of the function
                                               call: STS_OK or an
                                               error code on
                                               failure.

virtual MotionResult kinMoveCmdDirectAsyncEx(const
dia::CmdSourceInfo& sourceInfo, const char* kinName,
const cmd::CmdKinPosePair* targetPose, const uint32_t

nofTargetPoseElements, cmd::kin::CmdTargetCOS targetCOS, const
cmd::DynamicLimitsT& dynLim, uint64_t& cmdID, bool buffered =
true) const = 0;

### 7.4.5 KinMove2DCircle - Movement on a plane-related circular/helical

path
Basics
The command interpolates a circular path
● clockwise (CW) or
● counterclockwise (CCW)
in the active working plane of the PCS to the target position commanded in
the working plane.
The command is only available for the buffered default setting.

If a new position is also commanded for the coordinate perpendicular to the
plane, which is the z-coordinate when the XY plane is active, this is also
interpolated linearly and a helical line with a constant gradient is created
geometrically. This is also referred to as helical or helical interpolation.

Commanded target positions for additional axes of the kinematics are also
interpolated linearly.
Changes to the orientation are processed using parallel SLERP interpolation
(see ⮫ Chapter Moving on a straight line - MoveLinear on page 279) if avail‐
able.
As the target position, enter the position value, the meaning and the desired
attribute for each axis/coordinate of the kinematics to be moved at ⮫ Chapter
7.4.1 Overview on page 603. Depending on the attribute, the position values
are interpreted as absolute or relative values.
                      With plane-related circular/helical interpolation, all
      NOTICE          commanded positions and additional geometric param‐
                      eters always refer to the PCS.

Geometric additional parameters (circular parameters)
The circle can be defined by specifying the
● Circle radius, or the
● circle center point
.
If the circular path is to include more than one revolution, the number of
revolutions is added to the command as a parameter.
As the target position, the circle parameters are also specified by a sequence
of value pairs, each consisting of a numerical value and an "extended
meaning”. This "extended meaning" consists of a meaning that describes
which circle parameter the numerical value refers to and an attribute with
additional information that specifies how the numerical value is to be inter‐
preted.
(<numerical value>, (<meaning>, <attribute>))
● For the circle parameters, the attribute only has an effect on the corre‐
  sponding center point parameters
● The attribute can be used to specify whether the commanded center point
  parameter should be interpreted as absolute or relative. In this context,
  relative means that the specified value refers to the starting point.
● Only those parameters whose value is unequal to 0 has to be specified.

Meaning
The meaning indicates which circle parameter the specified numerical value
refers to.
● RADIUS - circle radius: If the opening angle of the circle > is to be 180 ⁰, a
    negative radius value has to be specified
● CP_X - X-coordinate of the center of the circle
● CP_Y - Y-coordinate of the center of the circle
● CP_Z - Z-coordinate of the center of the circle
● REV - Number of complete circular rotations
With a circle, either the center or the radius is commanded. Specifying both
parameters generates a diagnostics.
The same applies if the center point coordinate outside the working plane is

commanded.
Specifying the number of circular rotations is optional.
If an exact full circle is to be commanded, no target position has to be speci‐
fied. It is sufficient to specify the center of the circle. In this case, specifying
the circular rotation (REV=1) is optional and yields the same result.

Attribute
The attribute only influences the interpretation of the center point parameters.
● UNDEF - Default attribute (center point parameter is interpreted as a rela‐
  tive value)
● INCR_VALUE - Center point parameter is interpreted incrementally
● ABS_VALUE - Center point parameter is interpreted as absolute

Circles with radius programming
For a circle with radius programming, the radius has to be specified in addi‐
tion to the target position. Make sure that the radius value is at least half
as large as the distance between the start and endpoints in relation to the
circular plane.
If the opening angle of the circle > is to be 180 ⁰, the radius has to have a
negative sign.
With an exact semicircle, the sign of the radius is arbitrary.

Circles with center point programming
For a circle with radius programming, the coordinates of the center point have
to be specified in addition to the target position.
Only those coordinates that deviate from the starting position need to be
commanded. The coordinates of the center point are interpreted relative to
the starting point by default. However, an attribute can also be used to
specify an absolute value.

PLC:

ML_KinMoveCircleCw2D
Name       Data type        Inherited   Address       Initial value   Comment
                            from
  Data       ML_KinMove‐                                              InOut: Command parame‐
             CircleData2D                                             ters

   ML_KinMo‐ BOOL                                                     Returns, whether it was
veCir‐                                                                possible to add the com‐
cleCw2D                                                               mand to the kinematic
                                              object.
                                              ● TRUE: The ML_KinMove‐
                                                CircleCw2D command
                                                was added successfully
                                              ● FALSE: An error
                                                occurred. Details in
                                                ML_oCmdResult
ML_KinMoveCircleCcw2D
Name       Data type        Inherited   Address       Initial value   Comment
                            from
  Data       ML_KinMove‐                                              InOut: Command parame‐
             CircleData2D                                             ters
   ML_KinMo‐ BOOL                                                     Returns, whether it was
veCir‐                                                                possible to add the com‐
cleCcw2D                                                              mand to the kinematic
                                                                      object.
                                                                      ● TRUE: The ML_KinMove‐
                                                                        CircleCcw2D command
                                                                        was added successfully
                                                                      ● FALSE: An error
                                                                        occurred. Details in
                                                                        ML_oCmdResult
STRUCT ML_KinMoveCircleData2D
Name       Data type    Inherited       Address       Initial value   Comment
                        from
  In       ML_iKinCmd‐                                                Input: Command data of
           Circle                                                     the command
  Out      ML_oCmdRe‐                                                 Output: Command parame‐
           sult                                                       ters
STRUCT ML_iKinCmdCircle EXTENDS ML_iKinCmdBase
Name        Data type   Inherited   Address    Initial value          Comment
                        from
  KinName STRING(15) ML_iKinCmd‐                                      Name of the kinematics
                        Base                                          used to execute the com‐
                                                                      mand

STRUCT ML_iKinCmdCircle EXTENDS ML_iKinCmdBase
  Source    STRING(50) ML_iKinCmd‐                                      Specifies the command
Base                                            source, e.g PlcApplication1
is displayed in the diag‐
nostic messages
SourceLine ULINT          ML_iKinCmd‐                             Specifies the source line of
Base                                    the command; is displayed
in the diagnostic messages
  CmdKin‐    ML_KinMo‐                                                  Commanded absolute
Pose         tionCmd‐                                                   target position with mean‐
Target                                                     ings
  CmdCircle‐ ML_KinMo‐                                                  Commanded circle data
Data         tionCmd‐
Circle
  DynLimits ML_iDynLi‐                                                  Limit values of the position
mits                                                       command
STRUCT ML_KinMotionCmdTarget
Name       Data type   Inherited              Address   Initial value   Comment
                       from
  CmdKin‐  ARRAY                                                        Commanded target posi‐
Target     [0..24] OF                                                   tion with meanings
           ML_KinCmd‐
           PosePair
  CmdKin‐  UINT                                                         Number of entries in
TargetSize                                                              CmdKinTarget
STRUCT ML_KinCmdPosePair
Name       Data type   Inherited              Address   Initial value   Comment
                       from
  Value    LREAL                                                        A value of the cmdKinPose
  Meaning  ML_Meaning                                                   Associated meaning of the
                                                                        value
      Attribute    ML_Attrib‐                           UNDEF           Additional attribute of the
                   utes                                                 meaning
ENUM ML_Meaning
Name      Data type             Inherited     Address   Initial value   Comment
                                from
      UNDEF        INT                                  0               Error or undefined
      X            INT                                                  Absolute position of the x-
                                                                        axis
      Y            INT                                                  Absolute position of the y-
                                                                        axis
      Z            INT                                                  Absolute position of the z-
                                                                        axis
      AX1          INT                                                  Absolute position of axis 1
      AX2          INT                                                  Absolute position of axis 2
      AX3          INT                                                  Absolute position of axis 3
...
ENUM ML_MeaningAttribute
Name      Data type      Inherited            Address   Initial value   Comment
                         from

ENUM ML_MeaningAttribute
  UNDEF   INT                                        0               Error, undefined or not
used
INT                                                     IC(): Incremental value
INCR_VALUE
INT                                                     AC(): Absolute value
ABS_VALUE
INT                                                     DC(): Shortest route
SHORT_WAY
INT                                                     ACP(): Positive direction of
POS_ROT_DI                                                           rotation
R

INT                                                     ACN(): Negative direction
NEG_ROT_DI                                                           of rotation
R
STRUCT ML_KinMotionCmdCircle
Name       Data type    Inherited       Address      Initial value   Comment
                        from
  CmdKin‐  ARRAY [0..7]                                              Commanded circle data
CircleData OF                                                        with circle meaning
           ML_KinCmd‐
           CircleData‐
           Pair
           INT                                       0               Number of entries in
INCR_VALUE                                                           CmdKinCircle
STRUCT ML_KinCmdCircleDataPair
Name        Data type  Inherited        Address      Initial value   Comment
                       from
  Value     LREAL                                                    A value of the circle data
  Meaning   ML_Circle‐                                               Associated meaning of the
            Meaning                                                  value
  Attribute ML_Meanin‐                               UNDEF           Additional attribute of the
            gAttribute                                               meaning
ENUM ML_CircleMeaning
Name       Data type        Inherited   Address      Initial value   Comment
                            from
  RADIUS     INT                                     0               Radius of a circle com‐
                                                                     mand
  CP_X       INT                                                     Center of the circle X-axis
  CP_ Y      INT                                                     Center of the circle Y-axis
  CP_ Z      INT                                                     Center of the circle Z-axis
  IP_X       INT                                                     Intermediate point of the
                                                                     circle X-axis
  IP_Y       INT                                                     Intermediate point of the
                                                                     circle Y-axis
  IP_Z       INT                                                     Intermediate point of the
                                                                     circle Z-axis
  REV        INT                                                     Circular rotations

STRUCT ML_iDynLimits
Name        Data type           Inherited   Address     Initial value   Comment
                                from
   Velocity        LREAL                                                Velocity limit value
   Accelera‐       LREAL                                                Acceleration limit value
tion
   Decelera‐       LREAL                                                Deceleration limit value
tion
   JerkAcc         LREAL                                0               Jerk limit value for acceler‐
                                                                        ation phase
   JerkDec         LREAL                                0               Jerk limit value for deceler‐
                                                                        ation phase
STRUCT ML_oCmdResult
Name       Data type            Inherited   Address     Initial value   Comment
                                from
   CmdID           ULINT                                                Command ID (is set to
                                                                        18446744073709551615 in
                                                                        the event of an error)
   Error           BOOL                                                 Error ID TRUE indicates
                                                                        that an error occurred
   ErrorID         UDINT                                                Specifies the type of
                                                                        occurred error: The upper
                                                                        4 bytes reflect the main
                                                                        diagnostics, the lower 4
                                                                        bytes reflect the detailed
                                                                        diagnostics, 0 means no
                                                                        error

Data Layer
/motion/kin/<kin_name>/cmd/circle2d-cw
/motion/kin/<kin_name>/cmd/circle2d-ccw

Python

<cmdID> = motion.kin_cmd_move_2D_circle_cw( kin=<kinName>
 [,kin_pose_pair=<targetPose>], circle_data_pair=<circleData>,
[,vel=<velocity>]
 [,acc=<acceleration>] [,dec=<deceleration>]
[,jrk_acc=<jerkAcceleration>]
 [,jrk_dec=<jerkDeceleration>] )

<cmdID> = motion.kin_cmd_move_2D_circle_ccw( kin=<kinName>
 [,kin_pose_pair=<targetPose>], circle_data_pair=<circleData>,
[,vel=<velocity>]
 [,acc=<acceleration>] [,dec=<deceleration>]
[,jrk_acc=<jerkAcceleration>]
 [,jrk_dec=<jerkDeceleration>] )
Example:
motion.kin_cmd_move_2D_circle_cw("Robot", {"X":40.0,
"Y":-100.0, "Z":42.0},
 {"IP_X":20.0, "IP_Y":-100.0, "IP_Z":15.5}, vel=0, acc=1.5,
dec=1.7)

Python

Creates a KinMove2DCircle command (cw or ccw) for a kinematic with a
target position as a tuple of coordinate meanings and position values (with
optional attributes) and circle parameters, also as a tuple of parameter mean‐
ings and values (with optional attributes). (Object has to be "attached”), see
documentation Python Runtime App ⮫ Python Functions
● <kinName> - string, kinematic name
● <targetPose> - Specify a target position of the command by pairing a
  meaning and a corresponding value for the coordinates to be offset.
  The pairs are collected in a dictionary data type { <meaning string>:<posi‐
  tion>, ... ,<meaning string>:<position>}.

  <position>can be a <float>, <long> or a <sub dictionary> with {<attribute
  string>:<float|long>}.
  Example:
  circle_data_pair={ "CP_X":7.3, "CP_Y":{"ABS__VALUE":-2.7}, "REV":2}
● <velocity> - double, velocity limit value of the command (the last pro‐
  grammed velocity limit value is used if this parameter is not programmed)
● <acceleration> - double, acceleration limit value of the command (the last
  programmed acceleration limit value is used if this parameter is not pro‐
  grammed)
● <deceleration> - double, acceleration limit value of the command (the last
  programmed acceleration limit value is used if this parameter is not pro‐
  grammed)
● <jerkAcceleration> - double, jerk limit value for the acceleration of the com‐
  mand (the last programmed jerk limit value for the acceleration is used if
  this parameter is not programmed)
● <jerkDeceleration> - double, jerk limit value for the deceleration of the
  command (the last programmed jerk limit value for the deceleration is used
  if this parameter is not programmed)

/// @brief Create a command for 2D circular interpolation
    in the active plane
///
/// @param[in]   handle             Handle of the interface
/// @param[in]   sourceInfo         Command source
                                    information
/// @param[in]   kinName            Name of the motion
                                    object
/// @param[in]   cmdType            clockwise or
                                    counter-clockwise
/// @param[in]   targetKinPosePair Target position of the
                                    command with meanings
/// @param[in]   sizeKinPose        Size of the
                                    targetKinPosePair
                                    array
/// @param[in]   circleDataPair     Circle data of the
                                    command with circle
                                    meanings
/// @param[in]   sizeCircleData     Size of the
                                    targetCircleDataPair
                                    array
/// @param[in]   dynLim             Factors to reduce the
                                    individual dynamic
                                    limits
/// @param[out] cmdID               The ID of the added

                                            command
/// @return                                 Status of the function
                                            call: STS_OK or an
                                            error code on
                                            failure.

Virtual MotionResult(*kinMove2DCircleCmd)(void* handle,
const dia::CmdSourceInfo& sourceInfo, const char*
kinName, cmd::kin::KinCmdType cmdType, const
cmd::CmdKinPosePair* targetKinPosePair, uint32_t sizeKinPose,
const cmd::CmdCircleDataPair* circleDataPair, uint32_t
sizeCircleData, const cmd::DynamicLimitsT& dynLim, uint64_t&
cmdID) const = 0;

### 7.4.6 KinMove3DCircle - Moving on a circular path in space

Basics
The command interpolates a circular path via an intermediate point (IP) in
space to the commanded target position. It is only available as a buffered
command.
It is not possible to command a full circle using intermediate point program‐
ming.

Commanded target positions for additional axes of the kinematics are also
interpolated linearly.
Changes to the orientation are processed using parallel SLERP interpolation
(see ⮫ Chapter Moving on a straight line - MoveLinear on page 279) if avail‐
able.
As the target position, enter the position value, the meaning and the desired
attribute for each axis/coordinate of the kinematics to be moved at ⮫ Chapter
7.4.1 Overview on page 603. Depending on the attribute, the position values
are interpreted as absolute or relative values.

Geometric additional parameters (circular parameters)
The circle is defined by specifying the intermediate point.
As the target position, the circle parameters are also specified by a sequence
of value pairs, each consisting of a numerical value and an "extended
meaning", consisting of a meaning that describes which circle parameter the
numerical value refers to and an attribute with additional information that
specifies how the numerical value is to be interpreted.
(<numerical value>, (<meaning>, <attribute>))

● For the circle parameters, the attribute only has an effect on the corre‐
  sponding center point parameters
● The attribute can be used to specify whether the commanded center point
  parameter should be interpreted as absolute or relative. In this context,
  relative means that the specified value refers to the starting point.
● Only those parameters whose value is unequal to 0 has to be specified.

Meaning
The meaning indicates which circle parameter the specified numerical value
refers to.
● IP_X - X-coordinate of the intermediate point on the circular path
● IP_Y - Y-coordinate of the intermediate point on the circular path

● IP_Z - Z-coordinate of the intermediate point on the circular path

Attribute
The attribute only influences the interpretation of the intermediate point
parameters.
● UNDEF - Default attribute (intermediate point parameter is interpreted as
  an absolute value)
● INCR_VALUE - Intermediate point parameter is interpreted incrementally
● ABS_VALUE - Intermediate point parameter is interpreted as absolute

PLC:

ML_KinMoveCircle3D
Name       Data type        Inherited     Address       Initial value   Comment
                            from
  Data      ML_KinMove‐                                                 InOut: Command parame‐
            CircleData3D                                                ters
  ML_KinMo‐ BOOL                                                        Returns, whether it was
veCircle3D                                                              possible to add the com‐
                                                                        mand to the kinematic
                                                                        object.
                                                                        ● TRUE: The ML_KinMove‐
                                                                          Circle3D command was
                                                                          added successfully
                                                                        ● FALSE: An error
                                                                          occurred. Details in
                                                                          ML_oCmdResult
STRUCT ML_KinMoveCircleData3D
Name       Data type    Inherited         Address       Initial value   Comment
                        from
  In       ML_iKinCmd‐                                                  Input: Command data of
           Circle3D                                                     the command
  Out      ML_oCmdRe‐                                                   Output: Command parame‐
           sult                                                         ters

STRUCT ML_iKinCmdCircle3D EXTENDS ML_iKinCmdBase
Name        Data type   Inherited  Address     Initial value            Comment
                        from
  KinName STRING(15) ML_iKinCmd‐                                        Name of the kinematics
                        Base                                            used to execute the com‐
                                                                        mand
   Source          STRING(50)   ML_iKinCmd‐                             Specifies the command
                                Base                                    source, e.g PlcApplication1
                                                                        is displayed in the diag‐
                                                                        nostic messages
   SourceLine ULINT             ML_iKinCmd‐                             Specifies the source line of
                                Base                                    the command; is displayed
                                                                        in the diagnostic messages
  CmdKin‐     ML_KinMo‐         ML_iKinCmd‐                             Commanded absolute
Pose          tionCmd‐          Circle                                  target position with mean‐
              Target                                                    ings
   CmdCircle‐ ML_KinMo‐         ML_iKinCmd‐                             Commanded circle data
Data          tionCmd‐          Circle
              Circle
   DynLimits ML_iDynLi‐         ML_iKinCmd‐                             Limit values of the position
              mits              Circle                                  command
CoordSys      ML_CoordSy                                                Coordinate system of the
              s                                                         commanded target position
AllowInv‐     BOOL                                      FALSE           Allow invalid meanings
Meaning
STRUCT ML_KinMotionCmdTarget
Name       Data type   Inherited              Address   Initial value   Comment
                       from
  CmdKin‐  ARRAY                                                        Commanded target posi‐
Target     [0..24] OF                                                   tion with meanings
           ML_KinCmd‐
           PosePair
  CmdKin‐  UINT                                                         Number of entries in
TargetSize                                                              CmdKinTarget
STRUCT ML_KinCmdPosePair
Name       Data type   Inherited              Address   Initial value   Comment
                       from
  Value    LREAL                                                        A value of the cmdKinPose
  Meaning  ML_Meaning                                                   Associated meaning of the
                                                                        value
   Attribute       ML_Attrib‐                           UNDEF           Additional attribute of the
                   utes                                                 meaning
ENUM ML_Meaning
Name      Data type             Inherited     Address   Initial value   Comment
                                from
   UNDEF           INT                                  0               Error or undefined
   X               INT                                                  Absolute position of the x-
                                                                        axis
   Y               INT                                                  Absolute position of the y-
                                                                        axis

ENUM ML_Meaning
  Z       INT                                                            Absolute position of the z-
                                                        axis
AX1        INT                                                     Absolute position of axis 1
AX2        INT                                                     Absolute position of axis 2
AX3        INT                                                     Absolute position of axis 3
...
ENUM ML_MeaningAttribute
Name      Data type      Inherited          Address      Initial value   Comment
                         from
  UNDEF   INT                                            0               Error, undefined or not

                                                        used
INT                                                     IC(): Incremental value
INCR_VALUE
INT                                                     AC(): Absolute value
ABS_VALUE
INT                                                     DC(): Shortest route
SHORT_WAY
INT                                                     ACP(): Positive direction of
POS_ROT_DI                                                               rotation
R
INT                                                     ACN(): Negative direction
NEG_ROT_DI                                                               of rotation
R
STRUCT ML_KinMotionCmdCircle
Name       Data type    Inherited           Address      Initial value   Comment
                        from
  CmdKin‐  ARRAY [0..7]                                                  Commanded circle data
CircleData OF                                                            with circle meaning
           ML_KinCmd‐
           CircleData‐
           Pair
           INT                                           0               Number of entries in
INCR_VALUE                                                               CmdKinCircle
STRUCT ML_KinCmdCircleDataPair
Name        Data type  Inherited            Address      Initial value   Comment
                       from
  Value     LREAL                                                        A value of the circle data
  Meaning   ML_Circle‐                                                   Associated meaning of the
            Meaning                                                      value
  Attribute ML_Meanin‐                                   UNDEF           Additional attribute of the
            gAttribute                                                   meaning
ENUM ML_CircleMeaning
Name       Data type            Inherited   Address      Initial value   Comment
                                from
      IP_X       INT                                                     Intermediate point of the
                                                                         circle X-axis
      IP_Y       INT                                                     Intermediate point of the
                                                                         circle Y-axis

ENUM ML_CircleMeaning
  IP_Z     INT                                                            Intermediate point of the
                                                 circle Z-axis
ENUM ML_CoordSys
Name      Data type               Inherited   Address     Initial value   Comment
                                  from
   UNDEF           INT                                    0               Error or undefined
   PCS             INT                                                    Target coordinate system is
                                                                          product coordinate system
   WCS             INT                                                    Target coordinate system is
                                                                          world coordinate system
   MCS             INT                                                    Target coordinate system is
                                                                          machine coordinate system
   ACS             INT                                                    Target coordinate system is
                                                                          axis coordinate system
STRUCT ML_iDynLimits
Name        Data type             Inherited   Address     Initial value   Comment
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
Name       Data type              Inherited   Address     Initial value   Comment
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

Data Layer
/motion/kin/<kin_name>/cmd/move-3D-circle

Python

<cmdID> = motion.kin_cmd_move_3D_circle ( kin=<kinName>
 [,kin_pose_pair=<targetPose>], circle_data_pair=<circleData>,
[,vel=<velocity>]

 [,acc=<acceleration>] [,dec=<deceleration>]
[,jrk_acc=<jerkAcceleration>]
 [,jrk_dec=<jerkDeceleration>] )
Example:
motion.kin_cmd_move_3D_circle("Robot", {"X":40.0, "Y":-100.0,
"Z":42.0},
{"IP_X":20.0, "IP_Y":-100.0, "IP_Z":15.5}, vel=0, acc=1.5,
dec=1.7)

Creates a KinMove3DCircle command for a kinematic with a target position as
a tuple of coordinate meanings and position values (with optional attributes)
and circle parameters, also as a tuple of parameter meanings and values (with
optional attributes). (Object has to be "attached”), see documentation Python

Runtime App ⮫ Python Functions
● <kinName> - string, kinematic name
● <targetPose> - Specify a target position of the command by pairing a
  meaning and a corresponding value for the coordinates to be offset.
  The pairs are collected in a dictionary data type { <meaning string>:<posi‐
  tion>, ... ,<meaning string>:<position>}.
  <position>can be a <float>, <long> or a <sub dictionary> with {<attribute
  string>:<float|long>}.
  Example:
  circle_data_pair={ "CP_X":7.3, "CP_Y":{"ABS__VALUE":-2.7}, "REV":2}
● <velocity> - double, velocity limit value of the command (the last pro‐
  grammed velocity limit value is used if this parameter is not programmed)
● <acceleration> - double, acceleration limit value of the command (the last
  programmed acceleration limit value is used if this parameter is not pro‐
  grammed)
● <deceleration> - double, acceleration limit value of the command (the last
  programmed acceleration limit value is used if this parameter is not pro‐
  grammed)
● <jerkAcceleration> - double, jerk limit value for the acceleration of the com‐
  mand (the last programmed jerk limit value for the acceleration is used if
  this parameter is not programmed)
● <jerkDeceleration> - double, jerk limit value for the deceleration of the
  command (the last programmed jerk limit value for the deceleration is used
  if this parameter is not programmed)

BundleIF:

/// @brief Create a circular 3D motion command for a kinematics
///
/// @param[in]    handle               Handle of the interface
/// @param[in]    sourceInfo           Command source
information
/// @param[in]    kinName              Name of the motion
object
/// @param[in]    targetKinPosePair    Target position of the
                                       command with meanings
/// @param[in]    sizeKinPose          Size of the
targetKinPosePair
                                       array
/// @param[in]    targetCircleDataPair Circle data of the
command with
                                       circle meanings
/// @param[in]    sizeCircleData       Size of the

targetCircleDataPair
                                               array
/// @param[in]        targetCOS                Target coordinate
system for the
                                               targetPos
/// @param[in]        dynLimFactors            Factors to reduce the
individual
                                               dynamic limits
/// @param[in]        allowInvMeaning          Allow the commanding of
invalid
                                               meanings, default is
false
/// @param[out]       cmdID                    The ID of the added
command
/// @return                                    Status of the function
call:
                                               STS_OK or an error code
on
                                               failure.

Virtual MotionResult(*kinMove3DCircleCmd)(void* handle, const
dia::CmdSourceInfo& sourceInfo, const char* kinName,
const cmd::CmdKinPosePair* targetKinPosePair, uint32_t
sizeKinPose, const:CmdCircleDataPair* circleDataPair, uint32_t
sizeCircleData, cmd::kin::CmdTargetCOS targetCOS, const
cmd::DynamicLimitsT& dynLim, uint64_t& cmdID);

### 7.4.7 KinMoveToPointLin - Moving the kinematics linearly to a saved

point
Basics
This command moves the kinematics linearly from the current position to a
stored, specific point. The possible coordinate system is already contained
in the saved point (see ⮫ Chapter Points management on page 280) as a
reference system.
For more information on the motion type and the other parameters of the
command, please refer to ⮫ Chapter 7.4.2 KinMoveLinEx - Moving on a straight
line in space on page 605.
In particular, the dynamic motion limit values can be configured as described
in ⮫ Chapter 7.4.2 KinMoveLinEx - Moving on a straight line in space
on page 605.

PLC:

ML_KinMoveToPointLin
Name        Data type            Inherited    Address     Initial value   Comment
                                 from
   Data            ML_KinMove‐                                            InOut: Command parame‐
                   ToPointData                                            ters

ML_KinMoveToPointLin
  ML_KinMo‐ BOOL                                                      Returns, whether it was
veToPointLin                                                          possible to add the com‐
mand to the kinematic
object.
● TRUE: The ML_KinMo‐
  veToPointLin command
  was added successfully
● FALSE: An error
  occurred. Details in
  ML_oCmdResult
STRUCT ML_KinMoveToPointData

Name       Data type   Inherited           Address    Initial value   Comment
                       from
  In       ML_iKinMo‐                                                 Input: Command data of
           veToPoint                                                  the command
  Out      ML_oCmdRe‐                                                 Output: Command parame‐
           sult                                                       ters
STRUCT ML_iKinMoveToPointLin EXTENDS ML_iKinCmdBase
Name        Data type   Inherited   Address     Initial value         Comment
                        from
  KinName STRING(63) ML_iKinCmd‐                                      Name of the kinematics
                        Base                                          used to execute the com‐
                                                                      mand
  Source       STRING(50)    ML_iKinCmd‐                              Specifies the command
                             Base                                     source, e.g PlcApplication1
                                                                      is displayed in the diag‐
                                                                      nostic messages
  SourceLine ULINT           ML_iKinCmd‐                              Specifies the source line of
                             Base                                     the command; is displayed
                                                                      in the diagnostic messages
  Target‐      STRING(50)                                             Name of the target point
Point                                                                 (teach point)
  Buffered     BOOL                                   TRUE            TRUE, if the command
                                                                      is to be executed as buf‐
                                                                      fered command, otherwise
                                                                      FALSE
  DynLimits ML_iDynLi‐                                                Limit values of the position
            mits                                                      command
STRUCT ML_iDynLimits
Name        Data type        Inherited     Address    Initial value   Comment
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
Name       Data type            Inherited    Address      Initial value   Comment
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

Data Layer
Method: POST
/motion/kin/<kin_name>/cmd/move-to-point-lin
Payload:
{
    "type":"object" , "value":
    {
        "pointName":"Test",
        "lim":{
            “vel":800,
            “acc":3,
            "dec":3,
            "jrkAcc":0,
            "jrkDec":0
        },
        "buffered":true
    }
}

Python
<cmdID> = motion.kin_cmd_move_to_point_lin( kin=<kinName>,
target_point=<targetPoint>
 [,vel=<velocity>] [,acc=<acceleration>] [,dec=<deceleration>]
 [,jrk_acc=<jerkAcceleration>] [,jrk_dec=<jerkDeceleration>]
[,buffered=<buffered>])

Creates a MoveToPointLin command that interpolates the motion on a line to
the specified target point for a kinematic (object has to be "attached"), see
documentation Python Runtime App ⮫ Python Functions.
● <kinName> - string, kinematic name
● <targetPoint> - string, name of the target point (teach point)
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

### 7.4.8 KinMoveToPointDirect - Moving the kinematics directly to a saved

point
Basics
This command moves the kinematics linearly from the current position to
a stored, specific point at which the path of the actuator is not relevant.
The possible coordinate system is already contained in the saved point (see
⮫ Chapter Points management on page 280) as a reference system.
For more information on the motion type and the other parameters of the
command, please refer to ⮫ Chapter 7.4.3 KinMoveDirectEx - Point-to-point
motion at axis level on page 609.
In particular, the dynamic motion limit values can be configured as described
in ⮫ Chapter 7.4.3 KinMoveDirectEx - Point-to-point motion at axis level
on page 609.

PLC:

ML_KinMoveDirect
Name       Data type         Inherited    Address        Initial value   Comment
                             from
 Data       ML_KinMove‐                                                  InOut: Command parame‐
            ToPointData                                                  ters
  ML_KinMo‐ BOOL                                                         Returns, whether it was
veToPoint‐                                                               possible to add the com‐
Direct                                                                   mand to the kinematic
                                                                         object.
                                                                         ● TRUE: The ML_KinMove‐
                                                                           ToPointDirect command
                                                                           was added successfully
                                                                         ● FALSE: An error
                                                                           occurred. Details in
                                                                           ML_oCmdResult

STRUCT ML_KinMoveToPointData
Name       Data type   Inherited              Address   Initial value   Comment
                       from
  In       ML_iKinMo‐                                                   Input: Command data of
           veToPoint                                                    the command
  Out      ML_oCmdRe‐                                                   Output: Command parame‐
           sult                                                         ters
STRUCT ML_iKinMoveToPointDirect EXTENDS ML_iKinCmdBase
Name        Data type   Inherited    Address     Initial value          Comment
                        from
  KinName STRING(63) ML_iKinCmd‐                                        Name of the kinematics
                        Base                                            used to execute the com‐
                                                                        mand
   Source          STRING(50)   ML_iKinCmd‐                             Specifies the command
                                Base                                    source, e.g PlcApplication1
                                                                        is displayed in the diag‐
                                                                        nostic messages
   SourceLine ULINT             ML_iKinCmd‐                             Specifies the source line of
                                Base                                    the command; is displayed
                                                                        in the diagnostic messages
  Target‐          STRING(50)                                           Name of the target point
Point                                                                   (teach point)
  Buffered         BOOL                                 TRUE            TRUE, if the command
                                                                        is to be executed as buf‐
                                                                        fered command, otherwise
                                                                        FALSE
   DynLimits ML_iDynLi‐                                                 Factors (0 ... 1) for
             mits                                                       dynamic motion limits
                                                                        (velocity, acceleration,
                                                                        deceleration, jerkAcc,
                                                                        jerkDec)
STRUCT ML_iDynLimits
Name        Data type           Inherited     Address   Initial value   Comment
                                from
   Velocity        LREAL                                                Velocity limit value
   Accelera‐       LREAL                                                Acceleration limit value
tion
   Decelera‐       LREAL                                                Deceleration limit value
tion
   JerkAcc         LREAL                                0               Jerk limit value for acceler‐
                                                                        ation phase
   JerkDec         LREAL                                0               Jerk limit value for deceler‐
                                                                        ation phase
STRUCT ML_oCmdResult
Name       Data type            Inherited     Address   Initial value   Comment
                                from
   CmdID           ULINT                                                Command ID (is set to
                                                                        18446744073709551615 in
                                                                        the event of an error)
   Error           BOOL                                                 Error ID TRUE indicates
                                                                        that an error occurred

STRUCT ML_oCmdResult
  ErrorID  UDINT                                                       Specifies the type of
                                                   occurred error: The upper
                                                   4 bytes reflect the main
                                                   diagnostics, the lower 4
                                                   bytes reflect the detailed
                                                   diagnostics, 0 means no
                                                   error

Data Layer
Method: POST
/motion/kin/<kin_name>/cmd/move-to-point-direct

Payload:
{
        "type":"object" , "value":
        {
            "pointName":"Test",
            "lim":{
                “vel":800,
                “acc":3,
                "dec":3,
                "jrkAcc":0,
                "jrkDec":0
            },
            "buffered":true
        }
}

Python
<cmdID> = motion.kin_cmd_move_to_point_direct( kin=<kinName>,
target_point=<targetPoint>
 [,vel=<velocity>] [,acc=<acceleration>] [,dec=<deceleration>]
 [,jrk_acc=<jerkAcceleration>] [,jrk_dec=<jerkDeceleration>]
[,buffered=<buffered>])

Creates a MoveToPointDirect command that moves to a specified target point
for a kinematic and does not follow a given path (object has to be "attached"),
see documentation Python Runtime App ⮫ Python Functions.
● <kinName> - string, kinematic name
● <targetPoint> - string, name of the target point (teach point)
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
