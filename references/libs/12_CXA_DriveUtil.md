# 12 CXA_DriveUtil

## 12.1 Introduction and overview

Target systems
The library CXA_DriveUtil.library includes function blocks to control drives,
frequency converters and supply units.

Overview on the library content
● "PowerSupply” folder:
Function blocks to control supply units with EtherCAT SoE.
Table 79: Fields of application and function blocks of CXA_DriveUtil, folder "PowerSupply"
Field of application (folder in library)
Function blocks/functions/data types              Description
Power supply (PowerSupply/POUs)
⮫ MB_PowerSupplyDriveIntegrated                   The function block MB_PowerSupplyDriveInte‐
                                                  grated can identify the internal power supply
                                                  state, handle the transitions between the power
                                                  supply states, set the power supply into the

required state and control the operation mode.
⮫ MB_ECATSoEPowerSupplyStandalone                 The function of the function block MB_ECAT‐
SoEPowerSupplyStandalone corresponds to
MB_PowerSupplyDriveIntegrated. The function
block can also reset a power supply error and
provide diagnostic information on the power
supply state.
⮫ MB_ECATSoEPowerSupplyDcDcIslandGrid             The MB_ECATSoEPowerSupplyDcDcIslandGrid
function block monitors and controls a supply
unit.
Data types (PowerSupply/DUTs):
(For information on the data structures, refer to the ctrlX PLC Engineering library manager in the
library CXA_DriveUtil in the folder PowerSupply/DUTs)
MB_POWERSUPPLY_ACTUAL_MODE                         Enumeration of the state machine states of a
 power supply
MB_POWERSUPPLY_ERROR_MODE                          Enumeration to which state the power supply
 switches to when exiting an internal error state
MB_POWERSUPPLY_MODE                                Enumeration of the operation modes of the
 power supply
MB_POWERSUPPLY_TARGET_MODE                         Enumeration of the available target modes
 for the function blocks MB_PowerSupplyDriveIn‐
 tegrated and MB_ECATSoEPowerSupplyStand‐
 alone. The target mode decides on the final
 state to be reached by the power supply as well
 as on the path to be traveled to reach the final
 state
MB_PS_TARGET_MODE_DC_DC_ISLAND_GRID                Enumeration of the available target modes
 for the function block MB_ECATSoEPowerSup‐
 plyDcDcIslandGrid. The target mode decides on
 the final state to be reached by the power
 supply as well as on the path to be traveled to
 reach the final state
MB_POWERSUPPLY_FUNCTION                            Enumeration of the extended supply unit func‐
 tions for the function block MB_ECATSoEPower‐
 SupplyDcDcIslandGrid
● "FreqConv” folder:
Function blocks to control Rexroth frequency converters EFC via EtherCAT
SoE.
Table 80: Fields of application and function blocks of CXA_DriveUtil, folder "FreqConv"
Field of application (folder in library)
Function blocks/functions/data types              Description

Control frequency converter (FreqConv/POUs)
MB_ECATCoEFreqConv mode FreqConv/POUs/sub_FreqConv:
⮫ MB_ECATCoEFreqConv                               The function block MB_ECATCoEFreqConv con‐
trols the Rexroth frequency converter EFC via
Ethercat CoE.
⮫ MB_ECATCoEFreqConvCtrlWordEnCoding               The     MB_ECATCoEFreqConvCtrlWordEnCoding
function generates the control word for the
Rexroth frequency converter EFC via Ethercat
CoE.
MB_ECATCoE402FreqConv mode (FreqConv/POUs/sub_402ctrlMode):
⮫ MB_ECATCoE402FreqConv                            The function block MB_ECATCoE402FreqConv
controls the Rexroth frequency converter EFC via
Ethercat CoE.
⮫ MB_ECATCoEFreqConv402CtrlWordEnCoding The                   MB_ECATCoEFreqConv402CtrlWordEn‐
Coding      function     controls   the       Freq‐
Conv402CtrlWord. It converts the operating
state of the EFC to the control word in bits.
MB_ECATCoETorque mode (FreqConv/POUs/sub_TorqueCtrl):
⮫ MB_ECATCoETorque                                 The function block MB_ECATCoETorque controls
the Rexroth frequency converter EFC via Ethercat
CoE.
⮫       MB_ECATCoEFreqConvTorqueCtrlWordEn‐ The            MB_ECATCoEFreqConvTorqueCtrlWordEn‐
Coding                                             Coding function computes FreqConvCtrlWord. It
converts the operating state of the EFC to the
control word in bits.
MB_ECATCoEFreqConv_FnT mode (FreqConv/POUs/sub_FnT):
⮫ MB_ECATCoEFreqConv_FnTe                          The function block MB_ECATCoEFreqConv_FnT to
control the Rexroth frequency converter EFC via
Ethercat CoE.
⮫ MB_ECATCoEFreqConvCtrlWordEnCoding_FnT The                      MB_ECATCoEFreqConvCtrlWordEn‐
Coding_FnT function computes FreqConvCtrl‐
Word. It converts the operating state of the EFC
into the control word in bits.
Data types (FreqConv/DUTs):
(For information on the data structures, refer to the ctrlX PLC Engineering library manager in the
library CXA_DriveUtil in the folder FreqConv/DUTs)
MB_FreqConvCtrlWord_bits
MB_FreqConvCtrlWord_Union
MB_FreqConvStatusWord_Bits
MB_FreqConvStatusWord_Union
MB_FREQCONV_OPMODE
MB_FREQCONV_OPSTATE
MB_FreqConv402CtrlWord_bits
MB_FreqConv402CtrlWord_Union
MB_FreqConv402StatusWord_Bits
MB_FreqConv402StatusWord_Union
MB_FREQCONV402_OPMODE
MB_FREQCONV402_OPSTATE

## 12.2 PowerSupply

### 12.2.1 Introduction and overview

The PowerSupply function blocks control the power supply. EtherCAT is used
to communicate between the control and the power supply. These function
blocks can identify the internal status of the power supply. Additionally, they
are responsible for a smooth transition between the state machines of the
power supply. They also set the power supply to its required state, control
the operation mode, delete the power supply fault and retrieve the diagnostic
information of the power supply.
The following rules apply when using function blocks for the power supply:
● If the ctrlX CORE controls an inverter containing a drive and the required

   power supply (e.g. XCS) and if this inverter is connected to the Motion
   (i.e. an inverter axis is connected to an axis profile), the function block
   MB_PowerSupplyDriveIntegrated is used
● If an alternative field bus is used instead of a ctrlX CORE, the field bus-
   independent function block MB_PowerSupplyDriveIntegrated can be used
● In all other cases, use the function block MB_ECATSoEPowerSupplyStand‐
   alone
If the power supply XVR is for example connected to a ctrlX CORE, use
the function block MB_ECATSoEPowerSupplyStandalone. MB_ECATSoEPower‐
SupplyStandalone is normally the most frequently used function block. In
addition to the power supply control, this function block also checks the
availability of the device at the bus. It is provided with an output that issues
the device state at the bus and provides an input to clear the error.
The following figure shows the state machine of a back-feeding supply unit
controlled by the function blocks of the supply unit.

For more information, refer to the documentation “ctrlX DRIVE Runtime, Appli‐
cation Manual” "AXS-V-02 Functions", DOK-XDRV**-AXS-02VRS**-APRS-EN-P.

### 12.2.2 MB_PowerSupplyDriveIntegrated

Brief description
The MB_PowerSupplyDriveIntegrated function block monitors and controls a
supply unit.
Data is exchanged via any field bus between the function block and the supply
unit.
The function block can identify the internal supply unit state, trigger the tran‐
sitions of the supply unit state machine, set the supply unit into the required
state and control the operation mode.
The function block continuously monitors the status word InProcStatus of
the supply unit and updates the control word OutProcCtrl of the supply unit
based on the inputs assignment.

Interface description

Table 81: Interface variables of the MB_PowerSupplyDriveIntegrated function block
                Name                     Type                                  Comment

VAR_INPUT       Enable                   BOOL                                  Processing enabled (cyclic, state-controlled)

TargetMode               MB_POWERSUPPLY_TARGET_MODE            Target mode to be reached by the supply unit

OperationModeSelection   MB_POWERSUPPLY_MODE                   Operation mode of supply unit

ErrorMode                MB_POWERSUPPLY_ERROR_MODE             Error at the transition handling input for the
                                                               supply unit

Timeout                  TIME                                  Max. permitted time of each ActualMode -> Tar‐
                                                               getMode

VAR_IN_OUT
CONSTANT

InProcStatus             WORD                                  Status     word      of   the   supply   unit   S-0-2058
                                                               (S-0-1720.0.2)

VAR_OUTPUT      InOperation              BOOL                                  The function block operates correctly. Output
                                                               data is valid

Error                    BOOL                                  Indicates that an error occurred (see ErrorID and
                                                               ErrorIdent)

