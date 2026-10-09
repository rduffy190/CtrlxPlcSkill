# 6.3 Kinematic functions

### 6.3.1 Position and orientation in space

For most machining processes, it is necessary to move a tool to different
positions, or if required, to move the tool along a defined path. Examples
include pick-and-place applications or a welding process on a component. In
addition to specifying a target position, an orientation can also be defined for
the motion. This is required for a process such as gluing in order to move
along a path in space so that the tool is at a certain angle to the workpiece to
be processed. The combination of position and orientation is referred to as a
pose in space. The following section explains how the required positions can
be defined in different coordinate systems before going into more detail on
orientations.
Coordinate systems
A Cartesian coordinate system is usually used for positions in space. This con‐
sists of three mutually perpendicular axes, whereby the position is specified
by the distance to the origin of the axes in the x, y and z directions. These
distances px, py and pz are shown as dashed lines in the image below.

Different Cartesian coordinate systems can be used in space, which differ in
the position of their origin or the direction of the axes. When describing a
point, it is therefore always important to specify which coordinate system is
referred to. In ctrlX CORE, it is distinguished between the following coordi‐
nate systems:
World Coordinate System: (WCS)
The world coordinate system (WCS) is usually fixed to the ground and thus
defines a reference system that is independent of the motion of various
machines or the position of components to be machined. An example of a
WCS could be the corner of a robot cell or factory floor. If there are multiple
robots in the WCS, an offset for the machine coordinate system of each robot
has to be defined.
Machine Coordinate System: (MCS)
The machine coordinate system (MCS) is permanently connected to the base
of the machine. In the case of a robot, for example, this would be the base of
a robot, whereby the z-axis of the MCS often corresponds to the first rotary
axis. Positions can thus be easily described in the work zone of the machine.
In other controls, the machine coordinate system is sometimes referred to as
the basic coordinate system.
Flange Coordinate System: (FCS)
The flange coordinate system (FCS) is located at the center of the end effector
of a robot and represents the pick-up option for a tool. While the MCS and
WCS are normally stationary during a process, the FCS moves with every
robot motion.
Tool Coordinate System: (TCS)
The tool coordinate system (TCS) has its origin at the tool center point: (TCP)
and points with the z-axis in the direction of impact of the tool. In a gluing
process, the TCP would be the exit point of the adhesive at the tip of the
tool, in a gripper, the center point between the two gripper jaws. The TCS is
usually defined as a simple displacement relative to the flange.
This coordinate system is particularly suited for jogging tool motions.
When jogging in the TCS, it must be complied with the defined z-direction of
the flange or TCP of the active axis transformation, as this differs for the var‐
ious axis transformations. This can point away from the flange, as in ⮫ Further
information on page 176, as well as towards the flange.

                                                        +B
                                                        y
     z
                                                               x              +X
                                              TCS
                     y
                                                                   z

 MCS                     x
Product Coordinate System: (PCS)
It is possible to define several product coordinate systems (PCS). Examples of
this would be a machining table or the workpiece to be machined. This allows
points or paths to be defined relative to a workpiece or table, facilitating
changes to the setup. For example, after moving a workpiece, the position of
the PCS would simply have to be updated instead of having to recalculate
or redefine all paths. Common designations in other control systems are work‐
piece, object or program coordinate system.
The image below shows the coordinate systems described in an example
scene.

Axis Coordinate System (ACS)
In addition to Cartesian coordinate systems, it is also possible to describe
positions in space using the axis values of a mechanical system. The axis
coordinate system (ACS) is used for this purpose. The rotation angles of the
rotary axes or distances of the linear axes of a mechanism are noted. In
the following figure, the position of the robot shown in the ACS would be
described by the values of its two rotary axes with the values α = 30° and β =
-45° and its linear axis with z = 50 mm.

Commanding in different coordinate systems

When commanding motion commands of ctrlX MOTION you can choose
between the following coordinate system types mentioned above in addition
to position and orientation: ACS, MCS, WCS and PCS. Commanding in FCS
and TCS is not yet possible at the moment. It should also be noted that a pair
of coordinate systems is always implicitly specified for Cartesian coordinate
systems; for example, linear traversing in the MCS means moving the flange
(i.e. the flange coordinate system FCS) to a pose defined in the MCS. A more
detailed explanation can be found in the chapter on motion commands for
kinematics.
The KinCoordTransform auxiliary function is available for converting from
one coordinate system to another (⮫ Chapter 7.8.3 KinCoordTransform - Con‐
verting the coordinate system on page 776).

Relevant parameters
Dynamic limit values for orientation
Functional description:
The configured dynamic limit values of the orientation have an influence on
the dynamic limit values of the (Cartesian) path.
A motion with a small Cartesian component and a large orientation motion
would result in a very fast orientation motion. This is limited by the dynamic
limit values of the orientation.

Currently, only the velocity limit value of the orientation is taken into account
for limiting the path dynamics.

If the share of the orientation velocity in the web velocity exceeds the limit
value of the configured velocity, the web velocity is reduced proportionally so
that the limit value is not exceeded.
This is done according to this formula:
● oriVel = ipoVel * oriFactor / Lin2RotConversionFactor
oriVel:                     Orientation velocity
ipoVel:                     Web velocity
oriFactor:                  Coupling factor between the
                            interpolation path length and the
                            orientation path
Lin2RotConversionFactor: Configuration parameters for the
                            conversion between rotational
                            (orientation) and linear (Cartesian path)
                            Motion components

If the orientation velocity is greater than the limit value of the orientation
speed:
● ipoVelMax = oriVelMax * Lin2RotConversionFactor/oriFactor
The dynamic limit values for the orientation motion can be configured in the
ctrlX MOTION user interface or directly in the Data Layer.
Data Layer:
URL              Command                Result
motion/kin/      read/write             Reads or writes the dynamic limits for
[name]/cfg/geom‐                        the orientation
etry/orienta‐
tion/lim

Method: READ/WRITE
Payload:
{
    "vel": 45,
    "acc": 90,
    "dec": 90,
    "jrkAcc": 180,
    "jrkDec": 180,
    "velUnit": "deg/s",
    "accUnit": "deg/s^2",
    "decUnit": "deg/s^2",
    "jrkAccUnit": "deg/s^3",
    "jrkDecUnit": "deg/s^3"

}

Conversion factor between rotary and linear motion parts
Functional description:
In many cases, a kinematic motion contains both Cartesian path parts and
orientation parts. Auxiliary axes can also be assigned to the kinematics.
A dynamic calculation therefore includes both rotational and linear motion
parts.
Motion part                            Motion type
Cartesian orbit                        linear
Orientation                            rotary
Linear auxiliary axes                  linear
Rotary auxiliary axis                  rotary
All these motion parts have to be scaled in relation to each other in order to
determine valid limit values.
This scaling can be set by the user with the configuration parameter "rot-to-
lin-conversion-factor".
A typical value would be, for example, 1°==1mm. This means that a rotational
motion of 1° has the same influence on the dynamics of the kinematics as a
traversing motion in Cartesian space of 1 mm in length.
The conversion factor between rotary and linear motion components can be
configured in the ctrlX MOTION user interface or directly in the Data Layer.
Data Layer:
URL                  Command           Result
motion/kin/          read/write        Reads or writes the conversion factor
[name]/cfg/geom‐                       to convert rotary values into linear
etry/orienta‐                          values
tion/rot-to-lin-con‐
version-factor
Method: READ/WRITE
Payload:
{
     “factor”:1,
     “unit_lin”: “mm”,
    “unit_rot”: “deg”
}

### 6.3.2 Orientation & rotation

General information

As mentioned above, an orientation can also be specified for a process in
addition to the position. The orientations that can be achieved with the tool
in space depend on the kinematics on which the tool is installed. While a
6-axis robot, for example, has all three degrees of freedom for orientations, a
5-axis robot may only be able to rotate the tool around the y- and z-axes and a
SCARA robot only around the z-axis.
The following illustration shows a gripper that is oriented by a rotation so that
it is able to grip the workpiece. You can clearly see how the TCS connected
to the gripper changes its orientation depending on the situation. Similar to
the positions, the reference coordinate system is essential for describing the
orientation; it makes a difference whether the orientation of the gripper is
described in the PCS or WCS. The same applies to a rotation that is applied
to an existing orientation. A rotation around the z-axis in the TCS results in a
different end orientation than a rotation around the z-axis in the MCS.

There are now several formalisms for describing orientations and rotations.
Axis and angle as well as Euler angle are discussed below.
Axis and angle
An orientation can be defined as the result of a rotation of the original coordi‐
nate system around a freely selectable spatial axis. This axis is specified as a
vector in space. The direction of rotation always follows the "right-hand rule":

If the thumb of the right hand points in the direction of the axis of rotation,
rotation takes place in the direction of the remaining fingers. You also define
an angle that specifies how far you want to rotate.
Example of the axis and angle representation:
In the following illustration, a rotation of 45° around the rotary axis (20, 30,
40) is performed. The original orientation is shown on the left and the target
orientation on the right.

This rotation process can be represented on a sphere, whereas the rotation
of the coordinate axes takes place along a circular path on a plane, perpendic‐
ular to the rotary axis.

Euler angle
The so-called Euler angles are another way of describing an orientation. In this
notation, three angles are used to determine how a body is oriented relative
to a reference system. These angles are usually labeled α, β, γ, or ψ, θ, φ, or
A, B, C. The orientation results from successive rotations around the specified
angles. The rotary axes correspond to the axes of the coordinate system.
There are 24 different possible, valid combinations of the rotary axes (e.g.
X-Y-Z or Z-X-Z). The choice of specific rotary axes and their sequence is known
as the Euler convention. It is also important to specify whether the rotary axes
for the second and third rotation refer to the co-rotated or the original, fixed
coordinate system. This is referred to as intrinsic or extrinsic representation.
Extrinsic representation
In the extrinsic representation, all rotations refer to the axes of the original,
fixed coordinate system, which is assumed to be fixed. For the X-Y-Z conven‐
tion, this means that the first rotation is around the x-axis. It is then rotated
around the original y-axis and finally around the original z-axis. The extrinsic
representation is sometimes also referred to as "fixed-frame".
Example of extrinsic representation:
In the following example, a rotation with the Euler convention XYZ (extrinsic)
with the values α = 35°, β = -20° and γ = 45° is to take place. The first step is
to rotate around the original x-axis of the reference system by α = 35°. As we
are currently still in the start orientation, the rotary axis also corresponds to
the current x-axis.

The next step is to rotate around the original y-axis of the reference system,
i.e. the non-rotated coordinate system by β = -20°. As the first step has already
rotated around a different axis, the axis of rotation no longer matches the

current y-axis.

In the last step, the coordinate system is rotated by γ = 45° around the orig‐
inal z-axis of the reference system. Here too, the rotary axis does not match
the current z-axis.

Intrinsic representation
In the intrinsic representation, the respective rotations refer to the current,
co-rotated coordinate system. As a result, the rotary axes for the second and
third angles depend on the previous rotations. In order to make the differ‐
ence between the Euler convention and the extrinsic representation clear, the
rotated axes are identified by an apostrophe, e.g. X-Y'-Z''. In this example, this
means that the first rotation takes place around the x-axis. The second rota‐
tion then takes place around the y-axis, which is also rotated, and the third
rotation takes place around the z-axis, which is rotated twice. The intrinsic
representation is sometimes also referred to as "current-frame".
Example of intrinsic representation:
In the example below, the individual steps for a rotation with the Euler con‐
vention XY'Z'' (intrinsic) with the values α = 20°, β = -25° and γ = 45° are
shown. In the first step, the original x-axis of the reference system is rotated
by α = 20°.

 Next, the coordinate system is rotated around the new y-axis by β = -25°. In
 the figure below, you can clearly see the difference to the extrinsic representa‐
 tion before, where, in contrast, the original y-axis was rotated.

 Finally, the system is rotated by γ = 45° around the current z-axis (which has
 already been rotated twice):

 Conversion between extrinsic and intrinsic representation
 It is easy to convert between intrinsic and extrinsic representation. To get
 from the extrinsic representation X-Y-Z with the angles A, B, C to the intrinsic
 representation, the order of the rotary axes first have to be reversed. The
 corresponding Euler convention thus becomes Z-Y'-X''. Subsequently, the cor‐
 responding angles also have to be swapped, i.e. the rotations with the angles
 have to be carried out in the order C, B, A.

### 6.3.3 Substitute function

Substitute function for kinematic axes
ctrlX MOTION allows the user to assign different axes to a kinematic system.
This assignment can be changed during operation. In many cases, however,
the assignment of the axes to the kinematics is clear. That means: A maximum
of one axis is assigned to each axis index of the kinematics and a maximum of
one kinematics is assigned to each axis.
For applications that can change the axis assignment during operation, the
substitute function for kinematic axes can be used. The actual axis positions
are mirrored in the actual position of the kinematics, even if the axes have not
yet been added to the kinematics by command (⮫ Chapter 7.2.42 AxsAddToKin

- Adding the axis to the kinematics on page 512). This means that in this case
there is a clear difference between the actual position and the target position
of the kinematics. The command values are still disconnected, but the actual
values are already read from the axes.
The substitute function is only active if the configuration of the kinematic axes
is unique. This check is carried out for each axis. This means that the function
may be active for some - but not all - axes.
The substitute function only acts in the direction of axes to the kinematics
(actual values). If the axes are to be moved by the kinematics, they have to be
added to the kinematics as before (⮫ Chapter 7.2.42 AxsAddToKin - Adding the
axis to the kinematics on page 512).

Checking and starting the substitute function

This method checks whether an error-free kinematic configuration exists and
whether the substitute function can therefore work:
URL                Command              Result
motion/kin/        Method               Starts the check whether the configu‐
[name]/cfg/valida‐                      ration of the kinematic axes is unique
tion/kin-axis-cfg-                      and returns the result
unambiguous
Also refer to ⮫ Substitute function active on page 187

Substitute function active
In the Data Layer node of the kinematics, you can check whether the substi‐
tute function is active:
URL                 Command             Result
motion/kin/         read                Result of the check as to whether the
[name]/state/                           configuration of the kinematic axes is
capabilities/kin-                       unique and therefore the substitute
axis-cfg-unambig‐                       function is active
uous
Example of a unique configuration of the kinematic axes:
{
        "count": 1,
        "mainDiag": 0,
        "detailDiag": 0
}
Example of an ambiguous configuration of the kinematic axes:
{
        "count": 0,
        "mainDiag": 151978066,
        "detailDiag": 206963387,
        "addInfo": "Axis configuration ambiguous",
        "uri": "motion/kin/Robot/cfg/kin-axs",
        "moreInfo": [
            {
                "count": 0,
                "mainDiag": 206963382,
                "detailDiag": 206963382,
                "addInfo": "Axes R2 and Axis_1 are both at index
1",
               "uri": "motion/kin/Robot/cfg/kin-axs"

          }
      ]
}

Disabling the substitute function
In certain cases, the behavior of the substitute function may be undesirable.
In these cases, the substitute function can be switched off in the kinematic
configuration. A Data Layer node is provided:
URL                 Command            Result
motion/kin/         bool               Setting whether the substitute func‐
[name]/cfg/coord-                      tion for kinematic axes should be used
systems/set‐
tings/use-kin-axes-
fallback
The substitute function can only be switched off for all axes of a kinematic
system. It is not possible to switch off individual axes.

Conversion factor between rotary and linear motion parts
Functional description:
In many cases, a kinematic motion contains both Cartesian path parts and
orientation parts. Auxiliary axes can also be assigned to the kinematics.
A dynamic calculation therefore includes both rotational and linear motion
parts.
Motion part                            Motion type
Cartesian orbit                        linear
Orientation                            rotary
Linear auxiliary axes                  linear
Rotary auxiliary axis                  rotary
All these motion parts have to be scaled in relation to each other in order to
determine valid limit values.
This scaling can be set by the user with the configuration parameter "rot-to-
lin-conversion-factor".
A typical value would be, for example, 1°==1mm. This means that a rotational
motion of 1° has the same influence on the dynamics of the kinematics as a
traversing motion in Cartesian space of 1 mm in length.
The conversion factor between rotary and linear motion components can be
configured in the ctrlX MOTION user interface or directly in the Data Layer.
Data Layer:
URL                  Command           Result
motion/kin/          read/write        Reads or writes the conversion factor
[name]/cfg/geom‐                       to convert rotary values into linear
etry/orienta‐                          values
tion/rot-to-lin-con‐
version-factor
Method: READ/WRITE
Payload:
{
     “factor”:1,
     “unit_lin”: “mm”,
    “unit_rot”: “deg”
}

    Substitute function axis transformations of a kinematic system
In ctrlX MOTION, various axis transformations (see ⮫ Chapter Introduction
and overview on page 192) can be actively switched in a kinematic system.
These transformations can be changed during operation (see ⮫ Chapter 7.5.3
KinMCSP - Command options for kinematics machine coordinate system
on page 645).
In many cases, however, the axis transformation assignment to a kinematic
system cannot be changed. This means that the kinematics has either exactly
one basic transformation (e.g. ⮫ Chapter Axis transformation for 6-axis robots
with spherical hand on page 201) or a basic transformation with an additional
orientation transformation (e.g. ⮫ Chapter Axis transformation for delta robots
on page 224 with additional 2-D orientation transformation). The transforma‐
tions are not switched.

In many cases, however, the axis transformation assignment to a kinematic
system cannot be changed. This means that the kinematics have either exactly
one basic transformation (e.g. serial 6-axis robot) or a basic transformation
with an additional orientation transformation (e.g. delta kinematics with addi‐
tional 2-D orientation transformation). The transformations are not switched.
For these applications, a substitute function for axis transformations of kine‐
matics is implemented in ctrlX MOTION. This means that the one configured
base transformation or the pair of base transformation and orientation trans‐
formation is active if no other transformation has been commanded. This basic
transformation (or the pair of basic transformation and orientation transfor‐
mation) does not have to be activated by a command.
The substitute function is only active if the configuration of the axis transfor‐
mations of a kinematic system is unique. To do this, the parameters of the
transformation has to be valid and all necessary axes have to be available
via the substitute function of the axes (see ⮫ Chapter Substitute function for
kinematic axes on page 186). No further transformations may be configured in
the kinematics.

Checking and starting the substitute function
This method checks whether an error-free kinematic configuration exists and
whether the substitute function can therefore work:
URL                 Command             Result
motion/kin/         Method              Starts the check whether the configu‐
[name]/cfg/valida‐                      ration of the axis transformations is
tion/kin-kin-joint-                     unique and returns the result
trafo-unambiguous
Also refer to ⮫ Substitute function active on page 187

Substitute function active
In the Data Layer node of the kinematics, you can check whether the substi‐
tute function for axis transformations is active:
URL                 Command             Result
motion/kin/         read                Result of the check whether the con‐
[name]/state/                           figuration of the axis transformations
capabilities/joint-                     is unique and therefore the replace‐
trafo-cfg-unambig‐                      ment function is active
uous
Example of a unique configuration of the kinematic axes:

{
    "count": 1,
    "mainDiag": 0,
    "detailDiag": 0
}
Example of an ambiguous configuration of the kinematic axes:
{
    "count": 0,
    "mainDiag": 151978066,
    "detailDiag": 206963388,
    "addInfo": "Axis transformation configuration ambiguous",
    "uri": "motion/kin/Robot/cfg/coord-systems/mcs",
    "moreInfo": [
        {
            "count": 0,
            "mainDiag": 206897942,
            "detailDiag": 206897942,
            "addInfo": "MCS set Scara_LinearAxisBase is
invalid",
            "uri": "motion/kin/Robot/cfg/coord-systems/mcs/
Scara_LinearAxisBase"
        }
    ]
}

Disabling the substitute function
In certain cases, the behavior of the substitute function may be undesirable.
In these cases, the substitute function can be switched off in the kinematic
configuration. A Data Layer node is provided:
URL               Command              Result
motion/kin/       bool                 Setting whether the substitute func‐
[name]/cfg/coord-                      tion should be used for axis transfor‐
systems/set‐                           mations
tings/use-axis-
trafo-fallback

### 6.3.4 Orientation interpolation

SLERP
When moving along a path, not only the position but also the orientation can
change. For example, you can imagine a gluing process in which you want to
move the tool along a curved surface at a certain angle. For this purpose, it
is necessary to determine the desired orientation between a start and target
orientation at any time in between, i.e. to carry out an interpolation.
There are various options. Currently, SLERP is supported by ctrlX MOTION.
SLERP interpolation (Spherical Linear Interpolation) initially defines a fixed
rotary axis which is specified by the start and end orientation. Interpolation
takes place via a rotation angle, which is changed between the value zero
(start orientation) and the maximum rotation angle (target orientation) (see
⮫ Further information on page 181 "Axis and angle").
Geometrically, SLERP represents the shortest path between the start and end
orientation. Consequently, the system always rotates in the direction in which
the target position is a maximum of 180° away.

The images above show an application and illustration of the SLERP interpola‐
tion. A tool (e.g. a welding machine) moves along a workpiece edge. At the
corner of the workpiece, the tool has to be rotated by 90° in order to continue
along the next edge. The dashed line in the middle sketch shows the target
orientation of the tool, which is to be transferred to the continuous start
orientation. In this case, the rotary axis corresponds to the z-axis in the world
coordinate system (WCS). All interpolated orientations between the start and
end orientations lie on the arc which the tool describes during the rotation.

### 6.3.5 Kinematic functions - Axis transformation

Introduction and overview

Differentiating between axes, kinematics and axis transformations
In the context of mechanics, an axis is a component that generally enables the
motion of a machine or individual machine parts. It is distinguished between
rotary axes, which enable rotational motion, and linear axes, which enable a
translatory motion.
It is possible to create and configure axes in the Motion app. By adding an
axis profile, the created axes can be linked to a drive that controls a real
existing axis.
Possible configuration parameters of an axis include axis limits for the posi‐
tion, velocity and acceleration of the axis. It also has to be specified whether
the axis is a linear axis or a rotary axis and in which unit it is moved. The
configured axes can be controlled individually using the Motion app.
To group several semantically related axes, they have to be added to a kine‐
matics in the Motion app. The directions of rotation of the individual axes can
also be specified in a kinematic system. The grouped axes can then move to
synchronized positions in the axis coordinate system (ACS).
In order to be able to move a kinematic system to any position and orientation
in space, an axis transformation is required which converts between Carte‐
sian coordinates and axis coordinates. An axis transformation can be of the
"6-axis robot with spherical hand", "SCARA" or "delta kinematics" type, for
example. Several axis transformations can be added to a kinematic system.
For example, the kinematics of a 6-axis robot could also be controlled with
a future 5-axis robot axis transformation if, for example, it operates with a
rotational-symmetric tool. Typically, a motion takes place on a geometrically
defined path (e.g. a straight line, a circle or a spline). The axis transformation
then transforms the interpolated Cartesian values into nominal axis values.
The Cartesian is a special case here, as the x, y and z coordinates coincide
with the three linear axes and no axis transformation is required. A coordinate
in Cartesian space always corresponds to the values of the respective axes in
the Cartesian.

Functional principle of an axis transformation
An axis transformation consists of two parts:
● Forward transformation: The Cartesian position and orientation of the end
   effector are calculated from the specified axis values
● Inverse transformation: The axis values required to achieve a given Carte‐
   sian position and orientation of the end effector are calculated
To enable a correct forward or backward transformation, the axis transfor‐
mation may require further information about the kinematics, depending on
the type of axis transformation. These values can be, for example, distances
between the axes.
The forward transformation for converting the axis values into the Cartesian
position and orientation is always possible and unambiguous for open kine‐
matics (e.g. SCARA, 6-axis robots with spherical hand), provided that all axis
values are given as finite numbers and lie within the axis limits. Exceptions
are closed kinematics, which are characterized by the fact that there are sev‐
eral connection points from the end effector to the base (e.g. delta robots).
The backward transformation for converting the Cartesian position into the
individual axis values cannot provide a solution for every position. Some
positions are too far away, others cannot be reached due to other geometric

restrictions. Several axis positions can also be considered for positions and
orientations, between which the axis transformation can select based on the
current position, for example.

Basic transformations and orientation transformations
A distinction is made between two types of transformations in the control
system: Basic and orientation transformations. To configure a kinematic cor‐
rectly, a basic transformation is created first. It should represent the robot to
be controlled as accurately as possible. An example of a basic transformation
would be the "axis transformation for 6-axis robots with spherical hand". In
addition to the basic transformation, it is possible to assign an orientation
transformation to the kinematics. This means that a basic transformation,
which cannot map orientations on its own, can be expanded to include this

option.
The following restriction applies when creating orientation transformations:
An orientation transformation can only be assigned to a kinematic if its
underlying base transformation does not support any type of orientation. For
example, no orientation transformation can be assigned to an "axis transfor‐
mation for 6-axis robots with spherical hand" or an "axis transformation for
SCARA robots", as these two basic transformations can already map orienta‐
tions completely or partially.
The division into basic and orientation transformation allows a modular con‐
figuration of kinematics in the control system. For example, it is possible to
configure a 4-axis delta robot with three rotary axes for spatial positioning
and one rotary axis for mapping orientations around the Z-axis by selecting
the "Axis transformation for delta robots with three rotary axes" as the basic
transformation and the "Axis transformation for 1D orientations on the flange"
as the orientation transformation.

