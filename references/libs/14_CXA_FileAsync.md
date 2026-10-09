# 14 CXA_FileAsync

## 14.1 Introduction and overview

The library CXA_FileAsync includes function blocks and methods to access
files and directories.
It uses the functions of the operating system. Thus, access restrictions can
apply.
The library divides the functions into two groups:
● File functions
  They are in the “File” folder:
● Directory functions
  They are in the “Directory” folder:

## 14.2 Time response of the function blocks

Time response of the function blocks complies with the PLCopen standard.
In read-only mode, files and folders are treated as objects on which actions
can be performed. A file or a directory opens at a rising edge at the “Enable”
input. If the opening was successful, the "InOperation" output becomes
active. If an error occurs, the "Error" output becomes active.
All other actions are started at a rising edge at the “Execute” input of the
respective function block. File and directory accesses require multiple PLC
cycles. During this period, the "Active" output is TRUE. After the action, the
“Done” output is set and “Active” is reset. If an error occurs while processing,
the "Error" output becomes active. All other Boolean outputs are reset.

## 14.3 Malfunction

The function blocks set the error code of the secondary functions if possible.
Own error codes are defined in some cases.
If an error is present, the “Errors” of the respective function block is set. The
system error code can be composed as follows using ErrorIdent.Additional1
and ErrorIdent.Additional2:
● Main diagnostics: ErrorIdent.Additional1
● Detailed diagnostics: ErrorIdent.Additional2
The main diagnostics includes the library code. The detailed diagnostics
includes the error code in the library.

## 14.4 File access

### 14.4.1 Introduction and overview

The file operations to manipulate the file content and to change the file are
handled individually.
The function block IL_FileAsync is used to access file content. It opens and
closes the file. The instance of the function block provides an access token at
the “FileHandle” output.
They can be used to execute more operations on the file using the following
function blocks:
● IL_FileReadAsync - Reads from a file
● IL_FileWriteAsync - Writes to a file
● IL_FileGetPosAsync – Gets the current writing or reading position in the
  file
● IL_FileSeekAsync – Sets the current writing or reading position in the file

    Create the access token for these function blocks at the “FileHandle” input.
    The following function blocks support the file manipulation:
    ● IL_FileCopyAsnyc - Creates a file copy
    ● IL_FileDeleteAsync - Deletes a file
    ● IL_FileGetSizeAsync - Determines a file size
    ● IL_FileGetTimeAsync - Determines the creation time, modification time and
      the last access time of a file
    ● IL_FileRenameAsync - Renames or moves this file

### 14.4.2 IL_FileAsync

    Brief description

    The function block IL_FileAsync closes or creates a file.

    Interface description

Table 204: Interface variables of the IL_FileAsync function block
                 Name            Type                                   Description
VAR_INPUT        Enable          BOOL                                   A rising edge opens the file
                                                                        and a falling closes the file
                 FileName        STRING                                 Name of the file to be
                                                                        opened
                 Mode            ⮫ L_FILE_ACCESS_MODE                   Mode of access
VAR_OUTPUT       InOperation     BOOL                                   File is open
                 Active          BOOL                                   File access active
                 Shutdown        BOOL                                   File is closed
                 Error           BOOL                                   An error occurred
                 ErrorID         ⮫ ERROR_CODE                           Error classification
                 ErrorIdent      ⮫ ERROR_STRUCT                         Error Diagnostics
                 FileHandle      ITF_FILEASYNC                          Access token

Table 205: Min./max. and default values of the IL_FileAsync function block inputs
Name         Type                Min. value Max. value       Default value Applied
Enable       BOOL                FALSE      TRUE             FALSE         Continuous
FileName     STRING                                                        Rising edge at "IL_FileA‐
                                                                           syncEnable"
Mode         IL_FILE_ACCESS_M                                AM_READ       Rising edge at "IL_FileA‐
             ODE                                                           syncEnable"

Functional description
The function block IL_FileAsync opens or creates a file. The input "IL_FileA‐
syncFileName" contains the name and the file directory if present. Paths
are specified separately with "IL_FileAsync/" in Unix style. The “Mode” input
specifies how to open the file.
There are the following options:
Table 206: Options
Mode                        File                     Read/Write                Position
AM_READ                     Exists                   Read                      BoF
AM_WRITE                    New/overwrite            Write                     Beginning of file
AM_APPEND                   Exists                   Write                     EoF
AM_READ_PLUS                Exists                   Read and write            BoF
AM_WRITE_PLUS               New/overwrite            Read and write            BoF
AM_APPEND_PLUS              Exists, possibly new     Read and write            EoF
                        The inputs "IL_FileAsyncFileName" and "IL_FileAsyncMode" are applied at a
                        rising edge at the "IL_FileAsyncEnable" input. If the file could be opened or
                        created, the function block returns an access token at the "IL_FileAsyncFile‐
                        Handle” output. The output "IL_FileAsyncInOperation" becomes TRUE. If an
                        error occurs while opening, the "IL_FileAsyncError" output is set. The outputs
                        "IL_FileAsyncErrorID" and "IL_FileAsyncErrorIdent" provide information on the
                        error type.
                        The functions blocks can use the access node issued at the "IL_FileAsyncFile‐
                        Handle” output for the following operations:
                        ● IL_FileReadAsync - Reads from a file
                        ● IL_FileWriteAsync - Writes to a file
                        ● IL_FileGetPosAsync – Gets the current writing or reading position in the
                          file
                        ● IL_FileSeekAsync – Sets the current writing or reading position in the file
                        The “Active” output is set during file operation.

