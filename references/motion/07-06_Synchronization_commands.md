# 7.6 Synchronization commands

### 7.6.1 JoinCmd - Synchronized start of Motion objects

Introduction
The joinCmd is a buffered Motion command and waits until a group of
Motion objects all execute a joinCmd on the same group of Motion objects.
All Motion objects then start the subsequent command at the same time
(synchronized start). A joinCmd has to be specified for each axis or kinematic
that is defined in a "group".
The joinCmd command performs the following steps.
1.    As long as no other command is ready for execution (PREPARED), this
      step remains active. This step is optional and ensures that another com‐
      mand is executed as soon as the join command is set to DONE (see step
      3), which then enables the synchronous start of these commands.
2.    Registration that the Motion object has joined the group.
3.    As soon as all Motion objects have joined the group, they have all
      performed step 2 and the status of all joinCmd commands changes
      to DONE. This takes place in the same execution cycle for all Motion
      objects that execute the joinCmd command after the last Motion object
      has executed step 2. Step 3 is carried out until all Motion objects have
      joined the group.
Result of step 1: There is always a next command for all Motion objects in
the group if step 2 has been executed. All Motion objects start their next
command synchronously in the same cycle.
The number of Motion objects that can be defined for joinCmd is limited to
32.

PLC:

Table 69: ML_JoinCmd
STRUCT ML_JoinCmdData
Name       Data type            Inherited   Address   Initial value   Comment
                                from

  In             ML_iJoinCm                                           Input data
d
  Out            ML_oCmdRe‐                                           Output data of the request
sult
STRUCT ML_iJoinCmd EXTENDS ML_iCmdBase
Name        Data type  Inherited  Address             Initial value   Comment
                       from
  ObjName STRING(15) ML_iCmd‐                                         Motion object name to exe‐
                       Base                                           cute the command
  Source    STRING(50) ML_iCmd‐                                       Specifies the source of the
                       Base                                           command, e.g. PlcApplica‐
                                                                      tion1, is displayed in the
                                                                      diagnostic messages
  SourceLine ULINT              ML_iCmd‐                              Specifies the source line of
                                Base                                  the command, is displayed
                                                                      in the diagnostic messages
 Group           ARRAY[0..31]                                         List of the names of the
                 STRING(15)                                           Motion objects in the join
                                                                      group. Attention: the first
                                                                      empty string in the array
                                                                      refers to the end of the
                                                                      group. Further strings fol‐
                                                                      lowing the empty string are
                                                                      ignored
 SyncStart‐      BOOL                                                 Specifies whether the join
NextCmd                                                               command has to wait for
                                                                      the next available com‐
                                                                      mand to be executed
STRUCT ML_oCmdResult
Name       Data type            Inherited   Address   Initial value   Comment
                                from
  CmdID          ULINT                                                Command ID (is set to
                                                                      18446744073709551615 in
                                                                      the event of an error)
  Error          BOOL                                                 Error flag, TRUE means
                                                                      that an error has occurred
                                                                      (e.g. typing error in the
                                                                      object name)

STRUCT ML_oCmdResult
  ErrorID  ULINT                                                         Specifies the error type.
                                                  The upper four bytes refer
                                                  to the main diagnostics,
                                                  the lower four bytes refer
                                                  to the detailed diagnostics.
                                                  0 indicates “no error”

Data Layer:
Method: POST
URL:                https://<ip-addr>/automation/api/v2/nodes/motion/axs/
<axs_name>/cmd/join
URL:                https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/join
Payload:

{
"type":"object","value":
{
    "group": ["X", "Y"],
    "syncStartNextCmd": false
}
}

Python:

<cmdId> = motion.join(<objName>, group=<groupObjNames>,
sync_start_next_cmd=<syncStartNextCmd>)

● objName
    Motion object name executing the command.
● groupObjNames
    The group of Motion objects that forms the join group. All Motion objects
    in a group have to execute a joinCmd with the same group definition.
● syncStartNextCmd
    If this parameter is TRUE, step 1 (see above) is executed. The Motion
    object only actually joins the group if the next command for the Motion
    object can be executed (is in PREPARED status). The start of the next
    command with other commands of the Motion objects in the group can
    only be ensured if all commands have the status "PREPARED". If SyncStart‐
    NextCmd is FALSE, the Motion object joins the group, even if no other
    command is available or has not yet been prepared. This means that step 1
    of the joinCmd is skipped.
● cmdID
    The returned command identification (can be used to query the state of the
    command, see ⮫ GetCmdState).
If syncStartNextCmd is TRUE, the next command cannot be waitPrepare, as
this leads to a deadlock. WaitPrepare (see ⮫ WaitPrepare) is only prepared
(PREPARED) if the previous command (the joinCmd command) is set to
DONE. The deadlock occurs because the joinCmd command is only set to
DONE when the next command (waitPrepare) is prepared (PREPARED).

The joinCmd command is available in the (real-time capable) bundle interface
(MotionCmdIfT).

BundleIF:

/// @brief Create a command, that blocks the motion execution
///         until all join commands of the given group are also
///         active
/// @param[in]     handle           Handle to the motion
///                                 commands interface
/// @param[in]     sourceInfo       Source info
/// @param[in]     objName          Name of the motion object
/// @param[in]     group            List of names of the motion
///                                 objects in the join group
/// @param[in]     syncStartNextCmd Flag if join command needs
///                                 to wait until there is a

///                                 next command available to
///                                 be executed
/// @param[out] cmdID               The ID of the added command
/// @return                         Status of the function call:
///                                 STS_OK or an error code on
///                                 failure
extern "C" MotionResult MOTION_CORE_joinCmd)(void* handle,
const motion::core::dia::CmdSourceInfo& sourceInfo, const
char* objName, const std::vector<std::string>& group, bool
syncStartNextCmd, uint64_t& cmdID);

Example of a joinCmd:

// Move axes X, Y and Z to position 0.
// Once all axes have reached this position, that is, all 3
// movements have been completed, synchronously start the next
// movement on the X-axis and Y-axis.
// Once the Y-axis has completed its second movement,
// synchronously start a third movement on the Y-axis and
// Z-axis.

using namespace ::motion::core::cmd::axs;

uint64_t cmdId;

// assume dynLimits is a valid
// ::motion::core::cmd::DynamicLimitsT object.

cmdIf->axsPosCmd(cmdIf, {}, "X", AxsCmdType::AXS_CMD_POS_ABS,
0.0, dynLimits, true, cmdId);
cmdIf->axsPosCmd(cmdIf, {}, "Y", AxsCmdType::AXS_CMD_POS_ABS,
0.0, dynLimits, true, cmdId);
cmdIf->axsPosCmd(cmdIf, {}, "Z", AxsCmdType::AXS_CMD_POS_ABS,
0.0, dynLimits, true, cmdId);

std::vector<std::string> joinGroup1 {"X", "Y", "Z"};
cmdIf->joinCmd(cmdIf, {}, "X", joinGroup1, true, cmdId);
cmdIf->joinCmd(cmdIf, {}, "Y", joinGroup1, true, cmdId);
cmdIf->joinCmd(cmdIf, {}, "Z", joinGroup1, false, cmdId);

// The Z-axis is used in the group, because the next movement
// of the X-axis and Y-axis has to start after the Z-axis has
// completed its previous movement.
// There is no next command for axis Z.

// Thus, syncStartNextCmd is set to false.

// When the first movement to zero has been completed on the
// X-axis, Y-axis, and Z-axis, start the next movements
// synchronously.
// X-axis moves from 0 to 8, and Y-axis moves from 0 to 2.

