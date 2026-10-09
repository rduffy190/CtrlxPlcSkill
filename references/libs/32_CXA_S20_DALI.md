# 32 CXA_S20_DALI

## 32.1 Introduction and overview

DALI - Digital Addressable Lighting Interface is a protocol for lighting and
building automation according to the standard IEC 62386.

Use the library CXA_S20_Dali together with the S20 module S20-DALI-2-PWR
(R911174403). The S20 module can be connected using the S20-EC-BK bus
coupler (Ethercat).
If an S20-DALI module is a double master (S20-DALI-2-PWR), up to 64 devices
can be accessed twice (e.g. lamps, ballasts, sensors or dimmers). To extend
a DALI network, further S20-DALI-2-PWR can be connected to the S20-EC-BK.
Bosch Rexroth provides lamps with DALI support like SL36 or SL78 elec‐
tronic. The DALI network can be set up in line or star topology. Each device
can be addressed individually or via broadcast commands. DALI ballasts can
be arranged and accessed in groups (max. 16 groups) or scenes (max. 16
scenes).

                                  max. 64

PWR-2 and SL36 electronic
The CXA_S20_Dali library provides a basic (all to start with DALI) and an
advanced (additional support) part. With the Bosch Rexroth DALI function
block solution, it is possible to control a DALI network without the need
for any other tool (no external tool is needed to set up the DALI addresses
initially, can be done using the function block IH_DaliProgramShortAddress).
To start a PLC program with CXA_S20_Dali, the function block IH_S20DaliR‐
eadWrite has to be instantiated for each DALI S20 module. It provides
the communication handle (Token) for all other function blocks in the
CXA_S20_Dali library, e.g. IH_DALIOn, IH_DALIDim.

Table 827: Function blocks of the CXA_S20_Dali library
Type                                     Description
Basic function blocks (Basic)
⮫ IH_DaliReadWrite                       Master function block that ensures the communication
                                         with the DALI Inline module and provides the communica‐
                                         tion handle “IOstrToken” for the other function blocks
⮫ IH_DaliDim                             Controls the light level of the ballast, can be used for
                                         groups or broadcast (switch on the ballast if required),
                                         the light level is defined
⮫ IH_DaliOff                             Switch off the ballast, can be used for groups or broad‐
                                         cast

⮫ IH_DaliOn                              Switch on the ballast, can be used for groups or broad‐
cast
⮫ IH_DaliDirectPower                     Controls the light level of the ballast, can be used for
groups or broadcast (switch on the ballast if necessary),
the light level can be specified
⮫ IH_DaliAddress                         Assigns a new address to the ballast
⮫ IH_DaliCallScene                       Changes the light level of the scene to the defined value
⮫ IH_DaliAddToGroup                      Adds the ballast to a group
⮫ IH_DaliAddToScene                      Adds the ballast or a group to the scene
⮫ IH_DaliRemoveFromGroup                 Removes the ballast from the group
⮫ IH_DaliRemoveFromScene                 Removes the ballast or a group from the scene
Advanced function blocks
⮫ IH_DaliQueryStatus                     Reads the status of all connected DALI ballasts
⮫ IH_DaliQueryActualLevel                Reads the actual performance of the ballast
⮫ IH_DaliQuerySceneLevel                 Reads the actual performance of the scene
⮫ IH_DaliQueryDTR                        Reads the Data Transfer Register (DTR) of the ballast
⮫ IH_DaliStoreParameter                  Stores the content of the Data Transfer Register (DTR) to a
specified parameter of the ballast
⮫ IH_DaliQueryParameter                  Reads the parameters "Fade Rate", "Fade Time", "Min
Level", "Max Level", "Power On Level", "System Failure
Level" of the ballast
⮫ IH_DaliQueryGroup                      Reads the assigned group of the ballast
⮫ IH_DaliQueryRandomAddress              Reads the random address of the ballast
⮫ IH_DaliSearchAddress                   Stores the search address of the ballast
⮫ IH_DaliProgramShortAddress             Assigns a short address to the ballast by random address
allocation or physical selection during initialization
⮫ IH_DaliReset                           Resets variables in the persistent memory of the ballast

## 32.2 IH_DaliDim

Brief description
The function block IH_DaliDim is used to control the light level of the ballast.
The function block has to be called in the function block ⮫ IH_DaliReadWrite.

     Interface description

Table 828: Interface variables of the IH_DaliDim function block
I/O type           Name               Data type             Description
VAR_INPUT          Execute            BOOL                  Rising edge starts computation
                   DimMode            ⮫ IH_INLN_DALI_DIM‐   Enumeration to select the DimMode
                                      MODE
                   AddressType        ⮫ IH_INLN_DALI_ADDR‐ Enumeration to select the address
                                      TYPE                 type
                   Address            BYTE                 The address depends on the selected
                                                           type under AddressType
                                                           Values between 0 and 63 are possible
                                                           for short addresses and 0 to 15 for
                                                           group addresses
VAR_OUTPUT Done                       BOOL                 Computation completed
           Active                     BOOL                 Computation ongoing
           Error                      BOOL                 Indicates an error
           ErrorID                    ⮫ ERROR_CODE         Error class
                   ErrorIdent         ⮫ ERROR_STRUCT        Detailed error information
VAR_IN_OUT         IOstrToken                              Structure to handle data between the
                                      ⮫ IH_INLN_DALI_TOKEN IH_S20DaliReadWrite and other Dali
                                                           function blocks.

     Min./max. and default values
The following table lists the min./max. and default values as well as the
application behavior of the function block inputs.
Table 829: Min./max. and default values as well as the response of the function block inputs of
IH_DaliDim during application
Name               Type          Min. value       Max. value Default value     Effective
Execute            BOOL          FALSE            TRUE       FALSE             Continuous
DimMode            IH_INLN_DALI_ UP               STEP‐      UP                Rising edge at Exe‐
                   DIMMODE                        DOWN_AND_O                   cute
                                                  FF
AddressType        IH_INLN_DALI_ SHORTADDR        BROADCAST  SHORTADDR         Rising edge at Exe‐
                   ADDRTYPE                                                    cute
Address            BYTE          0                Short address 0              Rising edge at Exe‐
                                                  = 63                         cute
                                                  Group address
                                                  = 15

Functional description
This function block is used to change the light level for a single ballast, a
group or all connected ballasts. This depends on the selection made under
AddressType. The user can set different dimming modes under "DimMode".
The function block is enabled after the first PLC cycle by setting the "Execute"
input to TRUE. Changed input values are only applied with a new rising edge
at the "Execute" input. The "Active" output is set to TRUE during operation.
The bit "Done" is set to TRUE upon completion. The function block can be
initialized again via a new rising edge at the "Execute" input. If an error results
during the operation, the "Error" bit is set to TRUE. "ErrorID" and "ErrorIdent"
show error information. The error can be acknowledged via a rising edge at
the "Execute" input.

Non-functional criteria
Call this function block to communicate with the Dali module via the
IH_S20DaliReadWrite function block.
Example of a function block
Instantiate the function block IH_S20DaliReadWrite before the IH_DaliDim
function block can be instantiated to communicate with the Dali module.
The input/output variable "stDaliToken" exchanges data between the function
blocks IH_S20DaliReadWrite and IH_DaliDim. Thus, this variable has to be
assigned to "IOstrToken" in both function blocks.
In this example, the function block IH_DaliDim in the ON_AND_STEPUP mode
is configured for a single ballast. If the ballast is switched off in this mode, it
is switched on by the command and then set to Min Level. A new rising edge
at the "bExecute" input increments the light level by one step.

Variable declaration

VAR
  fbIH_DaliDim: IH_DaliDim;
  bExecute: BOOL;
  stDaliToken: IH_INLN_DALI_TOKEN;
  bDone: BOOL;
  bActive: BOOL;
  bError: BOOL;
  enErrorID: ERROR_CODE;
  stErrorIdent: ERROR_STRUCT;
END_VAR

Example

fbIH_DaliDim(
  Execute:= bExecute,
  DimMode:= IH_INLN_DALI_DIMMODE.ON_AND_STEPUP,
  AddressType:= IH_INLN_DALI_ADDRTYPE.SHORTADDR,
  Address:= BYTE#2,
  IOstrToken:= stDaliToken,
  Done=> bDone,
  Active=> bActive,
  Error=> bError,
  ErrorID=> enErrorID,
  ErrorIdent=> stErrorIdent);

## 32.3 IH_DaliAddress

     Brief description
     The function block IH_DaliAddress assigns a new short address to a ballast.
     The function block has to be called using the function block ⮫ IH_DaliRead‐
     Write.

     Interface description

Table 830: Interface variables of the IH_DaliAddress function block
I/O type   Name                        Data type         Description
VAR_INPUT  Execute                     BOOL              Rising edge starts computation
           OldAddress                  BYTE              Old address of the ballast (0 to 63)
           NewAddress                  BYTE              New address of the ballast (0 to 63)
VAR_OUTPUT Done                        BOOL              Computation completed
           Active                      BOOL              Computation ongoing
           Error                       BOOL              Indicates an error
                   ErrorID             ⮫ ERROR_CODE      Error class
                   ErrorIdent          ⮫ ERROR_STRUCT Detailed error information
VAR_IN_OUT                                              Structure to handle data between the
                                       ⮫ IH_INLN_DALI_T
                   IOstrToken                           IH_S20DaliReadWrite and other Dali func‐
                                       OKEN
                                                        tion blocks.

     Min./max. and default values
 The following table lists the min./max. and default values as well as the
 application behavior of the function block inputs.
Table 831: Min./max. and default values as well as the response of the function block inputs of
IH_DaliAddress during application
Name               Type            Min. value      Max. value     Default value   Effective
Execute            BOOL            FALSE           TRUE           FALSE           Continuous
OldAddress         BYTE            0               63             0               Rising edge at Exe‐
                                                                                  cute
NewAddress         BYTE            0               63             0               Rising edge at Exe‐
                                                                                  cute

Functional description
The function block assigns a new short address to a ballast. The function
block is enabled after the first PLC cycle by setting the "Execute" input to
TRUE. Changed input values are only applied with a new rising edge at the
"Execute" input. The "Active" output is set to TRUE during operation. The bit
"Done" is set to TRUE upon completion. The function block can be initialized
again via a new rising edge at the "Execute" input. If an error results during
the operation, the "Error" bit is set to TRUE. "ErrorID" and "ErrorIdent" show
error information.
The error can be acknowledged via a rising edge at the "Execute" input.
Non-functional criteria
Call this function block to communicate with the Dali module via the

IH_S20DaliReadWrite function block.
Example of a function block
Instantiate the function block IH_S20DaliReadWrite before the IH_DaliAddress
function block can be instantiated to communicate with the Dali module.
The input/output variable "stDaliToken" exchanges data between the function
blocks IH_S20DaliReadWrite and IH_DaliAddress. Thus, this variable has to be
assigned to "IOstrToken" in both function blocks.
The function block IH_DaliAddress is exemplarily configured to change the
ballast address from 2 to 4. The new address is assigned to the ballast via a
new rising edge at the "Execute" input.

Variable declaration

VAR
  fbDaliAddress : IH_DaliAddress;
  bExecute      : BOOL;
  stDaliToken   : IH_INLN_DALI_TOKEN;
  bDone         : BOOL;
  bActive       : BOOL;
  bError        : BOOL;
  enErrorID     : ERROR_CODE;
  stErrorIdent : ERROR_STRUCT;
END_VAR

Example

fbDaliAddress(
  Execute:= bExecute,
  OldAddress:= BYTE#2,
  NewAddress:= BYTE#4,
  IOstrToken:= stDaliToken,
  Done=> bDone,
  Active=> bActive,
  Error=> bError,
  ErrorID=> enErrorID,
  ErrorIdent=> stErrorIdent);

## 32.4 IH_DaliCallScene

Brief description
The IH_DaliCallScene function block is used to call an already defined scene.
The function block has to be called using the function block ⮫ IH_DaliRead‐
Write.

     Interface description

Table 832: Interface variables of the IH_DaliCallScene function block
I/O type           Name               Data type         Description
VAR_INPUT          Execute            BOOL              Rising edge starts computation
                                                        Scene number
                   Scene              BYTE
                                                        Value range from 0 to 15
VAR_OUTPUT Done                       BOOL              Computation completed
           Active                     BOOL              Computation ongoing
           Error                      BOOL              Indicates an error
                   ErrorID            ⮫ ERROR_CODE      Error class
                   ErrorIdent         ⮫ ERROR_STRUCT Detailed error information
VAR_IN_OUT                                             Structure to handle data between the
                                      ⮫ IH_INLN_DALI_T
                   IOstrToken                          IH_S20DaliReadWrite and other Dali func‐
                                      OKEN
                                                       tion blocks.

     Min./max. and default values
The following table lists the min./max. and default values as well as the
application behavior of the function block inputs.
Table 833: Min./max. and default values as well as the response of the function block inputs of
IH_DaliCallScene during application
Name               Type            Min. value     Max. value     Default value   Effective
Execute            BOOL            FALSE          TRUE           FALSE           Continuous
Scene              BYTE            0              15             0               Rising edge at Exe‐
                                                                                 cute

Functional description
This function block calls an already defined scene. Up to 16 scenes can be
called in total. The "Scene" value is between 0 and 15. The function block
is enabled after the first PLC cycle by setting the "Execute" input to TRUE.
Changed input values are only applied with a new rising edge at the "Execute"
input. The "Active" output is set to TRUE during operation. The bit "Done"
is set to TRUE upon completion. The function block can be initialized again
via a new rising edge at the "Execute" input. If an error results during the
operation, the "Error" bit is set to TRUE. "ErrorID" and "ErrorIdent" show error
information. The error can be acknowledged via a rising edge at the "Execute"
input.
Non-functional criteria

Call this function block to communicate with the Dali module via the
IH_S20DaliReadWrite function block.
Example of a function block
Instantiate the function block IH_S20DaliReadWrite before the IH_DaliCallS‐
cene function block can be instantiated to communicate with the Dali module.
The input/output variable "stDaliToken" exchanges data between the function
blocks IH_S20DaliReadWrite and IH_DaliCallScene. Thus, this variable has to
be assigned to "IOstrToken" in both function blocks.
In this example, the already defined scene number 5 is called with IH_Dali‐
CallScene. At a rising edge at the "Execute" input, scene 5 is enabled on all
defined ballasts.

Variable declaration

VAR
  fbIH_DaliCallScene: IH_DaliCallScene;
  bExecute: BOOL;
  stDaliToken: IH_INLN_DALI_TOKEN;
  bDone: BOOL;
  bActive: BOOL;
  bError: BOOL;
  enErrorID: ERROR_CODE;
  stErrorIdent: ERROR_STRUCT;
END_VAR

Example

fbIH_DaliCallScene(
  Execute:= bExecute,
  Scene:= BYTE#5,
  IOstrToken:= stDaliToken,
  Done=> bDone,
  Active=> bActive,
  Error=> bError,
  ErrorID=> enErrorID,
  ErrorIdent=> stErrorIdent);

## 32.5 IH_DaliRemoveFromGroup

Brief description
Use the IH_DaliRemoveFromGroup function block to remove a ballast from the
specified group. The function block has to be called using the function block
⮫ IH_DaliReadWrite.