Troubleshooting:
The function block can output the following error codes:
Table 207: Error codes of the IL_FileAsync function block
ErrorID                   Additional1            Additional2           Description
OTHER_ERROR               16#0A0F0102            16#0C230001           Operation failed
INPUT_INVALID_ERR         16#0A0F0102            16#0C230002           Parameter invalid
OR
SYSTEM_ERROR              16#0A0F0102            16#0C230005           Operation takes too long
SYSTEM_ERROR              16#0A0F0102            16#0C23000A           Another file operation is still
                                                                       active
INPUT_INVALID_ERR 16#0A0F0102                    16#0C230014           "IL_FileAsyncFileHandle"
OR                                                                     invalid
RESOURCE_ERROR 16#0A0F0102                       16#0C230015           End of file reached

### 14.4.3 IL_FileReadAsync

Brief description
The function block IL_FileReadAsync reads data from an open file.

   Interface description

Table 208: Interface variables of the IL_FileReadAsync function block
                  Name            Type                                  Description
VAR_INPUT         Execute         BOOL                                  Rising edge starts the
                                                                        reading operation
                  BufferAddr      POINTER TO BYTE                       Pointer to reading buffer
                  BufferSize      UDINT                                 Size of reading buffer in
                                                                        bytes
                  FileHandle      ITF_FILEASYNC                         Access token
VAR_OUTPUT        Done            BOOL                                  Operation successful
                  Active          BOOL                                  File access active
                  Error           BOOL                                  An error occurred
                  ErrorID         ⮫ ERROR_CODE                          Error classification
                  ErrorIdent      ⮫ ERROR_STRUCT                        Error Diagnostics
                  BytesRead       UDINT                                 Number of read bytes

Table 209: Min./max. and default values of the IL_FileReadAsync function block inputs
Name         Type                Min. value     Max. value        Default        Applied
                                                                  value
Execute      BOOL            FALSE              TRUE              FALSE          Continuous
BufferAddr   POINTER TO BYTE 0                                    0              Rising edge at "Exe‐
                                                                                 cute"
BufferSize   UDINT               0              232-1             0              Rising edge at "Exe‐
                                                                                 cute"
FileHandle   ITF_FILEASYNC       0                                0              Rising edge at "Exe‐
                                                                                 cute"

   Functional description
   The function block IL_FileReadAsync reads data starting from the current posi‐
   tion of a file already opened with the IL_FileAsync function block. Data is
   stored in the buffer specified at the “BufferAddr“ input. Up to the number of
   bytes specified in "BufferSize” can be read. The file-internal position pointer is
   offset by the number of read bytes.
   Create the access token of the open file via the “FileHandle” input. The oper‐
   ation starts with a rising edge at the "Execute” input. The "Active" output is
   set during file access. After a successful access, the output is set to “Done”.
   If an error occurs during processing, the "Error" output is set. The outputs
   “ErrorID” and “ErrorIdent” contain more detailed information on the error.

    Troubleshooting:
    The function block can output the following error codes:
Table 210: Error codes of the IL_FileReadAsync function block
ErrorID            Additional1                     Additional2         Description
OTHER_ERROR        16#0A0F0102                     16#0C230001         Operation failed
INPUT_INVALID_ERRO 16#0A0F0102                     16#0C230002         Parameter invalid
R
SYSTEM_ERROR       16#0A0F0102                     16#0C230005         Operation takes too long
SYSTEM_ERROR       16#0A0F0102                     16#C2300006         No buffer storage specified
OTHER_ERROR        16#0A0F0102                     16#0C23000A         Another file operation is still
                                                                       active
RESOURCE_ERROR     16#0A0F0102                     16#0C23000F         Created data buffer too small
INPUT_INVALID_ERRO 16#0A0F0102                     16#0C230014         "FileHandle" invalid
R
RESOURCE_ERROR     16#0A0F0102                     16#0C230015         End of file reached

### 14.4.4 IL_FileWriteAsync

    Brief description
    The function block IL_FileWriteAsync writes data to an open file.

    Interface description

Table 211: Interface variables of the IL_FileWriteAsync function block
                    Name                    Type                            Description
VAR_INPUT           Execute                 BOOL                            Rising edge starts the
                                                                            writing operation
                    BufferAddr              POINTER TO BYTE                 Pointer to writing buffer
                    BufferSize              UDINT                           Number of writes to be
                                                                            written
                    FileHandle              ITF_FILEASYNC                   Access token
VAR_OUTPUT          Done                    BOOL                            Operation successful
                    Active                  BOOL                            File access active
                    Error                   BOOL                            An error occurred
                    ErrorID                 ⮫ ERROR_CODE                    Error classification
                    ErrorIdent              ⮫ ERROR_STRUCT                  Error Diagnostics
                    BytesWritten            UDINT                           Number of written bytes

Table 212: Min./max. and default values of the IL_FileWriteAsync function block inputs
Name             Type              Min. value   Max. value        Default value Applied
Execute          BOOL              FALSE        TRUE              FALSE         Continuous
BufferAddr       POINTER TO        0                              0             Rising edge at
                 BYTE                                                           "Execute"
BufferSize       UDINT             0            232-1             0             Rising edge at
                                                                                "Execute"
FileHandle       ITF_FILEASYNC 0                                  0             Rising edge at
                                                                                "Execute"

Functional description

The function block IL_FileWriteAsync writes data starting from the current
position to a file already opened with the IL_FileAsync function block. Data
to be written is created at the "BufferAddr” input. Up to the number of bytes
specified in "BufferSize” can be written.
The file-internal position pointer is offset by the number of written bytes.
Create the access token of the open file via the “FileHandle” input. The oper‐
ation starts with a rising edge at the "Execute” input. The "Active" output is
set during file access. After a successful access, the output is set to “Done”.
If an error occurs during processing, the "Error" output is set. The outputs
“ErrorID” and “ErrorIdent” contain more detailed information on the error.

