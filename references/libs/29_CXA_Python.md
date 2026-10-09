# 29 CXA_Python

## 29.1 Introduction and overview

Use the function blocks of the PLC library CXA_Python to execute, delete,
monitor and reset Python scripts. The rexroth-python package is required in
addition to the PLC.
The scripts are executed on script instances. Multiple instances can be cre‐
ated. Each instance can execute one Python script at the same time.
Function blocks:
● ⮫ IL_ScriptInstance
● ⮫ IL_StartScript
● ⮫ IL_StartScriptFile
● ⮫ IL_CreateScriptInstance
● ⮫ IL_DeleteScriptInstance
● ⮫ IL_AbortScript
● ⮫ IL_ResetInstance
● ⮫ IL_ReadInstanceDiagnostics
● ⮫ IL_ReadInstanceState
● ⮫ IL_ScriptInstanceStatus
Data types:
● ⮫ INSTANCE_STATE
● ⮫ INSTANCE_RESET_CMD_STATE
● ⮫ INSTANCE_ABORT_CMD_STATE

Example
The IL_ScriptInstance function block creates a script instance and monitors
it. Scripts can be started on this instance using the function blocks IL_Start‐
Script and IL_StartScriptFile.

(* This example shows how to start an python script on a script instance *)

PROGRAM Example_PythonScript
VAR
  fbInst: IL_ScriptInstance;
  fbScript: IL_StartScript;
  iState: INT := 0;
END_VAR

     CASE iState OF
       0:
          fbInst(Enable:=TRUE, InstanceName:='Test1');
          IF fbInst.Enable THEN
            iState := 1;
          END_IF
       1:
          fbScript(Execute:=TRUE,
     InstanceName:='Test1',
     PythonString:='import time$Ntime.sleep(10)');
          iState :=2;
       2:
          fbInst();
          IF fbInst.State = INSTANCE_STATE.READY THEN
            iState := 3;
          END_IF
       3:
          ;

     END_CASE

## 29.2 IL_ScriptInstance

     Brief description
     The function block IL_ScriptInstance creates, monitors and deletes a Python
     script instance in the Data Layer.

     Interface description

Table 793: Interface variables of the IL_ScriptInstance function block
I/O type           Name              Data type          Description
VAR_INPUT          Enable            BOOL               A rising edge creates a script instance and a
                                                        falling edge deletes it again
           InstanceName              STRING             Instance name
           ResetInstance             BOOL               A rising edge resets a script instance
           AbortScript               BOOL               A rising edge stops a running script
VAR_OUTPUT InOperation               BOOL               The script instance is monitored
           Error                     BOOL               An error occurred
           ErrorID                   ⮫ ERROR_CODE       Error classification
                   ErrorIdent        ⮫ ERROR_STRUCT Error diagnostics
                   State             INSTANCE_STATE State of the script instance
                   ResetState        INSTANCE_RESET_ Status of the reset command
                                     CMD_STATE

I/O type       Name               Data type        Description
AbortState         INSTANCE_ABORT Status of the abort command
                   _CMD_STATE
Script             STRING(255)      Name of the script file or character string
MotionObjAtta‐     ARRAY [0..15] OF Motion object assigned to the instance
chedTo             STRING
Line               ULINT            Currently interpreted line is not the line index
                                    of the source file
pid                UDINT            Process ID of this instance
LastMainDiag       UDINT            Script main diagnostic number
LastDetailDiag     UDINT            Script detailed diagnostic number

ErrorMessage       STRING(255)      Error message of the script

       Functional description
       At a rising edge at “Enable”, the IL_ScriptInstance function block creates a
       script instance with the same name specified at the “InstanceName” input
       in the Data Layer. The instance is created below the Data Layer node /script/
       instances/. An already existing instance with the same name is applied. The
       instance is deleted at a falling edge at "Enable”.
       The instance state is checked continuously and output at the “State” output
       when “Enable” is active.
       In case of error, the instance can be reset via a rising edge at the "ResetIn‐
       stance” input. A rising edge at the “AbortScript” input stops a currently run‐
       ning Python script.
       The function blocks ⮫ IL_StartScriptFile and ⮫ IL_StartScript execute Python
       scripts on the script instance.

       Programming example
       Refer to ⮫ Chapter 29.1 Introduction and overview on page 913

## 29.3 IL_StartScript

       Brief description
       The IL_StartScript function block executes a short Python file on a script
       instance.

       Interface description

