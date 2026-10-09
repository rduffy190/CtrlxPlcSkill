# 7.8 Additional information

### 7.8.1 AxsGetIpoAddData - Additional axis data

Basics
The axis Motion objects have additional Motion object data, related to the
actual motion command, for non-real-time access:
●   Current time (from start)
●   Time until target position is reached
●   Current distance (from start)
●   Remaining distance until target position
If no motion command is pending, all values are set to zero.

PLC:

ML_AxsGetIpoAddData
Name        Data type           Inherited      Address       Initial value   Comment
                                from
   Data      ML_AxsGetI‐                                                     Output: Command parame‐
             poAddData                                                       ters
   ML_AxsGe‐ BOOL                                                            Returns information
tIpoAddData                                                                  whether the command can
                                                                             be added to the axis
                                                                             object.
                                                                             ● TRUE: The ML_AxsGe‐
                                                                               tIpoAddData command
                                                                               could be added success‐
                                                                               fully
                                                                             ● FALSE: An error
                                                                               occurred. Details in
                                                                               ML_oCmdResult
STRUCT ML_AxsGetIpoAddDataData
Name         Data type   Inher‐             Addres Initial   Comment
                         ited               s      value
                         from
  In         ML_iAxsSta‐                                     Input: Command data of the command
             teBase

STRUCT ML_AxsGetIpoAddDataData
  Out        ML_oGetI‐                                  Output: Command parameters
poAddData
STRUCT ML_iAxsStateBase
Name          Data type       Inher‐   Addres Initial   Comment
                              ited     s      value
                              from
  AxisName      STRING(63)                              Name of the axis used to execute the com‐
                                                        mand
STRUCT ML_oGetIpoAddData EXTENDS ML_oStateBase
Name           Data type Inher‐  Addres Initial Comment

     ited    s      value
     from
  Error        BOOL      ML_oSta                Error ID TRUE indicates that an error
     teBase                 occurred
  ErrorID      ULINT     ML_oSta                Specifies the type of occurred error: The
     teBase                 upper 4 bytes refer to the main diag‐
                            nostics, the lower 4 bytes refer to the
                            detailed diagnostics, 0 means no error
  DistToTarget LREAL                            Distance to target position (kinematic
                            motion) of the current interpolation
  DistFrom‐    LREAL                            Distance to starting position (kinematic
Start                                           motion) of the current interpolation
  TimeToTarget LREAL                            Estimated time to target position with cur‐
                            rent override of the current interpolation
  TimeFrom‐    LREAL                            Lapsed time from the starting position
Start                                           with current override of the current inter‐
                            polation

Data Layer:
Method: GET
For more information about the data structure, refer to
URL:      https://<ip-addr>/automation/api/v2/nodes/motion/axs/<axs_name>/
state/values/ipo-add
Access to individual values:
URL:      https://<ip-addr>/automation/api/v2/nodes/motion/axs/<axs_name>/
state/values/ipo-add/dist-from-start
URL:      https://<ip-addr>/automation/api/v2/nodes/motion/axs/<axs_name>/
state/values/ipo-add/dist-to-target
URL:      https://<ip-addr>/automation/api/v2/nodes/motion/axs/<axs_name>/
state/values/ipo-add/time-from-start
URL:      https://<ip-addr>/automation/api/v2/nodes/motion/axs/<axs_name>/
state/values/ipo-add/time-to-target
Payload: (blank)

Python:
<result> = motion.get_axs_ipo_add_data( <axsName> )

Return a directory with these entries:

●   dist_from_start - distance from start position
●   dist_to_target - distance to target position
●   time_from_start - lapsed time from the start position
●   time_to_target - estimated time to target position (assuming an override)
● <axsName> - string, axis name

BundleIF:
//! @brief This method gets the additional interpolation data
from an axis.
//! @param[in]     axsName       Name of the axis
//! @param[out]    distFromStart Interpolated distance from
start point
//! @param[out]    distToTarget  Distance to interpolate to
target position
//! @param[out]    timeFromStart Interpolated time from start
point
//! @param[out]    timeToTarget  Estimated time to interpolate
to target position
//!
//! @return                      Was everything okay?
virtual MotionResult getAxsAdditionalIpoData(const char*
axsName, double& distFromStart, double& distToTarget, double&
timeFromStart, double& timeToTarget) const = 0;

### 7.8.2 KinGetIpoAddData - Additional kinematic data

Basics
The kinematic motion objects provide some additional Motion object data,
related to the actual motion command, for non-real-time access:
● Current time (from start)
● Time until target position is reached
● Current distance (from start)
● Remaining distance until target position
If no motion command is active, all values are set to zero.

PLC:

ML_KinGetIpoAddData
Name        Data type            Inherited     Address       Initial value   Comment
                                 from
   Data            ML_KinGetI‐                                               InOut: Command parame‐
                   poAddData                                                 ters

ML_KinGetIpoAddData
   ML_KinGe‐ BOOL                                                    Returns whether the com‐
tIpoAddData                                                          mand could be added.
                                                 ● TRUE: The ML_KinGe‐
                                                   tIpoAddData command
                                                   could be added success‐
                                                   fully
                                                 ● FALSE: An error
                                                   occurred. Details in
                                                   ML_oCmdResult
STRUCT ML_KinGetIpoAddDataData
Name         Data type   Inher‐       Addres Initial   Comment

     ited         s      value
     from
  In         ML_iKinSta‐                               Input: Command data of the command
