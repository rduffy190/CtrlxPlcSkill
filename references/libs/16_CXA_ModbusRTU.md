# 16 CXA_ModbusRTU

## 16.1 Introduction and overview

Use the CXA_ModbusRTU library with the ctrlX I/O modules XI521001/
XI522001 or with the S20 module S20-RS-Uni.
The ctrlX I/O modules XI521001/XI522001 are connected locally to a ctrlX
CORE plus/X5/X7 or to an EtherCAT bus coupler XB-EC-12.
The S20 module is connected to the S20-EC-BK EtherCAT bus coupler.

and EFC3600 frequency converter
(1) 1..n serial communication modules
(2) 1..x devices
The library CXA_ModbusRTU provides function blocks to communicate with
the Modbus RTU protocol as master or client.
For the <HW_ID>, "XI" ® replaces ID for the ctrlX I/O module IH_XIMBRTU‐
Master.
For the <HW_ID>, "S20" ® replaces ID for the S20 module IH_S20MBRTU‐
Master.

To start the PLC program with CXA_ModbusRTU, the function block
IH_<HW_ID>MBRTUSlave has to be instantiated for the client and the function
block IH_<HW_ID>MBRTUMaster for the master.
● The function block IH_<HW_ID>MBRTUMaster provides the communication
   handle for all other function blocks in the CXA_ModbusRTU library, e.g.
   IH_MBReadCoils, IH_MBWriteSingleCoil.
● The function block IH_<HW_ID>MBRTUSlave ensures the communication
   with a Modbus RTU master.
With IH_<HW_ID>MBRTUMaster and IH_<HW_ID>MBRTUSlave, direct data
exchange between two ctrlX CORE controls from Bosch Rexroth is possible.
Each function block with Modbus function code can be used in a single

request or in the polling mode. In polling mode, the polling interval can be
specified and the function block sends the requests automatically on time.
Pay attention if Modbus RTU with EFC frequency converters is used.
Currently, one Modbus RTU connection requires approx. 100 ms for sending
and receiving. Thus, 10 requests take 1 second.
Example:
5 Modbus RTU devices, 2 requests to each device = 10 requests
If high refresh rates are expected or if multiple Modbus RTU devices are used,
further serial S20 communication modules are required.
Other Modbus RTU applications might need less than 100 ms.

Table 261: Function blocks of the CXA_ModbusRTU library
Type                                    Description                                      Function
⮫ IH_MBGetCommEventCounter              Returns the status word and the communication       11
                                        event counter
⮫ IH_MBGetCommEventLog                  Returns the event log structure which includes      12
                                        the status word, communication event counter,
                                        message counter and a field of event bytes
⮫ IH_MBMaskWriteRegister                Modifies the content of a specified Holding reg‐    22
                                        ister using an AND mask, an OR mask and the
                                        current content of the register
⮫ IH_MBReadCoils                        Reads the ON or OFF value from 1 to 2000 coils,      1
                                        i.e. continuous output bits
⮫ IH_MBReadDeviceIdentification         Reads the ID and additional information on the      43
                                        physical and functional description of a remote
                                        device from the client (master)
⮫ IH_MBReadDiagnostics                  Provides tests to check the communication            8
                                        between master and slave or internally in the
                                        master
⮫ IH_MBReadDiscreteInputs               Read from 1 to 2000 neighboring status of dis‐       2
                                        crete inputs, bit data access
⮫ IH_MBReadExceptionStatus              Reads the diagnostic status byte (8 bits) of the     7
                                        Modbus RTU slave
⮫ IH_MBReadFIFOQue                      Reads the content of a First-In-First-Out (FIFO)    24
                                        register queue of a remote device
⮫ IH_MBReadFileRecord                   Reads the specified file information, subre‐        20
                                        quests are possible
⮫ IH_MBReadHoldingRegisters             Reads the content of a neighboring Holding reg‐      3
                                        ister block, word data access

Type                                     Description                                          Function
⮫ IH_MBReadInputRegisters                Reads from 1 to 125 neighboring input registers,         4
                    word data access
⮫ IH_MBReadWriteMultipleRegisters        Executes a read and a write operation in one            23
                    Modbus transaction. First, it is written, then it is
                    read
⮫ IH_S20MBRTUMaster                      Provides the communication handle for all other
                    function blocks in the CXA_ModbusRTU library,
                    e.g. IH_MBReadCoils, IH_MBWriteSingleCoil
                    Together with S20-RS-UNI
⮫ IH_S20MBRTUSlave                       Ensures the communication with a Modbus RTU
                    master, e.g. can be used to exchange data with
                    the IH_S20MBRTUMaster
                    Together with S20-RS-UNI
⮫ IH_XIMBRTUMaster                       Provides the communication handle for all other
                    function blocks in the CXA_ModbusRTU library,
                    e.g. IH_MBReadCoils, IH_MBWriteSingleCoil
                    Together with ctrlX I/O XI521001/XI522001
⮫ IH_XIMBRTUSlave                        Ensures the communication with a Modbus RTU
                    master, e.g. can be used to exchange data with
                    the IH_S20MBRTUMaster
                    Together with ctrlX I/O XI521001/XI522001
⮫ IH_MBWriteFileRecord                   Writes the specified file information, subre‐           21
                    quests are possible
⮫ IH_MBWriteMultipleCoils                Writes multiple ON or OFF values from 1 to              15
                    1968 coils, i.e. continuous output bits
⮫ IH_MBWriteMultipleRegisters            Writes multiple registers (1 to 123 registers),         16
                    word data access
⮫ IH_MBWriteSingleCoil                   Writes the ON or OFF value from 1 to 2000                5
                    coils, i.e. single output bit
⮫ IH_MBWriteSingleRegister               Writes a single Holding register, word data              6
                    access

## 16.2 IH_MBGetCommEventCounter

Function code
FC 11

Brief description
The function block IH_MBGetCommEventCounter calls a status word and the
number of events from the communication event counter of a slave device.
The function block has to be called using the Modbus master function block
⮫ IH_S20MBRTUMaster.

       Interface description

Table 262: Interface variables of the IH_MBGetCommEventCounter function block
I/O type       Name                 Data type         Description
VAR_INPUT      Enable               BOOL              Function block active if TRUE
               SendRequest          BOOL              A request is sent at a rising edge
                                                      Polling enabled
                                                      SendRequest does not have to be triggered
               EnablePoll           BOOL              at each interval
                                                      The function block sends requests automat‐
                                                      ically
               SlaveAddress         BYTE              Slave address
                                                      Polling interval
               PollInterval         TIME
                                                      Request is sent continuously at intervals
               TimeOut              TIME              Timeout interval for response from slaves
VAR_OUTPUT                                            Computation completed and starts again in
               Done                 BOOL
                                                      the next cycle
               Active               BOOL              Function block is active
               Error                BOOL              Indicates an error
               ErrorID              ⮫ ERROR_CODE      Error class
               ErrorIdent           ⮫ ERROR_STRUCT Detailed error information
                                                     True if the function block communicates
               Busy                 BOOL
                                                     with the master
               Status               WORD             Status word
               EventCount           WORD             Number of communication events
VAR_IN_OUT     MBData               ⮫ IH_INLN_MB_DAT Structure handles data between the master
                                    A                and other Modbus function blocks of the
                                                     function codes

Min./max. and default values
The following table lists the min./max. and default values as well as the
application behavior of the function block inputs.
Table 263: Min./max. and default values as well as the response of the function block inputs of
IH_MBGetCommEventCounter during application
Name               Data type       Min. value    Max. value       Default value   Effective
Enable             BOOL            FALSE         TRUE             FALSE           Continuous
                                                                                  Continuously      at
SendRequest        BOOL            FALSE         TRUE             FALSE
                                                                                  Enable
                                                                                  Continuously      at
EnablePoll         BOOL            FALSE         TRUE             FALSE
                                                                                  Enable
                                                                                  Rising    edge    at
SlaveAddress       BYTE            0             247              0
                                                                                  Enable
                                                                                  Continuously      at
PollInterval       TIME            T#1s          -------------    T#1s
                                                                                  Enable
                                                                                  Rising    edge    at
TimeOut            TIME            T#1s          --------------   T#1s
                                                                                  Enable

Functional description
The function block IH_MBGetCommEventCounter (FC 11) calls a status word
and the number of events from the communication event counter of a slave
device. The function block has to be called using the Modbus master function
block. "MBData" has to be linked to the master function block in the program.
It is used for communication purposes and data exchange.
The event counter of the device is incremented by one for each successfully
completed message. It is not incremented for exception responses, polling
commands or commands to the event counter.
The normal response contains a two-byte status word and a two–byte number
of events. The status word consists only of ones (FF FF hex) if a previously
issued program command is still being executed by the remote device (if the
device is busy). Otherwise, the status word consists only of zeros.
The function block is enabled after the first PLC cycle by setting the "Enable"
input to TRUE. The "Active" output is set to TRUE during operation. The bit
"Done" is set to TRUE upon completion. If an error results during the oper‐
ation, the "Error" bit is set to TRUE. "ErrorID" and "ErrorIdent" show error
information. The error can be acknowledged via a rising edge at the "Enable"
input.
Example of a function block
The function block IH_MBGetCommEventCounter has to be instantiated
together with the IH_MBRTUMaster to communicate with the Modbus slave.
Use a common variable for "MBData" of the IH_MBGetCommEventCounter and
IH_MBRTUMaster function blocks to exchange data with the Modbus slave.
In this example, the function block IH_MBGetCommEventCounter is used to
retrieve the status word and number of events of the slave with address 1.
The two function blocks IH_MBRTUMaster and IH_MBGetCommEventCounter
are enabled with a rising edge at the "bSendRequest" input. The function
block reads the status word and the number of events of slave address 1 and
the result is saved in "wStatus" and "wEventCount".
If "bEnablePoll" variable is set to TRUE and "PollInterval" to more than 1
second, data is read from the slave at regular intervals.

Variable declaration

VAR
  fbIH_MBGetCommEventCounter: IH_MBGetCommEventCounter;
  bEnable: BOOL;
  bEnablePoll: BOOL;
  bSendRequest: BOOL;
  stMBData: IH_INLN_MB_DATA;
  bDone: BOOL;
  bActive: BOOL;
  bError: BOOL;
  enErrorID: ERROR_CODE;
  stErrorIdent: ERROR_STRUCT;
  bBusy: BOOL;

  wStatus: WORD;
  wEventCount: WORD;
END_VAR

Implementation

fbIH_MBGetCommEventCounter(
  Enable:= bEnable,
  SendRequest:= bSendRequest,
  EnablePoll:= bEnablePoll,
  SlaveAddress:= BYTE#1,
  PollInterval:= T#1S,
  TimeOut:= T#1S,
  MBData:= stMBData,
  Done=> bDone,
  Active=> bActive,
  Error=> bError,
  ErrorID=> enErrorID,
  ErrorIdent=> stErrorIdent,
  Busy=> bBusy,
  Status=> wStatus,
  EventCount=> wEventCount);

## 16.3 IH_MBGetCommEventLog

Function code
FC 12

Brief description
The function block IH_MBGetCommEventLog is used to retrieve a status word,
number of events, number of messages and the field of event bytes in the
short log of the event communication from the slave module.
The function block has to be called using the Modbus master function block
⮫ IH_S20MBRTUMaster.

       Interface description

Table 264: Interface variables of the IH_MBGetCommEventLog function block
I/O type           Name                 Data type         Description
VAR_INPUT          Enable               BOOL              Function block active if TRUE
                   SendRequest          BOOL              A request is sent at a rising edge
                                                          Polling enabled
                                                          SendRequest does not have to be triggered
                   EnablePoll           BOOL              at each interval
                                                          The function block sends requests automat‐
                                                          ically
                   SlaveAddress         BYTE              Slave address
                                                          Polling interval
                   PollInterval         TIME
                                                          Request is sent continuously at intervals
                   TimeOut              TIME              Timeout interval for response from slaves
VAR_OUTPUT                                                Computation completed and starts again in
                   Done                 BOOL
                                                          the next cycle
                   Active               BOOL              Function block is active
                   Error                BOOL              Indicates an error
                   ErrorID              ⮫ ERROR_CODE      Error class
                   ErrorIdent           ⮫ ERROR_STRUCT Detailed error information
                                                         True if the function block communicates
                   Busy                 BOOL
                                                         with the master
                                                         The structure contains additional informa‐
                                        ⮫ IH_INLN_MB_EVE
                   EventLog                              tion on Status, EventCount, MessageCount
                                        NTLOG
                                                         and Events
VAR_IN_OUT         MBData               ⮫ IH_INLN_MB_DAT Structure handles data between the master
                                        A                and other Modbus function blocks

Min./max. and default values
The following table lists the min./max. and default values as well as the
application behavior of the function block inputs.
Table 265: Min./max. and default values as well as the response of the function block inputs of
IH_MBGetCommEventLog during application
Name            Data type       Min. value       Max. value       Default value   Effective
Enable          BOOL            FALSE            TRUE             FALSE           Continuous
                                                                                  Continuously     at
SendRequest     BOOL            FALSE            TRUE             FALSE
                                                                                  Enable
                                                                                  Continuously     at
EnablePoll      BOOL            FALSE            TRUE             FALSE
                                                                                  Enable

                                                             Rising    edge   at
SlaveAddress    BYTE            0                247              0
                                                             Enable
                                                             Continuously     at
PollInterval    TIME            T#1s             -------------    T#1s
                                                             Enable
                                                             Rising    edge   at
TimeOut         TIME            T#1s             --------------   T#1s
                                                             Enable