Axis offsets
When configuring a kinematic system, a previously defined zero position is
always assumed. In the following descriptions of the individual axis transfor‐
mations, this usually corresponds to the position of the kinematics on the
images describing the axes, unless explicitly stated otherwise. For example,
a 6-axis robot with a spherical hand is in the zero position by default when
the robot arm is pointing completely upwards. If you want to define this
position differently due to other mechanical zero points of the axes, this can
be realized via axis offsets.

Axis directions
By default, a direction is specified for each axis in which it moves. This
direction can be either positive or negative. Within a kinematic system, it is
possible to configure the direction of the respective axis for each axis.

Singularities
In robotics, a singularity is a position of the robot in which one or more
degrees of freedom of the robot are lost. Singularities can occur, for example,
if several joint axes lie on a straight line or the robot is at the edge of the
working area and the joints therefore reach their limits.
                      When moving through a singularity or in its vicinity,
        WARNING       excessively high accelerations and axis velocities may
                      occur. See ⮫ Dealing with singularities on page 194
Thus, unexpected robot behavior can be monitored. If the robot moves close
to a singularity, large axis motions have to take place even for very small
motions in Cartesian space.

To prevent this, the robot control has to detect in good time when the robot
is close to a singularity and has to react accordingly. The special handling is
described in the following section.

Dealing with singularities
Since singularities can occur in the entire working area - a good example here
are the wrist singularities in the 6-axis robot with a spherical hand - two strat‐
egies for dealing with motions in the vicinity of singularities are implemented
in the control.
If the distance to the singularity is large enough so that the axis velocities
do not become too high, the motion can be implemented by the control by
reducing the Cartesian velocity to such an extent that axis limits are not
exceeded during the motion. This behavior ensures that the motion follows
the correct path.
Otherwise, a special treatment of the singularity is carried out in the control.

The figure shows a programmed motion that runs from bottom left from "A" to
top right to "B" (black + dashed line). In this example, there is a singularity at
point "S". A critical range of motion around point "C" is detected and handled
in the control. For this purpose, an area of length             around point C is
separated from the original linear motion command and replaced by a direct
motion (interpolation on the axis values).
The result of this treatment is thus:
1.    A linear motion along the programmed path to point "A".
      The position and orientation of point "C" and the axis that would need
      to move the most are displayed in the Data Layer node motion/kin/
      <Kinematics Name>/state/geometry/singularity/near as long as
      the robot is located at a configurable distance in front of point "C."
2.    To bridge the singularity, the motion is now continued by interpolating
      the axis values at point "A" to the axis values at point "B".
3.    The programmed linear motion can then be continued from point "B".
At the points "A" and "B", the control system reduces the velocity consider‐
ably, even to a standstill depending on the configured axis reserve. This is due
to the fact that the transition between the original contour and the inserted
direct axis motion is not continuous in the first two contour lines, i.e. tangent
and curvature.
Due to the direct motion between point "A" and point "B", the programmed
path is inevitably left. The control checks that the resulting deviation does not
exceed the configured by more than 10%.

                       By default, direct motion is performed using the max‐
         WARNING       imum axis limits. Unexpected rapid axis motions may
                       occur. It is recommended to limit the axis dynamics.
                       ⮫ Configuration for handling singularities on page 195
Possible problems that can occur when handling singularities:
1.   The size of the critical area around point "C" is greater than : As a
     result, the size of the segment to be replaced exceeds the maximum
     permitted size of      and may not be replaced.
2.   The deviation of the replaced segment from the programmed path is
     greater than       .
In both cases, an error is reported by the control and the programmed motion
cannot be carried out.

The    thus defines both the maximum permitted deviation from the pro‐
grammed motion and the maximum size of the segment of the linear motion
to be replaced.

Configuration for handling singularities
Various parameters can be used to influence how singularities are handled.
The user can limit the axis dynamics during direct motion between point “A”
and point “B” to a percentage of the regular axis limits. The following parame‐
ters are available for this purpose; each may assume values between 0.01 and
1:
{
        "vel": 1,
        "acc": 1,
        "dec": 1,
        "jrkAcc": 1,
        "jrkDec": 1
}
The parameters can be configured by the user via the Data Layer:
motion/kin/<Kinematik Name>/cfg/geometry/singularity/dynamics
A value of 1 does not represent any further restriction. A value smaller than 1
represents a restriction relative to the normal axis limits (for example, a value
of 0.7 results in a restriction to 70% of the axis limits). The default values for
new kinematics are 1 for all parameters.
The epsilon described above defines both the maximum allowable deviation
from the programmed motion and the maximum length of the segment of
linear motion to be replaced. The epsilon can be chosen arbitrarily, but should
be smaller than the maximum tolerable deviation from the specified path.
The configuration node can be found in the Data Layer under the
motion/kin/<Kinematik Name>/cfg/geometry/singularity/epsilon.
The radius within which a singularity is displayed at the node men‐
tioned above (“information distance”) can be changed using the configura‐
tion node motion/kin/<Kinematics Name>/cfg/geometry/singularity/
information-distance.
You can enable or disable singularity handling via the node motion/kin/
<Kinematics Name>/cfg/geometry/singularity/enabled.
The following section describes the influence and interaction of these configu‐
ration parameters in various scenarios.
Default configuration
By default, singularity handling is enabled, with epsilon preconfigured to 10
mm and the information distance configured to 50 mm. In this case, singu‐
larity handling is performed as described above, and information about the

first singularity on the path is displayed. If information about such singulari‐
ties is required at a greater distance due to typical travel speeds and their
spatial location, the information distance can be adjusted. However, it should
be noted that singularities located outside the orbit but still within the infor‐
mation distance are not displayed.
If the user jogs toward a singularity, the cursor automatically stops at an
epsilon distance from the singularity, and, as usual, information about that
singularity is provided. If the user continues jogging toward the singularity
after stopping, the cursor bypasses it using the singularity handling mecha‐
nism. The information about the singularity disappears at this moment, since
the singularity is no longer on the path.
Configuration for disabling the singularity detection
If singularities are not to be avoided and the specified path must be followed
exactly, Epsilon can be set to 0, thereby disabling singularity detection. This
may be necessary if the space does not allow the singularity to be avoided.
Motions with sufficient distance to singularities can be driven at reduced
velocity. If the path is too close to the singularity, the velocity limit is
exceeded at the singularity during the run, causing an error. No information
about a nearby singularity is displayed because singularities are not detected.
Jog motions can be performed right up to the singularity, at which point
an error message is displayed due to exceeding the velocity limit. Jogging
through a singularity is not possible.
Configuration for disabling the singularity handling
If you want to abort the motion before it is executed if a singularity is
detected on the path, you can disable singularity handling. Make sure to set
Epsilon to a value greater than 0 so that singularity detection is enabled.
Then, while preparing the motion, an error message is generated that includes
the position and orientation where the singularity was detected, as well as the
axis with the greatest motion at that point. Since the motion is not executed,
there is no information regarding a singularity at the time of execution.
Unlike planned motions, when jogging in the direction of a singularity, the
motion starts and automatically stops before reaching the singularity, and
information about the singularity is provided. However, if you continue jogging
in the direction of the singularity after the movement has stopped, the error
described above occurs.

Supported axis transformations
The Motion currently supports the following transformations:
Basic transformations:
● Cartesian robot (see ⮫ Chapter Axis transformation for Cartesians
  on page 197)
● 2-axis wrapping transformation (see ⮫ Chapter Axis transformation for a
  2-axis wrapping kinematics on page 200)
● 3-axis twisting crane robot (see ⮫ Chapter Axis transformation for a 3-axis
  twisting crane robot on page 208)
● SCARA robot (see ⮫ Chapter Axis transformation for SCARA robots
  on page 212)
● 4-axis SCARA robot with a crank (see ⮫ Chapter Axis transformation for a
  4-axis SCARA robot with a crank on page 218)
● Delta robot with three rotary axes (see ⮫ Chapter Axis transformation for
  delta robots with three rotary axes on page 224)
● Delta robot with three rotary axes (see ⮫ Chapter Axis transformation for
  delta robots with three linear axes on page 231)

● Delta robot with two rotary axes (see ⮫ Chapter Axis transformation for
   delta robots with two rotary axes on page 235)
● 6-axis robot with spherical hand (see ⮫ Chapter Axis transformation for
   6-axis robots with spherical hand on page 201)
● 2-axis parallelogram (see ⮫ Chapter Axis transformation for 2-axis parallelo‐
   gram on page 241)
● 2-axis delta slide (see ⮫ Chapter Axis transformation for 2-axis delta slide
   on page 247)
● 3-axis Adabot (see ⮫ Chapter Axis transformation for 3-axis Adabot
   on page 252)
● 3-axis flex stamper (see ⮫ Chapter Axis transformation for 3-axis flex
   stamper on page 256)
Orientation transformations:

● 1D orientations on the flange (see ⮫ Chapter Axis transformation for 1D
  orientations on the flange on page 261)
● 2D orientations (see ⮫ Chapter Axis transformation for 2D orientations on
  the flange on page 264)

    Axis transformation for Cartesians
In principle, it is not necessary to create an extra axis transformation in the
control in order to move several linear axes as Cartesian. There is an implicit
fallback solution for the case that no axis transformation is active and a
motion with MCS is still to be executed. In this case, linear axes that lie on
axis positions 1-3 are interpreted directly as x, y and z components.
However, there are cases in which the explicit creation of a mapping transfor‐
mation is necessary:
● Combination of a Cartesian with an orientation transformation (e.g.
   ⮫ Chapter Axis transformation for 1D orientations on the flange
   on page 261)
● The linear axes are on a different axis index outside of position 1-3.
● Axis offsets are to be defined for the linear axes
Table 14: Overview XYZ-Cartesian
ID                                      Cartesian_XYZ
Type                                    Basic transformation
License                                 SWL-XC*-MOT-CARTESIAN****-NNNN
Required axes                           3 (linear axes)
Compatible with orientation transfor‐   Yes
mations
Table 15: Overview XY-Cartesian
ID                                      Cartesian_XY
Type                                    Basic transformation
License                                 SWL-XC*-MOT-CARTESIAN****-NNNN
Required axes                           2 (linear axes)
Compatible with orientation transfor‐   Yes
mations
Table 16: Overview XZ-Cartesian
ID                                      Cartesian_XZ
Type                                    Basic transformation
License                                 none

Required axes                           2 (linear axes)
Compatible with orientation transfor‐   Yes
mations
Table 17: Overview YZ-Cartesian
ID                                      Cartesian_YZ
Type                                    Basic transformation
License                                 none
Required axes                           2 (linear axes)
Compatible with orientation transfor‐   Yes
mations

Variant
With the help of the Cartesian transformation, positioning in space is possible
using linear axes. The orientation cannot be changed. The control system
offers four different variants depending on the number and direction of the
axes:
● Cartesian with x-, y- and z-axis; see ⮫ Table 14 Overview XYZ-Cartesian
   on page 197 and Fig. 106
● Cartesian with x-, y- and z-axis; see ⮫ Table 15 Overview XY-Cartesian
   on page 197 and Fig. 107
● Cartesian with x- and z-axis; see ⮫ Table 16 Overview XZ-Cartesian
   on page 197 and Fig. 108
● Cartesian with y- and z-axis; see ⮫ Table 17 Overview YZ-Cartesian
   on page 198 and Fig. 109
The zero position of the Cartesian is defined by the zero position of the axes
used. In the zero position, the flange lies exactly in the coordinate system of
the base. If a zero position is required, e.g. as shown in Fig. 106, this can be
achieved by configuring the corresponding axis offsets.

                                                  LinY

                LinZ

          Z
              Y                      LinX

               X

                         LinY

Z
Y

X                   LinX

    LinZ                       LinX

Z
Y

X

    LinZ

                              LinY

Z
Y

X

Axis transformation for a 2-axis wrapping kinematics
 Table 18: Overview of 2-axis wrapping kinematics
  ID                                      Contact_TwoAxis
  Type                                    Basic transformation
  License                                 SWL-XCx-MOT-KINxLEVEL2xxx-NNNN
  Required axes                           2 (rotary axes)
  Compatible with orientation transfor‐   Yes
  mations

Robot structure
The 2-axis wrapping kinematics consist of two stationary rotary axes of equal
size Rot1 and Rot2, a toothed belt that is routed around the kinematic system
via deflection axes, and a movable vertical center beam. The two rotary axes
drive the toothed belt, which in turn moves the movable vertical center beam
in the XZ plane. The zero position of the wrapping kinematics is defined by
the zero positions of the axes used. In the zero position, the flange is located
at the center of the Rot1 axis. Other flange positions at the zero position can
be set by configuring the appropriate axis offsets.

                                                           Z

                                                 X

                Rot2                                      Rot1

Robot parameters
Table: The following parameter is required to configure the 2-axis wrapping
kinematics:
Parameters                          Description           Condition
I1                                  The diameter of Rot1 l1 > 0
               and Rot2 (to the
               center of the toothed
               belt)

                                                        Z

                                              X

                    l1                                      l1

    Axis transformation for 6-axis robots with spherical hand
 Table 19: Overview of 6-axis robots with spherical hand
  ID                                      SixAxisRobot_SphericalWrist
  Type                                    Basic transformation
  License                                 SWL-XCx-MOT-KINxLEVEL3xxx-NNNN
  Required axes                           6 (rotary axes)
  Compatible with orientation transfor‐   No
  mations

Robot structure
The 6-axis robot with spherical hand consists of the six rotary axes Rot1 -
Rot6 (also known as joints), which are connected by links (see Fig. 112).
The robot can be logically divided into two kinematic parts - orthoparallel
"arm" kinematics (Rot1, Rot2, Rot3) and "spherical hand" kinematics (Rot4,
Rot5, Rot6). The necessary condition for a spherical hand is that the axes of
rotation of the joints Rot4, Rot5 and Rot6 intersect at a common point. This
point of intersection is referred to as the root point (WCP) (see Fig. 113).

                                            Z
                                   Rot6         Y

                                                 X

                                                Rot5

                                                          Rot3

                                    Rot4

                                 Rot1
                                                              Rot2
                  Z
                      Y

                      X

                                  Rot5
                          Rot4                  Wc

                                                       Rot6

The Rot1, Rot2 and Rot3 axes enable the robot to move its root point WCP
to a desired position in 3D space. The joint Rot1 rotates the robot around
the Z-axis and determines the position of the wrist in the XY plane. The Rot2
and Rot3 joints rotate around the Y-axis and in combination determine the
position of the wrist in the X'Z plane. X' is the X-axis after it has been rotated
by Rot1.
The joints Rot4, Rot5 and Rot6, which form the spherical hand, are used to
orient the flange. By adjusting the Rot4, Rot5 and Rot6 values, any alignment
can be set (provided that the physical axis limits allow this).

Robot dimensions
The dimensions of the robot are defined for each of the seven links. The first
link connects the robot base to the Rot1 joint. The second link connects the
Rot1 and Rot2 joints, and so on. Finally, the seventh link connects the Rot7
joint to the flange, on which a tool can be mounted.
The zero position of the axes has to be selected so that the robot is extended
upwards and points in the X-direction when angling Rot2 to 90°.

                                          z7

                                          z6
                                          z5
                                                                  -y3

                           -x4            z4

                                                            -y4
                                          z3

                          x2                                 y2
                                          z2

     Z                                                                        Z
                                          z1

           X                                                                         Y

  The parameters describe the joint offset from the base of the robot to the
  flange in the zero position and are listed in the table below. All crossed out
  parameters (-) cannot be specified (e.g. specification x6 not possible, as the
  kinematics would no longer fulfill the conditions for a spherical hand). The
  configuration parameters x2, y2, y3, x4, y4 and all z-values are required. In
  addition to these frequently used parameters, it is possible to configure some
  optional parameters. These optional parameters are highlighted in bold in the
  table and are only shown in the following Fig. 115.
Links              X-offset       Y-offset              Z-offset              Additional conditions
Base → Joint 1     x1             y1                    z1 >= 0
Joint 1 → Joint 2 x2              y2                    z2 >= 0
Joint 2 → Joint 3 -               y3                    z3 > 0
Joint 3 → Joint 4 x4              y4                    z4 >= 0               |x4| +z4 +z5 >0
Joint 4 → Joint 5 -               y5                    z5 >= 0               y5 + y6 = 0
Joint 5 → Joint 6 -               y6                    z6 >= 0               y5 + y6 = 0
Joint 6 → Flange x7               y7                    z7 >= 0
  The parameters x and y, provided they are defined, can take on any value
  (both positive and negative). The requirements for the z-parameters are that
  they are not negative and that z3 is greater than 0. In addition, the parameters

x4, z4 and z5 must not all be zero simultaneously in order to guarantee the
full number of degrees of freedom. To meet the spherical hand condition, y5
and y6 have to cancel each other out, i.e. it is required that y5 + y6 = 0.

                    x7                                      y7

                                       z7
                                                                   -y6

                                       z6
                                                                   y5

                                       z5
                                                                  -y3

                                       z4
                         -x4

                                                            -y4
                                       z3
               x1    x2                              y1      y2
                                       z2

  Z                                                                          Z
                                       z1

      X                                                                           Y

In addition to the parameters for the robot dimensions mentioned up to this
point, more optional parameters can be set. These parameters describe the
existence of a unidirectional mechanical coupling between two rotary axes.
These parameters can be found in the table below and the coupling factors
are described in more detail in the following section.
Group/coupling    Parameters           Description               Condition
factor
Coupling factor   cRot5Rot4Ratio1      Rot5 rotates by           If cRot5Rot4Ratio1
from red4 to red5                      cRot5Rot4Ratio1           or
                                       units when                cRot5Rot4Ratio2
                                       Rot4 rotates by           are zero, no axis
                                       cRot5Rot4Ratio2           coupling is present
                                       units, due to
                                       mechanical cou‐
                                       pling
                    cRot5Rot4Ratio2    If Rot4 rotates by
                                       cRot5Rot4Ratio2
                                       units, then
                                       Rot5 rotates by
                                       cRot5Rot4Ratio1
                                       units, due to
                                       mechanical cou‐
                                       pling

Group/coupling    Parameters             Description          Condition
factor
Coupling factor   cRot6Rot4Ratio1        Rot6 rotates by    If cRot6Rot4Ratio1
from red4 to red6                        cRot6Rot4Ratio1 or
                                         units when         cRot6Rot4Ratio2
                                         Rot4 rotates by    are zero, no axis
                                         cRot6Rot4Ratio2 coupling is present
                                         units, due to
                                         mechanical cou‐
                                         pling
                     cRot6Rot4Ratio2     If Rot4 rotates by
                                         cRot6Rot4Ratio2
                                         units, then

                                         Rot6 rotates by
                                         cRot6Rot4Ratio1
                                         units due to
                                         mechanical cou‐
                                         pling
Coupling factor   cRot6Rot5Ratio1        Rot6 rotates by    If cRot6Rot5Ratio1
from red5 to red6                        cRot6Rot5Ratio1 or
                                         when Rot5          cRot6Rot5Ratio2
                                         rotates by         are zero, no axis
                                         cRot6Rot5Ratio2, coupling is present
                                         due to mechanical
                                         coupling
                     cRot6Rot5Ratio2     If Rot5
                                         rotates around
                                         cRot6Rot5Ratio2,
                                         then Rot6
                                         rotates around
                                         cRot6Rot5Ratio1,
                                         due to mechanical
                                         coupling

Axis coupling
There are mechanical designs of the 6-axis robot with spherical hand, in
which rotations of one rotary axis result in a coupled rotation of one or more
other rotary axes. In order to be able to compensate for this behavior using
the respective axis and thus enable isolated rotations of specific axes, there
are the coupling factor pairs shown in ⮫ Further information on page 205
● cRot5Rot4Ratio1 with cRot5Rot4Ratio2, which describe a coupling from
   Rot4 to Rot5
● cRot6Rot4Ratio1 with cRot6Rot4Ratio2, which describe a coupling from
   Rot4 to Rot6
● cRot6Rot5Ratio1 with cRot6Rot5Ratio2, which describe a coupling from
   Rot5 to Rot6
The relationship of these mechanical couplings is unidirectional, which means
that a rotation of, for example, axis Rot4 leads to a rotation of Rot5, but a
rotation of Rot5 does not result in a change in Rot4.
The values of the coupling factors have no units, as the value pairs each
describe a ratio. If the signs are the same, the rotation is in the same direc‐
tion and if the signs are different, the conditional rotation is in the opposite
direction. If at least one of the values of a coupling factor value pair is 0, this
coupling is disabled.

The coupling factors are only taken into account for motions in Cartesian
coordinate systems (e.g. MCS or PCS). When moving in the ACS coordinate
system, rotations of the Rot4 axis can result in movements of the Rot5 and
Rot6 axes if the coupling factors are not complied with. The same applies to
the Rot6 axis when the Rot5 axis is rotated.

axis robot with spherical hand, represented by their respective value pairs
(Ratio1:Ratio2)

Singularities of a 6-axis robot with a spherical hand
Three different types of singularities occur in the 6-axis robot with a spherical
hand: the wrist singularity, the elbow singularity and the shoulder singularity.

Wrist joint singularity:

The wrist singularity occurs when the axis 5 of the robot is at 0° or a multiple
of 180° and therefore the axes 4 and 6 form a straight line. In this position,
axes 4 and 6 can be rotated against each other without causing the end
effector to move. In addition, it is no longer possible to move the end effector
perpendicular to axis 5, which means that the robot loses one degree of
freedom.

Elbow singularity:

The elbow singularity occurs when the carpal point lies on the extension of
the connection between axes 2 and 3. In other words, when the robot arm is
fully extended. The robot is therefore located at the edge of the workspace.
Here, too, the robot has lost degrees of freedom, as a significant motion
of one of the two axes 2 and 3 is initially required for a motion along the
extended connection of axes 2 and 3.

  Shoulder singularity:

  singularity
  The shoulder singularity occurs when the root point is located directly above
  axis 1. In this position, a motion of axis 1 does not change the position of the
  root point and can therefore always be compensated by a motion of the last
  three axes. On the other hand, motion along the axis of rotation of Rot2 is not
  directly possible, so that a degree of freedom is lost here as well.

Solution selection
Depending on the position, this type of robot can have up to eight different
options for bringing the flange into a desired position and orientation. The
robot's transformation function will attempt to select the optimum solution
depending on the current axis values or a specified axis position. The aim is to
avoid switching between different solutions (e.g. elbow up and elbow down).
Due to geometric restrictions, there are also fewer than eight or even no valid
solutions at some Cartesian positions.

Axis transformation for a 3-axis twisting crane robot
 Table 20: Overview of 3-axis twisting crane robot
  ID                                      Crane_ThreeAxisTwisting
  Type                                    Basic transformation
  License                                 SWL-XCx-MOT-KINxLEVEL2xxx-NNNN
  Required axes                           3 (rotary axes)
  Compatible with orientation transfor‐   No
  mations

Robot structure
The 3-axis twisting crane robot has three rotary axes (Rot1, Rot2, Rot3). The
axes Rot1 and Rot2 form the basis of the robot. Both axes are located at
the origin of the coordinate system and allow the entire kinematic system to
rotate around the Z-axis (Rot1) or around the Y-axis (Rot2), respectively. An
arm consisting of three segments extends from the robot base. Between the
first and second segments is the axis Rot3, which controls the corresponding
angle between the two segments. In the zero position, the two segments are
perpendicular to each other. Unlike the other two rotary axes, the direction of
rotation of the Rot3 axis is counterclockwise. The flange is located at the end
of the third segment. A special joint ensures that the last segment—and thus
the flange as well—is always mechanically parallel to the XY plane and points
in the direction defined by the Rot1 axis.⮫ Further information on page 209

shows the 3-axis twisting crane in its zero position with markings for the three
axes.

  While the Rot1 axis can be rotated freely, there are restrictions on Rot2
  and Rot3 axes. The angle of rotation for axis Rot2 is limited to the range
  between -180° and 180°, excluding the endpoints. Axis Rot3 can assume
  angles between -90° and 90°, excluding the negative limit value and including
  the positive limit value. The axis constraints are summarized in ⮫ Further
  information on page 209.
  Table 21: Overview of the axis restrictions for the 3-axis twisting crane
  Axis                                     Restriction
  Rot2                                     –180° < Rot2 < 180°
  Rot3                                     –90° < Rot3 < 90°

Robot parameters
The configuration parameters for the 3-axis twisting crane robot are listed in
the ⮫ Further information on page 209 file.

Parameters                          Description           Condition
I1                                  Length of the first   l1 > 0
               arm segment of Rot2
               to Rot3
I2                                  Length of the second l2 > 0
               arm segment, starting
               at Rot3
I3                                  Length of the third   l3 ³ 0
               arm segment to the
               flange

Solution selection
Due to the joint between the first and second segments of the arm and
the fixed orientation of the flange, certain limitations have to be taken into
account when selecting a solution.

  Forward transformation
  Due to its mechanical configuration and parallel orientation to the XY plane,
  the flange of the 3-axis twisting crane robot points away from the Z-axis.
  Under certain configurations, it is mechanically possible for the flange to be
  located behind the Z-axis. For consistency reasons, these solutions are not
  allowed, and the corresponding axis values are not accepted by the forward
  transformation. ⮫ Forward transformation on page 210 shows an example of
  valid and invalid solutions.

