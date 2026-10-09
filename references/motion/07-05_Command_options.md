# 7.5 Command options

### 7.5.1 Overview

Command options are only available for buffered commands.

A command option is a feature for commands. Using this option, properties
and behavior of commands are extended. Command options have parameters
and are issued like regular commands via the same interfaces. Available for
axis and kinematics.
There are the following command options types, differing in their validity:
● Permanent: This type can be enabled and disabled. It applies to all com‐
   mands issued during enabling and disabling
● Once: This type only applies to the next command. If this type is issued, it
   cannot be canceled
Command options can be overwritten by issuing the command option again
using other parameters.
Command options of type "Once" have a higher priority than the options of
type "Permanent". If a command is within the validity range of both types,
only the type "Once" applies to the commands.
Command options are only added to relevant commands.

Validity in the Data Layer interface
In the Data Layer interfaces of the command options, the validity is specified
by a string. The following behavior is implemented for all command options:
● "Once" or empty string ("") means validity "Once"
● "PermOn" or if the "permType" element in the request is omitted altogether,
    means "Permanently turn on” validity
● All other strings mean "Switch off permanently” validity
Please note that not all variants of validity are supported by all command
options. For example, there is no "Once" variant for the "Machine coordinate
system" command option, as it is extremely untypical (and thus tends to
result in errors) to activate the coordinate system only for a single command.
If an unsupported variant of the validity of a command option is commanded,
the ctrlX MOTION generates a runtime error and the commanded kinematics
goes into an error state.

### 7.5.2 KinBlend, KinBlendP - Blending/permanent kinematic option

Basics
Naming: Blending means that two or more commands can be executed simul‐
taneously. The superimposition of commands is also referred to as “Block‐
Slope”.
The use case of blending is blending of individual motions. If a motion in
Y follows a motion in X, blending results in a continuous motion, whereas
motion 2 starts before motion 1 has been completed.

Compliance with the dynamic axis limit values is not ensured on the blended
contour. For example, if two commands are blended in the same direction,
the limit value can be exceeded by a maximum of double the value.
If blending is enabled, sporadically more than one command is active in a
Motion object. This command returns the state ACTIVE.

Parameter description
D1: Distance to the end position of the first motion command (corner E1/S2)
until blending can start.
D2: Distance after the starting position of the second motion command
(corner E1/S2) in which the motion has to be retraced to the path (end of
blending).

During blending using “BlockSlope”, it is not possible to define a path devia‐
tion as the path has not previously been defined.
If D1 or D2 are set to very high values (e.g. D1 > S1), the entire path of
both commands can be blended (D1 and D2 are limited to the maximum path
length).
D1 and D2 are limits up to which the motion can leave the path defined by
both motion commands. The resulting motion is time-optimized.
Table 68: Sequence example:
Commands/command          Blending
option
Blend_1 (permanent on)
Move_1                    Blend_1
Blend_2 (once)
Move_2                                              Blend_2
Move_3                    Blend_1
Move_4
Blend (off)
Blend_3 (permanent on)
Move_5                    Blend_3
Blend_4 (permanent on)
Move_6                                              Blend_4

Commands/command           Blending
option
Move_7
Blend (off)

Restrictions
As a matter of principle, the command options “Blending” and “PolyTrans”
rule each other out. An error is generated if both are simultaneously enabled
for the same kinematics.
When using blending with an axis transformation that is not linear (not a
simple Cartesian XYZ kinematics) and when commanding the superimposed
motion with high dynamic limits (so that these limits have to be reduced to
ensure the axis limits), the D2 distance can be exceeded by a small amount.
The size of the exceedance is deterministic (it is always the same for a given
set of dynamic limits and overrides). The D1 distance is never exceeded.

PLC:
Blending only possible with the next command:

ML_KinBlend
Name        Data type           Inherited       Address       Initial value   Comment
                                from
   Data            ML_Kin‐                                                    InOut: Parameter of the
                   BlendData                                                  command option
  ML_Kin‐          BOOL                                                       Returns, whether it was
Blend                                                                         possible to add the com‐
                                                                              mand option to the kine‐
                                                                              matic object.
                                                                              ● TRUE: The command
                                                                                option was added suc‐
                                                                                cessfully
                                                                              ● FALSE: An error
                                                                                occurred. Details in
                                                                                ML_oCmdResult
STRUCT ML_KinBlendData
Name       Data type   Inherited                Address       Initial value   Comment
                       from
  In       ML_iKin‐                                                           Input: Command data of
           Blend                                                              the command option
  Out      ML_oCm‐                                                            Output: Parameter of the
           dOptResult                                                         command option
STRUCT ML_iKinBlend EXTENDS ML_iKinCmdBase
Name        Data type   Inherited   Address                   Initial value   Comment
                        from
  KinName STRING(15) ML_iKinCmd‐                                              Name of the kinematics
                        Base                                                  used to execute the com‐
                                                                              mand option

STRUCT ML_iKinBlend EXTENDS ML_iKinCmdBase
  Source    STRING(50) ML_iKinCmd‐                                  Returns the command
Base                                        option source, e.g. PlcAp‐
plication1 is displayed in
the diagnostic messages
  SourceLine ULINT          ML_iKinCmd‐                             Specifies the source line of
Base                                    the command; is displayed
in the diagnostic messages
  D1         LREAL                                                  Distance to end position of
the first motion command
at which blending starts
  D2         LREAL                                                  Distance between the

starting position of the
second motion command
and the end position of
blending
STRUCT ML_oCmdOptResult
Name       Data type  Inherited           Address   Initial value   Comment
                      from
  Error    BOOL                                                     Error ID TRUE indicates
                                                                    that an error occurred
  ErrorID    UDINT                                                  Specifies the type of
                                                                    occurred error: The upper
                                                                    4 bits reflect the main diag‐
                                                                    nostics, the lower 4 bytes
                                                                    reflect the detailed diag‐
                                                                    nostics, 0 means no error

Permanent blending:

ML_KinBlendP
Name        Data type       Inherited     Address   Initial value   Comment
                            from
  Data       ML_Kin‐                                                InOut: Parameter of the
             BlendPData                                             command option
  ML_Kin‐    BOOL                                                   Returns, whether it was
BlendP                                                              possible to add the com‐
                                                                    mand option to the kine‐
                                                                    matic object.
                                                                    ● TRUE: The command
                                                                      option was added suc‐
                                                                      cessfully
                                                                    ● FALSE: An error
                                                                      occurred. Details in
                                                                      ML_oCmdResult
STRUCT ML_KinBlendPData
Name       Data type    Inherited         Address   Initial value   Comment
                        from

STRUCT ML_KinBlendPData
  In       ML_iKin‐                                                     Input: Command data of
BlendP                                                       the command option
  Out      ML_oCm‐                                                      Output: Parameter of the
dOptResult                                                   command option
STRUCT ML_iKinBlendP EXTENDS ML_iKinCmdBlend
Name        Data type   Inherited   Address             Initial value   Comment
                        from
  KinName STRING(15) ML_iKinCmd‐                                        Name of the kinematics
                        Base                                            used to execute the com‐
                                                                        mand option
   Source          STRING(50)   ML_iKinCmd‐                             Returns the command
                                Base                                    option source, e.g. PlcAp‐
                                                                        plication1 is displayed in
                                                                        the diagnostic messages
   SourceLine ULINT             ML_iKinCmd‐                             Specifies the source line of
                                Base                                    the command; is displayed
                                                                        in the diagnostic messages
   D1              LREAL        ML_iKinCmd‐                             Distance to end position of
                                Blend                                   the first motion command
                                                                        at which blending starts
   D2              LREAL        ML_iKinCmd‐                             Distance between the
                                Blend                                   starting position of the
                                                                        second motion command
                                                                        and the end position of
                                                                        blending.
   SwitchOff BOOL                                       FALSE           FALSE means that the
                                                                        blending option is perma‐
                                                                        nently activated, use TRUE
                                                                        to deactivate the command
                                                                        option again
STRUCT ML_oCmdOptResult
Name       Data type  Inherited               Address   Initial value   Comment
                      from
  Error    BOOL                                                         Error ID TRUE indicates
                                                                        that an error occurred
   ErrorID         UDINT                                                Specifies the type of
                                                                        occurred error: The upper
                                                                        4 bytes reflect the main
                                                                        diagnostics, the lower 4
                                                                        bytes reflect the detailed
                                                                        diagnostics, 0 means no
                                                                        error

Data Layer:
Method: POST
URL:                https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/opt-blend
Payload:

{
"type":"object","value":
{

"permType":"PermOn",
"dist1":10.0,
"dist2":10.0
}
}

The parameter "permType" can assume the values "PermOn", “PermOff".

Python:
motion.kin_cmd_opt_blend( kin=<kinName> , d1=<D1>, d2=<D2> )

Creates a blending command for a kinematic (object has to be "attached"),
see documentation Python Runtime App ⮫ Python functions.

● <kinName> - string, kinematic object name
● <D1> - Blending length of the first motion command
● <D2> - Blending length of the second motion command

motion.kin_cmd_opt_blend_p( kin=<kinName> [,d1=<D1>]
[,d2=<D2>] )

Creates a permanent blending command for a kinematic (object has to be
"attached"), see documentation Python Runtime App ⮫ Python functions.
If d1 and d2 are not programmed, the permanent command option is disa‐
bled.
● <kinName> - string, kinematic object name
● <D1> - Blending length of the first motion command
● <D2> - Blending length of the second motion command

BundleIF:
//! Create a command option for blending the next two move
commands (KIN_CMD_OPT_BLEND)
//!
//! @param[in] sourceInfo       Command source information
//! @param[in] duration          Do this command option once,
permanent or remove it?
//! @param[in] kinName           Name of the motion object
//! @param[in] preCornerDist     Earliest start from next
movement before reach the end of the first movement command
//! @param[in] postCornerDist Start distance before end of
commandName of the motion object
//! @param[in] mode             Optional blending mode
//! @return                     Was everything okay?
virtual MotionResult kinBlend(const cmd::Cmd-SourceInfo&
sourceInfo, cmd::CmdOptPermType duration, const char* kinName,
double preCornerDist, double postCornerDist) const = 0;

### 7.5.3 KinMCSP - Command options for kinematics machine coordinate

system
Basics
When working with a non-Cartesian kinematics but when wanting to program
positions in a Cartesian coordinate system, an axis transformation is required.
This component transforms position data of the axis coordinate system (ACS)
to the machine coordinate system (MCS) and back. These transformations are

referred to as forward transformation (ACS→MCS) and inverse transformation
(MCS→ACS). In addition, it is possible to pass a WCS offset to the MCS if
multiple kinematics exist in the world coordinate system (WCS).
All configuration data of such an axis transformation are saved as set. Define
several sets per kinematics. All sets are addressed via a (unique) string name.
The set contains the name of the axis transformation as well as their parame‐
ters. To change the sets, switch the Motion system to configuration mode (not
allowed during running operation).
Once the configuration is completed and it is changed to operating mode,
enable the MCS by using the command option kinMCS.
As long as an MCS is active, all subsequent commands refer to this system.

Naming:
ACS: Axis coordinate system
MCS: Machine coordinate system
Set: A set contains the name of the axis transformation as well as their param‐
eters.
Examples of a set:
● All relevant data for the axis transformation of a Scara kinematics
● All relevant data for the orientation transformation of a rotary table
● All relevant data for a cylinder jacket transformation

