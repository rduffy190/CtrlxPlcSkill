# 13 CXA_EthercatMaster

## 13.1 Introduction and overview

The CXA_EthercatMaster is the interface between the PLC programming envi‐
ronment and the Ethercat master.
EtherCAT® is a registered trademark and patented technology licensed by the
Beckhoff Automation GmbH, Germany.

## 13.2 Acyclic communication SoE

### 13.2.1 IL_ECATSoeRead

Brief description
Use the function block IL_ECATSoeRead to acyclically read a parameter from
an EtherCAT slave device.

          Interface description

Table 103: Interface variables of the IL_ECATSoeRead function block
I/O type           Name              Data type                          Description

VAR_INPUT          Execute           BOOL                               Function block processing enabled (once, edge-controlled)

ClientId          ⮫ IL_HANDLE                        ClientId is currently not supported (default: ClientId := 0)

MasterName        POINTER TO STRING                  Instance name of the master

AddressType       ⮫ IL_ECAT_ADDRESS_TYPE             Selection of the slave addressing (EtherCAT address or AutoInc
                                                     address)

SlaveAddress      UINT                               EtherCAT address or the current AutoInc address at the bus
                                                     (depends on the input "AddressType")

DriveNo           BYTE                               Drive number (for single-axis device "0")

Element           BYTE                               Element number of the parameter, refer to IL_ECAT_SOE_ELE‐
                                                     MENT

Idn               WORD                               ID number of the parameter

SizeOfValue       UDINT                              Size of the buffer or the variable in bytes to receive data
                                                     (SIZEOF(Value))

ValueAdr          POINTER TO BYTE                    Address    of   the   buffer   or   the   variable    to    receive    data
                                                     (ADR(Value))

Timeout           TIME                               Timeout monitoring

VAR_OUTPUT         Done              BOOL                               Processing completed without error. Output data valid

Active            BOOL                               Processing active. Output data invalid

Error             BOOL                               Processing completed with error. Output data invalid

ErrorID           ⮫ ERROR_CODE                       Standardized rough error classification

ErrorIdent        ⮫ ERROR_STRUCT                     Function block-specific detailed information on the error

NoOfRecBytes      UDINT                              Number of bytes copied to the "ValueAdr” buffer

RecElement        BYTE                               For receiving elements, refer to IL_ECAT_SOE_ELEMENT (if more
                                                     than one bit was set at the "Element" input)

Table 104: Min./max. and default values of the inputs of the IL_ECATSoeRead function block
Name          Data type              Min.                     Max                               Default                            Effective

Execute       BOOL                   -                        -                                 FALSE                              Continuous

ClientId      IL_HANDLE              0                        0                                 0                                  Rising edge at

MasterName    POINTER TO STRING      n. def.                  n. def.                           0                                  Rising edge at

AddressType   IL_ECAT_ADDRESS_TYP ECAT_AUTOINC_ADDRESS ECAT_ETHERCAT_ADDRESS                    ECAT_ETHERCAT_ADDRES               Rising edge at
E                                                                                 S                                  Execute

Name            Data type            Min.                   Max                    Default               Effective

SlaveAddress    UINT                 0                      65535                  0                     Rising edge at

DriveNo         BYTE                 0                      7                      0                     Rising edge at

Element         BYTE                 16#01                  16#FF                  SOE_ELEMENT_OPDATA    Rising edge at

Idn             WORD                 0                      n. def.                0                     Rising edge at

SizeOfValue     UDINT                0                      n. def.                0                     Continuous

ValueAdr        POINTER TO BYTE      n. def.                n. def.                0                     Continuous

Timeout         TIME                 T#1ms                  n. def.                TIME#3s0ms            Rising edge at

Functional description
Use the function block IL_ECATSoeRead to acyclically read a parameter from
an EtherCAT slave device.
The slave device has to support the mailbox protocol "Servo drive profile over
EtherCAT" (SoE). Mailbox communication is only possible in the EtherCAT
states PreOP, SafeOP and OP.
The parameter to be retrieved is addressed with "Idn", "Element" and
"DriveNo". The function IL_ECATSoeIdnCoding is recommended for Idn coding.
The enumeration type IL_ECAT_SOE_ELEMENT is recommended for the "Ele‐
ment” input. Multiple bits can also be set. Thus, multiple elements can be
retrieved with one acyclic request.
For example Sercos attribute and data:
fbECATSoeRead.Element               :=        SOE_ELEMENT_ATTRIBUTE           OR
SOE_ELEMENT_OPDATA;
In the response data, the values of the requested elements are entered into
the element bit sequence. Check the applied elements at the "RecElement”
output.
Reading multiple elements with one acyclic request is an optional function‐
ality in the slave devices. If this is not supported by the slave, the slave only
responds with the data of the first element bit set (refer to the "RecElement"
output). This is not an error, i.e. the function block does not report an error.
The requested elements have to be read out one after the other.
If a list parameter is read, the read out data shows the current length of the
list at the bits 0 and 1, the maximum length of the list at the bytes 2 and 3
and data of the list parameter starting from byte 4.

Implementation in ST
Beispiel:

TYPE IL_EG_ECAT_SOE_STRING :
STRUCT
  ActLength    : UINT;   // actual length without 0-ending
  MaxLength    : UINT; // max length without 0-ending
  Text         : STRING(255); // text value
END_STRUCT
END_TYPE
TYPE IL_EG_ECAT_SOE_WORD_LIST :
STRUCT
   ActLength    : UINT; // actual length
   MaxLength    : UINT; // max length
   awIDN        : ARRAY[0..999] OF WORD; // List elements
END_STRUCT
END_TYPE

PROGRAM EG_IL_ECATSoeRead
VAR
  strMasterName   : STRING := 'ethercatmaster';

  // Example A : read a UINT Parameter (S-0-0002)
  fbECATSoeRead1 : IL_ECATSoeRead;
  uiCycleTime     : UINT;

  // Example B : read a STRING Parameter (S-0-0095)
  fbECATSoeRead2 : IL_ECATSoeRead;
  rDiagnosis      : IL_EG_ECAT_SOE_STRING;

  // Example C : read an array (S-0-0017)
  fbECATSoeRead3 : IL_ECATSoeRead;

  rValue          : IL_EG_ECAT_SOE_WORD_LIST;

  // Example D : read unit of S-0-0001 (NC cycle time )
  fbECATSoeRead4 : IL_ECATSoeRead;
  rValueUnitS1    : IL_EG_ECAT_SOE_STRING;
END_VAR

// Example A : read a UINT Parameter (S-0-0002)
fbECATSoeRead1.Execute      := TRUE;
fbECATSoeRead1.MasterName   := ADR(strMasterName);
fbECATSoeRead1.SlaveAddress := 1001;
fbECATSoeRead1.Idn          := IL_ECATSoeIdnCoding(SOE_S_PARAM,0,2); // := S-0-0002
fbECATSoeRead1.ValueAdr     := ADR(uiCycleTime);
fbECATSoeRead1.SizeOfValue := SIZEOF(uiCycleTime);
fbECATSoeRead1();
IF TRUE = fbECATSoeRead1.Done THEN
  ; // FB finished . cycle time is in uiCycleTime.
END_IF
IF TRUE = fbECATSoeRead1.Error THEN
  ; // Error handling
END_IF

// Example B : read a STRING Parameter (S-0-0095)
fbECATSoeRead2.Execute      := TRUE;
fbECATSoeRead2.MasterName   := ADR(strMasterName);
fbECATSoeRead2.SlaveAddress := 1001;
fbECATSoeRead2.Idn          := IL_ECATSoeIdnCoding(SOE_S_PARAM,0,95); // = S-0-0095
fbECATSoeRead2.ValueAdr     := ADR(rDiagnosis);
fbECATSoeRead2.SizeOfValue := SIZEOF(rDiagnosis);
fbECATSoeRead2();
IF TRUE = fbECATSoeRead2.Done THEN
  rDiagnosis.Text[rDiagnosis.ActLength]:=0; ;     // FB finished. We make zero termination
of string.
END_IF
IF TRUE = fbECATSoeRead2.Error THEN
  ; // Error handling
END_IF

// Example C : read an array (S-0-0017)
//fbECATSoeRead3.Execute    := TRUE;
fbECATSoeRead3.MasterName   := ADR(strMasterName);
fbECATSoeRead3.SlaveAddress := 1001;
fbECATSoeRead3.Idn          := IL_ECATSoeIdnCoding(SOE_S_PARAM,0,17); // = S-0-0017
fbECATSoeRead3.ValueAdr     := ADR(rValue);
fbECATSoeRead3.SizeOfValue := SIZEOF(rValue);
fbECATSoeRead3();
IF TRUE = fbECATSoeRead3.Done THEN
  ; // FB finished . values are in rValue.
END_IF
IF TRUE = fbECATSoeRead3.Error THEN
  ; // Error handling
END_IF

// Example D : read unit of S-0-0001 (NC cycle time)
//fbECATSoeRead3.Execute    := TRUE;
fbECATSoeRead4.MasterName   := ADR(strMasterName);
fbECATSoeRead4.SlaveAddress := 1001;
fbECATSoeRead4.Element      := IL_ECAT_SOE_ELEMENT.SOE_ELEMENT_UNIT;
fbECATSoeRead4.Idn          := IL_ECATSoeIdnCoding(SOE_S_PARAM,0,1); // = S-0-0001
fbECATSoeRead4.ValueAdr     := ADR(rValueUnitS1);
fbECATSoeRead4.SizeOfValue := SIZEOF(rValueUnitS1);
fbECATSoeRead4();
IF TRUE = fbECATSoeRead4.Done THEN
  rValueUnitS1.Text[rValueUnitS1.ActLength]:=0; ;    // FB finished. We make zero
termination of string. Content of string should be ‘us’.

          END_IF
          IF TRUE = fbECATSoeRead4.Error THEN
            ; // Error handling
          END_IF

          Error description
          For more information on the error codes, refer to:
          ⮫ Chapter 13.11 Error codes on page 257
         ⮫ Diagnostics 0C0F0000

### 13.2.2 IL_ECATSoeWrite

          Brief description
          Use the function block IL_ECATSoeWrite to acyclically write a parameter from
          an EtherCAT slave device.

          Interface description

Table 105: Interface variables of the IL_ECATSoeWrite function block
I/O type           Name                Data type                   Description

VAR_INPUT          Execute             BOOL                        Function block processing enabled (once, edge-controlled)

ClientId            ⮫ IL_HANDLE                 ClientId is currently not supported (default: ClientId := 0)

MasterName          POINTER TO STRING           Instance name of the master

AddressType         ⮫ IL_ECAT_ADDRESS_TYPE      Selection of the slave addressing (EtherCAT address or AutoInc
                                                address)

SlaveAddress        UINT                        EtherCAT address or the current AutoInc address at the bus
                                                (depends on the input "AddressType")

DriveNo             BYTE                        Drive number (for single-axis device "0")

Element             BYTE                        Element number of the parameter, refer to IL_ECAT_SOE_ELE‐
                                                MENT

Idn                 WORD                        ID number of the parameter (refer to IL_ECATSoeIdnCoding)

SizeOfValue         UDINT                       Number of bytes to be written at "ValueAdr” (SIZEOF(Value))

ValueAdr            POINTER TO BYTE             Address of the buffer or the variable used to write data
                                                (ADR(Value))

Timeout             TIME                        Timeout monitoring

VAR_OUTPUT         Done                BOOL                        Processing completed without error. Output data valid

Active              BOOL                        Processing active. Output data invalid

Error               BOOL                        Processing completed with error. Output data invalid

ErrorID             ⮫ ERROR_CODE                Standardized rough error classification

ErrorIdent          ⮫ ERROR_STRUCT              Function block-specific detailed information on the error

Table 106: Min./max. and default values of the inputs of the IL_ECATSoeWrite function block
Name           Data type               Min.                Max                    Default              Effective

Execute        BOOL                    -                   -                      FALSE                Continuous

ClientId       IL_HANDLE               0                   0                      0                    Rising edge at

MasterName     POINTER TO STRING       n. def.             n. def.                0                    Rising edge at

AddressType    IL_ECAT_ADDRESS_TYPE ECAT_AUTOINC_ADDRESS ECAT_ETHERCAT_ADDRESS ECAT_ETHERCAT_ADDRESS Rising edge at

SlaveAddress   UINT                    0                   65535                  0                    Rising edge at

DriveNo        BYTE                    0                   7                      0                    Rising edge at

Element        BYTE                    16#01               16#FF                  SOE_ELEMENT_OPDATA   Rising edge at

Idn            WORD                    0                   n. def.                0                    Rising edge at

SizeOfValue    UDINT                   0                   n. def.                0                    Continuous

ValueAdr       POINTER TO BYTE         n. def.             n. def.                0                    Continuous

Timeout        TIME                    T#1ms               n. def.                TIME#3s0ms           Rising edge at

Functional description
Use the function block IL_ECATSoeWrite to acyclically write a parameter from
an EtherCAT slave device.
The slave device has to support the mailbox protocol "Servo drive profile over
EtherCAT" (SoE). Mailbox communication is only possible in the EtherCAT
states PreOP, SafeOP and OP.
The parameter to be written is addressed with "Idn", "Element" and "DriveNo".
The function IL_ECATSoeIdnCoding is recommended for Idn coding.
To write a list parameter, supplement 4 bytes at the beginning of the data to
be written: The bytes 0 and 1 have to contain the current length and the bytes
2 and 3 are reserved for the maximum data length (this maximum length does
not have to be set).

The library parameter ParaCxaEthercatMaster.ECAT_STATIS_BUF_SOE_WRITE
can be used to affect the behavior of the function block.
The default value of the parameter is 8.
The function block statically allocates 8 bytes of memory to write data when
the application is loaded. If more bytes are written with the function block,
memory is allocated dynamically in the function block while called. The
parameter can be changed and will be active when the application is loaded
again.

Implementation in ST
Beispiel:

PROGRAM EG_IL_ECATSoeWrite
VAR
  fbECATSoeWrite : IL_ECATSoeWrite;
  strMasterName : STRING := 'ethercatmaster';

  // Example A : write '2 Byte Parameter' (S-0-0000)
  uiWriteValue : UINT := 16#1234;
END_VAR

         // Example A : write '2 Byte Parameter' (S-0-0000)
         fbECATSoeWrite.Execute      := TRUE;
         fbECATSoeWrite.MasterName   := ADR(strMasterName);
         fbECATSoeWrite.SlaveAddress := 1001;
         fbECATSoeWrite.Idn          := IL_ECATSoeIdnCoding(SOE_S_PARAM,0,0); // := S-0-0000
         fbECATSoeWrite.ValueAdr     := ADR(uiWriteValue);
         fbECATSoeWrite.SizeOfValue := SIZEOF(uiWriteValue);
         fbECATSoeWrite();
         IF TRUE = fbECATSoeWrite.Done THEN
           ; // FB finished .
         END_IF
         IF TRUE = fbECATSoeWrite.Error THEN
           ; // Error handling
         END_IF

         Error description
         For more information on the error codes, refer to:
         ⮫ Chapter 13.11 Error codes on page 257
         ⮫ Diagnostics 0C0F0000

### 13.2.3 IL_ECATSoeCommand

         Brief description
         Use the function block IL_ECATSoeCommand to acyclically execute SoE com‐
         mands of an EtherCAT slave device.

         Interface description

Table 107: Interface variables of the IL_ECATSoeCommand function block
I/O type           Name               Data type                  Description

VAR_INPUT          Execute            BOOL                       Function block processing enabled (once, edge-controlled)

ClientId           ⮫ IL_HANDLE                ClientId is currently not supported (default: ClientId := 0)

MasterName         POINTER TO STRING          Instance name of the master

AddressType        ⮫ IL_ECAT_ADDRESS_TYPE     Selection of the slave addressing (EtherCAT address or AutoInc
                                              address)

SlaveAddress       UINT                       EtherCAT address or the current AutoInc address at the bus
                                              (depends on the input "AddressType")

DriveNo            BYTE                       Drive number (for single-axis device "0")

Idn                WORD                       ID number of the command parameter (refer to ⮫             IL_ECAT‐
                                              SoeIdnCoding)

KeepActive         BOOL                       Keeps the command active after processing (state-controlled)

Cancel             BOOL                       Abort of the running command (at a rising edge)

Timeout            TIME                       Timeout monitoring of internally used acyclic services

VAR_OUTPUT         Done               BOOL                       Processing completed without error. Output data valid

Active             BOOL                       Processing active. Output data invalid

I/O type             Name              Data type                      Description

CommandAborted BOOL                              Command successfully aborted and reset

Error             BOOL                           Processing completed with error. Output data invalid

ErrorID           ⮫ ERROR_CODE                   Standardized rough error classification

ErrorIdent        ⮫ ERROR_STRUCT                 Function block-specific detailed information on the error

CommandExe‐       BOOL                           Command successful
cuted

CommandStatus     ⮫ IL_ECAT_SOE_DATA_STATUS      Command parameter status

Table 108: Min./max. and default values of the inputs of the IL_ECATSoeCommand function block

Name          Data type                    Min.               Max.                          Default                          Applied

Execute       BOOL                         -                  -                             FALSE                            Continuous

ClientId      IL_HANDLE                    0                  0                             0                                Rising edge
                                                                                                        at      “Exe‐

MasterName    POINTER TO STRING            N. def.            N. def.                       0                                Rising edge
                                                                                                        at      “Exe‐

AddressType   IL_ECAT_ADDRESS_TYPE ECAT_AUTOINC_ADDRES        ECAT_ETHERCAT_ADDRESS ECAT_ETHERCAT_ADDRESS                    Rising edge
                      S                                                                                 at      “Exe‐

SlaveAddress UINT                          0                  65535                         0                                Rising edge
                                                                                                        at      “Exe‐

DriveNo       BYTE                         0                  7                             0                                Rising edge
                                                                                                        at “Exe‐

Idn           WORD                         0                  N. def.                       0                                Rising edge
                                                                                                        at “Exe‐

KeepActive    BOOL                         -                  -                             FALSE                            Continuous

Timeout       TIME                         T#1ms              N. def.                       TIME#3s0ms                       Rising edge
                                                                                                        at      “Exe‐

          Functional description
          Use the function block IL_ECATSoeCommand to acyclically execute SoE com‐
          mands of an EtherCAT slave device.
          The slave device has to support the mailbox protocol Servo drive profile
          over EtherCAT (SoE). Mailbox communication is only possible in the EtherCAT
          states PreOP, SafeOP and OP.
          The command parameter to be executed is addressed with "Idn" and
          "DriveNo". The function ⮫ IL_ECATSoeIdnCoding is recommended for Idn
          coding.
          The command is reset automatically after processing. The command execution
          can be aborted at any time via the “Cancel” input.
          After a successful command execution, the command can be kept active. If
          “KeepActive” is disabled, the command is automatically reset as well.

          Implementation in ST
          Beispiel:

        PROGRAM Example_IL_ECATSoeCommand
        VAR
          fbECATSoeCommand : IL_ECATSoeCommand;
          strMasterName    : STRING := 'ethercatmaster';
          boExecute        : BOOL := FALSE;
          uiEthercatAddr   : UINT := 1001;
        END_VAR

        // Example to execute the Reset command (S-0-0099)
        fbECATSoeCommand.Execute      := TRUE;
        fbECATSoeCommand.MasterName   := ADR(strMasterName);
        fbECATSoeCommand.SlaveAddress := 1001;
        fbECATSoeCommand.Idn          := IL_ECATSoeIdnCoding(SOE_S_PARAM,0,99); // :=
        S-0-0099
        fbECATSoeCommand();
        IF TRUE = fbECATSoeCommand.Done THEN
          ; // FB finished .
        END_IF
        IF TRUE = fbECATSoeCommand.Error THEN
          ; // Error handling
        END_IF

## 13.3 Acyclic communication CoE

### 13.3.1 IL_ECATCoeReadSdo

        Brief description
        Use the function block IL_ECATCoeReadSdo to acyclically read a Service-Data-
        Object (SDO) from an EtherCAT slave device.

        Interface description

Table 109: Interface variables of the IL_ECATCoeReadSdo function block
I/O type           Name             Data type                Description

VAR_INPUT          Execute          BOOL                     Function block processing enabled (once, edge-controlled)

ClientId         ⮫ IL_HANDLE              ClientId is currently not supported (default: ClientId := 0)

MasterName       POINTER TO STRING        Instance name of the master

AddressType      ⮫ IL_ECAT_ADDRESS_TYPE   Selection of the slave addressing (EtherCAT address or AutoInc
                                          address)

SlaveAddress     UINT                     EtherCAT address or the current AutoInc address at the bus
                                          (depends on the input "AddressType")

Index            WORD                     Object index

SubIndex         BYTE                     SubIndex of the object

CompleteAccess   BOOL                     Read the complete parameter with TRUE (all SubIndices)

I/O type           Name              Data type               Description

SizeOfValue       UDINT                   Size of the buffer or the variable in bytes to receive data
                                          (SIZEOF(Value))

ValueAdr          POINTER TO BYTE         Address   of   the   buffer   or   the   variable    to   receive    data
                                          (ADR(Value))

Timeout           TIME                    Timeout monitoring

VAR_OUTPUT         Done              BOOL                    Processing completed without error. Output data valid

Active            BOOL                    Processing active. Output data invalid

Error             BOOL                    Processing completed with error. Output data invalid

ErrorID           ⮫ ERROR_CODE            Standardized rough error classification

ErrorIdent        ⮫ ERROR_STRUCT          Function block-specific detailed information on the error

NoOfRecBytes      UDINT                   Number of bytes copied to the "ValueAdr” buffer

Table 110: Min./max. and default values of the inputs of the IL_ECATCoeReadSdo function block
Name            Data type              Min.              Max.                          Default                           Applied

Execute         BOOL                   -                 -                             FALSE                             Contin‐

ClientId        IL_HANDLE              0                 0                             0                                 Rising
                                                                                                      edge       at

MasterName      POINTER TO STRING      N. def.           N. def.                       0                                 Rising
                                                                                                      edge       at

AddressType     IL_ECAT_ADDRESS_TYPE ECAT_AUTOINC_ADDRESS ECAT_ETHERCAT_ADDRESS ECAT_ETHERCAT_ADDRESS Rising
                                                                                                      edge       at

SlaveAddress    UINT                   0                 65535                         0                                 Rising
                                                                                                      edge       at

Index           WORD                   0                 65535                         0                                 Rising
                                                                                                      edge       at

SubIndex        BYTE                   0                 255                           0                                 Rising
                                                                                                      edge       at

CompleteAccess BOOL                    -                 -                             FALSE                             Rising
                                                                                                      edge       at

SizeOfValue     UDINT                  0                 N. def.                       0                                 Contin‐

ValueAdr        POINTER TO BYTE        N. def.           N. def.                       0                                 Contin‐

Timeout         TIME                   T#1ms             N. def.                       TIME#3s0ms                        Rising
                                                                                                      edge       at

          Functional description
          Use the function block IL_ECATCoeReadSdo to acyclically read a Service-Data-
          Object (SDO) from an EtherCAT slave device.
          The slave device has to support the mailbox protocol "CAN application pro‐
          tocol over EtherCAT" (CoE). Mailbox communication is only possible in the
          EtherCAT states PreOP, SafeOP and OP.

