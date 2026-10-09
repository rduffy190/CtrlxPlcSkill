# 6.1 General functions

### 6.1.1 Extrapolation of actual values

There is always an offset between the current position of a drive as an actual
value within the ctrlX control and the actual position of the drive. This offset
is primarily influenced by the field bus communication times between the
control and the drive, as well as by the coupling method or the type of axis
used. The used source can be dynamically switched between the drive's actual
values and an external encoder.
To compensate for this offset in the ctrlX internally, an axis-specific extrapola‐
tion can be configured.
The following variables are extrapolated:
● Actual position
● Actual velocity
● Actual acceleration

Extrapolation types:
● Extrapolation using actual dynamic data (velocity and acceleration)
● Extrapolation using external dynamic data (velocity and acceleration)
Extrapolation using actual dynamic data works well during axis motion at a
constant velocity. However, during the acceleration or deceleration phase of
the axis, the actual dynamic values lag behind the corresponding interpolated
dynamic values due to the long delay between the ctrlX CORE and the drive,
rendering their use for calculating extrapolated values inaccurate. For encoder
axes, only the actual position value is available, which results in a less accu‐
rate extrapolation.
If the interpolated dynamic values for the target axis are available, the user
can feed them into the extrapolation process via the PLC interface, resulting
in significantly higher accuracy. For applications that require high position
accuracy, such as “flying shear,” where the cutting unit typically has to be
synchronized with an encoder axis, extrapolation using external dynamic data
is recommended.

The default selection for extrapolation is “Extrapolation with actual dynamic
data”; the user can change this to “Extrapolation with external dynamic
data” via the Data Layer path “motion/axs/[axsName]/functions/extrapola‐
tion/extrapolate-dynamic-source.”
The default setting for selecting dynamic data in “Extrapolation with external
dynamic data” is “Velocity Only”; the user can change this to “Velocity
and acceleration” via the Data Layer path “motion/axs/[axsName]/func‐
tions/extrapolation/extrapolate-external-dynamic-select.”

Use cases for extrapolation:
● Real axis (actual position, actual velocity if configured).
   The extrapolation has to be configured manually and the desired extrapola‐
   tion time entered.
   – Synchronized Motion Commands (e.g. gear-in-pos, gear-in-vel,,,) using
      actual values: Using the SyncSource input parameter with the
      "SYNC_ACTUAL_EXTRAPOLATED" option
   – Changing the sequence of callables in the scheduler and therefore
      manual adjustment of the compensation time
● Encoder axis (encoder position)
   – Extrapolation is automatically selected and an extrapolation time is
      entered
Mathematics in principle:
Extrapolation using actual velocity and acceleration:
● Extrapolated position:
   posextrapolatedt = accactualt / 2 * (kT)2 + velactualt * (kT) + posactualt
                     n            n                     n                   n

● Extrapolated velocity:
   velextrapolatedt = accactualt * (kT) + velactualt
                 n            n                   n

● Extrapolated acceleration:
   accextrapolatedt = accactualt
                     n            n

Extrapolation using external velocity and acceleration:
● Extrapolated position:

● Extrapolated velocity:
   velextrapolatedt = accexternalt * T + velexternalt
                 n                    n-1         n-1

● Extrapolated acceleration:
   accextrapolatedt = accexternalt
                     n                 n-1

T is the fixed system cycle time of the ctrlX CORE, k is the integer number of
cycles, and kT refers to the configured extrapolation time.
Relevant commands:
● getAxisExtrapolatedActValues ⮫ Chapter 7.8.4 AxsGetExtrapolatedActValues
  - Extrapolated axis values on page 779
● AxsSetExtrapolateExternalDynamic ⮫ Chapter 7.8.5 AxsSetExtrapolateExter‐
  nalDynamic - Source for dynamic extrapolation data on page 780

Relevant configuration (Data Layer):
There are 4 configuration parameters per axis:
● "extrapolate-actual" Boolean switch to enable extrapolation
● Extrapolation time "extrapolation-time" (usec, s, ms, min, h)
● setAxisExtrapolateExternalDynamic ⮫ Chapter 7.8.5 AxsSetExtrapolateEx‐
  ternalDynamic - Source for dynamic extrapolation data on page 780
