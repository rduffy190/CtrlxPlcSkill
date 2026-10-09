# 7.7 General commands

### 7.7.1 SetErrorLevel - Setting the error state

Basics
This function sets an error in a Motion object.

Functional description
An error class has to be specified for each reported error. Depending on the

error class, there are different error reactions.
Supported error classes:
Error class                             Error reaction
LIGHT                                   Axes and kinematics decelerate with
                                        the last commanded dynamic limit
                                        values up to a full stop. Kinematics
                                        decelerates on the path
SEVERE                                  Axes decelerate with the configured
                                        dynamic limit values. All kinematic
                                        axes are removed from the kinematics
                                        and decelerate with the configured
                                        dynamic limit values. The kinematics
                                        leaves the programmed path
CRITICAL                                Like SEVERE error class
To set the error and the error class, generate a command. This command is
executed immediately. When querying the command status with the returned
command ID, DONE is always returned.
To set the error class to NONE again, generate a reset command.

PLC:

ML_SetErrorLevel
Name         Data type       Inherited       Address     Initial value   Comment
                             from
  Data      ML_SetError‐                                                 InOut: Command parame‐
            LevelData                                                    ters
  ML_SetEr‐ BOOL                                                         Returns whether the com‐
rorLevel                                                                 mand could be added.
                                                                         ● TRUE: The command
                                                                           could be added success‐
                                                                           fully
                                                                         ● FALSE: An error
                                                                           occurred. Details in
                                                                           ML_oCmdResult

STRUCT ML_SetErrorLevelData
Name       Data type     Inherited           Address       Initial value   Comment
                         from
  In       ML_iSetEr‐                                                      Input parameters
           rorLevel
  Out      ML_oCmdRe‐                                                      Output data of the query
           sult
STRUCT ML_iSetErrorLevel EXTENDS ML_iCmdBase
Name        Data type     Inherited  Address               Initial value   Comment
                          from
  ObjName STRING(63) ML_iCmd‐                                              Motion object name to exe‐
                          Base                                             cute the command
  Source    STRING(50) ML_iCmd‐                                            Specifies the command
                          Base                                             source, e.g.: PlcApplica‐
                                                                           tion1 is shown in the diag‐
                                                                           nostic messages
   SourceLine ULINT              ML_iCmd‐                                  Returns the source code
                                 Base                                      line of the command, is
                                                                           displayed in diagnostic
                                                                           messages
   Level           STRING(15)                                              Error class to be set (see
                                                                           ML_SetErrorLevel)
STRUCT ML_oCmdResult
Name       Data type             Inherited   Address       Initial value   Comment
                                 from
   CmdID           ULINT                                                   Command ID (set to
                                                                           18446744073709551615 in
                                                                           case of error)
   Error           BOOL                                                    Error ID, TRUE indicates
                                                                           that an error occurred
   ErrorID         UDINT                                                   Specifies the type of the
                                                                           occurred error (above 4
                                                                           bytes: main diagnostics,
                                                                           below 4 bytes: detailed
                                                                           diagnostics); 0 means “no
                                                                           error”

Data Layer:
Method: POST
URL:                https://<ip-addr>/automation/api/v2/nodes/motion/axs/
<axs_name>/cmd/err-level
Method: POST
URL:                 https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/err-level
Payload:

{"type": "string","value":"LIGHT"}

Python:
<cmdID> = motion.set_err_level( <objName>, <errLvl> )

Sets an error in the Motion object (object does not have to be attached).

This command is executed immediately. When querying the command status
with the returned command ID (getCmdState()), DONE is always returned.
To set the error class to NONE again, generate a reset command.
● <objName> - string, Motion object name
● <errLvl> - string, error class to be set ('LIGHT', 'SEVERE', 'CRITICAL')

BundleIF:
//! Set the error level of a motion object
//! @param[in]   handle      Handle of the interface
//! @param[in]   sourceInfo Command source information
//! @param[in]   objName     Name of the motion object
//! @param[in]   level       Error level to be set

//! @param[out] cmdID        The ID of the added command
//! @return                  Return value indicating success
(>=0) or error (<0) anzeigt
extern "C" MotionResult MOTION_CORE_SetErrorLevel(void
*handle, const dia::CmdSourceInfo& sourceInfo, const char *
objName, ::motion::core::ErrLevel level, uint64_t &cmdID);

### 7.7.2 GetOverride - Reading out the override

Basics
The override reduces the commanded velocity of a motion.

Functional description
The override value is in the range of 0 ... 1. A value of 0 means "zero override",
it causes the Motion object to stop. A value of 1 means "100% override", the
Motion object moves at the specified velocity.
The current override can be read out via a Motion command. When querying
the command status with the returned command ID (getCmdState()), DONE is
always returned.
The current effective override value can be read out in the Data Layer via the
effective-override node. This value is influenced by the user override, by
the "force100% override" function and by internal stop conditions (e.g. as part
of the error reaction).

Related topics
● ⮫ Chapter 7.7.3 SetOverride - Override on page 739
● ⮫ Chapter 7.7.4 ForceOverride100 - Overriding the override on page 742
● ⮫ Chapter 7.7.5 SetAccOverride, GetAccOverride - Acceleration override
  on page 744
● ⮫ Chapter 7.7.6 ForceAccOverride100 - Overriding acceleration override
  on page 748

PLC:

ML_GetOverride
Name        Data type          Inherited    Address      Initial value   Comment
                               from
   Data    ML_GetOver‐                                                   InOut: Command parame‐
           rideData                                                      ters
  ML_GetO‐ BOOL                                                          Returns whether the com‐
verride                                                                  mand could be added.
                                                                         ● TRUE: The ML_GetO‐
                                                                           verride command could
                                                                           be added successfully
                                                                         ● FALSE: An error
                                                                           occurred. Details in
                                                                           ML_oCmdResult
STRUCT ML_GetOverrideData
Name       Data type    Inherited           Address      Initial value   Comment
                        from
  In       ML_iGetO‐                                                     Input parameters
           verride
  Out      ML_oGetO‐                                                     Output data of the query
           verride
STRUCT ML_iGetOverride EXTENDS ML_iCmdBase
Name        Data type    Inherited  Address              Initial value   Comment
                         from
  ObjName STRING(15) ML_iCmd‐                                            Object name (axis or kin‐
                         Base                                            ematics) whose override
                                                                         value is queried
STRUCT ML_oGetOverride EXTENDS ML_oStateBase
Name       Data type    Inherited  Address               Initial value   Comment
                        from
  Error    BOOL         ML_oState‐                                       Error ID, TRUE indicates
                        Base                                             that an error occurred (e.g.
                                                                         typo in the object name)
   ErrorID         UDINT       ML_oState‐                                Specifies the type of error
                               Base                                      that has occurred (cur‐
                                                                         rently not in use, is always
                                                                         set to 1)
   Value           LREAL                                                 Requested override value

Data Layer:
Method: GET
URL:      https://<ip-addr>/automation/api/v2/nodes/motion/axs/<axs_name>/
state/values/override
Method: GET
URL:       https://<ip-addr>/automation/api/v2/nodes/motion/kin/<kin_name>/
values/override
Method: GET
URL:      https://<ip-addr>/automation/api/v2/nodes/motion/axs/<axs_name>/
state/values/effective-override
Method: GET
URL:       https://<ip-addr>/automation/api/v2/nodes/motion/kin/<kin_name>/
values/effective-override

Payload: (blank)

{"type": "double","value": 1}

Python:
<Value> = motion.get_override( obj=<objName> )

Provides the current override value of the Motion object
● <objName> - string, Motion object name
● <Value> - the current override value of the Motion object

BundleIF:

//! Get the override value of a motion object [0..1]
//!
//! @param[in]   handle    Handle of the interface
//! @param[in]   objName   Name of the motion object
//! @param[out] ovrValue Value of the override of this
motion object
//! @return                Was everything okay?
extern "C" MotionResult MOTION_CORE_GetOverride( void *handle,
const char *objName, double &ovrValue );

### 7.7.3 SetOverride - Override

Basics
The override reduces the commanded velocity of a motion.

Functional description
The override value is in the range of 0 ... 1. A value of 0 means "zero override",
it causes the Motion object to stop. A value of 1 means "100% override", the
Motion object moves at the specified velocity.
The override is set via a Motion command. The command is executed imme‐
diately. When querying the command status with the returned command ID
(getCmdState()), DONE is always returned.
The currently active override value can be read out in the Data Layer. This
value is influenced by the user override, by the "force100% override" function
and by internal stop conditions (e.g. as part of the error reaction).