The object to be read is addressed with “Index” and “SubIndex”.
To read all SubIndices of an object with one call, set "CompleteAccess" =
TRUE.
The “SubIndex” is set a start SubIndex:
● SubIndex = 0 → all SubIndices incl. SubIndex 0 (start SubIndex 0)
● SubIndex = 1 → all SubIndices without SubIndex 0 (start SubIndex 1)
Not all slaves support “CompleteAccess”. It can also be object-specifically.

Implementation in ST
Beispiel:

VAR
  fbECATCoeReadSdo : IL_ECATCoeReadSdo;
  strMasterName    : STRING := 'ethercatmaster';
  boExecute        : BOOL   := FALSE;
  uiEthercatAddr   : UINT   := 1001;
  wIndex           : WORD   := 16#1018; // Identity Object
  bySubIndex       : BYTE   := 1;       // Vendor ID
  udiVendorId      : UDINT;END_VAR
END_VAR

// Example A : read Vendor ID
fbECATCoeReadSdo.Execute      := TRUE;
fbECATCoeReadSdo.MasterName   := ADR(strMasterName);
fbECATCoeReadSdo.SlaveAddress := 1001;
fbECATCoeReadSdo.Index        := wIndex;
fbECATCoeReadSdo.SubIndex     := bySubIndex;
fbECATCoeReadSdo.ValueAdr     := ADR(udiVendorId);
fbECATCoeReadSdo.SizeOfValue := SIZEOF(udiVendorId);
fbECATCoeReadSdo();
IF TRUE = fbECATCoeReadSdo.Done THEN
  ; // FB finished . Vendor ID is in udiVendorId.
END_IF
IF TRUE = fbECATCoeReadSdo.Error THEN
  ; // Error handling
END_IF

Error description
For more information on the error codes, refer to:
⮫ Chapter 13.11 Error codes on page 257
⮫ Diagnostics 0C0F0000

### 13.3.2 IL_ECATCoeWriteSdo

Brief description
Use the function block IL_ECATCoeWriteSdo to acyclically write a Service-
Data-Object (SDO) from an EtherCAT slave device.

          Interface description

Table 111: Interface variables of the IL_ECATCoeWriteSdo function block
I/O type           Name              Data type                      Description

VAR_INPUT          Execute           BOOL                           Function block processing enabled (once, edge-controlled)

ClientId          ⮫ IL_HANDLE                    ClientId is currently not supported (default: ClientId := 0)

MasterName        POINTER TO STRING              Instance name of the master

AddressType       ⮫ IL_ECAT_ADDRESS_TYPE         Selection of the slave addressing (EtherCAT address or AutoInc
                                                 address)

SlaveAddress      UINT                           EtherCAT address or the current AutoInc address at the bus
                                                 (depends on the input "AddressType")

Index             WORD                           Object index

SubIndex          BYTE                           SubIndex of the object

CompleteAccess    BOOL                           Write the complete parameter with TRUE (all SubIndices)

SizeOfValue       UDINT                          Number of bytes to be written at "ValueAdr” (SIZEOF(Value))

ValueAdr          POINTER TO BYTE                Address of the buffer or the variable used to write data
                                                 (ADR(Value))

Timeout           TIME                           Timeout monitoring

VAR_OUTPUT         Done              BOOL                           Processing completed without error. Output data valid

Active            BOOL                           Processing active. Output data invalid

Error             BOOL                           Processing completed with error. Output data invalid

ErrorID           ⮫ ERROR_CODE                   Standardized rough error classification

ErrorIdent        ⮫ ERROR_STRUCT                 Function block-specific detailed information on the error

Table 112: Min./max. and default values of the inputs of the IL_ECATCoeWriteSdo function block
Name           Data type               Min.                   Max                            Default                        Effective

Execute        BOOL                    -                      -                              FALSE                          Contin‐

ClientId       IL_HANDLE               0                      0                              0                              Rising
                                                                                                         edge        at

MasterName     POINTER TO STRING       n. def.                n. def.                        0                              Rising
                                                                                                         edge        at

AddressType    IL_ECAT_ADDRESS_TYP     ECAT_AUTOINC_ADDRESS ECAT_ETHERCAT_ADDRESS ECAT_ETHERCAT_ADDRESS                     Rising
E                                                                                                            edge        at

Name             Data type               Min.             Max                  Default              Effective

SlaveAddress     UINT                    0                65535                0                    Rising
                                                                       edge        at

Index            WORD                    0                65535                0                    Rising
                                                                       edge        at

SubIndex         BYTE                    0                255                  0                    Rising
                                                                       edge        at

CompleteAccess BOOL                      -                -                    FALSE                Rising
                                                                       edge        at

SizeOfValue      UDINT                   0                n. def.              0                    Contin‐

ValueAdr         POINTER TO BYTE         n. def.          n. def.              0                    Contin‐

Timeout          TIME                    T#1ms            n. def.              TIME#3s0ms           Rising
                                                                       edge        at

Functional description
Use the function block IL_ECATCoeWriteSdo to acyclically write a Service-
Data-Object (SDO) from an EtherCAT slave device.
The slave device has to support the mailbox protocol "CAN application pro‐
tocol over EtherCAT" (CoE). Mailbox communication is only possible in the
EtherCAT states PreOP, SafeOP and OP.
The object to be written is addressed with “Index” and “SubIndex”.
To write all SubIndices of an object with one call, set "CompleteAccess" =
TRUE.
The “SubIndex” is set a start SubIndex:
● SubIndex = 0 → all SubIndices incl. SubIndex 0 (start SubIndex 0)
● SubIndex = 1 → all SubIndices without SubIndex 0 (start SubIndex 1)
Not all slaves support “CompleteAccess”. It can also be object-specifically.

The library parameter ParaCxaEthercatMaster.ECAT_STATIS_BUF_COE_WRITE
can be used to affect the behavior of the function block.
The default value of the parameter is 8.
The function block statically allocates 8 bytes of memory to write data when
the application is loaded. If more bytes are written with the function block,
memory is allocated dynamically in the function block while called. The
parameter can be changed and will be active when the application is loaded
again.

Implementation in ST
Beispiel:

PROGRAM Example_IL_ECATCoeWriteSdo
VAR
  // Example A : write 1 Byte value
  fbECATCoeWriteSdo : IL_ECATCoeWriteSdo;
  strMasterName     : STRING := 'ethercatmaster';
  uiEthercatAddr    : UINT := 1001;
  wIndex            : WORD := 16#4000; // device specific Index/SubIndex

  bySubIndex          : BYTE := 3;          // ... which is writeable!
  byWriteValue        : BYTE := 16#FF;
END_VAR

// Example A : write 1 Byte value
fbECATCoeWriteSdo.Execute      := TRUE;
fbECATCoeWriteSdo.MasterName   := ADR(strMasterName);
fbECATCoeWriteSdo.SlaveAddress := 1001;
fbECATCoeWriteSdo.Index        := wIndex;
fbECATCoeWriteSdo.SubIndex     := bySubIndex;
fbECATCoeWriteSdo.ValueAdr     := ADR(byWriteValue);
fbECATCoeWriteSdo.SizeOfValue := SIZEOF(byWriteValue);
fbECATCoeWriteSdo();

IF TRUE = fbECATCoeWriteSdo.Done THEN
  ; // FB finished . byWriteValue was written to slave.
END_IF
IF TRUE = fbECATCoeWriteSdo.Error THEN
  ; // Error handling
END_IF

Error description
For more information on the error codes, refer to:
⮫ Chapter 13.11 Error codes on page 257
⮫ Diagnostics 0C0F0000

## 13.4 Acyclic communication AoE

### 13.4.1 IL_ECATAoeGetConfigInfo

Brief description
Use the IL_ECATAoeGetConfigInfo function block to retrieve the configured
AoE NetID of an EtherCAT slave device.

Interface description

Table 113: Interface variables of the IL_ECATAoeGetConfigInfo function block
I/O type           Name           Data type                 Description

VAR_INPUT          Execute        BOOL                      Function block processing enabled

                                  (once, edge-controlled)

ClientId       ⮫ IL_HANDLE               ClientId is currently not supported

                                  (Default: ClientId := 0)

MasterName     POINTER TO STRING         Instance name of the master

AddressType    ⮫ IL_ECAT_ADDRESS_TYPE    Selecting the slave addressing

                                  (EtherCAT address or AutoInc address)

I/O type           Name                Data type                    Description

SlaveAddress        UINT                         EtherCAT address or the current AutoInc address at the bus

                                                 (depends on the input "AddressType")

Timeout             TIME                         Timeout monitoring

VAR_OUTPUT         Done                BOOL                         Processing completed without error. Output data valid

Active              BOOL                         Processing active. Output data invalid

Error               BOOL                         Processing completed with error. Output data invalid

ErrorID             ⮫ ERROR_CODE                 Standardized rough error classification

ErrorIdent          ⮫ ERROR_STRUCT               Function block-specific detailed information on the error

NetId               IL_ECAT_AOE_NET_ID           AoE NetID

Table 114: Min./max. and default values of the inputs of the IL_ECATAoeGetConfigInfo function
block
Name           Data type                        Min.                 Max.                               Default         Applied

Execute        BOOL                             -                    -                                  -               Continuous

ClientId       IL_HANDLE                        0                    0                                  0               Rising    edge
                                                                                                     at “Execute”

MasterName     POINTER TO STRING                N. def.              N. def.                            0               Rising    edge
                                                                                                     at “Execute”

AddressType    IL_ECAT_ADDRESS_TYPE             ECAT_AUTOINC_ADDRESS ECAT_ETHERCAT_ADDRESS              -               Rising    edge
                                                                                                     at “Execute”

SlaveAddress   UINT                             0                    16#FFFF                            0               Rising    edge
                                                                                                     at “Execute”

Timeout        TIME                             T#1ms                N. def.                            TIME#3s0ms      Rising    edge
                                                                                                     at “Execute”

          Functional description
          Use the IL_ECATAoeGetConfigInfo function block to retrieve the configured
          AoE NetID of an EtherCAT slave device.
          The slave device has to support the mailbox protocol "ADS application pro‐
          tocol over EtherCAT" (AoE).

          Implementation in ST
          Beispiel:

          PROGRAM Example_IL_ECATAoeGetConfigInfo
          VAR
            fbIL_ECATAoeGetConfigInfo: IL_ECATAoeGetConfigInfo;

            strMasterName        : STRING             := 'ethercatmaster'; // Instance name of the
          fieldbus master
            uiEthercatAddr       : UINT               := 1001;                // EtherCAT address of the
          EtherCAT device
          END_VAR

          //fbIL_ECATAoeGetConfigInfo.Execute        := TRUE;
          fbIL_ECATAoeGetConfigInfo.MasterName     := ADR(strMasterName);
          fbIL_ECATAoeGetConfigInfo.SlaveAddress   := uiEthercatAddr;
          fbIL_ECATAoeGetConfigInfo();
          IF TRUE = fbIL_ECATAoeGetConfigInfo.Done THEN
            ; // FB finished . result: fbIL_ECATAoeGetConfigInfo.NetId
          END_IF
          IF TRUE = fbIL_ECATAoeGetConfigInfo.Error THEN
            ; // Error handling
          END_IF

### 13.4.2 IL_ECATAoeRead

          Brief description
          Use the function block IL_ECATAoeRead to acyclically read data from an AoE
          EtherCAT slave device.

          Interface description

Table 115: Interface variables of the IL_ECATAoeRead function block
I/O type         Name              Data type                Description

VAR_INPUT        Execute           BOOL                     Function block processing enabled

                                           (once, edge-controlled)

ClientId          ⮫ IL_HANDLE              ClientId is currently not supported

                                           (Default: ClientId := 0)

MasterName        POINTER TO STRING        Instance name of the master

AddressType       ⮫ IL_ECAT_ADDRESS_TYPE   Selecting the slave addressing

                                           (EtherCAT address or AutoInc address)

SlaveAddress      UINT                     EtherCAT address or the current AutoInc address at the bus

                                           (depends on the input "AddressType")

TargetNetId       IL_RCAT_AOE_NET_ID       AoE target NetID of the slave

                                           See ⮫ IL_ECATAoeGetConfigInfo

TargetPort        UINT                     AoE TargetPort

IndexGroup        UDINT                    AoE IndexGroup

IndexOffset       UDINT                    AoE IndexOffset

SizeOfValue       UDINT                    Size of the buffer or the variable in bytes to receive data

                                           (SIZEOF(Value))

ValueAdr          POINTER TO BYTE          Address of the buffer or the variable to receive data

                                           (ADR(Value))

Timeout           TIME                     Timeout monitoring

VAR_OUTPUT       Done              BOOL                     Processing completed without error. Output data valid

Active            BOOL                     Processing active. Output data invalid

Error             BOOL                     Processing completed with error. Output data invalid

ErrorID           ⮫ ERROR_CODE             Standardized rough error classification

ErrorIdent        ⮫ ERROR_STRUCT           Function block-specific detailed information on the error

ErrorCode         UDINT                    AoE response error code

CmdResult         UDINT                    AoE reading response result

NoOfRecBytes      UDINT                    Number of bytes copied to the "ValueAdr” buffer

Table 116: Min./max. and default values of the inputs of the IL_ECATAoeRead function block
Name            Data type               Min.                    Max.                         Default              Applied

Execute         BOOL                    -                       -                            -                    Continuous

ClientId        IL_HANDLE               0                       0                            0                    Rising edge at

MasterName      POINTER TO STRING       N. def.                 N. def.                      0                    Rising edge at

AddressType     IL_ECAT_ADDRESS_TYPE ECAT_AUTOINC_ADDRES ECAT_ETHERCAT_ADDRESS               -                    Rising edge at
            S                                                                         “Execute”

SlaveAddress    UINT                    0                       16#FFFF                      0                    Rising edge at

TargetNetId     IL_RCAT_AOE_NET_ID      (0, 0, 0, 0, 0, 0)      (255, 255, 255, 255, 255,    (0, 0, 0, 0, 0, 0)   Rising edge at
                                    255)                                              “Execute”

TargetPort      UINT                    0                       16#FFFF                      0                    Rising edge at

IndexGroup      UDINT                   0                       16#FFFFFFFF                  0                    Rising edge at

IndexOffset     UDINT                   0                       16#FFFFFFFF                  0                    Rising edge at

SizeOfValue     UDINT                   0                       N. def.                      0                    Continuous

ValueAdr        POINTER TO BYTE         N. def.                 N. def.                      0                    Continuous

Timeout         TIME                    T#1ms                   N. def.                      TIME#3s0ms           Rising edge at

Functional description
Use the function block IL_ECATAoeRead to acyclically read data from an
EtherCAT slave device.
The slave device has to support the mailbox protocol "ADS application pro‐
tocol over EtherCAT" (AoE). Mailbox communication is only possible in the
EtherCAT states PreOP, SafeOP and OP.
The AoE server in the slave is addressed with "TargetNetId" and "TargetPort".
The object to be read is addressed with “IndexGroup” and “IndexOffset”.

Implementation in ST
Beispiel:

PROGRAM Example_IL_ECATAoeRead
VAR
  szVendorName     : STRING(32);

  fbIL_ECATAoERead : IL_ECATAoERead;

   strMasterName      : STRING          := 'ethercatmaster'; // Instance name of the fieldbus
master
   uiEthercatAddr     : UINT            := 1001;                // EtherCAT address of the
EtherCAT device
   strTargetNetId     : IL_ECAT_AOE_NET_ID := (Byte0 := 1, Byte1 := 2, Byte2 := 3, Byte3 :=
4,
                                                 Byte4 := 5, Byte5 := 7);       // TargetNetId =
1.2.3.4.5.7
  uiIoLinkPortNbr : UINT                := 1;        // X1 = plug, the Io-Link device is
connected
  wIoLinkIndex     : WORD               := 16;       // IO-Link Index    = 16 (vendor name)
  byIoLinkSubIndex : BYTE               := 0;        // IO-Link SubIndex = 0 (vendor name)
END_VAR