Troubleshooting:
The function block can output the following error codes:
Table 213: Error codes of the IL_FileWriteAsync function block
ErrorID                      Additional1         Additional2          Description
OTHER_ERROR                  16#0A0F0102         16#0C230001          Operation failed
INPUT_INVALID_ERROR          16#0A0F0102         16#0C230002          Parameter invalid
SYSTEM_ERROR                 16#0A0F0102         16#0C230005          Operation takes too long
SYSTEM_ERROR                 16#0A0F0102         16#0C230006          No buffer storage specified
OTHER_ERROR                  16#0A0F0102         16#0C23000A          Another file operation is still
                                                                      active
RESOURCE_ERROR               16#0A0F0102         16#0C23000F          Created data buffer too
                                                                      small
INPUT_INVALID_ERROR 16#0A0F0102                  16#0C230014          "FileHandle" invalid
RESOURCE_ERROR      16#0A0F0102                  16#0C230015          End of file reached

### 14.4.5 IL_FileGetPosAsync

Brief description
The function block IL_FileGetPosAsync reads the position in the already open
file.

  Interface description

Table 214: Interface variables of the IL_FileGetPosAsync function block
                      Name                 Type                       Description
VAR_INPUT             Execute              BOOL                       Rising edge starts the operation
                      FileHandle           ITF_FILEASYNC              Access token
VAR_OUTPUT            Done                 BOOL                       Operation successful
                      Active               BOOL                       File access active
                      Error                BOOL                       An error occurred
                      ErrorID              ERROR_CODE                 Error classification
                      ErrorIdent           ERROR_STRUCT               Error Diagnostics
                      Position             UDINT                      Position in the file

Table 215: Min./max. and default values of the IL_FileGetPosAsync function block inputs
Name               Type             Min. value     Max. value     Default value Applied
Execute            BOOL             FALSE          TRUE           FALSE         Continuous
FileHandle         ITF_FILEASYNC    0                             0             Rising edge at "Exe‐
                                                                                cute"

  Functional description
  The function block IL_FileGetPosAsync reads the file-internal position pointer
  to a file already opened with the IL_FileAsync function block.
  Create the access token of the open file via the “FileHandle” input. The oper‐
  ation starts with a rising edge at the "Execute” input. The "Active" output is
  set during file access. After a successful access, the output is set to “Done”.
  If an error occurs during processing, the "Error" output is set. The outputs
  “ErrorID” and “ErrorIdent” contain more detailed information on the error.

  Troubleshooting:
The function block can output the following error codes:
Table 216: Error codes of the IL_FileGetPosAsync function block
ErrorID            Additional1                   Additional2          Description
OTHER_ERROR        16#0A0F0102                   16#0C230001          Operation failed
INPUT_INVALID_ERRO 16#0A0F0102                   16#0C230002          Parameter invalid
R
SYSTEM_ERROR       16#0A0F0102                   16#0C230005          Operation takes too long
OTHER_ERROR        16#0A0F0102                   16#0C23000A          Another file operation is still
                                                                      active
INPUT_INVALID_ERRO 16#0A0F0102                   16#0C230014          "FileHandle" invalid
R

ErrorID                  Additional1            Additional2           Description
RESOURCE_ERROR           16#0A0F0102            16#0C230015           End of file reached

### 14.4.6 IL_FileSeekAsync

  Brief description
  The function block IL_FileSeekAsync sets the position in the already open file.

  Interface description

Table 217: Interface variables of the IL_FileSeekAsync function block
                     Name                  Type                               Description
VAR_INPUT            Execute               BOOL                               Rising edge starts the
                                                                              operation
                     Position              UDINT                              New position in the file
                     FileHandle            ITF_FILEASYNC                      Access token
VAR_OUTPUT           Done                  BOOL                               Operation successful
                     Active                BOOL                               File access active
                     Error                 BOOL                               An error occurred
                     ErrorID               ⮫ ERROR_CODE                       Error classification
                     ErrorIdent            ⮫ ERROR_STRUCT                     Error Diagnostics

Table 218: Min./max. and default values of the IL_FileSeekAsync function block inputs
Name           Type                Min. value     Max. value         Default value    Applied
Execute        BOOL                FALSE          TRUE               FALSE            Continuous
Position       UDINT               0              232-1              0                Rising edge at
                                                                                      "Execute"
FileHandle     ITF_FILEASYNC       0                                 0                Rising edge at
                                                                                      "Execute"

  Functional description
  The function block IL_FileSeekAsync sets the file-internal position pointer to a
  file already opened with the IL_FileAsync function block.
  Create the access token of the open file via the “FileHandle” input. The oper‐
  ation starts with a rising edge at the "Execute” input. The "Active" output is
  set during file access. After a successful access, the output is set to “Done”.
  If an error occurs during processing, the "Error" output is set. The outputs
  “ErrorID” and “ErrorIdent” contain more detailed information on the error.

  Troubleshooting:
  The function block can output the following error codes:

Table 219: Error codes of the IL_FileSeekAsync function block
ErrorID          Additional1            Additional2        Description
OTHER_ERROR      16#0A0F0102            16#0C230001        Operation failed
INPUT_INVALID_ER 16#0A0F0102            16#0C230002        Parameter invalid
ROR
SYSTEM_ERROR     16#0A0F0102            16#0C230005        Operation takes
                                                           too long
OTHER_ERROR          16#0A0F0102        16#0C23000A        Another file opera‐
                                                           tion is still active
INPUT_INVALID_ER 16#0A0F0102            16#0C230014        "FileHandle"
ROR                                                        invalid
RESOURCE_ERRO 16#0A0F0102               16#0C230015        End of file reached
R

### 14.4.7 IL_FileCopyAsync

Brief description
The function block IL_FileCopyAsync copies an already existing file.

Interface description

Table 220: Interface variables of the IL_FileCopyAsync function block
                         Name                Type                             Description
VAR_INPUT                Execute             BOOL                             Rising edge starts the
                                                                              operation
                         SrcFile             STRING                           File to be copied
                         DestFile            STRING                           New file