Related topics
● ⮫ Chapter 7.7.2 GetOverride - Reading out the override on page 737
● ⮫ Chapter 7.7.4 ForceOverride100 - Overriding the override on page 742
● ⮫ Chapter 7.7.5 SetAccOverride, GetAccOverride - Acceleration override
  on page 744
● ⮫ Chapter 7.7.6 ForceAccOverride100 - Overriding acceleration override
  on page 748

PLC:

ML_SetOverride
Name         Data type           Inherited   Address   Initial value   Comment
                                 from
   Data            ML_SetOver‐                                         InOut: Command parame‐
                   rideData                                            ters
  ML_SetO‐         BOOL                                                Returns whether the com‐
verride                                                                mand could be added.
                                                                       ● TRUE: The command
                                                                         could be added success‐
                                                                         fully
                                                                       ● FALSE: An error
                                                                         occurred. Details in
                                                                         ML_oCmdResult
STRUCT ML_SetOverrideData
Name       Data type    Inherited            Address   Initial value   Comment
                        from
  In       ML_iSetO‐                                                   Input parameters
           verride
  Out      ML_oCmdRe‐                                                  Output data of the query
           sult
STRUCT ML_iSetOverride EXTENDS ML_iCmdBase
Name        Data type    Inherited  Address            Initial value   Comment
                         from
  ObjName STRING(15) ML_iCmd‐                                          Motion object name to exe‐
                         Base                                          cute the command
  Source    STRING(50) ML_iCmd‐                                        Specifies the command
                         Base                                          source, e.g.: PlcApplica‐
                                                                       tion1 is shown in the diag‐
                                                                       nostic messages
   SourceLine ULINT              ML_iCmd‐                              Returns the source code
                                 Base                                  line of the command, is
                                                                       displayed in diagnostic
                                                                       messages
   Value           LREAL                                               New override value (per‐
                                                                       missible range [0..1], se
                                                                       ML_SetOverride for more
                                                                       details)
STRUCT ML_oCmdResult
Name       Data type             Inherited   Address   Initial value   Comment
                                 from
   CmdID           ULINT                                               Command ID (set to
                                                                       18446744073709551615 in
                                                                       case of error)
   Error           BOOL                                                Error ID, TRUE indicates
                                                                       that an error occurred
   ErrorID         UDINT                                               Specifies the type of the
                                                                       occurred error (above 4
                                                                       bytes: main diagnostics,
                                                                       below 4 bytes: detailed
                                                                       diagnostics); 0 means “no
                                                                       error”

Data Layer:
Method: GET
URL:      https://<ip-addr>/automation/api/v2/nodes/motion/axs/<axs_name>/
state/values/override
Data type: double
Value range: 0.0 .. 1.0
Method: POST
URL:                    https://<ip-addr>/automation/api/v2/nodes/motion/axs/
<axs_name>/cmd/override
Data type: double
Value range: 0.0 .. 1.0

Method: GET
URL:      https://<ip-addr>/automation/api/v2/nodes/motion/axs/<axs_name>/
state/values/effective-override
Data type: double
Value range: 0.0 .. 1.0
Method: GET
URL:       https://<ip-addr>/automation/api/v2/nodes/motion/kin/<kin_name>/
state/values/override
Data type: double
Value range: 0.0 .. 1.0
Method: POST
URL:                    https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/override
Data type: double
Value range: 0.0 .. 1.0
Method: GET
URL:       https://<ip-addr>/automation/api/v2/nodes/motion/kin/<kin_name>/
state/values/effective-override
Data type: double
Value range: 0.0 .. 1.0
Payload:

{"type": "double","value": 1}

Python
<cmdID> = motion.set_override( obj=<objName>, val=<Value> )

Provides the current override value of the Motion object
● <objName> - string, Motion object name
● <Value> - the current override value of the Motion object

BundleIF:
//! @brief Set the override value of a motion object [0..1]
//! @param[in]   handle      Handle of the interface
//! @param[in]   sourceInfo Command source information
//! @param[in]   objName     Name of the motion object
//! @param[in]   ovrValue    New value of the override of this
motion object
//! @param[out] cmdID        The ID of the added command

//! @return                  Was everything okay?
extern "C" MotionResult MOTION_CORE_SetOverride(void *handle,
const dia::CmdSourceInfo&sourceInfo, const char *objName,
double ovrValue, uint64_t &cmdID);

### 7.7.4 ForceOverride100 - Overriding the override

Basics
The override reduces the commanded velocity of a motion.

Functional description
The "ForceOverride100" command can be used to override a set user override
and thus achieve full speed again.
If the function is disabled again (with the same command but a different
parameter), the originally commanded user override is active again. The func‐
tion can be used if the commanded velocity is always to apply for a certain
section of the application (or due to the process) without the end user being
able to reduce it using the override.
The function can be used if the commanded velocity is always to apply for a
certain section of the application (or due to the process) without the end user
being able to reduce it using the override.

Related topics
● ⮫ Chapter 7.7.3 SetOverride - Override on page 739
● ⮫ Chapter 7.7.2 GetOverride - Reading out the override on page 737
● ⮫ Chapter 7.7.5 SetAccOverride, GetAccOverride - Acceleration override
  on page 744
● ⮫ Chapter 7.7.6 ForceAccOverride100 - Overriding acceleration override
  on page 748

PLC:

ML_ForceOverride100
Name        Data type           Inherited       Address    Initial value   Comment
                                from
   Data     ML_ForceO‐                                                     InOut: Command parame‐
            verride100Da                                                   ters
            ta
  ML_Force‐ BOOL                                                           Returns whether the com‐
Override100                                                                mand could be added.
                                                                           ● TRUE: The command
                                                                             could be added success‐
                                                                             fully
                                                                           ● FALSE: An error
                                                                             occurred. Details in
                                                                             ML_oCmdResult

STRUCT ML_ForceOverride100Data
Name       Data type    Inherited        Address     Initial value   Comment
                        from
  In       ML_iForceO‐                                               Input parameters
           verride100
  Out      ML_oCmdRe‐                                                Output data of the query
           sult
STRUCT ML_iForceOverride100 EXTENDS ML_iCmdBase
Name        Data type    Inherited  Address     Initial value        Comment
                         from
  ObjName STRING(15) ML_iCmd‐                                        Motion object name to exe‐

     Base                                        cute the command
  Source    STRING(50) ML_iCmd‐                                      Specifies the command
     Base                                        source, e.g.: PlcApplica‐
                                                 tion1 is shown in the diag‐
                                                 nostic messages
  SourceLine ULINT           ML_iCmd‐                                Returns the source code
         Base                                    line of the command, is
                                                 displayed in diagnostic
                                                 messages
  Force100   BOOL                                                    TRUE: It should be driven
                                                 at full speed
                                                 FALSE: The velocity limita‐
                                                 tion set with setOverride is
                                                 to be active
STRUCT ML_oCmdResult
Name       Data type         Inherited   Address     Initial value   Comment
                             from
  CmdID      ULINT                                                   Command ID (set to
                                                                     18446744073709551615 in
                                                                     case of error)
  Error      BOOL                                                    Error ID, TRUE indicates
                                                                     that an error occurred
  ErrorID    UDINT                                                   Specifies the type of the
                                                                     occurred error (above 4
                                                                     bytes: main diagnostics,
                                                                     below 4 bytes: detailed
                                                                     diagnostics); 0 means “no
                                                                     error”

Data Layer:
Method: POST
URL:               https://<ip-addr>/automation/api/v2/nodes/motion/axs/
<axs_name>/cmd/force-override-to-100-percent
Method: POST
URL:                https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/force-override-to-100-percent

Python
<cmdID> = motion.force_override_100(obj=<objName>,
force100=<force100>)

Overrides the user override and acts as a 100 % override for the axis or
kinematics.
The command becomes active immediately, getCmdState() with the returned
command ID always returns the state DONE.
● <objName> - string, axis/kinematic name
● <force100> - bool, should the function be switched on or off?

BundleIF:
//! @brief Force the override value of a motion object to 100
percent (ignoring the commanded override value)
//! @param[in]   handle      Handle of the interface
//! @param[in]   sourceInfo Command source information
//! @param[in]   objName     Name of the motion object
//! @param[in]   force100    Force to 100 percent or remove
the force
//! @param[out] cmdID        The ID of the added command
//! @return                  Was everything okay?
extern "C" MotionResult
MOTION_CORE_ForceOverrideTo100Percent(void *handle, const
dia::CmdSourceInfo&sourceInfo, const char *objName, bool
force100, uint64_t &cmdID);