//fbIL_ECATAoERead.Execute           := TRUE;
fbIL_ECATAoERead.MasterName        := ADR(strMasterName);
fbIL_ECATAoERead.SlaveAddress      := uiEthercatAddr;
fbIL_ECATAoERead.TargetNetId       := strTargetNetId ;

       fbIL_ECATAoERead.TargetPort        := 16#1000 + uiIoLinkPortNbr;
       fbIL_ECATAoERead.IndexGroup        := 16#F302;
       fbIL_ECATAoERead.IndexOffset       := (16#FFFF0000 AND SHL(ANY_TO_UDINT(wIoLinkIndex), 16))
       OR
                                          (16#000000FF AND ANY_TO_UDINT(byIoLinkSubIndex));
       fbIL_ECATAoERead.ValueAdr       := ADR(szVendorName);
       fbIL_ECATAoERead.SizeOfValue    := SIZEOF(szVendorName);
       fbIL_ECATAoERead();
       IF TRUE = fbIL_ECATAoERead.Done THEN
         ; // FB finished . vendor name is in szVendorName.
       END_IF
       IF TRUE = fbIL_ECATAoERead.Error THEN
         ; // Error handling
       END_IF

### 13.4.3 IL_ECATAoeWrite

       Brief description
       Use the function block IL_ECATAoeWrite to acyclically write data of an AoE
       EtherCAT slave device.

       Interface description

Table 117: Interface variables of the IL_ECATAoeWrite function block
I/O type         Name             Data type                     Description

VAR_INPUT        Execute          BOOL                          Function block processing enabled

                                               (once, edge-controlled)

ClientId         ⮫ IL_HANDLE                   ClientId is currently not supported

                                               (Default: ClientId := 0)

MasterName       POINTER TO STRING             Instance name of the master

AddressType      ⮫ IL_ECAT_ADDRESS_TYPE        Selecting the slave addressing

                                               (EtherCAT address or AutoInc address)

SlaveAddress     UINT                          EtherCAT address or the current AutoInc address at the bus

                                               (depends on the input "AddressType")

TargetNetId      IL_RCAT_AOE_NET_ID            AoE target NetID of the slave

                                               See ⮫ IL_ECATAoeGetConfigInfo

TargetPort       UINT                          AoE TargetPort

IndexGroup       UDINT                         AoE IndexGroup

IndexOffset      UDINT                         AoE IndexOffset

SizeOfValue      UDINT                         Number of bytes to be written

                                               (SIZEOF(Value))

ValueAdr         POINTER TO BYTE               Address of the buffer or the variable used to write data

                                               (ADR(Value))

I/O type            Name              Data type                       Description

Timeout           TIME                            Timeout monitoring

VAR_OUTPUT          Done              BOOL                            Processing completed without error. Output data valid

Active            BOOL                            Processing active. Output data invalid

Error             BOOL                            Processing completed with error. Output data invalid

ErrorID           ⮫ ERROR_CODE                    Standardized rough error classification

ErrorIdent        ⮫ ERROR_STRUCT                  Function block-specific detailed information on the error

ErrorCode         UDINT                           AoE response error code

CmdResult         UDINT                           AoE reading response result

Table 118: Min./max. and default values of the inputs of the IL_ECATAoeWrite function block
Name             Data type                   Min.                 Max                               Default              Effective

Execute          BOOL                        -                    -                                 -                    Continuous

ClientId         IL_HANDLE                   0                    0                                 0                    Rising edge at

MasterName       POINTER TO STRING           n. def.              n. def.                           0                    Rising edge at

AddressType      IL_ECAT_ADDRESS_TYPE        ECAT_AUTOINC_ADDRES ECAT_ETHERCAT_ADDRESS              -                    Rising edge at
                         S                                                                           Execute

SlaveAddress     UINT                        0                    16#FFFF                           0                    Rising edge at

TargetNetId      IL_RCAT_AOE_NET_ID          (0, 0, 0, 0, 0, 0)   (255, 255, 255, 255, 255,         (0, 0, 0, 0, 0, 0)   Rising edge at
                                              255)                                                   Execute

TargetPort       UINT                        0                    16#FFFF                           0                    Rising edge at

IndexGroup       UDINT                       0                    16#FFFFFFFF                       0                    Rising edge at

IndexOffset      UDINT                       0                    16#FFFFFFFF                       0                    Rising edge at

SizeOfValue      UDINT                       0                    n. def.                           0                    Continuous

ValueAdr         POINTER TO BYTE             n. def.              n. def.                           0                    Continuous

Timeout          TIME                        T#1ms                n. def.                           TIME#3s0ms           Rising edge at

          Functional description
          Use the function block IL_ECATAoeRead to acyclically write data to an
          EtherCAT slave device.
          The slave device has to support the mailbox protocol "ADS application pro‐
          tocol over EtherCAT" (AoE). Mailbox communication is only possible in the
          EtherCAT states PreOP, SafeOP and OP.
          The AoE server in the slave is addressed with "TargetNetId" and "TargetPort".
          The object to be read is addressed with “IndexGroup” and “IndexOffset”.

          The library parameter ParaCxaEthercatMaster.ECAT_STATIS_BUF_AOE_WRITE
          can be used to affect the behavior of the function block.
          The default value of the parameter is 8.
          The function block statically allocates 8 bytes of memory to write data when
          the application is loaded. If more bytes are written with the function block,
          memory is allocated dynamically in the function block while called. The
          parameter can be changed and will be active when the application is loaded
          again.

Implementation in ST
Beispiel:

PROGRAM Example_IL_ECATAoeWrite
 VAR
   szApplicationTag : STRING(32)     := 'MyApplication';

    fbIL_ECATAoeWrite : IL_ECATAoeWrite;

   strMasterName      : STRING       := 'ethercatmaster'; // Instance name of the fieldbus
master
   uiEthercatAddr     : UINT         := 1001;             // EtherCAT address of the
EtherCAT device
       strTargetNetId    : IL_ECAT_AOE_NET_ID := (Byte0 := 1, Byte1 := 2, Byte2 := 3,

Byte3 := 4,
                                              Byte4 := 5, Byte5 := 7); // TargetNetId =
1.2.3.4.5.7
   uiIoLinkPortNbr    : UINT         := 1;       // X1 = plug, the Io-Link device is
connected
   wIoLinkIndex      : WORD          := 24;      // IO-Link Index    = 24 (application
spezific tag)
   byIoLinkSubIndex : BYTE           := 0;       // IO-Link SubIndex = 0 (vendor name)
END_VAR

//fbIL_ECATAoeWrite.Execute        := TRUE;
fbIL_ECATAoeWrite.MasterName     := ADR(strMasterName);
fbIL_ECATAoeWrite.SlaveAddress   := uiEthercatAddr;
fbIL_ECATAoeWrite.TargetNetId    := strTargetNetId ;
fbIL_ECATAoeWrite.TargetPort     := 16#1000 + uiIoLinkPortNbr;
fbIL_ECATAoeWrite.IndexGroup     := 16#F302;
fbIL_ECATAoeWrite.IndexOffset    := (16#FFFF0000 AND SHL(ANY_TO_UDINT(wIoLinkIndex), 16))
OR
                                    (16#000000FF AND ANY_TO_UDINT(byIoLinkSubIndex));
fbIL_ECATAoeWrite.ValueAdr       := ADR(szApplicationTag);
fbIL_ECATAoeWrite.SizeOfValue    := IL_LEN(ADR(szApplicationTag));
fbIL_ECATAoeWrite();
IF TRUE = fbIL_ECATAoeWrite.Done THEN
  ; // FB finished . szApplicationTag was written.
END_IF
IF TRUE = fbIL_ECATAoeWrite.Error THEN
  ; // Error handling
END_IF

## 13.5 Acyclic communication VoE

### 13.5.1 IL_ECATVoeRead

Brief description
The IL_ECATVoeRead function block can be used to read the "VoE - Vendor
specific protocol over EtherCAT" mailbox of a EtherCAT slave.

Interface description

Table 119: Interface variables of the IL_ECATVoeRead function block
I/O type           Name              Data type                  Description

VAR_INPUT          Execute           BOOL                       Function block processing enabled

                                      (once, edge-controlled)

ClientId          ⮫ IL_HANDLE                ClientId is currently not supported

                                      (Default: ClientId := 0)

I/O type               Name              Data type                      Description

MasterName        POINTER TO STRING              Instance name of the master

AddressType       ⮫ IL_ECAT_ADDRESS_TYPE         Selecting the slave addressing

                                                 (EtherCAT address or AutoInc address)

SlaveAddress      UINT                           EtherCAT address or the current AutoInc address at the bus

                                                 (depends on the input "AddressType")

SizeOfValue       UDINT                          Size of the buffer or the variable in bytes to receive data

                                                 (SIZEOF(Value))

ValueAdr          POINTER TO BYTE                Address of the buffer or the variable to receive data

                                                 (ADR(Value))

Timeout           TIME                           Timeout monitoring

VAR_OUTPUT             Done              BOOL                           Processing completed without error. Output data valid

Active            BOOL                           Processing active. Output data invalid

Error             BOOL                           Processing completed with error. Output data invalid

ErrorID           ⮫ ERROR_CODE                   Standardized rough error classification

ErrorIdent        ⮫ ERROR_STRUCT                 Function block-specific detailed information on the error

NoOfRecBytes      UDINT                          Number of bytes copied to the "ValueAdr” buffer

Table 120: Min./max. and default values of the inputs of the IL_ECATVoeRead function block
Name            Data type                 Min                     Max                            Default                        Effective

Execute         BOOL                      -                       -                              FALSE                          Continuous

ClientId        IL_HANDLE                 0                       0                              0                              Rising edge
                                                                                                         at Execute

MasterName      POINTER TO STRING         n. def.                 n. def.                        0                              Rising edge
                                                                                                         at Execute

AddressType     IL_ECAT_ADDRESS_TYPE ECAT_AUTOINC_ADDRESS ECAT_ETHERCAT_ADDRESS                  ECAT_ETHERCAT_ADDRES Rising edge
                                                                          S                              at Execute

SlaveAddress    UINT                      0                       65535                          0                              Rising edge
                                                                                                         at Execute

SizeOfValue     UDINT                     0                       n. def.                        0                              Continuous

ValueAdr        POINTER TO BYTE           n. def.                 n. def.                        0                              Continuous

Timeout         TIME                      T#1ms                   n. def.                        TIME#3s0ms                     Rising edge
                                                                                                         at Execute

          Functional description
          The IL_ECATVoeRead function block can be used to read the "VoE - Vendor
          specific protocol over EtherCAT" mailbox of a EtherCAT slave.
          This is possible in the EtherCAT states PreOP, SafeOP and OP.
          The "VendorID" (4 bytes) and "Vendor Type" (2 bytes) defined as VoE header
          are located at the beginning of the buffer and are therefore also part of "NoO‐
          fRecBytes". The data array follows.
          As the VoE protocol does not provide any length information, the application
          has to check the length.
          If the read buffer is smaller than the mailbox, the node reports a successful
          read operation, even if not all data was read from the mailbox. This is a
          limitation of the VoE protocol. Data may be lost. To ensure that all relevant
          data was read from the mailbox, the user has to ensure that the buffer is large
          enough to read the entire mailbox or to cover the entire length of the "Vendor
          Type" used.

Example in ST
Deklaration

PROGRAM Example_IL_ECATVoeRead
VAR
    fbECATVoeRead : IL_ECATVoeRead;
    strMasterName    : STRING := 'ethercatmaster';
    boExecute        : BOOL := FALSE;
    uiEthercatAddr   : UINT := 1001;
    abData           : ARRAY [0 .. 9] OF BYTE := [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
    udiRecBytes      : UDINT := 0;
END_VAR

Implementation

// Read VoE mailbox from a slave
fbECATVoeRead.Execute := TRUE;
fbECATVoeRead.MasterName := ADR(strMasterName);
fbECATVoeRead.SlaveAddress := uiEthercatAddr;
fbECATVoeRead.ValueAdr := ADR(abData);
fbECATVoeRead.SizeOfValue   := SIZEOF(abData);
fbECATVoeRead();

IF (TRUE = fbECATVoeRead.Done) THEN
    udiRecBytes := fbECATVoeRead.NoOfRecBytes;
    // FB finished. Use read value
END_IF

IF (TRUE = fbECATVoeRead.Error) THEN
    ; // Error
END_IF

Error description
For more information on the error codes, refer to:
⮫ Chapter 13.11 Error codes on page 257
⮫ Diagnostics 0C0F0000

### 13.5.2 IL_ECATVoeWrite

Brief description
The IL_ECATVoeWrite function block can be used to write the "VoE - Vendor
specific protocol over EtherCAT" mailbox of a EtherCAT slave.

Interface description

Table 121: Interface variables of the IL_ECATVoeWrite function block
I/O type         Name             Data type                    Description

VAR_INPUT        Execute          BOOL                         Function block processing enabled

                                       (once, edge-controlled)

ClientId         ⮫ IL_HANDLE                  ClientId is currently not supported

                                       (Default: ClientId := 0)

MasterName       POINTER TO STRING            Instance name of the master

AddressType      ⮫ IL_ECAT_ADDRESS_TYPE       Selecting the slave addressing

                                       (EtherCAT address or AutoInc address)

I/O type               Name                Data type                       Description

SlaveAddress        UINT                            EtherCAT address or the current AutoInc address at the bus

                                                    (depends on the input "AddressType")

SizeOfValue         UDINT                           Number of bytes to be written

                                                    (SIZEOF(Value))

ValueAdr            POINTER TO BYTE                 Address of the buffer or the variable used to write data

                                                    (ADR(Value))

Timeout             TIME                            Timeout monitoring

VAR_OUTPUT             Done                BOOL                            Processing completed without error. Output data valid

Active              BOOL                            Processing active. Output data invalid

Error               BOOL                            Processing completed with error. Output data invalid

ErrorID             ⮫ ERROR_CODE                    Standardized rough error classification

ErrorIdent          ⮫ ERROR_STRUCT                  Function block-specific detailed information on the error

Table 122: Min./max. and default values of the inputs of the IL_ECATVoeWrite function block
Name            Data type                  Min                   Max                            Default                       Effective

Execute         BOOL                       -                     -                              FALSE                         Continuous

ClientId        IL_HANDLE                  0                     0                              0                             Rising edge at

MasterName      POINTER TO STRING          n. def.               n. def.                        0                             Rising edge at

AddressType     IL_ECAT_ADDRESS_TYPE ECAT_AUTOINC_ADDRESS ECAT_ETHERCAT_ADDRESS ECAT_ETHERCAT_ADDRESS Rising edge at

SlaveAddress    UINT                       0                     65535                          0                             Rising edge at

SizeOfValue     UDINT                      0                     n. def.                        0                             Continuous

ValueAdr        POINTER TO BYTE            n. def.               n. def.                        0                             Continuous

Timeout         TIME                       T#1ms                 n. def.                        TIME#3s0ms                    Rising edge at

          Functional description
          The IL_ECATVoeWrite function block can be used to write the "VoE - Vendor
          specific protocol over EtherCAT" mailbox of a EtherCAT slave.
          This is possible in the EtherCAT states PreOP, SafeOP and OP.
          The VoE header with the fields "VendorId" (4 bytes) and "Vendor Type" (2
          bytes) is part of the transferred buffer and located in front of the data array.

          Example in ST
          Deklaration

          PROGRAM Example_IL_ECATVoeWrite
          VAR
              fbECATVoeWrite : IL_ECATVoeWrite;
              strMasterName    : STRING := 'ethercatmaster';
              boExecute        : BOOL := FALSE;
              uiEthercatAddr   : UINT := 1001;
              abData           : ARRAY [0 .. 9] OF BYTE := [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
          END_VAR

          Implementation

          // Writing to the VoE mailbox of a slave
          fbECATVoeWrite.Execute := TRUE;
          fbECATVoeWrite.MasterName := ADR(strMasterName);

         fbECATVoeWrite.SlaveAddress := uiEthercatAddr;
         fbECATVoeWrite.ValueAdr := ADR(abData);
         fbECATVoeWrite.SizeOfValue := SIZEOF(abData);
         fbECATVoeWrite();

         IF (TRUE = fbECATVoeWrite.Done) THEN
             ; // FB finished. Use read value
         END_IF

         IF (TRUE = fbECATVoeWrite.Error) THEN
             ; // Error
         END_IF

         Error description
         For more information on the error codes, refer to:

         ⮫ Chapter 13.11 Error codes on page 257
         ⮫ Diagnostics 0C0F0000

## 13.6 Acyclic communication register

### 13.6.1 IL_ECATReadRegister

         Brief description
         Use the IL_ECATReadRegister function block to read a memory area of the
         EtherCAT slave controller (ESC).

         Interface description

Table 123: Interface variables of the IL_ECATReadRegister function block
I/O type           Name               Data type                     Description

VAR_INPUT          Execute            BOOL                          Function block processing enabled

                                                 (once, edge-controlled)

ClientId           ⮫ IL_HANDLE                   ClientId is currently not supported

                                                 (Default: ClientId := 0)

MasterName         POINTER TO STRING             Instance name of the master

AddressType        ⮫ IL_ECAT_ADDRESS_TYPE        Selecting the slave addressing

                                                 (EtherCAT address or AutoInc address)

SlaveAddress       UINT                          EtherCAT address or the current AutoInc address at the bus

                                                 (depends on the input "AddressType")

RegisterOffset     UINT                          Register offset in the EtherCAT slave controller

SizeOfValue        UDINT                         Size of the buffer or the variable in bytes to receive data
                                                 (SIZEOF(Value))

ValueAdr           POINTER TO BYTE               Address of the buffer or the variables to receive data

                                                 (ADR(Value))

Timeout            TIME                          Timeout monitoring

VAR_OUTPUT         Done               BOOL                          Processing completed without error. Output data valid

Active             BOOL                          Processing active. Output data invalid

Error              BOOL                          Processing completed with error. Output data invalid

I/O type             Name                Data type                    Description

ErrorID             ⮫ ERROR_CODE                 Standardized rough error classification

ErrorIdent          ⮫ ERROR_STRUCT               Function block-specific detailed information on the error

NoOfRecBytes        UDINT                        Number of bytes copied to the "ValueAdr” buffer

Table 124: Min./max. and default values of the inputs of the IL_ECATReadRegister function block
Name             Data type                 Min.                 Max                          Default                      Effective

Execute          BOOL                      -                    -                            FALSE                        Continuous

ClientId         IL_HANDLE                 0                    0                            0                            Rising edge
                                                                                           at Execute

MasterName       POINTER TO STRING         n. def.              n. def.                      0                            Rising edge
                                                                                           at Execute

AddressType      IL_ECAT_ADDRESS_TYPE ECAT_AUTOINC_ADDRESS ECAT_ETHERCAT_ADDRESS ECAT_ETHERCAT_ADDRESS Rising edge
                                                                                           at Execute

SlaveAddress     UINT                      0                    65535                        0                            Rising edge
                                                                                           at Execute

RegisterOffset   UINT                      0                    16#FFFF                      0                            Rising edge
                                                                                           at Execute

SizeOfValue      UDINT                     0                    n. def.                      0                            Continuous

ValueAdr         POINTER TO BYTE           n. def.              n. def.                      0                            Continuous

Timeout          TIME                      T#1ms                n. def.                      T#3s                         Rising edge
                                                                                           at Execute

Functional description
Use the IL_ECATReadRegister function block to read a memory area (register)
of the EtherCAT slave controller (ESC).
This is possible in the EtherCAT states Init, PreOP, Bootstrap, SafeOP and OP.

Multiple consecutive registers can be read simultaneously by transferring the
sum of the individual register lengths to the "SizeOfValue" input.

Implementation in ST
Beispiel:

PROGRAM EG_IL_ECATReadRegister
VAR
  strMasterName : STRING := 'ethercatmaster';

  // Example A : read the UINT Register FeatureSupported(0x0008)
  fbECATReadRegister1 : IL_ECATReadRegister;
  uiFeatureSupported : UINT := 0;
END_VAR

// Example A : read the UINT Register FeatureSupported(0x0008)
fbECATReadRegister1.Execute      := TRUE;
fbECATReadRegister1.MasterName   := ADR(strMasterName);
fbECATReadRegister1.SlaveAddress := 1001;
fbECATReadRegister1.RegisterOffset := 8;
fbECATReadRegister1.ValueAdr     := ADR(uiFeatureSupported);
fbECATReadRegister1.SizeOfValue := SIZEOF(uiFeatureSupported);
fbECATReadRegister1();
IF TRUE = fbECATReadRegister1.Done THEN
  ; // FB finished . read result is in uiFeatureSupported
END_IF
IF TRUE = fbECATReadRegister1.Error THEN
  ; // Error handling
END_IF

          Error description
          For more information on the error codes, refer to:
          ⮫ Chapter 13.11 Error codes on page 257
         ⮫ Diagnostics 0C0F0000

### 13.6.2 IL_ECATWriteRegister

          Brief description
          Use the IL_ECATWriteRegister function block to write a memory area of the
          EtherCAT slave controller (ESC).

          Interface description

Table 125: Interface variables of the IL_ECATWriteRegister function block
I/O type          Name              Data type                      Description

VAR_INPUT         Execute           BOOL                           Function block processing enabled

                                                 (once, edge-controlled)

ClientId          ⮫ IL_HANDLE                    ClientId is currently not supported

                                                 (Default: ClientId := 0)

MasterName        POINTER TO STRING              Instance name of the master

AddressType       ⮫ IL_ECAT_ADDRESS_TYPE         Selecting the slave addressing

                                                 (EtherCAT address or AutoInc address)

SlaveAddress      UINT                           EtherCAT address or the current AutoInc address at the bus

                                                 (depends on the input "AddressType")

RegisterOffset    UINT                           Register offset in the EtherCAT slave controller

SizeOfValue       UDINT                          Number of bytes to be written at "ValueAdr"

                                                 (SIZEOF(Value))

ValueAdr          POINTER TO BYTE                Address of the buffer or the variable used to write data

                                                 (ADR(Value))

Timeout           TIME                           Timeout monitoring

VAR_OUTPUT        Done              BOOL                           Processing completed without error. Output data valid

Active            BOOL                           Processing active. Output data invalid

Error             BOOL                           Processing completed with error. Output data invalid

ErrorID           ⮫ ERROR_CODE                   Standardized rough error classification

ErrorIdent        ⮫ ERROR_STRUCT                 Function block-specific detailed information on the error

Table 126: Min./max. and default values of the inputs of the IL_ECATWriteRegister function block
Name          Data type              Min.                    Max                              Default                     Effective

Execute       BOOL                   -                       -                                FALSE                       Continuous

ClientId      IL_HANDLE              0                       0                                0                           Rising edge
                                                                                                        at Execute

MasterName    POINTER TO STRING      n. def.                 n. def.                          0                           Rising edge
                                                                                                        at Execute

Name            Data type               Min.                 Max                        Default                Effective

AddressType     IL_ECAT_ADDRESS_TYPE ECAT_AUTOINC_ADDRESS ECAT_ETHERCAT_ADDRESS         ECAT_ETHERCAT_ADDRES   Rising edge
                                                            S                      at Execute

SlaveAddress    UINT                    0                    65535                      0                      Rising edge
                                                                                   at Execute

RegisterOffset UINT                     0                    16#FFFF                    0                      Rising edge
                                                                                   at Execute

SizeOfValue     UDINT                   0                    n. def.                    0                      Continuous

ValueAdr        POINTER TO BYTE         n. def.              n. def.                    0                      Continuous

Timeout         TIME                    T#1ms                n. def.                    T#3s                   Rising edge
                                                                                   at Execute

Functional description
Use the IL_ECATReadRegister function block to read a memory area (register)
of the EtherCAT slave controller (ESC).
This is possible in the EtherCAT states Init, PreOP, Bootstrap, SafeOP and OP.

Multiple consecutive registers can be written simultaneously by transferring
the sum of the individual register lengths to the "SizeOfValue" input.

Implementation in ST
Beispiel:

PROGRAM EG_IL_ECATWriteRegister
VAR
  strMasterName : STRING := 'ethercatmaster';

  // Example A : write the UINT Register AlControl (16#120)
  fbECATWriteRegister1 : IL_ECATWriteRegister;
  uiAlControl : UINT := 4;
END_VAR

// Example A : write the UINT Register AlControl (16#120)
fbECATWriteRegister1.Execute      := TRUE;
fbECATWriteRegister1.MasterName   := ADR(strMasterName);
fbECATWriteRegister1.SlaveAddress := 1001;
fbECATWriteRegister1.RegisterOffset := 16#120;
fbECATWriteRegister1.ValueAdr     := ADR(uiAlControl);
fbECATWriteRegister1.SizeOfValue := SIZEOF(uiAlControl);
fbECATWriteRegister1();
IF TRUE = fbECATWriteRegister1.Done THEN
  ; // FB finished . cycle time is in uiCycleTime.
END_IF
IF TRUE = fbECATWriteRegister1.Error THEN
  ; // Error handling
END_IF

Error description
For more information on the error codes, refer to:
⮫ Chapter 13.11 Error codes on page 257
⮫ Diagnostics 0C0F0000

## 13.7 Diagnostics

### 13.7.1 IL_ECATGetConfigEthercatAddrList

Brief description
The IL_ECATGetConfigEthercatAddrList function block is used to provide the
addresses (ECAT_ETHERCAT_ADDRESS) of the configured slaves.

              Interface description

Table 127: Interface variables of the IL_ECATGetConfigEthercatAddrList function block

I/O type       Name                   Data type             Initial value   Description

VAR_INPUT      Execute                BOOL                                  Function block processing enabled

                                                             (once, edge-controlled)

ClientId               ⮫ IL_HANDLE           0               ClientId is currently not supported

                                                             (Default: ClientId := 0)

MasterName             POINTER TO STRING                     Instance name of the master

SizeOfEthercatAddrList UDINT                 0               Size of "EthercatAddrList" (SIZEOF(EthercatAddrList))

EthercatAddrListAdr    POINTER TO UINT       0               Pointer to "EthercatAddrList" (ADR(EthercatAddrList))

Timeout                TIME                  TIME#3s0ms      Timeout monitoring

VAR_OUTPUT     Done                   BOOL                                  Processing completed without error. Output data valid

Active                 BOOL                                  Processing active. Output data invalid

Error                  BOOL                                  Processing completed with error. Output data invalid

ErrorID                ⮫ ERROR_CODE                          Standardized rough error classification

ErrorIdent             ⮫ ERROR_STRUCT                        Function block-specific detailed information on the error

NumConfigSlaves        UDINT                 0               Number of configured slaves (= number of entries in
                                                             "EthercatAddrList")

Table 128: Min./max. and default values of the inputs of the IL_ECATGetConfigEthercatAddrList
function block
Name                     Data type                Min.          Max           Default              Effective

Execute                  BOOL                     -             -             FALSE                Continuous

ClientId                 IL_HANDLE                0             0             0                    Rising edge at Execute

MasterName               POINTER TO STRING        n. def.       n. def.       0                    Rising edge at Execute

SizeOfEthercatAddrList UDINT                      0             n. def.       0                    Rising edge at Execute

EthercatAddrListAdr      POINTER TO UINT          n. def.       n. def.       n. def.              Continuous

Timeout                  TIME                     T#1ms         n. def.       T#3s                 Rising edge at Execute

              Functional description
              A pointer to a UINT array with ADR(ArrayName) and its size with
              SIZEOF(ArrayName) is transferred to a pointer. The array has to contain at
              least the same number of elements as configured EtherCAT slaves.
              When the function block is called successfully, the addresses of the config‐
              ured slaves are written to the array in the format "EthercatAddr". Addresses
              from position 0 are written to the array until all addresses are entered into
              the array. Data in the array is thus overwritten. If the array contains more
              elements than configured slaves, the positions after NumConfigSlaves -1 are
              not changed. To reliably iterate over the addresses in the array after calling
              the function block, use the output value "NumConfigSlaves".

              Programming example

PROGRAM Example_IL_ECATGetConfigEthercatAddrList
VAR
  szMasterName                       : STRING    := 'ethercatmaster'; // Instance name of
the fieldbus master
  udiNumConfigSlaves                 : UDINT     := 0;                // returns number of
configured slaves
  fbIL_ECATGetConfigEthercatAddrList : IL_ECATGetConfigEthercatAddrList;
  uiarAddressList                    : ARRAY [0..10] OF UINT;         // must have at
least 'udiNumConfigSlaves' elements, dependent on current ethercat configuration.

  udiIdx           : UDINT;
  uiCurrentAddress : UINT;
END_VAR

//fbIL_ECATMasterState.Execute       := TRUE;
fbIL_ECATGetConfigEthercatAddrList.MasterName    := ADR(szMasterName);
fbIL_ECATGetConfigEthercatAddrList.EthercatAddrListAdr := ADR(uiarAddressList);
fbIL_ECATGetConfigEthercatAddrList.SizeOfEthercatAddrList:= SIZEOF(uiarAddressList);
fbIL_ECATGetConfigEthercatAddrList();
IF TRUE = fbIL_ECATGetConfigEthercatAddrList.Done THEN
  udiNumConfigSlaves := fbIL_ECATGetConfigEthercatAddrList.NumConfigSlaves; // FB
finished. Result of the FB is number of configured slaves
  FOR udiIdx := 0 TO (udiNumConfigSlaves -1) DO // Example for iteration over all written
addresses in the array
       uiCurrentAddress:= uiarAddressList[udiIdx]; // Do something with the address
  END_FOR
END_IF
IF TRUE = fbIL_ECATGetConfigEthercatAddrList.Error THEN
  ; // Error handling
END_IF

Error description
If the function block returns the error "Ecat: Invalid size", increase the array
size. The array has to include at least "CategoryCount" elements.
For more information on the error codes, refer to:
⮫ Chapter 13.11 Error codes on page 257
⮫ Diagnostics 0C0F0000

### 13.7.2 IL_ECATGetEthercatAddrByName

Brief description
The IL_ECATGetEthercatAddrByName function block returns the EtherCAT
address of a configured slave when the name of the slave is transferred to
the function block.

Interface description

Table 129: Interface variables of the IL_ECATGetEthercatAddrByName function block
I/O type           Name             Data type                  Description

VAR_INPUT          Execute          BOOL                       Function block processing enabled

                                     (once, edge-controlled)

ClientId         ⮫ IL_HANDLE                ClientId is currently not supported

                                     (Default: ClientId := 0)

I/O type          Name                Data type                   Description

MasterName          POINTER TO STRING           Instance name of the master

SlaveName           POINTER TO STRING           Slave name

Timeout             TIME                        Timeout monitoring

VAR_OUTPUT        Done                BOOL                        Processing completed without error. Output data valid

Active              BOOL                        Processing active. Output data invalid

Error               BOOL                        Processing completed with error. Output data invalid

ErrorID             ⮫ ERROR_CODE                Standardized rough error classification

ErrorIdent          ⮫ ERROR_STRUCT              Function block-specific detailed information on the error

EthercatAddress     UDINT                       EtherCAT address of the slave

Table 130: Min./max. and default values of the inputs of the IL_ECATGetEthercatAddrByName
function block
Name             Data type                        Min.      Max             Default         Effective

Execute          BOOL                             -         -               FALSE           Continuous

ClientId         IL_HANDLE                        0         0               0               Rising edge at Execute

MasterName       POINTER TO STRING                n. def.   n. def.         0               Rising edge at Execute

SlaveName        POINTER TO STRING                n. def.   n. def.         0               Rising edge at Execute

Timeout          TIME                             T#1ms     n. def.         T#3s            Rising edge at Execute

          Functional description
          The IL_ECATGetEthercatAddrByName function block returns the EtherCAT
          address of a configured slave when the name of the slave is transferred to
          the function block.

          The function block can only process slave names with up to 80 characters.

          Programming example

          PROGRAM EG_IL_ECATGetEthercatAddrByName
          VAR
            strMasterName          : STRING := 'ethercatmaster'; // Instance name of the fieldbus
          master
            strSlaveName           : STRING := 'NXIO_100_RE_ECS';

            fbIL_ECATGetEthercatAddrByName : IL_ECATGetEthercatAddrByName;
            uiEthercatAddress: UINT;
          END_VAR

          fbIL_ECATGetEthercatAddrByName.Execute      := TRUE;
          fbIL_ECATGetEthercatAddrByName.MasterName   := ADR(strMasterName);
          fbIL_ECATGetEthercatAddrByName.SlaveName    := ADR(strSlaveName);
          fbIL_ECATGetEthercatAddrByName();
          IF fbIL_ECATGetEthercatAddrByName.Done THEN
            uiEthercatAddress := fbIL_ECATGetEthercatAddrByName.EthercatAddress;
          END_IF

          Error description
          For more information on the error codes, refer to:
          ⮫ Chapter 13.11 Error codes on page 257
         ⮫ Diagnostics 0C0F0000

### 13.7.3 IL_ECATGetNumConfigMailboxSlaves

          Brief description
          The function block IL_ECATGetNumConfigMailboxSlaves returns the number of
          configured slaves with mailbox support.

             Interface description

Table 131: Interface variables of the IL_ECATGetNumConfigMailboxSlaves function block
I/O type       Name            Data type                  Initial value   Description

VAR_INPUT      Execute         BOOL                                       Function block processing enabled

                                                           (once, edge-controlled)

ClientId        ⮫ IL_HANDLE                0               ClientId is currently not supported

                                                           (Default: ClientId := 0)

MasterName      POINTER TO STRING                          Instance name of the master

Timeout         TIME                       TIME#3s0ms Timeout monitoring

VAR_OUTPUT     Done            BOOL                                       Processing completed without error. Output data valid

Active          BOOL                                       Processing active. Output data invalid

Error           BOOL                                       Processing completed with error. Output data invalid

ErrorID         ⮫ ERROR_CODE                               Standardized rough error classification

ErrorIdent      ⮫ ERROR_STRUCT                             Function block-specific detailed information on the error

NumConfig‐      UDINT                      0               Number of slaves with mailbox functionality
MailboxSlaves

Table 132: Min./max. and default values of the inputs of the IL_ECATGetNumConfigMailboxSlaves
function block
Name               Data type                    Min.                  Max                  Default                 Effective

Execute            BOOL                         -                     -                    FALSE                   Continuous

ClientId           IL_HANDLE                    0                     0                    0                       Rising edge at Execute

MasterName         POINTER TO STRING            n. def.               n. def.              0                       Rising edge at Execute

Timeout            TIME                         T#1ms                 n. def.              T#3s                    Rising edge at Execute

             Functional description
             The function block IL_ECATGetNumConfigMailboxSlaves returns the number of
             configured slaves with mailbox support.

             Declaration CodeExample

             PROGRAM Example_IL_ECATGetNumConfigMailboxSlaves
             VAR
               strMasterName                      : STRING := 'ethercatmaster';                             // Instance name
             of the fieldbus master
               fbIL_ECATGetNumConfigMailboxSlaves : IL_ECATGetNumConfigMailboxSlaves;                       // Instance of
             function block IL_ECATGetNumConfigMailboxSlaves
               udiNumConfigMailboxSlaves          : UDINT := 0;                                             // Result of the
             FB is number of configured mailbox slaves
               bExecute                           : BOOL   := FALSE;
             END_VAR

             Implementation CodeExample

          fbIL_ECATGetNumConfigMailboxSlaves.Execute      := bExecute;
          fbIL_ECATGetNumConfigMailboxSlaves.MasterName   := ADR(strMasterName);
          fbIL_ECATGetNumConfigMailboxSlaves();
          IF TRUE = fbIL_ECATGetNumConfigMailboxSlaves.Done THEN
            udiNumConfigMailboxSlaves :=
          fbIL_ECATGetNumConfigMailboxSlaves.NumConfigMailboxSlaves; // FB finished. Result of the
          FB is number of configured mailbox slaves
          END_IF
          IF TRUE = fbIL_ECATGetNumConfigMailboxSlaves.Error THEN
            ; // Error handling
          END_IF

          Error description
          For more information on the error codes, refer to:

          ⮫ Chapter 13.11 Error codes on page 257
          ⮫ Diagnostics 0C0F0000

### 13.7.4 IL_ECATGetNumConfigSlaves

          Brief description
          The function block IL_ECATGetNumConfigSlaves returns the number of config‐
          ured slaves in the EtherCAT master.

          Interface description

Table 133: Interface variables of the IL_ECATGetNumConfigSlaves function block
I/O type          Name                 Data type                 Description

VAR_INPUT         Execute              BOOL                      Function block processing enabled (once, edge-controlled)

ClientId             ⮫ IL_HANDLE               ClientId is currently not supported

                                               (Default: ClientId := 0)

MasterName           POINTER TO STRING         Instance name of the master

Timeout              TIME                      Timeout monitoring

VAR_OUTPUT        Done                 BOOL                      Processing completed without error. Output data valid

Active               BOOL                      Processing active. Output data invalid

Error                BOOL                      Processing completed with error. Output data invalid

ErrorID              ⮫ ERROR_CODE              Standardized rough error classification

ErrorIdent           ⮫ ERROR_STRUCT            Function block-specific detailed information on the error

NumConfigSlaves      UDINT                     Number of configured slaves in the EtherCAT master

Table 134: Min./max. and default values of the inputs of the IL_ECATGetNumConfigSlaves function
block
Name            Data type          Min.                 Max.            Default             Applied

Execute         BOOL               -                    -               FALSE               Continuous

ClientId        IL_HANDLE          0                    0               0                   Rising edge at “Execute”

MasterName      POINTER         TO n.def.               n.def.          0                   Rising edge at “Execute”
STRING

Functional description
The function block IL_ECATGetNumConfigSlaves returns the number of config‐
ured slaves in the EtherCAT master.

Implementation in ST (example)
Deklaration:

PROGRAM Example_IL_ECATGetNumConfigSlaves
VAR
  szMasterName       : STRING    := 'ethercatmaster'; // Instance name of the
fieldbus master
  udiNumConfigSlaves : UDINT     := 0;                // result of the FB is
number of configured slaves
  fbIL_ECATGetNumConfigSlaves : IL_ECATGetNumConfigSlaves;
END_VAR

Implementation:

//fbIL_ECATMasterState.Execute      := TRUE;
fbIL_ECATGetNumConfigSlaves.MasterName   := ADR(szMasterName);
fbIL_ECATGetNumConfigSlaves();
IF TRUE = fbIL_ECATGetNumConfigSlaves.Done THEN
  udiNumConfigSlaves := fbIL_ECATGetNumConfigSlaves.NumConfigSlaves; // FB
finished. Result of the
                                                                     // FB is
number of configured
                                                                     // slaves
END_IF
IF TRUE = fbIL_ECATGetNumConfigSlaves.Error THEN
  ; // Error handling
END_IF

### 13.7.5 IL_ECATGetNumOnlineDcSlaves

Brief description
The function block IL_ECATGetNumOnlineDcSlaves returns the number of con‐
nected DC (Distributed Clocks) slaves.

Interface description

Table 135: Interface variables of the IL_ECATGetNumOnlineDcSlaves function block
I/O type      Name               Data type           Initial value   Description

VAR_INPUT     Execute            BOOL                                Function block processing enabled

                                          (once, edge-controlled)

ClientId           ⮫ IL_HANDLE         0               ClientId is currently not supported

                                          (Default: ClientId := 0)

MasterName         POINTER TO STRING                   Instance name of the master

Timeout            TIME                TIME#3s0ms      Timeout monitoring

VAR_OUTPUT    Done               BOOL                                Processing completed without error. Output data valid

I/O type      Name               Data type                Initial value             Description

Active             BOOL                                               Processing active. Output data invalid

Error              BOOL                                               Processing completed with error. Output data invalid

ErrorID            ⮫ ERROR_CODE                                       Standardized rough error classification

ErrorIdent         ⮫ ERROR_STRUCT                                     Function block-specific detailed information on the
                                                         error

NumOnlineDcSlaves UDINT                     0                         Number of DC (Distributed Clocks) slaves

Table 136: Min./max. and default values of the inputs of the IL_ECATGetNumOnlineDcSlaves
function block

Name           Data type                Min.        Max                   Default                    Effective

Execute        BOOL                     -           -                     FALSE                      Continuous

ClientId       IL_HANDLE                0           0                     0                          Rising edge at Execute

MasterName     POINTER TO STRING        n. def.     n. def.               0                          Rising edge at Execute

Timeout        TIME                     T#1ms       n. def.               T#3s                       Rising edge at Execute

Functional description
The function block IL_ECATGetNumOnlineDcSlaves returns the number of con‐
nected DC (Distributed Clocks) slaves.

Declaration CodeExample

PROGRAM Example_IL_ECATGetNumOnlineSlaves
VAR
  szMasterName: STRING:= 'ethercatmaster'; // Instance name of the fieldbus master
  udiNumOnlineDcSlaves : UDINT     := 0;   // Result of the FB is number of online DC
slaves
  fbIL_ECATGetNumOnlineDcSlaves : IL_ECATGetNumOnlineDcSlaves;
END_VAR

Implementation CodeExample

fbIL_ECATGetNumOnlineDcSlaves.Execute     := TRUE;
fbIL_ECATGetNumOnlineDcSlaves.MasterName   := ADR(szMasterName);
fbIL_ECATGetNumOnlineDcSlaves();
IF TRUE = fbIL_ECATGetNumOnlineDcSlaves.Done THEN
  udiNumOnlineDcSlaves := fbIL_ECATGetNumOnlineDcSlaves.NumOnlineDcSlaves; // FB finished.
Result of the FB is number of online DC slaves
END_IF
IF TRUE = fbIL_ECATGetNumOnlineDcSlaves.Error THEN
  ; // Error handling
END_IF

Error description
For more information on the error codes, refer to:
⮫ Chapter 13.11 Error codes on page 257
⮫ Diagnostics 0C0F0000

### 13.7.6 IL_ECATGetNumOnlineSlaves

Brief description
The function block IL_ECATGetNumOnlineSlaves returns the number of slaves
currently connected to the EtherCAT master.

          Interface description

Table 137: Interface variables of the IL_ECATGetNumOnlineSlaves function block
I/O type           Name                 Data type                 Description

VAR_INPUT          Execute              BOOL                      Function block processing enabled (once, edge-controlled)

ClientId             ⮫ IL_HANDLE               ClientId is currently not supported

                                               (Default: ClientId := 0)

MasterName           POINTER TO STRING         Instance name of the master

VAR_OUTPUT         Done                 BOOL                      Processing completed without error. Output data valid

Active               BOOL                      Processing active. Output data invalid

Error                BOOL                      Processing completed with error. Output data invalid

ErrorID              ⮫ ERROR_CODE              Standardized rough error classification

ErrorIdent           ⮫ ERROR_STRUCT            Function block-specific detailed information on the error

NumOnlineSlaves      UDINT                     Number of currently connected slaves at the EtherCAT master

Table 138: Min./max. and default values of the inputs of the IL_ECATGetNumOnlineSlaves function
block
Name            Data type           Min.                 Max.            Default             Applied

Execute         BOOL                -                    -               FALSE               Continuous

ClientId        IL_HANDLE           0                    0               0                   Rising edge at Execute

MasterName      POINTER          TO n.def.               n.def.          0                   Rising edge at “Execute”
STRING

          Functional description
          The function block IL_ECATGetNumOnlineSlaves returns the number of cur‐
          rently connected slaves at the EtherCAT master.

          Implementation in ST (example)
          Deklaration:

          PROGRAM Example_IL_ECATGetNumOnlineSlaves
          VAR
            szMasterName         : STRING    := 'ethercatmaster'; // Instance name of the fieldbus
          master
            udiNumOnlineSlaves   : UDINT     := 0;                //Result of the FB is number of
          online slaves
            fbIL_ECATGetNumOnlineSlaves : IL_ECATGetNumOnlineSlaves;
          END_VAR

          Implementation:

          //fbIL_ECATMasterState.Execute      := TRUE;
          fbIL_ECATGetNumOnlineSlaves.MasterName   := ADR(szMasterName);
          fbIL_ECATGetNumOnlineSlaves();
          IF TRUE = fbIL_ECATGetNumOnlineSlaves.Done THEN
            udiNumOnlineSlaves := fbIL_ECATGetNumOnlineSlaves.NumOnlineSlaves; // FB finished.
          Result of the FB is number of online slaves

          END_IF
          IF TRUE = fbIL_ECATGetNumOnlineSlaves.Error THEN
            ; // Error handling
          END_IF

### 13.7.7 IL_ECATGetSlaveConfigInfo

          Brief description
          Information on a configured slave can be retrieved from the EtherCAT master
          using the IL_ECATGetSlaveConfigInfo function block.

          Interface description

Table 139: Interface variables of the IL_ECATGetSlaveConfigInfo function block
I/O type           Name                Data type                        Description

VAR_INPUT          Execute             BOOL                             Function block processing enabled (once, edge-controlled)

ClientId            ⮫ IL_HANDLE                      ClientId is currently not supported

                                                     (Default: ClientId := 0)

MasterName          POINTER TO STRING                Instance name of the master

AddressType         IL_ECAT_ADDRESS_TYPE             Selection of the slave addressing (EtherCAT address or AutoInc
                                                     address)

SlaveAddress        UINT                             EtherCAT address or the configured AutoInc address (depends on
                                                     the input "AddressType")

VAR_OUTPUT         Done                BOOL                             Processing completed without error. Output data valid

Active              BOOL                             Processing active. Output data invalid

Error               BOOL                             Processing completed with error. Output data invalid

ErrorID             ⮫ ERROR_CODE                     Standardized rough error classification

ErrorIdent          ⮫ ERROR_STRUCT                   Function block-specific detailed information on the error

SlaveConfigInfo     ⮫ IL_ECAT_SLAVE_CONFIG_INFO Information on a configured slave

Table 140: Min./max. and default values of the inputs of the IL_ECATGetSlaveConfigInfo function
block
Name           Data type                Min.                     Max.                              Default                     Applied

Execute        BOOL                     -                        -                                 FALSE                       Contin‐

ClientId       IL_HANDLE                0                        0                                 0                           Rising
                                                                                                            edge      at

MasterName     POINTER TO STRING        n.def.                   n.def.                            0                           Rising
                                                                                                            edge      at

AddressType    IL_ECAT_ADDRESS_TYPE ECAT_AUTOINC_ADDRESS ECAT_ETHERCAT_ADDRESS ECAT_ETHERCAT_ADDRESS                           Rising
                                                                                                            edge      at

SlaveAddress   UINT                     0                        65535                             0                           Rising
                                                                                                            edge      at

Functional description
Information on a configured slave can be retrieved from the EtherCAT master
using the IL_ECATGetSlaveConfigInfo function block.
During the EtherCAT configuration of the slaves, the AutoInc address has to be
specified continuously without gaps (0, 0xFFFF (-1), 0xFFFE (-2), …). Thus, all
information data of all configured slaves can be retrieved using a simple loop
(refer to the following programming example).

Implementation in ST (example)
Deklaration:

PROGRAM Example_IL_ECATGetSlaveConfigInfo
VAR
  strMasterName     : STRING     := 'ethercatmaster'; // Instance name of the
fieldbus master
  uiEthercatAddr    : UINT       := 1001;             // EtherCAT address of
the EtherCAT device

  fbIL_ECATGetSlaveConfigInfo : IL_ECATGetSlaveConfigInfo;
END_VAR

Implementation:

fbIL_ECATGetSlaveConfigInfo.Execute      := TRUE;
fbIL_ECATGetSlaveConfigInfo.MasterName   := ADR(strMasterName);
fbIL_ECATGetSlaveConfigInfo.SlaveAddress := uiEthercatAddr;
fbIL_ECATGetSlaveConfigInfo();
IF TRUE = fbIL_ECATGetSlaveConfigInfo.Done THEN
  ;// FB finished. Result of the FB is configuration information of the slave
in fbIL_ECATGetSlaveConfigInfo.SlaveConfigInfo.
END_IF
IF TRUE = fbIL_ECATGetSlaveConfigInfo.Error THEN
  ; // Error handling
END_IF

### 13.7.8 IL_ECATGetSlaveOnlineInfo

Brief description
Information on a currently connected slave can be retrieved from the EtherCAT
master using the IL_ECATGetSlaveOnlineInfo function block.

Interface description

Table 141: Interface variables of the IL_ECATGetSlaveOnlineInfo function block
I/O type           Name           Data type                Description

VAR_INPUT          Execute        BOOL                     Function block processing enabled (once, edge-controlled)

ClientId       ⮫ IL_HANDLE              ClientId is currently not supported

                                 (Default: ClientId := 0)

MasterName     POINTER TO STRING        Instance name of the master

AddressType    IL_ECAT_ADDRESS_TYPE     Selection of the slave addressing (EtherCAT address or AutoInc
                                 address)

I/O type             Name              Data type                       Description

SlaveAddress      UINT                            EtherCAT address or the current AutoInc address (depends on
                                                  the input "AddressType")

Timeout           TIME                            Timeout monitoring

VAR_OUTPUT           Done              BOOL                            Processing completed without error. Output data valid

Active            BOOL                            Processing active. Output data invalid

Error             BOOL                            Processing completed with error. Output data invalid

ErrorID           ⮫ ERROR_CODE                    Standardized rough error classification

ErrorIdent        ⮫ ERROR_STRUCT                  Function block-specific detailed information on the error

SlaveOnlineInfo   ⮫ IL_ECAT_SLAVE_ONLINE_INFO Information on a currently connected slave

Table 142: Min./max. and default values of the inputs of the IL_ECATGetSlaveOnlineInfo function
block
Name          Data type                 Min.                    Max.                          Default                     Applied

Execute       BOOL                      -                       -                             FALSE                       Continuous

ClientId      IL_HANDLE                 0                       0                             0                           Rising edge at

MasterName    POINTER TO STRING         n.def.                  n.def.                        0                           Rising edge at

AddressType   IL_ECAT_ADDRESS_TYPE      ECAT_AUTOINC_ADDRESS ECAT_ETHERCAT_ADDRESS ECAT_ETHERCAT_ADDRES                   Rising edge at
                                                                         S                           “Execute”

SlaveAddress UINT                       0                       65535                         0                           Rising edge at

Timeout       TIME                      T#1ms                   n. def.                       TIME#3s0ms                  Rising edge at

          Functional description
          Information on a currently connected slave can be retrieved from the EtherCAT
          master using the IL_ECATGetSlaveOnlineInfo function block.
          The EtherCAT executes a bus scan automatically if a change in the topology
          was detected ("DL status event"). The IL_ECATGetSlaveOnlineInfo function
          retrieves the collected data from the EtherCAT master.

          Implementation in ST (example)
          Deklaration:

          PROGRAM Example_IL_ECATGetSlaveOnlineInfo
          VAR
            strMasterName     : STRING              := 'ethercatmaster'; // Instance name
          of the fieldbus master
            uiEthercatAddr    : UINT                := 1001;             // EtherCAT
          address of the EtherCAT device

            fbIL_ECATGetSlaveOnlineInfo : IL_ECATGetSlaveOnlineInfo;
          END_VAR

          Implementation:

          //fbIL_ECATGetSlaveConfigInfo.Execute      := TRUE;
          fbIL_ECATGetSlaveOnlineInfo.MasterName   := ADR(strMasterName);
          fbIL_ECATGetSlaveOnlineInfo.SlaveAddress := uiEthercatAddr;
          fbIL_ECATGetSlaveOnlineInfo();
          IF TRUE = fbIL_ECATGetSlaveOnlineInfo.Done THEN
            ;// FB finished. Result of the FB is configuration information of the slave
          in fbIL_ECATGetSlaveOnlineInfo.SlaveOnlineInfo.
          END_IF

          IF TRUE = fbIL_ECATGetSlaveOnlineInfo.Error THEN
            ; // Error handling
          END_IF

### 13.7.9 IL_ECATMasterState

          Brief description
          The function block IL_ECATMasterState provides a summary of the diagnostic
          information on the EtherCAT master.

          Interface description

Table 143: Interface variables of the IL_ECATMasterState function block
I/O type           Name                 Data type                 Description

VAR_INPUT          Enable               BOOL                      Function block processing enabled (permanent, level-controlled)

ClientId             ⮫ IL_HANDLE               ClientId is currently not supported

                                               (Default: ClientId := 0)

MasterName           POINTER TO STRING         Instance name of the master

VAR_OUTPUT         InOperation          BOOL                      Cyclic processing state

Error                BOOL                      Processing completed with error

ErrorID              ⮫ ERROR_CODE              Standardized rough error classification

ErrorIdent           ⮫ ERROR_STRUCT            Function block-specific detailed information on the error

State                DWORD                     Diagnostic status information on the EtherCAT master

                                               For details, refer to ⮫ IL_ECAT_MASTER_STATE

Table 144: Min./max. and default values of the inputs of the IL_ECATMasterState function block
Name            Data type           Min.                 Max.            Default             Applied

Enable          BOOL                -                    -               FALSE               Continuous

ClientId        IL_HANDLE           0                    0               0                   Rising edge at Execute

MasterName      POINTER          TO n.def.               n.def.          0                   Rising edge at “Enable”
STRING

          Functional description
          The function block IL_ECATMasterState provides a summary of the diagnostic
          information of the EtherCAT master.
          If the output "State" = 0, no diagnostics is present and the master is OK.
          For a description of the diagnostic bits of the "State” output, refer to the
          structure IL_ECAT_MASTER_STATE and to the auxiliary function IL_ECATMaster‐
          StateDecoding.

          Implementation in ST (example)
          Deklaration:

          PROGRAM Example_IL_ECATMasterState
          VAR
            szMasterName     : STRING            := 'ethercatmaster'; // Instance name
          of the fieldbus master
            strMasterStatus : IL_ECAT_MASTER_STATE;

            fbIL_ECATMasterState : IL_ECATMasterState;
          END_VAR

          Implementation:

          //fbIL_ECATMasterState.Execute      := TRUE;
          fbIL_ECATMasterState.MasterName   := ADR(szMasterName);

          fbIL_ECATMasterState();
          IF TRUE = fbIL_ECATMasterState.Done THEN
            strMasterStatus.StateDWord := fbIL_ECATMasterState.State; // FB finished.
          Master status is in state.
          END_IF
          IF TRUE = fbIL_ECATMasterState.Error THEN
            ; // Error handling
          END_IF

### 13.7.10 IL_ECATRemoteSlaveState

          Brief description
          The function block IL_ECATRemoteSlaveState provides diagnostic status infor‐
          mation on an EtherCAT slave.

          Interface description

Table 145: Interface variables of the IL_ECATRemoteSlaveState function block
I/O type        Name              Data type                Description

VAR_INPUT       Execute           BOOL                     Function block processing enabled

                                           (once, edge-controlled)

ClientId          ⮫ IL_HANDLE              ClientId is currently not supported

                                           (Default: ClientId := 0)

MasterName        POINTER TO STRING        Instance name of the master

AddressType       ⮫ IL_ECAT_ADDRESS_TYPE   Selection of the slave addressing (EtherCAT address or AutoInc
                                           address)

SlaveAddress      UINT                     EtherCAT address or the current AutoInc address at the bus
                                           (depends on the input "AddressType")

Timeout           TIME                     Timeout monitoring

VAR_OUTPUT      Done              BOOL                     Processing completed without error. Output data valid

Active            BOOL                     Processing active. Output data invalid

Error             BOOL                     Processing completed with error. Output data invalid

ErrorID           ⮫ ERROR_CODE             Standardized rough error classification

ErrorIdent        ⮫ ERROR_STRUCT           Function block-specific detailed information on the error

State             DWORD                    Diagnostic status information of the slave.

                                           For details, refer to ⮫ IL_ECAT_SLAVE_STATE

Table 146: Min./max. and default values of the inputs of the IL_ECATRemoteSlaveState function
block
Name        Data type            Min.                     Max                      Default                  Effective

Execute     BOOL                 -                        -                        FALSE                    Contin‐

ClientId    IL_HANDLE            0                        0                        0                        Rising
                                                                                   edge     at

MasterName POINTER TO STRING     n. def.                  n. def.                  0                        Rising
                                                                                   edge     at

AddressType IL_ECAT_ADDRESS_TYP ECAT_           UNDEFINED ECAT_ETHERCAT _ADDRESS ECAT _ETHERCAT _ADDRESS    Rising
E                    _ADDRESS                                                                   edge     at

SlaveAd‐    UNIT                 0                        65535                    0                        Rising
dress                                                                                                       edge     at

Timeout     TIME                 T#1ms                    n. def.                  T#3s                     Rising
                                                                                   edge     at

Functional description
The function block IL_ECATRemoteSlaveState returns a DWORD after a suc‐
cessful execution via "State". The DWORD contains information on the current
state of the EtherCAT slave.
When addressing the slaves, use AddressType ECAT_ETHERCAT_ADDRESS.
To check whether the EtherCAT slave is in the operating state "OP" and
whether there are no errors, the output value "State" can be compared with 0
when the function block was executed successfully.
To simplify the evaluation, write the output value "State" to
IL_ECAT_SLAVE_STATE.StateDWord to subsequently access the individual bits
via IL_ECAT_SLAVE_STATE.IL_ECAT_SLAVE_STATE_BITS.
For a description of the diagnostic bits of the "State” output, refer to
IL_ECAT_SLAVE_STATE_BITS⮫ Chapter 13.10.33 IL_ECAT_SLAVE_STATE_BITS
on page 257.

Programming example

PROGRAM Example_IL_ECATRemoteSlaveState
VAR
  strMasterName             : STRING    := 'ethercatmaster'; // Instance name of the
fieldbus master
  unRemoteSlaveStatus       : IL_ECAT_SLAVE_STATE     := 0; //Result of the FB is
SlaveStatus Code
  fbIL_ECATRemoteSlaveState : IL_ECATRemoteSlaveState;
END_VAR

//fbIL_ECATRemoteSlaveState.Execute      := TRUE;
fbIL_ECATRemoteSlaveState.MasterName   := ADR(strMasterName);
fbIL_ECATRemoteSlaveState();
IF TRUE = fbIL_ECATRemoteSlaveState.Done THEN
  unRemoteSlaveStatus.StateDWord := fbIL_ECATRemoteSlaveState.State; // FB finished.
Result of the FB is SlaveStatus Code
END_IF
IF TRUE = fbIL_ECATRemoteSlaveState.Error THEN
  ; // Error handling
END_IF

Error description
For more information on the error codes, refer to:

           ⮫ Chapter 13.11 Error codes on page 257
           ⮫ Diagnostics 0C0F0000

### 13.7.11 Distributed Clocks

IL_ECATGetDcSlaveConfigInfo
           Brief description
           This function block returns the Distributed Clock configuration as defined in
           the EtherCAT network configuration.

           Interface description

Table 147: Interface variables of the IL_ECATGetDcSlaveConfigInfo function block
I/O type        Name             Data type                 Description

VAR_INPUT       Execute          BOOL                      Function block processing enabled

                                           (once, edge-controlled)

ClientId         ⮫ IL_HANDLE               ClientId is currently not supported

                                           (Default: ClientId := 0)

MasterName       POINTER TO STRING         Instance name of the master

AddressType      ⮫ IL_ECAT_ADDRESS_TYPE    Selection of the slave addressing (EtherCAT address or AutoInc address)

SlaveAddress     UINT                      EtherCAT address or the current AutoInc address at the bus (depends on
                                           the input "AddressType")

Timeout          TIME                      Timeout monitoring

VAR_OUTPUT      Done             BOOL                      Processing completed without error. Output data valid

Active           BOOL                      Processing active. Output data invalid

Error            BOOL                      Processing completed with error. Output data invalid

ErrorID          ⮫ ERROR_CODE              Standardized rough error classification

ErrorIdent       ⮫ ERROR_STRUCT            Function block-specific detailed information on the error

DcSlaveConfi‐    ⮫ IL_ECAT_DC_SLAVE_CONFI DC slave configuration
gInfo            G_INFO

Table 148: Min./max. and default values of the inputs of the IL_ECATGetDcSlaveConfigInfo
function block
Name         Data type                  Min                  Max                          Default                        Effective

Execute      BOOL                       -                    -                            FALSE                          Contin‐

ClientId     IL_HANDLE                  0                    0                            0                              Rising
                                                                                                         edge        at

MasterName   POINTER TO STRING          n. def.              n. def.                      0                              Rising
                                                                                                         edge        at

AddressType IL_ECAT_ADDRESS_TYPE ECAT_AUTOINC_ADDRES         ECAT_ETHERCAT_ADDRESS        ECAT_ETHERCAT_ADDRESS          Rising
                        S                                                                                edge        at

Name        Data type             Min                   Max                     Default                  Effective

SlaveAddress UINT                 0                     65535                   0                        Rising
                                                                                 edge        at

Timeout     TIME                  T#1ms                 n. def.                 T#3s                     Rising
                                                                                 edge        at

Functional description
This function block returns the Distributed Clock configuration as defined in
the EtherCAT network configuration.
Reading out is possible when the EtherCAT master is configured.

Example in ST
Deklaration

PROGRAM Example_IL_ECATGetDcSlaveConfigInfo
VAR
    fbIL_ECATGetDcSlaveConfigInfo   : IL_ECATGetDcSlaveConfigInfo;
    strMasterName                   : STRING := 'ethercatmaster'; // Instance name of the
fieldbus master
    stIL_ECAT_DC_SLAVE_CONFIG_INFO : IL_ECAT_DC_SLAVE_CONFIG_INFO;
END_VAR

Implementation

fbIL_ECATGetDcSlaveConfigInfo.Execute := TRUE;
fbIL_ECATGetDcSlaveConfigInfo.MasterName := ADR(strMasterName);
fbIL_ECATGetDcSlaveConfigInfo.SlaveAddress := 1001;
fbIL_ECATGetDcSlaveConfigInfo();

IF TRUE = fbIL_ECATGetDcSlaveConfigInfo.Done THEN
    stIL_ECAT_DC_SLAVE_CONFIG_INFO := fbIL_ECATGetDcSlaveConfigInfo.DcSlaveConfigInfo;
    fbIL_ECATGetDcSlaveConfigInfo(Execute := FALSE);
END_IF
IF TRUE = fbIL_ECATGetDcSlaveConfigInfo.Error THEN
    ; // Error handling
END_IF

Error description
For more information on the error codes, refer to:
⮫ Chapter 13.11 Error codes on page 257
⮫ Diagnostics 0C0F0000

### 13.7.12 Master statistics

IL_ECATGetMasterFrameStatisticCounters
Brief description
The function block IL_ECATGetMasterFrameStatisticCounters provides infor‐
mation on the EtherCAT frame statistics.

Interface description

Table 149: Interface variables of the IL_ECATGetMasterFrameStatisticCounters function block
I/O type      Name                     Data type                                     Initial value    Description

VAR_INPUT     Execute                  BOOL                                                           Function block processing ena‐

                                                                           (once, edge-controlled)

ClientId                 ⮫ IL_HANDLE                                   0                ClientId is currently not supported

                                                                           (Default: ClientId := 0)

MasterName               POINTER TO STRING                                              Instance name of the master

Timeout                  TIME                                          TIME#3s0ms       Timeout monitoring

VAR_OUTPUT    Done                     BOOL                                                           Processing    completed      without

                                                                           error. Output data valid

Active                   BOOL                                                           Processing active. Output data

Error                    BOOL                                                           Processing completed with error.
                                                                           Output data invalid

ErrorID                  ⮫ ERROR_CODE                                                   Standardized rough error classifi‐

ErrorIdent               ⮫ ERROR_STRUCT                                                 Function    block-specific   detailed
                                                                           information on the error

FrameStatisticCounters   ⮫      IL_ECAT_MASTER_FRAME_STATISTIC_COUN‐ 0                  EtherCAT frame statistic counter
            TERS

Table   150:     Min./max.     and    default     values                             of        the           inputs         of        the
IL_ECATGetMasterFrameStatisticCounters function block
Name              Data type                     Min.           Max            Default                Effective

Execute           BOOL                          -              -              FALSE                  Continuous

ClientId          IL_HANDLE                     0              0              0                      Rising edge at Execute

MasterName        POINTER TO STRING             n. def.        n. def.        0                      Rising edge at Execute

Timeout           TIME                          T#1ms          n. def.        T#3s                   Rising edge at Execute

Functional description
The function block IL_ECATGetMasterFrameStatisticCounters provides infor‐
mation on the EtherCAT frame statistics (see ⮫ IL_ECAT_MASTER_FRAME_STA‐
TISTIC_COUNTERS).

Declaration CodeExample

PROGRAM Example_IL_ECATGettMasterFrameStatisticCounters
VAR
  strMasterName                             : STRING := 'ethercatmaster';                                  //
name of the fieldbus master

  fbIL_ECATGetMasterFrameStatisticCounters : IL_ECATGetMasterFrameStatisticCounters; //
Instance of function block IL_ECATResetMasterFrameStatisticCounters (example 1)
  bExecute                                  : BOOL := FALSE;
  stMasterFrameStatisticCounters            : IL_ECAT_MASTER_FRAME_STATISTIC_COUNTERS; //
Result of the FB is the frame statistic
END_VAR

Implementation CodeExample

(* Example: Reading the frame statistic counters
*)
fbIL_ECATGetMasterFrameStatisticCounters.Execute    := bExecute;
fbIL_ECATGetMasterFrameStatisticCounters.MasterName := ADR(strMasterName);
fbIL_ECATGetMasterFrameStatisticCounters();
IF TRUE = fbIL_ECATGetMasterFrameStatisticCounters.Done THEN
   stMasterFrameStatisticCounters :=

fbIL_ECATGetMasterFrameStatisticCounters.FrameStatisticCounters; // FB finished.
END_IF
IF TRUE = fbIL_ECATGetMasterFrameStatisticCounters.Error THEN
  ; // Error handling
END_IF

Error description
For more information on the error codes, refer to:
⮫ Chapter 13.11 Error codes on page 257
⮫ Diagnostics 0C0F0000

IL_ECATGetMasterMailboxStatisticCounters
Brief description
The IL_ECATGetMasterMailboxStatisticCounters function block returns the
mailbox statistic counters of the master.

Interface description

Table 151: Interface variables of the IL_ECATGetMasterMailboxStatisticCounters function block
I/O type     Name                     Data type                                       Description

VAR_INPUT    Execute                  BOOL                                            Function block processing enabled

                                                          (once, edge-controlled)

ClientId                 ⮫ IL_HANDLE                                     ClientId is currently not supported

                                                          (Default: ClientId := 0)

MasterName               POINTER TO STRING                               Instance name of the master

Timeout                  TIME                                            Timeout monitoring

VAR_OUTPUT Done                       BOOL                                            Processing     completed    without   error.
                                                          Output data valid

Active                   BOOL                                            Processing active. Output data invalid

MailboxStatisticCounters ⮫ IL_ECAT_MASTER_MAILBOX_STATISTIC_COUNTERS     Master mailbox statistic data

Error                    BOOL                                            Processing completed with error. Output
                                                          data invalid

ErrorID                  ⮫ ERROR_CODE                                    Standardized rough error classification

ErrorIdent               ⮫ ERROR_STRUCT                                  Function block-specific detailed informa‐
                                                          tion on the error

Table   152:    Min./max.      and    default     values                         of    the           inputs        of        the
IL_ECATGetMasterMailboxStatisticCounters function block
Name            Data type                    Min          Max             Default        Effective

Execute         BOOL                         -            -               FALSE          Continuous

ClientId        IL_HANDLE                    0            0               0              Rising edge at Execute

MasterName      POINTER TO STRING            n. def.      n. def.         0              Rising edge at Execute

Timeout         TIME                         T#1ms        n. def.         T#3s           Rising edge at Execute

Functional description
The IL_ECATGetMasterMailboxStatisticCounters function block returns the
mailbox statistic counters of the master.
These counters can be used to evaluate the number and data volume of the
exchanged mailbox protocols in read and write direction in total and in the
last second.
The exact selection of the counter is performed via nested structures.

Example in ST
Deklaration

PROGRAM Example_IL_ECATGetMasterMailboxStatisticCounters
VAR
    strMasterName   : STRING := 'ethercatmaster'; // name of the fieldbus master
    fbIL_ECATGetMasterMailboxStatisticCounters :
IL_ECATGetMasterMailboxStatisticCounters; // Instance of function block
IL_ECATGetMasterMailboxStatisticCounters
    bExecute                                              : BOOL := FALSE;
    stMasterMailboxStatisticCounters   : IL_ECAT_MASTER_MAILBOX_STATISTIC_PROTOCOLS; //
Result of the FB is the frame statistic
END_VAR

Implementation

(* Example: Reading the mailbox statistic counters
*)
fbIL_ECATGetMasterMailboxStatisticCounters.Execute    := bExecute;
fbIL_ECATGetMasterMailboxStatisticCounters.MasterName := ADR(strMasterName);
fbIL_ECATGetMasterMailboxStatisticCounters();
IF TRUE = fbIL_ECATGetMasterMailboxStatisticCounters.Done THEN
   stMasterMailboxStatisticCounters :=
fbIL_ECATGetMasterMailboxStatisticCounters.MailboxStatisticCounters; // FB finished.
END_IF
IF TRUE = fbIL_ECATGetMasterMailboxStatisticCounters.Error THEN
   ; // Error handling
END_IF

Error description
For more information on the error codes, refer to:
⮫ Chapter 13.11 Error codes on page 257
⮫ Diagnostics 0C0F0000

    IL_ECATResetMasterFrameStatisticCounters
Brief description
The function block IL_ECATResetMasterFrameStatisticCounters deletes the
EtherCAT frame statistic counters.

Interface description

Table 153: Interface variables of the IL_ECATResetMasterFrameStatisticCounters function block
I/O type        Name            Data type               Initial value     Description

VAR_INPUT       Execute         BOOL                                      Function block processing enabled

                                                          (once, edge-controlled)

ClientId        ⮫ IL_HANDLE             0                 ClientId is currently not supported

                                                          (Default: ClientId := 0)

MasterName      POINTER TO STRING                         Instance name of the master

ResetCounters DWORD                     0                 Bit string to clear the frame statistic counters.

                                                          See ⮫ IL_ECAT_MASTER_FRAME_STATISTIC_COUNTERS

Timeout         TIME                    TIME#3s0ms Timeout monitoring

VAR_OUTPUT      Done            BOOL                                      Processing completed without error. Output data valid

Active          BOOL                                      Processing active. Output data invalid

Error           BOOL                                      Processing completed with error. Output data invalid

ErrorID         ⮫ ERROR_CODE                              Standardized rough error classification

ErrorIdent      ⮫ ERROR_STRUCT                            Function block-specific detailed information on the error

Table    154:    Min./max.     and    default     values                                     of      the         inputs         of      the
IL_ECATResetMasterFrameStatisticCounters function block
Name                Data type                 Min.              Max                      Default            Effective

Execute             BOOL                      -                 -                        FALSE              Continuous

ClientId            IL_HANDLE                 0                 0                        0                  Rising edge at Execute

MasterName          POINTER TO STRING         n. def.           n. def.                  0                  Rising edge at Execute

ResetCounters       DWORD                     0                 0xFFFFFFFF               0                  Rising edge at Execute

Timeout             TIME                      T#1ms             n. def.                  T#3s               Rising edge at Execute

             Functional description
             The function block IL_ECATResetMasterFrameStatisticCounters deletes the
             EtherCAT frame statistic counters. The input "ResetCounters" can be used
             to select which counters are to be reset (see ⮫ IL_ECAT_MASTER_FRAME_STA‐
             TISTIC_COUNTERS). If the input ResetCounters := 0 is set, all counters are
             reset.

             Declaration CodeExample

             PROGRAM Example_IL_ECATResetMasterFrameStatisticCounters
             VAR
               strMasterName                                 : STRING :=
             'ethercatmaster';                     // name of the fieldbus master

               fbIL_ECATResetMasterFrameStatisticCountersEg1 :
             IL_ECATResetMasterFrameStatisticCounters;       // Instance of function block
             IL_ECATResetMasterFrameStatisticCounters (example 1)
               boExecuteEg1                                  : BOOL;

               fbIL_ECATResetMasterFrameStatisticCountersEg2 :
             IL_ECATResetMasterFrameStatisticCounters;       // Instance of function block
             IL_ECATResetMasterFrameStatisticCounters (example 2)
               boExecuteEg2                                  : BOOL;
               stResetMasterFrameStatisticCountersEg2        :
             IL_ECAT_RESET_MASTER_FRAME_STATISTIC_COUNTERS; // Result of the FB is the frame statistic
             END_VAR

             Implementation CodeExample

             (* Example 1: Reseting all frame statistic counters
                fbIL_ECATResetMasterFrameStatisticCountersEg1.ResetCounters := 0; // 0 = default value
             of input ResetCounters
             *)

fbIL_ECATResetMasterFrameStatisticCountersEg1.Execute    := boExecuteEg1;
fbIL_ECATResetMasterFrameStatisticCountersEg1.MasterName := ADR(strMasterName);
fbIL_ECATResetMasterFrameStatisticCountersEg1();
IF TRUE = fbIL_ECATResetMasterFrameStatisticCountersEg1.Done THEN
  ; // FB finished.
END_IF
IF TRUE = fbIL_ECATResetMasterFrameStatisticCountersEg1.Error THEN
  ; // Error handling
END_IF

(* Example 2: Reseting frame statistic counter NumCyclicFrames
*)
fbIL_ECATResetMasterFrameStatisticCountersEg2.Execute            := boExecuteEg2;
fbIL_ECATResetMasterFrameStatisticCountersEg2.MasterName         := ADR(strMasterName);
stResetMasterFrameStatisticCountersEg2.ResetBits.NumCyclicFrames := TRUE;

fbIL_ECATResetMasterFrameStatisticCountersEg2.ResetCounters      :=
stResetMasterFrameStatisticCountersEg2.ResetDWord;
fbIL_ECATResetMasterFrameStatisticCountersEg2();
IF TRUE = fbIL_ECATResetMasterFrameStatisticCountersEg2.Done THEN
   ; // FB finished.
END_IF
IF TRUE = fbIL_ECATResetMasterFrameStatisticCountersEg2.Error THEN
   ; // Error handling
END_IF

Error description
For more information on the error codes, refer to:
⮫ Chapter 13.11 Error codes on page 257
⮫ Diagnostics 0C0F0000

### 13.7.13 Slave statistics

IL_ECATGetSlaveStatisticAutoMode
Brief description
The function block IL_ECATGetSlaveStatisticAutoMode provides the settings
for the Auto Mode of the functionality of the slave statistics.

Interface description

Table 155: Interface variables of the IL_ECATGetSlaveStatisticAutoMode function block
I/O type         Name               Data type                  Description

VAR_INPUT        Execute            BOOL                       Function block processing enabled

                                     (once, edge-controlled)

ClientId           ⮫ IL_HANDLE                ClientId is currently not supported

                                     (Default: ClientId := 0)

MasterName         POINTER TO STRING          Instance name of the master

Timeout            TIME                       Timeout monitoring

VAR_OUTPUT       Done               BOOL                       Processing completed without error. Output data valid

Active             BOOL                       Processing active. Output data invalid

Error              BOOL                       Processing completed with error. Output data invalid

I/O type            Name                Data type                  Description

ErrorID             ⮫ ERROR_CODE               Standardized rough error classification

ErrorIdent          ⮫ ERROR_STRUCT             Function block-specific detailed information on the error

AutoModeEnable      BOOL                       TRUE: Slave statistic functionality is enabled

AutoModeIdleTime TIME                          Idle time during which the master does not collect any registers
                                     from the slaves

Functional description
The function block IL_ECATGetSlaveStatisticAutoMode provides the settings
for the Auto Mode of the functionality of the slave statistics.
If the output "AutoModeEnable" = TRUE, the master collects the error coun‐
ters of the slaves cyclically. The AutoModeIdleTime specifies how long the
master pauses after collecting the error counters until the next cycle starts.

Declaration CodeExample

PROGRAM Example_IL_ECATGetSlaveStatisticAutoMode
VAR
  strMasterName    : STRING             := 'ethercatmaster'; // Instance name of the
fieldbus master
  fbIL_ECATGetSlaveStatisticAutoMode: IL_ECATGetSlaveStatisticAutoMode;

  bAutoModeEnable       : BOOL;
  tAutoModeIdleTime     : TIME;
END_VAR

Implementation CodeExample

fbIL_ECATGetSlaveStatisticConfig.Execute        := TRUE;
fbIL_ECATGetSlaveStatisticAutoMode.MasterName     := ADR(strMasterName);
fbIL_ECATGetSlaveStatisticAutoMode();
IF TRUE = fbIL_ECATGetSlaveStatisticAutoMode.Done THEN
  bAutoModeEnable   := fbIL_ECATGetSlaveStatisticAutoMode.AutoModeEnable;
  tAutoModeIdleTime := fbIL_ECATGetSlaveStatisticAutoMode.AutoModeIdleTime;
END_IF
IF TRUE = fbIL_ECATGetSlaveStatisticAutoMode.Error THEN
  ; // Error handling
END_IF

IL_ECATGetSlaveStatisticCounters
Brief description
The function block IL_ECATGetSlaveStatisticCounters reads out the collected
error counters of a slave device from the master.

Interface description

Table 156: Interface variables of the IL_ECATGetSlaveStatisticCounters function block
I/O type           Name                   Data type                         Description

VAR_INPUT          Execute                BOOL                              Function block processing enabled

                                              (once, edge-controlled)

ClientId               ⮫ IL_HANDLE                       ClientId is currently not supported

                                              (Default: ClientId := 0)

MasterName             POINTER TO STRING                 Instance name of the master

I/O type       Name                  Data type                               Description

AddressType           ⮫ IL_ECAT_ADDRESS_TYPE                  Selection of the slave addressing (EtherCAT address or
                                                              AutoInc address)

SlaveAddress          UINT                                    EtherCAT address or the current AutoInc address at the
                                                              bus (depends on the input "AddressType")

Timeout               TIME                                    Timeout monitoring

VAR_OUTPUT     Done                  BOOL                                    Processing completed without error. Output data valid

Active                BOOL                                    Processing active. Output data invalid

Error                 BOOL                                    Processing completed with error. Output data invalid

ErrorID               ⮫ ERROR_CODE                            Standardized rough error classification

ErrorIdent            ⮫ ERROR_STRUCT                          Function block-specific detailed information on the
                                                              error

SlaveStatisticCounters ⮫     IL_ECAT_SLAVE_STATISTIC_COUN‐ Slave statistic counter of the slave device
                      TERS

          Functional description
          The function block IL_ECATGetSlaveStatisticCounters reads out the collected
          error counters of a slave device from the master.

          Declaration CodeExample

          PROGRAM Example_IL_ECATGetSlaveStatisticCounters
          VAR
            strMasterName    : STRING             := 'ethercatmaster'; // Instance name of the
          fieldbus master
            fbIL_ECATGetSlaveStatisticCounters: IL_ECATGetSlaveStatisticCounters;

            stSlaveStatisticCounters:                 IL_ECAT_SLAVE_STATISTIC_COUNTERS;
          END_VAR

          Implementation CodeExample

          fbIL_ECATGetSlaveStatisticCounters.Execute        := TRUE;
          fbIL_ECATGetSlaveStatisticCounters.MasterName     := ADR(strMasterName);
          fbIL_ECATGetSlaveStatisticCounters.SlaveAddress   := 1001;
          fbIL_ECATGetSlaveStatisticCounters();
          IF TRUE = fbIL_ECATGetSlaveStatisticCounters.Done THEN
            stSlaveStatisticCounters := fbIL_ECATGetSlaveStatisticCounters.SlaveStatisticCounters;
            fbIL_ECATGetSlaveStatisticCounters(Execute := FALSE);
          END_IF
          IF TRUE = fbIL_ECATGetSlaveStatisticCounters.Error THEN
            ; // Error handling
          END_IF

IL_ECATResetSlaveStatisticCounters
          Brief description
          The function block IL_ECATResetSlaveStatisticCounter deletes all error coun‐
          ters in all slave devices.

          Interface description

Table 157: Interface variables of the IL_ECATResetSlaveStatisticCounters function block
I/O type           Name                Data type                  Description

VAR_INPUT          Execute             BOOL                       Function block processing enabled

                                               (once, edge-controlled)

ClientId            ⮫ IL_HANDLE                ClientId is currently not supported

                                               (Default: ClientId := 0)

MasterName          POINTER TO STRING          Instance name of the master

Timeout             TIME                       Timeout monitoring

VAR_OUTPUT         Done                BOOL                       Processing completed without error. Output data valid

Active              BOOL                       Processing active. Output data invalid

Error               BOOL                       Processing completed with error. Output data invalid

ErrorID             ⮫ ERROR_CODE               Standardized rough error classification

ErrorIdent          ⮫ ERROR_STRUCT             Function block-specific detailed information on the error

          Functional description
          The function block IL_ECATResetSlaveStatisticCounters deletes all error coun‐
          ters in all slave devices.

          Declaration CodeExample

          PROGRAM Example_IL_ECATResetSlaveStatisticCounters
          VAR
            strMasterName    : STRING             := 'ethercatmaster'; // Instance name of the
          fieldbus master

            fbIL_ECATResetSlaveStatisticCounters: IL_ECATResetSlaveStatisticCounters;

          END_VAR

          Implementation CodeExample

          fbIL_ECATResetSlaveStatisticCounters.Execute := TRUE;
          fbIL_ECATResetSlaveStatisticCounters.MasterName     := ADR(strMasterName);
          fbIL_ECATResetSlaveStatisticCounters();
          IF TRUE = fbIL_ECATResetSlaveStatisticCounters.Done THEN
            ; // FB finished .
          END_IF
          IF TRUE = fbIL_ECATResetSlaveStatisticCounters.Error THEN
            ; // Error handling
          END_IF

IL_ECATSetSlaveStatisticAutoMode
          Brief description
          The function block IL_ECATSetSlaveStatisticAutoMode sets the settings for the
          Auto Mode of the functionality of the slave statistics.

          Interface description

Table 158: Interface variables of the IL_ECATSetSlaveStatisticAutoMode function block
I/O type         Name                Data type                  Description

VAR_INPUT        Execute             BOOL                       Function block processing enabled

                                               (once, edge-controlled)

ClientId            ⮫ IL_HANDLE                ClientId is currently not supported

                                               (Default: ClientId := 0)

MasterName          POINTER TO STRING          Instance name of the master

Timeout             TIME                       Timeout monitoring

AutoModeEnable      BOOL                       TRUE: Slave statistic functionality is enabled

AutoModeIdleTime TIME                          Idle time during which the master does not collect any registers
                                               from the slaves

VAR_OUTPUT       Done                BOOL                       Processing completed without error. Output data valid

Active              BOOL                       Processing active. Output data invalid

Error               BOOL                       Processing completed with error. Output data invalid

ErrorID             ⮫ ERROR_CODE               Standardized rough error classification

ErrorIdent          ⮫ ERROR_STRUCT             Function block-specific detailed information on the error

          Functional description
          The function block IL_ECATSetSlaveStatisticAutoMode sets the settings for the
          Auto Mode of the functionality of the slave statistics.
          If the input "AutoModeEnable" = TRUE, the master collects the error counters
          of the slaves cyclically. The AutoModeIdleTime specifies how long the master
          pauses after collecting the error counters until the next cycle starts.

          Declaration CodeExample

          PROGRAM Example_IL_ECATSetSlaveStatisticAutoMode
          VAR
            strMasterName    : STRING             := 'ethercatmaster'; // Instance name of the
          fieldbus master

            fbIL_ECATSetSlaveStatisticAutoMode: IL_ECATSetSlaveStatisticAutoMode;
          END_VAR

          Implementation CodeExample

          fbIL_ECATSetSlaveStatisticAutoMode.Execute        := TRUE;
          fbIL_ECATSetSlaveStatisticAutoMode.AutoModeEnable := TRUE;
          fbIL_ECATSetSlaveStatisticAutoMode.AutoModeIdleTime := T#2S;
          fbIL_ECATSetSlaveStatisticAutoMode.MasterName     := ADR(strMasterName);
          fbIL_ECATSetSlaveStatisticAutoMode();
          IF TRUE = fbIL_ECATSetSlaveStatisticAutoMode.Done THEN
            ; // FB finished
          END_IF
          IF TRUE = fbIL_ECATSetSlaveStatisticAutoMode.Error THEN
            ; // Error handling
          END_IF

IL_ECATSetSlaveStatisticAutoModeEnable
          Brief description
          The function block IL_ECATSetSlaveStatisticAutoModeEnable sets the setting
          AutoModeEnable for the functionality of the slave statistics.

          Interface description

Table 159: Interface variables of the IL_ECATSetSlaveStatisticAutoModeEnable function block
I/O type           Name                Data type                  Description

VAR_INPUT          Execute             BOOL                       Function block processing enabled

                                               (once, edge-controlled)

ClientId            ⮫ IL_HANDLE                ClientId is currently not supported

                                               (Default: ClientId := 0)

MasterName          POINTER TO STRING          Instance name of the master

Timeout             TIME                       Timeout monitoring

AutoModeEnable      BOOL                       TRUE: Slave statistic functionality is enabled

VAR_OUTPUT         Done                BOOL                       Processing completed without error. Output data valid

Active              BOOL                       Processing active. Output data invalid

Error               BOOL                       Processing completed with error. Output data invalid

ErrorID             ⮫ ERROR_CODE               Standardized rough error classification

ErrorIdent          ⮫ ERROR_STRUCT             Function block-specific detailed information on the error

          Functional description
          The function block IL_ECATSetSlaveStatisticAutoModeEnable sets the setting
          AutoModeEnable for the functionality of the slave statistics.
          If the input "AutoModeEnable" = TRUE, the master collects the error counters
          of the slaves cyclically.

          Declaration CodeExample

          PROGRAM Example_IL_ECATSetSlaveStatisticAutoModeEnable
          VAR
            strMasterName    : STRING             := 'ethercatmaster'; // Instance name of the
          fieldbus master
            fbIL_ECATSetSlaveStatisticAutoModeEnable: IL_ECATSetSlaveStatisticAutoModeEnable;
          END_VAR

          Implementation CodeExample

          fbIL_ECATSetSlaveStatisticAutoModeEnable.Execute        := TRUE;
          fbIL_ECATSetSlaveStatisticAutoModeEnable.MasterName     := ADR(strMasterName);
          fbIL_ECATSetSlaveStatisticAutoModeEnable.AutoModeEnable := TRUE;
          fbIL_ECATSetSlaveStatisticAutoModeEnable();
          IF TRUE = fbIL_ECATSetSlaveStatisticAutoModeEnable.Done THEN
            ; // FB finished
          END_IF
          IF TRUE = fbIL_ECATSetSlaveStatisticAutoModeEnable.Error THEN
            ; // Error handling
          END_IF

IL_ECATSetSlaveStatisticAutoModeIdleTime
          Brief description
          The function block IL_ECATSetSlaveStatisticAutoModeIdleTime sets the set‐
          ting AutoModeIdleTime for the functionality of the slave statistics.

Interface description

Table 160: Interface variables of the IL_ECATSetSlaveStatisticAutoModeIdleTime function block

I/O type       Name            Data type                  Description
VAR_INPUT      Execute         BOOL                       Function block processing enabled
                                     (once, edge-controlled)
ClientId        ⮫ IL_HANDLE                ClientId is currently not supported
                                     (Default: ClientId := 0)
MasterName          POINTER TO STRING          Instance name of the master
Timeout             TIME                       Timeout monitoring
AutoModeI‐          BOOL                       Idle time during which the master does not
dleTime                                        collect any registers from the slaves
VAR_OUTPUT Done                BOOL                       Processing completed without error. Output
                                     data valid
Active          BOOL                       Processing active. Output data invalid
Error           BOOL                       Processing completed with error. Output data
                                     invalid
ErrorID         ⮫ ERROR_CODE               Standardized rough error classification
ErrorIdent      ⮫ ERROR_STRUCT             Function block-specific detailed information
                                     on the error

Functional description
The function block IL_ECATSetSlaveStatisticAutoModeIdleTime sets the set‐
ting AutoModeIdleTime for the functionality of the slave statistics.
The AutoModeIdleTime specifies how long the master pauses after collecting
the error counters until the next cycle starts.

Declaration CodeExample

PROGRAM Example_IL_ECATSetSlaveStatisticAutoModeIdleTime
VAR
  strMasterName    : STRING             := 'ethercatmaster'; // Instance name of the
fieldbus master
  fbIL_ECATSetSlaveStatisticAutoModeIdleTime: IL_ECATSetSlaveStatisticAutoModeIdleTime;
END_VAR

Implementation CodeExample

fbIL_ECATSetSlaveStatisticAutoModeIdleTime.Execute        := TRUE;
fbIL_ECATSetSlaveStatisticAutoModeIdleTime.MasterName     := ADR(strMasterName);
fbIL_ECATSetSlaveStatisticAutoModeIdleTime.AutoModeIdleTime := T#2S;
fbIL_ECATSetSlaveStatisticAutoModeIdleTime();
IF TRUE = fbIL_ECATSetSlaveStatisticAutoModeIdleTime.Done THEN
  ; // FB finished
END_IF
IF TRUE = fbIL_ECATSetSlaveStatisticAutoModeIdleTime.Error THEN
  ; // Error handling
END_IF

## 13.8 State machine

### 13.8.1 IL_ECATMasterGetBusState

         Brief description
         The function block IL_ECATMasterGetBusState returns the current bus state of
         the EtherCAT master.

         Interface description

Table 161: Interface variables of the IL_ECATMasterGetBusState function block
I/O type           Name               Data type                        Description

VAR_INPUT          Execute            BOOL                             Function block processing enabled (once, edge-controlled)

ClientId           ⮫ IL_HANDLE                      ClientId is currently not supported (default: ClientId := 0)

                   IL_HANDLE

MasterName         POINTER TO STRING                Instance name of the master

VAR_OUTPUT         Done               BOOL                             Processing completed without error. Output data valid

Active             BOOL                             Processing active. Output data invalid

Error              BOOL                             Processing completed with error. Output data invalid

ErrorID            ⮫ ERROR_CODE                     Standardized rough error classification

ErrorIdent         ⮫ ERROR_STRUCT                   Function block-specific detailed information on the error

ReqBusState        IL_ECAT_STATE ⮫ IL_ECAT_STATE Requested bus state of the EtherCAT master

ActBusState        IL_ECAT_STATE ⮫ IL_ECAT_STATE Current bus state of the EtherCAT master

Table 162: Min./max. and default values of the inputs of the IL_ECATMasterGetBusState function
block
Name           Data type                     Min.            Max             Default              Effective

Execute        BOOL                          -               -               FALSE                Continuous

ClientId       IL_HANDLE                     0               0               0                    Rising edge at Execute

MasterName     POINTER TO STRING             n. def.         n. def.         0                    Rising edge at Execute

         Functional description
         The function block IL_ECATMasterGetBusState returns the current bus state of
         the EtherCAT master.

         Implementation in ST
         Beispiel:

         PROGRAM EG_IL_ECATMasterGetBusState
         VAR
           fbECATMasterGetBusState: IL_ECATMasterGetBusState;
           eActBusState :           IL_ECAT_STATE;
           strMasterName:           STRING := 'ethercatmaster';
         END_VAR

          fbECATMasterGetBusState.Execute    := TRUE;
          fbECATMasterGetBusState.MasterName := ADR(strMasterName);
          fbECATMasterGetBusState();
          IF TRUE = fbECATMasterGetBusState.Done THEN
            eActBusState := fbECATMasterGetBusState.ActBusState;
          END_IF
          IF TRUE = fbECATMasterGetBusState.Error THEN
            ; // error handling
          END_IF

          Error description
          For more information on the error codes, refer to:
          ⮫ Chapter 13.11 Error codes on page 257

          ⮫ Diagnostics 0C0F0000

### 13.8.2 IL_ECATMasterSetBusState

          Brief description
          Use the function block IL_ECATMasterSetBusState to request an EtherCAT bus
          state at the EtherCAT master.

          Interface description

Table 163: Interface variables of the IL_ECATMasterSetBusState function block
I/O type          Name              Data type                      Description

VAR_INPUT         Execute           BOOL                           Function block processing enabled (once, edge-controlled)

ClientId          ⮫ IL_HANDLE                    ClientId is currently not supported (default: ClientId := 0)

MasterName        POINTER TO STRING              Instance name of the master

NewBusState       ⮫ IL_ECAT_STATE                Requested EtherCAT bus state

Timeout           TIME                           Timeout monitoring (disabled with T#0s)

VAR_OUTPUT        Done              BOOL                           Processing completed without error. Output data valid

Active            BOOL                           Processing active. Output data invalid

Error             BOOL                           Processing completed with error. Output data invalid

ErrorID           ⮫ ERROR_CODE                   Standardized rough error classification

ErrorIdent        ⮫ ERROR_STRUCT                 Function block-specific detailed information on the error

ReqBusState       IL_ECAT_STATE                  Requested bus state of the EtherCAT master
                  ⮫ IL_ECAT_STATE

ActBusState       IL_ECAT_STATE                  Current bus state of the EtherCAT master
                  ⮫ IL_ECAT_STATE

Table 164: Min./max. and default values of the IL_ECATMasterSetBusState inputs
Name            Data type                  Min.          Max                     Default                          Effective

Execute         BOOL                       -             -                       FALSE                            Continuous

ClientId        IL_HANDLE                  0             0                       0                                Rising edge at Execute

MasterName      POINTER TO STRING          n. def.       n. def.                 0                                Rising edge at Execute

Name           Data type                Min.              Max             Default                Effective

NewBusState    IL_ECAT_STATE            ECAT_STATE_INIT   ECAT_STATE_OP   ECAT_STATE_UNKNOWN     Rising edge at Execute

Timeout        TIME                     T#0s              n. def.         T#0s                   Rising edge at Execute

Functional description
Use the function block IL_ECATMasterSetBusState to request an EtherCAT bus
state at the EtherCAT master.
The EtherCAT master intends to switch the bus state and the state of all slaves
to the requested state.
The following EtherCAT states can be requested:
● Init
● PreOP
● SafeOP
● OP
If the requested bus state is not reached within the timeout monitoring
("Timeout" > T#0s), the function block reports an error, but the internal com‐
mand execution cannot be stopped!
If the master is in a defined state (e.g. OP), but some slaves are not in this
state, the IL_ECATMasterSetBusState can also be called with this target state.
The master intends to switch all slaves to the requested state.
Note that the output "ActBusState” only displays the bus state. To determine
whether all slaves are in the master state, use the diagnostic function block
IL_ECATMasterState.

Implementation in ST
Beispiel:

PROGRAM EG_IL_ECATMasterSetBusState
VAR
  fbECATMasterSetBusState: IL_ECATMasterSetBusState;
  strMasterName:           STRING := 'ethercatmaster';
END_VAR

fbECATMasterSetBusState.Execute     := TRUE;
fbECATMasterSetBusState.MasterName := ADR(strMasterName);
fbECATMasterSetBusState.NewBusState := IL_ECAT_STATE.ECAT_STATE_OP;
fbECATMasterSetBusState();
IF TRUE = fbECATMasterSetBusState.Done THEN
  ; // master reached operational state.
END_IF
IF TRUE = fbECATMasterSetBusState.Error THEN
  ; // error handling
END_IF

Error description
For more information on the error codes, refer to:
⮫ Chapter 13.11 Error codes on page 257
⮫ Diagnostics 0C0F0000

### 13.8.3 IL_ECATRemoteSlaveGetDevState

Brief description
The function block IL_ECATRemoteSlaveGetDevState returns the current
EtherCAT state of a slave.

          Interface description

Table 165: Interface variables of the IL_ECATRemoteSlaveGetDevState function block
I/O type           Name              Data type                    Description

VAR_INPUT          Execute           BOOL                         Function block processing enabled (once, edge-controlled)

ClientId          ⮫ IL_HANDLE                  ClientId is currently not supported (default: ClientId := 0)

MasterName        POINTER TO STRING            Instance name of the master

AddressType       ⮫ IL_ECAT_ADDRESS_TYPE       Selection of the slave addressing (EtherCAT address or AutoInc
                                               address)

SlaveAddress      UINT                         EtherCAT address or the current AutoInc address at the bus
                                               (depends on the input "AddressType")

VAR_OUTPUT         Done              BOOL                         Processing completed without error. Output data valid

Active            BOOL                         Processing active. Output data invalid

Error             BOOL                         Processing completed with error. Output data invalid

ErrorID           ⮫ ERROR_CODE                 Standardized rough error classification

ErrorIdent        ⮫ ERROR_STRUCT               Function block-specific detailed information on the error

ReqDevState       ⮫ IL_ECAT_STATE              Requested EtherCAT state of the slave device

ActDevState       ⮫ IL_ECAT_STATE              Current EtherCAT state of the slave device

Table 166: Min./max. and default values of the IL_ECATRemoteSlaveGetDevState inputs
Name           Data type                 Min.                 Max                           Default                              Effective

Execute        BOOL                      -                    -                             FALSE                                Contin‐

ClientId       IL_HANDLE                 0                    0                             0                                    Rising
                                                                                                              edge      at

MasterName     POINTER TO STRING         n. def.              n. def.                       0                                    Rising
                                                                                                              edge      at

AddressType    IL_ECAT_ADDRESS_TYPE ECAT_AUTOINC_ADDRES       ECAT_ETHERCAT_ADDRESS ECAT_ETHERCAT_ADDRESS                        Rising
                      S                                                                                       edge      at

SlaveAddress   UINT                      0                    65535                         0                                    Rising
                                                                                                              edge      at

          Functional description
          The function block IL_ECATRemoteSlaveGetDevState returns the current
          EtherCAT state of a slave.

          Implementation in ST
          Beispiel:

         PROGRAM EG_IL_ECATRemoteSlaveGetDevState
         VAR
           fbIL_ECATRemoteSlaveGetDevState: IL_ECATRemoteSlaveGetDevState;
           strMasterName:                   STRING := 'ethercatmaster';
           eActDevState :                   IL_ECAT_STATE;
         END_VAR

         fbIL_ECATRemoteSlaveGetDevState.Execute      := TRUE;
         fbIL_ECATRemoteSlaveGetDevState.MasterName   := ADR(strMasterName);
         fbIL_ECATRemoteSlaveGetDevState.SlaveAddress := 1001;
         fbIL_ECATRemoteSlaveGetDevState();
         IF TRUE = fbIL_ECATRemoteSlaveGetDevState.Done THEN
           eActDevState := fbIL_ECATRemoteSlaveGetDevState.ActDevState;
         END_IF
         IF TRUE = fbIL_ECATRemoteSlaveGetDevState.Error THEN
           ; // error handling
         END_IF

         Error description
         For more information on the error codes, refer to:
         ⮫ Chapter 13.11 Error codes on page 257
        ⮫ Diagnostics 0C0F0000

### 13.8.4 IL_ECATRemoteSlaveSetDevState

         Brief description
         Use the function block IL_ECATRemoteSlaveSetDevState to request an
         EtherCAT state at a slave device.

         Interface description

Table 167: Interface variables of the IL_ECATRemoteSlaveSetDevState function block
I/O type           Name                Data type                Description

VAR_INPUT          Execute             BOOL                     Function block processing enabled (once, edge-controlled)

ClientId            ⮫ IL_HANDLE              ClientId is currently not supported (default: ClientId := 0)

MasterName          POINTER TO STRING        Instance name of the master

AddressType         ⮫ IL_ECAT_ADDRESS_TYPE   Selection of the slave addressing (EtherCAT address or AutoInc
                                             address)

SlaveAddress        UINT                     EtherCAT address or the current AutoInc address at the bus
                                             (depends on the input "AddressType")

NewDevState         ⮫ IL_ECAT_STATE          EtherCAT state requested at the slave device

Timeout             TIME                     Timeout monitoring (disabled with T#0s)

VAR_OUTPUT         Done                BOOL                     Processing completed without error. Output data valid

Active              BOOL                     Processing active. Output data invalid

Error               BOOL                     Processing completed with error. Output data invalid

ErrorID             ⮫ ERROR_CODE             Standardized rough error classification

ErrorIdent          ⮫ ERROR_STRUCT           Function block-specific detailed information on the error

ReqDevState         ⮫ IL_ECAT_STATE          Requested EtherCAT state of the slave device

I/O type            Name                Data type             Description

ActDevState         ⮫ IL_ECAT_STATE       Current EtherCAT state of the slave device

Table 168: Min./max. and default values of the IL_ECATRemoteSlaveSetDevState inputs
Name         Data type              Min.                     Max                         Default                 Effective

Execute      BOOL                   -                        -                           FALSE                   Contin‐

ClientId     IL_HANDLE              0                        0                           0                       Rising
                                                                                      edge        at

MasterName POINTER TO STRING        n. def.                  n. def.                     0                       Rising

                                                                                      edge        at

AddressType IL_ECAT_ADDRESS_TYPE ECAT_AUTOINC_ADDRESS        ECAT_ETHERCAT_ADDRESS ECAT_ETHERCAT_ADDRESS         Rising
                                                                                      edge        at

SlaveAddress UINT                   0                        65535                       0                       Rising
                                                                                      edge        at

NewDevState IL_ECAT_STATE           ECAT_STATE_INIT          ECAT_STATE_OP               ECAT_STATE_UNKNOWN      Rising
                                                                                      edge        at

Timeout      TIME                   T#0s                     n. def.                     T#0s                    Rising
                                                                                      edge        at

Functional description
Use the function block IL_ECATRemoteSlaveSetDevState to request an
EtherCAT state at a slave device.
The following EtherCAT states can be requested:
● Init
● PreOP
● Bootstrap
● SafeOP
● OP
Boundary conditions:
● The requested state in a slave device may not be higher than the one in
  the EtherCAT master bus state (e.g. if the master is in PreOP, a slave device
  cannot be switched to SafeOP or OP)
● The EtherCAT slave state "Bootstrap” is optional in the slave devices. The
  "Bootstrap” state can only be reached from the EtherCAT slave state "Init"
● If the requested bus state is not reached within the timeout monitoring
  ("Timeout" > T#0s), the function block reports an error, but the internal
  command execution cannot be stopped!

Implementation in ST
Beispiel:

PROGRAM EG_IL_ECATRemoteSlaveSetDevState
VAR
  fbIL_ECATRemoteSlaveSetDevState: IL_ECATRemoteSlaveSetDevState;
  strMasterName:                   STRING := 'ethercatmaster';
END_VAR

fbIL_ECATRemoteSlaveSetDevState.Execute          := TRUE;

fbIL_ECATRemoteSlaveSetDevState.MasterName   := ADR(strMasterName);
fbIL_ECATRemoteSlaveSetDevState.SlaveAddress := 1001;
fbIL_ECATRemoteSlaveSetDevState.NewDevState := IL_ECAT_STATE.ECAT_STATE_OP;
fbIL_ECATRemoteSlaveSetDevState();
IF TRUE = fbIL_ECATRemoteSlaveSetDevState.Done THEN
  ; // slave reached state operational
END_IF
IF TRUE = fbIL_ECATRemoteSlaveSetDevState.Error THEN
  ; // error handling
END_IF

Error description
For more information on the error codes, refer to:
⮫ Chapter 13.11 Error codes on page 257
⮫ Diagnostics 0C0F0000

## 13.9 Auxiliary functions

### 13.9.1 IL_ECATSoeAttributeDecoding

Brief description
The function IL_ECATSoeAttributeDecoding decodes the SoE parameter
“Attribute”.

Interface description

Table 169: Interface variables of the IL_ECATSoeAttributeDecoding function
I/O type             Name                          Data type                   Description

VAR_INPUT            Attribute                     DWORD                       SoE parameter “Attribute” value

RETURN VALUE         IL_ECATSoeAttributeDecoding   IL_ECAT_SOE_ATTRIBUTE       Parameter attribute as structure type

Functional description
The function IL_ECATSoeAttributeDecoding decodes the SoE parameter
“Attribute”.

Implementation in ST
Beispiel:

VAR
   dwAttribute : DWORD; // read value
   rAttribute : IL_ECAT_SOE_ATTRIBUTE;
END_VAR

rAttribute := IL_ECATSoeAttributeDecoding( dwAttribute );

Error description
The function IL_ECATSoeAttributeDecoding is not provided with any trouble‐
shooting.

### 13.9.2 IL_ECATSoeIdnCoding

Brief description
The function IL_ECATSoeIdnCoding summarizes the following individual ele‐
ments in one parameter identification number: Parameter type, parameter
block and data block number.

Interface description

Table 170: Interface variables of the IL_ECATSoeIdnCoding function
I/O type              Name                  Data type                    Description

VAR_INPUT             ParamType             IL_ECAT_SOE_PARAM_TYPE       Parameter type (S- or P-parameter)

ParamSet              USINT                        Parameter block (0..7)

BlockNum              UINT                         Data block number

RETURN VALUE          IL_ECATSoeIdnCoding   WORD                         Parameter identification number

Functional description
The function IL_ECATSoeIdnCoding summarizes the following individual ele‐
ments in one parameter identification number: Parameter type, parameter
block and data block number.

Implementation in ST
Beispiel:

 fbSoeRead.Idn := IL_ECATSoeIdnCoding(SOE_S_PARAM, 0,
1504); // ^= S-0-1504

Error description
The function IL_ECATSoeAttributeDecoding is not provided with any trouble‐
shooting.

## 13.10 Data types

### 13.10.1 IL_ECAT_ADDRESS_TYPE

Brief description
The enumeration type IL_ECAT_ADDRESS_TYPE describes the EtherCAT
addressing type.
Table 171: Elements of the IL_ECAT_ADDRESS_TYPE enumeration type
Name                                   Value              Description
ECAT_AUTOINC_ADDRESS                   0                  Auto-increment address
ECAT_ETHERCAT_ADDRESS                  1                  EtherCAT (fixed physical address)

### 13.10.2 IL_ECAT_BASE_DATA_TYPE

    Brief description
The enumeration type IL_ECAT_BASE_DATA_TYPE describes the data types acc.
of the ETG coding.
Table 172: Elements of the IL_ECAT_BASE_DATA_TYPE enumeration type
Name                                       Value     Description
ECAT_DATATYPE_BOOLEAN                      16#0001   BOOL
ECAT_DATATYPE_INTEGER8                     16#0002   Short Integer
ECAT_DATATYPE_INTEGER16                    16#0003   Integer
ECAT_DATATYPE_INTEGER32                    16#0004   Double Integer
ECAT_DATATYPE_UNSIGNED8                    16#0005   Unsigned Short Integer
ECAT_DATATYPE_UNSIGNED16                   16#0006   Unsigned Integer
ECAT_DATATYPE_UNSIGNED32                   16#0007   Unsigned Double Integer
ECAT_DATATYPE_REAL32                       16#0008   Floating Point
ECAT_DATATYPE_VISIBLE_STRING               16#0009   STRING(n), 1 byte per character
ECAT_DATATYPE_OCTET_STRING                 16#000A   ARRAY(0..n) OF BYTE, 1 byte per character
                                                     (+1)
ECAT_DATATYPE_UNICODE_STRING               16#000B   ARRAY(0..n) OF WORD, 2 bytes per character
                                                     (+1)
ECAT_DATATYPE_TIME_OF_DAY                  16#000C   -
ECAT_DATATYPE_TIME_DIFFERENCE              16#000D   -
ECAT_DATATYPE_DOMAIN                       16#000F   -
ECAT_DATATYPE_INTEGER24                    16#0010   -
ECAT_DATATYPE_REAL64                       16#0011   Long Float
ECAT_DATATYPE_INTEGER40                    16#0012   -
ECAT_DATATYPE_INTEGER48                    16#0013   -
ECAT_DATATYPE_INTEGER56                    16#0014   -
ECAT_DATATYPE_INTEGER64                    16#0015   Long Integer
ECAT_DATATYPE_UNSIGNED24                   16#0016   -
ECAT_DATATYPE_UNSIGNED40                   16#0018   -
ECAT_DATATYPE_UNSIGNED48                   16#0019   -
ECAT_DATATYPE_UNSIGNED56                   16#001A   -
ECAT_DATATYPE_UNSIGNED64                   16#001B   Unsigned Long Integer
ECAT_DATATYPE_GUID                         16#001D   Globally unique identifier, 128 bit
ECAT_DATATYPE_BYTE                         16#001E   1 Octet
ECAT_DATATYPE_WORD                         16#001F   2 Octet
ECAT_DATATYPE_DWORD                        16#0020   4 Octet
ECAT_DATATYPE_PDO_MAPPING                  16#0021   -
ECAT_DATATYPE_IDENTITY                     16#0023   -
ECAT_DATATYPE_COMMAND_PAR                  16#0025   -
ECAT_DATATYPE_PDO_PARAMETER                16#0027   -
ECAT_DATATYPE_ENUM                         16#0028   -
ECAT_DATATYPE_SYNC_PAR                     16#0029   -
ECAT_DATATYPE_RECORD                       16#002A   -
ECAT_DATATYPE_BACKUP_PARAM‐                16#002B   -
ETER
ECAT_DATATYPE_MOD_DEV_PROFILE              16#002C   Modular Device Profile

Name                                     Value       Description
ECAT_DATATYPE_BITARR8                    16#002D     8 individual bits
ECAT_DATATYPE_BITARR16                   16#002E     16 individual bits
ECAT_DATATYPE_BITARR32                   16#002F     32 individual bits
ECAT_DATATYPE_BIT1                       16#0030     -
ECAT_DATATYPE_BIT2                       16#0031     -
ECAT_DATATYPE_BIT3                       16#0032     -
ECAT_DATATYPE_BIT4                       16#0033     -
ECAT_DATATYPE_BIT5                       16#0034     -

ECAT_DATATYPE_BIT6                       16#0035     -
ECAT_DATATYPE_BIT7                       16#0036     -
ECAT_DATATYPE_BIT8                       16#0037     -

### 13.10.3 IL_ECAT_DC_SLAVE_CONFIG_INFO

  Brief description
The IL_ECAT_DC_SLAVE_CONFIG_INFO structure contains the Distributed
Clock configuration data for read and write direction. It can be requested via
the function block ⮫ IL_ECATGetDcSlaveConfigInfo.
Table 173: Elements of the IL_ECAT_DC_SLAVE_CONFIG_INFO structure
Structural element           Data type      Description
DcSupport                    BOOL           Slave supports DC (Distributed Clocks)
DcReferenceClock             BOOL           Slave is DC reference clock
CycleTime0                   UDINT          Cycle time of the Sync0 event in nanoseconds (defined
                                            in ETG 2100)
CycleTime1                   UDINT          Cycle time of the Sync1 event in nanoseconds (defined
                                            in ETG 2100)
ShiftTime                    DINT           Shift time of the Sync0 event in nanoseconds (defined
                                            in ETG 2100)

### 13.10.4 IL_ECAT_PORT_ERROR_COUNTERS

  Brief description
The structure IL_ECAT_PORT_ERROR_COUNTERS describes the error counter
of a port.
Table 174: Elements of the IL_ECAT_PORT_ERROR_COUNTERS structure
Structural element           Data type      Description
InvalidFrameCounters         BYTE           Error counter of invalid frames received
                                            (Register 0x0300/0x0302/0x0304/0x0306)
RxErrorCounter               BYTE           Error counter of invalid frames received (MII/EBUS)
                                            (Register 0x0301/0x0303/0x0305/0x0307)
FwdRxErrorCounter            BYTE           Error counter of invalid frames routed
                                            (Register 0x0308:0x030B)
LostLinkCounter              BYTE           Error counter of link loss
                                            (Register 0x0310:0x0313)
                                            Only if loop detection “Auto” and if the port is “open”

### 13.10.5 IL_ECAT_SLAVE_STATISTIC_COUNTERS

    Brief description
The structure IL_ECAT_SLAVE_STATISTIC_COUNTERS describes the error
counter of a slave device.
Table 175: Elements of the IL_ECAT_SLAVE_STATISTIC_COUNTERS structure
Structural element Data type                                Description
AlStatusCode       UINT                                     Application status code
ProcUnitError‐     BYTE                                     Error counter "Processing
Counter                                                     unit" (e.g. FCS)
                                                            (Register 0x030C)
PdiErrorCounter BYTE                                        Error counter "Process Data
                                                            Interface" (PDI)
                                                            (Register 0x030D)
PortErrorCounters ARRAY[0..3] OF ⮫ IL_ECAT_PORT_ERROR_COUN‐ Error counter per port
                  TERS

### 13.10.6 IL_ECAT_SOE_ATTRIBUTE

    Brief description
The structure IL_ECAT_SOE_ATTRIBUTE describes the SoE parameter attribute
(refer to IL_ECATSoeAttributeDecoding).
Table 176: Elements of the IL_ECAT_SOE_ATTRIBUTE structure
Structural element           Data type                  Description
Res31                        BOOL                       Bit 31: Reserved
WriteProtectedCp4            BOOL                       Bit 30: Parameter is write-protected in
                                                        the state OP (CP4)
WriteProtectedCp3            BOOL                       Bit 29: Parameter is write-protected in
                                                        the state SafeOP (CP3)
WriteProtectedCp2            BOOL                       Bit 28: Parameter is write-protected in
                                                        the state PreOP (CP2)
DecPoints                    USINT                      Bit 24-27: Number of decimal places
Res23                        BOOL                       Bit 23: Reserved
DataType                     IL_ECAT_SOE_DATA_TYPE      Bit 20-22: Data type and display format
IsCommand                    BOOL                       Bit 19: Parameter is a command
DataLength                   IL_ECAT_SOE_DATA_LENGTH    Bit 16-18: Data length
ConversionFactor             UINT                       Bit 0-15: Factor for representation

### 13.10.7 IL_ECAT_SOE_DATA_LENGTH

    Brief description
The enumeration type IL_ECAT_SOE_DATA_LENGTH supports the analysis of
the SoE parameter attribute with regard to data length and differentiation
between list parameter (VAR_x_BYTE) and individual parameter (FIX_x_BYTE)
(refer to IL_ECATSoeAttrbuteDecoding).
Table 177: Elements of the IL_ECAT_SOE_DATA_LENGTH enumeration type
Name                                     Value    Description
SOE_DATALENGTH_RES0                      0        Reserved
SOE_DATALENGTH_FIX_2_BYTE                1        Data length is 2 bytes
SOE_DATALENGTH_FIX_4_BYTE                2        Data length is 4 bytes
SOE_DATALENGTH_FIX_8_BYTE                3        Data length is 8 bytes

Name                                  Value        Description
SOE_DATALENGTH_VAR_1_BYTE             4            Data length is variable with 1 byte of data
SOE_DATALENGTH_VAR_2_BYTE             5            Data length is variable with 2 bytes of data
SOE_DATALENGTH_VAR_4_BYTE             6            Data length is variable with 4 bytes of data
SOE_DATALENGTH_VAR_8_BYTE             7            Data length is variable with 8 bytes of data

### 13.10.8 IL_ECAT_SOE_DATA_STATUS

  Brief description
The enumeration type IL_ECAT_SOE_DATA_STATUS describes the data status
of an SoE parameter (e.g. bits 0-3 are used for the status of a command

execution).
Table 178: Elements of the IL_ECAT_SOE_DATA_STATUS enumeration type
Name                                  Value      Description
SOE_DATA_CMD_NOT_SET                  0          Command is not yet enabled or it was canceled
SOE_DATA_CMD_SET                      1          Command was enabled
SOE_DATA_CMD_END_OK                   3          Command execution was completed successfully
SOE_DATA_CMD_INTERRUPTED              5          Command execution was interrupted
SOE_DATA_CMD_RUNNING                  7          Command is enabled, but not yet completed
SOE_DATA_CMD_ERROR                    15         Error: Command execution not possible
SOE_DATA_DATUM_INVALID                256        (Bit 8) data is invalid

### 13.10.9 IL_ECAT_SOE_DATA_TYPE

  Brief description
The enumeration type IL_ECAT_SOE_DATA_TYPE supports the analysis of the
SoE parameter attribute with regard to data type and display format (refer to
IL_ECATSoeAttributeDecoding).
Table 179: Elements of the IL_ECAT_SOE_DATA_TYPE enumeration type
Name                            Value         Description
SOE_DATATYPE_BINARY             0             Binary number (representation binary)
SOE_DATATYPE_UDEC               1             Integer without sign (decimal representation)
SOE_DATATYPE_DEC                2             Integer with sign (decimal representation)
SOE_DATATYPE_HEX                3             Integer without sign (hexadecimal representation)
SOE_DATATYPE_TEXT               4             Extended character set (text representation)
SOE_DATATYPE_IDN                5             Integer without sign (IDN representation, e.g
                                              "S-0-0000")
SOE_DATATYPE_FLOAT              6             Floating point number (decimal representation with
                                              exponent)
SOE_DATATYPE_RES7               7             Reserved

### 13.10.10 IL_ECAT_SOE_ELEMENT

  Brief description
The enumeration type IL_ECAT_SOE_ELEMENT describes the elements of an
SoE parameter.
Table 180: Elements of the IL_ECAT_SOE_ELEMENT enumeration type
Name                                Value              Description
SOE_ELEMENT_STATUS                  16#01              Service channel of data status
SOE_ELEMENT_NAME                    16#02              Name (max. 64 bytes) (optional)
SOE_ELEMENT_ATTRIBUTE               16#04              Attribute

Name                                 Value               Description
SOE_ELEMENT_UNIT                     16#08               Unit (optional)
SOE_ELEMENT_MIN                      16#10               Minimum value (optional)
SOE_ELEMENT_MAX                      16#20               Maximum value (optional)
SOE_ELEMENT_OPDATA                   16#40               Operating data
SOE_ELEMENT_DEFAULT                  16#80               Default value (optional)

### 13.10.11 IL_ECAT_SOE_PARAM_TYPE

    Brief description
The enumeration type IL_ECAT_SOE_PARAM_TYPE distinguishes between SoE
standard parameters and product-specific parameters.
Table 181: Elements of the IL_ECAT_SOE_PARAM_TYPE enumeration type
Name                                 Value               Description
SOE_S_PARAM                          0                   Standard IDN (“S-parameters”)
SOE_P_PARAM                          1                   Product-specific IDN (“P-parameters”)

### 13.10.12 IL_ECAT_STATE

    Brief description
    The enumeration type IL_ECAT_STATE describes the EtherCAT state.
Table 182: Elements of the IL_ECAT_STATE enumeration type
Name                                 Value       Description
ECAT_STATE_UNKNOWN                   0           EtherCAT state “Unknown”
ECAT_STATE_INIT                      1           EtherCAT state “Init”
ECAT_STATE_PREOP                     2           EtherCAT state “Pre-Operational”
ECAT_STATE_BOOTSTRAP                 3           EtherCAT state “Bootstrap” (only for slaves,
                                                 optional state for slave devices are mainly for firm‐
                                                 ware update. It can only be reached from the slave
                                                 state “Init”.)
ECAT_STATE_SAFEOP                    4           EtherCAT state “Safe-Operational”
ECAT_STATE_OP                        8           EtherCAT state “Operational”

### 13.10.13 IL_ECAT_DL_STATUS

    Brief description
The structure IL_ECAT_DL_STATUS describes the Data Link status of an
EtherCAT slave (ESC register 0x0110:0x0111).
Table 183: Elements of the IL_ECAT_DL_STATUS structure
Structural element             Data type     Description
PdiOperationalEeprom‐          BIT           Bit 0.0: PDI operational, EEPROM loaded correctly
Loaded
PdiWatchdogStatus              BIT           Bit 0.1: Watchdog loaded/running
EnhancedLinkDetection          BIT           Bit 0.2: Extended link detection for at least one port
Reserved03                     BIT           Bit 0.3: Reserved
LinkPort0                      BIT           Bit 0.4: Link at port 0
LinkPort1                      BIT           Bit 0.5: Link at port 1
LinkPort2                      BIT           Bit 0.6: Link at port 2
LinkPort3                      BIT           Bit 0.7: Link at port 3
LoopClosedPort0                BIT           Bit 1.0: Port 0 closed

Structural element            Data type     Description
CommunicationPort0            BIT           Bit 1.1: Communication at port 0
LoopClosedPort1               BIT           Bit 1.2: Port 1 closed
CommunicationPort1            BIT           Bit 1.3: Communication at port 1
LoopClosedPort2               BIT           Bit 1.4: Port 2 closed
CommunicationPort2            BIT           Bit 1.5: Communication at port 2
LoopClosedPort3               BIT           Bit 1.6: Port 3 closed
CommunicationPort3            BIT           Bit 1.7: Communication at port 3

### 13.10.14 IL_ECAT_ESC_FEATURES

Brief description
The structure IL_ECAT_ESC_FEATURES describes the properties of an
EtherCAT slave controller (ESC register 0x0008:0x0009).
Table 184: Elements of the IL_ECAT_ESC_FEATURES structure
Structural element            Data type     Description
FmmuOperationByte             BIT           Bit 0.0: Fieldbus Memory Management Unit (FALSE =
                                            Bit-oriented, TRUE = Byte-oriented)
Reserved01                BIT               Bit 0.1: Reserved
DcSupport                 BIT               Bit 0.2: Distributed Clocks is supported
Dc64Support               BIT               Bit 0.3: Distributed Clocks 64 bits is supported
LowJitterEbus             BIT               Bit 0.4: Jitter minimized
EnhancedLinkDetectio‐     BIT               Bit 0.5: Extended link detection EBUS
nEbus
EnhancedLinkDetectionMii BIT                Bit 0.6: Extended link detection MII
SeparateHandlingFcsErrors BIT               Bit 0.7: FCS errors are analyzed individually
EnhancedDcSyncActivation BIT                Bit 1.0: Extended DC Sync activation
LrwCommandNotSupported BIT                  Bit 1.1: LRW command not supported
RwCommandNotSupported BIT                   Bit 1.2: BRW/APRW/FPRW commands not supported
FixedFmmuSyncManConfig BIT                  Bit 1.3: Fix FMMU/SyncManager configuration
Reserved14                BIT               Bit 1.4: Reserved
Reserved15                BIT               Bit 1.5: Reserved
Reserved16                BIT               Bit 1.6: Reserved
Reserved17                BIT               Bit 1.7: Reserved

### 13.10.15 IL_ECAT_MASTER_FRAME_STATISTIC_COUNTERS

Brief description
The structure IL_ECAT_MASTER_FRAME_STATISTIC_COUNTERS contains
EtherCAT frame statistic counters providing information on the number of sent
cyclic and acyclic EtherCAT telegrams (see ⮫ IL_ECATGetMasterFrameStatistic‐
Counters).
Table 185: Elements of the IL_ECAT_MASTER_FRAME_STATISTIC_COUNTERS structure
Structural element           Data type     Description
NumTxFrames                  UDINT         Counter of sent frames
NumRxFrames                  UDINT         Counter of received frames
NumCyclicFrames              UDINT         Counter of cyclic frames
NumCyclicDatagrams           UDINT         Counter of cyclic data packages
NumAcyclicFrames             UDINT         Counter of acyclic frames
NumAcyclicDatagrams          UDINT         Counter of acyclic data packages

Structural element            Data type       Description
NumLostFrames                 UDINT           Counter of lost frames
NumLostCyclicFrames           UDINT           Counter of lost cyclic frames
NumLostAcyclicFrames          UDINT           Counter of lost acyclic frames

### 13.10.16 IL_ECAT_MASTER_MAILBOX_STATISTIC_COUNTERS

        Brief description
        The IL_ECAT_MASTER_MAILBOX_STATISTIC_COUNTERS structure contains the
        individual master protocol statistics for the respective mailbox protocol. It can
        be requested via the ⮫ IL_ECATGetMasterMailboxStatisticCounters function.
Table 186: Elements of the IL_ECAT_MASTER_MAILBOX_STATISTIC_COUNTERS structure
Structural     Data type                                             Description
element
Aoe            ⮫ IL_ECAT_MASTER_PROTOCOL_STATISTIC                   Protocol statistics for AoE
Coe            ⮫ IL_ECAT_MASTER_PROTOCOL_STATISTIC                   Protocol statistics for CoE
Eoe            ⮫ IL_ECAT_MASTER_PROTOCOL_STATISTIC                   Protocol statistics for EoE
Foe            ⮫ IL_ECAT_MASTER_PROTOCOL_STATISTIC                   Protocol statistics for FoE
Soe            ⮫ IL_ECAT_MASTER_PROTOCOL_STATISTIC                   Protocol statistics for SoE
Voe            ⮫ IL_ECAT_MASTER_PROTOCOL_STATISTIC                   Protocol statistics for VoE
Raw            ⮫ IL_ECAT_MASTER_PROTOCOL_STATISTIC                   Protocol statistics for Raw

### 13.10.17 IL_ECAT_MASTER_PROTOCOL_STATISTIC

        Brief description
        The IL_ECAT_MASTER_PROTOCOL_STATISTIC structure contains the protocol
        statistic periods for the read and write direction. It is subordinated to the
        ⮫ IL_ECAT_MASTER_MAILBOX_STATISTIC_COUNTERS structure.
Table 187: Elements of the IL_ECAT_MASTER_PROTOCOL_STATISTIC structure
Structural     Data type                                             Description
element
Read           ⮫ IL_ECAT_MASTER_PROTOCOL_STA‐            Protocol statistic period counter
               TISTIC_PERIOD_COUNTERSIL_ECAT_MASTER_PRO‐ for the read direction
               TOCOL_STATISTIC_PERIOD_COUNTERS
Write          ⮫ IL_ECAT_MASTER_PROTOCOL_STA‐            Protocol statistic period counter
               TISTIC_PERIOD_COUNTERSIL_ECAT_MASTER_PRO‐ for the write direction
               TOCOL_STATISTIC_PERIOD_COUNTERS

### 13.10.18 IL_ECAT_MASTER_PROTOCOL_STATISTIC_COUNTERS

        Brief description
    The IL_ECAT_MASTER_PROTOCOL_STATISTIC_COUNTERS structure contains
    the protocol statistic counter number of requests and the number of bytes
    transferred. It is subordinated to the ⮫ IL_ECAT_MASTER_PROTOCOL_STA‐
    TISTIC_PERIOD_COUNTERS structure.
Table 188: Elements of the IL_ECAT_MASTER_PROTOCOL_STATISTIC_COUNTERS structure
Structural element                    Data type                  Description
NumRequests                           UDINT                      Number of requests
NumBytes                              UDINT                      Number of transferred data

### 13.10.19 IL_ECAT_MASTER_PROTOCOL_STATISTIC_PERIOD_COUNTERS

  Brief description
  The IL_ECAT_MASTER_PROTOCOL_STATISTIC_PERIOD_COUNTERS structure
  contains the protocol statistic counters for the last second and in total
  since the start of counting. It is subordinated to the ⮫ IL_ECAT_MASTER_PRO‐
  TOCOL_STATISTIC_COUNTERS structure.
Table 189: Elements of the IL_ECAT_MASTER_PROTOCOL_STATISTIC_PERIOD_COUNTERS structure
Structural    Data type                                          Description
element
Total         ⮫ IL_ECAT_MASTER_PROTOCOL_STATISTIC_COUN‐          Protocol statistic counter in total

TERS
LastSecond ⮫ IL_ECAT_MASTER_PROTOCOL_STATISTIC_COUN‐             Protocol statistic counter in the
TERS                                                  last second

### 13.10.20 IL_ECAT_MASTER_STATE

  Brief description
The union IL_ECAT_MASTER_STATE allows to easily change the bits of the
output "State" of ⮫ IL_ECATMasterState via a bit string.
Table 190: Elements of the union IL_ECAT_MASTER_STATE
Name           Data type                                    Description
StateBits      ⮫ IL_ECAT_MASTER_STATE_BITS                  Bit definition to evaluate the master
                                                            status
StateDword     DWORD

### 13.10.21 IL_ECAT_MASTER_STATE_BITS

  Brief description
The structure IL_ECAT_MASTER_STATE_BITS allows to easily change the bits of
the output "State" of ⮫ IL_ECATMasterState via a bit string.
Table 191: Elements of the IL_ECAT_MASTER_STATE_BITS structure
Structural element           Data type       Description
NoEthernetLink               BIT             0.0: No master Ethernet link
NotInStateOp                 BIT             0.1: Master is not in "Operational” state
NotInReqState                BIT             0.2: Master is not in requested state
Res03                        BIT             0.3: Reserved
StateInit                    BIT             0.4: Master is in "Init” state
StatePreOp                   BIT             0.5: Master is in "Pre-Operational” state
StateSafeOp                  BIT             0.6: Master is in "Safe-Operational” state
Res07                        BIT             0.7: Reserved
TopologyNotOk                BIT             1.0: Topology is not OK (the configured slaves do not
                                             match the online slaves)
SlavesNotInMasterState       BIT             1.1: One or multiple slaves are not in the master
                                             state
SlavesError                  BIT             1.2: One or multiple slaves report(s) an error
Res13                        BIT             1.3: Reserved
DcNotInSync                  BIT             1.4: "Distributed Clocks (DC) is not within the con‐
                                             figured limit values (only if DC is enabled)
Res15                        BIT             1.5: Reserved
…                            …               …

Structural element         Data type           Description
Res33                      BIT                 3.3: Reserved
SettingsInvalidOrInconsis‐ BIT                 3.4: Invalid or inconsistent settings
tent
PortError                  BIT                 3.5: Port not found
LicenseError               BIT                 3.6: No license available
Res37                      BIT                 3.7: Reserved

### 13.10.22 IL_ECAT_MBX_CONFIG_PROTOCOLS

    Brief description
The structure IL_ECAT_MBX_CONFIG_PROTOCOLS describes the supported
mailbox protocols of a configured slave device.
Table 192: Elements of the IL_ECAT_MBX_CONFIG_PROTOCOLS structure
Structural element              Data type      Description
MbxProtocolAoE                  BIT            Bit 0.0: ADS over EtherCAT (Automation Device Spec‐
                                               ification)
MbxProtocolEoE                  BIT            Bit 0.1: Ethernet over EtherCAT
MbxProtocolCoE                  BIT            Bit 0.2: CAN application protocol over EtherCAT
MbxProtocolFoE                  BIT            Bit 0.3: File access over EtherCAT
MbxProtocolSoE                  BIT            Bit 0.4: Servo drive profile over EtherCAT
MbxProtocolVoE                  BIT            Bit 0.5: Vendor specific profile over EtherCAT
Reserved06                      BIT            Bit 0.6: Reserved
…                               …              …
Reserved37                      BIT            Bit 3.7: Reserved

### 13.10.23 IL_ECAT_MBX_ONLINE_PROTOCOLS

    Brief description
The structure IL_ECAT_MBX_ONLINE_PROTOCOLS describes the supported
mailbox protocols of a slave device connected to the bus.
Table 193: Elements of the IL_ECAT_MBX_ONLINE_PROTOCOLS structure
Structural element                 Data type   Description
MbxProtocolAoE                     BIT         Bit 0.0: ADS over EtherCAT (Automation Device
                                               Specification)
MbxProtocolEoE                     BIT         Bit 0.1: Ethernet over EtherCAT
MbxProtocolCoE                     BIT         Bit 0.2: CAN application protocol over EtherCAT
MbxProtocolFoE                     BIT         Bit 0.3: File access over EtherCAT
MbxProtocolSoE                     BIT         Bit 0.4: Servo drive profile over EtherCAT
MbxProtocolVoE                     BIT         Bit 0.5: Vendor specific profile over EtherCAT
Reserved06                         BIT         Bit 0.6: Reserved
…                                  …           …
Reserved17                         BIT         Bit 1.7: Reserved

### 13.10.24 IL_ECAT_MBX_SIZE_INFO

    Brief description
    The structure IL_ECAT_MBX_SIZE_INFO describes the mailbox size of a slave
    device.

Table 194: Elements of the IL_ECAT_MBX_SIZE_INFO structure
Structural element             Data type      Description
SizeIn                         UDINT          Mailbox input size (slave reception)
SizeOut                        UDINT          Mailbox output size (slave sending)

### 13.10.25 IL_ECAT_MEMORY_INFO

Brief description
The structure IL_ECAT_MEMORY_INFO describes a memory range.
Table 195: Elements of the IL_ECAT_MEMORY_INFO structure

Structural element             Data type      Description
Offset                         UDINT          Memory offset
Size                           UDINT          Memory size

### 13.10.26 IL_ECAT_PORT_STATE

Brief description
The structure IL_ECAT_PORT_STATE describes the EtherCATport status of a
slave device.
In contrast to the DL status, only the status of the physical ports is shown.
Table 196: Elements of the IL_ECAT_PORT_STATE structure
Structural element             Data type      Description
ConnectionPort0                BIT            Bit 0.0: Connection at port 0
ConnectionPort1                BIT            Bit 0.1: Connection at port 1
ConnectionPort2                BIT            Bit 0.2: Connection at port 2
ConnectionPort3                BIT            Bit 0.3: Connection at port 3
LinkPort0                      BIT            Bit 0.4: Link at port 0
LinkPort1                      BIT            Bit 0.5: Link at port 1
LinkPort2                      BIT            Bit 0.6: Link at port 2
LinkPort3                      BIT            Bit 0.7: Link at port 3
LoopClosedPort0                BIT            Bit 1.0: Port 0 closed (only physical ports)
LoopClosedPort1                BIT            Bit 1.1: Port 1 closed (only physical ports)
LoopClosedPort2                BIT            Bit 1.2: Port 2 closed (only physical ports)
LoopClosedPort3                BIT            Bit 1.3: Port 3 closed (only physical ports)
CommunicationPort0             BIT            Bit 1.4: Communication at port 0
CommunicationPort1             BIT            Bit 1.5: Communication at port 1
CommunicationPort2             BIT            Bit 1.6: Communication at port 2
CommunicationPort3             BIT            Bit 1.7: Communication at port 3
                     The diagnostic bit "Connection(PortX)" is a logic connection of the other
                     status bits:
Communication     LoopClosed     LinkStatus     => Connection       Note
0                 0              0              0                   E.g. port not configured
0                 0              1              1                   -
0                 1              0              0                   Default "Loop closed"
0                 1              1              0                   Possibly “old” devices
1                 0              0              1                   possibly “old” devices
1                 0              1              1                   Default "Loop Open"
1                 1              0              0                   -
1                 1              1              0                   E.g. EK1122 "closed Port"

### 13.10.27 IL_ECAT_RESET_MASTER_FRAME_STATISTIC_COUNTERS

    Brief description
    The union IL_ECAT_RESET_MASTER_FRAME_STATISTIC_COUNTERS allows to
    easily set the bits of the input "ResetCounters" of ⮫ IL_ECATResetMasterFra‐
    meStatisticCounters via a bit string.
Table 197: Elements of the union IL_ECAT_RESET_MASTER_FRAME_STATISTIC_COUNTERS
Structural ele‐ Data type                                      Description
ment
ResetBits       ⮫ IL_ECAT_RESET_MASTER_FRAME_STA‐              Bit definition to reset the individual
                TISTIC_COUNTERS_BITS                           frame statistic counters
ResetDword      DWORD

### 13.10.28 IL_ECAT_RESET_MASTER_FRAME_STATISTIC_COUNTERS_BITS

    Brief description
The structure IL_ECAT_RESET_MASTER_FRAME_STATISTIC_COUNTERS_BITS
allows to easily set the bits of the input "ResetCounters" of ⮫ IL_ECATReset‐
MasterFrameStatisticCounters.
Table 198: Elements of the IL_ECAT_RESET_MASTER_FRAME_STATISTIC_COUNTERS_BITS structure
Structural element            Data type      Description
NumTxFrames                   BIT            0.0: Reset counter NumTxFrames
NumRxFrames                   BIT            0.1: Reset counter NumRxFrames
NumCyclicFrames               BIT            0.2: Reset counter NumCyclicFrames
NumCyclicDatagrams            BIT            0.3: Reset counter NumCyclicDatagrams
NumAcyclicFrames              BIT            0.4: Reset counter NumAcyclicFrames
NumAcyclicDatagrams           BIT            0.5: Reset counter NumAcyclicDatagrams
NumLostFrames                 BIT            0.6: Reset counter NumLostFrames
NumLostCyclicFrames           BIT            0.7: Reset counter NumLostCyclicFrames
NumLostAcyclicFrames          BIT            1.0: Reset counter NumLostAcyclicFrames
Res11                         BIT            1.1: Reserved
Res12                         BIT            1.2: Reserved
…                             …              …
Res37                         BIT            3.7: Reserved

### 13.10.29 IL_ECAT_SLAVE_CONFIG_INFO

    Brief description
The structure IL_ECAT_SLAVE_CONFIG_INFO describes information on a slave
device configured in the EtherCAT master.
Table 199: Elements of the IL_ECAT_SLAVE_CONFIG_INFO structure
Structural element Data type                                Description
AutoIncAddr        UINT                                     Auto increment address
EthercatAddr       UINT                                     EtherCAT address ("Fixed Physical
                                                            Address")
IdentifyAdo            UINT                                 Address offset (ADO) for identification
                                                            command
IdentifyValue          UINT                                 Identification value
SlaveHandle            DWORD                                Internal slave ID (internal use)
HcGroupIdx             DWORD                                Index of the Hot Connect Group (0 =
                                                            mandatory)

Structural element Data type                             Description
PreviousEtherca‐   UINT                                  EtherCAT address of the previous slave
tAddr                                                    (in the topology)
PreviousPort       UINT                                  Port of the previous slave (in the top‐
                                    ology)
SlaveIdentity        ⮫ IL_ECAT_SLAVE_IDENTITY_INFO       Slave identity information
SlaveName            STRING(127)                         Configured device name
MbxProtocols         ⮫ IL_ECAT_MBX_CONFIG_PROTO‐         Supported mailbox protocols
COLS
MbxStandard          ⮫ IL_ECAT_MBX_SIZE_INFO             Mailbox standard size

MbxBootstrap     ⮫ IL_ECAT_MBX_SIZE_INFO                 Mailbox bootstrap size
ProcessDataIn    ARRAY[0..3] OF                          Process data range of the inputs
⮫ IL_ECAT_MEMORY_INFO
ProcessDataOut   ARRAY[0..3] OF                          Process data range of the outputs
⮫ IL_ECAT_MEMORY_INFO
NumProcessVarsIn UINT                                    Number of input process data of the
                                    variables
NumProcess‐          UINT                                Number of output process data of the
VarsOut                                                  variables
PortDescriptor       BYTE                                Port descriptor (0b10 = EBUS, 0b11
                                    = MII/…) (Port0^Bit0:1, Port1^Bit2:3,
                                    etc.)
Reserved01         ARRAY[0..2] OF BYTE                   Reserved
WkcStateDiagOffsIn ARRAY[0..3] OF UINT                   Internal (internal use)
WkcStateDia‐       ARRAY[0..3] OF UINT                   Internal (internal use)
gOffsOut
Reserved02         ARRAY[0..2] OF UDINT                  Reserved
IsPresent          BOOL                                  Slave currently connected to the bus
                                    (online)
IsHcGroupPresent     BOOL                                Hot Connect Group of the slave cur‐
                                    rently connected to the bus
DcSupport            BOOL                                Slave supports DC (Distributed
                                    Clocks)

### 13.10.30 IL_ECAT_SLAVE_IDENTITY_INFO

Brief description
The structure IL_ECAT_SLAVE_IDENTITY_INFO describes identity data of an
EtherCAT slave device.
Table 200: Elements of the IL_ECAT_SLAVE_IDENTITY_INFO structure
Structural element           Data type         Description
VendorId                     UDINT             Vendor ID (e.g. Rexroth = 16#24)
ProductCode                  UDINT             Product code (vendor-specific)
RevisionNumber               UDINT             Revision number
SerialNumber                 UDINT             Serial number

### 13.10.31 IL_ECAT_SLAVE_ONLINE_INFO

Brief description
The structure IL_ECAT_SLAVE_ONLINE_INFO describes the “online” informa‐
tion of a slave device connected to the EtherCAT master.

Table 201: Elements of the IL_ECAT_SLAVE_ONLINE_INFO structure
Structural element Data type                         Description
AutoIncAddr        UINT                              Auto increment address
EthercatAddr       UINT                              EtherCAT address ("Fixed Physical
                                                     Address") (ESC register 0x0010)
StationAlias           UINT                          Station Alias ("Second Slave Address")
                                                     (ESC register 0x0012)
IdentifyValue          UINT                          Identification value (only if
                                                     an ADO is configured, see
                                                     ⮫ IL_ECAT_SLAVE_CONFIG_INFO → Identi‐
                                                     fyAdo)
SlaveHandle      DWORD                               Internal slave ID (internal use)
PortSlaveHandles ARRAY[0..3] OF DWORD                Port internal slave IDs (internal use)
SlaveIdentity    ⮫ IL_ECAT_SLAVE_IDENTITY_INFO       Slave identity information (EEPROM
                                                     offset 0x0008)
EscType                BYTE                          EtherCAT slave controller type (ESC reg‐
                                                     ister 0x0000)
EscRevision            BYTE                          EtherCAT slave controller revision number
                                                     (ESC register 0x0001)
EscBuild               WORD                          EtherCAT slave controller build number
                                                     (ESC register 0x0002)
EscFeatures            ⮫ IL_ECAT_ESC_FEATURES        EtherCAT slave controller-supported fea‐
                                                     tures (ESC register 0x0008)
PortDescriptor         BYTE                          Port descriptor (ESC register 0x0007)
                                                     (0b10 = EBUS, 0b11 = MII/…)
                                                     (Port0^Bit0:1, Port1^Bit2:3, etc.)
Reserved01             BYTE                          Reserved
AlStatus               WORD                          Application Layer Status (ESC register
                                                     0x0130)
AlStatusCode           WORD                          Application Layer Status Code (ESC reg‐
                                                     ister 0x0134) (reset when the state of the
                                                     slave changes in the master)
MbxProtocols           ⮫ IL_ECAT_MBX_ONLINE_PROTO‐   Supported mailbox protocols (EEPROM
                       COLS                          offset 0x001C). The value is "0” if the
                                                     slave is configured in the master, see
                                                     ⮫ IL_ECAT_SLAVE_CONFIG_INFO.
DlStatus               ⮫ IL_ECAT_DL_STATUS           Data Link Status (ESC register 0x0110)
PortState              ⮫ IL_ECAT_PORT_STATE          Port status
PreviousPort           UINT                          Port of the previous slave (in the top‐
                                                     ology)
SystemTimeDiffer‐ UDINT                              System time difference in ns (ESC register
ence                                                 0x092C) (this value is only valid if DC is
                                                     configured)
SlaveDelay             UDINT                         Time delay “after” the slave in ns (this
                                                     value is only valid if DC is configured)
PropagationDelay       UDINT                         Transmission delay in ns (ESC register
                                                     0x0928) (this value is only valid if DC is
                                                     configured)
Reserved02             ARRAY[0..3] OF DWORD          Reserved
DcSupport              BOOL                          Slave supports DC (Distributed Clocks)

Structural element Data type                             Description
Dc64Support        BOOL                                  Slave supports 64 bits DC (Distributed
                                    Clocks)
IsRefClock           BOOL                                Slave is reference clock
LineCrossed          BOOL                                EtherCAT cabling of the slave is incorrect
                                    (IN-OUT port interchanged)

### 13.10.32 IL_ECAT_SLAVE_STATE

Brief description
The union IL_ECAT_SLAVE_STATE allows to easily change the bits of the output

"State" of ⮫ IL_ECATRemoteSlaveState via a bit string.
Table 202: Elements of the union IL_ECAT_SLAVE_STATE
Name                   Data type                Description
StateBits              ⮫ IL_ECAT_SLAVE_STATE_BI Bit definition to evaluate the slave status
                       TS
StateDword             DWORD

### 13.10.33 IL_ECAT_SLAVE_STATE_BITS

Brief description
The structure IL_ECAT_SLAVE_STATE_BITS allows to easily change the bits of
the output "State" of ⮫ IL_ECATRemoteSlaveState via a bit string.
Table 203: Elements of the IL_ECAT_SLAVE_STATE_BITS structure
Structural element           Data type      Description
NotOnline                    BIT            0.0: Slave is not connected to the bus
NotInStateOp                 BIT            0.1: Slave is not in the state "Operational"
Error                        BIT            0.2: Slave reports errors, refer to "AL status code"
Res03                        BIT            0.3: Reserved
StateInit                    BIT            0.4: Slave is in "Init" state (Init & PreOp = Bootstrap)
StatePreOp                   BIT            0.5: Slave is in "Pre-Operational" state (Init & PreOp =
                                            Bootstrap)
StateSafeOp                  BIT            0.6: Slave is in "Safe-Operational" state
Res07                        BIT            0.7: Reserved
Res10                        BIT            1.0: Reserved
…                            …              …
Res37                        BIT            3.7: Reserved

## 13.11 Error codes

All error codes of the Ethercat master are part of the ctrlX diagnostic system.
The main diagnostic number is output at the "ErrorIdent.Additional1” output
and the detailed diagnostics of the ctrlX diagnostic database is output at the
"ErrorIdent.Additional2”.

Related documents:
Refer to the diagnostics ⮫ 0C0F0000 in the documentation "ctrlX CORE Diag‐
nostics" (DOK-XCORE*-DIAG*******-RE03-EN-E)