Inverse position kinematics
Due to the joint between the first and second arm segments, the choice of
solution in the inverse transformation is generally not unique. Since the range
of values for the rotary axis Rot3 is limited to –90° to 90°, only solutions in
which the elbow is bent upward are allowed. ⮫ Inverse position kinematics
on page 211 illustrates the solution selection.

Singularities of a 3-axis twisting crane robot
The 3-axis twisting crane robot generally has two singularities.

Singularity with fully extended arm
At the edges of the twisting crane's working area, the first two arm segments
form a straight line. When the joint is fully extended, its orientation can no
longer be determined. Another motion involves bending the elbow to the
right or left. When exiting the singularity, the limited range of values for the
Rot3 rotary axis is used to select the solution in which the elbow remains
raised (see ⮫ Inverse position kinematics on page 211). ⮫ Singularity with
fully extended arm on page 211 shows the twisting crane robot with its arm
extended.

Singularity when the flange is positioned on the Z-axis
The 3-axis twisting crane is also in a singularity if the flange is located on
the Z-axis. In this position, the value for the rotary axis Rot1 in the backward
transformation can be freely selected (see ⮫ Singularity when the flange is
positioned on the Z-axis on page 212). To ensure that a unique solution is
chosen, the current axis value is given preference.

Axis transformation for SCARA robots
Table 22: Overview of SCARA robots with the linear axis on the flange
ID                                        Scara_LinearAxisFlange
Type                                      Basic transformation
License                                   SWL-XCx-MOT-KINxLEVEL2xxx-NNNN
Required axes                             2 (rotary axes)
                                          Additionally optional: 1 (rotary axis) +
                                          1 (linear axis)
Compatible with orientation transfor‐     No
mations

  Table 23: Overview of SCARA robots with the linear axis at the base
  ID                                      Scara_LinearAxisBase
  Type                                    Basic transformation
  License                                 SWL-XCx-MOT-KINxLEVEL2xxx-NNNN
  Required axes                           2 (rotary axes)
                                          Additionally optional: 1 (rotary axis) +
                                          1 (linear axis)
  Compatible with orientation transfor‐   No
  mations

Robot structure
The SCARA robot basically consists of two rotary axes Rot1 and Rot2 around

the Z-axis (also known as joints), which enable the end effector to be posi‐
tioned in the XY plane. In addition, a SCARA can optionally have two more
axes: A linear axis Lin1 for moving along the Z-axis and an orientation axis
Rot3 for achieving a specific rotation of the end effector around the Z-axis.
The zero position of a SCARA robot depends on the specified height offset on
the linear axis.

Variant
  The control provides two different variants of the SCARA, which differ in the
  arrangement of the linear axis:
  ● Linear axis for flange (see ⮫ Table 22 Overview of SCARA robots with the
    linear axis on the flange on page 212 and Fig. 126)
  ● Linear axis at the base (see ⮫ Table 23 Overview of SCARA robots with the
    linear axis at the base on page 213 and Fig. 127)

                            Rot1
                                          Rot2

                                                           Lin1

                                                 Rot3

                       Lin1      Rot1
                                              Rot2

                                                     Rot3

Robot parameters
In order for the axis transformation to calculate correctly, information about
the distances between the joints and between the joints and the flange is
required. These parameters have to be specified when creating the axis trans‐
formation.

                                        l1              l2

                 l4

                  l3

  the flange

                                      l1               l2

         l4                                                         -l5

         l3

the base
The following table describes the possible parameters of a SCARA. The
parameters l1 and l2 are always required and have to be positive. The Z-values
l3 to l5 are optional and describe the possible height offsets in the super‐
structure. The height values always have to be specified in the zero position of
all axes.
Parameters                          Description           Condition
I1                                  The length of the     l1 > 0
              connection between
              Rot1 and Rot2
I2                                  The length of the     l2 > 0
              connection between
              Rot2 and the flange
I3                                  The height difference
              between the base
              and the first arm
I4                                  The height difference
              between the first and
              second arm
I5                                  The height difference
              from the second arm
              to the flange
If the axis Lin1 is defined, but the parameters l3, l4 and l5 are not specified,
the offset in the z-direction between the base and flange is zero, as can be
seen in the following images.

                                    l1               l2

 axis on the flange)

                                         l1               l2

 axis at the base)

Singularities of a SCARA robot
There is only one type of singularity in a SCARA robot. This singularity occurs
when the joint Rot2 is at 0°, i.e. the robot arm is fully extended. In this
position, the end effector lies on the extension of the connection between
Rot1 and Rot2 and the robot is at the edge of the workspace, which means it
loses one degree of freedom. To move the end effector in the direction of the
base, a significant motion of the two axes is first required.

Solution selection

Normally, a SCARA robot has two possible solutions to reach a desired posi‐
tion in Cartesian space. Both solutions differ in the positioning of the elbow
joint, i.e. the rotational axis Rot2.

  In this case, the transformation function determines the optimum solution
  based on the current axis positions or an additionally specified position. The
  transformation attempts to avoid changing the solution branch and not to
  traverse through the singularity. If the starting position or the additionally
  specified position is in or near a singularity, the solution closest to this posi‐
  tion is selected. However, there may also be positions that the robot can only
  reach with one solution or not at all due to axis limitations.
  For the SCARA with the linear axis at the base, the singularities are identical.

Axis transformation for a 4-axis SCARA robot with a crank
 Table 24: Overview of 4-axis SCARA robots with crank
  ID                                       ScaraCrank_FourAxis
  Type                                     Basic transformation
  License                                  SWL-XCx-MOT-KINxLEVEL2xxx-NNNN
  Required axes                            4 (rotary axes)
  Compatible with orientation transfor‐    No
  mations

Robot structure
A 4-axis SCARA with a crank consists of a crank that is moved by the rotary
axis Rot1, enabling the end-effector to be positioned in the Z-direction, and
two rotary axes Rot2 and Rot3 around the Z-axis, which allow the end-effector
to be positioned in the XY plane, and a rotary axis Rot4 to achieve a specific
rotation of the end-effector about the Z-axis.

Robot parameters
In order for the axis transformation to calculate correctly, information about
the distances between the joints and between the joints and the flange is
required. These parameters have to be specified when creating the axis trans‐
formation.

                 l1                  l4                     l5

                               l3

            l2

  The following parameters are required to configure the 4-axis SCARA with a
  crank:

Parameters                              Description           Condition
I1                                      The distance from
                   the origin to the
                   crank pivot point in
                   the negative X-direc‐
                   tion
I2                                      The length of the     l2 > 0
                   crank
I3                                      The length of the     l3 > 0
                   push rod
I4                                      The length of the     l4 > 0
                   connection from Rot2
                   to Rot3
I5                                      The length of the     l5 > 0
                   connection from Rot3
                   to the flange
  In addition to the parameters for the robot dimensions mentioned up to
  this point, more optional parameters can be set. These parameters describe
  the availability of a unidirectional mechanical coupling between rotary axes.
  These parameters can be found in the table below and the coupling factors
  are described in more detail in the following section.
  |l1| < l2 + l3          If the condition is not met, the distance between the
                          Rot1 axis and the Rot2 axis is so great that it can only be
                          bridged with a horizontal push rod—or not at all. In this
                          case, the crank is not working.
  |l1| > l2 - l3          If the condition is not met, the push rod is so short that
                          it cannot reach the Rot2 axis from either the leftmost
                          point of the crank or the rightmost point of the crank.

Axis coupling
The parameters listed above cRot2Rot3 and cRot23Rot4 describe the availa‐
bility of a mechanical coupling between rotary axes. There are mechanical
designs for the 4-axis SCARA with a crank—particularly for the SCARA compo‐
nent—in which the rotation of one rotary axis results in the coupled rotation of
another rotary axis. To compensate for this behavior through the affected axis
and to enable isolated rotations of specific axes, coupling factors are used, as
shown in ⮫ Further information on page 220.
  ● cRot2Rot3 describes a coupling of Rot2 to Rot3
  ● cRot23Rot4 describes a coupling of Rot2 and Rot3 according to Rot4
  The connection between these mechanical couplings is unidirectional. This
  means that a rotation of e.g. the Rot2 axis results in a rotation of the Rot3
  axis, but a rotation of Rot3 does not result in a rotation of Rot2. The coupling
  factors are unitless because they represent the ratio between the rotation of
  the causing axis and the amount of compensation applied by the affected
  axis. A negative value results in a rotation of both axes in the same direction.
  The coupling factors are only taken into account for motions in Cartesian
  coordinate systems (e.g. MCS or PCS). When moving in the ACS coordinate
  system, rotations of the Rot2 axis can result in motions of the Rot3 axis if the
  coupling factors are not taken into account. The same applies to rotations of
  axes Rot2 and Rot3 for axis Rot4.

with a crank

Singularities of a 4-axis SCARA robot with a crank
The 4-axis SCARA with a crank has two types of singularities:

Push rod and crank rod aligned along a straight line
A type of singularity occurs when the push rod and the crank rod are aligned
along a straight line. In this case, the end-effector is located at the edge of the
working area in the Z-direction, and the robot loses one degree of freedom.
For the end-effector to move in the Z-direction, a significant motion of the axis
is first required.

Rot2 to 0 or 180°
Another type of singularity occurs when the joint Rot2 is at 0° (or 180°), i.e.,
the robot arm is fully extended (bent). In this position, the end-effector rests
on the connection between Rot1 and Rot2; the robot is at the edge of the
working area and loses one degree of freedom. For the end-effector to move
toward the base (away from the base), a significant motion of both axes is
first required.

Solution selection
Selecting a crank design
Usually, the crank has two options to reach a desired position in the Z-direc‐
tion. The two options differ depending on whether the bend between the
connecting rod and the push rod is to the right or to the left.
In this case, the transformation function determines the optimal solution
based on the current axis position of the crank or an additional specified
position. In doing so, the transformation avoids a change in the solution
branch and passing through the singularity. There may be positions that the
robot can only reach with one option or not at all, either due to an axis
limitations or due to the robot parameter configuration.

Selecting a SCARA solution
Usually, the SCARA component of the robot has two options to reach a
desired position in the XY plane. The two solutions differ in the positioning of
the elbow joint—that is, the rotary axis Rot3.
In this case, the transformation function determines the optimum solution
based on the current axis positions or an additionally specified position. The
transformation attempts to avoid changing the solution branch and not to
traverse through the singularity. If the starting position or the additionally
specified position is in or near a singularity, the solution closest to this posi‐
tion is selected. However, there may also be positions that the robot can only
reach with one solution or not at all due to axis limitations.

Axis transformation for delta robots

Axis transformation for delta robots with three rotary axes
 Table 25: Overview of delta robots with three rotary axes
  ID                                      Delta_ThreeAxisRotational
  Type                                    Basic transformation
  License                                 SWL-XCx-MOT-KINxLEVEL2xxx-NNNN
  Required axes                           3 (rotary axes)
  Compatible with orientation transfor‐   Yes
  mations

Robot structure
A delta robot with three axes of rotation (referred to as "3-axis delta robot" in
the following) consists of a fixed upper platform, three rotary axes Rot1, Rot2,
Rot3 (also called shoulders), three upper arms, three elbows, three lower
arms and the movable lower platform. The upper arms are each connected
to a rotary axis (shoulder). The elbows are located between the upper and
lower arms. The lower, movable platform is connected to the robot via the
forearms. The shoulders are at a 120° angle to each other. In a 3-axis delta
robot, the three rotary axes Rot1, Rot2 and Rot3 are driven. This allows the
lower platform to be positioned in the room. The elbows can swivel freely
around two axes. As the lower arms consist of two parallel spokes, the design
of the robot ensures that the lower platform is always parallel to the upper
platform. This means that it is not possible to change the orientation of the
flange on the 3-axis delta robot.

                          z
                                   y
                  Rot1
                                       Rot3
                                   x
                         Rot2

z
    y

     x

Robot parameters

                                       Z
                         l1

                                                X
        l2
             l3

         Z

                     X        l4

                                                 X

                             X         l4

                                                     X

                                                 Y

                            X
                                            l4
                     Y

   The following assumptions are made so that the axis transformation can be
   carried out correctly:
● The rotary axis defined as Rot1 is located opposite the x-axis at a distance
   l1 from the robot origin. (see Fig. 142)
● The axes Rot1, Rot2 and Rot3 are offset from each other by 120°, with
   Rot2 offset in the negative y-direction (counterclockwise when viewed from
   above)
● The length l2 is identical for all three arms of the robot
● The length l3 is identical for all three arms of the robot
● In the zero position of the Rot1, Rot2 and Rot3 axes, the upper arms are
   aligned horizontally (in the same plane as the upper platform)
● In the positive position of the rotary axes Rot1, Rot2, Rot3, the upper arms
   point downwards. For example, the following applies: If the axis is at 90°,
   the corresponding upper arm points straight down, opposite the Z-axis
Table 26: The following parameters are required to configure the 3-axis delta robot:
Parameters                        Description           Condition
I1                                The radius of the     l1 > 0
                                  upper platform to
                                  which the rotary axes
                                  Rot1, Rot2, Rot3 are
                                  attached
I2                                The length of the     l2 > 0
                                  upper arms, between
                                  the Rot1/Rot2/Rot3
                                  axis and the elbow

Parameters                         Description           Condition
I3                                 The length of the     l3 > 0
              forearms, between
              the elbow and the
              edge of the lower,
              movable platform
I4                                 The radius of the     l4 > 0
              lower platform
Table 27: Additional restriction of the parameters:
l1 ≠ l4 or l2 ≠ l3                                           This condition has to be met for the
                                                             axis transformation to work.
                                                             If the condition is not fulfilled, then:

                                        ● the size of the upper and lower plat‐
                                           form is identical
                                        ● the upper arms and forearms are
                                           the same length
                                        Then the condition is not fulfilled.
                                        In this case, the robot has a special
                                        structural singularity: As soon as all
                                        axis values are less than or equal to 0,
                                        the solution of the forward transforma‐
                                        tion is always the origin of the robot

Solution selection
With the 3-axis delta robot, there are several solutions for both forward and
backward transformation.

Forward transformation
For the forward transformation, there are one or two different solutions for a
specified axis position:

 with rotary axes

 with rotary axes
 The position of the elbows is clearly determined by the position of the rotary
 axes Rot1, Rot2, Rot3. However, the movable platform could be located either
 above the elbows (Fig. 143) or below the elbows (Fig. 144).
 In the axis transformation, it is assumed that the robot is always in the lower
 solution (Fig. 144).

Inverse position kinematics
For the backward transformation, there are up to 2 solutions per arm of the
robot for a specified Cartesian position. This results in a maximum of 2³ = 8
different solutions in which the arms are angled inwards or outwards.

 with rotary axes
 The axis transformation always selects the outer solution for all three arms of
 the robot. Moving to an inner elbow position is possible, for example, using
 motion commands in the axis space. If the robot is in this situation, motions
 in Cartesian space are no longer possible, as these would cause a change to
 the outer solution.

Singularities of a 3-axis delta robot with rotary axes
With a 3-axis delta robot, singularities occur at the upper and lower edge of
the working area.

Singularities at the lower edge of the working area
These singularities can also be referred to as elbow singularities. They occur
when the shoulder, elbow and connection point to the movable platform are
in line for at least one arm of the 3-axis delta robot. In addition to the restric‐
tions in the direction of motion, it would be possible in this singularity for a
change from the outer to the inner elbow solution to take place.

 In Fig. 146, the right arm of the 3-axis delta robot is fully extended. It is
 no longer possible to move downwards in the direction of the outstretched
 arm. In addition, an instantaneous upward motion in the direction of the out‐
 stretched arm is not possible, as the shoulder of the outstretched arm would
 have to rotate too quickly.

Singularities at the upper edge of the working area
The design of the robot has be taken into account for the singularities at the
upper edge of the working area. For 3-axis delta robots with the property l1
+ l2 < l3 + l4, the following singularity can occur at the upper edge of the
working area:

 delta robots
 In this type of singularity, the elbow is completely folded in. The shoulder,
 elbow and connection point to the moving platform are in line here. In this
 case, upward motion in the direction of the folded arm is no longer possible.
 In addition, an instantaneous downward motion in the direction of the folded
 arm is not possible, as the shoulder of the folded arm would have to rotate
 too quickly. In this type of singularity, a change from the outer to the inner

  elbow solution could occur. For 3-axis delta robots with the property l1 + l2
  > l3 + l4, the following singularity can occur at the upper edge of the working
  area:

  delta robots
  This singularity occurs when the forearms are positioned in such a way that
  the elbows can no longer be moved outwards. In this position, it is not pos‐
  sible to predict in which direction the moving platform moves. Transitions
  from the lower to the upper solution of the forward transformation can there‐
  fore occur here. Linear motions can no longer be performed as soon as the
  robot is in the upper solution.

Axis transformation for delta robots with three linear axes
  Table 28: Overview of delta robots with three linear axes
  ID                                      Delta_ThreeAxisLinear
  Type                                    Basic transformation
  License                                 SWL-XCx-MOT-KINxLEVEL2xxx-NNNN
  Required axes                           3 (linear axes)
  Compatible with orientation transfor‐   Yes
  mations

Robot structure
This 3-axis delta robot has three linear axes (Lin1, Lin2, Lin3). The three
linear axes move parallel to the Z-axis and are arranged equidistantly along
a circle (see ⮫ Further information on page 231). While the first linear axis,
Lin1, lies on the negative X-axis, the XY coordinates of the Lin2 and Lin3
axes each lie along a line inclined at ±60° in the XY plane. This results in an
angular difference of 120° between the positions of the axes on the circle.
The origin of the coordinate system is located at the center of the circular
arrangement and thus at the center of the three axes. At the zero position, the
axes lie in the XY plane.
A movable platform is connected to the three linear axes via a linkage and, by
definition, is located below all of the axes. The flange is located in the center
of this movable platform and is always oriented parallel to the XY plane by
means of a mechanical mechanism.
As a counterpart to the movable platform, a “fixed platform” is assumed in
the following. This fixed platform serves as the robot's base and defines the
circular arrangement of the linear axes at the home position.

Robot parameters
The 3-axis delta with linear axes is parameterized using three lengths (l1,
l2, l3). Here, l1 describes the radius of the fixed platform and thus the dis‐
tance of the axes from the origin in the zero position. The distance between
the linear axes and the corresponding outer edge of the moving platform is
defined by the length parameter l2. When setting the parameter l2, note that
it has to be large enough to geometrically connect the axes to the platform.
The radius of the movable platform is specified by l3 and has to be smaller
than the radius of the fixed platform.
  The ⮫ Further information on page 232 lists the available parameters for con‐
  figuring the 3-axis delta (linear axes), and ⮫ Further information on page 231
  provides a schematic diagram.

Functions

                            X             l4

                                                        X

                                                    Y

                           X
                                               l4
                    Y

Table 29: The following parameters are required to configure the 3-axis delta robot with linear
axes:
Parameters                        Description             Condition
I1                                The radius of the       l1 > 0
                                  fixed platform of the
                                  delta robot
I2                                The length of the       l2 > 0
                                  connection between      l2 ³ l1 - l3
                                  the motors and the
                                  corresponding edges
                                  of the moving plat‐
                                  form
I3                                The radius of the       0 £ l3 < l1
                                  movable platform of
                                  the delta robot

Solution selection
The choice of solution in the forward and inverse transformations is based
primarily on the condition that the Z-coordinate of the flange lies below the
axes.

Forward transformation
When calculating the forward transformation, there are generally two solu‐
tions for the position of the flange. For the 3-axis delta linear, only those
solutions are selected in which the flange is located below the three linear
axes.

Inverse position kinematics
 Similar to the approach used for the forward transformation, the inverse
 transformation also selects only those solutions for the axis positions for
 which the target position of the flange lies below the axes.

Singularities of a 3-axis delta robot with linear axes
 The 3-axis delta robot with linear axes exhibits singularities at the boundaries
 of its working area whenever at least one of the linear axes moves to the same
 height (Z-coordinate) as the flange. In these configurations, right angles are
 formed between the guides of the linear axes and the corresponding linkages
 (see ⮫ Further information on page 235).
 When exiting these singularities, it is theoretically possible for the linear axes
 to switch to the underside of the flange. These solutions are not permitted,

 and the solution in which all linear axes are located above the flange is always
 selected.

Axis transformation for delta robots with two rotary axes
 Table 30: Overview of delta robots with two rotary axes
  ID                                      Delta_TwoAxisRotational
  Type                                    Basic transformation
  License                                 SWL-XCx-MOT-KINxLEVEL2xxx-NNNN
  Required axes                           2 (rotary axes)
  Compatible with orientation transfor‐   Yes
  mations

Robot structure
A delta robot with two rotary axes (referred to as "2-axis delta robot” in the
following) consists of a fixed upper platform, two rotary axes Rot1 and Rot2
(also called shoulders), two upper arms, two elbows, two lower arms and
the movable lower platform. The upper arms are each connected to a rotary
axis (shoulder). The elbows are located between the upper and lower arms.
The lower, movable platform is connected to the robot via the forearms. The
shoulders are at a 180° angle to each other. In a 2-axis delta robot, the two

rotary axes Rot1 and Rot2 are driven. This allows the lower platform to be
positioned in the X-Z plane. The elbows can pivot freely. A parallel design on
the lower arms ensures that the lower platform is always parallel to the upper
platform. This means that it is not possible to change the orientation of the
flange on the 2-axis delta robot.

                                                Z

                               Rot1                         Rot2
                                                        X

             Z

                           X

Robot parameters

                                                    Z
                                      l1

                                                            X
                 l2
                      l3

                  Z

                               X           l4

  The following assumptions are made so that the axis transformation can be
  carried out correctly:
● The rotary axis defined as Rot1 is located opposite the x-axis at a distance
   l1 from the robot origin. (see Fig. 152)
● The Rot1 and Rot2 axes are offset from each other by 180°, with Rot2
   pointing in the positive x-direction
● The length l2 is identical for all three arms of the robot
● The length l3 is identical for all three arms of the robot
● In the zero position of the Rot1 and Rot2 axes, the upper arms are aligned
   horizontally (in the same plane as the upper platform)
● In the positive position of the rotary axes Rot1 and Rot2, the upper arms
   point downwards. For example, the following applies: If the axis is at 90°,
   the corresponding upper arm points straight down, opposite the Z-axis

Table 31: The following parameters are required to configure the 2-axis delta robot:
Parameters                        Description         Condition
I1                                The radius of the   l1 ≥ 0
                                  upper platform to
                                  which the rotary
                                  axes Rot1, Rot2 are
                                  attached
I2                                The length of the   l2 > 0
                                  upper arms, between
                                  the Rot1/Rot2 axis
                                  and the elbow
I3                                The length of the   l3 > 0
                                  forearms, between
                                  the elbow and the
                                  edge of the lower,
                                  movable platform
I4                                The radius of the   l4 ≥ 0
                                  lower platform
Table 32: Additional restriction of the parameters:
l1 ≠ l4 or l2 ≠ l3                This condition has to be met for the axis transformation to work.
                                  If the condition is not fulfilled, then:
                                  ● the size of the upper and lower platform is identical
                                  ● the upper arms and forearms are the same length
                                  Then the condition is not fulfilled.
                                  In this case, the robot has a special structural singularity: As
                                  soon as all axis values are less than or equal to 0, the solution
                                  of the forward transformation is always the origin of the robot

Solution selection
 With the 2-axis delta robot, there are several solutions for both forward and
 backward transformation.

Forward transformation
 For the forward transformation, there are one or two different solutions for a
 specified axis position:

 with rotary axes

 with rotary axes
 The position of the elbows is clearly determined by the position of the rotary
 axes Rot1 and Rot2. However, the movable platform could be located either
 above the elbows (Fig. 154) or below the elbows (Fig. 155).
 In the axis transformation, it is assumed that the robot is always in the lower
 solution (Fig. 155).

Inverse position kinematics
For the backward transformation, there are up to 2 solutions per arm of the
robot for a specified Cartesian position. This results in a maximum of 2² = 4
different solutions in which the arms are angled inwards or outwards.

with rotary axes

 The axis transformation always selects the outer solution for both arms of
 the robot. Moving to an inner elbow position is possible, for example, using
 motion commands in the axis space. If the robot is in this situation, motions
 in Cartesian space are no longer possible, as these would cause a change to
 the outer solution.

Singularities of a 2-axis delta robot with rotary axes
With a 2-axis delta robot, singularities occur at the upper and lower edge of
the working area

Singularities at the lower edge of the working area
These singularities can also be referred to as elbow singularities. They occur
when the shoulder, elbow and connection point to the moving platform are
in line for at least one arm of the 2-axis delta robot. In addition to the restric‐
tions in the direction of motion, it would be possible in this singularity for a
change from the outer to the inner elbow solution to take place.

 At Fig. 157, the right arm of the 2-axis Delta robot is fully extended. It is
 no longer possible to move downwards in the direction of the outstretched
 arm. In addition, an instantaneous upward motion in the direction of the out‐
 stretched arm is not possible, as the shoulder of the outstretched arm would
 have to rotate too quickly.