cmdIf->axsPosCmd(cmdIf, {}, "X", AxsCmdType::AXS_CMD_POS_REL,
8.0, dynLimits, true, cmdId);
cmdIf->axsPosCmd(cmdIf, {}, "Y", AxsCmdType::AXS_CMD_POS_REL,
2.0, dynLimits, true, cmdId);

// The Z-axis has to wait until the movement of the Y-axis
// has been completed. Subsequently, synchronously start a
// third movement by the Y-axis and the Z-axis.

std::vector<std::string> joinGroup2 {"Y", "Z"};
cmdIf->joinCmd(cmdIf, {}, "Y", joinGroup2, true, cmdId);
cmdIf->joinCmd(cmdIf, {}, "Z", joinGroup2, true, cmdId);

// The next 2 movements start synchronously when the previous
// movement by the Y-axis has been completed.
// Note that the X-axis is not part of the group.
// The X-axis is still executing its previous movement towards
// position 8.0.
// Y-axis moves from 2 to 5, and Z-axis moves from 0 to -1.

cmdIf->axsPosCmd(cmdIf, {}, "Y", AxsCmdType::AXS_CMD_POS_REL,
3.0, dynLimits, true, cmdId);
cmdIf->axsPosCmd(cmdIf, {}, "Z", AxsCmdType::AXS_CMD_POS_REL,
-1.0, dynLimits, true, cmdId);

If a joinCmd is aborted either by a cancel command or by resetting an error,
this can result in an infinite wait time.
Canceling the join commands
In the "Example of a joinCmd", we consider the first "join" of the X-axis,
Y-axis and Z-axis after their first absolute motions. It is assumed that all
commands have been successfully sent to the axes. If a MINOR error occurs
during the first motion of the Y-axis and this error is reset, all commands on
the Y-axis are canceled, including the join command. However, this does not
affect the execution of join commands by the X-axis and the Z-axis. These join
commands cannot be executed successfully, see ⮫ Chapter 7.2.4 AxsAbort -
Canceling the axis command on page 337. To continue, the X-axis and Z-axis
also have to be canceled.
In the second example, it is not necessary to cancel the commanding of the
axis because no joinCmd has yet been sent to the corresponding axis.

Example of a canceled joinCmd:

// simplified pseudo code

joinCmd(X, {X,Y,Z});
joinCmd(Y, {X,Y,Z});
// Join commands are not completed and remain ACTIVE,

// because no join command for the Z-axis has been commanded.

// Now, assume that an error occurs on the X-axis. The join
// command on the X-axis gets aborted by resetting this error.
// But the join command on the Y-axis continues and is never
// completed. Therefore, the Y-axis has to be aborted.

abortCmd(Y);      // *required*

// Note: no abort on the Z-axis is required.
// The Z-axis did not execute a join for this group.

// Start new join to complete successfully.

joinCmd(X, {X,Y,Z});
joinCmd(Y, {X,Y,Z});
joinCmd(Z, {X,Y,Z});

Therefore, if a join command is unexpectedly not completed, the other join
commands of the other Motion objects in the group should be checked. All
participating join commands that have already been sent have to be canceled.
These join commands are not implicitly canceled by the system. It is recom‐
mended to cancel all participating Motion objects in a join command if an
error occurs.

Example: Synchronization of multiple Motion objects
In the example, the command processing of three axes (Axis1, Axis2, Axis3)
is to be synchronized so that all three axes start a defined motion in the
command sequence at the same time. The command directly after the "syn‐
chronization point" should then be started at the same time.
● All Motion objects execute their command sequence.
● When a Motion object reaches its "synchronization point"
   – In ACTIVE status, wait until the next command is prepared in the com‐
      mand buffer (PREPARED).
   – Signalling that the "synchronization point" has been reached.
   – In ACTIVE status, wait for the remaining Motion objects in the group to
      reach their "synchronization point".
● Once all Motion objects in the group have reached their "synchronization
   point", all objects start their next command in the same cycle.
The following section describes the programs (pseudo code) and the motions
(path-time diagram) of all three axes.

Axis1
# All commands are buffered

AxsMoveAbs(axis1, ...)
AxsMoveAbs(axis1, ...)

#define group
group = {axis1, axis2, axis3};

# Wait until all axes have completed
joinCmd(axis1, group)

# Continue the motion synchronized with the other axes
AxsMoveAbs(axis1, ...)

                                   1                    3

                                             2

1 Synchronization point
2 Axis at standstill in the synchronization point
3 Other axes reach the synchronization point ® the command is switched

Axis2
# All commands are buffered

AxsMoveAbs(axis2, ...)
AxsMoveAbs(axis2, ...)

#define group
group = {axis1, axis2, axis3};

# Wait until all axes have completed
joinCmd(axis2, group)

# Continue the motion synchronized with the other axes
AxsMoveAbs(axis2, ...)

                                     1        3

                                 2

1 Synchronization point
2 Axis at standstill in the synchronization point
3 Other axes reach the synchronization point ® the command is switched

Axis3
# All commands are buffered

AxsMoveAbs(axis3, ...)
AxsMoveAbs(axis3, ...)

#define group
group = {axis1, axis2, axis3};

# Wait until all axes have completed
joinCmd(axis3, group)

# Continue the motion synchronized with the other axes
AxsMoveAbs(axis3, ...)

                                     1                     3

                                                2

1 Synchronization point
2 Axis at standstill in the synchronization point
3 Other axes reach the synchronization point ® the command is switched

### 7.6.2 SetSignalCmd - Synchronization by sending signals

Synchronization by sending and receiving signals

Introduction
Signals can be sent and received as part of a serial command execution or as
a function of an application that is executed asynchronously to the handling
of the command by Motion objects. The signals can be waited for in the
"Standstill" state.
The following properties are defined for signals.
● Signals are defined globally and are specified by an integer value in the
   range from 0 ... 99
● The signal status can be set and reset by commands and using the system
   interface and can be set by a command option
   As a command option, the option is only effective for the next command
● The commands are exclusively buffered commands
● The signal status can be queried via the Data Layer NRT or using the system
   interface. The status can also be queried and set in the Data Layer RT. Each
   signal has an "in" data element and an "out" data element in the Data Layer
   RT. If "in" and "out" are different, the signal is considered "set"
Command interface versus system interface
The ctrlX MOTION command interface is used to set signals and wait for sig‐
nals by executing commands from the command buffer of the Motion objects.
This means that signals are set in the command processing sequence or that
command processing is stopped at the exact point in the sequence until
the signal being waited for has been set externally. Using the ctrlX MOTION
system interface, signals can be controlled without the use of Motion objects.
For example, a PLC task, a script or another program can use the SetSignal
function to set a signal that a Motion object waits for with WaitForSignalCmd
or WaitForSignalResetCmd.

The signal functions do not have a timeout option and no "Cancel" func‐
tions are defined. The system can therefore hang if the signal for a waitFor‐
SignalCmd does not change to active or the signal for waitForSignalResetCmd
does not change to inactive.
It is not recommended to set or reset the signal in order to interrupt the wait‐
ForSignalCmd or waitForSignalResetCmd function, as other instances may
also be waiting for the same signal and could perform an inappropriate action
if the signal is incorrect. This depends on the application.

PLC:

Table 70: ML_SetSignalCmd
STRUCT ML_SignalCmdData
Name       Data type    Inherited          Address        Initial value   Comment
                        from
  In       ML_iSignalC                                                    Input data
           md
  Out      ML_oCmdRe‐                                                     Output data of the request
           sult
