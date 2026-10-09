# 5 Standard64

## 5.1 Introduction and overview

The "Standard64" library extends the known⮫ "Standard" library with func‐
tions and function blocks that use the ⮫ WSTRING and ⮫ LTIME data types.

String functions (text processing functions)
●   ⮫ WCONCAT
●   ⮫ WDELETE
●   ⮫ WFIND
●   ⮫ WINSERT
●   ⮫ WLEFT
●   ⮫ WLEN
●   ⮫ WMID
●   ⮫ WREPLACE
●   ⮫ WRIGHT

Timer (time intervals)
● ⮫ LTOF Time interval with switch-off delay
● ⮫ LTON Time interval with switch-on delay
● ⮫ LTP pulse encoder with presettable pulse width

## 5.2 WCONCAT

Brief description
The WCONCAT function of type WSTRING returns the concatenation of two
character strings:
Character string STR2 is attached to character string STR1, the total string is
output.

      Interface description

Table 1: Interface variables of the WCONCAT function
I/O type       Name              Data type       Description
VAR_INPUT      STR1              WSTRING(255)    First substring

STR2              WSTRING(255)    Second substring
RETURN         WCONCAT           WSTRING(255)    Return value: Total string

      Example

## 5.3 WDELETE

      Brief description
      The function WDELETE of type ⮫ WSTRING deletes a substring of length LEN
      from a larger total string STR starting at a given position POS.

      Interface description

Table 2: Interface variables of the WDELETE function
I/O type       Name              Data type    Description
VAR_INPUT      STR               WSTRING(255) Total string
               LEN               INT          Number of characters to be deleted
               POS               INT          Position in STR from which LEN characters are
                                              deleted to the right
RETURN         WDELETE           WSTRING(255) Return value: remaining character string

Example

## 5.4 WFIND

Brief description
The function WFIND of type INT browses for the position of a substring STR2
in the complete string STR1 (both of type ⮫ WSTRING).

Interface description

Table 3: Interface variables of the WFIND function
I/O type           Name           Data type       Description
VAR_INPUT          STR1           WSTRING(255)    Total string
                   STR2           WSTRING(255)    Searched substring
RETURN             WFIND          INT             Return value: Position

Example

## 5.5 WINSERT

Brief description
The WINSERT function of type ⮫ WSTRING inserts a substring STR2 into a
character string STR1 from a given position POS.

      Interface description

Table 4: Interface variables of the WINSERT function
I/O type       Name              Data type       Description
VAR_INPUT      STR1              WSTRING(255)    Character string

STR2              WSTRING(255)    Substring to be inserted
POS               INT             Position in STR1 after which STR2 is inserted
RETURN         WINSERT           WSTRING(255)    Return value: Total string

      Example

## 5.6 WLEFT

      Brief description
      The WLEFT function of type ⮫ WSTRING browses for a SIZE-sized substring in
      the STR string starting from the left and outputs it.

      Interface description

Table 5: Interface variables of the WLEFT function
I/O type       Name              Data type       Description
VAR_INPUT      STR               WSTRING(255)    Total string
               SIZE              INT             Length of the substring starting from left
RETURN         WLEFT             WSTRING(255)    Return value: Substring

Example

## 5.7 WLEN

Brief description
The function WLEN of type INT determines the length of the character string
STR of type ⮫ WSTRING and outputs it.

Interface description

Table 6: Interface variables of the WLEN function
I/O type           Name           Data type    Description
VAR_INPUT          STR            WSTRING(255) Character string
RETURN             WLEN           INT          Return value: String length

Example

## 5.8 WMID

Brief description
The WMID function of type ⮫ WSTRING determines a LEN-long substring from
the character string STR from the POS position and outputs this substring.

Interface description

Table 7: Interface variables of the WMID function
I/O type       Name              Data type          Description
VAR_INPUT      STR               WSTRING(255)       Character string
               LEN               INT                Substring length
               POS               INT                Position from which the substring is determined
RETURN         WLEN              INT                Return value: Substring

      Example

## 5.9 WREPLACE

      Brief description
      The function WREPLACE of type ⮫ WSTRING replaces a LEN long substring in
      the complete string STR1 from position POS with the replace string STR2 and
      outputs the new complete string.

      Interface description

Table 8: Interface variables of the WREPLACE function
I/O type       Name              Data type    Description
VAR_INPUT      STR1              WSTRING(255) Total string
               STR2              WSTRING(255) Replace string
               L                 INT          Length of the character string to be replaced in
                                              STR1
               P                 INT          Position in STR1 from which the replace string is
                                              used
RETURN         WREPLACE          WSTRING(255) Return value: remaining total string

Example

## 5.10 WRIGHT

Brief description
The WRIGHT function of type ⮫ WSTRING browses for a SIZE-sized substring
in the STR total string starting from the right and outputs it.

Interface description

Table 9: Interface variables of the WRIGHT function
I/O type           Name           Data type        Description
VAR_INPUT          STR            WSTRING(255)     Total string
                   SIZE           INT              Length of the substring starting from right
RETURN             WLEFT          WSTRING(255)     Return value: Substring

Example

## 5.11 LTOF

Brief description
The function block implements a time interval with switch-off delay.

Interface description

Table 10: Interface variables of the LTOF function block
I/O type       Name              Data type        Description
VAR_INPUT      IN                BOOL             Processing enabled
               PT                ⮫ LTIME          Time delay in ns

VAR_OUTPUT Q                     BOOL             Evaluation
ET                    ⮫ LTIME          Current delay time

Functional description
At a rising edge of IN, output Q switches from FALSE to TRUE.
After the transition from TRUE to FALSE at IN, output Q remains in the TRUE
state for the time PT (ns). Q only changes from TRUE to FALSE after this time
has elapsed.

Example

## 5.12 LTON

Brief description
The function block implements a time interval with switch-on delay.

Interface description

Table 11: Interface variables of the LTON function block
I/O type           Name           Data type        Description
VAR_INPUT          IN             BOOL             Processing enabled
                   PT             ⮫ LTIME          Time delay in ns
VAR_OUTPUT Q                      BOOL             Evaluation
           ET                     ⮫ LTIME          Current delay time

Functional description
At a rising edge of IN, the time interval at output ET starts counting.
Once the specified time delay (PT in ns) reached output ET, Q switches to
TRUE.
When IN is still TRUE, Q remains TRUE and ET retains the value of PT.
With the transition from TRUE to FALSE at IN, Q assumes the value FALSE and
ET the value zero.

Example

## 5.13 LTP

Brief description
Function block that operates as pulse generator with presettable pulse width.

Interface description

Table 12: Interface variables of the LTP function block
I/O type           Name           Data type        Description
VAR_INPUT          IN             BOOL             Processing enabled
                   PT             ⮫ LTIME          Time delay in ns
VAR_OUTPUT Q                      BOOL             Evaluation
           ET                     ⮫ LTIME          Current delay time

Functional description
After enabling, input IN goes from FALSE to TRUE, the timer ET (ns) is
counted up to a specified upper limit (PT in ns).
While incrementing, output Q is TRUE, otherwise FALSE.

Example