Singularities at the upper edge of the working area
The design of the robot has to be taken into account for the singularities at
the upper edge of the working area. For 2-axis delta robots with the property
l1 + l2 < l3 + l4, the following singularity can occur at the upper edge of the
working area:

delta robots
In this type of singularity, the elbow is completely folded in. The shoulder,
elbow and connection point to the moving platform are in line here. In this
case, upward motion in the direction of the folded arm is no longer possible.
In addition, an instantaneous downward motion in the direction of the folded
arm is not possible, as the shoulder of the folded arm would have to rotate
too quickly. In this type of singularity, a change from the outer to the inner
elbow solution could occur. For 2-axis delta robots with the property l1 + l2
> l3 + l4, the following singularity can occur at the upper edge of the working
area:

delta robots
This singularity occurs when the forearms are positioned in such a way that
the elbows can no longer be moved outwards. In this position, it is not pos‐
sible to predict in which direction the moving platform moves. Transitions
from the lower to the upper solution of the forward transformation can there‐
fore occur here. Linear motions can no longer be performed as soon as the
robot is in the upper solution.

    Axis transformation for 2-axis parallelogram
Table 33: Overview of 2-axis parallelogram robot
ID                                      Parallelogram_TwoAxis
Type                                    Basic transformation
License                                 SWL-XCx-MOT-KINxLEVEL2xxx-NNNN
Required axes                           2 (rotary axes)
Compatible with orientation transfor‐   No
mations

Structure
The 2-axis parallelogram robot consists of two rotary axes (Rot1, Rot2), with
one arm each. Another link is attached to each of the two arms. The arms
are connected to each other at a connection point (J in ⮫ Further information
on page 241) to form a closed chain. We can therefore speak of an upper
arm (O) and a lower arm (U), with the upper arm being the limb directly
connected to the rotary axis. The elbow (E) is the point at which the upper
arm is connected to the forearm. The flange (F) is firmly connected to the
lower arm of the first rotary axis via another link. The angle between the lower
arm of the first rotary axis and the link that runs between the elbow of the
first rotary axis and the flange can be adjusted during configuration.

 upper arm (O) and lower arm (U)
 The 2-axis parallelogram is positioned via two rotary axes that can rotate
 around the Z-axis. This allows the end effector to be positioned in the XY
 plane. Depending on the direction of rotation of the axis, a counterclockwise
 axis motion takes place when entering a positive axis angle. It is not possible
 to change the orientation of the end effector individually due to the geometry.
 The origin of the transformation is located at the intersection of the two upper
 arms, where the rotary axes are also connected.

 The robot structure of the parallelogram is restricted which affects the posi‐
 tion of the connection point. To verify that the robot has a permissible setup,
 the position of the elbow (E2 in the figures in Table 2) of the second rotary
 axis relative to the forearm of the first rotary axis can be used. If this point
 (E2) is on the right-hand side of a line starting from the elbow of the first
 rotary axis (E1) through the connection point (J), it is a permissible configura‐
 tion. However, if the point is on the left-hand side, this configuration is not
 permitted for this axis transformation.

Table 34: Examples of permitted and non-permitted parallelogram configurations
Permitted

Not allowed

Parameterization
The lengths of the individual arms are defined by the respective parameters.
They have be greater than zero for each link. For the transformation, it is not
necessary for opposite sides to be the same length.
In addition to the arm lengths, the fixed angle between the arms l2 and
l3 can also be specified via the angle parameter a1. An angle of 20° approx‐
imately corresponds to the position of a1 shown in ⮫ Further information
on page 243.

  The possible parameters for configuring the 2-axis parallelogram are listed
  under ⮫ Further information on page 243. The angle parameter a1 is optional
  and 0° by default. All other values are always required. The optional param‐
  eter is marked in bold in the table.

Table 35: Overview of the parameters of the 2-axis parallelogram
Parameters                                  Description                    Condition
l1                                          Length of the link connected l1 > 0
                                            to the Rot1 axis (upper arm
                                            of the first rotary axis)
l2                                          Length of the link connected l2 > 0
                                            to the flange
l3                                          Length of the link between     l3 > 0
                                            the end of the upper arm of
                                            the first rotary axis (l1) and
                                            the connection point (lower
                                            arm of the first rotary axis)
l4                                          Length of the link between     l4 > 0
                                            the end of the upper arm of
                                            the second rotary axis (l5)
                                            and the connection point
l5                                          Length of the link connected l5 > 0
                                            to the Rot2 axis (upper arm
                                            of the second rotary axis)
a1                                          Size of the fixed angle        0° ≤ a1 ≤ 360°
                                            between the lower arm of the
                                            first rotary axis (l3) and the
                                            flange part (l2)
                       In addition to the condition that none of the values may be negative, there is
                       an additional restriction on the parameters. This restriction concerns the side
                       length ratio and is described under ⮫ Further information on page 243.
                       Table 36: Additional restriction of the parameters of the parallelogram
                       l1 < l3 + l4 + l5   These conditions must all be met, otherwise the axis trans‐
                       l3 < l1 + l4 + l5   formation cannot be realized. If one of the conditions is
                                           violated, it is not geometrically not possible to generate a
                       l4 < l1 + l3 + l5
                                           square using these parameters.
                       l5 < l1 + l3 + l4

Solution selection
In case of the axis transformation of the 2-axis parallelogram robot, there are
several valid options how the individual connections and joints of the robot
can be positioned and oriented. There are different options for forward and
backward transformation, referred to below as solutions, which are described
in more detail below.

Forward transformation
There are two different solutions for the forward transformation. This con‐
cerns the connection point (J), which can be located either on one side or the
other of a line between the two elbows. This would result in either a convex
or a concave solution. As it is not possible to know at which of the two solu‐
tions the connection point is located on the basis of the two rotation angles
alone, the same solution is always used here and it is assumed that the point
is located at this point. This also results in the restriction for the robot design
described above, in which the right-hand variant under ⮫ Forward transforma‐
tion on page 244 is not permitted.

parallelogram forward transformation, of which the example on the right is

not a permitted configuration

Inverse position kinematics
The backward transformation can have up to four different solutions, starting
from the current position of the flange. The aim is not to switch between dif‐
ferent solutions, which are described in the following. The solution is deter‐
mined on the basis of the current axis position when executing the motion
or an additionally specified position. If several valid solutions remain after
excluding all invalid solutions, the solution with the smallest difference to the
current axis position is selected.
The first two solutions concern the elbow of the first arm. This can be either
above or below the dashed blue line from the origin to the target point, as
can be seen under ⮫ Inverse position kinematics on page 245. In the example
under ⮫ Inverse position kinematics on page 245, the right-hand variant would
not be a valid solution, as the elbow of the second arm is on the wrong
side of the first upper arm and therefore there is no permitted parallelogram
configuration, as described at the beginning of the robot design.

parallelogram backward transformation, of which the example on the right
is not a permitted configuration
For each of the two solutions of the first elbow, there are in turn two solu‐
tions for the elbow of the second rotary axis. The solutions are visualized at
⮫ Inverse position kinematics on page 245. The point can be either to the left
or right of the blue line. The selection is again based on the orientation of the
current axis positions, taking into account the current solution path.

 parallelogram backward transformation

Restrictions on the workspace
In certain configurations, the angular distance between the two rotary axes
may not exceed (αmax) or fall below (αmin) a certain value, as there are no
solutions for this range. In case of an invalid angle combination, the axis
transformation cannot be enabled.

 and maximum angular distance (αmax)
 A maximum angle always occurs when l3 + l4 < l1 + l5 is fulfilled. A minimum
 angle, on the other hand, always occurs when l3 + l4 < l1 + l5 is fulfilled.
 There may also be configurations in which there is both a minimum and a
 maximum intermediate angle.

Singularities
The 2-axis parallelogram has two singularities, whereby it depends on the
parameterization of the robot whether they can also be realized.

 Singularity with fully extended arm
 At the end of the parallelogram, the upper arm/forearm combination forms a
 straight line. The angle (β) of this connection is 180°. Further outward motion
 is then no longer possible in this position. This results in the loss of one
 degree of freedom in the motion of the end effector.

 Singularity with superimposed arms
 For setups in which both upper arms have the same length, another singu‐
 larity can occur if the angle (α) between the two rotary axes becomes very
 small and thus both elbows overlap at the same point. In this case, it is no
 longer possible to clearly determine the position of the connection point and
 the end effector, as these two points could be located anywhere on a circle
 around the elbows.

    Axis transformation for 2-axis delta slide
Table 37: Overview of 2-axis delta slide robots
 ID                                      Delta_TwoAxisSlide
 Type                                    Basic transformation
 License                                 SWL-XCx-MOT-KINxLEVEL2xxx-NNNN
 Required axes                           2 (linear axes)
 Compatible with orientation transfor‐   Yes
 mations

Structure
The 2-axis delta slide has two linear axes (Lin1 and Lin2). Both axes run on
the same rail along the X-axis, which runs through the origin of the coordinate
system. Due to this structure on the same rail, the restriction applies that axis
Lin2 always has to have a greater value than axis Lin1, i.e. the position of axis
Lin1 must not overtake the position of axis Lin2. The zero positions of both
axes are at the origin, the intersection of the x-axis and the y-axis.
There is one arm on each of the two linear axes, which are connected at one
point, the connection point, so that a closed kinematic chain is formed. These
two arms always have the same length.
Starting from this connection point , an additional third arm can be located
(cf. ⮫ Further information on page 247 left). The arm has an individual length.
This third arm is mounted at a fixed angle in relation to the first arm (the
arm from Lin1 to the connection point). This angle runs clockwise. In the

   zero position of this angle, the alignment of the third arm corresponds to the
   alignment of the first arm (cf. ⮫ Further information on page 248 where this
   angle is 205°).
   Depending on the third arm, the flange is located either directly at the end of
   this arm or, if the third arm is missing, at the connection point (see Figure 1,
   right). As with other delta axis transformations, it is not possible to change
   the orientation of the flange with the 2-axis delta slide. It is mechanically
   ensured that its orientation corresponds to the orientation of the machine
   coordinate system.

        Lin1                     Lin2            Lin1                     Lin2

Parameterization
The possible parameters for configuring the 2-axis delta slide are listed under
⮫ Further information on page 248 and shown schematically under ⮫ Further
information on page 248.
Table 38: Overview of the parameters of the 2-axis delta slide
Parameters                                 Description                    Condition
l1                                         Length of the connections      l1 > 0
                                           between the axes and the
                                           connecting joint
l2                                         Length of the connection       l2 ≥ 0
                                           between the connecting joint l1 ≠ l2 for a1 = 0
                                           and the flange
a1                                         Angle between the connection 0° ≤ a1 ≤ 360°
                                           on the first axis and the con‐
                                           nection to the flange

          l1                      l1                 l1                     l1
                        a1

                             l2

Solution selection
For the 2-axis delta slide with third arm, there are two distinct working spaces
for the flange depending on the parameters and axis values: the left work‐
space and the right working space. The working space in which the flange is
located can be determined by comparing its X-coordinate with the value of
axis Lin1. The flange (F) is located either to the left of axis Lin1 or to the right
of axis Lin1 (see ⮫ Further information on page 249).
The robot can switch between the two workspaces by moving the axes. A
robot whose fixed angle a1 is between 90° and 180° (e.g. left figure in ⮫ Fur‐
ther information on page 247) always operates in the right-hand area.

                                              Lin1   Lin2

                                       F

                                           Left   Right

                            Lin1                       Lin2

                                       F

                     Left      Right

 configuration

 Forward transformation
 The forward transformation always has only one valid solution, except in the
 case of a singularity, which is explained in a subsequent section. As men‐
 tioned above, the forward transformation, i.e. the motion of the robot in the
 axis coordinate system (ACS), can be used to switch back and forth between
 the left and right workspaces.

 Inverse position kinematics
 The backward transformation can have two valid solutions, which refer to the
 left and right workspace. The selection of the correct solution, i.e. whether
 the flange is on the left or right, is made during the backward transformation
 on the basis of the last robot pose, so that the backward transformation
 always remains consistent in the respective workspace.
 If the flange is located exactly on the boundary of the two workspaces, the
 solution with the smaller axis motion is selected.

Restrictions on the workspace
For all configurations, it is possible that certain axis value combinations of
Lin1 and Lin2 are invalid. As explained at the beginning, this includes the
case of identical axis values or if Lin2 has a smaller value than Lin1. In addi‐
tion, the distance between Lin1 and Lin2 must not be twice the arm length
l1 or more. If one of these invalid axis value combinations occurs, the axis
transformation cannot be enabled.

Singularities
The 2-axis delta slide has three singularities, whereby it depends on the
parameterization of the robot whether they can all be realized.

 Singularity in case of identical axis values
 If both linear axes have the same value, the position of the connection point
 (C) can no longer be clearly determined. In this case, every point on a circle
 with radius l1 and origin in Lin1 or Lin2 is a theoretically valid position
 for the connection point (cf. ⮫ Singularity in case of identical axis values

on page 250). This position is also mechanically impossible, as both axes
operate on the same rail. Such positions of the robot, which correspond to
the singularity, are therefore prohibited in the axis transformation.

                             Lin1 = Lin2

                                               F

                               C

Singularity with linear alignment of both upper arms and the connection point
If the distance between axis Lin1 and axis Lin2 is twice the value of l1, both
upper arms form a straight line with the connecting point (C) in the middle.
It would no longer be possible to move the axes apart. Moving together is
also problematic, as it cannot be predicted as to whether the connection
point (C) would move up or down from this position (see ⮫ Singularity with
linear alignment of both upper arms and the connection point on page 251 ).
Accordingly, positions of the robot that correspond to the singularity are pro‐
hibited in the axis transformation.

                      Lin1                              Lin2

                                               C

                                           F

 Singularities when Lin1 matches the X-coordinate of the flange
 The third singularity occurs when the x-coordinate of the flange has the same
 value as the Lin1 axis (see ⮫ Singularities when Lin1 matches the X-coordinate
 of the flange on page 251). This pose represents the boundary between the
 left and right workspaces. In this singularity, a significant motion of both axes
 is necessary for the flange to move upwards.
 This singularity can only occur for parameterizations in which a1 is either
 greater than 180° or in which l2 is greater than l1 and a1 is less than 90°.
 For all other robots, this pose is outside the workspace and therefore cannot
 occur.

                                 Lin1            Lin2

                             F

                          Left      Right

 flange

Axis transformation for 3-axis Adabot
Table 39: Overview of 3-axis Adabot robots
 ID                                         Adabot_ThreeAxis
 Type                                       Basic transformation
 License                                    SWL-XCx-MOT-KINxLEVEL2xxx-NNNN
 Required axes                              3 (rotary axes)
 Compatible with orientation transfor‐      No
 mations

Structure
The 3-axis Adabot has three rotary axes (Rot1, Rot2, Rot3). The base of the
robot is formed by the centrally located axis Rot3, which also serves as the
origin of the coordinate system. On the other two rotary axes (Rot1, Rot2)
there is one arm each, both of which are connected to an elbow joint. The
ends of the two arms are mechanically connected via a joint. The flange is
located below the connection point. The orientation of the link between the
connection point and the flange is maintained by a mechanical device so that
it is aligned with the rotary axis Rot3.
By adjusting the rotary axis Rot3 the entire mechanism can be rotated around
the X-axis. When the axes are at their zero positions, the flange is in the XZ
plane.

  For the axis transformation to function correctly, the positioning angle of the
  rotary axis Rot3 has to be within the range of −90° to +90°. This restriction
  means that the flange is always located below the XY plane.

Parameterization
The 3-axis Adabot is defined by six length parameters, and the length l5 can
be set to zero. All other lengths have to be greater than zero. Furthermore,
the distance (2 × l6) between the axes Rot1 and Rot2 must not exceed the
combined length of the two arms.

The ⮫ Further information on page 253 lists the available parameters for con‐
figuring the 3-axis Adabot robot.
Table 40: Overview of the parameters of the 3-axis Adabot robot
Parameters                               Description                  Condition
l1                                       Length of the connection,    l1 > 0
                                         which is directly located on
                                         the Rot1 axis.
l2                                       Length of the connection,    l2 > 0
                                         which is directly located on
                                         the Rot2 axis.
l3                                       Length of the second connec‐ l3 > 0
                                         tion of the arm Rot1.

Parameters                                Description                  Condition
l4                                        Length of the second connec‐ l4 > 0
                   tion of the arm Rot2
l5                                        Length of the connection     l5 ≥ 0
                   between the flange and the
                   common connection point.
l6                                        Absolute distance between    l6 ≥ 0
                   the origin and Rot1/Rot2.    l6 + l6 < l1 + l2 + l3 + l4

Tool-dependent parameterization
Due to the specified orientation of the last link of the Adabot, the kinematics
are incompatible with the "tool length" command option. By selecting an
appropriate value for the length parameter l5, a tool offset can be mapped
in the direction of the last link.

Solution selection
Forward transformation
The forward transformation for the Adabot is generally not unique, since there
are two valid positions for the connection point of the two arms (Rot1, Rot2).
To resolve the ambiguity, the solution chosen for this kinematic configuration
is always the one in which the connection point lies below an imaginary line
connecting the two elbow joints. The solution selection is shown in ⮫ Forward
transformation on page 254

Inverse position kinematics
Due to the elbow joints of the two arms (Rot1, Rot2), the inverse transforma‐
tion is not unique. For the 3-axis Adabot, the solution in which both elbow
joints point outward is therefore always selected. This choice of solution for
the positions of the two joints is illustrated in ⮫ Inverse position kinematics
on page 254. In this case, the elbow of the arm attached to Rot1 is always
to the left of a line drawn from the Rot1 axis to the connection point. Accord‐
ingly, the elbow for the arm at Rot2 is always to the right of the line drawn
from the Rot2-axis.

Singularities
Due to its elbow joints, the 3-axis Adabot has singularities at the end of its
working area, which is defined by its two arms.

Singularity with fully extended Rot1/Rot2 arm
If the flange at the bottom of the working area moves, one of the arms is fully
extended. When exiting the singularity, the solution selection in the transfor‐
mations chooses the solution in which the elbows point outward. ⮫ Singu‐
larity with fully extended Rot1/Rot2 arm on page 255 shows the Adabot in the
corresponding singularities.

Singularities at the upper end of the working area
At the upper end of the working area, two additional singularities occur
depending on the length parameterization. If the elbow can move into the
upper XZ half-plane, the two segments of an arm may end up parallel to each
other. If the length parameters do not allow this pose to be achieved, the
forearms of both arms are parallel to each other. In both cases, the robot is
in a singular position. ⮫ Singularities at the upper end of the working area
on page 255 shows the Adabot in both singularities.

Axis transformation for 3-axis flex stamper
Table 41: Overview of 3-axis flex stamper robots
 ID                                         FlexStamper_ThreeAxis
 Type                                       Basic transformation
 License                                    SWL-XCx-MOT-KINxLEVEL2xxx-NNNN
 Required axes                              3 (rotary axes)
 Compatible with orientation transfor‐      No
 mations

Structure
The 3-axis flex stamper robot has three rotary axes (Rot1, Rot2, Rot3). The
axes separated by a configurable distance Rot1 and Rot2 form the basis of
the robot. Here, the position of the Rot1 axis corresponds to the origin of
the coordinate system. There is an arm on each of the two rotary axes (Rot1,
Rot2). Each of these arms consists of two links that are connected by an
elbow joint. The two arms are connected via a common connection point,
forming a closed kinematic chain. The vertical connection of the second arm
creates a characteristic "T" section for the Flex Stamper. The exact shape and
form of this "T" piece depends on the parameterization of the robot.

                                               Rot1

                       Rot2

                                     Rot3

 The third rotary axis (Rot3) is located at the remaining end of the "T" piece
 and enables the flange to be aligned in the XY plane. In the zero position of
 Rot3, the arm located directly at Rot3 points in the direction of the "T" piece.

  There is a restriction in the robot structure of the flex stamper that affects the
  position and alignment of the "T" piece. The elbow joints of the two arms gen‐
  erally allow four different positions for the "T" piece. A detailed description
  of the restrictions resulting from the solution selection can be found in the
  section on forward transformation.

Parameterization
The following assumptions are made for the correct use of the axis transfor‐
mation:
  ● The rotary axes specified as Rot1 and Rot2 can only approach values
     between -270° and 90°. In the zero position of Rot1 and Rot2, both arms
     point in the direction of the X-axis
  ● The rotary axis specified as Rot3 points in its zero position in the direction

     of the joint on which it is located. The axis transformation does not restrict
     the value range of Rot3
  The 3-axis flex stamper robot is defined via eight length parameters, whereby
  the lengths l5, l6 and l8 can be set to zero. All other lengths have to be
  greater than zero. If the length (l8) of the vertically mounted section is set to
  zero, there is no longer a fixed 90° angle for the point of application.

                                  l5

                         l7                      l1

                                                           l3
                                                      l8
                                       l4
                                                                l2

                                            l6

The possible parameters for configuring the 3-axis flex stamper robot are
listed under ⮫ Further information on page 257.
Table 42: Overview of the parameters of the 3-axis flex stamper robot
Parameters                                Description                     Condition
l1                                        Length of the connection,       l1 > 0
                                          which is directly located on
                                          the Rot1 axis
l2                                        Length of the connection        l2 > 0
                                          between the Rot3 axis and
                                          the first joint of the Rot1 arm
l3                                        Absolute distance at which      l3 > 0
                                          the right-angled attachment of
                                          the connection between the
                                          Rot3 axis and the first con‐
                                          nection of the arm at Rot1 is
                                          located
l4                                        Length of the second connec‐ l4 > 0
                                          tion of the arm Rot2

Parameters                                Description                     Condition
l5                                        Absolute distance between       l5 ≥ 0
                   the axes Rot1 and Rot2
l6                                        Length of the connection        l6 ≥ 0
                   between the Rot3 axis and
                   the flange

Solution selection
Depending on the configuration, there are up to four different solutions for
both forward and backward transformation. The solutions result from the nec‐
essary alignment of the two elbow joints.

Forward transformation
The position of the connection point of the two arms and the alignment of
the "T" piece result in four possible positions for the robot. This ambiguity
is resolved by limiting it to a single solution. The consistent selection of the
same solution results in the limitations in the robot configuration mentioned
in the introduction.
The position of the connection point of the two arms and the alignment of
the "T" piece result in four possible positions for the robot. This ambiguity
is resolved by limiting it to a single solution. The consistent selection of the
same solution results in the limitations in the robot configuration mentioned
in the introduction. The first case differentiation deals with the position of
point H in relation to the two elbows (point D, point B). In the supported
configuration, point H has to be on the right-hand side of a line from point
D to point B (see the figure on the left under ⮫ Forward transformation
on page 258).
The second case distinction deals with the position of point C in relation to
the two points H and B. In the supported configuration, point C has to be
located on the right-hand side of a line from point H to point B (see figure on
the right under ⮫ Forward transformation on page 258).

Inverse position kinematics
The four different solutions for the backward transformation result from two
independent decisions on the alignment of the elbow joints (point B, point
D). To determine the position of the joint points and thus the axis values, the
current position of the robot has to be used as an indicator for the desired
solution.
A distinction is made between solutions in which:

 ● point B is to the left or right of a line from point A to point C
 ●
   point D is to the left or right of a line from point G to point H
 The two case decisions are presented under ⮫ Inverse position kinematics
 on page 258.
 Taking into account the current pose of the robot, all four possible solu‐
 tions are compared with regard to the direction of the elbows and the corre‐
 sponding solution is selected. If the robot is in a singularity, it may not be
 possible to clearly determine the orientation of the elbows. In these cases,
 the solution with the smallest deviation from the robot's current axis values
 is selected. In addition, the solution in which point B is to the left of the
 line starting from point A to point C and point D is to the right of the line
 starting from point G to point H is slightly preferred in the solution selection.

 The preference leads to the solution shown in the figures and is indicated by
 arrows in ⮫ Inverse position kinematics on page 258.
 Solutions in which point H is above the line between the elbow points are
 categorically excluded. This exclusion is analogous to the solution selection in
 the forward transformation.

Restrictions on the working area
In case of certain robot parameterizations, the workpace may be restricted by
the closed kinematic chain. Possible restrictions arise from the mechanical
connection of the links with the lengths l1, l3, l4, l5, l7 and l8. Axis value
combinations in which the lengths of the links do not correspond to the
geometric requirements of the robot do not allow the axis transformation to
be activated.

Singularities
The 3-axis flex stamper robot has four singularities. It depends on the parame‐
terization of the robot whetherthey can all be realized.

 Singularity with fully extended Rot1/Rot2 arm
 At least one arm (points A, B and C or points G, D and H) forms a straight
 line at the edges of the working area of the Flex-Stamper. The angle of this
 connection is 180°. When extended, the alignment of the elbow points (point
 B or D) can no longer be determined. Another motion involves bending the
 elbow to the right or left. The two singularities are shown in ⮫ Singularity

with fully extended Rot1/Rot2 arm on page 259. When leaving the singularity,
the most obvious solution for the current axis values is selected by the case
decision of the backward transformation.

Singularity with superimposed arms
Under appropriate configurations, the two elbow points of the two arms can
overlap. In this case, the rest of the mechanism is free to rotate around this
point. In this singularity, it is not possible to calculate the forward and back‐
ward transformations.

