# 33 CXA_S20_KNX

## 33.1 Introduction and overview

The library CXA_S20_KNX contains function blocks to access the PLC program
on the S20 KNX module.
The ctrlX CORE controls support the library (an S20-EC-BK is required with
the S20-KNX-1).

1030 /    ctrlX PLC Engineering
1344      Introduction and overview

Functions
ctrlX CORE controls ③ include a software interface consisting of the
"IH_S20KNXClient" and the function blocks for the individual datapoint types
(see ⮫ Table 885 KNX services and datapoint types on page 1031).
The function block IH_S20KNXClient ③ manages the communication to the
object server ⑤ using a communication protocol ④ based on the serial FT1.2
protocol.
The S20 KNX-1 module ⑥ provides the KNX object server ⑤. It includes the
"ServerItems " and "DataPoints ".
The KNX object server ⑤ is configured and parameterized using the ETS soft‐
ware and the programming tool USB KNX Interface, or ETH KNX Gateway with
interface ⑨ on the S20-KNX-1 module ⑥.
An external KNX power supply unit ⑧ supplies the S20 KNX-1 module and the
connected KNX devices ⑦.

                                          1

                                                            7

                                          6
            2

                          3       4       5

                                                           8

                                                                9
The library and the S20-KNX-1 module support the following services and
datapoint types:

                                           Introduction and overview       1344

Table 885: KNX services and datapoint types
Service              Function block     Description                               Data width
ctrlX CORE and       IH_S20KNXClient    Communication with the S20 KNX-1 module
S20-EC-BK                               (requires the S20BusHandle from the func‐
                                        tion block ⮫ IH_S20ComConfiguration)
DPT1                 IH_S20KNXDPT1      Binary                                    1 bit
DPT2                 IH_S20KNXDPT2      Binary with priority                      2 bits
DPT3                 IH_S20KNXDPT3      Dimming up/down                           4 bits
DPT4                 IH_S20KNXDPT4      Characters                                1 byte
DPT5                 IH_S20KNXDPT5      Percentage value                          1 byte
DPT6                 IH_S20KNXDPT6      Signed value                              1 byte

DPT7                 IH_S20KNXDPT7      Unsigned value                            2 bytes
DPT8                 IH_S20KNXDPT8      Signed value                              2 bytes
DPT9                 IH_S20KNXDPT9      Floating point value                      2 bytes
DPT10                IH_S20KNXDPT10     Time                                      3 bytes
DPT11                IH_S20KNXDPT1      Date                                      3 bytes
DPT12                IH_S20KNXDPT12     Unsigned value                            4 bytes
DPT13                IH_S20KNXDPT13     Signed value                              4 bytes
DPT14                IH_S20KNXDPT14     Floating point value                      4 bytes
DPT16                IH_S20KNXDPT16     Text/string                               14 bytes
DPT18                IH_S20KNXDPT18     Scene with learning function              1 byte
The module S20 KNX-1 does not support DPT15 and DPT17!

For the documentation including sample code on the function blocks of the
CXA_S20_KNX library, refer to the ctrlX PLC Engineering library manager.
Open the library manager in the application and select the respective function
block in the library CXA_S20_KNX.
The "Documentation" folder includes the following function block information:
●  Special features
●  Structures
●  Enumerations
●  Program code samples for different DPT function blocks in the folder
   _CodeExamples (for further samples and commissioning videos, refer to
   the product in the internet)
The recommended PLC cycle time is 10 ms for the function block
IH_S20KNXClient.

1032 /    ctrlX PLC Engineering
1344      Introduction and overview

Diagnostics and error codes
For the error codes and function blocks, refer to the following table.
For specifications on the error codes of the S20 KNX-1 module, refer to the
data sheet of the module.
Potential error sources:
● The KNX (ETS) configuration of the S20 KNX-1 module is invalid
● The KNX voltage supply is missing or overloaded
● Error in the KNX cabling/installation
Table 886: Diagnostics and error codes
Additional 1 Additional 2         ErrorID             Description
16#xxxx010B 16#YYYY0002           INPUT_RANGE_ERROR   Wrong slot
16#xxxx010B 16#YYYY0005           INPUT_RANGE_ERROR   TimeOut beyond the range
                                                      (5s..120s - Client, 3s..60s DPT FB)