ErrorID                  ⮫ ERROR_CODE                          Error cause

ErrorIdent               ⮫ ERROR_STRUCT                        Detailed error cause

ActualMode               MB_POWERSUPPLY_ACTUAL_MODE            Initial state of the state machine of the supply
                                                               unit

OperationModeStatus      MB_POWERSUPPY_MODE                    Actual operation mode of the supply unit

PowerSupplyError         BOOL                                  Internal supply unit error

PowerSupplyWarning       BOOL                                  Internal supply unit warning

VAR_IN_OUT

OutProcCtrl              WORD                                  Supply        unit        control    word       S-0-2057
                                                               (S-0-1720.0.1)

Table 82: Min./max. and default values and use of the MB_PowerSupplyDriveIntegrated function
block inputs
Name                      Type                            Min.    Max.    Default value                                 Application
                                                          value   value

Enable                    BOOL                                            FALSE                                         Continuous

TargetMode                MB_POWERSUPPLY_TARGET_MODE                      MAINS_OFF_NO_DISCHARGE                        Continuous

OperationModeSelection    MB_POWERSUPPLY_MODE                             OPERATIONMODE1                                Continuous

ErrorMode                 MB_POWERSUPPLY_ERROR_MODE                       ERROR_TRANSITION_NO_DISCHARGE Continuous

Name                 Type                         Min.    Max.    Default value           Application
                             value   value

Timeout              TIME                         N. def. N.      T#10s                   Continuous
                                     def.

InProcStatus         WORD                         N. def. N.      -                       Continuous
                                     def.

Functional description
The function block monitors and controls the supply unit. The function block
can implement different supply unit functions specified in the supply unit
control word.
The main task of the function block is to execute a state transition of the
supply unit to the target mode.
The cyclic data exchange between the function block and the supply unit is
described in the following.
● InProcStatus – Updates to S-0-2057 (supply unit status word S-0-1720.0.2)
● OutProcCtrl – Updates to S-0-2058 (supply unit control word S-0-1720.0.1)
For a general description of the internal state machine of the supply unit, refer
to the documentation of the ctrlX DRIVE supply unit functions.

The function block uses this status word to identify the current state of the
state machine of the supply unit.
The target mode to be reached by the state machine of the supply unit is
at the TargetMode input. The function block executes the transition to Target‐
Mode by controlling the internal state machine of the supply unit.
In case of a function block error, the state handling is stopped and the error is
cleared.

If the supply unit goes into error state, the target and error mode decide on
the next state of the supply unit.
Contradictory input combinations can result between ErrorMode and Target‐
Mode.
In these cases, TargetMode dominates, irrespective of the ErrorMode input
value.
See the following example.
−   ActualMode = _ERROR
−   TargetMode = DC_POWER_OFF_NO_DISCHARGE
−   ErrorMode = ERROR_TRANSITION_DISCHARGE
If the supply unit leaves the Error state, it is required for the TargetMode that
the supply unit goes into the DC Power OFF state without discharging the DC
bus.
For ErrorMode, the supply unit has to discharge the DC bus before switching
into the next state.
In this case, TargetMode dominates and the supply unit is switched to mode
DC Power Off without discharging the DC bus.
This has to be considered by the programmer when programming the applica‐
tion.
The time - which the supply unit needs to reach the target mode (from the
current mode) - is monitored.
If the time expires, the Timeout input reports an error and the state machine
handling is stopped.
If the Enable input of the function block is reset, the function block detects
the current supply unit state and decides whether it is requires to switch off
the supply unit (DC).
The OperationModeSelection input is immediately and continuously displayed
on bits 8 and 9 of the control word.
The InProcStatus input refreshes the function block outputs during each PLC
scan. Each status word change is immediately output at the outputs.
The outputs Error, ErrorID and ErrorIdent contain the error information.

Troubleshooting
The function block can go into an error state due to invalid inputs or an
expired timeout timer. In both cases, the function block reports an error and
cancels the operation.
The user can troubleshoot the error cause, reset the Enable input and set the
input again (standard procedure when resetting errors).
The function block continues. Refer to the following tables for available error
codes.
The function block can generate the following error codes:

Table 83: Error codes of the MB_PowerSupplyDriveIntegrated function block
ErrorID                       Additional1     Additional2      Description
INPUT_INVALID_ERROR           16#0A0F010A     16#0C230201      TargetMode input is invalid (see
                                                               MB_POWERSUPPLY_TARGET_MODE)
INPUT_INVALID_ERROR           16#0A0F010A     16#0C230202      OperationModeSelection
                                                               input        invalid        (see
                                                               MB_POWERSUPPLY_MODE)
INPUT_INVALID_ERROR           16#0A0F010A     16#0C230203      ErrorMode input is invalid (see
                                                               MB_POWERSUPPLY_ERROR_MODE)

ErrorID                      Additional1     Additional2      Description
STATE_MACHINE_ERROR          16#0A0F010A     16#0C230204      Timeout (actual mode -> target
                                         mode)
STATE_MACHINE_ERROR          16#0A0F010A     16#0C230205      ActualMode        of       the
                                         device      is  invalid   (see
                                         MB_POWERSUPPLY_ACTUAL_MODE)

Use case with MB_PowerSupplyDriveIntegrated
Two IndraDrive XMS are connected to one IndraDrive XCS with integrated
supply unit.
Use the function block MB_PowerSupplyDriveIntegrated to control the supply

unit XCS. The inverters XMS are enabled using the outputs of this function
block (switched from “bb” to “Ab”).

Prerequisite: The supply unit in the XCS is configured to “External activation
via field bus”.

The following parameters have to be configured cyclically for the XCS:
● MDT: S-0-2057 (S-0-1720.0.1), “Supply unit control word"
● AT: S-0-2058 (S-0-1720.0.2), "Power supply status word”
The following parameters are cyclically configured for the XMS drives:
● MDT: S-0-0240, "DC bus power control”
● AT: P-0-0115, "Device control: Status word”
This example code is also included in the CXA_DriveUtil library.

Variable definition

fbMB_PowerSupply: MB_PowerSupplyDriveIntegrated;
bEnablePower: BOOL :=FALSE;

wXCSPowerSupplyStatus:   WORD;   // S-0-2058 [S-0-1720.0.02] of XCS (Power Supply Status Word)
        // must be configured in AT of slave configuration
wXCSPowerSupplyControl: WORD;    // S-0-2057 [S-0-1720.0.01] of XCS (Power Supply Control Word)
        // must be configured in MDT of slave configuration.

wXMS1DeviceStatus: WORD;      // P-0-0115 of XMS1 (Device control: status word)
     // must be configured in AT of slave configuration.
wXMS1DCBusPowerControl: WORD; // S-0-0240 of XMS1 (DC Bus Power Control)
     // must be configured in MDT of slave configuration.
wXMS2DeviceStatus: WORD;      // P-0-0115 of XMS2 (Device control: status word)
     // must be configured in AT of slave configuration.
wXMS2DCBusPowerControl: WORD; // S-0-0240 of XMS2 (DC Bus Power Control)
     // must be configured in MDT of slave configuration.

Called cyclically

// Check that all devices are ready for operation ("bb"-relais is closed)
IF (wXMS1DeviceStatus.0 AND wXMS2DeviceStatus.0) AND bEnablePower THEN
  // switching direct to OPERATION_MODE when drives are ready
  fbMB_PowerSupply.TargetMode := MB_POWERSUPPLY_TARGET_MODE.OPERATION_MODE;
ELSE
  // switching OFF when drives are not ready or bEnablePower is FALSE
  fbMB_PowerSupply.TargetMode := MB_POWERSUPPLY_TARGET_MODE.MAINS_OFF_NO_DISCHARGE;
END_IF
fbMB_PowerSupply(
  Enable:= bEnablePower OR (fbMB_PowerSupply.ActualMode <> MB_POWERSUPPLY_ACTUAL_MODE.MAINS_OFF),
  TargetMode:= ,
  OperationModeSelection:= ,
  ErrorMode:= ,
  Timeout:= ,

  InProcStatus:= wXCSPowerSupplyStatus,
  OperationModeStatus=> ,
  PowerSupplyError=> ,
  PowerSupplyWarning=> ,
  OutProcCtrl:= wXCSPowerSupplyControl);
IF fbMB_PowerSupply.Error THEN
  bEnablePower := FALSE;
  // add your error handling here: e.g. mSetError(fbMB_PowerSupply.ErrorID, fbMB_PowerSupply.ErrorIdent);
END_IF;
// copy output of FB to DC Bus Power Control, bit 0 of all XMS
IF fbMB_PowerSupply.ActualMode = MB_POWERSUPPLY_ACTUAL_MODE.OPERATION_MODE THEN
  // activate power in DC Bus Power Control
  wXMS1DCBusPowerControl.0 := TRUE; // axis 1 (XMS1)
  wXMS2DCBusPowerControl.0 := TRUE; // axis 2 (XMS2)
