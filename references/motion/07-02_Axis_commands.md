# 7.2 Axis commands

### 7.2.1 Overview

Processing axis commands
Axis commands can be processed as unbuffered and as buffered. This proc‐
essing type can be specified via a parameter in the axis commands. By
default, axis commands are processed as unbuffered.
There are exceptions for particular commands which can exclusively be proc‐
essed as unbuffered. This includes, for example:
●   Override
●   Abort
●   Interrupt
●   Continue

Special features
If an unbuffered command replaces an active command, the active command
reports state ABORTED.
If several unbuffered commands are issued in a cycle, only the last command
is active and reports state ACTIVE. All other issued commands report state
ABORTED.
If an unbuffered command is issued and if there are still commands in
the command buffer, these commands are discarded and report the state
ABORTED.

Single-axis commands
The following single axis commands are implemented:
●   AxsPower
●   AxsReset
●   AxsAbort
●   AxsStop
●   AxsInterrupt
●   AxsContinue
●   AxsVelocity
●   AxsPosAbs
●   AxsPosRel
●   AxsPosAdd
●   AxsJogIncr
●   AxsJobCont
●   CyclicSetPoint

Synchronization commands
The following synchronized Motion commands have been implemented
●   AxsGearInPos
●   AxsGearInPosEx
●   AxsGearInPos2
●   AxsGearInPos2Ex
●   GearInVel
●   AxsCamIn
●   AxsFlexProfile

### 7.2.2 AxsPower - Axis power

Basics
This command adds power to the axis. This function is the prerequisite for
every motion, acceleration or deceleration.
It is not differentiated between real and simulated axes. The function imple‐
ments the transition between the states DISABLED and STANDSTILL.
After the axis has been enabled or disabled, the command is set to DONE
and the PLCOpen status of the axis changes to the commanded state (DIS‐
ABLED/STANDSTILL). If the command is active, the PLCOpen state of the
axis is STANDSTILL_PENDING. The command waits until the power is actually
available. Only then does the axis state change to STANDSTILL.
During the transition from DISABLED to STANDSTILL, the status of the com‐

mand value processing is evaluated in the drive status word. This status has to
be set to achieve the STANDSTILL state. (Drive status word bit 3, drive follows
command values)
ML_AxsGetPLCOpenState or ML_GetCmdState can be used to read the status.
If an error occurs during execution, the axis is set to state ERRORSTOP.
This command is an unbuffered command, i.e. the previously active command
is canceled, the commands of the preparation buffer are discarded.

PLC:

ML_AxsPower
Name        Data type        Inherited    Address       Initial value   Comment
                             from
  Data       ML_AxsPo‐                                                  Output: Command parame‐
             werData                                                    ters
  ML_Axs‐    BOOL                                                       Returns information
Power                                                                   whether the command can
                                                                        be added to the axis
                                                                        object.
                                                                        ● TRUE: The command
                                                                          could be added success‐
                                                                          fully
                                                                        ● FALSE: An error
                                                                          occurred. Details in
                                                                          ML_oCmdResult
STRUCT ML_AxsPowerData
Name       Data type   Inherited          Address       Initial value   Comment
                       from
  In       ML_iAxs‐                                                     Input: Command data of
           Power                                                        the command
  Out      ML_oCmdRe‐                                                   Output: Command parame‐
           sult                                                         ters

STRUCT ML_iAxsPower EXTENDS ML_iAxsCmdBase
Name        Data type   Inherited  Address                Initial value   Comment
                        from
  AxisName STRING(63) ML_iAxsCmd‐                                         Name of the axis used to
                        Base                                              execute the command
  Source    STRING(50) ML_iAxsCmd‐                                        Specifies the command
                        Base                                              source, e.g PlcApplication1
                                                                          is displayed in the diag‐
                                                                          nostic messages
   SourceLine ULINT              ML_iAxsCmd‐                              Specifies the source line of
                                 Base                                     the command; is displayed
                                                                          in the diagnostic messages
   SwitchOn        BOOL                                                   TRUE means connect
                                                                          power, FALSE means dis‐
                                                                          connect power
STRUCT ML_oCmdResult
Name       Data type             Inherited     Address    Initial value   Comment
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
URL:              https://<ip-addr>/automation/api/v2/nodes/motion/axs/
<axs_name>/cmd/power
Payload:

{"type":"bool8","value":true}

Python:
<cmdID> = motion.axs_cmd_power( axs=<axsName>
[,switch_on=<switchOn>])

Generates a power command for a single axis (object has to be "attached"),
see documentation Python Runtime App ⮫ Python functions
.
● <axsName> - string, axis object name
● <switchOn> - bool, is set to TRUE to switch on power (TRUE is default)

BundleIF:
//! Create a power command for a single axis (AXS_CMD_POWER)
//!
//! @param[in]     sourceInfo    Command source information
//! @param[in]     axsName       Name of the motion object
//! @param[in]     switchOn      Switch on or off?
//! @param[out]    cmdID         The ID of the added command
//! @return                      Was everything okay?
virtual MotionResult axsPowerCmd(const cmd::Cmd-SourceInfo&
sourceInfo, const char* axsName, bool switchOn,
uint64_t&cmdID) const = 0;

### 7.2.3 AxsReset - AxsReset - Resetting the axis

Basics
This command resets all reported axis errors and returns the axis to a defined
state. It implements the transition from the ERRORSTOP state to the STAND‐
STILL, STOPPED or DISABLED state, depending on the previous state of the
power connection and the state of the "Drive Halt" drive function. An axis that
is part of a kinematic system or a gantry, for example, is removed from the
kinematic system or the gantry with the reset. The reset is only permitted if
the axis is in an error state or in one of the states STANDSTILL, STOPPED or
DISABLED.
This command is an unbuffered command, i.e. all previously active commands
and the commands of the preparation buffer are discarded.

PLC:

ML_AxsReset
Name        Data type        Inherited      Address       Initial value   Comment
                             from
  Data       ML_AxsReset                                                  Output: Command parame‐
                                                                          ters
  ML_Axs‐    BOOL                                                         Returns information
Reset                                                                     whether the command can
                                                                          be added to the axis
                                                                          object.
                                                                          ● TRUE: The ML_AxsReset
                                                                            command could be
                                                                            added successfully
                                                                          ● FALSE: An error
                                                                            occurred. Details in
                                                                            ML_oCmdResult
ML_AxsResetData
Name          Data type         Inher‐   Addres Initial   Comment
                                ited     s      value
                                from

ML_AxsResetData
 Data         ML_AxsRe‐                                    InOut: Command parameters
setData
 ML_AxsReset BOOL                                          Returns information whether the com‐
                                    mand can be added to the axis object.
                                    ● TRUE: The command could be added
                                      successfully
                                    ● FALSE: An error occurred. Details in
                                      ML_oCmdResult
STRUCT ML_AxsResetData
Name         Data type           Inher‐   Addres Initial   Comment
                                 ited     s      value
                                 from
   In              ML_iAxsCmd                              Input: Command data of the command
                   Base
   Out             ML_oCm‐                                 Output: Command parameters
                   dResult
STRUCT ML_iAxsCmdBase
Name          Data type          Inher‐   Addres Initial   Comment
                                 ited     s      value
                                 from
   AxisName        STRING(63)                              Name of the axis used to execute the com‐
                                                           mand
   Source          STRING(50)                              Specifies the command source, e.g PlcAp‐
                                                           plication1 is displayed in the diagnostic
                                                           messages
   SourceLine      ULINT                                   Specifies the source line of the command;
                                                           is displayed in the diagnostic messages
STRUCT ML_oCmdResult
Name        Data type            Inher‐   Addres Initial   Comment
                                 ited     s      value
                                 from
   CmdID           ULINT                                   Command ID (is set to
                                                           18446744073709551615 in the event of
                                                           an error)
   Error           BOOL                                    Error ID TRUE indicates that an error
                                                           occurred
   ErrorID         UDINT                                   Specifies the type of occurred error: The
                                                           upper 4 bytes reflect the main diagnostics,
                                                           the lower 4 bytes reflect the detailed diag‐
                                                           nostics, 0 means no error

Data Layer:
Method: POST
URL:               https://<ip-addr>/automation/api/v2/nodes/motion/axs/
<axs_name>/cmd/reset
Payload: (blank)

Python:
<cmdID> = motion.axs_cmd_reset( axs=<axsName> )

Generates a reset command for a single axis (object has to be "attached"), see
documentation Python Runtime App ⮫ Python functions.
● <axsName> - string, axis name

BundleIF:
//! Create a reset command for a single axis (AXS_CMD_RESET)
//!
//! @param[in]     sourceInfo    Command source information
//! @param[in]     axsName       Name of the motion object
//! @param[out]    cmdID         The ID of the added command
//! @return                      Was everything okay?
virtual MotionResult axsResetCmd(const cmd::CmdSourceInfo&
sourceInfo, const char* axsName, uint64_t &cmdID) const = 0;

### 7.2.4 AxsAbort - Canceling the axis command

Basics
This command cancels the current motion for an individual axis. It decelerates
with the specified dynamic limits up to velocity zero. During processing, the
PLCOpen status of the axis is set to ABORTED. If standstill is reached, the
status of the command is set to DONE and the PLCOpen status of the axis is
set to STANDSTILL.
The programmed limit values for deceleration and jerk have to be positive
(greater than zero), as otherwise the parameters would be inconsistent.
Exception: If the jerk limit value is exactly zero, the motion is executed
without jerk limit (trapezoid velocity profile).
This command is an unbuffered command, i.e. the previously active command
is canceled, the commands of the preparation buffer are discarded. These
commands are assigned the command state ABORTED.

PLC:

ML_AxsAbort
Name        Data type        Inherited      Address     Initial value   Comment
                             from
  Data       ML_AxsA‐                                                   Output: Command parame‐
             bortData                                                   ters
  ML_AxsA‐   BOOL                                                       Returns information
bort                                                                    whether the command can
                                                                        be added to the axis
                                                                        object.
                                                                        ● TRUE: The command
                                                                          could be added success‐
                                                                          fully
                                                                        ● FALSE: An error
                                                                          occurred. Details in
                                                                          ML_oCmdResult

STRUCT ML_AxsAbortData
Name       Data type   Inherited             Address   Initial value   Comment
                       from
  In       ML_iAxsA‐                                                   Input: Command data of
           bort                                                        the command
  Out      ML_oCmdRe‐                                                  Output: Command parame‐
           sult                                                        ters
STRUCT ML_iAxsAbort EXTENDS ML_iAxsCmdBase
Name        Data type   Inherited   Address            Initial value   Comment
                        from
  AxisName STRING(63) ML_iAxsCmd‐                                      Name of the axis used to
                        Base                                           execute the command
  Source    STRING(50) ML_iAxsCmd‐                                     Specifies the command
                        Base                                           source, e.g PlcApplication1
                                                                       is displayed in the diag‐
                                                                       nostic messages
   SourceLine ULINT            ML_iAxsCmd‐                             Specifies the source line of
                               Base                                    the command; is displayed
                                                                       in the diagnostic messages
   Decelera‐       LREAL                                               Dynamic limitation: max‐
tion                                                                   imum deceleration during
                                                                       abort (deceleration)
   JerkDec         LREAL                                               Dynamic limitation: max‐
                                                                       imum deceleration jerk
                                                                       during abort (deceleration)
STRUCT ML_oCmdResult
Name       Data type           Inherited     Address   Initial value   Comment
                               from
   CmdID           ULINT                                               Command ID (is set to
                                                                       18446744073709551615 in
                                                                       the event of an error)
   Error           BOOL                                                Error ID TRUE indicates
                                                                       that an error occurred
   ErrorID         UDINT                                               Specifies the type of
                                                                       occurred error: The upper
                                                                       4 bytes reflect the main
                                                                       diagnostics, the lower 4
                                                                       bytes reflect the detailed
                                                                       diagnostics, 0 means no
                                                                       error

Data Layer:
Method: POST
URL:              https://<ip-addr>/automation/api/v2/nodes/motion/axs/
<axs_name>/cmd/abort
Payload:

{
"type":"object","value":
{
"dec":10,

"jrkDec":0
}
}

Python:
<cmdID> = motion.axs_cmd_abort( axs=<axsName>
[,dec=<deceleration>] [,jrk_dec=<jerkDeceleration>] )

Generates an abort command for a single axis (object has to be "attached"),
see documentation Python Runtime App ⮫ Python functions.
● <axsName> - string, axis object name
● <deceleration> - double, deceleration limit value of the command (the last

  programmed deceleration limit value is used if this parameter is not pro‐
  grammed)
● <jerkDeceleration> - double, jerk limit value for the deceleration of the
  command (the last programmed jerk limit value for the deceleration is used
  if this parameter is not programmed)

BundleIF:

/// @brief Create an abort command for a single axis
(AXS_CMD_ABORT)
///
/// @param[in]     handle       Handle of the interface
/// @param[in]     sourceInfo   Command source information
/// @param[in]     axsName      Name of the motion object
/// @param[in]     dynLim       Dynamic limits of the command
/// @param[out]    cmdID        The ID of the added command
/// @return                     Status of the function call:
STS_OK or an error code on failure.
::motion::core::MotionResult(*axsAbortCmd)(void* handle,
const ::motion::core::dia::CmdSourceInfo& sourceInfo, const
char* axsName, const ::motion::core::cmd::DynamicBreakLimitsT&
dynLim, uint64_t& cmdID);

with the following data types:

//! data container for dynamic break limits
struct DynamicBreakLimitsT
{
  double m_dec = 0.0;        //!< deceleration limit
  double m_jrkDec = 0.0;     //!< jerk limit while decelerating
  double m_jrkDec2 = 0.0;    //!< second jerk limit while
decelerating (not used)
};

Please note: m_jrkDec2 is currently not supported and has to be set to 0.

### 7.2.5 AxsStop - Stop axis command

Basics
This command cancels the current motion for an individual axis and stops the
axis so that no further motion is possible. The command decelerates to zero
velocity with the specified dynamic limits. During processing, the PLCOpen

status of the axis is set to STOPPING. If standstill is reached, the status of
the command is set to DONE and the PLCOpen status of the axis is set to
STOPPED. In this state, the “Drive Halt" drive function is active so that the
axis no longer moves.
The programmed limit values for deceleration and jerk have to be positive
(greater than zero), as otherwise the parameters would be inconsistent.
Exception: If the jerk limit value is exactly zero, the motion is executed
without jerk limit (trapezoid velocity profile).
The PLCOpen status STOPPED can only be exited again with a stop command
in "UNSTOP" mode and change to STANDSTILL. The drive function "Drive Halt"
is switched off again so that motion commands can be specified again.
This command is an unbuffered command, i.e. the previously active command
is canceled, the commands of the preparation buffer are discarded. These
commands are assigned the command state ABORTED.

Settings in the drive
If the CoE (CANopen over EtherCAT) Motion profile is used in the axis profile,
the drive parameter "0x605D:00, Drive Halt: Halt option code" has to be set
to "quick stop" (-1). This ensures that the "Drive Halt" drive function can be
activated correctly.

PLCOpen states for the stop command

Steps of a stop command
1.      A stop command is issued during an active motion
2.      The command becomes active and ...
        ● sets the status of the command to ACTIVE
        ● sets the PLCOpen status of the axis to STOPPING
        ● decelerates the axis with the specified dynamic limits
        In this state, only the following commands are permitted:
        ● another stop command with other dynamic limits
        ● an internal EStop command in the event of an axis error
3.      If the axis has stopped, then ...
        ●  the drive function "Drive Halt" is activated
        ●  the drive operating mode remains unchanged
        ●  the PLCOpen status of the axis is set to STOPPED
        ●  the status of the command is set to DONE
        In this state, only the following commands are permitted:
        ● another stop command with other dynamic limits (without function,
            as the axis is already stationary)
        ● a "UNSTOP" command
        ● an internal EStop command in the event of an axis error
4.      If an "UNSTOP" command is issued, then
        ● the actual position of the drive is set as an interpolated position
        ● the drive is switched back to the "Position" operation mode
        ● the drive function "Drive Halt" is switched off
        ● wait until the drive follows the command value input of the control
          system again
        ● the PLCOpen status of the axis is set to STANDSTILL
        ● the status of the command is set to DONE

PLC:

ML_AxsStop
Name       Data type               Inherited from   Address   Initial   Comment
                                                              value
   Data            ML_AxsStop‐                                          Output: Command parame‐
                   Data                                                 ters
  ML_Axs‐          BOOL                                                 Returns information whether
Stop                                                                    the command can be added
                                                                        to the axis object.
                                                                        ● TRUE: The command
                                                                          could be added success‐
                                                                          fully
                                                                        ● FALSE: An error occurred.
                                                                          Details in ML_oCmdRe‐
                                                                          sult
STRUCT ML_AxsStopData
Name       Data type               Inherited from   Address   Initial   Comment
                                                              value
   In              ML_iAxsStop                                          Input: Command data of the
                                                                        command
   Out             ML_oCmdRe‐                                           Output: Command parame‐
                   sult                                                 ters
STRUCT ML_iAxsStop EXTENDS ML_iAxsCmdBase
Name       Data type    Inherited from Address                Initial   Comment
                                                              value
   AxisName STRING(15)             ML_iAxsCmd‐                          Name of the axis used to
                                   Base                                 execute the command
   Source          STRING(50)      ML_iAxsCmd‐                          Specifies the command
                                   Base                                 source, e.g PlcApplication1
                                                                        is displayed in the diag‐
                                                                        nostic messages
  Source‐          ULINT           ML_iAxsCmd‐                          Specifies the source line of
Line                               Base                                 the command; is displayed
                                                                        in the diagnostic messages
   DoStop          BOOL                                                 TRUE: Command is executed
                                                                        in STOP mode
                                                                        FALSE: Command is exe‐
                                                                        cuted in UNSTOP mode
                                                                        (switch back to STAND‐
                                                                        STILL)
   Decelera‐       LREAL                                                Dynamic limitation: max‐
tion                                                                    imum deceleration during
                                                                        abort (deceleration)

STRUCT ML_iAxsStop EXTENDS ML_iAxsCmdBase
  JerkDec  LREAL                                                     Dynamic limitation: max‐
                                                imum deceleration jerk
                                                during abort (deceleration)
STRUCT ML_oCmdResult
Name       Data type           Inherited from   Address   Initial    Comment
                                                          value
 CmdID       ULINT                                                   Command ID (is set to
                                                                     18446744073709551615 in
                                                                     the event of an error)
 Error       BOOL                                                    Error ID TRUE indicates that
                                                                     an error occurred

 ErrorID     UDINT                                                   Specifies the type of
                                                occurred error: The upper 4
                                                bytes reflect the main diag‐
                                                nostics, the lower 4 bytes
                                                reflect the detailed diagnos‐
                                                tics, 0 means no error

Data Layer:
Method: POST
URL:               https://<ip-addr>/automation/api/v2/nodes/motion/axs/
<axs_name>/cmd/stop
Payload:

{
"type":"object","value":
{
"doStop":true,
"dec":10,
"jrkDec":0
}
}

Python:
<cmdID> = motion.axs_cmd_stop( axs=<axsName>,
do_stop=<boolDoStop> [, dec=<deceleration>] [,
jrk_dec=<jerkDeceleration>] )

Generates a stop command for a single axis (object has to be "attached"), see
documentation Python Runtime App ⮫ Python functions.
● <axsName> - string, axis object name
● <boolDoStop> - boolean, True: STOP mode, False: UNSTOP mode
● <deceleration> - double, deceleration limit value of the command (the last
  programmed deceleration limit value is used if this parameter is not pro‐
  grammed)
● <jerkDeceleration> - double, jerk limit value for the deceleration of the
  command (the last programmed jerk limit value for the deceleration is used
  if this parameter is not programmed)

BundleIF:

/// @brief Command to enter the PLCopen state STOPPING and
STOPPED and back to STANDSTILL
///
/// @param[in]     handle       Handle of the interface
/// @param[in]     sourceInfo   Command source information
/// @param[in]     axsName      Name of the motion object
/// @param[in]     doStop       command STOP? (when false ->
UNSTOP will switch back to STANDSTILL)
/// @param[in]     dynLim       Dynamic limits of the command
(deceleration and jerk limit); only relevant when doStop==true
/// @param[out]    cmdID        The ID of the added command
/// @return                     Status of the function call:
STS_OK or an error code on failure.
::motion::core::MotionResult(*axsStopCmd)(void* handle,
const ::motion::core::dia::CmdSourceInfo& sourceInfo,
const char* axsName, bool doStop,
const ::motion::core::cmd::DynamicBreakLimitsT& dynLim,
uint64_t& cmdID);

with the following data types:

/// data container for dynamic break limits
struct DynamicBreakLimitsT
{
  double m_dec = 0.0;        ///< deceleration limit
  double m_jrkDec = 0.0;     ///< jerk limit while decelerating
 double m_jrkDec2 = 0.0;     ///< second jerk limit while
decelerating (not used)
};

Please note: m_jrkDec2 is currently not supported and has to be set to 0.

### 7.2.6 AxsEmergencyStop - Axis Emergency Stop

Basics
If one of the coupled axes on the drive enters an error reaction, the second
axis should also decelerate in the same manner. This command allows the
customer to control the timing at which the emergency stop for the other axis
is triggered.
This command is part of the error handling managed by the customer.
This command sets the error level to SEVERE and indirectly activates the error
reaction process (if the axis is connected to a drive, the drive stop function
is activated at the same time; otherwise, only the interpolation delay of the
control is activated).
This command is an unbuffered command, i.e. the previously active command
is canceled, the commands of the preparation buffer are discarded. The com‐
mand causes the system to transition to the PLCopen ERRORSTOP state.

PLC:

FUNCTION ML_AxsEmergencyStop: BOOL
Name        Data type   Inherited  Address                  Initial value    Comment
                        from
  IN_OUT    ML_AxsEmer‐                                                      Input/output data
Data        gencyStop‐

Data
  OUTPUT BOOL
ML_AxsEmer‐
gencyStop
STRUCT ML_AxsEmergancyStopData
Name       Data type    Inherited from            Address    Initial        Comment
                                                             value
  In             ML_iAxsCmd‐                                                Input: Command data of the
                 Base                                                       command
  Out            ML_oCmdRe‐                                                 Output: Command parame‐
                 sult                                                       ters
STRUCT ML_iAxsCmdBase
Name       Data type             Inherited from   Address    Initial        Comment
                                                             value
  AxisName STRING(15)                                                       Name of the axis used to
                                                                            execute the command
  Source         STRING(50)                                                 Specifies the command
                                                                            source, e.g PlcApplication1
                                                                            is displayed in the diag‐
                                                                            nostic messages
  Source‐        ULINT                                                      Specifies the source line of
Line                                                                        the command; is displayed
                                                                            in the diagnostic messages
STRUCT ML_oCmdResult
Name       Data type            Inherited from    Address    Initial        Comment
                                                             value
  CmdID          ULINT                                                      Command ID (is set to
                                                                            18446744073709551615 in
                                                                            the event of an error)
  Error          BOOL                                                       Error ID TRUE indicates that
                                                                            an error occurred
  ErrorID        ULINT                                                      Specifies the type of
                                                                            occurred error: The upper 4
                                                                            bytes reflect the main diag‐
                                                                            nostics, the lower 4 bytes
                                                                            reflect the detailed diagnos‐
                                                                            tics, 0 means no error

Data Layer:
Method: POST
URL:              https://<ip-addr>/automation/api/v2/nodes/motion/axs/
<axs_name>/cmd/emergency-stop
Payload: (blank)

BundleIF:

/// @brief Create an emergency stop command for a single axis
(AXS_CMD_ESTOP)
///
/// @param[in]     handle       Handle of the interface
/// @param[in]     sourceInfo   Command source information
/// @param[in]     axsName      Name of the motion object
/// @param[out]    cmdID        The ID of the added command
/// @return                     Status of the function call:
STS_OK or an error code on failure.
::motion::core::MotionResult(*axsEmergencyStopCmd)(void*
handle, const ::motion::core::dia::CmdSourceInfo& sourceInfo,
const char* axsName, std::uint64_t& cmdID);

### 7.2.7 AxsInterrupt - Interrupting the axis command

Basics
This command interrupts the current axis motion with the current dynamic
limit values. The behavior is identical to setting the axis override to 0%. Con‐
tinue the motion with the AxsContinue command. This command is effective
immediately, it does not change the command buffer (so all buffered com‐
mands are still available).

States of the Interrupt/Continue command
The Interrupt and Continue commands are active together with the regular
command processing. Thus, there are the following command states:
Commanding sequence       Axis behavior              Command state
Motion command            Axis starts moving         Move: ACTIVE
becomes active
Interrupt is commandedAxis decelerates with     Move: ACTIVE; Interrupt:
                      the currently commanded ACTIVE
                      dynamics
-                     Axis has stopped          Move: ACTIVE; Interrupt:
                                                DONE
Continue is commanded Axis accelerates again    Move: ACTIVE; Interrupt:
                      (continues the motion     DONE; Continue: DONE
                      command)
-                     Target position of motion Move: DONE; Interrupt:
                      command is reached,       DONE; Continue: DONE
                      motion is stopped
The Continue command can also be commanded before a complete axis
standstill resulting from an interrupt task.

States of the Interrupt/Abort command
The Abort command also aborts an Interrupt command.
Axis command states:

Commanding sequence         Axis behavior            Command state
Motion command              Axis starts moving       Move: ACTIVE
becomes active
Interrupt is commanded      Axis decelerates with   Move: ACTIVE; Interrupt:
                            the currently commanded ACTIVE
                            dynamics
Abort is commanded          Axis decelerates with   Move: ABORTED; Inter‐
before it is stopped        the commanded abort     rupt: ABORTED; Abort:
                            dynamics                ACTIVE
-                           Motion is stopped       Move: ABORTED; Inter‐
                                                    rupt: ABORTED; Abort:
                                                    DONE

PLC:

ML_AxsInterrupt
Name           Data type      Inher‐   Addres Initial     Comment
                              ited     s      value
                              from
  Data         ML_AxsInter‐                               InOut: Command parameters
               ruptData
  ML_AxsInter‐ BOOL                                       Returns information whether the com‐
rupt                                                      mand can be added to the axis object.
                                                          ● TRUE: The command could be added
                                                            successfully
                                                          ● FALSE: An error occurred. Details in
                                                            ML_oCmdResult
STRUCT ML_AxsInterruptData
Name         Data type     Inher‐      Addres Initial    Comment
                           ited        s      value
                           from
  In         ML_iAxsCmd                                  Input: Command data of the command
             Base
  Out        ML_oCm‐                                     Output: Command parameters
             dResult
STRUCT ML_iAxsCmdBase
Name          Data type       Inher‐   Addres Initial    Comment
                              ited     s      value
                              from
  AxisName       STRING(63)                              Name of the axis used to execute the com‐
                                                         mand
  Source         STRING(50)                              Specifies the command source, e.g PlcAp‐
                                                         plication1 is displayed in the diagnostic
                                                         messages

STRUCT ML_iAxsCmdBase
  SourceLine ULINT                                           Specifies the source line of the command;
                                      is displayed in the diagnostic messages
STRUCT ML_oCmdResult
Name        Data type              Inher‐   Addres Initial   Comment
                                   ited     s      value
                                   from
   CmdID           ULINT                                     Command ID (is set to
                                                             18446744073709551615 in the event of
                                                             an error)
   Error           BOOL                                      Error ID TRUE indicates that an error
                                                             occurred
   ErrorID         UDINT                                     Specifies the type of occurred error: The
                                                             upper 4 bytes reflect the main diagnostics,
                                                             the lower 4 bytes reflect the detailed diag‐
                                                             nostics, 0 means no error

Data Layer:
Method: POST
URL:               https://<ip-addr>/automation/api/v2/nodes/motion/axs/
<axs_name>/cmd/interrupt
Payload: (blank)

Python:
<cmdID> = motion.axs_cmd_interrupt ( obj=<axsName> )

Generates an interrupt command for a single axis (object has to be
"attached"), see documentation Python Runtime App ⮫ Python functions
● <axsName> - string, axis name

BundleIF:
//! Create an interrupt command for a single axis
(AXS_CMD_INTERRUPT)
//!
//! @param[in]   handle      Pointer to the interface
//! @param[in]   sourceInfo Command source information
//! @param[in]   axsName     Name of the motion object
//! @param[out] cmdID        The ID of the added command
//! @return                  Was everything okay?
extern "C" MotionResult MOTION_CORE_AxsInterruptCmd(void
*handle, const dia::CmdSourceInfo& sourceInfo, const char*
axsName, uint64_t &cmdID);

### 7.2.8 AxsContinue - Continuing the axis command

Basics
This command continues the current axis motion that has been interrupted
by the “AxisInterrupt" command, using the current dynamic limit values. The
behavior is identical to setting the axis override to the previous value. This
command is applied immediately. It does not change the command buffer, i.e.
all buffered commands are preserved (overrides from 0 to the previous value).

PLC:

ML_AxsContinue
Name          Data type      Inher‐   Addres Initial   Comment
                             ited     s      value
                             from

  Data        ML_AxsCon‐                               InOut: Command parameters
tinueData
   ML_AxsCon‐ BOOL                                     Returns information whether the com‐
tinue                                                  mand can be added to the axis object.
                          ● TRUE: The command could be added
                            successfully
                          ● FALSE: An error occurred. Details in
                            ML_oCmdResult
STRUCT ML_AxsContinueData
Name         Data type    Inher‐      Addres Initial   Comment
                          ited        s      value
                          from
  In         ML_iAxsCmd                                Input: Command data of the command
             Base
  Out        ML_oCm‐                                   Output: Command parameters
             dResult
STRUCT ML_iAxsCmdBase
Name          Data type      Inher‐   Addres Initial   Comment
                             ited     s      value
                             from
  AxisName      STRING(63)                             Name of the axis used to execute the com‐
                                                       mand
  Source        STRING(50)                             Specifies the command source, e.g PlcAp‐
                                                       plication1 is displayed in the diagnostic
                                                       messages
  SourceLine    ULINT                                  Specifies the source line of the command;
                                                       is displayed in the diagnostic messages
STRUCT ML_oCmdResult
Name        Data type        Inher‐   Addres Initial   Comment
                             ited     s      value
                             from
  CmdID         ULINT                                  Command ID (is set to
                                                       18446744073709551615 in the event of
                                                       an error)
  Error         BOOL                                   Error ID TRUE indicates that an error
                                                       occurred

STRUCT ML_oCmdResult
  ErrorID   UDINT                                          Specifies the type of occurred error: The
                                    upper 4 bytes reflect the main diagnostics,
                                    the lower 4 bytes reflect the detailed diag‐
                                    nostics, 0 means no error

Data Layer:
Method: POST
URL:               https://<ip-addr>/automation/api/v2/nodes/motion/axs/
<axs_name>/cmd/continue
Payload: (blank)

Python:
<cmdID> = motion.axs_cmd_continue ( obj=<axsName> )

Removes an active interrupt command of a single axis (object has to be
"attached"), see documentation Python Runtime App ⮫ Python functions.
The command is active immediately, getCmdState( ) with the specified com‐
mand ID always returns a DONE.
● <axsName> - string, axis name

BundleIF:
//! Create a continue command for a single axis and removes an
active interrupt command (AXS_CMD_CONTINUE)
//!
//! @param[in]   handle      Pointer to the interface
//! @param[in]   sourceInfo Command source information
//! @param[in]   axsName     Name of the motion object
//! @param[out] cmdID        The ID of the added command
//! @return                  Was everything okay?
extern "C" MotionResult MOTION_CORE_AxsContinueCmd(void
*handle, const dia::CmdSourceInfo& sourceInfo, const char*
axsName, uint64_t &cmdID);

### 7.2.9 AxsVelocity - Axis velocity

Basics
This command commands a motion of a single axis to the specified target
velocity.
Prerequisite: The axis has to be powered on, see⮫ Chapter 7.2.2 AxsPower -
Axis power on page 333
During the motion, the PLCopen state of the axis is set to CONTIN‐
UOUS_MOTION. It is ensured that the configured dynamic limits of the axis
is complied with. If a target velocity is specified that is greater than the con‐
figured maximum velocity or greater than the commanded dynamic limit, a
runtime error is generated and the axis goes into ERRORSTOP.
The ML_AxsGetPLCOpenState function block of the CXA_Motion library can be
used to determine the current PLC open state, for example.
Depending on the parameters, it is interpolated to the target velocity with a
jerk limit or without (both jerk limit values to the commanded dynamic limits
are zero).

If the target velocity is reached, the command continues to travel endlessly
at constant velocity. The command state remains ACTIVE. The command can
be aborted with AxsAbort, see ⮫ Chapter 7.2.4 AxsAbort - Canceling the axis
command on page 337. In this case the command state changes to ABORTED.
In contrast to the position commands, the target velocity for this command is
adjusted using the velocity override.
Example: a target velocity of 500mm/min is commanded. If the override is
now set to 0.5, ctrlX MOTION performs an interpolation of the axis velocity to
250 mm/min (= 500 * 0.5).
The acceleration override has an impact on the acceleration limit value, analo‐
gously to the position command.
An AxsVelocity command can be interrupted with an AxsInterrupt com‐

mand, see ⮫ Chapter 7.2.7 AxsInterrupt - Interrupting the axis command
on page 346. In this case, the ctrlX MOTION generates a decelerating motion
(in compliance with all dynamic limit values) until it comes to a standstill.
The AxsVelocity command remains active and the axis remains in the PLCopen
state CONTINUOUS_MOTION. If an AxsContinue command is issued later, the
ctrlX MOTION interpolates back to the commanded target velocity.
The command can be issued as buffered or unbuffered command. The buf‐
fered commands are stored in a command buffer and executed sequentially.
Unbuffered commands are prepared within the framework of the execution.
They cancel the currently active command. In this case, the remaining com‐
mand buffer is deleted (all commands are assigned the state ABORTED,
when querying the state with ⮫ Chapter 7.8.7 GetCmdState - Command states
on page 787). Since the AxsVelocity command is not automatically terminated,
it makes no sense to command buffered commands after a buffered AxsVe‐
locity, as the (eternally running) AxsVelocity command can only be terminated
by means of an AxsAbort or another unbuffered command, which in turn
deletes the command buffer.
Use the command AxsVelocity (per parameter) to specify whether the respec‐
tive drive is to be switched to the "Velocity" operation mode, see ⮫ Chapter
Axis objects on page 20. Alternatively, the command AxesVelocity can also be
executed in the operation mode "Position".
If the axis encoder value is “noisy” or if the axis is slow or reacts imprecisely,
a considerably more constant velocity can be achieved with the “velocity”
operation mode.
Switching the operation mode is currently only possible in standstill. An axis
standstill is e.g. reached at the end of a motion command. Optionally, the
override can be set to zero or the AxsInterrupt can be commanded. A running
motion can also be canceled using AxsAbort so that the axis is in standstill if
AxsAbort is completed.
This means that an AxsVelocity command that does not change the opera‐
tion mode can also be commanded as an unbuffered command during a
motion. An AxsVelocity command changing the operation mode can only be
commanded if the axis is at standstill.

PLC:

STRUCT ML_AxsVelData
Name       Data type            Inherited     Address   Initial value   Comment
                                from
   In              ML_iAxsVel                                           Input: Command data of
                                                                        the command
   Out             ML_oCmdRe‐                                           Output: Command parame‐
                   sult                                                 ters
STRUCT ML_iAxsVel EXTENDS ML_iAxsCmdBase
Name        Data type   Inherited  Address              Initial value   Comment
                        from
  AxisName STRING(15) ML_iAxsCmd‐                                       Name of the axis used to
                        Base                                            execute the command
  Source    STRING(50) ML_iAxsCmd‐                                      Specifies the command
                        Base                                            source, e.g PlcApplication1
                                                                        is displayed in the diag‐
                                                                        nostic messages
   SourceLine ULINT             ML_iAxsCmd‐                             Specifies the source line of
                                Base                                    the command; is displayed
                                                                        in the diagnostic messages
 Velocity          LREAL                                                Velocity limit value
 DriveVel‐         BOOL                                 FALSE           TRUE if the command is to
Mode                                                                    switch the drive to velocity
                                                                        operating mode (otherwise
                                                                        it moves to position mode)
   Buffered        BOOL                                                 TRUE, if the command is
                                                                        to be executed as a buf‐
                                                                        fered command, otherwise
                                                                        FALSE
   DynLimits ML_iDynLi‐                                                 Limit values of the position
             mits                                                       command
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
  ErrorID  ULINT                                                       Specifies the type of
                                                   occurred error: The upper
                                                   4 bytes reflect the main
                                                   diagnostics, the lower 4
                                                   bytes reflect the detailed
                                                   diagnostics, 0 means no
                                                   error

Data Layer:
Method: POST
URL:               https://<ip-addr>/automation/api/v2/nodes/motion/axs/

<axs_name>/cmd/velocity
Payload:

{
"type":"object","value":
{"axsVel":10,
  "driveVelMode":true,
  "buffered":false,
  "lim":{ "vel":10,
           "acc":10,
           "dec":10,
           "jrkAcc":0,
           "jrkDec":0
           }
}
}

Python:
<cmdID> = motion.axs_cmd_velocity( axs=<axsName>,
target_vel=<targetVel> [,vel=<velocity>] [,acc=<acceleration>]
[,dec=<deceleration>] [,jrk_acc=<jerkAcceleration>]
[,jrk_dec=<jerkDeceleration>] [,drive_vel_mode=<driveVelMode>]
[,buffered=<buffered>] )

Creates a velocity command for a single axis (object has to be "attached"),
see documentation Python Runtime App ⮫ Python functions
● <axsName> - string, axis object name
● <targetVel> - double, target velocity of the command
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

● <driveVelMode> - bool, specifies if the command is to switch the drive to
  the velocity mode (otherwise, the position mode is retained), (presetting is
  FALSE)
● <buffered> - bool, use TRUE if the command is to be buffered (TRUE by
  default)

BundleIF:
//! @brief Create a velocity command for a single axis
(AXS_CMD_VELOCITY)
//!
//! @param[in]   sourceInfo    Command source information
//! @param[in]   axsName       Name of the motion object
//! @param[in]   targetVel     Target velocity of the command
(might be negative)
//! @param[in]   dynLim        Dynamic limits of the command
//! @param[in]   driveVelMode Should the drive switched/stay
in velocity mode? (set to false, that the drive is switched/
stay in position mode)
//! @param[in]   buffered      Create as a buffered command
//! @param[out] cmdID          The ID of the added command
//! @return                    Was everything okay?
virtual MotionResult axsVelCmd(const dia::CmdSourceInfo&
sourceInfo, const char* axsName, double targetVel, const
cmd::DynamicLimitsT& dynLim, bool driveVelMode, bool buffered,
uint64 t& cmdID) const = 0;

mit

//! @brief data container for dynamic limits
struct DynamicLimitsT
{
double m_vel = 0.0;      //!< Velocity limit
double m_acc = 0.0;      //!< Acceleration limit
double m_dec = 0.0;      //!< Deceleration limit
double m_jrkAcc = 0.0;   //!< Jerk limit while accelerating
double m_jrkDec = 0.0;   //!< Jerk limit while decelerating
double m_jrkAcc2 = 0.0; //!< Second jerk limit while
accelerating (not used)
double m_jrkDec2 = 0.0; //!< Second jerk limit while
decelerating (not used)
};

### 7.2.10 AxsTorque - Torque axis

Basics
This command switches the operation mode in the drive to "Torque/force
control with speed limitation" and commands the axis to the set torque with
the specified parameters (⮫ Chapter 6.2.5 Torque/force control on page 155).
Prerequisite: The axis has to be powered on, see ⮫ Chapter 7.2.2 AxsPower -
Axis power on page 333.
Configuring the operation mode in the drive

SOE

The "Torque/force control with speed limitation" operation mode has to be
configured in a secondary operation mode in the drive. e.g. secondary oper‐
ating mode 2 value "0x8101 hex" or "33025 decimal".

This can be realized by a one-off parameterization in the drive or by config‐
uring the start parameters in the IO project.

COE
The operation mode "cyclic sync torque mode" is used.

For drives with COE connection, it is required to set the speed limitation for
torque mode once.
To do this, the value "4" has to be entered in the parameter object 0x60CA
"Torque/force control Torque limitation option code".
Otherwise, an error message is reported when the torque command is acti‐
vated.

PLC:

STRUCT ML_AxsTrqData
Name       Data type            Inherited     Address   Initial value   Comment
                                from
   In              ML_iAxsTrq                                           Input: Command data of
                                                                        the command
   Out             ML_oCmdRe‐                                           Output: Command parame‐
                   sult                                                 ters
STRUCT ML_iAxsTrq EXTENDS ML_iAxsCmdBase
Name        Data type   Inherited  Address              Initial value   Comment
                        from
  AxisName STRING(15) ML_iAxsCmd‐                                       Name of the axis used to
                        Base                                            execute the command
  Source    STRING(50) ML_iAxsCmd‐                                      Specifies the command
                        Base                                            source, e.g PlcApplication1
                                                                        is displayed in the diag‐
                                                                        nostic messages
   SourceLine ULINT             ML_iAxsCmd‐                             Specifies the source line of
                                Base                                    the command; is displayed
                                                                        in the diagnostic messages
   Torque          LREAL                                                Torque
                                                                        in (Nm, kNm, lb ft, lb in)
  Tor‐             LREAL                                                Ramp for the torque
queRamp                                                                 in units/sec, e.g. Nm/sec
   DynLimits ML_iDynLi‐                                                 Limit values of the position
             mits                                                       command
STRUCT ML_iDynLimits
Name        Data type           Inherited     Address   Initial value   Comment
                                from
   Velocity        LREAL                                                Velocity limit value
                                                                        With a positive sign for
                                                                        HighVelocityLimit, with a
                                                                        negative sign for LowVelo‐
                                                                        cityLimit
   Accelera‐       LREAL                                                Acceleration limit value
tion
   Decelera‐       LREAL                                                Deceleration limit value
tion
   JerkAcc         LREAL                                0               Jerk limit value for acceler‐
                                                                        ation phase
   JerkDec         LREAL                                0               Jerk limit value for deceler‐
                                                                        ation phase

STRUCT ML_oCmdResult
Name       Data type          Inherited    Address       Initial value   Comment
                              from
 CmdID       ULINT                                                       Command ID (is set to
                                                                         18446744073709551615 in
                                                                         the event of an error)
 Error       BOOL                                                        Error ID TRUE indicates
                                                                         that an error occurred
 ErrorID     ULINT                                                       Specifies the type of
                                                                         occurred error: The upper
                                                                         4 bytes reflect the main
                                                                         diagnostics, the lower 4

                                                     bytes reflect the detailed
                                                     diagnostics, 0 means no
                                                     error
In the ML_iDynLimits structure, the value for velocity with a positive sign is
used for the "HighVelocityLimit" limit, and with a negative sign for the "LowVe‐
locityLimit" limit. The other values in the structure are not used.
Error reaction

Data Layer:
Method: POST
URL:               https://<ip-addr>/automation/api/v2/nodes/motion/axs/
<axs_name>/cmd/torque
Payload:

{
"type":"object","value":
{
    "targetTrq": 1,
    "trqRamp": 0,
    "lim": {
        "vel": 1,
        "acc": 1,
        "dec": 1,
        "jrkAcc": 0,
        "jrkDec": 0
    }
}
}

Python:
<cmdID> = motion.axs_cmd_torque( axs=<axsName>,
target_trq=<targetTrq> [,trqRamp=<trqRamp>] [,vel=<velocity>]
[,acc=<acceleration>] [,dec=<deceleration>]
[,jrk_acc=<jerkAcceleration>] [,jrk_dec=<jerkDeceleration>] )

Creates a Torque command for a single axis (object has to be "attached"), see
documentation Python Runtime App ⮫ Python Functions.
●   <axsName> - string, axis object name
●   <targetTrq> - double, target torque of the command
●   <trqRamp> - double, torque ramp of the command
●   <velocity> - double, velocity limit value of the command (the last pro‐
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
/// @brief Create a motion command for a single axis to
interpolate to a target force/torque (AXS_CMD_TORQUE)
///
/// This command switches the drive to torque mode. The
prerequisites for this (e.g. suitable IO configuration) must
be met for the switching to take place. This command is always
unbuffered.
///
/// @param[in]     sourceInfo     Command source information
/// @param[in]     axsName        Name of the motion object
/// @param[in]     targetTrq      Maximum target force/torque
                                  of the command
/// @param[in]     trqRamp        Force/torque difference that
                                  can be achieved within the
                                  ramp time
/// @param[in]     dynLim         Dynamic limits of the command
/// @param[out]    cmdID          The ID of the added command
/// @return                       Status of the function call:
                                  STS_OK or an error code on
                                  failure.
virtual MotionResult axsTorqueCmd(const dia::CmdSourceInfo&
sourceInfo, const char* axsName, double targetTrq, double
trqRamp, const cmd::DynamicLimitsT& dynLim, uint64_t& cmdID)
const = 0;

with

//! @brief data container for dynamic limits
struct DynamicLimitsT
{
double m_vel = 0.0;      //!< Velocity limit
double m_acc = 0.0;      //!< Acceleration limit
double m_dec = 0.0;      //!< Deceleration limit
double m_jrkAcc = 0.0;   //!< Jerk limit while accelerating
double m_jrkDec = 0.0;   //!< Jerk limit while decelerating
double m_jrkAcc2 = 0.0; //!< Second jerk limit while
                              accelerating (not used)
double m_jrkDec2 = 0.0; //!< Second jerk limit while
                              decelerating (not used)
};

### 7.2.11 AxsPosAbs, AxsPosAbsEx - Absolute positioning of the axis

Basics
This command positions the axis absolute to the specified position by using
this position as new target position. During the motion, the PLCOpen status
of the axis is set to DISCRETE_MOTION. If the commanded target position is
reached, the command status is set to DONE and the PLCOpen status of the
axis is set to STANDSTILL.
Use ML_AxsGetPLCOpenState or ML_GetCmdState to read out the status.
If an error occurs before the execution (e.g. violation of the dynamic limit,
invalid command parameters), the command is not added to the axis object.
If an error occurs during execution, the axis is set to state ERRORSTOP.

If the command is issued as non-buffered command, the previously active
command is canceled, the commands of the preparation buffer are dis‐
carded and the command is executed immediately (with the new commanded
dynamic limit values).
This function requires that the axis is powered up (state STANDSTILL)
The programming limit values for velocity, acceleration, deceleration as well
as both jerk limits have to be positive (greater than zero), as otherwise the
parameters would be inconsistent.
Exception: If both jerk limit values are exactly zero, the motion is executed
without jerk limit (trapezoid velocity profile).
There is an extended variant (PosAbsEx - position absolute extended) in which
a direction of travel can be specified if the command is issued for a modulo
axis. If it is not a modulo axis, the direction parameter is ignored. The simple
PosAbs always takes the shortest path with modulo axes (see also ⮫ Chapter
Axis objects on page 20).
Table 59: These directions of travel can be specified for PosAbsEx:
Direction           Description
SHORTEST_WAY        Take the shortest route to the target position
POSITIVE_DIR        Always drive in a positive direction to the target position
NEGATIVE_DIR        Always drive in a negative direction to the target position
CURRENT_DIR         If the command is commanded as unbuffered and the axis
                    is moving on a straight line during the command, maintain
                    this direction until the target position is reached. In all
                    other cases, take the shortest route to the target position
In addition to the specified direction of travel, a target position window can
also be configured. This can be found in the Data Layer under the node
"motion/axs/[name]/cfg/functions/pos-mode/target-pos-window-modulo".            If
the axis is within this target position window when commanding,
SHORTEST_WAY is always used, regardless of what was actually commanded.
If the axis is currently moving when an unbuffered command is commanded,
the check for the target position window is not carried out with the current
position, but with the stop position (at which the axis stopped in compliance
with the commanded dynamic limits).
If an axis is currently moving in a positive direction and a PosAbsEx is
then commanded unbuffered with the direction of travel NEGATIVE_DIR, it
continues to move in a positive direction until it has stopped in compliance
with the commanded dynamic limits. Only then does the axis move exclusively
in the negative direction. In this case, no special diagnostics is generated. The
behavior is analogous for the other direction.

PLC:

ML_AxsPosAbs
Name       Data type            Inherited     Address   Initial value   Comment
                                from
   Data     ML_AxsPos‐                                                  Output: Command parame‐
            Data                                                        ters
  ML_AxsPo‐ BOOL                                                        Returns information
sAbs                                                                    whether the command can
                                                                        be added to the axis
                                                                        object.
                                                                        ● TRUE: The command
                                                                          could be added success‐
                                                                          fully
                                                                        ● FALSE: An error
                                                                          occurred. Details in
                                                                          ML_oCmdResult
STRUCT ML_AxsPosData
Name       Data type            Inherited     Address   Initial value   Comment
                                from
   In              ML_iAxsPos                                           Input: Command data of
                                                                        the command
   Out             ML_oCmdRe‐                                           Output: Command parame‐
                   sult                                                 ters
STRUCT ML_iAxsPos EXTENDS ML_iAxsCmdBase
Name        Data type  Inherited   Address              Initial value   Comment
                       from
  AxisName STRING(63) ML_iAxsCmd‐                                       Name of the axis used to
                       Base                                             execute the command
  Source    STRING(50) ML_iAxsCmd‐                                      Specifies the command
                       Base                                             source, e.g PlcApplication1
                                                                        is displayed in the diag‐
                                                                        nostic messages
   SourceLine ULINT             ML_iAxsCmd‐                             Specifies the source line of
                                Base                                    the command; is displayed
                                                                        in the diagnostic messages
   Position        LREAL                                                Commanded absolute
                                                                        target position
   Buffered        BOOL                                                 TRUE, if the command is
                                                                        to be executed as a buf‐
                                                                        fered command, otherwise
                                                                        FALSE
   DynLimits ML_iDynLi‐                                                 Limit values of the position
             mits                                                       command

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
  ErrorID      UDINT                                               Specifies the type of
                                                                   occurred error: The upper
                                                                   4 bytes reflect the main
                                                                   diagnostics, the lower 4
                                                                   bytes reflect the detailed
                                                                   diagnostics, 0 means no
                                                                   error

PLC:

ML_AxsPosAbsEx
Name       Data type         Inherited   Address   Initial value   Comment
                             from
  Data      ML_AxsPo‐                                              Output: Command parame‐
            sAbsExData                                             ters
  ML_AxsPo‐ BOOL                                                   Returns information
sAbsEx                                                             whether the command can
                                                                   be added to the axis
                                                                   object.
                                                                   ● TRUE: The command
                                                                     could be added success‐
                                                                     fully
                                                                   ● FALSE: An error
                                                                     occurred. Details in
                                                                     ML_oCmdResult

STRUCT ML_AxsPosAbsExData
Name       Data type   Inherited          Address   Initial value   Comment
                       from
  In       ML_iAxsPo‐                                               Input: Command data of
           sAbsEx                                                   the command
  Out      ML_oCmdRe‐                                               Output: Command parame‐
           sult                                                     ters
STRUCT ML_iAxsPosAbsEx EXTENDS ML_iAxsCmdBase
Name        Data type   Inherited  Address    Initial value         Comment
                        from
  AxisName STRING(63) ML_iAxsCmd‐                              Name of the axis used to
                        Base                                   execute the command
  Source    STRING(50) ML_iAxsCmd‐                             Specifies the command
                        Base                                   source, e.g PlcApplication1
                                                               is displayed in the diag‐
                                                               nostic messages
   SourceLine ULINT         ML_iAxsCmd‐                        Specifies the source line of
                            Base                               the command; is displayed
                                                               in the diagnostic messages
   Position        LREAL                                       Commanded absolute
                                                               target position
   Buffered        BOOL                                        TRUE, if the command is
                                                               to be executed as a buf‐
                                                               fered command, otherwise
                                                               FALSE
   DynLimits ML_iDynLi‐                                        Limit values of the position
             mits                                              command
   Direction ML_PosAb‐                              DIREC‐     Commanded motion direc‐
             sExDirection                           TION_SHORT tion for modulo axes
                                                    EST_WAY
STRUCT ML_iDynLimits
Name        Data type       Inherited     Address   Initial value   Comment
                            from
   Velocity        LREAL                                            Velocity limit value
   Accelera‐       LREAL                                            Acceleration limit value
tion
   Decelera‐       LREAL                                            Deceleration limit value
tion
   JerkAcc         LREAL                            0               Jerk limit value for acceler‐
                                                                    ation phase
   JerkDec         LREAL                            0               Jerk limit value for deceler‐
                                                                    ation phase
STRUCT ML_oCmdResult
Name       Data type        Inherited     Address   Initial value   Comment
                            from
   CmdID           ULINT                                            Command ID (is set to
                                                                    18446744073709551615 in
                                                                    the event of an error)
   Error           BOOL                                             Error ID TRUE indicates
                                                                    that an error occurred

STRUCT ML_oCmdResult
  ErrorID  UDINT                                                     Specifies the type of
                                                 occurred error: The upper
                                                 4 bytes reflect the main
                                                 diagnostics, the lower 4
                                                 bytes reflect the detailed
                                                 diagnostics, 0 means no
                                                 error
TYPE ML_PosAbsExDirection
Name        Data type    Inherited      Address      Initial value   Comment
                         from
  DIREC‐                                                             Take the shortest route to

TION_SHORT                                                           the target position
EST_WAY
  DIREC‐                                                             Always drive in a positive
TION_POSI‐                                                           direction to the target posi‐
TIVE                                                                 tion
  DIREC‐                                                             Always drive in a negative
TION_NEGA‐                                                           direction to the target posi‐
TIVE                                                                 tion
  DIREC‐                                                             If the command is com‐
TION_CUR‐                                                            manded as unbuffered and
RENT                                                                 the axis is moving on a
                                                 straight line during the
                                                 command, then maintain
                                                 this direction until the
                                                 target position is reached.
                                                 In all other cases, take the
                                                 shortest route to the target
                                                 position

Data Layer:
Method: POST
URL:               https://<ip-addr>/automation/api/v2/nodes/motion/axs/
<axs_name>/cmd/pos-abs
Payload:

{
"type":"object","value":
{"axsPos":10,
  "buffered":false,
  "lim":{ "vel":10,
           "acc":10,
           "dec":10,
           "jrkAcc":0,
           "jrkDec":0
           }

}
}

Python:
<cmdID> = motion.axs_cmd_pos_abs( axs=<axsName>,
pos=<targetPos> [,vel=<velocity>] [,acc=<acceleration>]
[,dec=<deceleration>] [,jrk_acc=<jerkAcceleration>]
[,jrk_dec=<jerkDeceleration>] [,buffered=<buffered>]
[,direction<direction>] )

Creates a posAbs command for a single axis (object has to be "attached"), see
documentation Python Runtime App ⮫ Python functions
● <axsName> - string, axis object name
● <pos> - double, target position of a command
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
● <direction> - int, 0-SHORTEST_WAY; 1-POSITIVE_DIR; 2-NEGATIVE_DIR; 3-
  CURRENT_DIR (default is 0)

BundleIF:
To position the axis as absolute, the command type has to be:

cmd::axs::AxsCmdType::AXS_CMD_POS_ABS
//! @brief Create a motion command for a single axis
(AXS_CMD_MOVE_*)
//!
//! @param[in]   sourceInfo Command source information
//! @param[in]   axsName     Name of the motion object
//! @param[in]   cmdType     Type of the command
//! @param[in]   targetPos   Target position of the command
//! @param[in]   dynLim      Dynamic limits of the command
//! @param[in]   buffered    Create as a buffered command
//! @param[out] cmdID        The ID of the added command
//! @return                  Was everything okay?
virtual MotionResult axsPosCmd(const cmd::CmdSourceInfo&
sourceInfo, const char* axsName, cmd::axs::AxsCmdType cmdType,
double targetPos, const cmd::DynamicLimitsT &dynLim, bool
buffered, uint64_t&cmdID) const = 0;

//! @brief Create a motion command for a single axis
(AXS_CMD_MOVE_*)
//!
//! @param[in]   sourceInfo Command source information
//! @param[in]   axsName     Name of the motion object

//! @param[in]   cmdType     Type of the command
//! @param[in]   targetPos   Target position of the command
//! @param[in]   dynLim      Dynamic limits of the command
//! @param[in]   cmdDir      Commanded direction (only used
for PosAbs for modulo axes)
//! @param[in]   buffered    Create as a buffered command
//! @param[out] cmdID        The ID of the added command
//! @return                  Was everything okay?
virtual MotionResult axsPosCmdEx(const cmd::CmdSourceInfo&
sourceInfo, const char* axsName, cmd::axs::AxsCmdType
cmdType, double targetPos, const cmd::DynamicLimitsT
&dynLim, ::motion::core::cmd::CmdPosAbsDir cmdDir, bool
buffered, uint64_t&cmdID) const = 0;

### 7.2.12 AxsPosRel - Relative positioning of the axis

Basics
This target positions the axis as relative by adding the specified position to
the actual position and by using this sum as new target position. As buffered
command, the behavior is identical to a PositionAdditive command. During
the motion, the PLCOpen status of the axis is set to DISCRETE_MOTION.
If the commanded target position is reached, the command status is set to
DONE and the PLCOpen status of the axis is set to STANDSTILL.
Use ML_AxsGetPLCOpenState or ML_GetCmdState to read out the status.
If an error occurs before execution (e.g. violation of the dyn. Limit, invalid
command parameters), the command is not added to the axis object.
If an error occurs during execution, the axis is set to state ERRORSTOP.
If the command is issued as non-buffered command, the previously active
command is canceled, the commands of the preparation buffer are dis‐
carded and the command is executed immediately (with the new commanded
dynamic limit values).
For this function, current has to be applied to the axis (state STANDSTILL).
The programming limit values for velocity, acceleration, deceleration as well
as both jerk limits have to be positive (greater than zero), as otherwise the
parameters would be inconsistent.
Exception: If both jerk limit values are exactly zero, the motion is executed
without jerk limit (trapezoid velocity profile).

PLC:

ML_AxsPosRel
Name        Data type        Inherited    Address       Initial value   Comment
                             from
  Data       ML_AxsPos‐                                                 Output: Command parame‐
             Data                                                       ters

ML_AxsPosRel
BOOL                                                        Returns information
ML_AxsPosR                                                              whether the command can
el                                                                      be added to the axis
object.
● TRUE: The command
  could be added success‐
  fully
● FALSE: An error
  occurred. Details in
  ML_oCmdResult
STRUCT ML_AxsPosData
Name       Data type            Inherited     Address   Initial value   Comment
                                from
   In              ML_iAxsPos                                           Input: Command data of
                                                                        the command
   Out             ML_oCmdRe‐                                           Output parameter of the
                   sult                                                 command
STRUCT ML_iAxsPos EXTENDS ML_iAxsCmdBase
Name        Data type  Inherited   Address              Initial value   Comment
                       from
  AxisName STRING(63) ML_iAxsCmd‐                                       Name of the axis used to
                       Base                                             execute the command
  Source    STRING(50) ML_iAxsCmd‐                                      Specifies the command
                       Base                                             source, e.g PlcApplication1
                                                                        is displayed in the diag‐
                                                                        nostic messages
   SourceLine ULINT             ML_iAxsCmd‐                             Specifies the source line of
                                Base                                    the command; is displayed
                                                                        in the diagnostic messages
   Position        LREAL                                                Commanded relative target
                                                                        position
   Buffered        BOOL                                                 TRUE, if the command is
                                                                        to be executed as a buf‐
                                                                        fered command, otherwise
                                                                        FALSE
   DynLimits ML_iDynLi‐                                                 Limit values of the position
             mits                                                       command
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
URL:               https://<ip-addr>/automation/api/v2/nodes/motion/axs/
<axs_name>/cmd/pos-rel
Payload:

{
"type":"object","value":
{"axsPos":10,
  "buffered":false,
  "lim":{ "vel":10,
           "acc":10,
           "dec":10,
           "jrkAcc":0,
           "jrkDec":0
           }

}
}

Python:
<cmdID> = motion.axs_cmd_pos_rel( axs=<axsName>,
pos=<targetPos> [,vel=<velocity>] [,acc=<acceleration>]
[,dec=<deceleration>] [,jrk_acc=<jerkAcceleration>]
[,jrk_dec=<jerkDeceleration>] [,buffered=<buffered>] )

Generates a posRel command for a single axis (object has to be "attached"),
see documentation Python Runtime App ⮫ Python functions
● <axsName> - string, axis object name
● <pos> - double, target position of a command
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
To position the axis as relative, the command type has to be as follows:

cmd::axs::AxsCmdType::AXS_CMD_POS_REL
//! Create a motion command for a single axis (AXS_CMD_MOVE_*)
//!
//! @param[in]   sourceInfo Command source information
//! @param[in]   axsName     Name of the motion object
//! @param[in]   cmdType     Type of the command
//! @param[in]   targetPos   Target position of the command
//! @param[in]   dynLim      Dynamic limits of the command
//! @param[in]   buffered    Create as a buffered command
//! @param[out] cmdID        The ID of the added command
//! @return                  Was everything okay?
virtual MotionResult axsPosCmd(const cmd::CmdSourceInfo&
sourceInfo, const char* axsName, cmd::axs::AxsCmdType cmdType,
double targetPos, const cmd::DynamicLimitsT &dynLim, bool
buffered, uint64_t &cmdID) const = 0;

### 7.2.13 AxsPosAdd - Additive positioning of the axis

Basics
This command positions the axis as additive by adding the specified position
to the previous target position and by using the specified position as new
target position. During the motion, the PLCOpen status of the axis is set
to DISCRETE_MOTION. If the commanded target position is reached, the com‐
mand status is set to DONE and the PLCOpen status of the axis is set to
STANDSTILL.
Use ML_AxsGetPLCOpenState or ML_GetCmdState to read out the status.
If an error occurs before the execution (e.g. violation of the dynamic limit,
invalid command parameters), the command is not added to the axis object.
If an error occurs during execution, the axis is set to state ERRORSTOP.
If the command is issued as non-buffered command, the previously active
command is canceled, the commands of the preparation buffer are dis‐
carded and the command is executed immediately (with the new commanded
dynamic limit values).
For this function, current has to be applied to the axis (state STANDSTILL).
The programming limit values for velocity, acceleration, deceleration as well
as both jerk limits have to be positive (greater than zero), as otherwise the
parameters would be inconsistent.
Exception: If both jerk limit values are exactly zero, the motion is executed
without jerk limit (trapezoid velocity profile).

PLC:

ML_AxsPosAdd
Name       Data type            Inherited     Address   Initial value   Comment
                                from
  Data      ML_AxsPos‐                                                  Output: Command parame‐
            Data                                                        ters

  ML_AxsPo‐ BOOL                                                        Returns information
sAbs                                                                    whether the command can
be added to the axis
object.
● TRUE: The command
  could be added success‐
  fully
● FALSE: An error
  occurred. Details in
  ML_oCmdResult
STRUCT ML_AxsPosData
Name       Data type            Inherited     Address   Initial value   Comment
                                from
  In             ML_iAxsPos                                             Input: Command data of
                                                                        the command
  Out            ML_oCmdRe‐                                             Output parameter of the
                 sult                                                   command
STRUCT ML_iAxsPos EXTENDS ML_iAxsCmdBase
Name        Data type  Inherited   Address              Initial value   Comment
                       from
  AxisName STRING(63) ML_iAxsCmd‐                                       Name of the axis used to
                       Base                                             execute the command
  Source    STRING(50) ML_iAxsCmd‐                                      Specifies the command
                       Base                                             source, e.g PlcApplication1
                                                                        is displayed in the diag‐
                                                                        nostic messages
  SourceLine ULINT              ML_iAxsCmd‐                             Specifies the source line of
                                Base                                    the command; is displayed
                                                                        in the diagnostic messages
  Position       LREAL                                                  Commanded additive
                                                                        target position
  Buffered       BOOL                                                   TRUE, if the command is
                                                                        to be executed as a buf‐
                                                                        fered command, otherwise
                                                                        FALSE
  DynLimits ML_iDynLi‐                                                  Limit values of the position
            mits                                                        command

STRUCT ML_iDynLimits
Name        Data type            Inherited   Address    Initial value   Comment
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
Name       Data type             Inherited   Address    Initial value   Comment
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

Data Layer:
Method: POST
URL:               https://<ip-addr>/automation/api/v2/nodes/motion/axs/
<axs_name>/cmd/pos-add
Payload:

{
"type":"object","value":
{"axsPos":10,
  "buffered":false,
  "lim":{ "vel":10,
           "acc":10,
           "dec":10,
             "jrkAcc":0,
             "jrkDec":0
           }

}
}

Python:
<cmdID> = motion.axs_cmd_pos_add( axs=<axsName>,
pos=<targetPos> [,vel=<velocity>] [,acc=<acceleration>]
[,dec=<deceleration>] [,jrk_acc=<jerkAcceleration>]
[,jrk_dec=<jerkDeceleration>] [,buffered=<buffered>] )

Generates a posAdd command for a single axis (object has to be "attached"),
see documentation Python Runtime App ⮫ Python functions
● <axsName> - string, axis object name
● <pos> - double, target position of a command
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
To position the axis as additive, the command type has to be as follows:

cmd::axs::AxsCmdType::AXS_CMD_POS_ADD
//! Create a motion command for a single axis (AXS_CMD_MOVE_*)
//!
//! @param[in]     sourceInfo    Command source information
//! @param[in]     axsName       Name of the motion object
//! @param[in]     cmdType       Type of the command
//! @param[in]     targetPos     Target position of the command
//! @param[in]     dynLim        Dynamic limits of the command
//! @param[in]     buffered      Is buffered mode?
//! @param[out]    cmdID         The ID of the added command
//! @return                      Was everything okay?
virtual MotionResult axsPosCmd(const cmd::CmdSourceInfo&
sourceInfo, const char* axsName, cmd::axs::AxsCmdType cmdType,
double targetPos, const cmd::DynamicLimitsT &dynLim, bool
buffered, uint64_t &cmdID) const = 0;

### 7.2.14 AxsJogIncr - Incremental axis jogging

Basics
This command incrementally jogs the axis with the specified distance and the
commanded dynamic limits.
The command moves the axis in a certain direction (positive or negative). The
length for possible motions is always limited by the configured permissible
axis ranges. If the current position is outside the configured, permissible axis
range, the axis can move towards the permitted range but cannot move away
from the range.
The command moves the axis maximally around the specified increment (posi‐
tive or negative).

● Jogging of the axis is only permitted if the axis is in state STANDSTILL
● The current axis velocity is NULL
● No command is active for the axis
The programming limit values for velocity, acceleration, deceleration as well
as both jerk limits have to be positive (greater than zero), as otherwise the
parameters would be inconsistent.
Exception: If both jerk limit values are exactly zero, the motion is executed
without jerk limit (trapezoid velocity profile).

PLC:

ML_AxsJogIncr
Name        Data type          Inherited     Address      Initial value   Comment
                               from
   Data     ML_AxsJo‐                                                     Output: Command parame‐
            gIncrData                                                     ters
  ML_AxsJo‐ BOOL                                                          Returns information
gIncr                                                                     whether the command can
                                                                          be added to the axis
                                                                          object.
                                                                          ● TRUE: The command
                                                                            could be added success‐
                                                                            fully
                                                                          ● FALSE: An error
                                                                            occurred. Details in
                                                                            ML_oCmdResult
STRUCT ML_AxsJogIncrData
Name       Data type     Inherited           Address      Initial value   Comment
                         from
  In       ML_iAxsJo‐                                                     Input: Command data of
           gIncr                                                          the command
  Out      ML_oCmdRe‐                                                     Output parameter of the
           sult                                                           command
STRUCT ML_iAxsJogIncr EXTENDS ML_iAxsCmdBase
Name        Data type    Inherited  Address               Initial value   Comment
                         from
  AxisName STRING(63) ML_iAxsCmd‐                                         Name of the axis used to
                         Base                                             execute the command
  Source    STRING(50) ML_iAxsCmd‐                                        Specifies the command
                         Base                                             source, e.g PlcApplication1
                                                                          is displayed in the diag‐
                                                                          nostic messages
   SourceLine ULINT            ML_iAxsCmd‐                                Specifies the source line of
                               Base                                       the command; is displayed
                                                                          in the diagnostic messages
   Increment LREAL                                                        Distance of incremental jog
                                                                          command

STRUCT ML_iAxsJogIncr EXTENDS ML_iAxsCmdBase
  PosDir    BOOL                                                      TRUE indicates a positive
                                                 direction of motion, FALSE
                                                 indicates a negative direc‐
                                                 tion of motion
  DynLimits ML_iDynLi‐                                                Limit values for the jog
mits                                                      command
STRUCT ML_iDynLimits
Name        Data type        Inherited   Address      Initial value   Comment
                             from
   Velocity    LREAL                                                  Velocity limit value

   Accelera‐   LREAL                                                  Acceleration limit value
tion
   Decelera‐   LREAL                                                  Deceleration limit value
tion
   JerkAcc     LREAL                                                  Jerk limit value for acceler‐
                                                 ation phase
  JerkDec      LREAL                                                  Jerk limit value for deceler‐
                                                 ation phase
STRUCT ML_oCmdResult
Name       Data type         Inherited   Address      Initial value   Comment
                             from
  CmdID        ULINT                                                  Command ID (is set to
                                                                      18446744073709551615 in
                                                                      the event of an error)
  Error        BOOL                                                   Error ID TRUE indicates
                                                                      that an error occurred
  ErrorID      UDINT                                                  Specifies the type of
                                                                      occurred error: The upper
                                                                      4 bytes reflect the main
                                                                      diagnostics, the lower 4
                                                                      bytes reflect the detailed
                                                                      diagnostics, 0 means no
                                                                      error

Data Layer:
Method: POST
URL:                https://<ip-addr>/automation/api/v2/nodes/motion/axs/
<axs_name>/cmd/jog-incr
Payload:

{
"type":"object","value":
{
  "jogDir":"+",
  "jogIncrement":10,
  "lim":{ "vel":10,
           "acc":10,
           "dec":10,
             "jrkAcc":0,
             "jrkDec":0
           }

}
}

Python:
<cmdID> = motion.axs_cmd_jog_incr( axs=<axsName>,
dir=<direction>, incr=<increment> [,vel=<velocity>]
[,acc=<acceleration>] [,dec=<deceleration>]
[,jrk_acc=<jerkAcceleration>] [,jrk_dec=<jerkDeceleration>] )

Generates an incremental jog command for a single axis (object has to be
"attached"), see documentation Python Runtime App ⮫ Python functions
●   <axsName> - string, axis object name
●   <dir> - string, + or - jogging direction
●   <incr> - double, increment to be moved
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
//! Create a nonbuffered jog command for a single axis
(AXS_CMD_JOG_INCR)
//!
//! @param[in] sourceInfo    Command source information
//! @param[in] axsName       Name of the motion object
//! @param[in] cmdType       Type of the command
( AXS_CMD_JOG_ABS/ AXS_CMD_JOG_REL )
//! @param[in] jogDir        Jog direction (+/-) of the command
//! @param[in] jogIncrement Positive incremental jog distance
( only AXS_CMD_JOG_REL )
//! @param[in] dynLim        Dynamic limits of the command
//! @param[out] cmdID        The ID of the added command
//! @return                  Was everything okay?
virtual MotionResult axsJogCmd(const cmd::Cmd-SourceInfo&
sourceInfo, const char* axsName, cmd::axs::AxsCmdType
cmdType, cmd::CmdJogDir jogDir, double jogIncrement, const
cmd::DynamicLimitsT &dynLim, uint64_t&cmdID) const = 0;

with the following data types:

//! @brief Data container for dynamic limits
 struct DynamicLimitsT
 {
   double m_vel = 0.0;    //!<velocity limit

  double m_acc = 0.0;     //!<acceleration limit
  double m_dec = 0.0;     //!<deceleration limit
  double m_jrkAcc = 0.0; //!<jerk limit while accelerating
  double m_jrkDec = 0.0; //!<jerk limit while decelerating
  double m_jrkAcc2 = 0.0; //!<second jerk limit while
accelerating (not used)
  double m_jrkDec2 = 0.0; //!<second jerk limit while
decelerating (not used)
 };

cmdType has to be: AxsCmdType::AXS_CMD_JOG_REL (for incremental jog‐
ging)

Please note: m_jrkAcc2 and m_jrkDec2 is currently not supported and has to
be set to 0.

### 7.2.15 AxsJogCont - Continuous axis jogging

Basics
This command continuously jogs an axis.
The command moves an axis in a certain direction (positive or negative). The
length for possible motions is always limited by the configured permissible
axis ranges. If the current position is outside the configured, permissible axis
range, the axis can move towards the permitted range but cannot move away
from the range.
AxsJogCont moves the axis in a certain direction (positive or negative).
To cancel the motion of the AxsJogCont command, use commando AxsAbort.
● Jogging of the axis is only permitted if the axis is in state STANDSTILL
● The axis velocity has to be NULL.
● No command can be active for the axis
The programming limit values for velocity, acceleration, deceleration as well
as both jerk limits have to be positive (greater than zero), as otherwise the
parameters would be inconsistent.
Exception: If both jerk limit values are exactly zero, the motion is executed
without jerk limit (trapezoid velocity profile).

PLC:

ML_AxsJogCont
Name       Data type         Inherited    Address        Initial value   Comment
                             from
 Data        ML_AxsJog‐                                                  Output: Command parame‐
             ContData                                                    ters

ML_AxsJogCont
  ML_Axs‐  BOOL                                                    Returns information
JogCont                                                            whether the command can
be added to the axis
object.
● TRUE: The command
  could be added success‐
  fully
● FALSE: An error
  occurred. Details in
  ML_oCmdResult
STRUCT ML_AxsJogContData
Name       Data type   Inherited         Address   Initial value   Comment
                       from
  In       ML_iAxsJog‐                                             Input: Command data of
           Cont                                                    the command
  Out      ML_oCmdRe‐                                              Output parameter of the
           sult                                                    command
STRUCT ML_iAxsJogCont EXTENDS ML_iAxsCmdBase
Name        Data type   Inherited  Address         Initial value   Comment
                        from
  AxisName STRING(63) ML_iAxsCmd‐                                  Name of the axis used to
                        Base                                       execute the command
  Source    STRING(50) ML_iAxsCmd‐                                 Specifies the command
                        Base                                       source, e.g PlcApplication1
                                                                   is displayed in the diag‐
                                                                   nostic messages
   SourceLine ULINT        ML_iAxsCmd‐                             Specifies the source line of
                           Base                                    the command; is displayed
                                                                   in the diagnostic messages
   PosDir          BOOL                                            TRUE indicates a positive
                                                                   direction of motion, FALSE
                                                                   indicates a negative direc‐
                                                                   tion of motion
   DynLimits ML_iDynLi‐                                            Limit values for the jog
             mits                                                  command
STRUCT ML_iDynLimits
Name        Data type      Inherited     Address   Initial value   Comment
                           from
   Velocity        LREAL                                           Velocity limit value
   Accelera‐       LREAL                                           Acceleration limit value
tion
   Decelera‐       LREAL                                           Deceleration limit value
tion
   JerkAcc         LREAL                                           Jerk limit value for acceler‐
                                                                   ation phase
   JerkDec         LREAL                                           Jerk limit value for deceler‐
                                                                   ation phase
STRUCT ML_oCmdResult
Name       Data type       Inherited     Address   Initial value   Comment
                           from

STRUCT ML_oCmdResult
  CmdID    ULINT                                                       Command ID (is set to
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
URL: https://<ip-addr>/automation/api/v2/nodes/motion/axs/<axs_name>/jog-
cont
Payload:

{
"type":"object","value":
{
  "jogDir":"+",
  "lim":{ "vel":10,
           "acc":10,
           "dec":10,
           "jrkAcc":0,
           "jrkDec":0
                  }

}
}

Python:
<cmdID> = motion.axs_cmd_jog_cont( axs=<axsName>,
dir=<direction>, [,vel=<velocity>] [,acc=<acceleration>]
[,dec=<deceleration>] [,jrk_acc=<jerkAcceleration>]
[,jrk_dec=<jerkDeceleration>] )

Generates a continuous jog command for a single axis (object has to be
"attached"), see documentation Python Runtime App ⮫ Python functions
● <axsName> - string, axis object name
● <dir> - string, + or - jogging direction
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
//! Create a nonbuffered jog command for a single axis
(AXS_CMD_JOG_CONT)
//!
//! @param[in] sourceInfo    Command source information
//! @param[in] axsName       Name of the motion object
//! @param[in] cmdType       Type of the command
( AXS_CMD_JOG_ABS/ AXS_CMD_JOG_REL )
//! @param[in] jogDir        jog direction (+/-) of the command
//! @param[in] jogIncrement positive incremental jog distance
( only AXS_CMD_JOG_REL )
//! @param[in] dynLim        Dynamic limits of the command
//! @param[out] cmdID        The ID of the added command
//! @return                  Was everything okay?
virtual MotionResult axsJogCmd(const cmd::Cmd-SourceInfo&
sourceInfo, const char* axsName, cmd::axs::AxsCmdType
cmdType, cmd::CmdJogDir jogDir, double jogIncrement, const
cmd::DynamicLimitsT &dynLim, uint64_t&cmdID) const = 0;

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

cmdType has to be: AxsCmdType::AXS_CMD_JOG_ABS (for continous jogging)
Please note: m_jrkAcc2 and m_jrkDec2 is currently not supported and has to
be set to 0.

### 7.2.16 AxsCyclicSetPoint, SetCyclicSetPoint - Cyclic command value

General information
The user can implement individual Motion profiles and cyclically send the
command value to the drive with this function.

The function consists of two parts:
● AxsCyclicSetPoint is an unbuffered Motion command that cyclically sends
   the external command value of an axis directly to the drive.
● SetCyclicSetPoint is a Motion system interface which is used to update the
   external command value of the axis in a real-time bundle or in a PLC task
   whose cycle time is equal to the Motion kernel.
   First, enable the function with the AxsCyclicSetPoin command The axis has
   to be in the STANDSTILL state. Subsequently, the command value can be
   updated with the SetCyclicSetPoint command.
After the AxsCyclicSetPoint command is active:
● The axis remains on the current position until the external command value
  is changed

● The axis is always in the DISCRETE_MOTION state, also if the axis velocity
  is zero
● The AxsCyclicSetPoint command can only be stopped by the axsAbort com‐
  mand
● The axis runs into the error state and stops the motion if its dynamic
  limits (position/velocity/acceleration, deceleration) exceed the configura‐
  tion values
● The AxsInterrupt and AxsContinue commands do not work in this case
● The command cannot be influenced by “Override”

Interface
PLC:

ML_AxsCyclicSetPoint
Name         Data type       Inherited      Address        Initial value   Comment
                             from
  Data       ML_AxsCy‐                                                     IN/OUT data
             clicSetPoint‐
             Data
   ML_AxsCy‐ BOOL                                                          Returns if the command
clicSetPoint                                                               value has been changed
                                                                           successfully
                                                                           ● TRUE: The command
                                                                             value has been changed
                                                                             successfully
                                                                           ● FALSE: An error
                                                                             occurred. Details in
                                                                             ML_oStateBase (data)
STRUCT ML_AxsCyclicSetPointData
Name         Data type    Inher‐         Addres Initial    Comment
                          ited           s      value
                          from
  In         ML_iAxsCmd                                    Input: Command data of the command
             Base

STRUCT ML_AxsCyclicSetPointData
  Out        ML_oCm‐                                          Output: Command parameters
dResult
STRUCT ML_iAxsCmdBase
Name          Data type           Inher‐     Addres Initial   Comment
                                  ited       s      value
                                  from
   AxisName         STRING(63)                                Name of the axis used to execute the com‐
                                                              mand
   Source           STRING(50)                                Specifies the command source, e.g PlcAp‐
                                                              plication1 is displayed in the diagnostic
                                                              messages
   SourceLine       ULINT                                     Specifies the source line of the command;
                                                              is displayed in the diagnostic messages
STRUCT ML_oStateBase
Name       Data type             Inherited      Address        Initial value   Comment
                                 from
   CmdID           ULINT                                                       Command ID (is set to
                                                                               18446744073709551615 in
                                                                               the event of an error)
   Error           BOOL                                                        Error ID TRUE indicates
                                                                               that an error occurred
   ErrorID         ULINT                                                       Specifies the type of
                                                                               occurred error: The upper
                                                                               4 bytes reflect the main
                                                                               diagnostics, the lower 4
                                                                               bytes reflect the detailed
                                                                               diagnostics, 0 means no
                                                                               error

System interface

ML_SetCyclicSetPoint
Name         Data type       Inherited      Address        Initial value   Comment
                             from
  Data       ML_SetCy‐                                                     IN/OUT data

clicSetPoint‐
Data
   ML_SetCy‐ BOOL                                                          Returns information
clicSetPoint                                                               whether the command can
                                                be added to the axis
                                                object.
                                                ● TRUE: The command
                                                  could be added success‐
                                                  fully
                                                ● FALSE: An error
                                                  occurred. Details in
                                                  ML_oStateBase (data)
STRUCT ML_SetCyclicSetPointData
Name         Data type    Inher‐         Addres Initial   Comment
                          ited           s      value
                          from
  In         ML_iSetCy‐                                   Input: Command data of the command
             clicSetPoint
  Out        ML_oState‐                                   Output: Command parameters
             Base
STRUCT ML_iSetCyclicSetPoint EXTENDS
Name         Data type     Inher‐  Addres Initial         Comment
                           ited    s      value
                           from
  AxisName   STRING(15) ML_iAxs                           Name of the axis used to execute the com‐
                           CmdBas                         mand
                           e
  Source     STRING(50) ML_iAxs                           Specifies the command source, e.g PlcAp‐
                           CmdBas                         plication1 is displayed in the diagnostic
                           e                              messages
  SourceLine ULINT         ML_iAxs                        Specifies the source line of the command;
                           CmdBas                         is displayed in the diagnostic messages
                           e
  Value      LREAL

STRUCT ML_oStateBase
Name       Data type             Inherited   Address      Initial value   Comment
                                 from
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
URL:               https://<ip-addr>/automation/api/v2/nodes/motion/axs/
<axs_name>/cmd/cyclic-set-point
Payload:

{
"type":"object","value":
{
"buffered":false
}
}

The "buffered" value should always be "false""FALSE".

Python:
<cmdID> = motion.axs_cyclic_set_point (axs=<axsName>)

Generates a cyclical command value command for a single axis (object has to
be "attached"), see documentation Python Runtime App ⮫ Python functions.
● <axsName> - string, axis name

BundleIF:
//! @brief Create a motion command for a single axis (Cyclic
setpoint)
//!
//! @param[in]     handle        Handle of the interface
//! @param[in]     sourceInfo    Command source information
//! @param[in]     axsName       Name of the axis
//! @param[out]    cmdID         The ID of the added command
//! @return                      Was everything okay?
motion::core::MotionResult axsCyclicSetPointCmd(void* handle,
const
motion::core::dia::CmdSourceInfo & sourceInfo, const char*
axsName, uint64_t & cmdID);

//! @brief This method sets the external set point of the axis.
//! @param[in]    handle        Handle of the interface
//! @param[in]    axsName       Name of the axis
//! @param[out]   setPoint      Cyclic ipo position from
external set point generator

//! @return                     Was everything okay?
motion::core::MotionResult setAxisCyclicSetPoint( void*
handle, const char* axsName, double setPoint );

Further information
● See ⮫ MB_CyclicSetPoint

### 7.2.17 AxsSetIpoPosFromActPos - Setting the interpolator position to

the actual axis value
Basics
This command is used to reset the position of the control command in the
interpolator to the active position of the axis. A "STANDSTILL" check is per‐

formed at the start of the execution.
The current position is determined and set to the IPO position. IPO velocity,
acceleration and jerk are set to 0 for this purpose. The last active command is
aborted.

PLC:

ML_AxsSetIpoPosFromActPos
Name         Data type   Inherited        Address       Initial value   Comment
                         from
   Data      ML_AxsSetI‐                                                Command parameters
             poPosFro‐
             mActPosData
   ML_AxsSe‐ BOOL                                                       Returns information
tIpoPosFro‐                                                             whether the command can
mActPos                                                                 be added to the axis
                                                                        object.
                                                                        ● TRUE: The command
                                                                          could be added success‐
                                                                          fully
                                                                        ● FALSE: An error
                                                                          occurred. Details in
                                                                          ML_oCmdResult
STRUCT ML_AxsSetIpoPosFromActPosData
Name       Data type    Inherited   Address             Initial value   Comment
                        from
  In       ML_iAxsSetI‐                                                 Input: Command data of
           poPosFro‐                                                    the command
           mActPos
  Out      ML_oCmdRe‐                                                   Output: Command parame‐
           sult                                                         ters
STRUCT ML_iAxsSetIpoPosFromActPos EXTENDS ML_iAxsCmdBase
Name        Data type   Inherited   Address     Initial value           Comment
                        from

STRUCT ML_iAxsSetIpoPosFromActPos EXTENDS ML_iAxsCmdBase
  AxisName STRING(15) ML_iAxsCmd‐                                         Name of the axis used to
 Base                                              execute the command
  Source    STRING(50) ML_iAxsCmd‐                                        Specifies the command
 Base                                              source, e.g PlcApplication1
                                                   is displayed in the diag‐
                                                   nostic messages
   SourceLine ULINT              ML_iAxsCmd‐                              Specifies the source line of
          Base                                     the command; is displayed
                                                   in the diagnostic messages
   Buffered        BOOL                                                   TRUE, if the command is
                                                   to be executed as a buf‐
                                                   fered command, otherwise
                                                   FALSE
STRUCT ML_oCmdResult
Name       Data type             Inherited     Address    Initial value   Comment
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
URL:                https://<ip-addr>/automation/api/v2/nodes/motion/axs/
<axs_name>/cmd/set-ipo-pos-from-act-pos
Payload:
{
"type":"object","value":
{
"buffered":false
}
}

Python:
<cmdID> =
motion.axs_cmd_set_ipo_pos_from_act_pos(axs=<axsName>,
buffered=<buffered>)

Create a command to set the IPO position from the act position command for
a single axis (object has to be "attached"), see Python Runtime App ⮫ Python
functionsdocumentation.
● <axsName> - string, axis object name
● <buffered> - bool, use TRUE if the command is to be buffered (TRUE by
  default)

BundleIF:
//! @brief Create a set ipo position from act position command
for a single axis (SetIpoPosFromActPos)
//!
//! @param[in] handle       Handle of the interface
//! @param[in] sourceInfo Command source information
//! @param[in] axsName      Name of the motion object
//! @param[in] buffered     Is buffered mode?
//! @param[out] cmdID       The ID of the added command
//! @return                 Status of the function call:
                            STS_OK or an error code on failure
::motion::core::MotionResult(*axsSetIpoPosFromActPos)(void*
handle, const ::motion::core::dia::CmdSourceInfo& sourceInfo,

const char* axsName, bool buffered, uint64_t &cmdID);

### 7.2.18 AxsGetSyncMotionState - Synchronization state

PLC:
This function block outputs the current synchronization status of an axis
object.

Table 60: ML_AxsGetSyncMotionState
STRUCT ML_AxsGetSyncMotionData
Name       Data type   Inherited         Address      Initial value   Comment
                       from
  In       ML_iAxsSta‐                                                Input: Input data of the
           teBase                                                     command
  Out      ML_oAxsGet‐                                                Output: Synchronization
           SyncMotion‐                                                state of the axis
           State
ENUM ML_SyncMotionState
Name       Data type    Inherited        Address      Initial value   Comment
                        from
           INT                                                        No Sync-Motion command
NO_SYNC_M                                                             active
OTION
           INT                                                        The slave axis is synchron‐
SYNCHRON‐                                                             ized with the master axis
IZED                                                                  and uses the values calcu‐
                                                                      lated by the pipeline.
  INI‐      INT                                                       Initial synchronization state
TIAL_DYN_SY                                                           when the axis starts a
NCHRO‐                                                                sync motion command;
NIZING                                                                the axis moves unsynchron‐
                                                                      ized towards the command
                                                                      values of the calculation
                                                                      pipeline

ENUM ML_SyncMotionState
  DYN_SYN‐ INT                                                                        The axis is resynchronized
CHRONIZING                                                                            because it has lost its
                                                             synchronized state
INT                                                                Coupling error occurred
SYNC_ERRO
R
STRUCT ML_iAxsStateBase
Name        Data type   Inherited               Address               Initial value   Comment
                        from
  AxisName STRING(15)                                                                 Axis name from which the
                                                                                      status is to be queried
STRUCT ML_oAxsGetSyncMotionState EXTENDS ML_oStateBase
Name       Data type   Inherited    Address    Initial value                          Comment
                       from
  Error    BOOL        ML_oState‐                                                     Error flag, TRUE means
                       Base                                                           that an error has occurred
                                                                                      (e.g. typing error in the
                                                                                      object name)
   ErrorID         ULINT           ML_oState‐                                         Specifies the error type.
                                   Base                                               The upper four bytes refer
                                                                                      to the main diagnostics,
                                                                                      the lower four bytes to
                                                                                      the detailed diagnostics). 0
                                                                                      indicates “no error”.
   State           ML_SyncMo‐                                                         The current state of the
                   tionState                                                          synchronized motion

### 7.2.19 AxsGearInPos - Synchronizing to position

Basics
GearInPos belongs to a group of synchronized Motion functions that behave
like a gearbox. The GearInPos commands control the slave axis in the "Posi‐
tion" function on the drive and use the position of the master axis. As a result,
the position of the slave axis (y) is proportional to the position of the master
axis (x) with the specified ratio (r) and optionally with a position offset, see
Fig. 253. This is defined by the equation y = rx + offset, which can be
represented by a red line in the master/slave plane.
      y

                            (masterOffset , slaveOffset)

                        r

The offsets of the master axis and the slave axis are selected so that the coor‐
dinate (masterOffset, slaveOffset) is on the red line. Therefore, the equation
can be written as follows:

                                       _ masterOffset
            y =    r   * ( x                          ) + slaveOffset

The described formula is a basic equation. The functionality of the synchron‐
ized Motion GearInPos is extended by several parameters, for example secon‐
dOrderInterpolatedOffset and firstOrderFilteredOffset. These parameters can

be set via the Data Layer RT.
The master/slave relationship is clearly defined, provided that masterOffset
and slaveOffset are defined. This is not the case with a modulo axis. If the
master axis is a modulo axis with the modulo value p, the positions master‐
Offset and masterOffset + n * p are equivalent. The master/slave relationship
can be drawn as follows in the master/slave level.
        y

                       (masterOffset , slaveOffset)   (masterOffset , slaveOffset)   (masterOffset , slaveOffset)

                   r                            r                              r

The transmission ratio (r) is expressed by a rational number and optionally
a percentage correction, which is referred to as fineAdjust. FineAdjust can be
specified with the GearInPos command and via the Data Layer RT.

                   ratioNumerator                                            fineAdjust
        r =
                  ratioDenominator                     *     (1 +               100
After the GearInPos command, the axis remains in the gearing function. To
end the command, the command has to be canceled. For example, by a cancel
command or by a new, non-buffered Motion command. A new command of
the GearInPos command results in the axis not being synchronized when the
command becomes active.

Functional description of GearInPos
GearInPos are Motion commands for axes that are based on the functionality
of synchronized Motion.

GearInPos can be buffered and non-buffered. The commanded axis becomes a
slave axis in relation to a specified master axis. This command sets the slave
axis to the PLCopen state SYNCHRONIZED MOTION. While the command is
ACTIVE, the position of the slave axis follows the position of the master axis.
Before the master axis and the slave axis are moved synchronously, the slave
axis first has to execute a motion so that the master/slave position reference
can be established and maintained. This motion is realized with the dynamic
synchronization functionality. How the dynamic synchronization is executed is
defined by SyncMode, and additionally for a slave axis by DynSyncDirection.
● If an absolute position reference between the master and slave axes is not
    required, the SYNC_RELATIVE SyncMode can be selected. In this case, a
    position difference between the master and slave axes remains the same
    from the start of the command
● If a position difference between the master and slave axis is to be adjusted,
    i.e. position synchronization, the SYNC_ABSOLUTE SyncMode has to be
    selected
If the slave axis is a modulo axis and dynamic synchronization is active, the
slave axis attempts to synchronize to the target position with the lowest
number of revolutions if the slave axis is a rotary axis, or with the lowest
number of modulo ranges if the slave axis is a linear axis.
If the master axis is a modulo axis and the SyncMode SYNC_ABSOLUTE is
selected, several lines can be tracked in the master/slave level, see ⮫ Func‐
tional description of GearInPos on page 387. The DynSyncDirection command
parameter can be used to select a specific line, see ⮫ Chapter Dynamic syn‐
chronization on page 115 for more information.
If the master axis is a modulo axis, the master axis position is the continu‐
ously (linearized) offset master axis position since the start of the command.
For example, if the modulo value of the master axis is 100 and the GearInPos
command starts at master axis position 60, the initial position is 60. However,
if the master axis is moved over a distance of +220 (2.2 times the modulo
distance), the master axis position is (60 + 220) mod 100 = 80, and the
master axis position in the GearInPos calculation pipeline is 60 + 220 = 280.
While the GearInPos command is active, the command ensures that the
motion of the slave axis does not violate any restrictions for maximum
velocity, maximum acceleration and maximum jerk. Due to these restrictions,
it is possible that the slave axis cannot follow the master axis. For example,
if the slave axis has to move faster than the maximum velocity specification
allows. The violation of a constraint condition leads to a reaction defined by
the configured dynamic synchronization error reaction, see ⮫ Chapter 6.2.1
Synchronized Motion on page 84.
If you want to achieve synchronization with a specific master position, use
GearInPos2.
Synchronization to a specified master position and a fixed synchronization
direction should be performed while the slave axis is stationary. If the slave
axis is rotating, the axis may rotate backward.
The following GearInPos commands are available:
●   AxsGearInPosCmd
●   AxsGearInPosCmdEx
●   AxsGearInPosCmd2
●   AxsGearInPosCmd2Ex

   PLC:

Starting with version 4.2, the GearInPos command was expanded to include
the "MasterSyncPosition" and "MasterStartPosition" parameters. For compati‐
bility reasons, the previous command functions "ML_AxsGearInPos" and data
types for GearInPos from the "CXA_Motion" PLC library, as well as the
new function "ML_AxisGearInPos2," are available. Preferably, the ML_AxsGear‐
InPos2 function and the corresponding data types should be used.

In the PLC library CXA_PLCopen and in the CXA_MotionInterface, the existing
function blocks and structures have been extended to be compatible.
Table 61: ML_AxsGearInPos
STRUCT ML_AxsGearInPosData
Name       Data type    Inherited         Address       Initial value   Comment
                        from
  In       ML_iAxsGear‐                                                 Input: Command data of
           InPos                                                        the command
  Out      ML_oCmdRe‐                                                   Output: Command parame‐
           sult                                                         ters
ENUM ML_SyncMode
Name            Data         Inherited    Address      Initial value    Comment
                type         from
  SYNC_RELATIVE INT                                                     Execute the slave axis and
                                                                        initialize the pipeline
  SYNC_RELA‐         INT                                                Execute the slave axis rel‐
TIVE_KEEP_STATE                                                         atively and maintain the
                                                                        status of the pipeline
  SYNC_ABSO‐         INT                                                Use the absolute result of
LUTE                                                                    the calculation pipeline for
                                                                        the slave axis and initialize
                                                                        the pipeline
  SYNC_ABSO‐    INT                                                     Use of the absolute result
LUTE_KEEP_STATE                                                         of the calculation pipeline
                                                                        for the slave axis and reten‐
                                                                        tion of the pipeline status
ENUM ML_SyncSource
Name       Data type         Inherited    Address       Initial value   Comment
                             from
  SYNC_SET‐ INT                                                         Synchronization based on
POINT                                                                   the command value of the
                                                                        master axis(es)
              INT                                                       Synchronization based on
SYNC_ACTUA                                                              the current value of the
L                                                                       master axis(es)
Enum ML_Dyn‐
SyncDirection
Name          Data type          Inherited from   Address         Initial value     Comment

Enum ML_Dyn‐
SyncDirection
SHORTEST_WA INT                                                                        Initiating syn‐
Y                                                                                      chronization via
                                                               the shortest
                                                               path
POSITIVE            INT                                                                Synchronization
                                                               in positive
                                                               direction
NEGATIVE            INT                                                                Synchronization
                                                               in negative
                                                               direction
DIRECT              INT                                                                Direct transfer
                                                               of the synchro‐
                                                               nization differ‐
                                                               ence between
                                                               master and
                                                               slave
STRUCT ML_iAxsGearInPosParameters
Name         Data type  Inherited             Address   Initial value   Comment
                        from
  Master‐    LREAL                                      0.0             Master offset
Offset
  Slave‐     LREAL                                      0.0             Slave offset
Offset
  RatioNum‐ DINT                                        1               Ratio numerator
erator
  RatioDeno‐ DINT                                       1               Ratio denominator
minator
  FineAdjust LREAL                                      0.0             Fine adjust
STRUCT ML_iAxsGearInPos EXTENDS ML_iAxsCmdBase
Name        Data type   Inherited   Address    Initial value            Comment
                        from
  AxisName STRING(63) ML_iAxsCmd‐                                       Name of the axis used to
                        Base                                            execute the command
  Source    STRING(50) ML_iAxsCmd‐                                      Specifies the source of
                        Base                                            the command, e.g. PlcAp‐
                                                                        plication1. Appears in diag‐
                                                                        nostic messages
   SourceLine ULINT             ML_iAxsCmd‐                             Displays the source line of
                                Base                                    the command. Is displayed
                                                                        in diagnostic messages
  Master‐          STRING(15)                                           Name of the master axis
Name                                                                    that is being followed
  Syn‐             ML_Syn‐                                              Synchronization source
cSource            cSource

STRUCT ML_iAxsGearInPos EXTENDS ML_iAxsCmdBase
  SyncMode ML_Syn‐                                                Function of
cMode                                                 the synchronization
                                             command: SYNC_ABSO‐
                                             LUTE, SYNC_RELA‐
                                             TIVE, SYNC_ABSO‐
                                             LUTE_KEEP_STATE,
                                             SYNC_RELA‐
                                             TIVE_KEEP_STATE
   DynSync‐   ML_DynSync‐                                         Direction of synchroniza‐
Direction     Direction                                           tion
   Parame‐    ML_iAxsGear‐                                        Parameters for the Gear‐

ters          InPosPara‐                                          InPos command
meters
  Buffered    BOOL                                                TRUE, if the command is
                                             to be executed as a buf‐
                                             fered command, otherwise
                                             FALSE

Data Layer
Method: POST
URL: motion/axs/<axs_name>/cmd/gear-in-pos
Payload:
{
    "master": "X",
    "syncSource": "SYNC_SETPOINT",
    "syncMode": "SYNC_ABSOLUTE",
    "dynSyncDirection": "SHORTEST_WAY",
    "masterSyncPosition": 0.0,
    "masterStartDistance": 0.0,
    "parameters": {
       "masterOffset", 0.0,
       "slaveOffset": 0.0,
       "ratioDenominator": 1,
       "ratioNumerator": 1,
       "fineAdjust": 0.0
    },
    "buffered": true
}

Python:
axs_cmd_gear_in_pos(axs: str, master: str, sync_source: int, sync_mode: int,
dyn_sync_direction: int,
    parameters: Dict[str, Union[float, int]], buffered:
bool,
   master_sync_position: float = 0.0,
master_start_distance: float = 0.0) -> int:
"""Couple the axis to a master axis and synchronously follow
   using position control.
   (Objects have to be attached, see motion.attach_obj()).

   Follow the position of the master axis with a specified
   gear ratio, fine adjust and position offsets. The command
   uses the Data Layer RT (at motion axis or system level),
   where the parameter locations in the Data Layer RT are

    predefined. To explicitly define the locations of these
    parameters in the Data Layer RT, axs_cmd_gear_in_pos_ex
    can be used.

    Args:
axs:                 Name of the slave axis.
master:              Name of the master axis.
sync_source:         Synchronization source.
     Setpoint = 0, Actual = 1.
sync_mode:          Synchronization command mode.
     Relative = 0, RelativeKeepState = 1,
     Absolute = 2, AbsoluteKeepState = 3.
dyn_sync_direction: Dynamic synchronization movement
     direction.
     ShortestWay = 0, Positive = 1,
     Negative = 2,
     Direct = 3.
parameters:         The parameters used for synchronized
     motion with the following keys:
     master_offset (float):
            Master offset value.
     slave_offset (float):
            Slave offset value.
     ratio_numerator (int):
            Gear ratio numerator.
     ratio_denominator (int):
            Gear ratio denominator.
     fine_adjustment (float):
            Fine adjustment parameter.
buffered:           Create this command as a buffered
     command.
master_sync_position:
     Master position, where the slave is
     synchronized with the master
master_start_distance:
     Master distance, where the synchronization is started

    Returns:
The command id.
    """

BundleIF:
Ab Version 4.2 wurde das GearInPos-Kommando um die Parameter "Mas‐
terSyncPosition" und "MasterStartPosition" erweitert. Aus Kompatibilitäts‐
gründen sind die bisherigen Kommandofunktionen "MOTION_CORE_AxsGearIn‐
PosCmd()" und "MOTION_CORE_AxsGearInPosCmdEx()" und die neuen Funk‐
tionen "MOTION_CORE_AxsGearInPosCmd2()" und "MOTION_CORE_AxsGear‐
InPosCmdEx2()" im Bunde-Interface vorhanden.
Vorzugsweise sollten die neuen Funktionen "MOTION_CORE_AxsGear‐
InPosCmd2()" und "MOTION_CORE_AxsGearInPosCmdEx2()" verwendet
werden.
namespace motion::sync::cmd {
  enum class SyncSource : uint32_t
  {
    ///< use master ipo position (setpoint position)
    SYNC_SETPOINT,

      ///< use master actual position (encoder position)
      SYNC_ACTUAL,

      ///< use extrapolated master position
      SYNC_ACTUAL_EXTRAPOLATED,

      SYNC_LAST_ENTRY
    };

    enum class SyncMode : uint32_t
    {
      ///< run the slave relative and init the pipeline
      SYNC_RELATIVE,

      ///< run the slave relative and keep the pipeline state
      SYNC_RELATIVE_KEEP_STATE,

      ///< use the absolute result of the calculation
      ///< pipeline for the slave and init the pipeline
      SYNC_ABSOLUTE,

      ///< use the absolute result of the calculation
      ///< pipeline for the slave and keep the pipeline state
      SYNC_ABSOLUTE_KEEP_STATE,

      SYNC_LAST_ENTRY
    };

    enum class DynSyncDirection : uint32_t
    {
       SHORTEST_WAY,
       POSITIVE,
       NEGATIVE,
       DIRECT,
       SYNC_LAST_ENTRY
    };

    struct GearInPosParameters
    {
      ///< master offset value
      double masterOffset {0.0};

      ///< slave offset value
      double slaveOffset {0.0};

      ///< numerator ratio value
      int32_t ratioNumerator {1};

      ///< denominator ratio value
      int32_t ratioDenominator {1};

      ///< fine adjust parameter
      double fineAdjust {0.0};
    };
}

::motion::core::MotionResult (*axsGearInPosCmd)
(void* handle,

  const ::motion::core::dia::CmdSourceInfo& sourceInfo,
  const char* slaveName,
  const char* masterName,
  ::motion::sync::cmd::SyncSource syncSource =
  ::motion::sync::cmd::SyncSource::SYNC_SETPOINT,
  ::motion::sync::cmd::SyncMode syncMode =
  ::motion::sync::cmd::SyncMode::SYNC_RELATIVE,
  ::motion::sync::cmd::DynSyncDirection dynSyncDirection =
  ::motion::sync::cmd::DynSyncDirection::SHORTEST_WAY,
  motion::sync::cmd::GearInPosParameters& parameters,
  bool buffered = false,
  uint64_t& cmdId);

### 7.2.20 AxsGearInPosEx - Synchronizing to position

Basics
GearInPos is part of a group of synchronized Motion functions that behave
like a gearbox. The GearInPos commands control the slave axis in the "Posi‐
tion" function on the drive and use the position of the master axis. As a result,
the position of the slave axis (y) is proportional to the position of the master
axis (x) with the specified ratio (r) and optionally with a position offset, see
Fig. 258. This is defined by the equation y = rx + offset, which can be
represented by a red line in the master/slave plane.
      y

                            (masterOffset , slaveOffset)

                        r

The offsets of the master axis and the slave axis are selected so that the coor‐
dinate (masterOffset, slaveOffset) is on the red line. Therefore, the equation
can be written as follows:

                               _ masterOffset
          y =    r   * ( x                    ) + slaveOffset

The described formula is a basic equation. The functionality of the synchron‐
ized Motion GearInPos is extended by several parameters, for example secon‐
dOrderInterpolatedOffset and firstOrderFilteredOffset. These parameters can
be set via the Data Layer RT.

The master/slave relationship is clearly defined, provided that masterOffset
and slaveOffset are defined. This is not the case with a modulo axis. If the
master axis is a modulo axis with the modulo value p, the positions master‐
Offset and masterOffset + n * p are equivalent. The master/slave relationship
can be drawn as follows in the master/slave level.

        y

                     (masterOffset , slaveOffset)   (masterOffset , slaveOffset)   (masterOffset , slaveOffset)

                 r                            r                              r

The transmission ratio (r) is expressed by a rational number and optionally
a percentage correction, which is referred to as fineAdjust. FineAdjust can be
specified with the GearInPos command and via the Data Layer RT.

                ratioNumerator                                             fineAdjust
        r =
               ratioDenominator                      * (1 +                   100
After the GearInPos command, the axis remains in the gearing function. To
end the command, the command has to be canceled. For example, by a cancel
command or by a new, non-buffered Motion command. A new command of
the GearInPos command results in the axis not being synchronized when the
command becomes active.

Functional description of GearInPos
GearInPos are Motion commands for axes that are based on the functionality
of synchronized Motion.
GearInPos can be buffered and non-buffered. The commanded axis becomes a
slave axis in relation to a specified master axis. This command sets the slave
axis to the PLCopen state SYNCHRONIZED MOTION. While the command is
ACTIVE, the position of the slave axis follows the position of the master axis.
Before the master axis and the slave axis are moved synchronously, the slave
axis first has to execute a motion so that the master/slave position reference
can be established and maintained. This motion is realized with the dynamic
synchronization functionality. How the dynamic synchronization is executed is
defined by SyncMode, and additionally for a slave axis by DynSyncDirection.

● If an absolute position reference between the master and slave axes is not
    required, the SYNC_RELATIVE SyncMode can be selected. In this case, a
    position difference between the master and slave axes remains the same
    from the start of the command
● If a position difference between the master and slave axis is to be adjusted,
    i.e. position synchronization, the SYNC_ABSOLUTE SyncMode has to be
    selected
If the slave axis is a modulo axis and dynamic synchronization is active, the
slave axis attempts to synchronize to the target position with the lowest
number of revolutions if the slave axis is a rotary axis, or with the lowest
number of modulo ranges if the slave axis is a linear axis.
If the master axis is a modulo axis and the SyncMode SYNC_ABSOLUTE is
selected, several lines can be tracked in the master/slave level, see ⮫ Chapter
7.2.19 AxsGearInPos - Synchronizing to position on page 386. The DynSync‐
Direction command parameter can be used to select a specific line, see
⮫ Chapter Dynamic synchronization on page 115 for more information.
If the master axis is a modulo axis, the master axis position is the continu‐
ously (linearized) offset master axis position since the start of the command.
For example, if the modulo value of the master axis is 100 and the GearInPos
command starts at master axis position 60, the initial position is 60. However,
if the master axis is moved over a distance of +220 (2.2 times the modulo
distance), the master axis position is (60 + 220) mod 100 = 80, and the
master axis position in the GearInPos calculation pipeline is 60 + 220 = 280.
While the GearInPos command is active, the command ensures that the
motion of the slave axis does not violate any restrictions for maximum
velocity, maximum acceleration and maximum jerk. Due to these restrictions,
it is possible that the slave axis cannot follow the master axis. For example,
if the slave axis has to move faster than the maximum velocity specification
allows. The violation of a constraint condition leads to a reaction defined by
the configured dynamic synchronization error reaction, see ⮫ Chapter 6.2.1
Synchronized Motion on page 84.
The following GearInPos commands are available:
● AxsGearInPosCmd
● AxsGearInPosCmdEx

PLC:

Starting with version 4.2, the GearInPos command was expanded to include
the "MasterSyncPosition" and "MasterStartPosition" parameters. For compati‐
bility reasons, the previous command functions "ML_AxsGearInPos" and data
types for GearInPos from the "CXA_Motion" PLC library, as well as the new
function "ML_AxisGearInPos2," are available. The ML_AxsGearInPos2 function
and the corresponding data types should preferably be used.
In the PLC library CXA_PLCopen and in the CXA_MotionInterface, the existing
function blocks and structures have been extended to be compatible.

Table 62: ML_AxsGearInPos
STRUCT ML_AxsGearInPosExData
Name       Data type    Inherited         Address       Initial value   Comment
                        from
  In       ML_iAxsGear‐                                                 Input: Command data of
           InPosEx                                                      the command
  Out      ML_oCmdRe‐                                                   Output: Command parame‐
           sult                                                         ters
ENUM ML_SyncMode
Name            Data         Inherited    Address      Initial value    Comment
                type         from

  SYNC_RELATIVE INT                                                     Execute the slave axis and
initialize the pipeline
  SYNC_RELA‐           INT                                              Execute the slave axis rel‐
TIVE_KEEP_STATE                                                         atively and maintain the
status of the pipeline
  SYNC_ABSO‐           INT                                              Use the absolute result of
LUTE                                                                    the calculation pipeline for
the slave axis and initialize
the pipeline
  SYNC_ABSO‐    INT                                                     Use of the absolute result
LUTE_KEEP_STATE                                                         of the calculation pipeline
for the slave axis and reten‐
tion of the pipeline status
ENUM ML_SyncSource
Name       Data type         Inherited    Address       Initial value   Comment
                             from
  SYNC_SET‐ INT                                                         Synchronization based on
POINT                                                                   the command value of the
                                                                        master axis(es)
              INT                                                       Synchronization based on
SYNC_ACTUA                                                              the current value of the
L                                                                       master axis(es)
Enum ML_Dyn‐
SyncDirection
Name          Data type          Inherited from   Address         Initial value     Comment
SHORTEST_WA INT                                                                     Initiating syn‐
Y                                                                                   chronization via
                                                                                    the shortest
                                                                                    path
POSITIVE         INT                                                                Synchronization
                                                                                    in positive
                                                                                    direction
NEGATIVE         INT                                                                Synchronization
                                                                                    in negative
                                                                                    direction
DIRECT           INT                                                                Direct transfer
                                                                                    of the synchro‐
                                                                                    nization differ‐
                                                                                    ence between
                                                                                    master and
                                                                                    slave

STRUCT ML_iAxsGearInPosParameters
Name         Data type  Inherited   Address   Initial value   Comment
                        from
  Master‐    LREAL                            0.0             Master offset
Offset
  Slave‐     LREAL                            0.0             Slave offset
Offset
  RatioNum‐ DINT                              1               Ratio numerator
erator
  RatioDeno‐ DINT                             1               Ratio denominator
minator
  FineAdjust LREAL                            0.0             Fine adjust
STRUCT ML_iAxsGearInPosDlParameters
Name         Data type  Inherited   Address   Initial value   Comment
                        from
  SoiMaster‐ DINT                             -1              Master axis Data Layer
OffsetDlIdx                                                   index used for second
                                                              order offset
  SoiMaster‐ DINT                             -1              Master axis offset velocity
OffsetVel‐                                                    Data Layer index used for
DlIdx                                                         second order offset
  SoiMaster‐ DINT                             -1              Master axis offset accelera‐
OffsetAcc‐                                                    tion Data Layer index for
DlIdx                                                         second order offset
  SoiSla‐    DINT                             -1              Slave axis Data Layer index
veOffset‐                                                     used for the second order
DlIdx                                                         slave axis
  SoiSla‐    DINT                             -1              Slave axis offset velocity
veOffsetVel‐                                                  Data Layer index used for
DlIdx                                                         second-order offset
  SoiSla‐    DINT                             -1              Slave axis acceleration
veOffsetAcc‐                                                  Data Layer index used for
DlIdx                                                         the second order offset
  FofMaster‐ DINT                             -1              Master axis Data Layer
OffsetDlIdx                                                   index used for filtered first-
                                                              order offset
  FofMaster‐ DINT                             -1              Master axis Time constant
OffsetTime‐                                                   Data Layer index for fil‐
Constant‐                                                     tered first-order offset
DlIdx
  FofSla‐     DINT                            -1              Slave axis Data Layer index
veOffset‐                                                     used for the filtered first-
DlIdx                                                         order offset
  FofSla‐     DINT                            -1              Slave axis time constant
veOffsetTi‐                                                   Data Layer index used for
meConstant‐                                                   filtered first-order offset
DlIdx
  FineAdjust‐ DINT                            -1              Fine adjustment Data Layer
DlIdx                                                         index for fine adjustment of
                                                              the transmission ratio

STRUCT ML_iAxsGearInPosEx EXTENDS ML_iAxsCmdBase
Name        Data type   Inherited  Address     Initial value         Comment
                        from
  AxisName STRING(63) ML_iAxsCmd‐                                    Name of the axis used to
                        Base                                         execute the command
  Source    STRING(50) ML_iAxsCmd‐                                   Specifies the command
                        Base                                         source, e.g PlcApplication1
                                                                     is displayed in the diag‐
                                                                     nostic messages
  SourceLine ULINT           ML_iAxsCmd‐                             Specifies the source line of
                             Base                                    the command; is displayed
                                                                     in the diagnostic messages

  Master‐  STRING(15)                                                Name of the master axis
Name                                                                 that is being followed
  Syn‐     ML_Syn‐                                                   Synchronization source
cSource    cSource
  SyncMode ML_Syn‐                                                   Function of
cMode                                                     the synchronization
                                                command: SYNC_ABSO‐
                                                LUTE, SYNC_RELA‐
                                                TIVE, SYNC_ABSO‐
                                                LUTE_KEEP_STATE,
                                                SYNC_RELA‐
                                                TIVE_KEEP_STATE
   DynSync‐  ML_DynSync‐                                             Direction of synchroniza‐
Direction    Direction                                               tion
   Parame‐   ML_iAxsGear‐                                            Parameters for the Gear‐
ters         InPosPara‐                                              InPos command
meters
DlParameters ML_iAxsGear‐                                            Data Layer parameters for
InPosDlPara‐                                            the GearInPos command
meters
  Buffered   BOOL                                                    TRUE, if the command is
                                                to be executed as a buf‐
                                                fered command, otherwise
                                                FALSE

Data Layer
Method: POST
URL: motion/axs/<axs_name>/cmd/gear-in-pos-ex
Payload:
{
    "master": "X",
    "syncSource": "SYNC_SETPOINT",
    "syncMode": "SYNC_ABSOLUTE",
    "dynSyncDirection": "SHORTEST_WAY",
    "masterSyncPosition": 0.0,
    "masterStartDistance": 0.0,
    "parameters": {
       "masterOffset": 0.0,
       "slaveOffset": 0.0,
       "ratioDenominator": 1,
       "ratioNumerator": 1,
       "fineAdjust": 0.0

    },
    "dlParameters": {
       "soiMasterOffsetDlIdx": -1,
       "soiMasterOffsetVelDlIdx": -1,
       "soiMasterOffsetAccDlIdx": -1,
       "soiSlaveOffsetDlIdx": -1,
       "soiSlaveOffsetVelDlIdx": -1,
       "soiSlaveOffsetAccDlIdx": -1,
       "fofMasterOffsetDlIdx": -1,
       "fofMasterOffsetTimeConstantDlIdx": -1,
       "fofSlaveOffsetDlIdx": -1,
       "fofSlaveOffsetTimeConstantDlIdx": -1,
       "fineAdjustDlIdx": -1
    },
    "buffered": true
}

Python:
axs_cmd_gear_in_pos_ex(axs: str, master: str, sync_source: int,
sync_mode: int, dyn_sync_direction: int,
parameters: Dict[str, Union[float, int]],
dl_parameters: Dict[str, int],
buffered: bool,
master_sync_position: float = 0.0,
master_start_distance: float = 0.0) -> int:

"""Couple the axis to a master axis and synchronously follow using position
control.
(objects have to be attached, see motion.attach_obj())

Follow the position of the master axis with a specified gear ratio, fine adjust
and position offsets. The realtime
Data Layer indices for offsets and other parameters also have to be specified.
If an index value is -1, the default index
is selected. If an index value is < 1000, the specified index is used. If an
index value is >= 1000, the system
realtime Data Layer is referred.

Args:
    axs:                  Name of the slave axis.
    master:               Name of the master axis.
    sync_source:          Sync source (Setpoint = 0, Actual = 1).
    sync_mode:            Command mode (Relative = 0, RelativeKeepState = 1,
   Absolute = 2, AbsoluteKeepState = 3).
dyn_sync_direction: Dynamic sync direction (ShortestWay = 0, Positive
   = 1, Negative = 2, Direct = 3).
parameters:         The parameters used for synchronized motion with
   the following keys:
   master_offset (float): Master offset value.
   slave_offset (float): Slave offset value.
   ratio_numerator (int): Gear ratio numerator.
   ratio_denominator (int): Gear ratio denominator.
   fine_adjustment (float): Fine adjustment parameter.
dl_parameters:
soi_master_offset_dl_idx (int): index of master offset target
value, second order interpolated.
soi_master_offset_vel_dl_idx (int): index of master offset

velocity constraint for second order interpolation.
soi_master_offset_acc_dl_idx (int): index of master offset
acceleration constraint for second order interpolation.
soi_slave_offset_dl_idx (int): index of slave offset target
value, second order interpolated.
soi_slave_offset_vel_dl_idx (int): index of slave offset
velocity constraint for second order interpolation.
soi_slave_offset_acc_dl_idx (int): index of slave offset
acceleration constraint for second order interpolation.
fof_master_offset_dl_idx (int): index of second master
offset, first order filtered.
fof_master_offset_time_constant_dl_idx (int): index of time
constant for change rate of fofMasterOffset.

fof_slave_offset_dl_idx (int): index of second slave offset,
first order filtered.
fof_slave_offset_time_constant_dl_idx (int): index of time
constant for change rate of fofSlaveOffset.
fine_adjustment_dl_idx (int): index of fine adjustment
percentage in addition to the commanded fine adjustment.
buffered:          Create this command as a buffered command.
master_sync_position:
Master position, where the slave is synchronized with the master
master_start_distance:
Master distance, where the synchronization is started

Returns:
    The command id.
"""

BundleIF:
Ab Version 4.2 wurde das GearInPos-Kommando um die Parameter "Mas‐
terSyncPosition" und "MasterStartPosition" erweitert. Aus Kompatibilitäts‐
gründen sind die bisherigen Kommandofunktionen "MOTION_CORE_AxsGearIn‐
PosCmd()" und "MOTION_CORE_AxsGearInPosCmdEx()" und die neuen Funk‐
tionen "MOTION_CORE_AxsGearInPosCmd2()" und "MOTION_CORE_AxsGear‐
InPosCmdEx2()" im Bunde-Interface vorhanden.
Vorzugsweise sollten die neuen Funktionen "MOTION_CORE_AxsGear‐
InPosCmd2()" und "MOTION_CORE_AxsGearInPosCmdEx2()" verwendet
werden.
namespace motion::sync::cmd {
  enum class SyncSource : uint32_t
  {
    ///< use master ipo position (setpoint position)
    SYNC_SETPOINT,

    ///< use master actual position (encoder position)
    SYNC_ACTUAL,

    ///< use extrapolated master position
    SYNC_ACTUAL_EXTRAPOLATED,

    SYNC_LAST_ENTRY
  };

  enum class SyncMode : uint32_t
  {
    ///< run the slave relative and init the pipeline

      SYNC_RELATIVE,

      ///< run the slave relative and keep the pipeline state
      SYNC_RELATIVE_KEEP_STATE,

      ///< use the absolute result of the calculation
      ///< pipeline for the slave and init the pipeline
      SYNC_ABSOLUTE,

      ///< use the absolute result of the calculation
      ///< pipeline for the slave and keep the pipeline state
      SYNC_ABSOLUTE_KEEP_STATE,

      SYNC_LAST_ENTRY
   };

   enum class DynSyncDirection : uint32_t
   {
      SHORTEST_WAY,
      POSITIVE,
      NEGATIVE,
      DIRECT,
      SYNC_LAST_ENTRY
   };

   struct GearInPosParameters
   {
     ///< master offset value
     double masterOffset {0.0};

      ///< slave offset value
      double slaveOffset {0.0};

      ///< numerator ratio value
      int32_t ratioNumerator {1};

      ///< denominator ratio value
      int32_t ratioDenominator {1};

      ///< fine adjust parameter
      double fineAdjust {0.0};
   };

   struct GearInPosDlParameters
   {
     ///< Data Layer index of master offset
     int32_t soiMasterOffsetDlIdx {-1};

      ///< Data Layer index of master offset velocity
      int32_t soiMasterOffsetVelDlIdx {-1};

      ///< Data Layer index of master offset acceleration
      int32_t soiMasterOffsetAccDlIdx {-1};

      ///< Data Layer index of slave offset
      int32_t soiSlaveOffsetDlIdx {-1};

      ///< Data Layer index of slave offset velocity

int32_t soiSlaveOffsetVelDlIdx {-1};

///< Data Layer index of slave offset acceleration
int32_t soiSlaveOffsetAccDlIdx {-1};

///< Data Layer index of additional master offset
int32_t fofMasterOffsetDlIdx {-1};

///< Data Layer index of additional master offset
///< time constant
int32_t fofMasterOffsetTimeConstantDlIdx {-1};

///< Data Layer index of additional slave offset

int32_t fofSlaveOffsetDlIdx {-1};

///< Data Layer index of additional slave offset
///< time constant
int32_t fofSlaveOffsetTimeConstantDlIdx {-1};

///< Data Layer index of additional fine adjust
int32_t fineAdjustDlIdx {-1};
    };
}

::motion::core::MotionResult (*axsGearInPosCmdEx)
(void* handle,
 const ::motion::core::dia::CmdSourceInfo& sourceInfo,
 const char* slaveName,
 const char* masterName,
 ::motion::sync::cmd::SyncSource syncSource =
 ::motion::sync::cmd::SyncSource::SYNC_SETPOINT,
 ::motion::sync::cmd::SyncMode syncMode =
 ::motion::sync::cmd::SyncMode::SYNC_RELATIVE,
 ::motion::sync::cmd::DynSyncDirection dynSyncDirection =
 ::motion::sync::cmd::DynSyncDirection::SHORTEST_WAY,
 motion::sync::cmd::GearInPosParameters& parameters,
 motion::sync::cmd::GearInPosDlParameters& dlParameters,
 bool buffered = false,
 uint64_t& cmdId);

### 7.2.21 AxsGearInPos2 - Synchronizing to position

Basics
GearInPos belongs to a group of synchronized Motion functions that behave
like a gearbox. The GearInPos commands control the slave axis in the "Posi‐
tion" function on the drive and use the position of the master axis. As a result,
the position of the slave axis (y) is proportional to the position of the master
axis (x) with the specified ratio (r) and optionally with a position offset, see
Fig. 263. This is defined by the equation y = rx + offset, which can be
represented by a red line in the master/slave plane.

      y
                                 (masterOffset , slaveOffset)

                           r

The offsets of the master axis and the slave axis are selected so that the coor‐
dinate (masterOffset, slaveOffset) is on the red line. Therefore, the equation
can be written as follows:

                                     _ masterOffset
          y =    r   * ( x                          ) + slaveOffset

The described formula is a basic equation. The functionality of the synchron‐
ized Motion GearInPos is extended by several parameters, for example secon‐
dOrderInterpolatedOffset and firstOrderFilteredOffset. These parameters can
be set via the Data Layer RT.
The master/slave relationship is clearly defined, provided that masterOffset
and slaveOffset are defined. This is not the case with a modulo axis. If the
master axis is a modulo axis with the modulo value p, the positions master‐
Offset and masterOffset + n * p are equivalent. The master/slave relationship
can be drawn as follows in the master/slave level.
      y

                     (masterOffset , slaveOffset)   (masterOffset , slaveOffset)   (masterOffset , slaveOffset)

                 r                            r                              r

The transmission ratio (r) is expressed by a rational number and optionally
a percentage correction, which is referred to as fineAdjust. FineAdjust can be
specified with the GearInPos command and via the Data Layer RT.

                ratioNumerator                    fineAdjust
        r =
               ratioDenominator       *   (1 +       100
                                                               )
After the GearInPos command, the axis remains in the gearing function. To
end the command, the command has to be canceled. For example, by a cancel
command or by a new, non-buffered Motion command. A new command of
the GearInPos command results in the axis not being synchronized when the
command becomes active.

Functional description of GearInPos
GearInPos are Motion commands for axes that are based on the functionality
of synchronized Motion.
GearInPos can be buffered and non-buffered. The commanded axis becomes a
slave axis in relation to a specified master axis. This command sets the slave
axis to the PLCopen state SYNCHRONIZED MOTION. While the command is
ACTIVE, the position of the slave axis follows the position of the master axis.
Before the master axis and the slave axis are moved synchronously, the slave
axis first has to execute a motion so that the master/slave position reference
can be established and maintained. This motion is realized with the dynamic
synchronization functionality. How the dynamic synchronization is executed is
defined by SyncMode, and additionally for a slave axis by DynSyncDirection.
● If an absolute position reference between the master and slave axes is not
    required, the SYNC_RELATIVE SyncMode can be selected. In this case, a
    position difference between the master and slave axes remains the same
    from the start of the command
● If a position difference between the master and slave axis is to be adjusted,
    i.e. position synchronization, the SYNC_ABSOLUTE SyncMode has to be
    selected
If the slave axis is a modulo axis and dynamic synchronization is active, the
slave axis attempts to synchronize to the target position with the lowest
number of revolutions if the slave axis is a rotary axis, or with the lowest
number of modulo ranges if the slave axis is a linear axis.
If the master axis is a modulo axis and the SyncMode SYNC_ABSOLUTE is
selected, several lines can be tracked in the master/slave level, see ⮫ Chapter
7.2.19 AxsGearInPos - Synchronizing to position on page 386. The DynSync‐
Direction command parameter can be used to select a specific line, see
⮫ Chapter Dynamic synchronization on page 115 for more information.
If the master axis is a modulo axis, the master axis position is the continu‐
ously (linearized) offset master axis position since the start of the command.
For example, if the modulo value of the master axis is 100 and the GearInPos
command starts at master axis position 60, the initial position is 60. However,
if the master axis is moved over a distance of +220 (2.2 times the modulo
distance), the master axis position is (60 + 220) mod 100 = 80, and the
master axis position in the GearInPos calculation pipeline is 60 + 220 = 280.
While the GearInPos command is active, the command ensures that the
motion of the slave axis does not violate any restrictions for maximum
velocity, maximum acceleration and maximum jerk. Due to these restrictions,
it is possible that the slave axis cannot follow the master axis. For example,
if the slave axis has to move faster than the maximum velocity specification

allows. The violation of a constraint condition leads to a reaction defined by
the configured dynamic synchronization error reaction, see ⮫ Chapter 6.2.1
Synchronized Motion on page 84.
Functionality: “Reaching synchronization at a specified master position":
To ensure synchronization of the slave axis at a specific master position, the
following parameters can be used in the "GearinPos" command:
● "MasterSyncPosition" (master position at which the slave axis should be
    synchronized with the master axis)
● "MasterStartDistance" (distance from "MasterSyncPosition" at which syn‐
    chronization starts)
Specify the master position at which synchronization should occur. In this
case, the synchronization direction is ignored.
If parameter "MasterStartDistance" = "0" when executing the “GearInPos com‐
mand”, the synchronization process is executed according to the “errror reac‐
tion” setting and the dynamic axis limit.
The traversing motion is then implemented using a 5th-order polynomial.
Calculating the "sync position" of the slave axis:
SlaveSyncPosition = (((MasterSyncPosition % Modulo - MasterStartDistance)
% Modulo + MasterStartDistance) * Gear + SlaveOffset) % Modulo

Synchronization to a specified master position and a fixed synchronization
direction should be performed while the slave axis is stationary. If the slave
axis is rotating, the axis may rotate backward.
The following GearInPos commands are available:
● AxsGearInPosCmd
● AxsGearInPosCmdEx

PLC:

Table 63: ML_AxsGearInPos2
STRUCT ML_AxsGearInPos2Data
Name       Data type    Inherited          Address       Initial value   Comment
                        from

  In       ML_iAxsGear‐                                                  Input: Command data of
InPos2                                                        the command
  Out      ML_oCmdRe‐                                                    Output: Command parame‐
sult                                                          ters
ENUM ML_SyncMode
Name            Data          Inherited    Address      Initial value    Comment
type          from
  SYNC_RELATIVE INT                                                      Execute the slave axis and
initialize the pipeline
  SYNC_RELA‐           INT                                               Execute the slave axis rel‐
TIVE_KEEP_STATE                                                          atively and maintain the
status of the pipeline
  SYNC_ABSO‐           INT                                               Use the absolute result of
LUTE                                                                     the calculation pipeline for
the slave axis and initialize
the pipeline
  SYNC_ABSO‐    INT                                                      Use of the absolute result
LUTE_KEEP_STATE                                                          of the calculation pipeline
for the slave axis and reten‐
tion of the pipeline status
ENUM ML_SyncSource
Name       Data type          Inherited    Address       Initial value   Comment
                              from
  SYNC_SET‐ INT                                                          Synchronization based on
POINT                                                                    the command value of the
                                                                         master axis(es)
              INT                                                        Synchronization based on
SYNC_ACTUA                                                               the current value of the
L                                                                        master axis(es)
Enum ML_Dyn‐
SyncDirection
Name          Data type           Inherited from   Address         Initial value     Comment
SHORTEST_WA INT                                                                      Initiating syn‐
Y                                                                                    chronization via
                                                                                     the shortest
                                                                                     path
POSITIVE         INT                                                                 Synchronization
                                                                                     in positive
                                                                                     direction

Enum ML_Dyn‐
SyncDirection
NEGATIVE      INT                                                                Synchronization
                                                         in negative
                                                         direction
DIRECT             INT                                                           Direct transfer
                                                         of the synchro‐
                                                         nization differ‐
                                                         ence between
                                                         master and
                                                         slave
STRUCT ML_iAxsGearInPosParameters
Name         Data type  Inherited       Address   Initial value   Comment
                        from
  Master‐    LREAL                                0.0             Master offset
Offset
  Slave‐     LREAL                                0.0             Slave offset
Offset
  RatioNum‐ DINT                                  1               Ratio numerator
erator
  RatioDeno‐ DINT                                 1               Ratio denominator
minator
  FineAdjust LREAL                                0.0             Fine adjust
STRUCT ML_iAxsGearInPos2 EXTENDS ML_iAxsCmdBase
Name        Data type   Inherited  Address     Initial value      Comment
                        from
  AxisName STRING(63) ML_iAxsCmd‐                                 Name of the axis used to
                        Base                                      execute the command
  Source    STRING(50) ML_iAxsCmd‐                                Specifies the source of
                        Base                                      the command, e.g. PlcAp‐
                                                                  plication1. Appears in diag‐
                                                                  nostic messages
   SourceLine ULINT       ML_iAxsCmd‐                             Displays the source line of
                          Base                                    the command. Is displayed
                                                                  in diagnostic messages
  Master‐  STRING(15)                                             Name of the master axis
Name                                                              that is being followed
  Syn‐     ML_Syn‐                                                Synchronization source
cSource    cSource
  SyncMode ML_Syn‐                                                Function of
           cMode                                                  the synchronization
                                                                  command: SYNC_ABSO‐
                                                                  LUTE, SYNC_RELA‐
                                                                  TIVE, SYNC_ABSO‐
                                                                  LUTE_KEEP_STATE,
                                                                  SYNC_RELA‐
                                                                  TIVE_KEEP_STATE
  DynSync‐ ML_DynSync‐                                            Direction of synchroniza‐
Direction   Direction                                             tion
MasterSync‐ LREAL                                 0.0             Master position in which
Position                                                          slave is synchronized with
                                                                  the master

STRUCT ML_iAxsGearInPos2 EXTENDS ML_iAxsCmdBase
MasterStart‐ LREAL                             0.0                Distance from the start of
Distance                                                          the slave motion to the
                                             point at which the slave
                                             axis achieves synchroniza‐
                                             tion
   Parame‐    ML_iAxsGear‐                                        Parameters for the Gear‐
ters          InPosPara‐                                          InPos command
meters
  Buffered    BOOL                                                TRUE, if the command is
                                             to be executed as a buf‐
                                             fered command, otherwise

                                             FALSE

Data Layer
Method: POST
URL: motion/axs/<axs_name>/cmd/gear-in-pos
Payload:
{
    "master": "X",
    "syncSource": "SYNC_SETPOINT",
    "syncMode": "SYNC_ABSOLUTE",
    "dynSyncDirection": "SHORTEST_WAY",
    "masterSyncPosition": 0.0,
    "masterStartDistance": 0.0,
    "parameters": {
       "masterOffset", 0.0,
       "slaveOffset": 0.0,
       "ratioDenominator": 1,
       "ratioNumerator": 1,
       "fineAdjust": 0.0
    },
    "buffered": true
}

Python:
axs_cmd_gear_in_pos(axs: str, master: str, sync_source: int, sync_mode: int,
dyn_sync_direction: int,
    parameters: Dict[str, Union[float, int]], buffered:
bool,
   master_sync_position: float = 0.0,
master_start_distance: float = 0.0) -> int:
"""Couple the axis to a master axis and synchronously follow
   using position control.
   (Objects have to be attached, see motion.attach_obj()).

   Follow the position of the master axis with a specified
   gear ratio, fine adjust and position offsets. The command
   uses the Data Layer RT (at motion axis or system level),
   where the parameter locations in the Data Layer RT are
   predefined. To explicitly define the locations of these
   parameters in the Data Layer RT, axs_cmd_gear_in_pos_ex
   can be used.

   Args:

axs:                Name of the slave axis.
master:             Name of the master axis.
sync_source:        Synchronization source.
Setpoint = 0, Actual = 1.
sync_mode:          Synchronization command mode.
Relative = 0, RelativeKeepState = 1,
Absolute = 2, AbsoluteKeepState = 3.
dyn_sync_direction: Dynamic synchronization movement
direction.
ShortestWay = 0, Positive = 1,
Negative = 2,
Direct = 3.
parameters:         The parameters used for synchronized
motion with the following keys:
master_offset (float):
       Master offset value.
slave_offset (float):
       Slave offset value.
ratio_numerator (int):
       Gear ratio numerator.
ratio_denominator (int):
       Gear ratio denominator.
fine_adjustment (float):
       Fine adjustment parameter.
buffered:           Create this command as a buffered
command.
master_sync_position:
Master position, where the slave is
synchronized with the master
master_start_distance:
Master distance, where the synchronization is started

    Returns:
The command id.
    """

BundleIF:
namespace motion::sync::cmd {
  enum class SyncSource : uint32_t
  {
    ///< use master ipo position (setpoint position)
    SYNC_SETPOINT,

///< use master actual position (encoder position)
SYNC_ACTUAL,

///< use extrapolated master position
SYNC_ACTUAL_EXTRAPOLATED,

SYNC_LAST_ENTRY
   };

   enum class SyncMode : uint32_t
   {
///< run the slave relative and init the pipeline
SYNC_RELATIVE,

      ///< run the slave relative and keep the pipeline state
      SYNC_RELATIVE_KEEP_STATE,

      ///< use the absolute result of the calculation
      ///< pipeline for the slave and init the pipeline
      SYNC_ABSOLUTE,

      ///< use the absolute result of the calculation
      ///< pipeline for the slave and keep the pipeline state
      SYNC_ABSOLUTE_KEEP_STATE,

      SYNC_LAST_ENTRY
    };

    enum class DynSyncDirection : uint32_t
    {
       SHORTEST_WAY,
       POSITIVE,
       NEGATIVE,
       DIRECT,
       SYNC_LAST_ENTRY
    };

    struct GearInPosParameters
    {
      ///< master offset value
      double masterOffset {0.0};

      ///< slave offset value
      double slaveOffset {0.0};

      ///< numerator ratio value
      int32_t ratioNumerator {1};

      ///< denominator ratio value
      int32_t ratioDenominator {1};

      ///< fine adjust parameter
      double fineAdjust {0.0};
    };
}

::motion::core::MotionResult (*axsGearInPosCmd2)
(void* handle,
 const ::motion::core::dia::CmdSourceInfo& sourceInfo,
 const char* slaveName,
 const char* masterName,
 ::motion::sync::cmd::SyncSource syncSource =
 ::motion::sync::cmd::SyncSource::SYNC_SETPOINT,
 ::motion::sync::cmd::SyncMode syncMode =
 ::motion::sync::cmd::SyncMode::SYNC_RELATIVE,
 ::motion::sync::cmd::DynSyncDirection dynSyncDirection =
 ::motion::sync::cmd::DynSyncDirection::SHORTEST_WAY,
 double masterSyncPosition,
 double masterStartDistance,
 motion::sync::cmd::GearInPosParameters& parameters,

  bool buffered = false,
  uint64_t& cmdId);

### 7.2.22 AxsGearInPos2Ex - Synchronizing to position

Basics
GearInPos belongs to a group of synchronized Motion functions that behave
like a gearbox. The GearInPos commands control the slave axis in the "Posi‐
tion" function on the drive and use the position of the master axis. As a result,
the position of the slave axis (y) is proportional to the position of the master
axis (x) with the specified ratio (r) and optionally with a position offset, see
Fig. 269. This is defined by the equation y = rx + offset, which can be
represented by a red line in the master/slave plane.
      y

                            (masterOffset , slaveOffset)

                        r

The offsets of the master axis and the slave axis are selected so that the coor‐
dinate (masterOffset, slaveOffset) is on the red line. Therefore, the equation
can be written as follows:

                               _ masterOffset
          y =    r   * ( x                    ) + slaveOffset

The described formula is a basic equation. The functionality of the synchron‐
ized Motion GearInPos is extended by several parameters, for example secon‐
dOrderInterpolatedOffset and firstOrderFilteredOffset. These parameters can
be set via the Data Layer RT.
The master/slave relationship is clearly defined, provided that masterOffset
and slaveOffset are defined. This is not the case with a modulo axis. If the
master axis is a modulo axis with the modulo value p, the positions master‐
Offset and masterOffset + n * p are equivalent. The master/slave relationship
can be drawn as follows in the master/slave level.

        y
                     (masterOffset , slaveOffset)   (masterOffset , slaveOffset)   (masterOffset , slaveOffset)

                 r                            r                              r

The transmission ratio (r) is expressed by a rational number and optionally
a percentage correction, which is referred to as fineAdjust. FineAdjust can be
specified with the GearInPos command and via the Data Layer RT.

                ratioNumerator                                             fineAdjust
        r =
               ratioDenominator                      *     (1 +               100
After the GearInPos command, the axis remains in the gearing function. To
end the command, the command has to be canceled. For example, by a cancel
command or by a new, non-buffered Motion command. A new command of
the GearInPos command results in the axis not being synchronized when the
command becomes active.

Functional description of GearInPos
GearInPos are Motion commands for axes that are based on the functionality
of synchronized Motion.
GearInPos can be buffered and non-buffered. The commanded axis becomes a
slave axis in relation to a specified master axis. This command sets the slave
axis to the PLCopen state SYNCHRONIZED MOTION. While the command is
ACTIVE, the position of the slave axis follows the position of the master axis.
Before the master axis and the slave axis are moved synchronously, the slave
axis first has to execute a motion so that the master/slave position reference
can be established and maintained. This motion is realized with the dynamic
synchronization functionality. How the dynamic synchronization is executed is
defined by SyncMode, and additionally for a slave axis by DynSyncDirection.
● If an absolute position reference between the master and slave axes is not
    required, the SYNC_RELATIVE SyncMode can be selected. In this case, a
    position difference between the master and slave axes remains the same
    from the start of the command
● If a position difference between the master and slave axis is to be adjusted,
    i.e. position synchronization, the SYNC_ABSOLUTE SyncMode has to be
    selected
If the slave axis is a modulo axis and dynamic synchronization is active, the
slave axis attempts to synchronize to the target position with the lowest
number of revolutions if the slave axis is a rotary axis, or with the lowest
number of modulo ranges if the slave axis is a linear axis.

If the master axis is a modulo axis and the SyncMode SYNC_ABSOLUTE is
selected, several lines can be tracked in the master/slave level, see ⮫ Chapter
7.2.19 AxsGearInPos - Synchronizing to position on page 386. The DynSync‐
Direction command parameter can be used to select a specific line, see
⮫ Chapter Dynamic synchronization on page 115 for more information.
If the master axis is a modulo axis, the master axis position is the continu‐
ously (linearized) offset master axis position since the start of the command.
For example, if the modulo value of the master axis is 100 and the GearInPos
command starts at master axis position 60, the initial position is 60. However,
if the master axis is moved over a distance of +220 (2.2 times the modulo
distance), the master axis position is (60 + 220) mod 100 = 80, and the
master axis position in the GearInPos calculation pipeline is 60 + 220 = 280.
While the GearInPos command is active, the command ensures that the
motion of the slave axis does not violate any restrictions for maximum
velocity, maximum acceleration and maximum jerk. Due to these restrictions,
it is possible that the slave axis cannot follow the master axis. For example,
if the slave axis has to move faster than the maximum velocity specification
allows. The violation of a constraint condition leads to a reaction defined by
the configured dynamic synchronization error reaction, see ⮫ Chapter 6.2.1
Synchronized Motion on page 84.
Functionality: “Reaching synchronization at a specified master position":
To ensure synchronization of the slave axis at a specific master position, the
following parameters can be used in the "GearinPos" command:
● "MasterSyncPosition" (master position at which the slave axis should be
    synchronized with the master axis)
● "MasterStartDistance" (distance from "MasterSyncPosition" at which syn‐
    chronization starts)
Specify the master position at which synchronization should occur. In this
case, the synchronization direction is ignored.
If parameter "MasterStartDistance" = "0" when executing the “GearInPos com‐
mand”, the synchronization process is executed according to the “errror reac‐
tion” setting and the dynamic axis limit.
The traversing motion is then implemented using a 5th-order polynomial.
Calculating the "sync position" of the slave axis:
SlaveSyncPosition = (((MasterSyncPosition % Modulo - MasterStartDistance)
% Modulo + MasterStartDistance) * Gear + SlaveOffset) % Modulo

Synchronization to a specified master position and a fixed synchronization
direction should be performed while the slave axis is stationary. If the slave
axis is rotating, the axis may rotate backward.
The following GearInPos commands are available:
 ● AxsGearInPosCmd
 ● AxsGearInPosCmdEx

 PLC:

Table 64: ML_AxsGearInPos2
STRUCT ML_AxsGearInPosEx2Data
Name       Data type    Inherited         Address       Initial value   Comment
                        from
  In       ML_iAxsGear‐                                                 Input: Command data of
           InPosEx2                                                     the command
  Out      ML_oCmdRe‐                                                   Output: Command parame‐
           sult                                                         ters
ENUM ML_SyncMode
Name           Data          Inherited    Address      Initial value    Comment
               type          from

ENUM ML_SyncMode
  SYNC_RELATIVE INT                                                         Execute the slave axis and
initialize the pipeline
  SYNC_RELA‐               INT                                              Execute the slave axis rel‐
TIVE_KEEP_STATE                                                             atively and maintain the
status of the pipeline
  SYNC_ABSO‐               INT                                              Use the absolute result of
LUTE                                                                        the calculation pipeline for
the slave axis and initialize
the pipeline
  SYNC_ABSO‐    INT                                                         Use of the absolute result
LUTE_KEEP_STATE                                                             of the calculation pipeline
for the slave axis and reten‐
tion of the pipeline status
ENUM ML_SyncSource
Name       Data type             Inherited    Address       Initial value   Comment
                                 from
  SYNC_SET‐ INT                                                             Synchronization based on
POINT                                                                       the command value of the
                                                                            master axis(es)
                   INT                                                      Synchronization based on
SYNC_ACTUA                                                                  the current value of the
L                                                                           master axis(es)
Enum ML_Dyn‐
SyncDirection
Name          Data type              Inherited from   Address         Initial value        Comment
SHORTEST_WA INT                                                                            Initiating syn‐
Y                                                                                          chronization via
                                                                                           the shortest
POSITIVE             INT                                                                   Synchronization
                                                                                           in positive
NEGATIVE             INT                                                                   Synchronization
                                                                                           in negative
DIRECT               INT                                                                   Direct transfer
                                                                                           of the synchro‐
                                                                                           nization differ‐
                                                                                           ence between
                                                                                           master and
STRUCT ML_iAxsGearInPosParameters
Name        Data type   Inherited             Address       Initial value   Comment
                        from
  Master‐   LREAL                                           0.0             Master offset
Offset
  Slave‐    LREAL                                           0.0             Slave offset
Offset
  RatioNum‐ DINT                                            1               Ratio numerator
erator

STRUCT ML_iAxsGearInPosParameters
  RatioDeno‐ DINT                                1               Ratio denominator
minator
  FineAdjust LREAL                               0.0             Fine adjust
STRUCT ML_iAxsGearInPosDlParameters
Name         Data type  Inherited   Address      Initial value   Comment
                        from
  SoiMaster‐ DINT                                -1              Master axis Data Layer
OffsetDlIdx                                                      index used for second
                                                                 order offset
  SoiMaster‐ DINT                                -1              Master axis offset velocity

OffsetVel‐                                                       Data Layer index used for
DlIdx                                                            second order offset
  SoiMaster‐ DINT                                -1              Master axis offset accelera‐
OffsetAcc‐                                                       tion Data Layer index for
DlIdx                                                            second order offset
  SoiSla‐    DINT                                -1              Slave axis Data Layer index
veOffset‐                                                        used for the second order
DlIdx                                                            slave axis
  SoiSla‐    DINT                                -1              Slave axis offset velocity
veOffsetVel‐                                                     Data Layer index used for
DlIdx                                                            second-order offset
  SoiSla‐    DINT                                -1              Slave axis acceleration
veOffsetAcc‐                                                     Data Layer index used for
DlIdx                                                            the second order offset
  FofMaster‐ DINT                                -1              Master axis Data Layer
OffsetDlIdx                                                      index used for filtered first-
                                         order offset
  FofMaster‐ DINT                                -1              Master axis Time constant
OffsetTime‐                                                      Data Layer index for fil‐
Constant‐                                                        tered first-order offset
DlIdx
  FofSla‐     DINT                               -1              Slave axis Data Layer index
veOffset‐                                                        used for the filtered first-
DlIdx                                                            order offset
  FofSla‐     DINT                               -1              Slave axis time constant
veOffsetTi‐                                                      Data Layer index used for
meConstant‐                                                      filtered first-order offset
DlIdx
  FineAdjust‐ DINT                               -1              Fine adjustment Data Layer
DlIdx                                                            index for fine adjustment of
                                         the transmission ratio
STRUCT ML_iAxsGearInPosEx2 EXTENDS ML_iAxsCmdBase
Name        Data type   Inherited  Address     Initial value     Comment
                        from
  AxisName STRING(63) ML_iAxsCmd‐                                Name of the axis used to
                        Base                                     execute the command
  Source    STRING(50) ML_iAxsCmd‐                               Specifies the command
                        Base                                     source, e.g PlcApplication1
                                                                 is displayed in the diag‐
                                                                 nostic messages

STRUCT ML_iAxsGearInPosEx2 EXTENDS ML_iAxsCmdBase
  SourceLine ULINT      ML_iAxsCmd‐                                    Specifies the source line of
 Base                                           the command; is displayed
                                                in the diagnostic messages
  Master‐  STRING(15)                                                  Name of the master axis
Name                                                                   that is being followed
  Syn‐     ML_Syn‐                                                     Synchronization source
cSource    cSource
  SyncMode ML_Syn‐                                                     Function of
cMode                                                       the synchronization
                                                command: SYNC_ABSO‐
                                                LUTE, SYNC_RELA‐
                                                TIVE, SYNC_ABSO‐
                                                LUTE_KEEP_STATE,
                                                SYNC_RELA‐
                                                TIVE_KEEP_STATE
  DynSync‐ ML_DynSync‐                                                 Direction of synchroniza‐
Direction   Direction                                                  tion
MasterSync‐ LREAL                                       0.0            Master position in which
Position                                                               the slave is synchronized
                                                with the master
MasterStart‐ LREAL                                      0.0            Distance from the start of
Distance                                                               the slave motion to the
                                                point at which the slave
                                                axis achieves synchroniza‐
                                                tion
   Parame‐   ML_iAxsGear‐                                              Parameters for the Gear‐
ters         InPosPara‐                                                InPos command
meters
DlParameters ML_iAxsGear‐                                              Data Layer parameters for
InPosDlPara‐                                              the GearInPos command
meters
  Buffered   BOOL                                                      TRUE, if the command is
                                                to be executed as a buf‐
                                                fered command, otherwise
                                                FALSE

Data Layer
Method: POST
URL: motion/axs/<axs_name>/cmd/gear-in-pos-ex
Payload:
{
    "master": "X",
    "syncSource": "SYNC_SETPOINT",
    "syncMode": "SYNC_ABSOLUTE",
    "dynSyncDirection": "SHORTEST_WAY",
    "masterSyncPosition": 0.0,
    "masterStartDistance": 0.0,
    "parameters": {
       "masterOffset": 0.0,
       "slaveOffset": 0.0,
       "ratioDenominator": 1,
       "ratioNumerator": 1,
       "fineAdjust": 0.0

  },
  "dlParameters": {
     "soiMasterOffsetDlIdx": -1,
     "soiMasterOffsetVelDlIdx": -1,
     "soiMasterOffsetAccDlIdx": -1,
     "soiSlaveOffsetDlIdx": -1,
     "soiSlaveOffsetVelDlIdx": -1,
     "soiSlaveOffsetAccDlIdx": -1,
     "fofMasterOffsetDlIdx": -1,
     "fofMasterOffsetTimeConstantDlIdx": -1,
     "fofSlaveOffsetDlIdx": -1,
     "fofSlaveOffsetTimeConstantDlIdx": -1,
     "fineAdjustDlIdx": -1

  },
  "buffered": true
}

Python:
axs_cmd_gear_in_pos_ex(axs: str, master: str, sync_source: int,
sync_mode: int, dyn_sync_direction: int,
parameters: Dict[str, Union[float, int]],
dl_parameters: Dict[str, int],
buffered: bool,
master_sync_position: float = 0.0,
master_start_distance: float = 0.0) -> int:

"""Couple the axis to a master axis and synchronously follow using position
control.
(objects have to be attached, see motion.attach_obj())

Follow the position of the master axis with a specified gear ratio, fine adjust
and position offsets. The realtime
Data Layer indices for offsets and other parameters also have to be specified.
If an index value is -1, the default index
is selected. If an index value is < 1000, the specified index is used. If an
index value is >= 1000, the system
realtime Data Layer is referred.

Args:
    axs:                Name of the slave axis.
    master:             Name of the master axis.
    sync_source:        Sync source (Setpoint = 0, Actual = 1).
    sync_mode:          Command mode (Relative = 0, RelativeKeepState = 1,
 Absolute = 2, AbsoluteKeepState = 3).
    dyn_sync_direction: Dynamic sync direction (ShortestWay = 0, Positive
 = 1, Negative = 2, Direct = 3).
    parameters:         The parameters used for synchronized motion with
 the following keys:
 master_offset (float): Master offset value.
 slave_offset (float): Slave offset value.
 ratio_numerator (int): Gear ratio numerator.
 ratio_denominator (int): Gear ratio denominator.
 fine_adjustment (float): Fine adjustment parameter.
    dl_parameters:
soi_master_offset_dl_idx (int): index of master offset target
value, second order interpolated.
soi_master_offset_vel_dl_idx (int): index of master offset

velocity constraint for second order interpolation.
soi_master_offset_acc_dl_idx (int): index of master offset
acceleration constraint for second order interpolation.
soi_slave_offset_dl_idx (int): index of slave offset target
value, second order interpolated.
soi_slave_offset_vel_dl_idx (int): index of slave offset
velocity constraint for second order interpolation.
soi_slave_offset_acc_dl_idx (int): index of slave offset
acceleration constraint for second order interpolation.
fof_master_offset_dl_idx (int): index of second master
offset, first order filtered.
fof_master_offset_time_constant_dl_idx (int): index of time
constant for change rate of fofMasterOffset.
fof_slave_offset_dl_idx (int): index of second slave offset,
first order filtered.
fof_slave_offset_time_constant_dl_idx (int): index of time
constant for change rate of fofSlaveOffset.
fine_adjustment_dl_idx (int): index of fine adjustment
percentage in addition to the commanded fine adjustment.
buffered:          Create this command as a buffered command.
master_sync_position:
Master position, where the slave is synchronized with the master
master_start_distance:
Master distance, where the synchronization is started

Returns:
    The command id.
"""

BundleIF:
namespace motion::sync::cmd {
  enum class SyncSource : uint32_t
  {
    ///< use master ipo position (setpoint position)
    SYNC_SETPOINT,

///< use master actual position (encoder position)
SYNC_ACTUAL,

///< use extrapolated master position
SYNC_ACTUAL_EXTRAPOLATED,

SYNC_LAST_ENTRY
   };

   enum class SyncMode : uint32_t
   {
///< run the slave relative and init the pipeline
SYNC_RELATIVE,

///< run the slave relative and keep the pipeline state
SYNC_RELATIVE_KEEP_STATE,

///< use the absolute result of the calculation
///< pipeline for the slave and init the pipeline
SYNC_ABSOLUTE,

  ///< use the absolute result of the calculation
  ///< pipeline for the slave and keep the pipeline state
  SYNC_ABSOLUTE_KEEP_STATE,

  SYNC_LAST_ENTRY
};

enum class DynSyncDirection : uint32_t
{
   SHORTEST_WAY,
   POSITIVE,
   NEGATIVE,
   DIRECT,

Commands
   SYNC_LAST_ENTRY
};

struct GearInPosParameters
{
  ///< master offset value
  double masterOffset {0.0};

  ///< slave offset value
  double slaveOffset {0.0};

  ///< numerator ratio value
  int32_t ratioNumerator {1};

  ///< denominator ratio value
  int32_t ratioDenominator {1};

  ///< fine adjust parameter
  double fineAdjust {0.0};
};

struct GearInPosDlParameters
{
  ///< Data Layer index of master offset
  int32_t soiMasterOffsetDlIdx {-1};

  ///< Data Layer index of master offset velocity
  int32_t soiMasterOffsetVelDlIdx {-1};

  ///< Data Layer index of master offset acceleration
  int32_t soiMasterOffsetAccDlIdx {-1};

  ///< Data Layer index of slave offset
  int32_t soiSlaveOffsetDlIdx {-1};

  ///< Data Layer index of slave offset velocity
  int32_t soiSlaveOffsetVelDlIdx {-1};

  ///< Data Layer index of slave offset acceleration
  int32_t soiSlaveOffsetAccDlIdx {-1};

  ///< Data Layer index of additional master offset
  int32_t fofMasterOffsetDlIdx {-1};

  ///< Data Layer index of additional master offset

///< time constant
int32_t fofMasterOffsetTimeConstantDlIdx {-1};

///< Data Layer index of additional slave offset
int32_t fofSlaveOffsetDlIdx {-1};

///< Data Layer index of additional slave offset
///< time constant
int32_t fofSlaveOffsetTimeConstantDlIdx {-1};

///< Data Layer index of additional fine adjust
int32_t fineAdjustDlIdx {-1};
    };
}

::motion::core::MotionResult (*axsGearInPosCmdEx2)
(void* handle,
 const ::motion::core::dia::CmdSourceInfo& sourceInfo,
 const char* slaveName,
 const char* masterName,
 ::motion::sync::cmd::SyncSource syncSource =
 ::motion::sync::cmd::SyncSource::SYNC_SETPOINT,
 ::motion::sync::cmd::SyncMode syncMode =
 ::motion::sync::cmd::SyncMode::SYNC_RELATIVE,
 ::motion::sync::cmd::DynSyncDirection dynSyncDirection =
 ::motion::sync::cmd::DynSyncDirection::SHORTEST_WAY,
 double masterSyncPosition,
 double masterStartDistance,
 motion::sync::cmd::GearInPosParameters& parameters,
 motion::sync::cmd::GearInPosDlParameters& dlParameters,
 bool buffered = false,
 uint64_t& cmdId);

### 7.2.23 AxsGearInVel - Synchronizing to velocity

Basics
GearInVel belongs to a group of synchronized Motion functions that behave
like a gearbox. The GearInVel commands control the slave axis in the
"velocity" function on the drive and use the velocity of the master axis. As
a result, the velocity of the slave axis (y) is proportional to the velocity of
the master axis with the specified ratio. Note that the GearInVel commands
can also calculate the position by integrating the calculated velocity, but this
position is not controlled by the drive. The actual axis position may therefore
deviate from this calculated position.
After the GearInVel command, the axis remains in the gearing function. To end
the command, the command has to be canceled. For example, by a cancel
command or by a new, non-buffered Motion command. A new command of
the GearInVel command results in the axis not being synchronized when the
command becomes active.

Functional description of GearInVel
GearInVel are Motion commands for axes that are based on the functionality
of synchronized Motion. GearInVel can be issued as a buffered command or
as an unbuffered command. The commanded axis becomes a slave axis in

relation to a specific master axis. This command sets the slave axis to the
PLCopen state SYNCHRONIZED MOTION. While the command is ACTIVE, the
velocity of the slave axis follows the velocity of the master axis.
The status of the synchronized Motion of the GearInVel commands always
changes from NO_SYNC_MOTION to INITIAL_DYN_SYNCHRONIZING, as their
calculation pipeline uses the derivation calculation step.
While the GearInVel command is active, the command ensures that the motion
of the slave axis does not violate any restrictions for maximum velocity, max‐
imum acceleration and maximum jerk. Due to these restrictions, it is possible
that the slave axis cannot follow the master axis. For example, if the slave
axis has to move faster than the maximum velocity specification allows. The
violation of a constraint condition leads to a reaction defined by the config‐
ured dynamic synchronization error reaction, see ⮫ Chapter Error reaction

on page 126.
The following GearInVel commands are available:
● AxsGearInVelCmd
● AxsGearInVelCmdEx
Both commands have the following parameters:
Table 65: GearInVel command parameters
Command parameters                                     Description
masterName                                             Master axis name
syncSource                                             Master axis used for toothing, only the
                                                       SYNC_SETPOINT option is supported. The
                                                       command returns an error if another option
                                                       is specified
Parameters                    slaveVelOffset           Slave axis offset value
                              ratioNumerator           Numerator of the transmission ratio as a
                                                       rational number. The parameter can be neg‐
                                                       ative in order to realize a counter-rotating
                                                       gear
                              ratioDenominator         Denominator of the transmission ratio as a
                                                       rational number. The parameter can be neg‐
                                                       ative in order to realize a counter-rotating
                                                       gear
                              fineAdjust               Percentage fine adjustment of the gear ratio
                                                       as a rational number. The value causes an
                                                       immediate change in the output of the cal‐
                                                       culation pipeline without interpolation or
                                                       filtering
buffered                                               Flag: buffered or non-buffered command

The behavior of the GearInVel commands can be influenced by using parame‐
ters in the Data Layer RT of the axis. The standard indices for each Data Layer
variable are listed in the following table.
Table 66: Data Layer RT index values for GearInVel
Data Layer RT index     Parameter name       Description                   Remarks
0                       soiMasterOffsetDlIdx Data Layer RT index for       Same index as Gear‐
                                             master axis, interpolated     InPos
                                             second order. When set to -1,
                                             the Data Layer RT input index
                                             0 is used

Data Layer RT index      Parameter name        Description                      Remarks
1                        soiMasterOffsetVelIdx Data Layer RT index for the      Same index as Gear‐
                        master axis offset velocity      InPos
                        constraint for second-order
                        interpolation. When set to -1,
                        the Data Layer RT input index
                        1 is used
2                        soiMasterOffsetAc‐    Data Layer RT index for the      Same index as Gear‐
  cIdx                  master axis offset accelera‐     InPos
                        tion limitation for second
                        order interpolation. If set to
                        -1, the Data Layer RT input
                        index 2 is used
6                        fofMasterOffsetDlIdx Data Layer RT index for           Same index as Gear‐
                        master axis offset, filtered     InPos
                        first order. If set to -1, the
                        Data Layer RT input index 6
                        is used
7                        fofMasterOffsetTime‐ Data Layer RT index for the       Same index as Gear‐
  ConstantDlIdx         master axis offset time con‐ InPos
                        stant for the change rate. If
                        set to -1, the Data Layer RT
                        input index 7 is used
10                       fineAdjustDlIdx       Data Layer RT index for per‐ Same index as Gear‐
                        centage fine adjustment. With InPos
                        a setting of -1, the Data Layer
                        RT input index 10 is used
11                       slaveVelOffsetDlIdx   Data Layer RT index for the
                        slave axis. If set to -1, the
                        Data Layer RT input index 11
                        is used
12                       foiSlaveOffsetDlIdx   Data Layer RT index for slave
                        axis, interpolated first order.
                        If set to -1, the Data Layer RT
                        input index 12 is used
13                       foiSlaveOffsetAcc‐    Data Layer RT index for the
  DlIdx                 slave axis offset acceleration
                        limitation for the first order
                        interpolation. If set to -1, the
                        Data Layer RT input index 13
                        is used

Note that the standard input indices of the Data Layer RT start at 0 and
continue without a gap in between. The meaning of the standard indices is
different for the GearInPos and GearInVel commands.
A GearInVel command does not actively initialize the Data Layer RT. The com‐
mands do not write any data to the Data Layer RT. The user of the system is
responsible for setting values in the Data Layer RT.
AxsGearInVelCmdEx offers more flexibility than AxsGearInVelCmd. Both com‐
mands use the Data Layer RT for all variables of the Data Layer RT. How‐
ever, AxsGearInVelCmd does not offer the option of specifying indices for
the Data Layer RT variables, but uses AxsGearInVelCmdEx with a value of -1
for each Data Layer index. The value -1 is interpreted by AxsGearInVelCmdEx
as the default index for each of the parameters specified with the value -1.

The first 15 elements in the Data Layer RT are reserved for Motion.sync com‐
mands and are partly used for the GearInVel commands. Data Layer RT path:
motion®admin®axs®{axis-name}®cfg®realtime-inputs®double-array-size.

PLC:

Table 67: ML_AxsGearInVel
STRUCT ML_AxsGearInVelData

Name       Data type    Inherited         Address       Initial value   Comment
                        from
  In       ML_iAxsGear‐                                                 Input: Command data of
           InVel                                                        the command
  Out      ML_oCmdRe‐                                                   Output: Command parame‐
           sult                                                         ters
STRUCT ML_AxsGearInVelExData
Name       Data type    Inherited         Address       Initial value   Comment
                        from
  In       ML_iAxsGear‐                                                 Input: Command data of
           InVelEx                                                      the command
  Out      ML_oCmdRe‐                                                   Output: Command parame‐
           sult                                                         ters
ENUM ML_SyncSource
Name       Data type         Inherited    Address       Initial value   Comment
                             from
  SYNC_SET‐ INT
POINT
            INT
SYNC_ACTUA
L
STRUCT ML_iAxsGearInVelParameters
Name         Data type  Inherited         Address       Initial value   Comment
                        from
  SlaveVe‐   LREAL                                                      Slave axis offset
lOffset
  RatioNum‐ DINT                                                        Numerator of the ratio
erator
  RatioDeno‐ DINT                                                       Denominator of the ratio
minator
  FineAdjust LREAL
STRUCT ML_iAxsGearInVelDlParameters
Name         Data type   Inherited        Address       Initial value   Comment
                         from
  SoiMaster‐ DINT                                       -1              Master axis Data Layer
OffsetDlIdx                                                             index used for second-
                                                                        order offset

STRUCT ML_iAxsGearInVelDlParameters
  SoiMaster‐ DINT                                 -1            Master axis offset velocity
OffsetVel‐                                                      Data Layer index used for
DlIdx                                                           second-order offset
  SoiMaster‐ DINT                                 -1            Master axis offset accelera‐
OffsetAcc‐                                                      tion Data Layer index for
DlIdx                                                           second-order offset
  FofMaster‐ DINT                                 -1            Master axis Data Layer
OffsetDlIdx                                                     index used for filtered first-
                                       order offset
  FofMaster‐ DINT                                 -1            Master axis Time constant
OffsetTime‐                                                     Data Layer index for fil‐
Constant‐                                                       tered first-order offset
DlIdx
  FineAdjust‐ DINT                                -1            Fine adjustment Data Layer
DlIdx                                                           index for fine adjustment of
                                       the transmission ratio
  SlaveVe‐   DINT                                 -1            Slave axis offset velocity
lOffsetDlIdx                                                    Data Layer Index
  FoiSla‐    DINT                                 -1            Slave axis Data Layer index
veOffset‐                                                       used for the first-order
DlIdx                                                           interpolated offset
  FoiSla‐    DINT                                 -1            Slave axis offset accelera‐
veOffsetAcc‐                                                    tion Data Layer index used
DlIdx                                                           for first-order interpolated
                                       offset
STRUCT ML_iAxsGearInVel EXTENDS ML_iAxsCmdBase
Name        Data type    Inherited  Address    Initial value    Comment
                         from
   Master‐  STRING(15)                                          Name of the master axis
Name                                                            that is being followed
   Syn‐     ML_Syn‐                                             Synchronization source
cSource     cSource
   Parame‐  ML_iAxsGear‐                                        Parameters for the Gear‐
ters        InVelParame‐                                        InVel command
            ters
   Buffered BOOL                                                TRUE, if the command
                                                                is to be executed as buf‐
                                                                fered command, otherwise
                                                                FALSE
STRUCT ML_iAxsGearInVelEx EXTENDS ML_iAxsCmdBase
Name        Data type    Inherited  Address     Initial value   Comment
                         from
   Master‐  STRING(15)                                          Name of the master axis
Name                                                            that is being followed
   Syn‐     ML_Syn‐                                             Synchronization source
cSource     cSource
   Parame‐  ML_iAxsGear‐                                        Parameters for the Gear‐
ters        InVelParame‐                                        InVel command
            ters

STRUCT ML_iAxsGearInVelEx EXTENDS ML_iAxsCmdBase
DlParameters ML_iAxsGear‐                                           Data Layer parameters for
InVelDlPara‐                                           the GearInVel command
meters
  Buffered   BOOL                                                   TRUE, if the command
                                                is to be executed as buf‐
                                                fered command, otherwise
                                                FALSE

Data Layer
Method: POST
URL: motion/axs/<axs_name>/cmd/gear-in-vel

Payload:
{
    "masterName": "X",
    "syncSource": "SYNC_SETPOINT",
    "parameters": {
       "slaveVelOffset": 0.0,
       "ratioNumerator": 1,
       "ratioDenominator": 1,
       "fineAdjust": 0.0
    },
    "buffered": true
}

Method: POST
URL: motion/axs/<axs_name>/cmd/gear-in-vel-ex
Payload:
{
    "masterName": "X",
    "syncSource": "SYNC_SETPOINT",
    "parameters": {
       "slaveVelOffset": 0.0,
       "ratioNumerator": 1,
       "ratioDenominator": 1,
       "fineAdjust": 0.0
    },
    "dlParameters": {
       "soiMasterOffsetDlIdx": -1,
       "soiMasterOffsetVelDlIdx": -1,
       "soiMasterOffsetAccDlIdx": -1,
       "fofMasterOffsetDlIdx": -1,
       "fofMasterOffsetTimeConstantDlIdx": -1,
       "slaveVelOffsetDlIdx": -1,
       "foiSlaveOffsetDlIdx": -1,
       "foiSlaveOffsetAccDlIdx": -1,
       "fineAdjustDlIdx": -1
    },
    "buffered": true
}

Python:
axs_cmd_gear_in_vel(axs: str, master: str, sync_source: int,
parameters: Dict[str, Union[float, int]], buffered: bool)
-> int:

"""Couple an axis to a master axis and synchronously follow
   using velocity control.

   Follow the velocity of the master axis with a specified
   gear ratio, fine adjust and velocity offset. The command
   uses the realtime Data Layer (at motion axis or system
   level), where the parameter locations in the realtime
   Data Layer are pre-defined.
   To explicitly define the locations of these parameters
   in the realtime Data Layer axs_cmd_gear_in_vel_ex can be
   used.

   Arguments:
      axs:              Name of the slave axis.
      master:           Name of the master axis.
      sync_source:      Sync source (Setpoint = 0, Actual = 1).
      parameters:       Parameters used for synchronized motion
                        with the following keys:
                        slave_vel_offset: (float):
                             Slave velocity offset value.
                        ratio_numerator (int):
                             Gear ratio numerator.
                        ratio_denominator (int):
                             Gear ratio denominator.
                        fine_adjustment (float):
                             Fine adjustment parameter.
      buffered:         True: create this command as a
                               buffered command.
                        False: create this command as a
                               non-buffered command.

   Returns:
      The command id.
"""

axs_cmd_gear_in_vel_ex(axs: str, master: str, sync_source: int,
parameters: Dict[str, Union[float, int]],
dl_parameters: Dict[str, int], buffered: bool) -> int:

"""Couple an axis to a master axis and synchronously follow
   using velocity control.

   Follow the velocity of the master axis with a specified
   gear ratio, fine adjust and velocity offset. The realtime
   Data Layer indices for offsets and other parameters also
   have to be specified.
   If an index value is -1, the default index is selected.
   If an index value is < 1000, the specified index is used.
   If an index value is >= 1000, the system realtime Data
   Layer is referred.

   Arguments:

axs:              Name of the slave axis.
master:           Name of the master axis.
sync_source:      Sync source (Setpoint = 0, Actual = 1).
parameters:       Parameters used for synchronized motion
with the following keys:
slave_vel_offset: (float):
   Slave velocity offset value.
ratio_numerator (int):
   Gear ratio numerator.
ratio_denominator (int):
   Gear ratio denominator.
fine_adjustment (float):
   Fine adjustment parameter.

dl_parameters:    soi_master_offset_dl_idx (int):
   index of master offset target value,
   second order interpolated.
soi_master_offset_vel_dl_idx (int):
   index of master offset velocity
   constraint for second order
   interpolation.
soi_master_offset_acc_dl_idx (int):
   index of master offset acceleration
   constraint for second order
   interpolation.
fof_master_offset_dl_idx (int):
   index of second master offset,
   first order filtered.
fof_master_offset_time_constant_dl_idx
(int):
   index of time constant for change
   rate of fofMasterOffset.
slave_vel_offset_dl_idx (int):
   index of slave offset without
   constraints.
foi_slave_offset_dl_idx (int):
   index of slave offset constraint
   for first order interpolation.
foi_slave_offset_acc_dl_idx (int):
   index of slave offset acceleration
   constraint for first order
   interpolation.
fine_adjustment_dl_idx (int):
   index of fine adjustment percentage
   in addition to the commanded fine
   adjustment.
buffered:         True: create this command as a
       buffered command.
False: create this command as a
       non-buffered command.

Returns:
The command id.
"""

BundleIF:
namespace motion::sync::cmd {
  enum class SyncSource : uint32_t
  {
    ///< use master ipo position (setpoint position)
    SYNC_SETPOINT,

      ///< use master actual position (encoder position)
      SYNC_ACTUAL,

      ///< use extrapolated master position
      SYNC_ACTUAL_EXTRAPOLATED,

      SYNC_LAST_ENTRY
   };

   struct GearInVelParameters
   {
     ///< slave velocity offset value
     double slaveVelOffset {0.0};

      ///< numerator ratio value
      int32_t ratioNumerator {1};

      ///< denominator ratio value
      int32_t ratioDenominator {1};

      ///< fine adjust parameter
      double fineAdjust {0.0};
   };

   struct GearInVelDlParameters
   {
     ///< Data Layer index of master offset
     int32_t soiMasterOffsetDlIdx {-1};

      ///< Data Layer index of master offset velocity
      int32_t soiMasterOffsetVelDlIdx {-1};

      ///< Data Layer index of master offset acceleration
      int32_t soiMasterOffsetAccDlIdx {-1};

      ///< Data Layer index of additional master offset
      int32_t fofMasterOffsetDlIdx {-1};

      ///< Data Layer index of additional master offset
      ///< time constant
      int32_t fofMasterOffsetTimeConstantDlIdx {-1};

      ///< Data Layer index of slave velocity offset
      int32_t slaveVelOffsetDlIdx {-1};

      ///< Data Layer index of additional slave offset
      int32_t foiSlaveOffsetDlIdx {-1};

      ///< Data Layer index of additional slave offset
      ///< acceleration

int32_t foiSlaveOffsetAccDlIdx {-1};

///< Data Layer index of additional fine adjust
int32_t fineAdjustDlIdx {-1};
    };
}

::motion::core::MotionResult(*axsGearInVelCmd)
(void* handle,
 const ::motion::core::dia::CmdSourceInfo& sourceInfo,
 const char* slaveName,
 const char* masterName,
 ::motion::sync::cmd::SyncSource syncSource,

 const ::motion::sync::cmd::GearInVelParameters& parameters,
 bool buffered,
 uint64_t& cmdID);

::motion::core::MotionResult(*axsGearInVelCmdEx)
(void* handle,
 const ::motion::core::dia::CmdSourceInfo& sourceInfo,
 const char* slaveName,
 const char* masterName,
 ::motion::sync::cmd::SyncSource syncSource,
 const ::motion::sync::cmd::GearInVelParameters& parameters,
 const ::motion::sync::cmd::GearInVelDlParameters&
 dlParameters,
 bool buffered,
 uint64_t& cmdID);

### 7.2.24 AxsCamIn, AxsCamInEx - Controlling a cam with a scaling factor

Basics
This command uses the "Cam with scaling factor" feature to link a slave axis
to a master axis. The coupling is position-based.
The CamIn command is based on a simplified Flexprofile command with a
point table and an adjustable scaling factor (stroke).
As soon as the command is active, the PLCOpen status of the axis is set to
SYNCHRONIZED_MOTION. The CamIn command does not end automatically,
but has to be aborted by another unbuffered command (such as AxsAbort or
PosAbs).
ML_AxsGetPLCOpenState or ML_GetCmdState can be used to read the status.
In addition, the status of the synchronization can be queried with ML_AxsGet‐
SyncMotionState (see ⮫ Chapter 7.2.18 AxsGetSyncMotionState - Synchroniza‐
tion state on page 385).
If an error occurs before the execution (e.g. violation of the dynamic limit,
invalid command parameters), the command is not added to the axis object.
If an error occurs during execution, the slave axis is set to the ERRORSTOP
state and it brakes to a standstill. The master axis is not affected by an error
in the slave axis. If the master axis goes into the ERROR_STOP state, the slave
axis continues to follow the calculated slave axis target position. Typically, the
master axis stops in the event of an error, which means that the slave axis
also stops. However, the FlexProfile command of the slave axis remains active.
This command requires that the axis is active (STANDSTILL, DIS‐
CRETE_MOTION, SYNCHRONIZED_MOTION or CONTINUOUS_MOTION state).

PLC:

STRUCT ML_AxsCamInData
Name       Data type   Inherited               Address   Initial value   Comment
                       from
  In       ML_iAxs‐                                                      Input: Command data of
           CamIn                                                         the command
  Out      ML_oCmdRe‐                                                    Output: Command parame‐
           sult                                                          ters
STRUCT ML_iAxsCamIn EXTENDS ML_iAxsCmdBase
Name        Data type  Inherited   Address               Initial value   Comment
                       from
  AxisName STRING(15) ML_iAxsCmd‐                                        Name of the axis used to
                       Base                                              execute the command
  Source    STRING(50) ML_iAxsCmd‐                                       Specifies the command
                       Base                                              source, e.g PlcApplication1
                                                                         is displayed in the diag‐
                                                                         nostic messages
   SourceLine ULINT              ML_iAxsCmd‐                             Specifies the source line of
                                 Base                                    the command; is displayed
                                                                         in the diagnostic messages
   Master‐         STRING(15)                                            Name of the master axis to
Name                                                                     be added to the axis
   Syn‐            ML_Syn‐                                               Synchronization source
cSource            cSource
   DynSync‐        ML_DynSync‐                                           Synchronization direction
Direction          Direction
   Parame‐         ML_iAxsCa‐                                            Parameters for the CamIn
ters               mInParame‐                                            command
                   ters
STRUCT ML_iAxsCamInParameters
Name        Data type  Inherited               Address   Initial value   Comment
                       from
  Master‐   LREAL                                        0.0             Offset of the master axis
Offset
  Slave‐    LREAL                                        0.0             Offset of the slave axis
Offset
  RatioNum‐ DINT                                         1               Transmission ratio counter
erator                                                                   for master axis gearbox
                                                                         output revolutions (limited
                                                                         to a value between 0 and
                                                                         65535)
  RatioDeno‐ DINT                                        1               Transmission ratio - denom‐
minator                                                                  inator master axis gear
                                                                         input revolutions (limited
                                                                         to a value between 0 and
                                                                         65535)

STRUCT ML_iAxsCamInParameters
  FineAdjust LREAL                                  0.0        Fine adjustment of the gear
ratio in %
  GainFactor LREAL                                  1.0        Scaling factor for cam
table
   AngleAd‐   LREAL                                 0.0        Constant angle adjustment
just                                                           for CamIn
   Profi‐     ML_Profi‐                             SLAVE_CUR‐ Describes how the origin
leEntry       leEntry                               RENT_MASTE of the profile is to be inter‐
R_CURRENT preted at a profile start or
profile change
  ProfileExe‐ ML_ProfileEx‐                         PRO‐       Determines how the Flex‐

cutionMode ecutionMode                              FILE_MODE_ Profile is executed
CYCLIC
  PointTable STRING(50)                                        Specifies which cam table
is to be executed
   SwitchPo‐ LREAL                                  0.0        Master axis used to switch
sition                                                         to the new profile and/or
the new gear
   SwitchPro‐ BOOL                                  FALSE      If FALSE, the system imme‐
fileOnPos                                                      diately switches to the
selected profile. If TRUE,
the system only switches
to the selected profile
when the switch position is
reached
  Switch‐     BOOL                                  FALSE      If FALSE, the system imme‐
GearOnPos                                                      diately switches to the
selected gear. If TRUE, the
system only switches to
the selected gear when the
SwitchPosition is reached
   SwitchPo‐ LREAL                                  0.0        Master position at which
sitionGain‐                                                    a changed scaling factor
Factor                                                         takes effect (if "Switch‐
GainFactorOnPos" is set
accordingly)
SwitchGain‐ BOOL                                    FALSE      Select if the scaling
FactorOnPos                                                    factor is applied immedi‐
ately when executing the
command or is applied
depending on the position.
  GearRe‐     DINT                                  0          Gear reduction ratio (disa‐
duction                                                        bled if 0; limited to a value
between 0 and 65535)
ENUM ML_SyncSource
Name       Data type          Inherited   Address   Initial value   Comment
                              from
  SYNC_SET‐ INT                                                     Synchronize based on the
POINT                                                               command value of the
                                                                    master axis(es)

ENUM ML_SyncSource
INT                                                  Synchronization based on
SYNC_ACTUA                                                      the actual value of the
L                                                               master axis(es)
INT                                                  Synchronization based on
SYNC_ACTUA                                                      the extrapolated actual
L_EXTRAPO‐                                                      value of the master
LATED                                                           axis(es)
ENUM ML_DynSyncDirection
Name       Data type    Inherited     Address   Initial value   Comment
                        from
           INT                                                  Initiating synchronization
SHORTEST_                                                       via the shortest path
WAY
  POSITIVE INT                                                  Synchronization always in
                                                                positive direction
   NEGATIVE INT                                                 Synchronization always in
                                                                negative direction
DIRECT             INT                                          Synchronization takes
                                                                place immediately without
                                                                dynamic synchronization
ENUM ML_ProfileEntry
Name       Data type      Inherited   Address   Initial value   Comment
                          from
                   INT                                          Absolute access to the pro‐
SLAVE_ORIGI                                                     file
N_MASTER_O
RIGIN
                   INT                                          The profile starts at the
SLAVE_CUR‐                                                      current position of the
RENT_MASTE                                                      master axis and the slave
R_CURRENT                                                       axis
                   INT                                          Profile starts at the current
SLAVE_ORIGI                                                     position of the master axis
N_MASTER_C                                                      and the absolute position
URRENT                                                          of the slave axis
                   INT                                          Profile starts at the current
SLAVE_CUR‐                                                      position of the slave axis
RENT_MASTE                                                      and the absolute position
R_ORIGIN                                                        of the master axis
                   INT                                          The profile starts at the
SLAVE_RELA‐                                                     absolute master axis posi‐
TIVE_MASTE                                                      tion. The position of the
R_ORIGIN                                                        slave axis is defined so that
                                                                the axis is moved relatively
ENUM ML_ProfileExecutionMode
Name       Data type     Inherited    Address   Initial value   Comment
                         from
  PRO‐     INT                                                  The profile is processed
FILE_MODE_                                                      cyclically
CYCLIC

ENUM ML_ProfileExecutionMode
  PRO‐     INT                                                         The profile is processed
FILE_MODE_                                                             once and then continued at
SINGLE                                                                 final speed
  PRO‐     INT                                                         Reserved
FILE_MODE_
JUMP

Data Layer:
Method: POST
URL:         https://<ip-addr>/automation/api/v2/nodes/motion/axs/<axs‐
Name>/cmd/cam-in

Payload:

{
"type":"object","value":
{
    "master": "R_Main",
    "syncSource": "SYNC_SETPOINT",
    "dynSyncDirection": "SHORTEST_WAY",
    "parameters": {
        "masterOffset": 0,
        "slaveOffset": 0,
        "ratioNumerator": 1,
        "ratioDenominator": 1,
        "fineAdjust": 0,
        "gainFactor": 1,
        "angleAdjust": 0,
        "profileEntry": "SLAVE_CURRENT_MASTER_CURRENT",
        "profileExecutionMode": "CYCLIC",
        "pointTable": "Cam2",
        "switchPosition": 0,
        "switchProfileOnPos": false,
        "switchGearOnPos": false,
        "switchPositionGainFactor": 0,
        "switchGainFactorOnPos": false,
        "gearReduction": 0
    }
}

Python:
<cmdID> = motion.axs_cmd_cam_in( axs=<axsName>,
master=<masterName> [,sync_source=<syncSource>]
[,dyn_Sync_direction=<dynSyncDirection>]
[,parameters=<parameter>] )

Creates a CamIn command for a single axis (object has to be "attached"), see
documentation Python Runtime App ⮫ Python functions.
● <axsName> - string, name of the axis object (slave axis)
● <masterName> - string, name of the axis object (master axis)
● <syncSource> - int, which value of the master axis is to be used as the
  basis for the electronic cam? Interpolated position of the master axis = 0,
  actual position of the master axis = 1, extrapolated actual position of the
  master axis = 2

● <dynSyncDirection> - int, how should a modulo axis be synchronized?
  Shortest path = 0, positive = 1, negative = 2, direct = 3
● <parameter> - Dict[str, Union[bool, float, int, string]], parameters of the
  CamIn functionality:
  – "master_offset" - float, offset on the side of the master axis
  – "slave_offset" - float, offset on the side of the slave axis
  – "ratio_numerator" - int, counter of the gear function
  – "ratio_denominator" - int, denominator of the gear function
  – "fine_adjust" - float, percentage value of the fine adjustment
  – “gain_factor” – float, scaling factor for cam table
  – "angle_adjust" - float, constant angle adjustment for CamIn
  – "profile_entry" - int, synchronization method,
    SLAVE_ORIGIN_MASTER_ORIGIN = 0, SLAVE_CURRENT_MASTER_CUR‐
    RENT = 1, SLAVE_ORIGIN_MASTER_CURRENT = 2, SLAVE_CUR‐
    RENT_MASTER_ORIGIN = 3, SLAVE_RELATIVE_MASTER_ORIGIN = 4
  – "profile_execution_mode" - int, how should the profile be interpreted?
    CYCLIC = 0, SINGLE = 1
  – “pointTable” – string, cam table name (e. g. "Cam1" or "Cam2")
  – "switch_position" - float, position at which the command should become
    active
  – "switch_profile_on_pos" - bool, should the command only become active
    at the position specified in "switch_position"?
  – "switch_gear_on_pos" - bool, should the gear function only be switched
    at the position specified in "switch_position"?
  – “switch_position_gain_factor” – float, master position at which a
    changed scaling factor becomes active
  – “switch_gain_factor_on_pos” – Bool, select if the scaling factor is
    applied immediately when executing the command or is applied
    depending on the position
  – "gear_reduction" – int, gear reduction ratio (disabled if 0)

BundleIF:

/// @brief Create an axis synchronized motion command for
CamIn function with gear reduction parameter
///
/// @param[in]     handle           Handle of the interface
(not used)
/// @param[in]     sourceInfo       Command source information
/// @param[in]     slaveName        Name of the slave motion
object
/// @param[in]     masterName       Name of the master motion
object
/// @param[in]     syncSource       Sync source
/// @param[in]     dynSyncDirection Dynamic Sync direction
/// @param[in]     parameters       CamIn parameters
/// @param[out]    cmdID            The ID of the added command
/// @return                         Status of the function
call: STS_OK or an error code on failure.
::motion::core::MotionResult(*axsCamInCmd2)(void* handle,
const ::motion::core::dia::CmdSourceInfo& sourceInfo, const
char* slaveName, const char*
masterName, ::motion::sync::cmd::SyncSource syncSource,

   ::motion::sync::cmd::DynSyncDirection dynSyncDirection,
const ::motion::sync::cmd::CamInParameters2& parameters,
std::uint64_t& cmdId);

PLC:

STRUCT ML_AxsCamInExData
Name       Data type   Inherited           Address   Initial value   Comment
                       from
  In       ML_iAxsCa‐                                                Input: Command data of
           mInEx                                                     the command
  Out      ML_oCmdRe‐                                                Output: Command parame‐
           sult                                                      ters
STRUCT ML_iAxsCamInEx EXTENDS ML_iAxsCmdBase
Name        Data type   Inherited  Address           Initial value   Comment
                        from
  AxisName STRING(15) ML_iAxsCmd‐                                    Name of the axis used to
                        Base                                         execute the command
  Source    STRING(50) ML_iAxsCmd‐                                   Specifies the command
                        Base                                         source, e.g PlcApplication1
                                                                     is displayed in the diag‐
                                                                     nostic messages
  SourceLine ULINT           ML_iAxsCmd‐                             Specifies the source line of
                             Base                                    the command; is displayed
                                                                     in the diagnostic messages
   Master‐    STRING(15)                                             Name of the master axis to
Name                                                                 be added to the axis
   Syn‐      ML_Syn‐                                                 Synchronization source
cSource      cSource
   DynSync‐  ML_DynSync‐                                             Synchronization direction
Direction    Direction
   Parame‐   ML_iAxsCa‐                                              Parameters for the CamIn
ters         mInParame‐                                              command
             ters
   DlParame‐ ML_iAxsCa‐                                              Data Layer parameters for
ters         mInDIPara‐                                              the gear in position com‐
             meters                                                  mand
STRUCT ML_iAxsCamInDlParameters
Name         Data type Inherited           Address   Initial value   Comment
                       from
  SoiMaster‐ DINT                                    -1              The Data Layer index of the
OffsetDlIdx                                                          master axis used for the
                                                                     second-order offset

STRUCT ML_iAxsCamInDlParameters
  SoiMaster‐ DINT                                          -1           The Data Layer index of the
OffsetVel‐                                                              master axis for the velocity
DlIdx                                                                   used for the second-order
offset
  SoiMaster‐ DINT                                          -1           The Data Layer index of the
OffsetAcc‐                                                              master axis for the acceler‐
DlIdx                                                                   ation used for the second-
order offset
  SoiSla‐          DINT                                    -1           The Data Layer index of the
veOffset‐                                                               slave axis for the second
DlIdx                                                                   order offset
  SoiSla‐          DINT                                    -1           The Data Layer index of the
veOffsetVel‐                                                            slave offset for the velocity
DlIdx                                                                   used for the second-order
offset
  SoiSla‐    DINT                                          -1           The Data Layer index of the
veOffsetAcc‐                                                            slave axis for the acceler‐
DlIdx                                                                   ation used for the second-
order offset
  FofMaster‐ DINT                                          -1           The Data Layer index of the
OffsetDlIdx                                                             master axis for the filtered
first-order offset
  FofMaster‐ DINT                                          -1           The Data Layer index of the
OffsetTime‐                                                             master axis for the time
Constant‐                                                               constant used for the fil‐
DlIdx                                                                   tered first-order offset
  FofSla‐     DINT                                         -1           The Data Layer index of the
veOffset‐                                                               slave axis used for the fil‐
DlIdx                                                                   tered first-order offset
  FofSla‐     DINT                                         -1           The Data Layer index of the
veOffsetTi‐                                                             slave axis for the time con‐
meConstant‐                                                             stant used for the filtered
DlIdx                                                                   first-order offset
  FineAdjust‐ DINT                                         -1           The Data Layer index for
DlIdx                                                                   fine adjustment, which is
used to fine-tune the trans‐
mission ratio
SoiAngleAd‐        DINT                                    -1           The Data Layer index used
justDlIdx                                                               for the angle adjustment
SoiAngleAd‐        DINT                                    -1           The Data Layer index used
justVelDlIdx                                                            for the velocity of the angle
adjustment
SoiAngleAd‐ DINT                                           -1           The Data Layer index used
justAccDlIdx                                                            for the acceleration of the
angle adjustment
fofAngleAd‐        DINT                                    -1           The Data Layer index used
justDlIdx                                                               for first-order filtering of
the angle adjustment
fofAngleAd‐ DINT                                           -1           The Data Layer index used
justTimeCon‐                                                            for the filter time constant
stantDlIdx                                                              of the angle adjustment
For other parameters such as ML_iAxsCamInParameter, see ML_AxsCamIn.

Data Layer:
Method: POST
URL:         https://<ip-addr>/automation/api/v2/nodes/motion/axs/<axs‐
Name>/cmd/cam-in-ex
Payload:

{
"type":"object","value":
{
    "master": "R_Main",
    "syncSource": "SYNC_SETPOINT",
    "dynSyncDirection": "SHORTEST_WAY",

    "parameters": {
        "masterOffset": 0,
        "slaveOffset": 0,
        "ratioNumerator": 1,
        "ratioDenominator": 1,
        "fineAdjust": 0,
        "gainFactor": 1,
        "angleAdjust": 0,
        "profileEntry": "SLAVE_CURRENT_MASTER_CURRENT",
        "profileExecutionMode": "CYCLIC",
        "pointTable": "Cam2",
        "switchPosition": 0,
        "switchProfileOnPos": false,
        "switchGearOnPos": false,
        "switchPositionGainFactor": 0,
        "switchGainFactorOnPos": false,
        "gearReduction": 0
    },
    "dlParameters": {
        "soiMasterOffsetDlIdx": -1,
        "soiMasterOffsetVelDlIdx": -1,
        "soiMasterOffsetAccDlIdx": -1,
        "soiSlaveOffsetDlIdx": -1,
        "soiSlaveOffsetVelDlIdx": -1,
        "soiSlaveOffsetAccDlIdx": -1,
        "fofMasterOffsetDlIdx": -1,
        "fofMasterOffsetTimeConstantDlIdx": -1,
        "fofSlaveOffsetDlIdx": -1,
        "fofSlaveOffsetTimeConstantDlIdx": -1,
        "fineAdjustDlIdx": -1,
        "soiAngleAdjustDlIdx": -1,
        "soiAngleAdjustVelDlIdx": -1,
        "soiAngleAdjustAccDlIdx": -1,
        "fofAngleAdjustDlIdx": -1,
        "fofAngleAdjustTimeConstantDlIdx": -1
    }
}
}

Python:
<cmdID> = motion.axs_cmd_cam_in_ex( axs=<axsName>,
master=<masterName> [,sync_source=<syncSource>]
[,dynSync_direction=<syncDirection>]
[,parameters=<parameter>] )

Creates a CamIn command for a single axis (object has to be "attached"), see
documentation Python Runtime App ⮫ Python functions.
● <axsName> - string, name of the axis object (slave axis)
● <masterName> - string, name of the axis object (master axis)
● <syncSource> - int, which value of the master axis is to be used as the
basis for the electronic cam? Interpolated position of the master axis = 0,
actual position of the master axis = 1, extrapolated actual position of the
master axis = 2
● <dynSyncDirection> - int, how should a modulo axis be synchronized?
Shortest path = 0, positive = 1, negative = 2, direct = 3
● <parameter> - Dict[str, Union[bool, float, int, string]], parameter of the
FlexProfile functionality:
– "master_offset" - float, offset on the side of the master axis
– "slave_offset" - float, offset on the side of the slave axis
– "ratio_numerator" - int, counter of the gear function
– "ratio_denominator" - int, denominator of the gear function
– "fine_adjust" - float, percentage value of the fine adjustment
– “gain_factor” – float, scaling factor for cam table
– "angle_adjust" - float, constant angle adjustment for CamIn
– "profile_entry" - int, synchronization method,
   SLAVE_ORIGIN_MASTER_ORIGIN = 0, SLAVE_CURRENT_MASTER_CUR‐
   RENT = 1, SLAVE_ORIGIN_MASTER_CURRENT = 2, SLAVE_CUR‐
   RENT_MASTER_ORIGIN = 3, SLAVE_RELATIVE_MASTER_ORIGIN = 4
– "profile_execution_mode" - int, how should the profile be interpreted?
   CYCLIC = 0, SINGLE = 1
– “pointTable” – string, cam table name (e. g. "Cam1" or "Cam2")
– "switch_position" - float, position at which the command should become
   active
– "switch_profile_on_pos" - bool, should the command only become active
   at the position specified in "switch_position"?
– "switch_gear_on_pos" - bool, should the gear function only be switched
   at the position specified in "switch_position"?
– “switch_position_gain_factor” – float, master position at which a
   changed scaling factor becomes active
– “switch_gain_factor_on_pos” – Bool, select if the scaling factor is
   applied immediately when executing the command or is applied
   depending on the position
– "gear_reduction" – int, gear reduction ratio (disabled if 0)
● <dlParameter> - Dict[str, int], Data Layer parameter of the FlexProfile func‐
tionality:
– "soi_master_offset_dl_idx" - int, index of the real-time input for the inter‐
   polated master axis offset
– "soi_master_offset_vel_dl_idx" - int, index of the real-time input for the
   velocity limit of the interpolated master axis offset
– "soi_master_offset_acc_dl_idx" - int, index of the real-time input for the
   acceleration limit of the interpolated master axis offset
– "soi_slave_offset_dl_idx" - int, index of the real-time input for the inter‐
   polated slave axis offset
– "soi_slave_offset_vel_dl_idx" - int, index of the real-time input for the
   velocity limit of the interpolated following axis offset
– "soi_slave_offset_acc_dl_idx" - int, index of the real-time input for the
   acceleration limit of the interpolated slave axis offset
– "fof_master_offset_dl_idx" - int, index of the real-time input for the fil‐
   tered master axis offset

   – "fof_master_offset_time_constant_dl_idx " - int, index of the real-time
      input for the time constant of the filtered master axis offset
   – "fof_slave_offset_dl_idx" - int, index of the real-time input for the filtered
      slave axis offset
   – "fof_slave_offset_time_constant_dl_idx " - int, index of the real-time input
      for the time constant of the filtered slave axis offset
   – "fine_adjust_dl_idx" - int, index of the real-time input for fine adjustment
   – "soi_angle_adjust_dl_idx" - int, index of the real-time input for the angle
      adjust
   – "soi_angle_adjust_vel_dl_idx" - int, index of the real-time input for the
      velocity of the angle adjust
   – "soi_angle_adjust_vel_dl_idx" - int, index of the real-time input for the

      acceleration of the angle adjust
   – fof_angle_adjust_dl_idx" - int, index of the real-time input for the angle
      adjust
   – fof_angle_adjust_time_constant_dl_idx" - int, index of the real-time input
      for the time constant of the angle adjust
The return value is a command ID that can be used to query the command
status.

BundleIF:
//! @brief Create an axis synchronized motion command for
CamInEx function
//!
/// @param[in]   handle             Handle of the interface
(not used)
/// @param[in]   sourceInfo         Command source information
/// @param[in]   slaveName          Name of the slave motion
object
/// @param[in]   masterName         Name of the master motion
object
/// @param[in]   syncSource         Sync source (Setpoint/
Actual/Actual extrapolated)
/// @param[in]   dynSyncDirection Sync direction
/// @param[in]   parameters         CamIn parameters (slave
and master offset, ratio numerator, ratio denominator, fine
adjust, gain factor, angle adjust, profile entry, point table)
/// @param[in]   dlParameters     Structure containing all
real-time data layer indices (for the parameters that are
stored in the real-time data layer only)
/// @param[out] cmdID               The ID of the added command
/// @return                         Status of the function
call: STS_OK or an error code on failure.
::motion::core::MotionResult(*axsCamInCmdEx)(void* handle,
const ::motion::core::dia::CmdSourceInfo& sourceInfo, const
char* slaveName, const char*
masterName, ::motion::sync::cmd::SyncSource
syncSource, ::motion::sync::cmd::DynSyncDirection
dynSyncDirection, const ::motion::sync::cmd::CamInParameters&
parameters, const ::motion::sync::cmd::CamInDlParameters&
dlParameters, uint64_t& cmdId);

Further information
● See chapter 4 "Introduction and overview"
● ⮫ Chapter 7.2.28 AxsFlexprofile, AxsFlexprofile2, AxsFlexprofileEx, AxsFlex‐
  profileEx2 - Commanding an electronic cam (FlexProfile) on page 457
● ⮫ Chapter 8.1.2 Window – “Axes” on page 795
● ⮫ Chapter 8.1.3 Window – “Axis Profiles” on page 803
● ⮫ Chapter 8.1.4 Window – “Coordinated Motion” on page 806

### 7.2.25 AxsCamIn2, AxsCamInEx2 - Commanding a cam with a scaling

factor
Basics
This command uses the "Cam with scaling factor" feature to link a slave axis
to a master axis. The coupling is position-based.
The CamIn command is based on a simplified Flexprofile command with a
point table and an adjustable scaling factor (stroke).
As soon as the command is active, the PLCOpen status of the axis is set to
SYNCHRONIZED_MOTION. The CamIn command does not end automatically,
but has to be aborted by another unbuffered command (such as AxsAbort or
PosAbs).
ML_AxsGetPLCOpenState or ML_GetCmdState can be used to read the status.
In addition, the status of the synchronization can be queried with ML_AxsGet‐
SyncMotionState (see ⮫ Chapter 7.2.18 AxsGetSyncMotionState - Synchroniza‐
tion state on page 385).
If an error occurs before the execution (e.g. violation of the dynamic limit,
invalid command parameters), the command is not added to the axis object.
If an error occurs during execution, the slave axis is set to the ERRORSTOP
state and it brakes to a standstill. The master axis is not affected by an error
in the slave axis. If the master axis goes into the ERROR_STOP state, the slave
axis continues to follow the calculated slave axis target position. Typically, the
master axis stops in the event of an error, which means that the slave axis
also stops. However, the FlexProfile command of the slave axis remains active.
This command requires that the axis is active (STANDSTILL, DIS‐
CRETE_MOTION, SYNCHRONIZED_MOTION or CONTINUOUS_MOTION state).

PLC:

Starting with version 4.6, the CamIn command was expanded to include the
"GearReduction" parameter. For compatibility reasons, the previous command
functions "ML_AxsCamIn" and data types for CamIn from the "CXA_Motion"
PLC library, as well as the new function "ML_AxisCamIn2" with "GearReduc‐
tion," are available. Preferably, the ML_AxisCamIn2 function and the corre‐
sponding data types should be used.
In the PLC library CXA_PLCopen and in the CXA_MotionInterface, the existing
function blocks and structures have been extended to be compatible.

STRUCT ML_AxsCamIn2Data
Name       Data type   Inherited           Address   Initial value   Comment
                       from
  In       ML_iAxs‐                                                  Input: Command data of
           CamIn2                                                    the command
  Out      ML_oCmdRe‐                                                Output: Command parame‐
           sult                                                      ters
STRUCT ML_iAxsCamIn2 EXTENDS ML_iAxsCmdBase
Name        Data type  Inherited   Address           Initial value   Comment
                       from
  AxisName STRING(15) ML_iAxsCmd‐                                    Name of the axis used to

Base                                          execute the command
  Source    STRING(50) ML_iAxsCmd‐                                   Specifies the command
Base                                          source, e.g PlcApplication1
                                              is displayed in the diag‐
                                              nostic messages
  SourceLine ULINT           ML_iAxsCmd‐                             Specifies the source line of
      Base                                    the command; is displayed
                                              in the diagnostic messages
   Master‐    STRING(15)                                             Name of the master axis to
Name                                                                 be added to the axis
   Syn‐       ML_Syn‐                                                Synchronization source
cSource       cSource
   DynSync‐   ML_DynSync‐                                            Synchronization direction
Direction     Direction
   Parame‐    ML_iAxsCa‐                                             Parameters for the CamIn
ters          mInParame‐                                             command
ters2
STRUCT ML_iAxsCamInParameters2
Name        Data type  Inherited           Address   Initial value   Comment
                       from
  Master‐   LREAL                                    0.0             Offset of the master axis
Offset
  Slave‐    LREAL                                    0.0             Offset of the slave axis
Offset
  RatioNum‐ DINT                                     1               Transmission ratio counter
erator                                                               for gearbox output revolu‐
                                                                     tions (limited to a value
                                                                     between 0 and 65535)
  RatioDeno‐ DINT                                    1               Transmission ratio - denom‐
minator                                                              inator master axis gear
                                                                     input revolutions (limited
                                                                     to a value between 0 and
                                                                     65535)
  FineAdjust LREAL                                   0.0             Fine adjustment of the gear
                                                                     ratio in %
  GainFactor LREAL                                   1.0             Scaling factor for cam
                                                                     table
   AngleAd‐   LREAL                                  0.0             Constant angle adjustment
just                                                                 for CamIn

STRUCT ML_iAxsCamInParameters2
  Profi‐    ML_Profi‐                               SLAVE_CUR‐ Describes how the origin
leEntry     leEntry                                 RENT_MASTE of the profile is to be inter‐
R_CURRENT preted at a profile start or
profile change
  ProfileExe‐ ML_ProfileEx‐                         PRO‐       Determines how the Flex‐
cutionMode ecutionMode                              FILE_MODE_ Profile is executed
CYCLIC
   PointTable STRING(50)                                       Specifies which cam table
is to be executed
   SwitchPo‐ LREAL                                  0.0        Master axis used to switch
sition                                                         to the new profile and/or
the new gear
   SwitchPro‐ BOOL                                  FALSE      If FALSE, the system imme‐
fileOnPos                                                      diately switches to the
selected profile. If TRUE,
the system only switches
to the selected profile
when the switch position is
reached
  Switch‐          BOOL                             FALSE      If FALSE, the system imme‐
GearOnPos                                                      diately switches to the
selected gear. If TRUE, the
system only switches to
the selected gear when the
SwitchPosition is reached
   SwitchPo‐ LREAL                                  0.0        Master position at which
sitionGain‐                                                    a changed scaling factor
Factor                                                         takes effect (if "Switch‐
GainFactorOnPos" is set
accordingly)
SwitchGain‐ BOOL                                    FALSE      Select if the scaling
FactorOnPos                                                    factor is applied immedi‐
ately when executing the
command or is applied
depending on the position.
  GearRe‐          DINT                             0          Gear reduction ratio (disa‐
duction                                                        bled if 0; limited to a value
between 0 and 65535)
ENUM ML_SyncSource
Name       Data type          Inherited   Address   Initial value   Comment
                              from
  SYNC_SET‐ INT                                                     Synchronize based on the
POINT                                                               command value of the
                                                                    master axis(es)
                   INT                                              Synchronization based on
SYNC_ACTUA                                                          the actual value of the
L                                                                   master axis(es)
                   INT                                              Synchronization based on
SYNC_ACTUA                                                          the extrapolated actual
L_EXTRAPO‐                                                          value of the master
LATED                                                               axis(es)

ENUM ML_DynSyncDirection
Name       Data type    Inherited       Address   Initial value   Comment
                        from
           INT                                                    Initiating synchronization
SHORTEST_                                                         via the shortest path
WAY
  POSITIVE INT                                                    Synchronization always in
                                                                  positive direction
  NEGATIVE INT                                                    Synchronization always in
                                                                  negative direction
DIRECT        INT                                                 Synchronization takes
                                                                  place immediately without

                                              dynamic synchronization
ENUM ML_ProfileEntry
Name       Data type        Inherited   Address   Initial value   Comment
                            from
              INT                                                 Absolute access to the pro‐
SLAVE_ORIGI                                                       file
N_MASTER_O
RIGIN
              INT                                                 The profile starts at the
SLAVE_CUR‐                                                        current position of the
RENT_MASTE                                                        master axis and the slave
R_CURRENT                                                         axis
              INT                                                 Profile starts at the current
SLAVE_ORIGI                                                       position of the master axis
N_MASTER_C                                                        and the absolute position
URRENT                                                            of the slave axis
              INT                                                 Profile starts at the current
SLAVE_CUR‐                                                        position of the slave axis
RENT_MASTE                                                        and the absolute position
R_ORIGIN                                                          of the master axis
              INT                                                 The profile starts at the
SLAVE_RELA‐                                                       absolute master axis posi‐
TIVE_MASTE                                                        tion. The position of the
R_ORIGIN                                                          slave axis is defined so that
                                                                  the axis is moved relatively
ENUM ML_ProfileExecutionMode
Name       Data type     Inherited      Address   Initial value   Comment
                         from
  PRO‐     INT                                                    The profile is processed
FILE_MODE_                                                        cyclically
CYCLIC
  PRO‐     INT                                                    The profile is processed
FILE_MODE_                                                        once and then continued at
SINGLE                                                            final speed
  PRO‐     INT                                                    Reserved
FILE_MODE_
JUMP

Data Layer:
Method: POST

URL:         https://<ip-addr>/automation/api/v2/nodes/motion/axs/<axs‐
Name>/cmd/cam-in
Payload:

{
"type":"object","value":
{
    "master": "R_Main",
    "syncSource": "SYNC_SETPOINT",
    "dynSyncDirection": "SHORTEST_WAY",
    "parameters": {
        "masterOffset": 0,
        "slaveOffset": 0,
        "ratioNumerator": 1,
        "ratioDenominator": 1,
        "fineAdjust": 0,
        "gainFactor": 1,
        "angleAdjust": 0,
        "profileEntry": "SLAVE_CURRENT_MASTER_CURRENT",
        "profileExecutionMode": "CYCLIC",
        "pointTable": "Cam2",
        "switchPosition": 0,
        "switchProfileOnPos": false,
        "switchGearOnPos": false,
        "switchPositionGainFactor": 0,
        "switchGainFactorOnPos": false,
        "gearReduction": 0
    }
}

Python:
<cmdID> = motion.axs_cmd_cam_in( axs=<axsName>,
master=<masterName> [,sync_source=<syncSource>]
[,dyn_Sync_direction=<dynSyncDirection>]
[,parameters=<parameter>] )

Creates a CamIn command for a single axis (object has to be "attached"), see
documentation Python Runtime App ⮫ Python functions.
● <axsName> - string, name of the axis object (slave axis)
● <masterName> - string, name of the axis object (master axis)
● <syncSource> - int, which value of the master axis is to be used as the
  basis for the electronic cam? Interpolated position of the master axis = 0,
  actual position of the master axis = 1, extrapolated actual position of the
  master axis = 2
● <dynSyncDirection> - int, how should a modulo axis be synchronized?
  Shortest path = 0, positive = 1, negative = 2, direct = 3
● <parameter> - Dict[str, Union[bool, float, int, string]], parameters of the
  CamIn functionality:
  – "master_offset" - float, offset on the side of the master axis
  – "slave_offset" - float, offset on the side of the slave axis
  – "ratio_numerator" - int, counter of the gear function
  – "ratio_denominator" - int, denominator of the gear function
  – "fine_adjust" - float, percentage value of the fine adjustment
  – “gain_factor” – float, scaling factor for cam table
  – "angle_adjust" - float, constant angle adjustment for CamIn

   – "profile_entry" - int, synchronization method,
     SLAVE_ORIGIN_MASTER_ORIGIN = 0, SLAVE_CURRENT_MASTER_CUR‐
     RENT = 1, SLAVE_ORIGIN_MASTER_CURRENT = 2, SLAVE_CUR‐
     RENT_MASTER_ORIGIN = 3, SLAVE_RELATIVE_MASTER_ORIGIN = 4
   – "profile_execution_mode" - int, how should the profile be interpreted?
     CYCLIC = 0, SINGLE = 1
   – “pointTable” – string, cam table name (e. g. "Cam1" or "Cam2")
   – "switch_position" - float, position at which the command should become
     active
   – "switch_profile_on_pos" - bool, should the command only become active
     at the position specified in "switch_position"?
   – "switch_gear_on_pos" - bool, should the gear function only be switched
     at the position specified in "switch_position"?

   – “switch_position_gain_factor” – float, master position at which a
     changed scaling factor becomes active
   – “switch_gain_factor_on_pos” – Bool, select if the scaling factor is
     applied immediately when executing the command or is applied
     depending on the position
   – "gear_reduction" – int, gear reduction ratio (disabled if 0)

BundleIF:

/// @brief Create an axis synchronized motion command for
CamIn function with gear reduction parameter
///
/// @param[in]     handle           Handle of the interface
(not used)
/// @param[in]     sourceInfo       Command source information
/// @param[in]     slaveName        Name of the slave motion
object
/// @param[in]     masterName       Name of the master motion
object
/// @param[in]     syncSource       Sync source
/// @param[in]     dynSyncDirection Dynamic Sync direction
/// @param[in]     parameters       CamIn parameters
/// @param[out]    cmdID            The ID of the added command
/// @return                         Status of the function
call: STS_OK or an error code on failure.
::motion::core::MotionResult(*axsCamInCmd2)(void* handle,
const ::motion::core::dia::CmdSourceInfo& sourceInfo, const
char* slaveName, const char*
masterName, ::motion::sync::cmd::SyncSource syncSource,

   ::motion::sync::cmd::DynSyncDirection dynSyncDirection,
const ::motion::sync::cmd::CamInParameters2& parameters,
std::uint64_t& cmdId);

PLC:

STRUCT ML_AxsCamInEx2Data
Name       Data type   Inherited              Address   Initial value   Comment
                       from
  In       ML_iAxsCa‐                                                   Input: Command data of
           mInEx2                                                       the command
  Out      ML_oCmdRe‐                                                   Output: Command parame‐
           sult                                                         ters
STRUCT ML_iAxsCamInEx2 EXTENDS ML_iAxsCmdBase
Name        Data type   Inherited  Address    Initial value             Comment
                        from
  AxisName STRING(15) ML_iAxsCmd‐                                       Name of the axis used to
                        Base                                            execute the command
  Source    STRING(50) ML_iAxsCmd‐                                      Specifies the command
                        Base                                            source, e.g PlcApplication1
                                                                        is displayed in the diag‐
                                                                        nostic messages
   SourceLine ULINT             ML_iAxsCmd‐                             Specifies the source line of
                                Base                                    the command; is displayed
                                                                        in the diagnostic messages
   Master‐         STRING(15)                                           Name of the master axis to
Name                                                                    be added to the axis
   Syn‐      ML_Syn‐                                                    Synchronization source
cSource      cSource
   DynSync‐  ML_DynSync‐                                                Synchronization direction
Direction    Direction
   Parame‐   ML_iAxsCa‐                                                 Parameters for the CamIn
ters         mInParame‐                                                 command
             ters2
   DlParame‐ ML_iAxsCa‐                                                 Data Layer parameters for
ters         mInDIPara‐                                                 the gear in position com‐
             meters                                                     mand
STRUCT ML_iAxsCamInDlParameters
Name         Data type Inherited              Address   Initial value   Comment
                       from
  SoiMaster‐ DINT                                       -1              The Data Layer index of the
OffsetDlIdx                                                             master axis, which is used
                                                                        for the second-order offset
  SoiMaster‐ DINT                                       -1              The Data Layer index of
OffsetVel‐                                                              the master axis for velocity
DlIdx                                                                   used for the second-order
                                                                        offset
  SoiMaster‐ DINT                                       -1              The Data Layer index of
OffsetAcc‐                                                              the master axis for acceler‐
DlIdx                                                                   ation, which is used for the
                                                                        second-order offset
  SoiSla‐          DINT                                 -1              The data layer index of the
veOffset‐                                                               slave axis for the second-
DlIdx                                                                   order offset
  SoiSla‐          DINT                                 -1              The Data Layer index of
veOffsetVel‐                                                            the slave offset for the
DlIdx                                                                   velocity, which is used for
                                                                        the second-order offset

STRUCT ML_iAxsCamInDlParameters
  SoiSla‐    DINT                                     -1           The Data Layer index of
veOffsetAcc‐                                                       the slave axis for accelera‐
DlIdx                                                              tion, which is used for the
                                             second-order offset
  FofMaster‐ DINT                                     -1           The Data Layer index of the
OffsetDlIdx                                                        master axis for the filtered
                                             first-order offset
  FofMaster‐ DINT                                     -1           The Data Layer index of
OffsetTime‐                                                        the slave axis for the time
Constant‐                                                          constant used for the first-
DlIdx                                                              order filtered offset

  FofSla‐     DINT                                    -1           The Data Layer index of the
veOffset‐                                                          slave axis used for the fil‐
DlIdx                                                              tered first-order offset
  FofSla‐     DINT                                    -1           The Data Layer index of
veOffsetTi‐                                                        the slave axis for the time
meConstant‐                                                        constant used for the first-
DlIdx                                                              order filtered offset
  FineAdjust‐ DINT                                    -1           The Data Layer index for
DlIdx                                                              fine-tuning, which is used
                                             to fine-tune the transmis‐
                                             sion ratio
SoiAngleAd‐    DINT                                   -1           The Data Layer index used
justDlIdx                                                          for angle adjustment
SoiAngleAd‐    DINT                                   -1           The Data Layer index
justVelDlIdx                                                       is used to measure the
                                             velocity of the angle adjust‐
                                             ment
SoiAngleAd‐ DINT                                      -1           The Data Layer index used
justAccDlIdx                                                       for accelerating the angle
                                             adjustment
fofAngleAd‐    DINT                                   -1           The Data Layer index used
justDlIdx                                                          for the first-order filter for
                                             angular adjustment
fofAngleAd‐ DINT                                      -1           The Data Layer index used
justTimeCon‐                                                       for the filter time constant
stantDlIdx                                                         of the angular adjustment
For other parameters, such as ML_iAxsCamInParameters2, see ML_Axs‐
CamIn2.

Data Layer:
Method: POST
URL:         https://<ip-addr>/automation/api/v2/nodes/motion/axs/<axs‐
Name>/cmd/cam-in-ex
Payload:

{
"type":"object","value":
{
    "master": "R_Main",
    "syncSource": "SYNC_SETPOINT",
    "dynSyncDirection": "SHORTEST_WAY",
    "parameters": {

          "masterOffset": 0,
          "slaveOffset": 0,
          "ratioNumerator": 1,
          "ratioDenominator": 1,
          "fineAdjust": 0,
          "gainFactor": 1,
          "angleAdjust": 0,
          "profileEntry": "SLAVE_CURRENT_MASTER_CURRENT",
          "profileExecutionMode": "CYCLIC",
          "pointTable": "Cam2",
          "switchPosition": 0,
          "switchProfileOnPos": false,
          "switchGearOnPos": false,
          "switchPositionGainFactor": 0,
          "switchGainFactorOnPos": false,
          "gearReduction": 0
    },
    "dlParameters": {
        "soiMasterOffsetDlIdx": -1,
        "soiMasterOffsetVelDlIdx": -1,
        "soiMasterOffsetAccDlIdx": -1,
        "soiSlaveOffsetDlIdx": -1,
        "soiSlaveOffsetVelDlIdx": -1,
        "soiSlaveOffsetAccDlIdx": -1,
        "fofMasterOffsetDlIdx": -1,
        "fofMasterOffsetTimeConstantDlIdx": -1,
        "fofSlaveOffsetDlIdx": -1,
        "fofSlaveOffsetTimeConstantDlIdx": -1,
        "fineAdjustDlIdx": -1,
        "soiAngleAdjustDlIdx": -1,
        "soiAngleAdjustVelDlIdx": -1,
        "soiAngleAdjustAccDlIdx": -1,
        "fofAngleAdjustDlIdx": -1,
        "fofAngleAdjustTimeConstantDlIdx": -1
    }
}
}

Python:
<cmdID> = motion.axs_cmd_cam_in_ex( axs=<axsName>,
master=<masterName> [,sync_source=<syncSource>]
[,dynSync_direction=<syncDirection>]
[,parameters=<parameter>] )

Creates a CamIn command for a single axis (object has to be "attached"), see
documentation Python Runtime App ⮫ Python functions.
● <axsName> - string, name of the axis object (slave axis)
● <masterName> - string, name of the axis object (master axis)
● <syncSource> - int, which value of the master axis is to be used as the
  basis for the electronic cam? Interpolated position of the master axis = 0,
  actual position of the master axis = 1, extrapolated actual position of the
  master axis = 2
● <dynSyncDirection> - int, how should a modulo axis be synchronized?
  Shortest path = 0, positive = 1, negative = 2, direct = 3

● <parameter> - Dict[str, Union[bool, float, int, string]], parameter of the
FlexProfile functionality:
– "master_offset" - float, offset on the side of the master axis
– "slave_offset" - float, offset on the side of the slave axis
– "ratio_numerator" - int, counter of the gear function
– "ratio_denominator" - int, denominator of the gear function
– "fine_adjust" - float, percentage value of the fine adjustment
– “gain_factor” – float, scaling factor for cam table
– "angle_adjust" - float, constant angle adjustment for CamIn
– "profile_entry" - int, synchronization method,
   SLAVE_ORIGIN_MASTER_ORIGIN = 0, SLAVE_CURRENT_MASTER_CUR‐
   RENT = 1, SLAVE_ORIGIN_MASTER_CURRENT = 2, SLAVE_CUR‐

   RENT_MASTER_ORIGIN = 3, SLAVE_RELATIVE_MASTER_ORIGIN = 4
– "profile_execution_mode" - int, how should the profile be interpreted?
   CYCLIC = 0, SINGLE = 1
– “pointTable” – string, cam table name (e. g. "Cam1" or "Cam2")
– "switch_position" - float, position at which the command should become
   active
– "switch_profile_on_pos" - bool, should the command only become active
   at the position specified in "switch_position"?
– "switch_gear_on_pos" - bool, should the gear function only be switched
   at the position specified in "switch_position"?
– “switch_position_gain_factor” – float, master position at which a
   changed scaling factor becomes active
– “switch_gain_factor_on_pos” – Bool, select if the scaling factor is
   applied immediately when executing the command or is applied
   depending on the position
– "gear_reduction" – int, gear reduction ratio (disabled if 0)
● <dlParameter> - Dict[str, int], Data Layer parameter of the FlexProfile func‐
tionality:
– "soi_master_offset_dl_idx" - int, index of the real-time input for the inter‐
   polated master axis offset
– "soi_master_offset_vel_dl_idx" - int, index of the real-time input for the
   velocity limit of the interpolated master axis offset
– "soi_master_offset_acc_dl_idx" - int, index of the real-time input for the
   acceleration limit of the interpolated master axis offset
– "soi_slave_offset_dl_idx" - int, index of the real-time input for the inter‐
   polated slave axis offset
– "soi_slave_offset_vel_dl_idx" - int, index of the real-time input for the
   velocity limit of the interpolated following axis offset
– "soi_slave_offset_acc_dl_idx" - int, index of the real-time input for the
   acceleration limit of the interpolated slave axis offset
– "fof_master_offset_dl_idx" - int, index of the real-time input for the fil‐
   tered master axis offset
– "fof_master_offset_time_constant_dl_idx " - int, index of the real-time
   input for the time constant of the filtered master axis offset
– "fof_slave_offset_dl_idx" - int, index of the real-time input for the filtered
   slave axis offset
– "fof_slave_offset_time_constant_dl_idx " - int, index of the real-time input
   for the time constant of the filtered slave axis offset
– "fine_adjust_dl_idx" - int, index of the real-time input for fine adjustment
– "soi_angle_adjust_dl_idx" - int, index of the real-time input for the angle
   adjust

   – "soi_angle_adjust_vel_dl_idx" - int, index of the real-time input for the
      velocity of the angle adjust
   – "soi_angle_adjust_vel_dl_idx" - int, index of the real-time input for the
      acceleration of the angle adjust
   – fof_angle_adjust_dl_idx" - int, index of the real-time input for the angle
      adjust
   – fof_angle_adjust_time_constant_dl_idx" - int, index of the real-time input
      for the time constant of the angle adjust
The return value is a command ID that can be used to query the command
status.

BundleIF:

/// @brief Create an extended axis synchronized motion command
for CamIn function with gear reduction parameter
///
/// Using this extended CamIn command, the locations (indices)
of the CamIn parameters that are stored in the real-time data
layer can be specified explicitly.
/// Specifying -1 for a given index will use its default index
value.
///
/// @param[in]     handle           Handle of the interface
(not used)
/// @param[in]     sourceInfo       Command source information
/// @param[in]     slaveName        Name of the slave motion
object
/// @param[in]     masterName       Name of the master motion
object
/// @param[in]     syncSource       Sync source
/// @param[in]     dynSyncDirection Dynamic Sync direction
/// @param[in]     parameters       CamIn parameters
/// @param[in]     dlParameters     Structure containing all
real-time data layer indices (for the parameters that are
stored in the real-time data layer only)
/// @param[out]    cmdID            The ID of the added command
/// @return                         Status of the function
call: STS_OK or an error code on failure.
::motion::core::MotionResult(*axsCamInCmdEx2)(void* handle,
const ::motion::core::dia::CmdSourceInfo& sourceInfo, const
char* slaveName, const char*
masterName, ::motion::sync::cmd::SyncSource syncSource,
                                              ::motion::sync::c
md::DynSyncDirection dynSyncDirection,
const ::motion::sync::cmd::CamInParameters2& parameters,
const ::motion::sync::cmd::CamInDlParameters& dlParameters,
std::uint64_t& cmdId);

Further information
● See chapter 4 "Introduction and overview"
● ⮫ Chapter 7.2.28 AxsFlexprofile, AxsFlexprofile2, AxsFlexprofileEx, AxsFlex‐
  profileEx2 - Commanding an electronic cam (FlexProfile) on page 457
● ⮫ Chapter 8.1.2 Window – “Axes” on page 795
● ⮫ Chapter 8.1.3 Window – “Axis Profiles” on page 803
● ⮫ Chapter 8.1.4 Window – “Coordinated Motion” on page 806

### 7.2.26 AxsGetCamInState - Reading the points table status

Basics
This function makes it possible to read out various states of a points table.
The following statuses can be queried:
● SINGLE_EXECUTION_DONE
● WAIT_FOR_SWITCH_GAIN
● WAIT_FOR_SWITCH_POS

PLC:

STRUCT ML_AxsGetCamInStateData
Name       Data type   Inherited           Address        Initial value   Comment
                       from
  In       ML_iAxsGet‐                                                    Input: Command data of
           CamInState                                                     the command
  Out      ML_oAxsGet‐                                                    Output: Command parame‐
           CamInState                                                     ters
STRUCT ML_iAxsGetCamInState
Name        Data type  Inherited           Address        Initial value   Comment
                       from
  AxisName STRING(15)                                                     Name of the axis used to
                                                                          execute the command
  StateSe‐    ML_CamIn‐                                                   Name of the status to be
lector        StateSelector                                               read
ENUM ML_CamInStateSelector
Name        Data type   Inherited          Address        Initial value   Comment
                        from
            BOOL                                                          The points table was
SINGLE_EXE‐                                                               executed once (only
CUTION_DON                                                                for the "profileExecution‐
E                                                                         Mode": "SINGLE" (CamIn or
                                                                          CamInEx)
               BOOL                                                       The system waits for the
WAIT_FOR_S                                                                specified switching position
WITCH_POS                                                                 to switch the table
               BOOL                                                       The system waits for the
WAIT_FOR_W                                                                specified switching position
AIT_FOR_SWI                                                               to switch the gain factor
TCH_GAIN_P
OS
STRUCT ML_oAxsGetCamInState
Name       Data type   Inherited           Address        Initial value   Comment
                       from

STRUCT ML_oAxsGetCamInState
  Error    BOOL        ML_oState‐                                       Error ID TRUE indicates
Base                                             that an error occurred
  ErrorID  ULINT       ML_oState‐                                       Specifies the type of
Base                                             occurred error: The upper
                                                 4 bytes reflect the main
                                                 diagnostics, the lower 4
                                                 bytes reflect the detailed
                                                 diagnostics, 0 means no
                                                 error
   State           UDINT                                                Status of the status to be
                                                 displayed

Data Layer:
Method: GET
URL:           https://<ip-addr>/automation/api/v2/nodes/motion/axs/<axs‐
Name>/state/functions/coupling/sync-motion/cam-in/execution-info
Payload:

{
    "master": "Axis_1",
    "syncSource": "SYNC_SETPOINT",
    "dynSyncDirection": "SHORTEST_WAY",
    "parameters": {
        "masterOffset": 0,
        "slaveOffset": 0,
        "ratioNumerator": 1,
        "ratioDenominator": 1,
        "fineAdjust": 0,
        "gainFactor": 1,
        "angleAdjust": 0,
        "profileEntry": "SLAVE_CURRENT_MASTER_CURRENT",
        "profileExecutionMode": "CYCLIC",
        "pointTable": "Table1",
        "switchPosition": 10,
        "switchProfileOnPos": true,
        "switchGearOnPos": true,
        "switchPositionGainFactor": 20,
        "switchGainFactorOnPos": true
    }
}
If the command shown above is used with "switchProfileOnPos": TRUE and/or
"switchGearOnPos": TRUE, the status for WAIT_FOR_SWITCH_POS is set to
TRUE. If the switching position "switchPosition": 10 has been reached, the
status is set to 0.
If the command shown above is used with "switchGainFactorOnPos": TRUE,
the status for WAIT_FOR_SWITCH_GAIN is set to TRUE. If the switching posi‐
tion "switchPositionGainFactor": 20 has been reached, the status is set to 0.
If the command shown above is used with "profileExecutionMode": "SINGLE"
is executed, the status SINGLE_EXECUTION_DONE changes to FALSE when
the command is sent and becomes TRUE once the profile has been com‐
pletely executed. Used in connection with "profileExecutionMode": "SINGLE"
also "switchProfileOnPos": TRUE is used, the profile is first switched when
the switching position is reached and then checked for one-time processing

of the points table. This means that in this case the status SINGLE_EXECU‐
TION_DONE is set to FALSE when the switching position is passed, the table
is switched and set to TRUE after the table has been completely processed.

BundleIF:
/// @brief Get a state information (defined by the state
/// selector) of the active CamIn.
///
/// Get the state information for several functionalities of
/// an active CamIn with this function. This
/// information is only updated, when there is a axsCamInCmd
/// active.
///

/// The function is optimized for speed and can be used in a
/// real-time context (lock- and wait-free), when the motion
/// kernel is in state RUNNING.
/// If the motion kernel is not in state RUNNING, the function
/// call is not real-time capable.
///
/// @param[in]    handle           Handle of the interface.
/// @param[in]    axsName          Name of CamIn axis
/// @param[in]    stateSelector    Selector for different state
                                   information
/// @param[out]   state            Selected state of the active
                                   CamIn
/// @return                        Status of the function call:
                                   STS_OK or an error code on
                                   failure.
::motion::core::MotionResult(*getCamInState)(void* handle,
const char* axsName, ::motion::sync::data::CamInStateSelector
stateSelector, uint32_t& state);

Further information
● See chapter 4 "Introduction and overview"
● ⮫ Chapter 7.2.28 AxsFlexprofile, AxsFlexprofile2, AxsFlexprofileEx, AxsFlex‐
  profileEx2 - Commanding an electronic cam (FlexProfile) on page 457
● ⮫ Chapter 8.1.2 Window – “Axes” on page 795
● ⮫ Chapter 8.1.3 Window – “Axis Profiles” on page 803
● ⮫ Chapter 8.1.4 Window – “Coordinated Motion” on page 806

### 7.2.27 AxsGetCamInActivePointTable - Points table

Basics
This function is used to read out the active points table.

PLC:

ML_AxsGetCamInActivePointTable
Name        Data type    Inherited       Address    Initial value   Comment
                         from
   Data     ML_AxsGet‐                                              Input: Command data of
            CamInActive‐                                            the command
            PointTable‐
            Data
   ML_Axs‐  BOOL                                                    Output: Command parame‐
GetCamInAc‐                                                         ters
tivePoint‐
Table
STRUCT ML_AxsGetCamInActivePointTableData
Name       Data type    Inherited    Address        Initial value   Comment
                        from
  In       ML_iAxsSta‐                                              Input data
           teBase
  Out      ML_oAxsGet‐                                              Return values
           CamInActive‐
           PointTable
STRUCT ML_iAxsStateBase
Name        Data type   Inherited        Address    Initial value   Comment
                        from
  AxisName STRING(15)                                               Name of the axis used to
                                                                    execute the command
ENUM ML_oAxsGetCamInActivePointTable
Name       Data type   Inherited     Address        Initial value   Comment
                       from
  Error    BOOL        ML_oState‐                                   Errors
                       Base
  ErrorID  ULINT       ML_oState‐                                   Error number
                       Base
  PointTa‐ STRING(31)                                               Name of the active points
bleName                                                             table

BundleIF:
/// @brief Get the name of the currently active pointtable.
///
/// Read, which pointtable is currently active. This
/// information is only updated, when there is an axsCamInCmd
/// is active.
///
/// The function is optimized for speed and can be used in a
/// real-time context (lock- and wait-free), when the motion
/// kernel is in state RUNNING.
/// If the motion kernel is not in state RUNNING, the function
/// call is not real-time capable.
///
/// @param[in]    handle       Handle of the interface.
/// @param[in]    axsName      Name of CamIn axis
/// @param[out]   pointTable   Name of the active point table
/// @return                    Status of the function call:
///                            STS_OK

///                            or an error code on failure.
::motion::core::MotionResult(*getCamInActivePointTable)(void*
handle, const char* axsName, const char*& pointTable);

Further information
● See chapter 4 "Introduction and overview"
● ⮫ Chapter 7.2.28 AxsFlexprofile, AxsFlexprofile2, AxsFlexprofileEx, AxsFlex‐
  profileEx2 - Commanding an electronic cam (FlexProfile) on page 457
● ⮫ Chapter 8.1.2 Window – “Axes” on page 795
● ⮫ Chapter 8.1.3 Window – “Axis Profiles” on page 803
● ⮫ Chapter 8.1.4 Window – “Coordinated Motion” on page 806

### 7.2.28 AxsFlexprofile, AxsFlexprofile2, AxsFlexprofileEx, AxsFlexprofi‐

leEx2 - Commanding an electronic cam (FlexProfile)
Basics
This command uses the electronic cam (FlexProfile) functionality to couple a
slave axis to a master axis. The coupling is position-based and implements an
electronic cam plate.
As soon as the command is active, the PLCOpen status of the axis is set
to SYNCHRONIZED_MOTION. The FlexProfile command does not end automat‐
ically, but has to be aborted by another unbuffered command (such as AxsA‐
bort or PosAbs).
ML_AxsGetPLCOpenState or ML_GetCmdState can be used to read the status.
In addition, the status of the synchronization can be queried with ML_AxsGet‐
SyncMotionState (see ⮫ Chapter 7.2.18 AxsGetSyncMotionState - Synchroniza‐
tion state on page 385) .
If an error occurs before the execution (e.g. violation of the dynamic limit,
invalid command parameters), the command is not added to the axis object.
If an error occurs during execution, the slave axis is set to the ERRORSTOP
state and it brakes to a standstill. The master axis is not affected by an error
in the slave axis. If the master axis goes into the ERROR_STOP state, the slave
axis continues to follow the calculated slave axis target position. Typically, the
master axis stops in the event of an error, which means that the slave axis
also stops. However, the FlexProfile command of the slave axis remains active.
If the command is sent as a non-buffered command, the previously active
command is canceled, the commands from the preparation buffer are dis‐
carded and the command is executed immediately (with the new commanded
parameters).
This command requires that the axis is active (STANDSTILL, DIS‐
CRETE_MOTION, SYNCHRONIZED_MOTION or CONTINUOUS_MOTION state).

PLC:

From version 3.6, the "SlaveAdjust" parameter has been added to the FlexPro‐
file command. For compatibility reasons, the previous command functions
"ML_AxsFlexprofile" and data types for the FlexProfile of the PLC library
"CXA_Motion" and the new function "ML_AxisFlexProfile2" with the "SlaveAd‐
just" are available. The ML_AxsFlexprofile2 function and the corresponding
data types should preferably be used.
In the PLC library CXA_PLCopen and in the CXA_MotionInterface, the existing
function blocks and structures have been extended to be compatible.
STRUCT ML_AxsFlexprofile2Data
Name       Data type     Inherited              Address     Initial value   Comment
                         from
  In       ML_iAxsFlex‐                                                     Input: Command data of
           profile2                                                         the command
  Out      ML_oCmdRe‐                                                       Output: Command parame‐
           sult                                                             ters
STRUCT ML_iAxsFlexprofile2 EXTENDS ML_iAxsCmdBase
Name        Data type     Inherited  Address     Initial value              Comment
                          from
  AxisName STRING(15) ML_iAxsCmd‐                                           Name of the axis used to
                          Base                                              execute the command
  Source    STRING(50) ML_iAxsCmd‐                                          Specifies the command
                          Base                                              source, e.g PlcApplication1
                                                                            is displayed in the diag‐
                                                                            nostic messages
   SourceLine ULINT               ML_iAxsCmd‐                               Specifies the source line of
                                  Base                                      the command; is displayed
                                                                            in the diagnostic messages
   Master‐         STRING(15)                                               Name of the master axis to
Name                                                                        be added to the axis
   Syn‐            ML_Syn‐                                                  Synchronization source
cSource            cSource
   DynSync‐        ML_DynSync‐                                              Synchronization direction
Direction          Direction
   Parame‐         ML_iAxsFlex‐                                             Parameters for the FlexPro‐
ters               profilePara‐                                             file command
                   meters2
   Buffered        BOOL                                                     TRUE, if the command is
                                                                            to be executed as a buf‐
                                                                            fered command, otherwise
                                                                            FALSE
STRUCT ML_iAxsFlexprofileParameters2
Name        Data type     Inherited             Address     Initial value   Comment
                          from
  Master‐   LREAL                                           0.0             Offset of the master axis
Offset

STRUCT ML_iAxsFlexprofileParameters2
  Slave‐    LREAL                                   0.0             Offset of the slave axis
Offset
  RatioNu‐  DINT                                    1          Transmission ratio - Master
merataor                                                       axis counter gear output
revolutions
  RatioDeno‐ DINT                                   1          Transmission ratio - denom‐
minator                                                        inator master axis gear
input revolutions
  FineAdjust LREAL                                  0.0        Fine adjustment of the gear
ratio in %
  Profi‐      ML_Profi‐                             SLAVE_CUR‐ Describes how the origin

leEntry       leEntry                               RENT_MASTE of the profile is to be inter‐
R_CURRENT preted at a profile start or
profile change
  Profile     STRING(50)                                       Specifies which profile is
to be executed
  ProfileExe‐ ML_ProfileEx‐                         PRO‐       Determines how the Flex‐
cutionMode ecutionMode                              FILE_MODE_ Profile is executed
CYCLIC
   SwitchPo‐ LREAL                                  0.0        Master axis used to switch
sition                                                         to the new profile and/or
the new gear
   SwitchPro‐ BOOL                                  FALSE      If FALSE, the system imme‐
fileOnPos                                                      diately switches to the
selected profile. If TRUE,
the system only switches
to the selected profile
when the switch position is
reached
  Switch‐     BOOL                                  FALSE      If FALSE, the system
GearOnPos                                                      immediately shifts to the
selected gear. If TRUE, the
system only shifts to the
selected gear when the
switch position is reached
AngleAdjust   LREAL                                 0.0        Angle offset after gearbox
before FlexProfile access
SlaveAdjust   LREAL                                 0.0        Slave-side angle offset
(if "SwitchProfileOnPos" =
TRUE is used, the offset
is active when the "Switch‐
Position" is reached, other‐
wise when the command is
started)
ENUM ML_SyncSource
Name       Data type          Inherited   Address   Initial value   Comment
                              from
  SYNC_SET‐ INT                                                     Synchronize based on the
POINT                                                               command value of the
                                                                    master axis(es)

ENUM ML_SyncSource
INT                                                  Synchronization based on
SYNC_ACTUA                                                      the actual value of the
L                                                               master axis(es)
INT                                                  Synchronization based on
SYNC_ACTUA                                                      the extrapolated actual
L_EXTRAPO‐                                                      value of the master
LATED                                                           axis(es)
ENUM ML_DynSyncDirection
Name       Data type    Inherited     Address   Initial value   Comment
                        from
           INT                                                  Initiating synchronization
SHORTEST_                                                       via the shortest path
WAY
  POSITIVE INT                                                  Synchronization always in
                                                                positive direction
   NEGATIVE INT                                                 Synchronization always in
                                                                negative direction
DIRECT             INT                                          Synchronization takes
                                                                place immediately without
                                                                dynamic synchronization
ENUM ML_ProfileEntry
Name       Data type      Inherited   Address   Initial value   Comment
                          from
                   INT                                          Absolute access to the pro‐
SLAVE_ORIGI                                                     file
N_MASTER_O
RIGIN
                   INT                                          The profile starts at the
SLAVE_CUR‐                                                      current position of the
RENT_MASTE                                                      master axis and the slave
R_CURRENT                                                       axis
                   INT                                          Profile starts at the current
SLAVE_ORIGI                                                     position of the master axis
N_MASTER_C                                                      and the absolute position
URRENT                                                          of the slave axis
                   INT                                          Profile starts at the current
SLAVE_CUR‐                                                      position of the slave axis
RENT_MASTE                                                      and the absolute position
R_ORIGIN                                                        of the master axis
                   INT                                          The profile starts at the
SLAVE_RELA‐                                                     absolute master axis posi‐
TIVE_MASTE                                                      tion. The position of the
R_ORIGIN                                                        slave axis is defined so that
                                                                the axis is moved relatively
ENUM ML_ProfileExecutionMode
Name       Data type     Inherited    Address   Initial value   Comment
                         from
  PRO‐     INT                                                  The profile is processed
FILE_MODE_                                                      cyclically
CYCLIC

ENUM ML_ProfileExecutionMode
  PRO‐     INT                                                        The profile is processed
FILE_MODE_                                                            once and then continued at
SINGLE                                                                final speed
  PRO‐     INT                                                        Reserved
FILE_MODE_
JUMP

Data Layer:
Method: POST
URL:          https://<ip-addr>/automation/api/v2/nodes/motion/axs/<axs‐
Name>/cmd/flexprofile

Payload:

{
"type":"object","value":
{
    "master": "R_Main",
    "syncSource": "SYNC_SETPOINT",
    "dynSyncDirection": "SHORTEST_WAY",
    "parameters": {
        "masterOffset": 0,
        "slaveOffset": 17.5,
        "ratioNumerator": 1,
        "ratioDenominator": 1,
        "fineAdjust": 0,
        "profileEntry": "SLAVE_ORIGIN_MASTER_ORIGIN",
        "profile": "FlyingSawProfile",
        "profileExecutionMode": "CYCLIC",
        "switchPosition": 0,
        "switchProfileOnPos": false,
        "switchGearOnPos": false,
        "angleAdjust" : 0,
        "slaveAdjust" : 0
    },
    "buffered": false
}
}

Python:
<cmdID> = motion.axs_cmd_flexprofile( axs=<axsName>,
master=<masterName> [,sync_source=<syncSource>]
[,dyn_sync_direction=<dynSyncDirection>]
[,parameters=<parameter>] [,buffered=<buffered>] )

Creates a FlexProfile command for a single axis (object has to be "attached"),
see documentation Python Runtime App ⮫ Python functions.
● <axsName> - string, name of the axis object (slave axis)
● <masterName> - string, name of the axis object (master axis)
● <syncSource> - int, which value of the master axis is to be used as the
  basis for the electronic cam? Interpolated position of the master axis = 0,
  actual position of the master axis = 1, extrapolated actual position of the
  master axis = 2
● <syncDirection> - int, how should a modulo axis be synchronized? Shortest
  path = 0, positive = 1, negative = 2, direct = 3

● <parameter> - Dict[str, Union[bool, float, int, string]], parameter of the
   FlexProfile functionality:
   – "master_offset" - float, offset on the side of the master axis
   – "slave_offset" - float, offset on the side of the slave axis
   – "ratio_numerator" - int, counter of the gear function
   – "ratio_denominator" - int, denominator of the gear function
   – "fine_adjust" - float, percentage value of the fine adjustment
   – "profile_entry" - int, synchronization method,
      SLAVE_ORIGIN_MASTER_ORIGIN = 0, SLAVE_CURRENT_MASTER_CUR‐
      RENT = 1, SLAVE_ORIGIN_MASTER_CURRENT = 2, SLAVE_CUR‐
      RENT_MASTER_ORIGIN = 3, SLAVE_RELATIVE_MASTER_ORIGIN = 4
   – "profile" - string, name of the profile (e.g. “0” or “2”)
   – "profile_execution_mode" - int, how should the profile be interpreted?
      CYCLIC = 0, SINGLE = 1
   – "switch_position" - float, position at which the command should become
      active
   – "switch_profile_on_pos" - bool, should the command only become active
      at the position specified in "switch_position"?
   – "switch_gear_on_pos" - bool, should the gear function only be switched
      at the position specified in "switch_position"?
   – "angle_adjust" - float, constant angle adjustment for flex profiles
   – "slave_adjust" - float, slave-side angle offset (if "SwitchProfileOnPos" =
      TRUE is used, the offset is active when the "SwitchPosition" is reached,
      otherwise when the command is started)
● <buffered> - bool, use TRUE if the command is to be buffered (TRUE by
   default)
The return value is a command ID that can be used to query the command
status.

BundleIF:
//! @brief Create an axis synchronized motion command for
Flexprofile function
//!
/// @param[in]   handle             Handle of the interface
                                  (not used)
/// @param[in]   sourceInfo         Command source information
/// @param[in]   slaveName          Name of the slave motion
                                  object
/// @param[in]   masterName         Name of the master motion
                                  object
/// @param[in]   syncSource         Sync source (Setpoint/
Actual)
/// @param[in]   dynSyncDirection Sync direction
/// @param[in]   parameters         Flexprofile parameters
(slave
                                  and master offset, ratio
                                  numerator, ratio
denominator,
                                  fine adjust, profile entry,
                                  set selection)
/// @param[in]   buffered           Buffered command?
/// @param[out] cmdID               The ID of the added command
/// @return                         Status of the function
call:
                                  STS_OK or an error code on

failure.
::motion::core::MotionResult(*axsFlexprofileCmd)(void* handle,
const ::motion::core::dia::CmdSourceInfo& sourceInfo, const
char* slaveName, const char*
masterName, ::motion::sync::cmd::SyncSource
syncSource, ::motion::sync::cmd::DynSyncDirection
dynSyncDirection,
const ::motion::sync::cmd::FlexprofileParameters& parameters,
bool buffered, uint64_t& cmdID);

PLC:

From version 3.6, the "SlaveAdjust" parameter has been added to the FlexPro‐
file command. For compatibility reasons, the previous command functions
"ML_AxisFlexProfileEx" and data types for the FlexProfile of the PLC library
"CXA_Motion" and the new function "ML_AxisFlexProfileEx2" are available with
SlaveAdjust. The ML_AxisFlexprofileEx2 function and the corresponding data
types should preferably be used.
In the PLC library CXA_PLCopen and in the CXA_MotionInterface, the existing
function blocks and structures have been extended to be compatible.
STRUCT ML_AxsFlexprofileEx2Data
Name       Data type     Inherited        Address      Initial value   Comment
                         from
  In       ML_iAxsFlex‐                                                Input: Command data of
           profileEx                                                   the command
  Out      ML_oCmdRe‐                                                  Output: Command parame‐
           sult                                                        ters
STRUCT ML_iAxsFlexprofileEx2 EXTENDS ML_iAxsCmdBase
Name        Data type     Inherited  Address     Initial value         Comment
                          from
  AxisName STRING(15) ML_iAxsCmd‐                                      Name of the axis used to
                          Base                                         execute the command
  Source    STRING(50) ML_iAxsCmd‐                                     Specifies the command
                          Base                                         source, e.g PlcApplication1
                                                                       is displayed in the diag‐
                                                                       nostic messages
  SourceLine ULINT          ML_iAxsCmd‐                                Specifies the source line of
                            Base                                       the command; is displayed
                                                                       in the diagnostic messages

STRUCT ML_iAxsFlexprofileEx2 EXTENDS ML_iAxsCmdBase
  Master‐   STRING(15)                                          Name of the gantry master
Name                                                            axis to be added to the
axis
   Syn‐      ML_Syn‐                                            Synchronization source
cSource      cSource
   DynSync‐  ML_DynSync‐                                        Synchronization direction
Direction    Direction
   Parame‐   ML_iAxsFlex‐                                       Parameters for the FlexPro‐
ters         profilePara‐                                       file command
meters2
   DlParame‐ ML_iAxsFlex‐                                       Data Layer parameters for
ters         profileDI‐                                         the gear in position com‐
Parameters                                         mand
   Buffered  BOOL                                               TRUE, if the command is
to be executed as a buf‐
fered command, otherwise
FALSE
STRUCT ML_iAxsFlexprofileDlParameters
Name         Data type    Inherited   Address   Initial value   Comment
                          from
  SoiMaster‐ DINT                               -1              The Data Layer index of the
OffsetDlIdx                                                     master axis used for the
                                                                second-order offset
  SoiMaster‐ DINT                               -1              The Data Layer index of the
OffsetVel‐                                                      master axis for the velocity
DlIdx                                                           used for the second-order
                                                                offset
  SoiMaster‐ DINT                               -1              The Data Layer index of the
OffsetAcc‐                                                      master axis for the acceler‐
DlIdx                                                           ation used for the second-
                                                                order offset
  SoiSla‐          DINT                         -1              The Data Layer index of the
veOffset‐                                                       slave axis for the second
DlIdx                                                           order offset
  SoiSla‐          DINT                         -1              The Data Layer index of the
veOffsetVel‐                                                    slave offset for the velocity
DlIdx                                                           used for the second-order
                                                                offset
  SoiSla‐    DINT                               -1              The Data Layer index of the
veOffsetAcc‐                                                    slave axis for the acceler‐
DlIdx                                                           ation used for the second-
                                                                order offset
  FofMaster‐ DINT                               -1              The Data Layer index of the
OffsetDlIdx                                                     master axis for the filtered
                                                                first-order offset
  FofMaster‐ DINT                               -1              The Data Layer index of the
OffsetTime‐                                                     master axis for the time
Constant‐                                                       constant used for the fil‐
DlIdx                                                           tered first-order offset
  FofSla‐    DINT                               -1              The Data Layer index of the
veOffset‐                                                       slave axis used for the fil‐
DlIdx                                                           tered first-order offset

STRUCT ML_iAxsFlexprofileDlParameters
  FofSla‐     DINT                                     -1            The Data Layer index of the
veOffsetTi‐                                                          slave axis for the time con‐
meConstant‐                                                          stant used for the filtered
DlIdx                                                                first-order offset
  FineAdjust‐ DINT                                     -1            The Data Layer index for
DlIdx                                                                fine adjustment, which is
                                               used to fine-tune the trans‐
                                               mission ratio
SoiAngleAd‐    DINT                                    -1            The Data Layer index used
justDlIdx                                                            for the angle adjustment
SoiAngleAd‐    DINT                                    -1            The Data Layer index used

justVelDlIdx                                                         for the velocity of the angle
                                               adjustment
SoiAngleAd‐ DINT                                       -1            The Data Layer index used
justAccDlIdx                                                         for the acceleration of the
                                               angle adjustment
fofAngleAd‐    DINT                                    -1            The Data Layer index used
justDlIdx                                                            for first-order filtering of
                                               the angle adjustment
fofAngleAd‐ DINT                                       -1            The Data Layer index used
justTimeCon‐                                                         for the filter time constant
stantDlIdx                                                           of the angle adjustment
For other parameters such as ML_iAxsFlexprofileParameter, see ML_AxsFlex‐
profile.

Data Layer:
Method: POST
URL:          https://<ip-addr>/automation/api/v2/nodes/motion/axs/<axs‐
Name>/cmd/flexprofile-ex
Payload:

{
       "master": "",
       "syncSource": "SYNC_SETPOINT",
       "dynSyncDirection": "SHORTEST_WAY",
       "parameters": {
           "masterOffset": 0,
           "slaveOffset": 0,
           "ratioNumerator": 1,
           "ratioDenominator": 1,
           "fineAdjust": 0,
           "profileEntry": "SLAVE_CURRENT_MASTER_CURRENT",
           "profile": "",
           "profileExecutionMode": "CYCLIC",
           "switchPosition": 0,
           "switchProfileOnPos": false,
           "switchGearOnPos": false,
           "angleAdjust": 0,
           "slaveAdjust": 0
       },
       "dlParameters": {
           "soiMasterOffsetDlIdx": -1,
           "soiMasterOffsetVelDlIdx": -1,
           "soiMasterOffsetAccDlIdx": -1,

          "soiSlaveOffsetDlIdx": -1,
          "soiSlaveOffsetVelDlIdx": -1,
          "soiSlaveOffsetAccDlIdx": -1,
          "fofMasterOffsetDlIdx": -1,
          "fofMasterOffsetTimeConstantDlIdx": -1,
          "fofSlaveOffsetDlIdx": -1,
          "fofSlaveOffsetTimeConstantDlIdx": -1,
          "fineAdjustDlIdx": -1,
          "soiAngleAdjustDlIdx": -1,
          "soiAngleAdjustVelDlIdx": -1,
          "soiAngleAdjustAccDlIdx": -1,
          "fofAngleAdjustDlIdx": -1,
          "fofAngleAdjustTimeConstantDlIdx": -1
    },
    "buffered": false
}

Python:
<cmdID> = motion.axs_cmd_flexprofile_ex( axs=<axsName>,
master=<masterName> [,sync_source=<syncSource>]
[,dyn_sync_direction=<dynSyncDirection>]
[,parameters=<parameter>] [,dl_parameters=<dlParameter>]
[,buffered=<buffered>] )

Creates a FlexProfile command for a single axis (object has to be "attached"),
see documentation Python Runtime App ⮫ Python functions.
● <axsName> - string, name of the axis object (slave axis)
● <masterName> - string, name of the axis object (master axis)
● <syncSource> - int, which value of the master axis is to be used as the
  basis for the electronic cam? Interpolated position of the master axis = 0,
  actual position of the master axis = 1
● <syncDirection> - int, how should a modulo axis be synchronized? Shortest
  distance = 0, delay = 1, catch up = 2
● <parameter> - Dict[str, Union[bool, float, int, string]], parameter of the
  FlexProfile functionality:
  – "master_offset" - float, offset on the side of the master axis
  – "slave_offset" - float, offset on the side of the slave axis
  – "ratio_numerator" - int, counter of the gear function
  – "ratio_denominator" - int, denominator of the gear function
  – "fine_adjust" - float, percentage value of the fine adjustment
  – "profile_entry" - int, synchronization method,
     SLAVE_ORIGIN_MASTER_ORIGIN = 0, SLAVE_CURRENT_MASTER_CUR‐
     RENT = 1, SLAVE_ORIGIN_MASTER_CURRENT = 2, SLAVE_CUR‐
     RENT_MASTER_ORIGIN = 3, SLAVE_RELATIVE_MASTER_ORIGIN = 4
  – "profile" - string, name of the profile (e.g. “0” or “2”)
  – "profile_execution_mode" - int, how should the profile be interpreted?
     CYCLIC = 0, SINGLE = 1
  – "switch_position" - float, position at which the command should become
     active
  – "switch_profile_on_pos" - bool, should the command only become active
     at the position specified in "switch_position"?
  – "switch_gear_on_pos" - bool, should the gear function only be switched
     at the position specified in "switch_position"?

   – "angle_adjust" - float, constant angle adjustment for flex profiles
   – "slave_adjust" - float, slave-side angle offset (if "SwitchProfileOnPos" =
      TRUE is used, the offset is active when the "SwitchPosition" is reached,
      otherwise when the command is started)
● <dlParameter> - Dict[str, int], Data Layer parameter of the FlexProfile func‐
   tionality:
   – "soi_master_offset_dl_idx" - int, index of the real-time input for the inter‐
      polated master axis offset
   – "soi_master_offset_vel_dl_idx" - int, index of the real-time input for the
      velocity limit of the interpolated master axis offset
   – "soi_master_offset_acc_dl_idx" - int, index of the real-time input for the
      acceleration limit of the interpolated master axis offset

   – "soi_slave_offset_dl_idx" - int, index of the real-time input for the inter‐
      polated slave axis offset
   – "soi_slave_offset_vel_dl_idx" - int, index of the real-time input for the
      velocity limit of the interpolated following axis offset
   – "soi_slave_offset_acc_dl_idx" - int, index of the real-time input for the
      acceleration limit of the interpolated slave axis offset
   – "fof_master_offset_dl_idx" - int, index of the real-time input for the fil‐
      tered master axis offset
   – "fof_master_offset_time_constant_dl_idx " - int, index of the real-time
      input for the time constant of the filtered master axis offset
   – "fof_slave_offset_dl_idx" - int, index of the real-time input for the filtered
      slave axis offset
   – "fof_slave_offset_time_constant_dl_idx " - int, index of the real-time input
      for the time constant of the filtered slave axis offset
   – "fine_adjust_dl_idx" - int, index of the real-time input for fine adjustment
   – "soi_angle_adjust_dl_idx" - int, index of the real-time input for the angle
      adjust
   – "soi_angle_adjust_vel_dl_idx" - int, index of the real-time input for the
      velocity of the angle adjust
   – "soi_angle_adjust_vel_dl_idx" - int, index of the real-time input for the
      acceleration of the angle adjust
   – fof_angle_adjust_dl_idx" - int, index of the real-time input for the angle
      adjust
   – fof_angle_adjust_time_constant_dl_idx" - int, index of the real-time input
      for the time constant of the angle adjust
● <buffered> - bool, use TRUE if the command is to be buffered (TRUE by
   default)
The return value is a command ID that can be used to query the command
status.

BundleIF:
//! @brief Create an axis synchronized motion command for
    Flexprofile function
//!
/// Using this extended Flexprofile command, the locations
    (indices) of the Flexprofile parameters that are stored
    in the real-time data layer can be specified explicitly.
/// Specifying -1 for a given index will use its default
    index value.
///
/// @param[in]   handle             Handle of the interface
                                  (not used)

/// @param[in]        sourceInfo         Command source information
/// @param[in]        slaveName          Name of the slave motion
                                       object
/// @param[in]        masterName         Name of the master motion
                                       object
/// @param[in]        syncSource         Sync source (Setpoint/
                                       Actual)
/// @param[in]        dynSyncDirection Sync direction
/// @param[in]        parameters         Flexprofile parameters
                                       (slave and master offset,
                                       ratio numerator, ratio
                                       denominator, fine adjust,
                                       profile entry, set selection)
/// @param[in]        buffered           Buffered command?
/// @param[out]       cmdID              The ID of the added command
/// @return                              Status of the function
call:
                                  STS_OK or an error code on
                                  failure.
::motion::core::MotionResult(*axsFlexprofileCmd)(void* handle,
const ::motion::core::dia::CmdSourceInfo& sourceInfo, const
char* slaveName, const char*
masterName, ::motion::sync::cmd::SyncSource
syncSource, ::motion::sync::cmd::DynSyncDirection
dynSyncDirection,
const ::motion::sync::cmd::FlexprofileParameters& parameters,
bool buffered, uint64_t& cmdID);

Further information
● See chapter 4 "Introduction and overview"
● ⮫ Chapter 7.2.28 AxsFlexprofile, AxsFlexprofile2, AxsFlexprofileEx, AxsFlex‐
  profileEx2 - Commanding an electronic cam (FlexProfile) on page 457
● ⮫ Chapter 8.1.2 Window – “Axes” on page 795
● ⮫ Chapter 8.1.3 Window – “Axis Profiles” on page 803
● ⮫ Chapter 8.1.4 Window – “Coordinated Motion” on page 806

### 7.2.29 AxsSetFlexProfileConfiguration, AxsFlexProfileValidate - Config‐

uring and validating the electronic cam (FlexProfile)
Basics
By using these function, an electronic cam (FlexProfile) can be config‐
ured and validated (see also ⮫ Chapter 6.2.3 Electronic cam (FlexProfile)
on page 128). After successful validation, the FlexProfile can be executed (see
also ⮫ Chapter States on page 145).
It is not possible to configure the FlexProfile in the following FlexProfile states
(see also ⮫ Chapter States on page 145):
● LOCKED_FOR_RUN: The FlexProfile is currently executed. Exit the command
  to be able to configure the FlexProfile
● IN_VALIDATION: The FlexProfile is currently validated. Wait until the valida‐
  tion is complete. The state then changes to VALID or INVALID
The following differences occur in the available interfaces:

● Data Layer: There is a separate Data Layer node for configuration and one
  for validation. Processing is not deterministic
● PLC: There is a function that performs both the configuration and the
  validation. It is deterministic, but does not guarantee real-time capability.
  The processing time required depends on the size and complexity of the
  FlexProfile
● BundleIF: There is a separate function for configuration and a separate
  function for validation. They are deterministic, but do not guarantee real-
  time capability. The processing time required depends on the size and
  complexity of the FlexProfile
                      Depending on the number of segments and events,
        NOTICE        calling up the function in a real-time context can lead
                      to a high CPU load.

PLC:

STRUCT ML_AxsSetFlexProfileConfigurationData
Name       Data type     Inherited     Address            Initial value   Comment
                         from
  In       ML_iAxsSet‐                                                    Input: Configuration data
           FlexProfile‐                                                   of the FlexProfile
           Configuration
  Out      ML_oState‐                                                     Output: Return parameter
           Base
STRUCT ML_iAxsSetFlexProfileConfiguration EXTENDS ML_iAxsStateBase
Name         Data type    Inherited     Address    Initial value Comment
                          from
   AxisName STRING(63) ML_iAxsSta‐                               Name of the axis whose
                          teBase                                 data is to be processed
   Profile‐  STRING(15)                                          Name of the FlexProfile to
Name                                                             be configured
   NumberOf‐ UINT                                                Number of configured seg‐
Segments                                                         ments (max. 64)
   NumberO‐ UINT                                                 Number of configured
fEvents                                                          events (max. 64)
   Segments ARRAY                                                Segment configuration
             [1..64] OF
             ML_iAxsFlex‐
             ProfileSeg‐
             ment
   Events    ARRAY                                               Event configuration
             [1..64] OF
             ML_iAxsFlex‐
             ProfileEvent
   MasterAx‐ LREAL                                               Master axis reference
isReference‐                                                     velocity
Velocity

STRUCT ML_iAxsSetFlexProfileConfiguration EXTENDS ML_iAxsStateBase
  Units     ML_iAxsFlex‐                                        Unit configuration
ProfileUnits
STRUCT ML_iAxsFlexProfileSegment
Name        Data type     Inherited    Address      Initial value   Comment
                          from
 Gain       LREAL                                   0.0        Stroke of the segment -
                                                               range of the slave axis (Y)
   Range           LREAL                            0.0        Length of the segment -
                                                               range of the master axis
                                                               (X)
   V0              LREAL                            0.0        Start velocity
   A0              LREAL                            0.0        Start acceleration
   J0              LREAL                            0.0        Start jerk
   V1              LREAL                            0.0        Final velocity
   A1              LREAL                            0.0        Final acceleration
   J1              LREAL                            0.0        End jerk
   LimV            LREAL                            0.0        Limit velocity
   LimA0           LREAL                            0.0        Limit acceleration
   LimA1           LREAL                            0.0        Limit delay
   LimJ0           LREAL                            0.0        Limit acceleration jerk
   LimJ1           LREAL                            0.0        Limit delay jerk
   Lambda          LREAL                            0.5        Inflection point (range 0.0
                                                               to 1.0)
   SyncType        ML_iAxsFlex‐                     SEG_DEFAUL Segment transition type
                   ProfileSeg‐                      T
                   mentSync‐
                   Type
   LawType         ML_iAxsFlex‐                     COMMON_P Type of motion law (e.g.
                   ProfileSeg‐                      OLYNO‐   5th degree polynomial)
                   mentLaw‐                         MIAL_5
                   Type
  PointTa‐         STRING(50)                                       Point table name
bleReference
  Master     UINT                                   1               Master type (0: time
                                                                    master, 1: axis master)
ENUM ML_iAxsFlexProfileSegmentSyncType
Name       Data type     Inherited   Address        Initial value   Comment
                         from
           INT                                                      Analytical profile, cam pro‐
SEG_DEFAUL                                                          file
T
           INT                                                      X: relative, Y: relative
SEG_FLEX_R
EL_REL
           INT                                                      X: absolute, Y: relative
SEG_FLEX_A
BS_REL

ENUM ML_iAxsFlexProfileSegmentSyncType
INT                                                X: relative, Y: absolute
SEG_FLEX_R
EL_ABS
INT                                                X: absolute, Y: absolute
SEG_FLEX_A
BS_ABS
ENUM ML_iAxsFlexProfileSegmentLawType
Name                           Data Inher‐ Addres Initial   Comment
type   ited s      value
from
  REST_IN_REST_INCLINED_SINE INT                            Rest-in-rest, inclined sine line

  REST_IN_REST_POLYNOMIAL_5 INT                             Rest-in-rest, 5th order poly‐
nomial
  REST_IN_VELOCITY_POLYNO‐    INT                           Rest-in-velocity, 5th order
MIAL_5                                                      polynomial
  REST_IN_VELOCITY_POLYNO‐    INT                           Rest-in-velocity, 7th order
MIAL_7                                                      polynomial
  VELOCITY_IN_REST_POLYNO‐    INT                           Velocity-in-rest, 5th order
MIAL_5                                                      polynomial
  VELOCITY_IN_REST_POLYNO‐    INT                           Velocity-in-rest, 7th order
MIAL_7                                                      polynomial
  VELOCITY_IN_VELOCITY_LINEAR INT                           Velocity-in-velocity, constant
velocity
  VELOCITY_IN_VELOCITY_POLY‐   INT                          Velocity-in-velocity, polyno‐
NOMIAL_5                                                    mial 5th order
  REST_IN_REST_LINEAR          INT                          Rest-in-rest, standstill
  REST_IN_REST_POLYNOMIAL_7    INT                          Rest-in-rest, 7th order poly‐
nomial
  REST_IN_REST_SINE            INT                          Rest-in-rest, sine line
  REST_IN_REST_SINE_GUTMAN     INT                          Rest-in-rest, Gutman sinus‐
oids
  REST_IN_REST_SINE_ACC        INT                          Rest-in-rest, acceleration-
optimal inclined sine line
  REST_IN_REST_SINE_TORQUE     INT                          Rest-in-rest, torque-optimal
inclined sine line
  REST_IN_REST_MOD_TRAPEZE     INT                          Rest-in-rest, modified acceler‐
ation trapezoid
  REST_IN_REST_MOD_SINE        INT                          Rest-in-rest, modified sinoids
  VELOCITY_IN_VELOCITY_POLY‐   INT                          Velocity-in-velocity, polyno‐
NOMIAL_7                                                    mial 7th order
INT                            Velocity-in-velocity, modified
VELOCITY_IN_VELOCITY_MOD_SIN                                sinoids
E
  REST_IN_REST_POLYNO‐       INT                            Rest-in-rest, 5th order
MIAL_5_VLIM                                                 velocity-limited polynomial
  REST_IN_REST_PARABOLA      INT                            Rest-in-rest, square parabola
  REST_IN_REST_POLYNOMIAL_8 INT                             Rest-in-rest, 8th order poly‐
nomial
  MOTION_IN_MOTION_POLYNO‐     INT                          Motion-in-motion, 5th order
MIAL_5                                                      polynomial

ENUM ML_iAxsFlexProfileSegmentLawType
  MOTION_IN_MOTION_POLYNO‐ INT                                    Motion-in-motion, 7th order
MIAL_7                                                            polynomial
  COMMON_POLYNOMIAL_5          INT                                5th order polynomial
  COMMON_POLYNOMIAL_7          INT                                7th order polynomial
  COMMON_POLYNOMIAL_2          INT                                2nd order polynomial
  COMMON_POLYNOMIAL_3          INT                                3th order polynomial
  COMMON_POLYNOMIAL_4          INT                                4th order polynomial
  COMMON_POLYNOMIAL_8          INT                                8th order polynomial
  VELOCITY_IN_VELOCITY_TRA‐    INT                                Velocity-in-velocity, accelera‐
PEZE_ALIM                                                         tion-limited trapezoidal pro‐
file
  MOTION_IN_MOTION_POLYNO‐       INT                              Motion-in-motion, 5th order
MIAL_5_VLIM                                                       velocity-limited polynomial
  MOTION_IN_MOTION_POLYNO‐       INT                              Motion-in-motion, overshoot-
MIAL_5_SLIM                                                       free 5th order polynomial
  FIT_VEL_TRAPEZE_ALIM           INT                              Acceleration-limited motion
(trapezoidal profile)
   FIT_SINE_TRAPEZE_ALIM         INT                              Acceleration-limited motion
(sine curve)
   FIT_ACC_TRAPEZE_JLIM          INT                              Jerk-lim. motion (trapezoidal
profile)
   MOTION_IN_MOTION_ACAM         INT                              Motion-in-motion, linear
acceleration
   MOTION_IN_MOTION_VCAM         INT                              Motion-in-motion, linear
velocity
   MOTION_IN_MOTION_VCAM2_A      INT                              Motion-in-motion, 2nd order
velocity (start acceleration 0)
   MOTION_IN_MOTION_VCAM2_B INT                                   Motion-in-motion, 2nd order
velocity (final acceleration 0)
   POINTS_TABLE_AUTO             INT                              Point table with interpolation
(up to 1,024 points)
   POINTS_TABLE_LIN              INT                              Point table with linear inter‐
polation (up to 100,000
points)
   POINTS_TABLE_SPLINE           INT                              Point table with spline inter‐
polation (up to 100,000
points)
STRUCT ML_iAxsFlexProfileEvent
Name        Data type       Inherited   Address   Initial value     Comment
                            from
  Seg‐      UINT                                  0          Segment number for which
mentNmb                                                      the event is configured
  Trigger‐  ML_iAxsFlex‐                          SEG_TRIGGE Trigger condition
Condition   ProfileSegment‐                       R_EXTERNAL
            TriggerCondi‐
            tion
  Trigger‐  LREAL                                 0.0               Trigger value
Value
  Master‐   UINT                                  1                 Trigger master type (0: time
Type                                                                master, 1: axis master)

STRUCT ML_iAxsFlexProfileEvent
  Action‐   ML_iAxsFlex‐                         SEG_ACTION Action
Mode        ProfileSegmen‐                       _EXTERNAL_I
tActionMode                          NSTANT
  ActionBit UINT                                 0           Number of the status bit
                                    that is set by the action
                                    (0...31)
ENUM ML_iAxsFlexProfileSegmentTriggerCondition
Name        Data type    Inherited    Address    Initial value   Comment
                         from
            INT                                                  Trigger with external signal
SEG_TRIGGE

R_EXTERNAL
INT                                                  Trigger for absolute slave
SEG_TRIGGE                                                       axis position
R_SLAVE_RE
ACHED_ABS
INT                                                  Trigger for relative slave
SEG_TRIGGE                                                       axis position
R_SLAVE_RE
ACHED_REL
INT                                                  Trigger with absolute
SEG_TRIGGE                                                       master axis position
R_MASTER_R
EACHED_ABS
INT                                                  Trigger with relative master
SEG_TRIGGE                                                       axis position
R_MASTER_R
EACHED_REL
INT                                                  Trigger after a relative time
SEG_TRIGGE
R_MASTER_TI
ME_REACHE
D_REL
ENUM ML_iAxsFlexProfileSegmentActionMode
Name        Data type    Inherited   Address     Initial value   Comment
                         from
            INT                                                  Set the status bit immedi‐
SEG_ACTION                                                       ately
_EXTERNAL_I
NSTANT
            INT                                                  Set the status bit at the
SEG_ACTION                                                       end of the segment
_EXTERNAL_
AFTERSEG
            INT                                                  Set the status bit at the
SEG_ACTION                                                       end of the FlexProfile
_EXTERNAL_
AFTER‐
GROUP

ENUM ML_iAxsFlexProfileSegmentActionMode
INT                                                         Set the status bit immedi‐
SEG_ACTION                                                              ately and switch to the next
_EXTERNAL_I                                                             segment
NSTANT_NEX
TSEG
STRUCT ML_iAxsFlexProfileUnits
Name          Data type   Inherited        Address      Initial value   Comment
                          from
   PosUnit‐   STRING(15)                                            Position unit of the master
Master                                                              axis
   VelUnit‐   STRING(15)                                ANY_TO_STRI Velocity unit of the master
Master                                                  NG("rpm")   axis
   PosUnit‐   STRING(15)                                            Position unit of the slave
Slave                                                               axis
   VelUnit‐   STRING(15)                                            Velocity unit of the slave
Slave                                                               axis
   AccUnit‐   STRING(15)                                            Acceleration unit of the
Slave                                                               slave axis
   JrkUnit‐   STRING(15)                                            Jerk unit of the slave axis
Slave
   ActivateU‐ BOOL                                      FALSE           Should the units be com‐
nits                                                                    plied with

Data Layer:
Method: POST
URL: https://<ip-addr>/automation/api/v2/nodes/motion/axs/[axsName]/cfg/
functions/coupling/sync-motion/flexprofile/profiles/[profileName]
Payload: Configuring a FlexProfile

{
"type":"object","value":
{
  "name": "0",
  "segments": [
    {
      "gain": 50,
      "range": 10,
      "v0": 0,
      "a0": 0,
      "j0": 0,
      "v1": 0,
      "a1": 0,
      "j1": 0,
      "limV": 0,
      "limA0": 0,
      "limA1": 0,
      "limJ0": 0,
      "limJ1": 0,
      "lambda": 0.5,
      "syncType": "SEG_DEFAULT",
      "lawType": "REST_IN_REST_POLYNOMIAL_5",
      "pointTableReference": "",
      "master": 1,

            "camBuilderSegmentData": ""
        }
    ],
    "events": [
       {
         "segmentNmb": 0,
         "triggerCondition": "SEG_TRIGGER_MASTER_REACHED_REL",
         "triggerValue": 5,
         "masterType": 1,
         "actionMode": "SEG_ACTION_EXTERNAL_INSTANT",
         "actionBit": 0,
         "segmentNmbFormula": 0,
         "valueFormula": ""

       }
    ],
    "masterAxsRefVel": 1,
    "camBuilderProfileData": ""
    "units": {
         "posUnitMaster": "deg",
         "velUnitMaster": "rpm",
         "posUnitSlave": "deg",
         "velUnitSlave": "rpm",
         "accUnitSlave": "rad/s^2",
         "jrkUnitSlave": "rad/s^3",
         "activateUnits": true
       }
}
}

Method: POST
URL: https://<ip-addr>/automation/api/v2/nodes/motion/axs/[axsName]/cfg/
functions/coupling/sync-motion/flexprofile/validate
Payload: FlexProfile name

{
"type":"string","value":"0"
}

BundleIF:
/// @brief Configure a FlexProfile.
///
/// The function is optimized for speed and can be used in
    real-time context (lock- and wait-free), when the
    motion kernel is in state RUNNING.
/// If the motion kernel is not in state RUNNING, the
    function call is not real-time capable.
///
/// @param[in]   handle    Handle of the interface.
/// @param[in]   axsName   Name of FlexProfile axis
/// @param[in]   config    Configuration of a single
                           FlexProfile
/// @return                Status of the function call:
                           STS_OK or an error code on
                           failure.
::motion::core::MotionResult(*axsFlexProfileConfig)(void*
handle, const char*
axsName, ::motion::sync::data::FlexProfileCfg& config);

/// @brief Validate a FlexProfile.
///
/// The function is optimized for speed and can be used
    in a real-time context (lock- and wait-free), when
    the motion kernel is in state RUNNING.
/// If the motion kernel is not in state RUNNING, the
    function call is not real-time capable.
///
/// @param[in]   handle        Handle of the interface.
/// @param[in]   axsName       Name of FlexProfile axis
/// @param[in]   profileName   Name of FlexProfile
/// @return                    Status of the function call:
                               STS_OK or an error code on
                               failure.
::motion::core::MotionResult(*axsFlexProfileValidate)(void*
handle, const char* axsName, const char* profileName);

Further information
● ⮫ Chapter 7.1 General information on page 325
● ⮫ Chapter 7.2.29 AxsSetFlexProfileConfiguration, AxsFlexProfileValidate -
  Configuring and validating the electronic cam (FlexProfile) on page 468
● ⮫ Chapter 8.1.2 Window – “Axes” on page 795
● ⮫ Chapter 8.1.3 Window – “Axis Profiles” on page 803
● ⮫ Chapter 8.1.4 Window – “Coordinated Motion” on page 806

### 7.2.30 AxsSetAbsPos - Set axis to absolute position

Basics
This command is used to:
● Set a position data reference for an absolute measuring system
● Referencing the position of an encoder axis
The command does not move the axis physically but only sets the new posi‐
tion value. The execution behavior is automatically determined based on the
axis category selected by the user:
● Use case 1: executed for ⮫ Chapter Axis objects on page 20
● Use case 2: executed for ⮫ Chapter Encoder axis objects on page 26
In use case 2, the command only creates an offset between the encoder and
the motion. Therefore, the command for this use case is executed synchro‐
nously, i.e. without delay.

PLC:

ML_AxsSetAbsPos
Name        Data type           Inherited    Address       Initial value   Comment
                                from

ML_AxsSetAbsPos
  Data      ML_AxsSe‐                                               Output: Command parame‐
tAbsPos                                                 ters
  ML_AxsSe‐ BOOL                                                    Returns information
tAbsPos                                                             whether the command can
be added to the axis
object.
● TRUE: The ML_AxsSe‐
  tAbsPos command could
  be added successfully
● FALSE: An error
  occurred. Details in

  ML_oCmdResult
STRUCT ML_AxsSetAbsPosData
Name       Data type   Inherited          Address   Initial value   Comment
                       from
  In       ML_iAxsSe‐                                               Input: Command data of
           tAbsPos                                                  the command
  Out      ML_oCmdRe‐                                               Output: Command parame‐
           sult                                                     ters
STRUCT ML_iAxsSetAbsPos EXTENDS ML_iAxsCmdBase
Name        Data type   Inherited  Address     Initial value        Comment
                        from
  AxisName STRING(15) ML_iAxsCmd‐                                   Name of the axis used to
                        Base                                        execute the command
  Source    STRING(50) ML_iAxsCmd‐                                  Specifies the command
                        Base                                        source, e.g PlcApplication1
                                                                    is displayed in the diag‐
                                                                    nostic messages
  SourceLine ULINT          ML_iAxsCmd‐                             Specifies the source line of
                            Base                                    the command; is displayed
                                                                    in the diagnostic messages
  Position   LREAL                                                  Commanded absolute
                                                                    target position
STRUCT ML_oCmdResult
Name       Data type        Inherited     Address   Initial value   Comment
                            from
  CmdID      ULINT                                                  Command ID (is set to
                                                                    18446744073709551615 in
                                                                    the event of an error)
  Error      BOOL                                                   Error ID TRUE indicates
                                                                    that an error occurred
  ErrorID    ULINT                                                  Specifies the type of
                                                                    occurred error: The upper
                                                                    4 bytes reflect the main
                                                                    diagnostics, the lower 4
                                                                    bytes reflect the detailed
                                                                    diagnostics, 0 means no
                                                                    error

Data Layer:
Method: POST

URL:               https://<ip-addr>/automation/api/v2/nodes/motion/axs/
<axs_name>/cmd/set-pos-abs
Payload:

{
"type":"object","value":
{
"buffered":false,
"axsPos":0.0
}
}

Python:
<cmdID> = MotionLib.axs_set_pos_abs( axs=<axsName>,
pos=<NewPosition>, buffered=True )

Generates a posAbs command for a single axis (object has to be "attached"),
see documentation Python Runtime App ⮫ Python functions.
● <axsName> - string, axis object name
● <NewPosition> - double, new axis position

BundleIF:

//! Create a motion command for a single axis (SetAbsPos)
//!
//! @param[in]    handle     Handle of the interface
//! @param[in]    sourceInfo Command source information
//! @param[in]    axsName    Name of the motion object
//! @param[in]    targetPos  Target position to be set
//! @param[in]    buffered   Is buffered mode? (Only support
bufferd mode yet)
//! @param[out] cmdID        The ID of the added command
//! @return                  Was everything okay?
motion::core::MotionResult MOTION_CORE_AxsSetAbsPosCmd(void*
handle, const motion::core::dia::CmdSourceInfo & sourceInfo,
const char* axsName, double targetPos, bool buffered,
uint64_t&cmdID);

### 7.2.31 AxsProbe - Axis probe

Basics
The AxsProbe command activates the probe functionality in the drive. Specify
the axis name, the triggering input and the data storage. The measuring probe
can be configured for single or continuous triggering.
The recorded values can be read with the command ⮫ Chapter 7.2.32 GetAxis‐
ProbeValues - Read axis probe on page 484. The command ⮫ Chapter 7.2.33
AxsProbeAbort - Axis probe, abort measurement on page 487 cancels the
measurement.
In MOT-V-0118:
−   The input signal supports only the actual position value and the calcula‐
    tion of the edge difference only supports the standard mode

Further information, in particular on configuration, can be found under
⮫ Chapter 6.1.3 Measuring probe on page 76.

PLC:

STRUCT ML_AxsProbeData

Name       Data type   Inherited          Address   Initial value   Comment
                       from
  In       ML_iAxsP‐                                                Input: Command data of
           robe                                                     the command
  Out      ML_oCmdRe‐                                               Output: Command parame‐
           sult                                                     ters
STRUCT ML_iAxsProbe EXTENDS ML_iAxsCmdBase
Name        Data type   Inherited   Address         Initial value   Comment
                        from
  AxisName STRING(15) ML_iAxsCmd‐                                   Name of the axis used to
                        Base                                        execute the command
  Source    STRING(50) ML_iAxsCmd‐                                  Specifies the command
                        Base                                        source, e.g PlcApplication1
                                                                    is displayed in the diag‐
                                                                    nostic messages
  SourceLine ULINT          ML_iAxsCmd‐                             Specifies the source line of
                            Base                                    the command; is displayed
                                                                    in the diagnostic messages
  TriggerSrc‐ STRING(15)                                            Axis name of the trigger
Name                                                                axis
  Index       ML_Pro‐                                               Selecting the measuring
              beIndex                                               input
  Data        ML_Probe‐                                             Data for measuring param‐
              DataT                                                 eters
STRUCT ML_oCmdResult
Name       Data type        Inherited     Address   Initial value   Comment
                            from
  CmdID      ULINT                                                  Command ID (is set to
                                                                    18446744073709551615 in
                                                                    the event of an error)
  Error      BOOL                                                   Error ID TRUE indicates
                                                                    that an error occurred
  ErrorID    ULINT                                                  Specifies the type of
                                                                    occurred error: The upper
                                                                    4 bytes reflect the main
                                                                    diagnostics, the lower 4
                                                                    bytes reflect the detailed
                                                                    diagnostics, 0 means no
                                                                    error

ENUM ML_ProbeIndex
Name       Data type              Inherited   Address   Initial value   Comment
                                  from
   PROBE_1         INT                                                  Touch probe 1
   PROBE_2         INT                                                  Touch probe 2
STRUCT ML_ProbeDataT
Name       Data type              Inherited   Address   Initial value   Comment
                                  from
  Measuring‐ ML_Measur‐                                 ML_MESUR‐ Measuring signal selection
SigSelect    ingSigSelect                               INGSIGSE‐
                                                        LECT .POS_F
                                                        EED‐
                                                        BACK_VAL_E
                                                        NCODER_1
  Measuring‐ ML_Measur‐                                 ML_MESUR‐ Measurement type: contin‐
Type         ingType                                    INGTYPE .SI uous or single measure‐
                                                        NGLE_SHOT ment
  Evalua‐          ML_Evalua‐                           ML_EVALUA‐ Selection which edge is
teEdgeType         teEdgeType                           TEEDGE‐      evaluated
                                                        TYPE .EVAL_
                                                        DIABLED
  Evaluate‐        ML_Evaluate‐                         ML_EVALUA‐ Type of difference evalua‐
DiffType           DiffType                             TEDI‐        tion
                                                        FFTYPE .EVA
                                                        L_DIFF_DISA‐
                                                        BLED
   Expect‐    BOOL                                      FALSE        If TRUE, the expectation
WindowEdg‐                                                           window is enabled
eEnable
   Expect‐    LREAL                                     0.0             Start of the expectation
WindowStart                                                             window
   Expect‐    LREAL                                     0.0             End of expectation window
WindowEnd
   Enable‐    BOOL                                      FALSE           If TRUE, the lost marker
MarkerFai‐                                                              check is enabled
lure
   MaxNum‐ UDINT                                        0               Maximum number of
berOfMarker‐                                                            marker failures
Failures
   TimeCom‐ BOOL                                        FALSE           If TRUE, enable the probe
pensateEn‐                                                              dead time compensation
able
   TimeCom‐ LREAL                                       0.0             Dead time compensation
pensatePo‐                                                              for positive edge
sEdge
   TimeCom‐ LREAL                                       0.0             Dead time compensation
pensateNe‐                                                              for negative edge
gEdge
   Monitorin‐ BOOL                                      FALSE           Switch-on level monitoring
gActive                                                                 active, only works with
                                                                        drive-based probe 1

STRUCT ML_ProbeDataT
  AutoActi‐ BOOL                                  FALSE           If TRUE, the probe system
vated                                                             is enabled following the
                                          configuration
ENUM ML_MeasuringSigSelect
Name       Data type    Inherited       Address   Initial value   Comment
                        from
           INT                                                    Actual position value,
POS_FEED‐                                                         encoder 1
BACK_VAL_E
NCODER_1
           INT                                                    Actual position value,

POS_FEED‐                                                         encoder 2
BACK_VAL_E
NCODER_2
INT                                                    System time
SYSTEM_FIN
E_TIME
ENUM ML_MeasuringType
Name      Data type         Inherited   Address   Initial value   Comment
                            from
  CONTIN‐    INT                                                  Continuous measurement
UOUS
             INT                                                  Single measurement
SINGLE_SHO
T
ENUM ML_EvaluateEdgeType
Name        Data type   Inherited       Address   Initial value   Comment
                        from
  EVAL_DIS‐ INT                                                   Disabling the evaluation
ABLED
            INT                                                   Evaluating the positive
EVAL_POS_E                                                        edge
DGE
            INT                                                   Evaluating the negative
EVAL_NEG_E                                                        edge
DGE
            INT                                                   Positive and negative edge
EVAL_POS_N                                                        are evaluated
EG_EDGE
ENUM ML_EvaluateDiffType
Name        Data type    Inherited      Address   Initial value   Comment
                         from
            INT                                                   Differential measurement is
EVAL_DIFF_D                                                       disabled
ISABLED
            INT                                                   Difference of the last two
EVAL_DIFF_S                                                       measured values
TAN‐
DARD_MODE

ENUM ML_EvaluateDiffType
INT                                                      Difference between nega‐
EVAL_DIFF_N                                                          tive edge to negative edge
EG_TO_NEG_
EDGE
INT                                                      Difference between posi‐
EVAL_DIFF_P                                                          tive edge to negative edge
OS_TO_NEG_
EDGE
INT                                                      Difference between nega‐
EVAL_DIFF_N                                                          tive edge to positive edge
EG_TO_POS_
EDGE
INT                                                      Difference between posi‐
EVAL_DIFF_P                                                          tive edge to positive edge
OS_TO_POS_
EDGE

Data Layer:
Method: POST
URL:               https://<ip-addr>/automation/api/v2/nodes/motion/axs/
<axs_name>/cmd/probe
Payload:

{
"type":"object","value":
     {
       "baseData":
       {
          "triggerSrc": "",
          "probeIndex": ""
       },
       "cfgData":
       {
          "measurSigSel": "",
          "measurType": "",
          "evalEdgeType": "",
         "evalDiffType": "",
         "expWindowEdgeEnable": false,
         "expWindowStart": 0,
         "expWindowEnd": 0,
         "enableMarkFailure": false,
         "maxNumOfMarkFailuer": 0,
         "timeCompEnable": false,
         "timeCompPosEdge": 0,
         "timeCompNegEdge": 0,
         "lvlMonitorActive": false,
         "isAutoActivated": false
      }
}

Python:
<cmdID> = MotionLib.axs_cmd_probe(axs=<axsName>,
trigge_src=<trigge_src>,
              probe_index=< probe_index >,

              measur_sig_sel=<measur_sig_sel >,
              measur_type=< measur_type >,
              eval_edge_type=< measur_type >,
              eval_diff_type=< eval_diff_type >,
              exp_window_edge_enable=<>,
              exp_window_start=< exp_window_start >,
              exp_window_end=< exp_window_end >,
              enable_mark_failure=< enable_mark_failure >,
              max_num_of_mark_failuer=<
max_num_of_mark_failuer >,
              time_comp_enable=< time_comp_enable >,
              time_comp_pos_edge=< time_comp_pos_edge >,
              time_comp_neg_edge=< time_comp_neg_edge >,

              lvl_monitor_active=< lvl_monitor_active >,
              is_auto_activated=< is_auto_activated >)

● <axsName> - string, axis name
● <probe_index> - string, the index of the probe, currently available "probe1",
  "probe2"
● <trigge_src> - string, default is empty
● <measur_sig_sel> - string, type of measurement signal ("encoder1",
  "encoder2", "finetime")
● <measur_type> - string, type of measurement ("continuous", "singleShot")
● <eval_edge_type> - string, edge type ("disabled", "posEdge", "negEdge",
  "posNeg")
● <eval_diff_type> - string, edge type ("disabled", "posEdge", "negEdge",
  "posNeg")
● <exp_window_edge_enable> - bool, the expectation window is enabled
● <exp_window_start> - float, start of the expectation window when the posi‐
  tive edge is evaluated
● <exp_window_end> - float, end of the expectation window when the posi‐
  tive edge is evaluated
● <enable_mark_failure> - bool, enable check for lost marker
● <max_num_of_mark_failuer> - int, threshold value for the registered number
  of marking errors
● <time_comp_enable> - bool, enable compensation of tester dead time
● <time_comp_pos_edge> - float, dead time compensation for the positive
  edge, if evaluated
● <time_comp_neg_edge> - float, dead time compensation for the negative
  edge, if evaluated
● <lvl_monitor_active> - bool, switch-on level monitoring active, works only
  with drive based probe1
● <is_auto_activated> - bool, button is automatically activated after configura‐
  tion

BundleIF:

/// @brief Create an probe command for a single axis
(AXS_CMD_PROBE)
///
/// @param[in]   sourceInfo      Command source information
/// @param[in]   axsName         Name of the axis object which
                                 the command will execute in
/// @param[in]   triggerSrcName Provides the probing device,

                                 can be nullptr or empty
                                 string to use the axsName
                                 as trigger axis
///                              When using self drive build
                                 in probe, set triggerSrcName
                                 to nullptr or empty string
///                              When using an external
                                 trigger source there are 2
                                 approach, which can be used
                                 probing on virtual axis:
///                              Setting triggerSrcName to a
                                 name of real axis whose
                                 probe will used;
///                              Setting triggerSrcName to
                                 "IO" which means probe will
                                 using external trigger
                                 signal, system interface
                                 setAxsProbeTrigger can be
                                 used to trigger one
                                 measurement.
/// @param[in]   index           Select of probe index
/// @param[in]   probeData       Parameter of probe
/// @param[out] cmdID            The ID of the added command
/// @return                      Status of the function call:
                                 STS_OK or an error code
                                 on failure.
::motion::core::MotionResult(*axsProbeCmd)(void* handle,
const ::motion::core::dia::CmdSourceInfo& sourceInfo,
const char* axsName, const char*
triggerSrcName, ::motion::core::cmd::probe::ProbeIndex index,
const ::motion::core::cmd::ProbeDataT& probeData, uint64_t
&cmdID);

### 7.2.32 GetAxisProbeValues - Read axis probe

Basics
The command getAxsProbeValue reads the determined values of a probe.
Specify the axis name, the triggering input and the data storage.
The measurement can be started with the ⮫ Chapter 7.2.31 AxsProbe - Axis
probe on page 478command. The command ⮫ Chapter 7.2.33 AxsProbeAbort -
Axis probe, abort measurement on page 487 cancels the measurement.
Further information, in particular on configuration, can be found under
⮫ Chapter 6.1.3 Measuring probe on page 76.

PLC:

FUNCTION ML_GetAxisProbeValues: BOOL
Name       Data type   Inherited    Address              Initial value   Comment
                       from

FUNCTION ML_GetAxisProbeValues: BOOL
  IN_OUT    ML_GetAxis‐                                            Input/output data
Data        ProbeValues‐
Data
   OUTPUT BOOL
ML_GetAxis‐
ProbeValues
STRUCT ML_GetAxisProbeValuesData
Name       Data type    Inherited        Address   Initial value   Comment
                        from
  In       ML_iGetAxis‐                                            Input data

ProbeValues
  Out      ML_oGetAxis‐                                            Initial data of the request
ProbeValues
STRUCT ML_iGetAxisProbeValues
Name        Data type   Inherited        Address   Initial value   Comment
                        from
  AxisName STRING(15)                                              Name of the axis from
                                                                   which you want to request
                                                                   data
  Index      ML_Pro‐                                               Selecting the probe index
             beIndex
ENUM ML_ProbeIndex
Name       Data type        Inherited    Address   Initial value   Comment
                            from
  PROBE_1    INT                                                   Probe 1
  PROBE_2    INT                                                   Probe 2
STRUCT ML_oGetAxisProbeValues EXTENDS ML_oStateBase
Name       Data type    Inherited   Address     Initial value      Comment
                        from
  Error    BOOL         ML_oState‐                                 Error flag TRUE means
                        Base                                       that an error has occurred
                                                                   (e.g. typing error in object
                                                                   name)
  ErrorID    ULINT          ML_oState‐                             Specifies the type of
                            Base                                   occurred error: The upper
                                                                   4 bytes reflect the main
                                                                   diagnostics, the lower 4
                                                                   bytes reflect the detailed
                                                                   diagnostics, 0 means no
                                                                   error
  Values     ML_Actual‐                                            Result of the current probe
             ProbeValueT                                           value
STRUCT ML_ActualProbeValueT
Name       Data type    Inherited        Address   Initial value   Comment
                        from
  Valid    BOOL                                                    If FALSE, the measured
                                                                   values could be partly new
                                                                   and partly old

STRUCT ML_ActualProbeValueT
  Measured‐ LREAL                                                            Measured value at which a
ValPosEdge                                                                   positive edge occurred
  Measured‐ LREAL                                                            Measured value at which a
ValNegEdge                                                                   negative edge occurred
  Position‐ LREAL                                                            Difference between trigger
Difference                                                                   values depending on Eval‐
                                                          uateDiffType
  Position‐ UDINT                                                            Differential measurement is
Difference‐                                                                  performed
Count
  Measured‐ UDINT                                                            Number of positive edges
ValPosEdge‐                                                                  detected
Count
  Measured‐ UDINT                                                            Number of negative edges
ValNegEdge‐                                                                  detected
Count
  Missing‐  UDINT                                                            Number of missing edges
MarksEdge‐
Count
  Status    ML_ProbeS‐                                                       Current probe status
tatus
ENUM ML_ProbeStatus
Name       Data type               Inherited   Address       Initial value   Comment
                                   from
                   INT                                                       Touch probe inactive
PROBE_IDLE
                   INT                                                       Touch probe in configura‐
PROBE_CON                                                                    tion
FIG
                   INT                                                       Touch probe is active
PROBE_ACTI
VE
                   INT                                                       Touch probe is incorrect
PROBE_ERR
OR

      Data Layer:
      Method: POST
      URL:     https://<ip-addr>/automation/api/v2/nodes/motion/axs/<axs_name>/
      state/functions/probe/[probe_index]
      Payload: (blank)

      Python:
      <Result> = MotionLib.get_axs_probe_values(axs=<axsName>,
      probe_index=<probe_index> )

      ● <axsName> - string, axis name
      ● <probe_index> - string, the index of the probe, currently available "probe1",
        "probe2"

● <Return> - Returns a directory with these entries:
  – measuredValueNegEdge - negative edge value
  – measuredValueNegEdgeCount - number of negative edges
  – measuredValuePosEdge - positive edge value
  – measuredValuePosEdgeCount - number of positive edges
  – missingMarksEdgeCount - number of missing marks on the edge
  – positionDifference - Position difference
  – positionDifferenceCount - number of position differences
  – Status - Status
  – Valid

BundleIF:

The button function consists of two command interfaces (activate/cancel
button) and one system interface (retrieve current button values):

/// @brief Get the probe actual value.
///
/// @param[in]   handle           Handle of the interface.
/// @param[in]   axsName          Name of the axis
/// @param[in]   index            Select of the probe index
/// @param[out] value             Actual value of the probe
/// @return                       Status of the function call:
                                  STS_OK or an error code on
                                  failure.
::motion::core::MotionResult(*getAxisProbeValues)(void
*handle, const char*
axsName, ::motion::core::cmd::probe::ProbeIndex
index, ::motion::core::data::ActualProbeValueT& value);

### 7.2.33 AxsProbeAbort - Axis probe, abort measurement

Basics
The AxsProbeAbort command completes the measurement with a probe. The
axis name and the triggering input have to be specified.
The measurement can be started with the ⮫ Chapter 7.2.31 AxsProbe - Axis
probe on page 478command. The command ⮫ Chapter 7.2.32 GetAxisProbe‐
Values - Read axis probe on page 484 reads the values determined by a meas‐
uring probe.
Further information, in particular on configuration, can be found under
⮫ Chapter 6.1.3 Measuring probe on page 76.

PLC:

STRUCT ML_AxsProbeAbortData
Name       Data type   Inherited         Address      Initial value   Comment
                       from
  In       ML_iAxsPro‐                                                Input: Command data of
           beAbort                                                    the command

STRUCT ML_AxsProbeAbortData
  Out      ML_oCmdRe‐                                                        Output: Command parame‐
sult                                                              ters
STRUCT ML_iAxsProbeAbort EXTENDS ML_iAxsCmdBase
Name        Data type   Inherited  Address     Initial value                 Comment
                        from
  AxisName STRING(15) ML_iAxsCmd‐                                            Name of the axis used to
                        Base                                                 execute the command
  Source    STRING(50) ML_iAxsCmd‐                                           Specifies the command
                        Base                                                 source, e.g PlcApplication1
                                                                             is displayed in the diag‐
                                                                             nostic messages
   SourceLine ULINT                ML_iAxsCmd‐                               Specifies the source line of
                                   Base                                      the command; is displayed
                                                                             in the diagnostic messages
  TriggerSrc‐ STRING(15)                                                     Trigger axis name
Name
  Index       ML_Pro‐                                                        Selecting the probe index
              beIndex
ENUM ML_ProbeIndex
Name       Data type               Inherited     Address     Initial value   Comment
                                   from
   PROBE_1         INT                                                       Touch probe 1
   PROBE_2         INT                                                       Touch probe 2

Data Layer:

Method: POST
URL:               https://<ip-addr>/automation/api/v2/nodes/motion/axs/
<axs_name>/cmd/probe-abort
Payload:

{
"type":"object","value":
     {
       "triggerSrc": "",
       "probeIndex": ""
     }
}

Python:
<cmdID> =
MotionLib.axs_cmd_probe_abort(axs=<axsName>,trigge_src_name=<tr
igge_src_name>,probe_index=<probe_index>)

● <axsName> - string, axis object name
● <trigge_src_name> - string, default is empty
● <probe_index> - string, the index of the currently available probe "probe1",
  "probe2"

BundleIF:

/// @brief Create an probe abort command for a single axis
(AXS_CMD_PROBEABORT)
///
/// @param[in]    sourceInfo      Command source information
/// @param[in]    axsName         Name of the axis object
                                  which the command will
                                  execute in
/// @param[in]    triggerSrcName  Provides the probing device,
                                  can be nullptr or empty
                                  string to use the axsName
                                  as trigger axis

///                               When using self drive build
                                  in probe, set triggerSrcName
                                  to nullptr or empty string
///                               When using an external
                                  trigger source there are
                                  2 approach, which can be
                                  used probing on virtual
                                  axis;
///                               Setting triggerSrcName to a
                                  name of real axis whose
                                  probe will used;
///                               Setting triggerSrcName to
                                  "IO" which means probe will
                                  using external trigger
                                  signal, system interface
                                  setAxsProbeTrigger can be
                                  used to trigger one
                                  measurement.
/// @param[in]    index           Select of probe
/// @param[out] cmdID             The ID of the added command
/// @return                       Status of the function call:
                                  STS_OK or an error code on
                                  failure.
::motion::core::MotionResult(*axsProbeAbortCmd)(void* handle,
const ::motion::core::dia::CmdSourceInfo& sourceInfo,
const char* axsName, const char*
triggerSrcName, ::motion::core::cmd::probe::ProbeIndex index,
uint64_t &cmdID);

### 7.2.34 AxsProbeEx - Axis extended probe

Basics
The AxsProbeEx command enables the probe functionality in the drive.
Specify the axis name, the triggering input and the data storage. The meas‐
uring probe can be configured for single or continuous triggering.
The recorded values can be read with the command ⮫ Chapter 7.2.32 GetAxis‐
ProbeValues - Read axis probe on page 484. The command ⮫ Chapter 7.2.35
AxsProbeAbortEx - Abort axis extended probe measurement on page 491 can‐
cels the measurement.
In MOT-V-0118:
−   The input signal supports only the actual position value and the calcula‐
    tion of the edge difference only supports the standard mode

Further information, in particular on configuration, can be found under
⮫ Chapter 6.1.3 Measuring probe on page 76.

PLC:

STRUCT ML_AxsProbeData
Name       Data type   Inherited              Address    Initial value   Comment
                       from
  In       ML_iAxsPro‐                                                   Input: Command data of
           beBase                                                        the command
  Out      ML_oCmdRe‐                                                    Output: Command parame‐
           sult                                                          ters
STRUCT ML_iAxsProbeBase EXTENDS ML_iAxsCmdBase
Name        Data type   Inherited  Address     Initial value             Comment
                        from
  AxisName STRING(15) ML_iAxsCmd‐                                        Name of the axis used to
                        Base                                             execute the command
  Source    STRING(50) ML_iAxsCmd‐                                       Specifies the command
                        Base                                             source, e.g PlcApplication1
                                                                         is displayed in the diag‐
                                                                         nostic messages
   SourceLine ULINT             ML_iAxsCmd‐                              Specifies the source line of
                                Base                                     the command; is displayed
                                                                         in the diagnostic messages
   Index           ML_Pro‐                                               Selecting the measuring
                   beIndex                                               input
STRUCT ML_oCmdResult
Name       Data type            Inherited     Address    Initial value   Comment
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
ENUM ML_ProbeIndex
Name       Data type            Inherited     Address    Initial value   Comment
                                from
   PROBE_1         INT                                                   Touch probe 1
   PROBE_2         INT                                                   Touch probe 2

Data Layer:
Method: POST
URL:               https://<ip-addr>/automation/api/v2/nodes/motion/axs/
<axs_name>/cmd/probe-ex
Payload:
{
    "type":"object",
    "value":
    {
      "probeIndex": "PROBE1"
    }
}

Python:
<cmdID> = MotionLib.axs_cmd_probe-ex(axs=<axsName>,
probe_index=< probe_index >)

● <axsName> - string, axis name
● <probe_index> - string, the index of the probe, currently available "probe1",
  "probe2"

BundleIF:

/// @brief Create an extended probe command for a single axis
///
/// Probe configuration has default value and can be changed
on datalayer
/// url: motion/axs/[axsName]/functions/probe/[probeIndex].
/// New configuration is only effect when a new command
instance is created.
///
/// @param[in]   sourceInfo      Command source information
/// @param[in]   axsName         Name of the axis object which
                                 the command will execute in
/// @param[in]   index           Select of probe index
/// @param[out] cmdID            The ID of the added command
/// @return                      Status of the function call:
                                 STS_OK or an error code
                                 on failure.
::motion::core::MotionResult(*axsProbeCmdEx)(void* handle,
const
::motion::core::dia::CmdSourceInfo& sourceInfo, const char*
axsName,
::motion::core::cmd::probe::ProbeIndex index, uint64_t &cmdID);

### 7.2.35 AxsProbeAbortEx - Abort axis extended probe measurement

Basics
The AxsProbeAbortEx command completes the extended measurement with a
probe. The axis name and the triggering input have to be specified.
The measurement can be started with the ⮫ Chapter 7.2.34 AxsProbeEx - Axis
extended probe on page 489command. The command ⮫ Chapter 7.2.32 GetAx‐
isProbeValues - Read axis probe on page 484 reads the values determined by
a measuring probe.

Further information, in particular on configuration, can be found under
⮫ Chapter 6.1.3 Measuring probe on page 76.

PLC:

STRUCT ML_AxsProbeBaseData
Name       Data type   Inherited              Address    Initial value   Comment
                       from
  In       ML_iAxsPro‐                                                   Input: Command data of
           beBase                                                        the command
  Out      ML_oCmdRe‐                                                    Output: Command parame‐
           sult                                                          ters
STRUCT ML_iAxsProbeBase EXTENDS ML_iAxsCmdBase
Name        Data type   Inherited  Address     Initial value             Comment
                        from
  AxisName STRING(15) ML_iAxsCmd‐                                        Name of the axis used to
                        Base                                             execute the command
  Source    STRING(50) ML_iAxsCmd‐                                       Specifies the command
                        Base                                             source, e.g PlcApplication1
                                                                         is displayed in the diag‐
                                                                         nostic messages
   SourceLine ULINT             ML_iAxsCmd‐                              Specifies the source line of
                                Base                                     the command; is displayed
                                                                         in the diagnostic messages
   Index           ML_Pro‐                                               Selecting the touch probe
                   beIndex                                               index
STRUCT ML_oCmdResult
Name       Data type            Inherited     Address    Initial value   Comment
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
ENUM ML_ProbeIndex
Name       Data type            Inherited     Address    Initial value   Comment
                                from
   PROBE_1         INT                                                   Touch probe 1
   PROBE_2         INT                                                   Touch probe 2

Data Layer:

Method: POST
URL:               https://<ip-addr>/automation/api/v2/nodes/motion/axs/
<axs_name>/cmd/probe-abort-ex
Payload:
{
"type":"object","value":
     {
       "probeIndex": "PROBE1"
     }
}

Python:
<cmdID> = motionLib.axs_cmd_probe_abort_ex (axs=<axsName>,
probe_index=<probe_index>)

● <axsName> - string, axis object name
● <probe_index> - string, the index of the currently available probe "probe1",
  "probe2"

BundleIF:

/// @brief Create an extended probe abort command for a single
axis
///
/// @param[in]   sourceInfo       Command source information
/// @param[in]   axsName          Name of the axis object
                                  which the command will
                                  execute in
/// @param[in]   index            Select of probe
/// @param[out] cmdID             The ID of the added command
/// @return                       Status of the function call:
                                  STS_OK or an error code on
                                  failure.
::motion::core::MotionResult(*axsProbeAbortCmdEx)(void*
handle, const
::motion::core::dia::CmdSourceInfo& sourceInfo, const char*
axsName,
::motion::core::cmd::probe::ProbeIndex index, uint64_t &cmdID);

### 7.2.36 AxsHoming - Homing command

General information
The homing command is used as motion command to position the axis on the
set reference point.
When the Motion command is executed, command C0600 is initiated on the
drive, triggering drive-guided homing.
The following actions are supported:
● Traversing the axis to the reference point and setting the new reference
  position
● Using the current position as reference point

Starting with Motion App version 4.2, cyclic monitoring of the "Homed" status
is supported only for SoE, not for CoE. For CoE, the drives can also be moved
in absolute mode even when no reference is available.
            Command type                            Is supported
              Buffered                                   Yes
             Not buffered                              Not yet

          Command interface                         Is supported
              Bundle                                     Yes
             Data Layer                                  Yes
                PLC                                      Yes
              Python                                     Yes

−   Homing method can be set in the drive
−   The homing command depends on the PLCopen state machine. This means
    that homing can only be initiated when the axis is in the STOP state.
−   If the drive's homed status is not set cyclically, the reference status is
    checked acyclically only when power is turned on for an axis.
−   An axis cannot be added to a kinematic system or gantry if it has not been
    homed

Configuration
To transmit the reference state cyclically, select the relevant settings.
IO configuration:
In the IO configuration, the parameter S-0-0144 (Signal Status Word) has to
be transferred in the AT S-0-0016.

Drive:
In parameter S-0-0144 "Signal status word," parameter S-0-0403 Homing pro‐
cedure: The actual value status word has to be stored.

Data Layer node
"motion/axs/x/state/capabilities/homed-cyclic"

In the Data Layer, you can use the "motion/axs/x/state/capabilities/homed-
cyclic" node to check whether the homed status is transmitted cyclically. If
the status is not transmitted, "addInfo": "signal status word not assigned" is
displayed there.

"motion/axs/x/state/values/homed"
You can use the "motion/axs/x/state/values/homed" node to check whether
the axis is homed.

PLC:

STRUCT ML_AxsHomingData
Name         Data type  Inher‐         Addres Initial   Comment
                        ited           s      value
                        from
  In         ML_iAx‐                                    Input: Command data of the command
             sHoming
  Out        ML_oCm‐                                    Output: Command parameters
             dResult
STRUCT ML_iAxsHoming EXTENDS ML_iAxsCmdBase
Name          Data type  Inher‐  Addres Initial         Comment
                         ited    s      value
                         from
  AxisName    STRING(15) ML                             Name of the axis used to execute the com‐
                         iAxscmd                        mand
                         Base
  Source      STRING(50) ML                             Specifies the command source, e.g PlcAp‐
                         iAxscmd                        plication1 is displayed in the diagnostic
                         Base                           messages
  SourceLine ULINT       ML                             Specifies the source line of the command;
                         iAxscmd                        is displayed in the diagnostic messages
                         Base
  NewRefPos LREAL                                       New reference point

STRUCT ML_oCmdResult
Name       Data type             Inherited   Address    Initial value   Comment
                                 from
   CmdID           ULINT         ML_iAxscmd‐                            Command ID (is set to
                                 Base                                   18446744073709551615 in
                                                                        the event of an error)
   Error           BOOL          ML_iAxscmd‐                            Error ID TRUE indicates
                                 Base                                   that an error occurred
   ErrorID         ULINT         ML_iAxscmd‐                            Specifies the type of
                                 Base                                   occurred error: The upper
                                                                        4 bytes reflect the main
                                                                        diagnostics, the lower 4
                                                                        bytes reflect the detailed
                                                                        diagnostics, 0 means no
                                                                        error

Data Layer:
Method: POST
URL:              https://<ip-addr>/automation/api/v2/nodes/motion/axs/
<axs_name>/cmd/homing
Payload:

{
"type":"object","value":
{
"buffered":true,
"newRefPos":0
}
}

Python:
<cmdID> = motion.axs_cmd_homing(axs=<axsName>, newRefPos)

Generates an axis referencing command for a single axis (object has to be
"attached"), see documentation Python Runtime App ⮫ Python functions.
● <axsName> - string, axis name
● <newRefPos> - double, new axis position

BundleIF:
//! @brief Create a motion command for a single axis
    (homing)
//!
//! @param[in]   handle      Handle of the interface
//! @param[in]   sourceInfo Command source information
//! @param[in]   axsName     Name of the motion object
//! @param[in]   newRefPos   New reference position after
                             homing
//! @param[in]   buffered    Is buffered mode? (only
                             support buffered mode yet)
//! @param[out] cmdID        The ID of the added command
//! @return                  Was everything okay?
motion::core::MotionResult MOTION_CORE_axsHomingCmd(void*
handle, const motion::core::dia::CmdSourceInfo & sourceInfo,

const char* axsName, double newRefPos, bool buffered, uint64_t
& cmdID);

### 7.2.37 AxsFixedStop - Traveling the axis to a fixed stop

Basics
This command enables traveling to fixed stop.
The command is an active stop function with limitation of the torque/force
and traveling of the axis to the specified target position by complying with
the specific dynamic limitations. The axis stops and the command changes
to state DONE if the torque/actual force exceeds the specified limit value
settings or reaches the target position.

Command type: buffered/unbuffered (unbuffered is not yet supported).
Command interface: Bundle, Data Layer, PLC, Python.
The following steps are executed after the fixed stop command has been cre‐
ated:
Section                                Execution
Preparation                            ● Wait for DONE of previous com‐
                                         mand in buffer
                                       ● Calculate target position
                                       ● Check dynamic limitations
                                       ● Set torque/force limit and enable
                                         positive stop
Before execution                       None
Execution                              ● Set IPO result to axis object
                                       ● Check status of positive stop
                                         – Stop axis, switch command to
                                           DONE if positive stop is trig‐
                                           gered
                                         – Approach target position and
                                           switch command to DONE
In version MOT-V-0108, wait for reaching of DONE state of the previous com‐
mand in the buffer prior to creating a fixed stop command. Wait for reaching
of DONE state of the fixed stop prior to creating a new command in the buffer.

PLC:

ML_AxsFixedStop
Name        Data type        Inherited    Address       Initial value   Comment
                             from
  Data       ML_AxsFixed‐                                               Output: Command parame‐
             Stop                                                       ters

ML_AxsFixedStop
  ML_AxsFix‐ BOOL                                                       Returns information
edStop                                                                  whether the command can
be added to the axis
object.
● TRUE: The ML_AxsFixed‐
  Stop command could be
  added successfully
● FALSE: An error
  occurred. Details in
  ML_oCmdResult
STRUCT ML_AxsFixedStopData
Name         Data type    Inher‐       Addres Initial   Comment
                          ited         s      value
                          from
  In         ML_iAxsFix‐                                Input: Command data of the command
             edStop
  Out        ML_oCm‐                                    Output: Command parameters
             dResult
STRUCT ML_iAxsFixedStop EXTENDS ML_iAxsCmdBase
Name        Data type    Inherited  Address    Initial value            Comment
                         from
  AxisName STRING(15) ML_iAxsCmd‐                                       Name of the axis used to
                         Base                                           execute the command
  Source    STRING(50) ML_iAxsCmd‐                                      Specifies the command
                         Base                                           source, e.g PlcApplication1
                                                                        is displayed in the diag‐
                                                                        nostic messages
   SourceLine ULINT        ML_iAxsCmd‐                                  Specifies the source line of
                           Base                                         the command; is displayed
                                                                        in the diagnostic messages
   MaxTorque LREAL                                                      Torque/force limit, value in
                                                                        configured unit
   Position        LREAL                                                Specified absolute position
                                                                        depending on command
                                                                        type
   DynLimits ML_iDynLi‐                                                 Limit values of the position
             mits                                                       command
STRUCT ML_iDynLimits
Name        Data type      Inherited      Address       Initial value   Comment
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
Name        Data type           Inher‐   Addres Initial   Comment
                                ited     s      value
                                from
 CmdID          ULINT                                     Command ID (is set to
                                                          18446744073709551615 in the event of
                                                          an error)
 Error          BOOL                                      Error ID TRUE indicates that an error
                                                          occurred
 ErrorID        ULINT                                     Specifies the type of occurred error: The
                                                          upper 4 bytes reflect the main diagnostics,
                                                          the lower 4 bytes reflect the detailed diag‐

                                      nostics, 0 means no error

Data Layer:
Method: POST
URL:               https://<ip-addr>/automation/api/v2/nodes/motion/axs/
<axs_name>/cmd/fixed-stop
Payload:

{
"type":"object","value":
{
  "axsPos":10,
  "maxTrq":10,
  "lim": {"vel":100,
            "acc":10,
            "dec":10,
            "jrkAcc":0,
            "jrkDec":0
          }
}
}

Python:
Is not yet supported.

BundleIF:

//! @brief Create a generic motion command
//!
//! @param[in]     sourceInfo   Command source information
//! @param[in]     name         Name of the motion object
//! @param[in]     cmdTypeID    The Type ID of the command to
be added
//! @param[in]     param        Parameters of the command
//! @param[in]     buffered     Is buffered mode? (only for
axis commands)
//! @param[out]    cmdID        The ID of the added command
//! @return                     Was everything okay?
motion::core::MotionResult genericCmd(const
dia::CmdSourceInfo& sourceInfo, const char* name,
cmd::CmdTypeID cmdTypeID, IContainer *param, bool buffered,
uint64_t &cmdID )
cmdTypeID：

motion::core::cmd::CmdTypeID(motion::core::ObjectType::AXIS,
"fixedstop")

### 7.2.38 AxsResetFixedStop - Reset the axis to fixed stop

Basics
This command is used to reset the command traveling to fixed stop.
Command type: buffered/unbuffered (unbuffered is not yet supported).
Command interface: Bundle, Data Layer, PLC, Python.
The following steps are executed after the command traveling to fixed stop is
reset:
Section                                  Execution
Preparation                              None
Before execution                         None
Execution                                ● Reset positive stop
                                         ● Set positive actual value to axis
                                           object

PLC:

ML_AxsResetFixedStop
Name        Data type           Inherited      Address       Initial value   Comment
                                from
   Data      ML_AxsRe‐                                                       Output: Command parame‐
             setFixedStop                                                    ters
  ML_AxsRe‐ BOOL                                                             Returns information
setFixedStop                                                                 whether the command can
                                                                             be added to the axis
                                                                             object.
                                                                             ● TRUE: The ML_AxsRe‐
                                                                               setFixedStop command
                                                                               could be added success‐
                                                                               fully
                                                                             ● FALSE: An error
                                                                               occurred. Details in
                                                                               ML_oCmdResult
STRUCT ML_AxsResetFixedStopData
Name         Data type    Inher‐            Addres Initial   Comment
                          ited              s      value
                          from
  In         ML_iAxsCmd                                      Input: Command data of the command
             Base
  Out        ML_oCm‐                                         Output: Command parameters
             dResult

STRUCT ML_iAxsCmdBase
Name        Data type         Inherited   Address          Initial value   Comment
                              from
 AxisName    STRING(15)       ML_iAxsCmd‐                                  Name of the axis used to
                              Base                                         execute the command
 Source      STRING(50)       ML_iAxsCmd‐                                  Specifies the command
                              Base                                         source, e.g PlcApplication1
                                                                           is displayed in the diag‐
                                                                           nostic messages
 SourceLine ULINT             ML_iAxsCmd‐                                  Specifies the source line of
                              Base                                         the command; is displayed
                                                                           in the diagnostic messages

STRUCT ML_oCmdResult
Name        Data type           Inher‐   Addres Initial   Comment
                                ited     s      value
                                from
 CmdID          ULINT                                     Command ID (is set to
                                                          18446744073709551615 in the event of
                                                          an error)
 Error          BOOL                                      Error ID TRUE indicates that an error
                                                          occurred
 ErrorID        ULINT                                     Specifies the type of occurred error: The
                                                          upper 4 bytes reflect the main diagnostics,
                                                          the lower 4 bytes reflect the detailed diag‐
                                                          nostics, 0 means no error

Data Layer:
Method: POST
URL:               https://<ip-addr>/automation/api/v2/nodes/motion/axs/
<axs_name>/cmd/reset-fixed-stop
Payload:

{
"type":"object","value":
{
"buffered": False
}
}

Python:
<cmdID> = motion.resetfixedstop(‘axsName’, buffered = true)

● <axsName> - string, axis object name
● buffered - boolean, command buffered type

BundleIF:

//! @brief Create a generic motion command
//!
//! @param[in]     sourceInfo   Command source information
//! @param[in]     name         Name of the motion object
//! @param[in]     cmdTypeID    The Type ID of the command to

be added
//! @param[in]     param        Parameters of the command
//! @param[in]     buffered     Is buffered mode? (only for
axis commands)
//! @param[out]    cmdID        The ID of the added command
//! @return                     Was everything okay?
motion::core::MotionResult genericCmd(const
dia::CmdSourceInfo& sourceInfo, const char* name,
cmd::CmdTypeID cmdTypeID, IContainer *param, bool buffered,
uint64_t &cmdID )
cmdTypeID：
motion::core::cmd::CmdTypeID(motion::core::ObjectType::AXIS,
"resetfixedstop")

### 7.2.39 AxsAddToGantry - Adding the axis to the gantry

Basics
This command adds the axis to a gantry master axis. This command does not
trigger a motion.
● The required slave axis and the gantry master axis have to be configured as
    gantry device
● The axes have to be in state STANDSTILL.
● The axis and the gantry master axis must not move.
If the axis has been added to the gantry successfully, the command is set to
DONE and the PLCOpen status of the axis changes to GANTRY_SLAVE.
Use ML_AxsGetPLCOpenState or ML_GetCmdState to read out the status.
Data Layer path            Type                    Description
https://<ip-addr>/         bool                    Is this axis part of a gantry?
automation/api/v2/                                 When set toTRUE, addToGantry and remove‐
nodes/motion/axs/                                  FromGantry are permitted
<axs_name>/cfg/func‐
                            If TRUE is set, the axis cannot be moved as long
tions/gantry/member
                            as it is connected.
https://<ip-addr>/     bool                        It is permitted to move an axis that is an uncon‐
automation/api/v2/                                 nected gantry device (risk mode).
nodes/motion/axs/
<axs_name>/cfg/func‐
tions/gantry/move-
allowed
https://<ip-addr>/     string                      NOT_GANTRY, UNCONNECTED, CON‐
automation/api/v2/                                 NECTED_MASTER, CONNECTED_SLAVE, UNCON‐
nodes/motion/axs/                                  NECTED_INDEP_MOVE_ALLOWED
<axs_name>/state/func‐
tions/coupling/gantry/
state
https://<ip-addr>/     int                         Number of synchronized Motion slaves currently
automation/api/v2/                                 connected to the axis
nodes/motion/axs/
<axs_name>/state/func‐
tions/coupling/sync-
slaves

PLC:

ML_AxsAddToGantry
Name       Data type         Inherited     Address   Initial value   Comment
                             from
  Data        ML_AxsAdd‐                                             Output: Command parame‐

ToGantry‐                                              ters
Data
BOOL                                                   Returns information
ML_AxsAdd‐                                                           whether the command can
ToGantry                                                             be added to the axis
object.
● TRUE: The command
  could be added success‐
  fully
● FALSE: An error
  occurred. Details in
  ML_oCmdResult
STRUCT ML_AxsAddToGantryData
Name       Data type   Inherited           Address   Initial value   Comment
                       from
  In       ML_iAxsAdd‐                                               Input: Command data of
           ToGantry                                                  the command
  Out      ML_oCmdRe‐                                                Output: Command parame‐
           sult                                                      ters
STRUCT ML_iAxsAddToGantry EXTENDS ML_iAxsCmdBase
Name        Data type   Inherited  Address     Initial value         Comment
                        from
  AxisName STRING(63) ML_iAxsCmd‐                                    Name of the axis used to
                        Base                                         execute the command
  Source    STRING(50) ML_iAxsCmd‐                                   Specifies the command
                        Base                                         source, e.g PlcApplication1
                                                                     is displayed in the diag‐
                                                                     nostic messages
  SourceLine ULINT           ML_iAxsCmd‐                             Specifies the source line of
                             Base                                    the command; is displayed
                                                                     in the diagnostic messages
MasterName STRING(15)                                                Name of the gantry master
                                                                     axis to be added to the
                                                                     axis
Buffered      Bool                                                   TRUE, if the command
                                                                     is to be executed as buf‐
                                                                     fered command, otherwise
                                                                     FALSE

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
URL:               https://<ip-addr>/automation/api/v2/nodes/motion/axs/
<axs_name>/cmd/add-to-gantry
Payload:

{
"type":"object","value":
{
  "masterName":"Axis1",
  "buffered":false
}
}

Python:
<cmdID> = motion.axs_cmd_add_to_gantry ( slave=<slaveName>,
master=<masterName> [,buffered=<buffered>] )

Creates an AddToGantry command for a single axis (object has to be
"attached"), see documentation Python Runtime App ⮫ Python functions
● <slaveName> - string, axis object name
● <masterName> - string, gantry master axis object name
● <buffered> - bool, use TRUE if the command is to be buffered (TRUE by
  default)

BundleIF:
//! Create a add to gantry command for a single axis
(AXS_CMD_ADDTOGANTRY)
//!
//! @param[in]   sourceInfo Command source information
//! @param[in]   slaveName   Name of the slave axis object
//! @param[in]   masterName Name of the master axis object
//! @param[in]   buffered    Is buffered mode?
//! @param[out] cmdID        The ID of the added command
//! @return                  Was everything okay?
virtual MotionResult axsAddToGantryCmd(const

cmd::CmdSourceInfo& sourceInfo, const char* slaveName, const
char* masterName, bool buffered, uint64_t &cmdID ) const = 0;

### 7.2.40 AxsRemoveFromGantry - Removing the axis from the gantry

Basics
This command removes an axis from the gantry master axis. This command
does not trigger a motion.
● The axis has to be in state GANTRY_SLAVE
● The axis and the gantry master must not move.
If the axis has been removed from the gantry successfully, the command is set
to DONE and the PLCOpen status of the axis is set to STANDSTILL.

Use ML_AxsGetPLCOpenState or ML_GetCmdState to read out the status.
This command is an unbuffered command, i.e. the previously active command
is canceled, the commands of the preparation buffer are discarded.
Data Layer path    Type               Description
https://<ip-       bool               Is this axis part of a gantry?
addr>/automa‐                         When set toTRUE, addToGantry and
tion/api/v2/nodes/                    removeFromGantry are permitted
motion/axs/
                                      If TRUE is set, the axis cannot be
<axs_name>/cfg/
                                      moved as long as it is not connected.
functions/gantry/
member
https://<ip-       bool               It is permitted to move an axis that
addr>/automa‐                         is an unconnected gantry device (risk
tion/api/v2/nodes/                    mode).
motion/axs/
<axs_name>/cfg/
functions/gantry/
move-allowed
https://<ip-       string             NOT_GANTRY, UNCONNECTED,
addr>/automa‐                         CONNECTED_MASTER,
tion/api/v2/nodes/
                                      CONNECTED_SLAVE,
motion/axs/
<axs_name>/state/                     UNCON‐
functions/cou‐                        NECTED_INDEP_MOVE_ALLOWED
pling/gantry/state
https://<ip-       int                Number of synchronized Motion slaves
addr>/automa‐                         currently connected to the axis
tion/api/v2/nodes/
motion/axs/
<axs_name>/state/
functions/cou‐
pling/sync-slaves

PLC:

ML_AxsRemoveFromGantry
Name        Data type  Inherited            Address   Initial value   Comment
                       from
  Data      ML_AxsRe‐                                                 Output: Command parame‐
            moveFrom‐                                                 ters
            GantryData
  ML_AxsRe‐ BOOL                                                      Returns information
moveFrom‐                                                             whether the command can
Gantry                                                                be added to the axis
                                                                      object.
                                                                      ● TRUE: The command
                                                                        could be added success‐
                                                                        fully
                                                                      ● FALSE: An error
                                                                        occurred. Details in
                                                                        ML_oCmdResult
STRUCT ML_AxsRemoveFromGantryData
Name       Data type   Inherited            Address   Initial value   Comment
                       from
  In       ML_iAxsCmd‐                                                Input: Command data of
           Base                                                       the command
  Out      ML_oCmdRe‐                                                 Output: Command parame‐
           sult                                                       ters
STRUCT ML_iAxsCmdBase
Name        Data type           Inherited   Address   Initial value   Comment
                                from
   AxisName STRING(63)                                                Name of the axis used to
                                                                      execute the command
   Source          STRING(50)                                         Specifies the command
                                                                      source, e.g PlcApplication1
                                                                      is displayed in the diag‐
                                                                      nostic messages
   SourceLine ULINT                                                   Specifies the source line of
                                                                      the command; is displayed
                                                                      in the diagnostic messages
STRUCT ML_oCmdResult
Name       Data type            Inherited   Address   Initial value   Comment
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

Data Layer:
Method: POST
URL:              https://<ip-addr>/automation/api/v2/nodes/motion/axs/
<axs_name>/cmd/rem-frm-gantry
Payload: (blank)

Python:
<cmdID> =
motion.axs_cmd_remove_from_gantry( slave=<slaveName> )

Creates a RemoveFromGantry command for a single axis (object has to be

"attached"), see documentation Python Runtime App ⮫ Python functions
● <slaveName> - string, axis object name

BundleIF:
//! Create a remove from gantry command for a single axis
(AXS_CMD_REMOVEFROMGANTRY)
//!
//! @param[in]   sourceInfo Command source information
//! @param[in]   slaveName   Name of the slave axis object
//! @param[out] cmdID        The ID of the added command
//! @return                  Was everything okay?
virtual MotionResult axsRemoveFromGantryCmd(const
cmd::CmdSourceInfo& sourceInfo, const char* slaveName,
uint64_t &cmdID ) const = 0;

### 7.2.41 AxsCtrlBasedGantryHoming - Control-based homing of gantry

axes
General information
Use this function to reference axes with incremental encoders of a gantry link.
Homing is a motion command used to reference the gantry axes.
The user can use the "refType" parameter to specify which position should be
used as the referenced position:
● Setting the reference position after axis stop
● The axes move back to the reference switch and set the reference position.
The following axes can be referenced with the parameter "markerSel":
● Using an individual reference switch
● Using the master reference switch
The "refMode" parameter can be used to specify the referencing type:
● Set reference position in the device/drive
● Set the reference position in the axis profile. A fixed offset between device/
  drive and axis profile remains
● Axes move only to the reference point, the user sets the reference

Drive:
To use this command, some parameters have to be set in the drive. Set the
parameters in the drive as follows for each drive:

  Control:
  A reference switch is required for this function.
  1. Adding an I/O device:

2. Configuration in the axis profile (this is an example of a use case):

Interface
PLC:

ML_AxsCtrlBasedGantryHoming
Name         Data type    Inherited      Address     Initial value   Comment
                          from

  Data       ML_AxsCtrl‐                                             Output: Command parame‐
BasedGantry‐                                            ters
HomingData
BOOL                                                    Returns information
ML_AxsCtrl‐                                                          whether the command can
BasedGantry‐                                                         be added to the axis
Homing                                                               object.
                                            ● TRUE: The command
                                              could be added success‐
                                              fully
                                            ● FALSE: An error
                                              occurred. Details in
                                              ML_oCmdResult
STRUCT ML_AxsCtrlBasedGantryHomingData
Name         Data type    Inher‐ Addres Initial      Comment
                          ited   s      value
                          from
  In         ML_iAxsCtrl‐                            Input: Command data of the command
             BasedGan‐
             tryHoming
  Out        ML_oCm‐                                 Output: Command parameters
             dResult
STRUCT ML_iAxsCtrlBasedGantryHoming EXTENDS ML_iAxsCtrlBasedHoming
Name          Data type  Inher‐    Addres Initial Comment
                         ited      s      value
                         from
  AxisName    STRING(15) ML                       Name of the axis used to execute the com‐
                         iAxscmd                  mand
                         Base
  Source      STRING(50) ML                       Specifies the command source, e.g PlcAp‐
                         iAxscmd                  plication1 is displayed in the diagnostic
                         Base                     messages
  SourceLine ULINT       ML                       Specifies the source line of the command;
                         iAxscmd                  is displayed in the diagnostic messages
                         Base
  NewRefPos LREAL        ML                       New reference point
                         iAxsCtrl‐
                         Base‐
                         dHomin
                         g

STRUCT ML_iAxsCtrlBasedGantryHoming EXTENDS ML_iAxsCtrlBasedHoming
   TravelDis‐  ML_Homi‐     ML                 Furthest travel distance to find the refer‐
tLimit         ngDirection iAxsCtrl‐           ence switch
             Base‐
             dHomin
             g
   HomingDir   ML_Homi‐     ML                 Homing direction, POSITIVE or NEGATIVE
ngRefType    iAxsCtrl‐
             Base‐
             dHomin
             g
   RefType     ML_iDynLi‐ ML                   Indicates which point was set as new ref‐
mits         iAxsCtrl‐          erence point, “STOPPED” or “MARKER”
             Base‐
             dHomin
             g
   DynLimits‐  ML_iDynLi‐ ML                   Fast velocity to find the reference mark
Forward        mits         iAxsCtrl‐
             Base‐
             dHomin
             g
   DynLimits‐  ML_iDynLi‐ ML                   Slow velocity to stop the axes
Backward       mits         iAxsCtrl‐
             Base‐
             dHomin
             g
   RefMode     ML_Homi‐     ML          SET_P Specifies which method should be used
ngRefMode iAxsCtrl‐      OS_DE to set the position, "SET_POS_DEVICE",
             Base‐       VICE   "SET_POS_PROFILE" or "SET_NONE".
             dHomin             Default is "SET_POS_DEVICE"
             g
   SlaveNum    UINT                            Slave numbers to be set
   SlaveParams POINTER TO                      Slave parameters
ML_iHoming‐
GantrySlave‐
Param
STRUCT ML_oCmdResult
Name       Data type       Inherited   Address      Initial value   Comment
                           from
   CmdID           ULINT                                            Command ID (is set to
                                                                    18446744073709551615 in
                                                                    the event of an error)
   Error           BOOL                                             Error ID TRUE indicates
                                                                    that an error occurred
   ErrorID         ULINT                                            Specifies the type of
                                                                    occurred error: The upper
                                                                    4 bits reflect the main diag‐
                                                                    nostics, the lower 4 bytes
                                                                    reflect the detailed diag‐
                                                                    nostics, 0 means no error

STRUCT ML_iHomingGantrySlaveParam
Name         Data type   Inher‐    Addres Initial   Comment
                         ited      s      value
                         from
  SlaveId    UINT        ML                         Slave axis ID
                         iAxscmd
                         Base
  NewRefPos LREAL        ML                         New reference point
                         iAxsCtrl‐
                         Base‐
                         dHomin
                         g

  MarkerSel  ML_Homi‐    ML                         Which reference point to use for homing
ngSlaveS‐   iAxsCtrl‐
witchSel    Base‐
     dHomin
     g

Data Layer:
Method: POST
URL:                https://<ip-addr>/automation/api/v2/nodes/motion/axs/
<axs_name>/cmd/ctrl-based-homing-gantry
Payload:

{
"type":"object","value":
       {
       "homingParam": {
          "newRefPos": 0,
          "travelDisLim": 10,
          "homingDir": "+",
          "refType": "STOPPED_POS",
          "dynForward": {
            "vel": 10,
            "acc": 10,
            "dec": 10,
            "jrkAcc": 0,
            "jrkDec": 0
       },
          "dynBackward":
       {
            "vel": 10,
            "acc": 10,
            "dec": 10,
            "jrkAcc": 0,
            "jrkDec": 0
       },
          "refMode": "SET_POS_DEVICE"
    },
       "homingSlaveParam": {
          "homingSlaveParamAll": [
        {
            "slaveId": 1,
            "newRefPos": 0,
            "markerSel": "MASTER_SWITCH"
        }

        ]
    }
}
}

Python:
Is not yet supported.

BundleIF:
//! @brief Create a motion command for gantry axes homing
(control based)
//!
//! @param[in] handle            Handle of the interface
//! @param[in] sourceInfo        Command source information
//! @param[in] axsName           Name of the motion object
//! @param[in] homingParam       Homing parameters of master
axis
//! @param[in] homingSlaveParam Homing parameters of slave
axes
//! @param[out] cmdID            The ID of the added command
//! @return                      Was everything okay?
motion::core::MotionResult(*axsCtrlBasedHomingGantryCmd)
(void* handle, const ::motion::core::dia::CmdSourceInfo
& sourceInfo, const char* axsName,
const ::motion::core::cmd::HomingParam& homingParam,
const std::vector<motion::core::cmd::HomingSlaveParam>&
homingSlaveParam, uint64_t& cmdID);

### 7.2.42 AxsAddToKin - Adding the axis to the kinematics

Basics
This command adds axes to a kinematics. The command does not trigger a
motion.
● Axes to be added to the kinematics have to be configured for this kine‐
   matics
● The axes have to be in status STANDSTILL
● The axis and the kinematics must not move
If the axis has been added to the kinematics successfully, the command
is set to DONE and the PLCOpen status of the axis changes to COORDI‐
NATED_MOTION.
ML_AxsGetPLCOpenState or ML_GetCmdState can be used to read the status.

PLC:

ML_AxsAddToKin
Name       Data type               Inherited   Address   Initial value   Comment
                                   from

ML_AxsAddToKin
  Data     ML_AxsAdd‐                                                Output: Command parame‐
ToKinData                                                 ters
BOOL                                                      Returns information
ML_AxsAdd‐                                                           whether the command can
ToKin                                                                be added to the axis
object.
● TRUE: The command
  could be added success‐
  fully
● FALSE: An error
  occurred. Details in

  ML_oCmdResult
STRUCT ML_AxsAddToKinData
Name       Data type   Inherited           Address   Initial value   Comment
                       from
  In       ML_iAxsAdd‐                                               Input: Command data of
           ToKin                                                     the command
  Out      ML_oCmdRe‐                                                Output: Command parame‐
           sult                                                      ters
STRUCT ML_iAxsAddToKin EXTENDS ML_iAxsCmdBase
Name        Data type   Inherited   Address   Initial value          Comment
                        from
  AxisName STRING(63) ML_iAxsCmd‐                                    Name of the axis used to
                        Base                                         execute the command
  Source    STRING(50) ML_iAxsCmd‐                                   Specifies the command
                        Base                                         source, e.g PlcApplication1
                                                                     is displayed in the diag‐
                                                                     nostic messages
  SourceLine ULINT           ML_iAxsCmd‐                             Specifies the source line of
                             Base                                    the command; is displayed
                                                                     in the diagnostic messages
  String‐     STRING(63)                                             Name of kinematics to
Name                                                                 which the axis is to be
                                                                     added to
  Buffered    BOOL                                                   TRUE, if the command is
                                                                     to be executed as a buf‐
                                                                     fered command, otherwise
                                                                     FALSE
STRUCT ML_oCmdResult
Name       Data type         Inherited     Address   Initial value   Comment
                             from
  CmdID       ULINT                                                  Command ID (is set to
                                                                     18446744073709551615 in
                                                                     the event of an error)
  Error       BOOL                                                   Error ID TRUE indicates
                                                                     that an error occurred

STRUCT ML_oCmdResult
  ErrorID  UDINT                                                       Specifies the type of
                                                occurred error: The upper
                                                4 bytes reflect the main
                                                diagnostics, the lower 4
                                                bytes reflect the detailed
                                                diagnostics, 0 means no
                                                error

Data Layer:
Method: POST
URL:               https://<ip-addr>/automation/api/v2/nodes/motion/axs/
<axs_name>/cmd/add-to-kin
Payload:

{
"type":"object","value":
{
  "kinName":"Kin1",
  "buffered":false
}
}

Python:
<cmdID> = motion.axs_cmd_add_to_kin( axs=<axsName>,
kin=<kinName> [,buffered=<buffered>] )

Creates an AddToKin command for a single axis (object has to be "attached"),
see documentation Python Runtime App ⮫ Python functions.
● <axsName> - string, axis object name
● <kinName> - string, kinematic object name
● <buffered> - bool, use TRUE if the command is to be buffered (TRUE by
  default)

BundleIF:
//! Create a add to kinematics command for a single axis
(AXS_CMD_ADDTOKIN)
//!
//! @param[in]     sourceInfo    Command source information
//! @param[in]     axsName       Name of the axis object
//! @param[in]     kinName       Name of the kinematics object
//! @param[in]     buffered      Is buffered mode?
//! @param[out]    cmdID         The ID of the added command
//! @return                      Was everything okay?
virtual MotionResult axsAddToKinCmd(const cmd::Cmd-SourceInfo&
sourceInfo, const char* axsName, const char* kinName, bool
buffered, uint64_t&cmdID) const = 0;

### 7.2.43 AxsRemoveFromKin - Removing the axis from the kinematics

Basics
This command removes an axis from the kinematics. The command does not
trigger a motion.

● The axis has to be in state COORDINATED_MOTION.
● The axis and the kinematics must not move.
If the axis has been removed from the kinematics successfully, the command
is set to DONE and the PLCOpen status of the axis is set to STANDSTILL.
Use ML_AxsGetPLCOpenState or ML_GetCmdState to read out the status.
This command is an unbuffered command, i.e. the previously active command
is canceled, the commands of the preparation buffer are discarded.

PLC:

ML_AxsRemoveFromKin
Name       Data type        Inherited    Address      Initial value   Comment
                            from
  Data      ML_AxsRe‐                                                 Output: Command parame‐
            moveFrom‐                                                 ters
            KinData
 ML_AxsRe‐ BOOL                                                       Returns information
moveFromKin                                                           whether the command can
                                                                      be added to the axis
                                                                      object.
                                                                      ● TRUE: The command
                                                                        could be added success‐
                                                                        fully
                                                                      ● FALSE: An error
                                                                        occurred. Details in
                                                                        ML_oCmdResult
STRUCT ML_AxsRemoveFromKinData
Name       Data type   Inherited         Address      Initial value   Comment
                       from
  In       ML_iAxsCmd‐                                                Input: Command data of
           Base                                                       the command
  Out      ML_oCmdRe‐                                                 Output: Command parame‐
           sult                                                       ters
STRUCT ML_iAxsCmdBase
Name        Data type       Inherited    Address      Initial value   Comment
                            from
  AxisName STRING(63)                                                 Name of the axis used to
                                                                      execute the command
  Source     STRING(50)                                               Specifies the command
                                                                      source, e.g PlcApplication1
                                                                      is displayed in the diag‐
                                                                      nostic messages
  SourceLine ULINT                                                    Specifies the source line of
                                                                      the command; is displayed
                                                                      in the diagnostic messages

STRUCT ML_oCmdResult
Name       Data type             Inherited   Address       Initial value   Comment
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

Data Layer:
Method: POST
URL:              https://<ip-addr>/automation/api/v2/nodes/motion/axs/
<axs_name>/cmd/rem-frm-kin
Payload: (blank)

Python:
<cmdID> =      motion.axs_cmd_remove_from_kin( axs=<axsName>)

Generates a RemoveFromKin command for a single axis (object has to be
"attached"), see documentation Python Runtime App ⮫ Python functions
● <axsName> - string, axis object name

BundleIF:
//! Create a remove from kinematics command for a single axis
(AXS_CMD_REMOVEFROMKIN)
//!
//! @param[in]     sourceInfo    Command source information
//! @param[in]     axsName       Name of the axis object
//! @param[out]    cmdID         The ID of the added command
//! @return                      Was everything okay?
virtual MotionResult axsRemoveFromKinCmd(const cmd::Cmd-
SourceInfo& sourceInfo, const char* axsName, uint64_t&cmdID)
const = 0;

### 7.2.44 AxsSetDriveFollowsMonitoring - Turning "Drive follows command

values" monitoring on or off
Basics
This command temporarily enables or disables the "Drive follows command
values" monitoring function.
For drives that are coupled to axes of ctrlX CORE via an axis profile, the
system cyclically monitors whether they are following the command value
input by the control (parameter P-0-0115 / 0x2802:02 "Axis status word," bit 3
"Status of external command processing").

If an "internal drive mode" is activated for such a drive (e.g., "Drive Halt”,
"drive-guided homing" ...), the ctrlX CORE executes a configurable error reac‐
tion (configuration options in the Cfg node of the axis: "NONE", "MESSAGE",
"WARNING", "SEVERE_ERROR").
See ⮫ Chapter 6.4.2 Drive does not follow the command values of the control
on page 321 for more information.
To temporarily disable or re-enable this error reaction when a "drive-internal
operating mode" is intentionally required, the "AxsSetDriveFollowsMonitoring"
command can be used to disabled or re-enable the ctrlX CORE monitoring.
Use case:
● Disabling the configured monitoring. Call "AxsSetDriveFollowsmonitoring"
   with the option "false"

● Selecting the drive's internal operation mode, e.g., "Drive Halt"
● Exiting the drive's internal operation mode
● Enabling the configured monitoring: Call "AxsSetDriveFollowsMonitoring"
   with the option "true"
After an axis reset or after switching from the "Configuration" state to the
"Operation" state, the configured monitoring is reactivated.

PLC:

ML_AxsSetDriveFollowsMonitoring
Name           Data type              Inherited Address   Initial      Comment
                                      from                value
  Data         ML_AxsSetDriveFol‐                                      Output: Command parame‐
               lowsMonitoringData                                      ters
  AxsSetDrive‐ BOOL                                                    Returns information
FollowsMoni‐                                                           whether the command can
toring                                                                 be added to the axis
                                                                       object.
                                                                       ● TRUE: The command
                                                                         could be added success‐
                                                                         fully
                                                                       ● FALSE: An error
                                                                         occurred. Details in
                                                                         ML_oCmdResult
STRUCT ML_AxsSetDriveFollowsMonitoringData
Name       Data type        Inherited Address          Initial value   Comment
                            from
  In       ML_iAxsSetDrive‐                                            Input: Command data of
           FollowsMonitor‐                                             the command
           ingData
  Out      ML_oCmdResult                                               Output parameter of the
                                                                       command

STRUCT ML_iAxsSetDriveFollowsMonitoringData EXTENDS ML_iAxsCmdBase
Name         Data type   Inherited    Address     Initial value Comment
                         from
  AxisName STRING(63) ML_iAxsCmd‐                               Name of the axis used to
                         Base                                   execute the command
  Source     STRING(50) ML_iAxsCmd‐                             Specifies the command
                         Base                                   source, e.g PlcApplication1
                                                                is displayed in the diag‐
                                                                nostic messages
  SourceLine ULINT       ML_iAxsCmd‐                            Specifies the source line of
                         Base                                   the command; is displayed
                                                                in the diagnostic messages
  SwitchOn BOOL                                                 TRUE indicates: Monitoring
                                                                is enabled; FALSE indi‐
                                                                cates: Monitoring is turned
                                                                off
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
URL:               https://<ip-addr>/automation/api/v2/nodes/motion/axs/
<axs_name>/cmd/set-monitoring-of-drive-follows-cmd-values
Payload:

{
"type":"object","value":
{

}
}

Python:
<cmdID> = axs_cmd_set_drive_follows_monitoring(axs: str,
switch_on: bool = True)

Generates a command for an axis to enable or disable monitoring of the
"drive-follows-command-values" flag.
This is always a non-buffered command (the object has to be "attached"); see
the documentation on Python Runtime App ⮫ Python Functions.

● <axsName> - string, axis object name
● <switchOn> - Do you want to switch on monitoring?
● <cmdID>
  The returned command identification (can be used to query the state of the
  command, see ⮫ GetCmdState)

BundleIF:
//! Create a command to switch the monitoring of the "drive-
follows-command-values" flag on or off
//!
/// After an axis reset or the switch to operation, the
monitoring is switched on by default.

/// The command becomes effective at once. Requesting the
command state will always return DONE.
///
/// @param[in]     handle       Handle of the interface
/// @param[in]     sourceInfo   Command source information
/// @param[in]     axsName      Name of the motion object
/// @param[in]     switchOn     switch on or off?
/// @param[out]    cmdID        The ID of the added command
/// @return                     Status of the function call:
STS_OK or an error code on failure.

MotionResult(*axsSetDriveFollowsMonitoringCmd)(void* handle,
const ::motion::core::dia::CmdSourceInfo& sourceInfo, const
char* axsName, bool switchOn, std::uint64_t& cmdID);
