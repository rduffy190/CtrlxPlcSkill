# 11 CXAC_Diagnostics

## 11.1 Introduction and overview

The CXAC_Diagnostics library provides functions to issue diagnostics from the
PLC program to the ctrlX CORE logbook.
The following functions are provided to the user:
● ⮫ RegisterDiagnostics
  Registering diagnostics
● ⮫ UnregisterDiagnostics
  Logging off diagnostics

● ⮫ SetDiagnostics
  Issuing diagnostics to the logbook/pending diagnostics
● ⮫ ResetDiagnostics
  Resetting pending diagnostics
● ⮫ ClearDiagnostics
  Deleting pending diagnostics
● ⮫ ClearAllPendingDiagnostics
  Resetting and deleting all pending diagnostics
● ⮫ GetPendingDiagnostics
  Reading out up to 64 pending diagnostics

The diagnostics from the PLC program are based on the ctrlX diagnostic
system.
For more information, refer to: ⮫ ctrlX Diagnostic System

## 11.2 RegisterDiagnostics

The RegisterDiagnostics function is used to register own diagnostics.

Example

VAR
  MyResult: CXA_Diagnostics.DIAG_RESULT;
END_VAR

  MyResult:=RegisterDiagnostics(JsonFile:='Example_diagnostics_en-US.json');

Functional description
Own diagnostics can be registered using a JSON file. The user has to transfer
it to the ctrlX CORE (into the "Applications" directory).
Two example JSON files are already available in the library.

All diagnostics in the example "alreadyRegisteredExample.json" are already
registered in the Runtime. Thus, a registration is not required.

Qualitative example:

{
    "language": "en-us",
    "product": "XCR-V-0118",
    "component": "plc.iec",
    "mainDiagnostics": {
        "0E0F0815": {
        "text": "Some error",
        "version": 1,
        "detailedDiagnostics": {
        "00000001": {
           "text": "Error 1",
        "version": 1},
        "00000002": {
        "text": "Error 2",
        "version": 1 }
        }
        },
      "0E0E0815": {
      "text": "Some Warning",
      "version": 1,
      "detailedDiagnostics": {
             "00000001": {
        "text": "Warning 1",

"version": 1 },
"00000002": {
  "text": "Warning 2",
"version": 1 }
  }
},
"0E0A0815": {
"text": "Some Message",
"version": 1,
"detailedDiagnostics": {
   "00000001": {
   "text": "Note 1",
   "version": 1 },
 "00000002": {
 "text": "Note 2",
   "version": 1 }
   }
}
}
}

Already registered diagnostics:

{
"language": "en-us",
"product": "XCR-V-0110",
"component": "plc.iec",
"mainDiagnostics": {
"0A0F0000": {
"text": "PLC error",
"version": 1,
"detailedDiagnostics": {
"00220000": {
   "text": "PLC error",
"version": 1}
}
},
"0A0A0001": {
"text": "PLC Log info",
"version": 1
},
"0A0E0001": {
"text": "PLC Log warning",
"version": 1
},
"0A0F0001": {
"text": "PLC Log error",
"version": 1
},
"0A0F0002": {
"text": "PLC Log exception",
"version": 1
},
"0A0A0115": {
"text": "PLC IEC info",
"version": 1
},
"0A0E0115": {
"text": "PLC IEC warning",
"version": 1
},
"0A0F0115": {
"text": "PLC IEC error",
"version": 1
},
"0A0F2115": {
"text": "PLC IEC F2-error -> stop single axis",
"version": 1
},
"0A0F6115": {
"text": "PLC IEC F6-error -> stop all axis",
"version": 1

        },
        "0A0F8115": {
        "text": "PLC IEC F8-error -> system error/stop the app",
        "version": 1
        },
        "0A0F9115": {
        "text": "PLC IEC F9-error -> system error/stop whole system",
        "version": 1
        }
    }
}

For more information on the structure of the JSON file, refer to⮫ Structure of
the JSON file.

Use the PLC Engineering to copy the JSON file to the ctrlX CORE.

