# 4.1 General information

### 4.1.1 Real axes

Overview
The ctrlX MOTION can control and manage several drives. For each drive, one
axis and one axis profile has to be created in ctrlX MOTION.

                                                                                        Introduction and overview
The Motion kernel generates command values (e.g. interpolated positions)
and sends them to the axis profile. The axis profile encodes these command
values according to the selected Motion profile (e.g. CANopen over EtherCAT
(CoE) or SERCOS over EtherCAT (SoE)). The axis profile thus realizes an
abstraction of the Motion profile - Motion profiles can be easily changed by
replacing the axis profile.
The axis profile then sends the coded command values to the field bus driver.
Currently, only an EtherCAT Master is implemented for ctrlX CORE, but further
field bus masters may be available for selection in the future.
The EtherCAT Master subsequently transmits the coded command values to
the drives via the field bus. These comand values apply the command values
as input variables in their control loops (e.g. target positions for the position
control loop).
At the same time, the drive reads its measuring systems (e.g. motor meas‐
uring system) and generates actual values (e.g. an actual position). The actual
values are then coded according to the Motion profile and sent from the drive
to the EtherCAT Master via the field bus.
The EtherCAT Master in turn provides the coded actual values to the axis
profile. The actual values are decoded in the axis profile and subsequently
provided to the Motion kernel.
The actual values can be queried in the Motion kernel or other functions (such
as extrapolation of actual values) can be based on them.
Many actual values are optional and do not necessarily have to be configured
in the IO configuration of the field bus or in the axis profile. In this case, they
are of course not available in the Motion kernel.
In addition to the communication path for the command value and actual
values, there is also acyclical communication between the Motion kernel and
the drive. Analogous to the communication of the command value and actual
values, acyclical communication also takes place via the axis profile and the
field bus master. Acyclical communication is used to read drive parameters or
to send commands to the drive (e.g. measuring with a measuring probe).

Restrictions
Not all drives are supported by ctrlX MOTION. Please check the relevant docu‐
ments to see whether your drive is supported.
Changes to drive parameters that are relevant for the motion may only be
changed in the SETUP state of the ctrlX CORE. The control checks these
parameters when switching from SETUP to OPERATION, or derived parameters
are calculated on this basis. Cyclic real-time operation is active in OPERA‐
TION. This mode is optimized for high performance, but therefore only sup‐
ports minor parameter changes.

### 4.1.2 Virtual axes

Overview
The ctrlX MOTION can additionally also control and manage virtual drives. In
this case, only one axis is created in the ctrlX MOTION. An axis profile is not
required.

Real and virtual axes differ from the point of view of the ctrlX MOTION only in
that real axes are assigned an axis profile and virtual axes are not.
Thus, reconfiguration between real and virtual axis is faciliated. A real axis can
be switched to a virtual axis by removing the reference to the axis profile from
the axis configuration. Conversely, a virtual axis becomes a real axis by adding
a reference to an axis profile. Reconfiguring the reference to the axis profile is
only permitted in the SETUP state.
With virtual axes, the command values are copied to the actual values at the
start of each cyclic call. So if you compare command and actual values in a
function (e.g. PLC task) that runs between actual value acquisition and com‐
mand value generation, both values are identical. If the comparative function
runs after the command value generation, the actual values have a clock lag to
the command values.

### 4.1.3 Disabling axes (maximal project)

General information
When implementing modular machines or large-scale projects, it may be nec‐
essary to enable or disable motion axes or kinematics in an existing configura‐
tion without having to make changes to that configuration.
The Motion app provides the following nodes for this purpose:

Relevant configuration (Data Layer):
Data Layer path        Type                           Description
motion/axs/<name>/cfg/ bool                           TRUE: The axis is disa‐
properties/activated                                  bled and cannot be used.
                                                      FALSE: The axis operates
                                                      as configured
motion/kin/<name>/cfg/ bool                           TRUE: Kinematics is disa‐
properties/activated                                  bled and cannot be used.
                                                      FALSE: The kinematics
                                                      are functioning as config‐
                                                      ured

Data Layer path              Type                      Description
motion/axs/<name>/           bool                      Current axis condition:
state/activated                                        ● TRUE: The axis is ena‐
                                                         bled
                                                       ● FALSE: The axis is dis‐
                                                         abled and cannot be
                                                         used
motion/kin/Kine‐             bool                      Current status of the kin‐
matics/state/activated                                 ematics:

                                                                                       Introduction and overview
                                                       ● TRUE: Kinematics is
                                                         enabled
                                                       ● FALSE: Kinematics is
                                                         disabled and cannot
                                                         be used
The content of the node is saved remanently and is retained even after the
control is switched off.
A change to the node only becomes active when the Motion is booted (switch
from Configuration to Running).

Basic principle:
● Maximal project: All potential axes, kinematics, and modules are created
  once in the project. On the specific machine, only the parts that are
  actually present are set to "active"; all others remain "inactive."
● Enabled/disabled flag: Each Motion object (axis, kinematics) has an activa‐
  tion flag that is set in the configuration. It takes effect when switching from
  SETUP to OPERATION.
● Modular and certifiable: A certified maximum project ensures that variants
  with reduced features are also covered, without having to certify each com‐
  bination separately
● High performance: Only active objects are calculated in hard real-time. Dis‐
  abled objects have little effect on real-time performance

Typical workflows:
Creating axes/kinematics (maximum project)
1.      Creating all axes and kinematics that may be needed.
        Assigning unique names and configuring basic parameters (e.g., units,
        limit values).
        Assignment of devices (axis profiles) using unique device names, pro‐
        vided the hardware supports this feature.