VAR_OUTPUT               Done                BOOL                             Operation successful
                         Active              BOOL                             File access active
                         Error               BOOL                             An error occurred
                         ErrorID             ⮫ ERROR_CODE                     Error classification
                         ErrorIdent          ⮫ ERROR_STRUCT                   Error Diagnostics
                         BytesCopied         UDINT                            Number of copied bytes

Table 221: Min./max. and default values of the IL_FileCopyAsync function block inputs
Name               Type             Min. value      Max. value    Default value   Applied
Execute            BOOL             FALSE           TRUE          FALSE           Continuous
SrcFile            STRING                                         ´´              Rising edge at "Exe‐
                                                                                  cute"
DestFile           STRING                                         ´´              Rising edge at "Exe‐
                                                                                  cute"

   Functional description
   The function block IL_FileCopyAsync copies an already existing file. The oper‐
   ation starts with a rising edge at the "Execute” input. The "Active" output is
   set during file access. The “Done” output is set after the successful operation.
   If an error occurs during processing, the "Error" output is set. The outputs
   “ErrorID” and “ErrorIdent” contain more detailed information on the error.

   Troubleshooting:
  The function block can output the following error codes:
Table 222: Error codes of the IL_FileCopyAsync function block
ErrorID                  Additional1              Additional2          Description

OTHER_ERROR              16#0A0F0102              16#0C230001          Operation failed
INPUT_INVALID_ERRO       16#0A0F0102              16#0C230002          Parameter invalid
R
SYSTEM_ERROR             16#0A0F0102              16#0C230005          Operation takes too long
SYSTEM_ERROR             16#0A0F0102              16#0C23000A          Another file operation is still
                                                     active
RESOURCE_ERROR           16#0A0F0102              16#0C230010          File does not exist
RESOURCE_ERROR           16#0A0F0102              16#0C230012          File already exists

### 14.4.8 IL_FileRenameAsync

   Brief description
   The function block IL_FileRenameAsync renames an already existing file or
   moves it to a new directory.

   Interface description

Table 223: Interface variables of the IL_FileRenameAsync function block
                  Name                   Type                               Description
VAR_INPUT         Execute                BOOL                               Rising edge starts the
                                                                            operation
                  OldName                STRING                             File to be moved
                  NewName                STRING                             New file name
VAR_OUTPUT        Done                   BOOL                               Operation successful
                  Active                 BOOL                               File access active
                  Error                  BOOL                               An error occurred
                  ErrorID                ⮫ ERROR_CODE                       Error classification
                  ErrorIdent             ⮫ ERROR_STRUCT                     Error Diagnostics

Table 224: Min./max. and default values of the IL_FileRenameAsync function block inputs
Name           Type           Min. value        Max. value   Default value     Applied
Execute        BOOL           FALSE             TRUE         FALSE             Continuous
OldName        STRING                                        ´´                Rising edge at "Execute"
NewName        STRING                                        ´´                Rising edge at "Execute"

     Functional description
     The function block IL_FileRenameAsync renames an already existing file or
     moves it to a new directory. The "Active" output is set during file access. The
     “Done” output is set after the successful operation. If an error occurs during
     processing, the "Error" output is set. The outputs “ErrorID” and “ErrorIdent”
     contain more detailed information on the error.

     Troubleshooting:
 The function block can output the following error codes:
Table 225: Error codes of the IL_FileRenameAsync function block
ErrorID             Additional1                      Additional2             Description
OTHER_ERROR         16#0A0F0102                      16#0C230001             Operation failed
INPUT_INVALID_ERROR 16#0A0F0102                      16#0C230002             Parameter invalid
SYSTEM_ERROR        16#0A0F0102                      16#0C230005             Operation takes too long
SYSTEM_ERROR        16#0A0F0102                      16#0C23000A             Another file operation is
                                                                             still active
RESOURCE_ERROR              16#0A0F0102              16#0C230010             File does not exist
RESOURCE_ERROR              16#0A0F0102              16#0C230012             File already exists

### 14.4.9 IL_FileDeleteAsync

     Brief description
     The function block IL_FileDeleteAsync deletes an existing file.

     Interface description

Table 226: Interface variables of the IL_FileDeleteAsync function block
                   Name                     Type                              Description
VAR_INPUT          Execute                  BOOL                              Rising edge starts the
                                                                              operation
                   FileName                 STRING                            File to be deleted
VAR_OUTPUT         Done                     BOOL                              Operation successful
                   Active                   BOOL                              File access active
                   Error                    BOOL                              An error occurred
                   ErrorID                  ⮫ ERROR_CODE                      Error classification

Name                   Type                             Description
ErrorIdent             ⮫ ERROR_STRUCT                   Error Diagnostics

Table 227: Min./max. and default values of the IL_FileDeleteAsync function block inputs
Name         Type            Min. value      Max. value    Default value    Applied
Execute      BOOL            FALSE           TRUE          FALSE            Continuous
FileName     STRING                                        ´´               Rising edge at "Execute"

  Functional description
  The function block IL_FileDeleteAsync deletes an existing file. The "Active"
  output is set during file access. The “Done” output is set after the successful

  operation. If an error occurs during processing, the "Error" output is set. The
  outputs “ErrorID” and “ErrorIdent” contain more detailed information on the
  error.

  Troubleshooting:
 The function block can output the following error codes:
Table 228: Error codes of the IL_FileDeleteAsync function block
ErrorID            Additional1                   Additional2          Description
OTHER_ERROR        16#0A0F0102                   16#0C230001          Operation failed
INPUT_INVALID_ERRO 16#0A0F0102                   16#0C230002          Parameter invalid
R
SYSTEM_ERROR       16#0A0F0102                   16#0C230005          Operation takes too long
SYSTEM_ERROR       16#0A0F0102                   16#0C23000A          Another file operation is still
                                                                      active