ELSE
  // switch off power in DC Bus Power Control
  wXMS1DCBusPowerControl.0 := FALSE; // axis 1 (XMS1)
  wXMS2DCBusPowerControl.0 := FALSE; // axis 2 (XMS2)

END_IF

For facilitation purposes, it is directly switched to OPERATION_MODE in this
example when the supply unit is ready. For interim states, see Fig. 128.

Use case: Automatic without MB_PowerSupplyDriveIntegrated

drives
Instead of enabling the supply unit using the function block MB_PowerSupply‐
DriveIntegrated, the automatic start of the supply unit can be used.
Select the option “if in OM”, then auto soft start in the dialog Configuration of
the integrated supply unit.

For the XCS, it is sufficient to configure bit 15 “Enabling” of the parameter
S-0-2058, “Power supply status word” into the signal status word. For the
XMS drives, bit 0 of the parameter S-0-0240 "DC bus power control" can be
configured into the signal control word.
It is assumed in the following programming example that the complete param‐
eter S-0-2058 is configured in the AT and that S-0-0240 is configured in the
MDT.
In the PLC, bit 15 of S-0-2058, “Supply unit status word” is copied from the
XCS to bit 0 of the parameter S-0-0240 "DC bus power control” of all XMS
drives.

Variable definition

wXCSPowerSupplyStatus:   WORD;   // S-0-2058 [S-0-1720.0.02] of XCS (Power Supply Status Word)
        // must be configured in AT of slave configuration

wXMS1DCBusPowerControl: WORD; // S-0-0240 of XMS1 (DC Bus Power Control)
     // must be configured in MDT of slave configuration.
wXMS2DCBusPowerControl: WORD; // S-0-0240 of XMS2 (DC Bus Power Control)
     // must be configured in MDT of slave configuration.

Called cyclically

// copy bit of XCS status word to DC Bus Power Control, bit 0 of all XMS
wXMS1DCBusPowerControl.0 := wXCSPowerSupplyStatus.15; // axis 1 (XMS1)
wXMS2DCBusPowerControl.0 := wXCSPowerSupplyStatus.15; // axis 2 (XMS2)

### 12.2.3 MB_ECATSoEPowerSupplyStandalone

Brief description
The MB_ECATSoEPowerSupplyStandalone function block monitors and con‐
trols a supply unit.
Data is exchanged via the EtherCAT field bus between the function block and
the supply unit.
The function block can identify the internal supply unit state, trigger the tran‐
sitions of the supply unit state machine, set the supply unit into the required
state and control the operation mode.
The function block continuously monitors the status word InProcStatus of
the supply unit and updates the control word OutProcCtrl of the supply unit
based on the inputs assignment.

Interface description

Table 84: Interface variables of the MB_ECATSoEPowerSupplyStandalone function block
                 Name                     Type                                Comment

VAR_INPUT        Enable                   BOOL                                Processing enabled (cyclic, state-controlled)

MasterName               POINTER TO STRING                   Instance name of the field bus master. If multiple mas‐
                                                             ters are simultaneously operated on the control, they
                                                             are distinguished by the “MasterName” input variable.
                                                             An internal variable ‘ethercatmaster’ is assigned to the
                                                             input by default and does thus not have to be assigned.

SlaveAddress             UINT                                Ethercat address of the slave node, e.g. 1001

TargetMode               MB_POWERSUPPLY_TARGET_MODE          Target mode to be reached by the supply unit

OperationModeSelection MB_POWERSUPPLY_MODE                   Operation mode of supply unit

ErrorMode                MB_POWERSUPPLY_ERROR_MODE           Error at the transition handling input for the supply unit

Timeout                  TIME                                Max. permitted time of each ActualMode -> TargetMode

ClearError               BOOL                                Clearing an error in the drive using the “Clear error”
                                                             command S-0-0099. After clearing, activate the selected
                                                             enabling.

VAR_IN_OUT
CONSTANT

InProcStatus             WORD                                Status word of the supply unit S-0-2058 (S-0-1720.0.2)

VAR_OUTPUT       InOperation              BOOL                                The function block operates correctly. Output data is
                                                             valid

Error                    BOOL                                Indicates that an error occurred (see ErrorID and ErrorI‐
                                                             dent)

ErrorID                  ⮫ ERROR_CODE                        Error cause

ErrorIdent               ⮫ ERROR_STRUCT                      Detailed error cause

ActualMode               MB_POWERSUPPLY_ACTUAL_MODE          Initial state of the state machine of the supply unit

OperationModeStatus      MB_POWERSUPPLY_MODE                 Actual operation mode of the supply unit

PowerSupplyError         BOOL                                Internal supply unit error

PowerSupplyWarning       BOOL                                Internal supply unit warning

ClearErrorAck            BOOL                                Confirmation that the command “Clear error” S-0-0099
                                                             was executed successfully

State                    ⮫ IL_ECAT_STATE                     Device status from ⮫ IL_ECATRemoteSlaveGetDevState

VAR_IN_OUT

OutProcCtrl              WORD                                Supply unit control word S-0-2057 (S-0-1720.0.1)

Table 85: Min./max. and default values and the                                 application           of    the   inputs       of      the
MB_ECATSoEPowerSupplyStandalone function blocks
Name                      Type                              Min.      Max.     Default value                             Application
                                                            value     value

Enable                    BOOL                                                 FALSE                                     Continuous

MasterName                POINTER TO STRING                 N. def.   N. def. 'ethercatmaster'

SlaveAddress              UINT                              0         N. def. 0

TargetMode                MB_POWERSUPPLY_TARGET_MODE                           MAINS_OFF_NO_DISCHARGE                    Continuous

OperationModeSelection MB_POWERSUPPLY_MODE                                     OPERATIONMODE1                            Continuous

ErrorMode                 MB_POWERSUPPLY_ERROR_MODE                            ERROR_TRANSITION_NO_DISCHARGE             Continuous

ClearError                BOOL                                                 FALSE                                     Continuous

Timeout                   TIME                              N. def.   N. def. T#10s                                      Continuous

InProcStatus              WORD                              N. def.   N. def. -                                          Continuous

Functional description
The function block monitors and controls the supply unit. The function block
can implement different supply unit functions specified in the supply unit
control word.
The main task of the function block is to execute a state transition of the
supply unit to the target mode.
The cyclic data exchange between the function block and the supply unit is
described in the following.
● InProcStatus – Updates to S-0-2058 (supply unit status word S-0-1720.0.2)
● OutProcCtrl – Updates to S-0-2057 (supply unit control word S-0-1720.0.1)
For a general description of the internal state machine of the supply unit, refer
to the documentation of the ctrlX DRIVE supply unit functions.

The function block uses this status word to identify the current state of the
state machine of the supply units.
The target mode to be reached by the state machine of the supply unit is
already available at the TargetMode input.
The traveled path to reach the target mode is known to the function block.
Thus, the function block triggers the supply unit transition to the next imme‐
diate state. This transition to the next immediate state continues until the
supply unit has reached the target mode after different states.

In case of a function block error, the state handling is stopped and the error is
cleared.
If the supply unit goes into error state, the target and error mode decide on
the next state of the supply unit.
Contradictory input combinations can result between ErrorMode and Target‐
Mode.
In these cases, TargetMode dominates, irrespective of the ErrorMode input
value.
See the following example.
−   ActualMode = _ERROR
−   TargetMode = DC_POWER_OFF_NO_DISCHARGE
−   ErrorMode = ERROR_TRANSITION_DISCHARGE
If the supply unit leaves the Error state, it is required for the TargetMode that
the supply unit goes into the DC Power OFF state without discharging the DC
bus.
For ErrorMode, the supply unit has to discharge the DC bus before switching
into the next state.
In this case, TargetMode dominates and the supply unit is switched to mode
DC Power Off without discharging the DC bus.
This has to be considered by the programmer when programming the applica‐
tion.
The time - which the supply unit needs to reach the target mode (from the
current mode) - is monitored.
If the time expires, the Timeout input reports an error and the state machine
handling is stopped.
If the Enable input of the function block is reset, the function block detects
the current supply unit state and decides whether it is required to switch off
the supply unit (DC).
In this case, the control word is set to set the supply unit to DC Power Off
mode (if required).
The outputs Error, ErrorID and ErrorIdent contain the error information.
The operation mode selection input is immediately and continuously displayed
on bits 8 and 9 of the control word. The InProcStatus input refreshes the
function block outputs during each PLC scan. Each status word change is
immediately output at the outputs.
Furthermore, a supply unit error can be cleared via the ClearError input. The
rising edge of this input triggers the “Clear error” command S-0-0099 for
the supply unit. The status of a successfully cleared error is output via the
ClearErrorAck output of the function block.
The diagnostic information on the supply unit is continuously updated at the
State function block output. The ⮫ IL_ECATRemoteSlaveGetDevState function
block performs the update.

