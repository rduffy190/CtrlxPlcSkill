# 7.1 General information

Overview
In case of different motion commands of the kinematics, it can be specified
whether they are issued as buffered or unbuffered.
Amongst others, this affects these commands:
● MoveLinAbs ⮫ Chapter 7.3.4 KinMoveLinAbs - Absolute traversing of kine‐
  matics on page 524
● MoveLinRel ⮫ Chapter 7.3.5 KinMoveLinRel - Relative traversing of kine‐
  matics on page 528

● MoveDirectAbs ⮫ Chapter 7.3.6 KinMoveDirectAbs - Direct absolute tra‐
  versing of kinematics on page 532
● MoveDirectRel ⮫ Chapter 7.3.7 KinMoveDirectRel - Direct relative traversing
  of kinematics on page 535
● MoveDirectAsyncAbs ⮫ Chapter 7.3.8 KinMoveDirectAsyncAbs - Direct asyn‐
  chronous absolute traversing of kinematics on page 538
● MoveDirectAsyncRel ⮫ Chapter 7.3.9 KinMoveDirectAsyncRel - Direct asyn‐
  chronous relative traversing of kinematics on page 543

Buffered motion commands
Buffered motion commands are subsequently (in the order of commanding)
entered in a buffer. The commands in this buffer are prepared for execution
in a lower-priority task (i.e. whenever the control is "ready"). This type of
preparation does not have any impact on the time-critical control tasks.
Whenever processing of a command is completed, the control retrieves
the next command from the buffer and executes the command. If time is
remaining in the current Motion cycle, the second command usually starts in
the same cycle in which the first command was completed. Thus, command
sequences can efficiently be commanded and executed. The conditions with
regard to time during commanding (e.g. in a script) are completely decoupled
from the execution of the command. Consequently, they cannot negatively
influence the processing time.

Unbuffered motion commands
Unbuffered motion commands are always used when an external event invalid‐
ates the previously commanded motion. This could occur, for example, when a
vision system provides new target coordinates that are now to be approached
without interruption. Whenever an unbuffered motion command is issued, a
high-priority task is activated to prepare for this command. In this task, the
command is prepared for execution as quickly as possible. The currently active
command continues to be executed. As soon as the unbuffered command
preparation has been completed, the command becomes active. It replaces
the previously active command which is assigned the state ABORTED, see
⮫ Chapter 7.8.7 GetCmdState - Command states on page 787. As the entire
command buffer becomes invalid, the buffer has to be discarded. The com‐
mands contained in the buffer are also assigned the state ABORTED.
The unbuffered command starts its interpolation but has to synchronize to
the current state of the axes (that are still in motion by the interrupted
command). Synchronization takes place by complying with the dynamic limit
values of the axes (if required, reduced by the kinAxsDynLim, see ⮫ Chapter

### 7.5.6 KinAxsDynLimP - Decreasing dynamic limits of the kinematic axis using

a command on page 660). The more dynamic is available, the earlier the
kinematic moves along the path specified in the unbuffered command again.
The command is completed (state DONE) once the synchronization is com‐
pleted and the commanded target position is reached. The motion dynamic
used for synchronization can also be reduced by the override, see ⮫ Chapter
7.7.3 SetOverride - Override on page 739 and ⮫ Chapter 7.7.5 SetAccOverride,
GetAccOverride - Acceleration override on page 744.
As each axis synchronizes independently from the other axes to the original,
programmed path, the resulting motion can be similar to a MoveDirectAsync,
see ⮫ Chapter 7.3.8 KinMoveDirectAsyncAbs - Direct asynchronous absolute
traversing of kinematics on page 538 and ⮫ Chapter 7.3.9 KinMoveDirectAsyn‐
cRel - Direct asynchronous relative traversing of kinematics on page 543 in
case of a low reserve of the axis dynamics.

Unbuffered commands can interrupt buffered as well as unbuffered com‐
mands. If many unbuffered commands are issued subsequently, the future
commands overwrite the previous commands. The last unbuffered command
wins. Depending on the time-dependent behavior, an overwritten command
sporadically becomes active for several cycles (if the last command is being
prepared).
The additional motion for the synchronization process is only triggered once
the unbuffered command becomes active. Thus, the motion can only be esti‐
mated during the preparation. Consequently, functions calculated during the
preparation result in incorrect results.
Amongst others, this affects:
● Monitoring the working areas and safe zones ⮫ Chapter 7.5.9 KinSafeAreaP
    - Working areas/safe zones on page 672

● Time until end of command ⮫ Chapter 7.8.1 AxsGetIpoAddData - Additional
    axis data on page 772 and ⮫ Chapter 7.8.2 KinGetIpoAddData - Additional
    kinematic data on page 774
