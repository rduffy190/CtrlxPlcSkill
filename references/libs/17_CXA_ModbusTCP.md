# 17 CXA_ModbusTCP

## 17.1 Introduction and overview

The Modbus TCP exchanges data between Ethernet devices supporting the
Modbus protocol. This documentation focuses on HMI devices. The Modbus
slave (server) is the control used for the Modbus masters (clients) to connect.
A Modbus TCP server is implemented in each of the ⮫ Chapter 17.2.4 IL_Mod‐
busTCPServer on page 401 and ⮫ Chapter 17.2.5 IL_ModbusTCPServerType02
on page 405 function blocks in the CXA_ModBusTCP library.

The functions blocks "IL_ModBusTCPServer" and "IL_ModBusTCPServer‐
Type02" differ in the following:
In contrast to the Modbus specification, the data ranges for "Coil Data" and
"Discrete Input Data" are summarized under "BitData", the "Holding Register"
and "Input Register" are summarized under "RegisterData" in the IL_Mod‐
BusTCPServer function block.

ModbusTCP, terms
● Coils: Coils form a bit array with a length of 65536 bits max. Bits can be
  read and written.
● Discrete Input: Discrete inputs form a bit array with a length of 65536 bits
  max. The bits can only be read.
● Holding Register: The registers form an array of words (16 bit values) with
  a length of 65536 words max. The register can be read and written.
● Input Register: The registers form an array of words (16 bit values) with a
  length of 65536 words max. The registers can only be read.

## 17.2 ModbusTCP server

### 17.2.1 Introduction and overview

It is useful for the configuration to execute first tests with the Modbus test
clients. Test client examples available in the internet for free (date 09.2008):
● IPC@CHIP Modbus Client V1.4
● Modbus TCP/IP Request Tool Pro
The following chapters describe the configuration of a TCP connection with
● Siemens WinCC-flexible 2007 (⮫ Chapter 17.2.2 Configuring with Siemens
   WinCC-flexible 2007 on page 392)
● Pro-face GP-Pro EX2.2 (⮫ Chapter 17.2.3 Configuring with Pro-face GP-Pro
   EX 2.2 on page 395)
The interfaces of third-party components can be subject to modifications. The
use cases are thus primarily for improving knowledge. Bosch Rexroth does not
guarantee the correctness of the information given.

Storage location for the example projects
The examples of the visualization systems Siemens WinCC-flexible and Pro-
face GP-Pro EX2.2 are located in the AddOn directory of the IndraWorks
installation DVD.

Addressing data from a PLC project
In the PLC project, data ranges for the register and bit data are transferred to
function block instance IL_ModbusTCPServer using the pointer.
The data ranges of the Modbus TCP server are accessed via the following
addressing by the Modbus client
Register data range:
Addressing the "Holding Register" data using %MW (read and write access) or
the "Input Register" data using %IW (only read access).
Bit data range:
Addressing the "Coil" data using %M (read and write access) or the "Discrete
Input" data using %I (only read access).

Bit data
In the test project, the bit data range was assigned as array of bytes from
where every single bit can be addressed continuously.
No ARRAY OF BOOL can be used for the bit data range since 8 bits of memory
are assigned to a variable of BOOL in the IndraLogic.
The individual bits of a byte can be copied on variables of type BOOL (and
vice versa)
The address of a variable from a bit data range corresponds to the bit number
from the byte array used for bit data.

Bit data (%M)
%M0 address corresponds to the BitData[0].0 variable
%M7 address corresponds to the BitData[0].7 variable
%M8 address corresponds to the BitData[1].0 variable
%M12 address corresponds to the BitData[1].4 variable

Register data
The register data range can consist of up to 65536 words and can be organ‐
ized by the user without any restrictions.
For a better overview on the register data, a structure containing arrays of
different PLC data types was used for the register data range in the test
project. This structure was created in such a way that the individual data type
areas are always provided with a length of 1000 words and do therefore begin
with a defined word address.

Example of a data structure for Register_Data

TYPE REGISTER_DATA :
STRUCT
   arWord:   ARRAY[0..999]OF WORD;     // %MW0000 - %MW0999
   arInt:    ARRAY[0..999]OF INT;      // %MW1000 - %MW1999
   arUint:   ARRAY[0..999]OF UINT;     // %MW2000 - %MW2999
   arDint:   ARRAY[0..499]OF DINT;     // %MW3000 - %MW3999
   arUdint: ARRAY[0..499]OF UDINT;     // %MW4000 - %MW4999
   arReal:   ARRAY[0..499]OF REAL;     // %MW5000 - %MW5999
   arString: ARRAY[0..99]OF STRING(19);// %MW6000 - %MW6999
   // String(19): because 19 byte string + 1 byte end sign
   // together 7000 WORDs
END_STRUCT
END_TYPE

Text string
Texts (STRING) can also be transferred via the register data range.
In the IndraLogic, the length of a STRING (in bytes) is always the given length
+ 1 byte of end ID
To define the STRINGS with their total word length, the length is always to be
specified with an odd number of bits
(e.g. string(19) => 19 byte string + 1 byte End ID = 20 byte = 10 words)

The address of a variable from the register data range results from the design
of the structure used for the register data.

If the previously data structure is used for RegisterData, the following
addresses result:

Register data (%MW)
%MW0 address corresponds to the RegisterData.arWord[0] variable
%MW1000 address corresponds to the RegisterData.arInt[0] variable
%MW1001 address corresponds to the RegisterData.arInt[1] variable
%MW5000 address corresponds to the RegisterData.arReal[0] variable
%MW5002 address corresponds to the RegisterData.arReal[1] variable
%MW6000 address corresponds to the RegisterData.arString[0] variable
%MW6010 address corresponds to the RegisterData.arString[1] variable

Program example - declaration section

PROGRAM ModbusCom
// Run in a low priority task
VAR
  fb_IL_ModBusTCPServerType02: IL_ModBusTCPServerType02; //
Instance of FB IL_ModbusTCPServerType02
  bEnableModbusSrv:    BOOL := TRUE;           // Enable FB
IL_ModbusTCPServerType02
  wPortNumber:         WORD := 502;            // Modbus
server port - 502 is Modbus default
  arbyBitData:         ARRAY[0..8191] OF BYTE; // Coil data
area for FC2, FC5 and FC15
  arbyDiscreteInputs: ARRAY[0..8191] OF BYTE; // Discrete
Input data area for FC1 (read only)
  RegisterData:        REGISTER_DATA;          // Holding
Register data area for FC3, FC6, FC16 and FC23
  InputRegisters:      REGISTER_DATA;          // Input
Register data area for FC4 (read only)
  bInOperation:        BOOL;                   // FB
IL_ModbusTCPServer is in operation
  bError:              BOOL;                   // FB
IL_ModbusTCPServer quits operation with error
  ErrorID:             ERROR_CODE;             // general
information about the error
  ErrorIdent:          ERROR_STRUCT;           // detailed
information about the error
  Stats:               IL_MODBUS_STATS;        // connection
statistics
END_VAR

Program example - implementation section

fb_IL_ModBusTCPServerType02(
  Enable := bEnableModbusSrv,
  Port := wPortNumber,
  CoilData:= ADR(arbyBitData),
  SizeOfCoilData:= SIZEOF(arbyBitData),
  InputData:= ADR(arbyDiscreteInputs),
  SizeOfInputData:= SIZEOF(arbyDiscreteInputs),
  HoldingRegisterData:= ADR(RegisterData),
  SizeOfHoldingRegisterData:= SIZEOF(RegisterData),
  InputRegisterData:= ADR(InputRegisters),
  SizeOfInputRegisterData:= SIZEOF(InputRegisters),
  InOperation => bInOperation,
  Error => bError,
  ErrorID => ErrorID,
  ErrorIdent => ErrorIdent,
  Stats => Stats);

### 17.2.2 Configuring with Siemens WinCC-flexible 2007

Communication settings
To configure the connection in WinCC-flexible, the following settings are
required:
1.     Open “Communication 🠂 Connections” in the project tree menu of the
       operating device
2.     Enter the name of the connection (comment is optional)
       Select the communication driver "Modicon MODBUS TCP/IP"
3.     Subsequently, the communication parameters are to be defined in the
       dialog

Table 320: WinCC-flexible Modbus TCP communication parameters
Section            Name            Value         Description
HMI device         Interface       Ethernet      Selection of the communication interface

