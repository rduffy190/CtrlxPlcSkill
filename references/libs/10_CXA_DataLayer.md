# 10 CXA_DataLayer

## 10.1 Introduction and overview

The CXA_Datalayer library contains function blocks and methods allowing
access from the IEC program to the Data Layer.
The Data Layer is a central instance to access nearly all data elements of the
ctrlX.
The library provides access to the following data in three folders:
● Non-real-time-capable data
● Real-time-capable data
● FlatBuffer

The function blocks providing simple access to the Data Layer are stored in
the POUs directory of the Datalayer_NRT folder.
Simple accesses to the Data Layer require only the NodeName (e.g.: "plc/app/
Application/admin/properties/name") and the data type to be read or written.
The "Advanced” folder provides more complex function blocks and methods
and allows to completely access the Data Layer (e.g. accesses to arrays).

## 10.2 Important information on programming

From the library version 1.2.6.0, theData Layer is accessed asynchronously.
With older versions, the access was synchronous and it was possible that
it was blocked. Thus, the processing time could increase to multiple millisec‐
onds (>100).
Access is not blocked anymore from the version 1.2.6.0. The time required to
completely execute the function block did not change.
As the calls have to be asynchronous, the input parameters of the function
blocks (NodeName, ClientId, NodeValues) have to remain constant and may
not change. Otherwise, error messages might be issued during processing.

## 10.3 Time response (sequence) of the function blocks

All function blocks implement the interface of the basic function block
"IL_ExecuteDoneBase".
Thus, each function block assigns the “Execute” input and the outputs “Done”
and “Active”. Furthermore, the error outputs "Error", "ErrorIDC" and "ErrorI‐
dent” are provided.
The basic function block implements a state machine suitable for standard
inputs and outputs. Function blocks of this type are used for non-recurring
tasks requiring a processing time of multiple cycles.

Interface description

Table 57: Interface variables of the IL_ExecuteDoneBase function block
                      Name             Type                Comment
VAR_INPUT             Execute          BOOL                Processing ena‐
                                                           bled (cyclic, edge-
                                                           controlled)
VAR_OUTPUT            Done             BOOL                Function block
                                                           completed proc‐
                                                           essing without
                                                           error
                      Active           BOOL                The function block
                                                           was started

                      Error            BOOL                Indicates that an
                                                           error occurred
                      ErrorID          ⮫ ERROR_CODE        Error cause
                      ErrorIdent       ⮫ ERROR_STRUCT Detailed error
                                                      cause

Signal-time diagram

## 10.4 “Simple” function blocks

### 10.4.1 Introduction and overview

The following function blocks are available to access the Data Layer simply:
● DL_BrowseNode - Browses all direct child nodes
  – GetChildNam - Method to read all child nodes
● DL_CreateNode - Creating a node, e.g. to control activities "axispro‐
  file/system/opstate/cmd",
  “Booting” can for example be sent as input parameter.
● DL_ReadNode - Reading a node
● DL_WriteNode - Writing to a node
● DL_DeleteNode - Deleting a node, e.g. to delete an activity "axispro‐
  file/system/opstate/cmd"
The "ClientId” input is not yet supported and does not have to be set.

### 10.4.2 DL_BrowseNode

Brief description
This function block calls the "browse service" of the Data Layer to return the
number and names of all directly subordinate nodes.

Interface description

Programming example to use DL_BrowseNode and GetChildName

Declaration:

VAR
   fbBrowseNode    : DL_BrowseNode;   // Instance of function block DL_BrowseNode
   ChildPtr : POINTER TO POINTER TO STRING;
   ChildNum : UDINT;
   ArrayIndex : UDINT;
   StringPtr : POINTER TO STRING;
   ArrayElementPtr : POINTER TO POINTER TO STRING;

      Child : ARRAY[0..32] OF STRING;   // Array where the child names are copied to.
                                          // Only for demonstration, the array bounds are not
checked
END_VAR

Implementation:

fbBrowseNode(Execute:= TRUE, NodeName:= 'plc', ChildPtr=> ChildPtr, ChildNum=> ChildNum);

// When fbBrowseNode signals "Done" then the returned child names are copied to a fixed
size array of strings.
// This is only to demonstrate the access to the child names. For simplicity it is not
checked if ChildNum
// is larger than array size.

// Here are shown two ways to access the child names:

// First example: using output parameter ChildPtr

IF fbBrowseNode.Done = TRUE THEN
  FOR ArrayIndex := 0 TO ChildNum - 1 DO
    ArrayElementPtr := (ChildPtr + (ArrayIndex * SIZEOF(POINTER TO STRING)));
    StringPtr := ArrayElementPtr^;
    StrCpyA(pBuffer:= ADR(Child[ArrayIndex]), iBufferSize:= SIZEOF(Child[ArrayIndex]),
pStr:= StringPtr);
  END_FOR;
END_IF;

// Second example: using method GetChildNode()

IF fbBrowseNode.Done = TRUE THEN
  FOR ArrayIndex := 0 TO ChildNum - 1 DO
    Child[ArrayIndex] := fbBrowseNode.GetChildName(Index:= ArrayIndex);
  END_FOR;
END_IF;

The test program requires the library "StringUtils” additionally.

### 10.4.3 DL_CreateNode

Brief description
The DL_CreateNode function block calls the "create service" of the Data Layer.

Creating a new node can also control activities for example (“axispro‐
file/system/opstate/cmd“). “Booting” can for example be sent as input param‐
eter.

Interface description

Table 58: Interface variables of the DL_CreateNode function block
            Name              Type                    Description                    Applied from
Input       Execute           BOOL                    Rising edge starts the         IL_ExecuteDoneBase
                                                      processing
Output      Done              BOOL                    Processing completed           IL_ExecuteDoneBase
            Active            BOOL                    In process                     IL_ExecuteDoneBase
            Error             BOOL                    An error occurred              IL_ExecuteDoneBase
            ErrorID           ⮫ ERROR_CODE            Error classification           IL_ExecuteDoneBase
            ErrorIdent        ⮫ ERROR_STRUCT          Detailed error cause           IL_ExecuteDoneBase
Input       ClientId          ⮫ IL_HANDLE             ID of the Data Layer
                                                      client
            NodeName          REFERENCE TO            Name of the node in the
                              STRING(255)             Data Layer
            ValueIn           __SYSTEM.AnyType
            ValueOut          __SYSTEM.AnyType

Test program for the DL_CreateNode

Declaration:

VAR
    m_fbCreateNode : CXA_Datalayer.DL_CreateNode;
    m_Execute : BOOL;
    m_ValueIn : STRING;
    m_ValueOut : UDINT;
    m_address : STRING;
END_VAR

Implementation:

m_address := 'motion/cmd/opstate';   // write motion opstate
m_ValueIn := 'Booting';
m_Execute := TRUE;
m_fbCreateNode(Execute:= m_Execute, NodeName:= m_address, ValueIn:= m_ValueIn, ValueOut:=
m_ValueOut);

IF (m_fbCreateNode.Done = TRUE) OR (m_fbCreateNode.Error = TRUE) THEN
  m_Execute := FALSE;
  m_fbCreateNode(Execute:= m_Execute, NodeName:= m_address, ValueIn:= m_ValueIn,
ValueOut:= m_ValueOut);
END_IF

### 10.4.4 DL_ReadNode

Brief description
The DL_ReadNode function block calls the "read service" of the Data Layer.
The user specifies the data type to be read out in the "Value" input.

Interface description

Table 59: Interface variables of the DL_ReadNode function block
              Name              Type                    Description                    Applied from
Input         Execute           BOOL                    Rising edge starts the         IL_ExecuteDoneBase
                                                        processing
Output        Done              BOOL                    Processing completed           IL_ExecuteDoneBase
              Active            BOOL                    In process                     IL_ExecuteDoneBase
              Error             BOOL                    An error occurred              IL_ExecuteDoneBase
              ErrorID           ⮫ ERROR_CODE            Error classification           IL_ExecuteDoneBase
              ErrorIdent        ⮫ ERROR_STRUCT          Detailed error cause           IL_ExecuteDoneBase
Input         ClientId          ⮫ IL_HANDLE      ID of the Data Layer
                                                 client
              NodeName          REFERENCE TO     Name of the node in the
                                STRING(255)      Data Layer
              Value             __SYSTEM.AnyType Value returned by the
                                                 node
Output        Size              DINT

Test program for the DL_ReadNode

Declaration:

VAR
  m_fbReadNode : CXA_Datalayer.DL_ReadNode;
    m_Execute : BOOL;
  m_value : STRING;
  m_address : STRING;
END_VAR

Implementation:

m_address := 'plc/app/Application/sym/Gvl/iecString';
m_Execute := TRUE;

m_fbReadNode(Execute:= m_Execute, NodeName:= m_address, Value:= m_value);
IF (m_fbReadNode.Done = TRUE) OR (m_fbReadNode.Error = TRUE) THEN
  m_Execute := FALSE;
  m_fbReadNode(Execute:= m_Execute, NodeName:= m_address, Value:= m_value);
END_IF

### 10.4.5 DL_WriteNode

Brief description
The DL_WriteNode function block calls the "write service" of the Data Layer.
The user specifies the data type to be written in the “Value” input. If the data
type does not match the actual data type, it is tried to change the transferred
data type to the correct data type. If this is not possible, an error is issued.

Interface description

Table 60: Interface variables of the DL_WriteNode function block
            Name              Type                    Description                     Applied from
Input       Execute           BOOL                    Rising edge starts the          IL_ExecuteDoneBase
                                                      processing
Output      Done              BOOL                    Processing completed            IL_ExecuteDoneBase
            Active            BOOL                    In process                      IL_ExecuteDoneBase
            Error             BOOL                    An error occurred               IL_ExecuteDoneBase
            ErrorID           ⮫ ERROR_CODE            Error classification            IL_ExecuteDoneBase
            ErrorIdent        ⮫ ERROR_STRUCT          Detailed error cause            IL_ExecuteDoneBase
Input       ClientId          ⮫ IL_HANDLE      ID of the Data Layer
                                               client
            NodeName          REFERENCE TO     Name of the node in the
                              STRING(255)      Data Layer
            Value             __SYSTEM.AnyType Value to write to a node

Test program for the DL_WriteNode

Declaration:

VAR
m_fbWriteNode : CXA_Datalayer.DL_WriteNode;
      m_Execute : BOOL;
  m_value : BOOL;
  m_address : STRING;
END_VAR

Implementation:

m_address := 'plc/app/Application/sym/Gvl/iecBool';
m_value := TRUE;

m_Execute := TRUE;
m_fbWriteNode(Execute:= m_Execute, NodeName:= m_address, Value:= m_value);

IF (m_fbWriteNode.Done = TRUE) OR (m_fbWriteNode.Error = TRUE) THEN
  m_Execute := FALSE;
  m_fbWriteNode(Execute:= m_Execute, NodeName:= m_address, Value:= m_value);
END_IF

### 10.4.6 DL_DeleteNode

Brief description
The DL_DeleteNode function block calls the "delete service" of the Data
Layer. This allows to again delete any nodes created with DL_CreateNode for
example.

Interface description

Table 61: Interface variables of the DL_DeleteNode function block
              Name              Type                    Description                    Applied from
Input         Execute           BOOL                    Rising edge starts the         IL_ExecuteDoneBase
                                                        processing
Output        Done              BOOL                    Processing completed           IL_ExecuteDoneBase
              Active            BOOL                    In process                     IL_ExecuteDoneBase
              Error             BOOL                    An error occurred              IL_ExecuteDoneBase
              ErrorID           ⮫ ERROR_CODE            Error classification           IL_ExecuteDoneBase
              ErrorIdent        ⮫ ERROR_STRUCT          Detailed error cause           IL_ExecuteDoneBase
Input         ClientId          ⮫ IL_HANDLE             ID of the Data Layer
                                                        client
              NodeName          REFERENCE TO            Name of the node in Data
                                STRING(255)             Layer

Test program for the DL_DeleteNode

Declaration:

VAR
   m_fbDeleteNode : CXA_Datalayer.DL_DeleteNode;
   m_Execute : BOOL;
   m_address : STRING;
   Result: CXA_Datalayer.DL_RESULT;
   value : INT;
END_VAR

Implementation:

m_address := 'motion/axs/Axis_1';

m_Execute := TRUE;
m_fbDeleteNode(Execute:= m_Execute, NodeName:= m_address);
IF (m_fbDeleteNode.Done = TRUE) OR (m_fbDeleteNode.Error = TRUE) THEN
  m_Execute := FALSE;
  m_fbDeleteNode(Execute:= m_Execute, NodeName:= m_address);
END_IF

## 10.5 “Advanced” function blocks

### 10.5.1 Introduction and overview

Use the "Advanced" function blocks for all non-real-time-capable accesses
to the Data Layer. Unlike the standard data types (simple types such as
BOOL or INT), nodes can also consist of more complex data types. Using
DL_NodeValue enables the user to also use these data types (for example via
FlatBuffers).

### 10.5.2 DL_NodeValue

Brief description

Each node with data in the Data Layer has a so-called "NodeValue".
Use this NodeValue to read or write all data values of all supported data types
of the Data Layer.
The function block DL_NodeValue provides methods to access a NodeValue in
the Data Layer.
All other function blocks of the "Advanced” folder require a instance of
the DL_NodeValue as input for the respective function block. Thus, before
calling an instance of DL_CreateNodeValue, DL_ReadNodeValue or DL_Write‐
NodeValue, create an instance of the type DL_NodeValue.

### 10.5.3 DL_CreateNodeValue

Brief description
The DL_CreateNodeValue function block calls the "create service" of the Data
Layer.
Creating a new node can also control activities for example (“axispro‐
file/system/opstate/cmd“). “Booting” can for example be sent as input param‐
eter.

Interface description

Table 62: Interface variables of the DL_CreateNodeValue function block
           Name               Type                Description               Applied from
Input      Execute            BOOL                Rising edge starts the    IL_ExecuteDoneBase
                                                  processing
Output     Done               BOOL                Processing completed      IL_ExecuteDoneBase
           Active             BOOL                In process                IL_ExecuteDoneBase
           Error              BOOL                An error occurred         IL_ExecuteDoneBase
           ErrorID            ⮫ ERROR_CODE        Error classification      IL_ExecuteDoneBase
           ErrorIdent         ⮫ ERROR_STRUCT Detailed error cause           IL_ExecuteDoneBase
Input      ClientId           ⮫ IL_HANDLE    ID of the Data Layer
                                             client

Name                  Type                   Description                   Applied from
NodeName              REFERENCE TO           Name of the node in the
           STRING(255)            Data Layer
NodeValueIn           REFERENCE TO           NodeValue to be written
           DL_NodeValue           to the node
NodeValueOut          REFERENCE TO           NodeValue returned by
           DL_NodeValue           the node

Test program for the DL_CreateNodeValue

Declaration:

VAR
      Result: CXA_Datalayer.DL_RESULT;
      m_fbCreateNodeValue : CXA_Datalayer.DL_CreateNodeValue;
      m_Execute : BOOL;
      m_NodeValueIn : DL_NodeValue;
      m_NodeValueOut : DL_NodeValue;
      m_address : STRING;
      value : STRING;

END_VAR

Implementation:

m_address := 'motion/cmd/opstate';   // write motion opstate
m_Execute := TRUE;
value :='Booting';
Result := m_NodeValueIn.SetValueString(ADR(value));
m_fbCreateNodeValue(Execute:= m_Execute, NodeName:= m_address, NodeValueIn:=
m_NodeValueIn, NodeValueOut:= m_NodeValueOut);

// Zugriff beenden
IF (m_fbCreateNodeValue.Done = TRUE) OR (m_fbCreateNodeValue.Error = TRUE) THEN
   m_Execute := FALSE;
  m_fbCreateNodeValue(Execute:= m_Execute, NodeName:= m_address, NodeValueIn:=
m_NodeValueIn, NodeValueOut:= m_NodeValueOut);
END_IF

### 10.5.4 DL_ReadNodeValue

Brief description
The DL_ReadNodeValue function block calls the "read service" of the Data
Layer to read any values from the Data Layer.

Interface description

Table 63: Interface variables of the DL_ReadNodeValue function block
              Name                Type                    Description                   Applied from
Input         Execute             BOOL                    Rising edge starts the        IL_ExecuteDoneBase
                                                          processing
Output        Done                BOOL                    Processing completed          IL_ExecuteDoneBase
              Active              BOOL                    In process                    IL_ExecuteDoneBase

Name             Type                Description                Applied from
Error            BOOL                An error occurred          IL_ExecuteDoneBase
ErrorID          ⮫ ERROR_CODE        Error classification       IL_ExecuteDoneBase
ErrorIdent       ⮫ ERROR_STRUCT      Detailed error cause       IL_ExecuteDoneBase
Input       ClientId         ⮫ IL_HANDLE         ID of the Data Layer
                           client
NodeName         REFERENCE TO        Name of the node in the
       STRING(255)         Data Layer
NodeValue        REFERENCE TO        NodeValue returned by
       DL_NodeValue        the node

Programming example of DL_ReadNodeValue
Reading an integer value from a Global Variable List “GvlBaseTypes”.
This is only an example to describe the access using the Data Layer. (Varia‐
bles in the IEC program can also be accessed directly).

Declaration:

VAR
             Result: CXA_Datalayer.DL_RESULT;
  m_fbReadNodeValue: CXA_Datalayer.DL_ReadNodeValue;
m_Execute : BOOL;
m_NodeValue : DL_NodeValue;
m_address : STRING;
value : INT;
END_VAR

Implementation:

m_address := 'plc/app/Application/sym/GvlBaseTypes/iecInt';
m_Execute := TRUE;
m_fbReadNodeValue(Execute:= m_Execute, NodeName:= m_address, NodeValue:= m_NodeValue);

IF m_fbReadNodeValue.Done = TRUE THEN
       Result := m_NodeValue.GetValueInt16(Value=>value);
END_IF
// Zugriff beenden
IF (m_fbReadNodeValue.Done = TRUE) OR (m_fbReadNodeValue.Error = TRUE) THEN
  m_Execute := FALSE;
  m_fbReadNodeValue(Execute:= m_Execute, NodeName:= m_address, NodeValue:= m_NodeValue);
END_IF

### 10.5.5 DL_ReadNodeValueType02

Brief description
Use the function block DL_ReadNodeValueType02 like the function block
⮫ DL_ReadNodeValue to read any values from the Data Layer.
When reading certain flat buffers, a NodeValueOut can also be transferred to
read out specific sections for example.

Interface description

Table 64: Interface variables of the DL_ReadNodeValueType02 function block
              Name              Type                    Description                    Applied from
Input         Execute           BOOL                    Rising edge starts the         IL_ExecuteDoneBase
                                                        processing
Output        Done              BOOL                    Processing completed           IL_ExecuteDoneBase
              Active            BOOL                    In process                     IL_ExecuteDoneBase
              Error             BOOL                    An error occurred              IL_ExecuteDoneBase
              ErrorID           ⮫ ERROR_CODE            Error classification           IL_ExecuteDoneBase
              ErrorIdent        ⮫ ERROR_STRUCT          Detailed error cause           IL_ExecuteDoneBase
Input         ClientId          ⮫ IL_HANDLE             ID of the Data Layer
                                                        client
              NodeName          REFERENCE TO            Name of the node in the
                                STRING(255)             Data Layer
              NodeValueIn       REFERENCE TO            NodeValue be written to
                                DL_NodeValue            the node

Name         Type                        Description                    Applied from
NodeValueOut REFERENCE TO                NodeValue returned by
    DL_NodeValue                the node

### 10.5.6 DL_WriteNodeValue

Brief description
The DL_WriteNodeValue function block calls the "write service" of the Data
Layer to write any values into the Data Layer.

Interface description

Table 65: Interface variables of the DL_WriteNodeValue function block
          Name               Type                    Description                    Applied from
Input     Execute            BOOL                    Rising edge starts the         IL_ExecuteDoneBase
                                                     processing
Output    Done               BOOL                    Processing completed           IL_ExecuteDoneBase
          Active             BOOL                    In process                     IL_ExecuteDoneBase
          Error              BOOL                    An error occurred              IL_ExecuteDoneBase
          ErrorID            ⮫ ERROR_CODE            Error classification           IL_ExecuteDoneBase
          ErrorIdent         ⮫ ERROR_STRUCT          Detailed error cause           IL_ExecuteDoneBase
Input     ClientId           ⮫ IL_HANDLE             ID of the Data Layer
                                                     client
          NodeName           REFERENCE TO            Name of the node in the
                             STRING(255)             Data Layer
          NodeValueIn        REFERENCE TO            NodeValue to be written
                             DL_NodeValue            to the node
          NodeValueOut       REFERENCE TO            NodeValue returned by
                             DL_NodeValue            the node

Declaration:

VAR
     Result: CXA_Datalayer.DL_RESULT;
     m_fbWriteNodeValue : CXA_Datalayer.DL_WriteNodeValue;
     m_Execute : BOOL;
    m_NodeValueIn : DL_NodeValue;
    m_NodeValueOut : DL_NodeValue;
    m_address : STRING;
    value : INT;
END_VAR

Implementation:

m_address := 'plc/app/Application/sym/GvlBaseTypes/iecInt';
m_Execute := TRUE;
value :=42;
Result := m_NodeValueIn.SetValueInt16(value);

m_fbWriteNodeValue(Execute:= m_Execute, NodeName:= m_address, NodeValueIn:= m_NodeValueIn,

NodeValueOut:= m_NodeValueOut);
// Zugriff beenden
IF (m_fbWriteNodeValue.Done = TRUE) OR (m_fbWriteNodeValue.Error = TRUE) THEN
    m_Execute := FALSE;
    m_fbWriteNodeValue(Execute:= m_Execute, NodeName:= m_address, NodeValueIn:=
m_NodeValueIn, NodeValueOut:= m_NodeValueOut);
END_IF

### 10.5.7 DL_MetaDataNodeValue

Brief description
The DL_MetaDataNodeValue function block can be used to read the metadata
of a NodeValue which is queried via the "metadata service" of the Data Layer.
This metadata contains information on the NodeValue characteristics, e.g.
access options (read, write, browse), descriptions (comments) and type (vari‐
able, methods, etc.).
To evaluate this metadata, include the CXA_AutomationCore_fbs library into
the project.
To read out certain metadata from the PLC symbols, it is possible that addi‐
tional settings have to be made in the symbol configuration.

Interface description

Table 66: Interface variables of the DL_MetaDataNodeValue function block
              Name              Type                    Description                    Applied from
Input         Execute           BOOL                    Rising edge starts the         IL_ExecuteDoneBase
                                                        processing
Output        Done              BOOL                    Processing completed           IL_ExecuteDoneBase
              Active            BOOL                    In process                     IL_ExecuteDoneBase
              Error             BOOL                    An error occurred              IL_ExecuteDoneBase
              ErrorID           ⮫ ERROR_CODE            Error classification           IL_ExecuteDoneBase
              ErrorIdent        ⮫ ERROR_STRUCT          Detailed error cause           IL_ExecuteDoneBase
Input         ClientId          ⮫ IL_HANDLE             ID of the Data Layer
                                                        client
              NodeName     REFERENCE TO                 Name of the node in the
                           STRING(255)                  Data Layer
              NodeValueIn REFERENCE TO                  NodeValue be written to
                           DL_NodeValue                 the node
              NodeValueOut REFERENCE TO                 NodeValue returned by
                           DL_NodeValue                 the node

Test program for the DL_MetaDataNodeValue

Declaration:

VAR
  m_fbReadMetaData: DL_MetaDataNodeValue;
  m_ExecuteMetaData : BOOL;

  m_MetaDataNodeValue : CXA_Datalayer.DL_NodeValue;
  m_Type : CXA_Datalayer.DL_DATA_TYPE;
  DescriptionString: STRING;

  MetaDataRead : CXA_Automationcore_fbs.comm_datalayer_Metadata;
    m_NodeClass : CXA_Automationcore_fbs.comm_datalayer_NodeClass;

END_VAR

Implementation:

m_fbReadMetaData( Execute:=m_ExecuteMetaData , NodeName:= 'plc/app/Application/sym/
PLC_PRG/test', NodeValueIn:= , NodeValueOut:=m_MetaDataNodeValue );
IF (m_fbReadMetaData.Done = TRUE) THEN
  m_Type := m_MetaDataNodeValue.GetType();

  MetaDataRead.getRootAsMetadata (data := m_MetaDataNodeValue.GetData(), size :=
m_MetaDataNodeValue.GetSize() );
  DescriptionString := MetaDataRead.getDescription();
  m_NodeClass := MetaDataRead.getNodeClass();
END_IF

IF (m_fbReadMetaData.Done = TRUE) OR (m_fbReadMetaData.Error = TRUE) THEN
  m_ExecuteMetaData := FALSE;
  m_fbReadMetaData(Execute:= m_ExecuteMetaData, NodeName:= 'plc/app/Application/sym/
PLC_PRG/test', NodeValueIn:= , NodeValueOut:=m_MetaDataNodeValue);
END_IF

## 10.6 "Bulk" function blocks

### 10.6.1 Introduction and overview

The CXA_Datalayer library contains function blocks and structures that allow
to access to the bulk mechanism of the Data Layer.
The following function blocks are available:
● DL_BulkBrowseNodeValues
● DL_BulkCreateNodeValues
● DL_BulkDeleteNodeValues
● DL_BulkMetaDataNodeValues
● DL_BulkReadNodeValues
● DL_BulkWriteNodeValues
To use the function blocks, it is important to understand and use the fol‐
lowing structures:
● DL_BulkRequest
● DL_BulkResponse

Further information
● For more information on using the Nodevalue object, refer to the documen‐
  tation on the CXA_DataLayer library.

### 10.6.2 DL_BulkBrowseNodeValues

Brief description
The function block DL_BulkBrowseNodeValues calls the "browse service" in all
specified nodes.
The following parameters can be transferred via the "browse service":
● BulkRequests: Pointer to an array of the type DL_BulkRequests
  Define the node name you intend to browse through in each array element.
● Count: Number of nodes to be read
  This is usually the size of your array of bulk requests.
● BulkResponses: Pointer to an array of the type DL_BulkResponse
  All results of your requests are stored here.

Interface description

Table 67: Interface variables of the DL_BulkBrowseNodeValues function block
            Name             Type                            Description                          Applied from

Input       Execute          BOOL                            Rising edge starts the processing    IL_ExecuteDoneBase

Output      Done             BOOL                            Processing completed                 IL_ExecuteDoneBase

Active           BOOL                            In process                           IL_ExecuteDoneBase

Error            BOOL                            An error occurred                    IL_ExecuteDoneBase

ErrorID          ⮫ ERROR_CODE                    Error classification                 IL_ExecuteDoneBase

ErrorIdent       ⮫ ERROR_STRUCT                  Detailed error cause                 IL_ExecuteDoneBase

Input       ClientId         ⮫ IL_HANDLE                     ID of the Data Layer client

BulkRequests     POINTER TO DL_BulkRequest       Name of the requested nodes in the
                                    Data Layer

Count            INT                             Number of nodes to be read

BulkResponses    POINTER TO DL_BulkResponse      Name of the requested nodes in the
                                    Data Layer

Example of DL_BulkBrowseNodeValues

Declaration:
PROGRAM Example_BulkBrowseNodeValues
VAR
m_fbBulkBrowseNode : DL_BulkBrowseNodeValues;
m_Execute : BOOL;
nodeValueOutType : DL_DATA_TYPE;   // the value type of the received node value

bulkRequests : ARRAY[0..1] OF DL_BulkRequest;            // Names of the requested nodes in data layer
bulkResponses : ARRAY[0..1] OF DL_BulkResponse;          // Values of the requested nodes in data layer

addressStringForRequest : STRING := 'diagnosis/'; // this is the first address we want to request
addressStringForRequest2 : STRING := 'plc/app/App/sym/GVL/xAutomaticClear';   // this is a not existing address
addressStringForResponse : STRING(255);            // this is the string where the first bulk response node will
be written

nodeCount : INT := 2;    // number of nodes that will be requested
i : INT := 0;            // iterator to validate the result

// this part of declaration is necessary to parse all strings out of the browsed array to an array of string
pointerToBrowseOutput : POINTER TO POINTER TO STRING;      // the outcoming browse values will be stored in this
array
tmpPointerToBrowseOutput : POINTER TO POINTER TO STRING;   // this temporary pointer is used to get every single
element
pointerToBrowseString : POINTER TO STRING;                 // this pointer will contain the address to the string
element
browsedStringsCount : UDINT;
arrayIndex : UDINT;

browseOutputStrings : ARRAY [0..16] OF STRING;    // this array will contain all browsed information

END_VAR

Implementation:
// at first set the nodename of the first bulk request elements in the array
bulkRequests[0].NodeName := ADR(addressStringForRequest);
bulkRequests[1].NodeName := ADR(addressStringForRequest2);

// OPTIONAL: set the nodename in the response, where the response nodename from the datalayer will be written too.
// If nothing is set, the nodename won't be filled in the response. However the DL_RESULT will still be set,
giving the information of success.
// Note: if length is not set (0), the node name won't be written!
bulkResponses[0].NodeName := ADR(addressStringForResponse);
bulkResponses[0].NodeLength := 255;

// now execute the bulk read request
m_fbBulkBrowseNode(Execute:= m_Execute, BulkRequests:= ADR(bulkRequests), BulkResponses:= ADR(bulkResponses),
Count := nodeCount);
IF (m_fbBulkBrowseNode.Done = TRUE) OR (m_fbBulkBrowseNode.Error = TRUE) THEN

  // if the request was successful, the value type for the browse request will return an array of string
  FOR i := 0 TO nodeCount-1 BY 1 DO
    IF (bulkResponses[i].DlResult = DL_RESULT.DL_OK) THEN
nodeValueOutType := bulkResponses[i].NodeValue.GetType();

// the outcoming array will be only parsed once, since the second requested nodename is an invalid address

// at first get the count of elements and the pointer to the elements out of the node value
bulkResponses[i].NodeValue.GetValueArrayOfString(ArrayPtr => pointerToBrowseOutput, Count =>
browsedStringsCount);
// now iterate through any single array element and copy them to a array of string
FOR ArrayIndex := 0 TO browsedStringsCount - 1 DO
tmpPointerToBrowseOutput := (pointerToBrowseOutput + (ArrayIndex * SIZEOF(POINTER TO STRING)));
pointerToBrowseString := tmpPointerToBrowseOutput^;
StrCpyA(pBuffer:= ADR(browseOutputStrings[ArrayIndex]), iBufferSize:=
SIZEOF(browseOutputStrings[ArrayIndex]), pStr:= pointerToBrowseString);
END_FOR;
    END_IF
  END_FOR
    m_Execute := FALSE;
END_IF

### 10.6.3 DL_BulkCreateNodeValues

Brief description
The DL_BulkCreateNodeValues function block calls the "create service" in all
specified nodes.
The following parameters can be transferred via the "create service":
● BulkRequests: Pointer to an array of the type DL_BulkRequests
  Define the node name you intend to create through in each array element.
● Count: Number of nodes to be read
  This is usually the size of your array of bulk requests.
● BulkResponses: Pointer to an array of the type DL_BulkResponse
  All results of your requests are stored here.

Interface description

Table 68: Interface variables of the DL_BulkCreateNodeValues function block
              Name               Type                   Description                         Applied from

Input         Execute            BOOL                   Rising edge starts the processing   IL_ExecuteDoneBase

Output        Done               BOOL                   Processing completed                IL_ExecuteDoneBase

Active             BOOL                   In process                          IL_ExecuteDoneBase

Error              BOOL                   An error occurred                   IL_ExecuteDoneBase

ErrorID            ⮫ ERROR_CODE           Error classification                IL_ExecuteDoneBase

ErrorIdent         ⮫ ERROR_STRUCT         Detailed error cause                IL_ExecuteDoneBase

Name                 Type                       Description                          Applied from

Input       ClientId             ⮫ IL_HANDLE                ID of the Data Layer client

BulkRequests         POINTER TO DL_BulkRequest Name of the requested nodes in the
                                 Data Layer

Count                INT                        Number of nodes to be read

BulkResponses        POINTER TO DL_BulkRes‐     Name of the requested nodes in the
      ponse                      Data Layer

Since the standard PLC node does not contain any node that provides a
"Create" service, no example is provided for this function block.

### 10.6.4 DL_BulkDeleteNodeValues

Brief description
The DL_BulkDeleteNodeValues function block calls the "delete service" in all
specified nodes.
The following parameters can be transferred via the "delete service":
● BulkRequests: Pointer to an array of the type DL_BulkRequests
  Define the node name you intend to delete through in each array element.
● Count: Number of nodes to be read
  This is usually the size of your array of bulk requests.
● BulkResponses: Pointer to an array of the type DL_BulkResponse
  All results of your requests are stored here.

Interface description

Table 69: Interface variables of the DL_BulkDeleteNodeValues function block
           Name                Type                         Description                          Applied from

Input      Execute             BOOL                         Rising edge starts the processing    IL_ExecuteDoneBase

Output     Done                BOOL                         Processing completed                 IL_ExecuteDoneBase

Active              BOOL                         In process                           IL_ExecuteDoneBase

Error               BOOL                         An error occurred                    IL_ExecuteDoneBase

ErrorID             ⮫ ERROR_CODE                 Error classification                 IL_ExecuteDoneBase

ErrorIdent          ⮫ ERROR_STRUCT               Detailed error cause                 IL_ExecuteDoneBase

Input      ClientId            ⮫ IL_HANDLE                  ID of the Data Layer client

BulkRequests        POINTER TO DL_BulkRequest    Name of the requested nodes in the
                                 Data Layer

Count               INT                          Number of nodes to be read

BulkResponses       POINTER TO DL_BulkResponse   Name of the requested nodes in the
                                 Data Layer

Since the standard PLC node does not contain a node that can be deleted, no
example is provided for this function block.

### 10.6.5 DL_BulkMetaDataNodeValues

             Brief description
             The function block DL_BulkMetaDataNodeValues calls the metadata for all
             specified nodes by calling "metadata service" for all nodes.
             The following parameters can be transferred via the "read service":
             ● BulkRequests: Pointer to an array of the type DL_BulkRequests
               Define the node name you intend to read in each array element.
             ● Count: Number of nodes to be read
               This is usually the size of your array of bulk requests.
             ● BulkResponses: Pointer to an array of the type DL_BulkResponse
               All results of your requests are stored here.

             Interface description

Table 70: Interface variables of the DL_BulkMetaDataNodeValues function block
               Name                Type                        Description                          Applied from

Input          Execute             BOOL                        Rising edge starts the processing    IL_ExecuteDoneBase

Output         Done                BOOL                        Processing completed                 IL_ExecuteDoneBase

Active              BOOL                        In process                           IL_ExecuteDoneBase

Error               BOOL                        An error occurred                    IL_ExecuteDoneBase

ErrorID             ⮫ ERROR_CODE                Error classification                 IL_ExecuteDoneBase

ErrorIdent          ⮫ ERROR_STRUCT              Detailed error cause                 IL_ExecuteDoneBase

Input          ClientId            ⮫ IL_HANDLE                 ID of the Data Layer client

BulkRequests        POINTER TO DL_BulkRequest   Name of the requested nodes in the
                                                Data Layer

Count               INT                         Number of nodes to be read

BulkResponses       POINTER TO DL_BulkRes‐      Name of the requested nodes in the
                    ponse                       Data Layer

             Example of DL_BulkMetaDataNodeValues

Declaration:
PROGRAM Example_BulkMetaDataNodeValues
VAR
m_fbBulkMetaDataNode : DL_BulkMetaDataNodeValues;
m_Execute : BOOL;

nodeValueOutType : DL_DATA_TYPE;          // the value type of the received node value from the first request

bulkRequests : ARRAY[0..1] OF DL_BulkRequest;             // Names of the requested nodes in data layer
bulkResponses : ARRAY[0..1] OF DL_BulkResponse;          // Values of the requested nodes in data layer

addressStringForRequest : STRING := 'diagnosis/';   // this is the first address we want to request
addressStringForRequest2 : STRING := 'plc/app/App/sym/GVL/xAutomaticClear';   // this is a not existing address
addressStringForResponse : STRING(255);    // this is the string where the first bulk response node will be
written

nodeCount : INT := 2;       // number of nodes that will be requested
i : INT := 0;               // iterator to validate the result

// now get the metadata out of the node value

(* To use this example you need to add the CXA_PLC_fbs and uncomment the following lines *)
//MetadataRead : plc_cmp_datalayer_fbs_AppInfo;
//DescriptionString: STRING;

END_VAR

Implementation:
// at first set the nodename of the first bulk request elements in the array
bulkRequests[0].NodeName := ADR(addressStringForRequest);
bulkRequests[1].NodeName := ADR(addressStringForRequest2);

// OPTIONAL: set the nodename in the response, where the response nodename from the datalayer will be written too.
// If nothing is set, the nodename won't be filled in the response. However the DL_RESULT will still be set,
giving the information of success.
// Note: if length is not set (0), the node name won't be written!
bulkResponses[0].NodeName := ADR(addressStringForResponse);
bulkResponses[0].NodeLength := 255;

// now execute the bulk read request
m_fbBulkMetaDataNode(Execute:= m_Execute, BulkRequests:= ADR(bulkRequests), BulkResponses:= ADR(bulkResponses),
Count := nodeCount);
IF (m_fbBulkMetaDataNode.Done = TRUE) OR (m_fbBulkMetaDataNode.Error = TRUE) THEN

  // if the request was successful, the value type for the browse request will return an array of string
  FOR i := 0 TO nodeCount-1 BY 1 DO
    IF (bulkResponses[i].DlResult = DL_RESULT.DL_OK) THEN
nodeValueOutType := bulkResponses[i].NodeValue.GetType();

(* To use this example you need to add the CXA_PLC_fbs and uncomment the following lines *)
//MetadataRead.getRootAsAppInfo(data := bulkResponses[i].NodeValue^.GetData(), size :=
bulkResponses[i].NodeValue^.GetSize());
//DescriptionString := MetaDataRead.getDescription();
    END_IF
  END_FOR
    m_Execute := FALSE;
END_IF

### 10.6.6 DL_BulkReadNodeValues

Brief description
The function block DL_BulkReadNodeValues calls the "read service" in all
specified nodes.
The following parameters can be transferred via the "read service":
● BulkRequests: Pointer to an array of the type DL_BulkRequests
  Define the node name you intend to read in each array element.
● Count: Number of nodes to be read
  This is usually the size of your array of bulk requests.
● BulkResponses: Pointer to an array of the type DL_BulkResponse
  All results of your requests are stored here.

Interface description

Table 71: Interface variables of the DL_BulkReadNodeValues function block
            Name             Type                       Description                         Applied from

Input       Execute          BOOL                       Rising edge starts the processing   IL_ExecuteDoneBase

Name                 Type                        Description                          Applied from

Output        Done                 BOOL                        Processing completed                 IL_ExecuteDoneBase

Active               BOOL                        In process                           IL_ExecuteDoneBase

Error                BOOL                        An error occurred                    IL_ExecuteDoneBase

ErrorID              ⮫ ERROR_CODE                Error classification                 IL_ExecuteDoneBase

ErrorIdent           ⮫ ERROR_STRUCT              Detailed error cause                 IL_ExecuteDoneBase

Input         ClientId             ⮫ IL_HANDLE                 ID of the Data Layer client

BulkRequests         POINTER TO DL_BulkRequest   Name of the requested nodes in the
                                  Data Layer

Count                INT                         Number of nodes to be read

BulkResponses        POINTER TO DL_BulkResponse Name of the requested nodes in the
                                  Data Layer

Example of DL_BulkReadNodeValues

Declaration:
PROGRAM Example_BulkReadNodeValues
VAR
m_fbBulkReadNode : DL_BulkReadNodeValues;
m_Execute : BOOL;

nodeValueOutType : DL_DATA_TYPE;          // the value type of the received node value from the first request

bulkRequests : ARRAY[0..1] OF DL_BulkRequest;             // Names of the requested nodes in data layer
bulkResponses : ARRAY[0..1] OF DL_BulkResponse;          // Values of the requested nodes in data layer

addressStringForRequest : STRING := 'diagnosis/';   // this is the first address we want to request
addressStringForRequest2 : STRING := 'plc/app/App/sym/GVL/xAutomaticClear';   // this is a not existing address
addressStringForResponse : STRING(255);    // this is the string where the first bulk response node will be
written

nodeCount : INT := 2;        // number of nodes that will be requested
i : INT := 0;                // iterator to validate the result

END_VAR

Implementation:
// at first set the nodename of the first bulk request elements in the array
bulkRequests[0].NodeName := ADR(addressStringForRequest);
bulkRequests[1].NodeName := ADR(addressStringForRequest2);

// OPTIONAL: set the nodename in the response, where the response nodename from the datalayer will be written too.
// If nothing is set, the nodename won't be filled in the response. However the DL_RESULT will still be set,
giving the information of success.
// Note: if length is not set (0), the node name won't be written!
bulkResponses[0].NodeName := ADR(addressStringForResponse);
bulkResponses[0].NodeLength := 255;

// now execute the bulk read request
m_fbBulkReadNode(Execute:= m_Execute, BulkRequests:= ADR(bulkRequests), BulkResponses:= ADR(bulkResponses),
Count := nodeCount);
IF (m_fbBulkReadNode.Done = TRUE) OR (m_fbBulkReadNode.Error = TRUE) THEN
  // if the request was successful, the value type for the browse request will return an OK. The Type for the
nodeName1 is flatbuffers
  FOR i := 0 TO nodeCount-1 BY 1 DO
    IF (bulkResponses[i].DlResult = DL_RESULT.DL_OK) THEN
nodeValueOutType := bulkResponses[0].NodeValue.GetType();
    END_IF
  END_FOR
    m_Execute := FALSE;
END_IF

### 10.6.7 DL_BulkWriteNodeValues

Brief description
The DL_BulkWriteNodeValues function block calls the "write service" in all
specified nodes.

The following parameters can be transferred via the "write service":
● BulkRequests: Pointer to an array of the type DL_BulkRequests
  Define the node name you intend to write through in each array element.
  You also need to set the DL_NodeValue object of each array element with
  the information you intend to write to the node.
● Count: Number of nodes to be read
  This is usually the size of your array of bulk requests.
● BulkResponses: Pointer to an array of the type DL_BulkResponse
  All results of your requests are stored here.

Interface description

Table 72: Interface variables of the DL_BulkWriteNodeValues function block
           Name                Type                         Description                          Applied from

Input      Execute             BOOL                         Rising edge starts the processing    IL_ExecuteDoneBase

Output     Done                BOOL                         Processing completed                 IL_ExecuteDoneBase

Active              BOOL                         In process                           IL_ExecuteDoneBase

Error               BOOL                         An error occurred                    IL_ExecuteDoneBase

ErrorID             ⮫ ERROR_CODE                 Error classification                 IL_ExecuteDoneBase

ErrorIdent          ⮫ ERROR_STRUCT               Detailed error cause                 IL_ExecuteDoneBase

Input      ClientId            ⮫ IL_HANDLE                  ID of the Data Layer client

BulkRequests        POINTER TO DL_BulkRequest    Name of the requested nodes in the
                                 Data Layer

Count               INT                          Number of nodes to be read

BulkResponses       POINTER TO DL_BulkResponse   Name of the requested nodes in the
                                 Data Layer

Example of DL_BulkWriteNodeValues

Declaration:
PROGRAM Example_BulkWriteNodeValues
VAR
m_fbBulkWriteNode : DL_BulkWriteNodeValues;
m_Execute : BOOL;

bulkRequests : ARRAY[0..1] OF DL_BulkRequest;         // Names of the requested nodes in data layer
bulkResponses : ARRAY[0..1] OF DL_BulkResponse;      // Values of the requested nodes in data layer

addressStringForRequest : STRING := 'diagnosis/';   // this is the first address we want to request
addressStringForRequest2 : STRING := 'plc/app/App/sym/GVL/xAutomaticClear';   // this is a not existing address
addressStringForResponse : STRING(255);    // this is the string where the first bulk response node will be
written

nodeCount : INT := 2;     // number of nodes that will be requested

nodeValueToBeWritten : BOOL := FALSE;

i : INT := 0;          // iterator to validate the result
resultNodeName1 : DL_RESULT;    // node 1 should exist and is writable, so it return OK

resultNodeName2 : DL_RESULT;   // this node does not exist and returns INVALID_ADDRESS

END_VAR

Implementation:
// at first set the nodename of the first bulk request elements in the array
bulkRequests[0].NodeName := ADR(addressStringForRequest);
bulkRequests[1].NodeName := ADR(addressStringForRequest2);

// to write any value, it is necessary to set the value in the nodevalue object of your array element
bulkRequests[0].NodeValue.SetValueBool8(nodeValueToBeWritten);

// OPTIONAL: set the nodename in the response, where the response nodename from the datalayer will be written too.
// If nothing is set, the nodename won't be filled in the response. However the DL_RESULT will still be set,
giving the information of success.
// Note: if length is not set (0), the node name won't be written!

bulkResponses[0].NodeName := ADR(addressStringForResponse);
bulkResponses[0].NodeLength := 255;

// now execute the bulk read request
m_fbBulkWriteNode(Execute:= m_Execute, BulkRequests:= ADR(bulkRequests), BulkResponses:= ADR(bulkResponses),
Count := nodeCount);
IF (m_fbBulkWriteNode.Done = TRUE) OR (m_fbBulkWriteNode.Error = TRUE) THEN
  // if the request was successful, the value type for the browse request will return an OK.
  resultNodeName1 := bulkResponses[0].DlResult;
  resultNodeName1 := bulkResponses[1].DlResult;
    m_Execute := FALSE;
END_IF

### 10.6.8 DL_BulkRequest

The structure DL_BulkRequest describes a single request for different Data
Layer services.
The structure should be part of an array of multiple requests used to create a
bulk request.

Implementation:
TYPE DL_BulkRequest :
STRUCT
  NodeName : POINTER TO STRING;   // address name to be read
  NodeValue : DL_NodeValue;         // nodevalue containing more information
          // Note: use of this information depends on the data provider
END_STRUCT
END_TYPE

### 10.6.9 DL_BulkResponse

The DL_BulkResponse structure describes a single response from any Data
Layer service.
After the structure has been used by a Data Layer request method, it usually
contains information on the result and the timestamp. To obtain a valid node
name, assign the structure before using the Data Layer method.
Different values are assigned to the node value. These assigned values depend
on the data provider and/or requested Data Layer method.

Implementation:
TYPE DL_BulkResponse :
STRUCT
  NodeName : POINTER TO STRING;   // address name to be read
  NodeLength : INT;                 // length of the expected node name
  NodeValue : DL_NodeValue;         // nodevalue containing more information
          // Note: use of this information depends on the data provider
  DlResult : DL_RESULT;             // result whether the request was successful
  Timestamp : ULINT;                // time of the response creation
END_STRUCT
END_TYPE

### 10.6.10 DL_ConvertDLTimestamp

The DL_BulkResponse structure contains a timestamp. This timestamp is
stored in the only format supported by the Data Layer s 64-bit file time.
For a comfortable and easy access, the DL_ConvertDLTimestamp function is
available. It converts the Data Layer timestamp into the appropriate, expected
IEC format (32-bit UTC).

The documentation of the CXA_Datalayer library contains more details on the
conversion of timestamps:

### 10.6.11 Creating a bulk request

Creating bulk requests is the same for every newly implemented function. It is
required to create an array of requests and another array of responses. Fill the
queries with the node names and (depending on the data provider and the
intended method) with the node values.
It is not required to initialize a value for the response, as this value is
optional.
Finally, the number of requests is required for each function block.
In the following example, a request is created and started for the function
block DL_BulkReadNodeValues.

Declaration:
m_fbBulkReadNode : DL_BulkReadNodeValues;        // Instance of the function block
m_Execute : BOOL;
bulkRequests : ARRAY[0..1] OF DL_BulkRequest;   // Names of the requested nodes (and values, depending on the
used method)

bulkResponses : ARRAY[0..1] OF DL_BulkResponse; // Values of the requested nodes

nodeCount : INT := 2;                     // number of nodes that will be requested

addressStringForRequest : STRING := ‘1stNodeNameHere’; // node name to be requested
addressStringForRequest2 : STRING := 2ndNodeNameHere’; // node name to be requested
addressStringForResponse : STRING(255);    // string, where the first bulk response node will be written

Implementation:
// at first set the nodename of the first bulk request elements in the array
bulkRequests[0].NodeName := ADR(addressStringForRequest);
bulkRequests[1].NodeName := ADR(addressStringForRequest2);

// OPTIONAL: set the nodename in the response, where the response nodename from the datalayer will be written too.
// If nothing is set, the nodename won't be filled in the response. However, the DL_RESULT will still be set,
giving the information of success.
// Note: if length is not set (0), the node name won't be written!

bulkResponses[0].NodeName := ADR(addressStringForResponse);
bulkResponses[0].NodeLength := 255;

// now execute the bulk read request
m_fbBulkReadNode(Execute:= m_Execute, BulkRequests:= ADR(bulkRequests), BulkResponses:= ADR(bulkResponses),
Count := nodeCount);

As a result, the array of responses is filled with the corresponding values. The
numbering of these values matches the queries. Now, evaluate the responses
according to the use case.

## 10.7 "Subscription" function blocks

### 10.7.1 Introduction and overview

The previously described function blocks are used for one-time queries of
Data Layer nodes. To work with the current values, retrieve them again and
again.
Subscriptions are a different approach: It is subscribed to a node and as long
as this subscription remains active, the values are always refreshed.
Events can now also additionally be triggered. As these events can only be
read out via subscriptions, this option is listed thematically in this chapter.

### 10.7.2 DL_CreateSubscription

Brief description
This function block calls the Data Layer service to create a subscription. Basic
settings can be made. They apply to all nodes registered under this subscrip‐
tion. If this function block is reset (Execute = TRUE -> FALSE), the subscrip‐
tion is also deregistered from the Data Layer and does no longer exists.
(Note: If no node is registered with the subscription within 30 seconds, it
expires and is deleted)
(Note: If the value specified for "SamplingInterval" is too small, the smallest
possible value is applied to Data Layer without returning an error. To check
the possible value ranges, please refer to the documentation of the Data Layer
for subscriptions)

Interface description

Table 73: Interface variables of the DL_CreateSubscription function block
                Name             Type                   Description                      Applied from
Input           Execute          BOOL                   Rising edge starts processing    IL_ExecuteDoneBase
Output          Done             BOOL                   Processing completed             IL_ExecuteDoneBase
                Active           BOOL                   In process                       IL_ExecuteDoneBase
                Error            BOOL                   An error occurred                IL_ExecuteDoneBase
                ErrorID          ⮫ ERROR_CODE           Error classification             IL_ExecuteDoneBase
                ErrorIdent       ⮫ ERROR_STRUCT         Detailed error cause             IL_ExecuteDoneBase
Input           SubscriptionName POINTER TO STRING      Name to identify the subscrip‐
                                                        tion just created

Name               Type                 Description                         Applied from
DeadBandValue      REAL                 If the difference between the
                              last value read and the current
                              value is greater than this param‐
                              eter, the value is updated
SamplingInterval   REFERENCE TO         Minimum time interval to query
         DL_NodeValue         a value

### 10.7.3 DL_CreateEventSubscription

Brief description
In addition to the DL_CreateSubscription function block, there is another
function block that allows to subscribe to an event. Further node registration
is performed analogously. The structure of the function block corresponds 1:1
to that of ⮫ DL_CreateSubscription. However, a different secondary setting is
made.

### 10.7.4 DL_Subscribe

Brief description
This function block opens the Data Layer service to register one or more
nodes for a subscription. When the function block is active, the nodes also
remain registered. If the function block is disabled (Enable = FALSE), all
nodes are also deregistered.

Interface description

Table 74: Interface variables of the DL_Subscribe function block
              Name               Type                 Description                         Applied from
Input         Enable             BOOL                 The signal to start the process IL_EnableDoneBase
                                                      that registers the nodes with
                                                      the subscription. A falling edge
                                                      deletes the nodes from the sub‐
                                                      scription.
Output        Done               BOOL                 Processing completed                IL_EnableDoneBase
              Active             BOOL                 In process                          IL_EnableDoneBase
              Error              BOOL                 An error occurred                   IL_EnableDoneBase
              ErrorID            ⮫ ERROR_CODE         Error classification                IL_EnableDoneBase
              ErrorIdent         ⮫ ERROR_STRUCT       Detailed error cause                IL_EnableDoneBase
Input         NodeNames          POINTER TO POINTER   Nodes to be registered
                                 TO STRING
              NodeValues         POINTER TO POINTER   The values are stored in these
                                 TO DL_NodeValue      DL_NodeValues in the order of
                                                      the registered nodes
              SubscriptionName POINTER TO STRING      Name of the subscription to
                                                      which the nodes are to be regis‐
                                                      tered

            Additional functions
            The DL_Subscribe function block also contains a GetValueStateByNodeName
            method. This method returns the value TRUE if the value of a registered node
            changed. If this method is called, the flag for the changed value is reset
            internally.

Table 75: Interface variables of the GetValueStateByNodeName method
               Name               Type                      Description                           Applied from
Input          NodeName           POINTER TO STRING         Node whose value change is to be
                                                            queried
               NodeValue          POINTER TO DL_NodeValue   Pointer to the value of the node
                                                            used for DL_Subscribe
Output         ValueChanged       BOOL                      Return value that the value of the
                                                            node changed

            A GetErrorStateByNodeName method is included for further error analysis. An
            error code DL_RESULT is returned together with the transferred node.

Table 76: Interface variables of the GetErrorStateByNodeName method
               Name               Type                      Description                           Applied from
Input          NodeName           POINTER TO STRING         Node whose value change is to be
                                                            queried
               NodeValue          POINTER TO DL_NodeValue   Pointer to the value of the node
                                                            used for DL_Subscribe
Output         errCode            DL_RESULT                 Error code that occurred during the
                                                            event with the node

### 10.7.5 BaseEventType

            Brief description
            This simple function block allows to trigger an event. To do this, derive the
            function block and call the secondary mFire() method. As secondary function,
            all variables in the "VAR_INPUT" area of the declaration are combined to one
            FlatBuffer object and output directly as event via the Data Layer "PublishE‐
            vent" service.

Interface description

Table 77: Interface variables of the BaseEventType function block
              Name                 Type                   Description                         Applied from
Input         SourceName           POINTER TO STRING      This variable should contain
                                                          the name of the event and is
                                                          optional. If an empty string is
                                                          transferred, the instance path of
                                                          the function block is used and
                                                          displayed.

Known restrictions
If a function block was derived, it is identified as event. This can be repeated
any number of times. If the derived function block is derived again, this subse‐
quently created function block is no longer identified as event.

### 10.7.6 Example of a subscription

Declaration

PROGRAM Example_Subscription_WithParameters
VAR
  // Create Subscription
  CreateSubscriptionWithParams : DL_CreateSubscription;
  Subscribe : DL_Subscribe;
  executeCreate : BOOL := TRUE;
  subscriptionName : STRING := 'Sub1';

  // Subscription Nodes
  Counter1 : INT;
  Counter2 : INT;
  SubscribedCounter1Value : INT;
  SubscribedCounter2Value : INT;

  // Subscribe
  enableSub : BOOL := TRUE;
  nodeAddressPointer : ARRAY [0..1] OF POINTER TO STRING;

  MyCounterValue1 : DL_NodeValue;
  MyCounterValue2 : DL_NodeValue;
  nodeValues : ARRAY[0..1] OF POINTER TO DL_NodeValue;
END_VAR

Implementation

// Do something with the counters behind the nodes that will be subscribed
Counter1 := Counter1 + 1;
Counter2 := Counter2 + 2;

// Create Subscription , min. 100ms , max 50 Nodes
// 30 Seconds without using the ruleset for a subscribe the subscription is lost
CreateSubscriptionWithParams(Execute := executeCreate,
  SubscriptionName := ADR(subscriptionName),
  deadBandValue := 0,
  samplingInterval := LTIME#100MS);

// Subscribe Node
IF (CreateSubscriptionWithParams.Done) THEN
  // initialize the node addresses to be subscribed
  nodeAddressPointer[0] := ADR('plc/app/Application/sym/PLC_PRG/Counter1');
  nodeAddressPointer[1] := ADR('plc/app/Application/sym/PLC_PRG/Counter2');

  // set the nodevalue pointer to a nodevalue, the received data will be written to those values
  nodeValues[0] := ADR(MyCounterValue1);
  nodeValues[1] := ADR(MyCounterValue2);
  Subscribe(Enable := enableSub, SubscriptionName := ADR(subscriptionName), NodeNames := nodeAddressPointer,

NodeValues := nodeValues);
END_IF

// When the subscription is finished the values will be read here correctly
IF (Subscribe.Active) THEN
  MyCounterValue1.GetValueInt16(Value => SubscribedCounter1Value);
  MyCounterValue2.GetValueInt16(Value => SubscribedCounter2Value);
END_IF

### 10.7.7 Example of an event

In this example, the Example_EventFiring function block is derived from the
BaseEventType function block via EXTENDS.

Declaration

(* The first derived function block from BaseEventType will be handled as event.
When deriving this "Example_PublishEvent" funciton block, it will NOT be recognized as event!
Only the VAR_INPUT will be packed into the published event. *)
FUNCTION_BLOCK Example_PublishEvent EXTENDS BaseEventType
VAR_INPUT
boolData : BOOL; // example variable with bool information
intData : INT;    // example variable with int information
END_VAR
VAR_OUTPUT
END_VAR
VAR
END_VAR

### 10.7.8 Example of an event with subscription

Declaration

PROGRAM Example_EventSubscription
VAR

    xInitialized : BOOL := FALSE;

    // Different from usual subscriptions, the block DL_CreateEventSubscription is used
    CreateEventSubscription : DL_CreateEventSubscription;
    // Subscribing is done with the usual subscribe block
    Subscribe : DL_Subscribe;
    // As example only one subscribe will be done. The received values will be saved in this array.
    SubscribedNodeValues : ARRAY [1..1] OF POINTER TO DL_NodeValue;
    SubscribedNodeValue : DL_NodeValue;

    // Name of the subscription is mandatory, but can be set as wished
    subscriptionName : STRING(255) := 'Event1';

    subscribedNodeName : ARRAY [1..1] OF POINTER TO STRING;
    nodeNameArray : ARRAY [1..1] OF STRING(350) := ['plc/app/<APPLICATION_NAME>/sym/Example_PublishEvent'];     //
APPLICATION_NAME and path to variable can be different in your configuration

    // This part is used to encode the flatbuffer object with the help of th "DecodeFlatbufferToOutputs" method
    // The method can be found in the CXA_OPCUAEXT library
    // Also the CXA_OpcUaClient library is need for the Arguments of type 'PLCVariable'
    fbReadNodeValueSchemaOutput:    DL_ReadNodeValue;
    strReference : STRING := 'types/events/plc/<APPLICATION_NAME>/Example_PublishEvent'; // APPLICATION_NAME and
path to variable can be different in your configuration
    fbNodeValueSchemaOutput : DL_NodeValue;

    // output arguments for the decoding method
    OutputArguments_: ARRAY [1..2] OF CXA_OpcUaClient.PLCVariable;
    OutputArgumentsCount: UINT := 2;
    // error of the decoding method
    Error_: ERROR_STRUCT;

    // received data from event subscription
    testDataBool : BOOL;
    testDataInt : INT;

    // result of publishing the event
    fireResult : DL_RESULT;

    // event previously defined in the example event firing
    // Symbol need to be configured in the symbol configuration or by attribute
    {attribute 'symbol' := 'readwrite'}
    eventFiring : Example_EventFiring;

END_VAR

Implementation

// initialize the node names and the output arguments, which will have the decoded flatbuffer values from the
read event
subscribedNodeName[1] := ADR(nodeNameArray[1]);
SubscribedNodeValues[1] := ADR(SubscribedNodeValue);

OutputArguments_[1]:= GetPlcVariableType(variable:= testDataBool );
OutputArguments_[2]:= GetPlcVariableType(variable:= testDataInt );

// Create the event subscription
CreateEventSubscription(Execute := TRUE, SubscriptionName := ADR(subscriptionName));

// if the creation of the subscription is done go tu subscribe the event node
IF (CreateEventSubscription.Done) THEN
    Subscribe(Enable := TRUE, NodeNames := subscribedNodeName, NodeValues := SubscribedNodeValues,
SubscriptionName := ADR(subscriptionName));
    // now the flatbuffer schema of the event needs to be read for decoding purpose
    IF (fbReadNodeValueSchemaOutput.Done <> TRUE) THEN
fbReadNodeValueSchemaOutput(Execute:= TRUE, NodeName:= strReference, NodeValue:= fbNodeValueSchemaOutput);
    END_IF

    // with all information the flatbuffer can be decoded into the variables 'testDataBool' and 'testDataInt'
    // the outcome should match the input from below: 'testDataBool = TRUE', 'testDataInt = 666'
    IF fbReadNodeValueSchemaOutput.Done AND Subscribe.Done THEN
Error_:=DecodeFlatbufferToOutputs(SchemaOut:=fbNodeValueSchemaOutput , Flatbuffer:=
SubscribedNodeValues[1]^, pOutputArguments:= ADR(OutputArguments_), OutputArgumentsCount:=
OutputArgumentsCount,boTolerant:=TRUE);
    END_IF
END_IF

// set the values to be set to the event and fire it
eventFiring(boolData := TRUE, intData := 666);
fireResult := eventFiring.mFire();

## 10.8 “Real-time” function blocks

### 10.8.1 Introduction and overview

The "Datalayer_RT" directory provides access to the real-time functions of the
Data Layer.

The function blocks are implemented in the Runtime and provide the interface
functions of the Data Layer almost 1:1. These functions can be used in the IEC
program.
The provided methods call the functionalities of the Data Layer directly and
blocking.
There are two options to use the real-time interface:
● User:
  The user can access and edit all real-time data in the Data Layer and edit
  them.
● Owner:
  The owner can create new real-time data in each node.
Each call of the BeginAccess method has to be terminated by the call of the
EndAccess method. Otherwise, the MemoryMap is blocked for any other user.

### 10.8.2 Functional description of DL_MemOwner

    Introduction and overview
The following function blocks are generated to access real-time data:
● DL_MemOwner
● DL_MemUser

  The methods CreateMemory (DL_MemOwner) and OpenMemory (DL_Mem‐
  User) create a new access to any MemoryMap. After calling the BeginAccess
  method, a pointer is returned to the first element of the intended Memo‐
  ryMap. The GetSize and GetType methods can be used to process any map‐
  ping.

CreateMemory
The CreateMemory method initializes the internal variables of the Runtime
to access the Data Layer interface. This method also calls the "createMemory‐
Sync" method of the Data Layer interface.
  ● NodeName:
    Name of the node to be created or accessed.
  ● SizeBytes:
    Size of the MemoryMap to be created.
  ● MemType:
    Type of memory allocation (Input, Output, Retain)

DeleteMemory
The DeleteMemory method deinitializes the internal variables of the Runtime
to access the Data Layer interface. This method also calls the "deleteMemory‐
Sync" method of the Data Layer interface.

SetMemoryMap
To set the MemoryMap to a suitable value, a flatbuffer construction is
required.
  For more information, refer to the example in ⮫ Chapter Example DL_Mem‐
  Owner on page 132.
  ● NodeValue:
    Object that contains the MemoryMap information.

    BeginAccess
The BeginAccess method allows to access the real-time data for this program
and blocks this real-time data for others. It is mandatory to call the EndAc‐
cess method after the corresponding operations are completed. Otherwise, no
other user can access the real-time data.
● Revision:
  The revision number required to access the created MemoryMap.
  (Note: When setting the MemoryMap later, ensure to use the same revision
  number)
● Data:
  This pointer is set to the first element of the MemoryMap created by calling
  the CreateMemory method.

    EndAccess
The EndAccess method terminates access to the real-time data for this pro‐
gram and allows others to access.

    GetMemoryMap
The GetMemoryMap method returns a NodeValue object. The function block
DL_NodeValue provides methods to access a NodeValue in the Data Layer.
● NodeValue:
  Object to which the MemoryMap is to be addressed.

    GetSize
The GetSize method specifies the number of elements addressed by the Mem‐
oryMap to iterate through the MemoryMap bytes.
● SizeBytes:
  Size of the MemoryMap (number of elements in the MemoryMap)

GetType
The GetType method returns the type of MemoryMap.
● MemType: There are currently four return values:
  – MEMORY_TYPE_UNKOWN = 0
  – MEMORY_TYPE_INPUT = 1
  – MEMORY_TYPE_OUTPUT = 2
  – MEMORY_TYPE_RETAIN = 3

Example DL_MemOwner
The function block DL_MemOwner differs mainly by calling the CreateMemory
method first instead of OpenMemory.
Size and type of the newly created MemoryMap have to be specified.

Declaration:

// This example program is used to create a new memory map in a new node.

PROGRAM Example_DatalayerRTMemOwner
VAR
  fbMemoryOwner : DL_MemOwner;              // function block to write a new memory map
  nodeNameRetainMemoryExample : STRING := 'sample/myPlcRTExample/NewRetainMemoryMap';
                                            // node name to the newly created memory map
  revisionNumber : UDINT := 5;              // revision number as described in the memory
map on the web-ui
  retainPointerWrite : POINTER TO BYTE;     // pointer to the newly created map
  memoryMapSize : UDINT := 32000;           // size of the new memory map

  memoryType : DL_MEMORY_TYPE;              // only to check the getType method

  xStart : BOOL := FALSE;                   // this will start the example program
  xInit : BOOL := FALSE;

  // different results to be requested by any method called from the function block
  ownerOpenMemoryResult : DL_RESULT;
  ownerBeginAccesResult : DL_RESULT;
  ownerEndAccesResult : DL_RESULT;
  ownerGetTypeResult : DL_RESULT;
  nodeValueResultOwner : DL_RESULT;

  i : UDINT := 0;                  // iterator for the memory map pointer

  // additional objects to set the revision number in memory map
  nodeValue : DL_NodeValue;
  fbConfigItem : CXA_AutomationCore_fbs.comm_datalayer_MemoryMap;
                                   //Flatbuffer function out of CXA_Automationcore_fbs
  fbBuilder : flatbuffers.FlatBufferBuilder;
                                   // Declare the flatbuffer builder out of
CXA_FlatbuffersEND_VAR

Implementation:

// Start the main code here
IF (xStart = TRUE) AND (xInit = TRUE)   THEN

// Begin to access the memory map at first, the Data-Pointer will be overwritten and will
point to the memory map
  ownerBeginAccesResult := fbMemoryOwner.BeginAccess(Data => retainPointerWrite,
Revision := revisionNumber);

  // Check the success of the BeginAccess-method to avoid null pointer actions
  IF (ownerBeginAccesResult = DL_RESULT.DL_OK) THEN

    fbMemoryOwner.GetSize(SizeBytes => memoryMapSize);

    // Create a new node value to set the revision number for the memory map
    fbBuilder(forceDefaults := TRUE); //Start flatbuffer builder and load with default

values

    fbConfigItem.startMemoryMap(fbBuilder);
    fbConfigItem.addRevision(revisionNumber);
     // Finish complete builder and closing the fbConfigItem
    fbBuilder.finish(fbConfigItem.endMemoryMap());
     //Set flatbuffer out of the builder in the variable to be written
    nodeValue.SetFlatbuffer(fbBuilder);

    nodeValueResultOwner := fbMemoryOwner.SetMemoryMap(NodeValue := nodeValue);

    // Now iterate every element in the pointed memory map
    FOR i := 0 TO memoryMapSize-1 BY 1 DO
        // as a short test set every value to 3
      retainPointerWrite^ := 3;
      // On every iteration also increase the pointer to get the next values
      retainPointerWrite := retainPointerWrite + 1;
    END_FOR
  END_IF

  // Before leaving this method end the access
  ownerEndAccesResult := fbMemoryOwner.EndAccess();
  xStart := FALSE;
END_IF

// At first call OpenMemory to set the nodename for the memorymap (in that case the retain
data node name)
IF (xStart = TRUE) AND (xInit = FALSE) THEN
  ownerOpenMemoryResult := fbMemoryOwner.CreateMemory(NodeName :=
nodeNameRetainMemoryExample, SizeBytes := 32000, MemType :=
DL_MEMORY_TYPE.MEMORY_TYPE_RETAIN);
  xInit := TRUE;
END_IF

### 10.8.3 Functional description of DL_MemUser

    Introduction and overview
The following function blocks are generated to access real-time data:
● DL_MemOwner
● DL_MemUser
The methods CreateMemory (DL_MemOwner) and OpenMemory (DL_Mem‐
User) create a new access to any MemoryMap. After calling the BeginAccess
method, a pointer is returned to the first element of the intended Memo‐
ryMap. The GetSize and GetType methods can be used to process any map‐
ping.

Each call of the BeginAccess method has to be terminated by the call of the
EndAccess method. Otherwise, the MemoryMap is blocked for any other user.

The provided methods call the functionalities of the Data Layer directly and
blocking.

CloseMemory
 The CloseMemory method deinitializes the internal variables of the Runtime
 to access the Data Layer interface. This method also calls the "closeMemory"
 method of the Data Layer interface.

OpenMemory
The OpenMemory method initializes the internal variables of the Runtime to
access the Data Layer interface. This method also calls the "openMemory"
method of the Data Layer interface.
    ● NodeName:
      Name of the node that should be accessed.

BeginAccess
  The BeginAccess method allows to access the real-time data for this program
  and blocks this real-time data for others. It is mandatory to call the EndAc‐
  cess method after the corresponding operations are completed. Otherwise, no
  other user can access the real-time data.
    ● Revision:
      The revision number required to access the created MemoryMap.
      (Note: When setting the MemoryMap later, ensure to use the same revision
      number)
    ● Data:
      This pointer is set to the first element of the MemoryMap created by calling
      the CreateMemory method.

EndAccess
    The EndAccess method terminates access to the real-time data for this pro‐
    gram and allows others to access.

    GetMemoryMap
The GetMemoryMap method returns a NodeValue object. The function block
DL_NodeValue provides methods to access a NodeValue in the Data Layer.
● NodeValue:

  Object to which the MemoryMap is to be addressed.

    GetSize
The GetSize method specifies the number of elements addressed by the Mem‐
oryMap to iterate through the MemoryMap bytes.
● SizeBytes:
  Size of the MemoryMap (number of elements in the MemoryMap)

    GetType
The GetType method returns the type of MemoryMap.
● MemType: There are currently four return values:
  – MEMORY_TYPE_UNKOWN = 0
  – MEMORY_TYPE_INPUT = 1
  – MEMORY_TYPE_OUTPUT = 2
  – MEMORY_TYPE_RETAIN = 3

    Example DL_MemUser
The following example explains the use of DL_MemUser in an IEC program.

Declaration:
// This example program is used to access a memory map and changing a newly created
persistent variable. This persistent variable must be created by the user and needs to be
localized in the memory map as it can differ from the example. In this example the
persistent variable has the index 68.
PROGRAM Example_DatalayerRTMemUser
VAR
    fbMemoryUser : DL_MemUser;                          // function block to be used by
this example
    nodeNameForRetain : STRING := 'plc/admin/retain';   // node name to any memory map to
be accessed
    revisionNumber : UDINT := 0;      // revision number as described in the memory map on
the web-ui
    retainPointer : POINTER TO BYTE; // pointer which will be overwritten with a pointer
to the requested memory map

    memoryMapSize : UDINT := 0;        // size of the memory map
    memoryType : DL_MEMORY_TYPE;   // only to check the getType method

    // flags to control this example
    xStart : BOOL := FALSE;          // this will start the example program
    xSetValue : BOOL := FALSE;      // this will set the persistent value to a fixed value
    fixedValue : BYTE := 70;        // the fixed value to be written in the persistent
value

    xInit : BOOL := FALSE;

    // different results to be requested by any method called from the function block
    openMemoryResult : DL_RESULT;
    beginAccesResult : DL_RESULT;
    endAccesResult : DL_RESULT;
    getSizeResult : DL_RESULT;
    getTypeResult : DL_RESULT;
    i : UDINT := 0;                  // iterator for the memory map pointer
END_VAR

Implementation:

// Start the main code here
IF (xStart = TRUE) AND (xInit = TRUE) THEN
// Begin to access the memory map at first, the Data-Pointer will be overwritten and will
point to the memory map
    beginAccesResult := fbMemoryUser.BeginAccess(Data := retainPointer, Revision :=
revisionNumber);

    // Check the success of the BeginAccess-method to avoid null pointer actions
    IF beginAccesResult = DL_RESULT.DL_OK THEN

        // get the map size to know how far it can be iterated
        getSizeResult := fbMemoryUser.GetSize(SizeBytes => memoryMapSize);

        // check the getType method
        getTypeResult := fbMemoryUser.GetType(MemType => memoryType);

        // Now iterate every element in the pointed memory map
        FOR i := 0 TO memoryMapSize-1 BY 1 DO

             (* To change any value just set the value behind the pointer
              For this test case a persistent variable is defined and written at index 68
              now we want to change it when the flag is set *)
             IF (i = 68) AND (xSetValue = TRUE) THEN
                 retainPointer^ := fixedValue;
             END_IF
             // On every iteration also increase the pointer to get the next value
             retainPointer := retainPointer + 1;
         END_FOR
    END_IF

    // Before leaving this method end the access
    endAccesResult := fbMemoryUser.EndAccess();
    fbMemoryUser.CloseMemory();
    xStart := FALSE;
END_IF

// At first call OpenMemory to set the nodename for the memorymap (in that case the retain
data node name)
IF (xStart = TRUE) AND (xInit = FALSE) THEN
    openMemoryResult := fbMemoryUser.OpenMemory(nodeNameForRetain);
    xInit := TRUE;
