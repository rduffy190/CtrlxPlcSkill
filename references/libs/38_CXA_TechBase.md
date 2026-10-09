# 38 CXA_TechBase

## 38.1 Introduction and overview

The CXA_TechBase PLC library provides functions for creating, deleting, and
reading FlexProfile and point tables.
Function blocks:
●   ⮫ MB_WriteFlexProfile
●   ⮫ MB_WriteFlexProfileType02
●   ⮫ MB_ReadFlexProfile
●   ⮫ MB_GetPointTableNames
●   ⮫ MB_IsPointTableExists
●   ⮫ MB_DeletePointTable
●   ⮫ MB_WritePointTable
●   ⮫ MB_WritePointTableType02
●   ⮫ MB_AxsValidateCamIn
●   ⮫ MB_ReadValidateCamIn
●   ⮫ MB_ReadCamInStateInfo

## 38.2 Data types

### 38.2.1 MB_PROFILE_NAME (STRUCT)

Table 1234: MB_PROFILE_NAME (STRUCT) data type
Name               Type              Default value         Description
0                  INT                                     Profile 0
1                  INT                                     Profile 1
2                  INT                                     Profile 2
3                  INT                                     Profile 3

### 38.2.2 MB_CAMIN_PROFILE_STATE (STRUCT)

Table 1235: MB_CAMIN_PROFILE_STATE (STRUCT) data type
Name               Type                          Default      Description
                                                 value
ProfileName        ⮫ MB_PROFILE_NAME             0            Profile name.
PointTableName     STRING (63)                   ‘’           Point table
                                                              name.
AccessState        AccessState                   UNVALI‐      The access
                                                 DATED        status of the
                                                              specified axis
                                                              profile.

                                                       Function blocks         1344

## 38.3 Function blocks

### 38.3.1 MB_WriteFlexProfile

Brief description
The function block provides a regular data type interface to write a FlexProfile
configuration to a specific axis. The entire process is not in real time.
Profile validation is performed automatically after writing, and the segment
and event arrays have to be large enough.
Setting the sets NumberOfSegments and NumberOfEvents to 0 can reset a
profile empty without a validation trigger being triggered when a profile is
reset. Events cannot be set independently of each other, i.e. if NumberOfSeg‐

ments is 0, NumberOfEvents cannot be 0.
Path of the Data Layer node: motion/axs/[axis]/cfg/functions/coupling/sync-
motion/flexprofile/profiles
Test with a ctrlX CORE X3 and an interval of 2 ms: Writing a profile with five
segments and five events can take up to three cycles.

Interface description

Table 1236: Interface variables of the MB_WriteFlexProfile function block
I/O type      Name            Data type         Comment
VAR_INPUT     Execute         BOOL              Start writing the FlexProfile
                                                configuration at a rising edge
              ProfileName     STRING            Name of the profile to be
                                                written
           NumberOfSeg‐ UINT                    Number of segments
           ments
           NumberOfE‐    UINT                   Number of events
           vents
           MasterAxisVe‐ LREAL                  Velocity of the master axis
           locity
VAR_OUTPUT Done          BOOL               Execution completed
           Active        BOOL               Execution running
           Error         BOOL               Indicates that an error
                                            occurred
              ErrorID         ⮫ ERROR_CODE Error class
              ErrorIdent      ⮫ ERROR_STRUC Detailed error information
                              T
VAR_IN_OUT Axis               AXIS_REF      Result of the point table
                                            name

1316 /    ctrlX PLC Engineering
1344      Function blocks

I/O type      Name             Data type         Comment
              ProfileSeg‐      ARRAY [*]         Array of segments that is large
              ments            OF MB_PRO‐        enough to store all segments
                               FILE_SEGMENT      Size should be greater than or
                                                 equal to NumberOfSegments
              ProfileEvents    ARRAY [*]         Array of events that is large
                               OF MB_PRO‐        enough to store all events
                               FILE_EVENT        Size should be greater than or
                                                 equal to NumberOfEvents
              ProfileUnits     MB_PRO‐           Configuration of the units in
                               FILE_UNITS        the FlexProfile

### 38.3.2 MB_WriteFlexProfileType02

Brief description
This function block writes a FlexProfile configuration to a specified axis.

Interface description

Table 1237: Interface variables of the MB_WriteFlexProfileType02 function
block
I/O type      Name             Data type         Comment
VAR_INPUT     Execute          BOOL              Resets all internal axis-related
                                                 errors
              ProfileName      STRING            Name of the profile to be
                                                 written
           NumberOfSeg‐ UINT                     Number of segments
           ments
           NumberOfE‐    UINT                    Number of events
           vents
           MasterAxisVe‐ LREAL                   Velocity of the master axis
           locity