Interface description

Table 834: Interface variables of the IH_DaliRemoveFromGroup function block
I/O type   Name                        Data type         Description
VAR_INPUT  Execute                     BOOL              Rising edge starts computation
           GroupAddress                BYTE              Address of the group (0 to 15)
           ShortAddress                BYTE              Ballast address (0 to 63)
VAR_OUTPUT Done                        BOOL              Computation completed
           Active                      BOOL              Computation ongoing
           Error                       BOOL              Indicates an error
           ErrorID                     ⮫ ERROR_CODE      Error class
                   ErrorIdent          ⮫ ERROR_STRUCT Detailed error information
VAR_IN_OUT         IOstrToken                           Structure to handle data between the
                                       ⮫ IH_INLN_DALI_T
                                                        IH_S20DaliReadWrite and other Dali func‐
                                       OKEN
                                                        tion blocks.

Min./max. and default values
The following table lists the min./max. and default values as well as the
application behavior of the function block inputs.
Table 835: Min./max. and default values as well as the response of the function block inputs of
IH_DaliRemoveFromGroup during application
Name         Type                  Min. value      Max. value    Default value   Effective
Run          BOOL                  FALSE           TRUE          FALSE           Continuous
GroupAddress BYTE                  0               15            0               Rising edge at Exe‐
                                                                                 cute
ShortAddress       BYTE            0               63            0               Rising edge at Exe‐
                                                                                 cute

Functional description
Use the function block to remove a ballast from the specified group. The
function block is enabled after the first PLC cycle by setting the "Execute"
input to TRUE. Changed input values are only applied with a new rising edge
at the "Execute" input. The "Active" output is set to TRUE during operation.
The bit "Done" is set to TRUE upon completion. The function block can be
initialized again via a new rising edge at the "Execute" input. If an error results
during the operation, the "Error" bit is set to TRUE. "ErrorID" and "ErrorIdent"
show error information. The error can be acknowledged via a rising edge at
the "Execute" input.
Non-functional criteria
Call this function block to communicate with the Dali module via the

IH_S20DaliReadWrite function block.
Example of a function block
Instantiate the function block IH_S20DaliReadWrite before the IH_DaliRemove‐
FromGroup function block can be instantiated to communicate with the Dali
module. The input/output variable "stDaliToken" exchanges data between the
function blocks IH_S20DaliReadWrite and IH_DaliRemoveFromGroup. Thus,
this variable has to be assigned to "IOstrToken" in both function blocks.
The IH_DaliRemoveFromGroup function block is exemplarily configured to
remove the ballast (address = 2) from group number 5. The ballast from the
specified group is removed at a new rising edge at the "bExecute" input.

Variable declaration

VAR
  fbDaliRemoveFromGroup: IH_DaliRemoveFromGroup;
  bExecute: BOOL;
  stDaliToken: IH_INLN_DALI_TOKEN;
  bDone: BOOL;
  bActive: BOOL;
  bError: BOOL;
  enErrorID: ERROR_CODE;
  stErrorIdent: ERROR_STRUCT;
END_VAR

Example

fbDaliRemoveFromGroup(
  Execute:= bExecute,
  GroupAddress:= BYTE#5,
  ShortAddress:= BYTE#2,
  IOstrToken:= stDaliToken,
  Done=> bDone,
  Active=> bActive,
  Error=> bError,
  ErrorID=> enErrorID,
  ErrorIdent=> stErrorIdent);

## 32.6 IH_DaliDirectPower

Brief description
The function block IH_DaliDirectPower is used to directly enter the light level.
The function block has to be called using the function block ⮫ IH_DaliRead‐
Write.

     Interface description

Table 836: Interface variables of the IH_DaliDirectPower function block
I/O type           Name                Data type         Description
VAR_INPUT          Execute             BOOL              Rising edge starts computation
                                                         The value specifies the light level
                   LightLevel          BYTE
                                                         The value range is between 0 and 254
                                       ⮫ IH_INLN_DALI_A
                   AddressType                          Enumeration to select the address type
                                       DDRTYPE
                                                        The address depends on the selected type
                                                        under AddressType
                   Address             BYTE             Values between 0 and 63 are possible for
                                                        short addresses and 0 to 15 for group
                                                        addresses
VAR_OUTPUT Done                        BOOL             Computation completed
           Active                      BOOL             Computation ongoing
           Error                       BOOL             Indicates an error
                   ErrorID             ⮫ ERROR_CODE      Error class
                   ErrorIdent          ⮫ ERROR_STRUCT Detailed error information
VAR_IN_OUT                                              Structure to handle data between the
                                       ⮫ IH_INLN_DALI_T
                   IOstrToken                           IH_S20DaliReadWrite and other Dali func‐
                                       OKEN
                                                        tion blocks.

     Min./max. and default values
The following table lists the min./max. and default values as well as the
application behavior of the function block inputs.
Table 837: Min./max. and default values as well as the response of the function block inputs of
IH_DaliDirectPower during application
Name               Type            Min. value      Max. value     Default value   Effective
Execute            BOOL            FALSE           TRUE           FALSE           Continuous
                                                                                  Rising edge at Exe‐
LightLevel         BYTE            0               254            254
                                                                                  cute
                   IH_INLN_DALI_                                                  Rising edge at Exe‐
AddressType                      SHORTADDR         BROADCAST      SHORTADDR
                   ADDRTYPE                                                       cute
                                                   Short address
                                                   = 63                           Rising edge at Exe‐
Address            BYTE            0                             0
                                                   Group address                  cute
                                                   = 15

Functional description
This function block is used to directly enter a light level for a single ballast,
a ballast group or all connected ballasts. This depends on the selection made
under "AddressType". The performance is calculated using the following for‐
mula:

X stands for the value of the "LightLevel" input.
The function block is enabled after the first PLC cycle by setting the "Execute"
input to TRUE. Changed input values are only applied with a new rising edge
at the "Execute" input. The "Active" output is set to TRUE during operation.
The bit "Done" is set to TRUE upon completion. The function block can be
initialized again via a new rising edge at the "Execute" input. If an error results
during the operation, the "Error" bit is set to TRUE. "ErrorID" and "ErrorIdent"
show error information. The error can be acknowledged via a rising edge at
the "Execute" input.
Non-functional criteria
Call this function block to communicate with the Dali module via the
IH_S20DaliReadWrite function block.
Example of a function block
Instantiate the function block IH_S20DaliReadWrite before the IH_DaliDirect‐
Power function block can be instantiated to communicate with the Dali
module. The input/output variable "stDaliToken" exchanges data between the
function blocks IH_S20DaliReadWrite and IH_DaliDirectPower. Thus, this vari‐
able has to be assigned to "IOstrToken" in both function blocks.
In the example, IH_DaliDirectPower is used to set the light level of a single
ballast to 254.

Variable declaration

VAR
  fbIH_DaliDirectPower: IH_DaliDirectPower;
  bExecute: BOOL;
  stDaliToken: IH_INLN_DALI_TOKEN;
  bDone: BOOL;
  bActive: BOOL;
  bError: BOOL;
  enErrorID: ERROR_CODE;
  stErrorIdent: ERROR_STRUCT;
END_VAR

Example

     fbIH_DaliDirectPower(
       Execute:= bExecute,
       LightLevel:= BYTE#254,
       AddressType:= IH_INLN_DALI_ADDRTYPE.SHORTADDR,
       Address:= BYTE#2,
       IOstrToken:= stDaliToken,
       Done=> bDone,
       Active=> bActive,
       Error=> bError,
       ErrorID=> enErrorID,
       ErrorIdent=> stErrorIdent);

## 32.7 IH_DaliRemoveFromScene

     Brief description
     Use the IH_DaliRemoveFromScene function block to remove a ballast from the
     specified scene. The function block has to be called using the function block
     ⮫ IH_DaliReadWrite.

     Interface description

Table 838: Interface variables of the IH_DaliRemoveFromScene function block
I/O type           Name               Data type          Description
VAR_INPUT          Execute            BOOL               Rising edge starts computation
                   Group              BOOL               TRUE = Address is group address
                                                         FALSE = Address is ballast address
                   Address            BYTE               Address of the ballast/group (depends on
                                                         the "Group" input)
           Scene                      BYTE               Scene number (0 to 15)
VAR_OUTPUT Done                       BOOL               Computation completed
           Active                     BOOL               Computation ongoing
           Error                      BOOL               Indicates an error
           ErrorID                    ⮫ ERROR_CODE       Error class
                   ErrorIdent         ⮫ ERROR_STRUCT Detailed error information
VAR_IN_OUT         IOstrToken                          Structure to handle data between the
                                      ⮫ IH_INLN_DALI_T
                                                       IH_S20DaliReadWrite and other Dali func‐
                                      OKEN
                                                       tion blocks.

Min./max. and default values
The following table lists the min./max. and default values as well as the
application behavior of the function block inputs.
Table 839: Min./max. and default values as well as the response of the function block inputs of
IH_DaliRemoveFromScene during application
Name            Type             Min. value      Max. value       Default value    Effective
Execute         BOOL             FALSE           TRUE             FALSE            Continuous
Group           BOOL             FALSE           TRUE             FALSE            Rising edge at Exe‐
                                                                                   cute
Address         BYTE             0               Group = 15       0                Rising edge at Exe‐
                                                 Ballast = 63                      cute

Scene           BYTE             0               15               0                Rising edge at Exe‐
                                                              cute

Functional description
Use the function block to remove a ballast/group from the specified scene.
The function block is enabled after the first PLC cycle by setting the "Execute"
input to TRUE. Changed input values are only applied with a new rising edge
at the "Execute" input. The "Active" output is set to TRUE during operation.
The bit "Done" is set to TRUE upon completion. The function block can be
initialized again via a new rising edge at the "Execute" input. If an error results
during the operation, the "Error" bit is set to TRUE. "ErrorID" and "ErrorIdent"
show error information. The error can be acknowledged via a rising edge at
the "Execute" input.
Non-functional criteria
Call this function block to communicate with the Dali module via the
IH_S20DaliReadWrite function block.
Example of a function block
Instantiate the function block IH_S20DaliReadWrite before the IH_DaliRemove‐
FromScene function block can be instantiated to communicate with the Dali
module. The input/output variable "stDaliToken" exchanges data between the
function blocks IH_S20DaliReadWrite and IH_DaliRemoveFromScene. Thus,
this variable has to be assigned to "IOstrToken" in both function blocks.
The IH_DaliRemoveFromScene function block is exemplarily configured to
remove the ballast (address = 2) from scene number 5. The ballast from the
specified scene is removed at a new rising edge at the "bExecute" input.

Variable declaration

VAR
  fbDaliRemoveFromScene: IH_DaliRemoveFromScene;
  bExecute: BOOL;
  stDaliToken: IH_INLN_DALI_TOKEN;
  bDone: BOOL;
  bActive: BOOL;
  bError: BOOL;
  enErrorID: ERROR_CODE;
  stErrorIdent: ERROR_STRUCT;
  bGroup: BOOL;
END_VAR

Example

fbDaliRemoveFromScene(
  Execute:= bExecute,
  Group:= bGroup,
  Address:= BYTE#2,
  Scene:= BYTE#5,
  IOstrToken:= stDaliToken,
  Done=> bDone,
  Active=> bActive,
  Error=> bError,
  ErrorID=> enErrorID,
  ErrorIdent=> stErrorIdent);

## 32.8 IH_DaliQueryStatus

Brief description
The function block IH_DaliQueryStatus is used to retrieve a status of the bal‐
lasts connected to a Dali bus. This function block has to be called using the
function block ⮫ IH_DaliReadWrite.

      Interface description

Table 840: Interface variables of the IH_DaliQueryStatus function block
I/O type       Name                 Data type         Description
VAR_INPUT      Execute              BOOL              Rising edge starts computation
               Address              BYTE              Ballast address (0 to 63 or 255)
                                                      Address        SizeOfStatus Number of
                                                                                    read ballasts
                                                      0-63           1              1 ballast
                                                      255            64             64 ballasts
                                                      255            Number of      Number of
                                                                     ballasts       ballasts in
                                                                     from 1 to 64 SizeOfStatus
               SizeOfStatus         UINT            Status size (1 to 64)
               StatusAdr            POINTER_TO_BYTE Address of the status array
                                                    Address value Size of the status array
                                                    0 to 63         1 byte
                                                    255             Number of ballasts (1 to 64)
VAR_OUTPUT Done                     BOOL            Computation completed
           Active                   BOOL            Computation ongoing
           Error                    BOOL            Indicates an error
           ErrorID                  ⮫ ERROR_CODE    Error class
               ErrorIdent           ⮫ ERROR_STRUCT Detailed error information
VAR_IN_OUT     IOstrToken                            Structure to handle data between the
                                    ⮫ IH_INLN_DALI_T
                                                     IH_S20DaliReadWrite and other Dali func‐
                                    OKEN
                                                     tion blocks.

      Min./max. and default values
    The following table lists the min./max. and default values as well as the
    application behavior of the function block inputs.
Table 841: Min./max. and default values as well as the response of the function block inputs of
IH_DaliQueryStatus during application
Name            Type            Min. value      Max. value     Default value   Effective
Execute         BOOL            FALSE           TRUE           FALSE           Continuous
Address         BYTE            0               255            0               Rising edge at Exe‐
                                                                               cute
SizeOfStatus    UINT            1               64             1               Rising edge at Exe‐
                                                                               cute

Functional description
The function block is used to retrieve the status of the ballasts connected to
the Dali bus. If the entered address value is between 0 and 63, the status
of the respective ballast is read. If the address value is 255, the function
block reads the status of the number of ballasts specified in "SizeOfStatus".
The status information is provided in the "Status" array. Ensure that value
specified in "SizeOfStatus" matches the array size specified in "StatusAdr".
The status of a single ballast is included in one byte providing the following
status information:
Bit           Status information
0             Status of the ballast 0 = OK 1= NOT OK
1             Lamp failure. 0 = OK
2             Lamp switched on. 0 = OFF
3             Limit value error. 0 = Latest lamp wattage requested was either
              between MIN LEVEL and MAX LEVEL or it was OFF
4             Dimming completed: 0 = Dimming completed 1 = Dimming takes
              place
5             Reset status. 0 = No
6             Short address is missing. 0 = No 1 = Yes
7             Error during current supply. 0 = No. A "Reset" or control com‐
              mand was received for the lamp wattage during the last switch-
              on
The function block is enabled after the first PLC cycle by setting the "Execute"
input to TRUE. Changed input values are only applied with a new rising edge
at the "Execute" input. The "Active" output is set to TRUE during operation.
The bit "Done" is set to TRUE upon completion. The function block can be
initialized again via a new rising edge at the "Execute" input.
If an error results during the operation, the "Error" bit is set to TRUE.
"ErrorID" and "ErrorIdent" show error information. The error can be acknowl‐
edged via a rising edge at the "Execute" input.
Non-functional criteria
Call this function block to communicate with the Dali module via the
IH_S20DaliReadWrite function block.
Example of a function block
Instantiate the function block IH_S20DaliReadWrite before the IH_DaliQueryS‐
tatus function block can be instantiated to communicate with the Dali module.
The input/output variable "stDaliToken" exchanges data between the function
blocks IH_S20DaliReadWrite and IH_DaliQueryStatus. Thus, this variable has
to be assigned to "IOstrToken" in both function blocks.