Nodes in the Data Layer for MCS data
The data of the MCS sets are contained in the Data Layer as part of the
kinematic configuration area.
Sets can be browsed, created and removed. The parameters of the set can be
read and written. Note that the parameters of an axis transformation depend
on the respective axis transformation. For example, a set of a delta kinematic
transformation has different parameters than the set of a Scara kinematic
transformation.
URL                        Command                    Result
https://<ip-addr>/         browse                     String array, containing
automation/api/v2/                                    the name of all sets
nodes/motion/kin/
<kin_name>/cfg/coord-
systems/mcs
https://<ip-addr>/         create                     Adding a new set (with
automation/api/v2/                                    specified name)
nodes/motion/kin/
<kin_name>/cfg/coord-
systems/mcs
https://<ip-addr>/         remove                     Removing an existing set
automation/api/v2/                                    (with specified name)
nodes/motion/kin/
<kin_name>/cfg/coord-
systems/mcs
https://<ip-addr>/         read/write                 All parameters of this set
automation/api/v2/
nodes/motion/kin/
<kin_name>/cfg/coord-
systems/mcs/<name>

URL                       Command             Result
https://<ip-addr>/        read/write          All parameters for the
automation/api/v2/                            position and orientation
nodes/motion/kin/                             offsets of the MCS in the
<kin_name>/cfg/coord-                         WCS
systems/mcs/wcs-offset
https://<ip-addr>/auto‐   read/write          Axis transformation name
mation/api/v2/nodes/
motion/kin/
<kin_name>/cfg/coord-
systems/mcs/<name>/
jnt-trafo

https://<ip-addr>/        read/write/browse   All parameters of the
automation/api/v2/                            axis transformation
nodes/motion/kin/
<kin_name>/cfg/coord-
systems/mcs/<name>/
param
https://<ip-addr>/        read/write          The axis assignment of
automation/api/v2/                            the axis transformation
nodes/motion/kin/
<kin_name>/cfg/coord-
systems/mcs/<name>/
param/axis-assignment
https://<ip-addr>/        read/write/browse   All general parameters of
automation/api/v2/                            the axis transformation
nodes/motion/kin/
<kin_name>/cfg/coord-
systems/mcs/<name>/
param/general
https://<ip-addr>/        read/write/browse   All parameters of a cer‐
automation/api/v2/                            tain parameter group of
nodes/motion/kin/                             the axis transformation
<kin_name>/cfg/coord-
systems/mcs/<name>/
param/<groups>
https://<ip-addr>/        read/write          Access to an individual
automation/api/v2/                            parameter
nodes/motion/kin/
<kin_name>/cfg/coord-
systems/mcs/<name>/
param/<groups>/<par‐
Name>

PLC:
Enables a machine coordinate system:

ML_KinMCSP
Name       Data type            Inherited      Address        Initial value   Comment
                                from
   Data            ML_KinMCSP                                                 InOut: Command parame‐
                                                                              ters
                   BOOL                                                       Returns, whether it was
ML_KinMCSP                                                                    possible to add the com‐
                                                                              mand to the kinematic
                                                                              object.
                                                                              ● TRUE: The ML_KinMCSP
                                                                                command could be
                                                                                added successfully
                                                                              ● FALSE: An error
                                                                                occurred. Details in
                                                                                ML_oCmdResult
STRUCT ML_KinMCSPData
Name         Data type           Inher‐     Addres Initial   Comment
                                 ited       s      value
                                 from
   In               ML_iKinMCS                               Input: Command data of the command
                    P
   Out              ML_oCm‐                                  Output: Command parameters
                    dOptResult
STRUCT ML_iKinMCSP
Name        Data type           Inherited   Address           Initial value   Comment
                                from
   KinName         STRING(63)   ML_iKinCmd‐                                   Name of the kinematics
                                Base                                          used to execute the com‐
                                                                              mand option
   Source          STRING(50)   ML_iKinCmd‐                                   Returns the command
                                Base                                          option source, e.g. PlcAp‐
                                                                              plication1 is displayed in
                                                                              the diagnostic messages
   SourceLine ULINT             ML_iKinCmd‐                                   Specifies the source line of
                                Base                                          the command; is displayed
                                                                              in the diagnostic messages
   SetName         STRING(50)                                                 Name of the configured
                                                                              axis transformation
   SwitchOff BOOL                                             FALSE           FALSE indicates that the
                                                                              MCS transformation is
                                                                              active permanently. Use
                                                                              TRUE to disable the com‐
                                                                              mand option again
STRUCT ML_oCmdOptResult
Name        Data type   Inher‐              Addres Initial   Comment
                        ited                s      value
                        from
  Error     BOOL                                             Error ID TRUE indicates that an error
                                                             occurred
   ErrorID          ULINT                                    Specifies the type of error (can currently
                                                             not be used and is always set to 1)

Data Layer:
Method: POST
For information about the complete data structure:
URL:                  https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/opt-mcs
Payload:

{
"type":"object","value":
{
"permType":"PermOn",
"setName": "Delta"

}
}

The parameter "permType" can assume the values "PermOn", “PermOff".

Python:
motion.kin_cmd_opt_mcs_p( kin=<kinName>, set=<setName>
[,switch=<ON/OFF>] )

Creates a permanent kinematics command option for an MCS (activating an
axis transformation, object has to be "attached"), see documentation Python
Runtime App ⮫ Python functions.
If the optional switch parameter is not programmed, the command enables
the option.
● <kinName> - string, kinematic object name
● <SetName> - name of the MCS set that has to be enabled/disabled
● <switch> - string that defines whether the block should be switched “ON"
  or “Off"

BundleIF
//! @brief Create a command option for activation of an axis
transformation (ACS ←→ MCS) (KIN_CMD_OPT_MCS)
//!
//! @param[in]   sourceInfo   Command source information
//! @param[in]   duration     Do this command option permanent
or remove it?
//! @param[in]   kinName      Name of the motion object
//! @param[in]   setName      Name of the axis transformation
set to activate/deactivate
//! @return                   Was everything okay?
virtual MotionResult kinMCS( const cmd::CmdSourceInfo&
sourceInfo, cmd::CmdOptPermType duration, const char* kinName,
const char* setName ) const = 0;

### 7.5.4 KinPCSP, KinPCSToolP - Command option for kinematic product

coordinate system
The function is obsolete
The tool correction implemented in this command option has been replaced
by the command option ⮫ Chapter 7.5.5 KinToolLengthsP - Non-static tool
offset on page 656. This should be used for new projects.

Basics
A product coordinate system (PCS) is a kinematic function to define a work‐
piece or a tool.
A PCS is defined by an OffsetXYZ, a rotation and an offset for auxiliary axes
and is saved as set.
Several sets, acting together can be linked to a group.
All sets and groups are addressed by names. The values are saved in the
configuration of the kinematics.
As long as a PCS is enabled, all subsequent motion commands are traversed
in this coordinate system.
If an offset is required for a single axis motion, a separate kinematics should
be created containing only the single axis.

Naming
WCS: World coordinate system
PCS: Product coordinate system
Set
A set contains offsets and orientation parameters describing a PCS:
● 3 offset values for axes with the geometric significance X, Y, Z
● 3 orientation parameter (Euler angle) describing the PCS orientation
● Up to 10 additional offset values for the additional kinematic axes (axes
   without geometric reference).
Examples of a set
● Set (palettA) for position and orientation of a pallet
● Set (boxGray) for position and orientation of a box
● Set (gripper1) for gripper description (size and orientation).
Group
Defines a PCS set sequence acting together; e.g. a box is positioned on a
pallet.
● Set “palletA" defines the position and orientation of the pallet
● Set "boxGray" defines the position and orientation of the box on the pallet
● Both sets form the “PalletA” group.

Use cases
Workpiece offset
An application has to machine/move a workpiece. In reality, there is typically
a deviation between the physical and the assumed position of the workpiece.
The deviation is measured and entered in a PCS set.
Another application of a workpiece offset is a fixed contour to be executed
at different positions in the working area. The offsets are defined in different
PCS sets.

Tool offset
An application can use different tools of different size/rotation. All specified
motions refer to the TCP (tool center point) The different tools are respon‐
sible for different axis motions, taken into consideration by the different off‐
sets.

Nodes on the Data Layer for PCS data (sets and groups)
The data of the PCS sets and PCS groups are contained in the Data Layer as
part of the Motion system configuration area.
URL                      Command                    Result
motion/cfg/coord-sys‐    browse                     String array, containing
tems/pcs/sets                                       the names of all sets
motion/cfg/coord-sys‐    create                     Adding a new set (with
tems/pcs/sets                                       specified name)
motion/cfg/coord-sys‐    remove                     Removing An existing set
tems/pcs/sets                                       (with specified name)
motion/cfg/coord-sys‐    read/write                 Offsets for XY coordi‐
tems/pcs/sets/<name>/                               nates of this set
offsetXYZ
motion/cfg/coord-sys‐    read/write                 Orientation of this set
tems/pcs/sets/<name>/                               (default: ZYZ Euler
orientation                                         angle)
motion/cfg/coord-sys‐    read/write                 Offsets for auxiliary axes
tems/pcs/sets/<name>/                               of this set
offsetAux
motion/cfg/coord-sys‐    browse                     String array, containing
tems/pcs/groups                                     names of all groups
motion/cfg/coord-sys‐    create                     Adding a new group
tems/pcs/groups                                     (with specified name)
motion/cfg/coord-sys‐    remove                     Removing an existing
tems/pcs/groups                                     group (with specified
                                                    name)
motion/cfg/coord-        read/write                 String array of all sets
systems/pcs/groups/                                 in this group (set order
<name>/sets                                         defines the sequence)

PLC:

ML_KinPCSP
Name       Data type             Inherited    Address     Initial value   Comment
                                 from
   Data            ML_KinPCSP‐                                            InOut: Parameter of the
                   Data                                                   command option

ML_KinPCSP
BOOL                                                   Returns, whether it was
ML_KinPCSP                                                             possible to add the com‐
mand option to the kine‐
matic object.
● TRUE: The command
  option was added suc‐
  cessfully
● FALSE: An error
  occurred. Details in
  ML_oCmdResult
STRUCT ML_KinPCSPData

Name       Data type           Inherited     Address   Initial value   Comment
                               from
 In             ML_iKinPCSP                                            Input: Command data of
                                                                       the command option
 Out            ML_oCm‐                                                Output: Parameter of the
                dOptResult                                             command option
STRUCT ML_iKinPCS EXTENDS ML_iKinCmdBase
Name        Data type  Inherited   Address             Initial value   Comment
                       from
  KinName STRING(63) ML_iKinCmd‐                                       Name of the kinematics
                       Base                                            used to execute the com‐
                                                                       mand option
 Source         STRING(50)     ML_iKinCmd‐                             Specifies the command
                               Base                                    option source, e.g.: PlcAp‐
                                                                       plication1 is shown in the
                                                                       diagnostic messages
 SourceLine ULINT              ML_iKinCmd‐                             Returns the source code
                               Base                                    line of the command
                                                                       option, is displayed in diag‐
                                                                       nostic messages
 SetName        STRING(50)     ML_iKinPCS                              Name of sets or the group
                                                                       of the PCS offset and the
                                                                       PCS orientation
 SwitchOff BOOL                                        FALSE           FALSE indicates that a
                                                                       PCS transformation is per‐
                                                                       manently set. With TRUE,
                                                                       the command option is ter‐
                                                                       minated again
STRUCT ML_oCmdOptResult
Name       Data type  Inherited              Address   Initial value   Comment
                      from
  Error    BOOL                                                        Error ID, TRUE indicates
                                                                       that an error occurred
 ErrorID        UDINT                                                  Specifies the type of the
                                                                       occurred error (currently
                                                                       not in use, is always set to
                                                                       1)
                       PLC:

ML_KinPCSP
Name       Data type             Inherited     Address   Initial value   Comment
                                 from
   Data            ML_KinPCSP‐                                           InOut: Parameter of the
                   Data                                                  command option
                   BOOL                                                  Returns, whether it was