STRUCT ML_iSignalCmd EXTENDS ML_iCmdBase
Name        Data type   Inherited  Address                Initial value   Comment
                        from
  ObjName STRING(15) ML_iCmd‐                                             Motion object name exe‐
                        Base                                              cuting the command
  Source    STRING(50) ML_iCmd‐                                           Specifies the source of the
                        Base                                              command, e.g. PlcApplica‐
                                                                          tion1, is displayed in the
                                                                          diagnostic messages
  SourceLine ULINT           ML_iCmd‐                                     Specifies the source line of
                             Base                                         the command, is displayed
                                                                          in the diagnostic messages
  SignalId    UDINT                                                       Signal to be set
STRUCT ML_oCmdResult
Name       Data type         Inherited     Address        Initial value   Comment
                             from
  CmdID       ULINT                                                       Command ID (is set to
                                                                          18446744073709551615 in
                                                                          the event of an error)
  Error       BOOL                                                        Error flag, TRUE means
                                                                          that an error has occurred
                                                                          (e.g. typing error in the
                                                                          object name)

STRUCT ML_oCmdResult
  ErrorID  ULINT                                                        Specifies the error type.
                                                 The upper four bytes refer
                                                 to the main diagnostics,
                                                 the lower four bytes refer
                                                 to the detailed diagnostics.
                                                 0 indicates “no error”

Data Layer:
Setting a Motion-global signal command
Method: POST
URL:                  https://<ip-addr>/automation/api/v2/nodes/motion/axs/
<axs_name>/cmd/set-signal
URL:                  https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/set-signal
Payload:

{
"type":"object","value":
{
"signalId": 0
}
}

Python:

<cmdId> = motion.axs_cmd_set_signal(<objName>,
signal_id=<signalId>)

<cmdId> = motion.kin_cmd_set_signal(<objName>,
signal_id=<signalId>)

● objName
  Motion object name executing the command.
● signalId
  Signal to be set.
● cmdID
  The returned command identification (can be used to query the state of the
  command, see ⮫ GetCmdState)

BundleIF:

/// @brief Create a command, that sets a signal
/// @param[in]   handle       Handle to the motion commands
///                           interface
/// @param[in]   sourceInfo   Source info
/// @param[in]   objName      Motion object on which the
///                           command is executed
/// @param[in]   signalId     The signal to set
/// @param[out] cmdID         Command ID
/// @return                   Status of the function call:
///                           STS_OK or an error code on
///                           failure

extern "C" MotionResult MOTION_CORE_setSignalCmd(void* handle,
const motion::core::dia::CmdSourceInfo& sourceInfo, const
char* objName, uint32_t signalId, uint64_t& cmdID);

### 7.6.3 SetSignalCmdOpt

PLC:

Table 71: ML_SetSignalCmdOpt
STRUCT ML_SetSignalCmdOptData
Name       Data type   Inherited        Address    Initial value   Comment
                       from
  In       ML_iSignalC                                             Input command data of the
           md                                                      command
  Out      ML_oCm‐                                                 Output command data of
           dOptResult                                              the command
STRUCT ML_iSignalCmd EXTENDS ML_iCmdBase
Name        Data type   Inherited  Address         Initial value   Comment
                        from
  ObjName STRING(15) ML_iCmd‐                                      Motion object name exe‐
                        Base                                       cuting the command
  Source    STRING(50) ML_iCmd‐                                    Specifies the source of the
                        Base                                       command, e.g. PlcApplica‐
                                                                   tion1, is displayed in the
                                                                   diagnostic messages
  SourceLine ULINT           ML_iCmd‐                              Specifies the source line of
                             Base                                  the command, is displayed
                                                                   in the diagnostic messages
  SignalId    UDINT                                                Signal to be set
STRUCT ML_oCmdOptResult
Name       Data type  Inherited         Address    Initial value   Comment
                      from
  Error    BOOL                                                    Error flag, TRUE means
                                                                   that an error has occurred
  ErrorID     ULINT                                                Specifies the error type.
                                                                   The upper four bytes refer
                                                                   to the main diagnostics,
                                                                   the lower four bytes refer
                                                                   to the detailed diagnostics.
                                                                   0 indicates “no error”

Data Layer:
Specify a motion-global command option for a signal
The parameter "permType" can assume the values "Once", "PermOn” or
"PermOff”.
Method: POST

URL:                https://<ip-addr>/automation/api/v2/nodes/motion/axs/
<axs_name>/cmd/opt-set-signal
URL:                https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/opt-set-signal
Payload:

{
"type":"object","value":
{
"permType": "Once",
"signalId": 0
}
}

Python:
<cmdId> = motion.axs_cmd_opt_set_signal(<objName>,
perm_type=<permType>, signal_id=<signalId>)

<cmdId> = motion.kin_cmd_opt_set_signal(<objName>,
perm_type=<permType>, signal_id=<signalId>)

● objName
  Motion object name executing the command
● signalId
  Signal to be set
● permType
  Parameter of the command option
  "ONCE" - The command is only executed once
● cmdID
  The returned command identification (can be used to query the state of the
  command, see ⮫ GetCmdState)

BundleIF:

/// @brief Create a command option, that sets a signal
///         within the next "real" command
/// @param[in]    handle        Handle to the motion commands
///                             interface
/// @param[in]    sourceInfo    Source info
/// @param[in]    objName       Motion object on which the
///                             command option is executed
/// @param[in]    signalId      The signal to set
/// @return                     Status of the function call:
///                             STS_OK or an error code on
///                             failure
extern "C" MotionResult MOTION_CORE_setSignalCmdOpt(void*
handle, const motion::core::dia::CmdSourceInfo& sourceInfo,
const char* objName, uint32_t signalId);

### 7.6.4 ResetSignalCmd - Resetting signals

PLC:

Table 72: ML_ResetSignalCmd
STRUCT ML_SignalCmdData
Name       Data type    Inherited         Address      Initial value   Comment

   from
  In       ML_iSignalC                                                 Input data
md
  Out      ML_oCmdRe‐                                                  Output data of the request
sult
STRUCT ML_iSignalCmd EXTENDS ML_iCmdBase
Name        Data type   Inherited  Address             Initial value   Comment
                        from
  ObjName STRING(15) ML_iCmd‐                                          Motion object name exe‐
                        Base                                           cuting the command
  Source    STRING(50) ML_iCmd‐                                        Specifies the source of the
                        Base                                           command, e.g. PlcApplica‐
                                                                       tion1, is displayed in the
                                                                       diagnostic messages
  SourceLine ULINT           ML_iCmd‐                                  Specifies the source line of
                             Base                                      the command, is displayed
                                                                       in the diagnostic messages
  SignalId    UDINT                                                    Signal to be reset
STRUCT ML_oCmdResult
Name       Data type         Inherited    Address      Initial value   Comment
                             from
  CmdID       ULINT                                                    Command ID (is set to
                                                                       18446744073709551615 in
                                                                       the event of an error)
  Error       BOOL                                                     Error flag, TRUE means
                                                                       that an error has occurred
                                                                       (e.g. typing error in the
                                                                       object name)
  ErrorID     ULINT                                                    Specifies the error type.
                                                                       The upper four bytes refer
                                                                       to the main diagnostics,
                                                                       the lower four bytes refer
                                                                       to the detailed diagnostics.
                                                                       0 indicates “no error”

Data Layer:
Resetting a global Motion signal command
Method: POST

URL:               https://<ip-addr>/automation/api/v2/nodes/motion/axs/
<axs_name>/cmd/reset-signal
URL:                https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/reset-signal
Payload:

{
"type":"object","value":
{
"signalId": 0
}
}

Python:
<cmdId> = motion.axs_cmd_reset_signal(<objName>,
signal_id=<signalId>)

<cmdId> = motion.kin_cmd_reset_signal(<objName>,
signal_id=<signalId>)

● objName
  Motion object name executing the command
● signalId
  Signal to be reset
● cmdID
  The returned command identification (can be used to query the state of the
  command, see ⮫ GetCmdState)

BundleIF:

/// @brief Create a command, that resets a signal
/// @param[in]   handle        Handle to the motion commands
///                            interface
/// @param[in]   sourceInfo    Source info
/// @param[in]   objName       Motion object on which the
///                            command is executed
/// @param[in]   signalId      The signal to reset
/// @param[out] cmdID          Command ID
/// @return                    Status of the function call:
///                            STS_OK or an error code on
///                            failure
extern "C" MotionResult MOTION_CORE_resetSignalCmd(void*
handle, const motion::core::dia::CmdSourceInfo& sourceInfo,
const char* objName, uint32_t signalId, uint64_t& cmdID);

### 7.6.5 WaitForSignalCmd - Wait for signal

PLC:

Table 73: ML_WaitForSignalCmd
STRUCT ML_WaitForSignalCmdData
Name       Data type    Inherited         Address       Initial value   Comment
                        from
  In       ML_iWaitFor‐                                                 Input data
           SignalCmd
  Out      ML_oCmdRe‐                                                   Initial data of the request
           sult
STRUCT ML_iWaitForSignalCmd EXTENDS ML_iCmdBase
Name       Data type     Inherited  Address    Initial value            Comment
                         from

  ObjName STRING(15) ML_iCmd‐                                           Motion object name exe‐
    Base                                           cuting the command
  Source   STRING(50) ML_iCmd‐                                          Specifies the source of the
    Base                                           command, e.g. PlcApplica‐
                                                   tion1, is displayed in the
                                                   diagnostic messages
  SourceLine ULINT           ML_iCmd‐                                   Specifies the source line of
        Base                                       the command, is displayed
                                                   in the diagnostic messages
  SignalId  UDINT                                                       Signal to be waited for
  AutoReset BOOL                                                        Indicate whether the signal
                                                   has to be reset
STRUCT ML_oCmdResult
Name       Data type         Inherited    Address       Initial value   Comment
                             from
  CmdID       ULINT                                                     Command ID (is set to
                                                                        18446744073709551615 in
                                                                        the event of an error)
  Error       BOOL                                                      Error flag, TRUE means
                                                                        that an error has occurred
                                                                        (e.g. typing error in the
                                                                        object name)
  ErrorID     ULINT                                                     Specifies the error type.
                                                                        The upper four bytes refer
                                                                        to the main diagnostics,
                                                                        the lower four bytes refer
                                                                        to the detailed diagnostics.
                                                                        0 indicates “no error”

Data Layer:
Waiting for a motion-global signal command.
Method: POST
URL:                  https://<ip-addr>/automation/api/v2/nodes/motion/axs/
<axs_name>/cmd/wait-for-signal
URL:                   https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/wait-for-signal
Payload:

{
"type":"object","value":

{
"signalId": 0,
"autoReset": false
}
}

Python:
<cmdId> = motion.axs_cmd_wait_for_signal(<objName>,
signal_id=<signalId>, auto_reset=<autoReset>)

<cmdId> = motion.kin_cmd_wait_for_signal(<objName>,
signal_id=<signalId>, auto_reset=<autoReset>)

● objName
  Motion object name executing the command
● signalId
  Signal to be waited for
● autoReset
  Indicate whether the signal has to be reset. If TRUE, the signal is automati‐
  cally reset after the waiting time for an active signal has expired
● cmdID
  The returned command identification (can be used to query the state of the
  command, see ⮫ GetCmdState)

BundleIF:

/// @brief Create a command, that blocks the motion execution
///         until a given signal is set (by an other instance)
/// @param[in]    handle        Handle to the motion commands
///                             interface
/// @param[in]    sourceInfo    Source info
/// @param[in]    objName       Motion object on which the
///                             command is executed
/// @param[in]    signalId      The signal to wait for
/// @param[in]    autoReset     Should the signal be reset
///                             afterwards?
/// @param[out] cmdID           Command ID
/// @return                     Status of the function call:
///                             STS_OK or an error code on
///                             failure
extern "C" MotionResult MOTION_CORE_waitForSignalCmd(void*
handle, const motion::core::dia::CmdSourceInfo& sourceInfo,
const char* objName, uint32_t signalId, bool autoReset,
uint64_t& cmdID);

### 7.6.6 WaitForSignalResetCmd - Waiting for a signal to be reset

PLC:

Table 74: ML_WaitForSignalResetCmd
STRUCT ML_WaitForSignalResetCmdData
Name       Data type    Inherited   Address             Initial value   Comment
                        from
  In       ML_iWaitFor‐                                                 Input data
           SignalRe‐
           setCmd
  Out      ML_oCmdRe‐                                                   Initial data of the request
           sult
STRUCT ML_iWaitForSignalResetCmd EXTENDS ML_iCmdBase
Name       Data type     Inherited  Address    Initial value            Comment
                         from

  ObjName STRING(15) ML_iCmd‐                                           Motion object name to exe‐
    Base                                           cute the command
  Source   STRING(50) ML_iCmd‐                                          Specifies the source of the
    Base                                           command, e.g. PlcApplica‐
                                                   tion1, is displayed in the
                                                   diagnostic messages
  SourceLine ULINT           ML_iCmd‐                                   Specifies the source line of
        Base                                       the command, is displayed
                                                   in the diagnostic messages
  SignalId    UDINT                                                     Signal to be waited for
STRUCT ML_oCmdResult
Name       Data type         Inherited    Address       Initial value   Comment
                             from
  CmdID       ULINT                                                     Command ID (is set to
                                                                        18446744073709551615 in
                                                                        the event of an error)
  Error       BOOL                                                      Error flag, TRUE means
                                                                        that an error has occurred
                                                                        (e.g. typing error in the
                                                                        object name)
  ErrorID     ULINT                                                     Specifies the error type.
                                                                        The upper four bytes refer
                                                                        to the main diagnostics,
                                                                        the lower four bytes refer
                                                                        to the detailed diagnostics.
                                                                        0 indicates “no error”

Data Layer:
Waiting for a reset motion global signal command.
Method: POST
URL:                  https://<ip-addr>/automation/api/v2/nodes/motion/axs/
<axs_name>/cmd/wait-for-signal-reset
URL:                   https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/wait-for-signal-reset
Payload:

{
"type":"object","value":
{

"signalId": 0
}
}

Python:
<cmdId> = motion.axs_cmd_wait_for_signal_reset(<objName>,
signal_id=<signalId>)

<cmdId> = motion.kin_cmd_wait_for_signal_reset(<objName>,
signal_id=<signalId>)

● objName
  Motion object name executing the command
● signalId
  Signal to be waited for
● cmdID
  The returned command identification (can be used to query the state of the
  command, see ⮫ GetCmdState)

BundleIF:

/// @brief Create a command, that blocks the motion execution
///         until a given signal is reset (by an other instance)
/// @param[in]    handle       Handle to the motion commands
///                            interface
/// @param[in]    sourceInfo   Source info
/// @param[in]    objName      Motion object on which the
///                            command is executed
/// @param[in]    signalId     The signal to wait for
/// @param[out] cmdID          Command ID
/// @return                    Status of the function call:
///                            STS_OK or an error code on
///                            failure
extern "C" MotionResult
MOTION_CORE_waitForSignalResetCmd(void* handle, const
motion::core::dia::CmdSourceInfo& sourceInfo, const char*
objName, uint32_t signalId, uint64_t& cmdID);