Singularity with linear alignment of both arms with the connection point
If the two elbow points (B and D) and the connecting point H are on a line,
the kinematics loses one degree of freedom in this pose, since the motion
of the two rotary axes Rot1 and Rot2 would each result in the same flange
motion.

point

    Axis transformation for 1D orientations on the flange
Table 43: Overview of 1D orientations on the flange (rotation around the X-
axis)
ID                                     Orientation_MountedXRotation
Type                                   Orientation transformation
License                                SWL-XCx-MOT-KINxLEVEL2xxx-NNNN
Required axes                          1 (rotary axis)
Table 44: Overview of 1D orientations on the flange (rotation around the Y-
axis)
ID                                     Orientation_MountedYRotation
Type                                   Orientation transformation

 License                                 SWL-XCx-MOT-KINxLEVEL2xxx-NNNN
 Required axes                           1 (rotary axis)
 Table 45: Overview of 1D orientations on the flange (rotation around the Z-
 axis)
 ID                                      Orientation_MountedZRotation
 Type                                    Orientation transformation
 License                                 SWL-XCx-MOT-KINxLEVEL2xxx-NNNN
 Required axes                           1 (rotary axis)

Structure
The 1D orientation transformation can be used to control a single rotary
axis that is mounted on the flange of a kinematic system without orientation
options. This allows the tool to be rotated around either the X-axis, the Y-axis
or the Z-axis. The 1D orientation transformation is assigned to a kinematic as
an extension of the basic transformation.

Variant
 The control provides three types of 1D orientation transformation. The var‐
 iants differ in the orientation of the rotary axis:
 ● Rotation around the X-axis; see Fig. 188 and ⮫ Table 43 Overview of 1D
   orientations on the flange (rotation around the X-axis) on page 261
 ● Rotation around the Y-axis; see Fig. 189 and ⮫ Table 44 Overview of 1D
   orientations on the flange (rotation around the Y-axis) on page 261
 ● Rotation around the Z-axis; see Fig. 190 and ⮫ Table 45 Overview of 1D
   orientations on the flange (rotation around the Z-axis) on page 262

                           Z
                                Y

                                X
                                                  Rot1
 position

                                                    Rot1

                          Z
                               Y

                               X

 position

                              Z
                                       Y

                                       X

                                                     Rot1

 position

Parameterization
All three versions of the 1D orientation transformation offer configurable off‐
sets from the robot flange to the rotary axis and from the rotary axis to the
tool.

                         Z                                      Z

                                  X                                  Y

                                           z1

                             x1                         y1

                                      x2        z2                  y2

 Fig. 191 shows a schematic layout of the rotary axis with alignment along the
 X-axis. The parameters x1, y1 and z1 describe the offset from the robot flange
 to the rotary axis. The parameters x2, y2 and z2 describe the offset from the
 rotary axis to the tool. All parameters listed here are optional.
Parameters                                                     Description
Robot flange → Rotary axis        x1                           The displacement from the robot flange to
                                           the rotary axis in the X-direction
              y1                           The displacement from the robot flange to
                                           the rotary axis in the Y-direction
              z1                           The displacement from the robot flange to
                                           the rotary axis in the Z-direction
Parameters                                                     Description
Rotary axis → Tool                x2                           The displacement from the rotary axis to
                                           the tool in the X-direction
              y2                           The displacement from the rotary axis to
                                           the tool in the Y-direction
              z2                           The displacement from the v to the tool in
                                           the Z-direction

                               Z                                 Z

                       X                                              Y

                                        z1

                           x1                               y1

                      x2                         z2                       y2

                           Z                                              Z

                                   X                                           Y

                                            z1

                 x1                                                                y1

                                       x2              z2            y2

Fig. 192 and Fig. 193 show the structure of the rotary axis again for the
other two versions in the Y- and Z-directions. The meaning of the optional
parameters does not change between the different versions.

Solution selection
The 1D orientation transformation always selects the shorter direction of rota‐
tion from the current to the target position.

Axis transformation for 2D orientations on the flange
Table 46: Overview of 2D orientations on the flange (rotation around the X-
axis and the Y-axis)
ID                                                    Orientation_MountedXYRotation
Type                                                  Orientation transformation
License                                               SWL-XCx-MOT-KINxLEVEL3xxx-NNNN
Required axes                                         2 (rotary axes)
Table 47: Overview of 2D orientations on the flange (rotation around the Y-
axis and the X-axis)
ID                                                    Orientation_MountedYXRotation
Type                                                  Orientation transformation
License                                               SWL-XCx-MOT-KINxLEVEL3xxx-NNNN
Required axes                                         2 (rotary axes)
Table 48: Overview of 2D orientations on the flange (rotation around the z-axis
and the x-axis)
ID                                                    Orientation_MountedZXRotation
Type                                                  Orientation transformation
License                                               SWL-XCx-MOT-KINxLEVEL3xxx-NNNN
Required axes                                         2 (rotary axes)
Table 49: Overview of 2D orientations on the flange (rotation around the Z-
axis and the Y-axis)
ID                                                    Orientation_MountedZYRotation
Type                                                  Orientation transformation

 License                                    SWL-XCx-MOT-KINxLEVEL3xxx-NNNN
 Required axes                              2 (rotary axes)

Structure
With a 2D orientation transformation, two rotary axes can be actuated, ena‐
bling a basic transformation without orientation option to align the direction
of impact of a tool (z-axis) in any direction. The rotation of the tool around
the Z-axis cannot be controlled, which makes it particularly useful to mount
rotationally symmetrical tools on the flange.

Variant
 The control supports four different variants of 2D orientation transformation,
 which can orient the tool's direction of impact in any direction (apart from

 restrictions due to the design of the kinematics). Other variants do not make
 sense, as they would either rotate twice around the same axis or would not
 allow the tool to be aligned in any direction.
 The variants differ in the orientation of the rotary axis:
 ● First rotation around X-axis, second rotation around twisted Y-axis; see Fig.
   194 and ⮫ Table 46 Overview of 2D orientations on the flange (rotation
   around the X-axis and the Y-axis) on page 264
 ● First rotation around Y-axis, second rotation around twisted X-axis; see Fig.
   195 and ⮫ Table 47 Overview of 2D orientations on the flange (rotation
   around the Y-axis and the X-axis) on page 264
 ● First rotation around Z-axis, second rotation around twisted X-axis; see Fig.
   196 and ⮫ Table 48 Overview of 2D orientations on the flange (rotation
   around the z-axis and the x-axis) on page 264
 ● First rotation around Z-axis, second rotation around twisted Y-axis; see Fig.
   197 and ⮫ Table 49 Overview of 2D orientations on the flange (rotation
   around the Z-axis and the Y-axis) on page 264

                               Z               Rot1
                                   Y Rot2

                                   X

 zero position

                                   Rot1

                               Z              Rot2
                                   Y

                                   X

 zero position

                                                 Rot1

                                  Z
                                      Y
                                                        Rot2
                                      X

   zero position

                                                 Rot1

                                  Z       Rot2
                                      Y

                                      X

   zero position

Parameterization
All four variants provide the option of using parameters to specify the offsets
between the flange of the basic transformation and the first axis of rotation,
the first axis of rotation and the second axis of rotation as well as the second
axis of rotation and the flange of the 2D orientation transformation. All param‐
eters are optional.
                                          z1

                            x1                                  y1

                             x2
                                          z2

                                                                y2

                             x3                                  y3
                                          z3

              Z                                                        Z
                   X                                                       Y

   Fig. 198 shows the schematic structure of an XY variant of the 2D orientation
   transformation. Here x1, y1 and z1 describe the offset between the flange
   of the basic transformation (here a delta kinematic) and the first rotary axis
   (Rot1), x2, y2 and z2 the offset between the first rotary axis (Rot1) and the
   second rotary axis (Rot2) and x3, y3 and z3 the offset between the second
   rotary axis (Rot2) and the flange of the 2D orientation transformation.
Parameters                                                     Description
Robot flange → first rotary axis x1                            The X-offset from the flange of the basic
                                           transformation to the first rotary axis
                  y1                       The Y-offset from the flange of the basic
                                           transformation to the first rotary axis
                  z1                       The Z-offset from the flange of the basic
                                           transformation to the first rotary axis

Parameters                                                 Description
first rotary axis → second rotary x2                       The X-offset of the first rotary axis to the
axis                                                       second rotary axis
y2                       The Y-offset of the first rotary axis to the
                       second rotary axis
z2                     The Z-offset of the first rotary axis to the
                       second rotary axis
second rotary axis → flange         x3                     The X-offset from the second rotary axis to
                       the flange of the 2D orientation transfor‐
                       mation
y3                     The Y-offset from the second rotary axis to
                       the flange of the 2D orientation transfor‐

                       mation
z3                     The Z-offset from the second rotary axis to
                       the flange of the 2D orientation transfor‐
                       mation

                      z1                    y1
            x1

            x2                              y2
                      z2
                      z3

Z               x3                               y3        Z
    X                                                           Y

                       z1

                 x1                          y1

                 x2                          y2
                       z3 z2

                 x3                           y3

Z                                                  Z
        X                                                   Y

                                   z1
                           x1                            y1

                            x2

                                   z3 z2
                                                         y2
                            x3                            y3

             Z                                                 Z
                 X                                                 Y

Fig. 199, Fig. 200 and Fig. 201 show the schematic structure and the corre‐
sponding parameters of the three other variants. The meaning of the parame‐
ters does not differ between the different variants.

Singularities

basic transformation)
With the ZX and ZY variants of the 2D orientation transformation, a singularity
occurs if the tool's direction of impact is to be oriented along the Z-direction
(see Fig. 202). In this situation, the angle of the second axis (rotation around
X or Y) has to be selected at 0 or a multiple of 180°, while the angle of the
first axis (rotation around Z) is freely selectable and has no influence on the
direction of impact. To leave this orientation in a desired direction, it may
be necessary to first bring the first axis into a suitable position before it is
possible to tilt the tool in the desired direction with the second axis. It can
also happen that the first axis stops and is rotated when moving through this
orientation. This behavior also occurs in configurations in which the first and
second axes of the orientation transformation are offset. In this case, a Car‐
tesian change in position generated by the orientation transformation (when
rotating around the first axis) is compensated for by the base transformation.

  basic transformation)
  A similar situation occurs with the XY or YX variant if the second angle is at
  -90° or 90° and the tool is therefore aligned in the x- or y-direction (see Fig.
  203).

Solution selection
Outside the singularities, there are two options for each orientation of the
tool joint direction, which can be achieved with the 2D orientation transfor‐
mation.

                                  Z    Y
                                              X

                                 Z

                                X
                                      Y
  Fig. 204 shows both solutions of an ZX variant for the same impact direction
  (along the Z-axis). In the solution on the left, the first axis is set to 0°, while
  the second axis is rotated by -90°. In the solution on the right, the same
  orientation is achieved by rotating the first axis by 180° and the second axis

 by 90°. In this case, the transformation function selects the optimal axis posi‐
 tion based either on the current axis positions or on an additional specified
 position. The solution that requires the smaller motion for the first rotary axis
 is always selected.

    Axis transformation for 1A orientations with commanded and interpolated axis values for
    orientation axes
Table 50: Overview of 1A orientations on the flange (rotation around the x-
axis)
 ID                                      AxisOrientation_MountedXRotation
 Type                                    Orientation transformation
 License                                 SWL-XCx-MOT-CARTESIANxxxx-NNNN

 Required axes                           1 (rotary axis)
 Table 51: Overview of 1A orientations on the flange (rotation around the y-
 axis)
 ID                                      AxisOrientation_MountedYRotation
 Type                                    Orientation transformation
 License                                 SWL-XCx-MOT-CARTESIANxxxx-NNNN
 Required axes                           1 (rotary axis)
 Table 52: Overview of 1A orientations on the flange (rotation around the z-
 axis)
 ID                                      AxisOrientation_MountedZRotation
 Type                                    Orientation transformation
 License                                 SWL-XCx-MOT-CARTESIANxxxx-NNNN
 Required axes                           1 (rotary axis)

Structure
The 1A orientation transformation is assigned as an extension of the base
transformation of a kinematic system. Using the 1A orientation transformation,
a single rotary axis can be controlled that is mounted on the flange of a
kinematic mechanism without orientation capability. This allows the tool to
be rotated around either the X-axis, the Y-axis or the Z-axis. Orientation is
controlled directly by programming the axis values. The motion is executed as
programmed. An axis without modulo calculations moves linearly to the pro‐
grammed position. A modulo axis is controlled by the programming logic and
moves in the positive direction of rotation, the negative direction of rotation,
or along the shortest path.

Variant
 The control provides three variants of the 1A orientation transformation. The
 variants differ in the orientation of the rotary axis:
 ● Rotation around the X-axis; see Fig. 205 and ⮫ Table 50 Overview of 1A
   orientations on the flange (rotation around the x-axis) on page 271
 ● Rotation around the Y-axis; see Fig. 206 and ⮫ Table 51 Overview of 1A
   orientations on the flange (rotation around the y-axis) on page 271
 ● Rotation around the Z-axis; see Fig. 207 and ⮫ Table 52 Overview of 1A
   orientations on the flange (rotation around the z-axis) on page 271

                               Z
                                         Y

                                         X
                                                         Rot1
   zero position

                                                          Rot1

                               Z
                                        Y

                                        X

   zero position

                                   Z
                                         Y

                                         X

                                                       Rot1

   zero position

Parameterization
All three variants of the 1A orientation transformation offer configurable off‐
sets from the robot flange to the rotary axis and from the rotary axis to the
tool.

                           Z                                     Z

                                    X                                 Y

                                             z1

                               x1                         y1

                                        x2        z2                 y2

Fig. 208 shows a schematic layout of the rotary axis with alignment along the
X-axis. The parameters x1, y1 and z1 describe the offset from the robot flange
to the rotary axis. The parameters x2, y2 and z2 describe the offset from the
rotary axis to the tool. All parameters listed here are optional.
Parameters                                                         Description
Robot flange → Rotary axis        x1                               The offset from the robot flange to the
                                              rotary axis in the X-direction
             y1                               The offset from the robot flange to the
                                              rotary axis in the Y-direction
             z1                               The offset from the robot flange to the
                                              rotary axis in the Z-direction
Parameters                                                         Description

Rotary axis → Tool                x2                               The offset from the rotary axis to the tool
                                              in the X-direction
             y2                               The offset from the rotary axis to the tool
                                              in the Y-direction
             z2                               The offset from the v to the tool in the
                                              Z-direction

                                Z                                 Z

                        X                                              Y

                                         z1

                            x1                               y1

                       x2                         z2                       y2

                            Z                                              Z

                                    X                                           Y

                                             z1

                  x1                                                                y1

                                        x2              z2            y2

Fig. 209 and Fig. 210 show the structure of the rotary axis again for the
other two versions in the Y- and Z-directions. The meaning of the optional
parameters does not change between the different versions.

Axis transformation for 2A orientations with specified and interpolated axis values for
orientation axes
Table 53: Overview of 2A orientations on the flange (rotation around the x-axis
and the y-axis)
ID                                                     AxisOrientation_MountedXYRotation
Type                                                   Orientation transformation
License                                                SWL-XCx-MOT-CARTESIANxxxx-NNNN
Required axes                                          2 (rotary axes)

Table 54: Overview of 2A orientations on the flange (rotation around the x-axis
and the z-axis)
ID                                     AxisOrientation_MountedXZRotation
Type                                   Orientation transformation
License                                SWL-XCx-MOT-CARTESIANxxxx-NNNN
Required axes                          2 (rotary axes)
Table 55: Overview of 2A orientations on the flange (rotation around the y-axis
and the x-axis).
ID                                     AxisOrientation_MountedYXRotation
Type                                   Orientation transformation
License                                SWL-XCx-MOT-CARTESIANxxxx-NNNN
Required axes                          2 (rotary axes)
Table 56: Overview of 2A orientations on the flange (rotation around the y-axis
and the z-axis)
ID                                     AxisOrientation_MountedYZRotation
Type                                   Orientation transformation
License                                SWL-XCx-MOT-CARTESIANxxxx-NNNN
Required axes                          2 (rotary axes)
Table 57: Overview of 2A orientations on the flange (rotation around the z-axis
and the x-axis)
ID                                     AxisOrientation_MountedZXRotation
Type                                   Orientation transformation
License                                SWL-XCx-MOT-CARTESIANxxxx-NNNN
Required axes                          2 (rotary axes)
Table 58: Overview of 2A orientations on the flange (rotation around the z-axis
and the y-axis)
ID                                     AxisOrientation_MountedZYRotation
Type                                   Orientation transformation
License                                SWL-XCx-MOT-CARTESIANxxxx-NNNN
Required axes                          2 (rotary axes)

Structure
A 2A orientation transformation allows you to control two rotary axes. Unlike
axis transformation for 2A orientation on the flange—where the orientation is
generally specified by Euler angles—the orientation is controlled directly by
programming the axis values. The motion is executed as programmed. An axis
without modulo calculations moves linearly to the programmed position. A
modulo axis is controlled by the programming logic and moves in the positive
direction of rotation, the negative direction of rotation, or along the shortest
path.

Variant
The control supports six different variants of the 2A orientation transforma‐
tion. Other variants are not recommended as they would rotate twice around
the same axis.
The variants differ in the orientation of the rotary axis:

● First rotation around X-axis, second rotation around twisted Y-axis; see Fig.
  211 and ⮫ Table 53 Overview of 2A orientations on the flange (rotation
  around the x-axis and the y-axis) on page 273
● First rotation around the X-axis, second rotation around the twisted Z-axis;
  see Fig. 212 and ⮫ Table 54 Overview of 2A orientations on the flange
  (rotation around the x-axis and the z-axis) on page 274
● First rotation around Y-axis, second rotation around twisted X-axis; see Fig.
  213 and ⮫ Table 55 Overview of 2A orientations on the flange (rotation
  around the y-axis and the x-axis). on page 274
● First rotation around the Y-axis, second rotation around the twisted Z-axis;
  see Fig. 213 and ⮫ Table 55 Overview of 2A orientations on the flange
  (rotation around the y-axis and the x-axis). on page 274
● First rotation around Z-axis, second rotation around twisted X-axis; see Fig.

  214 and ⮫ Table 56 Overview of 2A orientations on the flange (rotation
  around the y-axis and the z-axis) on page 274
● First rotation around Z-axis, second rotation around twisted Y-axis; see Fig.
  216 and ⮫ Table 58 Overview of 2A orientations on the flange (rotation
  around the z-axis and the y-axis) on page 274

                              Z              Rot1
                                  Y Rot2

                                  X

the zero position

the zero position

                                  Rot1

                              Z             Rot2
                                  Y

                                  X

the zero position

   the zero position

                                                 Rot1

                                  Z
                                      Y
                                                        Rot2
                                      X

   the zero position

                                                 Rot1

                                  Z       Rot2
                                      Y

                                      X

   the zero position

Parameterization
All six variants allow you to specif the offsets between the flange of the
base transformation and the first rotary axis, between the first rotary axis and
the second rotary axis, and between the second rotary axis and the flange
of the 2A orientation transformation by using parameters. All parameters are
optional.
                                          z1

                            x1                                 y1

                             x2
                                          z2

                                                               y2

                             x3                                y3
                                          z3

              Z                                                     Z
                  X                                                     Y

   Fig. 217 shows the schematic structure of an XY variant of the 2A orientation
   transformation. Here, x1, y1, and z1 describe the offset between the flange
   of the base transformation (in this case, delta kinematics) and the first rotary

axis (Rot1); x2, y2, and z2 describe the offset between the first rotary axis
(Rot1) and the second rotary axis (Rot2), and x3, y3, and z3 describe the
offset between the second rotary axis (Rot2) and the flange of the 2A orienta‐
tion transformation.
Parameters                                              Description
Robot flange → first rotary axis x1                     The X-offset from the flange of the basic
                                   transformation to the first rotary axis
               y1                  The Y-offset from the flange of the basic
                                   transformation to the first rotary axis
               z1                  The Z-offset from the flange of the basic
                                   transformation to the first rotary axis
first rotary axis → second rotary x2                    The X-offset of the first rotary axis to the

axis                                                    second rotary axis
             y2                    The Y-offset of the first rotary axis to the
                                   second rotary axis
               z2                  The Z-offset of the first rotary axis to the
                                   second rotary axis
second rotary axis → flange         x3                  The X-offset from the second rotary axis
                                   to the flange of the 2A orientation trans‐
                                   formation
               y3                  The Y-offset from the second rotary axis
                                   to the flange of the 2A orientation trans‐
                                   formation
               z3                  The Z-offset from the second rotary axis
                                   to the flange of the 2A orientation trans‐
                                   formation

                                 z1

                        x1                               y1

                         x2                              y2
                                 z2
                                 z3

           Z             x3                               y3     Z
                X                                                      Y

                                      z1
                              x1                            y1

                               x2                           y2

                                      z3 z2
                               x3                            y3

                Z                                                 Z
                    X                                                 Y

                                      z1                    y1
                              x1

                               x2
                                      z3 z2

                                                            y2
                               x3                            y3

                Z                                                 Z
                    X                                                 Y

   Fig. 219, Fig. 220 and Fig. 221 show the schematic layout and corresponding
   parameters of the five additional variants. The meaning of the parameters
   does not differ between the different variants.

### 6.3.6 Motion commands

Motion commands
A motion command issued for a kinematics causes the Tool Center Point
(TCP) to move in the space.
The TCP is a point of the kinematics that usually refers to the top of the
kinematics. The user sets the new TCP target position. The type of motion
command determines the path used to reach the new TCP position.
The new target position can be set in any coordinate system.
The coordinate system has no impact on the path used to reach the point.
   Refer to ⮫ Further information on page 176
   A motion command consists of the following:
   ● Endpoint and/or intermediate points: Points on the motion path
   ● Maximum values: Maximum values for the velocity profile, such as max‐
     imum velocity and maximum acceleration
   ● Motion type: The type of path on which the end points and the endpoint
     are/is to be reached
   ● Blending or buffer type: The type in which the block is to be started or
     blended

Command overview
The following motion commands for kinematics without orientation are sup‐
ported:
● Move Linear Absolute: ⮫ Chapter 7.3.4 KinMoveLinAbs - Absolute traversing
  of kinematics on page 524
● Move Linear Relative: ⮫ Chapter 7.3.5 KinMoveLinRel - Relative traversing
  of kinematics on page 528
● Move Direct Absolute: ⮫ Chapter 7.3.6 KinMoveDirectAbs - Direct absolute
  traversing of kinematics on page 532
● Move Direct Relative: ⮫ Chapter 7.3.7 KinMoveDirectRel - Direct relative
  traversing of kinematics on page 535
● Move Direct Async Absolute: ⮫ Chapter 7.3.8 KinMoveDirectAsyncAbs -

  Direct asynchronous absolute traversing of kinematics on page 538
● Move Direct Async Releative: ⮫ Chapter 7.3.9 KinMoveDirectAsyncRel -
  Direct asynchronous relative traversing of kinematics on page 543
● Jog Cont: ⮫ Chapter 7.3.13 KinJogCont - Continuous kinematic jogging
  on page 569
● Jog Incr: ⮫ Chapter 7.3.14 KinJogIncr - Incremental kinematic jogging
  on page 573

    Moving on a straight line - MoveLinear
Description
In the case of kinematic motion commands with extended programming
options, the target position is specified by a sequence of value pairs, each
consisting of a number for the position value and an "extended meaning",
consisting of a meaning that describes what the numerical value refers to
and an attribute with additional information that specifies how the numerical
value is to be interpreted:
(<position value>, (<meaning>, <attribute> ))
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

Meaning
The meaning indicates the axis or coordinate (position or orientation) to
which the specified numerical value refers.
The following meanings are supported:
X         X-coordinate
Y         Y-coordinate
Z         Z-coordinate
AX1       Axis 1 of the kinematics
AX2       Axis 2 of the kinematics
AX3       Axis 3 of the kinematics

...
AX16    Axis 16 of the kinematics
EUL1_ZY Euler angle 1 of the intrinsic orientation convention Z, Y', Z"
Z_I
EUL2_ZY Euler angle 2 of the intrinsic orientation convention Z, Y', Z"
Z_I
EUL3_ZY Euler angle 3 of the intrinsic orientation convention Z, Y', Z"
Z_I
EUL1_XY Euler angle 1 of the extrinsic orientation convention X, Y, Z
Z_E
EUL2_XY Euler angle 2 of the extrinsic orientation convention X, Y, Z
Z_E
EUL3_XY Euler angle 3 of the extrinsic orientation convention X, Y, Z
Z_E
EUL1_ZY Euler angle 1 of the intrinsic orientation convention Z, Y, X
X_E
EUL2_ZY Euler angle 2 of the intrinsic orientation convention Z, Y, X
X_E
EUL3_ZY Euler angle, 3 of the intrinsic orientation convention Z, Y, X
X_E
With regard to the orientation conventions, see also ⮫ Chapter 6.3.4 Orienta‐
tion interpolation on page 190