RESOURCE_ERROR          16#0A0F0102              16#0C230010          File does not exist

### 14.4.10 IL_FileGetSizeAsync

  Brief description
  The function block IL_FileGetSizeAsync determines the size of a file in bytes.

  Interface description

Table 229: Interface variables of the IL_FileGetSizeAsync function block
                   Name             Type                                   Description
VAR_INPUT          Execute          BOOL                                   Rising edge starts the
                                                                           operation
                   FileName         STRING                                 File name
VAR_OUTPUT         Done             BOOL                                   Operation successful
                   Active           BOOL                                   File access active

Name              Type                                      Description
Error             BOOL                                      An error occurred
ErrorID           ⮫ ERROR_CODE                              Error classification
ErrorIdent        ⮫ ERROR_STRUCT                            Error Diagnostics
FileSize          UDINT                                     File size in bytes

Table 230: Min./max. and default values of the IL_FileGetSizeAsync function block inputs
Name               Type           Min. value     Max. value      Default value     Applied
Execute            BOOL           FALSE          TRUE            FALSE             Continuous
FileName           STRING                                        ´´                Rising edge at "Exe‐
                                                                                   cute"

   Functional description
   The function block IL_FileGetSizeAsync determines the size of a file in bytes.
   The "Active" output is set during file access. The “Done” output is set after the
   successful operation. The file size in bytes is output at the "FileSize” output.
   If an error occurs during processing, the "Error" output is set. The outputs
   “ErrorID” and “ErrorIdent” contain more detailed information on the error.

   Troubleshooting:
The function block can output the following error codes:
Table 231: Error codes of the IL_FileGetSizeAsync function block
ErrorID                  Additional1             Additional2           Description
OTHER_ERROR              16#0A0F0102             16#0C230001           Operation failed
INPUT_INVALID_ERR        16#0A0F0102             16#0C230002           Parameter invalid
OR
SYSTEM_ERROR             16#0A0F0102             16#0C230005           Operation takes too long
SYSTEM_ERROR             16#0A0F0102             16#0C23000A           Another file operation is still
                                                                       active
RESOURCE_ERROR           16#0A0F0102             16#0C230010           File does not exist

### 14.4.11 IL_FileGetTimeAsync

   Brief description
   The function block IL_FileGetTimeAsync determines the creation time, modifi‐
   cation time and the last access time of a file.

   Interface description

Table 232: Interface variables of the IL_FileGetTimeAsync function block
                  Name             Type                                 Description
VAR_INPUT         Execute          BOOL                                 Rising edge starts the oper‐
                                                                        ation
                  FileName         STRING                               File name
VAR_OUTPUT        Done             BOOL                                 Operation successful
                  Active           BOOL                                 File access active
                  Error            BOOL                                 An error occurred
                  ErrorID          ⮫ ERROR_CODE                         Error classification
                  ErrorIdent       ⮫ ERROR_STRUCT                       Error Diagnostics

FileTime         IL_DIR_FILE_TIME                     Determined times

Table 233: Min./max. and default values of the IL_FileGetTimeAsync function block inputs
Name          Type             Min. value   Max. value      Default value    Applied
Execute       BOOL             FALSE        TRUE            FALSE            Continuous
FileName      STRING                                        ´´               Rising edge at "Exe‐
                                                                             cute"

   Functional description
   The function block IL_FileGetTimeAsync determines the creation time, modifi‐
   cation time and the last access time of a file. The "Active" output is set during
   file access. The “Done” output is set after the successful operation. The times
   are output in a structure at the "FileTime” output. If an error occurs during
   processing, the "Error" output is set. The outputs “ErrorID” and “ErrorIdent”
   contain more detailed information on the error.

   Troubleshooting:
  The function block can output the following error codes:
Table 234: Error codes of the IL_FileGetTimeAsync function block
ErrorID                Additional1            Additional2          Description
OTHER_ERROR            16#0A0F0102            16#0C230001          Operation failed
INPUT_INVALID_ERR      16#0A0F0102            16#0C230002          Parameter invalid
OR
SYSTEM_ERROR           16#0A0F0102            16#0C230005          Operation takes too long
SYSTEM_ERROR           16#0A0F0102            16#0C23000A          Another file operation is still
                                                                   active
RESOURCE_ERROR         16#0A0F0102            16#0C230010          File does not exist

## 14.5 Directory access

### 14.5.1 Introduction and overview

   The operations for directories are divided into changing accesses, read-only
   accesses and accesses to set the current path.
   Change the directories using the following operations:
   ● IL_DirCreateAsync - Creates a new directory
   ● IL_DirDeleteAsync - Deletes an existing directory
   ● IL_DirRenameAsync - Renames a directory or moves it
   Use the following operations for the read-only access:
   ● IL_DirReadAsync - Reads the content of a directory
   ● IL_DirGetCurrentAsync - Outputs the current directory path

 Change the access path using the following operations:
 ● IL_DirSetCurrentAsync - Sets the active directory

### 14.5.2 IL_DirCreateAsync

 Brief description
 The function block IL_DirCreateAsync creates a new directory.

 Interface description

Table 235: Interface variables of the IL_DirCreateAsync function block
                       Name                 Type                          Description
VAR_INPUT              Execute              BOOL                          Rising edge starts the oper‐
                                                                          ation
                       DirName              STRING                        Directory to be created
VAR_OUTPUT             Done                 BOOL                          Operation successful
                       Active               BOOL                          File access active
                       Error                BOOL                          An error occurred
                       ErrorID              ⮫ ERROR_CODE                  Error classification
                       ErrorIdent           ⮫ ERROR_STRUCT                Error Diagnostics