16#xxxx010B 16#YYYY_0065          RESOURCE_ERROR      Null pointer, S20BusHandle invalid
16#xxxx010B 16#YYYY_00CF          STATE_MACHINE_ERROR Internal State Machine Error
                                                      Restart the function block
16#xxxx010B        16#YYYY0148    INPUT_INVALID_ERROR Wrong module or wrong slot
16#xxxx010B        16#YYYY0322    DEVICE_ERROR        TimeOut
16#xxxx0112        16#YYYY0001    INPUT_RANGE_ERROR   DPT ID beyond the range 1...1,000
16#xxxx0112        16#YYYY0002    INPUT_RANGE_ERROR   "DPT Name" beyond the range
16#xxxx0112        16#YYYY0003    INPUT_RANGE_ERROR   "DPT Value" beyond the range. The
                                                      input range is DPT-specific
16#xxxx0112        16#YYYY0004    INPUT_RANGE_ERROR   ReadWrite beyond the range
16#xxxx0112        16#YYYY0065    DEVICE_ERROR        DPT is disabled in the KNX configura‐
                                                      tion (ETS)
16#xxxx0112        16#YYYY0066    DEVICE_ERROR        IH_S20KNXClient not ready (busy)
                                                           ● KNX client initialized
                                                           ● KNX client not "Enabled"
16#xxxx0112        16#YYYY0067    DEVICE_ERROR             Response telegram cannot be identified
16#xxxx0112        16#YYYY0068    DEVICE_ERROR             KNX supply voltage missing or KNX bus
                                                           not connected
16#xxxx0112        16#YYYY0069    DEVICE_ERROR             DPT configuration with ETS software
                                                           (ETS download) changed
16#xxxx0112        16#YYYYGHHH    DEVICE_ERROR             Negative response for a read/write
                                                           action
                                                           ● G-error numbers 0-11
                                                               (⮫ Table 887 Overview on KNX pro‐
                                                               tocol errors on page 1033)
                                                           ● HHH - DPT ID 16#0001 - 16#03E8
                                                           For more details, refer to the KNX pro‐
                                                           tocol specification appendix B
16#xxxx0112        16#YYYY_00C9   RESOURCE_ERROR           "DPT Type" does not match the object
                                                           server configuration
16#xxxx0112        16#YYYY_00CA   RESOURCE_ERROR           Data exchange token to the KNX client
                                                           is consumed. Up to 260 tasks can be
                                                           processed simultaneously. Wait for free
                                                           token and try again
16#xxxx0112        16#YYYY_00CB   RESOURCE_ERROR           DPT is not configured in the S20 KNX-1
                                                           module. No DPT configured with ETS.

                                             Introduction and overview      1344

Additional 1    Additional 2     ErrorID                  Description
16#xxxx0112     16#YYYY_00CC     RESOURCE_ERROR           DPT configurations (flags) does not
                                     meet the requirements for deep
                                     reading (Deep Read)
                                     "Write", "Transmit" and "Update" flag
                                     have to be enabled in the ETS configu‐
                                     ration
XXXX (Additional 1 Prefix) = 16#0A0F
YYYY (Additional 2 Prefix) = 16#0C23. /
The prefixes vary on another platform.
Table 887: Overview on KNX protocol errors

Error number           Description
0                      No error
1                      Internal error
2                      Element not found
3                      Buffer too small
4                      Item not writable
5                      Service not supported
6                      Incorrect service parameter (Bad)
7                      Wrong ID (Bad)
8                      Wrong command (Bad) / value (value)
9                      Incorrect length
10                     Message inconsistent
11                     Object server busy (busy)

Procedure in case of error
Perform the following checks if an error was issued:
1.   Check KNX voltage supply
2.   Check ETS configuration
3.   Check status and error code of the function blocks

DPT Status/Communication Status/Error
● The function block IH_S20_KNX_STATUS indicates what the
  IH_S20KNXClient function block is currently processing or whether an error
  is present
● Each KNX DPT function block is provided with a "Valid" output that signals
  that a KNX datapoint is valid and that the status corresponds to the status
  in the KNX bus of the real KNX application if the state is TRUE.
  There can be different reasons for "Valid" being FALSE:
  – Initial state, KNX is not yet initialized
  – No DPT read or written from the user program. No change in value in the
     actual KNX application
  – Check IH_S20KNXClient function block for pending diagnostics
  – S20-KNX-1 module in error (check the diagnostic code and LED at the
     S20-KNX-1 module)
  – KNX voltage missing (signaled at the S20-KNX-1 module with the error
     0x3402 and can be identified due to the E2-LED red)

