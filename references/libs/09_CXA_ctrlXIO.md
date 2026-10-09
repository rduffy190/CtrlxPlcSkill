# 9 CXA_ctrlXIO

## 9.1 Introduction and overview

The library CXA_ctrlXIO describes the access options of the IEC program to
the ctrlX I/O system using function blocks.
The ctrlX I/O system is used in ctrlX CORE controls with ctrlX I/O modules.

ctrlX station: Example with bus coupler and ctrlX I/O

Table 56: Function blocks of the CXA_ctrlXIO library
Category/module                   Function block                   Description
Communication
XI52x001                          IH_XISerialCom                   Serial data handling

For the support of the following modules, refer to the respective libraries:
−   ModbusRTU - XI52x001:
    CXA_ModbusRTU library

For an acyclic access, use the corresponding function blocks from the
CXA_EthercatMaster library, e.g. the IL_ECATCoeReadSdo or IL_ECATCoeWri‐
teSdo function blocks for CoE objects.

Documentation
For the documentation on each single function block, go to the
“Documentation” of the selected function block in the ctrlX PLC Engineering
library manager.
The “Documentation” tab includes the following information:
● Special features on the function blocks
● Structures of the function blocks
● Enumerations of the function blocks
Code samples are listed in the following.
The code samples are intended as help. For further examples, go to the
library manager of ctrlX PLC Engineering within the library in the "_Example"
folder.

## 9.2 IH_XISerialCom

The function block IH_XISerialCom and the ctrlX I/O modules allow the serial
communication with RS485/422 or RS232.
Supported modules:
● XI521001 - 1-channel Serial RS232
● XI522001 - 1-channel Serial RS485/RS422
ModbusRTU support
When using ModbusRTU, we recommend to use the library CXA_ModbusRTU.

Sample program: IH_XISerialCom function block with ctrlX I/O XI521001 on
the EtherCAT bus coupler XB-EC-12 or locally on a ctrlX CORE control

At the function block, it is directly linked to the ctrlX I/O XI522001 via
the cyclic process data. Therefore, no field bus or address configuration is
required.
TRUE at the "Enable" input applies the configuration and the function block
reads the current module status.

Step 1: Module configuration with ctrlX I/O Engineering.

Step 2: Variable declaration for the IH_XISerialCom module
Declaration:

PROGRAM Example_IH_XISerialCom
VAR
    fbIH_XISerialCom      : IH_XISerialCom;
    bEnable               : BOOL := FALSE;           // TRUE: Function is enabled
    bInOperation          : BOOL;                    // TRUE: Function Block is working on its actual task
    bError                : BOOL;                    // TRUE: Indicates an error
    ErrorID               : ERROR_CODE;              // Class of error
    ErrorIdent            : ERROR_STRUCT;            // Detailed information about error
    bSend                 : BOOL := FALSE;           // TRUE: Data is sent at a positive edge
    arSendData            : ARRAY[0..511] OF BYTE;   // Pointer to transmission data array. Use ADR( ) operator
    uiSizeOfSendData      : UINT := 1;               // Number of bytes to be sent. SizeOfSendData <= send data
array size). Use SIZEOF( ) operator
    bRecv                 : BOOL := FALSE;           // TRUE: FB Updates data from internally filled buffer to
user at a positive edge
    arRecvData            : ARRAY[0..511] OF BYTE;   // Pointer to reception data array. Use ADR( ) operator
    uiSizeOfRecvData      : UINT := 1;               // Number of bytes to be received. (SizeOfRecvData <=
RecvData array size). Use SIZEOF( ) operator
    bSendDone             : BOOL;                    // TRUE: Data Sending task is successfully done
    bRecvDone             : BOOL;                    // TRUE: Data Receiving task is successfully done
    bRecvBufferOverFlow   : BOOL;                    // TRUE: FB internal buffer is overflowing
    bRecvBufferNotEmpty   : BOOL;                    // TRUE: Data available for reading in buffer
    uiRecvBufferSize      : UINT;                    // Number of bytes available for reading in the buffer
    uiRecvCounter         : UINT;                    // Amount of received data in bytes

    // Process Data mapping; Change Mapping Address(Ex:- %IB219) as per your module mapping address. See below
image for detailed explanation.
    stInProcData AT %IB219    : IH_XI_INPROC_DATA;        // Input process data structure. Link this variable to
module process data
    stOutProcData AT %QB66    : IH_XI_OUTPROC_DATA;       // Output process data structure. Link this variable to
module process data
END_VAR

Program for the serial ctrlX I/O module with the function block:

// IH_XI52 Serial Communication FB Call
fbIH_XISerialCom(
    Enable:= bEnable,
    InOperation=> bInOperation,
    Error=> bError,
    ErrorID=> ErrorID,
    ErrorIdent=> ErrorIdent,
    Send:= bSend,
    SendDataAdr:= ADR(arSendData),
    SizeOfSendData:= uiSizeOfSendData,
    Recv:= bRecv,
    RecvDataAdr:= ADR(arRecvData),
    SizeOfRecvData:= uiSizeOfRecvData,
    InProcData:= stInProcData,
    OutProcData:= stOutProcData,
    TimeOut:= T#5S,
    SendDone=> bSendDone,
    RecvDone=> bRecvDone,
    RecvBufferOverFlow=> bRecvBufferOverFlow,
    RecvBufferNotEmpty=> bRecvBufferNotEmpty,
    RecvBufferSize=> uiRecvBufferSize,
    RecvCounter=> uiRecvCounter);

Sending and receiving data:
A positive edge triggers sending and reception. All data is read from the
module buffer or transferred to the buffer. If you expect 60 bytes for example
when reading, wait until the function block shows at least a value of 60 at the
"RecvBufferSize" output and then set "bRecv".
There is a "SendDone" and a "RecvDone" for sending and receiving, as the
module supports sending and receiving in parallel. Full duplex is required for
sending and receiving.
bSend := TRUE; // To Send the data
bRecv := TRUE; // To Receive the data

Step 3: Linking process data in the I/O mapping at the module in ctrlX PLC
Engineering
Determining and linking process data in the I/O mapping to the variables
declared in the PLC program for the ctrlX I/O XI521001 module via %
addresses.

## 9.3 Error codes

The function blocks of the CXA_ctrlXIO library use the following error codes:
ADD1: 16#0A0F.011A
ADD2: to be found in:
● CXA_ctrlXIO CTRLXIO_ErrorAdd
● CXA_EthercatMaster ErrorCodes
For the CXA_ctrlXIO error codes, refer to          the   Global   Variable   List
CTRLXIO_ErrorAdd in the library CXA_ctrlXIO.
For the CXA_EthercatMaster error codes, refer to the Global Variable List
ErrorCodes in the library CXA_EthercatMaster.