Table 236: Min./max. and default values of the IL_DirCreateAsync function block inputs
Name               Type          Min. value      Max. value    Default value   Applied
Execute            BOOL          FALSE           TRUE          FALSE           Continuous
DirName            STRING                                      ´´              Rising edge at "Exe‐
                                                                               cute"

 Functional description
 The function block IL_DirCreateAsync creates a new directory. The "Active"
 output is set during file access. The “Done” output is set after the successful
 operation. If an error occurs during processing, the "Error" output is set. The
 outputs “ErrorID” and “ErrorIdent” contain more detailed information on the
 error.

 Troubleshooting:
The function block can output the following error codes:
Table 237: Error codes of the IL_DirCreateAsync function block
ErrorID            Additional1                       Additional2       Description
OTHER_ERROR        16#0A0F0102                       16#0C230001       Operation failed
INPUT_INVALID_ERRO 16#0A0F0102                       16#0C230002       Parameter invalid
R
SYSTEM_ERROR       16#0A0F0102                       16#0C230005       Operation takes too long

ErrorID                 Additional1             Additional2         Description
SYSTEM_ERROR            16#0A0F0102             16#0C23000A         Another file operation is still
                                               active
RESOURCE_ERROR          16#0A0F0102             16#0C230012         Directory already exists

### 14.5.3 IL_DirDeleteAsync

Brief description
The function block IL_DirDeleteAsync deletes an existing directory.

Interface description

Table 238: Interface variables of the IL_DirDeleteAsync function block
                     Name                Type                            Description
VAR_INPUT            Execute             BOOL                            Rising edge starts the
                                                                         operation
                     DirName             STRING                          Directory to be deleted
VAR_OUTPUT           Done                BOOL                            Operation successful
                     Active              BOOL                            File access active
                     Error               BOOL                            An error occurred
                     ErrorID             ⮫ ERROR_CODE                    Error classification
                     ErrorIdent          ⮫ ERROR_STRUCT                  Error Diagnostics

Table 239: Min./max. and default values of the IL_DirDeleteAsync function block inputs
Name          Type             Min. value     Max. value      Default value    Applied
Execute       BOOL             FALSE          TRUE            FALSE            Continuous
DirName       STRING                                          ´´               Rising edge at "Exe‐
                                                                               cute"

Functional description
The function block IL_DirDeleteAsync deletes an existing directory. The
"Active" output is set during file access. The “Done” output is set after the
successful operation. If an error occurs during processing, the "Error" output
is set. The outputs “ErrorID” and “ErrorIdent” contain more detailed informa‐
tion on the error.

Troubleshooting:
The function block can output the following error codes:
Table 240: Error codes of the IL_DirDeleteAsync function block
ErrorID                Additional1            Additional2            Description
OTHER_ERROR            16#0A0F0102            16#0C230001            Operation failed

ErrorID                     Additional1         Additional2            Description
INPUT_INVALID_ERR           16#0A0F0102         16#0C230002            Parameter invalid
OR
SYSTEM_ERROR                16#0A0F0102         16#0C230005            Operation takes too long
SYSTEM_ERROR                16#0A0F0102         16#0C23000A            Another file operation is still
                                                  active
RESOURCE_ERROR              16#0A0F0102         16#0C230010            Directory not available

### 14.5.4 IL_DirRenameAsync

  Brief description
  The function block IL_DirRenameAsync renames a directory or moves it.

  Interface description

Table 241: Interface variables of the IL_DirRenameAsync function block
                     Name              Type                             Description
VAR_INPUT            Execute           BOOL                             Rising edge starts the oper‐
                                                                        ation
                     OldDir            STRING                           Original directory name
                     NewDir            STRING                           New directory name
VAR_OUTPUT           Done              BOOL                             Operation successful
                     Active            BOOL                             File access active
                     Error             BOOL                             An error occurred
                     ErrorID           ⮫ ERROR_CODE                     Error classification
                     ErrorIdent        ⮫ ERROR_STRUCT                   Error Diagnostics

Table 242: Min./max. and default values of the IL_DirRenameAsync function block inputs
Name               Type           Min. value    Max. value    Default value   Applied
Execute            BOOL           FALSE         TRUE          FALSE           Continuous
OldDir             STRING                                     ´´              Rising edge at "Exe‐
                                                                              cute"
NewDir             STRING                                     ´´              Rising edge at "Exe‐
                                                                              cute"

  Functional description
  The function block IL_DirRenameAsync renames a directory or moves it. The
  "Active" output is set during file access. The “Done” output is set after the
  successful operation. If an error occurs during processing, the "Error" output
  is set. The outputs “ErrorID” and “ErrorIdent” contain more detailed informa‐
  tion on the error.

 Troubleshooting:
 The function block can output the following error codes:
Table 243: Error codes of the IL_DirRenameAsync function block
ErrorID            Additional1                  Additional2           Description
OTHER_ERROR        16#0A0F0102                  16#0C230001           Operation failed
INPUT_INVALID_ERRO 16#0A0F0102                  16#0C230002           Parameter invalid
R
SYSTEM_ERROR       16#0A0F0102                  16#0C230005           Operation takes too long
SYSTEM_ERROR       16#0A0F0102                  16#0C23000A           Another file operation is still
                                                                      active
RESOURCE_ERROR          16#0A0F0102             16#0C230010           File does not exist

RESOURCE_ERROR          16#0A0F0102             16#0C230012           File already exists

### 14.5.5 IL_DirGetCurrentAsync

 Brief description
 The function block IL_DirGetCurrentAsync reads the active directory.

 Interface description

Table 244: Interface variables of the IL_DirGetCurrentAsync function block
                    Name             Type                                 Description
VAR_INPUT           Execute          BOOL                                 Rising edge starts the
                                                                          operation