The estimation in the preparation calculates additional motion for synchroni‐
zation but cannot return a result that is 100% correct.
It is recommended to use buffered commands when possible. The unbuffered
commands have a major impact on the temporal behavior of the system and
can result in considerable delays of other tasks. In the worst case, this
can negatively influence the real-time behavior of the control. Additionally,
a sequence of commands can be executed faster if it is commanded as a
sequence of buffered commands.

Operating principles of commands
Axis commands can be processed as unbuffered and as buffered. Kinematic
commands are generally processed as buffered (for more details about buf‐
fered and unbuffered kinematic commands, see above).
In case of buffered commands, only the task to execute an action is trig‐
gered. The action itself is carried out at a later time. To do this, the com‐
mand is placed in the so-called command buffer. This command buffer works
according to the FIFO principle (First In First Out). Commands are executed in
the order in which they were commanded. Preparation is required before the
command can be executed. All relevant data is calculated to ensure efficient
execution and interpolation. This preparation can take several Motion cycles
depending on the system load. If a command is prepared, it can be executed.
In case of unbuffered commands, processing is started directly after suc‐
cessful issuing of the command. The currently active command is canceled.
If previously, there have been buffered commands in the buffer, these com‐
mands are discarded. Unbuffered commands generally do not use the com‐
mand buffer.
As the preparation takes place in real-time context in case of unbuffered com‐
mands, the computation time is increased (always during commanding). In
the worst case, the Motion kernel cannot provide the new command values
in time and the watchdog triggers during monitoring of the real-time. In this
case, the command should be executed as a buffered command or the cycle
time of the Motion task should be increased.
Moreover, additional commands are available. These commands are executed
immediately after issuing the command but they do not discard the command
buffer. The interrupt-continue mechanism or the override change are part of
these commands, see ⮫ Chapter 7.2.7 AxsInterrupt - Interrupting the axis
command on page 346, ⮫ Chapter 7.3.15 KinInterrupt, KinInterrupt2 - Inter‐
rupting the kinematic command on page 577, ⮫ Chapter 7.2.8 AxsContinue
- Continuing the axis command on page 348, ⮫ Chapter 7.3.16 KinContinue

- Continuing the kinematic command on page 583 or changing the override,
see ⮫ Chapter 7.7.3 SetOverride - Override on page 739 and ⮫ Chapter 7.7.5
SetAccOverride, GetAccOverride - Acceleration override on page 744.

Command state

The command state indicates the processing step of the command in relation
to the command buffer. A command can be in one of the following states:
State           Meaning
CREATED         The command was issued and the command parameters
                have to be verified
INBUFFER        The command was issued successfully and is written to the
                command buffer.
PREPARED        The command preparation has been completed and the
                command waits for activation.
ACTIVE          The command is active and is currently being processed
DONE            The command processing has been completed, the target
                state has been reached

State             Meaning
ABORTED           The command was aborted, but the target state was not
                  reached. This status does not imply that the command has
                  ever been active.
OUTDATED          There is no information available anymore on this command
                  in the system

Command buffer
The command buffer is only active for buffered commands. Each axis and
each kinematic system has its own command buffer. There is no interaction
between the command buffers of different axes and kinematics. The size
of the command buffer influences how many application commands can be

entered into ctrlX MOTION. If the buffer is full, commands first have to be
processed before new commands are sent. As each command requires RAM,
the size of the command buffer is limited to 30 commands for axes and 100
commands for kinematics. This value can be modified at any time via the
configuration of the kinematics and takes effect immediately. This can be done
either by writing in the Data Layer or via the kinematic configuration dialogs.
Data Layer URL: motion/kin/<kin-name>/cfg/prep-limits/max-cmds-in-
buffer
Actions: READ, WRITE
Type: uint64
A large command buffer is desirable for two different reasons:
● Avoiding errors if the execution of the commands takes less time than the
  preparation
  In some applications, the motions of the commands are very short and the
  dynamics are very high. This can result in the processing time of such com‐
  mands taking only a few milliseconds. If the preparation of the buffered
  commands takes longer than the execution, sporadically, a command has
  been processed and the next command should become active but has not
  been prepared completely. If this happens in a sequence with a continuous
  velocity profile and tangential path transitions, the system generates an
  error and the kinematics are stopped as part of the error reaction.
  If a large command buffer is available and sufficient commands are speci‐
  fied in good time, the preparation can completely prepare many of these
  commands while long commands are executed. This creates a buffer of
  completely prepared commands that can bridge sections of the application
  in which the processing of the commands requires less time than their
  preparation. As long as the command buffer is never completely empty, the
  system does not generate an error.