### 7.7.5 SetAccOverride, GetAccOverride - Acceleration override

Basics
This command sets the current acceleration override for an axis or a kine‐
matics.

Functional description
By using the acceleration override, the currently commanded acceleration can
be further reduced. The command is active immediately and acts asynchro‐
nously to the regular command processing. The command does not depend on
commands already contained in the command buffer.
The value of the override has to be in the interval [0.01; 1]. A value of 0.01
indicates that an acceleration of 1 % of the commanded acceleration must not
be exceeded. A value of 1 indicates 100% override so that the commanded
acceleration can be used.
This command is executed immediately. If the command state with the
returned ID is queried, "DONE" is always returned.

Related topics
● ⮫ Chapter 7.7.6 ForceAccOverride100 - Overriding acceleration override
  on page 748
● ⮫ Chapter 7.7.2 GetOverride - Reading out the override on page 737
● ⮫ Chapter 7.7.4 ForceOverride100 - Overriding the override on page 742

PLC:

ML_SetAccOverride
Name        Data type       Inherited   Address   Initial value   Comment
                            from
  Data      ML_SetAccO‐                                           InOut: Command parame‐
            verride                                               ters
  ML_SetAc‐ BOOL                                                  Returns, whether it was
cOverride                                                         possible to add the com‐
                                                                  mand to the kinematic
                                                                  object.
                                                                  ● TRUE: The ML_SetAccO‐
                                                                    verride command could
                                                                    be added successfully

● FALSE: An error
  occurred. Details in
  ML_oCmdResult
STRUCT ML_SetAccOverrideData
Name       Data type    Inherited       Address   Initial value   Comment
                        from
  In       ML_iSetAc‐                                             Input parameters
           cOverride
  Out      ML_oCmdRe‐                                             Output data of the query
           sult
STRUCT ML_iSetAccOverride EXTENDS ML_iCmdBase
Name        Data type    Inherited  Address       Initial value   Comment
                         from
  ObjName STRING(15) ML_iCmd‐                                     Motion object name to exe‐
                         Base                                     cute the command
  Source    STRING(50) ML_iCmd‐                                   Specifies the command
                         Base                                     source, e.g.: PlcApplica‐
                                                                  tion1 is shown in the diag‐
                                                                  nostic messages
  SourceLine ULINT          ML_iCmd‐                              Returns the source code
                            Base                                  line of the command, is
                                                                  displayed in diagnostic
                                                                  messages
  Value      LREAL                                                New override value (per‐
                                                                  missible range [0..1], se
                                                                  ML_SetOverride for more
                                                                  details)
STRUCT ML_oCmdResult
Name       Data type        Inherited   Address   Initial value   Comment
                            from
  CmdID      ULINT                                                Command ID (set to
                                                                  18446744073709551615 in
                                                                  case of error)
  Error      BOOL                                                 Error ID, TRUE indicates
                                                                  that an error occurred

STRUCT ML_oCmdResult
  ErrorID  ULINT                                                          Specifies the type of the
                                                   occurred error (above 4
                                                   bytes: main diagnostics,
                                                   below 4 bytes: detailed
                                                   diagnostics); 0 means “no
                                                   error”

Data Layer:
Method: POST
URL:                https://<ip-addr>/automation/api/v2/nodes/motion/axs/
<axs_name>/cmd/acc-override
Method: POST
URL:                https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/acc-override
Payload:

{"type": "double","value": 0.5}

Python:
<cmdID> = motion.set_acc_override( obj=<objName>, val=<Value> )

Sets the acceleration override for the specified axis/kinematics. The axis/kine‐
matics has to be assigned to the script instance (object has to be "attached"),
see documentation Python Runtime App ⮫ Python functions
The command is active immediately, getCmdState( ) with the received com‐
mand ID always returns a DONE.
The value of the override should be in the interval [0.01; 1]. A value of 0.01
indicates that an acceleration of 1 % of the commanded acceleration must not
be exceeded. A value of 1 indicates 100% override so that the commanded
acceleration can be used.
● <objName> - string, axis/kinematic name
● <Value> - number, new value for the acceleration override

BundleIF:
//! @brief Set the acceleration override value of a motion
object [0.01..1]
//! @param[in]   handle      Handle of the interface
//! @param[in]   sourceInfo Command source information
//! @param[in]   objName     Name of the motion object
//! @param[in]   ovrValue    New value of the override of this
motion object
//! @param[out] cmdID        The ID of the added command
//! @return                  Was everything okay?
extern "C" MotionResult MOTION_CORE_setAccOverride(void
*handle, const dia::CmdSourceInfo&sourceInfo, const char
*objName, double ovrValue, uint64_t &cmdID);

PLC:

ML_GetAccOverride
Name       Data type        Inherited   Address   Initial value   Comment
                            from
  Data      ML_GetAccO‐                                           InOut: Command parame‐
            verride                                               ters

  ML_GetAc‐ BOOL                                                  Returns, whether it was
cOverride                                                         possible to add the com‐
                                              mand to the kinematic
                                              object.
                                              ● TRUE: The ML_GetAccO‐
                                                verride command could
                                                be added successfully
                                              ● FALSE: An error
                                                occurred. Details in
                                                ML_oCmdResult
STRUCT ML_GetAccOverrideData
Name       Data type    Inherited       Address   Initial value   Comment
                        from
  In       ML_iObjSta‐                                            Input parameters
           teBase
  Out      ML_oGetAc‐                                             Output data of the query
           cOverride
STRUCT ML_iObjStateBase
Name        Data type   Inherited       Address   Initial value   Comment
                        from
  ObjName STRING(15)                                              Motion object name (axes
                                                                  or kinematics) you want to
                                                                  request data from
STRUCT ML_oGetAccOverride EXTENDS ML_oStateBase
Name       Data type    Inherited  Address      Initial value     Comment
                        from
  Error    BOOL         ML_oState‐                                Error ID, TRUE indicates
                        Base                                      that an error occurred
  ErrorID  ULINT        ML_oState‐                                Specifies the type of the
                        Base                                      occurred error (above 4
                                                                  bytes: main diagnostics,
                                                                  below 4 bytes: detailed
                                                                  diagnostics); 0 means “no
                                                                  error”
  Value      LREAL                                                Requested override value

Data Layer:
Method: GET

URL:      https://<ip-addr>/automation/api/v2/nodes/motion/axs/<axs_name>/
state/values/acc-override
Method: GET
URL:       https://<ip-addr>/automation/api/v2/nodes/motion/kin/<kin_name>/
state/values/acc-override
Payload: (blank)

Python:
<Value> = motion.get_acc_override( obj=<objName> )

Returns the current acceleration override of the axis or the kinematics.
● <objName> - string, axis/kinematic name
● <Value> - the current acceleration override value of the axis or the kine‐
  matics

BundleIF:
//! @brief Get the acceleration override value of a motion
object [0.01..1]
//! @param[in]   handle      Handle of the interface
//! @param[in]   objName     Name of the motion object
//! @param[in]   ovrValue    Value of the acceleration
override of this motion object
//! @return                  Was everything okay?
extern "C" MotionResult MOTION_CORE_getAccOverride(void
*handle, const char *objName, double &ovrValue );

### 7.7.6 ForceAccOverride100 - Overriding acceleration override

Basics
This command sets the current acceleration override for an axis or a kine‐
matics.

Functional description
The "force-acc-override-to-100-percent" command can be used to override the
user override for acceleration so that 100% is always applied. The actual
numerical value of the user override is not changed and can still be read.
In the calculation of the target acceleration, however, 100% is active.
If the function is disabled again, the originally commanded user acceleration
override is active again. The function can be used if the commanded accelera‐
tion is always to apply for a certain section of the application (or due to the
process) without the end user being able to reduce it using the override.

Related topics
● ⮫ Chapter 7.7.5 SetAccOverride, GetAccOverride - Acceleration override
  on page 744
● ⮫ Chapter 7.7.2 GetOverride - Reading out the override on page 737
● ⮫ Chapter 7.7.4 ForceOverride100 - Overriding the override on page 742

PLC:

ML_ForceAccOverride100
Name        Data type       Inherited   Address        Initial value   Comment
                            from
  Data      ML_ForceAc‐                                                InOut: Command parame‐
            cOverride100                                               ters

  ML_Force‐ BOOL                                                       Returns, whether it was
AccO‐                                                                  possible to add the com‐
verride100                                                             mand to the kinematic
object.
● TRUE: The ML_SetAccO‐
  verride command could
  be added successfully