VAR_OUTPUT          Done             BOOL                                 Operation successful
                    Active           BOOL                                 File access active
                    Error            BOOL                                 An error occurred
                    ErrorID          ⮫ ERROR_CODE                         Error classification
                    ErrorIdent       ⮫ ERROR_STRUCT                       Error Diagnostics
                    DirName          STRING                               Active directory

Table 245: Min./max. and default values of the IL_DirGetCurrentAsync function block inputs
Name          Type            Min. value      Max. value      Default value       Applied
Execute       BOOL            FALSE           TRUE            FALSE               Continuous

 Functional description
 The function block IL_DirGetCurrentAsnyc reads the active directory. All file
 operations are relative to the specified directory path. The "Active" output is
 set during file access. The “Done” output is set after the successful operation.
 If an error occurs during processing, the "Error" output is set. The outputs
 “ErrorID” and “ErrorIdent” contain more detailed information on the error.

Troubleshooting:
The function block can output the following error codes:
Table 246: Error codes of the IL_DirGetCurrentAsync function block
ErrorID                 Additional1                 Additional2             Description
SYSTEM_ERROR            16#0A0F0102                 16#0C230005             Operation takes too long
SYSTEM_ERROR            16#0A0F0102                 16#0C23000A             Another file operation is
                                                                            still active

### 14.5.6 IL_DirSetCurrentAsync

Brief description
The function block IL_DirSetCurrentAsnyc sets the active directory.

Interface description

Table 247: Interface of the IL_DirSetCurrentAsync function block
                     Name                    Type                           Description
VAR_INPUT            Execute                 BOOL                           Rising edge starts the
                                                                            operation
                     DirName                 STRING                         New active directory
VAR_OUTPUT           Done                    BOOL                           Operation successful
                     Active                  BOOL                           File access active
                     Error                   BOOL                           An error occurred
                     ErrorID                 ⮫ ERROR_CODE                   Error classification
                     ErrorIdent              ⮫ ERROR_STRUCT                 Error Diagnostics

Table 248: Min./max. and default values of the IL_DirSetCurrentAsync function block inputs
Name           Type          Min. value       Max. value    Default value     Applied
Execute        BOOL          FALSE            TRUE          FALSE             Continuous
DirName        STRING                                       ´´                Rising edge at "Exe‐
                                                                              cute"

Functional description
The function block IL_DirSetCurrentAsnyc sets the active directory. All other
file operations are relative to the specified directory path. The "Active" output
is set during file access. The “Done” output is set after the successful oper‐
ation. If an error occurs during processing, the "Error" output is set. The
outputs “ErrorID” and “ErrorIdent” contain more detailed information on the
error.

Troubleshooting:
The function block can output the following error codes:

Table 249: Error codes of the IL_DirSetCurrentAsync function block
ErrorID             Additional1                      Additional2          Description
OTHER_ERROR         16#0A0F0102                      16#0C230001          Operation failed
INPUT_INVALID_ERROR 16#0A0F0102                      16#0C230002          Parameter invalid
SYSTEM_ERROR        16#0A0F0102                      16#0C230005          Operation takes too long
SYSTEM_ERROR        16#0A0F0102                      16#0C23000A          Another file operation is
                                                                          still active
RESOURCE_ERROR               16#0A0F0102             16#0C230010          File does not exist

### 14.5.7 IL_DirReadAsync

  Brief description

  The function block IL_DirReadAsync reads the content of a directory.

  Interface description

Table 250: Interface variables of the IL_DirReadAsync function block
                   Name                Type                                  Description
VAR_INPUT          Enable              BOOL                                  Rising edge opens direc‐
                                                                             tory
                   DirName             STRING                                New active directory
                   ReadNext            BOOL                                  Reads next entry
VAR_OUTPUT         InOperation         BOOL                                  Operation successful
                   Active              BOOL                                  File access active
                   Error               BOOL                                  An error occurred
                   ErrorID             ⮫ ERROR_CODE                          Error classification
                   ErrorIdent          ⮫ ERROR_STRUCT                        Error Diagnostics
                   EntryCnt            UDINT                                 Number of entries in the
                                                                             directory
                   DirEntry            IL_DIR_INFO                           Current directory entry

Table 251: Min./max. and default values of the IL_DirReadAsync function block inputs
Name          Type             Min. value       Max. value   Default value    Applied
Execute       BOOL             FALSE            TRUE         FALSE            Continuous
DirName       STRING                                         ´´               Rising edge at "Enable"
ReadNext      BOOL             FALSE            TRUE         FALSE            Continuous if “Enable”
                                                                              is TRUE

Functional description
The function block IL_DirReadAsync reads the content of a directory. The
function block is enabled at a rising edge at "Enable”. The output "DirEntry”
becomes TRUE after opening the directory. The number of entries is output
at the "EntryCnt" output. The first entry is already present at the "DirEntry”
output. Each rising edge at the “ReadNext” input outputs another entry at the
“DirEntry” output. The "Active" output is set during reading access. If an error
occurs during processing, the "Error" output is set. The outputs “ErrorID” and
“ErrorIdent” contain more detailed information on the error.

Troubleshooting:
The function block can output the following error codes:
Table 252: Error codes of the IL_DirReadAsync function block
ErrorID            Additional1                   Additional2          Description
OTHER_ERROR        16#0A0F0102                   16#0C230001          Operation failed
INPUT_INVALID_ERRO 16#0A0F0102                   16#0C230002          Parameter invalid
R
SYSTEM_ERROR       16#0A0F0102                   16#0C230005          Operation takes too long
SYSTEM_ERROR       16#0A0F0102                   16#0C230006          No buffer storage specified
OTHER_ERROR        16#0A0F0102                   16#0C23000A          Another file operation is still
                                                                      active
RESOURCE_ERROR           16#0A0F0102             16#0C230010          Directory does not exist
RESOURCE_ERROR           16#0A0F0102             16#0C230015          End of directory reached

## 14.6 Data types