Example 1
The function block IH_DaliQueryStatus is exemplarily configured to retrieve
the status of an individual ballast (address = 2). The status is saved in the
"byAddressStatus" byte.

Variable declaration

VAR
  fbDaliQueryStatus: IH_DaliQueryStatus;
  bExecute: BOOL;
  stDaliToken: IH_INLN_DALI_TOKEN;
  bDone: BOOL;
  bActive: BOOL;
  bError: BOOL;
  enErrorID: ERROR_CODE;
  stErrorIdent: ERROR_STRUCT;
  byAddressStatus: BYTE;
END_VAR

Implementation

fbDaliQueryStatus(
  Execute:= bExecute,
  Address:= BYTE#2,
  SizeOfStatus:= SIZEOF(byAddressStatus),
  StatusAdr:= ADR(byAddressStatus),
  IOstrToken:= stDaliToken,
  Done=> bDone,
  Active=> bActive,
  Error=> bError,
  ErrorID=> enErrorID,
  ErrorIdent=> stErrorIdent);

Example 2
The function block IH_DaliQueryStatus is exemplarily configured to retrieve
the status of all ballasts (address = 0 to 63). The status is saved in the
"arAddressStatus" array.

VAR
  fbDaliQueryStatus: IH_DaliQueryStatus;
  bExecute: BOOL;
  stDaliToken: IH_INLN_DALI_TOKEN;
  bDone: BOOL;
  bActive: BOOL;
  bError: BOOL;
  enErrorID: ERROR_CODE;
  stErrorIdent: ERROR_STRUCT;
  arAddressStatus: ARRAY[1..64] OF BYTE;
END_VAR

Implementation

fbDaliQueryStatus(
  Execute:= bExecute,
  Address:= BYTE#16#FF,
  SizeOfStatus:= SIZEOF(arAddressStatus),
  StatusAdr:= ADR(arAddressStatus),
  IOstrToken:= stDaliToken,
  Done=> bDone,
  Active=> bActive,
  Error=> bError,
  ErrorID=> enErrorID,
  ErrorIdent=> stErrorIdent);

## 32.9 IH_S20DaliReadWrite

     Brief description
     The function block IH_S20DaliReadWrite ensures the communication with the
     Dali master. It identifies the commands in the queue of other Dali function
     blocks in the program and ensures their execution. The function block has to
     be instantiated once for each Dali master.

     Interface description

Table 842: Interface variables of the IH_S20DaliReadWrite function block
I/O type           Name                Data type         Description
VAR_INPUT          Enable              BOOL              Function block active if TRUE
                   Status              BYTE              Input of process data byte "Status"
                   Response            BYTE              Input of process data byte "Response"
                   AddrIn_HighByte     BYTE              Input of process data byte "AddrIn_High‐
                                                         Byte"
                   CmdData_LowByte BYTE                  Input of process data byte "CmdData_Low‐
                                                         Byte"
VAR_OUTPUT Done                        BOOL              Computation completed and starts again in
                                                         the next cycle
                   Active              BOOL              The function block is operating
                   Error               BOOL              Indicates an error
                   ErrorID             ⮫ ERROR_CODE      Error class
                   ErrorIdent       ⮫ ERROR_STRUCT Detailed error information
                   Command          BYTE             Output of process data byte "Command"
                   AddrOut_HighByte BYTE             Output      of    process     data    byte
                                                     "AddrOut_HighByte"
                   Data_LowByte     BYTE             Input of process data byte "Data_LowByte"
VAR_IN_OUT         IOstrToken       ⮫ IH_INLN_DALI_T Structure to handle data between the
                                    OKEN             IH_S20DaliReadWrite and other Dali func‐
                                                     tion blocks

     Min./max. and default values
The following table lists the min./max. and default values as well as the
application behavior of the function block inputs.
Table 843: Min./max. and default values as well as the response of the function block inputs of
IH_S20DaliReadWrite during application
Name               Type              Min. value    Max. value    Default value   Effective
Enable             BOOL              FALSE         TRUE          FALSE           Continuous

Functional description
The function block ensures the communication with the Dali master. Input and
output process data bytes have to be mapped in the required Dali master.
"IOstrToken" has to be connected to other Dali function blocks in the program.
The structure "IOstrToken" communicates with other Dali function blocks and
exchanges data. The module optionally receives a response command and
forwards it to other Dali function blocks. Commands are evaluated and proc‐
essed in the respective Dali function blocks. The function block is enabled
after the first PLC cycle by setting the "Enable" input to TRUE. The "Active"
output is set to TRUE during operation. The bit "Done" is set to TRUE upon
completion. If commands are detected in the queue, the function block starts
processing until the "Enable" bit is set to TRUE. If an error results during

the operation, the "Error" bit is set to TRUE. If an error results during the
operation, the "Error" bit is set to TRUE. "ErrorID" and "ErrorIdent" show error
information. The error can be acknowledged via a rising edge at the "Enable"
input.
Non-functional criteria
The function block IH_S20DaliReadWrite has to be instantiated for the com‐
munication with the Dali module together with the other function blocks.
The current status of the ballast is not updated automatically. To update the
current status, a new query is required.
Example of a function block
Instantiate the function block IH_S20DaliReadWrite before other Dali function
blocks can be instantiated to communicate with the Dali module. The input/
output variable "stDaliToken" exchanges data between IH_S20DaliReadWrite
and other function blocks. Thus, this variable has to be assigned to "stDa‐
liToken" in both function blocks.
In the example, the function block IH_S20DaliReadWrite is configured to
exchange data with the Dali master and other Dali function blocks. The varia‐
bles for input and output process data have to be assigned to the Dali master
for communication purposes.
Some devices might require a Dali address for the addressing. Use the
“IH_DaliProgramShortAddress” function block for addressing.

Variable declaration

VAR
  fbIH_S20DaliReadWrite : IH_S20DaliReadWrite; // FB Instance
  bEnable_RW                 : BOOL;     // TRUE: Processing enabled (cyclic, state-controlled)
  bDone_RW                   : BOOL;     // The function block has output a result
  bActive_RW                 : BOOL;     // The function block is active
  bError_RW                 : BOOL;    // Indicates that an error occurred
  ErrorID_RW                 : ERROR_CODE;   // Error cause
  ErrorIdent_RW           : ERROR_STRUCT; // Detailed error cause
  byStatus                   : BYTE;     // Inprocess data: Status Byte
  byResponse                 : BYTE;     // Inprocess data: Response Byte
  byAddrIn_HighByte     : BYTE;      // Inprocess data: AddressIn Byte
  byCmdData_LowByte     : BYTE;      // Inprocess data: CommandData Byte
  byCommand                 : BYTE;    // Outprocess data: Command Byte
  byAddrOut_HighByte      : BYTE;      // Outprocess data: AddressOut Byte
  byData_LowByte            : BYTE;      // Outprocess data: Data Byte
  stDaliToken             : IH_INLN_DALI_TOKEN; // Structure used to handle data between IH_DaliReadWrite and
other Dali function blocks.
END_VAR

Example

fbIH_S20DaliReadWrite(
  Enable:= bEnable_RW,
  Done=> bDone_RW,
  Active=> bActive_RW,
  Error=> bError_RW,
  ErrorID=> ErrorID_RW,
  ErrorIdent=> ErrorIdent_RW,
  Status:= byStatus,
  Response:= byResponse,
  AddrIn_HighByte:= byAddrIn_HighByte,
  CmdData_LowByte:= byCmdData_LowByte,
  Command=> byCommand,
  AddrOut_HighByte=> byAddrOut_HighByte,
  Data_LowByte=> byData_LowByte,
  IOstrToken:= stDaliToken);

Process data mapping

## 32.10 IH_DaliQueryActualLevel

Brief description
The function block IH_DaliQueryActualLevel is used to read out the actual
lamp wattage of the ballasts connected to a Dali bus. This function block has
to be called using the function block ⮫ IH_DaliReadWrite.

Interface description

Table 844: Interface variables of the IH_DaliQueryActualLevel function block

I/O type        Name                Data typeDescription
VAR_INPUT       Execute             BOOL     Rising edge starts computation
Address             BYTE     Ballast address (0 to 63 or 255)
                        Address        SizeOfStatus Number of
                                                       read ballasts
                        0-63           1               1 ballast
                        255            64              64 ballasts
                        255            Number of       Number of
                                       ballasts        ballasts in
                                       from 1 to 64 ActualLevel
SizeOfActualLevel UINT            Size of the ActualLevel array (1 to 64)
ActualLevelAdr    POINTER_TO_BYTE Address of the ActualLevel array
                        Address value Size of the ActualLevel array
                        0 to 63        1 byte
                        255            Number of ballasts (1 to 64)
VAR_OUTPUT Done              BOOL            Computation completed
Active            BOOL            Computation ongoing
Error             BOOL            Indicates an error
ErrorID           ⮫ ERROR_CODE    Error class
ErrorIdent          ⮫ ERROR_STRUCT Detailed error information
VAR_IN_OUT      IOstrToken                           Structure to handle data between the
               ⮫ IH_INLN_DALI_T
                                IH_S20DaliReadWrite and other Dali func‐
               OKEN
                                tion blocks.

Min./max. and default values
The following table lists the min./max. and default values as well as the
application behavior of the function block inputs.
Table 845: Min./max. and default values as well as the response of the function block inputs of
IH_DaliQueryActualLevel during application
Name            Type            Min. value      Max. value     Default value    Effective
Execute         BOOL            FALSE           TRUE           FALSE            Continuous
Address         BYTE            0               255            0                Rising edge at Exe‐
                                                                                cute
SizeOfActual‐   UINT            1               64             1                Rising edge at Exe‐
Level                                                                           cute

Functional description
Use this function block to determine the actual lamp wattage of the ballasts
connected to the Dali bus. If the entered address value is between 0 and 63,
the “ActualLevel” of the respective ballast is read. If the address value is 255,
the function block reads the actual lamp wattage of the number of ballasts
specified in "SizeOfActualLevel". Information on the actual lamp wattage is
included in the array "ActualLevel".
The function block is enabled after the first PLC cycle by setting the "Execute"
input to TRUE. Changed input values are only applied with a new rising edge
at the "Execute" input. The "Active" output is set to TRUE during operation.
The bit "Done" is set to TRUE upon completion. The function block can be
initialized again via a new rising edge at the "Execute" input.
If an error results during the operation, the "Error" bit is set to TRUE.
"ErrorID" and "ErrorIdent" show error information. The error can be acknowl‐
edged via a rising edge at the "Execute" input.
Non-functional criteria
Call this function block to communicate with the Dali module via the
IH_S20DaliReadWrite function block.
Example of a function block
Instantiate the function block IH_S20DaliReadWrite before the IH_DaliQuer‐
yActualLevel function block can be instantiated to communicate with the Dali
module. The input/output variable "stDaliToken" exchanges data between the
function blocks IH_S20DaliReadWrite and IH_DaliQueryActualLevel. Thus, this
variable has to be assigned to "IOstrToken" in both function blocks.

Example 1
In the example, the function block IH_DaliQueryActualLevel reads out the
actual lamp wattage of a single ballast.
The function block reads the actual lamp wattage of ballast 2 and saves it to
the variable "byActualLevel".

Variable declaration

VAR
  fbIH_DaliQueryActualLevel: IH_DaliQueryActualLevel;
  bExecute: BOOL;
  byActualLevel: BYTE;
  stDaliToken: IH_INLN_DALI_TOKEN;
  bDone: BOOL;
  bActive: BOOL;
  bError: BOOL;
  enErrorID: ERROR_CODE;
  stErrorIdent: ERROR_STRUCT;

END_VAR

Implementation

fbIH_DaliQueryActualLevel(
  Execute:= bExecute,
  Address:= BYTE#2,
  SizeOfActualLevel:= SIZEOF(byActualLevel),
  ActualLevelAdr:= ADR(byActualLevel),
  IOstrToken:= stDaliToken,
  Done=> bDone,
  Active=> bActive,
  Error=> bError,
  ErrorID=> enErrorID,
  ErrorIdent=> stErrorIdent);

Example 2

In this example, the function block IH_DaliQueryActualLevel reads out the
actual lamp wattage of all 63 ballasts.
The function block reads the actual lamp wattage of 63 ballasts and saves it
to the array "arActualLevel".
An array of 63 bytes has to be created and the address of the array has to be
assigned to "ActualLevelAdr".
The size of the array is specified in "SizeOfActualLevel". If the actual array is
smaller than the value in the variable "SizeOfActualLevel", data can be written
to another address. This can cause malfunctions in the application.

Variable declaration

VAR
  fbIH_DaliQueryActualLevel: IH_DaliQueryActualLevel;
  bExecute: BOOL;
  stDaliToken: IH_INLN_DALI_TOKEN;
  bDone: BOOL;
  bActive: BOOL;
  bError: BOOL;
  enErrorID: ERROR_CODE;
  stErrorIdent: ERROR_STRUCT;
  arActualLevel: ARRAY [0..63] OF BYTE;
END_VAR

Implementation

fbIH_DaliQueryActualLevel(
  Execute:= bExecute,
  Address:= BYTE#16#FF,
  SizeOfActualLevel:= SIZEOF(arActualLevel),
  ActualLevelAdr:= ADR(arActualLevel),
  IOstrToken:= stDaliToken,
  Done=> bDone,
  Active=> bActive,
  Error=> bError,
  ErrorID=> enErrorID,
  ErrorIdent=> stErrorIdent);

## 32.11 IH_DaliAddToGroup

     Brief description
     Use the IH_DaliAddToGroup function block to insert a ballast into the speci‐
     fied group. The function block has to be called using the function block
     ⮫ IH_DaliReadWrite.

     Interface description

Table 846: Interface variables of the IH_DaliAddToGroup function block
I/O type   Name                        Data type         Description
VAR_INPUT  Execute                     BOOL              Rising edge starts computation
           GroupAddress                BYTE              Address of the group (0 to 15)
           ShortAddress                BYTE              Ballast address (0 to 63)
VAR_OUTPUT Done                        BOOL              Computation completed
           Active                      BOOL              Computation ongoing
           Error                       BOOL              Indicates an error
           ErrorID                     ⮫ ERROR_CODE      Error class
                   ErrorIdent          ⮫ ERROR_STRUCT Detailed error information
VAR_IN_OUT         IOstrToken          ⮫ IH_INLN_DALI_T Structure to handle data between the
                                       OKEN             IH_S20DaliReadWrite and other Dali func‐
                                                        tion blocks.

     Min./max. and default values
The following table lists the min./max. and default values as well as the
application behavior of the function block inputs.
Table 847: Min./max. and default values as well as the response of the function block inputs of
IH_DaliAddToGroup during application
Name               Type            Min. value      Max. value    Default value   Effective
Execute            BOOL            FALSE           TRUE          FALSE           Continuous
                                                                                 Rising edge at Exe‐
GroupAddress BYTE                  0               15            0
                                                                                 cute
                                                                                 Rising edge at Exe‐
ShortAddress       BYTE            0               63            0
                                                                                 cute