Device ID and synchronization (EtherCAT)
2.      Configuring one sync unit per module in the EtherCAT Master.
        Recommendation: Configure the master so that it does not wait for all
        devices when switching to OPERATION mode. Missing complete sync
        units does not result in a boot error; the DL node of the EtherCAT Master
        shows which devices are available.
        See "EtherCAT Master App," Application Manual (R911403772), ⮫
        Using the information from the DL node, the EtherCAT address can also
        be determined based on the unique device name.

Enabling/disabling objects
3.   Enable/disable the corresponding axes/kinematics in the DL.
     If an axis is set to "not available" (disabled), its axis profile is also
     "inactive."
Switch to OPERATION
4.   When you switch from SETUP to OPERATION, the changes to the ena‐
     bled/disabled flag take effect.

Motion HMI App:
Configuration dialog (axis/kinematics):
You can switch between "All objects" and "Active objects only."
Disabled objects are grayed out, but their parameters can still be edited.
Commissioning dialog (axis/kinematics):
Only active objects are displayed.
Inactive objects display the status "OUTDATED." This status is also returned in
the PLC for disabled objects.
See "Motion HMI App," Application Manual; ⮫ link to the web documentation

Diagnostics and commands:
Commands sent to disabled objects are ignored and result in a clear diag‐
nostic message (the object is disabled and cannot receive commands). This
does not cause the object to generate an error.
In addition, please note the following:
● Disabled axes cannot serve as masters in SyncMotion/Gantry
● An axis cannot be added to a disabled kinematic configuration
● Commands such as AddToGantry, SyncMotion, and AddToKin prevent
  invalid combinations and display the appropriate diagnostic message

Real-time and performance
Only active objects are processed in the real-time section (state determination
and value generation).
Disabled objects cause only minimal overhead.

Licensing:
License count: Disabled axes/kinematics do not count toward licenses.

### 4.1.4 Motion global state machine

General information
The Motion system has a global state machine. This state machine describes
the switch-on and the resulting start-up, the configuration, the RUNNING
operating state and the ERROR state.

Global state machine

                                                                                          Introduction and overview
    The global state machine has the following important properties:
    ● While the state change has not yet been completed, all other queries
      (except for “Error”) are rejected
    ● Special critical error
      – A state change in ERROR is always possible and is executed immedi‐
         ately.

Status        What is happening? Permitted                Not permitted        Next status
BOOTING       ● Reading the con‐ The following            Everything except    ● State RUNNING,
figuration       results in a change      for “Abort”            if initialization is
● Creating Motion to state CONFIGU‐                                successful
objects          RATION:                                       ● State CONFIGU‐
● Initializing       ●   Abort                                     RATION, if an
internal struc‐    ●   Errors                                    uncritical error
tures              ●   Empty configura‐                          (missing axis
● Consistency            tion                                      profile or “Abort”
check                                                            was triggered)
● Axis profile query                                             ● State ERROR,
to switch to RUN‐                                                if an error or
NING                                                             a critical error
                                                                 occurred
RUNNING       ● Execution is run‐ ● Commanding            ● Add/remove        ● State CONFIGU‐
ning and cyclic   ● Change of spe‐          Motion objects      RATION, if com‐
data are send to    cially permitted      ● Change of           mands have been
the axis profile    configuration           "Basic configura‐   completed and
● System accepts      data                    tion data" (e.g.    if all Motion
commands                                    cycle time)         objects have
                                                                reached the
                                                                status STAND‐
                                                                STILL
                                                              ● State ERROR,
                                                                if critical errors
                                                                occurred

Status     What is happening?         Permitted            Not permitted         Next status
CONFIGURA‐ ● System is in a           ● Add/remove         ● Commands            ● State BOOTING,
TION         static state               Motion objects                             after configura‐
● No program is            ● Configuration                              tion has been
executed                   data change                                completed
● No cyclic data                                                      ● State ERROR,
is transmitted to                                                     if critical errors
the field bus                                                         occurred
ERROR      ● System is set to         ● Change to state    ● everything except ●    State CONFIGU‐
safe state                 Configuration        for change to          RATION, after
                                       state CONFIGU‐         commanding and
                                       RATION                 after the safe
                                                              state has been
                                                              reached
The state of the ctrlX MOTION can be switched directly in the Motion configu‐
ration dialogs.
In addition, the status of the ctrlX MOTION changes when the status of the
entire control system (with all apps) is changed. The Motion status is linked
to the global control status.
The global status "OPERATION" corresponds to the ctrlX MOTION state "RUN‐
NING". In the global states "SETUP" and "SERVICE", the ctrlX MOTION auto‐
matically switches to "CONFIGURATION".

### 4.1.5 Motion objects

General information
Motion objects represent the central instances in the Motion system.
Depending on the type, they represent an axis or kinematics and can be con‐
figured and commanded.
The Motion objects are configured via the web interface or via direct access
via the Data Layer. As all Motion objects are addressed via their names, the
names have to be unique. The name can be up to 16 characters long and
may only contain the characters [a-z][A-Z][0-9]_. To create and delete Motion
objects, the Motion system has to be in CONFIGURATION state.

Axis objects
General information
The axis object is a characteristic of the Motion object. This object contains
information to control an axis.
The axis object configuration decides whether the axis is virtual or real. Real
axes have a configured axis profile in contrast to virtual axes. The axis profile
represents the interface between Motion axis and field bus.
The interfaces as well as the structure are identical for real and virtual axes.