teBase
  Out        ML_oGetI‐                                 Output: Command parameters
poAddData
STRUCT ML_iKinStateBase
Name          Data type      Inher‐   Addres Initial   Comment
                             ited     s      value
                             from
  KinName       STRING(63)                             Name of the kinematics from which you
                                                       want to request data
STRUCT ML_oGetIpoAddData EXTENDS ML_oStateBase
Name           Data type Inher‐  Addres Initial Comment
                         ited    s      value
                         from
  Error        BOOL      ML_oSta                Error ID TRUE indicates that an error
                         teBase                 occurred
  ErrorID      ULINT     ML_oSta                Specifies the type of occurred error: The
                         teBase                 upper 4 bytes refer to the main diag‐
                                                nostics, the lower 4 bytes refer to the
                                                detailed diagnostics, 0 means no error
  DistToTarget LREAL                            Distance to target position (kinematic
                                                motion) of the current interpolation
  DistFrom‐    LREAL                            Distance to starting position (kinematic
Start                                           motion) of the current interpolation
  TimeToTarget LREAL                            Estimated time to target position by taking
                                                the current override into consideration
  TimeFrom‐    LREAL                            Lapsed time from the starting position
Start

Data Layer:
Method: POST
For more information about the data structure, refer to
URL:      https://<ip-addr>/automation/api/v2/nodes/motion/kin/<kin_name>/
state/values/ipo-add
Access to individual values:
URL:      https://<ip-addr>/automation/api/v2/nodes/motion/kin/<kin_name>/
state/values/ipo-add/dist-from-start

URL:      https://<ip-addr>/automation/api/v2/nodes/motion/kin/<kin_name>/
state/values/ipo-add/dist-to-target
URL:      https://<ip-addr>/automation/api/v2/nodes/motion/kin/<kin_name>/
state/values/ipo-add/time-from-start
URL:      https://<ip-addr>/automation/api/v2/nodes/motion/kin/<kin_name>/
state/values/ipo-add/time-to-target
Payload: (blank)

Python:
<result> = motion.get_kin_ipo_add_data( <kinName> )

Return a directory with these entries:
●   dist_from_start - distance from start position (on the distance)
●   dist_to_target - distance to target position (on the distance)
●   time_from_start - lapsed time from the start position
●   time_to_target - estimated time to target position by taking the current
    override into consideration
● <kinName> - string, kinematic object name

BundleIF:
//! @brief This method gets the additional interpolation data
from kinematics
//! @param[in]     kinName       Name of the kinematics
//! @param[out]    distFromStart Interpolated distance from
start point
//! @param[out]    distToTarget  Distance to interpolate to
target position
//! @param[out]    timeFromStart Interpolated time from start
point
//! @param[out]    timeToTarget  Estimated time to interpolate
to target position
//!
//! @return                      Was everything okay?
virtual MotionResult getKinAdditionalIpoData(const char*
kinName, double& distFromStart, double& distToTarget, double&
timeFromStart, double& timeToTarget) const = 0;

### 7.8.3 KinCoordTransform - Converting the coordinate system

Basics
This auxiliary function converts the position and, if applicable, the orientation
of a kinematic model from one coordinate system to another.
KinCoordTransform supports the following coordinate systems:
●   ACS
●   MCS
●   WCS
●   PCS

PLC:

ML_KinCoordTransform
Name        Data type       Inherited   Address      Initial value   Comment
                            from
  Data        ML_Kin‐                                                InOut: Command parame‐

CoordTrans‐                                            ters
formData
   ML_Kin‐    BOOL                                                   Returns, whether it was
CoordTrans‐                                                          possible to add the com‐
form                                                                 mand to the kinematic
                                         object.
                                         ● TRUE: The command
                                           could be added success‐
                                           fully
                                         ● FALSE: An error
                                           occurred. Details in
                                           ML_oKinGetPos in the
                                           data struct
STRUCT ML_KinCoordTransformData
Name       Data type    Inherited       Address      Initial value   Comment
                        from
  In       ML_iKin‐                                                  Input: Command data of
           CoordTrans‐                                               the command
           form
  Out      ML_oKin‐                                                  Output: Output data of the
           GetPos                                                    query
STRUCT ML_iKinCoordTransform
Name        Data type    Inherited      Address      Initial value   Comment
                         from
  InCo‐     STRING(15)                                               Name of the input coordi‐
ordSys                                                               nate system
  Out‐      STRING(15)                                               Name of the initial coordi‐
CoordSys                                                             nate system
  Position  ARRAY                                                    Position in the input coor‐
            [0..15] OF                                               dinate system
            LREAL
STRUCT ML_oKinGetPos
Name       Data type        Inherited   Address      Initial value   Comment
                            from
  Error       BOOL                                                   Error ID TRUE indicates
                                                                     that an error occurred

STRUCT ML_oKinGetPos
  ErrorID  UDINT                                                           Specifies the type of
                                                    occurred error: The upper
                                                    4 bytes reflect the main
                                                    diagnostics, the lower 4
                                                    bytes reflect the detailed
                                                    diagnostics, 0 means no
                                                    error
   Position        BOOL                                                    Position in the requested
                                                    reference coordinate
                                                    system