Section        Name            Value      Description
Type            IP         Only IP is supported
PLC device     CPU type        Premium,   Schneider Modicon control type operating without
                Micro      address offset and normal bit counting (refer to the
                           Siemens user manual "WinCC-flexible 2007 Commu‐
                           nication Volume 2 - Chapter 6"
Server       "192.168.1.34 IP address of the control
             "
Port         "502"         Port of the communication connection (port of the
                           IL_ModbusTCPServer function block instance)
Remote slave "255"         Maintain default setting (255)!

address                    Not relevant for the Modbus TCP - refer to "MODBUS
                           Messaging on TCP/IP Implementation Guide V1.0b"
                           on ⮫ www.Modbus.org

      Variable declaration
      After configuring the connection, the variables can be declared.
      Therefore, the “Communication/Tags” menu is to be opened in the project
      tree of the operating device. Subsequently, a dialog is displayed and the varia‐
      bles required can be assigned.
      Example of a variable declaration in WinCC-flexible 2007:

WinCC - flexible variable declaration
Table 321: WinCC - flexible variable declaration
Input field          Example              Description
Name                 "Bit_0"              Variable name
Address              "%M0"                Modbus address of the variable

Input field          Example             Description
Connection           "BRC_Control"       Connection name
Data type            "Bit"               WinCC-flexible variable data type
Array count          "1"                 Number of array elements if variable is to be assigned as
                    array
Acquisition cycle    "1s"                Update rate of the variable values are to be read from the
                    control
In WinCC-flexible 2007, the following data types are available. The corre‐
sponding IndraLogic data types are listed below.

WinCC-flexible data types/IndraLogic data types
Table 322: WinCC - flexible data types
WinCC - flexible     IndraLogic           Description
Int                  UINT                 Unsigned integer length 16 bit
                                          Value range: 0 to 65535
+/-int               INT                  Signed integer length 16 bit
                                          Value range: -32768 to 32767
Double               UDINT                Unsigned double integer length 32 bit
                                          Value range: 0 to 4294967295
+/-double            DINT                 Signed double integer length 32 bit
                                          Value range: -2147483648 to 2147483647
Float                REAL                 Floating point length 32 bit
                                          Value range: 1.175494351e-38F to 3.402823466e+38F
Bit                  Single bit of a byte Single bit length 1 bit
16 bit group         WORD                 WORD length 16 bits
                                          Attention: For 16 bit groups, the bit counting in WinCC-
                                          flexible is vice versa to the one in IndraLogic
ASCII                STRING               The string length (in bytes) is to be configured in WinCC-
                                          flexible via the Tag Properties.
                     The declared variables can now be used for different WinCC-flexible function‐
                     alities.

Displaying and entering different variables

### 17.2.3 Configuring with Pro-face GP-Pro EX 2.2

Communication settings
The following settings are required to configure the connection in Pro-face
GP-Pro EX 2.2:
● Select the “Device/PLC” entry from the System settings menu
● Execute the “Add device/PLC” link in the working area of the window
● Subsequently, the following settings are to be carried out in the "Add
  device/PLC dialog":

Table 323: Communication settings - Device selection
Drop-down menu             Selection
Manufacturer               Schneider Electric Industries
Series                     MODBUS TCP master
Port                       Ethernet (TCP)
● Press [Add] to confirm the selection.
● Enter the connection name in the extended window of the working range
  under "Device name" and click on Settings

● Subsequently, the following settings are to be carried out in the "Equip‐
  ment configuration" register in the "Individual device settings" dialog:

Table 324: Table of the GP-Pro EX communication settings - Device parameters
Section              Name               Value               Description
Equipment            IP Address         "192.168.1.34"      IP address of the control
Address              Type               "502"               Port of the communication connec‐
                                                            tion (port of the IL_ModbusTCPServer
                                                            function block instance)
                     Unit ID            "255"               Maintain default setting (255)!
                                                            Not relevant for the Modbus TCP
                                                            - refer to "MODBUS Messaging on
                                                            TCP/IP Implementation Guide V1.0b"
                                                            on ⮫ www.Modbus.org
Bit manipulation    Reset of the bits in "Do not clear"     Maintain default setting (Do not clear)
to Holding Register this word
IEC61131 Syntax Address Mode             "0-based (default)" Activate IEC61131 Syntax and main‐
                                                             tain Address Mode for the default set‐
                                                             ting (0-based)
Variables           Double Word word "Low word first         Word order within a double word
                    order                (L/H)"

● The "MaxQuery" register defines the maximum number of data that can be
  packed in the Modbus request. The default settings remain.

● Press [OK] to confirm the selection.
● The "Text Data Mode" is still to be adapted to allow interpretation of texts.
  Therefore, click on the "Change" link in the working area window.

● Subsequently, select 2 in the "Change text data mode” dialog and press
  [Change].

Using addresses
After configuring the connection, the addresses can be used directly in dif‐
ferent GP-Pro EX functionalities.

Variable declaration
Symbol variables of type bit address and word address can also be declared.
The address content can be used in different GP-Pro EX functionalities via
these symbol variables.
To declare the symbol variables in the working area of the window, open
“Common settings 🠂 Symbol variables” in the menu.

After creating the symbol variable, it can be used as "placeholder" for the
address.

The number of the registers to be interpreted is defined via the data type used
in the individual display fields.
For display fields of type "Text Display", the number of characters to be dis‐
played are defined via the number of the registers to be interpreted.

Displaying and entering different variables

### 17.2.4 IL_ModbusTCPServer

Brief description
A Modbus TCP slave is implemented in the IL_ModbusTCPServer function
block. Discrete Inputs, Coils, Input Registers and Holding Registers are sup‐
ported with read and write access. Arrays are used for the data exchange.

        Table 325: Library assignment of the IL_ModbusTCPServer
        Library/folder
        CXA_ModbusTCP/Server

        Interface description

Table 326: Interface variables of the IL_ModbusTCPServer function block
                   Name               Type                Description
VAR_INPUT          Enable             BOOL                Function block processing enabled (level-
                                                          controlled)
                   Port               UINT                TCP port at which incoming connections are
                                                          expected
                   BitData            POINTER TO          Pointer to bit data.
                                      ARRAY[0..8191] OF
                                      BYTE
                   SizeOfBitData      UDINT               Number of bytes in BitData (bit number/8)
                   RegisterData       POINTER TO          Pointer to register data in word width
                                      ARRAY[0...65535]
                                      OF WORD
           SizeOfRegister‐            UDINT               Number of bytes in the register data (reg‐
           Data                                           ister number * 2)
VAR OUTPUT InOperation                BOOL                The Modbus server runs and accepts
                                                          incoming connections.
                   Error              BOOL                Error while processing the function block.
                   ErrorID            ⮫ ERROR_CODE        If the "Error" output is set, it contains a
                                                          broad error classification
                   ErrorIdent         ⮫ ERROR_STRUCT      If the "Error" output is set, this output con‐
                                                          tains detailed error information
                   Stats              ⮫,                  Contains counters for data packages and
                                      IL_MODBUS_STATS     errors
Table 327: Input behavior of the IL_ModbusTCPServer
Name                       Type          Min. value   Max. value     Default value Applied
Enable                     BOOL                                      FALSE         Continuous
Port                       UINT          0            65535          502           Rising edge at
                                                                                   "Enable"
BitData                    POINTER       0            N. def.        0             Rising edge at
                                                                                   "Enable"
SizeOfBitData              UDINT         0            8191           0             Rising edge at
                                                                                   "Enable"
RegisterData               POINTER       0            N. def.        0             Rising edge at
                                                                                   "Enable"

Name               Type            Min. value      Max. value     Default value Applied
SizeOfRegisterData UDINT           0               131070         0             Rising edge at
                                                            "Enable"

Functional description
The IL_ModbusTCPServer function block implements a Modbus slave that can
connect up to 16 Modbus masters. The function block is passive during the
data exchange. Being passive means that the Modbus master specifies which
data is read and which data is written. Discrete Inputs, Coils, Input Registers
and Holding Registers are supported.
In contrast to the Modbus specification, the respective Discrete Inputs, Coils

as well as Input Registers and Holding Registers are imaged on the same data
range.
In case more than 16 devices try to connect simultaneously, the connection
to the most previous data exchange is aborted before a new connection is
accepted. This behavior complies with the Modbus TCP specification. This
should be avoided in practice. Therefore, it is useful to open a second
Modbus TCP server on a different port.

Enable, InOperation
"Enable" is the processing enabled of the function block. The function block
is active as long as "Enable" is TRUE. All inputs are applied and the func‐
tion block is initialized at a rising edge at "Enable". After the initialization is
completed, the output is set to "InOperation" to indicate that the incoming
Modbus TCP connections are accepted and can now be processed. The
existing connections are closed and the port is shared at a falling edge at
"Enable".

Error, ErrorID, ErrorIdent
If an error occurs while processing the function block, the output "Error" is
set. "ErrorID" and "ErrorIdent" contain detailed error information. Function
block processing is paused. The "Error" output is reset at a falling edge at
"Enable”.
The error outputs are only set if errors occur while processing the function
block. Errors caused by the Modbus TCP protocol do not generate any output
at the error outputs. The "NumExceptions" field in the "Stats" output is used
for that purpose.

Port
Generally, the Modbus TCP uses the port 502, but a Modbus TCP server can
be optionally opened on a different port as well. Therefore, the port number
to be used has to be written on the "Port" input before the function block is
enabled.

BitData, SizeOfBitData
The "BitData" input corresponds to the Discrete Inputs and Coils defined in
the Modbus. Coils form a bit array with a length of 65536 bits max. Bits can
be read and written. The data exchange is executed via the array assigned at
the "BitData" input. Each array byte represents 8 bits.
The array size in byte is to be assigned at the "SizeOfBitData" input. The
SIZEOF() operator can be used for this. The function block checks whether
the incoming requests are within the assigned array using the "SizeOfBitData".

It is useful to define an own data structure to access the bits. The pragma
{bitaccess} in the IndraLogic 1.x or {bit} allows an access on the indi‐
vidual bits in IndraLogic 2G.
It is useful to define an own data structure to access the bits. The pragma
{bitaccess} in the IndraLogic 1.x or {bit} allows an access on the indi‐
vidual bits in IndraLogic 2G.
It is useful to define an own data structure to access the bits. The pragma
{bitaccess} in the IndraLogic 1.x or {bit} allows an access on the indi‐
vidual bits in IndraLogic 2G.

RegisterData, SizeOfRegisterData
The "RegisterData" input corresponds to the Input Registers and Holding Reg‐
isters defined in the Modbus. The registers form an array of words (16 bit
values) with a length of 65536 words max. Data is exchanged via the array
applied at the "RegisterData" input.
The array size in bytes has to be applied at the "SizeOfRegisterData" input.
The SIZEOF() operator can be used for this. The function block checks
whether the incoming requests are within the assigned array using the "SizeO‐
fRegisterData".
It is useful to define an own data structure to access the registers. The align‐
ment of the data (16 bit) has to fit into words.

Stats
The "Stats" output contains a data structure indicating the status and statistic
information on the running communication and the IP addresses of the con‐
nected clients. Read and write access is counted in the corresponding fields.
Protocol errors are only counted in the "NumExceptions" field. If the maximum
number of the counter is exceeded, it restarts with 0. The maximum value of a
counter is 232-1.

Supported Modbus function codes
Function codes are used by the Modbus master to access the Modbus slave.
Knowledge about the codes supported helps to find the errors. It is not
required for the normal operating mode though. The following function codes
are supported:
Table 328: Supported Modbus function codes
Function code        Name                       Description
1                    Read Coils                 Reads a number of bits from "BitData" starting
                                                from an initial address
2                    Read Discrete Inputs       Reads a number of bits from "BitData" starting
                                                from an initial address
3                    Read Holding Registers     Reads a number of registers from "RegisterData"
                                                starting from an initial address
4                    Read Input Registers       Reads a number of registers from "RegisterData"
                                                starting from an initial address
5                    Write Single Coil          Writes a bit into "BitData" starting from an initial
                                                address
6                    Write Single Register      Writes a register into "RegisterData" starting from
                                                an initial address
15                   Write Multiple Coils       Writes a number of bits into "BitData" starting
                                                from an initial address
16                   Write Multiple Registers   Writes a number of registers into "RegisterData"
                                                starting from an initial address

Function code        Name                       Description
23                   Read/Write Multiple Regis‐ Executes a combined read/write operation on
ters                       "RegisterData"
43/14                Read Device Identification Reads the default device information of the
                           Modbus TCP server:
                           ● VendorName: "Bosch Rexroth"
                           ● ProductCode: "IL_ModbusTCPServer"
                           ● MajorMinorRevision: "01Vxx"
The function codes 1, 2, 5, 15 access a storage area assigned at the "BitData"
input.

The function codes 3, 4, 6, 16 access a storage area assigned at the "Register‐
Data" input.

Troubleshooting
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1 and Additional2:
Table 329: Error codes of the IL_ModbusTCPServer
ErrorID                  Additional1     Additional2 Description
INPUT_INVALID_ERRO       16#0A0F0111     16#0C231800 The "BitData" input is a zero pointer.
R (16#0001)
INPUT_INVALID_ERRO       16#0A0F0111     16#0C231802 The "RegisterData" input is a zero pointer.
R (16#0001)
INPUT_INVALID_ERRO       16#0A0F0111     16#0C231804 The "SizeOfBitData" input is 0.
R (16#0001)
INPUT_INVALID_ERRO       16#0A0F0111     16#0C231806 The "SizeOfRegisterData" input is 0.
R (16#0001)
INPUT_INVALID_ERRO       16#0A0F0111     16#0C231808 The "SizeOfRegisterData" input is odd.
R (16#0001)
RESOURCE_ERROR           16#0A0F0111     16#0C231810 Could not open socket.
(16#0003)
RESOURCE_ERROR           16#0A0F0111     16#0C231811 The port is assigned.
(16#0003)
RESOURCE_ERROR           16#0A0F0111     16#0C231812 Could not accept incoming connection.
(16#0003)

### 17.2.5 IL_ModbusTCPServerType02

Brief description
A Modbus TCP slave is implemented in the IL_ModbusTCPServerType02 func‐
tion block. Discrete Inputs, Coils, Input Registers and Holding Registers are
supported with read and write access. The data exchange is executed via 4
separate arrays for the individual data ranges.

Table 330: Library assignment of the IL_ModbusTCPServerType02
Library/folder
CXA_ModbusTCP/Server

  Interface description

Table 331: Interface variables of the IL_ModbusTCPServerType02 function block
                   Name               Type           Description
VAR_INPUT          Enable             BOOL           Function block processing enabled (level-
                                                     controlled).
                   Port              UINT            TCP port at which incoming connections
                                                     are expected.
                   CoilData          POINTER TO      Pointer to coil data (bit data range is nei‐
                                     ARRAY[0..8191] ther read-protected nor write-protected).
                                     OF BYTE
                   SizeOfCoilData    UDINT           Number of bytes in CoilData (bit
                                                     number/8).
                   InputData         POINTER TO      Pointer to discrete input data (bit data
                                     ARRAY[0..8191] range is not read-protected).
                                     OF BYTE
                   SizeOfInputData   UDINT           Number of bytes in InputData (bit
                                                     number/8).
                   HoldingRegister‐  POINTER TO      Pointer to Holding register data in word
                   Data              ARRAY[0...65535 width (register data range is neither read-
                                     ] OF WORD       protected nor write-protected).
                   SizeOfHoldingRe‐ UDINT            Number of bytes in the holding register
                   gisterData                        data (register number * 2).
                   InputRegisterData POINTER TO      Pointer to Input register data in word
                                     ARRAY[0...65535 width (register data range is not read-pro‐
                                     ] OF WORD       tected).
                   SizeOfInputRegis‐ UDINT           Number of bytes in the Input register data
                   terData                           (register number * 2).
VAR OUTPUT         InOperation       BOOL            The Modbus server runs and accepts
                                                     incoming connections.
                   Error             BOOL            Error while processing the function block.
                   ErrorID           ⮫ ERROR_CODE If the "Error" output is set, it contains a
                                                     broad error classification.
                   ErrorIdent        ⮫ ERROR_STRUC If the "Error" output is set, this output
                                     T               contains detailed error information
                   Stats              ⮫,            Contains counters for data packages and
                                      IL_MODBUS_STA errors
                                      TS

Table 332: Input behavior of the IL_ModbusTCPServerType02
Name                 Type            Min. value    Max. value   Default value Applied
Enable               BOOL                                       FALSE         Continuous
Port                 UINT            0             65535        502           Rising edge at
                                                                              "Enable"
CoilData             POINTER         0             N. def.      0             Rising edge at
                                                                              "Enable"
SizeOfCoilData       UDINT           0             8191         0             Rising edge at
                                                                              "Enable"
InputData            POINTER         0             N. def.      0             Rising edge at
                                                                              "Enable"

SizeOfInputData      UDINT           0             8191         0             Rising edge at
                                                         "Enable"
HoldingRegister‐  POINTER            0             N. def.      0             Rising edge at
Data                                                                          "Enable"
SizeOfHoldingRe‐ UDINT               0             131070       0             Rising edge at
gisterData                                                                    "Enable"
InputRegisterData POINTER            0             N. def.      0             Rising edge at
                                                         "Enable"
SizeOfInputRegis‐    UDINT           0             131070       0             Rising edge at
terData                                                                       "Enable"
Table 333: IL_MODBUS_STATS data structure
Name                         Type              Default value    Description
NumReadBits                  UDINT             0                Number of read access on bits
NumReadRegisters             UDINT             0                Number of read access on reg‐
                                                                ister
NumWriteBit                  UDINT             0                Number of single write access on
                                                                bits
NumWriteRegister             UDINT             0                Number of single write access on
                                                                register
NumWriteBits                 UDINT             0                Number of multiple write access
                                                                on bits
NumWriteRegisters            UDINT             0                Number of multiple write access
                                                                on register
NumReadWriteRegs             UDINT             0                Number of combined read/write
                                                                access on register
NumExceptions                UDINT             0                Number of Modbus errors
ConnectedClients             ARRAY[0..15] OF                    IP addresses of the clients con‐
                             String(16)                         nected

Functional description
The IL_ModbusTCPServerType02 function block implements a Modbus slave
that can connect up to 16 Modbus masters. The function block is passive
during the data exchange. Being passive means that the Modbus master
(client) specifies which data is read and which data is written. Discrete
Inputs, Coils, Input Registers and Holding Registers are supported. As in the
Modbus specification, the Discrete Inputs, Coils as well as Input Registers
and Holding Registers are imaged on separate data ranges.

In case more than 16 devices try to connect simultaneously, the connection
to the most previous data exchange is aborted before a new connection is
accepted. This behavior complies with the Modbus TCP specification. This
should be avoided in practice. Therefore, it is useful to open a second
Modbus TCP server on a different port.

Enable, InOperation
"Enable" is the processing enabled of the function block. The function block
is active as long as "Enable" is TRUE. All inputs are applied and the func‐
tion block is initialized at a rising edge at "Enable". After the initialization is
completed, the output is set to "InOperation" to indicate that the incoming
Modbus TCP connections are accepted and can now be processed. The
existing connections are closed and the port is shared at a falling edge at
"Enable".

Error, ErrorID, ErrorIdent
If an error occurs while processing the function block, the output "Error" is
set. "ErrorID" and "ErrorIdent" contain detailed error information. Function
block processing is paused. The "Error" output is reset at a falling edge at
"Enable”.
The error outputs are only set if errors occur while processing the function
block. Errors caused by the Modbus TCP protocol do not generate any output
at the error outputs. The "NumExceptions" field in the "Stats" output is used
for that purpose.

Port
Generally, the Modbus TCP uses the port 502, but a Modbus TCP server can
be optionally opened on a different port as well. Therefore, the port number
to be used has to be written on the "Port" input before the function block is
enabled.

CoilData, SizeOfCoilData
The "CoilData" input corresponds to the coils defined in the Modbus. Coils
form a bit array with a length of 65536 bits max. Bits can be read and written.
The data exchange is executed via the array assigned at the "CoilData" input.
Each array byte represents 8 bits.
The array size in byte is to be assigned at the "SizeOfCoilData" input. The
SIZEOF() operator can be used for this. The function block checks whether
the incoming requests are within the assigned array using the "SizeOfCoil‐
Data".
It is useful to define an own data structure to access the bits. The pragma
{bitaccess } allows an access on the individual bits.

InputData, SizeOfInputData
The "InputData" input corresponds to the discrete inputs defined in the
Modbus. Discrete inputs form a bit array with a length of 65536 bits max. The
bits can only be read. The data exchange is executed via the array assigned at
the "InputData" input. Each array byte represents 8 bits.
The array size in byte is to be assigned at the "SizeOfInputData" input. The
SIZEOF() operator can be used for this. The function block checks whether
the incoming requests are within the assigned array using the "SizeOfInput‐
Data".
It is useful to define an own data structure to access the bits. The pragma
{bitaccess } allows an access on the individual bits.

HoldingRegisterData, SizeOfHoldingRegisterData
The "HoldingRegisterData" input corresponds to the Holding register defined
in the Modbus. The registers form an array of words (16 bit values) with
a length of 65536 words max. The register can be read and written. The
data exchange is executed via the array assigned at the "HoldingRegisterData"
input.
The array size in byte is to be assigned at the "SizeOfHoldingRegisterData"
input. The SIZEOF() operator can be used for this. The function block checks
whether the incoming requests are within the assigned array using the
"SizeOfHoldingRegisterData".
It is useful to define an own data structure to access the registers. The align‐

ment of the data (16 bit) has to fit into words.

InputRegisterData, SizeOfInputRegisterData
The "InputRegisterData" input corresponds to the Input register defined in the
Modbus. The registers form an array of words (16 bit values) with a length
of 65536 words max. The registers can only be read. The data exchange is
executed via the array assigned at the "InputRegisterData" input.
The array size in byte is to be assigned at the "SizeOfInputRegisterData"
input. The SIZEOF() operator can be used for this. The function block checks
whether the incoming requests are within the assigned array using the "SizeO‐
fInputRegisterData".
It is useful to define an own data structure to access the registers. The align‐
ment of the data (16 bit) has to fit into words.

Stats
The "Stats" output contains a data structure indicating the status and statistic
information on the running communication and the IP addresses of the con‐
nected clients. Read and write access is counted in the corresponding fields.
Protocol errors are only counted in the "NumExceptions" field. If the maximum
number of the counter is exceeded, it restarts with 0. The maximum value of a
counter is 232-1.

Supported Modbus function codes
Function codes are used by the Modbus master (client) to access the Modbus
slave (server). Knowledge about the codes supported helps to find the errors.
It is not required for the normal operating mode though. The following func‐
tion codes are supported:
Table 334: Supported Modbus function codes
Function code                Name                      Description
1                            Read Coils                Reads a number of bits from "CoilData"
                                                       starting from an initial address
2                            Read Discrete Inputs      Reads a number of bits from "InputData"
                                                       starting from an initial address
3                            Read Holding Registers    Reads a number of registers from "Hol‐
                                                       dingRegisterData" starting from an initial
                                                       address
4                            Read Input Registers      Reads a number of registers from "InputRe‐
                                                       gisterData" starting from an initial address
5                            Write Single Coil         Writes a bit into "CoilData" starting from an
                                                       initial address
6                            Write Single Register     Writes a register into "HoldingRegisterData"
                                                       starting from an initial address

Function code             Name                         Description
15                        Write Multiple Coils         Writes a number of bits into "CoilData"
                                  starting from an initial address
16                        Write Multiple Registers     Writes a number of registers into "Hol‐
                                  dingRegisterData" starting from an initial
                                  address
23                        Read/Write Multiple Regis‐   Executes a combined read/write operation
     ters                         on "HoldingRegisterData"
43/14                     Read Device Identification   Retrieves standard device information of
                                  the Modbus TCP server:
                                  ● VendorName: "Bosch Rexroth"
                                  ● ProductCode: "IL_ModbusTCPServer‐
                                    Type02"
                                  ● MajorMinorRevision: "01Vxx"
The function codes 1, 5, 15 access a storage area assigned at the "CoilData"
input.
The function code 2 accesses a storage area assigned at the "InputData" input.

The function codes 3, 6, 16 access a storage area assigned at the "HoldingRe‐
gisterData" input.
The function code 4 accesses a storage area assigned at the "InputRegister‐
Data" input.

Troubleshooting
The function block uses the F_RELATED_TABLE, 16#170x error table. It can
generate the following error messages in Additional1 and Additional2:
Table 335: Error codes of the IL_ModbusTCPType02
ErrorID                  Additional1    Additional2 Description
INPUT_INVALID_ERRO       16#0A0F0111    16#0C231800 The "CoilData" input is a zero pointer.
R (16#0001)
INPUT_INVALID_ERRO       16#0A0F0111    16#0C231801 The "InputData" input is a zero pointer.
R (16#0001)
INPUT_INVALID_ERRO       16#0A0F0111    16#0C231802 The "HoldingRegisterData" input is a zero
R (16#0001)                                         pointer.
INPUT_INVALID_ERRO       16#0A0F0111    16#0C231803 The "InputRegisterData" input is a zero
R (16#0001)                                         pointer.
INPUT_INVALID_ERRO       16#0A0F0111    16#0C231804 The "SizeOfCoilData" input is 0.
R (16#0001)
INPUT_INVALID_ERRO       16#0A0F0111    16#0C231805 The "SizeOfInputData" input is 0.
R (16#0001)
INPUT_INVALID_ERRO       16#0A0F0111    16#0C231806 The "SizeOfHoldingRegisterData" input is
R (16#0001)                                         0.
INPUT_INVALID_ERRO       16#0A0F0111    16#0C231807 The "SizeOfInputRegisterData" input is 0.
R (16#0001)
INPUT_INVALID_ERRO       16#0A0F0111    16#0C231808 The "SizeOfHoldingRegisterData" input is
R (16#0001)                                         odd.
INPUT_INVALID_ERRO       16#0A0F0111    16#0C231809 The "SizeOfInputRegisterData" input is
R (16#0001)                                         odd.
RESOURCE_ERROR           16#0A0F0111    16#0C231810 Could not open socket.
(16#0003)

ErrorID                  Additional1      Additional2 Description
RESOURCE_ERROR           16#0A0F0111      16#0C231811 The port is assigned.
(16#0003)
RESOURCE_ERROR           16#0A0F0111      16#0C231812 Could not accept incoming connection.
(16#0003)

### 17.2.6 IL_MODBUS_STATS

The IL_MODBUS_STATS structure contains status and statistic information on
the running communications and the IP addresses of the connected client.
Read and write access is counted in the corresponding fields. Protocol errors
are only counted in the "NumExceptions" field. If the maximum number of the

counter is exceeded, it restarts with 0. The maximum value of a counter is
232-1.
Table 336: IL_MODBUS_STATS data structure
Name                         Type              Default value   Description
NumReadBits                  UDINT             0               Number of read access on bits
NumReadRegisters             UDINT             0               Number of read access on register
NumWriteBit                  UDINT             0               Number of single write access on bits
NumWriteRegister             UDINT             0               Number of single write access on reg‐
                                                               ister
NumWriteBits                 UDINT             0               Number of multiple write access on
                                                               bits
NumWriteRegisters            UDINT             0               Number of multiple write access on
                                                               register
NumReadWriteRegs             UDINT             0               Number of combined read/write
                                                               access on register
NumExceptions                UDINT             0               Number of Modbus errors
ConnectedClients             ARRAY[0..15] OF                   IP addresses of the clients connected
                             String(16)

## 17.3 ModbusTCP client

### 17.3.1 Introduction and overview

   The function blocks to the ModbusTCP client exchange data with a Mod‐
   busTCP server. The communication partner can either be an I/O device or
   another control.
   The following example shows the cyclic data exchange with another control.
   Two data arrays (arrays of word) have to be defined.
   Additionally, one instance of each the function blocks IL_ModbusTCPClient
   and IL_ModbusTCPReadWriteMultipleRegisters are required.

      // IP address of ModbusTCP server
      strServerIP: STRING := '192.168.42.10';

      // Data arrays
      arOutData: ARRAY[100..199] OF WORD;
      arInData: ARRAY[500..599] OF WORD;

     // Function blocks
     fbModBusTCPClient: IL_ModBusTCPClient;
     fbModBusTCPReadWriteRegisters:
   IL_ModBusTCPReadWriteMultipleRegisters;

The IL_ModbusTCPClient function block establishes the connection to the
ModbusTCP server.
It does not yet exchange data. Data is exchanged by other client function
blocks connected to an instance of the IL_ModbusTCPClient function block
via the “ModbusLink”.

fbModBusTCPClient(Enable:=TRUE, Address:=strServerIP);

fbModBusTCPReadWriteRegisters(
   Enable := fbModBusTCPClient.InOperation,
   FirstReadRegister := 100,
   ReadQuantity := 100,
   ReadDataAddr := ADR(arInData),
   SizeOfReadData := SIZEOF(arInData),
   FirstWriteRegister := 500,
   WriteQuantity := 100,
   WriteDataAddr := ADR(arOutData),
   SizeOfWriteData := SIZEOF(arOutData)
);

This simplified example program establishes a ModbusTCP connection to a
ModbusTCP server specified in strServerIP.
The holding registers 100 to 199 are subsequently read cyclically and the
holding registers 500 to 599 are written. This example does not contain any
troubleshooting.

### 17.3.2 IL_ModbusTCPClient

Brief description
A Modbus TCP master is implemented in the IL_ModbusTCPClient function
block.
It is used to establish a connection to the ModbusTCP server.
The actual ModbusTCP queries are implemented by other function blocks.

Table 337: Library assignment of the IL_ModbusTCPClient
Library/folder
CXA_ModbusTCP/Client

Interface description

Table 338: Interface variables of the IL_ModbusTCPClient function block
                   Name                  Type         Description
VAR_INPUT          Enable                BOOL         Function block processing enabled (level-
                                                      controlled).
                   Address               STRING       IP address to be connected to.

Name                  Type          Description
Port                  UINT          TCP port of the Modbus TCP server.
VAR OUTPUT        InOperation           BOOL          The Modbus server runs and accepts
                                 incoming connections.
Error                 BOOL          Error while processing the function block.
ErrorID               ⮫ ERROR_CODE If the "Error" output is set, it contains a
                                 broad error classification.
ErrorIdent            ⮫ ERROR_STRUC If the "Error" output is set, this output
                   T             contains detailed error information
ModbusLink            IL_MODBUS_LIN Handle on the existing Modbus connec‐
                   K             tion is required by the client function

                                 blocks
Table 339: Input behavior IL_ModbusTCPClient
Name                 Type           Min. value     Max. value    Default value Applied
Enable               BOOL                                        FALSE         Continuous
Address              STRING                                      ''            Rising edge at
                                                                               "Enable"
Port                 UINT           0              65535         502           Rising edge at
                                                                               "Enable"
UnitID               USINT          0              255           255           Rising edge at
                                                                               "Enable"

Functional description
A Modbus TCP master is implemented in the IL_ModbusTCPClient function
block.
It is used to establish a connection to the ModbusTCP server.
The actual ModbusTCP queries are implemented by other function blocks.

Enable, InOperation
At a rising edge at “Enable”, the function block establishes a connection to
the ModbusTCP server specified in “Address” and “Port”. When the connec‐
tion is set up successfully, the “InOperation” output is set. The "ModbusLink"
output can then be used as input for the ModbusTCP client function blocks.
The connection to the ModbusTCP server is closed at a falling edge at Enable.

Error, ErrorID, ErrorIdent
If an error occurs while processing the function block, the output "Error" is
set. "ErrorID" and "ErrorIdent" contain detailed error information. Function
block processing is paused. The "Error" output is reset at a falling edge at
"Enable”.
The error outputs are only set if errors occur while processing the function
block. Errors caused by the Modbus TCP protocol do not generate any output
at the error outputs. These are reported by the ModbusTCP client function
blocks.

Port
Modbus TCP normally uses port 502. If the ModbusTCP server runs on
another TCP port, the port number to be used can be written to the "Port"
input.

Supported Modbus function codes
Function codes are used by the Modbus master to access the Modbus slave.

Knowledge about the codes supported helps to find the errors. It is not
required for the normal operating mode though.
The following function codes are supported by the Modbus TCP client func‐
tion blocks:
Table 340: Supported Modbus function codes
Function code Function block            Description
1             ⮫ Chapter 17.3.3          Reads a number of bits from "BitData" starting from
              IL_ModbusTCPReadCoils     the initial address
              on page 415
2             ⮫ Chapter 17.3.4 IL_Mod‐  Reads a number of bits from "BitData" starting from
              busTCPReadDiscreteInputs the initial address
              on page 417
3             ⮫ Chapter                 Reads a number of registers from "RegisterData"
              17.3.5 IL_ModbusTC‐       starting from the initial address
              PReadHoldingRegisters
              on page 420
4             ⮫ Chapter 17.3.6 IL_Mod‐  Reads a number of registers from "RegisterData"
              busTCPReadInputRegisters starting from the initial address
              on page 422
5             ⮫ Chapter 17.3.7 IL_Mod‐  Writes a bit into "BitData" starting from the initial
              BusTCPWriteSingleCoil     address
              on page 425
6             ⮫ Chapter 17.3.8 IL_Mod‐  Writes a register into "RegisterData" starting from the
              BusTCPWriteSingleRegister initial address
              on page 427
15            ⮫ Chapter 17.3.9 IL_Mod‐  Writes a number of bits into "BitData" starting from
              BusTCPWriteMultipleCoils  the initial address
              on page 429
16            ⮫ Chapter                 Writes a number of registers into "RegisterData"
              17.3.10 IL_ModbusTCP‐     starting from an initial address
              WriteMultipleRegisters
              on page 431
23            ⮫ Chapter                 Executes a combined read/write operation on "Regis‐
              17.3.11 IL_ModBusTCPRead‐ terData"
              WriteMultipleRegisters
              on page 434
43/14         ⮫ Chapter                 Reads the default device information of the Modbus
              17.3.12 IL_ModbusTC‐      TCP server
              PReadDeviceIdentification
              on page 437

  Troubleshooting
  The function block uses the error table CXA_TABLE, 16#0001.
  It can generate the following error messages in Additional1 and Additional2:
Table 341: Error codes of the IL_ModbusTCPClient
ErrorID             Additional1 Additional2 Description
INPUT_INVALID_ERROR 16#0A0F011 16#0C23020 The "Address" input is invalid.
                    1           8
INPUT_INVALID_ERROR 16#0A0F011 16#0C23020 The protocol is not supported.
                    1           4
OTHER_ERROR         16#0A0F011 16#0C23181 Could not open socket
                    1           0

ErrorID                      Additional1 Additional2 Description
OTHER_ERROR                  16#0A0F011 16#0C23020 Remote host denied connection setup - No
           1           9           ModBusTCP server is running there
OTHER_ERROR                  16#0A0F011 16#0C23020 The device does not respond.
           1           A
OTHER_ERROR                  16#0A0F011 16#0C23020 Remote host not found.
           1           B
OTHER_ERROR                  16#0A0F011 16#0C23020 No route to remote host.
           1           C
COMMUNICA‐                   16#0A0F011 16#0C23020 The connection was closed.
TION_ERROR                   1           E

COMMUNICA‐                   16#0A0F011 16#0C23021 Remote host closed the connection.
TION_ERROR                   1           1

### 17.3.3 IL_ModbusTCPReadCoils

   Brief description
   The IL_ModbusTCPReadCoils function block cyclically reads multiple coils
   from a ModbusTCP server.
   Thus, a connection managed by the IL_ModbusTCPClient function block is
   required.

   Table 342: Library assignment of the IL_ModbusTCPReadCoils
   Library/folder
   CXA_ModbusTCP/Client

   Interface description

Table 343: Interface variables of the IL_ModbusTCPReadCoils function block
                  Name                   Type           Description
VAR_INPUT         Enable                 BOOL           Function block processing enabled (level-
                                                        controlled).
                  FirstCoil              UINT           First coil to be read from
                  Quantity               UINT           Number of coils to be read
                  DataAddr               POINTER TO     Address of the data range the coils are to
                                         BOOL           be copied to
                  SizeOfData             UINT           Size of the data range created in "Data‐
                                                        Addr" in bytes
                  UnitID                 USINT          Unit ID or slave ID of the client
VAR_OUTPUT        Done                   BOOL           One transfer cycle is completed. Received
                                                        data was transferred to the range created
                                                        in "DataAddr"
                  Active                 BOOL           Transfer running

Name                 Type          Description
Error                BOOL          Error while processing the function block.
ErrorID              ⮫ ERROR_CODE If the "Error" output is set, it contains a
                                 broad error classification.
ErrorIdent           ⮫ ERROR_STRUC If the "Error" output is set, this output
                   T             contains detailed error information
VAR_IN_OUT         ModbusLink           IL_MODBUS_LIN Link to existing Modbus connection is pro‐
                   K             vided by the IL_ModbusTCPClient function
                                 block
Table 344: Input behavior IL_ModbusTCPClient
Name                 Type           Min. value     Max. value     Default value Applied
Enable               BOOL                                         FALSE         Continuous
FirstCoil            UINT           0              65535          0             Rising edge at
                                                                                "Enable"
Quantity             UINT           1              2000           0             Rising edge at
                                                                                "Enable"
DataAddr             POINTER TO     0                             0             Rising edge at
                     BOOL                                                       "Enable"
SizeOfData           UINT           1              2000           0             Rising edge at
                                                                                "Enable"
UnitID               USINT          0              255            255           Rising edge at
                                                                                "Enable"

Functional description
The IL_ModbusTCPReadCoils function block implements the Modbus function
code 1.
It cyclically reads multiple coils from a ModbusTCP server.
Thus, a connection managed by the IL_ModbusTCPClient function block is
required.

Enable, Done
The function block checks its inputs at a rising edge at "Enable". Subse‐
quently, it cyclically sends a request to the Modbus server via the IL_Mod‐
busTCPClient specified at "ModbusLink" and waits for response. After a suc‐
cessful transfer cycle, "Done" is set for one PLC cycle. The function block
is disabled at a falling edge at "Enable”. If it is still transferred, processing
continues using the IL_ModbusTCPClient function block and the result is dis‐
carded.

Error, ErrorID, ErrorIdent
If an error occurs while processing the function block, the output "Error" is
set. "ErrorID" and "ErrorIdent" contain detailed error information. Function
block processing is paused. The "Error" output is reset at a falling edge at
"Enable”.
The error outputs are set if errors occur at the function block inputs and in
the ModbusTCP protocol.

FirstCoil, Quantity
Modbus provides 65536 readable and writable coils. Each coil can either be
set or deleted. The "FirstCoil" input specifies the first coil to be read. From
this coil, "Quantity" coils are read. Up to 2000 coils can be read per call.

 DataAddr, SizeOfData
 The received data is stored in the data range specified in "DataAddr". An
 array of Bool is expected as reception buffer. The array size specified in
 "SizeOfData" has to be at least equal to the number of coils to be read. It
 is recommended to use the SIZEOF() operator to determine the array size.

 UnitID
 The unit ID of the ModbusTCP protocol corresponds to the slave ID of the
 Modbus RTU. It is used to differ between different clients on the bus or to
 access different address ranges.

 ModBusLink
 The "ModbusLink" input references the actual ModbusTCP connection. It is
 output by the IL_ModbusTCPClient function block and valid when the connec‐
 tion is set up.

 Troubleshooting
The function block uses the error table CXA_TABLE, 16#00000170.
It can generate the following error messages in Additional1 and Additional2:
Table 345: Error codes of the IL_ModbusTCPReadCoils
ErrorID             Additional1 Additional2 Description
RESOURCE_ERROR      16#0000181 16#0000000 The link specified at the "ModbusLink" input
                    0           0           is invalid.
INPUT_INVALID_ERROR 16#0000181 16#0000000 The address specified at the "DataAddr" input
                    1           0           is 0.
INPUT_INVALID_ERROR 16#0000181 16#0000000 The "SizeOfData” input is 0
                    2           0
INPUT_INVALID_ERROR 16#0000181 16#0000000 The "Quantity” input is 0
                    3           0
INPUT_RANGE_ERROR 16#0000181 16#0000000 The "Quantity" input is higher than 2000
                    4           0
INPUT_INVALID_ERROR 16#0000181 16#0000000 The value at the "Quantity" input is higher
                    5           0           than "SizeOfData"
RESOURCE_ERROR      16#0000181 Modbus       The Modbus operation returns an error code
                    7           error code

### 17.3.4 IL_ModbusTCPReadDiscreteInputs

 Brief description
 The IL_ModbusTCPReadDiscreteInputs function block cyclically reads multiple
 discrete inputs from a ModbusTCP server.
 Thus, a connection managed by the IL_ModbusTCPClient function block is
 required.

 Table 346: Library assignment of the IL_ModbusTCPReadDiscreteInputs
 Library/folder
 CXA_ModbusTCP/Client

  Interface description

Table 347: Interface variables of the IL_ModbusTCPReadDiscreteInputs function block
                   Name                Type          Description
VAR_INPUT          Enable              BOOL          Function block processing enabled (level-
                                                     controlled).
                   FirstCoil           UINT          First discrete input to be read from
                   Quantity            UINT          Number of inputs to be read
                   DataAddr            POINTER TO    Address of the data range to copy the
                                       BOOL          inputs to
                   SizeOfData          UINT          Size of the data range created in "Data‐
                                                     Addr" in bytes
                   UnitID              USINT         Unit ID or slave ID of the client
VAR_OUTPUT         Done                BOOL          One transfer cycle is completed. Received
                                                     data was transferred to the range created
                                                     in "DataAddr"
                   Error               BOOL          Error while processing the function block
                   ErrorID             ⮫ ERROR_CODE If the "Error" output is set, it contains a
                                                     broad error classification
                   ErrorIdent          ⮫ ERROR_STRUC If the "Error" output is set, this output
                                       T             contains detailed error information
VAR_IN_OUT         ModbusLink          IL_MODBUS_LIN Link to existing Modbus connection is pro‐
                                       K             vided by the IL_ModbusTCPClient function
                                                     block
Table 348: Input behavior of the IL_ModbusTCPReadDiscreteInputs
Name                 Type          Min. value     Max. value    Default value Applied
Enable               BOOL                                       FALSE         Continuous
FirstInput           UINT          0              65535         0             Rising edge at
                                                                              "Enable"
Quantity             UINT          1              2000          0             Rising edge at
                                                                              "Enable"
DataAddr             POINTER TO    0                            0             Rising edge at
                     BOOL                                                     "Enable"
SizeOfData           UINT          1              2000          0             Rising edge at
                                                                              "Enable"
UnitID               USINT         0              255           255           Rising edge at
                                                                              "Enable"

Functional description
The IL_ModbusTCPReadDiscreteInputs function block implements the
Modbus function code 2.
It cyclically reads multiple discrete inputs from a ModbusTCP server.
Thus, a connection managed by the IL_ModbusTCPClient function block is
required.

Enable, Done
The function block checks its inputs at a rising edge at "Enable". Subse‐
quently, it cyclically sends a request to the Modbus server via the IL_Mod‐
busTCPClient specified at "ModbusLink" and waits for response. After a suc‐

cessful transfer cycle, "Done" is set for one PLC cycle. The function block
is disabled at a falling edge at "Enable”. If it is still transferred, processing
continues using the IL_ModbusTCPClient function block and the result is dis‐
carded.

Error, ErrorID, ErrorIdent
If an error occurs while processing the function block, the output "Error" is
set. "ErrorID" and "ErrorIdent" contain detailed error information. Function
block processing is paused. The "Error" output is reset at a falling edge at
"Enable”.
The error outputs are set if errors occur at the function block inputs and in
the ModbusTCP protocol.

FirstInput, Quantity
Modbus provides 65536 read-only discrete inputs. Each input can either be
set or deleted. The "FirstInput" input specifies the first input to be read. From
this input, "Quantity" inputs are read. Up to 2000 inputs can be read per call.

DataAddr, SizeOfData
The received data is stored in the data range specified in "DataAddr". An
array of Bool is expected as reception buffer. The array size specified in
"SizeOfData" has to be at least equal to the number of inputs to be read.
It is recommended to use the SIZEOF() operator to determine the array size.

UnitID
The unit ID of the ModbusTCP protocol corresponds to the slave ID of the
Modbus RTU. It is used to differ between different clients on the bus or to
access different address ranges.

ModBusLink
The "ModbusLink" input references the actual ModbusTCP connection. It is
output by the IL_ModbusTCPClient function block and valid when the connec‐
tion is set up.

Troubleshooting
The function block uses the error table CXA_TABLE, 16#00000170.
It can generate the following error messages in Additional1 and Additional2:
Table 349: Error codes of the IL_ModbusTCPReadDiscreteInputs
ErrorID                      Additional1 Additional2 Description
RESOURCE_ERROR               16#0000181 16#0000000 The link specified at the "ModbusLink" input
                             0           0           is invalid.

ErrorID             Additional1 Additional2 Description
INPUT_INVALID_ERROR 16#0000181 16#0000000 The address specified at the "DataAddr" input
 1           0           is 0.
INPUT_INVALID_ERROR 16#0000181 16#0000000 The "SizeOfData” input is 0
 2           0
INPUT_INVALID_ERROR 16#0000181 16#0000000 The "Quantity” input is 0
 3           0
INPUT_RANGE_ERROR 16#0000181 16#0000000 The "Quantity" input is higher than 2000
 4           0
INPUT_INVALID_ERROR 16#0000181 16#0000000 The value at the "Quantity" input is higher
 5           0           than "SizeOfData"
RESOURCE_ERROR      16#0000181 Modbus       The Modbus operation returns an error code
 7           error code

### 17.3.5 IL_ModbusTCPReadHoldingRegisters

  Brief description
  The IL_ModbusTCPReadHoldingRegisters function block cyclically reads mul‐
  tiple holding registers from a ModbusTCP server.
  Thus, a connection managed by the IL_ModbusTCPClient function block is
  required.

  Table 350: Library assignment of the IL_ModbusTCPReadHoldingRegisters
  Library/folder
  CXA_ModbusTCP/Client

  Interface description

Table 351: Interface variables of the IL_ModbusTCPReadHoldingRegisters function block
                   Name                  Type         Description
VAR_INPUT          Enable                BOOL         Function block processing enabled (level-
                                                      controlled).
                   FirstRegister         UINT         First register to be read from
                   Quantity              UINT         Number of registers to be read
                   DataAddr              POINTER TO   Address of the data range to copy the reg‐
                                         WORD         isters to
                   SizeOfData            UINT         Size of the data range created in "Data‐
                                                      Addr" in bytes
                   UnitID                USINT        Unit ID or slave ID of the client

Name                  Type          Description
VAR_OUTPUT        Done                  BOOL          One transfer cycle is completed. Received
                                 data was transferred to the range created
                                 in "DataAddr"
Error                 BOOL          Error while processing the function block.
ErrorID               ⮫ ERROR_CODE If the "Error" output is set, it contains a
                                 broad error classification.
ErrorIdent            ⮫ ERROR_STRUC If the "Error" output is set, this output
                   T             contains detailed error information
VAR_IN_OUT        ModbusLink            IL_MODBUS_LIN Link to existing Modbus connection is pro‐
                   K             vided by the IL_ModbusTCPClient function

                                 block
Table 352: Input behavior of the IL_ModbusTCPReadHoldingRegisters
Name                 Type           Min. value     Max. value     Default value Applied
Enable               BOOL                                         FALSE         Continuous
FirstRegister        UINT           0              65535          0             Rising edge at
                                                                                "Enable"
Quantity             UINT           1              125            0             Rising edge at
                                                                                "Enable"
DataAddr             POINTER TO     0                             0             Rising edge at
                     WORD                                                       "Enable"
SizeOfData           UINT           2              250            0             Rising edge at
                                                                                "Enable"
UnitID               USINT          0              255            255           Rising edge at
                                                                                "Enable"

Functional description
The IL_ModbusTCPReadHoldingRegisters function block implements the
Modbus function code 3. It cyclically reads multiple holding registers from a
ModbusTCP server. Thus, a connection managed by the IL_ModbusTCPClient
function block is required.

Enable, Done
The function block checks its inputs at a rising edge at "Enable". Subse‐
quently, it cyclically sends a request to the Modbus server via the IL_Mod‐
busTCPClient specified at "ModbusLink" and waits for response. After a suc‐
cessful transfer cycle, "Done" is set for one PLC cycle. The function block
is disabled at a falling edge at "Enable”. If it is still transferred, processing
continues using the IL_ModbusTCPClient function block and the result is dis‐
carded.

Error, ErrorID, ErrorIdent
If an error occurs while processing the function block, the output "Error" is
set. "ErrorID" and "ErrorIdent" contain detailed error information. Function
block processing is paused. The "Error" output is reset at a falling edge at
"Enable”.
The error outputs are set if errors occur at the function block inputs and in
the ModbusTCP protocol.

 FirstRegister, Quantity
 Modbus provides 65536 readable and writable holding registers. Each register
 has a width of one word (2 bytes). It can assume a value between 0 and
 65535. The "FirstRegister" input specifies the first register to be read. From
 this register, "Quantity" registers are read. Up to 125 registers can be read per
 call.

 DataAddr, SizeOfData
 The received data is stored in the data range specified in "DataAddr". An
 array of Word is expected as reception buffer. The array size specified in
 "SizeOfData" has to be at least double the number of registers to be read. It is
 recommended to use the SIZEOF() operator to determine the array size.

 UnitID
 The unit ID of the ModbusTCP protocol corresponds to the slave ID of the
 Modbus RTU. It is used to differ between different clients on the bus or to
 access different address ranges.

 ModBusLink
 The "ModbusLink" input references the actual ModbusTCP connection. It is
 output by the IL_ModbusTCPClient function block and valid when the connec‐
 tion is set up.

 Troubleshooting
The function block uses the error table CXA_TABLE, 16#00000170.
It can generate the following error messages in Additional1 and Additional2:
Table 353: Error codes of the IL_ModbusTCPReadHoldingRegisters
ErrorID             Additional1 Additional2 Description
RESOURCE_ERROR      16#0000181 16#0000000 The link specified at the "ModbusLink" input
                    0           0           is invalid.
INPUT_INVALID_ERROR 16#0000181 16#0000000 The address specified at the "DataAddr" input
                    1           0           is 0.
INPUT_INVALID_ERROR 16#0000181 16#0000000 The "SizeOfData” input is 0
                    2           0
INPUT_INVALID_ERROR 16#0000181 16#0000000 The "Quantity” input is 0
                    3           0
INPUT_RANGE_ERROR 16#0000181 16#0000000 The "Quantity" input is higher than 125
                    4           1
INPUT_INVALID_ERROR 16#0000181 16#0000000 The value at the "Quantity"*2 input is higher
                    6           0           than "SizeOfData"
RESOURCE_ERROR      16#0000181 Modbus       The Modbus operation returns an error code
                    7           error code

### 17.3.6 IL_ModbusTCPReadInputRegisters

 Brief description
 The IL_ModbusTCPReadInputRegisters function block cyclically reads multiple
 input registers from a ModbusTCP server. Thus, a connection managed by the
 IL_ModbusTCPClient function block is required.

 Table 354: Library assignment of the IL_ModbusTCPReadInputRegisters
 Library/folder
 CXA_ModbusTCP/Client

   Interface description

Table 355: Interface variables of the IL_ModbusTCPReadInputRegisters function block
                  Name                 Type          Description
VAR_INPUT         Enable               BOOL          Function block processing enabled (level-
                                                     controlled).
                  FirstRegister        UINT          First register to be read from
                  Quantity             UINT          Number of registers to be read
                  DataAddr             POINTER TO    Address of the data range to copy the reg‐
                                       WORD          isters to
                  SizeOfData           UINT          Size of the data range created in "Data‐
                                                     Addr" in bytes
                  UnitID               USINT         Unit ID or slave ID of the client
VAR_OUTPUT        Done                 BOOL          One transfer cycle is completed. Received
                                                     data was transferred to the range created
                                                     in "DataAddr"
                  Error                BOOL          Error while processing the function block.
                  ErrorID              ⮫ ERROR_CODE If the "Error" output is set, it contains a
                                                     broad error classification.
                  ErrorIdent           ⮫ ERROR_STRUC If the "Error" output is set, this output
                                       T             contains detailed error information
VAR_IN_OUT        ModbusLink           IL_MODBUS_LIN Link to existing Modbus connection is pro‐
                                       K             vided by the IL_ModbusTCPClient function
                                                     block
Table 356: Input behavior of the IL_ModbusTCPReadInputRegisters
Name                 Type          Min. value     Max. value   Default value Applied
Enable               BOOL                                      FALSE         Continuous
FirstRegister        UINT          0              65535        0             Rising edge at
                                                                             "Enable"
Quantity             UINT          1              125          0             Rising edge at
                                                                             "Enable"
DataAddr             POINTER TO    0                           0             Rising edge at
                     WORD                                                    "Enable"
SizeOfData           UINT          2              250          0             Rising edge at
                                                                             "Enable"
UnitID               USINT         0              255          255           Rising edge at
                                                                             "Enable"

Functional description
The IL_ModbusTCPReadInputRegisters function block implements the
Modbus function code 4. It cyclically reads multiple input registers from a
ModbusTCP server. Thus, a connection managed by the IL_ModbusTCPClient
function block is required.

Enable, Done
The function block checks its inputs at a rising edge at "Enable". Subse‐
quently, it cyclically sends a request to the Modbus server via the IL_Mod‐
busTCPClient specified at "ModbusLink" and waits for response. After a suc‐
cessful transfer cycle, "Done" is set for one PLC cycle. The function block
is disabled at a falling edge at "Enable”. If it is still transferred, processing
continues using the IL_ModbusTCPClient function block and the result is dis‐
carded.

Error, ErrorID, ErrorIdent
If an error occurs while processing the function block, the output "Error" is
set. "ErrorID" and "ErrorIdent" contain detailed error information. Function
block processing is paused. The "Error" output is reset at a falling edge at
"Enable”.
The error outputs are set if errors occur at the function block inputs and in
the ModbusTCP protocol.

FirstRegister, Quantity
Modbus provides 65536 read-only input registers. Each register has a width
of one word (2 bytes). It can assume a value between 0 and 65535. The
"FirstRegister" input specifies the first register to be read. From this register,
"Quantity" registers are read. Up to 125 registers can be read per call.

DataAddr, SizeOfData
The received data is stored in the data range specified in "DataAddr". An
array of Word is expected as reception buffer. The array size specified in
"SizeOfData" has to be at least double the number of registers to be read. It is
recommended to use the SIZEOF() operator to determine the array size.

UnitID
The unit ID of the ModbusTCP protocol corresponds to the slave ID of the
Modbus RTU. It is used to differ between different clients on the bus or to
access different address ranges.

ModBusLink
The "ModbusLink" input references the actual ModbusTCP connection. It is
output by the IL_ModbusTCPClient function block and valid when the connec‐
tion is set up.

Troubleshooting
The function block uses the error table CXA_TABLE, 16#00000170.
It can generate the following error messages in Additional1 and Additional2:
Table 357: Error codes of the IL_ModbusTCPReadInputRegisters
ErrorID                   Additional1 Additional2 Description
RESOURCE_ERROR            16#0000181 16#0000000 The link specified at the "ModbusLink" input
                          0           0           is invalid.

ErrorID             Additional1 Additional2 Description
INPUT_INVALID_ERROR 16#0000181 16#0000000 The address specified at the "DataAddr" input
  1           0           is 0.
INPUT_INVALID_ERROR 16#0000181 16#0000000 The "SizeOfData” input is 0
  2           0
INPUT_INVALID_ERROR 16#0000181 16#0000000 The "Quantity” input is 0
  3           0
INPUT_RANGE_ERROR 16#0000181 16#0000000 The "Quantity" input is higher than 125
  4           1
INPUT_INVALID_ERROR 16#0000181 16#0000000 The value at the "Quantity"*2 input is higher
  6           0           than "SizeOfData"

RESOURCE_ERROR      16#0000181 Modbus       The Modbus operation returns an error code
  7           error code

### 17.3.7 IL_ModBusTCPWriteSingleCoil

   Brief description
   The IL_ModBusTCPWriteSingleCoil function block writes a coil once to a Mod‐
   busTCP server.
   Thus, a connection managed by the IL_ModbusTCPClient function block is
   required.

   Table 358: Library assignment of the IL_ModBusTCPWriteSingleCoil
   Library/folder
   CXA_ModbusTCP/Client

   Interface description

Table 359: Interface variables of the IL_ModBusTCPWriteMultipleCoils function block
                  Name                   Type          Description
VAR_INPUT         Execute                BOOL          Processing the function block enabled
                                                       (edge-controlled).
                  Coil                   UINT          Coil to be written
                  Value                  BOOL          Value to be written
                  UnitID                 USINT         Unit ID or slave ID of the client
VAR_OUTPUT        Done                   BOOL          One transfer cycle is completed.
                  Error                  BOOL          Error while processing the function block.
                  ErrorID                ⮫ ERROR_CODE If the "Error" output is set, it contains a
                                                       broad error classification.
                  ErrorIdent             ⮫ ERROR_STRUC If the "Error" output is set, this output
                                         T             contains detailed error information

Name                  Type          Description
VAR_IN_OUT         ModbusLink            IL_MODBUS_LIN Link to existing Modbus connection is pro‐
                    K             vided by the IL_ModbusTCPClient function
                                  block
Table 360: Input behavior of the IL_ModBusTCPWriteSingleCoil
Name                 Type            Min. value    Max. value     Default value Applied
Execute              BOOL                                         FALSE         Continuous
Coil                 UINT            0             65535          0             Rising edge at
                                                                                "Execute"
Value                BOOL                                         FALSE         Rising edge at
                                                                                "Execute"
UnitID               USINT           0             255            255           Rising edge at
                                                                                "Execute"

Functional description
The IL_ModBusTCPWriteSingleCoil function block implements the Modbus
function code 5. It writes a coil once to the ModbusTCP server. Thus, a con‐
nection managed by the IL_ModbusTCPClient function block is required.

Execute, Done
The function block checks its inputs at a rising edge at "Execute". Subse‐
quently, it sends once a request to the Modbus server via the IL_ModbusTCP‐
Client specified at "ModbusLink" and waits for response. After a successful
transfer cycle, "Done” is set. The function block continues running at a falling
edge at "Execute" until the current transfer is completed. "Done" is then set
for one PLC cycle.

Error, ErrorID, ErrorIdent
If an error occurs while processing the function block, the output "Error" is
set. "ErrorID" and "ErrorIdent" contain detailed error information. Function
block processing is paused. The "Error" output is reset at a falling edge at
"Enable”.
The error outputs are set if errors occur at the function block inputs and in
the ModbusTCP protocol.

Coil, Value
Modbus provides 65536 readable and writable coils. Each coil can either be
set or deleted. The "Coil" input specifies the coil to be written. The value in
"Value" is written to this coil.

UnitID
The unit ID of the ModbusTCP protocol corresponds to the slave ID of the
Modbus RTU. It is used to differ between different clients on the bus or to
access different address ranges.

ModBusLink
The "ModbusLink" input references the actual ModbusTCP connection. It is
output by the IL_ModbusTCPClient function block and valid when the connec‐
tion is set up.

Troubleshooting
The function block uses the error table CXA_TABLE, 16#00000170.

  It can generate the following error messages in Additional1 and Additional2:
Table 361: Error codes of the IL_ModBusTCPWriteSingleCoil
ErrorID                      Additional1 Additional2 Description
RESOURCE_ERROR               16#0000181 16#0000000 The link specified at the "ModbusLink" input
                             0           0           is invalid.
RESOURCE_ERROR               16#0000181 Modbus       The Modbus operation returns an error code
                             7           error code

### 17.3.8 IL_ModBusTCPWriteSingleRegister

   Brief description

   The IL_ModBusTCPWriteSingleRegister function block writes a holding register
   once to a ModbusTCP server.
   Thus, a connection managed by the IL_ModbusTCPClient function block is
   required.

   Table 362: Library assignment of the IL_ModBusTCPWriteSingleRegister
   Library/folder
   CXA_ModbusTCP/Client

   Interface description

Table 363: Interface variables of the IL_ModBusTCPWriteSingleRegister function block
                  Name                    Type          Description
VAR_INPUT         Execute                 BOOL          Processing the function block enabled
                                                        (edge-controlled).
                  Register                UINT          Register to be written
                  Value                   WORD          Value to be written
                  UnitID                  USINT         Unit ID or slave ID of the client
VAR_OUTPUT        Done                    BOOL          One transfer cycle is completed.
                  Error                   BOOL          Error while processing the function block.
                  ErrorID                 ⮫ ERROR_CODE If the "Error" output is set, it contains a
                                                        broad error classification
                  ErrorIdent              ⮫ ERROR_STRUC If the "Error" output is set, this output
                                          T             contains detailed error information
VAR_IN_OUT        ModbusLink              IL_MODBUS_LIN Link to existing Modbus connection is pro‐
                                          K             vided by the IL_ModbusTCPClient function
                                                        block
Table 364: Input behavior of the IL_ModBusTCPWriteSingleRegister
Name                 Type             Min. value     Max. value    Default value Applied
Execute              BOOL                                          FALSE         Continuous
HoldingRegister      UINT             0              65535         0             Rising edge at
                                                                                 "Execute"

Name                 Type            Min. value   Max. value      Default value Applied
Value                WORD            0            65535           0             Rising edge at
                                                           "Execute"
UnitID               USINT           0            255             255           Rising edge at
                                                           "Execute"

Functional description
The IL_ModBusTCPWriteSingleRegister function block implements the
Modbus function code 6. It reads and writes one holding register to a Mod‐
busTCP server. Thus, a connection managed by the IL_ModbusTCPClient func‐
tion block is required.

Execute, Done
The function block checks its inputs at a rising edge at "Execute". Subse‐
quently, it sends once a request to the Modbus server via the IL_ModbusTCP‐
Client specified at "ModbusLink" and waits for response. After a successful
transfer cycle, "Done” is set. The function block continues running at a falling
edge at "Execute" until the current transfer is completed. "Done" is then set
for one PLC cycle.

Error, ErrorID, ErrorIdent
If an error occurs while processing the function block, the output "Error" is
set. "ErrorID" and "ErrorIdent" contain detailed error information. Function
block processing is paused. The "Error" output is reset at a falling edge at
"Enable”.
The error outputs are set if errors occur at the function block inputs and in
the ModbusTCP protocol.

Register, Value
Modbus provides 65536 readable and writable holding registers. Each register
has a width of one word (2 bytes). It can assume a value between 0 and
65535. The "Register" input specifies the register to be written. The value at
the "Value" input is written to this register.

UnitID
The unit ID of the ModbusTCP protocol corresponds to the slave ID of the
Modbus RTU. It is used to differ between different clients on the bus or to
access different address ranges.

ModBusLink
The "ModbusLink" input references the actual ModbusTCP connection. It is
output by the IL_ModbusTCPClient function block and valid when the connec‐
tion is set up.

Troubleshooting
The function block uses the error table CXA_TABLE, 16#00000170.
It can generate the following error messages in Additional1 and Additional2:
Table 365: Error codes of the IL_ModBusTCPWriteSingleRegister
ErrorID                   Additional1 Additional2 Description
RESOURCE_ERROR            16#0000181 16#0000000 The link specified at the "ModbusLink" input
                          0           0           is invalid.
RESOURCE_ERROR            16#0000181 Modbus       The Modbus operation returns an error code
                          7           error code

### 17.3.9 IL_ModBusTCPWriteMultipleCoils

   Brief description
   The IL_ModBusTCPWriteMultipleCoils function block writes multiple coils
   once to a ModbusTCP server.
   Thus, a connection managed by the IL_ModbusTCPClient function block is
   required.

   Table 366: Library assignment of the IL_ModBusTCPWriteMultipleCoils
   Library/folder
   CXA_ModbusTCP/Client

   Interface description

Table 367: Interface variables of the IL_ModBusTCPWriteMultipleCoils function block
                  Name                   Type          Description
VAR_INPUT         Execute                BOOL          Processing the function block enabled
                                                       (edge-controlled).
                  FirstCoil              UINT          First coil to be written from
                  Quantity               UINT          Number of coils to be written
                  DataAddr               POINTER TO    Address of the data range the coils are to
                                         BOOL          be read from
                  SizeOfData             UINT          Size of the data range created in "Data‐
                                                       Addr" in bytes
                  UnitID                 USINT         Unit ID or slave ID of the client
VAR_OUTPUT        Done                   BOOL          One transfer cycle is completed.
                  Error                  BOOL          Error while processing the function block.
                  ErrorID                ⮫ ERROR_CODE If the "Error" output is set, it contains a
                                                       broad error classification.
                  ErrorIdent             ⮫ ERROR_STRUC If the "Error" output is set, this output
                                         T             contains detailed error information
VAR_IN_OUT        ModbusLink             IL_MODBUS_LIN Link to existing Modbus connection is pro‐
                                         K             vided by the IL_ModbusTCPClient function
                                                       block
Table 368: Input behavior of the IL_ModBusTCPWriteMultipleCoils
Name                 Type          Min. value       Max. value    Default value Applied
Execute              BOOL                                         FALSE         Continuous
FirstCoil            UINT          0                65535         0             Rising edge at
                                                                                "Execute"

Name                 Type            Min. value    Max. value      Default value Applied
Quantity             UINT            1             2000            0             Rising edge at
                                                            "Execute"
DataAddr             POINTER TO      0                             0             Rising edge at
BOOL                                                        "Execute"
SizeOfData           UINT            1             2000            0             Rising edge at
                                                            "Execute"
UnitID               USINT           0             255             255           Rising edge at
                                                            "Execute"

Functional description
The IL_ModBusTCPWriteMultipleCoils function block implements the Modbus
function code 15.
It writes multiple coils once to the ModbusTCP server.
Thus, a connection managed by the IL_ModbusTCPClient function block is
required.

Execute, Done
The function block checks its inputs at a rising edge at "Execute". Subse‐
quently, it sends once a request to the Modbus server via the IL_ModbusTCP‐
Client specified at "ModbusLink" and waits for response. After a successful
transfer cycle, "Done” is set. The function block continues running at a falling
edge at "Execute" until the current transfer is completed. "Done" is then set
for one PLC cycle.

Error, ErrorID, ErrorIdent
If an error occurs while processing the function block, the output "Error" is
set. "ErrorID" and "ErrorIdent" contain detailed error information. Function
block processing is paused. The "Error" output is reset at a falling edge at
"Enable”.
The error outputs are set if errors occur at the function block inputs and in
the ModbusTCP protocol.

FirstCoil, Quantity
Modbus provides 65536 readable and writable coils. Each coil can either be
set or deleted. The "FirstCoil" input specifies the first coil to be written. From
this coil, "Quantity" coils are written. Up to 2000 coils can be written per call.

DataAddr, SizeOfData
The data to be transmitted is retrieved from the data range specified in "Data‐
Addr". An array of Bool is expected as transmission buffer. The array size
specified in "SizeOfData" has to be at least equal to the number of coils to
be written. It is recommended to use the SIZEOF() operator to determine the
array size.

UnitID
The unit ID of the ModbusTCP protocol corresponds to the slave ID of the
Modbus RTU. It is used to differ between different clients on the bus or to
access different address ranges.

 ModBusLink
 The "ModbusLink" input references the actual ModbusTCP connection. It is
 output by the IL_ModbusTCPClient function block and valid when the connec‐
 tion is set up.

 Troubleshooting
The function block uses the error table CXA_TABLE, 16#00000170.
It can generate the following error messages in Additional1 and Additional2:
Table 369: Error codes of the IL_ModBusTCPWriteMultipleCoils
ErrorID             Additional1 Additional2 Description

RESOURCE_ERROR      16#0000181 16#0000000 The link specified at the "ModbusLink" input
0           0           is invalid.
INPUT_INVALID_ERROR 16#0000181 16#0000000 The address specified at the "DataAddr" input
1           0           is 0.
INPUT_INVALID_ERROR 16#0000181 16#0000000 The "SizeOfData” input is 0
2           0
INPUT_INVALID_ERROR 16#0000181 16#0000000 The "Quantity” input is 0
3           0
INPUT_RANGE_ERROR 16#0000181 16#0000000 The "Quantity" input is higher than 2000
4           0
INPUT_INVALID_ERROR 16#0000181 16#0000000 The value at the "Quantity" input is higher
5           0           than "SizeOfData"
RESOURCE_ERROR      16#0000181 Modbus       The Modbus operation returns an error code
7           error code

### 17.3.10 IL_ModbusTCPWriteMultipleRegisters

 Brief description
 The IL_ModBusTCPWriteMultipleRegisters function block writes multiple
 holding registers once to a ModbusTCP server.
 Thus, a connection managed by the IL_ModbusTCPClient function block is
 required.

 Table 370: Library assignment of the IL_ModbusTCPWriteMultipleRegisters
 Library/folder
 CXA_ModbusTCP/Client

 Interface description

Table 371: Interface variables of the IL_ModBusTCPWriteMultipleRegisters function block
                   Name                  Type          Description
VAR_INPUT          Execute               BOOL          Processing the function block enabled
                                                       (edge-controlled).
                   FirstRegister         UINT          First register to be written from
                   Quantity              UINT          Number of registers to be written
                   DataAddr              POINTER TO    Address of the data range the registers are
                                         WORD          to be copied from
                   SizeOfData            UINT          Size of the data range created in "Data‐
                                                       Addr" in bytes
                   UnitID                USINT         Unit ID or slave ID of the client
VAR_OUTPUT         Done                  BOOL          One transfer cycle is completed.
                   Error                 BOOL          Error while processing the function block.
                   ErrorID               ⮫ ERROR_CODE If the "Error" output is set, it contains a
                                                       broad error classification.
                   ErrorIdent            ⮫ ERROR_STRUC If the "Error" output is set, this output
                                         T             contains detailed error information
VAR_IN_OUT         ModbusLink            IL_MODBUS_LIN Link to existing Modbus connection is pro‐
                                         K             vided by the IL_ModbusTCPClient function
                                                       block
Table 372: Input behavior of the IL_ModBusTCPWriteMultipleRegisters
Name                 Type            Min. value     Max. value    Default value Applied
Execute              BOOL                                         FALSE         Continuous
FirstRegister        UINT            0              65535         0             Rising edge at
                                                                                "Execute"
Quantity             UINT            1              125           0             Rising edge at
                                                                                "Execute"
DataAddr             POINTER TO      0                            0             Rising edge at
                     WORD                                                       "Execute"
SizeOfData           UINT            2              250           0             Rising edge at
                                                                                "Execute"
UnitID               USINT           0              255           255           Rising edge at
                                                                                "Execute"

  Functional description
  The IL_ModBusTCPWriteMultipleRegisters function block implements the
  Modbus function code 16. It reads and writes multiple holding registers to a
  ModbusTCP server. Thus, a connection managed by the IL_ModbusTCPClient
  function block is required.

  Execute, Done
  The function block checks its inputs at a rising edge at "Execute". Subse‐
  quently, it sends once a request to the Modbus server via the IL_ModbusTCP‐
  Client specified at "ModbusLink" and waits for response. After a successful
  transfer cycle, "Done” is set. The function block continues running at a falling
  edge at "Execute" until the current transfer is completed. "Done" is then set
  for one PLC cycle.

 Error, ErrorID, ErrorIdent
 If an error occurs while processing the function block, the output "Error" is
 set. "ErrorID" and "ErrorIdent" contain detailed error information. Function
 block processing is paused. The "Error" output is reset at a falling edge at
 "Enable”.
 The error outputs are set if errors occur at the function block inputs and in
 the ModbusTCP protocol.

 FirstRegister, Quantity
 Modbus provides 65536 readable and writable holding registers. Each register
 has a width of one word (2 bytes). It can assume a value between 0 and

 65535. The "FirstRegister" input specifies the first register to be written.
 From this register, "Quantity" registers are written. Up to 125 registers can
 be written per call.

 DataAddr, SizeOfData
 The data to be transmitted is retrieved from the data range specified in "Data‐
 Addr". An array of Word is expected as transmission buffer. The array size
 specified in "SizeOfData" has to be at least double the size of the number of
 registers to be written. It is recommended to use the SIZEOF() operator to
 determine the array size.

 UnitID
 The unit ID of the ModbusTCP protocol corresponds to the slave ID of the
 Modbus RTU. It is used to differ between different clients on the bus or to
 access different address ranges.

 ModBusLink
 The "ModbusLink" input references the actual ModbusTCP connection. It is
 output by the IL_ModbusTCPClient function block and valid when the connec‐
 tion is set up.

 Troubleshooting
The function block uses the error table CXA_TABLE, 16#00000170.
It can generate the following error messages in Additional1 and Additional2:
Table 373: Error codes of the IL_ModBusTCPWriteMultipleRegisters
ErrorID             Additional1 Additional2 Description
RESOURCE_ERROR      16#0000181 16#0000000 The link specified at the "ModbusLink" input
                    0           0           is invalid.
INPUT_INVALID_ERROR 16#0000181 16#0000000 The address specified at the "DataAddr" input
                    1           0           is 0.
INPUT_INVALID_ERROR 16#0000181 16#0000000 The "SizeOfData” input is 0
                    2           0
INPUT_INVALID_ERROR 16#0000181 16#0000000 The "Quantity” input is 0
                    3           0
INPUT_RANGE_ERROR 16#0000181 16#0000000 The "Quantity" input is higher than 125
                    4           1
INPUT_INVALID_ERROR 16#0000181 16#0000000 The value at the "Quantity"*2 input is higher
                    6           0           than "SizeOfData"
RESOURCE_ERROR      16#0000181 Modbus       The Modbus operation returns an error code
                    7           error code

### 17.3.11 IL_ModBusTCPReadWriteMultipleRegisters

  Brief description
  The IL_ModBusTCPReadWriteMultipleRegisters function block cyclically reads
  and writes multiple holding registers from a ModbusTCP server.
  Thus, a connection managed by the IL_ModbusTCPClient function block is
  required.

  Table       374:       Library         assignment             of             the
  IL_ModBusTCPReadWriteMultipleRegisters
  Library/folder
  CXA_ModbusTCP/Client

  Interface description

Table 375: Interface variables of the IL_ModBusTCPReadWriteMultipleRegisters function block
                    Name                  Type         Description
VAR_INPUT           Enable                BOOL         Function block processing enabled (level-
                                                       controlled).
                    FirstReadRegister     UINT         First register to be read from
                    ReadQuantity          UINT         Number of registers to be read
                    ReadDataAddr          POINTER TO   Address of the data range to copy the reg‐
                                          WORD         isters to
                    SizeOfReadData        UINT         Size of the data range created in "ReadDa‐
                                                       taAddr" in bytes
                    FirstWriteRegister UINT            First register to be written from
                    WriteQuantity      UINT            Number of registers to be written
                    WriteDataAddr      POINTER TO      Address of the data range the registers to
                                       WORD            be copied from
                    SizeOfWriteData    UINT            Size of the data range created in "WriteDa‐
                                                       taAddr" in bytes
                    UnitID                USINT        Unit ID or slave ID of the client
VAR_OUTPUT          Done                  BOOL         One transfer cycle is completed. Received
                                                       data was transferred to the range created
                                                       in "DataAddr"
                    Error                 BOOL         Error while processing the function block.

Name                 Type          Description
ErrorID              ⮫ ERROR_CODE  If the "Error" output is set, it contains a
                                 broad error classification.
ErrorIdent           ⮫ ERROR_STRUC If the "Error" output is set, this output
                   T             contains detailed error information
VAR_IN_OUT          ModbusLink           IL_MODBUS_LIN Link to existing Modbus connection is pro‐
                   K             vided by the IL_ModbusTCPClient function
                                 block
Table 376: Input behavior of the IL_ModBusTCPReadWriteMultipleRegisters
Name                 Type            Min. value     Max. value     Default value Applied

Enable               BOOL                                          FALSE         Continuous
FirstReadRegister    UINT            0              65535          0             Rising edge at
                                                           "Enable"
ReadQuantity         UINT            1              125            0             Rising edge at
                                                           "Enable"
ReadDataAddr         POINTER TO      0                             0             Rising edge at
WORD                                                        "Enable"
SizeOfReadData       UINT            2              250            0             Rising edge at
                                                           "Enable"
FirstWriteRegister UINT              0              65535          0             Rising edge at
                                                           "Enable"
WriteQuantity        UINT            1              125            0             Rising edge at
                                                           "Enable"
WriteDataAddr        POINTER TO      0                             0             Rising edge at
WORD                                                        "Enable"
SizeOfWriteData      UINT            2              250            0             Rising edge at
                                                           "Enable"
UnitID               USINT           0              255            255           Rising edge at
                                                           "Enable"

Functional description
The IL_ModBusTCPReadWriteMultipleRegisters function block implements the
Modbus function code 23.
It cyclically reads and writes multiple holding registers from a ModbusTCP
server.
Thus, a connection managed by the IL_ModbusTCPClient function block is
required.

Enable, Done
The function block checks its inputs at a rising edge at "Enable". Subse‐
quently, it cyclically sends a request to the Modbus server via the IL_Mod‐
busTCPClient specified at "ModbusLink" and waits for response. After a suc‐
cessful transfer cycle, "Done" is set for one PLC cycle. The function block
is disabled at a falling edge at "Enable”. If it is still transferred, processing
continues using the IL_ModbusTCPClient function block and the result is dis‐
carded.

Error, ErrorID, ErrorIdent
If an error occurs while processing the function block, the output "Error" is
set. "ErrorID" and "ErrorIdent" contain detailed error information. Function
block processing is paused. The "Error" output is reset at a falling edge at
"Enable”.

The error outputs are set if errors occur at the function block inputs and in
the ModbusTCP protocol.

FirstReadRegister, ReadQuantity
Modbus provides 66536 readable and writable holding registers. Each register
has a width of one word (2 bytes). It can assume a value between 0 and
65535. The "FirstRegister" input specifies the first register to be read. From
this register, "ReadQuantity” registers are read. Up to 125 registers can be
read per call.

FirstWriteRegister, WriteQuantity
Modbus provides 66536 readable and writable holding registers. Each register
has a width of one word (2 bytes). It can assume a value between 0 and
65535. The "FirstWriteRegister" input specifies the first register to be written.
From this register, "WriteQuantity" registers are written. Up to 125 registers
can be written per call.

ReadDataAddr, SizeOfReadData
The received data is stored in the data range specified in "ReadDataAddr".
An array of Word is expected as reception buffer. The array size specified in
"SizeOfReadData" has to be at least double the number of registers to be
read. It is recommended to use the SIZEOF() operator to determine the array
size.

WriteDataAddr, SizeOfWriteData
The data to be transmitted is retrieved from the data range specified in "Read‐
DataAddr". An array of Word is expected as transmission buffer. The array
size specified in "SizeOfWriteData" has to be at least double the size of the
number of registers to be written. It is recommended to use the SIZEOF()
operator to determine the array size.

UnitID
The unit ID of the ModbusTCP protocol corresponds to the slave ID of the
Modbus RTU. It is used to differ between different clients on the bus or to
access different address ranges.

ModBusLink
The "ModbusLink" input references the actual ModbusTCP connection. It is
output by the IL_ModbusTCPClient function block and valid when the connec‐
tion is set up.

Troubleshooting
The function block uses the error table CXA_TABLE, 16#0170.
It can generate the following error messages in Additional1 and Additional2:
Table 377: Error codes of the IL_ModBusTCPReadWriteMultipleRegisters
ErrorID                   Additional1   Additional2    Description
RESOURCE_ERROR            16#1810       16#0000        The link specified at the "ModbusLink" input
                                                       is invalid.
INPUT_INVALID_ERROR 16#1811             16#0000        The address specified at the "ReadDataAddr"
                                                       input is 0.
INPUT_INVALID_ERROR 16#1811             16#0001        The address specified at the "WriteDataAddr"
                                                       input is 0.
INPUT_INVALID_ERROR 16#1812             16#0000        The "SizeOfRegisterData" input is 0.

ErrorID             Additional1           Additional2   Description
INPUT_INVALID_ERROR 16#1812               16#0001       The "SizeOfRegisterData" input is 0.
INPUT_INVALID_ERROR 16#1813               16#0000       The "ReadQuantity” input is 0
INPUT_INVALID_ERROR 16#1813               16#0001       The "WriteQuantity" input is 0
INPUT_RANGE_ERROR 16#1814                 16#0001       The "ReadQuantity" input is higher than 125
INPUT_RANGE_ERROR 16#1814                 16#0002       The "WriteQuantity" input is bigger than 125
INPUT_INVALID_ERROR 16#1816               16#0000       The value at the "ReadQuantity"*2 input is
                                   higher than "SizeOfReadData"
INPUT_INVALID_ERROR 16#1816               16#0001       The value at the "WriteQuantity”*2 input is
                                   higher than "SizeOfWriteData"

RESOURCE_ERROR               16#1817      Modbus        The Modbus operation returns an error code
                     error code

### 17.3.12 IL_ModbusTCPReadDeviceIdentification

Brief description
The IL_ModbusTCPReadDeviceIdentification function block reads all available
device information on the Modbus client device and provides them at its
outputs.
Thus, a connection managed by the IL_ModbusTCPClient function block is
required.

Table 378: Library assignment of the IL_ModbusTCPReadDeviceIdentification
Library/folder
CXA_ModbusTCP/Client

Interface description

Table 379: Interface variables of the IL_ModbusTCPReadDeviceIdentification function block
               Name                    Type             Description
VAR_INPUT      Execute                 BOOL             Processing the function block enabled (edge-
                                                        controlled).
               UnitID                  USINT            Unit ID or slave ID of the client

Name                        Type          Description
VAR_OUTPUT Done                        BOOL          One transfer cycle is completed. Received
                                  data was transferred to the range created in
                                  "DataAddr"
Active              BOOL          Transfer running
Error               BOOL          Error while processing the function block.
ErrorID             ⮫ ERROR_CODE If the "Error" output is set, it contains a
                                  broad error classification.
ErrorIdent          ⮫ ERROR_STRUC If the "Error" output is set, this output con‐
                    T             tains detailed error information
VendorName          STRING            Vendor name
ProductCode         STRING            Product code
MajorMinorRevi‐     STRING            Version number
sion
VendorUrl           STRING            Web address of the vendor
ProductName         STRING            Product name
ModelName           STRING            Model name
UserApplication‐    STRING            Application name
Name
VAR_IN_OUT         ModBusLink          IL_MODBUS_LIN Link to existing Modbus connection is pro‐
                    K             vided by the IL_ModbusTCPClient function
                                  block
Table 380: Input behavior of the IL_ModbusTCPReadDeviceIdentification
Name                   Type            Min. value     Max. value     Default value Applied
Execute                BOOL                                          FALSE         Continuous
UnitID                 USINT           0              255            255           Rising edge at
                                                                                   "Execute"

     Functional description
     The IL_ModbusTCPReadDeviceIdentification function block reads all available
     device information on the Modbus client device and provides them at its
     outputs.

     Execute, Active, Done
     The function block checks its inputs at a rising edge at "Execute". Subse‐
     quently, it sends the request to the Modbus server via the IL_ModbusTCP‐
     Client specified at "ModbusLink" and waits for response. During this period,
     the "Active" output is set. After a successful transfer reception, "Done" is set.
     The function block continues running at a falling edge at “Execute” until no
     data is received anymore or an error occurs.

     Error, ErrorID, ErrorIdent
     If an error occurs while processing the function block, the output "Error" is
     set. "ErrorID" and "ErrorIdent" contain detailed error information. Function
     block processing is paused. The "Execute" output is reset at a falling edge at
     "Enable".
     The error outputs are set if errors occur at the function block inputs and in
     the ModbusTCP protocol.

UnitID
The unit ID of the ModbusTCP protocol corresponds to the slave ID of the
Modbus RTU. It is used to differ between different clients on the bus or to
access different address ranges.

ModBusLink
The "ModbusLink" input references the actual ModbusTCP connection. It is
output by the IL_ModbusTCPClient function block and valid when the connec‐
tion is set up.

Troubleshooting

The function block uses the error table CXA_TABLE, 16#00000170. It can gen‐
erate the following error messages in Additional1 and Additional2:
Table 381: Error codes of the IL_ModbusTCPReadDeviceIdentification
ErrorID                      Additional1 Additional2 Description
RESOURCE_ERROR               16#0000181 16#0000000 The link specified at the "ModbusLink" input
                             0           0           is invalid.
RESOURCE_ERROR               16#0000181 Modbus       The Modbus operation returns an error code
                             7           error code