● FALSE: An error
  occurred. Details in
  ML_oCmdResult
STRUCT ML_ForceAccOverride100Data
Name       Data type    Inherited       Address        Initial value   Comment
                        from
  In       ML_iForceAc‐                                                Input parameters
           cOverride100
  Out      ML_oCmdRe‐                                                  Output data of the query
           sult
STRUCT ML_iForceAccOverride100 EXTENDS ML_iCmdBase
Name        Data type    Inherited  Address    Initial value           Comment
                         from
  ObjName STRING(15) ML_iCmd‐                                          Motion object name to exe‐
                         Base                                          cute the command
  Source    STRING(50) ML_iCmd‐                                        Specifies the command
                         Base                                          source, e.g.: PlcApplica‐
                                                                       tion1 is shown in the diag‐
                                                                       nostic messages
  SourceLine ULINT          ML_iCmd‐                                   Returns the source code
                            Base                                       line of the command, is
                                                                       displayed in diagnostic
                                                                       messages
  Force100   BOOL                                                      TRUE: Acceleration override
                                                                       should be 100%
                                                                       FALSE: The value set
                                                                       by ML_SetAccOverride
                                                                       becomes active.
STRUCT ML_oCmdResult
Name       Data type        Inherited   Address        Initial value   Comment
                            from

STRUCT ML_oCmdResult
  CmdID    ULINT                                                        Command ID (set to
                                                 18446744073709551615 in
                                                 case of error)
   Error           BOOL                                                 Error ID, TRUE indicates
                                                 that an error occurred
   ErrorID         ULINT                                                Specifies the type of the
                                                 occurred error (above 4
                                                 bytes: main diagnostics,
                                                 below 4 bytes: detailed
                                                 diagnostics); 0 means “no
                                                 error”

Data Layer:
Method: POST
URL:               https://<ip-addr>/automation/api/v2/nodes/motion/axs/
<axs_name>/cmd/force-acc-override-to-100-percent
Method: POST
URL:                https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/force-acc-override-to-100-percent

Python:
<cmdID> = motion.force_acc_override_100(obj=<objName>,
force100=<force100>)

Overrides the user acceleration override and acts as a 100% override for
the axis or kinematics. The axis/kinematics has to be assigned to the script
instance (object has to be "attached"), see documentation Python Runtime
App ⮫ Python functions
The command is active immediately, getCmdState( ) with the received com‐
mand ID always returns a DONE.
The value of the user acceleration override is not changed when the function
is enabled.
● <objName> - string, axis/kinematic name
● <force100> - bool, should the function be switched on or off?

BundleIF:
//! @brief Force the acceleration override value of a motion
object to 100 percent (ignoring the commanded override value)
//! @param[in]   handle      Handle of the interface
//! @param[in]   sourceInfo Command source information
//! @param[in]   objName     Name of the motion object
//! @param[in]   force100    Force to 100 percent or remove
                             the force
//! @param[out] cmdID        The ID of the added command
//! @return                  Was everything okay?
extern "C" MotionResult
MOTION_CORE_forceAccOverrideTo100Percent(void *handle, const
dia::CmdSourceInfo&sourceInfo, const char *objName, bool
force100, uint64_t &cmdID);

### 7.7.7 WaitPrepare - Stopping the preparation

Basics
This command is used to synchronize two commands. It can block the prepa‐
ration of a newer command in the command buffer and block the look-ahead
of the older command that needs data from a command newer than WAIT.

PLC:

ML_WaitPrepare
Name        Data type        Inherited   Address     Initial value   Comment
                             from
  Data       ML_WaitPre‐                                             InOut: Command parame‐
             pare                                                    ters
  ML_Wait‐   BOOL                                                    Returns, whether it was
Prepare                                                              possible to add the com‐
                                                                     mand to the kinematic
                                                                     object.
                                                                     ● TRUE: The ML_WaitPre‐
                                                                       pare command could be
                                                                       added successfully
                                                                     ● FALSE: An error
                                                                       occurred. Details in
                                                                       ML_oCmdResult
STRUCT ML_WaitPrepareData
Name       Data type    Inherited        Address     Initial value   Comment
                        from

STRUCT ML_WaitPrepareData
  In       ML_iCmd‐                                                     Input parameters
Base
  Out      ML_oCmdRe‐                                                   Output data of the query
sult
STRUCT ML_iCmdBase
Name        Data type           Inherited   Address     Initial value   Comment
                                from
   ObjName         STRING(15)                                           Motion object name to exe‐
                                                                        cute the command
   Source          STRING(50)                                           Specifies the command
                                                                        source, e.g PlcApplication1
                                                                        is displayed in the diag‐
                                                                        nostic messages
   SourceLine ULINT                                                     Specifies the source line of
                                                                        the command; is displayed
                                                                        in the diagnostic messages
STRUCT ML_oCmdResult
Name       Data type            Inherited   Address     Initial value   Comment
                                from
   CmdID           ULINT                                                Command ID (is set to
                                                                        18446744073709551615 in
                                                                        the event of an error)
   Error           BOOL                                                 Error ID TRUE indicates
                                                                        that an error occurred
   ErrorID         ULINT                                                Specifies the type of
                                                                        occurred error: The upper
                                                                        4 bytes reflect the main
                                                                        diagnostics, the lower 4
                                                                        bytes reflect the detailed
                                                                        diagnostics, 0 means no
                                                                        error

Data Layer:
Method: POST
For axes:
URL:               https://<ip-addr>/automation/api/v2/nodes/motion/axs/
<axs_name>/cmd/axs-wait-prepare
Payload:

{
"type":"object","value":
{
"buffered":false
}
}

For kinematics:
URL:                https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/cmd/kin-wait-prepare
Payload:

{
"type":"object","value":
{
"buffered":false
}
}

Python:
<cmdID> = MotionLib.wait_prepare ( obj=<objName>,
buffered=True )

Creates a waitPrepare command for a Motion object (object has to be
"attached"), see Python Runtime App ⮫ Python functions documentation.

● <objName> - string, Motion object name

BundleIF:

//! Create a motion command for a single axis (axsWait)
//!
//! @param[in]   handle      Handle of the interface
//! @param[in]   sourceInfo Command source information
//! @param[in]   objName     Name of the motion object
//! @param[out] cmdID        The ID of the added command
//! @return                  Was everything okay?
motion::core::MotionResult(*waitPrepareCmd)(void* handle,
const ::motion::core::dia::CmdSourceInfo & sourceInfo, const
char* objName, uint64_t &cmdID);

### 7.7.8 WaitExec - Wait command

Basics
When commands are processed in a buffered manner, it is sometimes nec‐
essary to pause the commanded motion for a defined wait time. For this
purpose, ctrlX MOTION provides a (buffered) wait command.
This means that, during buffered execution, all commands issued before the
wait command are executed subsequently. As soon as the sequence reaches
the wait command, the motion stops at the end point specified by the pre‐
ceding command. The time specified in the wait command elapses. The wait
command ends as soon as the wait time has elapsed. If there is a subsequent
command in the buffer, that command is executed.
The wait command always waits for a multiple of the configured cycle time—
it always waits for whole cycles. In other words, if, for example, you have
configured a cycle time of 2 milliseconds and issue a command for a wait time
of 11 milliseconds, the actual wait time will be 12 milliseconds (or 6 cycles).
The "Wait" command can be used for both individual axes and kinematics. It is
available only in buffered command processing mode.
The wait command reports the status ACTIVE as long as the wait time elapses.
As soon as the wait period has elapsed, the command reports the state
DONE. The state of the command can be queried using the ⮫ GetCmdState
function.
While waiting, an axis reports the PLC open state STANDSTILL. A kinematic
unit reports the PLC open state STANDBY.
Example:

In this example, there should be a 1.2-second delay between two motion
commands.
MoveLin(…)
WaitExec(1.2)
MoveLin(…)

Functional description
The wait command can be used to wait for a specified amount of time when
commands are processed in a buffered manner. The wait command can be
used for both individual axes and kinematics. It is available only in buffered
command processing mode.
The wait time is specified in the configured unit of time (usually seconds).
The wait command always waits for a multiple of the configured cycle time—
it always waits for whole cycles. This means that if, for example, you have
configured a cycle time of 2 milliseconds and then issue a command to wait
11 milliseconds, the actual wait time is 12 milliseconds (or 6 cycles).

PLC:

STRUCT ML_WaitExecData
Name       Data type   Inherited                Address    Initial value   Comment
                       from
  In       ML_iWai‐                                                        Input parameters
           tExec
  Out      ML_oCmdRe‐                                                      Output data of the query
           sult
