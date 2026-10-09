# 7 CXA_CommonTypes

## 7.1 Introduction and overview

The CXA_CommonTypes library contains data types and input and output vari‐
ables of the ctrlX function blocks.
All data types are implemented acc. to IEC 61131-3 irrespective of the hard‐
ware.
These libraries do not require any child libraries.

## 7.2 Global variables

### 7.2.1 CXA_PLC_MAINDIAG_ERROR

Brief description
CXA_PLC_MAINDIAG_ERROR defines a mask for the main diagnostics of the
data type DWORD. The basic function blocks use the constant to set the error
code.

Table 21: CXA_PLC_MAINDIAG_ERROR reference table
Library/folder
CXA_CommonTypes/Global Variables

Table 22: Type definition of the CXA_PLC_MAINDIAG_ERROR
Name                   Data type               Value
CXA_PLC_MAINDIAG_ERROR DWORD                   16#0A0F0000

### 7.2.2 CXA_PLC_DETAILDIAG_ERROR

Brief description
CXA_PLC_DETAILDIAG_ERROR defines a mask for the main diagnostics of the
data type DWORD. The basic function blocks use the constant to set the error
code.

Table 23: CXA_PLC_DETAILDIAG_ERROR reference table
Library/folder
CXA_CommonTypes/Global Variables

Table 24: Type definition of the CXA_PLC_DETAILDIAG_ERROR
Name                     Data type           Value
CXA_PLC_DETAILDIAG_ERROR DWORD               16#0C230000

## 7.3 Referencing objects

### 7.3.1 Introduction and overview

To reference objects (axes, kinematics and axis groups), one REF structure
with allocated string types is provided for each object type.
Information is sent to the respective function block using VAR_IN_OUT CON‐
STANT.
The REF structure contains a string with up to 15 characters. It is used as
unique object reference.

The unique names for axes, axis groups and kinematics are specified in the

control configuration.

### 7.3.2 AXIS_REF

Brief description
The structure contains information to control an axis.

Table 25: AXIS_REF reference table
Library/folder
CXA_CommonTypes/DUTs/PLCopen

Table 26: Type definition of AXIS_REF
Name                      Type                       Description
AxisName                  STRING(15)                 Unique object name of
                                                     the axis

Functional Description
The structure AXIS_REF contains a unique reference to an axis. It is used to
address single axes and axis-type objects.
The data structure is applied to the “Axis” input of the respective function
block. The respective function blocks are for example in the library For func‐
tion blocks of the example, go to CXA_PLCopen.

### 7.3.3 AXES_GROUP_REF

Brief description
The structure contains information to control a corresponding axis group.

Table 27: AXES_GROUP_REF reference table
Library/folder
CXA_CommonTypes/DUTs/PLCopen

Table 28: Type definition of AXES_GROUP_REF
Name                      Type                       Description
KinName                   STRING(15)                 Unique object name of
                                                     the axis group

Functional description
The structure AXES_GROUP_REF contains a unique reference to an axis group.
It is used to address kinematics.

The data structure is applied to the “AxesGroup” input of the respective func‐
tion block. The respective function blocks are for example in the library For
function blocks of the example, go to CXA_PLCopen.

### 7.3.4 DEVICE_REF

Brief description
The structure contains information to access another control or another logic
device.

Table 29: DEVICE_REF reference table
Library/folder
CXA_CommonTypes/DUTs/Logical addresses

Table 30: Type definition of DEVICE_REF
Name                      Type                      Description
UriPath                   STRING(255)               URI path of a logic device

Functional description
The structure DEVICE_REF contains a unique reference to a control or another
logic device.

### 7.3.5 IL_HANDLE

Brief description
The data type defines a generally usable reference to another object.

Table 31: IL_HANDLE reference table
Library/folder
CXA_CommonTypes/DUTs

Table 32: Type definition of IL_HANDLE
Name                      Type                      Description
IL_HANDLE                 POINTER TO BYTE           Untyped pointer to a data
                                                    object.

Functional description
The data type IL_HANDLE contains an untyped reference to a data object or a
logic resource.

## 7.4 Error Diagnostics

### 7.4.1 ERROR_CODE

Brief description
This enumeration contains all error types characterizing an error at the func‐
tion block.
The ERROR_CODE provides quick information on the error cause.

Table 33: ERROR_CODE reference table
Library/folder
CXA_CommonTypes/DUTs/Diagnostics of POUs

Table 34: Type definition of ERROR_CODE
Name                          Value       Description
NONE_ERROR                    16#0        No error
INPUT_INVALID_ERROR           16#1        Input error
COMMUNICATION_ERROR           16#2        Error during communication
RESOURCE_ERROR                16#3        Resource error (e.g. insufficient
                                          memory)
ACCESS_ERROR                  16#4        Access error, missing rights
STATE_MACHINE_ERROR           16#5        Invalid function block state
INPUT_RANGE_ERROR             16#6        Inputs beyond the valid range