Functional description
Use the IH_DaliAddToGroup function block to insert one or multiple ballast(s)
into a group. Up to 16 groups can be created. The function block is enabled
after the first PLC cycle by setting the "Execute" input to TRUE. Changed
input values are only applied with a new rising edge at the "Execute" input.
The "Active" output is set to TRUE during operation. The bit "Done" is set to
TRUE upon completion. The function block can be initialized again via a new
rising edge at the "Execute" input. If an error results during the operation, the
"Error" bit is set to TRUE. "ErrorID" and "ErrorIdent" show error information.
The error can be acknowledged via a rising edge at the "Execute" input.
Non-functional criteria
Call this function block to communicate with the Dali module via the

IH_S20DaliReadWrite function block.
Example of a function block
Instantiate the function block IH_S20DaliReadWrite before the IH_DaliAdd‐
ToGroup function block can be instantiated to communicate with the Dali
module. The input/output variable "stDaliToken" exchanges data between the
function blocks IH_S20DaliReadWrite and IH_DaliAddToGroup. Thus, this vari‐
able has to be assigned to "IOstrToken" in both function blocks.
The IH_DaliAddToGroup function block is exemplarily configured to add a bal‐
last with the address 2 to the group number 10. The function block can be
added to the specified group at a new rising edge at the "Execute" input.

Variable declaration

VAR
  fbDaliAddToGroup       : IH_DaliAddToGroup;
  bExecute               : BOOL;
  stDaliToken            : IH_INLN_DALI_TOKEN;
  bDone                  : BOOL;
  bActive                : BOOL;
  bError                 : BOOL;
  enErrorID              : ERROR_CODE;
  stErrorIdent           : ERROR_STRUCT;
END_VAR

Example

fbDaliAddToGroup(
  Execute:= bExecute,
  GroupAddress:= BYTE#10,
  ShortAddress:= BYTE#2,
  IOstrToken:= stDaliToken,
  Done=> bDone,
  Active=> bActive,
  Error=> bError,
  ErrorID=> enErrorID,
  ErrorIdent=> stErrorIdent);

## 32.12 IH_DaliAddToScene

Brief description
Use the IH_DaliAddToScene function block to add a ballast to the speci‐
fied scene. The function block has to be called using the function block
⮫ IH_DaliReadWrite.

     Interface description

Table 848: Interface variables of the IH_DaliAddToScene function block
I/O type           Name                Data type          Description
VAR_INPUT          Execute             BOOL               Rising edge starts computation
                   LightLevel          BYTE               Light intensity (0 to 254)
                   Group               BOOL               TRUE = Address is group address
                                                          FALSE = Address is ballast address
                   Address             BYTE               Address of the ballast/group (depends on
                                                          the "Group" input)
                                                          Values between 0 and 15 are possible for
                                                          groups and 0 to 63 for ballasts
           Scene                       BYTE               Scene number (0 to 15)
VAR_OUTPUT Done                        BOOL               Computation completed
           Active                      BOOL               Computation ongoing
           Error                       BOOL               Indicates an error
           ErrorID                     ⮫ ERROR_CODE       Error class
                   ErrorIdent          ⮫ ERROR_STRUCT Detailed error information
VAR_IN_OUT         IOstrToken                           Structure to handle data between the
                                       ⮫ IH_INLN_DALI_T
                                                        IH_S20DaliReadWrite and other Dali func‐
                                       OKEN
                                                        tion blocks.

     Min./max. and default values
The following table lists the min./max. and default values as well as the
application behavior of the function block inputs.
Table 849: Min./max. and default values as well as the response of the function block inputs of
IH_DaliAddToScene during application
Name               Type            Min. value      Max. value     Default value   Effective
Execute            BOOL            FALSE           TRUE           FALSE           Continuous
                                                                                  Rising edge at Exe‐
Light Level        BYTE            0               254            254
                                                                                  cute
                                                                                  Rising edge at Exe‐
Group              BOOL            FALSE           TRUE           FALSE
                                                                                  cute
                                                   Group = 15                     Rising edge at Exe‐
Address            BYTE            0                              0
                                                   Ballast = 63                   cute
                                                                                  Rising edge at Exe‐
Scene              BYTE            0               15             0
                                                                                  cute

Functional description
Use this function block to add a ballast or a group to a scene with a certain
light level. Devices of a scene can have different light levels. The function
block is enabled after the first PLC cycle by setting the "Execute" input to
TRUE. Changed input values are only applied with a new rising edge at the
"Execute" input. The "Active" output is set to TRUE during operation. The bit
"Done" is set to TRUE upon completion. The function block can be initialized
again via a new rising edge at the "Execute" input. If an error results during
the operation, the "Error" bit is set to TRUE. "ErrorID" and "ErrorIdent" show
error information. The error can be acknowledged via a rising edge at the
"Execute" input.
Non-functional criteria

Call this function block to communicate with the Dali module via the
IH_S20DaliReadWrite function block.
Example of a function block
Instantiate the function block IH_S20DaliReadWrite before the IH_DaliAdd‐
ToScene function block can be instantiated to communicate with the Dali
module. The input/output variable "stDaliToken" exchanges data between the
function blocks IH_S20DaliReadWrite and IH_DaliAddToScene. Thus, this vari‐
able has to be assigned to "IOstrToken" in both function blocks.
In the example, the function block IH_DaliAddToScene adds a ballast or a
group of ballasts with address 4 to the scene no. 10. Its light level is specified
with 100. The address type (short address or group address) depends on the
status of the variable "Group" ab (TRUE = Address is group address, FALSE =
Address is ballast address). The new rising edge at the "bExecute" input adds
ballast or a group to the scene with a specified light level.

Variable declaration

VAR
  fbDaliAddToScene : IH_DaliAddToScene;
  bExecute           : BOOL;
  bGroup       : BOOL;
  stDaliToken        : IH_INLN_DALI_TOKEN;
  bDone              : BOOL;
  bActive            : BOOL;
  bError             : BOOL;
  enErrorID          : ERROR_CODE;
  stErrorIdent       : ERROR_STRUCT;
END_VAR

Example

fbDaliAddToScene(
  Execute:= bExecute,
  LightLevel:= BYTE#100,
  Group:= bGroup,
  Address:= BYTE#4,
  Scene:= BYTE#12,
  IOstrToken:= stDaliToken,
  Done=> bDone,
  Active=> bActive,
  Error=> bError,
  ErrorID=> enErrorID,
  ErrorIdent=> stErrorIdent);

## 32.13 IH_DaliOff

     Brief description
     Use the IH_DaliOff function block to switch off a single ballast, a group of
     ballasts or all ballasts. The function block has to be called using the function
     block ⮫ IH_DaliReadWrite.

     Interface description

Table 850: Interface variables of the IH_DaliOff function block
I/O type           Name                Data type        Description
VAR_INPUT          Execute             BOOL             Rising edge starts computation
                   AddressType         IH_INLN_DALI_ADD Enumeration to select the address type.
                                       RTYPE
                   Address             BYTE             The address depends on the selected type
                                                        under AddressType
                                                        Values between 0 and 63 are possible for
                                                        short addresses and 0 to 15 for group
                                                        addresses
VAR_OUTPUT Done                        BOOL             Computation completed
           Active                      BOOL             Computation ongoing
           Error                       BOOL             Indicates an error
           ErrorID                     ⮫ ERROR_CODE     Error class
                   ErrorIdent          ⮫ ERROR_STRUCT Detailed error information
VAR_IN_OUT         IOstrToken                           Structure to handle data between the
                                       ⮫ IH_INLN_DALI_T
                                                        IH_S20DaliReadWrite and other Dali func‐
                                       OKEN
                                                        tion blocks.

     Min./max. and default values
 The following table lists the min./max. and default values as well as the
 application behavior of the function block inputs.
Table 851: Min./max. and default values as well as the response of the function block inputs of
IH_DaliOff during application
Name               Type          Min. value        Max. value       Default value   Effective
Execute            BOOL          FALSE             TRUE             FALSE           Continuous
                   IH_INLN_DALI_                                                    Rising edge at Exe‐
AddressType                      SHORTADDR         BROADCAST        SHORTADDR
                   ADDRTYPE                                                         cute
                                                   Group = 15                       Rising edge at Exe‐
Address            BYTE            0                                0
                                                   Ballast = 63                     cute

Functional description
Use the IH_DaliOff function block to switch off a single ballast, a group of
ballasts or all ballasts. The function block is enabled after the first PLC cycle
by setting the "Execute" input to TRUE. Changed input values are only applied
with a new rising edge at the "Execute" input. The "Active" output is set to
TRUE during operation. The bit "Done" is set to TRUE upon completion. The
function block can be initialized again via a new rising edge at the "Execute"
input. If an error results during the operation, the "Error" bit is set to TRUE.
"ErrorID" and "ErrorIdent" show error information. The error can be acknowl‐
edged via a rising edge at the "Execute" input.
Non-functional criteria
Call this function block to communicate with the Dali module via the

IH_S20DaliReadWrite function block.
Example of a function block
Instantiate the function block IH_S20DaliReadWrite before the IH_DaliOff
function block can be instantiated to communicate with the Dali module.
The input/output variable "stDaliToken" exchanges data between the function
blocks IH_S20DaliReadWrite and IH_DaliOff. Thus, this variable has to be
assigned to "IOstrToken" in both function blocks.
The IH_DaliOff function block is exemplarily configured to switch off a ballast
with the address 4, as the address type is SHORTADDR. At a new rising edge
at the "bExecute" input, either a ballast, a group of ballasts or all ballasts are
switched off depending on the type selected under AddressType.

Variable declaration

VAR
  fbDaliOff         : IH_DaliOff;
  bExecute              : BOOL;
  stDaliToken           : IH_INLN_DALI_TOKEN;
  bDone                 : BOOL;
  bActive               : BOOL;
  bError                : BOOL;
  enErrorID             : ERROR_CODE;
  stErrorIdent          : ERROR_STRUCT;

END_VAR

Example

fbDaliOff(
  Execute:= bExecute,
  AddressType:= IH_INLN_DALI_ADDRTYPE.SHORTADDR,
  Address:= BYTE#4,
  IOstrToken:= stDaliToken,
  Done=> bDone,
  Active=> bActive,
  Error=> bError,
  ErrorID=> enErrorID,
  ErrorIdent=> stErrorIdent);

## 32.14 IH_DaliOn

     Brief description
     Use the IH_DaliOn function block to switch on a single ballast, a group of bal‐
     lasts or all ballasts. The light level can also be set to Min., Mid. or Max. The
     function block has to be called using the function block ⮫ IH_DaliReadWrite.

     Interface description

Table 852: Interface variables of the IH_DaliOn function block
I/O type           Name               Data type         Description
VAR_INPUT          Execute            BOOL              Rising edge starts computation
                   LightLevel         ⮫ IH_INLN_DALI_LI The value specifies the light level. For more
                                      GHTLEVEL          information, go to the section on structures
                                                        and enumerations
                   AddressType        ⮫ IH_INLN_DALI_A Enumeration to select the address type
                                      DDRTYPE
                   Address            BYTE              The address depends on the selected type
                                                        under AddressType
                                                        Values between 0 and 63 are possible for
                                                        short addresses and 0 to 15 for group
                                                        addresses
VAR_OUTPUT Done                       BOOL              Computation completed
           Active                     BOOL              Computation ongoing
           Error                      BOOL              Indicates an error
           ErrorID                    ⮫ ERROR_CODE      Error class
                   ErrorIdent         ⮫ ERROR_STRUCT Detailed error information
VAR_IN_OUT         IOstrToken                          Structure to handle data between the
                                      ⮫ IH_INLN_DALI_T
                                                       IH_S20DaliReadWrite and other Dali func‐
                                      OKEN
                                                       tion blocks.

Min./max. and default values
The following table lists the min./max. and default values as well as the
application behavior of the function block inputs.
Table 853: Min./max. and default values as well as the response of the function block inputs of
IH_DaliOn during application
Name            Type          Min. value         Max. value       Default value   Effective
Execute         BOOL          FALSE              TRUE             FALSE           Continuous
                IH_INLN_DALI_ MIN_LEVEL                                           Rising edge at Exe‐
LightLevel                                       MAX_LEVEL        MAX_LEVEL
                LIGHTLEVEL                                                        cute
                IH_INLN_DALI_                                                     Rising edge at Exe‐
AddressType                   SHORTADDR          BROADCAST        SHORTADDR
                ADDRTYPE                                                          cute

                            Group = 15                       Rising edge at Exe‐
Address         BYTE             0                                0
                            Ballast = 63                     cute

Functional description
Use the function block to switch on a single ballast, a group of ballasts or all
ballasts. The light level can also be set to "Min", "Mid" or "Max" via the "Light‐
Level" input. The function block is enabled after the first PLC cycle by setting
the "Execute" input to TRUE. Changed input values are only applied with a
new rising edge at the "Execute" input. The "Active" output is set to TRUE
during operation. The bit "Done" is set to TRUE upon completion. The function
block can be initialized again via a new rising edge at the "Execute" input. If
an error results during the operation, the "Error" bit is set to TRUE. "ErrorID"
and "ErrorIdent" show error information. The error can be acknowledged via a
rising edge at the "Execute" input.
Non-functional criteria
Call this function block to communicate with the Dali module via the
IH_S20DaliReadWrite function block.
Example of a function block
Instantiate the function block IH_S20DaliReadWrite before the IH_DaliOn func‐
tion block can be instantiated to communicate with the Dali module. The
input/output variable "stDaliToken" exchanges data between the function
blocks IH_S20DaliReadWrite and IH_DaliOn. Thus, this variable has to be
assigned to "IOstrToken" in both function blocks.
In the example, the IH_DaliOn function block switches on the ballast with
the short address 2 and sets its light level to Max. At a new rising edge at
"bExecute", a ballast, a group of ballasts or all ballasts are switched on and
the light level is set to "Min", "Mid" or "Max" depending on the selection made
in the "LightLevel" input.

Variable declaration

VAR
  fbDaliOn     : IH_DaliOn;
  bExecute           : BOOL;
  stDaliToken        : IH_INLN_DALI_TOKEN;
  bDone              : BOOL;
  bActive            : BOOL;
  bError             : BOOL;
  enErrorID          : ERROR_CODE;
  stErrorIdent       : ERROR_STRUCT;
END_VAR

Example

fbDaliOn(
  Execute:= bExecute,
  LightLevel:= IH_INLN_DALI_LIGHTLEVEL.MAX_LEVEL,
  AddressType:= IH_INLN_DALI_ADDRTYPE.SHORTADDR,
  Address:= BYTE#2,
  IOstrToken:= stDaliToken,
  Done=> bDone,
  Active=> bActive,
  Error=> bError,
  ErrorID=> enErrorID,
  ErrorIdent=> stErrorIdent);

## 32.15 IH_DaliSearchAddress

Brief description
The IH_DaliSearchAddress function block saves the search address specified
by the user. The function block has to be called using the function block
⮫ IH_DaliReadWrite.

Interface description