STRUCT ML_iWaitExec EXTENDS ML_iCmdBase
Name       Data type    Inherited  Address                 Initial value   Comment
                        from
  ObjName STRING(63) ML_iCmd‐                                              Motion object name to exe‐
                        Base                                               cute the command
  Source   STRING(50) ML_iCmd‐                                             Specifies the command
                        Base                                               source, e.g PlcApplication1
                                                                           is displayed in the diag‐
                                                                           nostic messages
   SourceLine ULINT            ML_iCmd‐                                    Specifies the source line of
                               Base                                        the command; is displayed
                                                                           in the diagnostic messages
 TimeTo‐           LREAL                                                   Execution wait time in con‐
Wait                                                                       figured user units (for more
                                                                           details, see ML_WaitExec)
STRUCT ML_oCmdResult
Name       Data type           Inherited        Address    Initial value   Comment
                               from

STRUCT ML_oCmdResult
  CmdID    ULINT                                               Command ID (is set to
                                           18446744073709551615 in
                                           the event of an error)
 Error       BOOL                                              Error ID TRUE indicates
                                           that an error occurred
 ErrorID     ULINT                                             Specifies the type of
                                           occurred error: The upper
                                           4 bytes reflect the main
                                           diagnostics, the lower 4
                                           bytes reflect the detailed
                                           diagnostics, 0 means no

                                           error

Data Layer:
 Data Layer path  Type          Description
 motion/axs/      FLOAT64       Waits for the specified time (in user
 [name]/cmd/wait-               units) during execution
 exec
 motion/axs/
 [name]/cmd/wait-
 exec motion/kin/
 [name]/cmd/wait-
 exec

Python:
def wait_exec(obj: str, time: float) -> int:
 """Let the exection wait for a given time. The
    really waited time is always a multiple of your
    cycle time and greater or equal to the given time.

 (object has to be attached, see motion.attach_obj())

 Args:
   obj: The name of the motion object (axis or kinematics).
   time: Time to wait in the configured user units.

 Returns:
     The command id.
 """

BundleIF:

/// @brief Create a motion command for a single axis or
kinematics to wait in the execution for the given time
///
/// Please note, that the command will always wait for full
cycles (e.g. your cycle time is configured to 2ms, then the
command will wait for multiples of 2ms).
///
/// @param[in]     handle       Handle of the interface
/// @param[in]     sourceInfo   Command source information
/// @param[in]     objName      Name of the motion object
/// @param[in]     duration     Duration to wait in the

configured time unit
/// @param[out]    cmdID        The ID of the added command
/// @return                     Status of the function call:
STS_OK or an error code on failure.
::motion::core::MotionResult(*waitExecCmd)(void* handle,
const ::motion::core::dia::CmdSourceInfo& sourceInfo, const
char* objName, double duration, uint64_t& cmdID);

### 7.7.9 GetCollisionGuardState, CollisionAvoidance - Collision detection

and collision avoidance
Introduction
The collision detection (1D) and collision avoidance (1D) functionality imple‐
ments the collision detection and avoidance of two axes moving in the same
direction (1D). The axes involved can be a single axis, part of a gantry link,
part of a kinematic system or any combination of these.
The axis motions have to use the same coordinate system.

Definition of terminology
This chapter describes the terminology used for collision detection and colli‐
sion avoidance.
● Collision detection
  Functionality for detecting a collision when a requested motion is executed
  or when a motion is in progress. The GetCollisionGuardState function
  implements this functionality. For a detailed description, see ⮫ GetColli‐
  sionGuardState on page 758.
● Collision avoidance
  Functionality to avoid an imminent collision or to minimize the effects of an
  imminent collision. The CollisionAvoidance function implements this func‐
  tionality. For a detailed description, see ⮫ CollisionAvoidance on page 759.
● Collision protection (1D)
  The collision protection monitors a potential collision in one direction. It
  analyzes the risk of a collision between two axes. Collision protection is
  based on data provided by the parameter position, the axis braking dis‐
  tances and the safety distances used (e.g. stop distance, emergency stop
  distance). Collision protection creates a state that reflects the situation.
● Braking distance
  The braking distance of an axis is the distance required to come to a con‐
  trolled stop from the current position. AxsInterrupt, KinInterrupt, AxsAbort
  or KinAbort are called by the active Motion profile and if the override is set
  to 0. See ⮫ GetBrakingDistance on page 758 for more information.
● Emergency distance
  The emergency distance is the minimum distance that has to be maintained
  between two axes after these axes have performed an emergency stop to
  avoid a collision. The emergency distance is a parameter defined in the
  application.
● Minimum distance
  The minimum distance is the distance between two axes after these axes
  have performed a regular stop to avoid a collision. The minimum distance
  is a parameter defined in the application.

  ● Deceleration distance
    The braking distance is the minimum distance that has to be maintained
    between two axes if the velocity has to be reduced or if a stop has to be
    executed to avoid a collision. Refer to ⮫ Chapter Risk of a head-to-head
    collision on page 759. The braking distance is necessary for axes that move
    towards each other. The deceleration distance is a parameter defined in the
    application.
  ● Synchronization distance
    The synchronization distance is the distance between two axes at which
    the velocity between the axes have to be synchronized to avoid collisions.
    Refer to ⮫ Chapter Risk of a head-to-tail collision on page 760. The synchro‐
    nization distance applies to axes that move in the same direction. The
    synchronization distance is a parameter defined in the application.

  ● Hysteresis
    The hysteresis is the tolerance available in the safety distance parameters.
    This prevents quick changes to collision protection (and the associated
    actions). The hysteresis is only used for collision protection transitions to
    a less critical state, see ⮫ GetCollisionGuardState on page 758. The hyste‐
    resis distance is a parameter defined in the application.

    Overview of the architecture
The functionality of collision detection and avoidance, as implemented in the
ctrlX platform, mainly concerns PLC applications. Based on the PLC function
blocks GetBrakingDist, CollisionAvoidance and CollisionGuardState, an appli‐
cation implements collision detection and avoidance. These function blocks
contain the general functionality. The necessary, application-specific actions
have to be provided and implemented by the user. For a general overview
of the entities for collision detection and collision avoidance, see ⮫ Chapter
Overview of the architecture on page 757. In addition to the PLC interface,
other interfaces are also provided, see ⮫ Chapter Definition of terminology
on page 756.

ROBOT

Customer environment (PLC)

                        Customer Application

       Is there risk of a Customer Specific
collision between axis A CollisionAvoidance FB Take action based on
                 and B?                      returned state

               Axis A        Axis B        Axes A+B (in); State (out)

PLC environment          getBrakingDist                CollisionAvoidance                   CollisionGuardState

C++ environment                                              CollisionAvoidance

Generic getBrakingDistance                                              CollisionGuardState

GetBrakingDistance
The GetBrakingDistance function block determines the braking distance
between the axis and the neighboring axes. GetBrakingDistance supports
single axes, the gantry link and Cartesian kinematic models with linear
motion. This means that the blending process is not supported, as the braking
distance cannot be determined precisely during blending. There are further
restrictions for blending: The dynamic limits of both axes have to be identical,
including the override.
The GetBrakingDistance function calculates the stop distance based on a
controlled stop ( 3rd order profile). The emergency stop uses the quick stop
defined in the system properties of the axis ( 2nd order profile). As a result,
the axis position after a motion due to an emergency stop is smaller than the
motion calculated by the GetBrakingDistance function.

GetCollisionGuardState
The CollisionGuardState function block estimates the collision risk and
returns the result to the CollisionAvoidance function block. The following
states are returned by the CollisionGuardState in decreasing severity.
● CG_EMERGENCY_STOP: If an emergency stop is carried out on both axes, a
  collision can be avoided.
● CG_STOP: If a regular stop is executed on both axes, the axes do not
  collide.
● CG_SLOWDOWN_ADVICE: A head-on collision can occur, slow down or
  stop.
● CG_SYNC_ADVICE: A rear-end collision is possible, the velocity has to be
  synchronized.

● CG_TARGETS_CROSSING: An axis may not reach its target end position as
  other axes are blocking the way.
● CG_MONITORING: The axis is either at a standstill or in motion, but cannot
  cause a collision.