State machine
Each axis object has its own state machine. This shows the current status of
the axis. The state machine also defines the permitted state transitions. The
state machine is based on the PLCopen specification.
The state machine is only updated cyclically if the Motion kernel is in RUN‐
NING status. If the Motion kernel status is not in state RUNNING, the [axis
object/kinematic object] always returns the state OUTDATED.

                                                                                     Introduction and overview

Operation modes
Depending on the configuration and the used drive, an axis can be traversed
in different operation modes. Currently, position control, velocity control, and
torque control are supported.
An operation mode determines which command values are processed by the
connected device to generate the desired motion.
In position control mode, the position command value is transmitted cyclically
to the connected device and is processed by it. This operation mode is used if
it is important to approach the exact position.
In velocity control mode, the velocity command value is transmitted cyclically
to the connected device and processed by it. This operation mode is used if a
continuous motion at a certain velocity is required.
In torque control mode, the torque command value is transmitted cyclically
to the connected device, which then processes it. In addition, the upper and
lower velocity limit limits for the torque are specified.
The respective operation modes require different configurations and values in
the cyclic device data:
Operation mode            Cyclic data              Configuration in the
                                                   device
Position                  Position command value Positioning modes
Velocity                  Velocity command value Velocity mode
Torque with speed limita‐ Torque command value     Torque mode
tion                      Torque upper velocity    Torque command value
                          limit                    Torque upper velocity
                          Torque of lower velocity limit
                          limit                    Torque of lower velocity
                                                   limit
Example of a device with SoE communication profile:
Operation mode      Cyclic command     Actual cyclic        Configuration in
                    values             values               the device
Position            S-0-0047: Position S-0-0051: Actual     S-0-0032: 0x010B
                    command value      position value

Operation mode      Cyclic command     Actual cyclic      Configuration in
                    values             values             the device
Velocity            S-0-0036: Velocity S-0-0040 : Actual S-0-0033: 0x0002
                    command value      velocity value
Torque              S-0-0080: Torque S-0-0084: Actual     S-0-0034: 0x8101
                    command value      torque/force value
                    P-0-421.0.3 Torque P-0-0421.0.7
                    control High       Torque limitation
                    Velocity Value     status
                    P-0-0421.0.4
                    Torque control
                    Low Velocity Value
For the configuration of other profiles, please check the respective profile
specification.
After the start-up, after an AxsReset or AxsAbort, the axis is always in the
operation mode position control.
ctrlX MOTION continues to calculate target positions even in velocity control
mode. As a matter of principle, in case of longer travel in the operation mode
velocity control (in particular in case of “noisy” encoders or a very slow axis),
minimal deviation between the target position of the control and the actual
position of the drive can occur.