Table 794: Interface variables of the IL_StartScript function block
I/O type          Name        Data type               Description
VAR_INPUT         Execute     BOOL                    Rising edge starts a script on a script
                                                      instance
                  Instance‐    STRING                 Instance name
                  Name
                  PythonScript STRING(80)             Python script to be processed

I/O type           Name         Data type               Description
Parameter    REFERENCE TO            Array with parameters to be transferred
             ARRAY[0..9] OF
             STRING
VAR_OUTPUT Done                 BOOL                    The Python script was started
Active               BOOL                    The start is running
Error                BOOL                    An error occurred
ErrorID              ⮫ ERROR_CODE            Error classification
ErrorIdent   ⮫ ERROR_STRUCT          Error diagnostics

     Functional description
     The IL_StartScript function block starts a short Python script on a script
     instance at a rising edge at “Execute”. The instance name is created at the
     “InstanceName” input. The Python script is directly stored in a variable of the
     type STRING created at the "PythonString" input. The script length is limited
     to 80 characters. Additional parameters can additionally be transferred at the
     "Parameters" input.
     The function block ⮫ IL_ScriptInstance monitors the execution of the script in
     the script instance.

     Programming example
     Refer to ⮫ Chapter 29.1 Introduction and overview on page 913

## 29.4 IL_StartScriptFile

     Brief description
     The IL_StartScriptFile function block executes a Python file on a script
     instance.

     Interface description

Table 795: Interface variables of the IL_StartScriptFile function block
I/O type           Name         Data type               Description
VAR_INPUT          Execute      BOOL                    Rising edge starts a script on a script
                                                        instance
                   Instance‐    STRING                  Instance name
                   Name
                   FileName     STRING(80)              File name of the Python script
                   Parameter    REFERENCE TO            Array with parameters to be transferred
                                ARRAY[0..9] OF
                                STRING
VAR_OUTPUT Done                 BOOL                    The Python script was started
           Active               BOOL                    The start is running
           Error                BOOL                    An error occurred
           ErrorID              ⮫ ERROR_CODE            Error classification

I/O type          Name         Data type               Description
ErrorIdent   ⮫ ERROR_STRUCT          Error diagnostics

Functional description
The IL_StartScriptFile function block starts a short Python script on a script
instance at a rising edge at “Execute”. The instance name is created at the
“InstanceName” input. The Python script is stored in a file. Its name is created
at the "PythonString" input. Additional parameters can additionally be trans‐
ferred at the "Parameters" input.
The function block ⮫ IL_ScriptInstance monitors the execution of the script in
the script instance.

Programming example
Refer to ⮫ Chapter 29.1 Introduction and overview on page 913

## 29.5 IL_CreateScriptInstance

Brief description
The function block IL_CreateScriptInstance creates a Python script instance in
the Data Layer.

Interface description

Table 796: Interface variables of the IL_CreateScriptInstance function block
I/O type   Name                    Data type           Description
VAR_INPUT  Execute                 BOOL                Rising edge creates a script instance
           InstanceName            STRING              Instance name
VAR_OUTPUT Done                    BOOL                Instance is created
           Active                  BOOL                Instance is created
           Error                   BOOL                An error occurred
           ErrorID                 ⮫ ERROR_CODE        Error classification
               ErrorIdent          ⮫ ERROR_STRUCT Error diagnostics

Functional description
At a rising edge at “Execute”, the IL_CreateScriptInstance function block cre‐
ates a Python script instance with the same name specified at the “Instance‐
Name” input in the Data Layer. The instance is created below the Data Layer
node /script/instances/.
The function blocks ⮫ IL_ScriptInstanceStatus and ⮫ IL_StartScript monitor
the state and the diagnostics of the instance.

## 29.6 IL_DeleteScriptInstance

Brief description
The function block IL_DeleteScriptInstance deletes a Python script instance in
the Data Layer.

Interface description

Table 797: Interface variables of the IL_DeleteScriptInstance function block
I/O type   Name                     Data type          Description
VAR_INPUT  Execute                  BOOL               Rising edge deletes a script instance
           InstanceName             STRING             Instance name
VAR_OUTPUT Done                     BOOL               Instance is deleted
           Active                   BOOL               Instance is deleted
           Error                    BOOL               An error occurred
           ErrorID                  ⮫ ERROR_CODE       Error classification
                   ErrorIdent       ⮫ ERROR_STRUCT Error diagnostics

Functional description
At a rising edge at “Execute”, the IL_DeleteScriptInstance function block
deletes a Python script instance with the same name specified at the “Instan‐
ceName” input in the Data Layer. The instance is removed from the Data Layer
node /script/instances/.