CollisionAvoidance
Once the collision protection status has been analyzed, the corresponding col‐
lision avoidance actions are implemented by the CollisionAvoidance function
block. The following actions are implemented based on the collision protec‐
tion status:
● CG_EMERGENCY_STOP: An emergency stop is executed if the SetErrorLevel
   function sets the error level of the axis to SEVERE. This is the case as

   soon as the axis changes from a less critical state to this state. To continue
   processing, the application has to delete the error. If a new motion is
   started even though the emergency stop situation persists, the command is
   stopped/canceled again.
The calculations of the CG_EMERGENCY_STOP state are based on the braking
distance with a controlled stop profile. CollisionAvoidance uses a quick-stop
profile for each axis (activation at error level: SEVERE). This can cause the
axis to come to a standstill before emerDist. This can cause a CG_STOP state
after the CG_EMERGENCY_STOP state (the corresponding interrupt action is
not started). To avoid this situation, set the hysteresis to a sufficiently high
value.
● CG_STOP : Call AxsInterrupt or KinInterrupt to abort the command as soon
    as it changes from a less critical state to this state. The application (the
    PLC program) has to call AxsContinue or KinContinue to continue the
    command. axsAbortCmd or kinAbortCmd aborts the command. If a new
    motion is started even though the stop situation persists, the command is
    stopped/canceled again.
    Calculating the CollisionGuard for a stop or an emergency stop.
● CG_SLOWDOWN_ADVICE : No action
● CG_SYNC_ADVICE : No action
● CG_TARGETS_CROSSING : No action
● CG_MONITORING : No action
If an axis or kinematic system stops, but the stopping process has not yet
been fully completed due to collision avoidance actions, the collision protec‐
tion changes to a less critical state. Collision protection should be ignored if
the axis or kinematics stops but is not yet completely stopped.
The application can perform corresponding actions based on the Collision‐
GuardState.
If the "Enabled" input of the CollisionAvoidance function block is FALSE, the
function block recognizes the status change but does not execute any actions.

    Case studies

Risk of a head-to-head collision
Two axes move towards each other in a head-to-head collision situation. The
following distances are defined for a head-to-head collision, see ⮫ Chapter
Risk of a head-to-head collision on page 759.

● The emergency braking distance "emerDist" is the distance between two
  axes after an emergency stop has been performed to avoid a collision,
  as the axes are moving too close to each other. If an emergency stop is
  performed and the distance between the axes is less than "emerDist", a
  collision could occur
● The minimum distance "minDist" is the distance between two axes after a
  regular stop to avoid collisions. A regular stop can cause a collision if the
  distance between the axes is less than "minDist"
● The braking distance "SlowDownDist" is the distance up to the minimum
  distance at which a collision can be avoided by reducing the axis velocity.
  As the status is also returned to the application, it can also stop an axis
  before the defined "slowDownDist" is reached

                                      emerDist

                                      minDist

                                    slowDownDist
   Axs                                                                        Axs
    1                                                                          2

First, the distance between axis 1 and axis 2 is calculated in order to estimate
the risk of a head-to-head collision. Based on the calculated distance, the
following hazard assessments are possible:
● IF distance £ emerDist + |brakingDistAxs1| + |brakingDistAxs2|
  ® Emergency stop: setErrorLevel = SEVERE, CG_EMERGENCY_STOP (axis 1
  is already too close to axis 2)
● ELSEIF distance £ minDist + |brakingDistAxs1| + |brakingDistAxs2|
  ® Stop: AxsInterrupt/KinInterrupt, CG_STOP (axis 1 has to stop to avoid
  getting too close to axis 2)
● ELSEIF distance £ slowDownDist + |brakingDistAxs1| + |brakingDistAxs2|
  ® Signal for potential imminent collision, CG_SLOWDOWN_ADVICE
● ELSEIF targetPos1 and targetPos2 overlap
  ® (optional) CG_TARGETS_CROSSING
● ELSE - no problems
  ® Monitoring path, CG_MONITORING
The hysteresis is only used for state transitions to a less critical state. I.e., if a
CollisionGuardState has already been reached.

Risk of a head-to-tail collision
In a head-to-tail collision situation, two axes move in the same direction at
different velocities. The following distances are defined for a head-to-tail colli‐
sion, see ⮫ Chapter Risk of a head-to-tail collision on page 760.

● The emergency braking distance "emerDist" is the distance between two
  axes after an emergency stop has been performed to avoid a collision,
  as the axes are moving too close to each other. If an emergency stop is
  performed and the distance between the axes is less than "emerDist", a
  collision could occur.
● The minimum distance "minDist" is the distance between two axes after a
  regular stop to avoid collisions. A regular stop can cause a collision if the
  distance between the axes is less than "minDist”.
● The synchronization distance "syncDist" is the distance up to the minimum
  distance at which the reduction of the axis velocity (velocity synchroni‐
  zation with another axis) can prevent a collision. As the status is also
  returned to the application, the application can also stop an axis before
  the defined syncDist is reached.

                                                   emerDist

                                             minDist

                                       syncDist
   Axs                                                          Axs
    1                                                            2

First, the distance between axis 1 and axis 2 is calculated for a risk analysis of
a head-to-tail collision. Based on the calculated distance, the following hazard
assessments are possible:
● IF distance £ emerDist + |brakingDistAxs1|
  ® Emergency stop: setErrorLevel = SEVERE, CG_EMERGENCY_STOP (axis 1
  is already too close to axis 2)
● ELSEIF distance £ minDist + |brakingDistAxs1| - |brakingDistAxs2|
  ® Stop: AxsInterrupt/KinInterrupt, CG_STOP (axis 1 has to stop to avoid
  getting too close to axis 2)
● ELSEIF distance £ syncDist + |brakingDistAxs1| - |brakingDistAxs2|
  ® Signal for synchronization with axis 2, CG_SYNC_ADVICE
● ELSEIF targetPos1 and targetPos2 overlap
  ® (optional) CG_TARGETS_CROSSING
● ELSE - no problems
  ® Monitoring path, CG_MONITORING
The hysteresis is only used for state transitions to a less critical state. I.e., if a
CollisionGuardState has already been reached.

Axis at standstill or when moving away from another axis
No special calculations necessary. Continue monitoring, CollisionGuardState
is CG_MONITORING.

Implementation
PLC function block GetCollisionGuardState:

Table 86: ML_GetCollisionGuardState
STRUCT ML_GetCollisionGuardStateData
Name       Data type     Inherited   Address             Initial value   Comment
                         from
  In       ML_iGetColli‐                                                 Input data
           sionGuard‐
           State
  Out      ML_oGetCol‐                                                   Output data of the request
           lisionGuard‐
           State
STRUCT ML_iGetCollisionGuardState
Name        Data type    Inherited          Address      Initial value   Comment
                         from
  Emergen‐ LREAL                                                         If there are axes within this
cyDist                                                                   distance, the motion has to
                                                                         be stopped with an emer‐
                                                                         gency stop
   MinDist         LREAL                                                 If the axes are within this
                                                                         distance, there has to be a
                                                                         controlled motion of both
                                                                         axes
  Slow‐            LREAL                                                 If the axes are within this
DownDist                                                                 distance, decelerate the
                                                                         motion
   SyncDist        LREAL                                                 If the axes are within this
                                                                         distance, synchronize the
                                                                         motion of both axes
   ActPos          LREAL                                                 Actual position of the axis
   TargetPos       LREAL                                                 Target position of the axis
   ActBra‐         LREAL                                                 Axis braking distance
kingDist
   Neigh‐          LREAL                                                 Actual position of the
borPos                                                                   neighboring axis
   Neighbor‐       LREAL                                                 Target position of the
TargetPos                                                                neighboring axis
   Neighbor‐       LREAL                                                 Braking distance of the
BrakingDist                                                              neighboring axis
   Hystere‐        LREAL                                                 Offset added to minDist,
sisDist                                                                  slowDownDist and syn‐
                                                                         cDist to take the hyste‐
                                                                         resis into account when
                                                                         switching to a safe state

STRUCT ML_iGetCollisionGuardState
  PrevState ML_Collision‐                                           Previous state of the colli‐
GuardState                                              sion protection
STRUCT ML_oGetCollisionGuardState EXTENDS ML_oStateBase
Name       Data type    Inherited    Address     Initial value      Comment
                        from
  Error    BOOL         ML_oState‐                                  Error flag: TRUE means
                        Base                                        that an error has occurred
                                                                    (e.g. typing error in the
                                                                    object name)
  ErrorID    ULINT           ML_oState‐                             Specifies the type of
                             Base                                   occurred error. (Across four

bytes: Main diagnostics;
under four bytes: detailed
diagnostics). 0 indicates
“no error”
  State      ML_Collision‐                                          The resulting collision pro‐