VAR_OUTPUT Done          BOOL                Execution completed
           Active        BOOL                Execution running
           Error         BOOL                Indicates that an error
                                             occurred
              ErrorID          ⮫ ERROR_CODE Error class
              ErrorIdent       ⮫ ERROR_STRUC Detailed error information
                               T
VAR_IN_OUT Axis                AXIS_REF      Result of the point table
                                             name

                                                      Function blocks       1344

I/O type      Name            Data type         Comment
              ProfileSeg‐     ARRAY [*]         Array of segments that is large
              ments           OF MB_PRO‐        enough to store all segments
                              FILE_SEGMENT      Size should be greater than or
                                                equal to NumberOfSegments
              ProfileEvents   ARRAY [*]         Array of events that is large
                              OF MB_PRO‐        enough to store all events
                              FILE_EVENT        Size should be greater than or
                                                equal to NumberOfEvents
              ProfileUnits    MB_PRO‐           Configuration of the units in
                              FILE_UNITS        the FlexProfile

Functional description
This function writes a new FlexProfile configuration to the Motion kernel and
validates it.
The function responds deterministically, but is not suitable for constant real-
time applications. Processing can take longer than one cycle.
The time required depends on the size and complexity of the new FlexProfile.

### 38.3.3 MB_ReadFlexProfile

Brief description
The function block provides a regular data type interface to read a FlexProfile
configuration of a specific axis. The entire process is not in real time.
The segment and event arrays have to be large enough.
Path of the Data Layer node: motion/axs/[axis]/cfg/functions/coupling/sync-
motion/flexprofile/profiles
Test with a ctrlX CORE X3 and an interval of 2 ms: In most cases, a profile
with five segments and five events can be read in one cycle.

Interface description

Table 1238: Interface variables of the MB_WritePointTable function block
I/O type      Name            Data type         Comment
VAR_INPUT     Execute         BOOL              Start reading the FlexProfile
                                                configuration at a rising edge
           ProfileName   STRING                 Name of the profile to be read
VAR_OUTPUT MasterAxisVe‐ LREAL                  Velocity of the master axis
           locity
           NumberOfSeg‐ UINT                    Number of segments
           ments

1318 /    ctrlX PLC Engineering
1344      Function blocks

I/O type      Name            Data type       Comment
              NumberOfE‐      UINT            Number of events
              vents
              Done            BOOL          Execution completed
              Active          BOOL          Execution running
              Error           BOOL          Indicates that an error
                                            occurred
              ErrorID         ⮫ ERROR_CODE Error class
              ErrorIdent      ⮫ ERROR_STRUC Detailed error information
                              T
VAR_IN_OUT Axis               AXIS_REF      Result of the point table
                                            name
              ProfileSeg‐     ARRAY [*]     Array of segments that is large
              ments           OF MB_PRO‐    enough to store all segments.
                              FILE_SEGMENT Otherwise, the remaining seg‐
                                            ments are ignored
              ProfileEvents   ARRAY [*]     Array of events that is large
                              OF MB_PRO‐    enough to store all events.
                              FILE_EVENT    Otherwise, the remaining
                                            events are ignored
              ProfileUnits    MB_PRO‐       Configuration of the units in
                              FILE_UNITS    the FlexProfile

### 38.3.4 MB_GetPointTableNames

Brief description
The function block provides a regular data type interface to read FlatBuffer
from the Data Layer node and to retrieve all the names of the point tables.
The entire process is not in realtime. The array of PointTableNames must be
large enough to store all data. Otherwise, the rest is ignored and an error
is triggered. The PointTablesCount output specifies the number of currently
configured point tables.
Path of the Data Layer node: motion/cfg/functions/sync-motion/point-table/
tables
Test with a ctrlX CORE X3 and an interval of 2 ms: In most cases, all the
names of the point tables can be called in one cycle.

Interface description

Table 1239: Interface variables of the MB_GetPointTableNames function block
I/O type      Name            Data type       Comment
VAR_INPUT     Execute         BOOL            Start reading the point tables
                                              at a rising edge

                                                      Function blocks      1344

I/O type   Name              Data type         Comment
VAR_OUTPUT PointTables‐      UDINT             Total number of point tables
           Count
           Done              BOOL          Execution completed
           Active            BOOL          Execution running
           Error             BOOL          Indicates that an error
                                           occurred
              ErrorID        ⮫ ERROR_CODE Error class
              ErrorIdent     ⮫ ERROR_STRUC Detailed error information
                             T
VAR_IN_OUT PointTable‐       ARRAY [*] OF  Result of the point table

           Names             STRING        names

### 38.3.5 MB_IsPointTableExists

Brief description
The function block provides a regular data type interface to read FlatBuffer
from the Data Layer node and to check whether the specified point table
exists. The entire process is not in realtime. The total path length does not
have be greater than 256.
Path of the Data Layer node: motion/cfg/functions/sync-motion/point-table/
tables/[table]
Test with a ctrlX CORE X3 and an interval of 2 ms: In most cases, it can be
checked in one cycle whether a point table is available.