### 7.6.7 SetSignal - Setting a signal at system level

PLC:

Table 75: ML_SetSignal
STRUCT ML_SignalData
Name       Data type              Inherited   Address      Initial value   Comment
                                  from
   In              ML_iSignal                                              Input data
   Out             ML_oState‐                                              Initial data of the request
                   Base

STRUCT ML_iSignal
Name        Data type         Inherited   Address     Initial value   Comment
                              from
  SignalId   UDINT                                                    Signal that has to be set,
                                                                      reset or from which the
                                                                      current status has to be
                                                                      determined
STRUCT ML_oStateBase
Name       Data type          Inherited   Address     Initial value   Comment
                              from
  Error      BOOL                                                     Error flag, TRUE means
                                                                      that an error has occurred

                                                  (e.g. typing error in the
                                                  object name)
  ErrorID    ULINT                                                    Specifies the error type.
                                                  The upper four bytes refer
                                                  to the main diagnostics,
                                                  the lower four bytes refer
                                                  to the detailed diagnostics.
                                                  0 indicates “no error”

Data Layer:
Set (value = TRUE) a signal at system level
Method: PUT
URL:           https://<ip-addr>/automation/api/v2/nodes/motion/state/func‐
tions/somo/signals/<signalId>
Payload:

{"type":"bool8","value": true}

Reaction:

{"type":"bool8","value": true}

Python:
set_signal(signal_id):
  datalayer.write(f'motion/somo/signals/{signal_id}', True)

● signal_id
  Signal to be set.

BundleIF:

/// @brief Set a signal
/// @param[in]   handle        Handle to the motion
///                            system interface
/// @param[in]   signalId      The signal to set
/// @return                    Status of the function call:
///                            STS_OK or an error code on
///                            failure
extern "C" MotionResult MOTION_CORE_setSignal(void* handle,
uint32_t signalId);

### 7.6.8 ResetSignal - Resetting a signal at system level

PLC:

Table 76: ML_ResetSignal
STRUCT ML_GetSignalData
Name       Data type    Inherited           Address      Initial value   Comment
                        from
  In       ML_iSignal                                                    Input data
  Out      ML_oState‐                                                    Initial data of the request
           Base
STRUCT ML_iSignal
Name        Data type          Inherited    Address      Initial value   Comment
                               from
   SignalId        UDINT                                                 Signal that has to be set,
                                                                         reset or from which the
                                                                         current status has to be
                                                                         determined
STRUCT ML_oStateBase
Name       Data type           Inherited    Address      Initial value   Comment
                               from
   Error           BOOL                                                  Error flag, TRUE means
                                                                         that an error has occurred
                                                                         (e.g. typing error in the
                                                                         object name)
   ErrorID         ULINT                                                 Specifies the error type.
                                                                         The upper four bytes refer
                                                                         to the main diagnostics,
                                                                         the lower four bytes refer
                                                                         to the detailed diagnostics.
                                                                         0 indicates “no error”

Data Layer:
Reset (value=FALSE) of a signal at system level
Method: PUT
URL:           https://<ip-addr>/automation/api/v2/nodes/motion/state/func‐
tions/somo/signals/<signalId>
Payload:

{"type":"bool8","value": true}

Reaction:

{"type":"bool8","value": true}

Python:
reset_signal(signal_id):
  datalayer.write(f'motion/somo/signals/{signal_id}', False)

● signal_id
  Signal to be reset.

BundleIF:

/// @brief Reset a signal
/// @param[in] handle         Handle to the motion
///                           system interface

/// @param[in] signalId       The signal to reset
/// @return                   Status of the function call:
///                           STS_OK or an error code on
///                           failure
extern "C" MotionResult MOTION_CORE_resetSignal(void* handle,
uint32_t signalId);

### 7.6.9 GetSignal - Retrieving a signal value at system level

PLC:

Table 77: ML_GetSignal
STRUCT ML_GetSignalData
Name       Data type    Inherited            Address   Initial value   Comment
                        from
  In       ML_iSignal                                                  Input data
  Out      ML_oGet‐                                                    Output data of the request
           Signal
STRUCT ML_iSignal
Name        Data type          Inherited     Address   Initial value   Comment
                               from
  SignalId    UDINT                                                    Signal that has to be set,
                                                                       reset or from which the
                                                                       current status has to be
                                                                       determined
STRUCT ML_oGetSignal EXTENDS ML_oStateBase
Name       Data type    Inherited  Address             Initial value   Comment
                        from
  Error    BOOL         ML_oState‐                                     Error flag, TRUE means
                        Base                                           that an error has occurred
                                                                       (e.g. typing error in the
                                                                       object name)

STRUCT ML_oGetSignal EXTENDS ML_oStateBase
  ErrorID  ULINT        ML_oState‐                                       Specifies the error type.
 Base                                             The upper four bytes refer
                                                  to the main diagnostics,
                                                  the lower four bytes refer
                                                  to the detailed diagnostics.
                                                  0 indicates “no error”
   IsSignalled BOOL                                                      Current signal status

Data Layer:
Retrieving the value of a signal at system level
Method: GET
URL:            https://<ip-addr>/automation/api/v2/nodes/motion/state/func‐
tions/somo/signals/<signalId>
Payload:

{"type":"bool8","value": false}

Python:
get_signal(signal_Id):
  return datalayer.read(f'motion/somo/signals/{signal_id}')

● signal_id
  Signal to be read.

BundleIF:

/// @brief Get the current signal state
/// @param[in]   handle        Handle to the motion
///                            system interface
/// @param[in]   signalId      The signal for which the state
///                            needs to be retrieved
/// @param[out] isSignaled     The current state of the signal
/// @return                    Status of the function call:
///                            STS_OK or an error code on
///                            failure
extern "C" MotionResult MOTION_CORE_getSignal(void* handle,
uint32_t signalId, bool& isSignaled);

Example: Synchronizing a Motion object with an external instance
A "synchronization point" is defined in a Motion object with a sequence of
buffered commands. One or more external instances can wait for this "syn‐
chronization point".
● The Motion object executes its command sequence
● As soon as the Motion object reaches its "synchronization point", it signals
  "Synchronization point" reached
● The Motion object continues to execute its command sequence

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

Example: Synchronizing an external instance with a Motion object and waiting
for acknowledgment

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

                                     1                    3

                                               2

1 Synchronization point, sends signal to the PLC
2 Axis standstill is executed on the synchronization point and the PLC is
   signalled
3 The PLC sends an acknowledgement signal ®, the command is switched

PLC:

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

### 7.6.10 KinSetLocalSignal, KinSetLocalSignalCmdOpt, KinResetLocal‐

Signal, KinWaitForLocalSignal, KinWaitForLocalSignalReset, Set‐
KinLocalSignal, ResetKinLocalSignal, GetKinLocalSignal - Syn‐
chronization by sending local kinematic signals
Introduction
Local kinematic signals can be sent and received either as part of the sequen‐
tial execution of kinematics commands or as a function of an application that
runs asynchronously with respect to the processing of the command by kine‐
matic objects. These local signals can also be waited for while the kinematics
is in the "Standstill" state.
The following properties are defined for signals:

● Local signals are defined separately for each kinematic system and speci‐
    fied by an integer value in the range from 0 to 999