ML_KinPCSP                                                               possible to add the com‐
                                                                         mand option to the kine‐
                                                                         matic object.
                                                                         ● TRUE: The command
                                                                           option was added suc‐
                                                                           cessfully
                                                                         ● FALSE: An error
                                                                           occurred. Details in
                                                                           ML_oCmdResult
STRUCT ML_KinPCSPData
Name       Data type             Inherited     Address   Initial value   Comment
                                 from
   In              ML_iKinPCSP                                           Input: Command data of
                                                                         the command option
   Out             ML_oCm‐                                               Output: Parameter of the
                   dOptResult                                            command option
STRUCT ML_iKinPCS EXTENDS ML_iKinCmdBase
Name        Data type  Inherited   Address               Initial value   Comment
                       from
  KinName STRING(63) ML_iKinCmd‐                                         Name of the kinematics
                       Base                                              used to execute the com‐
                                                                         mand option
   Source          STRING(50)    ML_iKinCmd‐                             Specifies the command
                                 Base                                    option source, e.g.: PlcAp‐
                                                                         plication1 is shown in the
                                                                         diagnostic messages
   SourceLine ULINT              ML_iKinCmd‐                             Returns the source code
                                 Base                                    line of the command
                                                                         option, is displayed in diag‐
                                                                         nostic messages
   SetName         STRING(50)    ML_iKinPCS                              Name of sets or the group
                                                                         of the PCS tool offset and
                                                                         the PCS orientation
   SwitchOff BOOL                                        FALSE           FALSE indicates that a PCS
                                                                         tool transformation is per‐
                                                                         manently set. With TRUE,
                                                                         the command option is ter‐
                                                                         minated again.

STRUCT ML_oCmdOptResult
Name       Data type  Inherited          Address      Initial value   Comment
                      from
  Error    BOOL                                                       Error ID, TRUE indicates
                                                                      that an error occurred
 ErrorID     UDINT                                                    Specifies the type of the
                                                                      occurred error (currently
                                                                      not in use, is always set to
                                                                      1)

Data layer
Method: POST

URL:                https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/opt-pcs
URL:                https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/opt-pcs-tool
Payload:

{
"type":"object","value":
{
"permType":"PermOn",
"setName": "setX50"
}
}

The parameter "permType" can assume the values "PermOn", “PermOff".

Python
motion.kin_cmd_opt_pcs_p( kin=<kinName> [, set=<setName>] )

Creates a permanent kinematics command option for a PCS that refers to the
base (object has to be "attached"), see documentation Python Runtime App
⮫ Python functions.
If the optional set parameter is not programmed, the PCS command option
(referring to the basis) is disabled.
● <kinName> - string, kinematic object name
● <setName> - string, name of the PCS set or PCS group to be enabled

motion.kin_cmd_opt_pcs_tool_p( kin=<kinName> [,
set=<setName>] )

Creates a permanent kinematics command option for a PCS tool that refers
to the tool (object has to be "attached"), see documentation Python Runtime
App ⮫ Python functions.
If the optional set parameter is not programmed, the PCSTool command
option (referring to the tool).
● <kinName> - string, kinematic object name
● <setName> - string, name of the PCSTool set or PCSTool group to be ena‐
  bled

BundleIF
//! Create a command option for activation of a product
coordinate system (KIN_CMD_OPT_PCS)
//!
//! @param[in]   sourceInfo   Command source information
//! @param[in]   duration     Do this command option permanent
or remove it?
//! @param[in]   kinName      Name of the motion object
//! @param[in]   setName      Name of the set or group to
activate
//! @return                       Was everything okay?
virtual MotionResult kinPCS( const cmd::CmdSourceInfo&
sourceInfo, cmd::CmdOptPermType duration, const char* kinName,
const char* setName ) const = 0;

//! Create a command option for activation of a product
coordinate system tool (KIN_CMD_OPT_PCSTool)
//!
//! @param[in]   sourceInfo   Command source information
//! @param[in]   duration     Do this command option permanent
or remove it?
//! @param[in]   kinName      Name of the motion object
//! @param[in]   setName      Name of the set or group to
activate
//! @return                   Was everything okay?
virtual MotionResult kinPCSTool( const cmd::CmdSourceInfo&
sourceInfo, cmd::CmdOptPermType duration, const char* kinName,
const char* setName ) const = 0;

### 7.5.5 KinToolLengthsP - Non-static tool offset

Basics
Different actuators with different sizes/rotations can be used within an appli‐
cation. All commanded positions refer to the tool center point (TCP) and are
therefore independent of the selected tool. Actuators/tools of different sizes
are taken into account by different tool-specific offset values within the tool
data and offset by the tool length correction. This determines the resulting
path of the tool zero point from the specified motion of the TCP (position and
orientation), which corresponds to the path of the tool flange when the tool is
inserted. The use of different tools therefore results in different axis motions.

The tool length compensation (kinToolLengths) is a kinematic command
option that calculates the tool-specific offset values. The offset values can
include a spatial offset and a rotation, which are stored within a general
tool-specific data set.
Several data sets can be combined to form a group (tool data group ). For
example, the use of a tool in a specific tool adapter can be simulated.
All tool data sets and groups are addressed by name.

Set
A tool data record contains data for:
● 3 offset values (∆x, ∆y, ∆z) that describe the position of the tool zero point
   in relation to the tool center point (TCP)
● Units of the offset values ∆x, ∆y, ∆z
● 3 Euler angles, which describe a rotation of the tool zero point in relation
   to the tool center point (TCP). Analogous to the definition of a product
   coordinate system (PCS), the convention of the Euler angles Z-Y-Z is
   intrinsic
● Units for the Euler angles
● Target architecture radius, e.g. for
● Unit for the radius
● Edge orientation, e.g. for a turning machine
Examples of a tool data set
● Description of a gripper (size and orientation)
● Description of a tool adapter (size and orientation)
● Description of a drill (length and radius)
The values of the tool data sets have to be specified with a sign and refer
to the machine coordinate system (MCS) of the kinematics in their reference
orientation: With a 6-axis robot mounted on the floor, the tool points upwards
in the reference orientation, whereas with a Scara robot it is typically oriented
downwards. This means that the Z-length of a gripper have to be specified
with a negative sign in the first case, as the tool zero point is in the negative
Z-direction of the MCS in relation to the tool center point. With the Scara,
however, the Z-length is specified with a positive sign, as the tool zero point is
in the positive Z-direction of the MCS in relation to the tool center point.

Group
Defines a sequence of tool data sets that are to be activated together, e.g. a
tool adapter in which a gripper is located:
● Set "adapter" defines the size of the tool adapter
● Set "green tool" defines the size of the gripper
● ® define a group as a sequence of the two tool data sets "green tool" and
    "adapter"
The individual tool data sets have to be specified in the order from the tool
engagement to the tool flange.
All tool data records are stored on the Data Layer.
If the kinToolLengths command option is active, the activated offset values
and Euler angles are calculated for all subsequent motion commands.
Changes to correction values within a tool data set only take effect when the
tool length correction is reactivated. All motion commands that are already
in the command buffer at the time of reactivation are still executed with the
previously effective correction values!
The radius and cutting edge position elements of a tool data set are not
evaluated by the kinToolLengths command option!

Data Layer nodes for tool data (sets and groups)
The tool data is stored on the Data Layer as part of the Motion configuration.
Sets and groups can be created, deleted and browsed.
The elements of tool data sets and groups can be read and written.
URL                       Command                   Result
motion/cfg/functions/     browse                    Drawing field with the
tool-data/sets                                      names of all existing tool
                                                    data records (sets)
motion/cfg/function/tool- create                    Add a new tool data set
data/sets                                           (with specified name)
motion/cfg/functions/     remove                    Remove an existing tool
tool-data/sets                                      data set (with specified
                                                    name)
motion/cfg/functions/   read/write                  Offset values ∆x, ∆y, ∆z
tool-data/sets/<name>/                              of this set
offset-xyz
motion/cfg/func‐        read/write                  Orientation angle of this
tions/tool-data/sets/                               set (Euler angle Z-Y-Z
<name>/orientation                                  intrinsic)
motion/cfg/functions/   read/write                  Radius of this set
tool-data/sets/<name>/
radius
motion/cfg/func‐        read/write                  Edge orientation of this
tions/tool-data/sets/                               set
<name>/edge-orientation
motion/cfg/functions/   browse                      Drawing field with the
tool-data/groups                                    names of all existing tool
                                                    groups
motion/cfg/functions/     create                    Add a new tool group
tool-data/groups                                    (with specified name)
motion/cfg/functions/     remove                    Remove an existing tool
tool-data/groups                                    group (with specified
                                                    name)

URL                        Command                    Result
motion/cfg/functions/      read/write                 String array of all tool
tool-data/groups/                                     data records in this
<name>/sets                                           group (set order deter‐
  mines the sequence)

PLC:

STRUCT ML_iKinToolLengthsPData
Name        Data type    Inherited           Address     Initial value   Comment
                         from
  In        S                                                            Input: Command data of
                                                                         the command option
  Out        ML_oCm‐                                                     Output: Parameter of the
             dOptResult                                                  command option
STRUCT ML_iKinToolLenghtsP
Name        Data type    Inherited           Address     Initial value   Comment
                         from
  KinName STRING(15)                                                     Name of the kinematics
                                                                         used to execute the com‐
                                                                         mand option
  Source     STRING(50)                                                  Specifies the command
                                                                         option source, e.g.: PlcAp‐
                                                                         plication1 is shown in the
                                                                         diagnostic messages
  SourceLine ULINT                                                       Returns the source code
                                                                         line of the command
                                                                         option, is displayed in diag‐
                                                                         nostic messages
  SetName    STRING(50)                                                  Name of the set or group
                                                                         of tool data
  SwitchOff BOOL                                         FALSE           FALSE indicates that a
                                                                         PCS transformation is per‐
                                                                         manently set. With TRUE,
                                                                         the command option is ter‐
                                                                         minated again
STRUCT ML_oCmdOptResult
Name       Data type  Inherited              Address     Initial value   Comment
                      from
  Error    BOOL                                                          Error ID, TRUE indicates
                                                                         that an error occurred
  ErrorID    UDINT                                                       Specifies the type of the
                                                                         occurred error (currently
                                                                         not in use, is always set to
                                                                         1)

Data layer
Method: POST
URL:                https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/opt-tool-length

The parameter "permType" can assume the values "PermOn", “PermOff".

Python
motion.kin_cmd_tool_lengths_p( kin=<kinName> [, set=<setName/
groupName>] )

Creates a permanent kinematic command option for calculating the tool
lengths.
If the optional parameter (for the name of the data set or tool group) is not
programmed, the command option is deactivated.

● <kinName> - string, kinematic object name
● <setName> - string, name of the tool data set or tool group to be activated

BundleIF:
//! @brief Create a command option for activation of a tool
lengths correction (KIN_CMD_OPT_TOOL_LENGTHS)
//!
//! @param[in]     sourceInfo     Command source information
//! @param[in]     duration       Do this command option
permanent or remove it?
//! @param[in]     kinName        Name of the motion object
//! @param[in]     setName        Name of the tool data set or
group to activate
//! @return                       was everything okay?
virtual MotionResult kinToolLengths( const cmd::CmdSourceInfo&
sourceInfo, cmd::CmdOptPermType duration, const char* kinName,
const char* setName ) const = 0;

### 7.5.6 KinAxsDynLimP - Decreasing dynamic limits of the kinematic axis

using a command
Basics
This command option permanently decreases the dynamic limits of a kine‐
matic axis for all following travel commands until the command option is
explicitly deactivated.

Functional description
It can also happen that the user wants to reduce the dynamics of a kinematic
axis without wanting to change the configuration. In this case you can enable
this command option.
Setting a dynamic limit to zero means "do not reduce this limit".
If the axis limits, reduced using this command option, are to be changed, call
them again with the new limits.
If the command option is commanded, the axis has to be assigned to the
kinematics.
The dynamic limit values can only be further reduced and not increased in
contrast to the configured limits.
Example:

The gripper picked up a fragile product. The motions should now be very
careful. The highly dynamic axis "X" should only move with a reduced jerk of
2.5 m/s³. Set the jerk values of the dynamic input structure to 2.5 and set all
other values to zero (this means that they are not changed).
Call this command option with the "X" axis. If the command option was called
successfully, all following motion commands of this kinematics slow down
this motion so that the "X" axis moves at a jerk of greater than 2.5. If the
product was files and if the command options are disabled again, the config‐
ured limits become active again.

PLC:

ML_KinAxsDynLimP
Name        Data type       Inherited     Address       Initial value   Comment
                            from
  Data       ML_KinAxs‐                                                 InOut: Command parame‐
             DynLimP                                                    ters
  ML_Kin‐    BOOL                                                       Returns, whether it was
AxsDynLimP                                                              possible to add the com‐
                                                                        mand to the kinematic
                                                                        object.
                                                                        ● TRUE: The ML_KinAxs‐
                                                                          DynLimP command
                                                                          could be added success‐
                                                                          fully
                                                                        ● FALSE: An error
                                                                          occurred. Details in
                                                                          ML_oCmdResult
STRUCT ML_KinAxsDynLimPData
Name       Data type   Inherited          Address       Initial value   Comment
                       from
  In       ML_iKinAxs‐                                                  Input: Command data of
           DynLimP                                                      the command
  Out      ML_oCm‐                                                      Output: Command parame‐
           dOptResult                                                   ters
STRUCT ML_iKinMoveDirectAsync EXTENDS ML_iKinCmdBase
Name        Data type   Inherited   Address     Initial value           Comment
                        from
  KinName STRING(15) ML_iKinCmd‐                                        Name of the kinematics
                        Base                                            used to execute the com‐
                                                                        mand
  Source     STRING(50)     ML_iKinCmd‐                                 Specifies the command
                            Base                                        source, e.g PlcApplication1
                                                                        is displayed in the diag‐
                                                                        nostic messages

STRUCT ML_iKinMoveDirectAsync EXTENDS ML_iKinCmdBase
  SourceLine ULINT      ML_iKinCmd‐                                     Specifies the source line of
 Base                                            the command; is displayed
                                                 in the diagnostic messages
   AxsName         STRING(15)                                           Kinematic axis name for
                                                 which the dynamic limits
                                                 are to be reduced
   DynLimits ML_iDynLi‐                                                 Lowered dynamic axis
mits                                                       limits if they are part of the
                                                 kinematics
   SwitchOff BOOL                                       FALSE           FALSE means that the
                                                 blending option is perma‐
                                                 nently activated, use TRUE
                                                 to deactivate the command
                                                 option again
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
   Error           BOOL                                                 Error ID TRUE indicates
                                                                        that an error occurred
   ErrorID         ULINT                                                Specifies the type of
                                                                        occurred error: The upper
                                                                        4 bytes reflect the main
                                                                        diagnostics, the lower 4
                                                                        bytes reflect the detailed
                                                                        diagnostics, 0 means no
                                                                        error

Data Layer:
Method: POST
URL:                https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/opt-axs-dyn-lim
Payload:

{
"type":"object","value":
{
"axsName":"Y",
"lim":{
        "vel":0,

          "acc":0,
          "dec":0,
          "jrkAcc":0,
          "jrkDec":0
           }
}
}

If the structure does not contain "lim", the command option is disabled.

Python:
motion.kin_cmd_opt_axs_dyn_lim_p( kin=<kinName>, axs=<axsName>
[,vel=<velocity>] [,acc=<acceleration>] [,dec=<deceleration>]

[,jrk_acc=<jerkAcceleration>] [,jrk_dec=<jerkDeceleration>])

Enables/disables the permanent command option to reduce the kinematic
axis dynamics. The kinematics has to be assigned to the script instance
(object has to be "attached"), see documentation Python Runtime App
⮫ Python functions.
If no optional parameters are programmed for the dynamics, the command
option is disabled.
● <kinName> - string, kinematic name
● <axsName> - string, kinematic axis name
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
//! @brief Create a command option to reduce the kinematics
axis limits more than the configured values
//!
//! @param[in] sourceInfo Command source information
//! @param[in] duration   Do this command option once,
permanent or remove it?
//! @param[in] kinName    Name of the motion object
//! @param[in] axsName    Name of the kinematics axis object
(must be part of the kinematics at this time)
//! @param[in] dynLim     Dynamic limits of the command
//! @return               Was everything okay?
MotionResult kinAxsDynLim(const dia::CmdSourceInfo&

sourceInfo, cmd::CmdOptPermType duration, const char* kinName,
const char* axsName, const cmd::DynamicLimitsT& dynLim) const;

### 7.5.7 KinContMotionP - Continuous motion across several commands

Basics
This kinematic command option permanently enables the motion control via
several commands until it is explicitly disabled. Thus, it is possible to execute
several (buffered) commands successively without stopping in between.

Functional description
Without this kinematic command option, it is completely stopped at the
end of each command (velocity and acceleration are zero). If the kinematic
command option is active, the ctrlX MOTION calculates a maximum transi‐
tion velocity between the commands. In particular, this depends on the pro‐
grammed path (as e.g. on tangential transitions) as well as on the configured
axis reserve.
The transition velocity is determined so that the configured dynamic limit
values of the axes is usually not exceeded. By using the configurable axis
reserve, a factor can be specified by which the dynamic limit values of the
axis can be exceeded in the cycle in which it is changed from one command to
the next.
Example:
Configured maximum acceleration of axis X: 2.0 m/s².
Axis reserve of the X axis: 0.5.
Thus, the kinematic command option can determine a transition speed during
which the X axis can travel at an acceleration of 3.0 m/s² (acceleration limit +
reserve) in the cycle in which the command change takes place.
The command option is incompatible with blending, see ⮫ Chapter 7.5.2
KinBlend, KinBlendP - Blending/permanent kinematic option on page 640. If
blending is active, the velocity adaptation is determined by blending and not
by the continuous motion. Furthermore, the blending length should be consid‐
erably smaller than the commanded length of the motions if this command
option is active.
This command option is not optimized for very short motion commands. Very
short paths (less than a couple of millimeters) can result in an instable, math‐
ematical algorithms resulting in suboptimal velocity profiles. Furthermore, the
computation time can take too long.

Data Layer node
The axis reserve configuration can be read and written via Data Layer. It can
be found in the configuration area of the axes (as it is axis-specific). However,
it is only required if the axis is assigned to a kinematics, see ⮫ Chapter 7.2.42
AxsAddToKin - Adding the axis to the kinematics on page 512.
URL                           Command                      Result
https://<ip-addr>/automa‐     read/write                   Reads or write the axis acceleration
tion/api/v2/nodes/motion/axs/                              reserve
<axs_name>/cfg/kin-proper‐
ties/acc-reserve
https://<ip-addr>/automa‐     read/write                   Reads or write the axis jerk reserve
tion/api/v2/nodes/motion/axs/
<axs_name>/cfg/kin-proper‐
ties/jrk-reserve

The configured data for the axis reserve can be changed at any time (also
in case of an active motion). However, they are already used during the
command preparation. This means if you modify the data during running oper‐
ation, the command buffer has to empty first. The preparation is typically
several commands ahead of the execution.

PLC:

ML_KinContMotionP
Name       Data type        Inherited     Address     Initial value   Comment
                            from
  Data        ML_KinCont‐                                             InOut: Command parame‐
              MotionP                                                 ters
  ML_Kin‐     BOOL                                                    Returns, whether it was
ContMotionP                                                           possible to add the com‐
                                                                      mand to the kinematic
                                                                      object.
                                                                      ● TRUE: The ML_Kin‐
                                                                        ContMotionP command
                                                                        could be added success‐
                                                                        fully
                                                                      ● FALSE: An error
                                                                        occurred. Details in
                                                                        ML_oCmdResult
STRUCT ML_KinContMotionPData
Name       Data type    Inherited         Address     Initial value   Comment
                        from
  In       ML_iKinCont‐                                               Input: Command data of
           MotionP                                                    the command
  Out      ML_oCm‐                                                    Output: Command parame‐
           dOptResult                                                 ters
STRUCT ML_iKinContMotionP EXTENDS ML_iKinCmdBase
Name        Data type   Inherited  Address     Initial value          Comment
                        from
  KinName STRING(15) ML_iKinCmd‐                                      Name of the kinematics
                        Base                                          used to execute the com‐
                                                                      mand
  Source      STRING(50)    ML_iKinCmd‐                               Specifies the command
                            Base                                      source, e.g PlcApplication1
                                                                      is displayed in the diag‐
                                                                      nostic messages
  SourceLine ULINT          ML_iKinCmd‐                               Specifies the source line of
                            Base                                      the command; is displayed
                                                                      in the diagnostic messages

STRUCT ML_iKinContMotionP EXTENDS ML_iKinCmdBase
  SwitchOff BOOL                               FALSE                      FALSE means that the com‐
                                                   mand option is enabled
                                                   permanently, use TRUE
                                                   to disable the command
                                                   option again
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
URL:                https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/opt-cont-motion
Payload:

{
"type":"object","value":
{
"permType":"PermOn"
}
}

The parameter "permType" can assume the values "PermOn" and “PermOff".

Python:
motion.kin_cmd_opt_cont_motion_p( kin=<kinName> [,switch=<ON/
OFF>] )

Enables/disables the permanent command option for a continuous motion
across several commands. The kinematics has to be assigned to the script
instance (object has to be "attached"), see documentation Python Runtime
App ⮫ Python functions).
If the optional parameter "switch" is not programmed, the command option is
enabled.
● <kinName> - string, kinematic name
● <switch> - string, defines whether the command option is to be enabled
  ("ON") or disabled ("OFF")

BundleIF:

//! @brief Create a command option for activation of the
continuous motion over multiple commands
//!
//! @param[in] sourceInfo Command source information
//! @param[in] duration     Do this command option permanent
or remove it?
//! @param[in] kinName      Name of the motion object
//! @return                 Was everything okay?
MotionResult kinContMotion(const dia::CmdSourceInfo&
sourceInfo, cmd::CmdOptPermType duration, const char* kinName)
const;

### 7.5.8 KinPolyTransP - Command options for kinematics - Path rounding

with polynomial
Basics
If this command option is activated, it inserts a fade or a rounding by means
of a polynomial path between all consecutive motion commands. The com‐
mand option has to be explicitly switched off to end the rounding of subse‐
quent motion commands.
Commanded motions are shortened and a polynomial motion (c2-continuous)
is insulted in the resulting gap by ctrlX MOTION. The vehicle is then trav‐
eled along this path (in compliance with the programmed and configured
dynamic limits). A basic use case is the rounding of corners between two
linear motions on a defined path. On the inserted polynomial transition path,
the same path dynamics limits apply as on the motion command before the
corner.
A polynomial rounding can be used not only between linear motion com‐
mands, but also in combination with circular commands or orientation and/or
additional axis motions. In the case of a tangential transition from a straight
line to a circular path, the velocity usually has to be reduced, as a jump in the
path curvature (acceleration) occurs here. Activated polytrans ensures a twice
continuously differentiable (c2) transition.
Example:
If a motion 1 is commanded in X direction, following by a motion 2 in Y direc‐
tion (i.e. before a corner with 90°), the function generates a c2-continuous
path used to round the corner. On the rounded part, the same dynamic as for
motion 1 can be used for traveling (as long as the axis limit values are not
exceeded).

Minimal example as Python code