● Preview of subsequent commands as part of the preparation
  Various functions in the ctrlX MOTION require information from the fol‐
  lowing commands. An illustrative example of this is the PolyTrans com‐
  mand option (see also ⮫ Chapter 7.5.8 KinPolyTransP - Command options
  for kinematics - Path rounding with polynomial on page 667). This com‐
  mand option rounds off two consecutive motions. For this reason, geom‐
  etry data is required for both motion commands.
  Some functions (e.g. command option "⮫ Chapter 7.5.7 KinContMotionP
  - Continuous motion across several commands on page 664") require an
  even greater look-ahead than only 2 commands. The exact number of com‐
  mands required for this results from the commanded dynamics and the
  path length of the subsequent commands.

   In addition, the look-ahead can also be recursive (depending on the speci‐
   fied commands and command options). The command buffer has to be at
   least large enough to ensure that a complete look-ahead is possible when
   preparing a command.
   The ctrlX MOTION generates a warning if the command buffer is too small
   for the look-ahead and gives a recommendation for a sensible size.
However, a very large command buffer means that less memory is available to
the rest of the system, which can have a negative impact on the performance
and stability of the overall system.

Further information
● ⮫ Chapter 7.8.7 GetCmdState - Command states on page 787

Command identification
If a command is issued successfully, a command ID is assigned. The command
status can be queried via this command ID.

Command status query
The Motion object (axis name/kinematic name) as well as the cmdID have to
be specified for each function. The function returns the command status.
Data Layer URL: https://<ip-addr>/automation/api/v2/nodes/motion/axs/
<axs_name>/state/cmd-state    bzw.    https://<ip-addr>/automation/api/v2/
nodes/motion/kin/<kin_name>/state/cmd-state
PLC function: CXA_MotionLibrary.ML_GetCmdState
Python-Funktion: motion.get_cmd_state
BundleIF: MotionSysIfT.getCmdState

Interface overview
Commands can be issued via different interfaces. All commands are provided
via all interfaces. The interfaces have different properties with regard to the
parameters and the time sequence of commands.
● PLC
  The commands can be issued via the Motion PLC library. The Motion object
  as well as the command parameters have to be transmitted to the function
  blocks. This method can be used in real-time.
● ctrlX Data Layer
  The commands can be issued via the REST interface. The Motion object
  to be commanded is selected in the URL of the call. The payload only com‐
  prises the command parameters. This method cannot be used in real-time.
● Bundle interface
  The commands can be directly issued via the command interface of the
  celix ctrlX MOTION bundle. All parameters such as Motion object and com‐
  mand properties have to be transmitted in the programming language C in
  a call. This method can be used in real-time.
● Script
  The commands can be issued via a script interpreter. Bosch Rexroth pro‐
  vides an interpreter for the programming language Python. The interpreter
  interprets the command and sends it to ctrlX MOTION. This method cannot
  be used in real-time.

Restriction of dynamic limit values
Dynamic limit values can be specified both in motion commands for individual
axes and in motion commands for kinematics. These are always limited by the
configured dynamic limit values of the axis or kinematics.
In addition, ctrlX MOTION limits the dynamic limits for acceleration, decelera‐
tion and jerk as follows:
● The acceleration is reduced so that the maximum velocity is reached in one
   cycle from standstill, if it is not already lower
● The deceleration is reduced so that standstill is reached from the maximum
   velocity in one cycle if it is not already lower
● The jerk is reduced so that the maximum acceleration/deceleration is
   reached in one cycle, if it is not already smaller

This behavior prevents extremely large values for acceleration, deceleration
and jerk, which would otherwise lead to large rounding errors in subsequent
calculations (in most cases (with sensible limit values), this limitation should
have no effect).

Example of an effective limit:
● Configured dynamic limits:
   – Velocity 1000 mm/min
   – Acceleration & deceleration 4 m/s²
   – Jerk 5000 m/s³
● Commanded dynamic limits:
   – Velocity 500 mm/min
   – Acceleration & deceleration 8 m/s²
   – Jerk 5000 m/s³
In the first stage, all dynamic limits are set to the minimum configuration and
command.
● Effective dynamic limits in level 1:
   – Velocity 500 mm/min (from commanding)
   – Acceleration & deceleration 4 m/s² (from configuration)
   – Jerk 5000 m/s³ (from command/configuration)
In a second stage, acceleration, deceleration and jerk are adjusted so that
the maxima are reached within one cycle. A Motion cycle of 2 milliseconds is
assumed for this example.
● Velocity 500 mm/min == 0.5 m/min == 0.008333 m/s
● Acceleration & deceleration 0.008333 m/s / 0.002 s = 4.1666 m/s² (max‐
  imum velocity in one cycle is reached with acceleration 4.1666 m/s²) →
  This is greater than the limit of the configuration. Thus, the limit value of
  the configuration is used
● Jerk 4 m/s² / 0.002 s = 2000 m/s³ (maximum acceleration/deceleration in
  one cycle is achieved with a jerk of 2000 m/s³) → This is less than the
  limit of the command/configuration. Thus, the new limit value is used
During the motion, these dynamic limit values are active:
● Velocity 500 mm/min (from commanding)
● Acceleration & deceleration 4 m/s² (from configuration)
● Jerk 2000 m/s³ (from the limit with which the maximum accelera‐
  tion/deceleration is reached within a cycle)