Troubleshooting
The function block can go into an error state due to invalid inputs or an
expired timeout timer. In both cases, the function block generates an error
and cancels the operation.
The user can troubleshoot the error cause, reset the Enable input and set the
input again (standard procedure when resetting errors).
The function block continues. Refer to the following tables for available error
codes.

In addition to the errors of the internally used function blocks IL_ECATSoe‐
Command⮫ IL_ECATSoeCommand and ⮫ IL_ECATRemoteSlaveGetDevState, the
function block can generate the following error codes:

Table 86: Error codes of the MB_ECATSoEPowerSupplyStandalone function block
ErrorID                      Additional1      Additional2 Description
INPUT_INVALID_ERROR          16#0A0F010A      16#0C230201 TargetMode input is invalid (see
                                                          MB_POWERSUPPLY_TARGET_MODE)
INPUT_INVALID_ERROR          16#0A0F010A      16#0C230202 OperationModeSelection
                                                          input          invalid       (see
                                                          MB_POWERSUPPLY_MODE)
INPUT_INVALID_ERROR          16#0A0F010A      16#0C230203 ErrorMode input is invalid (see

                                     MB_POWERSUPPLY_ERROR_MODE)
STATE_MACHINE_ERROR          16#0A0F010A      16#0C230204 Timeout (actual mode -> target
                                     mode)
STATE_MACHINE_ERROR          16#0A0F010A      16#0C230205 ActualMode            of      the
                                     device      is      invalid  (see
                                     MB_POWERSUPPLY_ACTUAL_MODE)
INPUT_INVALID_ERROR          16#0A0F010A      16#0C230206 Reference of the MasterName input
                                     is invalid

Use case with MB_ECATSoEPowerSupplyStandalone
Two IndraDrive XMS are connected to one XVR supply unit.
Use the function block MB_ECATSoEPowerSupplyStandalone to control the
supply unit XVR. The drives at the inverters XMS are enabled using the out‐
puts of this function block (switched from “bb” to “Ab”).

The following parameters have to be configured cyclically for the XVR:
● MDT: S-0-2057 (S-0-1720.0.1), “Supply unit control word"
● AT: S-0-2058 (S-0-1720.0.2), "Power supply status word”
The following parameters are cyclically configured for the XMS drives:
● MDT: S-0-0240, "DC bus power control”
● AT: P-0-0115, "Device control: Status word”
This example code is also included in the CXA_DriveUtil library.

Variable definition

 fbMB_PowerSupply: MB_ECATSoEPowerSupplyStandAlone;
 bEnablePower: BOOL :=FALSE;

 wXVRPowerSupplyStatus:    WORD;   // S-0-2058 [S-0-1720.0.02] of XVR (Power Supply Status Word)
         // must be configured in AT of slave configuration
 wXVRPowerSupplyControl: WORD;     // S-0-2057 [S-0-1720.0.01] of XVR (Power Supply Control Word)
         // must be configured in MDT of slave configuration.

 wXMS1DeviceStatus: WORD;      // P-0-0115 of XMS1 (Device control: status word)
     // must be configured in AT of slave configuration.
 wXMS1DCBusPowerControl: WORD; // S-0-0240 of XMS1 (DC Bus Power Control)
     // must be configured in MDT of slave configuration.
 wXMS2DeviceStatus: WORD;      // P-0-0115 of XMS2 (Device control: status word)
     // must be configured in AT of slave configuration.
 wXMS2DCBusPowerControl: WORD; // S-0-0240 of XMS2 (DC Bus Power Control)
     // must be configured in MDT of slave configuration.

Called cyclically

// Check that all devices are ready for operation ("bb"-relais is closed)
IF (wXMS1DeviceStatus.0 AND wXMS2DeviceStatus.0) AND bEnablePower THEN
  // switching direct to OPERATION_MODE when drives are ready
  fbMB_PowerSupply.TargetMode := MB_POWERSUPPLY_TARGET_MODE.OPERATION_MODE;
ELSE
  // switching OFF when drives are not ready or bEnablePower is FALSE
  fbMB_PowerSupply.TargetMode := MB_POWERSUPPLY_TARGET_MODE.MAINS_OFF_NO_DISCHARGE;
END_IF
fbMB_PowerSupply(
  Enable:= bEnablePower OR (fbMB_PowerSupply.ActualMode <> MB_POWERSUPPLY_ACTUAL_MODE.MAINS_OFF),
  MasterName:= ,
  SlaveAddress:= 1001,
  TargetMode:= ,
  OperationModeSelection:= ,
  ErrorMode:= ,
  Timeout:= ,
  ClearError:= ,
  InProcStatus:= wXVRPowerSupplyStatus,

  OperationModeStatus=> ,
  PowerSupplyError=> ,
  PowerSupplyWarning=> ,
  ClearErrorAck=> ,
  State=> ,
  OutProcCtrl:= wXVRPowerSupplyControl);
IF fbMB_PowerSupply.Error THEN
  bEnablePower := FALSE;
  // add your error handling here: e.g. mSetError(fbMB_PowerSupply.ErrorID, fbMB_PowerSupply.ErrorIdent);
END_IF;
// copy output of FB to DC Bus Power Control, bit 0 of all XMS
IF fbMB_PowerSupply.ActualMode = MB_POWERSUPPLY_ACTUAL_MODE.OPERATION_MODE THEN
  // activate power in DC Bus Power Control
  wXMS1DCBusPowerControl.0 := TRUE; // axis 1 (XMS1)
  wXMS2DCBusPowerControl.0 := TRUE; // axis 2 (XMS2)
ELSE
  // switch off power in DC Bus Power Control
  wXMS1DCBusPowerControl.0 := FALSE; // axis 1 (XMS1)
  wXMS2DCBusPowerControl.0 := FALSE; // axis 2 (XMS2)
END_IF

For facilitation purposes, it is directly switched to OPERATION_MODE in this
example when all drives are ready. For interim states, see Fig. 133.

### 12.2.4 MB_ECATSoEPowerSupplyDcDcIslandGrid

Brief description
The MB_ECATSoEPowerSupplyDcDcIslandGrid function block monitors and
controls a supply unit using one of the following functions:
● XMV -> "DC-DC converter” for the DC-DC converter mode
● XVR -> “Mains function" - Regenerative supply unit in island grid mode
Data is exchanged via the EtherCAT field bus between the function block and
the supply unit.
The function block can identify the internal supply unit state, trigger the tran‐
sitions of the supply unit state machine, set the supply unit into the required
state and control the operation mode.
The function block continuously monitors the status word InProcStatus of
the supply unit and updates the control word OutProcCtrl of the supply unit
based on the inputs assignment.

             Interface description

Table 87: Interface variables of the MB_ECATSoEPowerSupplyDcDcIslandGrid function block
               Name                   Type                             Comment

VAR_INPUT      Enable                 BOOL                             Processing enabled (cyclic, state-controlled)

MasterName             POINTER TO STRING                Instance name of the field bus master. If multiple masters
                                                        are simultaneously operated on the control, they are distin‐
                                                        guished by the “MasterName” input variable. An internal
                                                        variable ‘ethercatmaster’ is assigned to the input by default
                                                        and does thus not have to be assigned.

SlaveAddress           UINT                             EtherCAT address of the slave node, e.g. 1001

PowerSupplyFunction    MB_POWERSUPPLY_FUNCTION          Advanced supply unit function

TargetMode             MB_PS_TARGET_MODE_DC_DC_         Target mode to be reached by the supply unit
                       ISLAND_GRID

OperationModeSelec‐    MB_POWERSUPPLY_MODE              Operation mode of supply unit
tion

Timeout                TIME                             Max. permitted time of each ActualMode -> TargetMode

ClearError             BOOL                             Clearing an error in the drive using the “Clear error” com‐
                                                        mand S-0-0099. After clearing, activate the selected ena‐
                                                        bling.

VAR_IN_OUT
CONSTANT

InProcStatus           WORD                             Status word of the supply unit S-0-2058 (S-0-1720.0.2)

VAR_OUTPUT     InOperation            BOOL                             The function block operates correctly. Output data is valid

Error                  BOOL                             Indicates that an error occurred (see ErrorID and ErrorI‐
                                                        dent)

ErrorID                ⮫ ERROR_CODE                     Error cause

ErrorIdent             ⮫ ERROR_STRUCT                   Detailed error cause

ActualMode             MB_POWERSUPPLY_ACTUAL_MODE Initial state of the state machine of the supply unit

OperationModeStatus    MB_POWERSUPPLY_MODE              Actual operation mode of the supply unit

PowerSupplyError       BOOL                             Internal supply unit error

PowerSupplyWarning     BOOL                             Internal supply unit warning

ClearErrorAck          BOOL                             Confirmation that the command “Clear error” S-0-0099 was
                                                        executed successfully