Table 854: Interface variables of the IH_DaliSearchAddress function block
I/O type   Name                       Data type         Description
VAR_INPUT  Execute                    BOOL              Rising edge starts computation
           SearchAddressH             BYTE              High-order byte of the search address
           SearchAddressM             BYTE              Middle byte of the search address
           SearchAddressL             BYTE              Low-order byte of the search address
VAR_OUTPUT Done                       BOOL              Computation completed
           Active                     BOOL              Computation ongoing
           Error                      BOOL              Indicates an error
           ErrorID                    ⮫ ERROR_CODE      Error class
                   ErrorIdent         ⮫ ERROR_STRUCT Detailed error information
VAR_IN_OUT         IOstrToken                          Structure to handle data between the
                                      ⮫ IH_INLN_DALI_T
                                                       IH_S20DaliReadWrite and other Dali func‐
                                      OKEN
                                                       tion blocks.

Min./max. and default values
The following table lists the min./max. and default values as well as the
application behavior of the function block inputs.
Table 855: Min./max. and default values as well as the response of the function block inputs of
IH_DaliSearchAddress during application
Name            Type            Min. value      Max. value     Default value   Effective
Execute         BOOL            FALSE           TRUE           FALSE           Continuous
SearchAd‐       BYTE            0               255            0               Rising edge at Exe‐
dressH                                                                         cute
SearchAd‐       BYTE            0               255            0               Rising edge at Exe‐
dressM                                                                         cute

SearchAd‐       BYTE            0               255            0               Rising edge at Exe‐
dressL                                                                         cute

Functional description
The function block saves the search address specified by the user. The func‐
tion block is enabled after the first PLC cycle by setting the "Execute" input
to TRUE. Changed input values are only applied with a new rising edge at the
"Execute" input. The "Active" output is set to TRUE during operation. The bit
"Done" is set to TRUE upon completion. The function block can be initialized
again via a new rising edge at the "Execute" input. If an error results during
the operation, the "Error" bit is set to TRUE. "ErrorID" and "ErrorIdent" show
error information.
The error can be acknowledged via a rising edge at the "Execute" input.
Non-functional criteria
Call this function block to communicate with the Dali module via the
IH_S20DaliReadWrite function block.
Example of a function block
Instantiate the function block IH_S20DaliReadWrite before the IH_DaliSearch‐
Address function block can be instantiated to communicate with the Dali
module. The input/output variable stDaliToken exchanges data between the
function blocks IH_S20DaliReadWrite and IH_DaliSearchAddress. Thus, this
variable has to be assigned to "IOstrToken" in both function blocks.
In the example, the IH_DaliSearchAddress function block is configured to
move the values of "bySearchAddressH", "bySearchAddressM" and "bySearch‐
AddressL" of the search address of the ballast. At a new rising edge at the
"bExecute" input, the user input is assigned as new search address of the
ballast.

Variable declaration

1000 /    ctrlX PLC Engineering
1344      IH_DaliQuerySceneLevel

VAR
  fbDaliSearchAddress: IH_DaliSearchAddress;
  bExecute: BOOL;
  bySearchAddressH: BYTE;
  bySearchAddressM: BYTE;
  bySearchAddressL: BYTE;
  stDaliToken: IH_INLN_DALI_TOKEN;
  bDone: BOOL;
  bActive: BOOL;
  bError: BOOL;
  enErrorID: ERROR_CODE;
  stErrorIdent: ERROR_STRUCT;
END_VAR

Example

fbDaliSearchAddress(
  Execute:= bExecute,
  SearchAddressH:= bySearchAddressH,
  SearchAddressM:= bySearchAddressM,
  SearchAddressL:= bySearchAddressL,
  IOstrToken:= stDaliToken,
  Done=> bDone,
  Active=> bActive,
  Error=> bError,
  ErrorID=> enErrorID,
  ErrorIdent=> stErrorIdent);

## 32.16 IH_DaliQuerySceneLevel

Brief description
The function block IH_DaliQuerySceneLevel reads out the scene level of
the ballast. The function block has to be called using the function block
⮫ IH_DaliReadWrite.

                                                    IH_DaliQuerySceneLevel       1344

      Interface description

Table 856: Interface variables of the IH_DaliQuerySceneLevel function block
I/O type   Name                     Data type         Description
VAR_INPUT  Execute                  BOOL              Rising edge starts computation
           ShortAddress             BYTE              Ballast address (0 to 63)
           Scene                    BYTE              Scene number, value range from 0 to 15
           Done                     BOOL              Computation completed
VAR_OUTPUT Active                   BOOL              Computation ongoing
           Error                    BOOL              Indicates an error
           ErrorID                  ⮫ ERROR_CODE      Error class
               ErrorIdent           ⮫ ERROR_STRUCT Detailed error information
               SceneLevel           BYTE             Scene level of the ballast
VAR_IN_OUT     IOstrToken           ⮫ IH_INLN_MB_DAT Structure to handle data between the
                                    A                IH_S20DaliReadWrite and other Dali func‐
                                                     tion blocks.

      Min./max. and default values
      The following table lists the min./max. and default values as well as the
      application behavior of the function block inputs.
Table 857: Min./max. and default values as well as the response of the function block inputs of
IH_DaliQuerySceneLevel during application
Name            Type            Min. value      Max. value     Default value   Effective
Execute         BOOL            FALSE           TRUE           FALSE           Continuous
ShortAddress    BYTE            0               63             0               Rising edge at Exe‐
                                                                               cute
Scene           BYTE            0               15             0               Rising edge at Exe‐
                                                                               cute

1002 /    ctrlX PLC Engineering
1344      IH_DaliQuerySceneLevel

Functional description
The function block is used to read out the scene level of the ballast. The value
of the scene level is between 0 and 15. If the value of "SceneLevel" is 255, the
value is invalid or the scene is not configured. The function block is enabled
after the first PLC cycle by setting the "Execute" input to TRUE. Changed
input values are only applied with a new rising edge at the "Execute" input.
The "Active" output is set to TRUE during operation. The bit "Done" is set to
TRUE upon completion. The function block can be initialized again via a new
rising edge at the "Execute" input. If an error results during the operation, the
"Error" bit is set to TRUE. "ErrorID" and "ErrorIdent" show error information.
The error can be acknowledged via a rising edge at the "Execute" input.
Non-functional criteria
Call this function block to communicate with the Dali module via the
IH_S20DaliReadWrite function block.
Example of a function block
Instantiate the function block IH_S20DaliReadWrite before the IH_DaliQuery‐
SceneLevel function block can be instantiated to communicate with the Dali
module. The input/output variable stDaliToken exchanges data between the
function blocks IH_S20DaliReadWrite and IH_DaliQuerySceneLevel. Thus, this
variable has to be assigned to "IOstrToken" in both function blocks.
In the example, the IH_DaliQuerySceneLevel function block is configured to
query the scene level of scene number 8 from the ballast address: 2. A new
rising edge at the "bExecute" input, queries the scene level of a specific bal‐
last.

Variable declaration

VAR
  fbDaliQuerySceneLevel: IH_DaliQuerySceneLevel;
  bExecute: BOOL;
  stDaliToken: IH_INLN_DALI_TOKEN;
  bDone: BOOL;
  bActive: BOOL;
  bError: BOOL;
  enErrorID: ERROR_CODE;
  stErrorIdent: ERROR_STRUCT;
  bySceneLevel: BYTE;
END_VAR

Example

fbDaliQuerySceneLevel(
  Execute:= bExecute,
  ShortAddress:= BYTE#2,
  Scene:= BYTE#8,
  IOstrToken:= stDaliToken,
  Done=> bDone,
  Active=> bActive,
  Error=> bError,
  ErrorID=> enErrorID,
  ErrorIdent=> stErrorIdent,
  SceneLevel=> bySceneLevel);

                                             IH_DaliProgramShortAddress        1344

## 32.17 IH_DaliProgramShortAddress

      Brief description
      The function block IH_DaliProgramShortAddress assigns a short address to
      the ballasts by random address allocation or physical selection during ini‐
      tialization. The function block has to be called using the function block
      ⮫ IH_DaliReadWrite.

      Interface description

Table 858: Interface variables of the IH_DaliProgramShortAddress function block
I/O type       Name                Data type         Description
VAR_INPUT      Enable              BOOL              Function block active if TRUE
                                                     If TRUE, the physical selection is set. If
               PhysicalMode        BOOL
                                                     FALSE, the random allocation is set
                                                     All ballasts are selected if TRUE
               AddressMode         BOOL              If FALSE, ballasts without address are
                                                     selected
                                                     Number of ballasts to be assigned to the
               NoOfBallasts        BYTE
                                                     short address
VAR_OUTPUT Done                    BOOL              Computation completed
           Active                  BOOL              Computation ongoing
           Error                   BOOL              Indicates an error
           ErrorID                 BOOL              Error class
           ErrorIdent              ⮫ ERROR_CODE      Detailed error information
               WaitForResponse     ⮫ ERROR_STRUCT In PhysicalMode, waiting for the physical
                                                   response of the ballasts
               OpMode              IH_INLN_DALI_OP Current operation mode
                                   MODE
                                 ⮫ IH_INLN_DALI_O
                                 PMODE
               BallastsCompleted BYTE             Total number to addresses assigned to bal‐
                                                  lasts
VAR_IN_OUT     IOstrToken        ⮫ IH_INLN_DALI_T Structure to handle data between the
                                 OKEN             IH_S20DaliReadWrite and other Dali func‐
                                                  tion blocks.

1004 /    ctrlX PLC Engineering
1344      IH_DaliProgramShortAddress

Min./max. and default values
The following table lists the min./max. and default values as well as the
application behavior of the function block inputs.
Table 859: Min./max. and default values as well as the response of the function block inputs of
IH_DaliProgramShortAddress during application
Name               Type          Min. value      Max. value      Default value   Effective
Enable             BOOL          FALSE           TRUE            FALSE           Continuous
PhysicalMode       BOOL          FALSE           TRUE            FALSE           Rising    edge    at
                                                                                 Enable
AddressMode        BOOL          FALSE           TRUE            FALSE           Rising    edge    at
                                                                                 Enable
NoOfBallasts       BYTE          1               64              0               Rising    edge    at
                                                                                 Enable

Functional description
The function block assigns a short address to the ballasts by random address
allocation or physical selection during initialization.
If "PhysicalMode" is TRUE, the ballast is addressed in the physical selection
mode. Otherwise, the random allocation is used.
Different address modes are listed in the following and provide an overview
on the internal response of the function block.
Random allocation: (traversing during execution in the function block)
● The algorithm start with the "INITIALIZE" command for all ballasts or for
  ballasts without address
● Sending command: "RANDOMIZE": All ballasts get a random binary number
  (BRN)
● The search address is determined like the random address
● The control section searches the ballast with the lowest BRN using the
  algorithm "COMPARE". The ballast with the BRN is found
● The BRN is moved to the search address using IH_DaliSearchAddress.
● The found ballast gets a short address of 6 bits (StartAddress) by exe‐
  cuting the command "PROGRAM SHORT ADDRESS"
● The command "VERIFY SHORT ADDRESS" verifies the programmed short
  address
● The found ballast is removed from the search by executing the command
  "WITHDRAW"
● The algorithm is repeated from step 3 until the counter reaches the value
  of "NoOfballasts"
● If the counter reaches the value of "NoOfBallasts", traversing stops with the
  command "TERMINATE"
Physical addressing: (traversing during execution in the function block)
● The control section sends the command "INITIALIZE" to all ballasts or bal‐
   lasts without address
● The control section sends the command "Physical selection" to enable the
   physical address selection
● The control section repeats the command "QUERY SHORT ADDRESS" reg‐
   ularly until a ballast responds. The ballast responds by disconnecting its
   lamp
To select a ballast, disconnect and reconnect its lamp. (The lamp has to be
reconnected within 5 seconds.)

                                           IH_DaliProgramShortAddress          1344

● The selected ballast gets a short address of 6 bits by executing the com‐
  mand "PROGRAM SHORT ADDRESS"
● The available lamp reconnected to the ballast is found using IH_DaliQuer‐
  yStatus
● The control section sends "RECALL MIN LEVEL" and "RECALL MAX LEVEL"
  to the short address to receive a visual feedback of 5 seconds. This is
  confirmed by the successful assignment of the short address.
● The algorithm is repeated from step 3 until the counter reaches the value
    of "NoOfballasts"
● If the counter reaches the value of "NoOfBallasts", traversing stops with the
    command "TERMINATE"
If "AddressMode" is TRUE, all ballasts are selected. If it is FALSE, ballasts

without short address are selected for addressing. While the function block is
waiting for a physical response from the ballast, "WaitForResponse" is TRUE.
"ballastsCompleted" counts the number of completely addressed ballasts.
"OpMode" specified the current operating mode of the function block.
The function block is enabled after the first PLC cycle by setting the "Enable"
input to TRUE. Changed input values are only applied with a new rising edge
at the “Enable" input. The "Active" output is set to TRUE during operation.
The bit "Done" is set to TRUE upon completion. The function block can be
initialized again via a new rising edge at the "Execute" input. If an error results
during the operation, the "Error" bit is set to TRUE. "ErrorID" and "ErrorIdent"
show error information.
The error can be acknowledged via a rising edge at the "Enable" input.
To be considered when handling
● The lamp has to be on (ON) when addressing all ballasts
● When addressing is completed using IH_DaliProgramShortAddress, switch
   off the Dali system and switch it on again to allow re-addressing
Non-functional criteria
Call this function block to communicate with the Dali module via the
IH_S20DaliReadWrite function block.
Example of a function block
Instantiate the function block IH_S20DaliReadWrite before the IH_DaliProg‐
ramShortAddress function block can be instantiated to communicate with the
Dali module. The input/output variable "stDaliToken" exchanges data between
the function blocks IH_S20DaliReadWrite and IH_DaliProgramShortAddress.
Thus, this variable has to be assigned to "IOstrToken" in both function blocks.
In the examples, the function block IH_DaliProgramShortAddress assigns
addresses to ballasts using the random allocation or the physical selection. A
new rising edge at the "bExecute" input assigns the addresses to the ballasts.
Here, "NoOfballasts" is BYTE#20.

Variable declaration

1006 /    ctrlX PLC Engineering
1344      IH_DaliProgramShortAddress

VAR
  fbDaliProgramShortAddress: IH_DaliProgramShortAddress;
  bEnable: BOOL;
  stDaliToken: IH_INLN_DALI_TOKEN;
  bDone: BOOL;
  bActive: BOOL;
  bError: BOOL;
  enErrorID: ERROR_CODE;
  stErrorIdent: ERROR_STRUCT;
  bWaitForResponse: BOOL;
  enOpMode: IH_INLN_DALI_OPMODE;
  byBallastsCompleted: BYTE;
END_VAR

This function block uses a random allocation to address all available ballasts.
Addressing starts at zero and is incremented until no further ballasts can be
found.

Random address allocation for all ballasts

fbDaliProgramShortAddress(
  Enable:= bEnable,
  PhysicalMode:= FALSE,
  AddressMode:= TRUE,
  NoOfBallasts:= BYTE#20,
  IOstrToken:= stDaliToken,
  Done=> bDone,
  Active=> bActive,
  Error=> bError,
  ErrorID=> enErrorID,
  ErrorIdent=> stErrorIdent,
  WaitForResponse=> bWaitForResponse,
  OpMode=> enOpMode,
  BallastsCompleted=> byBallastsCompleted);