GuardState                                             tection status
ENUM ML_CollisionGuardState
Name       Data type    Inherited         Address   Initial value   Comment
                        from
  MONI‐    INT                                                      Axis moves safely
TORING
  TAR‐     INT                                                      The axis may not reach
GETS_CROS                                                           the target position as other
SING                                                                axes may block the path
           INT                                                      A possible rear collision of
SYNC_ADVIC                                                          the axis with an adjacent
E                                                                   axis can occur, synchronize
                                                                    velocity
  SLOW‐   INT                                                       A possible head-on colli‐
DOWN_ADVI                                                           sion of the axis with a
CE                                                                  neighboring axis can occur,
                                                                    slowing down the velocity
  STOP       INT                                                    The collision protection
                                                                    stops the axis as the axis
                                                                    comes too close to a neigh‐
                                                                    boring axis
  EMER‐    INT                                                      The collision protection
GENCY STOP                                                          performs an emergency
                                                                    stop of the axis as the axis
                                                                    comes too close to a neigh‐
                                                                    boring axis
  UNKNOWN INT                                                       Collision protection status
                                                                    unknown

PLC function block CollisionAvoidance:

Table 87: ML_CollisionAvoidance
STRUCT ML_CollisionAvoidanceData
Name       Data type     Inherited          Address       Initial value   Comment
                         from
  In       ML_iCollisio‐                                                  Input data
           nAvoidance
  Out      ML_oCollisio‐                                                  Output data of the request
           nAvoidance
STRUCT ML_iCollisionAvoidance
Name        Data type     Inherited         Address       Initial value   Comment
                          from
  AxsName STRING(15)                                                      Name of the axis to which
                                                                          the collision avoidance is
                                                                          to be applied to
   Enabled         BOOL                                                   Collision avoidance is ena‐
                                                                          bled (if FALSE, only the
                                                                          collision protection status
                                                                          is retrieved)
  Emergen‐         LREAL                                                  If there are axes within this
cyDist                                                                    distance, the motion has to
                                                                          be stopped with an emer‐
                                                                          gency stop
   MinDist         LREAL                                                  If the axes are within this
                                                                          distance, there has to be a
                                                                          controlled motion of both
                                                                          axes
  Slow‐            LREAL                                                  If the axes are within this
DownDist                                                                  distance, decelerate the
                                                                          motion
   SyncDist        LREAL                                                  If the axes are within this
                                                                          distance, synchronize the
                                                                          motion of both axes
   ActPos          LREAL                                                  Actual position of the axis
   TargetPos       LREAL                                                  Target position of the axis
   ActBra‐         LREAL                                                  Axis braking distance
kingDist
   Neigh‐          LREAL                                                  Actual position of the
borPos                                                                    neighboring axis
   Neighbor‐       LREAL                                                  Target position of the
TargetPos                                                                 neighboring axis
   Neighbor‐       LREAL                                                  Braking distance of the
BrakingDist                                                               neighboring axis

STRUCT ML_iCollisionAvoidance
   Hystere‐ LREAL                                                Offset added to minDist,
sisDist                                                          slowDownDist and syn‐
                                               cDist to take the hyste‐
                                               resis into account when
                                               switching to a safe state
  PrevState   ML_Collision‐                                      Previous state of the colli‐
GuardState                                         sion protection
STRUCT ML_oCollisionAvoidance EXTENDS ML_oStateBase
Name       Data type     Inherited  Address      Initial value   Comment
                         from
  Error    BOOL          ML_oState‐                              Error flag: TRUE means

       Base                                    that an error has occurred
                                               (e.g. typing error in the
                                               object name)
  ErrorID     ULINT           ML_oState‐                         Specifies the type of
            Base                               occurred error. (Across four
                                               bytes: Main diagnostics;
                                               under four bytes: detailed
                                               diagnostics). 0 indicates
                                               “no error”
  State       ML_Collision‐                                      The resulting collision pro‐
GuardState                                         tection status

C-interface
  Command interface

//! @brief This method gets the collision guard state of an axis.
//!
//! @param[in]   handle    Handle of the interface.
//! @param[in]   params    Parameters of the collision guard.
//! @param[out] state      State of the collision guard.
//!
//! @return                Was everything okay?
extern "C" MotionResult MOTION_CORE_getCollisionGuardState(void* handle,
const motion::core::collision_avoidance::CollisionGuardParams& params ,
motion::core::collision_avoidance::CollisionGuardState& state);

  Collision avoidance:

namespace motion
{
  namespace core
  {
    namespace collision_avoidance
    {
/// @brief States for the collision guard.
enum class CollisionGuardState : uint32_t
{
MONITORING = 0,   ///< The axis is safe from collision
///< with the neighboring axis.
TARGETS_CROSSING, ///< The axis might not reach the
///< target end position, because an other
///< axis might be crossing its path.
SYNC_ADVICE,      ///< A possible head-to-tail collision

///< of axis with neighboring axis may
///< take place, synchronize velocity.
SLOWDOWN_ADVICE,       ///< A possible head-to-head collision
///< of axis with neighboring axis may
///< take place: slowdown.
STOP,                  ///< Collision guard executes a stop on
///< the axis, because the axis comes too
///< close to a neighboring axis.
EMERGENCY_STOP,        ///< Collision guard executes an
///< emergency stop on the axis, because
///< the axis comes too close to a
///< neighboring axis.
UNKNOWN,               ///< The collision guard state is
///< unknown.
};
/// @brief Parameters for the collision guard
struct CollisionGuardParams
{
double emergencyDist {};       ///< If axes are within this distance, then
        ///< the motion has to be stopped with
        ///< an emergency stop.
double minDist {};             ///< If axes are within this distance, then
        ///< the motion has to be stopped smoothly.
double slowDownDist {};        ///< If axes are within this distance, then
        ///< the motion has to be slowed down.
double syncDist {};            ///< If axes are within this distance, then
        ///< the motion of both axes has to be
        ///< synchronized.
double actPos {};              ///< The actual position of the axis.
double targetPos {};           ///< The target position of the axis.
double actBrakingDist {};      ///< The braking distance of the axis.
double neighborPos {};         ///< The actual position of the
        ///< neighboring axis.
double neighborTargetPos {};   ///< The target position of the
        ///< neighboring axis.
double neighborBrakingDist {}; ///< The braking distance of the
        ///< neighboring axis.
double hysteresisDist {};      ///< Offset added to minDist,
        ///< slowDownDist and syncDist to
        ///< include hysteresis in
        ///< switching to a safer state.
CollisionGuardState prevState; ///< The previous collision guard state.
};
    }
  }
}

typedef struct MotionSysIfT
{
  ::motion::core::MotionResult(*getCollisionGuardState)(void* handle, const
motion::core::collision_avoidance::CollisionGuardParams& params,
motion::core::collision_avoidance::CollisionGuardState& state);
} MotionSysIfT

typedef struct MotionCollisionAvoidanceIfT
{
  ::motion::collision_avoidance::MotionCollisionAvoidanceResult(*getCollisionGua
rdState)(void* handle, const

motion::core::collision_avoidance::CollisionGuardParams& params,
motion::core::collision_avoidance::CollisionGuardState& state);
  ::motion::collision_avoidance::MotionCollisionAvoidanceResult(*collisionAvoida
nce)(void* handle, const char* axsName, bool enable, const
motion::core::collision_avoidance::CollisionGuardParams& params,
motion::core::collision_avoidance::CollisionGuardState& state);
} MotionCollisionAvoidanceIfT;

Data Layer interface

motion/collision-avoidance/collision-avoidance
Write action input

table CollisionAvoidance {
  axsName:string;
  enable:bool;
  params:{
emergencyDist:double;
minDist:double;
slowDownDist:double;
syncDist:double;
actPos:double;
targetPos:double;
actBrakingDist:double;
neighborPos:double;
neighborTargetPos:double;
neighborBrakingDist:double;
hysteresisDist:double;
prevState:{ MONITORING, TARGETS_CROSSING, SYNC_ADVICE,
   SLOWDOWN_ADVICE, STOP, EMERGENCY_STOP, UNKNOWN};
  };
}

motion/collision-avoidance/collision-guard-state
Write action input

table GetCollisionGuardStateParams {
  emergencyDist:double;
  minDist:double;
  slowDownDist:double;
  syncDist:double;
  actPos:double;
  targetPos:double;
  actBrakingDist:double;
  neighborPos:double;
  neighborTargetPos:double;
  neighborBrakingDist:double;
  hysteresisDist:double;
  prevState:{ MONITORING, TARGETS_CROSSING, SYNC_ADVICE,
SLOWDOWN_ADVICE, STOP, EMERGENCY_STOP, UNKNOWN};
}