State                  ⮫ IL_ECAT_STATE                  Device status from ⮫ IL_ECATRemoteSlaveGetDevState

VAR_IN_OUT

OutProcCtrl            WORD                             Supply unit control word (S-0-1720.0.1)

Table 88: Min./max. and default values and use of the MB_ECATSoEPowerSupplyDcDcIslandGrid
inputs
Name                     Type                                 Min.      Max.      Default value         Application
                                                              value     value

Enable                   BOOL                                                     FALSE                 Continuous

MasterName               POINTER TO STRING                    N. def.   N. def.   'ethercatmaster'      Rising edge at

SlaveAddress             UINT                                 0         N. def.   0                     Rising edge at

PowerSupplyFunction      MB_POWERSUPPLY_FUNCTION                                  PS_FUNCTION_DC_DC     Rising   edge    at

TargetMode               MB_PS_TARGET_MODE_DC_DC_ISLAND_GRI                       MAINS_OFF             Continuous
D

OperationModeSelection   MB_POWERSUPPLY_MODE                                      OPERATIONMODE1        Continuous

ClearError               BOOL                                                     FALSE                 Continuous

Timeout                  TIME                                 N. def.   N. def.   T#10s                 Continuous

InProcStatus             WORD                                 N. def.   N. def.   0                     Continuous

Functional description
The function block monitors and controls the supply unit. The function block
can implement different supply unit functions specified in the supply unit
control word.
The main task of the function block is to set the supply unit to the desired
target mode.
The cyclic data exchange between the function block and the supply unit is
described in the following.
● InProcStatus – Updates to S-0-2058 (supply unit status word S-0-1720.0.2)
● OutProcCtrl – Updates to S-0-2057 (supply unit control word S-0-1720.0.1)
For a general description of the internal state machine of the supply unit, refer
to the documentation of the ctrlX DRIVE supply unit functions.

The function block uses the supply unit status word to identify the current
state of the state machine of the supply unit.
The current state is output at the ActualMode output. It depends either on the
DC/DC converter function or on the Island grid mode function selected at the
PowerSupplyFunction input (refer to the previous state graph).
The target mode to be reached by the state machine of the supply unit is
specified using the TargetMode input. The path traveled to reach the target
mode is stored in the function block. The function block performs all required
state transitions up to the target mode.
DC/DC converter: The function block includes the parameterization of
S-0-1741.0.150 (P-0-1647) "DC/DC converter control word". If bit 0 = 1 is par‐
ameterized, i.e. creating the DC output voltage is not required before power
is enabled, the so-called “bypass” is used and specified in the control word
directly from Bb to LF.
In case of a function block error, the state handling is stopped and the error is
signaled at the Error output.
The time that the supply unit requires to reach the target mode from the cur‐
rent mode is monitored using the Timeout input. If this timeout time expires,
the function block reports an error and the state machine handling is stopped.
If the Enable input of the function block is reset, the function block switches
off the supply unit. The control word is reset to set the supply unit to the
Mains Off mode.
The outputs Error, ErrorID and ErrorIdent contain the error information.
The operation mode selection input is continuously output on the bits 8 and 9
of the control word. The InProcStatus input refreshes the function block out‐
puts upon each function block call. Each status word change is immediately
output at the outputs.
Furthermore, a supply unit error can be cleared via the ClearError input. The
rising edge of this input triggers the “Clear error” command S-0-0099 for
the supply unit. The status of a successfully “Clear error” is output via the
ClearErrorAck output of the function block.
The diagnostic information on the supply unit is continuously updated at the
State function block output. The ⮫ IL_ECATRemoteSlaveGetDevState function
block performs the update.

Troubleshooting
The function block can go into an error state due to invalid inputs or an
expired timeout timer. In both cases, the function block generates an error
and cancels the operation.
The user can troubleshoot the error cause, reset the Enable input and set the
input again (standard procedure when resetting errors).
The function block continues. Refer to the following tables for available error
codes.
In addition to the errors of the internally used function blocks ⮫ IL_ECAT‐
SoeCommand, ⮫ IL_ECATSoeRead and ⮫ IL_ECATRemoteSlaveGetDevState, the
function block can generate the following error codes:

Table 89: Error codes of the MB_SIIIPowerSupplyDcDcIslandGrid function block
ErrorID                        Additional1       Additional2      Description
INPUT_INVALID_ERROR            16#0A0F010A       16#0C230201      TargetMode       input    is
                                                                  invalid     (see   MB_POWER‐
                                                                  SUPPLY_TARGET_MODE)

ErrorID                       Additional1        Additional2     Description
INPUT_INVALID_ERROR           16#0A0F010A        16#0C230202     OperationModeSelection      input
                                            invalid      (see      MB_POWER‐
                                            SUPPLY_MODE)
INPUT_INVALID_ERROR           16#0A0F010A        16#0C230203     ErrorMode           input       is
                                            invalid      (see      MB_POWER‐
                                            SUPPLY_ERROR_MODE)
STATE_MACHINE_ERROR           16#0A0F010A        16#0C230204     Timeout (actual mode -> target
                                            mode)
STATE_MACHINE_ERROR           16#0A0F010A        16#0C230205     ActualMode       of   the  device
                                            is invalid (see MB_POWER‐
                                            SUPPLY_ACTUAL_MODE)

INPUT_INVALID_ERROR           16#0A0F010A        16#0C230206     Reference of the MasterName
                                            input is invalid
INPUT_INVALID_ERROR           16#0A0F010A        16#0C230207     The PowerSupplyFunction input
                                            is invalid (see MB_POWER‐
                                            SUPPLY_FUNCTION)

Use case with MB_ECATSoEPowerSupplyDcDcIslandGrid
Use a DC/DC converter to charge a battery.
Use the MB_ECATSoEPowerSupplyDcDcIslandGrid function block to control
the inverter XMV.

The following parameters have to be configured cyclically at least for the XMV:
● MDT: S-0-2057 (S-0-1720.0.1), “Supply unit control word"
● MDT: P-0-3832 (S-0-1741.0.160), “DC voltage command value”
● AT: S-0-2058 (S-0-1720.0.2), "Power supply status word”
Parameterize at least at the XMV:

● Primary mode: Closed-loop DC voltage control
● Secondary mode 1: Closed-loop DC control
● In P-0-1647 (S-0-1741.0.150) "DC/DC converter control word”, bit 0 = 1,
    i.e. creating the DC output voltage is not required before power enabled
In this case, the DC contactor is switched using an S20 bus coupler S20-EC-
BK with an S20 relay module S20-DOR that is connected to a ctrlX CORE
control and the battery voltage is measured using an S20 analog module S20-
AI. Another hardware can also be used. The battery voltage can be measured
using an analog input of the XMV and the value can be applied using EtherCAT
at the ctrlX CORE.
Table 90: Sequence in the following program example
  uiS‐ Description                              TargetMode                  Target state
  tate                                          selection           ActualMode Supply unit
  vari‐                                                                           status
  able
   1    Power section selection off, DC con‐    MAINS_OFF           MAINS_OFF   bb
        tactor open
   2    Setting the voltage command value       POWER_OFF         DC_POWER_OF Bb
        (UComm, DC) equal to the measured bat‐                         F
        tery voltage and selecting the primary
        mode “Voltage control”.
        Power section selection off. Supply
        unit checks whether UIC > UComm, DC *
        1.01? No DC output voltage yet
   3    Selection to charge the DC output       OPERA‐                OPERA‐     LF
        voltage                                 TION_MODE          TION_MODE
   4    If the DC output voltage is charged     POWER_OFF         The DC output
        (UDC = battery voltage) and if the pri‐                   voltage should
        mary mode is acknowledged, “Bb” is                         remain. Con‐
        specified again.                                           tinue with 5
   5    Closing the DC contactor.               OPERA‐                OPERA‐     LF
        If the DC contactor is closed, select   TION_MODE          TION_MODE
        the secondary mode 1: Current control
        and "LF" specification
   6    If secondary mode 1 and “LF” are        OPERA‐                OPERA‐    LF
        acknowledged, proceed with step 7       TION_MODE           TION_MODE
   7    Ready. To switch off, set the variable  OPERA‐                OPERA‐    LF
        uiState to “1”.                         TION_MODE           TION_MODE
                     The procedure is controlled using the variable uiState:
                     ● uiState = "1" enables the function block and switches off
                     ● uiState = "2" also enables the function block and starts the automatic
                        procedure
                     In this example, the closed-loop control is disabled in step 4 and enabled
                     again in step 5 when closing the contactor using the closed-loop current
                     control. Depending on the application, go to the command value 0 and subse‐
                     quently enable the closed-loop current control and close the contactor.

  Variable definition

  fbPowerSupplyDcDcIslandGrid:
  MB_ECATSoEPowerSupplyDcDcIslandGrid;
  wPS_Status : WORD;      // connect to S-0-2058 (S-0-1720.0.2)
  "Power supply status word"