● The default API path is https://<ip-addr>/automation/api/v2/nodes
Data Layer path            Type                       Description
/motion/axs/               bool                       Activation of the extrapo‐
<axs_name>/cfg/                                       lation of actual values
functions/extrapola‐                                  TRUE: Extrapolation
tion/extrapolate-actual                               active

/motion/axs/              double                      Extrapolation time unit
<axs_name>/cfg/                                       depending on setting
functions/extrapola‐
tion/extrapolate-time
/motion/axs/              string                      Unit for the extrapolation
<axs_name>/cfg/                                       time
functions/extrapola‐
tion/extrapolate-time/
<time_unit>
/motion/axs/<name>/cfg/ string                        Source:
functions/extrapola‐                                  "Actual": Actual values of
tion/extrapolate-dynamic-                             the drive
source
                                                      "External": External
                                                      encoder
/motion/axs/<name>/cfg/ string                        Encoder data type:
functions/extrapola‐                                  "Velocity": just velocity
tion/extrapolate-external-
                                                      "VelocityAndAccelera‐
dynamic-select
                                                      tion": Velocity and accel‐
                                                      eration
The effective extrapolation time can be read out in the Data Layer.
Data Layer path            Type                       Description
/motion/axs/               double                     Effective extrapolation
<axs_name>/cfg/func‐                                  time
tions/extrapolation/effec‐
tive-extrapolate-time
/motion/axs/               string                     Unit for the effective
<axs_name>/cfg/func‐                                  extrapolation time
tions/extrapolation/effec‐
tive-extrapolate-time/
<time_unit>
Depending on the respective axis type and the corresponding cycle time, an
internal value is entered as the default value for the extrapolation time. For a
cycle time of 2 ms:
For a virtual axis: 0.002 s
For a real axis:    0.012 s
This value is added to the extrapolation time entered.
Example of a virtual axis with an extrapolation time of 0.1 s:

/motion/axs/<axs_name>/cfg/      TRUE
functions/extrapolation/extrapo‐
late-actual
/motion/axs/<axs_name>/cfg/      0.1 s
functions/extrapolation/extrapo‐
late-time

/motion/axs/<axs_name>/state/       0.102 s
functions/extrapolation/effec‐
tive-extrapolate-time
The extrapolated values for acceleration, position and velocity can be read out
in the Data Layer.
Data Layer path            Type                     Description
/motion/axs/               double                   Extrapolated actual
<axs_name>/state/                                   acceleration
values/extrapolated-
actual/acc
/motion/axs/               double                   Extrapolated actual posi‐
<axs_name>/state/                                   tion
values/extrapolated-
actual/pos
/motion/axs/               double                   Extrapolated actual
<axs_name>/state/                                   velocity
values/extrapolated-
actual/vel
The data source for dynamic extrapolation can be retrieved from the Data
Layer.
Data Layer path           Type                      Description
/motion/axs/              string                    Source for the dynamic
<axs_name>/cfg/                                     extrapolation (velocity
functions/extrapola‐                                and acceleration): Use
tion/extrapolate-dynamic-                           internal dynamics or set
source                                              them via an external
                                                    component. Possible
                                                    values: Actual value/
                                                    external
The dynamic range selected for extrapolation using an external dynamic range
can be viewed in the Data Layer.
Data Layer path            Type                     Description
/motion/axs/               string                   Selecting external
<axs_name>/cfg/                                     dynamic data for extrap‐
functions/extrapola‐                                olation: Extrapolation
tion/extrapolate-external-                          using only external
dynamic-select                                      velocity, or using both
                                                    external velocity and
                                                    acceleration. Possible
                                                    values: Velocity/velocity
                                                    and acceleration

### 6.1.2 Extrapolation for operating mode switching in motion

The ctrlX CORE control unit supports the operation mode switchover of
devices or drives in motion. It is possible to switch between position control,
velocity control and torque control.

To realize this changeover in motion, the required values for position, speed
and torque are automatically extrapolated during the changeover.
The delay time is the time required for a position generated by the control to
be sent to the drive via the field bus and read back again. This delay time has
to be compensated for.
For a ctrlX DRIVE with SoE (EtherCAT with ServoDrive profile) and 2 msec
Motion cycle time:
● Virtual axis: 0.002 sec (1 cycle)
  Real axis: 0.01 sec (5 cycles)