● The status of a local signal can be set and reset using commands and
    via the system interface, and can be configured using a command option.
    When used as a command option, the setting applies only to the next
    command
● The commands are all buffered commands.
● Each local signal is allocated to a bit in the data memory of the Data Layer
    RT. The status of a local signal can be queried via the Data Layer RT or via
    the system interface. The status can also be queried and set in the Data
    Layer RT
Command interface versus system interface

Local signals are specific to kinematic objects. The ctrlX MOTION command
interface is used to set local signals and wait for local signals by executing
commands from the command buffer of the kinematic objects.
This means that local signals are set during the kinematics command proc‐
essing sequence, or that the kinematics command processing is paused at
that exact point in the sequence until the expected local signal has been set
externally.
The ctrlX MOTION system interface allows local signals to be controlled
without using Motion objects. For example, a PLC task, a script, or another
program can use the "SetKinLocalSignal" function to set a local signal that a
kinematic object is waiting for using "KinWaitForLocalSignalCmd" or “KinWait‐
ForLocalSignalResetCmd.”
The local signal functions do not have a timeout option, and no "Cancel"
functions are defined. The system may therefore freeze if the local signal for a
"KinWaitForLocalSignalCmd" does not change to "active" or if the local signal
for "KinWaitForLocalSignalResetCmd" does not change to "inactive."
It is not recommended to set or reset the local signal to cancel the "KinWait‐
ForLocalSignalCmd" or “KinWaitForLocalSignalResetCmd” function as other
instances may also be waiting for the same signal and could perform an incor‐
rect action if the signal is incorrect. This depends on the application.

PLC:

Table 78: ML_KinSetLocalSignal
STRUCT ML_KinLocalSignalCmdData
Name       Data type     Inherited         Address        Initial value   Comment
                         from
  In       ML_iKinLo‐                                                     Input data
           cal‐
           SignalCmd
  Out      ML_oCmdRe‐                                                     Output data of the request
           sult
STRUCT ML_iKinLocalSignalCmd EXTENDS ML_iKinCmdBase
Name        Data type    Inherited  Address    Initial value              Comment
                         from

STRUCT ML_iKinLocalSignalCmd EXTENDS ML_iKinCmdBase
  KinName STRING(63) ML_iKinCmd‐                                          Motion object name exe‐
  Base                                             cuting the command
  Source    STRING(50) ML_iKinCmd‐                                        Specifies the source of the
  Base                                             command, e.g. PlcApplica‐
                                                   tion1, is displayed in the
                                                   diagnostic messages
   SourceLine ULINT              ML_iKinCmd‐                              Specifies the source line of
          Base                                     the command, is displayed
                                                   in the diagnostic messages
   SignalId        UDINT                                                  Signal to be set
STRUCT ML_oCmdResult
Name       Data type             Inherited     Address    Initial value   Comment
                                 from
   CmdID           ULINT                                                  Command ID (is set to
                                                                          18446744073709551615 in
                                                                          the event of an error)
   Error           BOOL                                                   Error flag, TRUE means
                                                                          that an error has occurred
                                                                          (e.g. typing error in the
                                                                          object name)
   ErrorID         ULINT                                                  Specifies the error type.
                                                                          The upper four bytes refer
                                                                          to the main diagnostics,
                                                                          the lower four bytes refer
                                                                          to the detailed diagnostics.
                                                                          0 indicates “no error”

Data Layer:
Setting a local kinematic signal command.
Method: POST
URL:                   https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/set-local-signal
Payload:

{
"type":"object","value":
{
"signalId": 0
}
}

Python:
<cmdId> = motion.kin_cmd_set_local_signal(<kinName>,
signal_id=<signalId>)

● kinName
  Kinematic object name executing the command
● signalId
  Signal to be set
● <cmdID>
  The returned command identification (can be used to query the state of the
  command, see ⮫ GetCmdState)

BundleIF:

/// @brief Create a command, that sets a local signal of
target kinematic

 /// @param[in]     handle       Handle to the motion commands
interface
 /// @param[in]     sourceInfo   Source info
 /// @param[in]     kinName      Kinematic object on which the
command is executed
 /// @param[in]     signalId     The signal to set
 /// @param[out]    cmdID        Command ID
 /// @return                     Status of the function call:
STS_OK or an error code on failure
 extern "C" MotionResult
MOTION_CORE_kinSetLocalSignalCmd(void* handle, const
motion::core::dia::CmdSourceInfo& sourceInfo, const char*
kinName, std::uint32_t signalId, std::uint64_t& cmdID);

PLC:

Table 79: ML_KinSetLocalSignalCmdOpt
STRUCT ML_KinSetLocalSignalCmdOptData
Name       Data type     Inherited  Address             Initial value   Comment
                         from
  In       ML_iKinLo‐                                                   Input data
           cal‐
           SignalCmd
  Out      ML_oCm‐                                                      Output data of the request
           dOptResult
STRUCT ML_iKinLocalSignalCmd EXTENDS ML_iKinCmdBase
Name        Data type    Inherited  Address    Initial value            Comment
                         from
  KinName STRING(63) ML_iKinCmd‐                                        Motion object name exe‐
                         Base                                           cuting the command
  Source    STRING(50) ML_iKinCmd‐                                      Specifies the source of the
                         Base                                           command, e.g. PlcApplica‐
                                                                        tion1, is displayed in the
                                                                        diagnostic messages

STRUCT ML_iKinLocalSignalCmd EXTENDS ML_iKinCmdBase
  SourceLine ULINT       ML_iKinCmd‐                                    Specifies the source line of
  Base                                           the command, is displayed
                                                 in the diagnostic messages
   SignalId        UDINT                                                Signal to be set
STRUCT ML_oCmdResult
Name       Data type             Inherited   Address    Initial value   Comment
                                 from
   Error           BOOL                                                 Error flag, TRUE means
                                                                        that an error has occurred
                                                                        (e.g. typing error in the
                                                                        object name)
   ErrorID         ULINT                                                Specifies the error type.
                                                                        The upper four bytes refer
                                                                        to the main diagnostics,
                                                                        the lower four bytes refer
                                                                        to the detailed diagnostics.
                                                                        0 indicates “no error”

Data Layer:
Specify a command option for a local kinematic signal command.
The "permType" parameter can assume the values "Once" or "PermOff."
Method: POST
URL:                https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/opt-set-local-signal
Payload:

{
"type":"object","value":
{
"permType": "Once",
"signalId": 0
}
}

Python:
<cmdId>=motion.kin_cmd_opt_set_local_signal(<kinName>,
perm_type=<permType>, signal_id=<signalId>)

● kinName
  Kinematic object name executing the command
● signalId
  Signal to be set
● permType
  Parameter of the command option
  "ONCE" - The command is only executed once

BundleIF:

/// @brief Create a command, that sets a local signal of
target kinematic
 /// @param[in]    handle        Handle to the motion commands

interface
 /// @param[in]     sourceInfo    Source info
 /// @param[in]     kinName       Kinematic object on which the
command is executed
 /// @param[in]     signalId      The signal to set
 /// @return                      Status of the function call:
STS_OK or an error code on failure
 extern "C" MotionResult
MOTION_CORE_kinSetLocalSignalCmdOpt(void* handle, const
motion::core::dia::CmdSourceInfo& sourceInfo, const char*
kinName, std::uint32_t signalId);

PLC:

Table 80: ML_KinResetLocalSignal
STRUCT ML_KinLocalSignalCmdData
Name       Data type     Inherited         Address    Initial value   Comment
                         from
  In       ML_iKinLo‐                                                 Input data
           cal‐
           SignalCmd
  Out      ML_oCm‐                                                    Output data of the request
           dOptResult