Data Layer:
Method: POST
URL: motion/kin/<kin_name>/state/values/coord-transform
Payload:
{
"type":"object","value":
{
    inPos: [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    inCoordSys: "WCS",
    outPos: [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    outCoordSys: "PCS"
}
}

Python:
<outPos> = motion.coord_transform(kin: str, pos:
Tuple[float, ...], coord_sys_in: str, coord_sys_out: str) ->
Tuple[float, ...]

Converts a position from one to a coordinate system to another coordinate
system. Returns the converted position.
●   <kin> - string, kinematic name
●   <pos> - Tuple[float, ...], position to be converted
●   <coord_sys_in> - string, input coordinate system
●   <coord_sys_out> - string, output coordinate system

BundleIF:
The required command type is:

/// @brief This method transforms the given coordinates into
other coordinate systems based on the actual state of the
kinematics.
///
/// The function calls the coordinate transformation functions
of the active command. So, it depends on the current state of
the kinematics (e.g. if you have an MCS
/// command option active).
///
/// Coordinate systems are:
/// * ACS - axis coordinate system

/// * MCS - machine coordinate system
/// * WCS - world coordinate system
/// * PCS - product coordinate system
///
/// The position is expected and returned as an array of 16
(MAX_KIN_AXES) double values.
/// * in ACS - this are the axis positions of all assigned axes
/// * in MCS/WCS/PCS - XYZ coordinates at index 0..2; Euler
angles extrinsic XYZ (often also called ABC) at index 3..5;
additional axes at index 6..15
///
/// The function is optimized for speed and can be used in
a real-time context (lock- and wait-free), when the motion

kernel is in state RUNNING,
/// but keep in mind, that here might be some calculations
required.
/// If the motion kernel is not in state RUNNING, the function
call is not real-time capable.
///
/// @param[in]     handle    Handle of the
                             interface
/// @param[in]     kinName Name of the
                             kinematics
/// @param[in,out] pos       position (Array of
                             MAX_KIN_AXES size)
/// @param[in]     inCOS     coordinate system in
                             which pos is given
/// @param[in]     outCOS    Target coordinate
                             system for the
                             position (result is
                             in pos)
/// @return                  Status of the
                             function call:
                             STS_OK or an error
                             code on failure.
::motion::core::MotionResult(*kinCoordTransform)(void*
handle, const char* kinName,
double* pos, ::motion::core::cmd::kin::CmdTargetCOS
inCOS, ::motion::core::cmd::kin::CmdTargetCOS outCOS);

### 7.8.4 AxsGetExtrapolatedActValues - Extrapolated axis values

Data Layer:
Method: GET
For more information about the data structure, refer to
URL:      https://<ip-addr>/automation/api/v2/nodes/motion/axs/<axs_name>/
state/values/extrapolated-actual
Access to individual values:
URL:      https://<ip-addr>/automation/api/v2/nodes/motion/axs/<axs_name>/
state/values/extrapolated-actual/acc
URL:      https://<ip-addr>/automation/api/v2/nodes/motion/axs/<axs_name>/
state/values/extrapolated-actual/pos
URL:      https://<ip-addr>/automation/api/v2/nodes/motion/axs/<axs_name>/
state/values/extrapolated-actual/vel
Payload: (blank)

Python:
Get-Function for reading the extrapolated values
// @brief Implement get act extrapolated values request.
      /// @param[in]   instance Name of the script instance.
      /// @param[in]   reqData   Request data with axis name.
      /// @param[out] respID     Response id that should be
sent to the runner.
      /// @param[out] respData Response data with FlatBuffer.
      /// @return STS_OK for a handled request or an error
return code on communication errors.
      ::script::manager::ScriptManagerResult
extrapolatedvalues(const ::script::manager::InstanceId&
instance,

const ::comm::datalayer::Variant* reqData,
                                                                  ::script
::manager::comm::MsgType& respID,
                                                                  ::comm::
datalayer::Variant* respData);

BundleIF:
//! @brief This method gets the additional interpolation data
from an axis.
//! @param[in]    axsName Name of the axis
//! @param[out]   exPos     Extrapolated position
//! @param[out]   exVel     Extrapolated velocity
//! @param[out]   exAcc     Extrapolated acceleration
//!
//! @return                      Was everything okay?
virtual MotionResult getAxisExtrapolatedActValues(const char*
axsName, double& exPos, double& exVel, double& exAcc) const =
0;

Further information
● ⮫ Chapter 7.8.4 AxsGetExtrapolatedActValues - Extrapolated axis values
  on page 779

### 7.8.5 AxsSetExtrapolateExternalDynamic - Source for dynamic extrapo‐

lation data
Basics
This configuration allows you to set the source of dynamic data of an encoder
for extrapolation.
Command interface: Data Layer, PLC

PLC:

ML_AxsSetExtrapolateExternalDynamic
Name          Data type           Inhe Address          Initial value   Comment
                                  rited
                                  from
  Data        ML_AxsSetExtrapola‐                                       Output: Command parame‐
              teExternalDynamic‐                                        ters
              Data
  ML_AxsSe‐ BOOL                                                        Returns information
tExtrapola‐                                                             whether the command can
teExternalDy‐                                                           be added to the axis
namic                                                                   object.
                                                                        ● TRUE:

                                                     The ML_AxsSetExtra‐
                                                     polateExternalDynamic
                                                     command was success‐
                                                     fully executed
                                                   ● FALSE: An error
                                                     occurred. Details in
                                                     ML_oStateBase
STRUCT ML_AxsSetExtrapolateExternalDynamicData
Name         Data type    Inher‐   Addres Initial       Comment
                          ited     s      value
                          from
  In         ML_iAxsSe‐                                 Input: Command data of the command
             tExtrapola‐
             teExternal‐
             Dynamic
  Out        ML_oState‐                                 Output: Command parameters
             Base
STRUCT ML_iAxsSetExtrapolateExternalDynamic EXTENDS ML_iAxsStateBase
Name         Data type   Inherited    Address     Initial value Comment
                         from
   AxisName STRING(63) ML_iAxsSta‐                              Name of the axis used to
                         teBase                                 execute the command
   Velocity  LREAL                                              External velocity
   Accelera‐ LREAL                                0             External acceleration (if no
tion                                                            external acceleration value
                                                                is specified, the default
                                                                value of 0 is used.)
STRUCT ML_oStateBase
Name         Data type        Inher‐   Addres Initial   Comment
                              ited     s      value
                              from
  Error          BOOL                                   Error ID TRUE indicates that an error
                                                        occurred
  ErrorID        ULINT                                  Specifies the type of occurred error: The
                                                        upper 4 bytes reflect the main diagnostics,
                                                        the lower 4 bytes reflect the detailed diag‐
                                                        nostics, 0 means no error

Data Layer:
Method: POST

URL: https://<ip-addr>/automation/api/v2/nodes/motion/axs/<axs_name>/cfg/
functions/extrapolation/extrapolate-dynamic-source
Payload:
"Actual": Actual axis value
"External": External encoder
Method: POST
URL: https://<ip-addr>/automation/api/v2/nodes/motion/axs/<axs_name>/cfg/
functions/extrapolation/extrapolate-external-dynamic-select
Payload:
"Velocity": Velocity
"VelocityAndAcceleration": Velocity and acceleration

Further information
● ⮫ Chapter 7.8.4 AxsGetExtrapolatedActValues - Extrapolated axis values
  on page 779

### 7.8.6 AxsGetBrakingDistance, AxsGetBrakingDistanceEx - Determining

the current braking distance
Basics
Use the GetBrakingDistance and GetBrakingDistanceEx function to determine
the length of the current braking distance.
The application program has to be able to determine the braking distance of
an axis. The braking distance is the distance from the current position to com‐
plete standstill when the override is set to 0. The braking distance is based
on the current velocity, acceleration and active dynamic limit values or on
the current velocity, acceleration and configuration limits. The axis can be an
individual axis, a gantry axis or a kinematic axis. Currently, only the Cartesian
kinematics is supported when calculating a kinematic axis. Two functions are
available to calculate a braking distance, GetBrakingDistance and GetBraking‐
DistanceEx.
Use GetBrakingDistance and GetBrakingDistanceEx only when necessary.
These functions are CPU intensive functions.

Functional description

GetBrakingDistance
GetBrakingDistance provides the current braking distance based on the cur‐
rent velocity, acceleration and active dynamic limit values and supports
normal axes, gantry axes and kinematic axes. Cartesian kinematic axes with
linear motion are supported for the KinMove, KinJog and KinMoveDirect func‐
tions.
GetBrakingDistance cannot determine the braking distance in the following
situations and returns the error ERR_NOT_SUPPORTED:
● The active command is an unbuffered kinematic command
● The active command is a generic axis or kinematic command, e.g. AxsFixed‐
  Stop, AxsCyclicSetpoint, AxsHoming, AxsGearInPos, AxsCtrlBasedHoming,
  AxsCtrlBasedGantryHoming
● The kinematics is not Cartesian. Note that this is not checked in the soft‐
  ware
● In the error handling

GetBrakingDistanceEx
GetBrakingDistanceEx contains the functionality of GetBrakingDistance and
additionally supports the calculation of the braking distance for emer‐
gency braking. An enumeration BrakingDistanceType defines the members
SOFT_STOP and ESTOP. These members define the type of braking distance
to be calculated (input parameter) and the returned calculated braking
distance (output parameter). GetBrakingDistanceEx returns the emergency
braking distance if the calculation of the soft stop distance is not possible
and ESTOP has been selected.
Differences between GetBrakingDistance and GetBrakingDistanceEx:
● GetBrakingDistanceEx has an input parameter selectedTypes that specifies
   which types of braking distances are taken into account in the calculation.

   The value of selectedTypes can be ESTOP, SOFT_STOP or a combination of
   both
● GetBrakingDistanceEx has an output parameter distanceType that specifies
   what kind of calculated braking distance is returned. The value of distance‐
   Type can be ESTOP or SOFT_STOP
● GetBrakingDistanceEx returns the emergency braking distance instead of
   the error ERR_NOT_SUPPORTED, if ESTOP is specified in selectedTypes
The application can select one or more brake types for which the GetBraking‐
DistanceEx function calculates the braking distance. The selected brake types
are specified in the selectedTypes array. The array can contain the values
SOFT_STOP and/or ESTOP. GetBrakingDistanceEx returns the type of braking
distance, distanceType, in addition to the braking distance. DistanceType
describes which type of braking distance is calculated. The following cases
are possible.
● If the array selectedTypes is empty, GetBrakingDistanceEx returns the
  parameter error ERR_INVALID_PARAM
● If the selectedTypes array contains invalid values, GetBrakingDistanceEx
  returns the parameter error ERR_INVALID_PARAM
● If the array selectedTypes contains only SOFT_STOP, GetBrakingDistanceEx
  behaves identically to the GetBrakingDistance function. If GetBrakingDis‐
  tanceEx is successful, distanceType contains the value SOFT_STOP and
  brakingDistance contains the SOFT_STOP braking distance
● If the selectedTypes array contains only ESTOP, GetBrakingDistanceEx is
  usually successful unless there is an internal system error. DistanceType
  contains ESTOP and brakingDistance contains the ESTOP braking distance
● If the array selectedTypes contains SOFT_STOP and ESTOP, GetBrakingDis‐
  tanceEx calculates the braking distance in the same way as GetBrakingDis‐
  tance
  – If the calculation of the SOFT_STOP braking distance is possible, distan‐
      ceType contains the value SOFT_STOP and brakingDistance contains the
      SOFT_STOP braking distance
  – If the calculation of the SOFT_STOP braking distance is not possible,
      GetBrakingDistanceEx calculates the ESTOP braking distance. This cal‐
      culation is usually successful. DistanceType contains ESTOP and bra‐
      kingDistance contains the ESTOP braking distance

PLC:

ML_AxsGetBrakingDistance
Name        Data type    Inherited         Address          Initial value   Comment
                         from
  Data      ML_AxsGet‐                                                      InOut: Command parame‐
            BrakingDis‐                                                     ters
            tance
  ML_Axs‐   BOOL                                                            Returns whether the com‐
GetBraking‐                                                                 mand could be added.
Distance                                                                    ● TRUE: The ML_AxsGet‐
                                                                              BrakingDistance com‐
                                                                              mand could be added
                                                                              successfully
                                                                            ● FALSE: An error
                                                                              occurred. Details in
                                                                              ML_oCmdResult
STRUCT ML_AxsGetBrakingDistanceData
Name       Data type    Inherited   Address                 Initial value   Comment
                        from
  In       ML_iAxsSta‐                                                      Input parameters
           teBase
  Out      ML_oAxsGet‐                                                      Output data of the query
           BrakingDis‐
           tance
STRUCT ML_iAxsStateBase
Name        Data type   Inherited          Address          Initial value   Comment
                        from
  AxisName STRING(63)                                                       Name of the axis from
                                                                            which you want to request
                                                                            data
STRUCT ML_oAxsGetBrakingDistance EXTENDS ML_oStateBase
Name       Data type    Inherited    Address    Initial value               Comment
                        from
  Error    BOOL         ML_oState‐                                          Error ID, TRUE indicates
                        Base                                                that an error occurred (e.g.
                                                                            typo in the object name)
   ErrorID         ULINT      ML_oState‐                                    Specifies the type of the
                              Base                                          occurred error (higher 4
                                                                            bytes are main diagnostics,
                                                                            low 4 bytes are detailed
                                                                            diagnostics). 0 indicates
                                                                            “no error”
  Braking‐         LREAL                                                    Braking distance
Distance

PLC:

ML_AxsGetBrakingDistanceEx
Name        Data type    Inherited       Address      Initial value   Comment
                         from
  Data      ML_AxsGet‐                                                InOut: Command parame‐

BrakingDis‐                                               ters
tanceEx
  ML_Axs‐   BOOL                                                      Returns whether the com‐
GetBraking‐                                                           mand could be added.
DistanceEx                                                            ● TRUE: The ML_AxsGet‐
  BrakingDistance com‐
  mand could be added
  successfully
● FALSE: An error
  occurred. Details in
  ML_oCmdResult
STRUCT ML_AxsGetBrakingDistanceExData
Name       Data type    Inherited    Address          Initial value   Comment
                        from
  In       ML_iAxsGet‐                                                Input parameters
           BrakingDis‐
           tanceEx
  Out      ML_oAxsGet‐                                                Output data of the query
           BrakingDis‐
           tanceEx
STRUCT ML_iAxsGetBrakingDistanceEx EXTENDS ML_iAxsStateBase
Name        Data type   Inherited    Address     Initial value        Comment
                        from
  AxisName STRING(63)                                                 Name of the axis from
                                                                      which you want to request
                                                                      data
  Selected‐   ARRAY[0..7]                                             Array of selected braking
Types         OF ML_Bra‐                                              distance types that are
              kingDistance‐                                           taken into consideration in
              Type                                                    the calculation.
                                                                      Note: The first UNDEFINED
                                                                      in the array indicates the
                                                                      end of the array. Other
                                                                      braking distance types
                                                                      after this UNDEFINED are
                                                                      ignored

ENUM ML_BrakingDistanceType
Name       Data type    Inherited              Address       Initial value   Comment
                        from
  UNDE‐    INT                                               0               Invalid braking distance
FINED                                                                        type
  ESTOP    INT                                                               Emergency stop path
           INT                                                               Smooth braking distance
SOFT_STOP                                                                    (according to override = 0)
STRUCT ML_oAxsGetBrakingDistanceEx EXTENDS ML_oStateBase
Name       Data type    Inherited    Address    Initial value                Comment
                        from
  Error    BOOL         ML_oState‐                                           Error ID, TRUE indicates
                        Base                                                 that an error occurred (e.g.
                                                                             typo in the object name)
   ErrorID         ULINT          ML_oState‐                                 Specifies the type of the
                                  Base                                       occurred error (higher 4
                                                                             bytes are main diagnostics,
                                                                             low 4 bytes are detailed
                                                                             diagnostics). 0 indicates
                                                                             “no error”
  Braking‐         LREAL                                                     Braking distance
Distance
  Distance‐        ML_Braking‐                                               Type of calculated braking
Type               DistanceType                                              distance

Data Layer:
Method: GET
URL:      https://<ip-addr>/automation/api/v2/nodes/motion/axs/<axs_name>/
state/values/braking-distance
URL:      https://<ip-addr>/automation/api/v2/nodes/motion/axs/<axs_name>/
state/values/braking-distance-ex

Python:
<brakingDistance> =
motion.get_axs_braking_distance( <axsName> )

def get_axs_braking_distance_ex(axs: str, selected_types:
Tuple[str] = ('SOFT_STOP', 'ESTOP')) -> Dict:

Determines the braking distance of a single axis.
● <axsName> - string, axis object name
● <brakingDistance> - double, current braking distance
Read the braking distance of the specified axis with the selected brake type.
Arguments:
● axs -- axis name
● selected_types -- the selected brake types ("SOFT_STOP", "ESTOP") that
  will be taken into account in the calculation
Return:
● Dict -- data type: dictionary with the fields "braking_distance" (calculated
  braking distance, float), "distance_type" (type of calculated braking dis‐
  tance, string ("SOFT_STOP" or "ESTOP")).

BundleIF:
/// This method gets the braking distance based on the current
interpolated velocity/acceleration and active dynamic limits
/// Currently only linear motion is supported in the
calculation for a kinematic axis. For example, not supported
by the motion KinMoveDirectAsync
/// @param[in]   handle          Handle of the interface
/// @param[in]   axsName         Name of the axis
/// @param[out] brakingDist      Braking distance
/// @return                      Was everything okay?
extern "C" MotionResult MOTION_CORE_getBrakingDistance(void*
handle, const char* axsName, double& brakingDist);

BundleIF:
/// @brief This enumeration defines the possible braking distance types that
///          can be selected as input, and can be given as output by the function
///          getBrakingDistanceEx.
enum class BrakingDistanceType
   {
UNDEFINED,    ///< invalid braking distance type
ESTOP,        ///< emergency stop distance
SOFT_STOP     ///< soft stop distance (corresponding to setting override to
0)
   };

/// @brief Get the braking distance of an axis with the specified braking
distance types.
///
/// @param[in] handle             Handle of the interface.
/// @param[in] axsName            Name of the axis.
/// @param[in] selectedTypes      Array of selected braking distance types
///                               which are considered in the calculation.
/// @param[in] nrOfSelectedTypes Number of elements in selectedTypes.
/// @param[out] brakingDistance   Calculated braking distance.
/// @param[out] distanceType      Type of the calculated braking distance.
/// @param[in] inInternalUnits    Provide the distance in internal units?
///                               Default = FALSE (distance in given in
//                                configured standard units).
/// @return                       Status of the function call.
///                               STS_OK or an error code on failure.

extern "C" MotionResult MOTION_CORE_getBrakingDistanceEx(void* handle,
const char* axsName, const BrakingDistanceType* selectedTypes, uint32_t
nrOfSelectedTypes, double& brakingDistance, BrakingDistanceType& distanceType);

### 7.8.7 GetCmdState - Command states

Basics
To create an application (in particular in case of PLC applications), the com‐
mand state has to be determined. On the basis of this information, the appli‐
cation can trigger more actions.
A typical scheme is designed as follows:
1.      A command is specified to the control
2.      Cyclically query whether the command is completed
3.      Once completed, the next command can be executed

As the status is queried cyclically (if required, also in a real-time task), it has
to be real-time capable. This means, the runtime has to be safely limited and
no other means of synchronization (such as Mutex, Semaphore) may be used.
This also comprises reserving and releasing memory. Browsing of large lists is
not possible (also refer to the restrictions under “Command status query”).
Required command states:
● Not yet active → the command is not yet being processed
● Active → the command is currently being processed
● Completed → the command has been completed/the target state has been
  reached
● Canceled → the command was canceled

Functional description

Command identification
To be able to identify the commands in the control, each executed com‐
mand is assigned an identification (cmdID). This identification is returned as
response during the (successful) execution of the command. The application
has to save this cmdID to query the command state at a later point.
Command status query
The command state can be queried via different interfaces. The Motion object
(axis name/kinematic name) as well as the cmdID have to be specified for
each function. The function returns the command status. If an invalid cmdID
is specified (which is not returned in the axis/kinematics when executing a
command), the query behavior is undefined. This means, a result is returned
but it can have any value. The user is responsible to only specify valid cmdIDs
(this behavior results from the implementation which is selected to be high-
performance. The function is designed to also be executed in real-time-critical
ranges).

Data Layer:
Method: GET
URL:     https://<ip-addr>/automation/api/v2/nodes/motion/axs/<axs_name>/
state/cmd-state bzw. https://<ip-addr>/automation/api/v2/nodes/motion/kin/
<kin_name>/state/cmd-state
Payload: (blank)
The cmdID has to be attached to the URL as number and a GET is executed on
this URL. Successful reading returns the command state as string.
Example:
● CmdID of an executed axis command is 1234
● URL is a result of "URL: https://<ip-addr>/automation/api/v2/nodes/
  motion/axs/<axs_name>/state/cmd-state/1234"
● Reading on this URL returns the command state (for instance "ACTIVE")

PLC:

ML_GetCmdState
Name       Data type          Inherited      Address       Initial value   Comment
                              from
  Data       ML_GetCmd‐                                                    InOut: Command parame‐
             State                                                         ters
             BOOL                                                          Returns whether the com‐
ML_GetCmd‐                                                                 mand could be added.
State                                                                      ● TRUE: The ML_GetCmd‐
                                                                             State command could
                                                                             be added successfully
                                                                           ● FALSE: An error
                                                                             occurred. Details in

                                                         ML_oCmdResult
STRUCT ML_GetCmdStateData
Name         Data type   Inher‐           Addres Initial   Comment
                         ited             s      value
                         from
  In         ML_iGetCmd                                    Input: Command data of the command
             Statease
  Out        ML_oGet‐                                      Output: Command parameters
             State
STRUCT ML_iGetCmdState EXTENDS ML_iObjStateBase
Name        Data type   Inherited  Address      Initial value              Comment
                        from
  ObjName STRING(15) ML_iObjSta‐                                           Motion object name (axes
                        teBase                                             or kinematics) you want to
                                                                           request data from
  CmdID      ULINT                                                         Command ID (returned by
                                                                           ML_oCmdResult) if a new
                                                                           command is added
STRUCT ML_oGetState EXTENDS ML_oStateBase
Name       Data type    Inherited  Address                 Initial value   Comment
                        from
  Error    BOOL         ML_oState‐                                         Error ID, TRUE indicates
                        Base                                               that an error occurred (e.g.
                                                                           enter object name)
  ErrorID    ULINT            ML_oState‐                                   Specifies the type of the
                              Base                                         occurred error (above 4
                                                                           bytes: main diagnostics,
                                                                           below 4 bytes: detailed
                                                                           diagnostics); 0 means “no
                                                                           error”
  State      STRING(50)                                                    Requested state as string

Python:
motion.get_cmd_state(obj: str, id: int) -> str:
"""Read the state of a given command (command id has to be
given) as a string.
    You get the command id as a return value, when you create
a command.
    Note, that the result is undefined, when you call the
function with a invalid command id.

    Arguments:
     obj -- The name of the motion object (axis or kinematics).
     id -- The command id of the command, that state is
requested.

      Returns:
       str -- The state of the command as string
"""

BundleIF:
//! @brief Get the state the command with the given ID
//! @param[in] handle    Handle of the interface
//! @param[in] objName Name of the motion object
//! @param[in] cmdID     Command ID
//! @param[out] state    State of the command
//! @return              Was everything okay?
MotionResult getCmdState( void *handle, const char *objName,
uint64_t cmdID, motion::core::cmd::CmdState &state );

//! @brief State of a command
enum class CmdState
{
CMD_STATE_CREATED = 0, //!< command is created
CMD_STATE_IN_BUFFER,   //!< command is in the command-buffer
CMD_STATE_PREPARED,    //!< command is prepared
CMD_STATE_ACTIVE,      //!< command is currently active
CMD_STATE_DONE,        //!< command is done
CMD_STATE_ABORTED,     //!< command is aborted
CMD_STATE_OUTDATED,    //!< there is no information about this
command in the system anymore
};

States
If an invalid cmdID is specified (e.g. by another Motion object), the returned
state is undefined (can assume any value). The function cannot detect,
whether a valid cmdID has been specified (due to runtime restrictions). The
user of the function is responsible to verify whether or not the cmdID is valid.
Possible command states, refer to ⮫ Command state on page 328

Special features
● If BLENDING is enabled, sporadically more than one command is active in
  a Motion object. This command returns the state ACTIVE
● Unbuffered commands:
  – If an unbuffered command is executed before an active command, the
      active command reports state ABORTED.
  – If several unbuffered commands are issued in a cycle, only the last com‐
      mand is active (and reports state ACTIVE). All other executed commands
      report state ABORTED
  – If an unbuffered command is issued and if there are still commands in
      the command buffer, these commands are discarded and report state
      ABORTED

● Error reaction:
  – If a minor error occurs in a Motion object, a stop on the path is executed
      as error reaction with the currently commanded dynamics (behavior
      identical to override = 0). The active command remains active (in case
      of a kinematics, more commands can become active until a stop has
      been executed) and returns the state ACTIVE. If a reset is commanded
      to delete the error state, the state of the previously active command
      changes to ABORTED
  – If a severe error occurs in a Motion object, the kinematics is resolved
      and decelerated in an uncoordinated manner based on the axis limit
      values. The Motion command immediately changes to the ABORTING
      state and to ABORTED when standstill is reached
● If an abort command is executed, all previously active command change to

  state ABORTED
● As the system can only retain a limited amount of information (due to
  runtime requirements) about previous commands (already processed or
  canceled commands), the state OUTDATED is output in case of older com‐
  mands. In this case, no command data is available in the system as the
  relevant memory areas have already been released in order to avoid loading
  the runtime memory unnecessarily. It is guaranteed that for 10 already
  executed command (per Motion object), information is still provided in the
  system and are not returned as OUTDATED

Interrupt/Continue
The Interrupt and Continue commands are active together with the regular
command processing. Thus, there are the following command states:
Motion command            Axis/kinematics starts     Move: ACTIVE
becomes active            moving
Interrupt is commanded    Axis/kinematics deceler‐   Move: ACTIVE; Interrupt:
                          ates with the currently    ACTIVE
                          commanded dynamics
                          Axis/kinematics stopped
                                                Move: ACTIVE; Interrupt:
                                                DONE
Continue is commanded Axis/kinematics acceler‐ Move: ACTIVE; Interrupt:
                      ates again (continues the DONE; Continue: DONE
                      motion command)
                      Target position of motion Move: DONE; Interrupt:
                      command is reached,       DONE; Continue: DONE
                      motion is stopped
The Continue command can also be commanded before a complete axis/kine‐
matic stop. In this case, the third table line is not applicable.

Interrupt/abort
The Abort command also aborts an Interrupt command.
Thus, there are the following kinematic command states:
Commanding sequence       Axis behavior            Command state
Motion command            Kinematics starts moving Move: ACTIVE
becomes active
Interrupt is commanded    Kinematics decelerates     Move: ACTIVE; Interrupt:
                          with the currently com‐    ACTIVE
                          manded dynamics

Commanding sequence        Axis behavior              Command state
Abort is commanded         Kinematics continues to    Move: ACTIVE; Interrupt:
before it is stopped       decelerate with the        ABORTED; Abort: ACTIVE
                           currently commanded
                           dynamics
-                          Motion is stopped          Move: ABORTED; Inter‐
                                                      rupt: ABORTED; Abort:
                                                      DONE
In case of buffered commands that do not stop until the end of the motion
(as e.g. during blending with splines), it can sporadically happen that several
commands become active after an abort until the kinematics is stopped.
Therefore, the active command is not immediately set to ABORTED (as it
might not have been processed completely and thus reached state DONE).
Axis command states:
Motion command             Axis starts moving         Move: ACTIVE
becomes active
Interrupt is commanded     Axis decelerates with   Move: ACTIVE; Interrupt:
                           the currently commanded ACTIVE
                           dynamics
Abort is commanded         Axis decelerates with   Move: ABORTED; Inter‐
before it is stopped       the commanded abort     rupt: ABORTED; Abort:
                           dynamics                ACTIVE
-                          Motion is stopped       Move: ABORTED; Inter‐
                                                   rupt: ABORTED; Abort:
                                                   DONE

### 7.8.8 AxsSetRTStateEnabled - Enabling cyclic axis data

Basics
This command enables or disables cyclic axis data.
The cyclic axis data represent a series of status bits and axis values. The real-
time Data Layer interface provides easy real-time access. The real-time status
of each axis is represented in the motion/realtime/cyclicStatusData
node. The AxsSetRTStateEnabled command is used to enable or disable the
cyclic generation of real-time data. This is necessary for performance reasons,
since copying the data takes processing time. The change takes effect immedi‐
ately, regardless of the axis state.
The real-time data is updated only when the ctrlX MOTION is in the RUNNING
state. Generating the data places an additional load on the system. This can
lead to watchdog errors in heavily loaded systems.
Command interface: Data Layer, PLC

PLC:

ML_AxsSetExtrapolateExternalDynamic
Name         Data type           Inhe Address               Initial value   Comment
                                 rited
                                 from

ML_AxsSetExtrapolateExternalDynamic
  Data        ML_AxsSetRTStateE‐                                         Output: Command parame‐
nabledData                                                 ters
  ML_Axs‐     BOOL                                                       Returns information
SetRTStateEn‐                                                            whether the command can
abled                                                                    be added to the axis
                                                     object.
                                                     ● TRUE:
                                                       The ML_AxsSetExtra‐
                                                       polateExternalDynamic
                                                       command was success‐
                                                       fully executed

                                                     ● FALSE: An error
                                                       occurred. Details in
                                                       ML_oStateBase
STRUCT ML_AxsSetRTStateEnabledData
Name         Data type   Inher‐  Addres Initial           Comment
                         ited    s      value
                         from
  In         ML_iAxs‐                                     Input: Command data of the command
             SetRTSta‐
             teEnabled
  Out        ML_oState‐                                   Output: Command parameters
             Base
STRUCT ML_iAxsSetRTStateEnabled EXTENDS ML_iAxsStateBase
Name        Data type   Inherited   Address     Initial value            Comment
                        from
  AxisName STRING(63) ML_iAxsSta‐                                        Name of the axis used to
                        teBase                                           execute the command
  Enable    BOOL                                                         TRUE enables the genera‐
                                                                         tion of cyclic real-time data
                                                                         FALSE disables the genera‐
                                                                         tion of cyclic real-time data
STRUCT ML_oStateBase
Name         Data type          Inher‐   Addres Initial   Comment
                                ited     s      value
                                from
  Error         BOOL                                      Error ID TRUE indicates that an error
                                                          occurred
  ErrorID       ULINT                                     Specifies the type of occurred error: The
                                                          upper 4 bytes reflect the main diagnostics,
                                                          the lower 4 bytes reflect the detailed diag‐
                                                          nostics, 0 means no error

BundleIF:
//! @brief activates the logic to set the status data in
realtime datalayer for the axis in parameter
//! @param[in]    axsName        name of the axis
//! @param[in]    enable         true->enable, false->disable
//!
//! @return                      status of the function call:

STS_OK or an error code on failure
virtual MotionResult setAxsRTStateProviderEnabled(const char*
axsName, const bool enable) const = 0;

Further information
● ⮫ Chapter 6.2.7 Axis status information on page 168