########## Python minimal example PolyTrans (active unit: mm) ##########
# Enable: continuous motion; velocity at command transitions &gt; 0
motion.kin_cmd_opt_cont_motion_p(kin_name, "ON")
# Enable: polynomial rounding with a corner distance of 20mm
motion.kin_cmd_opt_poly_trans_p(kin_name, eps=20)
# Enable: expect a sequence of motion commands and wait until
# at least 3 commands are prepared before the motion starts
motion.kin_cmd_contour(kin_name, True, 3)

# linear motion command: 100mm relative in the x-direction of the
# PCS coordinate system
motion.kin_cmd_move_ex(kin_name, {"X":{"INCR_VALUE": 100}}, "PCS", vel=100,
acc=2, dec=2)
# linear motion command: 100mm relative in the y-direction of the

# PCS coordinate system
motion.kin_cmd_move_ex(kin_name, {"Y":{"INCR_VALUE": 100}}, "PCS", vel=100,
acc=2, dec=2)

# Disable: do not expect any sequence of motion commands anymore
motion.kin_cmd_contour(kin_name, False)
# Disable: polynomial rounding
motion.kin_cmd_opt_poly_trans_p(kin_name)
# Disable: continuous motion

The calculation effort is considerably higher than for the command option
blending (⮫ Chapter 7.5.2 KinBlend, KinBlendP - Blending/permanent kine‐
matic option on page 640). Additionally, the traveled motion during blending
(⮫ Chapter 7.5.2 KinBlend, KinBlendP - Blending/permanent kinematic option
on page 640) is time-optimized (in contrast to PolyTrans).
In most cases, the "PolyTrans" function should be used in combination with
the "ContMotion" command option (see ⮫ Chapter 7.5.7 KinContMotionP -
Continuous motion across several commands on page 664) so that a contin‐
uous velocity profile is generated without braking to a standstill at command
transitions.

Parameter description
D1: Distance to the end position of the first motion command (corner E1/S2)
at which the rounding may begin.
D2: Distance after the starting position of the second motion command
(corner E1/S2) at which the motion has to be returned to the path (end of
rounding).
Eps: Distance to the corner.

Both D1 and D2 as well as Eps refer to the currently active FeedGroup (see
⮫ Chapter 7.5.11 KinFeedGroupP - Specifying the feed group on page 999).
This means that only coordinates or axes that are part of the active
FeedGroup are considered for the calculation of distances.
Set D1 or D2 to a very high value to blend the entire path (D1 and D2 are
restricted to half of the path).
It is possible to either program D1 and D2 or Eps, bot not both. Do not set
the used parameters to zero or omit them (depending on the used interface).
The used parameters have to be greater than zero.
If D1 and D2 are programmed, the originally programmed motions are short‐
ened by the corresponding lengths (by max. half the length of the original
path length) and the resulting gap is closed with a polynomial path (c2-con‐
tinuous).

If Eps is programmed, the polynomial path is generated which does not
deviate further than Eps from the originally programmed motions. The greatest
deviation is the distance to the corner point. The distance can also be less
due to geometric factors. The distance from start to end of the polynomial
path to the corner is also half the length of the original path length.

Restrictions
If the coordinate system is changed between two motion commands (e.g.
a new PCS set is activated), there is no crossfade between these two
motions. The corner is traveled completely. Even if one of the motions is
a point-to-point motion (e.g. MoveDirect, MoveDirectAsync), blending is not
used between these motions. Furthermore, there is no blending if the output
direction of the first motion is almost identical to the input direction of the
second motion (opening angle ≈ 180 °) or if one of the two motions is very
short.
As a matter of principle, the command options “Blending” and “PolyTrans”
rule each other out. An error is generated if both are simultaneously enabled
for the same kinematics.

PLC:

STRUCT ML_KinPolyTransPData
Name       Data type    Inherited         Address       Initial value   Comment
                        from
  In       ML_iKinPoly‐                                                 Input: Command data of
           TransP                                                       the command option
  Out      ML_oCm‐                                                      Output: Parameter of the
           dOptResult                                                   command option
STRUCT ML_iKinPolyTransP EXTENDS ML_iKinCmdBase
Name        Data type    Inherited  Address     Initial value           Comment
                         from
  KinName STRING(15) ML_iKinCmd‐                                        Name of the kinematics
                         Base                                           used to execute the com‐
                                                                        mand option

STRUCT ML_iKinPolyTransP EXTENDS ML_iKinCmdBase
  Source    STRING(50) ML_iKinCmd‐                                      Returns the command
  Base                                           option source, e.g. PlcAp‐
                                                 plication1 is displayed in
                                                 the diagnostic messages
   SourceLine ULINT            ML_iKinCmd‐                              Specifies the source line of
        Base                                     the command; is displayed
                                                 in the diagnostic messages
   D1              LREAL                                0.0             Distance to end position of
                                                 the first motion command
                                                 at which blending starts
   D2              LREAL                                0.0             Distance after the starting
                                                 position of the second
                                                 motion command in which
                                                 the motion has to be
                                                 retraced to the path (end
                                                 of blending).
   Eps             LREAL                                0.0             Distance to the pro‐
                                                 grammed boundary.
   SwitchOff BOOL                                       FALSE           FALSE means that the
                                                 blending option is perma‐
                                                 nently activated, use TRUE
                                                 to deactivate the command
                                                 option again
STRUCT ML_oCmdOptResult
Name       Data type  Inherited              Address    Initial value   Comment
                      from
  Error    BOOL                                                         Error ID TRUE indicates
                                                                        that an error occurred
   ErrorID         ULINT                                                Specifies the type of
                                                                        occurred error: The upper
                                                                        4 bytes reflect the main
                                                                        diagnostics, the lower 4
                                                                        bytes reflect the detailed
                                                                        diagnostics, 0 means no
                                                                        error

Data Layer:
Method: POST
URL:                https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/opt-poly-trans
Payload:
{
"type":"object","value":
      {
      "permType":"PermOn",
      "dist1":1,
      "dist2":1
      }
}
or

{
"type":"object","value":
      {
      "permType":"PermOn",
      "eps":1
      }
}

Only specify Dist1 and Dist2 or Eps during activation.

Python:
motion.kin_cmd_opt_poly_trans_p( kin=<kinName> [,d1=<D1>]
[,d2=<D2>] [,eps=<Eps>])

Enables/disables the permanent command option for contour rounding by
using polynomial paths to be inserted. The kinematics has to be assigned to
the script instance (object has to be "attached"), see documentation Python
Runtime App ⮫ Python functions.
If none of the optional parameters is programmed for the path, the command
option is disabled.
●  <kinName> - string, kinematic object name
●  <D1> - double; max. distance before the corner for rounding
●  <D2> - double; max. distance behind the corner for rounding
●  <Eps> - double; max. distance of the generated polynomial path from the
   corner
To enable the command option, program either D1 and D2 with a value
greater than 0 or Eps.

BundleIF:
//! Create a command option for inserting polynomial commands
between successively move commands (KIN_CMD_OPT_POLY_TRANS)
//!
//! @param[in] sourceInfo       Command source information
//! @param[in] duration         Do this command option once,
permanent or remove it?
//! @param[in] kinName          Name of the motion object
//! @param[in] preCornerDist    Distance to shorten the end of
the precorner (D1)
//! @param[in] postCornerDist Distance to shorten the start
of the postcorner (D2)
//! @param[in] eps              DEPRECATED (can be set to
PolyTransMode::MODE_L1L2 always
//! @param[in] mode             Mode L1L2 or EPS
//! @return                     Was everything okay?
virtual MotionResult kinPolyTrans(const dia::Cmd-SourceInfo&
sourceInfo, cmd::CmdOptPermType duration, const char* kinName,
double preCornerDist, double postCornerDist, double eps,
cmd::PolyTransMode mode) const = 0;

### 7.5.9 KinSafeAreaP - Working areas/safe zones

Basics
This kinematics command option permanently switches on the monitoring of
an individual protection zone or a permitted working area for all motion com‐
mands until it is explicitly switched off or a reset command is executed on the
kinematics or the Motion is switched to CONFIGURATION, which also happens
upon a control restart.
A detailed functional description can be found under ⮫ Chapter 6.3.8 Working
areas and safe zones on page 308.

PLC:

ML_KinSafeAreaP
Name        Data type           Inherited     Address      Initial value   Comment
                                from
   Data     ML_KinSa‐                                                      InOut: Command parame‐
            feAreaP                                                        ters
  ML_KinSa‐ BOOL                                                           Returns, whether it was
feAreaP                                                                    possible to add the com‐
                                                                           mand to the kinematic
                                                                           object.
                                                                           ● TRUE: The ML_KinSa‐
                                                                             feAreaP command could
                                                                             be added successfully
                                                                           ● FALSE: An error
                                                                             occurred. Details in
                                                                             ML_oCmdResult
STRUCT ML_KinSafeAreaPData
Name       Data type    Inherited             Address      Initial value   Comment
                        from
  In       ML_iKinSa‐                                                      Input: Command data of
           feAreaP                                                         the command
  Out      ML_oCm‐                                                         Output: Command parame‐
           dOptResult                                                      ters
STRUCT ML_iKinSafeAreaP EXTENDS ML_iKinCmdBase
Name        Data type    Inherited  Address    Initial value               Comment
                         from
  KinName STRING(15) ML_iKinCmd‐                                           Name of the kinematics
                         Base                                              used to execute the com‐
                                                                           mand
   Source          STRING(50)   ML_iKinCmd‐                                Specifies the command
                                Base                                       source, e.g PlcApplication1
                                                                           is displayed in the diag‐
                                                                           nostic messages

STRUCT ML_iKinSafeAreaP EXTENDS ML_iKinCmdBase
  SourceLine ULINT       ML_iKinCmd‐                                   Specifies the source line of
     Base                                          the command; is displayed
                                                   in the diagnostic messages
 SafeArea    STRING(50)                                                The name of the safe zone
                                                   or the work zone in the
                                                   configuration
 SwitchOff BOOL                                        FALSE           FALSE means that the com‐
                                                   mand option is enabled
                                                   permanently, use TRUE
                                                   to disable the command
                                                   option again

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
<kin_name>/cmd/opt-safe-area
Payload:

{
"type":"object","value":
{
"permType":"PermOn",
"safeArea":"Obstacle_A"
}
}

The parameter "permType" can assume the values "PermOn" and “PermOff".

Python:
motion.kin_cmd_opt_safe_area_p( kin=<kinName>,
safe_area=<safeArea> [,switch=<ON/OFF>] )

Activates/deactivates the monitoring of a working or protected area as a per‐
manent command option (object has to be "attached"), see documentation
Python Runtime App ⮫ Python functions).
If the optional parameter "switch" is not programmed, the monitoring of the
transferred working area or safe zone is enabled.

● <kinName> - string, kinematic name
● <safeArea> - string, name of the working area or safe zone whose moni‐
  toring is to be enabled or disabled
● <switch> - string, defines whether monitoring is to be enabled ("ON") or
  disabled ("OFF")

BundleIF:

//! @brief Create a command option for activation of a safe
zone or working area
//!
//! @param[in]    sourceInfo   Command source information
//! @param[in]    duration     Do this command option
permanent or remove it?
//! @param[in]    kinName      Name of the motion object
//! @param[in]    safeAreaName Name of the configured safe
zone or work area
//! @return                    Was everything okay?
MotionResult kinSafeArea(const dia::CmdSourceInfo& sourceInfo,
cmd::CmdOptPermType duration, const char* kinName, const char*
safeAreaName);

### 7.5.10 KinSafeAreaInExecutionP - Working areas/safe zones

Basics
This kinematics command option switches the monitoring of an individual
protection zone or a permitted working area permanently on for all motion
commands during the entire processing time until it is explicitly switched off
or a reset command is executed on the kinematics or the Motion is switched
to CONFIGURATION, which also happens upon a control restart.
A detailed functional description can be found under ⮫ Chapter 6.3.8 Working
areas and safe zones on page 308.