Attribute
The attribute specifies how the numerical value is to be interpreted. Currently,
there are only attributes for absolute and relative motion.
The attributes are also used when specifying geometry-specific parameters
(e.g. circle radius or circle center).
The following attributes are supported:
● UNDEF: Default attribute (positions are interpreted as absolute values)
● INCR_VALUE: The specified numerical value is interpreted incrementally
● ABS_VALUE: The specified numerical value is interpreted as absolute

Points management
In the ctrlX MOTION, Cartesian positions and orientations as well as axis
positions of a kinematics can be saved and managed as reusable points. The
following section explains the use cases for this, how points are defined and
how they are used by means of a Data Layer.

Use cases
There are various reasons why points that can be saved and are assigned
a name are useful in robot programming. On the one hand, they facilitate
moving a kinematic system manually to a specific position space and to save
this point. This process is often referred to as "teaching," and the stored
points are also called "teach points." Later, these points can be approached
again and again with precision. The teach function is therefore an important
aid when teaching a robot program.
On the other hand, the ctrlX MOTION facilitates saving of pecified positions
and to reuse them, which immensely facilitates programming.

Points definition
A point generally defines an absolute target of a kinematic motion. Points
belong to one kinematics and cannot be used by other kinematics. A point
consists of a name, a reference system, several tuples of meaning, value and
unit (e.g. X - 250 - mm for an x-position, EUL3_XYZ_E - 30 - deg for an Euler
angle or AX1 - 0 - deg for the value of an axis) and can contain a more
detailed description. The meaning of a point for the various reference systems
(currently ACS, MCS, CUSTOM and UNDEFINED) is explained below:
Axis coordinate system (ACS)
In the axis coordinate system (see ⮫ Chapter 6.3.1 Position and orientation in
space on page 176), the point defines a unique pose of a kinematic system.
The current tool is not taken into account, as only the axis values are saved
and the flange is therefore always approached in the same position. Following

a tool change, points would have to be taught in again to bring the tool tip
to the previous position. The point data contains the positions of the axes
involved. The advantage of this reference system is that you can easily save
the exact position of the robot and therefore also singular poses, for example.
Sample data for a SCARA when overwriting a point in the Data Layer look like
this:
{
    "name": "Home",
     "position": {
         "entries": [
             {"meaning": "AX1",
                  "value": 0,
                  "unit": "deg"},
             {"meaning": "AX2",
                  "value": 0,
                  "unit": "deg"},
             {"meaning": "AX3",
                 "value": 0,
                 "unit": "deg"},
             {"meaning": "AX4",
                 "value": 200,
                 "unit": "mm"}
         ]
     },
     "referenceSystem": "ACS",
     "description": "This is the home position.",
     "uiData": ""
}
Machine coordinate system (MCS)
A point in the MCS (see ⮫ Chapter 6.3.1 Position and orientation in space
on page 176) describes the position and orientation of the flange relative to
the coordinate origin of the kinematic base. The tool is not taken into account
here. Following a tool change, points would have to be taught again in order
to bring the tool tip to the previous position. The pose of the kinematics is
not unique, as the robot can reach a point through different joint positions. If
the respective position of the robot is important, the point has to be specified
in the ACS.
Sample data for a SCARA when overwriting a point in the Data Layer look like
this:
{
    "name": "Test",
     "position": {

         "entries": [
             {"meaning": "X",
                 "value": 300,
                 "unit": "mm"},
             {"meaning": "Y",
                 "value": -300,
                 "unit": "mm"},
             {"meaning": "Z",
                 "value": 180,
                 "unit": "mm"},
             {“meaning": "EUL3_XYZ_E",
                 "value": 0,
                 "unit": "deg"}
         ]
    },
    "referenceSystem": "MCS",
    "description": " This is a test point.",
    "uiData": ""
}
CUSTOM reference system
The custom version provides the option of saving Cartesian coordinates or
axis data, which are required in an application apart from motion commands.
An example could be a geometric offset between two objects that are used for
the calculation. However, it is not possible to teach the position of the robot
in this reference system or to use such a point directly in a motion command.
UNDEFINED
This reference system is set when a new point is created and shows that
the data is not specified. These points can therefore not be used in motion
commands.

Use via Data Layer
Points can be created, updated and deleted using the Data Layer. They can be
found under a kinematics under the path:
motion/kin/<kin_name>/cfg/points
Points can be assigned a name using "create" (e.g. "Test") and are then
displayed as a new node under the path specified above (e.g. motion/kin/
[name]/cfg/points/Test). This point node can be used to update the point
data or delete the point.
URL                       Command                   Result
motion/kin/               create                    Creating a new point
<kin_name>/cfg/points                               (with a predefined name)
                          read                      Reading the data of all
                                                    points
                          write                     String array that contains
                                                    the names of all points
motion/kin/               read                      Reading the data of a
<kin_name>/cfg/points/                              point
<point_name>              write                     Overwriting the data of a
                                                    point
                          delete                    Deleting a point
Point management is linked to the life cycle of the kinematics, i.e. when a
kinematic is deleted, the associated points are also automatically deleted and
when a kinematic is saved or loaded, the associated JSON file of the points is
automatically saved or loaded.

Command overview
Points can be approached linearly or directly without a defined path using the
two new commands KinMoveToPointLinCmd and KinMoveToPointDirectCmd.
The following motion commands for point tables are supported:
● Move Linear To Point: ⮫ Chapter 7.4.7 KinMoveToPointLin - Moving the
  kinematics linearly to a saved point on page 634
● Move Direct To Point: ⮫ Chapter 7.4.8 KinMoveToPointDirect - Moving the
  kinematics directly to a saved point on page 637

### 6.3.7 Belt-synchronous motion

    General information

"opt-belt-sync” command option
The “belt-synchronous" command option enables a kinematic motion that
is synchronous to an assembly or conveyor belt in terms of position and
orientation. The belt can be moved forwards or backwards as required,
change its velocity or stop. Depending on the configuration, the belt needs
to have a straight line and can be positioned anywhere in the room. The
command option supports several belts between which you can dynamically
resynchronize.
There are two scenarios for detecting objects on the transport belt:
1.    Static positioning: The objects are located at predefined positions on a
      stationary belt.
2.    Dynamic data recording: The objects are dynamically detected by a
      sensor (e.g., a photoelectric sensor or camera) as they move along a
      conveyor belt.