## 29.7 IL_AbortScript

Brief description
The IL_AbortScript function block cancels a Python script in the Data Layer.

Interface description

Table 798: Interface variables of the IL_AbortScript function block
I/O type           Name             Data type          Description
VAR_INPUT          Execute          BOOL               A rising edge cancels a running script

I/O type   Name                  Data type          Description
InstanceName          STRING             Instance name
VAR_OUTPUT Done                  BOOL               Script is aborted
Active                BOOL               Script is aborted
Error                 BOOL               An error occurred
ErrorID               ⮫ ERROR_CODE       Error classification
ErrorIdent        ⮫ ERROR_STRUCT Error diagnostics

Functional description
At a rising edge at “Execute”, the IL_AbortScript function block aborts a
running Python script of the instance with the same name specified at the

“InstanceName” input in the Data Layer.
After the script has been aborted, the instance is in the "INIT" state.

## 29.8 IL_ResetInstance

Brief description
The IL_ResetInstance function block resets a Python script instance.

Interface description

Table 799: Interface variables of the IL_ResetInstance function block
I/O type   Name                  Data type          Description
VAR_INPUT  Execute               BOOL               A rising edge resets a script instance
           InstanceName          STRING             Instance name
VAR_OUTPUT Done                  BOOL               Instance is reset
           Active                BOOL               Instance is reset
           Error                 BOOL               An error occurred
           ErrorID               ⮫ ERROR_CODE       Error classification
               ErrorIdent        ⮫ ERROR_STRUCT Error diagnostics

Functional description
At a rising edge at “Execute”, the IL_ResetInstance function block resets a
script instance to the "ERROR" state with the name specified at the “Instance‐
Name” input in the Data Layer.
After the script has been aborted, the instance is in the "INIT" state.
The Reset command can only be executed successfully if the instance is in
"ERROR" state.

## 29.9 IL_ReadInstanceDiagnostics

     Brief description
     The function block IL_ReadInstanceDiagnostics reads diagnostic information
     of a Python script instance in the Data Layer.

     Interface description

Table 800: Interface variables of the IL_ReadInstanceDiagnostics function block
I/O type   Name                     Data type         Description
VAR_INPUT  Execute                  BOOL              Rising edge reads diagnostic information
           InstanceName             STRING            Instance name
VAR_OUTPUT Done                     BOOL              Diagnostic information read successfully
           Active                   BOOL              Script is reset
           Error                    BOOL              An error occurred
           ErrorID                  ⮫ ERROR_CODE      Error classification
                   ErrorIdent       ⮫ ERROR_STRUCT Error diagnostics
                   LastMainDiag     UDINT            Main diagnostic number of the script
                   LastDetailDiag   UDINT            Detailed diagnostic number of the script
                   ErrorMessage     STRING(255)      Error message of the script
                   ErrorTrace       ARRAY [0..31] OF Error: Trace info of the script
                                    STRING(255)

     Functional description
     At a rising edge at "Execute", the IL_ReadInstanceDiagnostics function block
     reads the diagnostic information of a script instance with the same name
     specified at the “InstanceName” input in the Data Layer.
     The diagnostic information is retrieved from the Data Layer node /script/
     instances//[name]/diag.

## 29.10 IL_ReadInstanceState

     Brief description
     The function block IL_ReadInstanceState reads status information of a Python
     script instance in the Data Layer.

      Interface description

Table 801: Interface variables of the IL_ReadInstanceState function block
I/O type   Name                  Data type          Description
VAR_INPUT  Execute               BOOL               Rising edge reads instance status
           InstanceName          STRING             Instance name
VAR_OUTPUT Done                  BOOL               Instance status read successfully
           Active                BOOL               Instance status read
           Error                 BOOL               An error occurred
           ErrorID               ⮫ ERROR_CODE       Error classification
               ErrorIdent        ⮫ ERROR_STRUCT Error diagnostics
               State             INSTANCE_STATE Current instance status
               Script            STRING(255)      File name or string of the script
               MotionObjAtta‐    ARRAY [0..15] OF Motion object assigned to the instance
               chedTo            STRING
               Line              ULINT            Currently interpreted line. Not the line index
                                                  of the source file
               pid               UDINT            Process ID of this instance

      Functional description
      At a rising edge at "Execute", the IL_ReadInstanceState function block reads
      the status information of a script instance with the same name specified at
      the “InstanceName” input in the Data Layer.
      The diagnostic information is retrieved from the Data Layer node /script/
      instances//[name]/state.