PLC:

ML_KinSafeAreaInExecutionP
Name        Data type    Inherited           Address       Initial value   Comment
                         from
  Data      ML_KinSa‐                                                      InOut: Command parame‐
            feAreaInExe‐                                                   ters
            cutionP

ML_KinSafeAreaInExecutionP
  ML_KinSa‐ BOOL                                                    Returns, whether it was
feAreaInExe‐                                                        possible to add the com‐
cutionP                                                             mand to the kinematic
object.
● TRUE: The ML_KinSa‐
  feAreaP command could
  be added successfully
● FALSE: An error
  occurred. Details in
  ML_oCmdResult
STRUCT ML_KinSafeAreaPData

Name       Data type    Inherited         Address   Initial value   Comment
                        from
  In       ML_iKinSa‐                                               Input: Command data of
           feAreaP                                                  the command
  Out      ML_oCm‐                                                  Output: Command parame‐
           dOptResult                                               ters
STRUCT ML_iKinSafeAreaP EXTENDS ML_iKinCmdBase
Name        Data type    Inherited  Address    Initial value        Comment
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
  SafeArea   STRING(50)                                             The name of the safe zone
                                                                    or the work zone in the
                                                                    configuration
  SwitchOff BOOL                                    FALSE           FALSE means that the com‐
                                                                    mand option is enabled
                                                                    permanently, use TRUE
                                                                    to disable the command
                                                                    option again
STRUCT ML_oCmdResult
Name       Data type        Inherited     Address   Initial value   Comment
                            from
  CmdID      ULINT                                                  Command ID (is set to
                                                                    18446744073709551615 in
                                                                    the event of an error)
  Error      BOOL                                                   Error ID TRUE indicates
                                                                    that an error occurred

STRUCT ML_oCmdResult
  ErrorID  UDINT                                                        Specifies the type of
                                                 occurred error: The upper
                                                 4 bytes reflect the main
                                                 diagnostics, the lower 4
                                                 bytes reflect the detailed
                                                 diagnostics, 0 means no
                                                 error

Data Layer:
Method: POST
URL:                https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/opt-safe-area-exec
Payload:

{
"type":"object","value":
{
"permType":"PermOn",
"safeArea":"Obstacle_A"
}
}

The parameter "permType" can assume the values "PermOn" and “PermOff".

Python:
motion.kin_cmd_opt_safe_area_exec_p ( kin=<kinName>,
safe_area=<safeArea> [,switch=<PermOn/PermOff>] )

Enables/disables the monitoring of a working area or safe zone during pro‐
gram processing as permanent command option. The kinematics has to be
assigned to the script instance, see documentation Python Runtime App
⮫ Python Functions).
If the optional parameter "switch" is not programmed, the monitoring of the
transferred working area or safe zone is enabled.
● <kinName> - string, kinematic name
● <safeArea> - string, name of the working area or safe zone whose moni‐
  toring is to be enabled or disabled
● <switch> - string, defines whether monitoring is to be enabled ("ON") or
  disabled ("OFF")

BundleIF:

//! @brief Create a command option for monitoring of a safe
zone or working area in the execution or disable it
//!
//! @param[in]   sourceInfo    Command source information
//! @param[in]    duration     Do this command option
permanent or remove it?
//! @param[in]   kinName       Name of the motion object
//! @param[in]    safeAreaName Name of the configured safe
zone or work area
//! @return                    Was everything okay?
MotionResult(*kinSafeAreaInExecution)(void*

handle, const ::motion::core::dia::CmdSourceInfo&
sourceInfo, ::motion::core::cmd::CmdOptPermType duration,
const char* kinName, const char* safeAreaName);

### 7.5.11 KinFeedGroupP - Specifying the feed group

Basics
The KinFeedGroupP command option can be used to temporarily change the
configured feed group (which controls the dynamics calculation of the inter‐
polation).

In the ctrlX MOTION positioning and/or orientation motions in space can be
commanded with or without additional axes. However, it is not always useful

to include all coordinates and axes in the calculation of the interpolation.
Therefore, there is a possibility to create a feed group.
Examples of scope:
● FeedGroup FG_XYZ_O_A - All coordinates and axes are taken into account
  for the path dynamics
● FeedGroup FG_XYZ - Handling robot taking the geometrical path without
  the orientation into consideration
Examples of different FeedGroup definitions and their influence on axis veloci‐
ties:
●   Start pose: (x=0.02m, y=0.01m, z=0m, Rz=14°)
●   End pose: (x=0.1m, y=0.03m, z=0.005m, Rz=-76°)
●   Max path velocity velMax=50mm/s
●   Diff pose: (dx=0.08m, dy=0.02m, dz=0.005m, Rz=-90°)

Without FeedGroup, the default FeedGroup FG_XYZ is used:
s = 0.0826
axes velocity: (x: 48mm/s, y: 12mm/s, z: 3mm/s, Rz: -54°/s)
With FeedGroup FG_XY (theoretical case can currently not be configured):
s = 0.0825
axes velocity: (x: 48mm/s, y: 12mm/s, z: 3mm/s, Rz: -54°/s)
With FeedGroup FG_XY but dz=0.05 (theoretical case can currently not be
configured):
s = 0.096
axes velocity: (x: 42mm/s, y: 10mm/s, z: 26mm/s, Rz: -46°/s)
With FeedGroup FG_XYZ_O, without factor "red-to-lin-conversion":
s = 0.77
axes velocity: (x: 5.2mm/s, y: 1.3mm/s, z: 0.3mm/s, Rz: -5.8°/s)
With FeedGroup FG_XYZ_O, with factor "red-to-lin-conversion" =0.12 :
s = 0.122
axes velocity: (x: 33mm/s, y: 8mm/s, z: 2mm/s, Rz: -37°/s)
With FeedGroup FG_XYZ and individual max orientation velocity =20°/s:

s = 0.0826
Automatic reduction of the web velocity from velMax=50mm/s to
velMax=18.5mm/s axes velocity: (x: 18mm/s, y: 4mm/s, z: 1mm/s, Rz: -20°/s)

Functional description
There are two ways to change the feed group, either via a command option
or by overwriting the default feed group. The feed group defines a subset of
the parameters and states to be considered, which are used to calculate the
interpolation speed.
By default, FG_XYZ is defined as feed group. The subgroup defined in the feed
group can be used to ensure that, for example, only the path in the 3-D plane
is included in the calculation of the interpolation speed and that a change in
orientation or any other axis motion that may be involved is not taken into
account.
This means that when a kinematic command is issued, the axes contained in
the feed group are feed-forming.
Example:
● Kinematics with X,Y,Z,Y1,X2 and FeedGroup X,Y,Z with KinMoveAbs X=10
  and Y1=20
  – X is feedforward in the calculation of the interpolation speed
● Kinematics with X,Y,Z,Y1,X2,O and FeedGroup X,Y,Z with KinMoveAbs
  Y1=20, O=-5.8°/s
  – Calculation of the interpolation velocity with orientation, since no axis
      included in the FeedGroup is involved.
The following FeedGroups options are currently available:
● FG_XYZ (The path dynamic limit values refer only to the Cartesian coordi‐
  nates of the command, active by default)
● FG_XYZ_O (the path dynamics limit values refer only to the Cartesian coor‐
  dinates and the orientation coordinates of the command)
● FG_XYZ_A (The path dynamic limit values refer only to the Cartesian coordi‐
  nates and the additional axes of the command)
● FG_XYZ_O_A (the path dynamics limit values refer to all coordinates and
  axes of the command)

PLC:

STRUCT ML_KinFeedGroupPData
Name       Data type   Inherited          Address   Initial value   Comment
                       from

  In       ML_KinFeed‐                                              Input: Command data of
GroupP                                                   the command
  Out      ML_oCm‐                                                  Output: Command parame‐
dOptResult                                               ters
STRUCT ML_iKinFeedGroupP EXTENDS ML_iKinCmdBase
Name        Data type   Inherited  Address     Initial value        Comment
                        from
  KinName STRING(15) ML_iKinCmd‐                                    Name of the kinematics
                        Base                                        used to execute the com‐
                                                                    mand
  Source     STRING(50)     ML_iKinCmd‐                             Specifies the command
                            Base                                    source, e.g PlcApplication1
                                                                    is displayed in the diag‐
                                                                    nostic messages
  SourceLine ULINT          ML_iKinCmd‐                             Specifies the source line of
                            Base                                    the command; is displayed
                                                                    in the diagnostic messages
  FeedGroup ML_Feed‐                                                Defined feed group
            GroupType                                               (FG_XYZ, FG_XYZ_O,
                                                                    FG_XYZ_A, FGXYZ_O_A)
  SwitchOff BOOL                                    FALSE           FALSE means that the com‐
                                                                    mand option is activated
                                                                    and (as long as it is active)
                                                                    the configured feed group
                                                                    is blended with the com‐
                                                                    manded value. Use TRUE
                                                                    to disable the command
                                                                    option and return to using
                                                                    the configured feed group.
STRUCT ML_oCmdOptResult
Name       Data type  Inherited           Address   Initial value   Comment
                      from
  Error    BOOL                                                     Error ID TRUE indicates
                                                                    that an error occurred
  ErrorID    ULINT                                                  Specifies the type of
                                                                    occurred error: The upper
                                                                    4 bytes reflect the main
                                                                    diagnostics, the lower 4
                                                                    bytes reflect the detailed
                                                                    diagnostics, 0 means no
                                                                    error

Data Layer:
Command the command option:
Method: POST
URL:                https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/opt-feed-group
Payload:

{
"type":"object","value":
{
"permType":"PermOn",
"type": "FG_XYZ_O"
}
}

Change the default value in the ctrlX MOTION configuration :
Method: WRITE
URL: https://<ip-addr>/automation/api/v2/nodes/motion/kin/<kin_name>/cfg/
dynamics/default-feedgroup
Payload:

{
"type":"object","value":
{
"feedGroup": {
"type": "FG_XYZ_O"
}
}
}

Python:
motion.kin_cmd_opt_feed_group_p( kin=<kinName>,
feedGroup=<feedgroup> )

Example: kin_cmd_opt_feed_group_p( "Kinematics", "FG_XYZ_O" )

BundleIF:

/// @brief Create a command option to overwrite the configured
path feed group (list of axes, coordinates and orientation,
that should be considered regarding path dynamics)
/// @param[in] handle       Handle of the interface
/// @param[in] sourceInfo Command source information
/// @param[in] duration     Defines whether the command option
                            is to be activated (PERMANENT_ON),
                            or deactivated (PERMANENT_OFF)
/// @param[in] kinName      Name of the kinematics object
/// @param[in] feedGroup    Chosen feedGroup (value is
                            ignored, when command option
                            is removed)
/// @return                 Status of the function call:
                            STS_OK or an error code on failure
extern "C" MotionResult MOTION_CORE_KinFeedGroup(void* handle,
const dia::CmdSourceInfo & sourceInfo, cmd::CmdOptPermType
duration, const char* kinName, cfg::FeedGroup feedGroup)

### 7.5.12 KinActivePlaneP - Selecting the active plane

Basics
The active work plane is selected with the command option. It is defined by a
main and secondary coordinate. The 3rd coordinate is always perpendicular to
the working plane. The working plane always refers to the active PCS, which
can be shifted and rotated as required in relation to the MCS.

The command option is the basis for motion on a plane-related circular/hel‐
ical path.

PLC:

STRUCT ML_KinActivePlanePData
Name       Data type     Inherited            Address   Initial value   Comment
                         from
  In       ML_KinActi‐                                                  Input: Command data of
           vePlaneP                                                     the command
  Out      ML_oCm‐                                                      Output: Command parame‐
           dOptResult                                                   ters