Functional description
The function block IH_MBGetCommEventLog (FC 12) is used to retrieve a
status word, number of events, number of messages and the field of event
bytes in the short log of the event communication from the slave module.
The function block has to be called using the Modbus master function block.
"MBData" has to be linked to the master function block in the program. It is
used for communication purposes and data exchange.
Status word and number of events are identical to the data (11, 16#0B)
output using the function "Get Communications Event Counter".
The message counter contains the number of messages processed by the
remote device since the device was restarted, switched on or since the
counter was deleted. The number is identical to the number provided by the
diagnostic function (code 08), subfunction "Return Bus Message Count" (code
11, 0B hex).
The event byte array contains 0-64 bytes. Each byte corresponds to the status
of a MODBUS operation for sending or receiving by a remote device. The
remote device enters the events chronologically into the field. Byte 0 contains
the last event. A new byte always overwrites the oldest byte in the field.
Content of the event byte
The function "Get Communications Event Log" returns four types of event
bytes. The type of bit 7 (high-order bit) is defined in each byte. It can also be
defined by bit 6. This is explained in the following.
MODBUS receiving event in the remote device
The remote device saves this type as event byte if a message is received
with a query. It is saved before the remote device processes the message.
The event is defined with bit 7 = "1". The other bits are "1" if the respective
condition is true (TRUE). The bits are split as follows:

Table 266: Bit content
Bit      Description
0        Not used
1        Communication error
2        Not used
3        Not used
4        Character overflow
5        Currently in "Listen Only" mode
6        Received broadcast commands
7        1
MODBUS sending event in the remote device
The remote device saves this type of event byte if a message was processed
with a query. It is saved if the remote device returns either a normal response,
an exception as response or no response at all. The event is defined by bit 7
= "0" and bit 6 = "1". The other bits are "1" if the respective condition is true
(TRUE).
The bits are split as follows:
Table 267: Bit content
Bit      Description
0        Read exceptions sent (exception code 1-3)
1        Slave abort exception sent (exception code 4)
2        Slave busy exception sent (exception code 5-6)
3        Slave program NAK exception sent (exception code 7)
4        Timeout error during writing
5        Currently in "Listen Only" mode
6        1
7        0
The function block is enabled after the first PLC cycle by setting the "Enable"
input to TRUE. The "Active" output is set to TRUE during operation. The bit
"Done" is set to TRUE upon completion. If an error results during the oper‐
ation, the "Error" bit is set to TRUE. "ErrorID" and "ErrorIdent" show error
information. The error can be acknowledged via a rising edge at the "Enable"
input.
Example of a function block
The function block IH_MBGetCommEventLog has to be instantiated together
with the IH_MBRTUMaster to communicate with the Modbus slave. Use
a common variable for "MBData" of the IH_MBGetCommEventLog and
IH_MBRTUMaster function blocks to exchange data with the Modbus slave.
In this example, the function block IH_MBGetCommEventLog is used to
retrieve the log of the slave with address 1.
The two function blocks IH_MBRTUMaster and IH_MBGetCommEventLog are
enabled with a rising edge at the "bSendRequest" input. The function block
reads the status word and the number of events of slave address 1 and the
result is saved in the "stEventLog".
If "bEnablePoll" variable is set to TRUE and "PollInterval" to more than 1
second, data is read from the slave at regular intervals.
After each successful read operation, the bit "Done" is set to TRUE for one
PLC cycle.

Variable declaration

VAR
  fbIH_MBGetCommEventLog: IH_MBGetCommEventLog;
  bEnable: BOOL;
  bSendRequest: BOOL;
  bEnablePoll: BOOL;
  stMBData: IH_INLN_MB_DATA;
  bDone: BOOL;
  bActive: BOOL;
  bError: BOOL;
  enErrorID: ERROR_CODE;
  stErrorIdent: ERROR_STRUCT;
  bBusy: BOOL;

  stEventLog: IH_INLN_MB_EVENTLOG;
END_VAR

Implementation

fbIH_MBGetCommEventLog(
  Enable:= bEnable,
  SendRequest:= bSendRequest,
  EnablePoll:= bEnablePoll,
  SlaveAddress:= BYTE#1,
  PollInterval:= T#1S,
  TimeOut:= T#1S,
  MBData:= stMBData,
  Done=> bDone,
  Active=> bActive,
  Error=> bError,
  ErrorID=> enErrorID,
  ErrorIdent=> stErrorIdent,
  Busy=> bBusy,
  Eventlog=> stEventLog);

Response of event protocol
In this example, the status word is 16#0000, i.e. the remote device does not
process a program function. The event counter shows that the remote device
counted 264 (16#0108). The message counter indicates that 289 (16#0121)
were processed.
The latest communication event is shown in the event byte 0. Its content is 32
(16#20), i.e. the remote device recently entered the "Listen Only" mode.
The previous communication event is shown in the event byte 1. Its content
(00 hex) shows that the communication of the remote device was restarted.

## 16.4 IH_MBMaskWriteRegister

Function code
FC 22

Brief description
The function block IH_MBMaskWriteRegister is used to change a specific
Holding register with an AND mask, an OR mask and the registers of the slave
module.
The function block has to be called using the Modbus master function block
⮫ IH_S20MBRTUMaster.

       Interface description

Table 268: Interface variables of the IH_MBMaskWriteRegister function block
I/O type       Name                 Data type         Description
VAR_INPUT      Enable               BOOL              Function block active if TRUE
               SendRequest          BOOL              A request is sent at a rising edge
                                                      Polling enabled
                                                      SendRequest does not have to be triggered
               EnablePoll           BOOL              at each interval
                                                      The function block sends requests automat‐
                                                      ically
               SlaveAddress         BYTE              Slave address
               StartAddress         WORD              Start address of the Holding register
               ANDMask              WORD              AND mask value
               ORMask               WORD              OR mask value
                                                      Polling interval
               PollInterval         TIME
                                                      Request is sent continuously at intervals
               TimeOut              TIME              Timeout interval for response from slaves
VAR_OUTPUT                                            Computation completed and starts again in
               Done                 BOOL
                                                      the next cycle
               Active               BOOL              Function block is active
               Error                BOOL              Indicates an error
               ErrorID              ⮫ ERROR_CODE      Error class
               ErrorIdent           ⮫ ERROR_STRUCT Detailed error information
               Busy                 BOOL             True if the function block communicates
                                                     with the master
VAR_IN_OUT     MBData               ⮫ IH_INLN_MB_DAT Structure handles data between the master
                                    A                and other Modbus function blocks of the
                                                     function codes

Min./max. and default values
The following table lists the min./max. and default values as well as the
application behavior of the function block inputs.
Table 269: Min./max. and default values as well as the response of the function block inputs of
IH_MBMaskWriteRegister during application
Name               Data type       Min. value    Max. value       Default value   Effective
Enable             BOOL            FALSE         TRUE             FALSE           Continuous
                                                                                  Continuously      at
SendRequest        BOOL            FALSE         TRUE             FALSE
                                                                                  Enable
                                                                                  Continuously      at
EnablePoll         BOOL            FALSE         TRUE             FALSE
                                                                                  Enable
                                                                                  Rising    edge    at
SlaveAddress       BYTE            0             247              0
                                                                                  Enable
                                                                                  Rising    edge    at
StartAddress       WORD            0             65535            0
                                                                                  Enable
                                                                                  Rising    edge    at
ANDMask            WORD            0             65535            0
                                                                                  Enable
                                                                                  Rising    edge    at
ORMask             WORD            0             65535            0
                                                                                  Enable
                                                                                  Continuously      at
PollInterval       TIME            T#1s          -------------    T#1s
                                                                                  Enable
                                                                                  Rising    edge    at
TimeOut            TIME            T#1s          --------------   T#1s
                                                                                  Enable

Functional description
The function block IH_MBMaskWriteRegister (FC22) is used to change a spe‐
cific Holding register with an AND mask, an OR mask and the registers of
the slave module. Use the function to set or delete individual bits in or from
the register. The function block has to be called using the Modbus master
function block. "MBData" has to be linked to the master function block to
communicate with the master and to exchange data.
The function block is enabled after the first PLC cycle by setting the "Enable"
input to TRUE. The "Active" output is set to TRUE during operation. The bit
"Done" is set to TRUE upon completion. If an error results during the oper‐
ation, the "Error" bit is set to TRUE. "ErrorID" and "ErrorIdent" show error
information. The error can be acknowledged via a rising edge at the "Enable"
input.
Example of a function block
The function block IH_MBMaskWriteRegister has to be instantiated together
with the IH_MBRTUMaster to communicate with the Modbus slave. The input/
output variable "stMBData" exchanges data between the function blocks
IH_MBRTUMaster and IH_MBMaskWriteRegister. Thus, this variable has to be
assigned to "MBData" to both function blocks.
In the example, the function block IH_MBMaskWriteRegister applies a mask on
a register of the slave device.
Masking register with SendRequest condition
IH_MBMaskWriteRegister is used to mask a register of the address 100 in
slave address 2 with "bSendRequest" as BOOL variable to trigger register
masking.

Variable declaration

VAR
  fbIH_MBMaskWriteRegister: IH_MBMaskWriteRegister;
  bEnable: BOOL;
  bSendRequest: BOOL;
  stMBData: IH_INLN_MB_DATA;
  bDone: BOOL;
  bActive: BOOL;
  bError: BOOL;
  enErrorID: ERROR_CODE;
  stErrorIdent: ERROR_STRUCT;
  bBusy: BOOL;
END_VAR

Implementation

fbIH_MBMaskWriteRegister(
  Enable:= bEnable,
  SendRequest:= bSendRequest,
  EnablePoll:= FALSE,
  SlaveAddress:= BYTE#2,
  StartAddress:= WORD#100,
  ANDMask:= WORD#16#F2,
  ORMask:= WORD#16#25,
  PollInterval:= T#2S,
  TimeOut:= T#2S,
  MBData:= stMBData,
  Done=> bDone,
  Active=> bActive,
  Error=> bError,
  ErrorID=> enErrorID,
  ErrorIdent=> stErrorIdent,
  Busy=> bBusy);

## 16.5 IH_MBReadCoils

Function code
FC 1

Brief description
The function block IH_MBReadCoils detects whether coils have the status ON
or OFF, i.e. it reads the output bits of the slave module.
The function block has to be called using the Modbus master function block
⮫ IH_S20MBRTUMaster.

       Interface description

Table 270: Interface variables of the IH_MBReadCoils function block
I/O type           Name                 Data type         Description
VAR_INPUT          Enable               BOOL              Function block active if TRUE
                   SendRequest          BOOL              A request is sent at a rising edge
                                                          Polling enabled
                                                          SendRequest does not have to be triggered
                   EnablePoll           BOOL              at each interval
                                                          The function block sends requests automat‐
                                                          ically
                   SlaveAddress         BYTE              Slave address
                   StartAddress         WORD              Start address of the output bits
                   NoOfCoils            UINT              Number of coils (separate outputs)
                                        POINTER        TO Address of the array to save the read value
                   ValueAdr             ARRAY[0..1999]    of the output bit
                                        OF BOOL           Use the ADR () operator
                                                          Size of the Value array
                   SizeOfValue          UINT
                                                          Use the SIZEOF () operator
                                                          Polling interval. Request is sent continu‐
                   PollInterval         TIME
                                                          ously at intervals
                   TimeOut              TIME              Timeout interval for response from slaves
VAR_OUTPUT                                                Computation completed and starts again in
                   Done                 BOOL
                                                          the next cycle
                   Active               BOOL              Function block is active
                   Error                BOOL              Indicates an error
                   ErrorID              ⮫ ERROR_CODE      Error class
                   ErrorIdent           ⮫ ERROR_STRUCT Detailed error information
                   Busy                 BOOL           True if the function block communicates
                                                       with the master
VAR_IN_OUT         MBData               ⮫ IH_INLN_MB_DAT Structure handles data between the master
                                        A                and other Modbus function blocks

Min./max. and default values
The following table lists the min./max. and default values as well as the
application behavior of the function block inputs.
Table 271: Min./max. and default values as well as the response of the function block inputs of
IH_MBReadCoils during application
Name            Data type       Min. value      Max. value       Default value     Effective
Enable          BOOL            FALSE           TRUE             FALSE             Continuous
                                                                                   Continuously     at
SendRequest     BOOL            FALSE           TRUE             FALSE
                                                                                   Enable
                                                                                   Continuously     at
EnablePoll      BOOL            FALSE           TRUE             FALSE
                                                                                   Enable

                                                              Rising    edge   at
SlaveAddress    BYTE            0               247              0
                                                              Enable
                                                              Rising    edge   at
StartAddress    WORD            0               65535            0
                                                              Enable
                                                              Rising    edge   at
NoOfCoils       UINT            1               2000             1
                                                              Enable
                                                              Rising    edge   at
SizeOfValue     UINT            1               2000             -------------
                                                              Enable
                                                              Continuously     at
PollInterval    TIME            T#1s            -------------    T#1s
                                                              Enable
                                                              Rising    edge   at
TimeOut         TIME            T#1s            --------------   T#1s
                                                              Enable

Functional description
The function block IH_MBReadCoils (FC 1) reads the status from 1 to 2000
coils, i.e. continuous subsequent output bits of the slave module. The func‐
tion block has to be called using the Modbus master function block. "MBData"
has to be linked to the master function block in the program. It is used for
communication purposes and data exchange.
The function block is enabled after the first PLC cycle by setting the "Enable"
input to TRUE. The "Active" output is set to TRUE during operation. The bit
"Done" is set to TRUE upon completion. If an error results during the oper‐
ation, the "Error" bit is set to TRUE. "ErrorID" and "ErrorIdent" show error
information. The error can be acknowledged via a rising edge at the "Enable"
input.
Example of a function block
The function block IH_MBReadCoils has to be instantiated together with the
function block IH_MBRTUMaster to communicate with the Modbus slave. The
input/output variable "stMBData" exchanges data between the function blocks
IH_MBRTUMaster and IH_MBReadCoils. Thus, this variable has to be assigned
to "MBData" to both function blocks.
In the example, the function block IH_MBReadCoils is used to retrieve coils of
the slave device.
Reading coils with SendRequest condition
IH_MBReadCoils is used to read 8 coils of the start address 0x1000 of slave
address 2 with "bSendRequest" as BOOL variable to trigger coil reading.

Variable declaration

VAR
fbIH_MBReadCoils: IH_MBReadCoils;
bEnable: BOOL;
bSendRequest: BOOL;
arReadCoils: ARRAY [0..20] OF BOOL;
stMBData: IH_INLN_MB_DATA;
bDone: BOOL;
bActive: BOOL;
bError: BOOL;
enErrorID: ERROR_CODE;
stErrorIdent: ERROR_STRUCT;
bBusy: BOOL;
END_VAR

Implementation

fbIH_MBReadCoils(
Enable:= bEnable,
SendRequest:= bSendRequest,
EnablePoll:= FALSE,
SlaveAddress:= BYTE#2,
StartAddress:= WORD#1000,
NoOfCoils:= UINT#8,
ValueAdr:= ADR(arReadCoils),
SizeOfValue:= SIZEOF(arReadCoils),
PollInterval:= T#2S,
TimeOut:= T#2S,
MBData:= stMBData,
Done=> bDone,
Active=> bActive,
Error=> bError,
ErrorID=> enErrorID,
ErrorIdent=> stErrorIdent,
Busy=> bBusy);

Reading coils with PollIntervall condition
IH_MBReadCoils is used to read 5 coils of the start address 0x0500 of slave
address 5 with "PollInterval" (3 seconds) to trigger coil reading.

Variable declaration

VAR
  fbIH_MBReadCoils2: IH_MBReadCoils;
  bEnable2: BOOL;
  arReadCoils2: ARRAY [0..4] OF BOOL;
 stMBData: IH_INLN_MB_DATA;
  bDone2: BOOL;
  bActive2: BOOL;
  bError2: BOOL;
  enErrorID2: ERROR_CODE;
  stErrorIdent2: ERROR_STRUCT;
  bBusy2: BOOL;
END_VAR

Implementation

fbIH_MBReadCoils2(
  Enable:= bEnable2,
  SendRequest:= FALSE,
  EnablePoll:= TRUE,
  SlaveAddress:= BYTE#5,
  StartAddress:= WORD#500,
  NoOfCoils:= UINT#5,
  ValueAdr:= ADR(arReadCoils2),
  SizeOfValue:= SIZEOF(arReadCoils2),
  PollInterval:= T#3S,
  TimeOut:= T#2S,
  MBData:= stMBData,
  Done=> bDone2,
  Active=> bActive2,
  Error=> bError2,
  ErrorID=> enErrorID2,
  ErrorIdent=> stErrorIdent2,
  Busy=> bBusy2);

## 16.6 IH_MBReadDeviceIdentification

Function code
FC 43

Brief description
The function block IH_MBReadDeviceIdentification uses FC 43(0x2B) with MEI
(MODBUS Encapsulated Interface), type 14 (0x0E) to retrieve the ID and
additional information on the physical and functional description of a remote
device from the client (master).
It is recommended to call the function block using the Modbus master func‐
tion block ⮫ IH_S20MBRTUMaster.

       Interface description

Table 272: Interface variables of the IH_MBReadDeviceIdentification function block
I/O type           Name                 Data type       Description
VAR_INPUT          Enable               BOOL            Function block running if TRUE
                   SendRequest          BOOL            A rising edge sends a request
                   SlaveAddress         BYTE            Slave address
                                                        Parameter to define access types of the
                                        ⮫ IH_INLN_MB_DE
                   DeviceIdCode                         available object IDs (reading out the ID
                                        V_IDCODE
                                                        code of the device)
                   ObjectId             BYTE            Data object identification (object ID)
                   ValueAdr             POINTER TO BYTE Object address
                   SizeOfValue          UINT            Object size
                                                        Timeout interval during which the slave
                   TimeOut              TIME
                                                        responds
VAR_OUTPUT                                              Computation completed. Restarted in the
                   Done                 BOOL
                                                        next cycle
                   Active               BOOL            Function block is active
                   Error                BOOL            Indicates error
                   ErrorID              ⮫ ERROR_CODE      Error class
                   ErrorIdent           ⮫ ERROR_STRUCT Detailed error information
                   Busy                 BOOL           TRUE if the function block communicates
                                                       with the master
                   ConformityLevel      BYTE           Identification conformity level of the device
                                                       and the type of the supported access
                                                       Number of identification objects returned in
                   NoOfObjects          BYTE
                                                       the response
                                                       Total data size of the requested elements
                                                       "DeviceIdCode" or "ObjectId" in bytes
                   ObjectSize           WORD           ObjectSize = (ObjectId (1 byte) + object
                                                       length (1 byte) + value in Objectlength) *
                                                       NoOfObjects
                                                       VendorName returned by the object ID:
                   VendorName           STRING
                                                       0x00
                                                       ProductCode returned by the object ID:
                   ProductCode          STRING
                                                       0x01

I/O type       Name                Data type        Description
MajorMinorRevi‐                      MajorMinorRevision returned by the object
                    STRING
sion                                 ID: 0x02
VendorUrl           STRING           VendorUrl returned by the object ID: 0x03
                                     ProductName returned by the object ID:
ProductName         STRING
                                     0x04
ModelName           STRING           ModelName returned by the object ID: 0x05
UserApplication‐                     UserApplicationName returned by the
                    STRING
Name                                 object ID: 0x06
VAR_IN_OUT     MBData              ⮫ IH_INLN_MB_DAT Structure used to manage data between the
                    A                master, other Modbus function blocks and

                                     the function code

      Min./max. and default values
    The following table lists the min./max. and default values as well as the
    response of the function block inputs during application.
Table 273: Min./max. and default values as well as the response of the function block inputs of
IH_MBReadDeviceIdentification during application
                                                              Default
Name          Data type           Min. value   Max. value                  Application
                                                              value
Enable      BOOL             FALSE             TRUE           FALSE        Continuous
SendRequest BOOL             FALSE             TRUE           FALSE        Continuously at Enable
SlaveAd‐
            BYTE             0                 247            0            Rising edge at Enable
dress
DeviceId‐   IH_INLN_MB_DEV_I
                             1                 4              1            Rising edge at Enable
Code        DCODE
ObjectId    BYTE             16#00             16#FF          16#00        Rising edge at Enable
ValueAdr    POINTER TO BYTE Not defined        Not defined 0               Continuously at Enable
                                               Depends on
                                               the    device
SizeOfValue UINT                  0                           0            Rising edge at Enable
                                               object    size
                                               of the slave
Timeout       TIME                T#0ms        T#3600s        T#1s         Rising edge at Enable

Functional description
The function block IH_MBReadDeviceIdentification uses FC 43(0x2B) with MEI
(MODBUS Encapsulated Interface), type 14 (0x0E) to retrieve the ID and
additional information on the physical and functional description of a remote
device from the client (master).
Addressable data objects retrieve the device identification. The data objects
are addressed using the object ID.
Use the function block to access the following data object directories:
● Basic device identification:
   All objects of this category have to be available:
   "VendorName", "ProductCode" and change version
● General device identification:
   All objects of these categories are defined in the standard. The implemen‐
   tation is optional.
● Extended device identification:
   Provides the additional and optional identification and the private descrip‐
   tion data on the device. All devices are dependent and optional.
The supported data objects are shown with the object ID and the categories
in the following table.
Object ID     Object name/description                         Data type   M/O            Category
16#00         VendorName                                      STRING      Mandatory      Basis
                                                    field
16#01         ProductCode                                     STRING      Mandatory
                                                    field
16#02         MajorMinorRevision                              STRING      Mandatory
                                                    field
16#03         VendorUrl                                       STRING      Optional       Regular
16#04         ProductName                                     STRING      Optional
16#05         ModelName                                       STRING      Optional
16#06         UserApplicationName                             STRING      Optional
16#07         Reserved                                                    Optional
...
16#7F
16#80         Private objects can be defined optionally       Device-   Optional         Extended
...           The range [16#80 - 16#FF] is product-           dependent
16#FF         dependent
Access levels of the object category are specified in the "DeviceIdCode" input.
The function block supports the following "Read Device ID Code" access
types:
● 01: IH_INLN_MB_READ01 - Requests the basic device identification (access
   via stream)
● 02: IH_INLN_MB_READ02 - Requests the regular device identification
   (access via stream)
● 03: IH_INLN_MB_READ03 - Requests the extended device identification
   (access via stream)
● 04: IH_INLN_MB_READ04 - Requests a specific identification object (cus‐
   tomized access)
For the customized object ID access "DeviceIdCode" as IH_INLN_MB_READ04,
enter the object ID at the "ObjectId" input. The ObjectId should be 0 for all
other ID codes of the devices.

Objects with the defined data type in the basis and regular categories are
handled as direct function block outputs, e.g. "VendorName", "ProductCode"
… "UserApplicationName". All other device-dependent objects are processed
by default as "Byte" data type via "ValueAdr".
For ObjectIDs greater than 7, read data is available in "ValueAdr". "ValueAdr"
contains "ObjectID", "ObjectSize" and the object value.
If there are multiple objects, data is saved in the following format. For the
valid data size, refer to "ObjectSize".

The output "ConformityLevel" specifies the actual identification conformity
level of the device and the supported access type of the requested inputs
"ObjectId" and "DeviceIdCode".
The following information is returned in "ConformityLevel":
●  0x01: Basic identification (access only via stream)
●  0x02: Regular identification (access only via stream)
●  0x03: Extended identification (access only via stream)
●  0x81: Basic identification (access via stream and customized access)
●  0x82: Regular identification (access via stream and customized access)
●  0x83: Extended identification (access via stream and customized access)
Der output "NoOfObjects" indicates the number of returned identification
objects if "DeviceIdCode" is requested.
For DeviceIdCode = IH_INLN_MB_READ04, "NoOfObjects" is always 1.
The size of the object IDs 0x07…0xFF have to be identifiable in the device
data sheet and the desired length has to be assigned to complete the data.
This function block is called using the MODBUS master function block.
"MBData" links the master function block in the program. "MBData" is a
general structure to communicate between these two function blocks and to
exchange data.
The rising edge at the Enable inputs starts the process. If the process is
successful, the "Done" output is set to TRUE. If an error occurs, the "Error" bit
is set and detailed error information is provided in "ErrorID" and "ErrorIdent".

Special features
This function block is only tested with a CIMS sensor and not with other
devices that supported the function code 43.
Even though the function block supports retrieving the device ID codes from
IH_INLN_MB_READ01 to IH_INLN_MB_READ04, the CIMS sensor supports only
IH_INLN_MB_READ04. No tests were preformed for other device ID codes.

Example 1: Communication with the Bosch Rexroth sensor

Declaration

VAR
fbIH_MBReadDeviceIdentification:
IH_MBReadDeviceIdentification;
bEnable: BOOL;
bDone: BOOL;
bActive: BOOL;
bError: BOOL;
enErrorID: ERROR_CODE;
stErrorIdent: ERROR_STRUCT;
bSendRequest: BOOL;
bySlaveAddress: BYTE := 162;
enDeviceIDCode: IH_INLN_MB_DEV_IDCODE :=
IH_INLN_MB_DEV_IDCODE.IH_INLN_MB_READ_DEVID_04;
byObjectID: BYTE := 0;
arValueAdr: array[0..30] of byte;
bBusy: BOOL;
byConformityLevel: BYTE;
byNoOfObjects: BYTE;
wObjectSize: WORD;
strVendorName: STRING;
strProductCode: STRING;
strMajorMinorRevision: STRING;
strVendorUrl: STRING;
strProductName: STRING;
strModelName: STRING;
strUserApplicationName: STRING;
END_VAR

Implementation

fbIH_MBReadDeviceIdentification(
Enable:= bEnable,
Done=> bDone,
Active=> bActive,
Error=> bError,
ErrorID=> enErrorID,
ErrorIdent=> stErrorIdent,
SendRequest:= bSendRequest,
SlaveAddress:= bySlaveAddress,
DeviceIdCode:= enDeviceIDCode,
ObjectId:= byObjectID,
ValueAdr:= ADR(arValueAdr),
SizeofValue:= SIZEOF(arValueAdr),
TimeOut:= T#2S,
Busy=> bBusy,
ConformityLevel=> byConformityLevel,
NoOfObjects=> byNoOfObjects,
ObjectSize=> wObjectSize,
VendorName=> strVendorName,
ProductCode=> strProductCode,
MajorMinorRevision=> strMajorMinorRevision,
VendorUrl=> strVendorUrl,
ProductName=> strProductName,
ModelName=> strModelName,
UserApplicationName=> strUserApplicationName,
MBData:= stMBData);

Example 2:

Declaration

VAR
byObjectID: BYTE := 16#90; // Read order number in CIMS Sensor.
END_VAR

## 16.7 IH_MBReadDiagnostics

Function code
FC 8

Brief description
The function block IH_MBReadDiagnostics provides a number of tests to
check the communication system between a client (master) and a server
(slave) or to check different internal error conditions of a server in the RTU
mode.
The function block has to be called using the Modbus master function block
⮫ IH_S20MBRTUMaster.

       Interface description

Table 274: Interface variables of the IH_MBReadDiagnostics function block
I/O type       Name                 Data type         Description
VAR_INPUT      Enable               BOOL              Function block active if TRUE
               SendRequest          BOOL              A request is sent at a rising edge
                                                      Polling enabled.
                                                      SendRequest does not have to be triggered
               EnablePoll           BOOL              at each interval.
                                                      The function block sends requests automat‐
                                                      ically
               SlaveAddress         BYTE              Slave address
               SubFunc              WORD              Subfunction code
               Data                 WORD              Data field
                                                      Polling interval
               PollInterval         TIME
                                                      Request is sent continuously at intervals
               TimeOut              TIME              Timeout interval for response from slaves
VAR_OUTPUT                                            Computation completed and starts again in
               Done                 BOOL
                                                      the next cycle
               Active               BOOL              Function block is active
               Error                BOOL              Indicates an error
               ErrorID              ⮫ ERROR_CODE      Error class
               ErrorIdent           ⮫ ERROR_STRUCT Detailed error information
               Busy                 BOOL           True if the function block communicates
                                                   with the master
               RecvSubFunc          WORD           Subfunction code received by the device
               RecvData             WORD           Response data from the device
VAR_IN_OUT     MBData               ⮫ IH_INLN_MB_DAT Structure handles data between the master
                                    A                and other Modbus function blocks

Min./max. and default values
The following table lists the min./max. and default values as well as the
application behavior of the function block inputs.
Table 275: Min./max. and default values as well as the response of the function block inputs of
IH_MBReadDiagnostics during application
Name               Data type       Min. value   Max. value       Default value   Effective
Enable             BOOL            FALSE        TRUE             FALSE           Continuous
                                                                                 Continuously      at
SendRequest        BOOL            FALSE        TRUE             FALSE
                                                                                 Enable
                                                                                 Continuously      at
EnablePoll         BOOL            FALSE        TRUE             FALSE
                                                                                 Enable
                                                                                 Rising    edge    at
SlaveAddress       BYTE            0            247              0
                                                                                 Enable
                                                                                 Continuously      at
PollInterval       TIME            T#1s         -------------    T#1s
                                                                                 Enable
                                                                                 Rising    edge    at
TimeOut            TIME            T#1s         --------------   T#1s
                                                                                 Enable

Functional description
The function block IH_MBReadDiagnostics provides a number of tests to
check the communication system between a client (master) and a server
(slave) or to check different internal error conditions of a server. In the
request, the function uses one field for a 2-byte subfunction code to define
the tests to be executed. The server repeats the function code and the sub‐
function code in a normal response. In case of some diagnostics, data from
a removed device is returned in the data field of a normal response. The func‐
tion block has to be called using the Modbus master function block. "MBData"
has to be linked to the master function block in the program. It is used for
communication purposes and data exchange.
Serial devices support the following subfunction codes:

        Subfunction
Diagnostics name                            Data (requested)     Data (response)
        code
Return Query Data            16#0000    ANY                      Repeat request data
Restart Communications                  16#0000           (or)
    16#0001                                 Repeat request data
Option                                  16#FF00
Return Diagnostic Reg‐
    16#0002        16#0000                  Content of the diagnostic register
ister
Change     ASCII   Input
    16#0003        CHAR 00                  Repeat request data
Delimiter
Force Listen Only Mode 16#0004          16#0000                  No response
    16#05        …
RESERVED                                ------------             -------------
    16#09
Clear Counters and Diag‐
    16#000A        16#0000                  Repeat request data
nostic Register
Return Bus Message
    16#000B        16#0000                  Total number of messages
Count
Return Bus Communica‐
    16#000C        16#0000                  CRC error count
tion Error Count
Return Bus Exception
    16#000D        16#0000                  Number of exceptions
Error Count
Return Slave Message
    16#000E        16#0000                  Number of slave messages
Count
Return      Slave    No
    16#000F        16#0000                  Number of no response of slave
Response Count
Return Slave NAK Count 16#0010          16#0000                  Number of NAK of slave
Return Slave Busy Count 16#0011         16#0000                  Number of slave devices loaded
Return Bus Character                                             Number of character overflow of
    16#0012        16#0000
Overrun Count                                                    slave
RESERVED                 16# 0013       --------------           ----------------
Clear Overrun Counter
    16#0014        16#0000                  Repeat request data
and Flag
RESERVED                 Not specified --------------            ----------------
The function block is enabled after the first PLC cycle by setting the "Enable"
input to TRUE. The "Active" output is set to TRUE during operation. The bit
"Done" is set to TRUE upon completion. If an error results during the oper‐
ation, the "Error" bit is set to TRUE. "ErrorID" and "ErrorIdent" show error
information. The error can be acknowledged via a rising edge at the "Enable"
input.
Example of a function block

The function block IH_MBReadDiagnostics has to be instantiated together
with the function block IH_MBRTUMaster to communicate with the Modbus
slave. The input/output variable "stMBData" exchanges data between the
function blocks IH_MBRTUMaster and IH_MBReadDiagnostics. Thus, this var‐
iable has to be assigned to "MBData" to both function blocks.
In the example, the function block IH_MBReadDiagnostics is used to retrieve
the diagnostic status of the slave device.
Reading diagnostics with SendRequest condition
The function block IH_MBReadDiagnostics is used to read Return Diagnostic
Register of slave address 2.

Variable declaration

VAR
  fbIH_MBReadDiagnostics: IH_MBReadDiagnostics;
  bEnable: BOOL;
  bSendRequest: BOOL;
 wSubFunc : word;
 wData : word;
  stMBData: IH_INLN_MB_DATA;
  bDone: BOOL;
  bActive: BOOL;
  bError: BOOL;
  enErrorID: ERROR_CODE;
  stErrorIdent: ERROR_STRUCT;
  bBusy: BOOL;
  wRecvSubFunc: WORD;
  wRecvdata: WORD;
END_VAR

Implementation

fbIH_MBReadDiagnostics(
  Enable:= bEnable,
  SendRequest:= bSendRequest,
  EnablePoll:= FALSE,
  SlaveAddress:= BYTE#2,
  SubFunc:= wSubFunc,
  Data:= wData,
  PollInterval:= T#2S,
  TimeOut:= T#2S,
  MBData:= stMBData,
  Done=> bDone,
  Active=> bActive,
  Error=> bError,
  ErrorID=> enErrorID,
  ErrorIdent=> stErrorIdent,
  Busy=> bBusy,
  RecvSubFunc=> wRecvSubFunc,
  RecvData=> wRecvdata);

## 16.8 IH_MBReadDiscreteInputs

Function code
FC 2

Brief description
The function block IH_MBReadDiscreteInputs is used to read input bits in the
RTU mode.
The function block has to be called using the Modbus master function block
⮫ IH_S20MBRTUMaster.

       Interface description

Table 276: Interface variables of the IH_MBReadDiscreteInputs function block
I/O type           Name                 Data type         Description
VAR_INPUT          Enable               BOOL              Function block active if TRUE
                   SendRequest          BOOL              A request is sent at a rising edge
                                                          Polling enabled
                                                          SendRequest does not have to be triggered
                   EnablePoll           BOOL              at each interval
                                                          The function block sends requests automat‐
                                                          ically
                   SlaveAddress         BYTE              Slave address
                   StartAddress         WORD              Start address of the input bits
                   NoOfInputBits        UINT              Number of input bits to be read
                                        POINTER        TO
                                                          Address of the array is used to save the
                   ValueAdr             ARRAY[0..1999]
                                                          input bits Operator ADR ()
                                        OF BOOL
                                                          Size of the Value array
                   SizeOfValue          UINT
                                                          Use the SIZEOF () operator
                                                          Polling interval. Request is sent continu‐
                   PollInterval         TIME
                                                          ously at intervals
                   TimeOut              TIME              Timeout interval for response from slaves
VAR_OUTPUT                                                Computation completed and starts again in
                   Done                 BOOL
                                                          the next cycle
                   Active               BOOL              Function block is active
                   Error                BOOL              Indicates an error
                   ErrorID              ⮫ ERROR_CODE      Error class
                   ErrorIdent           ⮫ ERROR_STRUCT Detailed error information
                                                       True if the function block communicates
                   Busy                 BOOL
                                                       with the master
VAR_IN_OUT                              ⮫ IH_INLN_MB_DAT Structure handles data between the master
                   MBData
                                        A                and other Modbus function blocks

Min./max. and default values
The following table lists the min./max. and default values as well as the
application behavior of the function block inputs.
Table 277: Min./max. and default values as well as the response of the function block inputs of
IH_MBReadDiscreteInputs during application
Name            Data type       Min. value      Max. value       Default value   Effective
Enable          BOOL            FALSE           TRUE             FALSE           Continuous
                                                                                 Continuously      at
SendRequest     BOOL            FALSE           TRUE             FALSE
                                                                                 Enable
                                                                                 Continuously      at
EnablePoll      BOOL            FALSE           TRUE             FALSE
                                                                                 Enable

                                                            Rising    edge    at
SlaveAddress    BYTE            0               247              0
                                                            Enable
                                                            Rising    edge    at
StartAddress    WORD            0               16#FFFF          0
                                                            Enable
                                                            Rising    edge    at
NoOfInputBits UINT              1               2000             1
                                                            Enable
                                                            Rising    edge    at
SizeOfValue     UINT            1               2000             ----------
                                                            Enable
                                                            Continuously      at
PollInterval    TIME            T#1s            -------------    T#1s
                                                            Enable
                                                            Rising    edge    at
TimeOut         TIME            T#1s            --------------   T#1s
                                                            Enable

Functional description
The function block IH_MBReadDiscreteInputs (FC 2) is used to read input
bits in the RTU mode. The function block has to be called using the Modbus
master function block IH_MBRTUMaster. "MBData" has to be linked to the
master function block in the program. It is used for communication purposes
and data exchange.
The function block is enabled after the first PLC cycle by setting the "Enable"
input to TRUE. The "Active" output is set to TRUE during operation. The bit
"Done" is set to TRUE upon completion. If an error results during the oper‐
ation, the "Error" bit is set to TRUE. "ErrorID" and "ErrorIdent" show error
information. The error can be acknowledged via a rising edge at the "Enable"
input.
Example of a function block
The function block IH_MBReadDiscreteInputs has to be instantiated together
with the function block IH_MBRTUMaster to communicate with the Modbus
slave. The input/output variable "stMBData" exchanges data between the
function blocks IH_MBRTUMaster and IH_MBReadDiscreteInputs. Thus, this
variable has to be assigned to "MBData" to both function blocks.
In the example, the function block IH_MBReadDiscreteInputs is used to
retrieve separate inputs (Discrete Inputs) of the slave device.
Reading separate inputs with SendRequest condition
IH_MBReadDiscreteInputs is used to read 10 separate inputs of the start
address 0x1000 of slave address 2 with "bSendRequest" as BOOL variable
to trigger input reading.

Variable declaration

VAR
  fbIH_MBReadDiscreteInputs: IH_MBReadDiscreteInputs;
  bEnable: BOOL;
  bSendRequest: BOOL;
  arDiscreteInputs: ARRAY [0..2000] OF BOOL;
  stMBData: IH_INLN_MB_DATA;
  bDone: BOOL;
  bActive: BOOL;
  bError: BOOL;
  enErrorID: ERROR_CODE;
  stErrorIdent: ERROR_STRUCT;
  bBusy: BOOL;
END_VAR

Implementation

fbIH_MBReadDiscreteInputs(
  Enable:= bEnable,
  SendRequest:= bSendRequest,
  EnablePoll:= FALSE,
  SlaveAddress:= BYTE#2,
  StartAddress:= WORD#1000,
  ValueAdr:= ADR(arDiscreteInputs),
  NoOfInputBits:= UINT#10,
  SizeOfValue:= SIZEOF(arDiscreteInputs),
  PollInterval:= T#2S,
  TimeOut:= T#2S,
  MBData:= stMBData,
  Done=> bDone,
  Active=> bActive,
  Error=> bError,
  ErrorID=> enErrorID,
  ErrorIdent=> stErrorIdent,
  Busy=> bBusy);

Reading separate inputs with PollInterval condition
IH_MBReadDiscreteInputs is used to read 5 separate inputs of the start
address 0x0500 of slave address 5 with "PollInterval" (3 seconds) to trigger
input reading.

Variable declaration

VAR
  fbIH_MBReadDiscreteInputs2: IH_MBReadDiscreteInputs;
  bEnable2: BOOL;
  arDiscreteInputs2: ARRAY [0..10] OF BOOL;
  stMBData: IH_INLN_MB_DATA;
  bDone2: BOOL;
  bActive2: BOOL;
  bError2: BOOL;
  enErrorID2: ERROR_CODE;
  stErrorIdent2: ERROR_STRUCT;
  bBusy2: BOOL;
END_VAR

Implementation

fbIH_MBReadDiscreteInputs2(
  Enable:= bEnable2,
  SendRequest:= FALSE,
  EnablePoll:= TRUE,
  SlaveAddress:= BYTE#5,
  StartAddress:= WORD#500,
  ValueAdr:= ADR(arDiscreteInputs2),
  NoOfInputBits:= UINT#5,
  SizeOfValue:= SIZEOF(arDiscreteInputs2),
  PollInterval:= T#3S,
  TimeOut:= T#2S,
  MBData:= stMBData,
  Done=> bDone2,
  Active=> bActive2,
  Error=> bError2,
  ErrorID=> enErrorID2,
  ErrorIdent=> stErrorIdent2,
  Busy=> bBusy2);

## 16.9 IH_MBReadExceptionStatus

Function code
FC 7

Brief description
The function block IH_MBReadExceptionStatus is used to read the status of
the "Exception" output bit of a slave device with RTU mode.
The function block has to be called using the Modbus master function block
⮫ IH_S20MBRTUMaster.

       Interface description

Table 278: Interface variables of the IH_MBReadExceptionStatus function block
I/O type           Name                 Data type         Description
VAR_INPUT          Enable               BOOL              Function block active if TRUE
                   SendRequest          BOOL              A request is sent at a rising edge
                                                          Polling enabled
                                                          SendRequest does not have to be triggered
                   EnablePoll           BOOL              at each interval
                                                          The function block sends requests automat‐
                                                          ically
                   SlaveAddress         BYTE              Slave address
                                                          Polling interval.
                   PollInterval         TIME
                                                          Request is sent continuously at intervals
                   TimeOut              TIME              Timeout interval for response from slaves
VAR_OUTPUT                                                Computation completed and starts again in
                   Done                 BOOL
                                                          the next cycle
                   Active               BOOL              Function block is active
                   Error                BOOL              Indicates an error
                   ErrorID              ⮫ ERROR_CODE      Error class
                   ErrorIdent           ⮫ ERROR_STRUCT Detailed error information
                                                       True if the function block communicates
                   Busy                 BOOL
                                                       with the master
                                                       Contains eight exception states in the
                   Status               BYTE
                                                       output bits of the removed device
VAR_IN_OUT         MBData               ⮫ IH_INLN_MB_DAT Structure handles data between the master
                                        A                and other Modbus function blocks

Min./max. and default values
The following table lists the min./max. and default values as well as the
application behavior of the function block inputs.
Table 279: Min./max. and default values as well as the response of the function block inputs of
IH_MBReadExceptionStatus during application
Name            Data type       Min. value      Max. value       Default value   Effective
Enable          BOOL            FALSE           TRUE             FALSE           Continuous
                                                                                 Continuously      at
SendRequest     BOOL            FALSE           TRUE             FALSE
                                                                                 Enable
                                                                                 Continuously      at
EnablePoll      BOOL            FALSE           TRUE             FALSE
                                                                                 Enable

                                                            Rising    edge    at
SlaveAddress    BYTE            0               247              0
                                                            Enable
                                                            Continuously      at
PollInterval    TIME            T#1s            -------------    T#1s
                                                            Enable
                                                            Rising    edge    at
TimeOut         TIME            T#1s            --------------   T#1s
                                                            Enable

Functional description
The function block IH_MBReadExceptionStatus (FC 7) is used to read the
status of the "Exception" output bit of a slave device with RTU mode. The
function block has to be called using the Modbus master function block.
"MBData" has to be linked to the master function block in the program. It is
used for communication purposes and data exchange.
It reads the content of eight "Exception" status coils in the slave controller.
Some coils have pre-defined assignments in the different controllers. Users
can program other coils that then contains information on the controller
status, such like (machine ON/OFF), "heads retracted", "safeties satisfied",
"error conditions exist" or other customized flags.
Assignments on exception coils are predefined and depend on the controller
model used.
The function block is enabled after the first PLC cycle by setting the "Enable"
input to TRUE. The "Active" output is set to TRUE during operation. The bit
"Done" is set to TRUE upon completion. If an error results during the oper‐
ation, the "Error" bit is set to TRUE. "ErrorID" and "ErrorIdent" show error
information. The error can be acknowledged via a rising edge at the "Enable"
input.
Example of a function block:
The function block IH_MBReadExceptionStatus has to be instantiated together
with the function block IH_MBRTUMaster to communicate with the Modbus
slave. The input/output variable "stMBData" exchanges data between the
function blocks IH_MBRTUMaster and IH_MBReadExceptionStatus. Thus, this
variable has to be assigned to "MBData" to both function blocks.
In the example, the function block IH_MBReadExceptionStatus is used to
retrieve the Exception status of the slave device.
Reading status byte with SendRequest condition
The function block IH_MBReadExceptionStatus is used to read the status byte
of slave address 2. "bSendRequest" as BOOL variable triggers reading the
"Exception" status.

Variable declaration

VAR
  fbIH_MBReadExceptionStatus: IH_MBReadExceptionStatus;
  bEnable: BOOL;
  bSendRequest: BOOL;
  stMBData: IH_INLN_MB_DATA;
  bDone: BOOL;
  bActive: BOOL;
  bError: BOOL;
  enErrorID: ERROR_CODE;
  stErrorIdent: ERROR_STRUCT;
  bBusy: BOOL;
  byStatus: BYTE;
END_VAR

Implementation

fbIH_MBReadExceptionStatus(
  Enable:= bEnable,
  SendRequest:= bSendRequest,
  EnablePoll:= FALSE,
  SlaveAddress:= BYTE#2,
  PollInterval:= T#2S,
  TimeOut:= T#2S,
  MBData:= stMBData,
  Done=> bDone,
  Active=> bActive,
  Error=> bError,
  ErrorID=> enErrorID,
  ErrorIdent=> stErrorIdent,
  Busy=> bBusy,
  Status=> byStatus);

## 16.10 IH_MBReadFIFOQue

Function code
FC 24

Brief description
The function block IH_MBReadFIFOQue reads the First-In-First-Out register
queue (FIFO) of a slave module
The function block has to be called using the Modbus master function block
⮫ IH_S20MBRTUMaster.

       Interface description

Table 280: Interface variables of the IH_MBReadFIFOQue function block
I/O type       Name                 Data type         Description
VAR_INPUT      Enable               BOOL              Function block active if TRUE
               SendRequest          BOOL              A request is sent at a rising edge
                                                      Polling enabled
                                                      SendRequest does not have to be triggered
               EnablePoll           BOOL              at each interval.
                                                      The function block sends requests automat‐
                                                      ically
               SlaveAddress         BYTE              Slave address
               StartAddress         WORD              Start address of the output bits
                                                      Polling interval. Request is sent continu‐
               PollInterval         TIME
                                                      ously at intervals
               TimeOut              TIME              Timeout interval for response from slaves
VAR_OUTPUT                                            Computation completed and starts again in
               Done                 BOOL
                                                      the next cycle
               Active               BOOL              Function block is active
               Error                BOOL              Indicates an error
               ErrorID              ⮫ ERROR_CODE      Error class
               ErrorIdent           ⮫ ERROR_STRUCT Detailed error information
                                                      True if the function block communicates
               Busy                 BOOL
                                                      with the master
               FIFOData             ⮫ IH_INLN_MB_FIF‐ The structure contains additional informa‐
                                    ODATA             tion on the number of bytes, number of
                                                      FIFOs and FIFO register values
VAR_IN_OUT     MBData               ⮫ IH_INLN_MB_DAT Structure handles data between the master
                                    A                and other Modbus function blocks

Min./max. and default values
The following table lists the min./max. and default values as well as the
application behavior of the function block inputs.
Table 281: Min./max. and default values as well as the response of the function block inputs of
IH_MBReadFIFOQue during application
Name               Data type       Min. value    Max. value       Default value   Effective
Enable             BOOL            FALSE         TRUE             FALSE           Continuous
                                                                                  Continuously      at
SendRequest        BOOL            FALSE         TRUE             FALSE
                                                                                  Enable
                                                                                  Continuously      at
EnablePoll         BOOL            FALSE         TRUE             FALSE
                                                                                  Enable
                                                                                  Rising    edge    at
SlaveAddress       BYTE            0             247              0
                                                                                  Enable
                                                                                  Rising    edge    at
StartAddress       WORD            0             65535            0
                                                                                  Enable
                                                                                  Continuously      at
PollInterval       TIME            T#1s          -------------    T#1s
                                                                                  Enable
                                                                                  Rising    edge    at
TimeOut            TIME            T#1s          --------------   T#1s
                                                                                  Enable

Functional description
The function block IH_MBReadFIFOQue (FC 24) reads the First-In-First-Out
register queue (FIFO) of a slave module. The function block has to be called
using the Modbus master function block. "MBData" has to be linked to the
master function block in the program. It is used for communication purposes
and data exchange.
The function block is enabled after the first PLC cycle by setting the "Enable"
input to TRUE. The "Active" output is set to TRUE during operation. The bit
"Done" is set to TRUE upon completion. If an error results during the oper‐
ation, the "Error" bit is set to TRUE. "ErrorID" and "ErrorIdent" show error
information. The error can be acknowledged via a rising edge at the "Enable"
input.
Example of a function block
The function block IH_MBReadFIFOQue has to be instantiated together with
the IH_MBRTUMaster to communicate with the Modbus slave. Use a common
variable for "MBData" of the IH_MBReadFIFOQue and IH_MBRTUMaster func‐
tion blocks to exchange data with the Modbus slave.
In this example, the function block IH_MBReadFIFOQue reads the FIFO queue
of the slave with address 1 and StartAddress 2550.
The two function blocks IH_MBRTUMaster and IH_MBReadFIFOQue are ena‐
bled with a rising edge at the "bSendRequest" input. The function block reads
the FIFO queue of the slave with address 1. The result is saved in "stFIFO‐
Data".
If "bEnablePoll" variable is set to TRUE and "PollInterval" to more than 1
second, data is read from the slave at regular intervals.
After each successful read operation, the bit "Done" is set to TRUE for one
PLC cycle.

Variable declaration

VAR
fbIH_MBReadFIFOQue: IH_MBReadFIFOQue;
bEnable: BOOL;
bSendRequest: BOOL;
bEnablePoll: BOOL;
stMBData: IH_INLN_MB_DATA;
bDone: BOOL;
bActive: BOOL;
bError: BOOL;
enErrorID: ERROR_CODE;
stErrorIdent: ERROR_STRUCT;
bBusy: BOOL;

stFIFOData: IH_INLN_MB_FIFODATA;
END_VAR

Implementation

fbIH_MBReadFIFOQue(
Enable:= bEnable,
SendRequest:= bSendRequest,
EnablePoll:= bEnablePoll,
SlaveAddress:= BYTE#1,
StartAddress:= WORD#2550,
PollInterval:= T#1S,
TimeOut:= T#1S,
MBData:= stMBData,
Done=> bDone,
Active=> bActive,
Error=> bError,
ErrorID=> enErrorID,
ErrorIdent=> stErrorIdent,
Busy=> bBusy,
FIFOData=> stFIFOData);

Response

## 16.11 IH_MBReadFileRecord

Function code
FC 20

       Brief description
       The function block IH_MBReadFileRecord is used to read file protocols in the
       RTU mode.
       The function block has to be called using the Modbus master function block
       ⮫ IH_S20MBRTUMaster.

       Interface description

Table 282: Interface variables of the IH_MBReadFileRecord function block
I/O type           Name                 Data type
                                           Description
VAR_INPUT          Enable               BOOL
                                           Function block active if TRUE
                   SendRequest          BOOL
                                           A request is sent at a rising edge
                                           Polling enabled
                                           SendRequest does not have to be triggered
           EnablePoll      BOOL            at each interval
                                           The function block sends requests automat‐
                                           ically
           SlaveAddress    BYTE            Slave address
           NoOfSubRequests INT             Number of subrequests
                           ARRAY[1..30] OF List of subrequests
           SubRequests     IH_INLN_MB_SUB‐ Please refer to: Structures and enumera‐
                           REQUESTS        tions
                                           Polling interval
           PollInterval    TIME
                                           Request is sent continuously at intervals
           TimeOut         TIME            Timeout interval for response from slaves
VAR_OUTPUT                                 Computation completed and starts again in
           Done            BOOL
                                           the next cycle
           Active          BOOL            Function block is active
           Error           BOOL            Indicates an error
                   ErrorID              ⮫ ERROR_CODE       Error class
                   ErrorIdent           ⮫ ERROR_STRUCT Detailed error information
                   Busy                 BOOL            True if the function block communicates
                                                        with the master
                   OutputData           ⮫ IH_INLN_MB_RE Contains the requested data length and the
                                        CORD            subrequested data. Refer to: Structures and
                                                        enumerations
VAR_IN_OUT         MBData               ⮫ IH_INLN_MB_DAT Structure handles data between the master
                                        A                and other Modbus function blocks

Min./max. and default values
The following table lists the min./max. and default values as well as the
application behavior of the function block inputs.
Table 283: Min./max. and default values as well as the response of the function block inputs of
IH_MBReadFileRecord during application
Name            Data type        Min. value      Max. value       Default value   Effective
Enable          BOOL             FALSE           TRUE             FALSE           Continuous
                                                                                  Continuously     at
SendRequest     BOOL             FALSE           TRUE             FALSE
                                                                                  Enable
                                                                                  Continuously     at
EnablePoll      BOOL             FALSE           TRUE             FALSE
                                                                                  Enable

                                                            Rising    edge   at
SlaveAddress    BYTE             0               247              0
                                                            Enable
NoOfSubRe‐                                                                        Continuously     at
INT              1               30               1
quests                                                                            Enable
                                                            Continuously     at
PollInterval    TIME             T#1s            -------------    T#1s
                                                            Enable
                                                            Rising    edge   at
TimeOut         TIME             T#1s            --------------   T#1s
                                                            Enable

Functional description
The function block IH_MBReadFileRecord (FC 20) is used to read file
protocols in the RTU mode. The requested data lengths in the structure
IH_INLN_MB_SUBREQUESTS are specified in bytes. Protocol lengths are speci‐
fied as register. The function block has to be called using the Modbus master
function block. "MBData" has to be linked to the master function block in the
program. It is used for communication purposes and data exchange.
The function can read out multiple groups of references. It can be separate
(no adjacent) groups, but the references in the individual groups have to be
continuous.
● Each group is defined in a separate field for subrequests containing 7
   bytes.
● Reference type: 1 byte (to be specified as 6). Info: Considered as standard
   in this function block.
● File number: (Word) has to be (0x0000 to 0xFFFF).
● Initial protocol number in the file. (Word) has to be (0x0000 to 0x270F).
● Length of the protocol to be read (word).
The number of the registers to be read and all other fields in the expected
response may not exceed the permitted length of the MODBUS PDU: 253
bytes.
Thus, the total length of the protocol of all subrequests has to be smaller than
(123 – NoOfSubRequests).
The function block is enabled after the first PLC cycle by setting the "Enable"
input to TRUE. The "Active" output is set to TRUE during operation. The bit
"Done" is set to TRUE upon completion. If an error results during the oper‐
ation, the "Error" bit is set to TRUE. "ErrorID" and "ErrorIdent" show error
information. The error can be acknowledged via a rising edge at the "Enable"
input.
Example of a function block

The function block IH_MBReadFileRecord has to be instantiated together with
the function block IH_MBRTUMaster to communicate with the Modbus slave.
The input/output variable "stMBData" exchanges data between the function
blocks IH_MBRTUMaster and IH_MBReadFileRecord. Thus, this variable has to
be assigned to "MBData" to both function blocks.
In the example, the function block IH_MBReadFileRecord is used to retrieve
the file protocols of the slave device.

Reading two file protocols with SendRequest condition
The function block IH_MBReadFileRecord is used to read 2 protocols with the
length 4 and 3 of the file 1 and 2 from slave address 2 with "bSendRequest"
as BOOL variable to trigger reading.

Variable declaration

VAR
  fbIH_MBReadFileRecord: IH_MBReadFileRecord;
  bEnable: BOOL;
  bSendRequest: BOOL;
  stSubRequests: ARRAY [1..30] OF IH_INLN_MB_SUBREQUESTS;
  stMBData: IH_INLN_MB_DATA;
  bDone: BOOL;
  bActive: BOOL;
  bError: BOOL;
  enErrorID: ERROR_CODE;
  stErrorIdent: ERROR_STRUCT;
  bBusy: BOOL;
  stOutputData: IH_INLN_MB_RECORD;
END_VAR

Implementation

stSubRequests[1].FileNumber := WORD#1;
stSubRequests[1].RecordNumber := WORD#0;
stSubRequests[1].RecordLength := WORD#4;
stSubRequests[2].FileNumber := WORD#2;
stSubRequests[2].RecordNumber := WORD#5;
stSubRequests[2].RecordLength := WORD#3;

fbIH_MBReadFileRecord(
  Enable:= bEnable,
  SendRequest:= bSendRequest,
  EnablePoll:= FALSE,
  SlaveAddress:= BYTE#2,
  NoOfSubRequests:= INT#2,
  SubRequests:= stSubRequests,
  PollInterval:= T#2S,
  TimeOut:= T#2S,
  MBData:= stMBData,
  Done=> bDone,
  Active=> bActive,
  Error=> bError,
  ErrorID=> enErrorID,
  ErrorIdent=> stErrorIdent,
  Busy=> bBusy,
  OutputData=> stOutputData);

Reading one file protocol with PollInterval condition
The function block IH_MBReadFileRecord is used to read 1 protocol with
the length 6 from slave address 5 with "PollInterval" (3 seconds) to trigger
reading.

Variable declaration

VAR
  fbIH_MBReadFileRecord2: IH_MBReadFileRecord;
  bEnable2: BOOL;
  stSubRequests2: ARRAY [1..30] OF IH_INLN_MB_SUBREQUESTS;
  stMBData: IH_INLN_MB_DATA;
  bDone2: BOOL;
  bActive2: BOOL;
  bError2: BOOL;
  enErrorID2: ERROR_CODE;
  stErrorIdent2: ERROR_STRUCT;
  bBusy2: BOOL;
  stOutputdata2: IH_INLN_MB_RECORD;
END_VAR

Implementation

stSubRequests2[1].FileNumber := WORD#1;
stSubRequests2[1].RecordNumber := WORD#0;
stSubRequests2[1].RecordLength := WORD#6;

fbIH_MBReadFileRecord2(
  Enable:= bEnable2,
  SendRequest:= FALSE,
  EnablePoll:= TRUE,
  SlaveAddress:= BYTE#5,
  NoOfSubRequests:= INT#1,
  SubRequests:= stSubRequests2,
  PollInterval:= T#3S,
  TimeOut:= T#2S,
  MBData:= stMBData,
  Done=> bDone2,
  Active=> bActive2,
  Error=> bError2,
  ErrorID=> enErrorID2,
  ErrorIdent=> stErrorIdent2,
  Busy=> bBusy2,
  OutputData=> stOutputdata2);

## 16.12 IH_MBReadHoldingRegisters

Function code
FC 3

Brief description
The function block IH_MBReadHoldingRegisters is used to read a Holding reg‐
ister of the Modbus slave module.
The function block has to be called using the Modbus master function block
⮫ IH_S20MBRTUMaster.

       Interface description

Table 284: Interface variables of the IH_MBReadHoldingRegisters function block
I/O type       Name                 Data type        Description
VAR_INPUT      Enable               BOOL             Function block active if TRUE
               SendRequest          BOOL             A request is sent at a rising edge
               EnablePoll           BOOL             Polling enabled
                                                     SendRequest does not have to be triggered
                                                     at each interval
                                                     The function block sends requests automat‐
                                                     ically
               SlaveAddress         BYTE             Slave address
               StartAddress         WORD             Start address of the Holding register
               NoOfRegisters        UINT             Number of registers
               ValueAdr             POINTER TO       Address of the array to save the Holding
                                    ARRAY[0..124] OF register. Use the ADR () operator
                                    WORD
               SizeOfValue          UINT             Size of the Value array
                                                     Use the SIZEOF () operator
               PollInterval         TIME             Polling interval
                                                     Request is sent continuously at intervals
           TimeOut                  TIME             Timeout interval for response from slaves
VAR_OUTPUT Done                     BOOL             Computation completed and starts again in
                                                     the next cycle
               Active               BOOL             Function block is active
               Error                BOOL             Indicates an error
               ErrorID              ⮫ ERROR_CODE     Error class
               ErrorIdent           ⮫ ERROR_STRUCT Detailed error information
               Busy                 BOOL             True if the function block communicates
                                                     with the master
VAR_OUTPUT MBData                   ⮫ IH_INLN_MB_DAT Structure handles data between the master
                                    A                and other Modbus function blocks of the
                                                     function codes

Min./max. and default values
The following table lists the min./max. and default values as well as the
application behavior of the function block inputs.
Table 285: Min./max. and default values as well as the response of the function block inputs of
IH_MBReadHoldingRegisters during application
Name               Data type       Min. value    Max. value      Default value   Effective
Enable             BOOL            FALSE         TRUE            FALSE           Continuous
                                                                                 Continuously      at
SendRequest        BOOL            FALSE         TRUE            FALSE
                                                                                 Enable
                                                                                 Continuously      at
EnablePoll         BOOL            FALSE         TRUE            FALSE
                                                                                 Enable
                                                                                 Rising    edge    at
SlaveAddress       BYTE            0             247             0
                                                                                 Enable
                                                                                 Rising    edge    at
StartAddress       WORD            0             65535           0
                                                                                 Enable
                                                                                 Rising    edge    at
NoOfRegisters UINT                 1             125             1
                                                                                 Enable
                                                                                 Rising    edge    at
SizeOfValue        UINT            1             -----------     --------
                                                                                 Enable
                                                                                 Continuously      at
PollInterval       TIME            T#1s          -------------   T#1s
                                                                                 Enable
                                                                                 Rising    edge    at
TimeOut            TIME            T#1s          ------------    T#1s
                                                                                 Enable

Functional description
The function block IH_MBReadHoldingRegisters (FC 3) reads the Holding reg‐
ister of a slave module specified in "SlaveAddress". The function block has to
be called using the Modbus master function block. "MBData" has to be linked
to the master function block to communicate with the master and to exchange
data.
The function block is enabled after the first PLC cycle by setting the "Enable"
input to TRUE. The "Active" output is set to TRUE during operation. The bit
"Done" is set to TRUE upon completion. If an error results during the oper‐
ation, the "Error" bit is set to TRUE. "ErrorID" and "ErrorIdent" show error
information. The error can be acknowledged via a rising edge at the "Enable"
input.
Example of a function block
The function block IH_MBRTUMaster has to be instantiated together with
the ⮫ IH_S20MBRTUMaster to communicate with the Modbus slave. Use
a common variable for "MBData" of the IH_MBReadHoldingRegisters and
IH_MBRTUMaster function blocks to exchange data with the Modbus slave.

Example 1
In this example, the function block IH_MBReadHoldingRegisters reads the
Holding register of slave address 1 with "StartAddress" 5 and "NoOfRegisters"
5.
The function blocks IH_MBRTUMaster and IH_MBReadHoldingRegisters are
enabled with a rising edge at the "bSendRequest" input. The function block
reads data from slave address 1 and after each successful read operation, the
bit "Done" is set to TRUE for one PLC cycle.

Variable declaration

VAR
  fbIH_MBReadHoldingRegisters: IH_MBReadHoldingRegisters;
  bEnable: BOOL;
  bSendRequest: BOOL;
  bEnablePoll: BOOL;
  arHoldingRegister: ARRAY [0..4] OF WORD;
  stMBData: IH_INLN_MB_DATA;
  bDone: BOOL;
  bActive: BOOL;
  bError: BOOL;
  enErrorID: ERROR_CODE;
  stErrorIdent: ERROR_STRUCT;

  bBusy: BOOL;
END_VAR

Implementation

fbIH_MBReadHoldingRegisters(
  Enable:= bEnable,
  SendRequest:= bSendRequest,
  EnablePoll:= bEnablePoll,
  SlaveAddress:= BYTE#1,
  StartAddress:= WORD#5,
  NoOfRegisters:= UINT#5,
  ValueAdr:= ADR(arHoldingRegister),
  SizeOfValue:= SIZEOF(arHoldingRegister),
  PollInterval:= T#1S,
  TimeOut:= T#1S,
  MBData:= stMBData,
  Done=> bDone,
  Active=> bActive,
  Error=> bError,
  ErrorID=> enErrorID,
  ErrorIdent=> stErrorIdent,
  Busy=> bBusy);

Response
The read data is provided in the array arHoldingRegister.

Example 2
In this example, the function block IH_MBReadHoldingRegisters reads the
Holding register of slave address 2 with "StartAddress" 100 and "NoOfRegis‐
ters" 10 at a polling interval of 1 second.
The function blocks IH_MBRTUMaster and IH_MBReadHoldingRegisters are
enabled and "EnablePoll" with a polling interval of 1 second is set to TRUE.
The function block then reads data from slave address 2 at regular intervals of
1 second. After each successful read operation, the bit "Done" is set to TRUE
for one PLC cycle.

Variable declaration

VAR
fbIH_MBReadHoldingRegisters_2: IH_MBReadHoldingRegisters;
bEnable2: BOOL;
bSendRequest2: BOOL;
arHoldingRegister2: ARRAY [0..9] OF WORD;
bDone2: BOOL;
bActive2: BOOL;
bError2: BOOL;
enErrorID2: ERROR_CODE;
stErrorIdent2: ERROR_STRUCT;
bBusy2: BOOL;
stMBData: IH_INLN_MB_DATA;

END_VAR

Implementation

fbIH_MBReadHoldingRegisters_2(
Enable:= bEnable2,
SendRequest:= bSendRequest2,
EnablePoll:= TRUE,
SlaveAddress:= BYTE#2,
StartAddress:= WORD#100,
NoOfRegisters:= UINT#10,
ValueAdr:= ADR(arHoldingRegister2),
SizeOfValue:= SIZEOF(arHoldingRegister2),
PollInterval:= T#1S,
TimeOut:= T#1S,
MBData:= stMBData,
Done=> bDone2,
Active=> bActive2,
Error=> bError2,
ErrorID=> enErrorID2,
ErrorIdent=> stErrorIdent2,
Busy=> bBusy2);

Response
The read data is provided in the array arHoldingRegister2.

## 16.13 IH_MBReadInputRegisters

      Function code
      FC 4

      Brief description
      The function block IH_MBReadInputRegisters is used to read input registers in
      the RTU mode.
      The function block has to be called using the Modbus master function block
      ⮫ IH_S20MBRTUMaster.

      Interface description

Table 286: Interface variables of the IH_MBReadInputRegisters function block
I/O type       Name                  Data type         Description
VAR_INPUT      Enable                BOOL              Function block active if TRUE
               SendRequest           BOOL              A request is sent at a rising edge
                                                       Polling enabled
                                                       SendRequest does not have to be triggered
               EnablePoll            BOOL              at each interval
                                                       The function block sends requests automat‐
                                                       ically
               SlaveAddress          BYTE              Slave address
               StartAddress          WORD              Start address of the register
               NoOfRegisters         UINT              Number of registers to be read
                                     POINTER       TO
                                                      Address of the array is used to save input
               ValueAdr              ARRAY[0..124] OF
                                                      registers Operator ADR ()
                                     WORD
                                                      Size of the Value array
               SizeOfValue           UINT
                                                      Use the SIZEOF () operator
                                                      Polling interval
               PollInterval          TIME
                                                      Request is sent continuously at intervals
               TimeOut               TIME             Timeout interval for response from slaves
VAR_OUTPUT                                            Computation completed and starts again in
               Done                  BOOL
                                                      the next cycle
               Active                BOOL             Function block is active
               Error                 BOOL             Indicates an error
               ErrorID               ⮫ ERROR_CODE      Error class
               ErrorIdent            ⮫ ERROR_STRUCT Detailed error information

I/O type           Name                  Data type             Description
                                     True if the function block communicates
Busy                  BOOL
                                     with the master
VAR_IN_OUT                               ⮫ IH_INLN_MB_DAT Structure handles data between the master
MBData
               A                and other Modbus function blocks

Min./max. and default values
The following table lists the min./max. and default value as well as the appli‐
cation behavior of the function block inputs.
Table 287: Min./max. and default values as well as the response of the function block inputs of
IH_MBReadInputRegisters during application
Name               Data type         Min. value      Max. value       Default value   Effective
Enable             BOOL              FALSE           TRUE             FALSE           Continuous
                                                                                      Continuously      at
SendRequest        BOOL              FALSE           TRUE             FALSE
                                                                                      Enable
                                                                                      Continuously      at
EnablePoll         BOOL              FALSE           TRUE             FALSE
                                                                                      Enable
                                                                                      Rising    edge    at
SlaveAddress       BYTE              0               247              0
                                                                                      Enable
                                                                                      Rising    edge    at
StartAddress       WORD              0               16#FFFF          0
                                                                                      Enable
                                                                                      Rising    edge    at
NoOfRegisters UINT                   1               125              1
                                                                                      Enable
                                                                                      Rising    edge    at
SizeOfValue        UINT              1               -----------      ---------
                                                                                      Enable
                                                                                      Continuously      at
PollInterval       TIME              T#1s            -------------    T#1s
                                                                                      Enable
                                                                                      Rising    edge    at
TimeOut            TIME              T#1s            --------------   T#1s
                                                                                      Enable

Functional description
The function block IH_MBReadInputRegisters (FC 4) is used to read input reg‐
isters in the RTU mode. The function block has to be called using the Modbus
master function block. "MBData" has to be linked to the master function block
in the program. It is used for communication purposes and data exchange.
The function block is enabled after the first PLC cycle by setting the "Enable"
input to TRUE. The "Active" output is set to TRUE during operation. The bit
"Done" is set to TRUE upon completion. If an error results during the oper‐
ation, the "Error" bit is set to TRUE. "ErrorID" and "ErrorIdent" show error
information. The error can be acknowledged via a rising edge at the "Enable"
input.
Example of a function block
The function block IH_MBReadInputRegisters has to be instantiated together
with the function block IH_MBRTUMaster to communicate with the Modbus
slave. The input/output variable "stMBData" exchanges data between the
function blocks IH_MBRTUMaster and IH_MBReadInputRegisters. Thus, this
variable has to be assigned to "MBData" to both function blocks.
In the example, the function block IH_MBReadInputRegisters is used to
retrieve input registers of the slave device.

Reading input register with SendRequest condition
IH_MBReadInputRegisters is used to read 10 input registers of the start
address 0x1000 of slave address 2 with "bSendRequest" as BOOL variable
to trigger read inputs.

Variable declaration

VAR
  fbIH_MBReadInputRegisters: IH_MBReadInputRegisters;
  bEnable: BOOL;
  bSendrequest: BOOL;
  arInputRegisters: ARRAY [0..124] OF WORD;

  stMBData: IH_INLN_MB_DATA;
  bDone: BOOL;
  bActive: BOOL;
  bError: BOOL;
  enErrorID: ERROR_CODE;
  stErrorIdent: ERROR_STRUCT;
  bBusy: BOOL;
END_VAR

Implementation

fbIH_MBReadInputRegisters(
  Enable:= bEnable,
  SendRequest:= bSendrequest,
  EnablePoll:= FALSE,
  SlaveAddress:= BYTE#2,
  StartAddress:= WORD#1000,
  ValueAdr:= ADR(arInputRegisters),
  NoOfRegisters:= UINT#10,
  SizeOfValue:= SIZEOF(arInputRegisters),
  PollInterval:= T#2S,
  TimeOut:= T#2S,
  MBData:= stMBData,
  Done=> bDone,
  Active=> bActive,
  Error=> bError,
  ErrorID=> enErrorID,
  ErrorIdent=> stErrorIdent,
  Busy=> bBusy);

Reading input register with PollInterval condition
IH_MBReadInputRegisters is used to read five input registers of the start
address 0x0500 of slave address 5 with "PollInterval" (3 seconds) to trigger
read inputs.

Variable declaration

VAR
  fbIH_MBReadInputRegisters2: IH_MBReadInputRegisters;
  bEnable2: BOOL;
  arInputRegisters2: ARRAY [0..7] OF WORD;
  stMBData: IH_INLN_MB_DATA;
  bDone2: BOOL;
  bActive2: BOOL;
  bError2: BOOL;
  enErrorID2: ERROR_CODE;
    stErrorIdent2: ERROR_STRUCT;
  bBusy2: BOOL;
END_VAR

Implementation

fbIH_MBReadInputRegisters2(
  Enable:= bEnable2,
  SendRequest:= FALSE,
  EnablePoll:= TRUE,
  SlaveAddress:= BYTE#5,
  StartAddress:= WORD#500,
  ValueAdr:= ADR(arInputRegisters2),
  NoOfRegisters:= UINT#5,
  SizeOfValue:= SIZEOF(arInputRegisters2),
  PollInterval:= T#3S,
  TimeOut:= T#2S,
  MBData:= stMBData,
  Done=> bDone2,
  Active=> bActive2,
  Error=> bError2,
  ErrorID=> enErrorID2,
  ErrorIdent=> stErrorIdent2,
  Busy=> bBusy2);

## 16.14 IH_MBReadWriteMultipleRegisters

Function code
FC 23

      Brief description
      The function block IH_MBReadWriteMultipleRegisters combines a read and
      a write operation in one Modbus transaction. The function block has to be
      called using the Modbus master function block ⮫ IH_S20MBRTUMaster.

      Interface description

Table 288: Interface variables of the IH_MBReadWriteMultipleRegisters function block
I/O type       Name                Data type         Description
VAR_INPUT      Enable              BOOL              Function block active if TRUE
               SendRequest         BOOL              A request is sent at a rising edge
                                                     Polling enabled
                                                     SendRequest does not have to be triggered
               EnablePoll          BOOL              at each interval
                                                     The function block sends requests automat‐
                                                     ically
               SlaveAddress        BYTE              Slave address
                                                     Start address of the Holding register
               ReadStartAddress WORD
                                                     applies to the read operation
                                                     Start address of the Holding register
               WriteStartAddress WORD
                                                     applies to the write operation
               NoOfReadRegis‐
                                   UINT              Number of registers to be read
               ters
               NoOfWriteRegis‐
                                   UINT              Number of registers to be written
               ters
                                 POINTER       TO Address of the array to save the read value
               ReadDataValAdr    ARRAY[0..124] OF of the register
                                 WORD             Use the ADR () operator
                                                  Size of the ReadDataVal array
               SizeOfReadDataVal UINT
                                                  Use the SIZEOF () operator
                                 POINTER       TO The address of the array contains the write
               WriteDataValAdr   ARRAY[0..120] OF value of the registers
                                 WORD             Use the ADR () operator
               SizeOfWriteDa‐                     Size of the WriteDataVal array
                                 UINT
               taVal                              Use the SIZEOF () operator

I/O type           Name                  Data type             Description
                                                Polling interval. Request is sent continu‐
    PollInterval          TIME
                                                ously at intervals
    TimeOut               TIME                  Timeout interval for response from slaves
VAR_OUTPUT                                                     Computation completed and starts again in
    Done                  BOOL
                                                the next cycle
    Active                BOOL                  Function block is active
    Error                 BOOL                  Indicates an error
    ErrorID               ⮫ ERROR_CODE          Error class
    ErrorIdent            ⮫ ERROR_STRUCT Detailed error information
                                         True if the function block communicates
    Busy                  BOOL
                                         with the master
VAR_IN_OUT                               ⮫ IH_INLN_MB_DAT Structure handles data between the master
    MBData
                          A                and other Modbus function blocks

           Min./max. and default values
           The following table lists the min./max. and default values as well as the
           application behavior of the function block inputs.
Table 289: Min./max. and default values as well as the response of the function block inputs of
IH_MBReadWriteMultipleRegisters during application
Name                Data type        Min. value      Max. value         Default value   Effective
Enable              BOOL             FALSE           TRUE               FALSE           Continuous
                                                                                        Continuously      at
SendRequest         BOOL             FALSE           TRUE               FALSE
                                                                                        Enable
                                                                                        Continuously      at
EnablePoll          BOOL             FALSE           TRUE               FALSE
                                                                                        Enable
                                                                                        Rising    edge    at
SlaveAddress        BYTE             0               247                0
                                                                                        Enable
ReadStartAd‐                                                                            Rising    edge    at
               WORD                  0               65535              0
dress                                                                                   Enable
WriteStartAd‐                                                                           Rising    edge    at
               WORD                  0               65535              0
dress                                                                                   Enable
NoOfRea‐                                                                                Rising    edge    at
               UINT                  1               125                1
dRegisters                                                                              Enable
NoOfWriteR‐                                                                             Rising    edge    at
               UINT                  1               121                1
egisters                                                                                Enable
SizeOfReadDa‐                                                                           Rising    edge    at
               UINT                  1               -------------      -------------
taVal                                                                                   Enable
SizeOfWriteDa‐                                                                          Rising    edge    at
               UINT                  1               -------------      -------------
taVal                                                                                   Enable
                                                                                        Continuously      at
PollInterval        TIME             T#1s            -------------      T#1s
                                                                                        Enable
                                                                                        Rising    edge    at
TimeOut             TIME             T#1s            --------------     T#1s
                                                                                        Enable

Functional description
The function block IH_MBReadWriteMultipleRegisters (FC 23) combines a
read and a write operation in one Modbus transaction. The function block
has to be called using the Modbus master function block. "MBData" has to be
linked to the master function block to communicate with the master and to
exchange data.
The function block is enabled after the first PLC cycle by setting the "Enable"
input to TRUE. The "Active" output is set to TRUE during operation. The bit
"Done" is set to TRUE upon completion. If an error results during the oper‐
ation, the "Error" bit is set to TRUE. "ErrorID" and "ErrorIdent" show error
information. The error can be acknowledged via a rising edge at the "Enable"
input.

Example of a function block:
The function block IH_MBReadWriteMultipleRegisters has to be instantiated
together with the function block IH_MBRTUMaster to communicate with the
Modbus slave. The input/output variable "stMBData" exchanges data between
the function blocks IH_MBRTUMaster and IH_MBReadWriteMultipleRegisters.
Thus, this variable has to be assigned to "MBData" to both function blocks.
In the example, the function block IH_MBWriteMultipleCoils is used to read
registers on and write registers to the slave device.

Reading and writing registers with SendRequest condition
In the example, 5 registers of the start address 0x4000 of a Modbus slave
device are written and read with address 1. A rising edge at the "bSendRe‐
quest" input triggers the read and write operation.

Variable declaration

VAR
  fbIH_MBReadWriteMultipleRegisters:
IH_MBReadWriteMultipleRegisters;
  bEnable: BOOL;
  bSendRequest: BOOL;
  arReadData: ARRAY [0..4] OF WORD;
  arWriteData: ARRAY [0..4] OF WORD;
  stMBData: IH_INLN_MB_DATA;
  bDone: BOOL;
  bActive: BOOL;
  bError: BOOL;
  enErrorID: ERROR_CODE;
  stErrorIdent: ERROR_STRUCT;
  bBusy: BOOL;
END_VAR

Implementation

fbIH_MBReadWriteMultipleRegisters(
  Enable:= bEnable,
  SendRequest:= bSendRequest,
  EnablePoll:= FALSE,
  SlaveAddress:= BYTE#1,
  ReadStartAddress:= WORD#4000,
  WriteStartAddress:= WORD#4000,
  NoOfReadRegisters:= UINT#5,
  NoOfWriteRegisters:= UINT#5,
  ReadDataValAdr:= ADR(arReadData),
  SizeOfReadDataVal:= SIZEOF(arReadData),
  WriteDataValAdr:= ADR(arWriteData),
  SizeOfWriteDataVal:= SIZEOF(arWriteData),
  PollInterval:= T#1S,
  TimeOut:= T#1S,
  MBData:= stMBData,
  Done=> bDone,
  Active=> bActive,
  Error=> bError,
  ErrorID=> enErrorID,
  ErrorIdent=> stErrorIdent,
  Busy=> bBusy);

Reading and writing registers with SendRequest condition
In the example, 10 registers of the start address 0x4200 are written and 5
registers from the start address 0x4100 of a Modbus RTU slave device are
read with address 1.
"PollInterval" is set to 3 seconds and "EnablePoll" is TRUE.
A rising edge at the "bSendRequest" input triggers the read and write opera‐
tion.

Variable declaration

VAR
fbIH_MBReadWriteMultipleRegisters2:
IH_MBReadWriteMultipleRegisters;
bEnable2: BOOL;
arReadData2: ARRAY [0..4] OF WORD;
arWriteData2: ARRAY [0..9] OF WORD;
stMBData: IH_INLN_MB_DATA;
bDone2: BOOL;
bActive2: BOOL;
bError2: BOOL;
enErrorID2: ERROR_CODE;
stErrorIdent2: ERROR_STRUCT;

bBusy2: BOOL;
END_VAR

Implementation

fbIH_MBReadWriteMultipleRegisters2(
Enable:= bEnable2,
SendRequest:= FALSE,
EnablePoll:= TRUE,
SlaveAddress:= BYTE#1,
ReadStartAddress:= WORD#4100,
WriteStartAddress:= WORD#4200,
NoOfReadRegisters:= UINT#5,
NoOfWriteRegisters:= UINT#10,
ReadDataValAdr:= ADR(arReadData2),
SizeOfReadDataVal:= SIZEOF(arReadData2),
WriteDataValAdr:= ADR(arWriteData2),
SizeOfWriteDataVal:= SIZEOF(arWriteData2),
PollInterval:= T#3S,
TimeOut:= T#1S,
MBData:= stMBData,
Done=> bDone2,
Active=> bActive2,
Error=> bError2,
ErrorID=> enErrorID2,
ErrorIdent=> stErrorIdent2,
Busy=> bBusy2);

## 16.15 IH_S20MBRTUMaster

Brief description
The function block IH_S20MBRTUMaster ensures the communication between
the controller and the physical line network (slaves) in RTU mode. It receives
requests from other function blocks of function codes and sends them via the
modules S20-RS-Uni to the slaves. It receives the response from all slaves and
sends them back to the function block that originally sent the request. The
function block has to be instantiated once for all terminals. It communicates
with up to 33 function blocks of function codes at the same time.

        Interface description

Table 290: Interface variables of the IH_S20MBRTUMaster function block
I/O type       Name                  Data type        Description
VAR_INPUT      Enable                BOOL             Function block active if TRUE
                                     POINTER       TO
               S20BusHandle          IH_S20_BUS_IDEN‐ Bus handle for the S20 IO configuration
                                     TIFIER
               Slot                  UINT             Module slot 1..63
                                     IH_S20_MB_CONFI Used for the Modbus configuration of S20-
               MBConfig
                                     G                RS-Uni
                                     POINTER       TO Address of the array for input process data
               InputAdr              ARRAY[0..19] OF
                                     BYTE             Use the ADR () operator
                                                      Size of the InputAdr array
               SizeOfInput           UINT
                                                      Use the SIZEOF () operator
                                     POINTER       TO Address of the array for output process
               OutputAdr             ARRAY[0..19] OF data
                                     BYTE             Use the ADR () operator
                                                      Size of the OutputAdr array
               SizeOfOutput          UINT
                                                      Use the SIZEOF () operator
VAR_OUTPUT                                            The function block is working at its actual
               InOperation           BOOL
                                                      task
               Error                 BOOL             Indicates an error
               ErrorID               ⮫ ERROR_CODE      Error class
               ErrorIdent            ⮫ ERROR_STRUCT Detailed error information
                                                      True if the function block communicates
               Busy                  BOOL
                                                      with function blocks of the function code
               NoOfRequests          UINT             Number of requests sent
               NoOfResponses         UINT             Number of responses received
VAR_IN_OUT     MBData                ⮫ IH_INLN_MB_DAT Structure handles data between the
                                     A                IH_S20MBRTUMaster and other Modbus
                                                      function blocks of function codes

Min./max. and default values
The following table lists the min./max. and default values as well as the
application behavior of the function block inputs.
Table 291: Min./max. and default values as well as the response of the function block inputs of
IH_S20MBRTUMaster during application
Name               Data type       Min. value    Max. value       Default value   Effective
Enable             BOOL            FALSE         TRUE             FALSE           Continuous
                                                                                  Rising    edge    at
SizeOfInput        UINT            12            62               ----------
                                                                                  Enable
                                                                                  Rising    edge    at
SizeOfOutput       UINT            12            62               ----------
                                                                                  Enable
                                                                                  Rising    edge    at
Slot               UINT            1             63               1
                                                                                  Enable

Functional description
The function block IH_S20MBRTUMaster ensures the communication between
the controller and the physical line network (slaves) in RTU mode. It receives
requests from other function blocks of function codes and sends them via
the modules S20-RS-UNI to the slaves. It receives a response from one slave
and sends it back to the function block that sent the request. The function
block ensures the communication with the terminal. "InputAdr" and "Outpu‐
tAdr" have to be mapped in the terminal. "MBData" has to be linked to other
function blocks of function codes in the program. The structure is used for
communication purposes and data exchange with other function blocks. The
function block communicates with up to 33 function blocks of function codes
at the same time.
The function block is enabled after the first PLC cycle by setting the "Enable"
input to TRUE. The “InOperation" output is set to TRUE during operation.
If function codes are detected in the queue, the function block starts the
processing until the "Enable" bit is set to TRUE. If an error results during the
operation, the "Error" bit is set to TRUE. "ErrorID" and "ErrorIdent" show error
information. The error can be acknowledged via a rising edge at the "Enable"
input.
Handling
.    If a data width of 7 bits is selected for the communication, the MODBUS
     master or the slave can cause an error. A data width of 8 bits is the best
     for the communication.
Example of a function block:
The function block IH_S20MBRTUMaster has to be instantiated together
with other function blocks to communicate with the Modbus slave. The
input/output variable "stMBData" exchanges data between the function block
IH_S20MBRTUMaster and other function blocks. Thus, this variable has to be
assigned to "MBData" to both function blocks.
In the example, the function block IH_S20MBRTUMaster is configured to
exchange data with the Modbus unit and other Modbus function blocks.
For communication purposes, the variables "Input ProcessData" and "Output
ProcessData" have to be assigned to the Modbus unit.

Communication with S20-RS-UNI at S20-EC-BK
The function block IH_S20MBRTUMaster is used to communicate with the
Modbus slaves via the S20-RS-UNI module.

Variable declaration

PROGRAM Example_IH_S20MBRTUMaster
VAR
  // Bus Configuration FB
  fbIH_S20ComConfiguration    : CXA_ModbusRTU.CXA_S20.IH_S20ComConfiguration; // ComConfiguration FB Instance
  bEnable_ComConfig           : BOOL;                                         // TRUE: FB is enabled
  bInOperation_ComConfig      : BOOL;                                         // TRUE: FB is processing its task
  bError_ComConfig            : BOOL;                                         // TRUE: Indicates as error
  ErrorID_ComConfig           : ERROR_CODE;                                   // Class of error
  ErrorIdent_ComConfig        : ERROR_STRUCT;                                 // Detailed information about error
  enBusType                   : CXA_ModbusRTU.CXA_S20.IH_S20_BUSTYPE;         // Bus type selection
  stBusConfig                 : CXA_ModbusRTU.CXA_S20.IH_S20_BUS_CONFIG;      // Bus configuration parameters
  strBusMaster                : STRING (100) := 'ethercatmaster';             // Bus Master Name

  // Master FB
  fbIH_S20MBRTUMaster         : IH_S20MBRTUMaster;        // S20MBRTU Master FB Instance
  bEnable                     : BOOL;                     // TRUE: Function Block is enabled
  bInOperation                : BOOL;                     // TRUE: FB is processing its task

  bError                      : BOOL;                     // TRUE: Indicates as error
  ErrorID                     : ERROR_CODE;               // Class of error
  ErrorIdent                  : ERROR_STRUCT;             // Detailed information about error
  uiSlot                      : UINT;                     // Module Slot number
  stMBConfig                  : IH_S20_MB_CONFIG;         // Configuration of Modbus
  arInProcData                : ARRAY[0..19] OF BYTE;     // Input Process variable
  arOutProcData               : ARRAY[0..19] OF BYTE;     // Output Process variable
  bBusy                       : BOOL;                     // True when the block is busy/ used
  uiNoOfRequests              : UINT;                     // Number of sent requests
  uiNoOfResponses             : UINT;                     // Number of received responses
  stMBData                    : IH_INLN_MB_DATA;          // Structure used to handle data b/w Master and other
Modbus function blocks of function codes

  // Data Map Function
  wStatusWord                 : WORD;                     // Status word of S20-RS UNI
  arInputComplexProtocol      : ARRAY[0..17] OF BYTE;     // Input protocol data words
  wControlWord                : WORD;                     // Control word of S20-RS UNI
  arOutputComplexProtocol     : ARRAY[0..17] OF BYTE;     // Output protocol data words

  // Read Coils FB
  fbIH_MBReadCoils            : IH_MBReadCoils;           // FB Instance
  bEnable_ReadCoils           : BOOL;                     // TRUE: Function Block is enabled
  bDone_ReadCoils             : BOOL;                     // TRUE: Function Block has completed its task
  bActive_ReadCoils           : BOOL;                     // TRUE: Function Block is working on its actual task
  bError_ReadCoils            : BOOL;                     // TRUE: Indicates as error
  ErrorID_ReadCoils           : ERROR_CODE;               // Class of error
  ErrorIdent_ReadCoils        : ERROR_STRUCT;             // Detailed information about error
  bSendRequest_ReadCoils      : BOOL;                     // A rising edge sends a request
  bEnablePoll_ReadCoils       : BOOL;                     // Polling enabled. No need for SendRequest to be
triggered every interval. The block sends requests automatically
  bySlaveAddress_ReadCoils    : BYTE := 1;                // Slave address
  wStartAddress_ReadCoils     : WORD := WORD#1000;        // Starting address of Coil Bit
  uiNoOfCoils_ReadCoils       : UINT := UINT#8;           // Quantity of Coils
  arReadCoils_ReadCoils       : ARRAY[0..20] OF BOOL;     // Array to store Input bits
  tPollInterval_ReadCoils     : TIME := T#1S;             // Polling interval. Request is sent continuously in
intervals
  tTimeOut_ReadCoils          : TIME := T#3S;             // Timeout interval for slaves to respond
  bBusy_ReadCoils             : BOOL;                     // True when the Function Block is communicating with
master
END_VAR

Implementation

// "IH_S20ComConfiguration" FB should be instantiated to generate "BusHandle", which is required for Master FB,
to communicate with S20-RS-UNI module
// Bus configuration variables Initialization
bEnable_ComConfig                 := TRUE; // Enabling Bus Configuration FB

enBusType                         := CXA_ModbusRTU.CXA_S20.IH_S20_BUSTYPE.ETHERCAT;                        // Bus
Type: EtherCAT is slected
stBusConfig.EtherCAT.BusMaster    := ADR(strBusMaster);                                                    //
Busmaster : ethercatmaster
stBusConfig.EtherCAT.AddressType := CXA_ModbusRTU.CXA_S20.IL_ECAT_ADDRESS_TYPE.ECAT_ETHERCAT_ADDRESS;      //
Address Type: ECAT_ETHERCAT_ADDRESS
stBusConfig.EtherCAT.SlaveAddress := 1001;                                                                 //
EtherCAT Master Address

fbIH_S20ComConfiguration(
      Enable:= bEnable_ComConfig,
      InOperation=> bInOperation_ComConfig,
      Error=> bError_ComConfig,
      ErrorID=> ErrorID_ComConfig,
      ErrorIdent=> ErrorIdent_ComConfig,
      BusType:= enBusType,
      BusConfig:= stBusConfig,
      S20BusHandle=> );

// Master FB is Enabled with condition of "bEnable AND bInOperation_ComConfig", is to ensure that
"IH_S20ComConfiguration" FB is enabled and in InOperation
// Because Master FB needs 'BusHandle' from "IH_S20ComConfiguration" FB

// Variables Initialization
bEnable   := TRUE; // Enabling Master FB
uiSlot    := 1; // S20-RS-UNI Physical slot number

// Modbus Configuration
stMBConfig.Baudrate        := CXA_ModbusRTU.CXA_S20.IH_S20_RS_BAUDRATE.BAUDRATE_19200;              // BaudRate
stMBConfig.Protocol        := CXA_ModbusRTU.CXA_S20.IH_S20_RS_PROTOCOL.TRANSPARENT;                 // Protocol Type
stMBConfig.DataWidth       := CXA_ModbusRTU.CXA_S20.IH_S20_RS_DATAWIDTH.DATABIT8_EVEN_STOPBIT2;     // Data Width
stMBConfig.InterfaceType   := CXA_ModbusRTU.CXA_S20.IH_S20_RS_INTERFACE.RS232;                      // Interface
Type

fbIH_S20MBRTUMaster(
      Enable:= bEnable AND bInOperation_ComConfig,
      InOperation=> bInOperation,
      Error=> bError,
      ErrorID=> ErrorID,
      ErrorIdent=> ErrorIdent,
      S20BusHandle:= fbIH_S20ComConfiguration.S20BusHandle,
      Slot:= uiSlot,
      MBConfig:= stMBConfig,
      InputAdr:= ADR(arInProcData),
      SizeOfInput:= SIZEOF(arInProcData),
      OutputAdr:= ADR(arOutProcData),
      SizeOfOutput:= SIZEOF(arOutProcData),
      Busy=> bBusy,
      NoOfRequests=> uiNoOfRequests,
      NoOfResponses=> uiNoOfResponses,
      MBData:= stMBData);

// The EtherCAT fieldbus modules Process data structure is not compatible with "IH_S20MBRTUMaster" FB process
data inputs.
// Hence "IH_S20RSComDataMap" function is required to call along with "IH_S20MBRTUMaster" FB, to make process
data structure of the S20-RS-UNI module compatible to "IH_S20MBRTUMaster" FB inputs.
// Link "wStatusWord", "arInputComplexProtocol", "wControlWord" & "arOutputComplexProtocol" to the S20_RS-UNI
module
// Link "arInProcData" & "arOutProcData" to IH_S20MBRTUMaster FB
// Data map function will generate "arInProcData" by reading inputs "wStatusWord" & "arInputComplexProtocol"
variables
// Data map function will generate "wControlWord" & "arOutputComplexProtocol" by reading "arOutProcData"
CXA_ModbusRTU.IH_S20RSComDataMap(
       StatusWord:= wStatusWord,
       InputComplexProtocol:= arInputComplexProtocol,
       OutProcData:= arOutProcData,
       ControlWord=> wControlWord,
       OutputComplexProtocol=> arOutputComplexProtocol,
       InProcData=> arInProcData);

// Read Coils example is shown here, to illustarte Master FB Operation
// The Raising Edge at 'bSendRequest_ReadCoils' input will read '8' coils from slave with the start address
0x1000 only one time and the result will be available at 'arReadCoils' array.
// If you want to read one more time, then make state transition (TRUE -> FALSE) and again give TRUE at
'bSendRequest' input
// If you want to read the coils from slave at regular intervals automatically, then set 'bEnablePoll' variable
to TRUE and 'tPollInterval' to more than or equal to 1 second. In this case, Raising edge at 'bSendRequest' is
not required.

// The function block "IH_MBReadCoils" should be instantiated along with "IH_S20MBRTUMaster" to communicate with
the Modbus slave. Use a common variable at the MBData of "IH_MBReadCoils" & "IH_S20MBRTUMaster" function blocks
to exchange the data with the Modbus slave.

// Read Coils Variable Initialization
IF    (fbIH_S20MBRTUMaster.InOperation = TRUE) THEN // Ensuring that Master FB is in Inoperation, before sending
request
bEnable_ReadCoils   := TRUE;
bSendRequest_ReadCoils := TRUE;
END_IF

bySlaveAddress_ReadCoils := 1; // Ensure that Modbus Slave with "Slave Address: 1" is active and connected to
Master before running this example.
wStartAddress_ReadCoils   := WORD#1000;// Start address of the coils data
uiNoOfCoils_ReadCoils     := UINT#8; // Number of coils to be read

// Read Coils FB Instance

fbIH_MBReadCoils(
Enable:= bEnable_ReadCoils,
Done=> bDone_ReadCoils,
Active=> bActive_ReadCoils,
Error=> bError_ReadCoils,
ErrorID=> ErrorID_ReadCoils,
ErrorIdent=> ErrorIdent_ReadCoils,
SendRequest:= bSendRequest_ReadCoils,
EnablePoll:= bEnablePoll_ReadCoils,
SlaveAddress:= bySlaveAddress_ReadCoils,
StartAddress:= wStartAddress_ReadCoils,
NoOfCoils:= uiNoOfCoils_ReadCoils,
ValueAdr:= ADR(arReadCoils_ReadCoils),
SizeOfValue:= SIZEOF(arReadCoils_ReadCoils),
PollInterval:= tPollInterval_ReadCoils,
TimeOut:= tTimeOut_ReadCoils,
Busy=> bBusy_ReadCoils,
MBData:= stMBData);

Process data mapping

## 16.16 IH_S20MBRTUSlave

Function code
FC 1, 2, 3, 4, 5, 6, 15, 16, 22 and 23

       Brief description
       The function block IH_S20MBRTUSlave ensures the communication between
       the controller and the physical line network (master) in RTU mode. Thus, the
       controller (module S20-RS-UNI) can act like a slave with the address at the
       SlaveAddress input.
       The following function codes are supported: 1, 2, 3, 4, 5, 6, 15, 16, 22 und
       23.
       The function block has to be instantiated once for all terminals.

       Interface description

Table 292: Interface variables of the IH_S20MBRTUSlave function block
I/O type           Name                 Data type        Description
VAR_INPUT          Enable               BOOL             Function block active if TRUE
                                        POINTER       TO
                   S20BusHandle         IH_S20_BUS_IDEN‐ Bus handle for the S20 IO configuration
                                        TIFIER
                   Slot                 UINT             Module slot 1..63
                                        ⮫ IH_S20_MB_CON
                   MBConfig                             Used for the configuration
                                        FIG
                   SlaveAddress         BYTE            Slave address
                                                        Address offset
                                                        If the offset is 2000 for example, the
                   Offset               WORD            address of the Holding register with
                                                        address number 3 is 2003 (2000 + 3) in the
                                                        array HoldingRegisters and not 3
                                        POINTER      TO Address of the array to save input process
                   InputAdr             ARRAY[0..19] OF data
                                        BYTE            Use the ADR () operator
                                                        Size of the InputAdr array
                   SizeOfInput          UINT
                                                        Use the SIZEOF () operator
                                        POINTER      TO Address of the array to save output process
                   OutputAdr            ARRAY[0..19] OF data
                                        BYTE            Use the ADR () operator
                                                        Size of the OutputAdr array
                   SizeOfOutput         UINT
                                                        Use the SIZEOF () operator

I/O type       Name          Data type         Description
POINTER        TO
HoldingRegister‐                    Address of the array is used to save Hol‐
ARRAY[0...65535]
sAdr                                dingRegisters Operator ADR ()
OF WORD
SizeOfHolding‐                      Size of the HoldingRegisters array
UDINT
Registers                           Use the SIZEOF () operator
POINTER        TO Address of the array to save InputRegisters
InputRegistersAdr ARRAY[0...65535]
OF WORD           Use the ADR () operator

SizeOfInputRegis‐                   Size of the InputRegisters array
UDINT
ters                                Use the SIZEOF () operator

CoilsAdr          POINTER        TO Address of the array to save Coils data
ARRAY[0..8191]
OF BOOL           Use the ADR () operator
SizeOfCoils       UDINT             Size of the Coils array
                  Use the SIZEOF () operator
InputBitsAdr      POINTER        TO Address of the array to save InputBits
ARRAY[0..8191]
OF BOOL           Use the ADR () operator
SizeOfInputBits   UDINT             Size of the InputBits array
                  Use the SIZEOF () operator
VAR_OUTPUT InOperation       BOOL              The function block is working at its actual
                  task
Error             BOOL              Indicates an error
ErrorID           ⮫ ERROR_CODE      Error class
ErrorIdent         ⮫ ERROR_STRUCT Detailed error information
Busy               BOOL           True if the function block communicates
                    with the master
NoOfTransactions   UINT           Number of transactions

Min./max. and default values
The following table lists the min./max. and default values as well as the
application behavior of the function block inputs.
Table 293: Min./max. and default values as well as the response of the function block inputs of
IH_S20MBRTUSlave during application
Name               Data type       Min. value    Max. value       Default value   Effective
Enable             BOOL            FALSE         TRUE             FALSE           Continuous
                                                                                  Rising    edge    at
SlaveAddress       BYTE            0             247              0
                                                                                  Enable
                                                                                  Rising    edge    at
Offset             WORD            0             65536            0
                                                                                  Enable
                                                                  ----------      Rising    edge    at
SizeOfInput        UINT            12            62
                                                                                  Enable
                                                                  ----------      Rising    edge    at
SizeOfOutput       UINT            12            62
                                                                                  Enable
SizeOfHolding‐                                                    ----------      Rising    edge    at
               UDINT               1             65535
Registers                                                                         Enable
SizeOfInpu‐                                                       ----------      Rising    edge    at
               UDINT               1             65535
tRegisters                                                                        Enable
                                                                                  Rising    edge    at
SizeOfCoils        UDINT           1             8192             ----------
                                                                                  Enable
SizeOfInput‐                                                                      Rising    edge    at
                   UDINT           1             8192             ----------
Bits                                                                              Enable
                                                                                  Rising    edge    at
Slot               UINT            1             63               1
                                                                                  Enable

Functional description
Due to the function block IH_S20MBRTUSlave, the controller acts like a slave
in the RTU mode. Thus, the controller (module S20-RS-UNI) can act like a
slave with the address at the SlaveAddress input. It is provided with data
arrays emulating registers and bits like in the memory of a slave device.
The function block is enabled after the first PLC cycle by setting the "Enable"
input to TRUE. The “InOperation" output is set to TRUE during operation.
If function codes are detected in the queue, the function block starts the
processing until the "Enable" bit is set to TRUE. If an error results during the
operation, the "Error" bit is set to TRUE. "ErrorID" and "ErrorIdent" show error
information. The error can be acknowledged via a rising edge at the "Enable"
input.
Handling
.     If a data width of 7 bits is selected for the communication, the MODBUS
      master or the slave can cause a CRC error. A data width of 8 bits is the
      best for the communication.
Example of a function block
The function block IH_S20MBRTUSlave has to be instantiated once for each
Modbus module that should act like a slave with the address specified at the
SlaveAddress input.

Example 1
In this example, the function block configures the module R IB IL RS485 PRO
as Modbus slave.
Before enabling the function block, create an array for the Holding register
(arHoldingRegisters), Input register (arInputRegisters), Coils (arCoils) and
Input bits (arInputBits).
Additionally, create an array for process-internal (arInProcessData) and
process-external data (arOutProcessData) and the variables and process data
of the module R IB IL RS 485 PRO have to be mapped.
Assign the address to the SlaveAddress input and enable the function block.
The function block sets the variable "InOperation" to TRUE and thus indicates

that the slave is ready.

Variable declaration

PROGRAM Example_IH_S20MBRTUSlave
VAR
  // Bus Configuration FB
  fbIH_S20ComConfiguration    : CXA_ModbusRTU.CXA_S20.IH_S20ComConfiguration; // ComConfiguration FB Instance
  bEnable_ComConfig           : BOOL;                                         // TRUE: FB is enabled
  bInOperation_ComConfig      : BOOL;                                         // TRUE: FB is processing its task
  bError_ComConfig            : BOOL;                                         // TRUE: Indicates as error
  ErrorID_ComConfig           : ERROR_CODE;                                   // Class of error
  ErrorIdent_ComConfig        : ERROR_STRUCT;                                 // Detailed information about error
  enBusType                   : CXA_ModbusRTU.CXA_S20.IH_S20_BUSTYPE;         // Bus type selection
  stBusConfig                 : CXA_ModbusRTU.CXA_S20.IH_S20_BUS_CONFIG;      // Bus configuration parameters
  strBusMaster                : STRING (100) := 'ethercatmaster';             // Bus Master Name

  // Slave FB
  fbIH_S20MBRTUSlave          : IH_S20MBRTUSlave;          // S20MBRTU Slave FB Instance
  bEnable                     : BOOL;                      // TRUE: Function Block is enabled
  bInOperation                : BOOL;                      // TRUE: FB is processing its task
  bError                      : BOOL;                      // TRUE: Indicates as error
  ErrorID                     : ERROR_CODE;                // Class of error
  ErrorIdent                  : ERROR_STRUCT;              // Detailed information about error
  uiSlot                      : UINT;                      // Module Slot number
  stMBConfig                  : IH_S20_MB_CONFIG;          // Configuration of Modbus
  bySlaveAddress              : BYTE;                      // Slave address
  wOffset                     : WORD;                      // Address offset
  arInProcData                : ARRAY[0..19] OF BYTE;      // Input Process variable
  arOutProcData               : ARRAY[0..19] OF BYTE;      // Output Process variable
  arHoldingReg_Slave          : ARRAY[0..65535] OF WORD;   // Array to store HoldingRegisters
  arInputReg_Slave            : ARRAY[0..65535] OF WORD;   // Array to store InputRegisters
  arCoils_Slave               : ARRAY[0..8191] OF BOOL;    // Array to store Coils data
  arInputBits_Slave           : ARRAY[0..8191] OF BOOL;    // Array to store InputBits
  bBusy                       : BOOL;                      // True when the block is busy/ used
  uiNoOfTransactions          : UINT;                      // Number of Transactions happened

  // Data Map Function
  wStatusWord                 : WORD;                      // Status word of S20-RS UNI
  arInputComplexProtocol      : ARRAY[0..17] OF BYTE;      // Input protocol data words
  wControlWord                : WORD;                      // Control word of S20-RS UNI
  arOutputComplexProtocol     : ARRAY[0..17] OF BYTE;      // Output protocol data words
END_VAR

Implementation

// "IH_S20ComConfiguration" FB should be instantiated to generate "BusHandle", which is required for Slave FB, to
communicate with S20-RS-UNI module
// Bus configuration variables Initialization
bEnable_ComConfig                  := TRUE; // Enabling Bus Configuration FB

enBusType                         := CXA_ModbusRTU.CXA_S20.IH_S20_BUSTYPE.ETHERCAT;                       // Bus
Type: EtherCAT is slected
stBusConfig.EtherCAT.BusMaster    := ADR(strBusMaster);                                                   //
Busmaster : ethercatmaster
stBusConfig.EtherCAT.AddressType := CXA_ModbusRTU.CXA_S20.IL_ECAT_ADDRESS_TYPE.ECAT_ETHERCAT_ADDRESS;     //
Address Type: ECAT_ETHERCAT_ADDRESS
stBusConfig.EtherCAT.SlaveAddress := 1001; // EtherCAT Master Address

fbIH_S20ComConfiguration(
      Enable:= bEnable_ComConfig,
      InOperation=> bInOperation_ComConfig,
      Error=> bError_ComConfig,
      ErrorID=> ErrorID_ComConfig,
      ErrorIdent=> ErrorIdent_ComConfig,
      BusType:= enBusType,
      BusConfig:= stBusConfig,
      S20BusHandle=> );

// Slave FB is Enabled with condition of "bEnable AND bInOperation_ComConfig", is to ensure that
"IH_S20ComConfiguration" FB is enabled and in InOperation
// Because Slave FB needs 'BusHandle' from "IH_S20ComConfiguration" FB

// Variables Initialization
bEnable   := TRUE; // Enabling Master FB
uiSlot    := 2; // S20-RS-UNI Physical slot number

// Modbus Configuration
stMBConfig.Baudrate        := CXA_ModbusRTU.CXA_S20.IH_S20_RS_BAUDRATE.BAUDRATE_19200;             // BaudRate
stMBConfig.Protocol        := CXA_ModbusRTU.CXA_S20.IH_S20_RS_PROTOCOL.TRANSPARENT;                // Protocol Type
stMBConfig.DataWidth       := CXA_ModbusRTU.CXA_S20.IH_S20_RS_DATAWIDTH.DATABIT8_EVEN_STOPBIT2;    // Data Width
stMBConfig.InterfaceType   := CXA_ModbusRTU.CXA_S20.IH_S20_RS_INTERFACE.RS485;                     // Interface
Type

fbIH_S20MBRTUSlave(
      Enable:= bEnable AND bInOperation_ComConfig,
      InOperation=> bInOperation,
      Error=> bError,
      ErrorID=> ErrorID,
      ErrorIdent=> ErrorIdent,
      S20BusHandle:= fbIH_S20ComConfiguration.S20BusHandle,
      Slot:= uiSlot,
      MBConfig:= stMBConfig,
      SlaveAddress:= bySlaveAddress,
      Offset:= wOffset,
      InputAdr:= ADR(arInProcData),
      SizeOfInput:= SIZEOF(arInProcData),
      OutputAdr:= ADR(arOutProcData),
      SizeOfOutput:= SIZEOF(arOutProcData),
      HoldingRegistersAdr:= ADR(arHoldingReg_Slave),
      SizeOfHoldingRegisters:= SIZEOF(arHoldingReg_Slave),
      InputRegistersAdr:= ADR(arInputReg_Slave),
      SizeOfInputRegisters:= SIZEOF(arInputReg_Slave),
      CoilsAdr:= ADR(arCoils_Slave),
      SizeOfCoils:= SIZEOF(arCoils_Slave),
      InputBitsAdr:= ADR(arInputBits_Slave),
      SizeOfInputBits:= SIZEOF(arInputBits_Slave),
      Busy=> bBusy,
      NoOfTransactions=> uiNoOfTransactions);

// The EtherCAT fieldbus modules Process data structure is not compatible with "IH_S20MBRTUSlave" FB process data
inputs.
// Hence "IH_S20RSComDataMap" function is required to call along with "IH_S20MBRTUSlave" FB, to make process data
structure of the S20-RS-UNI module compatible to "IH_S20MBRTUSlave" FB inputs.
// Link "wStatusWord", "arInputComplexProtocol", "wControlWord" & "arOutputComplexProtocol" to the S20_RS-UNI
module
// Link "arInProcData" & "arOutProcData" to IH_S20MBRTUSlave FB
// Data map function will generate "arInProcData" by reading inputs "wStatusWord" & "arInputComplexProtocol"
variables
// Data map function will generate "wControlWord" & "arOutputComplexProtocol" by reading "arOutProcData"
CXA_ModbusRTU.IH_S20RSComDataMap(
       StatusWord:= wStatusWord,
       InputComplexProtocol:= arInputComplexProtocol,
       OutProcData:= arOutProcData,
       ControlWord=> wControlWord,
       OutputComplexProtocol=> arOutputComplexProtocol,
       InProcData=> arInProcData);

Process data mapping

## 16.17 IH_XIMBRTUMaster

Brief description
The function block IH_XIMBRTUMaster ensures the communication between
the controller and the physical line network (slaves) in RTU mode. It receives
requests from other function blocks of function codes and sends them via the
ctrlX I/O modules XI521001/XI522001 to the slaves. It receives the response
from all slaves and sends them back to the function block that originally sent
the request. The function block has to be instantiated once for all terminals.
It communicates with up to 33 function blocks of function codes at the same
time.

        Interface description

Table 294: Interface variables of the IH_XIMBRTUMaster function block
I/O type           Name                  Data type          Description
VAR_INPUT          Enable                BOOL               Function block active if TRUE
                                         REFERENCE      TO
                   InProcData            IH_XI_INPROC_DAT Address of the array for input process data
                                         A
                                         REFERENCE
                                                            Address of the array for output process
                   OutProcData           TO      IH_XI_OUT‐
                                                            data
                                         PROC_DATA
VAR_OUTPUT                                                  The function block is working at its actual
                   InOperation           BOOL
                                                            task
                   Error                 BOOL               Indicates an error
                   ErrorID               ⮫ ERROR_CODE       Error class
                   ErrorIdent            ⮫ ERROR_STRUCT Detailed error information
                                                          True if the function block communicates
                   Busy                  BOOL
                                                          with function blocks of the function code
                   NoOfRequests          UINT             Number of requests sent
                   NoOfResponses         UINT             Number of responses received
VAR_IN_OUT         MBData                ⮫ IH_INLN_MB_DAT Structure handles data between the
                                         A                IH_XIMBRTUMaster and other Modbus func‐
                                                          tion blocks of function codes

Functional description
The function block IH_XIMBRTUMaster ensures the communication between
the controller and the physical line network (slaves) in RTU mode. It receives
requests from other function blocks of function codes and sends them via the
ctrlX I/O modules XI521001/XI522001 to the slaves. It receives a response
from one slave and sends it back to the function block that sent the request.
The function block ensures the communication with the terminal. "InProcData"
and "OutProcData" have to be mapped in the terminal. "MBData" has to be
linked to other function blocks of function codes in the program. The struc‐
ture is used for communication purposes and data exchange with other func‐
tion blocks. The function block communicates with up to 33 function blocks of
function codes at the same time.

The function block is enabled after the first PLC cycle by setting the "Enable"
input to TRUE. The "InOperation" output is set to TRUE during operation.
If function codes are detected in the queue, the function block starts the
processing until the "Enable" bit is set to TRUE. If an error results during the
operation, the "Error" bit is set to TRUE. "ErrorID" and "ErrorIdent" show error
information. The error can be acknowledged via a rising edge at the "Enable"
input.
Handling
.    If a data width of 7 bits is selected for the communication, the MODBUS
     master or the slave can cause an error. A data width of 8 bits is the best
     for the communication.
Example of a function block:
The function block IH_XIMBRTUMaster has to be instantiated together with
other function blocks to communicate with the Modbus slave. The input/
output variable "stMBData" exchanges data between the function block
IH_XIMBRTUMaster and other function blocks. Thus, this variable has to be
assigned to "MBData" to both function blocks.
In the example, the function block IH_XIMBRTUMaster is configured to
exchange data with the Modbus unit and other Modbus function blocks.
For communication purposes, the variables "Input ProcessData" and "Output
ProcessData" have to be assigned to the Modbus unit.

Communication with the ctrlX I/O modules XI521001/XI522001 on an XB-
EC-12 or ctrlX CORE
The function block IH_XIMBRTUMaster is used to communicate with the
Modbus slaves via the ctrlX I/O modules XI521001/XI522001.

Variable declaration

PROGRAM Example_IH_XIMBRTUMaster
VAR
  // Master FB
  fbIH_XIMBRTUMaster          : IH_XIMBRTUMaster;        // XIMBRTU Master FB Instance
  bEnable                     : BOOL;                    // TRUE: Function Block is enabled
  bInOperation                : BOOL;                    // TRUE: FB is processing its task
  bError                      : BOOL;                    // TRUE: Indicates as error
  ErrorID                     : ERROR_CODE;              // Class of error
  ErrorIdent                  : ERROR_STRUCT;            // Detailed information about error
  bBusy                       : BOOL;                    // True when the block is busy/ used
  uiNoOfRequests              : UINT;                    // Number of sent requests
  uiNoOfResponses             : UINT;                    // Number of received responses
  stMBData                    : IH_INLN_MB_DATA;         // Structure used to handle data b/w Master and other
Modbus function blocks of function codes

  // Read Coils FB
  fbIH_MBReadCoils            : IH_MBReadCoils;           // FB Instance
  bEnable_ReadCoils           : BOOL;                     // TRUE: Function Block is enabled
  bDone_ReadCoils             : BOOL;                     // TRUE: Function Block has completed its task
  bActive_ReadCoils           : BOOL;                     // TRUE: Function Block is working on its actual task
  bError_ReadCoils            : BOOL;                     // TRUE: Indicates as error
  ErrorID_ReadCoils           : ERROR_CODE;               // Class of error
  ErrorIdent_ReadCoils        : ERROR_STRUCT;             // Detailed information about error
  bSendRequest_ReadCoils      : BOOL;                     // A rising edge sends a request
  bEnablePoll_ReadCoils       : BOOL;                     // Polling enabled. No need for SendRequest to be
triggered every interval. The block sends requests automatically
  bySlaveAddress_ReadCoils    : BYTE := 1;                // Slave address
  wStartAddress_ReadCoils     : WORD := WORD#1000;        // Starting address of Coil Bit
  uiNoOfCoils_ReadCoils       : UINT := UINT#8;           // Quantity of Coils
  arReadCoils_ReadCoils       : ARRAY[0..20] OF BOOL;     // Array to store Input bits
  tPollInterval_ReadCoils     : TIME := T#1S;             // Polling interval. Request is sent continuously in
intervals
  tTimeOut_ReadCoils          : TIME := T#3S;             // Timeout interval for slaves to respond
  bBusy_ReadCoils             : BOOL;                     // True when the Function Block is communicating with
master

  // Process Data mapping; Change Mapping Address(Ex:- %IB227) as per your module mapping address.
  stInProcData AT %IB227 : CXA_ModbusRTU.CXA_ctrlXIO.IH_XI_INPROC_DATA;       // Input process data structure.
Link this variable to module process data
  stOutProcData AT %QB74 : CXA_ModbusRTU.CXA_ctrlXIO.IH_XI_OUTPROC_DATA;      // Output process data structure.
Link this variable to module process data
END_VAR

Implementation

// Master FB Instance
fbIH_XIMBRTUMaster(
Enable:= bEnable,
InOperation=> bInOperation,
Error=> bError,
ErrorID=> ErrorID,
ErrorIdent=> ErrorIdent,
InProcData:= stInProcData,
OutProcData:= stOutProcData,
Busy=> bBusy,
NoOfRequests=> uiNoOfRequests,
NoOfResponses=> uiNoOfResponses,
MBData:= stMBData);

// Read Coils Variable Initialization
IF     (fbIH_XIMBRTUMaster.InOperation = TRUE) THEN // Ensuring that Master FB is in Inoperation, before sending
request

bEnable_ReadCoils    := TRUE;
bSendRequest_ReadCoils := TRUE;
END_IF

bySlaveAddress_ReadCoils := 1;            // Ensure that Modbus Slave with "Slave Address: 1" is active and
connected to Master before running this example.
wStartAddress_ReadCoils       := WORD#1000;   // Start address of the coils data
uiNoOfCoils_ReadCoils     := UINT#8;      // Number of coils to be read

// Read Coils FB Instance
fbIH_MBReadCoils(
Enable:= bEnable_ReadCoils,
Done=> bDone_ReadCoils,
Active=> bActive_ReadCoils,
Error=> bError_ReadCoils,
ErrorID=> ErrorID_ReadCoils,
ErrorIdent=> ErrorIdent_ReadCoils,
SendRequest:= bSendRequest_ReadCoils,
EnablePoll:= bEnablePoll_ReadCoils,
SlaveAddress:= bySlaveAddress_ReadCoils,
StartAddress:= wStartAddress_ReadCoils,
NoOfCoils:= uiNoOfCoils_ReadCoils,
ValueAdr:= ADR(arReadCoils_ReadCoils),
SizeOfValue:= SIZEOF(arReadCoils_ReadCoils),
PollInterval:= tPollInterval_ReadCoils,
TimeOut:= tTimeOut_ReadCoils,
Busy=> bBusy_ReadCoils,
MBData:= stMBData);

Process data mapping
"stInProcData" and "stOutProcData" are assigned directly to the I/O variable
mapping by the module using the % address.

## 16.18 IH_XIMBRTUSlave

Function code
FC 1, 2, 3, 4, 5, 6, 15, 16, 22 and 23

Brief description
The function block IH_XIMBRTUSlave ensures the communication between the
controller and the physical line network (master) in RTU mode. Thus, the
controller (ctrlX I/O-Module XI521001/XI522001) can act like a slave with the
address at the SlaveAddress input.
The following function codes are supported: 1, 2, 3, 4, 5, 6, 15, 16, 22 und
23.
The function block has to be instantiated once for all terminals.

Interface description

Table 295: Interface variables of the IH_XIMBRTUSlave function block
I/O type           Name               Data type      Description
VAR_INPUT          Enable             BOOL           Function block active if TRUE
                   SlaveAddress       BYTE           Slave address
                                                     Address offset
                                                     If the offset is 2000 for example, the
                   Offset             WORD           address of the Holding register with
                                                     address number 3 is 2003 (2000 + 3) in the
                                                     array HoldingRegisters and not 3
                             REFERENCE      TO
                                                Address of the array to save input process
                   InProcDataIH_XI_INPROC_DAT
                                                data
                             A
                             REFERENCE
                                                Address of the array to save output process
           OutProcData       TO      IH_XI_OUT‐
                                                data
                             PROC_DATA
                             POINTER        TO
           HoldingRegister‐                     Address of the array is used to save Hol‐
                             ARRAY[0...65535]
           sAdr                                 dingRegisters Operator ADR ()
                             OF WORD
           SizeOfHolding‐                       Size of the HoldingRegisters array
                             UDINT
           Registers                            Use the SIZEOF () operator
                             POINTER        TO Address of the array to save InputRegisters
           InputRegistersAdr ARRAY[0...65535]
                             OF WORD            Use the ADR () operator

SizeOfInputRegis‐                    Size of the InputRegisters array
UDINT
ters                                 Use the SIZEOF () operator
CoilsAdr          POINTER        TO Address of the array to save Coils data
ARRAY[0..8191]
OF BOOL            Use the ADR () operator
SizeOfCoils       UDINT              Size of the Coils array
                   Use the SIZEOF () operator
InputBitsAdr      POINTER        TO Address of the array to save InputBits
ARRAY[0..8191]
OF BOOL            Use the ADR () operator
SizeOfInputBits   UDINT              Size of the InputBits array
                   Use the SIZEOF () operator
VAR_OUTPUT InOperation       BOOL               The function block is working at its actual
                   task
Error             BOOL               Indicates an error
ErrorID           ⮫ ERROR_CODE       Error class

I/O type       Name                  Data type           Description
ErrorIdent            ⮫ ERROR_STRUCT Detailed error information
Busy                  BOOL           True if the function block communicates
                              with the master
NoOfTransactions      UINT           Number of transactions

Min./max. and default values
The following table lists the min./max. and default values as well as the
application behavior of the function block inputs.
Table 296: Min./max. and default values as well as the response of the function block inputs of
IH_XIMBRTUSlave during application

Name            Data type        Min. value      Max. value       Default value     Effective
Enable          BOOL             FALSE           TRUE             FALSE             Continuous
                                                                                    Rising    edge   at
SlaveAddress    BYTE             0               247              0
                                                                                    "Enable"
                                                                                    Rising    edge   at
Offset          WORD             0               65536            0
                                                                                    "Enable"
SizeOfHolding‐                                                    ----------        Rising    edge   at
               UDINT             1               65535
Registers                                                                           "Enable"
SizeOfInpu‐                                                       ----------        Rising    edge   at
               UDINT             1               65535
tRegisters                                                                          "Enable"
                                                                                    Rising    edge   at
SizeOfCoils     UDINT            1               8192             ----------
                                                                                    "Enable"
SizeOfInput‐                                                                        Rising    edge   at
                UDINT            1               8192             ----------
Bits                                                                                "Enable"

Functional description
Due to the function block IH_XIMBRTUSlave, the controller acts like a slave
in the RTU mode. Thus, the controller (ctrlX I/O-Module XI521001/XI522001)
can act like a slave with the address at the SlaveAddress input. It is provided
with data arrays emulating registers and bits like in the memory of a slave
device.
The function block is enabled after the first PLC cycle by setting the "Enable"
input to TRUE. The "InOperation" output is set to TRUE during operation.
If function codes are detected in the queue, the function block starts the
processing until the "Enable" bit is set to TRUE. If an error results during the
operation, the "Error" bit is set to TRUE. "ErrorID" and "ErrorIdent" show error
information. The error can be acknowledged via a rising edge at the "Enable"
input.
Handling
.     If a data width of 7 bits is selected for the communication, the MODBUS
      master or the slave can cause a CRC error. A data width of 8 bits is the
      best for the communication.
Example of a function block
The function block IH_XIMBRTUSlave has to be instantiated once for each
Modbus module that should act like a slave with the address specified at the
SlaveAddress input.

Communication with the ctrlX I/O modules XI521001/XI522001 on an XB-
EC-12 or ctrlX CORE a Modbus slave
Before enabling the function block, create an array for the holding register
("arHoldingRegisters"), Input register ("arInputRegisters"), Coils ("arCoils")
and input bits ("arInputBits").
In addition, the structures for internal process data ("stInProcData") and
external process data ("stOutProcData") are created, and the variables and
process data of the module are assigned directly to the I/O variable mapping
of the ctrlX I/O modules XI521001/XI522001 using the % address.
"stInProcData" and "stOutProcData" are assigned directly to the I/O variable
mapping by the module using the % address.
Assign the address to the SlaveAddress input and enable the function block.
The function block sets the variable "InOperation" to TRUE and thus indicates
that the slave is ready.

Variable declaration

PROGRAM Example_IH_XIMBRTUSlave
VAR
  // Slave FB
  fbIH_XIMBRTUSlave           : IH_XIMBRTUSlave;             // XIMBRTU Slave FB Instance
  bEnable                     : BOOL;                        // TRUE: Function Block is enabled
  bInOperation                : BOOL;                        // TRUE: FB is processing its task
  bError                      : BOOL;                        // TRUE: Indicates as error
  ErrorID                     : ERROR_CODE;                  // Class of error
  ErrorIdent                  : ERROR_STRUCT;                // Detailed information about error
  bySlaveAddress              : BYTE;                        // Slave address
  wOffset                     : WORD;                        // Address offset
  arHoldingReg_Slave          : ARRAY[0..65535] OF WORD;     // Array to store HoldingRegisters
  arInputReg_Slave            : ARRAY[0..65535] OF WORD;     // Array to store InputRegisters
  arCoils_Slave               : ARRAY[0..8191] OF BOOL;      // Array to store Coils data
  arInputBits_Slave           : ARRAY[0..8191] OF BOOL;      // Array to store InputBits
  bBusy                       : BOOL;                        // True when the block is busy/ used
  uiNoOfTransactions          : UINT;                        // Number of Transactions happened

  // Process Data mapping; Change Mapping Address(Ex:- %IB227) as per your module mapping address.
  stInProcData AT %IB227      : CXA_ModbusRTU.CXA_ctrlXIO.IH_XI_INPROC_DATA;      // Input process data
structure. Link this variable to module process data
  stOutProcData AT %QB74      : CXA_ModbusRTU.CXA_ctrlXIO.IH_XI_OUTPROC_DATA;     // Output process data
structure. Link this variable to module process data
END_VAR

Implementation

// Slave FB Instance
fbIH_XIMBRTUSlave(
Enable:= bEnable,
InOperation=> bInOperation,
Error=> bError,
ErrorID=> ErrorID,
ErrorIdent=> ErrorIdent,
SlaveAddress:= bySlaveAddress,
Offset:= wOffset,
InProcData:= stInProcData,
OutProcData:= stOutProcData,
HoldingRegistersAdr:= ADR(arHoldingReg_Slave),
SizeOfHoldingRegisters:= SIZEOF(arHoldingReg_Slave),
InputRegistersAdr:= ADR(arInputReg_Slave),
SizeOfInputRegisters:= SIZEOF(arInputReg_Slave),
CoilsAdr:= ADR(arCoils_Slave),
SizeOfCoils:= SIZEOF(arCoils_Slave),
InputBitsAdr:= ADR(arInputBits_Slave),
SizeOfInputBits:= SIZEOF(arInputBits_Slave),
Busy=> bBusy,
NoOfTransactions=> uiNoOfTransactions);

Process data mapping
"stInProcData" and "stOutProcData" are assigned directly to the I/O variable
mapping by the module using the % address.

## 16.19 IH_MBWriteFileRecord

      Function code
      FC 21

      Brief description
      The function block IH_MBWriteFileRecord writes a file protocol in the RTU
      mode.
      The function block has to be called using the Modbus master function block
      ⮫ IH_S20MBRTUMaster.

      Interface description

Table 297: Interface variables of the IH_MBWriteFileRecord function block
I/O type       Name                  Data type         Description
VAR_INPUT      Enable                BOOL              Function block active if TRUE
               SendRequest           BOOL              A request is sent at a rising edge
                                                       Polling enabled
                                                       SendRequest does not have to be triggered
               EnablePoll            BOOL              at each interval
                                                       The function block sends requests automat‐
                                                       ically
               SlaveAddress          BYTE              Slave address
                                     ⮫ IH_INLN_MB_SU
               SubRequest                             Subrequest
                                     BREQUESTS
                                     POINTER       TO Address of the protocol data array
               ValueAdr              ARRAY[0..119] OF
                                     WORD             Use the ADR () operator
                                                      Size of the ValueAdr array
               SizeOfValue           UINT
                                                      Use the SIZEOF () operator
                                                      Polling interval
               PollInterval          TIME
                                                      Request is sent continuously at intervals
               TimeOut               TIME             Timeout interval for response from slaves
VAR_OUTPUT                                            Computation completed and starts again in
               Done                  BOOL
                                                      the next cycle
               Active                BOOL             Function block is active
               Error                 BOOL             Indicates an error
               ErrorID               ⮫ ERROR_CODE      Error class
               ErrorIdent            ⮫ ERROR_STRUCT Detailed error information

I/O type           Name                Data type        Description
Busy                BOOL             True if the function block communicates
                                     with the master
OutputData          ⮫ IH_INLN_MB_RE It contains the data length of "Request" and
                    CORD             subrequested data
                                     Please refer to: Structures and enumera‐
                                     tions
VAR_IN_OUT         MBData              ⮫ IH_INLN_MB_DAT Structure handles data between the master
                    A                and other Modbus function blocks of the
                                     function codes

    Min./max. and default values
The following table lists the min./max. and default values as well as the
application behavior of the function block inputs.
Table 298: Min./max. and default values as well as the response of the function block inputs of
IH_MBWriteFileRecord during application
Name               Data type       Min. value      Max. value       Default value   Effective
Enable             BOOL            FALSE           TRUE             FALSE           Continuous
                                                                                    Continuously      at
SendRequest        BOOL            FALSE           TRUE             FALSE
                                                                                    Enable
                                                                                    Continuously      at
EnablePoll         BOOL            FALSE           TRUE             FALSE
                                                                                    Enable
                                                                                    Rising    edge    at
SlaveAddress       BYTE            0               247              0
                                                                                    Enable
                                                                                    Continuously      at
SizeOfValue        UINT            1               --------------   -----------
                                                                                    Enable
                                                                                    Continuously      at
PollInterval       TIME            T#1s            -------------    T#1s
                                                                                    Enable
                                                                                    Rising    edge    at
TimeOut            TIME            T#1s            --------------   T#1s
                                                                                    Enable

Functional description
The function block IH_MBWriteFileRecord (FC 21) is used to write file pro‐
tocols. The requested data lengths in the structure ⮫ IH_INLN_MB_SUBRE‐
QUESTS are specified in bytes. Protocol lengths are specified in words. The
function block has to be called using the Modbus master function block.
"MBData" has to be linked to the master function block in the program. It is
used for communication purposes and data exchange.
The function writes a single reference group. The groups can be separate
(not continuous), but the references in the individual groups have to be con‐
tinuous.
Each group is defined in a separate field for "subrequests" containing 7 bytes:

● Reference type: 1 byte (to be specified as 6)
    NOTE: Considered as standard in this function block.
● File number: (Word) has to be (0x0000 to 0xFFFF)
● Initial protocol number in the file. (Word) has to be (0x0000 to 0x270F)
● Length of the protocol to be read (word) has to be (1 to 120)
The number of the registers to be read and all other fields in the expected
response may not exceed the permitted length of the MODBUS PDU: 253
bytes.
The function block is enabled after the first PLC cycle by setting the "Enable"
input to TRUE. The "Active" output is set to TRUE during operation. The bit
"Done" is set to TRUE upon completion. If an error results during the oper‐
ation, the "Error" bit is set to TRUE. "ErrorID" and "ErrorIdent" show error
information. The error can be acknowledged via a rising edge at the "Enable"
input.
Example of a function block
The function block IH_MBWriteFileRecord has to be instantiated together with
the function block IH_MBRTUMaster to communicate with the Modbus slave.
The input/output variable "stMBData" exchanges data between the function
blocks IH_MBRTUMaster and IH_MBWriteFileRecord. Thus, this variable has to
be assigned to "MBData" to both function blocks.
In the example, the function block IH_MBWriteFileRecord is used to write the
file protocol to the slave device.

Writing file protocol with SendRequest condition
The function block IH_MBWriteFileRecord is used to write a protocol with the
protocol length 10 from protocol no. 4 in file no. 1 of slave address 2; with
the "bSendRequest" as BOOL variable to trigger writing.

Variable declaration

VAR
fbIH_MBWriteFileRecord: IH_MBWriteFileRecord;
bEnable: BOOL;
bSendRequest: BOOL;
stSubRequest: IH_INLN_MB_SUBREQUESTS;
arWriteRecordData: ARRAY [0..119] OF WORD;
stMBData: IH_INLN_MB_DATA;
bDone: BOOL;
bActive: BOOL;
bError: BOOL;
enErrorID: ERROR_CODE;
stErrorIdent: ERROR_STRUCT;
bBusy: BOOL;
stOutputData: IH_INLN_MB_RECORD;
END_VAR

Implementation

stSubRequest.FileNumber := WORD#1;
stSubRequest.RecordNumber := WORD#4;
stSubRequest.RecordLength := WORD#10;

fbIH_MBWriteFileRecord(
Enable:= bEnable,
SendRequest:= bSendRequest,
EnablePoll:= FALSE,
SlaveAddress:= BYTE#2,
SubRequest:= stSubRequest,
ValueAdr:= ADR(arWriteRecordData),
SizeOfValue:= SIZEOF(arWriteRecordData),
PollInterval:= T#2S,
TimeOut:= T#2S,
MBData:= stMBData,
Done=> bDone,
Active=> bActive,
Error=> bError,
ErrorID=> enErrorID,
ErrorIdent=> stErrorIdent,
Busy=> bBusy,
OutputData=> stOutputData);

Writing file protocol with PollInterval condition
The function block IH_MBWriteFileRecord is used to write a protocol with the
protocol length 5 from protocol no. 1 in file no. 2 of slave address 5; with the
"PollInterval" (3 seconds) to trigger writing.

Variable declaration

VAR
  fbIH_MBWriteFileRecord2: IH_MBWriteFileRecord;
  bEnable2: BOOL;
  stSubRequest2: IH_INLN_MB_SUBREQUESTS;
 stMBData: IH_INLN_MB_DATA;
  arWriteRecordData2: ARRAY [0..4] OF WORD;
  bDone2: BOOL;
  bActive2: BOOL;
  bError2: BOOL;
  enErrorID2: ERROR_CODE;
  stErrorIdent2: ERROR_STRUCT;
  bBusy2: BOOL;
  stOutputData2: IH_INLN_MB_RECORD;
END_VAR

Implementation

stSubRequest2.FileNumber := WORD#2;
stSubRequest2.RecordNumber := WORD#1;
stSubRequest2.RecordLength := WORD#5;

fbIH_MBWriteFileRecord2(
  Enable:= bEnable2,
  SendRequest:= FALSE,
  EnablePoll:= TRUE,
  SlaveAddress:= BYTE#5,
  SubRequest:= stSubRequest2,
  ValueAdr:= ADR(arWriteRecordData2),
  SizeOfValue:= SIZEOF(arWriteRecordData2),
  PollInterval:= T#3S,
  TimeOut:= T#2S,
  MBData:= stMBData,
  Done=> bDone2,
  Active=> bActive2,
  Error=> bError2,
  ErrorID=> enErrorID2,
  ErrorIdent=> stErrorIdent2,
  Busy=> bBusy2,
  OutputData=> stOutputData2);

## 16.20 IH_MBWriteMultipleCoils

Function code
FC 15

Brief description
The function block IH_MBWriteMultipleCoils is used to force multiple coils,
i.e. output bits ON or OFF of the slave module.
The function block has to be called using the Modbus master function block
⮫ IH_S20MBRTUMaster.

       Interface description

Table 299: Interface variables of the IH_MBWriteMultipleCoils function block
I/O type       Name                 Data type         Description
VAR_INPUT      Enable               BOOL              Function block active if TRUE
               SendRequest          BOOL              A request is sent at a rising edge
                                                      Polling enabled
                                                      SendRequest does not have to be triggered
               EnablePoll           BOOL              at each interval.
                                                      The function block sends requests automat‐
                                                      ically
               SlaveAddress         BYTE              Slave address
               StartAddress         WORD              Start address of the output bits.
               NoOfCoils            UINT              Number of coils (separate outputs)
                                    POINTER        TO Address of the array to save the written
               ValueAdr             ARRAY[0..1967]    value of the output bits
                                    OF BOOL           Use the ADR () operator
                                                      Size of the WriteDataVal array.
               SizeOfValue          UINT
                                                      Use the SIZEOF () operator
                                                      Polling interval. Request is sent continu‐
               PollInterval         TIME
                                                      ously at intervals
               TimeOut              TIME              Timeout interval for response from slaves
VAR_OUTPUT                                            Computation completed and starts again in
               Done                 BOOL
                                                      the next cycle
               Active               BOOL              Function block is active
               Error                BOOL              Indicates an error
               ErrorID              ⮫ ERROR_CODE      Error class
               ErrorIdent           ⮫ ERROR_STRUCT Detailed error information
                                                   True if the function block communicates
               Busy                 BOOL
                                                   with the master
VAR_IN_OUT                          ⮫ IH_INLN_MB_DAT Structure handles data between the master
               MBData
                                    A                and other Modbus function blocks

Min./max. and default values
The following table lists the min./max. and default values as well as the
application behavior of the function block inputs.
Table 300: Min./max. and default values as well as the response of the function block inputs of
IH_MBWriteMultipleCoils during application
Name               Data type       Min. value    Max. value       Default value   Effective
Enable             BOOL            FALSE         TRUE             FALSE           Continuous
                                                                                  Continuously      at
SendRequest        BOOL            FALSE         TRUE             FALSE
                                                                                  Enable
                                                                                  Continuously      at
EnablePoll         BOOL            FALSE         TRUE             FALSE
                                                                                  Enable
                                                                                  Rising    edge    at
SlaveAddress       BYTE            0             247              0
                                                                                  Enable
                                                                                  Rising    edge    at
StartAddress       WORD            0             FFFF             0
                                                                                  Enable
                                                                                  Rising    edge    at
NoOfCoils          UINT            1             1968             1
                                                                                  Enable
                                                                                  Rising    edge    at
SizeOfValue        UINT            1             1968             -------------
                                                                                  Enable
                                                                                  Continuously      at
PollInterval       TIME            T#1s          -------------    T#1s
                                                                                  Enable
                                                                                  Rising    edge    at
TimeOut            TIME            T#1s          --------------   T#1s
                                                                                  Enable

Functional description
The function block IH_MBWriteMultipleCoils (FC 15) is used to force multiple
coils, i.e. output bits ON or OFF of the slave module. The function block has
to be called using the Modbus master function block. "MBData" has to be
linked to the master function block in the program. It is used for communica‐
tion purposes and data exchange.
The function block is enabled after the first PLC cycle by setting the "Enable"
input to TRUE. The "Active" output is set to TRUE during operation. The bit
"Done" is set to TRUE upon completion. If an error results during the oper‐
ation, the "Error" bit is set to TRUE. "ErrorID" and "ErrorIdent" show error
information. The error can be acknowledged via a rising edge at the "Enable"
input.
Example of a function block
The function block IH_MBWriteMultipleCoils has to be instantiated together
with the IH_MBRTUMaster to communicate with the Modbus slave. The input/
output variable "stMBData" exchanges data between the function blocks
IH_MBRTUMaster and IH_MBWriteMultipleCoils. Thus, this variable has to be
assigned to "MBData" to both function blocks.
In the example, the function block IH_MBWriteMultipleCoils is used to write
coils to the slave device.

Writing coils with SendRequest condition
The function block IH_MBWriteMultipleCoils is used to write 7 coils of the
start address 0x1000 to slave address 2 with "bSendRequest" as BOOL vari‐
able to trigger coil writing.

Variable declaration

VAR
  fbIH_MBWriteMultipleCoils: IH_MBWriteMultipleCoils;
  bEnable: BOOL;
  bSendRequest: BOOL;
  arWriteMultipleCoils: ARRAY [0..6] OF BOOL;
  stMBData: IH_INLN_MB_DATA;
  bDone: BOOL;
  bActive: BOOL;
  bError: BOOL;
  enErrorID: ERROR_CODE;
  stErrorIdent: ERROR_STRUCT;
  bBusy: BOOL;

END_VAR

Implementation

fbIH_MBWriteMultipleCoils(
  Enable:= bEnable,
  SendRequest:= bSendRequest,
  EnablePoll:= FALSE,
  SlaveAddress:= BYTE#2,
  StartAddress:= WORD#1000,
  NoOfCoils:= UINT#7,
  ValueAdr:= ADR(arWriteMultipleCoils),
  SizeOfValue:= SIZEOF(arWriteMultipleCoils),
  PollInterval:= T#2S,
  TimeOut:= T#2S,
  MBData:= stMBData,
  Done=> bDone,
  Active=> bActive,
  Error=> bError,
  ErrorID=> enErrorID,
  ErrorIdent=> stErrorIdent,
  Busy=> bBusy);

Writing coils with PollIntervall condition
The function block IH_MBWriteMultipleCoils is used to write 4 coils of the
start address 0x500 to slave address 5 with "PollInterval" (3 seconds) to
trigger coil writing.

Variable declaration

VAR
  fbIH_MBWriteMultipleCoils2: IH_MBWriteMultipleCoils;
  bEnable2: BOOL;
  arWriteMultipleCoils2: ARRAY [0..3] OF BOOL;
  stMBData: IH_INLN_MB_DATA;
  bDone2: BOOL;
  bActive2: BOOL;
  bError2: BOOL;
  stErrorIdent2: ERROR_STRUCT;
  enErrorID2: ERROR_CODE;
  bBusy2: BOOL;
END_VAR

Implementation

fbIH_MBWriteMultipleCoils2(
  Enable:= bEnable2,
  SendRequest:= FALSE,
  EnablePoll:= TRUE,
  SlaveAddress:= BYTE#5,
  StartAddress:= WORD#500,
  NoOfCoils:= UINT#4,
  ValueAdr:= ADR(arWriteMultipleCoils2),
  SizeOfValue:= SIZEOF(arWriteMultipleCoils2),
  PollInterval:= T#3S,
  TimeOut:= T#2S,
  MBData:= stMBData,
  Done=> bDone2,
  Active=> bActive2,
  Error=> bError2,
  ErrorID=> enErrorID2,
  ErrorIdent=> stErrorIdent2,
  Busy=> bBusy2);

## 16.21 IH_MBWriteMultipleRegisters

Function code
FC 16

Brief description
The function block IH_MBWriteMultipleRegisters is used to write a Holding
register of the Modbus slave module.
The function block has to be called using the Modbus master function block
⮫ IH_S20MBRTUMaster.

       Interface description

Table 301: Interface variables of the IH_MBReadWriteMultipleRegisters function block
I/O type       Name                 Data type        Description
VAR_INPUT      Enable               BOOL             Function block active if TRUE
               SendRequest          BOOL             A request is sent at a rising edge
                                                     Polling enabled
                                                     SendRequest does not have to be triggered
               EnablePoll           BOOL             at each interval
                                                     The function block sends requests automat‐
                                                     ically
               SlaveAddress         BYTE             Slave address
               StartAddress         WORD             Start address of the Holding register
               NoOfRegisters        UINT             Number of registers
                                    POINTER       TO The  address of the array contains the write
               ValueAdr             ARRAY[0..122] OF value  of the registers
                                    WORD             Use the ADR () operator
                                                     Size of the Value array
               SizeOfValue          UINT
                                                     Use the SIZEOF () operator
                                                     Polling interval
               PollInterval         TIME
                                                     Request is sent continuously at intervals
               TimeOut              TIME             Timeout interval for response from slaves
VAR_OUTPUT                                           Computation completed and starts again in
               Done                 BOOL
                                                     the next cycle
               Active               BOOL             Function block is active
               Error                BOOL             Indicates an error
               ErrorID              ⮫ ERROR_CODE       Error class
               ErrorIdent           ⮫ ERROR_STRUCT Detailed error information
                                                   True if the function block communicates
               Busy                 BOOL
                                                   with the master
VAR_IN_OUT                          ⮫ IH_INLN_MB_DAT Structure handles data between the master
               MBData
                                    A                and other Modbus function blocks

Min./max. and default values
The following table lists the min./max. and default values as well as the
application behavior of the function block inputs.
Table 302: Min./max. and default values as well as the response of the function block inputs of
IH_MBWriteMultipleRegisters during application
Name               Data type       Min. value    Max. value       Default value   Effective
Enable             BOOL            FALSE         TRUE             FALSE           Continuous
                                                                                  Continuously      at
SendRequest        BOOL            FALSE         TRUE             FALSE
                                                                                  Enable
                                                                                  Continuously      at
EnablePoll         BOOL            FALSE         TRUE             FALSE
                                                                                  Enable
                                                                                  Rising    edge    at
SlaveAddress       BYTE            0             247              0
                                                                                  Enable
                                                                                  Rising    edge    at
StartAddress       WORD            0             65535            0
                                                                                  Enable
                                                                                  Rising    edge    at
NoOfRegisters UINT                 1             123              1
                                                                                  Enable
                                                                                  Rising    edge    at
SizeOfValue        UINT            1             ------------     -----------
                                                                                  Enable
                                                                                  Continuously      at
PollInterval       TIME            T#1s          -------------    T#1s
                                                                                  Enable
                                                                                  Rising    edge    at
TimeOut            TIME            T#1s          --------------   T#1s
                                                                                  Enable

Functional description
The function block IH_MBWriteMultipleRegisters (FC 16) writes the Holding
register of a slave module specified in SlaveAddress. The function block has to
be called using the Modbus master function block. "MBData" has to be linked
to the master function block to communicate with the master and to exchange
data.
The function block is enabled after the first PLC cycle by setting the "Enable"
input to TRUE. The "Active" output is set to TRUE during operation. The bit
"Done" is set to TRUE upon completion. If an error results during the oper‐
ation, the "Error" bit is set to TRUE. "ErrorID" and "ErrorIdent" show error
information. The error can be acknowledged via a rising edge at the "Enable"
input.
Example of a function block
The function block IH_MBWriteMultipleRegisters has to be instantiated
together with the IH_MBRTUMaster to communicate with the Modbus slave.
Use a common variable for "MBData" of the IH_MBWriteMultipleRegisters and
IH_MBRTUMaster function blocks to exchange data with the Modbus slave.

Example 1
In this example, the function block IH_MBWriteMultipleRegisters writes the
Holding register of slave address 1 with StartAddress 2000 and NoOfRegisters
5.
The function blocks IH_MBRTUMaster and IH_MBWriteMultipleRegisters are
enabled with a rising edge at the "bSendRequest" input. The function block
writes data to slave address 1 and after each successful write operation, the
bit "Done" is set to TRUE for one PLC cycle.

Variable declaration

VAR
  fbIH_MBWriteMultipleRegisters: IH_MBWriteMultipleRegisters;
  bEnable: BOOL;
  bSendRequest: BOOL;
  arWriteRegisters: ARRAY [0..4] OF WORD;
  stMBData: IH_INLN_MB_DATA;
  bDone: BOOL;
  bActive: BOOL;
  bError: BOOL;
  enErrorID: ERROR_CODE;
  stErrorIdent: ERROR_STRUCT;
  bBusy: BOOL;

END_VAR

Implementation

fbIH_MBWriteMultipleRegisters(
  Enable:= bEnable,
  SendRequest:= bSendRequest,
  EnablePoll:= FALSE,
  SlaveAddress:= BYTE#1,
  StartAddress:= WORD#2000,
  NoOfRegisters:= UINT#5,
  ValueAdr:= ADR(arWriteRegisters),
  SizeOfValue:= SIZEOF(arWriteRegisters),
  PollInterval:= T#1S,
  TimeOut:= T#1S,
  MBData:= stMBData,
  Done=> bDone,
  Active=> bActive,
  Error=> bError,
  ErrorID=> enErrorID,
  ErrorIdent=> stErrorIdent,
  Busy=> bBusy);

Request
Data to be written to the slave module has to be entered into the array "arWri‐
teRegisters".

Example 2
In this example, the function block IH_MBWriteMultipleRegisters writes the
Holding register of slave address 2 with StartAddress 3000 and NoOfRegisters
10 at a polling interval of 1 second. The function blocks IH_MBRTUMaster and
IH_MBWriteMultipleRegisters are enabled and EnablePoll with a "PollInterval"
of 1 second is set to TRUE. The function block then writes data from slave
address 2 at regular intervals of 1 second. After each successful write opera‐
tion, the bit "Done" is set to TRUE for one PLC cycle.

Variable declaration

VAR
fbIH_MBWriteMultipleRegisters2: IH_MBWriteMultipleRegisters;
bEnable2: BOOL;
bSendRequest2: BOOL;
bEnablePoll: BOOL;
arWriteRegisters2: ARRAY [0..9] OF WORD;
stMBData: IH_INLN_MB_DATA;
bDone2: BOOL;
bActive2: BOOL;
bError2: BOOL;
enErrorID2: ERROR_CODE;
stErrorIdent2: ERROR_STRUCT;
bBusy2: BOOL;
END_VAR

Implementation

fbIH_MBWriteMultipleRegisters2(
Enable:= bEnable2,
SendRequest:= bSendRequest2,
EnablePoll:= bEnablePoll,
SlaveAddress:= BYTE#2,
StartAddress:= WORD#3000,
NoOfRegisters:= UINT#10,
ValueAdr:= ADR(arWriteRegisters2),
SizeOfValue:= SIZEOF(arWriteRegisters2),
PollInterval:= T#1S,
TimeOut:= T#1S,
MBData:= stMBData,
Done=> bDone2,
Active=> bActive2,
Error=> bError2,
ErrorID=> enErrorID2,
ErrorIdent=> stErrorIdent2,
Busy=> bBusy2);

Response:
Data to be written to the slave module has to be entered into the array "arWri‐
teRegisters2".

## 16.22 IH_MBWriteSingleCoil

       Function code
       FC 5

       Brief description
       The function block IH_MBWriteSingleCoil writes the ON or OFF value to a
       single coil, i.e. a single output bit of the slave module.
       The function block has to be called using the Modbus master function block
       ⮫ IH_S20MBRTUMaster.

       Interface description

Table 303: Interface variables of the IH_MBWriteSingleCoil function block
I/O type       Name                   Data type         Description
VAR_INPUT      Enable                 BOOL              Function block active if TRUE
               SendRequest            BOOL              A request is sent at a rising edge
                                                        Polling enabled
                                                        SendRequest does not have to be triggered
               EnablePoll             BOOL              at each interval
                                                        The function block sends requests automat‐
                                                        ically
               SlaveAddress           BYTE              Slave address
               StartAddress           WORD              Start address of the input bits
               Value                  BOOL              Output bit value: TRUE or FALSE
                                                        Polling interval
               PollInterval           TIME
                                                        Request is sent continuously at intervals
               TimeOut                TIME              Timeout interval for response from slaves
VAR_OUTPUT                                              Computation completed and starts again in
               Done                   BOOL
                                                        the next cycle
               Active                 BOOL              Function block is active
               Error                  BOOL              Indicates an error
               ErrorID                ⮫ ERROR_CODE      Error class
               ErrorIdent             ⮫ ERROR_STRUCT Detailed error information
                                                     True if the function block communicates
               Busy                   BOOL
                                                     with the master
VAR_IN_OUT                            ⮫ IH_INLN_MB_DAT Structure handles data between the master
               MBData
                                      A                and other Modbus function blocks

Min./max. and default values
The following table lists the min./max. and default values as well as the
application behavior of the function block inputs.
Table 304: Min./max. and default values as well as the response of the function block inputs of
IH_MBWriteSingleCoil during application
Name               Data type       Min.value     Max. value       Default value   Effective
Enable             BOOL            FALSE         TRUE             FALSE           Continuous
                                                                                  Continuously      at
SendRequest        BOOL            FALSE         TRUE             FALSE
                                                                                  Enable
                                                                                  Continuously      at
EnablePoll         BOOL            FALSE         TRUE             FALSE
                                                                                  Enable
                                                                                  Rising    edge    at
SlaveAddress       BYTE            0             247              0
                                                                                  Enable
                                                                                  Rising    edge    at
StartAddress       WORD            0             FFFF             0
                                                                                  Enable
                                                                                  Rising    edge    at
Value              BOOL            FALSE         TRUE             FALSE
                                                                                  Enable
                                                                                  Continuously      at
PollInterval       TIME            T#1s          -------------    T#1s
                                                                                  Enable
                                                                                  Rising    edge    at
TimeOut            TIME            T#1s          --------------   T#1s
                                                                                  Enable

Functional description
The function block IH_MBWriteSingleCoil (FC 5) writes the ON or OFF value
to a single coil, i.e. a single output bit of the slave module. The function
block has to be called using the Modbus master function block. "MBData"
has to be linked to the master function block in the program. It is used for
communication purposes and data exchange.
The function block is enabled after the first PLC cycle by setting the "Enable"
input to TRUE. The "Active" output is set to TRUE during operation. The bit
"Done" is set to TRUE upon completion. If an error results during the oper‐
ation, the "Error" bit is set to TRUE. "ErrorID" and "ErrorIdent" show error
information. The error can be acknowledged via a rising edge at the "Enable"
input.
Example of a function block
The function block IH_MBWriteSingleCoil has to be instantiated together with
the function block IH_MBRTUMaster to communicate with the Modbus slave.
The input/output variable "stMBData" exchanges data between the function
blocks IH_MBRTUMaster and IH_MBWriteSingleCoil. Thus, this variable has to
be assigned to "MBData" to both function blocks.
In the example, the function block IH_MBWriteSingleCoil is used to write a
single coil to the slave device.

Writing single coil with SendRequest condition
The function block IH_MBWriteSingleCoil is used to write a single coil of the
start address 0x1000 to slave address 2 with "bSendRequest" as BOOL vari‐
able to trigger coil writing.

Variable declaration

VAR
  fbIH_MBWriteSingleCoil: IH_MBWriteSingleCoil;
  bEnable: BOOL;
  bSendRequest: BOOL;
  stMBData: IH_INLN_MB_DATA;
  bDone: BOOL;
  bActive: BOOL;
  bError: BOOL;
  enErrorID: ERROR_CODE;
  stErrorIdent: ERROR_STRUCT;
  bBusy: BOOL;
END_VAR

Implementation

fbIH_MBWriteSingleCoil(
  Enable:= bEnable,
  SendRequest:= bSendRequest,
  EnablePoll:= FALSE,
  SlaveAddress:= BYTE#2,
  StartAddress:= WORD#1000,
  Value:= TRUE,
  PollInterval:= T#2S,
  TimeOut:= T#2S,
  MBData:= stMBData,
  Done=> bDone,
  Active=> bActive,
  Error=> bError,
  ErrorID=> enErrorID,
  ErrorIdent=> stErrorIdent,
  Busy=> bBusy);

## 16.23 IH_MBWriteSingleRegister

Function code
FC 6

Brief description
The function block IH_MBWriteSingleRegister is used to write a single Holding
register of the Modbus to the slave module.
The function block has to be called using the Modbus master function block
⮫ IH_S20MBRTUMaster.

       Interface description

Table 305: Interface variables of the IH_MBWriteSingleRegister function block
I/O type           Name                 Data type         Description
VAR_INPUT          Enable               BOOL              Function block active if TRUE
                   SendRequest          BOOL              A request is sent at a rising edge
                                                          Polling enabled
                                                          SendRequest does not have to be triggered
                   EnablePoll           BOOL              at each interval
                                                          The function block sends requests automat‐
                                                          ically
                   SlaveAddress         BYTE              Slave address
                   StartAddress         WORD              Start address of the Holding register
                   WriteDataVal         WORD              Writing register value.
                                                          Polling interval
                   PollInterval         TIME
                                                          Request is sent continuously at intervals
                   TimeOut              TIME              Timeout interval for response from slaves
VAR_OUTPUT                                                Computation completed and starts again in
                   Done                 BOOL
                                                          the next cycle
                   Active               BOOL              Function block is active
                   Error                BOOL              Indicates an error
                   ErrorID              ⮫ ERROR_CODE      Error class
                   ErrorIdent           ⮫ ERROR_STRUCT Detailed error information
                                        BOOL           True if the function block communicates
                   Busy
                                                       with the master
VAR_IN_OUT         MBData               ⮫ IH_INLN_MB_DAT Structure handles data between the master
                                        A                and other Modbus function blocks

Min./max. and default values
The following table lists the min./max. and default values as well as the
application behavior of the function block inputs.
Table 306: Min./max. and default values as well as the response of the function block inputs of
IH_MBWriteSingleRegister during application
Name            Data type       Min. value      Max. value       Default value   Effective
Enable          BOOL            FALSE           TRUE             FALSE           Continuous
                                                                                 Continuously     at
SendRequest     BOOL            FALSE           TRUE             FALSE
                                                                                 Enable
                                                                                 Continuously     at
EnablePoll      BOOL            FALSE           TRUE             FALSE
                                                                                 Enable

                                                            Rising    edge   at
SlaveAddress    BYTE            0               247              0
                                                            Enable
                                                            Rising    edge   at
StartAddress    WORD            0               65535            0
                                                            Enable
                                                            Continuously     at
WriteDataVal    WORD            0               65535            0
                                                            Enable
                                                            Continuously     at
PollInterval    TIME            T#1s            -------------    T#1s
                                                            Enable
                                                            Rising    edge   at
TimeOut         TIME            T#1s            --------------   T#1s
                                                            Enable

Functional description
The function block IH_MBWriteSingleRegister (FC 6) writes a single Holding
register of a Modbus slave module specified in SlaveAddress. The function
block has to be called using the Modbus master function block. "MBData" has
to be linked to the master function block to communicate with the master and
to exchange data.
The function block is enabled after the first PLC cycle by setting the "Enable"
input to TRUE. The "Active" output is set to TRUE during operation. The bit
"Done" is set to TRUE upon completion. If an error results during the oper‐
ation, the "Error" bit is set to TRUE. "ErrorID" and "ErrorIdent" show error
information. The error can be acknowledged via a rising edge at the "Enable"
input.
Example of a function block
The function block IH_MBWriteSingleRegister has to be instantiated together
with the IH_MBRTUMaster to communicate with the Modbus slave. Use
a common variable for "MBData" of the IH_MBWriteSingleRegister and
IH_MBRTUMaster function blocks to exchange data with the Modbus slave.
In this example, the function block IH_MBWriteSingleRegister writes the
Holding register of slave address 1 with StartAddress 1000 and WriteDataVal
200.
The function blocks IH_MBRTUMaster and IH_ MBWriteSingleRegister are ena‐
bled with a rising edge at the "bSendRequest" input. The function block
writes data to slave address 1.
If the "bEnablePoll" variable is set to TRUE and "PollInterval" to more than 1
second, data is written to the slave at regular intervals.
After each successful write operation, the bit "Done" is set to TRUE for one
PLC cycle.

Variable declaration

VAR
fbIH_MBWriteSingleRegister: IH_MBWriteSingleRegister;
bEnable: BOOL;
bSendRequest: BOOL;
bEnablePoll: BOOL;
stMBData: IH_INLN_MB_DATA;
bDone: BOOL;
bActive: BOOL;
bError: BOOL;
enErrorID: ERROR_CODE;
stErrorIdent: ERROR_STRUCT;
bBusy: BOOL;
END_VAR

Implementation

fbIH_MBWriteSingleRegister(
Enable:= bEnable,
SendRequest:= bSendRequest,
EnablePoll:= bEnablePoll,
SlaveAddress:= BYTE#1,
StartAddress:= WORD#1000,
WriteDataVal:= WORD#200,
PollInterval:= T#1S,
TimeOut:= T#1S,
MBData:= stMBData,
Done=> bDone,
Active=> bActive,
Error=> bError,
ErrorID=> enErrorID,
ErrorIdent=> stErrorIdent,
Busy=> bBusy);

## 16.24 Data types

### 16.24.1 IH_INLN_MB_DATA

The structure is used internally to exchange commands and data between the
master function blocks and other function blocks of the function codes.

Table 307: Library assignment of the IH_INLN_MB_DATA
Library                                       Folder
CXA_ModbusRTU                                 Type

Table 308: IH_INLN_MB_DATA structure
                                                              Min.    Max. Default
Name            Data type              Description                                         Application
                                                              value   value value
                               Master        function
Ready           BOOL           block is ready for FALSE               TRUE FALSE           Continuous
                               communication
                               Indicates that the
SendRequest BOOL               master wants to sent FALSE             TRUE FALSE           Continuous
                               a request
                               Address     of     the
SlaveAddress BYTE                                         0           247          0       Continuous
                               respective slave

          Function         code
FunctionCode INT               requested by the -------               -------   -------    Continuous
          master
          Start address to exe‐
StartAddress WORD                                      --------       -------   --------   Continuous
          cute the code
ARRAY[0..124]  OF Data bytes of the
ArrayData                                              --------       -------   --------   Continuous
WORD              telegram
TimeOut      TIME              Timeout interval        T#1s           -------   T#1s       Continuous
RespErr      BYTE              Error information       --------       -------   --------   Continuous
          Master        function
Busy         BOOL                                     FALSE           TRUE FALSE           Continuous
          block is busy
NewDataRecv BOOL               New data is received FALSE             TRUE FALSE           Continuous
DataCount    UINT              Data length             --------       ------- --------     Continuous
          Process (request and
Done         BOOL              response) is com‐ FALSE                TRUE FALSE           Continuous
          pleted
          Internal Reset vari‐
Reset        BOOL              able to reset the FALSE                TRUE FALSE           Continuous
          master
ARRAY[0..32]   OF
Token                          Token                   --------       -------   --------   Continuous
IH_INLN_MB_TOKEN

### 16.24.2 IH_INLN_MB_DEV_IDCODE

The structure IH_INLN_MB_DEV_IDCODE specifies the access levels of the
object categories.
The function block ⮫ IH_MBReadDeviceIdentification supports the following
"Read Device ID Code" access types:

Name                         Value   Description
IH_INLN_MB_READ01              1     Requests the basic device identification (access via stream)
IH_INLN_MB_READ02              2     Requests the regular device identification (access via stream)
IH_INLN_MB_READ03              3     Requests the extended device identification (access via stream)
IH_INLN_MB_READ04              4     Requests a specific identification object (customized access)

For a customized object ID access "DeviceIdCode" as IH_INLN_MB_READ04,
specify the object ID at the "ObjectId" input. For all other device ID codes, the
"ObjectId" has to be 0.

### 16.24.3 IH_INLN_MB_FIFODATA

The structure returns the final response output of the ⮫ IH_MBReadFIFOQue
function block.

Table 309: Library assignment of the IH_INLN_MB_FIFODATA
Library                                           Folder
CXA_ModbusRTU                                     Type

Name                    Data type                          Description
                                                           Number of bytes (total number of received
ByteCount               UINT
                                                           bytes)
FIFOCount               UINT                               Number of FIFO registers
FIFORegValues           ARRAY [1.0,31] OF WORD             FIFO register values

### 16.24.4 IH_S20_MB_CONFIG

         The structure is an extension of IH_S20_RS_CONFIG and used to configure
         the communication settings of the Modbus master/slave function block
         (⮫ RIL_InlineIOModules.library, FB IL_RsCom, STRUCT IH_S20_RS_CONFIG)
         pointed to CXA_S20

Table 310: Library assignment of the IH_S20_MB_CONFIG
Library                                           Folder
CXA_ModbusRTU                                     Type

Table 311: IH_S20_MB_CONFIG structure
Name           Data type            Description      Min. value Max. value   Default value
Interface‐     IH_S20_RS_           Interface    type RS232    RS422         RS232            Rising
Type           INTERFACE            (RS232, RS485 or                                          edge     at
                                    RS422)                                                    Enable
                                    For further infor‐
                                    mation,      see:
                                    IH_S20_RS_INTER
                                    FACE
Protocol       IH_S20_RS_           Not for Modbus                                            Rising
               PROTOCOL                                                                       edge at
Baud rate      IH_S20_RS_           Baud rate          BAU‐     BAU‐       BAU‐               Rising
               BAUDRATE             For further infor‐ DRATE_11 DRATE_250  DRATE_9600         edge    at
                                    mation,      see:  0        000                           Enable
                                    IH_S20_RS_BAU‐
                                    DRATE
DataWidth      IH_S20_RS_           Data width         DATABIT7 DATABIT6_N DATABIT7_EVE Rising
               DATAWIDTH                               _EVEN_ST ONE_STOPB N_STOPBIT1 edge       at
                                                       OPBIT1   IT1                     Enable
FirstDeli‐     BYTE                 Not for Modbus 0                       16#0D        Rising
miter                                                                                   edge at
                                                                                        Enable
SecondDeli‐ BYTE                    Not for Modbus 0                       16#0A        Rising
miter                                                                                   edge at
                                                                                        Enable
ErrorPattern BYTE                   Not for Modbus 0                       16#24        Rising
                                                                                        edge at
                                                                                        Enable

Name          Data type          Description        Min. value Max. value   Default value
                                 Direct baud rate
● Uni1        BYTE               specification via                                          Rising
● Uni2        BYTE               bytes, refer to the 0                      0               edge       at
● Uni3        BYTE               data sheet S20-                                            Enable
                                 RS-Uni
Tv            BYTE               Lead time (ms)     0                       0               edge       at

Tn            BYTE               Lag time (ms)      0                       0               edge       at

### 16.24.5 IH_INLN_MB_TOKEN

    Use this structure to request the token availability of the master function
    block.

Table 312: Library assignment of the IH_INLN_MB_TOKEN
Library                                          Folder
CXA_ModbusRTU                                    Type

Table 313: IH_INLN_MB_TOKEN structure
                  Data                                    Min.      Max.    Defaul
Name                          Description                                           Application
                  type                                    value     value   t value
                              Token number is already
Occupied          BOOL                                   FALSE      TRUE    FALSE Continuous
                              used
                              A token request is sent to
SendRequest       BOOL                                   FALSE      TRUE    FALSE Continuous
                              the master
Reques‐
                  BOOL        Master allows token access FALSE      TRUE    FALSE Continuous
tGranted

### 16.24.6 IH_INLN_MB_SUBREQUESTS

    Use this structure to query access information on Modbus file protocols.

Table 314: Library assignment of the IH_INLN_MB_SUBREQUESTS
Library                                          Folder
CXA_ModbusRTU                                    Type

Table 315: IH_INLN_MB_SUBREQUESTS structure
Name                          Data type           Description
FileNumber                    WORD                File number
RecordNumber                  WORD                Protocol number
RecordLength                  WORD                Protocol length

### 16.24.7 IH_INLN_MB_RECORD

    The structure returns the final response output of the ⮫ IH_MBReadFileRecord
    function block.

Table 316: Library assignment of the IH_INLN_MB_RECORD
Library                                       Folder
CXA_ModbusRTU                                 Type

Table 317: IH_INLN_MB_RECORD structure
Name                       Data type                     Description
DataLength                 UINT                          Total number of received data (output)
SubRequestData             ARRAY [0.0,124] OF WORD       Requested protocol data

### 16.24.8 IH_INLN_MB_EVENTLOG

The structure returns the final response output of the ⮫ IH_MBGetCommEven‐
tLog function block.

Table 318: Library assignment of the IH_INLN_MB_EVENTLOG
Library                                       Folder
CXA_ModbusRTU                                 Type

Table 319: IH_INLN_MB_EVENTLOG structure
Name                 Data type                          Description
Status               WORD                               Status
EventCount           WORD                               Number of events
MessageCount         WORD                               Number of messages
Events               ARRAY [0.0,63] OF BYTE             Events

## 16.25 Error codes

The function blocks of the CXA_ModbusRTU library uses the error codes
ADD1: 16#0A0F.0111 and ADD2 can be found in:
● CXA_ModbusRTU: ModbusRTU_ErrorAdd
● CXA_EthercatMaster: ErrorCodes
For the CXA_ModbusRTU error codes, refer to the Global Variable List Mod‐
busRTU_ErrorAdd of the library CXA_ModbusRTU.
For the CXA_EthercatMaster error codes, refer to the Global Variable List
ErrorCodes in the library CXA_EthercatMaster.