This delay time for the operating mode switchover is calculated automatically
for the axis type.
An individual extrapolation time can also be specified, e.g. when connecting

external drives or when using a specially adapted calculation pipelines for
command value generation.

Relevant configuration (Data Layer):
● Extrapolation time "extrapolation-time" (usec, s, ms, min, h)
Data Layer path          Type                        Description
https://<ip-addr>/       double                      Extrapolation time. Unit
automation/api/v2/                                   depending on setting
nodes/motion/axs/
<axs_name>/cfg/func‐
tions/operation-mode-
switch/extrapolate-time
https://<ip-addr>/       string                      Unit for the extrapolation
automation/api/v2/                                   time
nodes/motion/axs/
<axs_name>/cfg/func‐
tions/operation-mode-
switch/extrapolate-time/
<time_unit>
The effective extrapolation time can be read out in the Data Layer (sum of the
automatically calculated value plus the value entered additively).
Data Layer path           Type                       Description
https://<ip-addr>/        double                     Effective extrapolation
automation/api/v2/                                   time
nodes/motion/axs/
<axs_name>/cfg/func‐
tions/operation-mode-
switch/effective-extrapo‐
late-time
https://<ip-addr>/        string                     Unit for the effective
automation/api/v2/                                   extrapolation time
nodes/motion/axs/
<axs_name>/cfg/func‐
tions/operation-mode-
switch/effective-extrapo‐
late-time/<time_unit>
Depending on the respective axis type and the corresponding cycle time, an
internal value is entered as the default value for the extrapolation time. For a
ctrlX DRIVE with SoE (EtherCAT with ServoDrive profile) and a cycle time of 2
ms:

For a virtual axis: 0.002 s
For a real axis:    0.01 s
A value entered for the extrapolation time is added to this default value.
Example of a real axis with extrapolation time 0.01 s:

... cfg/functions/operation-mode- 0.01 s
switch/extrapolate-time
...                               0.02 s
state/functions/operation-mode-
switch/effective-extrapolate-time
For Rexroth drives and standard calculation pipeline, no additional extrapo‐
lation time is required for the operating mode switchover "in motion". An
incorrect value can result in excessive control deviation in the drive.

### 6.1.3 Measuring probe

The measuring probe accepts the position value of the drive or the exact time
of the measurement and makes it available to the control system. As a rule,
the function is triggered by an external signal at a drive input.
Options:
● Drive encoder position on which the touch probe input is used (S-0-0051,
   S-0-0053)
● Current or commanded (IPO) position of an axis based on a drive time‐
   stamp (S-0-1305.0.2/P-0-2755). In this case, the ctrlX MOTION's touch
   probe function uses the timestamp to interpolate the axis position based
   on the edge time relative to system time and the position values. This
   allows the touch probe input of each drive to be used to detect the posi‐
   tion of each axis (real or virtual)
● Positions within the calculation pipeline of a synchronized axis (derived
   from the timestamp). Z. B.:
   – Incoming master axis position
   – Master axis position based on the master offset
   – Master axis position downstream of the electronic gearbox
● Highly accurate system time: The user can apply S-0-1305.0.2/P-0-2755
   directly if it is needed instead of the axis position.
This can be done with rising, falling or both edges:
● Positive edge (buffered times)
● Negative edge (buffered times)
● Edge value difference (only for SoE)
It is possible to set the expectation window, record marker failure times and
to set the dead time of both edges to compensate for the delay of the rising/
falling signal.
The AxsProbe and AxsProbeAbort commands can only be used with SoE. The
AxsProbeEx and AxsProbeAbortEx commands are available for CoE.
In MOT-V-0118:
−   The input signal supports only the actual position value and the calcula‐
    tion of the edge difference only supports the standard mode
The time can be measured using the AxsProbeEx command. By using the
FINE_TIME signal source, the accuracy of edge detection can be increased, as
shown in ⮫ Further information on page 76.

AxsProbeEx

Timestamps are currently only supported on ctrlX DRIVE with SoE. This func‐
tionality can therefore only be used there.
An expectation window can also be specified. Incorrect measurements can
be recorded. Setting the dead time for both edges reduces the measurement
delay.