This function block uses the physical selection only for ballasts without short
address. It browses through the network for available addresses and assigns
them to the physically selected ballasts.

Physical selection for ballasts without short address

fbDaliProgramShortAddress(
  Enable:= bEnable,
  PhysicalMode:= TRUE,
  AddressMode:= FALSE,
  NoOfBallasts:= BYTE#20,
  IOstrToken:= stDaliToken,
  Done=> bDone,
  Active=> bActive,
  Error=> bError,
  ErrorID=> enErrorID,
  ErrorIdent=> stErrorIdent,
  WaitForResponse=> bWaitForResponse,
  OpMode=> enOpMode,
  BallastsCompleted=> byBallastsCompleted);

                                                     IH_DaliStoreParameter       1344

## 32.18 IH_DaliStoreParameter

      Brief description
      The function block IH_DaliStoreParameter saves the content of the DTR to
      the respective parameters of the ballast, e.g. "Fade Rate", "Fade Time", "Min
      Level", "Max Level", "Power On Level", "System Failure Level". The function
      block has to be called using the function block ⮫ IH_DaliReadWrite.

      Interface description

Table 860: Interface variables of the IH_DaliStoreParameter function block
I/O type       Name                Type               Description
VAR_INPUT      Execute             BOOL               Rising edge starts computation
                                   ⮫ IH_INLN_DALI_PA
               Parameter                             Enumeration for parameter selection
                                   RAMETER
                                                     The parameter value depends on the selec‐
               ParameterValue      BYTE
                                                     tion in StoreParameter
               AddressType         ⮫ IH_INLN_DALI_A Enumeration to select the address type
                                   DDRTYPE
                                                     The address depends on the selected type
                                                     under AddressType.
               Address             BYTE              Values between 0 and 63 are possible for
                                                     short addresses and 0 to 15 for group
                                                     addresses.
VAR_OUTPUT Done                    BOOL              Computation completed
           Active                  BOOL              Computation ongoing
           Error                   BOOL              Indicates an error
               ErrorID             ⮫ ERROR_CODE       Error class
               ErrorIdent          ⮫ ERROR_STRUCT Detailed error information
VAR_IN_OUT                                          Structure to handle data between the
                                   ⮫ IH_INLN_DALI_T
               IOstrToken                           IH_S20DaliReadWrite and other Dali func‐
                                   OKEN
                                                    tion blocks.

1008 /    ctrlX PLC Engineering
1344      IH_DaliStoreParameter

Min./max. and default values
The following table lists the min./max. and default values as well as the
application behavior of the function block inputs.
Table 861: Min./max. and default values as well as the response of the function block inputs of
IH_DaliStoreParameter during application
Name               Type          Min. value       Max. value   Default value        Effective
Execute            BOOL          FALSE            TRUE         FALSE                Continuous
Parameter          IH_INLN_DALI_ FADE_RATE        SYSTEM_FAILU FADE_RATE            Rising edge at Exe‐
                   PARAMETER                      RE_LEVEL                          cute
Parameter‐         BYTE          -                -            -                    Rising edge at Exe‐
Value                                                                               cute
AddressType        IH_INLN_DALI_ SHORTADDR        BROADCAST        SHORTADDR        Rising edge at Exe‐
                   ADDRTYPE                                                         cute
Address            BYTE          0                Short address 0                   Rising edge at Exe‐
                                                  = 63                              cute
                                                  Group address
                                                  = 15

Functional description
The function block IH_DaliStoreParameter saves the content of the DTR to the
respective parameters, e.g. "Fade Rate", "Fade Time", "Min Level", "Max Level",
"Power On Level", "System Failure Level", individual ballasts, a group of bal‐
lasts or all ballasts. This depends on the type selected under "AddressType".
Parameters can be selected from the parameter list. All parameter values can
be entered using the input variable "ParameterValue".
The function block is enabled after the first PLC cycle by setting the "Execute"
input to TRUE. Changed input values are only applied with a new rising edge
at the "Execute" input. The "Active" output is set to TRUE during operation.
The bit "Done" is set to TRUE upon completion. The function block can be
initialized again via a new rising edge at the "Execute" input. If an error results
during the operation, the "Error" bit is set to TRUE. "ErrorID" and "ErrorIdent"
show error information. The error can be acknowledged via a rising edge at
the "Execute" input.
Non-functional criteria
Call this function block to communicate with the Dali module via the
IH_S20DaliReadWrite function block.
Example of a function block
Instantiate the function block IH_S20DaliReadWrite before the IH_DaliStore‐
Parameter function block can be instantiated to communicate with the Dali
module. The input/output variable "stDaliToken" exchanges data between the
function blocks IH_S20DaliReadWrite and IH_DaliStoreParameter. Thus, this
variable has to be assigned to "IOstrToken" in both function blocks.
In the example, the function block IH_DaliStoreParameter saves the value 120
to the parameter "Max Level" of the ballast with the short address 1.

Variable declaration

                                                       IH_DaliReset      1344

VAR
  fbDaliStoreParameter     : IH_DaliStoreParameter;
  bExecute             : BOOL;
  stDaliToken          : IH_INLN_DALI_TOKEN;
  bDone                : BOOL;
  bActive              : BOOL;
  bError               : BOOL;
  enErrorID            : ERROR_CODE;
  stErrorIdent         : ERROR_STRUCT;
END_VAR

Example

fbDaliStoreParameter(
  Execute:= bExecute,
  Parameter := IH_INLN_DALI_PARAMETER.MAX_LEVEL,
  ParameterValue := BYTE#120,
  AddressType:= IH_INLN_DALI_ADDRTYPE.SHORTADDR,
  Address:= BYTE#1,
  IOstrToken:= stDaliToken,
  Done=> bDone,
  Active=> bActive,
  Error=> bError,
  ErrorID=> enErrorID,
  ErrorIdent=> stErrorIdent);

## 32.19 IH_DaliReset

Brief description
The IH_DaliReset function block resets all values in the persistent memory
of the ballast. The function block has to be called using the function block
⮫ IH_DaliReadWrite.

1010 /    ctrlX PLC Engineering
1344      IH_DaliReset

     Interface description

Table 862: Interface variables of the IH_DaliReset function block
I/O type           Name                Data type          Description
VAR_INPUT          Execute             BOOL               Rising edge starts computation
                                       ⮫ IH_INLN_DALI_A
                   AddressType                          Enumeration to select the address type.
                                       DDRTYPE
                                                        The address depends on the selected type
                                                        under AddressType. Values between 0 and
                   Address             BYTE
                                                        63 are possible for short addresses and 0
                                                        to 15 for group addresses.
VAR_OUTPUT Done                        BOOL             Computation completed
           Active                      BOOL             Computation ongoing
           Error                       BOOL             Indicates an error
                   ErrorID             ⮫ ERROR_CODE       Error class
                   ErrorIdent          ⮫ ERROR_STRUCT Detailed error information
VAR_IN_OUT                                              Structure to handle data between the
                                       ⮫ IH_INLN_DALI_T
                   IOstrToken                           IH_S20DaliReadWrite and other Dali func‐
                                       OKEN
                                                        tion blocks.

     Min./max. and default values
 The following table lists the min./max. and default values as well as the
 application behavior of the function block inputs.
Table 863: Min./max. and default values as well as the response of the function block inputs of
IH_DaliReset during application
Name               Type          Min. value        Max. value      Default value   Effective
Execute            BOOL          FALSE             TRUE            FALSE           Continuous
                   IH_INLN_DALI_                                                   Rising edge at Exe‐
AddressType                      SHORTADDR         BROADCAST       SHORTADDR
                   ADDRTYPE                                                        cute
                                                   Group = 15                      Rising edge at Exe‐
Address            BYTE            0                               0
                                                   Ballast = 63                    cute

                                                           IH_DaliReset        1344

Functional description
The IH_DaliReset function block resets all values in the persistent memory
of the ballast. The following table lists the default values for resetting. A
single ballast, a group of ballasts or all connected ballasts can be selected via
"AddressType". While the "Reset" command is executed, the ballast might not
be able anymore to receive further commands within the next 300 ms.
The function block is enabled after the first PLC cycle by setting the "Execute"
input to TRUE. Changed input values are only applied with a new rising edge
at the "Execute" input. The "Active" output is set to TRUE during operation.
The bit "Done" is set to TRUE upon completion. The function block can be
initialized again via a new rising edge at the "Execute" input. If an error results
during the operation, the "Error" bit is set to TRUE. "ErrorID" and "ErrorIdent"

show error information. The error can be acknowledged via a rising edge at
the "Execute" input.
The reset values listed in the following can depend on the manufacturer, e.g.,
"Physical Min Level".
Table:
Variable                                      Reset value
ACTUAL DIM LEVEL                              254
POWER ON LEVEL                                254
SYSTEM FAILURE LEVEL                          254
MIN LEVEL                                     PHYSICAL MIN LEVEL
MAX LEVEL                                     254
FADE RATE                                     7 (45 steps/s)
FADE TIME                                     0 (NO DIMMING)
SHORT ADDRESS                                 NO CHANGE
SEARCH ADDRESS                                FF FF FF
RANDOM ADDRESS                                FF FF FF
GROUP 0-7                                     0000 0000 (NO GROUP)
GROUP 8-15                                    0000 0000 (NO GROUP)
SCENE 0-15                                    255 (MASK)
                                              0?100???
STATUS INFORMATION
                                              ? : Undefined
VERSION NUMBER                                NO CHANGE
DEVICE TYPE                                   0
PHYSICAL MIN LEVEL                            FACTORY SETTING
Non-functional criteria
Call this function block to communicate with the Dali module via the
IH_S20DaliReadWrite function block.
Example of a function block
Instantiate the function block IH_S20DaliReadWrite before the IH_DaliReset
function block can be instantiated to communicate with the Dali module.
The input/output variable "stDaliToken" exchanges data between the function
blocks IH_S20DaliReadWrite and IH_DaliReset. Thus, this variable has to be
assigned to "IOstrToken" in both function blocks.
In the example, the IH_DaliReset function block resets all values in the persis‐
tent memory of the ballast. In the first example, the ballast with address 1 is
reset. In the second example, all ballasts connected to the Dali bus are reset
via a broadcast command.

1012 /    ctrlX PLC Engineering
1344      IH_DaliQueryDTR

Variable declaration

VAR
  fbDaliReset           : IH_DaliReset;
  bExecute                : BOOL;
  stDaliToken             : IH_INLN_DALI_TOKEN;
  bDone                   : BOOL;
  bActive                 : BOOL;
  bError                  : BOOL;
  enErrorID               : ERROR_CODE;
  stErrorIdent            : ERROR_STRUCT;

END_VAR

Program with AddressType = Short Address (short address)

fbDaliReset(
  Execute:= bExecute,
  AddressType:= IH_INLN_DALI_ADDRTYPE.SHORTADDR,
  Address:= BYTE#1,
  IOstrToken:= stDaliToken,
  Done=> bDone,
  Active=> bActive,
  Error=> bError,
  ErrorID=> enErrorID,
  ErrorIdent=> stErrorIdent);

Program with AddressType = Broadcast

fbDaliReset(
  Execute:= bExecute,
  AddressType:= IH_INLN_DALI_ADDRTYPE.BROADCAST,
  Address:= ,
  IOstrToken:= stDaliToken,
  Done=> bDone,
  Active=> bActive,
  Error=> bError,
  ErrorID=> enErrorID,
  ErrorIdent=> stErrorIdent);

## 32.20 IH_DaliQueryDTR

Brief description
The function block IH_DaliQueryDTR reads out the content of the Data
Transfer Register (DTR) of the ballasts connected to the Dali bus. This func‐
tion block has to be called using the function block ⮫ IH_DaliReadWrite.

                                                             IH_DaliQueryDTR       1344

      Interface description

Table 864: Interface variables of the IH_DaliQueryDTR function block
I/O type   Name                    Data type          Description
VAR_INPUT  Execute                 BOOL               Rising edge starts computation
VAR_OUTPUT Done                    BOOL               Computation completed
           Active                  BOOL               Computation ongoing
           Error                   BOOL               Indicates an error
               ErrorID             ⮫ ERROR_CODE       Error class
               ErrorIdent          ⮫ ERROR_STRUCT Detailed error information
               ContentDTR          BYTE             DTR content
VAR_IN_OUT                                          Structure to handle data between the
                                   ⮫ IH_INLN_DALI_T
               IOstrToken                           IH_S20DaliReadWrite and other Dali func‐
                                   OKEN
                                                    tion blocks.

      Min./max. and default values
    The following table lists the min./max. and default values as well as the
    application behavior of the function block inputs.
Table 865: Min./max. and default values as well as the response of the function block inputs of
IH_DaliQueryDTR during application
Name            Type            Min. value     Max. value      Default value     Effective
Execute         BOOL            FALSE          TRUE            FALSE             Continuous

1014 /    ctrlX PLC Engineering
1344      IH_DaliQueryDTR

Functional description
The function block IH_DaliQueryDTR reads out the content of the DTR (Data
Transfer Register) of the ballasts connected to the Dali bus. If "Execute" is
TRUE, the DTR of all connected ballasts is read and the DTR content value is
saved in the output variable "ContentDTR".
The function block is enabled after the first PLC cycle by setting the "Execute"
input to TRUE. Changed input values are only applied with a new rising edge
at the "Execute" input. The "Active" output is set to TRUE during operation.
The bit "Done" is set to TRUE upon completion. The function block can be
initialized again via a new rising edge at the "Execute" input. If an error results
during the operation, the "Error" bit is set to TRUE. "ErrorID" and "ErrorIdent"
show error information. The error can be acknowledged via a rising edge at
the "Execute" input.
Non-functional criteria
Call this function block to communicate with the Dali module via the
IH_S20DaliReadWrite function block.
Example of a function block
Instantiate the function block IH_S20DaliReadWrite before the IH_DaliQuer‐
yDTR function block can be instantiated to communicate with the Dali
module. The input/output variable "stDaliToken" exchanges data between the
function blocks IH_S20DaliReadWrite and IH_DaliQueryDTR. Thus, this vari‐
able has to be assigned to "IOstrToken" in both function blocks.
In the example, the function block IH_DaliQueryDTR reads the content of the
DTR (Data Transfer Register) of the ballasts connected to the Dali bus. If
"Execute" is TRUE, the DTR of all connected ballasts is read and the DTR
content value is saved in the output variable "ContentDTR".

Variable declaration

VAR

  fbDaliQueryDTR: IH_DaliQueryDTR;
  bExecute: BOOL;
  stDaliToken: IH_INLN_DALI_TOKEN;
  bDone: BOOL;
  bActive: BOOL;
  bError: BOOL;
  enErrorID: ERROR_CODE;
  stErrorIdent: ERROR_STRUCT;
  byContentDTR: BYTE;

END_VAR

Example

fbDaliQueryDTR(
  Execute:= bExecute,
  IOstrToken:= stDaliToken,
  Done=> bDone,
  Active=> bActive,
  Error=> bError,
  ErrorID=> enErrorID,
  ErrorIdent=> stErrorIdent,
  ContentDTR=> byContentDTR);

                                                    IH_DaliQueryParameter        1344