In both cases, the current belt value must be read exactly at the time the
position is recorded. The belt value passed with the "beltSync" command
option serves as a fixed reference point for all subsequent motion commands.
You can think of it as a kind of timestamp that "freezes" the exact moment an
object's position is detected on the conveyor belt.
A motion command sent to the machine is therefore always interpreted in
relation to that original detection time. Specifically, the command "Move to
point P" means: The kinematic system moves to the object's current position
(P') on the transport belt. This target position P' is calculated dynamically
based on the originally detected position (P) and the corresponding belt value
used as a reference. This ensures that the machine follows the object, even if
the object has already moved to a new location due to the belt's movement.
Even if several different motion commands are sent to the machine after the
initial position detection, all of these commands—without exception—refer to
the single belt value that was initially provided. This ensures that all actions
are consistently aligned with the object's original position, regardless of how
the belt has moved in the meantime.

Belt value
The progress of the belt is described by the belt value. The belt value does
not reflect the physical value of the belt axis (belt axis value), but is a refer‐
ence value that moves along with the belt. The easiest way to interpret it is
as a time stamp: At a specified belt value, a part is located at a specific point
on the belt. The belt value read at the time of recording therefore indicates
where the part was at that moment—regardless of how far the belt has moved
in the meantime.
Belt target value, current belt value, and reference belt value

● Belt axis value: Actual position of the belt axis in the unit of the axis.
● Current belt value: the belt axis value scaled by the conversion factor "belt‐
   ValConversionFactor." The value is maintained modulo 10000.
● Reference belt value: the belt value passed via the "opt-belt-sync" com‐
   mand option. It "freezes" the point in time when the position is recorded
   and serves as the reference for all subsequent motion commands.
Value range and unit
● Scope of validity: 0 ≤ belt value < 10000. After reaching the maximum value
   of 10,000, the belt value resets to 0 (modulo 10,000).
● Negative belt values are rejected with a minor error.
● Although the belt value has a unit of length (the "nominatorUnitOfBeltCon‐
   versionFactor" parameter of the belt axis, e.g., mm), it does not represent a
   position in space. Only the difference between two belt values returns the
   distance traveled by the belt.
Belt feed since position detection
The belt distance traveled since the position was recorded is calculated as
the difference between the current belt value and the reference belt value.
Based on this path, the system calculates when the recorded part reaches the
starting plane and by how much the kinematics of the belt motion is to be
adjusted.
The difference is always calculated as the shortest distance within the modulo
range. The belt path that occurs between position detection and desynchroni‐
zation must therefore be less than half the modulo range (5000). The "belt‐
ValConversionFactor" conversion factor has to be used to ensure that this
condition is met during the process.

Coordinate systems
When the "beltSync" command option is enabled, specific coordinate systems
are used for motion planning. Before activation, any active PCS has to be
deactivated; otherwise, the command option is rejected with a minor error
("Command option PCS already active").
Four coordinate systems are relevant for belt-synchronous motion:
● MCS (Machine coordinate system): Basic kinematic system. All other sys‐
   tems are ultimately converted to the MCS.
● PCS_belt: the configured belt system. It describes the position and orienta‐
   tion of the belt; it is specified in the robot's MCS and configured under
   "motion/cfg/coord-systems/belt-cs/sets/[name]". The X-axis points in the
   travel direction of the belt.
● PCS (Product Coordinate System): The system activated by the command
   option, in which belt-synchronous motions are controlled. It is created from
   the PCS_belt by an additional offet of "distToStartPlane" in its X-direction.
   The origin of the PCS is thus located exactly on the starting plane; its
   orientation corresponds to that of the PCS_belt.
● CCS (Sensor or Camera Coordinate System): Describes the position and
   orientation of the sensing sensor. It is configured under "motion/cfg/coord-
   systems/ccs/sets/[name]" and specified in the WCS.
The configuration determines which systems are activated: The PCS_belt is
defined by the "beltCoordSysNameDefault" parameter of the belt axis, and
the camera coordinate system is defined by the "cameraCoordSysNameDe‐
fault" parameter of the belt-specific kinematic configuration.

Product Coordinate System (PCS)
A visual representation of the coordinate systems described can be found at
Fig. 222 below.

If, while the transport belt is stationary, a point with an X-value of 0 is
approached in the active PCS, the machine moves precisely to the defined
starting plane.
In the PCS, the following applies:
● X = 0 corresponds to the starting plane.
● Positive X-values lie behind the starting plane in the direction of belt
   travel, that is, within the synchronization range.
● Negative X-values indicate a position in front of the starting plane; the part
   has not yet reached the starting plane.
Motion commands can be issued in either the MCS/WCS, the PCS, or the
CCS. It is possible to switch between these systems within a process; this
does not affect the belt feed.

Sensor and camera coordinate system (CCS)
In addition to the PCS, activating beltSync also activates the sensor or camera
coordinate system (CCS) configured for the belt. This is particularly relevant
for the dynamic detection of objects: The coordinates provided by the sensor
can be used directly in the CCS without first having to convert them to the
machine or product coordinate system. The camera coordinate system speci‐
fied under "cameraCoordSysNameDefault" has to be configured; otherwise,
the command option is rejected with a minor error.
Operation involving multiple robots
It is possible to operate multiple robots on the same transport belt. In
such a setup, all robots can operate using the same sensor or camera coor‐
dinate system (CCS) to ensure consistent object detection. However, since
"PCS_belt" is based directly on the machine coordinate system (MCS) of the
individual robot, a separate, individual PCS_belt has to be configured for each
robot.

Lengths and levels on the belt
The three lengths—"distToStartPlane," "syncLength," and "distToEnd‐
Plane"—describe the range within which the kinematics follow the belt. They
are all interpreted as paths along the belt's direction of travel (the X-direction
of the PCS_belt or the PCS). The following figure shows the orientation of the
planes and the significance of the three lengths.

● distToStartPlane: Distance between the starting plane and the origin of
  PCS_belt. It determines the location of the PCS origin (X = 0).
● syncLength: The distance from the starting plane within which synchro‐
  nization has to be completed. If the syncLength is exceeded during
  synchronization (states SYNCHRONIZING, RESYNC_FROM_DECOUPLING,
  RESYNC_FROM_DECOUPLED) before full synchronization is achieved, an
  error reaction is triggered.
● distToEndPlane: Distance from the starting plane to the end plane. If
  the component reaches the end plane while in the SYNCHRONIZED state
  without having been desynchronized first, an error reaction is triggered.
Both "syncLength" and "distToEndPlane" are measured from the starting
plane, i.e., relative to the X-coordinate in the PCS. The following has to apply:
distToEndPlane ≥ syncLength. Otherwise, the configuration is rejected with an
error.
In addition, it is monitored that the starting level is reached from the correct
direction. If the part approaches the starting plane from the negative X-direc‐
tion (opposite the direction of the belt), it is rejected as an error.

State machine

States
The "opt-belt-sync" command option does not, by itself, trigger a state change.
A state change always takes effect only after the next motion command is
issued.
The currently active state is reflected in the Data Layer (see ⮫ Chapter Status
display on page 299).
DESYNCHRONIZED
Initial status. No belt synchronization is active. If belt-synchronous mode was
active, the desynchronization was completed.
WAIT_FOR_START_PLANE_PASSED
The command for the "opt-belt-sync" command option is sent. The command
option does not take effect until the subsequent motion command is issued.
In the WAIT_FOR_START_PLANE_PASSED state, the kinematic system waits
until the part on the belt has reached the starting plane. Only when the part
crosses the starting plane is the kinematics activated and the synchronization
mechanisms initiated. The motion command remains active even though there
is no initial motion in the kinematics.
SYNCHRONIZING
Once the part detected by the belt value has passed the starting plane on
the belt, the kinematic system starts moving toward its target position. The
synchronization starts on the belt axis as superimposed. When the kinematics
has synchronized with the belt axis, the status changes to SYNCHRONIZED.
The command remains active, the kinematics is running.
SYNCHRONIZED

The kinematics is synchronized to the belt axis and follows the belt axis. The
command remains active until the next command is completely prepared. The
status is retained for all further motion commands until the command option
is switched off or toggled. If no further motion command follows in this state,
the last command remains active.
DECOUPLING
After resending the "Belt-Synchronous" command option with a new belt value
and/or a new belt, the kinematics are decoupled from the belt axis upon the
next motion command. The kinematics remain in this state until the system
comes to a stop or until the belt axis passes the starting plane of the com‐
mand option. The status changes to DECOUPLED or RESYNC_FROM_DECOU‐
PLING. The command remains active.
DECOUPLED

The kinematics are completely decoupled from the belt motion and wait until
the new part passes the starting plane of the new belt. The command remains
active, the kinematics is not running.
RESYNC_FROM_DECOUPLING
The state becomes active when the kinematics are not yet fully desynchron‐
ized from the current belt and begins to synchronize with the new belt.
Once the kinematics has completed synchronization, the state changes to
SYNCHRONIZED.
RESYNC_FROM_DECOUPLED
The kinematics is desynchronized from the previous belt and synchronizes
with the new belt. Once the kinematics has completed synchronization, the
state changes to SYNCHRONIZED.
DESYNCHRONIZING
This state occurs after the belt-synchronous command option is disabled and
the subsequent motion command is issued. Desynchronization starts, and the
system moves to the target position specified by the motion command.
If a minor error occurs during belt-synchronous motion, the regular state tran‐
sitions are paused: The state that was active at the time of the error remains
in effect for the duration of the entire error reaction. Only after they are
completed does the status change to DESYNCHRONIZED.

Commanding
Belt synchronization is enabled via the command option ⮫ Chapter 7.5.14
KinBeltSyncP - Belt-synchronous on page 692.
When the command option is switched on, synchronization to the belt axis
is started with the following motion command. The states of the function
are switched from WAIT_FOR_START_PLANE_PASSED via SYNCHRONIZING to
SYNCHRONIZED. The SYNCHRONIZED state is retained for each subsequent
motion command.
Switching the command option to a different belt value within the belt or to
a different belt initiates synchronization to the new belt value. The states are
switched from DECOUPLING via RESYNC_FROM_DECOUPLING to SYNCHRON‐
IZED or from DECOUPLING via DECOUPLED via RESYNC_FROM_DECOUPLED
to SYNCHRONIZED . The SYNCHRONIZED state is retained for each subse‐
quent motion command.
Disabling the command option also requires a subsequent motion command
to initiate desynchronization from the belt axis. The states are switched
from DESYNCHRONIZING to DESYNCHRONIZED. For all following motion com‐
mands, the "Belt Sync" command option is switched off.

Error reaction
An individually configurable error reaction can be executed for a minor error in
the kinematics (see Configuration of the error reaction). Three different error
reaction modes can be selected. All modes are executed immediately after a
minor error occurs.
You can specify your own dynamic limits for the return motion in the config‐
uration (see ⮫ Error reaction on page 297). The limits should be selected
by the user so that the axis limits can be complied with if the kinematics
performs a return motion in addition to their actual programmed motion.
DESYNC_ONLY
The kinematics synchronize themselves from the belt and thus achieve a
standstill.
RETRACT_AND_DESYNC_SIMULTANEOUSLY
The kinematics simultaneously performs a return motion and a desynchroniza‐
tion from the belt. The return motion can be defined in the configuration. A
coordinate can be selected which is to move in a defined direction to a speci‐
fied target position. At the same time, the kinematics are desynchronized from
the belt. This mode can only be used if the kinematics are in the SYNCHRON‐
IZED state.
RETRACT_FIRST_AND_THEN_DESYNC
A return motion is performed first. A coordinate can be selected which is to
move in a defined direction to a specified target position. Meanwhile, the
kinematics remains synchronized with the belt. Once the return motion has
been completed, the belt is desynchronized. This mode can only be used if
the kinematics are in the SYNCHRONIZED state.

Typical workflows and use cases
Basic pattern
All sequences follow the same basic pattern: first issue the "opt-belt-sync"
command option, followed by one or more motion commands. The command
option alone does not change the state—it takes effect only with the subse‐
quent motion command.
● The command option is permanent: "PermOn" turns on or switches to belt-
  synchronous motion; "PermOff" turns it off. Any other values for "perm‐
  Type" are rejected.
● Any number of motion commands can be issued between two command
  options. They all refer to the same reference belt value.
● Before turning on the power, any active PCS has to be turned off.
● When turning the system on, reconfiguring it, or turning it off, Polytrans has
  to be shut down if the PCS_belt is rotated relative to the MCS.
● As long as the kinematics are synchronized with the belt, the most recent
  motion command remains active. A motion command is not reported
  as complete until the corresponding compensation motions for the belt
  tracking have been fully established or eliminated.

Use case 1: Synchronizing, multiple motions, desynchronizing
The standard procedure: A part is captured; the kinematics synchronize, per‐
form one or more motions in sync with the belt, and then desynchronize
again.
Command                                                 Status after completion
1. Command option "opt-belt-sync": permType             DESYNCHRONIZED (unchanged)
"PermOn", beltName, beltValue = belt value at the
time of recording

Command                                               Status after completion
2. Move the motion command to the identified part     WAIT_FOR_START_PLANE_PASSED, followed
position (e.g., in CCS)                               by SYNCHRONIZING
3. Issue the next motion command as soon as           SYNCHRONIZED
synchronized state is reaached
4. Any number of additional motion commands, all      SYNCHRONIZED
belt-synchronously
5. Command option "opt-belt-sync": permType           SYNCHRONIZED (unchanged)
"PermOff"
6. Next motion command (desynchronization)            DESYNCHRONIZING, then DESYNCHRON‐
                                 IZED
All positions in steps 2 to 4 refer to the reference belt value passed in step 1,

regardless of how far the belt has advanced in the meantime.

Use case 2: Pick-and-Place cycle with resynchronization
Typical cyclic process: Synchronizing, adjusting ("sync down"), gripping, lifting
("sync up"), resynchronizing to the next part, and so on. The kinematics
between the individual parts are not desynchronized, but rather resynchron‐
ized directly.
1.    Set the "PermOn" command option to the belt value of Part 1.
2.    Motion command for the part ("sync on"). State sequence:
      WAIT_FOR_START_PLANE_PASSED, SYNCHRONIZING, SYNCHRONIZED.
3.    Sync down and gripping The state remains SYNCHRONIZED.
4.    Sync up The state remains SYNCHRONIZED.
5.    Set the "PermOn" command option again, this time using the belt value
      from Part 2 (resynchronizing). The state remains SYNCHRONIZED for the
      time being.
6.    Next motion command. State sequence: DECOUPLING, then—depending
      on the timing—either RESYNC_FROM_DECOUPLING or DECOUPLED and
      RESYNC_FROM_DECOUPLED, and finally SYNCHRONIZED.
7.    Repeat steps 3 to 6 for each additional part.
8.    To exit, enter the "PermOff" command option and issue another motion
      command. State sequence: DESYNCHRONIZING, DESYNCHRONIZED.
If the approach and lift-off motions are executed using MoveJump or Move‐
HalfJump, the control system internally breaks the motion down into seg‐
ments (lift-off, traverse, placement). Turning belt synchronization on, off, or
switching it between states is spread across several of these segments; the
remaining segments remain in belt synchronization. Switching within a Move‐
Jump is therefore permitted (see ⮫ Chapter Belt synchronization for Move‐
Jump and MoveHalfJump on page 293).

Use case 3: Resynchronization—the two variants
If the command option is set to "PermOn" again while the kinematics are
already synchronized, it first decouples from the previous reference point
(DECOUPLING) and then synchronizes to the new one. Depending on when
the new part reaches the starting plane, there are two options:

● The new component reaches the starting plane before the decoupling is
   completed: DECOUPLING, RESYNC_FROM_DECOUPLING, SYNCHRONIZED.
   The deactivation of the old belt tracking and the activation of the new belt
   tracking overlap.
● Decoupling is completed before the new part reaches the starting plane:
   DECOUPLING, DECOUPLED, RESYNC_FROM_DECOUPLED, SYNCHRON‐
   IZED. In the DECOUPLED state, the belt tracking is completely deactivated;
   the kinematic system is waiting for the new part.
Which variant is executed depends on the belt speed, the dynamic reserve
enabled via "dynLimFactor," and the distance of the new part from the starting
plane. Both variants result in the same final state and do not need to be han‐
dled differently by the application. The synchronization length "syncLength" is
monitored in both resynchronization states.

Use case 4: Resynchronizing to a different belt
The procedure is the same as in use case 3; additionally, a different belt name
is specified in the command option. Please note:
● Each belt must have its own belt axis with its individual PCS_belt, as well
  as its own entry in the kinematic configuration (starting plane, synchroniza‐
  tion length, end plane, dynamic factor, camera coordinate system).
● If the belts are aligned differently, the compensation motions of the old
  and new belts overlap depending on the direction. The axis limits must
  allow for this superposition; if necessary, "dynLimFactor" has to be reduced
● When desynchronizing later after a belt change, only absolute or only rela‐
  tive commands should be used (see ⮫ Chapter Restrictions on page 304)

Use case 5: Changes in belt motion
The belt may accelerate, decelerate, stop, or run in reverse at any time. The
kinematics follows the motion of the belt; the state machine is not affected by
this.
● If the belt is stationary, the kinematics remains at the last position where
  they were synchronized with the belt. The condition remains the same.
● If the belt accelerates or decelerates sharply, the dynamic reserve enabled
  via "dynLimFactor" has to be sufficient to keep up with the belt's motion.
  Otherwise, the synchronization limit may be exceeded.
● If the belt runs backward, the part may cross the starting plane in the
  direction opposite to the belt's direction of travel. This is monitored and
  acknowledged as an error.
● Jitter in the belt value encoder is not filtered out by the function and is
  transmitted to the kinematic motion. If necessary, a suitable filter should
  be installed upstream.

Use case 6: Error during belt operation
If a minor error occurs, the procedure depends on the system's state at the
time of the error and on the configured error reaction:
● SYNCHRONIZED with "DESYNC_ONLY": ERR_DESYNCHRONIZING, then
  ERR_DONE.
● SYNCHRONIZED with "RETRACT_FIRST_AND_THEN_DESYNC":
  ERR_RETRACT, then ERR_DESYNCHRONIZING, then ERR_DONE.
● SYNCHRONIZED with "RETRACT_AND_DESYNC_SIMULTANOUSLY":
  ERR_RETRACT_AND_DESYNC_SIM, then ERR_DONE.

  ● SYNCHRONIZING, RESYNC_FROM_DECOUPLING, or
     RESYNC_FROM_DECOUPLED: ERR_DESYNCHRONIZING, then ERR_DONE. A
     return motion is not performed in these states as the kinematics is not yet
     fully synchronized.
  ● All other states: ERR_NTD, then ERR_DONE. No compensation motion is
     required.
  Throughout the error reaction, the execution state remains at the value that
  was active when the error occurred. Only when ERR_DONE is returned, the
  execution status changes to DESYNCHRONIZED and the error state reverts to
  NO_ERROR.

    Belt synchronization for MoveJump and MoveHalfJump
The MoveJump and MoveHalfJump commands are internally subdivided by

the control into several subcommands: vertical and straight segments, respec‐
tively, and the roundings between them. If belt synchronization is enabled,
synchronization, desynchronization or resynchronization is not performed
within a single command, but is spread across several of these geometry seg‐
ments. This means that significantly more travel and more time are available
for the synchronization process than with a single motion command.
The jump geometry itself—heights, roundings, and boundaries defined by safe
zones—is described in the documentation for the "MoveJump" and "MoveHalf‐
Jump" commands. This section shows only the assignment of the synchroniza‐
tion process to the individual subsections.

  MoveJump
  A MoveJump is divided into five segments:
  ● vertical lift-off from the starting point to the starting height,
  ● Rounding from the vertical to the horizontal,
  ● straight section at maximum jump height,
  ● Rounding from the horizontal to the vertical,
  ● vertical approach to the target point from the target height.
  The synchronization process is always applied to sections 2 to 4, that is, to
  rounding- straight line - rounding:
  ● Remain synchronized with the belt: All five sections are executed belt-syn‐
    chronously.
  ● Synchronize: Section 1 is not yet belt-synchronized; sections 2 to 4 perform
    the synchronization, and section 5 is already transmitted completely belt-
    synchronously.
  ● Resynchronize: Section 1 still follows the previous belt; sections 2 to 4
    perform the resynchronization; section 5 already follows the new belt.
  ● Desynchronize: Section 1 is still belt-synchronous, sections 2 to 4 perform
    desynchronization; section 5 is no longer belt-related.

  MoveHalfJump
  A MoveHalfJump is broken down into three subsegments. The order depends
  on the variant:
  ● "Upward" variant: vertical lift-off — rounding — straight section to the target
     point.
  ● "Downward" variant: straight section from the starting point—rounding—ver‐
     tical placement.
  The synchronization process occurs on each of the two sections leading away
  from the vertical segment:

● "Upward" variant: The process takes place across sections 2 and 3.
    During desynchronization and resynchronization, the vertical lift (section
    1) remains belt-synchronous; during synchronization, it is not yet belt-refer‐
    enced.
● "Downward" variant: The process takes place across sections 1 and 2. The
    vertical placement (section 3) is already fully belt-synchronous during syn‐
    chronization and resynchronization, but is no longer belt-referenced during
    desynchronization.
If the kinematics is to remain belt-synchronous throughout the MoveHalfJump,
all three sections are performed belt-synchronously.

Boundary conditions
● The command's target coordinate system has to be aligned with the PCS;
  that is, the lift-off direction has to be parallel to the Z-axis of the PCS. Oth‐
  erwise, the command is rejected with the error message "target coordinate
  system not aligned with PCS."
● No blending is performed between the internally inserted subsections, nor
  is a Polytrans motion inserted; the jump contour is traversed exactly.
● Relative desynchronization is suppressed for MoveJump and MoveHalf‐
  Jump: Desynchronization occurs relative to the commanded target position
  and not relative to the moving belt.
● The monitoring of "syncLength" and "distToEndPlane" remains active. Since
  the process spans several stages, the available belt path has to be suffi‐
  ciently long.

Configuring the coordinate systems
Belts
The coordinates for belts are specified in the MCS of the robot. Several belts
can be defined.
Method: Create/Delete
URL: motion/cfg/coord-systems/belt-cs/sets/[name]
Content:
Data Layer path             Type                              Description
setName                     String                            Belt name
offsetXYZ                   [X: double, Y: double, Z:         Position of the belt in the room
     double]
orientation                 [α: double, β: double, γ:         Alignment of the belt in Euler angles
     double]
offsetAux                   [double, double, double,          Auxiliary axis offset
     double, double, double, double,
     double, double, double]
offsetXYZUnits              [X: String, Y: String, Z: String] Unit of the parameters in "offsetXYZ"
orientationUnits            [α: String, β: String, γ: String] Unit of the parameters in "orientation"
offsetAuxUnits              [String, String, String, String,  Units of the parameters in "offsetAux"
     String, String, String, String,
     String, String]
Example:
{
"setName": "name",
  "offsetXYZ": [0,0,0],
  "orientation": [0,0,0],
  "offsetAux": [0,0,0,0,0,0,0,0,0,0],

    "offsetXYZUnits": ["mm","mm","mm"],
    "orientationUnits": [ "deg", "deg", "deg"],
    "offsetAuxUnits": [ "mm", "mm", "mm", "mm", "mm", "mm",
    "mm", "mm", "mm", "mm" ]
}

Cameras
The coordinates for cameras are specified in the WCS. Several cameras can be
defined.
Method: Create/Remove
URL: motion/cfg/coord-systems/ccs/sets/[name]

Content:
Data Layer path              Type                              Description
setName                      String                            Name of the camera
offsetXYZ                    [X: double, Y: double, Z:         Position of the camera in the room
        double]
orientation                  [α: double, β: double, γ:         Aligning the camera in Euler angles
        double]
offsetAux                    [double, double, double,          Auxiliary axis offset
        double, double, double, double,
        double, double, double]
offsetXYZUnits               [X: String, Y: String, Z: String] Unit of the parameters in "offsetXYZ"
orientationUnits             [α: String, β: String, γ: String] Unit of the parameters in "orientation"
offsetAuxUnits               [String, String, String, String,  Units of the parameters in "offsetAux"
        String, String, String, String,
        String, String]
Example:
{
  "setName": "name",
  "offsetXYZ": [0,0,0],
  "orientation": [0,0,0],
  "offsetAux": [0,0,0,0,0,0,0,0,0,0],
  "offsetXYZUnits": ["mm","mm","mm"],
  "orientationUnits": [ "deg", "deg", "deg"],
  "offsetAuxUnits": [ "mm", "mm", "mm", "mm", "mm", "mm",
 "mm", "mm", "mm", "mm" ]
}

Axis configuration
Belt axes
To configure an axis as a belt axis, the function has to be enabled in the axis
configuration.
Method: Create/Delete
URL: motion/axs/[name]/cfg/functions/belt
Content:
Data Layer path              Type                             Description
isBeltAxis                   Boolean                          TRUE: Axis is a belt drive
                                         FALSE: Axis is not a belt drive
beltValConversionFactor double                                Conversion factor between belt and
                                         axis value

Data Layer path        Type                                Description
beltCoordSysNameDe‐ String                                 PCS_belt name
fault
nominatorUnitOfBelt‐   String                              Unit for the numerator of the conver‐
ConversionFactor                                           sion factor (always linear)
denominatorUnitOfBelt‐ String                              Unit for the denominator of the conver‐
ConversionFactor                                           sion factor. If not set, the standard unit
                                    of the axis is used. (rotatory/linear)
Example:
{
    "isBeltAxis": true,
    "beltValConversionFactor": 1,
    "beltCoordSysNameDefault": "BeltCs",
    "nominatorUnitOfBeltConversionFactor": "mm",
    "denominatorUnitOfBeltConversionFactor": "mm"
}

Kinematic configuration
Belts
Several belts can be created per kinematics.
Method: Create/Delete
URL: motion/kin/[name]/cfg/functions/belt-sync/belts/[belt name]
Content:
Data Layer path         Type                               Description
Name                    String                             Belt name
kinBeltSyncCfgData.dis‐ double                             Distance from the zero point of the
tToStartPlane                                              PCS_belt to the starting plane
kinBeltSyncCfgData.dis‐ double                             Distance from the start level to the end
tToEndPlane                                                level
kinBeltSyncCfgData.syn‐ double                             Distance from the start level to the level
cLength                                                    at which synchronization has to be com‐
                                    pleted
kinBeltSyncCfg‐            double                          A factor for scaling the dynamic limits
Data.dynLimFactor                                          of the desynchronization/resynchroniza‐
                                    tion compensation motions. For a
                                    detailed explanation, see below the
                                    table.
kinBeltSyncCfg‐         String                             Name of the camera coordinate system
Data.cameraCoordSys‐
NameDefault
kinBeltSyncCfgData.dis‐ String                             Unit of the "distToStartPlane" param‐
tToStartPlaneUnit                                          eter
kinBeltSyncCfgData.dis‐ String                             Unit of the "distToEndPlane" parameter
tToEndPlaneUnit
kinBeltSyncCfgData.syn‐ String                             Unit of the "syncLength" parameter
cLengthUnit
Effect of the dynamic factor (dynLimFactor)
This factor scales the dynamic limits of the compensation motions during
synchronization and desynchronization, based on the dynamic limits of the
kinematics. It affects velocity, acceleration, and jerk to varying degrees:

● Velocity = Kinematic velocity limit × dynLimFactor × 0.75
● Acceleration = Kinematic acceleration limit × dynLimFactor × 1.0
● Jerk = lower jerk limit (acceleration/deceleration) of the kinematics × dyn‐
   LimFactor × 2.0
A higher value results in faster compensating motions (shorter synchronization
travel, higher axis load), while a lower value results in smoother compensa‐
tion motions (longer synchronization travel, lower axis load).
The factor is limited to a maximum value of 1.0. When dynLimFactor = 1.0,
the compensation motions reach 75% of the velocity limit, 100% of the accel‐
eration limit, and 200% of the (lower) jerk limit of the kinematics.
Example:
{

        "name": "Bandname",
        "kinBeltSyncCfgData": {
            "distToStartPlane": 0,
            "distToEndPlane": 0,
            "syncLength": 0,
            "dynLimFactor": 0.1,
            "cameraCoordSysNameDefault": "",
            "distToStartPlaneUnit": "mm",
            "distToEndPlaneUnit": "mm",
            "syncLengthUnit": "mm"
        }
}

Error reaction
The error reaction can be configured for a minor error in the kinematics.
Method: Get/Put
URL: motion/kin/[name]/cfg/functions/belt-sync/error-reaction
Content:
Data Layer path              Type                          Description
errorReactionType            String                        Error reaction mode.
                                      The following error reactions can be
                                      configured:
                                      ● DESYNC_ONLY
                                      ● RETRACT_AND_DESYNC_SIMULTANE‐
                                         OUSLY
                                      ● RETRACT_FIRST_AND_THEN_DESYNC
kinBeltRetractDirection‐ String                            Direction of the retract motion.
Type                                                       The following directions for the return
                                      motion can be configured:
                                      ● X_POSITIVE
                                      ● X_NEGATIVE
                                      ● Y_POSITIVE
                                      ● Y_NEGATIVE
                                      ● Z_POSITIVE
                                      ● Z_NEGATIVE
retractPlaneValue            double                        Absolute value for the retract plane
retractPlaneUnit             String                        Unit of the value for the retract plane in
                                      "retractPlaneValue"
retractMotionLimits.vel double                             Velocity limit value of the return motion

Data Layer path         Type                                Description
retractMotionLimits.acc double                              Acceleration limit value of the return
                                     motion
retractMotionLimits.dec double                              Braking acceleration limit value of the
                                     return motion
retractMotionLi‐             double                         Jerk limit value of the return motion
mits.jrkAcc
retractMotionLi‐             double                         Braking jerk limit value of the return
mits.jrkDec                                                 motion
retractMotionLi‐             String                         Unit of the value in "retractMotionLi‐
mits.velUnit                                                mits.vel"
retractMotionLi‐             String                         Unit of the value in "retractMotionLi‐
mits.accUnit                                                mits.acc"
retractMotionLi‐             String                         Unit of the value in "retractMotionLi‐
mits.decUnit                                                mits.dec"
retractMotionLi‐             String                         Unit of the value in "retractMotionLi‐
mits.jrkAccUnit                                             mits.jrkAcc"
retractMotionLi‐             String                         Unit of the value in "retractMotionLi‐
mits.jrkDecUnit                                             mits.jrkDec"

Boundary conditions and monitoring

Prerequisites
● Belt axis: The specified axis object has to be configured as a belt axis
  (isBeltAxis = true). Otherwise, the request is rejected with the message
  "can't find axis object (belt) with name …"
● No active PCS: If the PCS command option is active, beltSync is rejected
  with the message "Command option PCS already active."

Configuration rule
The following has to apply: distToEndPlane ≥ syncLength. Otherwise, the con‐
figuration is rejected with a minor error: "The distance to the end plane is less
than the synchronization length."

On-site monitoring
● syncLength exceeded (states SYNCHRONIZING, RESYNC_FROM_DECOU‐
  PLING, RESYNC_FROM_DECOUPLED): minor error with the diagnostic mes‐
  sage "Maximum length for synchronizing exceeded".
● distToEndPlane exceeded (SYNCHRONIZED state): minor error with the
  diagnostic message "Maximum area for synchronized movement exceeded".
● Belt jitter (states SYNCHRONIZING, RESYNC_FROM_DECOUPLING,
  RESYNC_FROM_DECOUPLED): Trace warning when the belt speed changes
  abruptly; see ⮫ Chapter Belt jitter and belt jumps on page 298

Belt jitter and belt jumps
The belt-synchronous motion follows the belt value unfiltered: Any change
in the belt value is immediately converted into a target position in the kine‐
matic system. In this case, the belt synchronization system cannot distinguish
whether the belt has actually moved or whether the jump is merely simulated
by an inaccurate, noisy, or malfunctioning encoder—it blindly follows every
jump.

A jump in the belt value therefore causes a corresponding jump in the target
position of the kinematics. The axes cannot follow such a jump: The Motion
control system detects a position gap in the affected axes, and their drives
report a lag error. There is no limiting, filtering, or smoothing that can com‐
pensate for this.
Accurate, stable, and noise-free recording of the belt value is therefore a pre‐
requisite for belt operation. Common sources of interference include:
●  mechanically poorly coupled or slip-prone encoders,
●  an encoder resolution that is too low relative to the belt velocity,
●  Transmission errors or missed cycles in the belt axis connection,
●  jerky motions of the belt itself, such as when starting up or when cargo
   becomes jammed.

Monitoring
For diagnostic purposes, the belt synchronization system compares the cur‐
rent belt velocity with that of the previous cycle in each cycle. If it deviates
by more than 5% and the deviation cannot be explained by the reported
belt acceleration, a trace warning is issued ("Large deviation in belt velocity
detected ... Possible velocity jitter!").
● Monitoring is active only in the SYNCHRONIZING, RESYNC_FROM_DECOU‐
    PLING, and RESYNC_FROM_DECOUPLED states.
● It only takes effect if both the current and the previous belt velocity are
    unequal to zero; a stationary or starting belt is not monitored.
● This is purely a diagnostic output in the trace of the belt-synchronous
    motion: No error is triggered, the motion is not affected, and the jump is
    not corrected.
If sporadic lag errors or position gaps occur during belt operation, this trace
warning should be evaluated first: It points to insufficient quality in the
recording of belt values.

Value range of belt value
● Scope of validity: 0 ≤ belt value < 10000 (modulo 10000).
● Negative belt values are rejected with a minor error.

    Status display
The states of the “belt-synchronous" command option are displayed in the
Data Layer.
Method: Get
URL: motion/kin/[name]/state/functions/belt-sync/sync-state
Type: String
Status values during operation:
● DESYNCHRONIZED – Initial state; no belt synchronization is active.
● WAIT_FOR_START_PLANE_PASSED – Belt synchronization is active; waiting
  until the start plane is reached.
● SYNCHRONIZING – Starts the motion toward the target position after the
  start plane has been passed.
● SYNCHRONIZED – Synchronization complete; the kinematics follow the
  motion of the belt.
● DECOUPLING – New belt value commanded; belt tracking is terminated
  (starting level not yet reached).
● DECOUPLED – Completely decoupled from the belt (starting level not yet
  reached), no compensation motion active, waiting for resynchronization.
● RESYNC_FROM_DECOUPLING – Resynchronization during decoupling; com‐
  pensation for path and velocity is required.

● RESYNC_FROM_DECOUPLED – Resynchronization after decoupling; velocity
   desynchronization has already been completed.
● DESYNCHRONIZING – Belt synchronization is disabled; tracking of the belt
   is stopped.
Status values in the event of an error:
● NO_ERROR – Initial state; no error or termination.
● ERR_DESYNCHRONIZING – Pure error desynchronization: The belt speed at
  the time the error occurred is reduced.
● ERR_RETRACT – Return motion first, followed by a desynchronization error.
● ERR_RETRACT_AND_DESYNC_SIM – Simultaneous return motion and
  desynchronization error.
● ERR_DONE – Error reaction is complete.
● ERR_NTD – No additional error reaction is required, as the compensation
  functions already handle this.

The states are described in ⮫ Chapter State machine on page 288.

Example
Belt definition
1.   Create the "Conveyor" axis and configure the Data Layer node
     motion/axs/Conveyor/cfg/functions/belt with the following data:
     {
           "isBeltAxis": true,
           "beltValConversionFactor": 1,
           "beltCoordSysNameDefault": "coordSysBeltDefault",
           "nominatorUnitOfBeltConversionFactor": "mm",
           "denominatorUnitOfBeltConversionFactor": "mm"
     }
Definition of the PCS_belt and the camera coordinate system
2.   The coordinate systems for the belt and the camera can be stored on the
     following two Data Layer nodes:
     ● motion/cfg/coord-systems/belt-cs/sets/
     ● motion/cfg/coord-systems/ccs/sets/
     The data has to be defined as follows:
     {
         "setName": "Name",
         "offsetXYZ": [ 0, 0, 0 ],
         "orientation": [ 0, 0, 0 ],
         "offsetAux": [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
         "offsetXYZUnits": [ "mm", "mm", "mm" ],
         "orientationUnits": [ "deg", "deg", "deg" ],
         "offsetAuxUnits": [ "mm", "mm", "mm", "mm", "mm", "mm",
                             "mm", "mm", "mm", "mm" ]
     }

Configuring the kinematics for belt synchronization
3.      There are various configuration options for the kinematics under the
motion/kin/Robot/cfg/functions/belt-sync/belts node.
On the one hand to configure the parameters for the synchronization
between kinematics and belt and to configure the error routine.
Here is an excerpt of a possible payload:
{
    "belts": [
        {
             "name": "Conveyor",
             "kinBeltSyncCfgData": {
                 "distToStartPlane": 20,

                 "distToEndPlane": 100,
                 "syncLength": 50,
                 "dynLimFactor": 0.1,
                 "cameraCoordSysNameDefault":
                 "coordSysCameraDefault",
                 "distToStartPlaneUnit": "mm",
                 "distToEndPlaneUnit": "mm",
                 "syncLengthUnit": "mm"
             }
        }
    ],
    "errorCfg": {
        "errorReactionType": "RETRACT_
          FIRST_AND_THEN_DESYNC",
        "kinBeltRetractDirectionType": "Z_POSITIVE",
        "retractPlaneValue": 1,
        "retractPlaneValueUnit": "mm",
        "retractMotionLimits": {
             "vel": 6000,
             "acc": 2,
             "dec": 2,
             "jrkAcc": 0,
             "jrkDec": 0,
             "velUnit": "mm/min",
             "accUnit": "m/s^2",
             "decUnit": "m/s^2",
             "jrkAccUnit": "m/s^3",
             "jrkDecUnit": "m/s^3"
        }
    }
}

Starting the belt synchronization
4.   Subsequently, the belt and kinematics can be synchronized using the
"Belt Sync" command option.
To use the “Belt-synchronous traveling" command option automatically,
you can use the ML_AxsGetBeltValueRT function block (see ⮫ PLC:
on page 692) via the PLC to read the current belt value and synchronize
it with the next part on the belt.
For example, the command option can be enabled under the
motion/kin/Robot/cmd/opt-belt-sync node.
{
     "permType": "PermOn",
     "beltName": "Conveyor",
     "beltValue": 0
}
A sensor (camera or similar device) detects a part on a belt. The coordi‐
nates and the current belt axis value are determined and passed as belt
value parameters using "opt-belt-sync."
Belt-synchronous motion is set up by enabling the "Belt-synchronous"
command option. The belt value that was requested by the sensor
during position determination is passed. The kinematics are then set to
the determined position of the part. Configuring the camera coordinate
system and the PCS_belt allows the kinematics to be controlled based
on the part's position. Only when this motion command is executed do
the "Belt Synchronization" and "PCS" functions become active.
The commanded kinematic motion in the X-axis is internally limited to
the position of the starting plane. An internal check is performed to
determine whether the detected part on the belt has reached the active
starting level. If not, the kinematics wait until the part has reached the
starting plane.
Note: If a relative motion is commanded for desynchronization, the last
commanded position is used as the starting point. In this case, the posi‐
tion on the starting plane that is limited to X.
As soon as the detected part crosses the starting plane, synchronization
begins.
The states of the kinematics can be read under the motion/kin/Robot/
state/functions/belt-sync/sync-state node.
Once synchronization is complete, the process of picking up or removing
the part can begin, and once that is finished, the desynchronization
process with the belt can be initiated.
Resynchronization
5.   Resynchronization to a different belt or a different section on the same
belt can be initiated by resending the "opt-belt-sync" command option,
followed by a motion command.

Desynchronization
6.      The command option is disabled under the node motion/kin/
Robot/cmd/opt-belt-sync:
{
    "permType": "PermOff",
    "beltName": "Conveyor",
    "beltValue": 0
}
motion/kin/Kinematics/cmd/move-ex
Desynchronization starts with the next motion command. Desynchroniza‐
tion with respect to the belt occurs either absolutely or relatively:
Absolute desynchronization

● moveAbs
● kinCmdMoveEx with explicit absolute commanding of X
{"cmdKinPose":
   [{
         "value": 0,
         "extMeaning": {"meaning": "X","addAttributes":
                           "ABS_VALUE"}}],
         {
         "value": 0,
         "extMeaning": {"meaning": "Y","addAttributes":
                           "ABS_VALUE"}},
         {
         "value": 0,
         "extMeaning": {"meaning": "Z","addAttributes":
                            "INCR_VALUE"}},],
...}
Relative desynchronization
● kinCmdMoveRel
● kinCmdMoveEx with explicit control of X relative to
{"cmdKinPose":
   [{
         "value": 0,
         "extMeaning": {"meaning": "X","addAttributes":
                        "INCR_VALUE"}},
       {
         "value": 0,
         "extMeaning": {"meaning": "Y","addAttributes":
                        "ABS_VALUE"}},
       {
         "value": 0,
         "extMeaning": {"meaning": "Z","addAttributes":
                        "INCR_VALUE"}},],
...}
● kinCmdMoveEx without the "Meaning:X" command.
{"cmdKinPose":
   [{
         "value": 0,
         "extMeaning": {"meaning": "Y","addAttributes":
                        "ABS_VALUE"}},
       {
         "value": 0,

                "extMeaning": {"meaning": "Z","addAttributes":
                               "INCR_VALUE"}},],
      ...}
      The end position is determined by the current position relative to the
      belt, the relative offset resulting from velocity desynchronization with the
      belt, and the programmed value for the relative motion.

Restrictions
Mixed commanding for desynchronization (kinCmdMoveEx)
A mixed command containing both absolute (ABS_VALUE) and relative
(INCR_VALUE) values for desynchronization (kinCmdMoveEx) is not supported
if the product coordinate system (PCS) changes immediately after BeltSync is
disabled.
This is especially true when the PCS_belt is twisted or when a new PCS is
activated to desynchronize the system.
Cause: The logic for relative desynchronization takes into account only the
commanded X-coordinate. In a rotated coordinate system, this axis no longer
corresponds to the direction of motion of the transport belt, which leads to
unpredictable behavior.
Recommendation: If the coordinate system has changed, use only absolute or
only relative commands to resynchronize.
Polytrans
When Polytrans is active, the “belt-synchronous" command option must not
be turned on, off, or toggled if the belt being used is offset or rotated relative
to the MCS. To ensure proper programming, Polytrans first has to be turned
off. Subsequently, Belt Sync can be reconfigured using a command option,
and then Polytrans can be turned back on. The following motion command
activates the mechanisms of belt-synchronous and Polytrans.
Belt jitter (encoder axes)
The “belt-synchronous" function cannot filter out belt jitter. It is absolutely
necessary to connect a suitable filter in series with encoder axes; otherwise,
unintended behavior may occur during synchronization or resynchronization.
Limited tests during motion preparation
When belt synchronization is active, the actual position of the kinematic
system is not determined until during execution, since it depends on the
progress of the belt. All tests that require a belt already familiar from the
preparation phase are therefore disabled. In this case, the responsibility for
ensuring a valid path lies with the user.
 ● Determining the path limits from the axis limits: The path dynamics are
   no longer automatically reduced to the limit values derived from the axis
   limits. The commanded path limits must therefore be carefully checked and
   specified. If the path limits are set too high, this can lead to position gaps.
 ● Singularity detection: Singularities are neither detected nor handled. There‐
   fore, the path has to be programmed to maintain a sufficient distance from
   singularities. In particular, the use of belt synchronization is generally not
   recommended for 6-axis robots; if it cannot be avoided, only very short
   belt-synchronized motions should be performed.
 ● Verification of safe zones and kinematic limits: Both checks are omitted
   from the preparation. A violation is not detected in advance, but only at
   runtime.

    Belt-synchronous with blending
Blending in combination with belt synchronization is only possible during syn‐
chronization and desynchronization. When desynchronizing, all positions in
the command have to be programmed as absolute values.
Blending with Beltsync is possible in the following cases:
1.    In Command 1, BeltSync is inactive (beltsync state = desynchronized),
      and in the following Command 2, BeltSync is active (beltsync state =
      synchronizing).
2.    Command 1 is the command for desynchronization (beltsync state
      = desynchronizing). In Command 1, all target positions are absolute
      values. In command 2, BeltSync is disabled.
3.    Command 1 is the command for desynchronization (beltsync state

      = desynchronizing). In Command 1, all target positions are absolute
      values. BeltSync was reactivated for the following command 2 (beltsync
      state = synchronizing).
In combinations where blending is not possible, blending is suppressed inter‐
nally. It is not necessary to disable the blending command option.
The following diagram shows command transitions where BeltSync with
blending is possible.

    Frequently Asked Questions (FAQ)
This chapter summarizes the most frequently asked questions regarding com‐
missioning and operation. You can find detailed descriptions in the respective
chapters.

  Procedure and commanding
  I have disabled the command option, but the status has not changed. What is
  the reason?

The "opt-belt-sync" command option does not, by itself, trigger a state change.
It does not take effect until the next motion command—this applies equally
to switching on, switching and switching off. As long as no motion command
follows, the current state remains unchanged.
The kinematic system does not move after the belt synchronization is turned
on. Is that a mistake?
No. After the first motion command, the kinematics enter the
WAIT_FOR_START_PLANE_PASSED state and remains there until the detected
part has reached the starting plane. The motion command remains active.
Motion and synchronization do not begin until the starting plane is crossed. If
in doubt, check the status in the Data Layer, as well as the transmitted belt
value and belt motion.
Why is my motion command marked as incomplete?
A motion command is not considered complete until the corresponding com‐
pensation motions for belt tracking have been fully completed or removed.
Furthermore, as long as the kinematics are synchronized with the belt, the
most recently issued motion command remains active, since the kinematics
has to continue to follow the belt.
Do I need to desync between two parts?
No. The standard procedure is to resynchronize: The command option is reset
with "PermOn" and the belt value of the next section; the next motion com‐
mand executes the change. Desynchronization is only necessary if the kine‐
matic system is actually supposed to leave the belt reference, for example, at
the end of a cycle.
What happens if the belt stops or runs backwards?
The kinematics follows the belt motion in both directions. If the belt is
stopped, it remains at the position where it was last in sync with the belt;
the state is preserved. If the belt runs backward, the kinematics follow suit. If
the part crosses the starting plane in the direction opposite to the direction
of travel of the belt, this is detected and the part is rejected with a minor
error.
Should I desynchronize absolutely or relatively?
Both options are possible: With absolute control, the kinematics moves to
the commanded target position; with relative control, the end position is
determined by the current position above the belt, the offset resulting from
velocity desynchronization, and the programmed relative offset. Mixing abso‐
lute and relative values in a single command is not supported if the coor‐
dinate system changes when belt synchronization is disabled—for example,
when the PCS_belt is rotated or when a new PCS is activated directly. In this
case, use only absolute or only relative commands (see ⮫ Chapter Restrictions
on page 304).

Belt value
What is the difference between the belt average value, the current belt value,
and the reference belt value?
The belt axis value is the actual position of the belt axis in the axis's unit of
measurement. The current belt value is the value of the belt converted using
"beltValConversionFactor" and kept modulo 10,000. The reference belt value is
the belt value passed via the command option; it records the time at which
the position was detected. All subsequent motion commands are calculated
relative to this reference belt value.
Why is the belt value not 0, even though the belt axis is set to 0?

The belt value and the axis value are two different quantities and generally do
not match. The belt value 0 does not refer to the axis origin, but to the axis
position at the moment it was activated as belt axis; from that point on, the
belt value tracks the belt progress. In addition, it is scaled by "beltValConver‐
sionFactor" and is calculated exclusively modulo 10,000. A modulo of the axis
itself—for example, 360 degrees for a rotary axis—is not included in the belt
value; the belt value extends beyond the axis modulo. This does not affect
the belt synchronization, since only the difference between two belt values is
evaluated—never an absolute value.
What happens when the belt value overflows at 10,000?
The belt value resets to 0. The application does not need to handle overflow
separately, since differences are always calculated as the shortest distance
within the modulo range. The condition is that the belt path between position

detection and desynchronization has to remain less than half the modulo
range (5000). This has to be ensured using the conversion factor "beltValCon‐
versionFactor."

Coordinate systems
Where is X = 0—in PCS_belt or in PCS?
Commands are issued in PCS. Its origin lies on the starting plane, offset by
"distToStartPlane" in the belt's direction of travel relative to the origin of the
PCS_belt. The following applies in the PCS: X = 0 is the starting plane; posi‐
tive x-values lie behind it in the synchronization region, and negative x-values
lie in front of it. The PCS_belt simply describes the position and orientation of
the belt in the MCS and is not directly controlled.

Configuration
What value should I set for "dynLimFactor"?
The factor scales the dynamic limits of the compensation motions based on
the kinematic limits: Velocity by a factor of 0.75, acceleration by 1.0, and
jerk by 2.0, each multiplied additionally by "dynLimFactor." A higher value
shortens the synchronization path but places greater stress on the axes; a
lower value results in smoother but longer compensation motions. Start with
a small value and increase it until synchronization is reliably completed within
the "syncLength" and the axis limits are still maintained.
The configuration is rejected with the message "The distance to the end plane
is smaller than the synchronization length."
The following has to apply: distToEndPlane ≥ syncLength. Both lengths are
measured from the starting plane; therefore, the end plane must not lie ahead
of the plane at which synchronization must be completed.

Messages and error behavior
"Can't find axis object (belt) with the name ..."
The axis specified in the command option is not configured as belt axis.
Check the axis name and set "isBeltAxis" to true in the axis configuration.
"Command option PCS is already active"
Belt synchronization even activates a product coordinate system. A coordinate
system that has already been activated using the PCS command option must
therefore be deactivated first.
"Maximum synchronization time exceeded"

The synchronization or resynchronization had not yet been completed based
on the synchronization length "syncLength" starting from the starting plane.
Common causes include a "syncLength" that is too short, a "dynLimFactor"
that is too small, a belt velocity that is too high, or a distance between the
kinematic position and the part position that is too large to compensate for.
"Maximum area for synchronized movement exceeded"
While in the SYNCHRONIZED state, the component reached the end state
without having been desynchronized or resynchronized beforehand. Either the
process above the belt has to be completed earlier, or "distToEndPlane" has
to be increased.
What happens if a minor error occurs during belt-synchronous motion?
The configured error reaction is executed immediately. The sequence state
remains at the value that was active when the error occurred, while the
error state progresses through the reactions (for example, ERR_RETRACT,
ERR_DESYNCHRONIZING, ERR_DONE). Only when ERR_DONE is returned, the
execution status changes to DESYNCHRONIZED and the error state reverts
to NO_ERROR. A return motion is performed only from the SYNCHRONIZED
state; during synchronization or resynchronization, the system is exclusively
desynchronized.

Position jumps and belt jitter
During belt mode, position gaps or lag errors occur sporadically. What is the
reason?
Belt synchronization tracks the belt value unfiltered and cannot distinguish
whether the belt has actually moved or whether a jump is merely simulated
by an inaccurate or malfunctioning encoder. Every jump in the belt value is
immediately translated into a jump in the target position, which the axes
cannot follow. There is no filtering, limiting, or smoothing that can compen‐
sate for this—the belt value measurement has to be free of jumps and noise
(see ⮫ Chapter Belt jitter and belt jumps on page 298).
How can I detect belt width jitter?
Belt synchronization compares the current belt velocity with the previous belt
velocity in each cycle. If it deviates by more than 5 percent and this cannot
be explained by the reported belt acceleration, the warning "Possible velocity
jitter!" is output. Monitoring is active only during synchronization and only
when the belt is running. It does not trigger any errors or correct anything;
rather, it is purely a diagnostic tool.
The belt value detection is accurate, but position gaps still occur. What could
be the cause?
When belt synchronization is active, the actual path is not determined until
processing is started. For this reason, among other things, the automatic
reduction of motion dynamics to the limit values derived from the axis limits
is no longer applied. If the path limits are set too high, they cannot be com‐
pensated anymore and may result in position jumps. Check the commanded
belt limits and reduce them if necessary. Singularity detection, as well as
the checking of safe zones and kinematic limits during preparation, are also
disabled (see ⮫ Chapter Restrictions on page 304).

### 6.3.8 Working areas and safe zones

Basics
This function permanently switches on the monitoring of an individual safe
zone or a permitted working area for all motion commands until it is explicitly
switched off. You can use this function to prevent machine damage caused by
inadvertent commands in blocked areas.

Several safe zones or work zones can be enabled using several calls of this
function.
In contrast to the command option ⮫ Chapter 7.5.9 KinSafeAreaP - Working
areas/safe zones on page 672, ⮫ Chapter 7.5.10 KinSafeAreaInExecutionP -
Working areas/safe zones on page 674 monitors the active motion and not the
commanded kinematic motion. If a safe zone is violated or the working areas
are left, an error reaction is triggered. With this function, you can prevent
machine damage as the kinematics is stopped if blocked areas are violated.
If a commanded motion (see ⮫ Chapter 7.5.9 KinSafeAreaP - Working areas/
safe zones on page 672) or the actual motion (see ⮫ Chapter 7.5.10 KinSa‐
feAreaInExecutionP - Working areas/safe zones on page 674) violates a safe
zone, leaves an exclusive working area or is not completely covered by all
active inclusive working areas then:

● an error is generated (the kinematic is switched to error state)
● if the execution of commands in this kinematics is stopped
● if a diagnostic message describing the error is reported
The configuration of the error reaction (see ⮫ Chapter Error detection and
error reaction on page 317) determines the behavior in the event of an error.
Please note that with the command option ⮫ Chapter 7.5.9 KinSafeAreaP -
Working areas/safe zones on page 672, the working areas and safe zones
are monitored when preparing the commands. If an error is detected and
if the kinematic stops, this refers to the currently prepared command and
not to the currently executed command. The preparation is typically several
commands ahead of the execution. Additionally, errors during monitoring can
occur ("violation detected even though there is no violation" as well as "no
violation detected even though violation occurred"), if the calculated path is
modified or if the path is not defined (as e.g. is the case for a MoveDirec‐
tAsync command, see ⮫ Chapter 7.3.8 KinMoveDirectAsyncAbs - Direct asyn‐
chronous absolute traversing of kinematics on page 538 and ⮫ Chapter 7.3.9
KinMoveDirectAsyncRel - Direct asynchronous relative traversing of kinematics
on page 543) as the check takes place during the preparation of the com‐
mand.

Functional description
Several working areas and safe zones can be configured for ctrlX MOTION.
This is realized in a central configuration so that the zones can be used for
all kinematics. Each zone is defined by a geometric object (currently, an axis-
parallel n-dimensional cuboid) and a coordinate system. If the monitoring is
active, all following motion commands are checked for active safe zones and
work zones.
●   A motion must never enter an active safe zone
●   A motion must never exit an active exclusive working area
●   Each of these violations generates an error in the kinematics
●   The limits of the working areas and safe zones are always allowed

Example

Example 1 - Violation of a safe zone:
Main diagnostics: Error in command option safe zone (safe zones and work
zones).
Detailed diagnostics: The commanded motion violates a safe zone.
Additional information: Safe zone: Safe zone1.
Notes:
● The detailed diagnostics shows that a safe zone has been violated
● In this additional information, it is specified which safe zone has been
  violated
● The error message always reports the first found violation

Example 2 - Exiting the intersection of all active exclusive work zones:
Main diagnostics: Error in command option safe zone (safe zones and work
zones).
Detailed diagnostics: Commanded motion left one of the exclusive.
Work areas additional information: excl. working area: Robot1.

Notes:
● The detailed diagnostics provides information that an exclusive working
  area has been exited
● In this additional information, it is specified which working are has been
  exited
● The error message always reports the first found violation

Example 3 - Exiting the sum of all active inclusive work zones:
Main diagnostics: Error in command option safe zone (safe zones and work
zones).
Detailed diagnostics: A part of the commanded motion is not covered by any
active inclusive work areas.

Additional          information:       uncovered         path         part
(0.990000-1.000000): (700.000000mm;200.000000mm;900.000000mm) -
(700.000000mm;200.000000mm;901.000000mm).
Notes:
● The detailed diagnostics provides information that a part of the com‐
  manded motion is not covered by the sum of all active inclusive work zones
● In this additional information, it is specified which part of the motion is not
  covered
● The first two numbers in the additional information (0.99 and 1.0) specify
  which part of the motion (related to the programmed path) is not covered.
  In this example, the last percent of the motion is outside of all inclusive
  work zones
● At the end of the additional information, the prohibited part of the motion
  for the first three coordinates is additionally specified. In this example,
  the section from (700mm;200mm;900mm) to (700mm;200mm;901mm), i.e.
  1mm travel of the z-coordinate, was not covered by the active inclusive
  working areas
Notes:
● The detailed diagnostics shows that the current motion is not in any of the
  existing active inclusive work zones
● In this additional information, it is specified which part of the motion is not
  covered
● The first two numbers in the additional information (0.99 and 1.0) specify
  which part of the motion (related to the programmed path) is not covered.
  In this example, the last percent of the motion is outside of all inclusive
  work zones
● At the end of the additional information, the prohibited part of the motion
  for the first three coordinates is additionally specified. In this example,
  the section from (700mm;200mm;900mm) to (700mm;200mm;901mm), i.e.
  1mm travel of the z-coordinate, was not covered by the active inclusive
  working areas

Additional information:
Being in a safe zone (or out of working areas) when the zone is enabled
results in an error when the next motion is commanded. There is no function‐
ality to "move out" (as with jogging and the axis position limit). Disable the
safe zone before commanding a motion.
If no working area is active, the check for working areas is disabled. If at
least one working area is enabled, the check is active and you have to be in a
working area to command a motion.

The jog mode is stopped in front of the prohibited areas (similar to the axis
position limit). If the starting position of a kinematic jog command is within
a prohibited zone, a diagnostic message is generated and the motion is not
executed. Disable monitoring of the safe area in order to jog.

Configuring working areas and safe zones
The configuration of the working areas and safe zones can be read and written
via Data Layer. It is within the system configuration area so that the configured
working areas and safe zones can be used by all kinematics.
URL                        Command           Result
motion/cfg/safe-areas      browse            String array containing the names
                                             of all configured working areas
                                             and safe zones
motion/cfg/safe-areas      create            Creates a new working area and
                                             safe zone with the transferred
                                             name
motion/cfg/safe-areas      remove            Deletes a new working areas and
                                             safe zones with the transferred
                                             name
motion/cfg/safe-areas/     read/write        Reads/writes the working areas
<name>                                       and safe zones with the trans‐
                                             ferred name
The data of the working areas and safe zones can be changed at any time
(even during an active motion). Upon activation of monitoring, the data are
copied to an internal memory and are valid there. This means, if you want
to change a working areas and safe zones, first change the configuration and
subsequently enable this working area and safe zone using the command
option. A new activations results in applying the current configuration from
the Data Layer to the internal memory.
Deleting a working area and safe zone does not affect the active working area
or safe zone as they are checked by the internal memory.
An active working area and safe zone can only be deactivated by disabling the
command option.

Workspace for kinematics
This feature permanently enables monitoring of a single working area for a
kinematic configuration. It represents an expansion of the work areas and
safety zones.
The working range of a kinematic system cannot be disabled. If a commanded
motion or the actual motion leaves the working area, a diagnostic message is
displayed (see ⮫ Chapter 6.3.8 Working areas and safe zones on page 308).
It is also possible to jog back to the working area. The working area is moni‐
tored both during the preparation and execution of commands.
Configuration:
The working area configuration can be read and written via the Data Layer. It
is within the scope of kinematic configuration.
URL                    Command               Result
motion/kin/<name>/cfg/ read/write            Reads/writes the working area of
functions/safe-areas/                        a kinematic with the specified
basic-work-area                              name

Monitoring the working area
The name of the working area or safe zone that was last violated can be
queried via the Data Layer.
URL                         Command          Result
motion/kin/[name]/          read             Name of the last working area
state/functions/safe-                        and safe zone that was violated.
areas/last-violated-safe-
area
The information in the node is updated each time a new check is performed
(e.g., as part of a command). If the validation was successful (and no viola‐
tion was detected), the Data Layer node returns an empty string.
This information can be used to enable an application to monitor the relevant

working area or to deactivate the corresponding protection zone so that the
user can exit the restricted area (for example, by jogging).
If a violation of the inclusive working area is detected (the kinematic position
is outside all inclusive working areas), the Data Layer node always reports the
first working area with active monitoring.

Command overview
The following command option is required to activate the working areas:
● ⮫ Chapter 7.5.9 KinSafeAreaP - Working areas/safe zones on page 672
● ⮫ Chapter 7.5.10 KinSafeAreaInExecutionP - Working areas/safe zones
  on page 674
● ⮫ Chapter 7.7.10 KinSafeAreaInExecutionCheckEnabled - Enabling the
  working area monitoring on page 768
● ⮫ Chapter 7.7.11 KinSafeAreaInExecutionAddCheckSize - Online modifica‐
  tion of the working area size on page 770

### 6.3.9 Reduced motion velocity depending on the safe axis states

Basics
The safe drive operation mode can be used to limit the axis or web velocity of
associated Motion objects (axis and kinematics). The implemented modes are:
"Safe Limited Speed" and "Safe Hold". Thus, it is possible to react to changes
in the safe drive operation mode and realize a functional and safe motion.
In order for the safe drive operation mode to be transferred to the associated
motion axis object or the assigned kinematics, this functionality has to be
enabled in the axis configuration of the Motion. This has to be activated indi‐
vidually for each axis. The kinematics only react to the associated axes with
the activated functionality.
The functionality can only be enabled or disabled in configuration mode.
During operation, there is no response to activation and deactivation.
The safe axis velocities are generally not complied with for kinematic com‐
mands. Only the configurable safe kinematic velocity is ensured for the web
velocity resulting from the FeedGroup devices.
The active mode can be queried via the axis or kinematics status, e.g. via the
Data Layer. With deactivated functionality or in normal operation (without a
special safe drive operation mode), the normal mode (SOM_NORMAL_MODE)
is present.
The kinematics processes the safe drive operation modes of the associated
axes, provided the functionality is activated in the drive configuration, and
is the safe operation mode of the kinematics. The highest rank of the
modes always prevails: SOM_SAFE_HOLD > SOM_SAFE_LIMITED_SPEED >
SOM_NORMAL_MODE

If the safe operating mode of the axis changes, the reaction is immediate. This
also applies when switching to normal mode.
Mode                              Behavior
SOM_NORMAL_MODE                   Motion is limited by the dynamics of the
                                  motion or the maximum dynamics of the
                                  axis/kinematic configuration
SOM_SAFE_LIMITED_SPEED            Motion is limited to the defined "Safe
                                  Limited Speed". The limiting values
                                  for acceleration and jerk apply as for
                                  SOM_NORMAL_MODE
SOM_SAFE_HOLD                     Velocity = 0; active motion is decelerated to a
                                  standstill. The limiting values for acceleration
                                  and jerk apply as for SOM_NORMAL_MODE
The kinematic commands ⮫ Chapter 7.3.8 KinMoveDirectAsyncAbs - Direct
asynchronous absolute traversing of kinematics on page 538 and ⮫ Chapter

### 7.3.9 KinMoveDirectAsyncRel - Direct asynchronous relative traversing of kine‐

matics on page 543 represent a special case. During this motion, the axes
move independently with the defined axis dynamics. With this kinematic
motion, only the axes that have a safe drive operation mode ("Safe Limited
Speed" or "Safe Hold") are limited. The other axes move with the defined axis
dynamics.

Example
The diagram Fig. 226 shows the velocity of an active motion over time.
● At time t0, normal mode is active and motion takes place at the pro‐
  grammed velocity (v_prog)
● From time t1, the SOM_SAFE_LIMITED_SPEED mode is set, which reduces
  the velocity to the defined safe velocity (v_sls)
● Normal mode takes place at time t2 and the velocity is increased to the
  programmed velocity again
● SOM_SAFE_HOLD becomes active from t3 and the motopm is stopped until
  the mode is set back to SOM_NORMAL_MODE (time t4)

            vel

   v_prog

    v_sls

                  t0   t1                   t2                  t3   t4
                             Text is not SVG - cannot display

The resulting dynamics of the change in velocity result from the commanded
and configured axis and kinematic limits.

Safe limited speed
The "Safe Limited Speed" functionality limits the velocity of an axis or kine‐
matic motion to the defined speed limit if the associated drives provide the
SOM_SAFE_LIMITED_SPEED safety mode and the functionality has previously
been activated in the ctrlX MOTION.

Safe hold
The "Safe hold" functionality stops the active axis or kinematic motion as soon
as the associated drive(s) provide the SOM_SAFE_HOLD safety mode. The
motion is continued if no associated axis has the "Safe Hold" state in Safety
Mode.

Data Layer

motion/axs/<axs_name>/cfg/functions/safe-motion/drive-safe-
limited-speed/enable
motion/axs/<axs_name>/cfg/functions/safe-motion/drive-safe-
limited-speed/vel-limit
motion/kin/<kin_name>/cfg/functions/safe-motion/drive-safe-
limited-speed/vel-limit
motion/axs/<axs_name>/state/functions/safe-motion/drive-safe-
limited-speed-mode
motion/kin/<kin_name>/state/functions/safe-motion/drive-safe-
limited-speed-mode

### 6.3.10 Switching on the path

Basics
By using the functionality switch on path, a signal can be triggered (can be
set or reset) if a certain point on the kinematic path is reached. The function
switch on path can be used to start an activity while a robot arm is still
moving. This saves time, as the application does not have to wait until the
robot arm is stationary to start the activity. Application examples for switching
on path are "pick and place" machines and liquid dosing machines.
The "SwitchOnPath" command is only available for kinematics.

Description
The Switch on path function defines a point on a kinematic path. This point
is referred to as target position. When a kinematic motion command reaches
the target position, a signal is triggered. Several signals can be triggered in a
motion.
Since it is often difficult to define a target point that is precisely reached by
a 3D interpolated motion, a radius around this target point can be defined to
ensure that the algorithm detects that the target point has been reached. This
radius is used to define a sphere with the target point as center point of the
sphere.

                              R                                R

                         TP                               TP

TP Target point
R Spherical radius
Switching is triggered when the calculated target position of the kinematics is
reached in the sphere. In Fig. 227, the numbers ① to ⑦ refer to the calculated
command values of the path. The "SwitchOnPath" signal is triggered during
the motion control cycle when the command value ③ is calculated along the
red section of the path
In the figure on the right, no command value is calculated that lies within the
sphere as the velocity is too high in relation to the radius of the sphere. In
this situation, the algorithm does not detect that the target position has been
reached. The signal is not triggered.
Several target positions and/or signal IDs can be queued by entering the
"SwitchOnPath” command options several times with the duration ONCE or
PEMANENT_ON. If the command option "SwitchOnPath" is set to duration
PERMANENT_OFF, all target positions in the queue whose duration is set to
PERMANENT_ON are removed for the specified kinematics.
If a "SwitchOnPath" command option with "PERMANENT_ON" is enabled for a
kinematics object and a "SwitchOnPath" command option with "ONCE" is also
enabled for this kinematic motion object, and both signals can be triggered in
the next issued kinematics command, only the signal of the "SwitchOnPath"
command option with "ONCE" is triggered in the result. The signal of the
command option "SwitchOnPath" with "PERMANENT_ON" is not triggered.
This behavior allows you to temporarily override a "SwitchOnPath" command
option with "PERMANENT_ON". The command option with "PERMANENT_ON"
remains active and the signal defined for this command option is triggered
with the next kinematics command if the conditions of the "SwitchOnPath"
command option are met.
The specified signal is only triggered once for each "SwitchOnPath" command
option. If the kinematics reaches the target position again during the execu‐
tion of the same motion command, no further triggering takes place.
It is also possible to define a “pre-trigger” time. This "pre-trigger" time is used
to trigger the signal some time before it enters the sphere around the target
position. The calculation to estimate whether the signal needs to be triggered
is based on an extrapolation of the current path. If the direction of motion to
the target position or the velocity changes, the extrapolated path may deviate
from the actual motion, resulting in incorrect or no triggering.
A false trigger or failure to trigger is more likely if a long "pre-trigger" time is
selected.

                                                                  5
                                           6
                                   5                  2     3         4
                                                 1
                             4
                        3
                  2
                                  TP                                      TP
            1
                                       R                                       R

TP Target point
R Spherical radius

In Fig. 228, the numbers ① to ⑥ refer to the calculated command values of
the kinematic path. If the “pre-trigger" time is set to the duration of an update
cycle of the motion controller, the "SwitchOnPath" signal is triggered during
the cycle of the motion controller when the command value ③ is calculated in
the red section of the path.
If the “pre-trigger" time in the figure on the right is set to the duration of an
update cycle of the motion controller, the "SwitchOnPath" signal is triggered
during the Motion cycle when the command value ③ is calculated in the red
section of the path. However, the motion path is changed after the command
value ③. The ④ position is therefore not reached, but the ⑤ position. In this
situation, the signal is triggered incorrectly.

Command option
● ⮫ Chapter 7.5.13 KinSwitchOnPath, KinSwitchOnPathP, KinSwitchOnPa‐
  thEx, KinSwitchOnPathExP - Switching on the path on page 683