Configuration
To configure the function, the following steps are required:
●   Adding probe-related parameters to the cyclic data
●   Assigning probe-related signals to the axis profile
●   Connecting the probe to the corresponding input of the drive
●   Setting the probe parameters in the Data Layer

The configuration of the touch probe in the axis profile is described in
⮫ Chapter 5.9 Touch probe on page 56.

Control via SoE
After mapping, the probe has to be configured in the Data Layer:
motion/axs/<axs_name>/cfg/functions/probe/probe1

−   The selection "FINE_TIME", "IPO_POS", "ACT_POS",
    "MOTION_INTERNAL_DATA" is only supported by ctrlX DRIVE. The
    "ENCODER_1/2" selection is only supported by ctrlX DRIVE and HCS01
−   "selectInfo" selects the signal if "MOTION_INTERNAL_DATA" is used
−   "diffType" is used to calculate the edge difference. The selection includes
    "STANDARD" and "DIFF_DISABLED"
−   "interpType” only supports "LINEAR"

Control via CoE
After mapping, the probe has to be configured in the Data Layer:
motion/axs/<axs_name>/cfg/functions/probe/probe1
The "shortType", "posEdge" and "negEdge" parameters have to be configured
for CoE drives.

  Command overview
  The following control commands support access to the touch probe function‐
  ality:
  ● ⮫ Chapter 7.2.31 AxsProbe - Axis probe on page 478
  ● ⮫ Chapter 7.2.32 GetAxisProbeValues - Read axis probe on page 484
  ● ⮫ Chapter 7.2.33 AxsProbeAbort - Axis probe, abort measurement
    on page 487
  ● ⮫ Chapter 7.2.34 AxsProbeEx - Axis extended probe on page 489
  ● ⮫ Chapter 7.2.35 AxsProbeAbortEx - Abort axis extended probe measure‐
    ment on page 491

  Further information
  ● ⮫ Chapter 5.9 Touch probe on page 56

### 6.1.4 Synchronizing Motion objects

    Introduction
With the help of the SoMO functionality (Synchronization of Motion Objects),
an application can synchronize the buffered commands using internal and
external signals. The functionality signals to the ctrlX MOTION at which point
in the sequence of buffered commands the execution has to be synchronized.
The synchronization of the execution of buffered commands on a Motion
object (axes and kinematics) is implemented with other entities in ctrlX
CORE. The following ctrlX CORE entities can be synchronized with a Motion
object.

● Other Motion objects, see ⮫ Chapter 7.6.1 JoinCmd - Synchronized start of
  Motion objects on page 694
● External instances, see ⮫ Chapter 7.6.2 SetSignalCmd - Synchronization by
  sending signals on page 702
  – PLC (real-time capable)
  – External bundle (real-time capable)
  – Data Layer RT (real-time capable)
  – Script (not real-time capable)
  – Data Layer NRT (not real-time capable)
Motion objects can be synchronized using the ⮫ joinCmd function. The
joinCmd function issues a join command.
Synchronization can be initiated by a Motion object and by an external
instance.
Motion objects can call up the following functions:
● ⮫ Chapter 7.6.2 SetSignalCmd - Synchronization by sending signals
   on page 702
● ⮫ Chapter 7.6.3 SetSignalCmdOpt on page 705
● ⮫ Chapter 7.6.4 ResetSignalCmd - Resetting signals on page 707
● ⮫ Chapter 7.6.5 WaitForSignalCmd - Wait for signal on page 708
● ⮫ Chapter 7.6.6 WaitForSignalResetCmd - Waiting for a signal to be reset
   on page 710
External instances can call up the following functions:
● ⮫ Chapter 7.6.7 SetSignal - Setting a signal at system level on page 712
● ⮫ Chapter 7.6.8 ResetSignal - Resetting a signal at system level
   on page 714
● ⮫ Chapter 7.6.9 GetSignal - Retrieving a signal value at system level
   on page 715
External instances can call up the SetSignal, ResetSignal and GetSignal func‐
tions. The signal functionality can send a signal and continue. The application
can also use this function to implement a "send signal and wait for acknowl‐
edgment".

Restrictions
 All Motion objects and external instances have to be part of the same ctrlX
 CORE. SoMO is not supported for Motion objects or external instances in
 various ctrlX CORE systems.