STRUCT ML_iKinLocalSignalCmd EXTENDS ML_iKinCmdBase
Name        Data type    Inherited  Address    Initial value          Comment
                         from
  KinName STRING(63) ML_iKinCmd‐                                      Motion object name exe‐
                         Base                                         cuting the command
  Source    STRING(50) ML_iKinCmd‐                                    Specifies the source of the
                         Base                                         command, e.g. PlcApplica‐
                                                                      tion1, is displayed in the
                                                                      diagnostic messages
  SourceLine ULINT           ML_iKinCmd‐                              Specifies the source line of
                             Base                                     the command, is displayed
                                                                      in the diagnostic messages
  SignalId    UDINT                                                   Signal to be set
STRUCT ML_oCmdResult
Name       Data type         Inherited     Address    Initial value   Comment
                             from
  Error       BOOL                                                    Error flag, TRUE means
                                                                      that an error has occurred
                                                                      (e.g. typing error in the
                                                                      object name)

STRUCT ML_oCmdResult
  ErrorID  ULINT                                                        Specifies the error type.
                                                 The upper four bytes refer
                                                 to the main diagnostics,
                                                 the lower four bytes refer
                                                 to the detailed diagnostics.
                                                 0 indicates “no error”

Data Layer:
Resetting a local kinematic signal command.
Method: POST
URL:                   https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/reset-local-signal
Payload:

{
"type":"object","value":
{
"signalId": 0
}
}

Python:
<cmdId> = motion.kin_cmd_reset_local_signal(<kinName>,
signal_id=<signalId>)

● kinName
  Kinematic object name executing the command
● signalId
  Signal to be set
● <cmdID>
  The returned command identification (can be used to query the state of the
  command, see ⮫ GetCmdState)

BundleIF:

 /// @brief Create a command, that sets a local signal of
target kinematic
 /// @param[in]     handle       Handle to the motion commands
interface
 /// @param[in]     kinName      Kinematic object on which the
command is executed
 /// @param[in]     signalId     The signal to reset
 /// @return                     Status of the function call:
STS_OK or an error code on failure
 extern "C" MotionResult MOTION_CORE_resetKinLocalSignal
(void* handle, const char* kinName, std::uint32_t signalId);

PLC:

Table 81: ML_KinWaitForLocalSignal
STRUCT ML_KinWaitForLocalSignalCmdData
Name       Data type    Inherited   Address             Initial value   Comment
                        from
  In       ML_iKinWait‐                                                 Input data

ForLocal‐
SignalCmd
  Out      ML_oCm‐                                                      Output data of the request
dOptResult
STRUCT ML_iKinWaitForLocalSignalCmd EXTENDS ML_iKinCmdBase
Name        Data type    Inherited   Address     Initial value          Comment
                         from
  KinName STRING(63) ML_iKinCmd‐                                        Motion object name exe‐
                         Base                                           cuting the command
  Source    STRING(50) ML_iKinCmd‐                                      Specifies the source of the
                         Base                                           command, e.g. PlcApplica‐
                                                                        tion1, is displayed in the
                                                                        diagnostic messages
  SourceLine ULINT           ML_iKinCmd‐                                Specifies the source line of
                             Base                                       the command, is displayed
                                                                        in the diagnostic messages
  SignalId  UDINT                                                       Signal to be set
  AutoReset BOOL                                                        Indicate whether the signal
                                                                        has to be reset
STRUCT ML_oCmdResult
Name       Data type         Inherited     Address      Initial value   Comment
                             from
  CmdID       ULINT                                                     Command ID (is set to
                                                                        18446744073709551615 in
                                                                        the event of an error)
  Error       BOOL                                                      Error flag, TRUE means
                                                                        that an error has occurred
                                                                        (e.g. typing error in the
                                                                        object name)
  ErrorID     ULINT                                                     Specifies the error type.
                                                                        The upper four bytes refer
                                                                        to the main diagnostics,
                                                                        the lower four bytes refer
                                                                        to the detailed diagnostics.
                                                                        0 indicates “no error”

Data Layer:
Waiting for a local kinematic signal command to be issued.
Method: POST

URL:                https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/wait-for-local-signal
Payload:

{
"type":"object","value":
{
"signalId": 0
"autoReset": false
}
}

Python:
<cmdId> = motion.kin_cmd_wait_for_local_signal(<kinName>,
signal_id=<signalId>, auto_reset=<autoReset>)

● kinName
  Kinematic object name executing the command
● signalId
  Signal to be waited for
● autoReset
  Indicate whether the signal has to be reset. If TRUE, the signal is automati‐
  cally reset after the waiting time for an active signal has expired
● <cmdID>
  The returned command identification (can be used to query the state of the
  command, see ⮫ GetCmdState)

BundleIF:

 /// @brief Create a command, that blocks the motion execution
until a given local signal of target kinematic is set (by an
other instance)
 /// @param[in]     handle        Handle to the motion commands
interface
 /// @param[in]     sourceInfo    Source info
 /// @param[in]     kinName       Kinematic object on which the
command is executed
 /// @param[in]     signalId      The local signal to wait for
 /// @param[in]     autoReset     Should the signal be reset
afterwards?
 /// @param[out]    cmdID         Command ID
 /// @return                      Status of the function call:
STS_OK or an error code on failure
 extern "C" MotionResult MOTION_CORE_kinWaitForLocalSignalCmd
(void* handle, const motion::core::dia::CmdSourceInfo&
sourceInfo, const char* kinName, std::uint32_t signalId, bool
autoReset, std::uint64_t& cmdID);

PLC:

Table 82: ML_KinWaitForLocalSignalReset
STRUCT ML_KinWaitForLocalSignalResetCmdData
Name       Data type    Inherited    Address            Initial value   Comment
                        from
  In       ML_iKinWait‐                                                 Input data

ForLocal‐
SignalRe‐
setCmd
  Out      ML_oCm‐                                                      Output data of the request
dOptResult
STRUCT ML_iKinWaitForLocalSignalResetCmd EXTENDS ML_iKinCmdBase
Name         Data type   Inherited    Address    Initial value Comment
                         from
  KinName STRING(63) ML_iKinCmd‐                               Motion object name exe‐
                         Base                                  cuting the command
  Source     STRING(50) ML_iKinCmd‐                            Specifies the source of the
                         Base                                  command, e.g. PlcApplica‐
                                                               tion1, is displayed in the
                                                               diagnostic messages
  SourceLine ULINT       ML_iKinCmd‐                           Specifies the source line of
                         Base                                  the command, is displayed
                                                               in the diagnostic messages
  SignalId   UDINT                                             Signal to be set
STRUCT ML_oCmdResult
Name       Data type         Inherited    Address       Initial value   Comment
                             from
  CmdID       ULINT                                                     Command ID (is set to
                                                                        18446744073709551615 in
                                                                        the event of an error)
  Error       BOOL                                                      Error flag, TRUE means
                                                                        that an error has occurred
                                                                        (e.g. typing error in the
                                                                        object name)
  ErrorID     ULINT                                                     Specifies the error type.
                                                                        The upper four bytes refer
                                                                        to the main diagnostics,
                                                                        the lower four bytes refer
                                                                        to the detailed diagnostics.
                                                                        0 indicates “no error”

Data Layer:
Waiting for a local kinematics signal command to reset.
Method: POST
URL:                    https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/wait-for-local-signal-reset

Payload:

{
"type":"object","value":
{
"signalId": 0
}
}