## 32.21 IH_DaliQueryParameter

      Brief description
      The function block IH_DaliQueryParameter reads the parameters "Fade Rate",
      "Fade Time", "Min Level", "Max Level", "Power On Level", "Physical Min Level"
      and "System Failure Level" of the ballast. The function block has to be called
      using the function block ⮫ IH_DaliReadWrite.

      Interface description

Table 866: Interface variables of the IH_DaliQueryParameter function block
I/O type       Name                Data type         Description
VAR_INPUT      Execute             BOOL              Rising edge starts computation
               Address             BYTE              Ballast address (0 to 63 or 255)
                                                     Address        SizeOf Param‐ Number of
                                                                    eterValue      ballasts to be
                                                                                   read
                                                     0-63           1              1 ballast
                                                     255            64             64 ballasts
                                                     255            Number of      Number of
                                                                    ballasts       ballasts in
                                                                    from 1 to 64 SizeOfPara‐
                                                                                   meterValue
               Parameter           ⮫ IH_INLN_DALI_PA Enumeration for parameter selection. For
                                   RAMETER           more information, go to the section on
                                                     structures and enumerations
           SizeOfParameter‐        UINT              Size of the parameter value (1 to 64)
           Value
           ParameterValueAdr POINTER_TO_BYTE ParameterValue address. (1 byte or array
                                             from 1 to 64)
                                             Address value Size of the ParameterValue
                                                            array
                                             0 to 63        1 byte
                                             255            Number of ballasts (1 to 64)
VAR OUTPUT Done              BOOL            Computation completed
           Active            BOOL            Computation ongoing
           Error             BOOL            Indicates an error
           ErrorID           ⮫ ERROR_CODE    Error class
               ErrorIdent          ⮫ ERROR_STRUCT Detailed error information
VAR_IN_OUT     IOstrToken                           Structure to handle data between the
                                   ⮫ IH_INLN_DALI_T
                                                    IH_S20DaliReadWrite and other Dali func‐
                                   OKEN
                                                    tion blocks.

1016 /    ctrlX PLC Engineering
1344      IH_DaliQueryParameter

Min./max. and default values
The following table lists the min./max. and default values as well as the
application behavior of the function block inputs.
Table 867: Min./max. and default values as well as the response of the function block inputs of
IH_DaliQueryParameter during application
Name               Type           Min. value      Max. value       Default value    Effective
Execute            BOOL           FALSE           TRUE             FALSE            Continuous
Address            BYTE           0               255              0                Rising edge at Exe‐
                                                                                    cute
Parameter          IH_INLN_DALI_ MAX_LEVEL        PHYS‐        MAX_LEVEL            Rising edge at Exe‐
                   PARAMETER                      ICAL_MIN_LEV                      cute
                                                  EL
SizeOfParame‐ UINT                1               64           1                    Rising edge at Exe‐
terValue                                                                            cute

Functional description
The function block IH_DaliQueryParameter reads the parameters of a ballast.
The function block reads the parameters, e.g. "Fade Rate", "Fade Time", "Min
Level", "Max Level", "Power On Level", "Physical Min Level" and "System
Failure Level" selected in the enumeration of IH_INLN_DALI_PARAMETER. The
response depends on the selection in "Address" and "SizeOfParameterValue".
● If the address is 0-63 and SizeOfParameterValue = 1, the response is 1 byte
    in ParameterValue
● If the address is 255 and SizeOfParameterValue = 10, the response is 1
    byte per ballast (address 0-9), i.e. in total 10 bytes in ParameterValue
● If the address is 255 and SizeOfParameterValue = 64, the response is 1
    byte per ballast (address 0-63), i.e. in total 64 bytes in ParameterValue
For FADE_RATE_AND_FADE_TIME, the command response is 1 byte and
includes XXXX YYYY. XXXX stands for FADE TIME and YYYY for FADE RATE.
If the ballast does not respond, 16#FF is assumed in ParameterValue. If the
value of the entered address is between 0 and 63, the respective ballast is
read out. If the address value is 255, the function block reads out the number
of ballasts specified in SizeOfParameterLevel.
The function block is enabled after the first PLC cycle by setting the "Execute"
input to TRUE. Changed input values are only applied with a new rising edge
at the "Execute" input. The "Active" output is set to TRUE during operation.
The bit "Done" is set to TRUE upon completion. The function block can be
initialized again via a new rising edge at the "Execute" input. If an error results
during the operation, the "Error" bit is set to TRUE. "ErrorID" and "ErrorIdent"
show error information. The error can be acknowledged via a rising edge at
the "Execute" input.
Non-functional criteria
Call this function block to communicate with the Dali module via the
IH_S20DaliReadWrite function block.
Example of a function block
Instantiate the function block IH_S20DaliReadWrite before the IH_DaliQuery‐
Parameter function block can be instantiated to communicate with the Dali
module. The input/output variable "stDaliToken" exchanges data between the
function blocks IH_S20DaliReadWrite and IH_DaliQueryParameter. Thus, this
variable has to be assigned to "IOstrToken" in both function blocks.

                                              IH_DaliQueryParameter        1344

Example 1
In the example, the function block IH_DaliQueryParameter reads out "Max
Level" of a single ballast.
The function block reads the parameter "Max Level" of the ballast with
address 2 and saves it to the variable "byParameterValue".

Variable declaration

VAR
  fbDaliQueryParameter: IH_DaliQueryParameter;
  bExecute: BOOL;
  byParameterValue: byte;

  stDaliToken: IH_INLN_DALI_TOKEN;
  bDone: BOOL;
  bActive: BOOL;
  bError: BOOL;
  enErrorID: ERROR_CODE;
  stErrorIdent: ERROR_STRUCT;
END_VAR

Implementation

fbDaliQueryParameter(
  Execute:= bExecute,
  Address:= BYTE#2,
  Parameter:= IH_INLN_DALI_PARAMETER.MAX_LEVEL,
  SizeOfParameterValue:= SIZEOF(byParameterValue),
  ParameterValueAdr:= ADR(byParameterValue),
  IOstrToken:= stDaliToken,
  Done=> bDone,
  Active=> bActive,
  Error=> bError,
  ErrorID=> enErrorID,
  ErrorIdent=> stErrorIdent);

Example 2
In this example, the function block IH_DaliQueryActualLevel reads out "Min
Level" of all 63 ballasts.
The function block reads the parameter "Min Level" of the 63 ballasts and
saves them to the "arParameterValue" array.
An array of 63 bytes has to be created and the address of the array has to be
assigned to "ParameterValueAdr".
The size of the data array has to correspond to the number of ballasts. Other‐
wise, severe malfunctions can occur in the PLC application.

Variable declaration

1018 /    ctrlX PLC Engineering
1344      IH_DaliQueryGroup

VAR
  fbDaliQueryParameter: IH_DaliQueryParameter;
  bExecute: BOOL;
  stDaliToken: IH_INLN_DALI_TOKEN;
  bDone: BOOL;
  bActive: BOOL;
  bError: BOOL;
  enErrorID: ERROR_CODE;
  stErrorIdent: ERROR_STRUCT;
  arParameterValue: ARRAY[0..63] OF BYTE;
END_VAR

Implementation

fbDaliQueryParameter(
  Execute:= bExecute,
  Address:= BYTE#16#FF,
  Parameter:= IH_INLN_DALI_PARAMETER.PHYSICAL_MIN_LEVEL,
  SizeOfParameterValue:= SIZEOF(arParameterValue),
  ParameterValueAdr:= ADR(arParameterValue),
  IOstrToken:= stDaliToken,
  Done=> bDone,
  Active=> bActive,
  Error=> bError,
  ErrorID=> enErrorID,
  ErrorIdent=> stErrorIdent);

## 32.22 IH_DaliQueryGroup

Brief description
The IH_DaliQueryGroup function block identifies the group of a ballast. The
function block has to be called using the function block ⮫ IH_DaliReadWrite.

                                                       IH_DaliQueryGroup       1344

      Interface description

Table 868: Interface variables of the IH_DaliQueryGroup function block

I/O type       Name                Data type       Description
VAR_INPUT      Execute             BOOL            Rising edge starts computation
Address             BYTE            Ballast address (0 to 63 or 255)
                                    Address        SizeOf Group Number of
                                                                  read ballasts
                                    0-63           1              1 ballast
                                    255            64             64 ballasts
                                    255            Number of      Number of
                                                   ballasts       ballasts in
                                                   from 1 to 64 SizeOfGroup
GroupRange          BOOL            FALSE = Query group 0 to 7
                                    TRUE = Query groups 8 to 15
SizeOfGroup         UINT            Size of the group (1 to 64).
GroupAdr            POINTER_TO_BYTE Address of the group (1 byte or array from
                                    1 to 64)
                                    Address value Size of the group
                                    0 to 63        1 BYTE
                                    255            Number of ballasts (1 to 64)
VAR OUTPUT Done                    BOOL            Computation completed
Active                  BOOL            Computation ongoing
Error                   BOOL            Indicates an error
ErrorID                 ⮫ ERROR_CODE    Error class
ErrorIdent          ⮫ ERROR_STRUCT Detailed error information
VAR_IN_OUT     IOstrToken                           Structure to handle data between the
                    ⮫ IH_INLN_DALI_T
                                     IH_S20DaliReadWrite and other Dali func‐
                    OKEN
                                     tion blocks.

1020 /    ctrlX PLC Engineering
1344      IH_DaliQueryGroup

Min./max. and default values
The following table lists the min./max. and default values as well as the
application behavior of the function block inputs.
Table 869: Min./max. and default values as well as the response of the function block inputs of
IH_DaliQueryGroup during application
Name               Type           Min. value      Max. value       Default value    Effective
Execute            BOOL           FALSE           TRUE             FALSE            Continuous
Address            BYTE           0               255              0                Rising edge at Exe‐
                                                                                    cute
GroupRange         BOOL           FALSE           TRUE             FALSE            Rising edge at Exe‐
                                                                                    cute
SizeOfGroup        UINT           1               64               1                Rising edge at Exe‐
                                                                                    cute

Functional description
The IH_DaliQueryGroup function block identifies the group of a ballast.
● If the address is 0-63 and SizeOfGroup = 1, the response is 1 byte in
    GroupAdr
● If the address is 255 and SizeOfGroup = 10, the response is 1 byte per
    ballast (address 0-9), i.e. in total 10 bytes in GroupAdr
● If the address is 255 and SizeOfGroup = 64, the response is 1 byte per
    ballast (address 0-63), i.e. in total 64 bytes in GroupAdr
The function block is enabled after the first PLC cycle by setting the "Execute"
input to TRUE. Changed input values are only applied with a new rising edge
at the "Execute" input. The "Active" output is set to TRUE during operation.
The bit "Done" is set to TRUE upon completion. The function block can be
initialized again via a new rising edge at the "Execute" input. If an error results
during the operation, the "Error" bit is set to TRUE. "ErrorID" and "ErrorIdent"
show error information. The error can be acknowledged via a rising edge at
the "Execute" input.
Non-functional criteria
Call this function block to communicate with the Dali module via the
IH_S20DaliReadWrite function block.
Example of a function block
Instantiate the function block IH_S20DaliReadWrite before the IH_DaliQuer‐
yGroup function block can be instantiated to communicate with the Dali
module. The input/output variable "stDaliToken" exchanges data between the
function blocks IH_S20DaliReadWrite and IH_DaliQueryGroup. Thus, this vari‐
able has to be assigned to "IOstrToken" in both function blocks.

Example 1
In the example, the function block IH_DaliQueryGroup reads out "Max Level"
of a single ballast.
The function block identifies the group range (0 to 7) of ballast 2 and saves it
to the variable "byQueryGroup".

Variable declaration

                                                  IH_DaliQueryGroup        1344

VAR
  fbDaliQueryGroup: IH_DaliQueryGroup;
  bExecute: BOOL;
  byQueryGroup: BYTE;
  stDaliToken: IH_INLN_DALI_TOKEN;
  bDone: BOOL;
  bActive: BOOL;
  bError: BOOL;
  enErrorID: ERROR_CODE;
  stErrorIdent: ERROR_STRUCT;
END_VAR

Implementation

fbDaliQueryGroup(
  Execute:= bExecute,
  Address:= BYTE#2,
  GroupRange:= FALSE,
  SizeOfGroup:=SIZEOF(byQueryGroup),
  GroupAdr:= ADR(byQueryGroup),
  IOstrToken:= stDaliToken,
  Done=> bDone,
  Active=> bActive,
  Error=> bError,
  ErrorID=> enErrorID,
  ErrorIdent=> stErrorIdent);

Example 2
In this example, the function block IH_DaliQueryGroup identifies the group
range (8 to 15) of all 63 ballasts.
The function block identifies the group range (8 to 15) of all 63 ballasts and
saves it to the array "arQueryGroup".
An array of 63 bytes has to be created and the address of the array has to be
assigned to "GroupAdr".
The size of the array is specified in "SizeOfGroup". If the actual array is
smaller than the value in the variable "SizeOfGroup", data can be written to
another address. This can cause malfunctions in the application.

Variable declaration

VAR
  fbDaliQueryGroup: IH_DaliQueryGroup;
  bExecute: BOOL;
  stDaliToken: IH_INLN_DALI_TOKEN;
  bDone: BOOL;
  bActive: BOOL;
  bError: BOOL;
  enErrorID: ERROR_CODE;
  stErrorIdent: ERROR_STRUCT;
  arQueryGroup: ARRAY[0..63] OF BYTE;
END_VAR

Implementation

1022 /    ctrlX PLC Engineering
1344      IH_DaliQueryRandomAddress

     fbDaliQueryGroup(
       Execute:= bExecute,
       Address:= BYTE#16#FF,
       GroupRange:= TRUE,
       SizeOfGroup:= SIZEOF(arQueryGroup),
       GroupAdr:= ADR(arQueryGroup),
       IOstrToken:= stDaliToken,
       Done=> bDone,
       Active=> bActive,
       Error=> bError,
       ErrorID=> enErrorID,
       ErrorIdent=> stErrorIdent);

## 32.23 IH_DaliQueryRandomAddress

     Brief description
     The IH_DaliQueryRandomAddress function block is used to read out the
     random address of the ballast. The function block has to be called using the
     function block ⮫ IH_DaliReadWrite.

     Interface description

Table 870: Interface variables of the IH_DaliQueryRandomAddress function block
I/O type           Name               Data type          Description
VAR_INPUT          Execute            BOOL               Rising edge starts computation
                                                         TRUE = Query random address in Broadcast
                   Broadcast          BOOL               mode. FALSE = Query random address of
                                                         the ballast specified in ShortAddress
           ShortAddress               BYTE               Short address of the ballast (0 to 63)
           Done                       BOOL               Computation completed
           Active                     BOOL               Computation ongoing
VAR_OUTPUT Error                      BOOL               Indicates an error
                   ErrorID            ⮫ ERROR_CODE       Error class
                   ErrorIdent     ⮫ ERROR_STRUCT         Detailed error information
                   RandomAddressH BYTE                 High-order byte of the random address
                   RandomAddressM BYTE                 Middle byte of the random address
                   RandomAddressL BYTE                 Low-order byte of the random address