END_IF

### 10.8.4 Known restrictions

WSTRING data type
The Data Layer does not support the WSTRING data type. It is always con‐
verted to a standard UTF8 string on the PLC provider side (and vice versa).
This cannot be automated for real-time data, which results in display errors.
Thus, it is not recommended to use the WSTRING data type.

## 10.9 FlatBuffer

Function blocks and methods are available to read the data type FlatBuffer on
the control or to write to it.

The library includes only the basic functionalities to allow general access to
the FlatBuffer.
It is required, as the axis configurations or the kinematic configurations are for
example created in FlatBuffers on the control.
We do not recommend a direct FlatBuffer programming with the CXA_Data‐
layer library and thus do not describe it further.
It should only exclusively be programmed via parent libraries, e.g. the
CXA_MotionCore_fbs. The complete function blocks and methods are normally
stored in these libraries to access axis configurations or kinematic configura‐
tions for example.

## 10.10 Error codes

### 10.10.1 Introduction and overview

If the “Error” output is set, all function blocks return a detailed error descrip‐
tion.
VAR_OUTPUT
                    Error                BOOL                Error (see ErrorID
                                                             and ErrorIdent)
                    ErrorID              ERROR_CODE          Error description
                    ErrorIdent           ERROR_STRUCT        Error description