wPS_Control: WORD;      // connect to S-0-2057 (S-0-1720.0.1)
"Power supply control word"
uiState    : UINT := 0; // set to 1 to Enable FB and stay in
OFF or set to 2 for automatic start-up

Called cyclically

//-------------------------------------------------------------
-----------------------------------------
//------------------------------ handle power-supply
---------------------------------------
//-------------------------------------------------------------
-----------------------------------------

CASE uiState OF
  1: fbPowerSupplyDcDcIslandGrid.Enable := TRUE;
      // to do: Open contactor between output DC/DC converter
and battery (S20-DOR)
      fbPowerSupplyDcDcIslandGrid.TargetMode :=
MB_PS_TARGET_MODE_DC_DC_ISLAND_GRID.MAINS_OFF; // all OFF

  2: fbPowerSupplyDcDcIslandGrid.Enable := TRUE;
     // to do: Open contactor between output DC/DC converter
and battery (S20-DOR)
     // to do: Set S-0-1741.0.160 "DC voltage command value"
to measured battery voltage (S20-AI)
     // Main operating mode Voltage control
     fbPowerSupplyDcDcIslandGrid.OperationModeSelection :=
MB_POWERSUPPLY_MODE.OPERATIONMODE1;
     // start automatic start-up. Switch to ready for
operation Bb
     fbPowerSupplyDcDcIslandGrid.TargetMode :=
MB_PS_TARGET_MODE_DC_DC_ISLAND_GRID.POWER_OFF;
     IF fbPowerSupplyDcDcIslandGrid.ActualMode =
MB_POWERSUPPLY_ACTUAL_MODE.DC_POWER_OFF AND
          TRUE (* to do: contactor is open? *)
     THEN
       uiState := uiState + 1;
     END_IF

  3: // Charging to LF
     fbPowerSupplyDcDcIslandGrid.TargetMode :=
MB_PS_TARGET_MODE_DC_DC_ISLAND_GRID.OPERATION_MODE;
     uiState := uiState + 1;

  4: // Charged to LF AND Ack Main op-mode
     IF fbPowerSupplyDcDcIslandGrid.ActualMode =
MB_POWERSUPPLY_ACTUAL_MODE.OPERATION_MODE AND
       fbPowerSupplyDcDcIslandGrid.OperationModeStatus =
MB_POWERSUPPLY_MODE.OPERATIONMODE1
     THEN
       // Back to "ready for operation" Bb
       fbPowerSupplyDcDcIslandGrid.TargetMode :=
MB_PS_TARGET_MODE_DC_DC_ISLAND_GRID.POWER_OFF;
       uiState := uiState + 1;
     END_IF

   5:
        // to do: Close contactor between output DC/DC converter

and battery (S20-DOR)
    IF TRUE (* to do: contactor closed? *) THEN
      // activate secondary operation mode 1, (DC) current
control
      fbPowerSupplyDcDcIslandGrid.OperationModeSelection :=
MB_POWERSUPPLY_MODE.OPERATIONMODE2;
      // Switch to operating LF
      fbPowerSupplyDcDcIslandGrid.TargetMode :=
MB_PS_TARGET_MODE_DC_DC_ISLAND_GRID.OPERATION_MODE;
      uiState := uiState + 1;
    END_IF

  6: // LF reached AND Ack 2nd op-mode
     IF fbPowerSupplyDcDcIslandGrid.ActualMode =
MB_POWERSUPPLY_ACTUAL_MODE.OPERATION_MODE AND
       fbPowerSupplyDcDcIslandGrid.OperationModeStatus =
MB_POWERSUPPLY_MODE.OPERATIONMODE2
     THEN
       uiState := uiState + 1;
     END_IF

   7: ; // Finished. Set uiState to 1 to switch power supply OFF

  99: ; // Error!! Add error-handling here
      // to do: Open contactor between output DC/DC converter
and battery (S20-DOR)

END_CASE
// call function block. I/Os are handled above
fbPowerSupplyDcDcIslandGrid(
  Enable:= ,
  InOperation=> ,
  Error=> ,
  ErrorID=> ,
  ErrorIdent=> ,
  MasterName:= ,
  SlaveAddress:= 1001,
  PowerSupplyFunction:=
MB_POWERSUPPLY_FUNCTION.PS_FUNCTION_DC_DC,
  TargetMode:= ,
  OperationModeSelection:= ,
  Timeout:= ,
  ClearError:= ,
  InProcStatus:= wPS_Status,
  ActualMode=> ,
  OperationModeStatus=> ,
  PowerSupplyError=> ,
  PowerSupplyWarning=> ,
  ClearErrorAck=> ,
  State=> ,
  OutProcCtrl:= wPS_Control);
IF fbPowerSupplyDcDcIslandGrid.Error THEN
  uiState := 99;
END_IF

## 12.3 FreqConv

### 12.3.1 Mode MB_ECATCoEFreqConv

MB_ECATCoEFreqConv
         Brief description
         The function block MB_ECATCoEFreqConv to control the Rexroth frequency
         converter EFC via Ethercat CoE

Interface description

Table 91: Interface variables of the MB_ECATCoEFreqConv function block
                   Name                         Type                       Comment

VAR_INPUT          Execute                      BOOL                       Rising edge starts the computation

FrequencyCmd                 UINT

FreqConvCtrlWord             MB_FreqConvCtrlWord_bits

FrequencyCmdAddress          REFERENCE TO UINT          Instance name of the field bus master

FreqConvCtrlWordAddress      REFERENCE TO UINT          EthercatAddr or AutoIncAddr at the bus depends
                                                        on the AddressType input

SettingFreqInConvAddress     REFERENCE TO UINT

FreqConvStatusWordAddress    REFERENCE TO UINT

VAR_OUTPUT         Done                         BOOL                       Computation completed

Active                       BOOL                       Computation active

Error                        BOOL                       An error occurred

ErrorID                      ERROR_CODE                 Error classification

ErrorIdent                   ERROR_STRUCT               Error diagnostics

         Functional description
         The control variable of MB_ECATCoEFreqConv is the frequency.
         The "FreqConvCtrlWord" input is the real-time control word for EFC. The
         address refers to the I/O address of ethercatmaster in the Data Layer.

         Troubleshooting
         For more information on the EFC error codes, refer to the documentation
         "Rexroth Frequency Converter EFC x610 Series EFC 3610 / EFC 5610" DOK-
         RCON03-EFC-X610***-ITRS-EN-P (R912005854)

Table 92: Error codes of the MB_ECATCoEFreqConv function block
ErrorID                        Additional1          Additional2              Description