STRUCT ML_iKinActivePlaneP EXTENDS ML_iKinCmdBase
Name        Data type    Inherited  Address     Initial value           Comment
                         from
  KinName STRING(15) ML_iKinCmd‐                                        Name of the kinematics
                         Base                                           used to execute the com‐
                                                                        mand
   Source          STRING(50)   ML_iKinCmd‐                             Specifies the command
                                Base                                    source, e.g PlcApplication1
                                                                        is displayed in the diag‐
                                                                        nostic messages
   SourceLine ULINT             ML_iKinCmd‐                             Specifies the source line of
                                Base                                    the command; is displayed
                                                                        in the diagnostic messages
  Active‐          ML_Active‐                                           New active plane
Plane              PlaneType
ENUM ML_ActivePlaneType
Name       Data type    Inherited             Address   Initial value   Comment
                        from
  XY_Plane INT                                                          XY plane with Z perpendic‐
                                                                        ular
   YZ_Plane        INT                                                  YZ plane with X perpendic‐
                                                                        ular
   ZX_Plane        INT                                                  ZX plane with Y perpendic‐
                                                                        ular
STRUCT ML_oCmdOptResult
Name       Data type  Inherited               Address   Initial value   Comment
                      from
  Error    BOOL                                                         Error ID TRUE indicates
                                                                        that an error occurred
   ErrorID         ULINT                                                Specifies the type of
                                                                        occurred error: The upper
                                                                        4 bytes reflect the main
                                                                        diagnostics, the lower 4
                                                                        bytes reflect the detailed
                                                                        diagnostics, 0 means no
                                                                        error

Data Layer:
Command the command option:
Method: POST
URL:                https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/opt-active-plane

BundleIF:
/// @brief Create a command option to set the active plane
(e.g. for MoveCircular2D)
///
/// @param[in]     handle         Handle of the interface
/// @param[in]     sourceInfo     Command source information

/// @param[in]     duration       Defines whether the command
option is to be activated (PERMANENT_ON), or deactivated
(PERMANENT_OFF).
/// @param[in]     kinName        Name of the motion object
/// @param[in]     plane          chosen active plane (value
is ignored, when command option is removed)
/// @return                       Status of the function call:
STS_OK or an error code on failure.
Virtual MotionResult(*kinActivePlane)(void* handle, const
dia::CmdSourceInfo& sourceInfo, cmd::CmdOptPermType duration,
const char* kinName, cmd::ActivePlane plane);

Python:
motion.kin_cmd_act_plane_p( kin=<kinName>, actPlane = <plane> )

Activates/deactivates the permanent command option for the active working
plane.

<plane> - “XY_PLANE“, “ZX_PLANE“, “YZ_PLANE“

### 7.5.13 KinSwitchOnPath, KinSwitchOnPathP, KinSwitchOnPathEx, KinS‐

witchOnPathExP - Switching on the path
Brief description
The switching on path command option triggers a signal when a defined point
is passed on the path of a kinematic system. A trigger radius can be defined
around the switching point. Several switching points for one kinematic system
can be active at the same time.
The ⮫ Chapter 6.3.10 Switching on the path on page 315 contains further
information.

PLC:
Triggers a signal when a certain point on the path is reached. This command
option is only active during the next command.

STRUCT ML_iKinSwitchOnPathData
Name        Data type   Inherited        Address       Initial value   Comment
                        from

STRUCT ML_iKinSwitchOnPathData
  In        ML_iKinS‐                                            Input: Command data of
witchOn‐                                             the command option
PathCmd
  Out       ML_oCm‐                                              Output: Parameter of the
dOptResult                                           command option
ENUM ML_KinSwitchOnPathMode
Name       Data type   Inherited     Address     Initial value   Comment
                       from
           INT                                                   Action execution when
ENTER_SPHE                                                       entering the sphere
RE
ENUM ML_KinSwitchOnPathAction
Name       Data type   Inherited     Address     Initial value   Comment
                       from
           INT                                                   Sets a signal
SET_SIGNAL
           INT                                                   Resets a signal
RESET_SIGN
AL
STRUCT ML_iKinSwitchOnPath EXTENDS ML_iKinCmdBase
Name           Data type   Inherited Address   Initial value     Comment
                           from
   Mode        ML_KinSwi‐                                        Trigger algorithm to be
               chOnPath‐                                         used
               Mode
   SignalId    UDINT                           0                 Signal ID
   SignalAc‐ ML_KinS‐                                            Signal action to be exe‐
tion           witchOnPa‐                                        cuted
               thAction
   targetPosi‐ ARRAY[0..2]                     [0.0, 0.0,        Trigger point in the
tion           OF LREAL                        0.0]              machine coordinate system
   Radius      LREAL                           0.0               Radius around the trigger
                                                                 point
  PreTrigger‐ LREAL                              0.0             Release time before
Time                                                             reaching the trigger point
STRUCT ML_oCmdOptResult
Name       Data type  Inherited      Address     Initial value   Comment
                      from
  Error    BOOL                                                  Error ID, TRUE indicates
                                                                 that an error occurred
   ErrorID         UDINT                                         Specifies the type of the
                                                                 occurred error (currently
                                                                 not in use, is always set to
                                                                 1)

        PLC:

     ML_KinSwitchOnPathP triggers a signal when a certain point on the path
     is reached. This command option remains active during all subsequent com‐
     mands until the signal is triggered or a non-buffered command becomes
     active.

STRUCT ML_iKinSwitchOnPathPData
Name        Data type   Inherited       Address      Initial value   Comment
                        from

  In        ML_iKinS‐                                                Input: Command data of
witchOn‐                                                 the command option
PathP
  Out       ML_oCm‐                                                  Output: Parameter of the
dOptResult                                               command option
ENUM ML_KinSwitchOnPathMode
Name       Data type   Inherited        Address      Initial value   Comment
                       from
           INT                                                       Action execution when
ENTER_SPHE                                                           entering the sphere
RE
ENUM ML_KinSwitchOnPathAction
Name       Data type   Inherited        Address      Initial value   Comment
                       from
           INT                                                       Sets a signal
SET_SIGNAL
           INT                                                       Resets a signal
RESET_SIGN
AL
STRUCT ML_iKinSwitchOnPathP EXTENDS ML_iKinSwithOnPath
Name           Data type   Inherited    Address Initial value        Comment
                           from
   Mode        ML_KinSwi‐ iKinSwitch‐                                Trigger algorithm to be
               chOnPath‐   OnPath                                    used
               Mode
   SignalId    UDINT       iKinSwitch‐          0                    Signal ID
                           OnPath
   SignalAc‐ ML_KinS‐      iKinSwitch‐                               Signal action to be exe‐
tion           witchOnPa‐ OnPath                                     cuted
               thAction
   targetPosi‐ ARRAY[0..2] iKinSwitch‐          [0.0, 0.0,           Trigger point in the
tion           OF LREAL    OnPath               0.0]                 machine coordinate system
   Radius      LREAL       iKinSwithOn‐         0.0                  Radius around the trigger
                           Path                                      point
   PreTrigger‐ LREAL       iKinSwithOn‐         0.0                  Release time before
Time                       Path                                      reaching the trigger point

STRUCT ML_iKinSwitchOnPathP EXTENDS ML_iKinSwithOnPath
  SwitchOff BOOL                                                           FALSE: Enables the com‐
                                                    mand option
                                                    TRUE: Switches the com‐
                                                    mand option off
STRUCT ML_oCmdOptResult
Name       Data type  Inherited              Address       Initial value   Comment
                      from
  Error    BOOL                                                            Error ID, TRUE indicates
                                                                           that an error occurred
   ErrorID         UDINT                                                   Specifies the type of the
                                                                           occurred error (currently
                                                                           not in use, is always set to
                                                                           1)

PLC:
The "SwitchOnPath" function has some limitations that no longer apply with
"SwitchOnPathEx" (as in "extended").
This allows the reference point to be specified in different coordinate systems
in "SwitchOnPathEx." While the TCP (Tool Center Point) is always specified
in the MCS (Machine Coordinate System) for "SwitchOnPath," the reference
point for "SwitchOnPathEx" can also be specified in the WCS (World Coordi‐
nate System) or the PCS (Product Coordinate System). In addition, you can
also refer to the flange (tool holder) in the MCS.
Furthermore, "SwitchOnPathEx" also supports motions for which no com‐
manded path existed (such as MoveDirect or Blending). The distance from the
current TCP to the reference point is correctly determined using "SwitchOnPa‐
thEx," and the signal switches correctly.
Finally, "SwitchOnPathEx" also has a special "Interrupt" action. "SwitchOnPa‐
thEx" with the "Interrupt" action is intended for applications in which the
TCP is not allowed to enter a specific section of the commanded path until
authorization has been granted. In this case, the command signal (command
parameter) is interpreted not as an output (as with other actions), but as an
input ("enable signal").
If "SwitchOnPathEx" has been commanded with the "Interrupt" action, it
behaves as follows depending on the enable signal:
● If the signal is set to 1 at the trigger time (i.e., when the TCP is closer
   to the reference point than the specified radius), nothing happens. The
   kinematics simply follows the specified dynamics along the specified path
● If the signal is at 0 at the trigger time, Motion automatically initiates an
   interrupt command. Kinematics decelerates on the path
● If the enable signal is set to 1 during this braking process or after the
   system has come to a stop, the kinematic system accelerates again and con‐
   tinues moving along the commanded path with the commanded dynamics.