1034 /    ctrlX PLC Engineering
1344      Introduction and overview

In the state of KNX voltage errors, KNX datapoints can still be read from the
buffer of the IH_S20KNXClient using the KNX-DPT function blocks. Writing and
"deep" reading causes an error, as the KNX bus is accessed. If the KNX voltage
is applied again, "Valid" is TRUE again on the KNX bus after the first refresh
from the respective datapoint.

IH_S20KNXClient
The function block IH_S20KNXClient is the software interface between
the module S20 KNX-1 and the KNX datapoint type function block (via
KNXHandle).
An own instance of the IH_S20KNXClient function block is required for each
configured S20 KNX-1 module.
To call the function block IH_S20KNXClient, the function block IH_S20Com‐
Configuration is required additionally. The function block provides the
required S20BusHandle for the IH_S20KNXClient function block.
The function block of the individual datapoint types operates analogously. The
interface is KNXHandle at the IH_S20KNXClient function block.

To set up the communication to the S20 KNX-1 module, set the "Enable" input
at the IH_S20KNXClient function block to TRUE.
When it is changed from FALSE to TRUE at the "Enable" input, the interface is
initialized.
All configured datapoints of the S20 KNX-1 module are retrieved and stored in
an internal data area (up to 1,000 datapoints).

                                          Introduction and overview       1344

The initialization is completed when all datapoints are loaded. The "InOpera‐
tion" output then changes to TRUE.
The S20 KNX-1 module is now ready.
The output "CommunicationStatus" shows the operational readiness via the
status CLIENT_READY.
The initialization might take a few seconds and is shown at the "Communica‐
tionStatus" output with "INIT_******".
Every new edge from FALSE to TRUE at the "Enable" input causes an initializa‐
tion.
After the initialization, all telegrams of the single KNX datapoints received
during operation are analyzed and saved in the RAW data of the function block
IH_S20KNXClient (buffer in the function block for all DPT).

In the application, it is communicated between the function blocks of the
different KNX datapoint types and the IH_S20KNXClient function block using
the KNXHandle.
The output parameter "DPTStatus" provides the following RAW data from the
KNX configuration:
●  DPTID
●  DPT type
●  Configuration flags of the ETS configuration
●  State
   – TransmissionStatus
   – ReadrequestFlag
   – UpdateFlag: Flag is set if ActValue of the respective DPT-ID was updated
   – ValidFlag
● KNX user data (14 bytes)
This information is analyzed and prepared using the function blocks of
the individual datapoint types (output parameter not mandatorily required/
optional).
The output parameter "ServerItems" provides the following information on the
loaded KNX project of the PLC application:
● Hardware type
● Hardware version
● Firmware version
● KNX Manufacturer Code DEV
● KNX Manufacturer Code APP
● ETS Applikation ID
● ETS application version
● Serial number
● Bus status (KNX)
● Protocol version
● Indication Sending
● Maximum number of datapoints
● Number of the configured datapoints (depends on the created ETS project,
  whether with 250 datapoints or more)
The available input and output parameters of the function blocks are deter‐
mined by the included or configured datapoint types.

1036 /    ctrlX PLC Engineering
1344      Application example

IH_S20KNXDPTxx
The individual function blocks IH_S20KNXDPTxx are provided with a "Read‐
Write" input with the enumeration "IH_S20_KNX_RW".
The following write/read modes are supported:
Table 888: IH_S20_KNX_RW
ReadWrite       Description
Mode
IDLE            "ActValue" (current value) is read (default mode)
WRITEONCE       "SetValue" is written once. If the "Threshold" input is used
                additionally, it is only written once when "SetValue" is greater
                than or equal to the “Threshold” value. Writing can be forced
                if "ActValue" is equal to "ACTValue" and if "Threshold" is set to
                zero. Cyclic execution is limited to 100 ms.
WRITEAUTO       "SetValue" is always written when this values differs from its
                last specification. If the "Threshold" input is used additionally,
                it is always written when "SetValue" is greater than or equal
                to the “Threshold” value and if it differs from the previous
                "SetValue". It is written once after a rising edge at “Enable”
                if the value differs from "ActValue" and if it is greater than
                "Threshold". Cyclic writing is limited to 100 ms.
READVIABUS      The KNX bus forces direct reading. It is read actively on the
                KNX bus