Python:
<cmdId>=motion.kin_cmd_wait_for_local_signal_reset(<kinName>,
signal_id=<signalId>)

● kinName
  Kinematic object name executing the command
● signalId
  Signal to be waited for
● <cmdID>
  The returned command identification (can be used to query the state of the
  command, see ⮫ GetCmdState)

BundleIF:

 /// @brief Create a command, that blocks the motion execution
until a given local signal of target kinematic is set (by an
other instance)
 /// @param[in]     handle       Handle to the motion commands
interface
 /// @param[in]     sourceInfo   Source info
 /// @param[in]     kinName      Kinematic object on which the
command is executed
 /// @param[in]     signalId     The local signal to wait for
 /// @param[out]    cmdID        Command ID
 /// @return                     Status of the function call:
STS_OK or an error code on failure.
 extern "C" MotionResult
MOTION_CORE_kinWaitForLocalSignalResetCmd (void* handle,
const motion::core::dia::CmdSourceInfo& sourceInfo, const
char* kinName, std::uint32_t signalId, bool autoReset,
std::uint64_t& cmdID);

PLC:

Table 83: ML_SetKinLocalSignal
STRUCT ML_KinLocalSignalData
Name       Data type     Inherited          Address       Initial value   Comment
                         from

STRUCT ML_KinLocalSignalData
  In       ML_iKinLo‐                                                  Input data
calSignal
  Out      ML_oState‐                                                  Output data of the request
Base
STRUCT ML_iKinLocalSignal
Name        Data type     Inherited Address            Initial value   Comment
                          from
  KinName STRING(63) ML_iKinCmd‐                                       Motion object name exe‐
                          Base                                         cuting the command
  SignalId  UDINT                                                      Signal to be set

STRUCT ML_oStateBase
Name       Data type          Inherited   Address      Initial value   Comment
                              from
  Error      BOOL                                                      Error flag, TRUE means
                                                                       that an error has occurred
                                                                       (e.g. typing error in the
                                                                       object name)
  ErrorID    ULINT                                                     Specifies the error type.
                                                                       The upper four bytes refer
                                                                       to the main diagnostics,
                                                                       the lower four bytes refer
                                                                       to the detailed diagnostics.
                                                                       0 indicates “no error”

Data Layer:
Set a local signal at system level (value = TRUE).
Method: POST
URL:      https://<ip-addr>/automation/api/v2/nodes/motion/kin/<kin_name>/
functions/somo/rt-data/data/<signalId>
Payload:

{"type":"bool8","value": true}

Reaction:

{"type":"bool8","value": true}

Python:

● kinName
  Kinematic object name executing the command
● signalId
  Signal to be set
● set_signal(kinName, signal_id):
  datalayer.write(f'motion/kin/kinName/somo/signals/{signal_id}', True)

BundleIF:

/// @brief Set a local signal of target kinematic
 /// @param[in]     handle       Handle to the motion commands
interface
 /// @param[in]     kinName      Kinematic object on which the
command is executed
 /// @param[in]     signalId     The signal to set
 /// @return                     Status of the function call:
STS_OK or an error code on failure
 extern "C" MotionResult MOTION_CORE_setKinLocalSignal (void*
handle, const char* kinName, std::uint32_t signalId);

PLC:

Table 84: ML_ResetKinLocalSignal
STRUCT ML_KinLocalSignalData
Name       Data type     Inherited           Address        Initial value   Comment
                         from
  In       ML_iKinLo‐                                                       Input data
           calSignal
  Out      ML_oState‐                                                       Output data of the request
           Base
STRUCT ML_iKinLocalSignal
Name        Data type     Inherited Address                 Initial value   Comment
                          from
  KinName STRING(63) ML_iKinCmd‐                                            Motion object name exe‐
                          Base                                              cuting the command
  SignalId  UDINT                                                           Signal to be set
STRUCT ML_oCmdResult
Name       Data type           Inherited     Address        Initial value   Comment
                               from
   Error           BOOL                                                     Error flag, TRUE means
                                                                            that an error has occurred
                                                                            (e.g. typing error in the
                                                                            object name)
   ErrorID         ULINT                                                    Specifies the error type.
                                                                            The upper four bytes refer
                                                                            to the main diagnostics,
                                                                            the lower four bytes refer
                                                                            to the detailed diagnostics.
                                                                            0 indicates “no error”

Data Layer:
Reset a local signal at system level (value = FALSE).
Method: POST

URL:      https://<ip-addr>/automation/api/v2/nodes/motion/kin/<kin_name>/
functions/somo/rt-data/data/<signalId>
Payload:

{"type":"bool8","value": false}

Reaction:

{"type":"bool8","value": false}

Python:

● kinName
  Kinematic object name executing the command
● signalId
  Signal to be set
● get_signal (kinName, signal_id):
  return datalayer.read(f'motion/ kin/kinName /somo/signals/{signal_id}')

BundleIF:

 /// @brief Get the current local signal state of target
kinematic
 /// @param[in]     handle       Handle to the motion commands
interface
 /// @param[in]     kinName      Kinematic object on which the
command is executed
 /// @param[in]     signalId     The signal to set
 /// @param[out]    isSignaled   The current state of the
signal
 /// @return                     Status of the function call:
STS_OK or an error code on failure
 extern "C" MotionResult MOTION_CORE_getKinLocalSignal (void*
handle, const char* kinName, std::uint32_t signalId , bool&
isSignaled);

PLC:

Table 85: ML_GetKinLocalSignal
STRUCT ML_GetKinLocalSignalData
Name       Data type    Inherited         Address       Initial value   Comment
                        from
  In       ML_iKinLo‐                                                   Input data
           calSignal
  Out      ML_oGetKin‐                                                  Output data of the request
           LocalSignal

STRUCT ML_iKinLocalSignal
Name        Data type     Inherited Address               Initial value   Comment
                          from
  KinName STRING(63) ML_iKinCmd‐                                          Motion object name exe‐
                          Base                                            cuting the command
  SignalId  UDINT                                                         Signal to be set
STRUCT ML_oGetKinLocalSignal EXTENDS ML_oStateBase
Name       Data type    Inherited   Address     Initial value             Comment
                        from
  Error    BOOL                                                           Error flag, TRUE means
                                                                          that an error has occurred
                                                                          (e.g. typing error in the
                                                                          object name)
   ErrorID         ULINT                                                  Specifies the error type.
                                                                          The upper four bytes refer
                                                                          to the main diagnostics,
                                                                          the lower four bytes refer
                                                                          to the detailed diagnostics.
                                                                          0 indicates “no error”
   IsSignalled BOOL

Data Layer:
Retrieve the value of a signal at system level.
Method: GET
URL:      https://<ip-addr>/automation/api/v2/nodes/motion/kin/<kin_name>/
functions/somo/rt-data/data/<signalId>
Payload:

{"type":"bool8","value": false}

Python:

● kinName
  Kinematic object name executing the command
● signalId
  Signal to be set
● get_signal (kinName, signal_id):
  return datalayer.read(f'motion/ kin/kinName /somo/signals/{signal_id}')

BundleIF:

 /// @brief Get the current local signal state of target
kinematic
 /// @param[in]     handle       Handle to the motion commands
interface
 /// @param[in]     kinName      Kinematic object on which the
command is executed
 /// @param[in]     signalId     The signal to set
 /// @param[out]    isSignaled   The current state of the
signal
 /// @return                     Status of the function call:
STS_OK or an error code on failure

 extern "C" MotionResult MOTION_CORE_getKinLocalSignal (void*
handle, const char* kinName, std::uint32_t signalId , bool&
isSignaled);