INPUT_INVALID_ERROR            16#0A0F010A          16#0C23XXXX              XXXX is the EFC error code

                                                 (Refer to the documentation "Rexroth Frequency Con‐
                                                 verter EFC x610 Series EFC 3610 / EFC 5610" DOK-
                                                 RCON03-EFC-X610***-ITRS-EN-P (R912005854)

MB_ECATCoEFreqConvCtrlWordEnCoding
Brief description
The MB_ECATCoEFreqConvCtrlWordEnCoding function generates the control
word for the Rexroth frequency converter EFC via Ethercat CoE.

Interface description

Table 93: Interface variables of the MB_ECATCoEFreqConvCtrlWordEnCoding function
                     Name                                         Type                                    Comment

VAR_INPUT            FCOpstate                                    MB_FREQCONV_OPSTATE

VAR_OUTPUT           MB_ECATCoEFreqConvCtrlWordEnCoding           MB_FreqConvCtrlWord_bits

Functional description
The MB_ECATCoEFreqConvCtrlWordEnCoding function converts the operating
state of the EFC into the control word in bits.

Sample program

Declaration:

PROGRAM Example_ECATCoEFreqConvCtrlWordEnCoding
VAR
  FCCtrlWordBit:      MB_FreqConvCtrlWord_bits;
END_VAR

Implementation:

FCCtrlWordBit := MB_ECATCoEFreqConvCtrlWordEnCoding(FreqConvOpState);

### 12.3.2 Mode MB_ECATCoE402FreqConv

MB_ECATCoE402FreqConv
Brief description
The function block MB_ECATCoE402FreqConv controls the Rexroth frequency
converter EFC via Ethercat CoE. It is part of the CXA_DriveUtil library.

Interface description

Table 94: Interface variables of the MB_ECATCoE402FreqConv function block
I/O type   Name                           Data type                     Initially          Comment                   Applied from

INPUT      Execute                        BOOL                                             Rising edge starts IL_ExecuteDoneBase
                                                               the computation

OUTPUT     Done                           BOOL                                             Computation        com‐ IL_ExecuteDoneBase

Active                         BOOL                                             Computation active IL_ExecuteDoneBase

Error                          BOOL                                             An error occurred         IL_ExecuteDoneBase

ErrorID                        ⮫ ERROR_CODE                                     Error classification      IL_ExecuteDoneBase

ErrorIdent                     ⮫ ERROR_STRUCT                                   Error diagnostics         IL_ExecuteDoneBase

INPUT      StrMasterName                  STRING                        'ethercatmaster'

uiEthercatAddr                 UINT                          1001               1001

VelocityCmd                    UINT                                             Target velocity

FreqConv402CtrlWord            MB_FreqConv402CtrlWord_bits                      Control word EFC

VelocityCmdAddress             REFERENCE TO UNIT                                I/O      address     of
                                                               ethercatmaster       in
                                                               the Data Layer

FreqConv402CtrlWordAddress     REFERENCE TO UNIT                                I/O      address     of
                                                               ethercatmaster       in
                                                               the Data Layer

SettingVelocityInConvAddress   REFERENCE TO UNIT                                I/O      address     of
                                                               ethercatmaster       in
                                                               the Data Layer

FreqConv402StatusWordAddress   REFERENCE TO UNIT                                I/O      address     of
                                                               ethercatmaster       in
                                                               the Data Layer

Functional description
The control variable of MB_ECATCoE402FreqConv is the velocity.
The "FreqConv402CtrlWord" input is the real-time control word for EFC. The
address refers to the I/O address of ethercatmaster in the Data Layer.
Switch to the mode 402
−   The EFC parameter H4.24 has to be set to -128. The FC has to be restarted
    to apply the change.
−   Configure the slave device of ethercatmaster of the ctrlX CORE in
    xFC01_Velocity_mode.

Table 95: Error codes of the MB_ECATCoE402FreqConv function block
ErrorID                   Additional1             Additional2                 Description

INPUT_INVALID_ERROR       16#0A0F010A             16#0C23XXXX                 XXXX is the EFC error code

                                                    (Refer to the documentation "Rexroth Frequency Con‐
                                                    verter EFC x610 Series EFC 3610 / EFC 5610" DOK-
                                                    RCON03-EFC-X610***-ITRS-EN-P (R912005854))

MB_ECATCoEFreqConv402CtrlWordEnCoding
Brief description
The MB_ECATCoEFreqConv402CtrlWordEnCoding function controls the Freq‐
Conv402CtrlWord. It converts the operating state of the EFC into the control
word in bits.

Interface description

Table 96: Interface variables of the MB_ECATCoEFreqConv402CtrlWordEnCoding function
I/O type           Name                                                              Type

VAR_INPUT          FCOpstate                                                         MB_FREQCONV402_OPSTATE

RETURN VALUE       MB_ECATCoEFreqConv402CtrlWordEnCoding                             MB_FreqConv402CtrlWord_bits

Functional description
The input FCOpstate of the function MB_ECATCoEFreqConv402CtrlWordEn‐
Coding uses the type of the enum MB_FREQCONV402_OPSTATE listed in the
following table.
Name                       Type             Initially           Description

FC_Init                    BYTE             0                   Switched-off state

FC_SwitchOn                BYTE             1                   Switch on, but do not enable

FC_OPEnabled               BYTE             2                   Enable Motion

FC_QuickStoped             BYTE             3                   Stop as per the parameter setting

FC_Reset                   BYTE             4                   Reset error

Sample program
This example shows the use of the function MB_ECATCoEFreq‐
Conv402CtrlWordEnCoding and of the function block MB_ECATCoE402Freq‐
Conv.

Declaration:

PROGRAM Example_MB_ECATCoEFreqConv402
VAR
FC402CtrlWordBit:     MB_FreqConv402CtrlWord_bits;
FreqConv402OpState: MB_FREQCONV402_OPSTATE := MB_FREQCONV402_OPSTATE.FC_Init;
fb_FreqConv:     MB_ECATCoE402FreqConv;
FBStart:     BOOL;
VelCmd:   INT:=1000;
VelCmd_Last:     INT;
FreqConv402OpState_Last: MB_FREQCONV402_OPSTATE;
END_VAR

Implementation:

IF(VelCmd<>VelCmd_Last)OR(FreqConv402OpState<>FreqConv402OpState_Last)THEN
     FBStart:=TRUE;
END_IF
FC402CtrlWordBit:=MB_ECATCoEFreqConv402CtrlWordEnCoding(FreqConv402OpState);

fb_FreqConv(Execute:=FBStart,
VelocityCmd:=VelCmd,
VelocityCmdAddress:=%QW2,
FreqConv402CtrlWord:=FC402CtrlWordBit,
FreqConv402CtrlWordAddress:=%QW0,
SettingVelocityInConvAddress:=%IW0,
FreqConv402StatusWordAddress:=%IW2);

VelCmd_Last:=VelCmd;
FreqConv402Opstate_Last:=FreqConv402OpState;

IF fb_FreqConv.Done THEN

   FBStart:=FALSE;
END_IF

### 12.3.3 Mode MB_ECATCoETorque

MB_ECATCoETorque
Brief description
The function block MB_ECATCoETorque controls the Rexroth frequency con‐
verter EFC via Ethercat CoE. It is part of the CXA_DriveUtil library.

Interface description

Table 97: Interface variables of the MB_ECATCoETorque function block
I/O type Name                         Data type                  Initially          Comment                      Applied from

INPUT   Execute                       BOOL                                          Rising    edge   starts   the IL_ExecuteDoneBase
                                                         computation

OUTPUT Done                           BOOL                                          Computation completed        IL_ExecuteDoneBase

Active                        BOOL                                          Computation active           IL_ExecuteDoneBase

Error                         BOOL                                          An error occurred            IL_ExecuteDoneBase

ErrorID                       ERROR_CODE                                    Error classification         IL_ExecuteDoneBase

ErrorIdent                    ERROR_STRUCT                                  Error diagnostics            IL_ExecuteDoneBase

INPUT   StrMasterName                 STRING                     'ethercatmaster'

uiEthercatAddr                UINT                       1001               1001

TorqueCmd                     UINT                                          Target torque

FreqConvCtrlWord              MB_FreqConvCtrlWord_bits                      Control word EFC

TorqueCmdAddress              REFERENCE TO UNIT                             I/O address of ethercat‐
                                                         master in the Data Layer

FreqConvCtrlWordAddress       REFERENCE TO UNIT                             I/O address of ethercat‐
                                                         master in the Data Layer

I/O type Name                            Data type                  Initially           Comment                    Applied from

SettingTorqueInConvAddress    REFERENCE TO UNIT                              I/O address of ethercat‐
                                                             master in the Data Layer

FreqConvStatusWordAddress     REFERENCE TO UNIT                              I/O address of ethercat‐
                                                             master in the Data Layer

Functional description
The control variable of MB_ECATCoETorque is the torque.
The "FreqConvCtrlWord" input is the real-time control word for EFC. The
address refers to the I/O address of ethercatmaster in the Data Layer.
Change to torque mode
−
The EFC parameter H4.24 has to be set to 2. The FC has to be restarted to
apply the change.
− Configure the slave device of ethercatmaster of the ctrlX CORE in
xFC01_Rexroth_mode.
Table 98: Error codes of the MB_ECATCoETorque function block
ErrorID                    Additional1                Additional2                 Description

INPUT_INVALID_ERROR        16#0A0F010A                16#0C23XXXX                 XXXX is the EFC error code

                                                       (Refer to the documentation "Rexroth Frequency Con‐
                                                       verter EFC x610 Series EFC 3610 / EFC 5610" DOK-
                                                       RCON03-EFC-X610***-ITRS-EN-P (R912005854))

MB_ECATCoEFreqConvTorqueCtrlWordEnCoding
Brief description
The MB_ECATCoEFreqConvTorqueCtrlWordEnCoding function computes Freq‐
ConvCtrlWord. It converts the operating state of the EFC into the control word
in bits.

Interface description

Table 99: Interface variables of the MB_ECATCoEFreqConvTorqueCtrlWordEnCoding function
I/O type               Name                                                                     Type

RETURN VALUE           MB_ECATCoEFreqConvTorqueCtrlWordEnCoding                                 MB_FreqConvCtrlWord_bits

VAR_INPUT              FCOpstate                                                                MB_FREQCONV_OPSTATE

Functional description
The input FCOpstate of the function MB_ECATCoEFreqConvTorqueCtrlWordEn‐
Coding uses the type of the enum MB_FREQCONV_OPSTATE listed in the fol‐
lowing table.
Name                           Type              Initially          Description

FC_Init                        BYTE              0                  Resetting all bits to FALSE

FC_ForwardStart                BYTE              1

FC_ReverseStart                BYTE              2

FC_ParaStop                    BYTE              3                  Stop as per the parameter setting

FC_Estop                       BYTE              4                  Stop as per the parameter setting

FC_Reset                       BYTE              5                  Resetting all bits to FALSE

Sample program
This example shows the use of the function MB_ECATCoEFreqConvTorqueCtrl‐
WordEnCoding and of the function block MB_ECATCoETorque.

Declaration:

PROGRAM Example_MB_ECATCoEFreqConvFnT
VAR
  FCCtrlWordBit:       MB_FreqConvCtrlWord_bits;
  FreqConvOpState:       MB_FREQCONV_OPSTATE := MB_FREQCONV_OPSTATE.FC_Init;
  fb_FreqConv:       MB_ECATCoETorque;
  FBStart:       BOOL;
  FreqCmd:       UINT:=600;
  FreqCmd_Last:      UINT;

  TqCmd:       UINT:=1000;
  TqCmd_Last:      UINT;
  FreqConvOpState_Last:     MB_FREQCONV_OPSTATE; END_VAR

Implementation:

IF(TqCmd<>TqCmd_Last)OR(FreqConvOpState<>FreqConvOpState_Last)THEN
     FBStart:=TRUE;
END_IF

FCCtrlWordBit:=MB_ECATCoEFreqConvTorqueCtrlWordEnCoding(FreqConvOpState);

fb_FreqConv(Execute:=FBStart,
TorqueCmd:=TqCmd,
TorqueCmdAddress:=%QW4,
FreqConvCtrlWord:=FCCtrlWordBit,
FreqConvCtrlWordAddress:=%QW0,
SettingTorqueInConvAddress:=%IW4,
FreqConvStatusWordAddress:=%IW2);

TqCmd_Last:=TqCmd;
FreqConvOpstate_Last:=FreqConvOpState;

IF fb_FreqConv.Done THEN
   FBStart:=FALSE;
END_IF

### 12.3.4 Mode MB_ECATCoEFreqConv_FnT

MB_ECATCoEFreqConv_FnT
Brief description
The function block MB_ECATCoEFreqConv_FnT to control the Rexroth fre‐
quency converter EFC via Ethercat CoE. It is part of the CXA_DriveUtil library.

Interface description

Table 100: Interface variables of the MB_ECATCoEFreqConv_FnT function block
I/O type   Name                           Data type                  Initially          Comment                            Applied from

INPUT      Execute                        BOOL                                          Rising edge starts the com‐ IL_ExecuteDone‐
                                                                    putation                           Base

OUTPUT     Done                           BOOL                                          Computation completed              IL_ExecuteDone‐

Active                         BOOL                                          Computation active                 IL_ExecuteDone‐

Error                          BOOL                                          An error occurred                  IL_ExecuteDone‐

ErrorID                        ERROR_CODE                                    Error classification               IL_ExecuteDone‐

ErrorIdent                     ERROR_STRUCT                                  Error diagnostics                  IL_ExecuteDone‐

INPUT      StrMasterName                  STRING                     'ethercatmaster'

uiEthercatAddr                 UINT                       1001               1001

FrequencyCmd                   UINT                                          Target frequency

TorqueCmd                      UINT                                          Target torque

ControlMode                    MB_FREQCONV_OPMODE                            Target control word

TorqueCtrlWord                 MB_FreqConvCtrlWord_bits                      Control word of EFC

FrequencyCmdAddress            REFERENCE TO UNIT                             I/O     address   of   ethercat‐
                                                                    master in the Data Layer

TorqueCmdAddress               REFERENCE TO UNIT                             I/O     address   of   ethercat‐
                                                                    master in the Data Layer

FreqConvCtrlWordAddress        REFERENCE TO UNIT                             I/O     address   of   ethercat‐
                                                                    master in the Data Layer

SettingFreqInConvAddress       REFERENCE TO UNIT                             I/O     address   of   ethercat‐
                                                                    master in the Data Layer

SettingTorqueInConvAddress REFERENCE TO UNIT                                 I/O     address   of   ethercat‐
                                                                    master in the Data Layer

FreqConvStatusWordAd‐          REFERENCE TO UNIT                             I/O     address   of   ethercat‐
dress                                                                        master in the Data Layer

        Functional description
The control variable of MB_ECATCoEFreqConv_FnT is either the torque or the
frequency (specified by ControlMode). The "FreqConvCtrlWord" input is the
real-time control word for EFC. The address refers to the I/O address of ether‐
catmaster in the Data Layer.
Table 101: Error codes of the MB_ECATCoEFreqConv_FnT function block
ErrorID                     Additional1                Additional2                Description

INPUT_INVALID_ERROR         16#0A0F010A                16#0C23XXXX                XXXX is the EFC error code

                                                              (Refer to the documentation "Rexroth Frequency Con‐
                                                              verter EFC x610 Series EFC 3610 / EFC 5610" DOK-
                                                              RCON03-EFC-X610***-ITRS-EN-P (R912005854))

MB_ECATCoEFreqConvCtrlWordEnCoding_FnT
        Brief description
        The MB_ECATCoEFreqConvCtrlWordEnCoding_FnT function computes Freq‐
        ConvCtrlWord. It converts the operating state of the EFC into the control word
        in bits.

Interface description

Table 102: Interface variables of the MB_ECATCoEFreqConvCtrlWordEnCoding_FnT function
I/O type          Name                                                       Type

RETURN VALUE      MB_ECATCoEFreqConvCtrlWordEnCoding_FnT                     MB_FreqConvCtrlWord_bits

VAR_INPUT         FCOpMode                                                   MB_FREQCONV_OPMODE

FCOpstate                                                  MB_FREQCONV_OPSTATE

Functional description
The input FCOpstate of the function MB_ECATCoEFreqConvCtrlWordEn‐
Coding_FnT uses the type of the enum MB_FREQCONV_OPSTATE listed in the
following table.
Name                              Type             Initially       Description

FC_Init                           BYTE             0               Resetting all bits to FALSE

FC_ForwardStart                   BYTE             1

FC_ReverseStart                   BYTE             2

FC_ParaStop                       BYTE             3               Stop as per the parameter setting

FC_EStop                          BYTE             4               Stop as per the parameter setting

FC_Reset                          BYTE             5               Resetting all bits to FALSE

The input FCOpMode of the function MB_ECATCoEFreqConvCtrlWordEn‐
Coding_FnT uses the type of the enum MB_FREQCONV_OPMODE listed in the
following table.
Name                              Type             Initially       Description
FC_Frequency                      BYTE             0
FC_Torque                         BYTE             1

Sample program
This example shows the use of the function MB_ECATCoEFreqConvCtrlWor‐
dEnCoding_FnT and of the function block MB_ECATCoEFreqConv_FnT.

Declaration:

PROGRAM Example_MB_ECATCoEFreqConvFnT
VAR
  FCCtrlWordBit:       MB_FreqConvCtrlWord_bits;
  FreqConvOpState:       MB_FREQCONV_OPSTATE := MB_FREQCONV_OPSTATE.FC_Init;
  fb_FreqConv2:      MB_ECATCoEFreqConv_FnT;
  FBStart:       BOOL;
  FreqCmd:       UINT:=600;
  FreqCmd_Last:      UINT;
  TqCmd:      UINT:=1000;
  TqCmd_Last:      UINT;
  FreqConvOpState_Last:     MB_FREQCONV_OPSTATE;
  FreqConvOpMode:      MB_FREQCONV_OPMODE := MB_FREQCONV_OPMODE.FC_Freque
  FreqConvOpMode_Last:      MB_FREQCONV_OPMODE;
END_VAR

Implementation:

IF FreqConvOpMode<>FreqConvOpMode_Last THEN
     FBStart:=TRUE;
END_IF

IF FreqConvOpMode=MB_FREQCONV_OPMODE.FC_Frequency THEN
   IF(FreqCom<>FreqCmd_Last)OR(FreqConvOpState<>FreqConvOpstate_Last) THEN
       FBStart:=TRUE;
   EnD_IF
ELSE
 IF(TqCmd<>TqCmd_Last)OR(FreqConvOpState<>FreqConvOpstate_Last) THEN
     FBStart:=TRUE;
   EnD_IF
END_IF
FCCtrlWordBit :=
MB_ECATCoEFreqConvCtrlWordEnCoding_FnT(FreqConvOpMode,FreqConvOpState);fb_FreqConv2(Execute
:=FBStart,
FrequencyCmd:= FreqCmd,
TorqueCmd:= TqCmd,
ControlMode:= FreqConvOpMode,
FrequencyCmdAddress:=%QW2,
TorqueCmdAddress:=%QW4,
FreqConvCtrlWord:=FCCtrlWordBit,
FreqConvCtrlWordAddress:=%QW0,
SettingFreqInConvAddress:=%IW0,
SettingTorqueInConvAddress:=%IW4,
FreqConvStatusWordAddress:=%IW2);

FreqCmd_Last := FreqCmd;
TqCmd_Last := TqCmd;
FreqConvOpMode_Last:= FreqConvOpMode;
FreqConvOpState_Last:= FreqConvOpState;
IF fb_FreqConv2.Done THEN
    FBStart := FALSE;
END_IF