If WRITEONCE, WRITEAUTO and READVIABUS were successful, "Done" is
shown for one PLC cycle. The cyclic execution is limited to 100 ms.
If a “Threshold” value is used and if “SetValue” is to be written with "0" or if
writing is forced, specify a “Threshold” of 0.

## 33.2 Application example

An example application is described in the following starting from the KNX
configuration on the S20-KNX-1 module up to the application program on the
control to read and write a KNX datapoint.

Prerequisite
1.   The S20-KNX-1 module is ready, connected to an S20-S3-BK+ and oper‐
     ating
2.   KNX power supply unit and supply present
3.   KNX devices connected to a KNX power supply unit and S20-KNX-1
4.   KNX programming device present, e.g. a KNX USB interface or a KNX IP
     gateway and connected to the S20-KNX-1 and the engineering PC
5.   ETS5 software downloaded from the KNX website and installed
6.   Required KNX description files can be directly loaded to the ETS5 soft‐
     ware if the files are available in the ETS catalog. Otherwise, contact
     the KNX device manufacturer and import the files directly into the ETS5
     software

                                                    Application example       1344

Creating ETS project
1.      Open the ETS5 software and create a new project:
        ●  Specify a name
        ●  Select Backbone "IP"
        ●  Select the topology "Create Line 1.1" and select "TP"
        ●  Select the group address style "Three Level"
        Table 889: Creating new project

        🡆 Project view:

1038 /    ctrlX PLC Engineering
1344      Application example

2.   Add a room to the project:
● Right-click on "MyProject" and add a room
● Specify a room name and create a room
Table 890: Adding a room

3.   Add devices analogously to the room:
● Right-click on the room and add devices.
● The device catalog opens automatically.
● Select the devices from the catalog and add a room to them.
   Drag&drop can be used..
In the present example, the module "S20-KNX-1" and the switch/push‐
button "4072.02LED" (company Albrecht Jung) and optionally the KNC
power supply unit MDT STV-320.02 are added
  KNX power supply units are part of the configuration and ensure that
the KNX bus supply is sufficient upon the validation.
4.   Configure S20-KNX-1 module for the room "MyRoom". Select the device
and the "Parameter" tab. In the “General”, the value "Enabled" has to be
selected under "Send Indications".
Table 891: "MyRoom" configuration

                                             Application example       1344

5.      Go from the menu “General” to “Datapoint 1-10” and select the type
"DPT 1 - Binary-1 Bit" for "Datapoint type 1" and for "Datapoint type 2".
For a better overview, provide a brief description for each point "Data‐
point description".
Table 892: Configuration "Datapoint 1-10"

6.      When going to the "Group Objects" tab, the two created datapoints are
shown. The respective flags are set for each datapoint via "Properties".
Table 893: "Group Objects" tab

Table 894: "Properties" tab

1040 /    ctrlX PLC Engineering
1344      Application example

7.   At the pushbutton, the default settings can remain except for the LED
response. In "Function", change the behavior from "Button-press display"
to "Status indicator (via LED object)".
A new datapoint is automatically inserted at the pushbutton. For this
datapoint, enable the flags under "Properties" as well.
Table 895: Pushbutton settings

The individual KNX devices are prepared. Use groups to interlink these
devices.
8.   To add the group view, select “Workplace 🠂 Open New Panel 🠂 Group
addresses” in the menu
Table 896: Menu "Workplace"

9.   Go to the “Add Main Groups” function to add the groups:
● First level "MainGroup"
● Next level "MiddleGroup"
● Group address "RockerSwitch1"
● Group address "RockerLED"
Table 897: Adding groups

                                               Application example       1344

10. Add the datapoints to the group addresses via drag&drop. Adding them
to a group is required for a unique addressing on the KNX. Datapoints
are linked to exchange data for reading and writing. All datapoints of
the same datapoint type to interact with each other are assigned to one
group address.
For the example, link "Group object 1" with "Rocker1 - Switching" to the
group address "0/0/1 RockerSwitch1" and "Group object 2" with "LED
left - Status indication" to "0/0/2 RockerLED".
Table 898: Assigning datapoints

      Without assigning datapoints to a group address, this datapoint cannot
    be used with the application S20-KNX-1 and causes the error "DPT is
    disabled in the KNX configuration (ETS)" during access.
    🡆 The ETS project is now created and can be assigned to the KNX
       devices.