Switching between different operation modes of a device in motion ("on-the-
fly operating mode switchover")
Switching between position control mode and velocity control mode and vice
versa can be realized "on the fly". During the operating mode switching, the
required values for position and velocity are automatically extrapolated for the
respective axis type. Additional customization in the Data Layer is possible for
devices from other manufacturers. Refer to ⮫ Chapter 6.1.2 Extrapolation for
operating mode switching in motion on page 74.
On-the-fly switching of the operation mode can only take place for "non-buf‐
fered" motion commands (command option "buffered = false")!

Axis types
The following axis types are supported:
● Linear axis (units in mm, inches,...)
● Rotary axis (units in degrees)
All axis types support the configuration as:
● Modulo axis (the position is always in the defined modulo range)

Modulo axes
Absolute commanding:
In case of absolute commanding (e.g. PosAbs), the commanded target posi‐
tion is internally converted to the defined modulo range. The positioning
strategy “Shortest distance” is used. In case this strategy is used, the direc‐
tion of motion is determined using the shortest distance to the target posi‐
tion. The distance is always a maximum of 0.5 * modulo value. When deter‐
mining the shortest distance, the deceleration path resulting from the current
velocity and acceleration is not taken into consideration.
Incremental commanding:

In case of incremental commanding (e.g. PosRel, PosAdd), the direction of
motion to the target position is determined by the sign of the commanded
distance. The commanded distance is travelled irrespective of the modulo
value.
In all cases, the reached target position lies within the defined modulo range:
0 <= reached target position < modulo value
Modulo configuration via Data Layer:
Method: GET/PUT
URL: https://<ip-addr>/automation/api/v2/nodes/motion/axs/<axs_name>/cfg/
properties/modulo

                                                                                     Introduction and overview
Payload:

{"type":"bool8","value":true}

Method: GET/PUT
https://<ip-addr>/automation/api/v2/nodes/motion/axs/<axs_name>/cfg/prop‐
erties/modulo-value
Payload:

{"type":"double","value":360}

Method: GET/PUT
https://<ip-addr>/automation/api/v2/nodes/motion/axs/<axs_name>/cfg/prop‐
erties/type
Payload:

{"type":"string","value":"LINEAR"}

The parameter can assume the values LINEAR or ROTATIONAL.
Examples (with modulo value = 360, start position = 0)
Table 1: Buffered commands: PosAbs
Commands                           Result                             Image
PosAbs(710)                        Travel -10 units to 350            1.1
PosAbs(730)                        Travel +10 units to 10             1.2
PosAbs(710), buffered              Travel -10 units to 350 Subse‐     1.3
PosAbs(-355), buffered             quently, travel +15 units to 5
PosAbs(730), buffered              Travel +10 to 10 Subsequently,     1.4
PosAbs(-365), buffered             travel -15 units to 355

Table 2: Unbuffered commands: PosAbs
Commands                           Result                              Image
PosAbs(-90), but in Position 350, Decelerate and travel to 20 in posi‐ 2.1
an unbuffered PosAbs(20) is com‐ tive direction
manded
PosAbs(90), but in position 10, an Decelerate and travel to 10 in neg‐ 2.2
unbuffered PosAbs(370) is com‐     ative direction
manded

                                                                                   Introduction and overview
Table 3: Unbuffered commands: PosRel, PosAbs
Commands                           Result                             Image
PosRel(10) with axis in STAND‐     Travel +10 units to 10             3.1
STILL
PosAbs(90), but in position 10,    Decelerate and travel to 350 in    3.2
an unbuffered PosRel(-20) is com‐ negative direction
manded
PosAbs(90), but in position 10,    A complete revolution and then     3.3
an unbuffered PosRel(360) is com‐ travel to 10
manded
PosAbs(90), but in position 10, an A complete revolution and then     3.4
unbuffered PosAdd(360) is com‐     travel to 90
manded

Commands                          Result                              Image
PosRel(720)                       Travel two complete revolutions     4.1
                                  in positive direction and subse‐
                                  quently travel to 0
PosRel(720), but in position 10,  A complete revolution and then      4.2
an unbuffered PosRel(360) is com‐ travel to 10
manded
PosRel(720), but in position 10   Decelerate and travel to 0 in nega‐ 4.3
but an unbuffered PosAdd(-720) is tive direction
commanded

Encoder axis objects
General information
Encoder axes are used to evaluate an additional encoder that is connected to
an actual physical axis and provides position information within the system.
An encoder axis serves as a master axis for synchronized motions, but cannot
be controlled directly.
Whether an encoder axis object is designated as a virtual or real axis is
determined by the connection of an encoder profile to the encoder axis. The
encoder profile serves as the axis profile type.

Encoder profile
The encoder profile focuses on data transfer and does not attempt to com‐
mand the encoder device. Profile categories are used to differentiate between
the drive profile and the encoder profile.
Profile categories:
● CATEGORY_DRIVE
● CATEGORY_ENCODER
Elements
To achieve the desired result, it is necessary to enter position data; velocity
data is optional.

Input elements            Cyclic data                 Configuration in the
                                                      device
Position                  Actual position of the      1. P-0-0052 for Indra
                          encoder                     Drive
                                                      2. User-configured posi‐
                                                      tion
Velocity                  Actual encoder velocity     1. P-0-0332 for Indra
                                                      Drive
                                                      2. User-configured

                                                                                      Introduction and overview
                                                      velocity
In contrast to the drive profile, the encoder profile only contains the input
assignment elements; the output assignment elements should be empty.

State machine
Each object of the encoder axis is equipped with its own state machine,
which reflects the current state of the axis. This machine not only displays the
current status, but also delimits the permissible status transitions.
The state machine is only updated cyclically if the Motion core is in state
RUNNING. If the motion kernel is not in state RUNNING, the OUTDATED state
is always returned.
Due to the nature of an encoder axis, which is designed to operate in either
the CONTINUES_MOTION or ERRORSTOP motion state. In the event of an
error, such as the loss of 3-AT telegrams, the state machine should switch to
the error stop state. However, it is important to note that the reset command
cannot be used in this scenario. Instead, alternative methods such as receiving
3-AT telegrams or switching operation are required to rectify and delete the
error.

Output
The encoder axis provides the current position and velocity data in the units
configured by the user.

Axis type
The following axis types are supported:
● Drive axis
● Encoder axis
The encoder axis supports some special configurations:

● Gear ratio: It consists of the input gear rotation and the output gear rota‐
  tion
● Resolution: The incremental position unit can be converted into SI units
  using the resolution. The resolution on the drive should not be changed,
  as this will lead to calculation errors. If the resolution on the drive is
  changed, the resolution value (S-02571 for SoE) has to match the value on
  the Motion.
● Feed constant: This parameter is only relevant for linear axes. The feed
  constant indicates the distance that the axis travels when the measuring
  device completes one revolution
● Filter: Filters the position information

Filter
Filters can be added to smooth the position value of noisy encoders:
●   1st order low-pass filter
●   2nd order low-pass filter
●   2nd order Butterworth filter
●   2nd order low-pass filter with velocity feedforward (dead time compen‐
    sated)
● 3rd order low-pass filter
● 3rd order Butterworth filter
● 3rd order low-pass filter with acceleration feedforward (dead time compen‐
    sated)
The cutoff frequency of the filters can be specified by the user.
Filters can also be applied to the encoder values of drives. The filter acts on
the actual position of the drive values. If the filter is activated, the extrapola‐
tion is based on the filtered values.

Commanding
Due to the characteristics of the encoder axis, this axis cannot be commanded
directly by the user. The only available commands are:
● "Setting the absolute position," which is used to define the reference posi‐
  tion
● "probe-ex/probe-abort-ex," which is used to start and stop the probe on
  the axis
Determine the reference position:
As an incremental encoder is used, the reference position is set after the
control is started.
The reference position can be set using the command ⮫ Chapter 7.2.30 AxsSe‐
tAbsPos - Set axis to absolute position on page 476 which uses the same
interface as the existing drive-based command. However, the behavior differs;
in particular, the encoder reference command merely establishes an offset
between the control and the encoder.

Fine-tuning function for the encoder axis

Function
The "Encoder axis fine-tuning" function provides a real-time, online method
for compensating for slip or scaling deviations between a moving material and
its encoder axis.
Typical use case (Flying Shear)
In a Flying Shear system:

The material moves continuously in one direction. An encoder axis measures
the movement of the material. A slite or cutting unit synchronizes with the
encoder axis during the cutting process.
If the encoder drifts relative to the material the virtual material position drifts
away and the cut length becomes inaccurate.
The fine-tuning function corrects this drift online by slightly scaling the
encoder position and velocity.
Fine-tuning behavior
Meaning of the fine-tuning value:

                                                                                          Introduction and overview
The fine-tuning value is a unitless percentage correction applied to the
encoder motion:
● 0.0 → No adjustment
● Positive value → Encoder motion is slightly increased
● Negative value → Encoder motion is slightly reduced
Internally, the value is converted to a gain factor centered at 1.0 to ensure
uniform scaling.
Effect on velocity:
● The encoder velocity is multiplied by the "Fine Adjust" gain factor
● The velocity changes smoothly according to the "Fine Adjust" input value
Impact on the position:
● The position is updated based on the adjusted velocity
● The data from the previous cycle is saved to ensure continuity
● There are no position jumps, not even in case of dynamic changes
Using the fine-tuning function
1.   Enable fine-tuning in the Data Layer
     Enable the feature using the following node in the Data Layer:
     motion/axs/<axis_name>/cfg/functions/encoder/fine-adjust
        Property                              Value
        Data type                             bool
        Access                                Read/write
        Version                               RM26.03 (4.6)
        ● TRUE → Fine-tuning enabled
        ● FALSE → Fine-tuning disabled
          For compatibility reasons, this flag is set to FALSE by default in proj‐
        ects created before version 4.6.
2.      Set system to running mode
        The fine-tuning feature works only in run mode.
        ● No configuration function required
        ● No restart required

3.   Enter the fine-tuning value online
     Enter the desired fine-tuning value cyclically or as needed in:
     motion/axs/<axis_name>/cmd-input/double/data/in
     Property                              Value
     Data type                             double
     Version                               RM26.03 (4.6)
     Index                                 10
     Default value                         0.0
     Section                               [-1000, 1000]
     Property value
     Data type
     Version RM26.03 (4.6)
     Index 10
     Default value 0.0
     Value handling:
    ● Values outside the valid range are automatically limited
    ● Example:
      – Input 1200 → is applied as 1000
      – Input -1500 → is applied as -1000
Recommended application strategy
● Start with 0.0
● Adjust the value gradually during manufacturing
● Avoid large changes in jump height
● Do you prefer ramp or control logic
Typical use cases:
● Manual correction by the operator
● PLC-based adaptive compensation
● Length-feedback-based adjustment
Restrictions and notes
● Fine-tuning is no substitute for the quality of installation of mechanical
  encoders
● High values indicate mechanical problems
● Intended for fine adjustment, not for rough scaling

Kinematic objects
General information
Kinematics facilitate coordinated multi-axis motions in Cartesian space (posi‐
tion, orientation, additional axes). Several axes are grouped in a link (at least
1, a maximum of 16) and can facilitate motions along a defined path.
Axes can be added to or removed from a kinematic system during operation
(Motion system status RUNNING) using commands. Therefore, it is necessary
that the axes have been configured for this kinematics before (Motion system
status CONFIGURATION).

State machine
Each kinematics object has its own state machine, which displays the current
state of the kinematics. The state machine is based on the PLCopen specifica‐
tion.

The state machine is only updated cyclically if the Motion kernel is in RUN‐
NING status. If the Motion kernel status is not in state RUNNING [axis object/
kinematic object] always returns the state OUTDATED.

                                                                                    Introduction and overview

Further information
Further details on kinematics and their functions can be found in the “Kine‐
matic functions" chapter.

### 4.1.6 Motion System Configuration

General information
The MotionKernel is configured via the Data Layer. The structure in the Data
Layer can be shown as tree.
All leave nodes can be read and written (Get/Put). Certain intermediate nodes
can be read and written as flat buffer structure (when using the WebServer,
Json structures are used).
It can be browsed on all levels (not on leaves).
All Motion objects (axes, kinematics) are addressed via their names. This
means that these names have to be unique in the system (no axis with iden‐
tical name as the kinematics).
The length of the names is limited to 16 characters.
Naming convention as regular expression:
● [\w][[:alnum:]]* /u
● [a..zA..Z0-9]
The configuration is applied immediately (to create and delete axes/kine‐
matics, the Motion system has to be in the CONFIGURATION state.)

To simplify the configuration, there is a user interface used to configure the
Motion system via the web browser.
Refer to ⮫ Chapter 8.1.2 Window – “Axes” on page 795

### 4.1.7 Saving Motion data

Configuration
Amongst others, the Motion configuration data is saved in the "Configuration".

Which data is archived
Configuration data of the Motion system
● Axis configuration (including limits, axis profile)
● Kinematic configuration (including limits, assigned axes, PCS)

Data format/file structure
Each configurable object has its own file. The file name is identical to the
object name (please note that these names are UTF8-coded).
All configuration files contain a json object containing the same information as
the configuration nodes in the Data Layer.
Axis objects are contained in the “Axis” folder, kinematic objects are con‐
tained in the “Kinematics” folder.

Content of Axis_1.json

{
     "$persistence_header": {
         "bfbs": "./bfbs/cfg.bfbs",
         "version": "0.0.2"
     },
     "$schema": "./types/cfg_schema.json",
     "axisProfileName": "Axis_1",
      "devErrReaction": {
         "estopSettings": {
             "estopToDevCriticalErr": "ESTOP_AXIS_LIMIT",
             "estopToDevFatalErr": "ESTOP_AXIS_LIMIT",
             "estopToDevLightErr": "ESTOP_AXIS_LIMIT",
             "estopToFieldbusErr": "ESTOP_AXIS_LIMIT",
             "estopToNoDevErr": "ESTOP_AXIS_LIMIT",
             "estopToNoDeviceInfo": "ESTOP_AXIS_LIMIT"
         },
         "userEstopLim": {
             "dec": 2.0,
             "decUnit": "m/s^2",
             "jrkDec": 0.0,
             "jrkDecUnit": "m/s^3"
         }
     },
     "functions": {
         "coupling": {
             "gantry": {
                 "isMember": false,
                 "moveAllowed": false,
                 "multiBrakeDyn": false
             }
         }

},
"kinProperties": {
    "accReserve": 0.0,
    "jrkReserve": 0.0
},
"limits": {
    "acc": 2.0,
    "accUnit": "m/s^2",
    "dec": 2.0,
    "decUnit": "m/s^2",

                                                                      Introduction and overview
    "jrkAcc": 0.0,
    "jrkAccUnit": "m/s^3",
    "jrkDec": 0.0,
    "jrkDecUnit": "m/s^3",
    "posMax": 1000.0,
    "posMaxUnit": "mm",
    "posMin": -1000.0,
    "posMinUnit": "mm",
    "velNeg": 6000.0,
    "velNegUnit": "mm/min",
    "velPos": 6000.0,
    "velPosUnit": "mm/min"
},
"objectType": "Axis",
"properties": {
    "axsType": "LINEAR",
    "modulo": false,
    "moduloValue": 360.0,
    "moduloValueUnit": "mm"
},
"rtInputs": {
    "doubleArraySize": 5,
    "int64ArraySize": 0
},
"units": {
    "default": [
        {
            "abbreviation": "mm",
            "valueType": "position+length"
        },
        {
            "abbreviation": "mm/min",
            "valueType": "velocity"
        },
        {
            "abbreviation": "m/s^2",
            "valueType": "acceleration"
        },
        {
            "abbreviation": "m/s^3",
            "valueType": "jerk"
        },
        {
            "abbreviation": "N",
            "valueType": "force"
        },
        {
            "abbreviation": "Nm",

                      "valueType": "torque"
               },
               {
                      "abbreviation": "s",
                      "valueType": "time"
               }
           ]
    }
}

Interface for Load/Save
There are interfaces to save and load configuration files in the Data Layer.
Each command is transferred as create (post).
Data Layer path                        What is executed
https://<ip-addr>/automation/api/v2/   Loads the configuration file of this
nodes/motion/axs/<axs_name>/cfg/       axis
load
https://<ip-addr>/automation/api/v2/   Saves the configuration file of this
nodes/motion/axs/<axs_name>/cfg/       axis
save
https://<ip-addr>/automation/api/v2/   Loads the configuration file of this kin‐
nodes/motion/kin/<kin_name>/cfg/       ematics
load
https://<ip-addr>/automation/api/v2/   Saves the configuration file of this kin‐
nodes/motion/kin/<kin_name>/cfg/       ematics
save
motion/cfg/load                        Loads the global configuration data of
                                       the Motion system
motion/cfg/save                        Saves the global configuration data of
                                       the Motion system
motion/cfg/load-all                    Loads the entire Motion system con‐
                                       figuration (all child nodes), objects
                                       without file are deleted
motion/cfg/save-all                    Saves the entire Motion system config‐
                                       uration (all child nodes)

Typical use cases
Most use cases of “Configuration” can be implemented as simple file opera‐
tions.
Use case                               How is this implemented
Render current configuration persis‐   Create (post) on "save-all"
tent
Reload entire configuration           Create (post) on “load-all"
Copying an axis                       Copy configuration file of the axis, the
                                      name of the new file corresponds to
                                      the name of the new axis
Generate 200 axes (with identical     Generate an axis template, copy this
parameters)                           file 199 times
Render changes of an individual kine‐ Create (Post) on "https://<ip-addr>/
matics persistent                     automation/api/v2/nodes/motion/kin/
                                      <kin_name>/cfg/save"
Renaming the axis                     Rename the corresponding file
                                      (becomes active after a “load-all”)

### 4.1.8 Motion kernel state via Data Layer

Configuration
The current state of the Motion kernel can be queried via the Data Layer.
The structure in the Data Layer can be shown as tree.
All leave nodes can be read (Get).
Complex nodes are returned as flat buffer structure (there are JSON struc‐
tures together with the WebServer).
It can be browsed on all levels (not on leaves).

                                                                                       Introduction and overview
All Motion objects (axes, kinematics) are addressed via their names. This
means that these names have to be unique in the system (no axis with iden‐
tical name as the kinematics).
Naming convention as regular expression:
[\w][[:alnum:]]* /u
[a..zA..Z0..9]
State tree, see "ctrlX OS", Application manual (R911403768), chapter ⮫ ctrlX
Data Layer - Node description ‒ “Motion” nodes

### 4.1.9 Units

Many values of ctrlX MOTION have units (e.g. millimeters, revolutions per
minute etc.)
The following is described in this chapter:
●   How to configure default units
●   How to query values of ctrlX MOTION in desired units
●   How to read and write configuration parameters in desired units
●   How ctrlX MOTION interprets parameters for commands

Basic information
Each unit is assigned to a value type:
● Position & length
● Velocity
● Acceleration
● Force
● Time
● …
The unit can only be used for values of this value type. For example, when
trying to set the default unit for web velocity of a kinematics (value type
“velocity”) to set to seconds (seconds → value type “time"), the change
request is rejected by ctrlX MOTION with an error message.
Moreover, each unit is assigned to an object type:
● Linear
● Rotary
● Linear/rotary
The object type is mainly relevant to axes. For example, the position for rotary
axes is specified in degree or revolutions, linear axis positions are specified
in millimeters or inch. Corresponding units exist for velocity, acceleration and
jerk.

                      If the axis type (linear, rotary) is changed, the default
       NOTICE         units of this axis are reinitialized by ctrlX MOTION. This
                      is required as there is no conversion between linear and
                      rotary units. Subsequently, all limit values of this axis
                      have to be reset.

Standard units
For each axis and each kinematics, standard units can be config‐
ured. In the Data Layer, the corresponding configuration URIs can
be found under the node https://<ip-addr>/automation/api/v2/nodes/
motion/axs/<axs_name>/cfg/units or https://<ip-addr>/automation/api/v2/
nodes/motion/kin/<kin_name>/cfg/units, see documentation "ctrlX CORE,
Data Layer Nodes 02VRS" ⮫ Link to the web documentation).
If the standard units of an axis or a kinematics have to be changed, the other
parameters of the axis/kinematics usually do not have to be adjusted. They are
converted to a new unit during queries. If required, the application might have
to be modified in order to take the new units in queries and commanding into
consideration.
For kinematics, the standard units are configured for position data of all 16
possible axes. The first three entries have to be linear units (for X, Y, Z);
subsequently, three entries with rotary units (for orientation purposes) and
ten entries with linear or rotary position units. The configured units have to
match the axis types to be assigned to this kinematics. If several axes are to
be assigned to the same kinematic index, they require the same position unit.

Commanding
When commanding axes and kinematics, a high-performance low-level inter‐
face is used. E.g, this is required to assign new commands to a task running in
synch to the ctrlX MOTION interpolation in real-time.
Therefore, all command parameters (e.g. the target position of AxsPosAbs)
is interpreted using the standard units. This means, if the position unit centi‐
meter is configured for the axis and a positioning command is specified with
target position 12.5, the axes travels to 12.5 centimeters. The same applies to
all other parameters with units (such as velocities, accelerations etc.).

Special case kinematic positions
If a kinematic motion is commanded, it also has to be specified in which coor‐
dinate system the target position/relative position/direction vector is specified
(PCS, WCS, MCS or ACS). If PCS, WCS or MCS is specified, the position
values are interpreted with the units configured for the kinematics. If, on
the other hand, programming is realized in ACS, the position values are inter‐
preted with the units configured for the axes of the kinematics.
Example:
●   Kinematic configuration: m, m, m
●   Axis x configuration: mm
●   Axis y configuration: mm
●   Axis z configuration: mm
●   The x, y, z axes are assigned to the kinematics
If (0.5; 0.7; 0.2) is commanded as target position in WCS for the kinematics,
the kinematics travels to (x=0.5m; y=0.7m; z=0.2m). However, if (100, 200,
300) is commanded in ACS, the kinematics travels to (x=100mm; y=200mm;
z=300mm).
It is recommended to configure the default units for the kinematic positions
and axis positions identically.

Querying values
Also when querying values of ctrlX MOTION of a bundle, the high-performance
low-level interface from the PLC or a script is used. This is e.g. required
to query data in a task that is running (synchronized) to the ctrlX MOTION
interpolation.
Therefore, all data (e.g. the interpolated axis velocity) are provided in the con‐
figured standard units. This means, if “revolutions per minute” is configured
as velocity unit for the axis and the interpolated velocity is 327, the axes
travels at a velocity of 327 rpm.

                                                                                       Introduction and overview
Reading and writing values in the Data Layer (non-RT)
ctrlX MOTION provides a large amount of data via the Data Layer (non-RT).
This data can be used in an application or a user interface (“state” child
node). These access data is read-only.
Additionally, access to the ctrlX MOTION configuration is possible via the Data
Layer (non-RT). The configuration data can be read and written (“cfg” child
node).

Single accesses
If a value with a unit is read by the regular Data Layer URI, ctrlX MOTION
returns this value as configured standard unit. This is also returned in
the URI meta data. Additionally, all supported units for this value can
be determined by browsing the URI. One of the provided values can
be attached to the URI to read the value in another unit. For example,
if m/s² is configured as the default unit for an axis acceleration, and
the Data Layer URL https://<ip-addr>/automation/api/v2/nodes/motion/axs/
<axs_name>/cfg/lim/acc returns the value 2.4, this means that an accelera‐
tion limit value of 2.54 m/s² is configured for this axis. Browsing on the
URI returns other potential units (such as "in-per-s^2" → inch per square
second). Thus a query on the URL https://<ip-addr>/automation/api/v2/
nodes/motion/axs/<axs_name>/cfg/lim/acc/in-per-s^2 returns the value 100
(because 100 in/s² == 2.54 m/s²). The described access can be a read access
(in case of states and configuration) as well as a write access (only configura‐
tion).

Querying structures
If a large part of the data or the configuration is read/written, structures are
used. These structures contain different values with different units. Values as
well as units are part of the overall structure.
If such a structure is read, it returns values to the configured standard units.
However, a structure can be transferred during reading that contains the
required units. In this case, the values are returned in the required units.

Writing structures
Complete structures can be written in the configuration. If no units have been
transferred during writing of a structure, the values are interpreted with the
configured standard units. If units are transferred, they are used.

Configuration data on ROM
Saved configurations use the same structures and algorithms as the access via
the Data Layer (non-RT). This means, units are also stored in the saved files.
If this data is modified, other units can also be entered in the files. If ctrlX
MOTION supports the units (and the value type and object type match), the
values are converted. If the types do not match, an error is reported.

Querying all supported units
To determine which units are supported by the current version of the ctrlX
MOTION you can query the motion/state/units node in the Data Layer, see
the documentation "ctrlX CORE, Data Layer Nodes 02VRS" ( ⮫ link to web
documentation). A list containing all supported units and their data (name,
abbreviation, URI, value type, object type) is returned. A filter can also be
added to the query. If an individual entry with e.g. a value type is transferred,
the query returns all units with the required value type. In the filter element,
several entries (e.g. value type and object type) can be included.
Optionally, an array can be returned containing only elements with the unit
name. All data of the corresponding units is returned.

Further information
● See chapter 4 "Introduction and overview"

### 4.1.10 Scalings

Different scalings can be configured in the drive. The axis profile is respon‐
sible for the drive scaling. The profile reads all parameters when switching
the axis profile to “Running” from the drive and calculates the scaling of the
“Least Significant Bit” (LSB ≘ bit with the lowest value) from the parameter
values.
By using this information, the following is possible:
● The ctrlX MOTION data can be transmitted to the drive correctly by the axis
  profile (matching the set scaling)
● The drive data can be transmitted to the drive correctly by the axis profile
  (matching the set scaling)
The following parameters are read by the drive:
●   S-0-0076 (scaling type for position data)
●   S-0-0077 (scaling factor for translatory position data)
●   S-0-0078 (scaling exponent of translatory position data)
●   S-0-0079 (rotation position resolution)

Restrictions with regard to the requirements
The current implementation does not yet facilitate the scaling configuration in
the virtual control and to subsequently upload it to the hardware. No image of
the scaling parameters are retained or managed in the axis profile.
Currently, only the position data scaling is supported.

Non-functional criteria
Due to performance reasons, the scaling cannot be refreshed continuously.
This is why the scaling is only refreshed when switching the axis profile to
state “Running”. This information is important for the user as a change in the
scaling directly on the drive (e.g. via ctrlX DRIVE) is initially not detected by
the control while the system is in state “Running”. Consequently, incorrectly
scaled motions can occur! The changes become active only in case of state
switching of the axis profile and the state between drive and control is consis‐
tent again.

Further information
● See chapter 4 "Introduction and overview"

### 4.1.11 Motion-synchronous commanding

The real axes are controlled via EtherCAT. In each cycle, the actual values
are transferred from the drive to the control and, in turn, the new command
values are transferred from the control to the drive. To enable optimum proc‐
essing, a so-called Motion-synchronous routine can be inserted between the
receipt of the actual values and the generation of the new command values.
In ctrlX CORE, the ctrlX MOTION s called in two "callables". The first "Call‐
able" ("DetermineState") takes care of processing the actual values supplied
by the drive. The second callable ("GenerateValues") generates the new com‐
mand values for the drive. The Motion-synchronous routine can be inserted

                                                                                                                                      Introduction and overview
between the two "callables" as an additional "callable".
In ⮫ fig. 4.1.11 shows the sequence of the various "callables" in the scheduler
task "ctrlXAutomation". This sequence is processed in every bus cycle.

                                  Motion      Real-time     Motion                      Real-time
        EtherCat   AxisProfile                                          AxisProfile                          EtherCat
                                 Determine   Application     Value                     Application
         Master    Adaption                                             Distribution                          Master
                                   State          A        Generation                       B

   New cycle                                                                                         New cylce          time

The two preferable positions for calling the "callable" of a real-time applica‐
tion are highlighted in color and marked with "Real-time Application A" and
"Real-time Application B". The appropriate position depends on the real-time
application. Influencing factors are the reaction time to events and the prompt
generation of new control commands. The graphic shows the optimum posi‐
tion in relation to the application requirements.
                                             Fast response to actual                         Fast generation of com‐
                                             values                                          mand values
Generating new motion                        Real-time Application A                         no preference
commands
Writing outputs                              no preference                                   Real-time Application B

Implementation as a real-time application
With the Real-Time SDK, a "callable" has to be created to create a real-time
application. The "SyncPoints" can be used to specify at which point in the
sequence in the scheduler task "ctrlXAutomation" the "Callable" of the real-
time application is called. Detailed information can be found in the documen‐
tation of the Real-Time SDK.
Real-time application A:
● After the SyncPoint motion-determine-state-exit
● Before the SyncPoint motion-value-generation-entry
Real-time application B:
● After the SyncPoint axisprofile-distribution-exit

Implementation in the PLC
As the PLC tasks are not managed by the scheduler of the ctrlX CORE, but
have a separate scheduler, some additional settings have to be selected.
● Creating a callable that wakes up a PLC task
● The PLC task has to run on the same CPU core as the ctrlX scheduler
● The PLC task has to have a higher priority than the scheduler task
Creating a callable

Create a callable of type plc-external-event in the scheduler task "ctrlXAu‐
tomation".
Set CPU core
In PLC Engineering, configure on which CPU core the real-time task of the
PLC should run. It has to be the same CPU core on which the scheduler task
"ctrlXAutomation" is running. You can see this in the overview dialog of the
scheduler.
Set priority
The priority of the PLC tasks has to be set to a lower value (== higher priority)
than the priority of the scheduler task "ctrlXAutomation". The PLC task priority
is set in the same dialog in which you specify the CPU core.

Further information
● See chapter 4 "Introduction and overview"