The action can be used as follows for the "restricted area" use case:
1.    Use the Motion module to calculate the braking distance (the "motion/
      state/brake-ramp" function in the Data Layer or "ML_GetBrakeRam‐
      pLength" in the PLC).
2.    This length is used as the radius in "SwitchOnPathEx."
3.    The reference point marks the beginning of the restricted area on the
      designated route.

      4.      The "SwitchOnPathEx" command option is triggered by the "Interrupt"
              action.
      5.      The PLC can now control whether the kinematic system moves into the
              prohibited area or stops short of it by clearing or setting the enable
              signal.
      PLC:

STRUCT ML_iKinSwitchOnPathExData
Name        Data type   Inherited             Address      Initial value   Comment
                        from
  In        ML_iKinS‐                                                      Input: Command data of
            witchOnPa‐                                                     the command option
            thEx
  Out       ML_oCm‐                                                        Output: Parameter of the
            dOptResult                                                     command option
ENUM ML_KinSwitchOnPathAction
Name       Data type   Inherited              Address      Initial value   Comment
                       from
           INT                                             0               Sets a signal
SET_SIGNAL
           INT                                                             Resets a signal
RESET_SIGN
AL
           INT                                                             Sets an interrupt
SET_INTER‐
RUPT
STRUCT ML_iKinSwitchOnPathEx EXTENDS ML_iKinCmdBase
Name        Data type   Inherited  Address     Initial value               Comment
                        from
  KinName STRING(63) ML_iKinCmd‐                                           Name of the kinematics
                        Base                                               used to execute the com‐
                                                                           mand
  Source       STRING(50)       ML_iKinCmd‐                                Specifies the command
                                Base                                       source, e.g PlcApplication1
                                                                           is displayed in the diag‐
                                                                           nostic messages
  SourceLine ULINT              ML_iKinCmd‐                                Specifies the source line of
                                Base                                       the command; is displayed
                                                                           in the diagnostic messages
  Mode         ML_KinSwi‐                                                  Trigger algorithm to be
               chOnPath‐                                                   used
               Mode
   SignalId    UDINT                                                       Signal ID
   SignalAc‐   ML_KinS‐                                                    Signal action to be exe‐
tion           witchOnPa‐                                                  cuted
               thAction

STRUCT ML_iKinSwitchOnPathEx EXTENDS ML_iKinCmdBase
   TargetPosi‐ ARRAY[0..2]                                      Trigger point in the
tion           OF LREAL                                         machine coordinate system
   TargetPo‐ ML_Switch‐                                         Coordinate system for the
sCOS           OnPathCOS‐                                       reference position
Type
   Radius      LREAL                                            Radius around the trigger
                                                 point
  PreTrigger‐ LREAL                                             Release time before
Time                                                            reaching the trigger point

        PLC:

STRUCT ML_iKinSwitchOnPathExP EXTENDS ML_iKinSwitchOnPathEx
Name           Data type   Inherited   Address  Initial value Comment
                           from
   KinName STRING(63) ML_iKinCmd‐                             Name of the kinematics
                           Base                               used to execute the com‐
                                                              mand
   Source      STRING(50) ML_iKinCmd‐                         Specifies the command
                           Base                               source, e.g PlcApplication1
                                                              is displayed in the diag‐
                                                              nostic messages
   SourceLine ULINT        ML_iKinCmd‐                        Specifies the source line of
                           Base                               the command; is displayed
                                                              in the diagnostic messages
   Mode        ML_KinSwi‐ ML_iKinS‐                           Trigger algorithm to be
               chOnPath‐   witchOnPa‐                         used
               Mode        thEx
   SignalId    UDINT       ML_iKinS‐                          Signal ID
                           witchOnPa‐
                           thEx
   SignalAc‐ ML_KinS‐      ML_iKinS‐                          Signal action to be exe‐
tion           witchOnPa‐ witchOnPa‐                          cuted
               thAction    thEx
   TargetPosi‐ ARRAY[0..2] ML_iKinS‐                          Trigger point in the
tion           OF LREAL    witchOnPa‐                         machine coordinate system
                           thEx
   TargetPo‐ ML_Switch‐ ML_iKinS‐                             Coordinate system for the
sCOS           OnPathCOS‐ witchOnPa‐                          reference position
               Type        thEx
   Radius      LREAL       ML_iKinS‐                          Radius around the trigger
                           witchOnPa‐                         point
                           thEx

STRUCT ML_iKinSwitchOnPathExP EXTENDS ML_iKinSwitchOnPathEx
  PreTrigger‐ LREAL     ML_iKinS‐                           Release time before
Time                    witchOnPa‐                          reaching the trigger point
    thEx
  SwitchOff BOOL                                            FALSE: Enables the com‐
                                        mand option
                                        TRUE: Switches the com‐
                                        mand option off

Data layer
Method: POST
URL:                https://<ip-addr>/automation/api/v2/nodes/motion/kin/

<kin_name>/cmd/opt-switch-on-path
Payload:
{
    "permType": "Once",
    "mode": ENTER_SPHERE,
    "signalId": 0,
    "signalAction": SET_SIGNAL,
    "targetPosition": [1, 0, 2],
    "radius": 0.05,
    "preTriggerTime": 0.0
}

Python:
kin_cmd_opt_switch_on_path(kin: str, mode: int, signal_id:
int, action: int, target_position: Tuple[float, ...], radius:
float, pre_trigger_time: float) -> None:

Enables a command option that triggers a signal if a kinematics reaches a
certain target position within the next motion command (object has to be
“attached”), see documentation Python Runtime App ⮫ Python Functions.
If the target position is reached within the sphere with the specified radius,
the signal specified by the "signal_id" is triggered. If the target position has
already been reached upon the start of the command, the signal specified by
the "signal_id" is triggered directly. Several target positions and/or signal IDs
can be positioned in a queue by executing this command option several times.
● kin
  Kinematic name
● mode
  Algorithm to be used (entry into sphere = 0)
● signal_id
  The ID of the signal
● action
  Action to be executed (set signal = 0, reset signal = 1)
● target_position
  Switching position (array [x, y, z]) for triggering the signal in the machine
  coordinate system
● radius
  Radius of the sphere around the switching position
● pre_trigger_time
  Signal triggering when the target position is reached within the specified
  time. This is decided based on the current velocity and direction

Python:
kin_cmd_opt_switch_on_path_p(kin: str, mode: Optional[int] =
None, signal_id: Optional[int] = None, action: Optional[int]
= None, target_position: Optional[Tuple[float, ...]] =
None, radius: Optional[float] = None, pre_trigger_time:
Optional[float] = None) -> None:

Triggers a signal when a certain point on the path is reached. This com‐
mand option remains active during all subsequent commands until the signal
is triggered or a non-buffered command becomes active (object has to be
"attached"), see documentation Python Runtime App ⮫ Python Functions.
If the target position is reached within the sphere with the specified radius,
the signal specified by the "signal_id" is triggered. If the target position has
already been reached upon the start of the command, the signal specified by
the "signal_id" is triggered directly. Several target positions and/or signal IDs
can be positioned in a queue by executing this command option several times.
If the command option is only executed with the "kin" parameter, all previous
switching positions of all signal IDs are deleted.
● kin
  Kinematic name
● mode
  Algorithm to be used (entry into sphere = 0)
● signal_id
  The ID of the signal
● action
  Action to be executed (set signal = 0, reset signal = 1)
● target_position
  Switching position (array [x, y, z]) for triggering the signal in the machine
  coordinate system
● radius
  Radius of the sphere around the switching position
● pre_trigger_time
  Signal triggering when the target position is reached within the specified
  time. This is decided based on the current velocity and direction

BundleIF:

namespace motion::somo
{
    /// Types of algorithms available to detect reaching the
    /// target position
    enum class SwitchOnPathMode : uint32_t
    {
        ENTER_SPHERE = 0    ///< Perform the action when
                            ///< entering the sphere
    };

     /// Action to perform when reaching the target position
     enum class SwitchOnPathAction : uint32_t
     {
         SET_SIGNAL = 0,     ///< Set a signal
         RESET_SIGNAL        ///< Reset a signal
     };
}

/// @brief Create a motion command option to trigger a signal
///         when a kinematics reaches a specified target
///         position
///
/// When the target position is reached within the sphere
/// defined by the specified radius, the signal specified by
/// signalId is triggered.
/// If the target position is already reached when the command
/// starts, the signal specified by signalId is triggered.
/// Multiple target positions and/or signal ids can be queued
/// by issuing this command option multiple times with
/// duration = ONCE or duration = PERMANENT_ON.

                                                                         Commands
/// When issuing with duration = PERMANENT_OFF, all queued
/// target positions with duration = PERMANENT_ON for the
/// given kinematics are removed.
///
/// @param[in] handle           Handle of the MotionCmdIf2T
///                             interface
/// @param[in] sourceInfo       Command source information
/// @param[in] duration         Defines whether the command
///                             option is to be activated,
///                             either ONCE or PERMANENT_ON,
///                             or deactivated, PERMANENT_OFF
/// @param[in] kinName          Name of the kinematics motion
///                             object
/// @param[in] mode             Type of algorithm to use
/// @param[in] signalId         The signal id
/// @param[in] action           Desired action to execute with
///                             the signal
/// @param[in] targetPosition Target position
///                             (array [x, y, z]) for switching
///                             (issuing the signal)
///                             [Machine Coordinate System]
/// @param[in] radius           Radius of the sphere around the
///                             target position
/// @param[in] preTriggerTime Trigger the signal when the
///                             target position will be reached
///                             (estimation, based on the
///                             current direction and velocity
///                             of the movement) within the
///                             given time
///
/// @retval     STS_OK Succesfully created the command option
/// @retval     ERR_*   Failed to create the command option
extern "C" MotionResult
MOTION_CORE_kinSwitchOnPathCmdOpt(void* handle,
const ::motion::core::dia::CmdSourceInfo&
sourceInfo, ::motion::core::cmd::CmdOptPermType duration,
const char* kinName, ::motion::somo::SwitchOnPathMode mode,
uint32_t signalId, ::motion::somo::SwitchOnPathAction action,
const double* targetPosition, double radius, double
preTriggerTime);

### 7.5.14 KinBeltSyncP - Belt-synchronous

Basics
The command option is used to activate the synchronization of a kinematics
with a belt.
The functional principle and the configuration are described in ⮫ Chapter
6.3.7 Belt-synchronous motion on page 283

PLC:

STRUCT ML_KinBeltSyncPData
Name       Data type    Inherited             Address      Initial value   Comment
                        from
  In       ML_KinBelt‐                                                     Input: Command data of
           SyncP                                                           the command
  Out      ML_oCm‐                                                         Output: Command parame‐
           dOptResult                                                      ters
STRUCT ML_iKinBeltSyncP EXTENDS ML_iKinCmdBase
Name        Data type    Inherited  Address    Initial value               Comment
                         from
  KinName STRING(63) ML_iKinCmd‐                                           Name of the kinematics
                         Base                                              used to execute the com‐
                                                                           mand
   Source          STRING(50)   ML_iKinCmd‐                                Specifies the command
                                Base                                       source, e.g PlcApplication1
                                                                           is displayed in the diag‐
                                                                           nostic messages
   SourceLine ULINT             ML_iKinCmd‐                                Specifies the source line of
                                Base                                       the command; is displayed
                                                                           in the diagnostic messages
  BeltName         STRING                                                  Belt object name
BeltValue          LREAL                                                   Belt value to which all sub‐
                                                                           sequent motion commands
                                                                           refer
SwitchOff          BOOL                                    FALSE           FALSE means that the com‐
                                                                           mand option is enabled
                                                                           permanently, use TRUE
                                                                           to disable the command
                                                                           option again

PLC:
In the PLC, the current belt value can be called in real time using the ML_Axs‐
GetBeltValueRT function.

STRUCT ML_AxsGetBeltValueData
Name       Data type    Inherited         Address         Initial value   Comment
                        from
  In       ML_iAxsSta‐                                                    Input: Command data of
           teBase                                                         the command

  Out      ML_oAxsGet‐                                                    Output: Command parame‐
BeltValue                                                      ters
ML_iAxsStateBase
Name         Data type        Inherited   Address         Initial value   Comment
                              from
  AxsName    STRING(63)                                                   Axis name
ML_oAxsGetBeltValue EXTENDS ML_oStateBase
AxisName   Data type     Inherited  Address               Initial value   Comment
                         from
  Error    BOOL          ML_oState‐                                       Error flag
                         Base
  ErrorID  ULINT         ML_oState‐                                       Error type
                         Base
  Position LREAL                                                          Current belt position

Data Layer:
Command the command option:
Method: POST
URL:                https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/opt-belt-plane
Content:
Element                   Data type                     Description
permType                  String                        Switching on, switching
                                                        off the command option
                                                        ● "PermOn"
                                                        ● "PermOff"
beltName                  String                        Belt name
beltValue                 double                        Belt value

Example:
{
        "permType": "",
        "beltName": "",
        "beltValue": 0
}

Python:
motion.kin_cmd_opt_belt_sync_p(       kin=<kinName>       [,belt=<beltName>]
[,value=<beltValue>] )

Activates/deactivates the permanent command option for synchronizing a kine‐
matic with a belt.
All subsequent motion commands refer to the belt value, i.e. the difference
between the current belt value and the "BeltValue" commanded here is added
to the target position. With the first motion command, the kinematic synchro‐
nizes with the belt and moves synchronously with the belt until the command
option is deactivated and a subsequent motion command is executed for
desynchronization.
If no optional parameters are programmed, the command option is disabled.
The kinematics has to be assigned to the script instance.
● <kinName> - string; kinematic name
● <beltName> - string; name of the belt with which the kinematics is to be
   synchronized.
● <beltValue> - double; belt value to which all subsequent motion commands
   refer.
The belt value is commanded in the unit configured in the axis configura‐
tion parameter "motion/axs//[name]/cfg/functions/belt nominatorUnitOfBelt‐
ConversionFactor".
The bundle IF function MotionData::getAxisBeltValue(..) returns the value con‐
verted to the unit.