1042 /    ctrlX PLC Engineering
1344      Application example

11. Upon the initial commissioning, specify the physical address once for the
KNX devices.
● Select “Download 🠂 Download all”. Physical addresses are specified
● Follow the ETS instructions. During the download, press the program‐
   ming pushbuttons of the KNX devices upon request
Table 899: Starting ETS download

Table 900: Request to press the programming pushbutton on the KNX
device (enable programming mode)

In case of further datapoint changes, a “Download 🠂 Download partial”
or “Download 🠂 Download application” is sufficient. The programming
pushbutton has not to be pressed anymore.
   After a complete download or upon the initial commissioning, discon‐
nect the module S20-KNX-1 from voltage. The control or the bus coupler
has to be disabled with the module and enabled again.
If only one data point was added or changed, a restart is not required.

                                                         Application example               1344

PLC application example
1.     Add the CXA_S20_KNX library.
       Create the function block IH_S20ComConfiguration.
       The function block provides the S20BusHandle to specify at which bus
       master (XM local or at the bus coupler) the S20-KNX-1 module is oper‐
       ated.
2.     Add the CXA_S20_KNX library.
       Create the function block IH_S20KNXClient.
       The function blocks IH_S20KNXClient and KNXHandle provide the inter‐
       face to the S20-KNX module and the KNX datapoint types. A new func‐
       tion block instance of the IH_S20KNXClient is required for each S20-

       KNX-1 module.
3.     To detect the pushbutton state, use the datapoint DPT1 of the group
       "0/0/1 RockerSwtich1".
       Create the IH_S20KNXDPT1 function block for each data point ID
       "DPTID" with the data point type DPT1 as own instance.
4.     Example program code
       Reading the DPT ID 1 of the group 0/0/1 RockerSwitch1 to read the DPT
       ID 0 state that corresponds to the actual pushbutton position of the real
       pushbutton

Example ST

PROGRAM KNX_Example
VAR
   // "IH_S20ComConfiguration" FB Variables
    fbIH_S20ComConfiguration   : CXA_S20_KNX.CXA_S20.IH_S20ComConfiguration;   // "ComConfiguration" FB instance
    bEnableComConfig           : BOOL := FALSE;                                // Function block processing
enabled( TRUE – once, edge-controlled )
    bInOpComConfig             : BOOL;                                         // TRUE: Function Block is working
on its actual task
    bErrorComConfig            : BOOL;                                         // TRUE: Indicates an error
    ErrorIDComConfig           : ERROR_CODE;                                   // Class of error
    ErrorIdentComConfig        : ERROR_STRUCT;                                 // Detailed information about error
    enBusType                  : CXA_S20_KNX.CXA_S20.IH_S20_BUSTYPE :=
CXA_S20_KNX.CXA_S20.IH_S20_BUSTYPE.ETHERCAT;    // Module is connected to EtherCAT fieldbus
    strBusMaster               : STRING(100) := 'ethercatmaster';              // EtherCAT Busmaster name
    stBusConfig                : CXA_S20_KNX.CXA_S20.IH_S20_BUS_CONFIG;
    pS20BusHandle              : POINTER TO CXA_S20_KNX.CXA_S20.IH_S20_BUS_IDENTIFIER;             // S20 Bus
Handle

   // "IH_S20KNXClient" Fb Variables
   fbIH_S20KNXClient       : IH_S20KNXClient;          // Client FB instance
   bEnable_Client          : BOOL := FALSE;            // TRUE: Enable Client, FALSE: Disable Client
   bInOp_Client            : BOOL;
   bError_Client           : BOOL;
   ErrorID_Client          : ERROR_CODE;
   ErrorIdent_Client       : ERROR_STRUCT;
   uiSlot                  : UINT := 1;                // Slot of the S20-KNX-1 module; Input your module slot