CALCULATION_ERROR             16#7        Error during computation
DEVICE_ERROR                  16#8        Device error occurred
OTHER_ERROR                   16#7FFE     Undefined error
SYSTEM_ERROR                  16#7FFF     System error occurred

### 7.4.2 ERROR_STRUCT

Brief description
The error structure provides all detailed information on an actual error.
This information can be analyzed and read directly at the corresponding
instance of a PLCopen function block.
The components have to be interpreted as follows:
● Determining table number
● For the CXA_TABLE, Additonal1 and Additional2 are the main and detailed
  diagnostics. For details, refer to the documentation ⮫ ctrlX OS Diagnostics
  xxVRS, Reference Book.
● It is a Sercos error code in the SERCOS_TABLE. The error is coded in the
  lower 16 bits of Additional2.

Table 35: ERROR_STRUCT reference table
Library/folder
CXA_CommonTypes/DUTs/Diagnostics of POUs

Table 36: Type definition of ERROR_STRUCT
Name                      Type                      Description
Table                     ERROR_TABLE               Diagnostic table
Additional1               DWORD                     Main diagnostic number
Additional2               DWORD                     Detailed diagnostic
                                                    number

Main and detailed diagnostics are output in Additional1 and Additional2. For
the error code table CXA_TABLE, refer to the error code listed in the documen‐
tation ⮫ ctrlX OS, Diagnostics xxVRS, Reference Book.

### 7.4.3 ERROR_TABLE

Brief description
The ERROR_TABLE provides the first element of the ERROR_STRUCT. Use the
number to select the table in which the "Additional1" error code has to be
searched.

Table 37: ERROR_TABLE reference table
Library/folder
CXA_CommonTypes/DUTs/Diagnostics of POUs

Table 38: Type definition of ERROR_TABLE
Name                      Value                      Description
NO_TABLE_USED             16#0                       No error
CXA_TABLE                 16#1                       ctrlX AUTOMATION
SERCOS_TABLE              16#10                      Sercos error
USER1_TABLE               16#1000                    Free user table
USER2_TABLE               16#1001                    Free user table
USER3_TABLE               16#1002                    Free user table
USER4_TABLE               16#1003                    Free user table
USER5_TABLE               16#1004                    Free user table
USER6_TABLE               16#1005                    Free user table
USER7_TABLE               16#1006                    Free user table
USER8_TABLE               16#1007                    Free user table
USER9_TABLE               16#1008                    Free user table
USER10_TABLE              16#1009                    Free user table

## 7.5 Reporting date and absolute time specification

### 7.5.1 Introduction and overview

There are three structures to provide the date and other absolute time specifi‐
cations.
● SYS_TIME64, system time in microseconds since 01.01.1970, 00:00 o'clock.
● EXT_SYS_TIME_DATE, system time in microseconds since 01.01.1970, 00:00
  o'clock, additional data is year, month, day, hours, minutes, seconds, milli‐
  seconds and week day are calculated from the system time.
● SYS_TIME_DATE, year, month, day, hours, minutes, seconds, milliseconds
  and week day, calculated based on the system time in microseconds since
  01.01.1970, 00:00 o'clock.

### 7.5.2 SYS_TIME64

Brief description
Structure to output the system time in microseconds since 01.01.1970, 00:00
o'clock.

Table 39: SYS_TIME64 reference table
Library/folder
CXA_CommonTypes/DUTs/Time

Table 40: Type definition of SYS_TIME64 - Microseconds since 1970
Name                      Type                       Description
LowValue                  DWORD                      Low value part (µs)
HighValue                 DWORD                      High value part (µs)

### 7.5.3 SYS_TIME_DATE

Brief description
Structure to provide information on year, month, day, hours, minutes, sec‐
onds, milliseconds and week day calculated from a system time in microsec‐
onds since 01.01.1970, 00:00 o'clock.

Table 41: SYS_TIME_DATE reference
Library/folder
CXA_CommonTypes/DUTs/Time

Table 42: Type definition of EXT_SYS_TIME_DATE
Name                      Type                      Description
Year                      UINT                      Year
Month                     UINT                      Month
Day                       UINT                      Day
Hour                      UINT                      Hour
Minute                    UINT                      Minute
Second                    UINT                      Second
Milliseconds              UINT                      Milliseconds

### 7.5.4 EXT_SYS_TIME_DATE

Brief description
Structure to return the system time in microseconds since 01.01.1970, 00:00
o’clock and additional data: year, month, day, hours, minutes, seconds, milli‐
seconds and week day are calculated from the system time.

Table 43: EXT_SYS_TIME_DATE reference table
Library/folder
CXA_CommonTypes/DUTs/Time

Type definition of EXT_SYS_TIME_DATE
Name                      Type                      Description
LowValue                  DWORD                     Low value word (µs)
HighValue                 DWORD                     High value word (µs)
Year                      UINT                      Year
Month                     UINT                      Month
Day                       UINT                      Day
Hour                      UINT                      Hour
Minute                    UINT                      Minute
Second                    UINT                      Second
Milliseconds              UINT                      Milliseconds
DayOfWeek                 UINT                      Weekday