Examples

Synchronizing a Motion object with an external instance
A "synchronization point" is defined in a Motion object with a sequence of
buffered commands. One or more external instances can wait for this "syn‐
chronization point".
● The Motion object executes its command sequence.
● As soon as the Motion object reaches its "synchronization point", it signals
  "Synchronization point" reached
● The Motion object continues to execute its command sequence.

M1
# All commands are buffered

syncPoint = 1;

AxsMoveAbs(M1, ...)
AxsMoveAbs(M1, ...)

# Signal the PLC that a certain point
# is reached in the sequence
SetSignalCmdOpt(M1, syncPoint);

# Continue the motion
AxsMoveAbs(M1, ...)

                                    1        3

                                2

1 Synchronization point, sends signal to the PLC
2 Axis at standstill in the synchronization point
3 Executes the command immediately and continues

PLC1
# Wait for synchronization point from axis

syncPoint = 1;

IF (GetSignal(syncPoint)) THEN
    # execute subsequent process steps in the PLC
    ...
ENDIF

PLC2
# Wait for synchronization point from axis

syncPoint = 1;

IF (GetSignal(syncPoint)) THEN
    # execute subsequent process steps in the PLC
    ...
ENDIF

Attention: If the motion is not to be stopped by the application, the command
option setSignalCmdOpt has to be used. Only then will the motion not be
stopped at the "synchronization point". The PLCs only receive the information
that the "synchronization point" has been reached. The signal has to be reset,
otherwise the next signal will not work as expected.

Example 2
By linking the examples described, it is then possible to synchronize more
than one Motion object with an external instance.
In the following example, M1 and M2 start their motions synchronously based
on the joinCmd after M1 has received signalOne.

Motion object M1

# Define signal
signalOne = 1;

AxsMoveAbs(M1, ...);

WaitForSignalCmd(M1, signalOne);

#define group
group = {M1, M2};

joinCmd(M1, group);

AxsMoveAbs(M1, ...);

Motion object M2

AxsMoveAbs(M2, ...);

#define group
group = {M1, M2};

joinCmd(M2, group);

AxsMoveAbs(M2, ...);

External instances

# Define signal
signalOne = 1;

SetSignal(signalOne);

Synchronizing an external instance with a Motion object and waiting for acknowledg‐
ment
A "synchronization point" is defined in a Motion object with a sequence of
buffered commands. An external instance can wait for this "synchronization
point" and then acknowledge it.
● The Motion object executes its command sequence.
● When a Motion object reaches its "synchronization point"
  – Signalling to the external instance that the "synchronization point" has
    been reached.
  – Wait for the external instance to acknowledge the signal and thus pre‐
    vent the execution of other commands.
● The Motion object continues to execute its command sequence.

Synchronization point restrictions
An axis standstill is forced at the "synchronization point", as continuous
motion is not supported.

An axis stops and signals the PLC that a gripper is closed during a sequence
of buffered commands and waits with the execution until the gripper is
closed.

M1
# All commands are buffered

# Define signals
signalCloseGripper = 1;
signalGripperClosed = 2;

AxsMoveAbs(M1, ...)
AxsMoveAbs(M1, ...)

# Signal the PLC to close the gripper
# and wait until the gripper is closed
SetSignalCmd(M1, signalCloseGripper)
WaitForSignalCmd(M1, signalGripperClosed)

# Continue the motion
AxsMoveAbs(M1, ...)

                                       1                     3

                                                 2

1 Synchronization point, sends signal to the PLC
2 Axis standstill is executed on the synchronization point and the PLC is
   signalled
3 The PLC sends an acknowledgement signal ®, the command is switched

PLC

# Wait for axis request to close the gripper

# Define signals
signalCloseGripper = 1;
signalGripperClosed = 2;

IF (GetSignalCmd(signalCloseGripper)) THEN
    out.gripperClose = 1;
    # update the internal state of the app
    state = GRIPPER_CLOSING;
ENDIF

# Signal the gripper is closed
IF (state = GRIPPER_CLOSING) AND (in.gripperClosed = 1) THEN
    SetSignal(signalGripperClosed);
    # update the internal state of the app
    state = GRIPPER_CLOSED;
ENDIF