### 7.7.10 KinSafeAreaInExecutionCheckEnabled - Enabling the working

area monitoring
Basics
If monitoring of the safe zones and working areas is active (command option
has been enabled with the corresponding areas), the individual areas can
be disabled or enabled directly via Celix or the PLC interface. Programming
has an immediate effect on the check. In this way, the areas or zones to be
checked can also be influenced during an active motion.
This method is real-time capable if it is called for a safe zone or working area
that already exists (by name) when the Motion changes to the RUNNING state.
Otherwise (if it is called for a safe area that is created in the RUNNING state),
calling this function can take up to 100 microseconds.
When the kinematics are reset or when the status is switched from CONFIGU‐
RATION to RUNNING, all safe zones and working areas are reactivated.
If the transferred area name cannot be found in the safe zones or working
areas, an error message is displayed
A detailed functional description can be found under ⮫ Chapter 6.3.8 Working
areas and safe zones on page 308.

PLC:

ML_KinSafeAreaInExecutionCheckEnable
Name         Data type    Inherited  Address                Initial value   Comment
                          from
  Data       ML_KinSa‐                                                      InOut: Command parame‐
             feAreaInExe‐                                                   ters
             cutionCheck‐
             EnableData
  ML_KinSa‐ BOOL                                                            Returns, whether it was
feAreaInExe‐                                                                possible to add the com‐
cutionCheck‐                                                                mand to the kinematic
Enable                                                                      object.
                                                                            ● TRUE: The ML_KinSa‐
                                                                              feAreaP command could
                                                                              be added successfully
                                                                            ● FALSE: An error
                                                                              occurred. Details in
                                                                              ML_oCmdResult
STRUCT ML_KinSafeAreaPData
Name       Data type    Inherited             Address       Initial value   Comment
                        from
  In       ML_iKinSa‐                                                       Input: Command data of
           feAreaInExe‐                                                     the command
           cutionCheck‐
           Enable
  Out      ML_oState‐                                                       Output: Command parame‐
           Base                                                             ters

STRUCT ML_iKinSafeAreaInExecutionCheckEnable EXTENDS ML_iKinStateBase
Name        Data type    Inherited   Address      Initial value Comment
                         from
  KinName STRING(15) ML_iKinSta‐                                Name of the kinematics
                         teBase                                 used to execute the com‐
                                                                mand
  SafeArea STRING(50)                                           Specifies the command
                                                                source, e.g PlcApplication1
                                                                is displayed in the diag‐
                                                                nostic messages
  Enable    BOOL                                  FALSE         Activate or deactivate mon‐
                                                                itoring of the safe zone or

                                            working area during com‐
                                            mand processing

Data Layer:
Method: POST
URL: https://<ip-addr>/automation/api/v2/nodes/motion/kin/<kin_name>/cfg/
functions/safe-areas/execution-check-enabled/<safeArea_name>

BundleIF:

//! @brief This method enables or disables the safe area check
in the execution for the given safe area.
//!
//! This method is real-time capable, when its called for a
safe area, that already exists (by name) when the motion
kernel is switched to RUNNING state.
//! Otherwise (when called for a safe area, that is created in
RUNNING state), the call of this function might take up to
100microseconds.
//!
//! The given safe area name must refer to an existing
configured safe area when this call is done, otherwise an
error (ERR_INVALID_PARAM) is returned.
//! This is not true, when the safe area existed when the
motion kernel was switched to RUNNING state and deleted
afterwards. In this case, this function
//! returns STS_OK and will also affect a safe zone
monitoring, that is still active with the old (yet deleted in
the configuration) safe area.
//!
//! You may call this method only in RUNNING state, otherwise
an error (ERR_INVALID_STATE) is returned.
//!
//! See command option kinSafeAreaInExecution for details.
//!
//! @param[in]   handle         Handle of the interface
//! @param[in]   kinName        Name of the kinematics
//! @param[in]   safeAreaName   Name of the safe zone or
                                work area
//! @param[in]   checkEnabled   True, if the safe area
                                check should be enabled,
                                false otherwise
//! @return                     Status of the function
                                call: STS_OK or an error

                                code on failure.
::motion::core::MotionResult(*setSafeAreaInExecutionCheckEnable
d)(void* handle, const char* kinName, const char*
safeAreaName, bool checkEnabled);

### 7.7.11 KinSafeAreaInExecutionAddCheckSize - Online modification of

the working area size
Basics
With active monitoring of the safe zones and working areas (command option
active), the sizes of the individual areas can be changed directly via Celix or
the PLC interface. The transferred value has an immediate effect on all safe
zones and working areas of the kinematics. In this way, the areas or zones to
be checked can also be influenced during an active motion.
The safe zones and working areas are affected as follows:
● Positive value - increases the safe zones and reduces the working areas.
   The valid range is reduced
● Negative value - reduces the safe zones and increases the working areas.
   The valid area is enlarged
The set value reduces or increases both the minimum and maximum value of
the respective protection and operating range.
Example:
Safe zone with the following properties:
X minimum: 0, maximum: 100; Y minimum: 20, maximum: 90
Adjusting the range size by: +10
Resulting size of the safe zone:
X minimum: -10, maximum: 110; Y minimum: 10, maximum: 100
The modification of the area sizes affects all active ranges of the kinematics.
By changing the area sizes, it is possible to adapt to the dynamics of the
motion. In case of a high dynamics, a positive value can reduce the valid
range, allowing earlier intervention if the valid range is violated.
The modification can also be used to reduce the size of an area so that it is no
longer included in the check.
A detailed functional description can be found under ⮫ Chapter 6.3.8 Working
areas and safe zones on page 308.

PLC:

ML_KinSafeAreaInExecutionAddCheckSize
Name        Data type    Inherited    Address               Initial value   Comment
                         from
  Data      ML_KinSa‐                                                       InOut: Command parame‐
            feAreaInExe‐                                                    ters
            cutionAdd‐
            CheckSize

ML_KinSafeAreaInExecutionAddCheckSize
  ML_KinSa‐ BOOL                                                   Returns, whether it was
feAreaInExe‐                                                       possible to add the com‐
cutionAdd‐                                                         mand to the kinematic
CheckSize                                                          object.
                                               ● TRUE: The ML_KinSa‐
                                                 feAreaP command could
                                                 be added successfully
                                               ● FALSE: An error
                                                 occurred. Details in
                                                 ML_oCmdResult
STRUCT ML_KinSafeAreaInExecutionAddCheckSizeData

Name       Data type    Inherited    Address     Initial value     Comment
                        from
  In       ML_iKinSa‐                                              Input: Command data of
           feAreaInExe‐                                            the command
           cutionAdd‐
           CheckSize
  Out      ML_oState‐                                              Output: Command parame‐
           Base                                                    ters
STRUCT ML_iKinSafeAreaInExecutionAddCheckSize EXTENDS ML_iKinStateBase
Name          Data type  Inherited   Address      Initial value Comment
                         from
  KinName STRING(15) ML_iKinSta‐                                Name of the kinematics
                         teBase                                 used to execute the com‐
                                                                mand
  Additional‐ LREAL                               0.0           Additive size to modify the
CheckSize                                                       working area and safe zone
                                                                for inspection during proc‐
                                                                essing

Data Layer:
The current value can be called up under the following Data Layer node:
URL: https://<ip-addr>/automation/api/v2/nodes/motion/kin/<kin_name>/cfg/
functions/safe-areas/execution-add-check-size

BundleIF:

/// @brief This method sets the additional check size for the
checks in MCS/WCS/PCS.
///
/// You may set some additional size of safe zones (become
larger with positive addSize) and work areas (become smaller
with positive addSize) for the
/// monitoring in the execution (see command option
kinSafeAreaInExecution for details).
///
/// The provided size is used, whenever a safe zone or work
area is defined in machine, world or product coordinate system
(MCS/WCS/PCS). Therefore, the given value refers to
/// coordinates of the kinematics.
///
/// This method is real-time capable.
///

/// @param[in]        handle
                           Handle of the interface
/// @param[in]        kinName
                           Name of the kinematics
/// @param[in]        addSize
                           New additional check size
                           for the checks in
                           MCS/WCS/PCS
/// @return                Status of the function
                           call: STS_OK or an error
                           code on failure.
::motion::core::MotionResult(*setSafeAreaInExecutionAddCoordChe
ckSize)(void* handle, const char* kinName, double addSize);