ACCESS_ERROR (16#4) is currently returned as ErrorID.
ERROR_STRUCT analyzes the error messages in detail. They include main and
detailed diagnostics.
● Additional1 – Main diagnostics
● Additional2 – Detailed diagnostics
If main and detailed diagnostics are not yet supported (Additional2 = NULL),
errors can be diagnosed in detail using the error table CXA_Table.
● Additional1 – Contains the error number
● Additional2 – NULL

### 10.10.2 Error codes of the CXA_Table for the CXA_Datalayer

Table 78: Error codes of the CXA_Table for the CXA_Datalayer
Additional1          DL_Result                     Data layer facility   Description

16#80000001          DL_FAILED                     General information   Temporary use

16#80010001          DL_INVALID_ADDRESS            Application           NodeName is unknown or wrong

16#80010002          DL_UNSUPPORTED                Application           Function not implemented

16#80010003          DL_OUT_OF_MEMORY              Application           Insufficient memory or resources

16#80010004          DL_LIMIT_MIN                  Application           Fallen below limit value

16#80010005          DL_LIMIT_MAX                  Application           Limit value exceeded

16#80010006          DL_TYPE_MISMATCH              Application           Wrong data type or wrong FlatBuffer

16#80010007          DL_SIZE_MISMATCH              Application           Size mismatch; Current size does not match
                                             requested size

16#80010009          DL_INVALID_FLOATINGPOINT      Application           Invalid floating point number

16#8001000A          DL_INVALID_HANDLE             Application           Invalid handle or NULL pointer

16#8001000B          DL_INVALID_OPERATION_MODE     Application           Cannot be accessed due to invalid operation
                                             mode (writing not possible)

16#8001000C          DL_INVALID_CONFIGURATION      Application           Configured value mismatches

16#8001000D          DL_INVALID_VALUE              Application           Invalid value

16#8001000E          DL_SUBMODULE_FAILURE          Application           Error in child module

16#8001000F          DL_TIMEOUT                    Application           Request timeout

16#80010010          DL_ALREADY_EXISTS             Application           Node cannot be created. It already exists

16#80010011          DL_CREATION_FAILED            Application           Error when creating the new node

16#80010012          DL_VERSION_MISMATCH           Application           Version conflict

16#80010013          DL_DEPRECATED                 Application           Error in child module

16#80010014          DL_PERMISSION_DENIED          Application           Old function. It is not supported anymore

16#80010015          DL_NOT_INITIALIZED            Application           Node not yet initialized

16#80020001          DL_COMM_PROTOCOL_ERROR        Communication         Internal protocol error

16#80020002          DL_COMM_INVALID_HEADER        Communication         Internal header error

16#80030001          DL_CLIENT_NOT_CONNECTED       Users                 Unknown user

16#80060001          DL_RT_NOTOPEN                 Realtime              Realtime object does not exist

16#80060002          DL_RT_INVALIDOBJECT           Realtime              Wrong realtime object

16#80060003          DL_RT_WRONGREVISON            Realtime              Wrong revision (version mismatch)

16#80060004          DL_RT_NOVALIDDATA             Realtime              No valid data available

16#80060005          DL_RT_MEMORYLOCKED            Realtime              Memory range currently locked