VAR_IN_OUT                                             Structure to handle data between the
                                      ⮫ IH_INLN_DALI_T
                   IOstrToken                          IH_S20DaliReadWrite and other Dali func‐
                                      OKEN
                                                       tion blocks.

                                          IH_DaliQueryRandomAddress            1344

Min./max. and default values
The following table lists the min./max. and default values as well as the
application behavior of the function block inputs.
Table 871: Min./max. and default values as well as the response of the function block inputs of
IH_DaliQueryRandomAddress during application
Name            Type             Min. value      Max. value       Default value    Effective
Execute         BOOL             FALSE           TRUE             FALSE            Continuous
Broadcast       BOOL             FALSE           TRUE             FALSE            Rising edge at Exe‐
                                                                                   cute
ShortAddress    BYTE             0               63               0                Rising edge at Exe‐
                                                                                   cute

Functional description
The IH_DaliQueryRandomAddress function block is used to read out the
random address of the ballast. The function block reads the 8 high-order bits,
8 mean bits and 8 low-order bits of a random address. The result can be
retrieved via the output variables "RandomAddressH", "RandomAddressM" and
"RandomAddressL".
If "Broadcast" is TRUE, the random address is queried using the broadcast
command. The individual ballasts have to be connected in the Broadcast
mode. Otherwise, a device error is issued during the query. If "Broadcast"
is FALSE, the random address of the ballast specified in "ShortAddress" is
queried.
The function block is enabled after the first PLC cycle by setting the "Execute"
input to TRUE. Changed input values are only applied with a new rising edge
at the "Execute" input. The "Active" output is set to TRUE during operation.
The bit "Done" is set to TRUE upon completion. The function block can be
initialized again via a new rising edge at the "Execute" input. If an error results
during the operation, the "Error" bit is set to TRUE. "ErrorID" and "ErrorIdent"
show error information. The error can be acknowledged via a rising edge at
the "Execute" input.
Non-functional criteria
Call this function block to communicate with the Dali module via the
IH_S20DaliReadWrite function block.
Example of a function block
Instantiate the function block IH_S20DaliReadWrite before the IH_DaliQueryR‐
andomAddress function block can be instantiated to communicate with the
Dali module. The input/output variable "stDaliToken" exchanges data between
the function blocks IH_S20DaliReadWrite and IH_DaliQueryRandomAddress.
Thus, this variable has to be assigned to "IOstrToken" in both function blocks.

Example 1
In the example, the IH_DaliQueryRandomAddress function block is used to
query the random address of a single ballast.
The function block reads the random address of ballast 2 and saves them to
the variables "byRandomAddressH", "byRandomAddressM" and "byRandomAd‐
dressL".

Variable declaration

1024 /    ctrlX PLC Engineering
1344      IH_DaliQueryRandomAddress

VAR
  fbDaliQueryRandomAddress: IH_DaliQueryRandomAddress;
  bExecute: BOOL;
  stDaliToken: IH_INLN_DALI_TOKEN;
  bDone: BOOL;
  bActive: BOOL;
  bError: BOOL;
  enErrorID: ERROR_CODE;
  stErrorIdent: ERROR_STRUCT;
  byRandomAddressH: BYTE;
  byRandomAddressM: BYTE;
  byRandomAddressL: BYTE;
END_VAR

Implementation

fbDaliQueryRandomAddress(
  Execute:= bExecute,
  Broadcast:= FALSE,
  ShortAddress:= BYTE#2,
  IOstrToken:= stDaliToken,
  Done=> bDone,
  Active=> bActive,
  Error=> bError,
  ErrorID=> enErrorID,
  ErrorIdent=> stErrorIdent,
  RandomAddressH=> byRandomAddressH,
  RandomAddressM=> byRandomAddressM,
  RandomAddressL=> byRandomAddressL);

Example 2
The function block reads the random accesses of all ballasts and saves them
to the variables "byRandomAddressH", "byRandomAddressM" and "byRando‐
mAddressL". If a random address of a ballast differs from the random address
of another ballast in the Broadcast mode, the Dali system issues the error
"Invalid response".

Implementation

fbDaliQueryRandomAddress(
  Execute:= bExecute,
  Broadcast:= TRUE,
  ShortAddress:= ,
  IOstrToken:= stDaliToken,
  Done=> bDone,
  Active=> bActive,
  Error=> bError,
  ErrorID=> enErrorID,
  ErrorIdent=> stErrorIdent,
  RandomAddressH=> byRandomAddressH,
  RandomAddressM=> byRandomAddressM,
  RandomAddressL=> byRandomAddressL);

                                                                        Data types      1344

## 32.24 Data types

### 32.24.1 IH_INLN_DALI_TOKEN

    This structure is internally used to exchange data between ⮫ IH_DaliReadWrite
    and other Dali function blocks.

Table 872: IH_INLN_DALI_TOKEN reference table
Library                                       Folder
CXA_S20_DALI                                  TYPE

Table 873: IH_INLN_ DALI_TOKEN structure

                                                   Max.           Default
Name        Type     Description                       Min. value                              Application
                                                   value          value
Device error during communica‐
byRespErr BYTE                                   16#0000            16#0F          16#0000     Continuous
tion
byRes‐           Device response during commu‐
BYTE                                 16#0000            16#FF          16#0000     Continuous
pSucc            nication
Token used by other Dali func‐
tion blocks to communicate
byToken     BYTE                                 16#0000            16#FF          16#0000     Continuous
with the IH_DaliReadWrite func‐
tion block
Repetition of the Dali command
bRepeat     BOOL                                 FALSE              TRUE           FALSE       Continuous
(50 ms)
Variable to process commands
wData2      WORD                                 --------           -------        --------    Continuous
or data

### 32.24.2 IH_INLN_DALI_ADDRTYPE

    The enumeration of address types is described using the data type
    IH_INLN_DALI_ADDRTYPE.

Table 874: Library assignment of the IH_INLN_DALI_ADDRTYPE
Library                                       Folder
CXA_S20_DALI                                  TYPE

Table 875: IH_INLN_DALI_ADDRTYPE data type
ENUM                               Description
SHORTADDR                          "Address" is the address of a ballast
GROUPADDR                          "Address" is a group address
BROADCAST                          Broadcast command. Command is executed for all ballasts

### 32.24.3 IH_INLN_DALI_DIMMODE

    The data type IH_INLN_DALI_DIMMODE describes the changes in light level.

Table 876: Library assignment of the IH_INLN_DALI_DIMMODE
Library                                       Folder
CXA_S20_DALI                                  TYPE

1026 /    ctrlX PLC Engineering
1344      Data types

Table 877: IH_INLN_DALI_DIMMODE data type
ENUM                              Description
                                  The lamp becomes brighter during a period of 200 ms. The dim‐
UP                                ming rate during these 200 ms is specified via the variable FADE
                                  RATE
STEPUP                            The lamp wattage is incremented by one step
                                  If required, the lamp is switched on and the lamp wattage is
ON_AND_STEPUP
                                  incremented by one step
                                  The lamp becomes darker during 200 ms. The dimming rate
DOWN
                                  during these 200 ms is specified via the variable FADE RATE
STEPDOWN                          The lamp wattage is decremented by one step
                                  The lamp wattage is decremented by one step. If the actual per‐
STEPDOWN_AND_OFF
                                  formance is on minimum (Min Level), the lamp is switched off

### 32.24.4 IH_INLN_DALI_LIGHTLEVEL

The data type IH_INLN_DALI_LIGHTLEVEL describes the levels of light level.

Table 878: Library assignment of the IH_INLN_DALI_LIGHTLEVEL
Library                                       Folder
CXA_S20_DALI                                  TYPE

Table 879: IH_INLN_DALI_LIGHTLEVEL data type
ENUM                              Description
MIN_LEVEL                         The light is on lowest level
MID_LEVEL                         The light level is on 50 percent
MAX_LEVEL                         The brightness is on highest level

### 32.24.5 IH_INLN_DALI_OPMODE

The data type IH_INLN_DALI_OPMODE shows the current operating mode of
the system.

Table 880: Library assignment of the IH_INLN_DALI_OPMODE
Library                                       Folder
CXA_S20_DALI                                  TYPE

                                                         Data types        1344

Table 881: ENUM IH_INLN_DALI_OPMODE enumeration
Name                 Value         Comment
VALUE_1_TO_DTR       0             Applies the value 1 to DTR
VALUE255_TO_DTR      1             Command: To apply values to the Data Transfer Register
MASKING_ALL_ADDRESS 2              Masks the addresses of all ballasts (deletes the addresses)
COMMAND_INITIALIZE   3             Command: Initialization
COMMAND_RANDOMISE 4                Command: Determine random number
SET_SEARCHADDRESS    5             Specify search address with IH_DaliSearchAddress
COMMAND_COMPARE      6             Command: Comparison
DECREMENTING_SEARCH‐ 7             Decrements the search address if Compare = TRUE
ADDR

INCREMENTING_SEARCH‐ 8             Increments the search address if Compare = FALSE
ADDR
ENABLE_PHYS‐         9             Command: Enabling physical selection
ICAL_SELECTION
FINDING_             10            Searches the next available addresses with IH_DaliQueryS‐
AVAILABLE_ADDRESS                  tatus
QUERY_SHORT_ADDR_IN_ 11            Command: Search of the short address during the physical
PHYSICAL                           selection
PROGRAM_SHORT_ADDR 12              Command: Short address of the program
VERIFY_SHORT_ADDR    13            Command: Check of the short address
VERIFY_LAMP_ON       14            Use IH_DaliQueryStatus to check in the selected ballast
              whether the lamp was switched on
RECALL_MINLEVEL              15    Command: Call MinLevel in ballast with address
RECALL_MAXLEVEL              16    Command: Call MaxLevel in ballast with address
WITHDRAWAL                   17    Command: Remove
TERMINATE                    18    Command: Terminate
COMMAND_INITIALIZE1          19    Command: Initial initialization
WITHDRAWAL1                  20    Withdrawal for first time
TERMINATE1                   21    Command: Terminate for first time
SEARCH_ADDR_TO_ZERO          22    Command: Set search address to zero
RESET_ALL_BALLASTS           23

### 32.24.6 IH_INLN_DALI_PARAMETER

Enumeration for parameter selection

Table 882: Library assignment of the IH_INLN_DALI_PARAMETER
Library                                     Folder
CXA_S20_DALI                                TYPE

1028 /    ctrlX PLC Engineering
1344      Troubleshooting

Table 883: IH_INLN_DALI_PARAMETER enumeration
Name                        Value   Comment
FADE_RATE                   0       FADE RATE specifies the velocity (in steps per second) of
                                    changes made in the lamp wattage calculated using the for‐
                                    mula
                                    Valid limit values (1-15)
FADE_TIME                   1       The FADE TIME specifies the time allowed for the current
                                    lamp wattage to be changed to the requested value calculated
                                    using the formula
                                    If the lamp is switched off, the preheating time and the igni‐
                                    tion time are not considered in FADE TIME
                                    Valid limit values (0-15)
MAX_LEVEL                   2       The ballast uses the variable MAX LEVEL to restrict the max‐
                                    imum wattage output to the lamp
                                    Valid limit values (Min Level - 254)
MIN_LEVEL                   3       The ballast uses the variable MIN LEVEL to specify the min‐
                                    imum wattage output to the lamp
                                    Valid limit values (Physical Min Level - Max Level)
POWER_ON_LEVEL              4       When current is supplied to the ballast, the lamp increases its
                                    performance up to the value specified in the variable POWER
                                    ON LEVEL
                                    Valid limit values (1-254)
SYSTEM_FAILURE_LEVEL        5       If there is malfunction in the DALI bus (the reactive voltage
                                    remains below the specified level for more than 500 ms), the
                                    lamp is increased to the performance specified by in the vari‐
                                    able SYSTEM FAILURE LEVEL
                                    Valid limit values (0-255)
FADE_RATE_AND_FADE_TI       6       Query command for FADE RATE and FADE TIME
ME                                  The response is XXXX YYYY. XXXX matches FADE RATE and
                                    YYYY matches FADE TIME
PHYSICAL_MIN_LEVEL          7

## 32.25 Troubleshooting

Troubleshooting
The function blocks of the library use the following error codes
ADD1: 16#0A0F.0113
ADD2: to be found in:
● CXA_S20_DALI CXA_S20_DALI_ErrorAdd
● CXA_EthercatMaster ErrorCodes
The S20 DALI error codes are available in the Global Variable List
CXA_S20_DALI_ErrorAdd in the library CXA_S20_DALI.
For the CXA_EthercatMaster error codes, refer to the Global Variable List
ErrorCodes in the library CXA_EthercatMaster.

It following error messages can be created in Additional2:

                                            Introduction and overview       1344

Table 884: CXA_S20_DALI error codes
ErrorID                      Additonal2 Description
INVALID_RANGE                16#0001    No free address
INPUT_INVALID_ERROR          16#0065    The input in "OldAddress" or "NewAddress" is invalid (<0
                                        or >63)
INPUT_INVALID_ERROR          16#0066    "GroupAddress“ is invalid (0< GroupAddress >15)
INPUT_INVALID_ERROR          16#0067    The input in "ShortAddress" is invalid (0< ShortAddress
                                        >63)
INPUT_INVALID_ERROR          16#0068    The     input    in   "LightLevel"   is   invalid   (0    or
                                        IH_INLN_DALI_LIGHTLEVEL.MIN_LEVEL < LightLevel >254
                                        or IH_INLN_DALI_LIGHTLEVEL.MAX_LEVEL)

INPUT_INVALID_ERROR          16#0069    The input "Address" is invalid
                   For group (0< Address >15)
                   For ballast (0< Address >63)
                   For query (0 < Address >63 and <> 255
INPUT_INVALID_ERROR          16#006A    The input "DimMode" is invalid
INPUT_INVALID_ERROR          16#006B    The input "AddressType" is invalid
INPUT_INVALID_ERROR          16#006C    The input in "Scene" is invalid
INPUT_INVALID_ERROR          16#006D    SizeOfActualLevel is invalid (1< SizeOfActualLevel > 64)
INPUT_INVALID_ERROR          16#006E    SizeOfStatus is invalid (1<SizeOfStatus> 64)
INPUT_INVALID_ERROR          16#006F    The input "Parameter" is invalid
INPUT_INVALID_ERROR          16#0070    The input "ParameterValue" is invalid
INPUT_INVALID_ERROR          16#0071    The input "SizeOfParameterValue" is invalid
INPUT_INVALID_ERROR          16#0072    The input "SizeOfGroup" is invalid
INPUT_INVALID_ERROR          16#0073    The input "NoOfBallasts" is invalid
DEVICE_ERROR                 16#00C9    Time error. The device does not respond.
DEVICE_ERROR                 16#00CA    The ballast received an invalid response (Dali bus error)
DEVICE_ERROR                 16#00CB    Unsupported command (no action on the Dali bus)
DEVICE_ERROR                 16#00CC I/O error (DALI failure)
DEVICE_ERROR                 16#00CD Undefined error
RESOURCE_ERROR               16#012D    Null pointer, variable not assigned
OTHER_ERROR                  16#0191    Invalid token or token between IH_DaliReadWrite and other
                   Dali function blocks not available