number here
   wStatusWord             : WORD;                     // Status word of S20-KNX-1 module
   arInputComplexProtocol : ARRAY [0..23] OF BYTE;     // Input data of S20-KNX-1 module
   stServerItems           : IH_S20_KNX_SERVERITEMS;   // Server items status
   stDPTStatus             : IH_S20_KNX_DPT_STATUS;    // DPT's RAW status
   enCommunicationStatus   : IH_S20_KNX_STATUS;        // Client FB state
   pKNXHandle              : POINTER TO IH_S20_KNX_HANDSHAKE; // KNX communication handle for DPT Fb's
   wControlWord            : WORD;                     // Control word of S20-KNX-1 module
   arOutputComplexProtocol : ARRAY [0..23] OF BYTE;    // output data of S20-KNX-1 module

   // "IH_S20KNXDPT1" Fb Variables
   fbIH_S20KNXDPT1     : IH_S20KNXDPT1;        // FB Instance
   bEnable_DPT1        : BOOL;                 // TRUE: Enable DPT FB, FALSE: Disable DPT FB
   bDone_DPT1          : BOOL;                 // Done, indicates when the value is changed
   bActive_DPT1        : BOOL;                 // DPT FB is in active state
   bError_DPT1         : BOOL;                 // DPT FB is in error
   enErrorID_DPT1      : ERROR_CODE;
   stErrorIdent_DPT1   : ERROR_STRUCT;

1044 /    ctrlX PLC Engineering
1344      Application example

   uiDPTID_DPT1       : UINT := 0;            // DPT ID; Input your DPT ID here
   enReadWrite_DPT1   : IH_S20_KNX_RW := IH_S20_KNX_RW.WRITEAUTO; // Read/Write mode; Input your mode here
   bSetValue_DPT1     : BOOL;                 // SetValue; Input your setvalue here
   bValid_DPT1        : BOOL;                 // Valid indicates the KNX valid flag of the DPT
   stState_DPT1       : IH_S20_KNX_DPT_STATE; // State information of the DPT
   bActValue_DPT1     : BOOL;                 // Actual value of the DPT
END_VAR

IF bInit THEN
  bEnableComConfig := TRUE;
  bEnableClient    := TRUE;
  bInit            := FALSE;
END_IF

// Bustype
enBusType :=   CXA_S20_KNX.CXA_S20.IH_S20_BUSTYPE.ETHERCAT;

// Bus Configuration
stBusConfig.EtherCAT.AddressType    := CXA_S20_KNX.CXA_S20.IL_ECAT_ADDRESS_TYPE.ECAT_ETHERCAT_ADDRESS; // Address
type
stBusConfig.EtherCAT.BusMaster      := ADR(strBusMaster); // Bus master name
stBusConfig.EtherCAT.SlaveAddress   := 1001; // Address of the slave (bus coupler)

// "IH_S20ComConfiguration" FB to generate Bus Handle
fbIH_S20ComConfiguration(
       Enable:= bEnableComConfig,
       InOperation=> bInOpComConfig,
       Error=> bErrorComConfig,
       ErrorID=> ErrorIDComConfig,
       ErrorIdent=> ErrorIdentComConfig,
       BusType:= enBusType,
       BusConfig:= stBusConfig,
       S20BusHandle=> pS20BusHandle);

// KNX Client FB Implementation
fbIH_S20KNXClient(
       Enable:= bEnable_Client AND bInOpComConfig, // Client FB is enabled after the "IH_S20ComConfiguration" is
in "InOperation" state
       InOperation=> bInOp_Client,
       Error=> bError_Client,
       ErrorID=> ErrorID_Client,
       ErrorIdent=> ErrorIdent_Client,
       S20BusHandle:= pS20BusHandle,
       Slot:= uiSlot,
       StatusWord:= wStatusWord,
       InputComplexProtocol:= arInputComplexProtocol,
       TimeOut:= T#5S,
       ServerItems=> stServerItems,
       DPTStatus=> stDPTStatus,
       CommunicationStatus=> enCommunicationStatus,
       KNXHandle=> pKNXHandle,
       ControlWord=> wControlWord,
       OutputComplexProtocol=> arOutputComplexProtocol);

// KNX DPT FB 1
fbIH_S20KNXDPT1(
       Enable:= bEnable_DPT1 AND bInOp_Client,
       Done=> bDone_DPT1,
       Active=> bActive_DPT1,
       Error=> bError_DPT1,
       ErrorID=> enErrorID_DPT1,
       ErrorIdent=> stErrorIdent_DPT1,
       DPTID:= uiDPTID_DPT1,
       ReadWrite:= enReadWrite_DPT1,
       SetValue:= bSetValue_DPT1,
       TimeOut:= T#3S,
       KNXHandle:= pKNXHandle,
       Valid=> bValid_DPT1,
       State=> stState_DPT1,
       ActValue=> bActValue_DPT1);

                                                  Introduction and overview              1344