Additional information
● To register three diagnostics ,approx. 500-800 microseconds are required
  on the ctrlX CORE X3 control (ARM64)
● Diagnostics registered on thectrlX CORE cannot be overwritten (only a
  newer version can be registered)
● Multilingualism is currently not supported.
  However, when issuing diagnostics, the dynamic text can be issued in any
  language

## 11.3 UnregisterDiagnostics

Brief description
The UnregisterDiagnostics function is used to log off diagnostics.

Functional description
Logging off diagnostic messages using a JSON file analog to logging in. For
this purpose, the existing JSON file (example in chapter ⮫ RegisterDiagnos‐
tics) used to register the diagnostic messages should be used. The format
described in chapter ⮫ RegisterDiagnostics is again used here.
After calling the function block and specifying the path of the JSON file, the
specified diagnostic messages are no longer registered. The corresponding
error for unregistered diagnostic messages is output when the messages are
set.

## 11.4 SetDiagnostics

Brief description
The SetDiagnostics function is used to issue diagnostics.

Functional description
When calling the function, MainDiagnosticCode, DetailedDiagnosticCode,
DynamicDescription and Entity(IEC_Diagnostics) are transferred.
The entity can be freely selected by the user (e.g. name of the company) to
clearly assign the diagnostics.
If an error is to be reset immediately when issued, the input (VAR_INPUT)
"Reset" can be set to TRUE.

Example of issuing a diagnostics

VAR
  MyDiagnostics : IEC_Diagnostics;
  MyResult: CXA_Diagnostics.DIAG_RESULT;
END_VAR
MyDiagnostics.MainDiagnosticCode := 16#0A0F0115; // Plc iec error
MyDiagnostics.DetailedDiagnosticCode := 0;
MyDiagnostics.DynamicDescription := 'this is a plc-error-diagnostics';
MyDiagnostics.Entity := 'BoschRexroth';
SetDiagnostics(IecDiag:=MyDiagnostics, Reset :=FALSE );

## 11.5 ResetDiagnostics

The ResetDiagnostics function is used to reset pending diagnostics.

Functional description
Pending diagnostic messages can be reset by specifying MainDiagnostic‐
Code, DetailedDiagnosticCode (if available) and the entity ("green check" for
pending diagnostics).

Example of a reset of a pending diagnostics

VAR
  MyPendingDiagnostics : Pending_Diagnostics;
  MyResult: CXA_Diagnostics.DIAG_RESULT;
END_VAR
MyPendingDiagnostics.MainDiagnosticCode := 16#0A0F0115; // Plc iec error
MyPendingDiagnostics.DetailedDiagnosticCode := 0;
MyPendingDiagnostics.Entity := 'BoschRexroth';
MyResult:=ResetDiagnostics(IecDiag:= MyPendingDiagnostics );

## 11.6 ClearDiagnostics

The ClearDiagnostics function is used to clear all pending diagnostics.

Functional description
After pending diagnostics have been reset, these diagnostics can be deleted
with ClearDiagnostics.
(This removes the entry from the pending diagnostics, the entry in the log‐
book remains)

## 11.7 ClearAllPendingDiagnostics

The ClearAllPendingDiagnostics function is used to reset and delete all
pending diagnostics.

Functional description
When using this function, all pending diagnostics are automatically queried,
individually reset if necessary and then deleted.
If further diagnostic messages occur during the deletion, these are not
deleted.
Only diagnostics - pending when the function is called - are deleted.

## 11.8 GetPendingDiagnostics

Brief description
The GetPendingDiagnostics function is used to read out pending diagnostics.

Functional description
The output parameter "PendingElements" provides the number of existing
pending diagnostics.
Up to 64 diagnostics can be entered into the "PendingDiagnosticsList". If
there are more than 64 pending diagnostics, only the first 64 are read out
from the list.

Example

VAR
ReadPendingList : ARRAY [0..63] OF Pending_Diagnostics;
MyPendingElements : WORD;
END_VAR
GetPendingDiagnostics(PendingElements=>MyPendingElements,
PendingDiagnosticsList=>ReadPendingList );