### 14.6.1 IL_DIR_INFO (ENUM)

Table 253: Data type IL_DIR_INFO (ENUM)
Name                   Type                      Note
EntryName              STRING                    File name or directory name
EntrySize              UDINT                     File size
EntryTime              IL_DIR_FILE_TIME          Creation time, modification time and access time
EntryType              IL_DIR_ENTRY_TYPE         FILE or DIR

### 14.6.2 IL_DIR_FILE_ASYNCSTATE (ENUM)

Table 254: Data type IL_DIR_FILE_ASYNCSTATE (ENUM)
Name                               Value              Note
ASYNCSTATE_INVALID                 16#FFFFFFFF        Task invalid
ASYNCSTATE_PENDING                 0                  Task is waiting for processing
ASYNCSTATE_ACTIVE                  1                  Task is processed
ASYNCSTATE_READY                   2                  Task was executed successfully
ASYNCSTATE_ERROR                   3                  Task was completed with error
ASYNCSTATE_TIMEOUT                 4                  Task takes too long

### 14.6.3 IL_DIR_ENTRY_TYPE (ENUM)

Table 255: Data type IL_DIR_ENTRY_TYPE (ENUM)
Name                                 Value                           Note
FILE                                 0                               Entry is a file
DIRECTORY                            2                               Entry is a directory

### 14.6.4 IL_DIR_FILE_TIME (STRUCT)

Table 256: Data type IL_DIR_FILE_TIME (STRUCT)
Name                              Type                               Note
Creation                          DT                                 Creation time
LastAccess                        DT                                 Time of the last access
LastModification                  DT                                 Time of the last change

### 14.6.5 IL_FILE_ACCESS_MODE (ENUM)

Table 257: Data type IL_FILE_ACCESS_MODE (ENUM)
Name                     Comment

AM_READ                  Open a file for the read-only access. If the file does not exist, access fails
AM_WRITE                 Creates a new file for write access. The file already exists, it is emptied
AM_APPEND                Open a file for the adding write access. If the file does not exist, access
fails
AM_READ_PLUS             Open a file for the read-only and write access. If the file does not exist,
access fails
AM_WRITE_PLUS            Creates a new file for the read-only and write access. The file already
exists, it is emptied
AM_APPEND_PLUS           Open a file for the adding write access. If the file does not yet exist, it is
created

## 14.7 Error codes

### 14.7.1 Error codes of the CXA_Table for the CXA_FileAsync

Table 258: Error codes of the CXA_Table for the CXA_FileAsync
ErrorID                           Additional2              Description
OTHER_ERROR                       16#0C230001              General internal error
INPUT_INVALID_ERROR               16#0C230002              Invalid parameters
RESOURCE_ERROR                    16#0C230003              Component not initialized.
OTHER ERROR                       16#0C230004              Version conflict
OTHER ERROR                       16#0C230005              Operation not completed in time
RESOURCE_ERROR                    16#0C230006              Created data buffer too small
SYSTEM_ERROR                      16#0C23000B              Too much tasks to be processed
SYSTEM_ERROR                      16#0C23000C              Function not implemented
RESOURCE_ERROR                    16#0C23000D              No object found with this number
SYSTEM_ERROR                      16#0C23000E              Integer overflow
RESOURCE_ERROR                    16#0C23000F              The buffer size is too small.
RESOURCE_ERROR                    16#0C230010              No object found with this name
RESOURCE_ERROR                    16#0C230011              No heap memory available
RESOURCE_ERROR                    16#0C230012              There is an object with the same name
RESOURCE_ERROR                    16#0C230013              Memory overflow
INPUT_INVALID_ERROR               16#0C230014              Invalid handle
INPUT_INVALID_ERROR               16#0C230017              Invalid interface
SYSTEM_ERROR                      16#0C230018              Unsupported functionality
ACCESS_ERROR                      16#0C230019              No access rights
RESOURCE_ERROR                    16#0C23001A              Resource limits exceeded
RESOURCE_ERROR                    16#0C23001B              Buffer too small. Not all entries are sent.
RESOURCE_ERROR                    16#0C23001C              Invalid session number

ErrorID                            Additional2         Description
SYSTEM_ERROR                       16#0C23001D         Exception
SYSTEM_ERROR                       16#0C23001E         Function signature does not match
SYSTEM_ERROR                       16#0C23001F         Version number does not match
SYSTEM_ERROR                       16#0C230020         Types does not match
SYSTEM_ERROR                       16#0C230021         ID does not match
SYSTEM_ERROR                       16#0C230022         Consistency error
SYSTEM_ERROR                       16#0C230023         No communication cycle required
SYSTEM_ERROR                       16#0C230024         A task cannot be closed after an excep‐
                                  tion
ACCESS_ERROR                       16#0C230025         Memory could not be locked
SYSTEM_ERROR                       16#0C230026         No license
ACCESS_ERROR                       16#0C230027         Operation denied
DEVICE_ERROR                       16#0C230028         Device error
DEVICE_ERROR                       16#0C230029         Storage medium full
DEVICE_ERROR                       16#0C230030         Internal runtime error
DEVICE_ERROR                       16#0C230031         Internal runtime error
DEVICE_ERROR                       16#0C230032         File access error, e.g. file is write-pro‐
                                  tected
DEVICE_ERROR                       16#0C230033         No free retain memory
DEVICE_ERROR                       16#0C230034         Fallen below lower limit of the resource
DEVICE_ERROR                       16#0C230035         Upper limit of the resource exceeded
INPUT_ INVALID _ERROR              16#0C230036         Size does not match
OTHER_ERROR                        16#0C230039         Security check failed
OTHER_ERROR                        16#0C23003A         Incorrect calling sequence
INPUT_ INVALID _ERROR              16#0C23003B         Invalid IEC reference
OTHER_ERROR                        16#0C23003C         Error during string conversion