Interface description

Table 1240: Interface variables of the MB_IsPointTableExists function block
I/O type      Name           Data type     Comment
VAR_INPUT     Execute        BOOL          Start a check whether the
                                           point table is available, at a
                                           rising edge
           PointTable‐       STRING        Name of the point table to be
           Name                            checked
VAR_OUTPUT Exists            BOOL          TRUE if the point table exists
           Done              BOOL          Execution completed
           Active            BOOL          Execution running
           Error             BOOL          Indicates that an error
                                           occurred
              ErrorID        ⮫ ERROR_CODE Error class
              ErrorIdent     ⮫ ERROR_STRUC Detailed error information
                             T

1320 /    ctrlX PLC Engineering
1344      Function blocks

### 38.3.6 MB_DeletePointTable

Brief description
The function block provides a regular data type interface to delete an existing
point table with a specific name. The entire process is not in realtime. The
total path length does not have be greater than 256.
Path of the Data Layer node: motion/cfg/functions/sync-motion/point-table/
tables/[table]
Test with a ctrlX CORE X3 and an interval of 2 ms: In most cases, a point
table can be deleted in one cycle.

Interface description

Table 1241: Interface variables of the MB_DeletePointTable function block
I/O type      Name           Data type     Comment
VAR_INPUT     Execute        BOOL          Start deleting the point table
                                           at a rising edge
           PointTable‐       STRING        Name of the point table to be
           Name                            deleted
VAR_OUTPUT Done              BOOL          Execution completed
           Active            BOOL          Execution running
           Error             BOOL          Indicates that an error
                                           occurred
              ErrorID        ⮫ ERROR_CODE Error class
              ErrorIdent     ⮫ ERROR_STRUC Detailed error information
                             T

### 38.3.7 MB_WritePointTable

Brief description
The function block refreshes the PointTable data via the Data Layer and cre‐
ates a new PointTable if the specified PointTableName does not exist.
The entire process is not in realtime. The size of PointTable must be greater
than or equal to NumberOfElements.
Path of the Data Layer node: motion/cfg/functions/sync-motion/point-table/
tables/[table]
Test with a ctrlX CORE X3 and an interval of 2 ms: Writing an existing point
table can take up to three cycles. Creating and writing a non-existent point
table can take up to six cycles.

                                                     Function blocks        1344

Interface description

Table 1242: Interface variables of the MB_WritePointTable function block
I/O type      Name           Data type         Comment

VAR_INPUT     Execute        BOOL              Start deleting the point table
                                               at a rising edge
           PointTable‐  STRING                 Target name of PointTable
           Name
           NumberOfEle‐ UINT                   Number of points
           ments
           PointTable   ARRAY [*] OF           Array of PointTable data
                        LREAL
VAR_OUTPUT Done         BOOL               Execution completed
           Active       BOOL               Execution running
           Error        BOOL               Indicates that an error
                                           occurred
              ErrorID        ⮫ ERROR_CODE Error class
              ErrorIdent     ⮫ ERROR_STRUC Detailed error information
                             T

### 38.3.8 MB_WritePointTableType02

Brief description
The function block writes a new point table to the Motion Runtime and vali‐
dates it so that it can then be activated.

Interface description

Table 1243: Interface variables: MB_WritePointTableType02 function block
I/O type       Name                Data type          Description
VAR_INPUT      Execute             BOOL               Start the write operation for the point table
                                                      configuration on the rising edge
               PointTableName      STRING (63)        Name of the affected points table
               ProfileName         ⮫ MB_PRO‐          A profile has to be specified when vali‐
                                   FILE_NAME          dating the point table

1322 /     ctrlX PLC Engineering
1344       Function blocks

I/O type           Name                 Data type            Description
NumberOfEle‐         UINT                 Number of points
ments
PointTableConfig     MB_POINT_TABLE_ Configuring the point table
                     CONFIG
VAR_OUTPUT Done                         BOOL            Processing completed
Active                       BOOL            In process
Error                        BOOL            Processing completed with error
ErrorID                      ⮫ ERROR_CODE    Diagnostic description in case of error
ErrorIdent           ⮫ ERROR_STRUCT Detailed diagnostics
VAR_IN_OUT         PointTableData       POINTER TO     Table data: The size has to be greater than
                     LREAL          or equal to "NumberOfElements"
VAR_IN_OUT         Axis                 ⮫ AXIS_REF
CONSTANT

       Functional description
       ● If the specified point table name does not exist, a new one is automatically
         created and validated. If the specified point table name already exists, it is
         overwritten and validated.
       ● The value of "PointTableAdr" has to be greater than or equal to "NumberO‐
         fElements".
       ● The function block is executed in a non-real-time task. In a test environ‐
         ment using ctrlX CORE X3, overwriting an existing point table takes three
         cycles. It takes about six cycles to create a new point table.