## 29.11 IL_ScriptInstanceStatus

      Brief description
      The function block IL_ScriptInstanceStatus monitors the status and diagnostic
      information of a Python script instance in the Data Layer.

     Interface description

Table 802: Interface variables of the IL_ScriptInstanceStatus function block
I/O type   Name                     Data type           Description
VAR_INPUT  Enable                   BOOL                Rising edge reads instance status
           InstanceName             STRING              Instance name
VAR_OUTPUT InOperation              BOOL                Status of the instance is monitored
           Error                    BOOL                An error occurred
           ErrorID                  ⮫ ERROR_CODE        Error classification
                   ErrorIdent       ⮫ ERROR_STRUCT Error diagnostics
                   State            INSTANCE_STATE Current instance status
                   Script           STRING(255)      File name or string of the script
                   MotionObjAtta‐   ARRAY [0..15] OF Motion object assigned to the instance
                   chedTo           STRING
                   Line             ULINT            Currently interpreted line. Not the line index
                                                     of the source file
                   pid              UDINT            Process ID of this instance
                   LastMainDiag     UDINT            Main diagnostic number of the script
                   LastDetailDiag   UDINT            Detailed diagnostic number of the script
                   ErrorMessage     STRING(255)      Error message of the script
                   ErrorTrace       ARRAY [0..31] OF Error: Trace info of the script
                                    STRING(255)

     Functional description
     At a rising edge at "Enable", the IL_ScriptInstanceStatus function block moni‐
     tors the status and diagnostic information of a script instance with the same
     name specified at the “InstanceName” input in the Data Layer. The output
     values are refreshed every 100 ms.

## 29.12 INSTANCE_STATE

     Brief description
  The enumeration type INSTANCE_STATE maps the states of a script instance.
  The ⮫ IL_ScriptInstance uses it at the "State" output.
Table 803: States of the INSTANCE_STATE enumeration type
State                     Description
INIT                      The script instance was created and ready to start a script
READY                     Ready to start a script
FINISHED                  The script was completed without error code

State                  Description
ERROR                  Error while executing the script.
TERMINATED             The script execution was aborted
BUSY                   A script is executed
UNKNOWN                The script instance is in an unknown state

## 29.13 INSTANCE_RESET_CMD_STATE

Brief description
The enumeration type INSTANCE_RESET_CMD_STATE creates the states of a
Reset command sent to the script instance. The ⮫ IL_ScriptInstance uses it at
the "ResetState" output.

Table 804: States of the INSTANCE_RESET_CMD_STATE enumeration type
State                  Description
IDLE                   No Reset command is executed
ABORTING               Reset command is sent to the instance
DONE                   Reset command was executed successfully
ERROR                  Reset command could not be executed

## 29.14 INSTANCE_ABORT_CMD_STATE

Brief description
The enumeration type INSTANCE_ABORT_CMD_STATE creates the states of an
abort command sent to the script instance. The ⮫ IL_ScriptInstance uses it at
the "AbortState" output.
Table 805: States of the INSTANCE_ABORT_CMD_STATE enumeration type
State                  Description
IDLE                   No abort command is executed
ABORTING               Abort command is sent to the instance
DONE                   Abort command was executed successfully
ERROR                  Abort command could not be executed

## 29.15 Error codes

The library CXA_Datalayer reports the error codes.
For detailed descriptions of the error codes, refer to the ⮫ Table of the error
codes of the CXA_Datalayer library.
Table 806: Error codes
Additional1             DL_Result               Description             Possible cause
16#80010001             DL_INVALID_ADDRESS      NodeName is unknown ● “Rexroth-python” app
                                                or wrong                   is not installed
                                                                        ● Instance does not
                                                                           exist
16#80010010             DL_ALREADY_EXISTS       Node cannot be created, Instance already exists
                                                as it already exists

Additional1            DL_Result                  Description             Possible cause
16#80010011            DL_CREATION_FAILED         Error when creating the Reset, Abort or Start‐
                             new node                Script command is sent
                                                     if the instance is not in
                                                     the requested state:
                                                       ● Resetting the
                                                         instance if the
                                                         instance is not in the
                                                         "ERROR" state
                                                       ● Canceling the script
                                                         file if the instance is
                                                         already in the "INIT"
                                                         state
                                                       ● Starting the script
                                                         file if the instance
                                                         is neither in the
                                                         "INIT" state nor in the
                                                         "READY" state