### 38.3.9 MB_AxsValidateCamIn

       Brief description
       This function validates a CamIn table for a specified profile. The function
       block is executed in a non-real-time task. The time required depends on the
       size of the CamIn table.

       Interface description

Table 1244: Interface variables: MB_AxsValidateCamIn function block
I/O type           Name                 Data type            Description
VAR_INPUT          Execute              BOOL                 Start validation of the point table with a
                                                             rising edge
                   PointTableName       STRING (63)          Name of the affected points table
                   ProfileName          ⮫ MB_PRO‐            A profile has to be specified when vali‐
                                        FILE_NAME            dating the point table
VAR_OUTPUT Done                         BOOL                 Processing completed
           Error                        BOOL                 Processing completed with error
           ErrorID                      ⮫ ERROR_CODE         Diagnostic description in case of error

                                                             Function blocks        1344

I/O type       Name                 Data type      Description
ErrorIdent           ⮫ ERROR_STRUCT Detailed diagnostics
VAR_IN_OUT     Axis                 ⮫ AXIS_REF
CONSTANT

       Functional description
       ● For the "Default" score table type (maximum 1,024 points), the cam table
         can be used with or without validation. However, for "Linear" or "Spline"
         point table types (up to 100,000 points), validation is required before exe‐
         cution. Otherwise, the error 090F2506/0C550637 of CXA_PLCopen 4.6.2.0
         is generated.

### 38.3.10 MB_ReadValidateCamIn

       Brief description
       This function validates a CamIn table for a specified profile. The function
       block is executed in a non-real-time task. The time required depends on the
       size of the CamIn table.

       Interface description

Table 1245: Interface variables: MB_ReadValidateCamIn function block
I/O type       Name                 Data type           Description
VAR_INPUT      Execute              BOOL                Start validation of the point table with a
                                                        rising edge
             PointTableName         STRING (63)         Name of the affected points table
VAR_IINPUT_C Axis                   ⮫ AXIS_REF          Reference to the target axis
ONSTANT
VAR_OUTPUT ProfileName              ⮫ MB_PRO‐           Profile assigned to the points table
                                    FILE_NAME
               AccessState          ML_FlexProfileAc‐   Profile access status
                                    cess
               Active               BOOL                Processing in progress
               Done                 BOOL                Processing completed
               Error                BOOL                Processing completed with error
               ErrorID              ⮫ ERROR_CODE        Diagnostic description in case of error
               ErrorIdent           ⮫ ERROR_STRUCT Detailed diagnostics

### 38.3.11 MB_ReadCamInStateInfo

       Brief description
       The function block reads the "CamIn" status information "ActivePointTable,"
       "ActiveProfile," "SingleExecutionDone," "WaitForSwitch," "WaitForSwitchGain,"
       and "Profiles" from the relevant axis.

1324 /    ctrlX PLC Engineering
1344      Function blocks

     Data Layer nodes in the Motion Runtime: motion/axs/<axis name>/state/func‐
     tions/coupling/sync-motion/cam-in
     The function block is executed in a non-real-time task.

     Interface description

Table 1246: Interface variables: MB_ReadCamInStateInfo function block
I/O type           Name               Data type          Description
VAR_INPUT          Execute            BOOL               Start validation of the point table with a
                                                         rising edge
VAR_IINPUT_C Axis                     ⮫ AXIS_REF         Reference to the target axis
ONSTANT
VAR_OUTPUT ActivePointTable           STRING (63)        Currently active axis point table
             ActiveProfile            ⮫ MB_PRO‐          Currently active axis cam profile
                                      FILE_NAME
                   SingleExecution‐   BOOL           The one-time execution of the cam disc has
                   Done                              been completed (only in "SINGLE" execu‐
                                                     tion mode).
                   WaitForSwitch     BOOL            CamIn waits for the specified switch posi‐
                                                     tion:
                                                     TRUE: CamIn is waiting
                                                     FALSE: CamIn does not wait
                   WaitForSwitchGain BOOL            CamIn is waiting for the specified setting
                                                     for the gain factor:
                                                     TRUE: CamIn is waiting for the gain factor
                                                     FALSE: CamIn does not wait
                   Profiles          ARRAY [0..3] OF State information for all profiles of the axes
                                     ⮫ MB_CAMIN_PRO‐ CamIn object
                                     FILE_STATE
                   Done              BOOL            Processing completed
                   Active            BOOL            Processing in progress
                   Error             BOOL            Processing completed with error
                   ErrorID           ⮫ ERROR_CODE    Diagnostic description in case of error
                   ErrorIdent         ⮫ ERROR_STRUCT Detailed diagnostics

                                                                               ctrlX AUTOMATION                               1344
