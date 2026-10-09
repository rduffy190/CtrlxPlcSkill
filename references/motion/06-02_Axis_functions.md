# 6.2 Axis functions

### 6.2.1 Synchronized Motion

Introduction
ctrlX MOTION supports the concept of the synchronized Motion. An axis can
be a slave axis of another axis, which is a master axis. The slave axis moves
synchronized using a function relative to the master axis. One example of such
a function is the toothing. A master axis can control several slave axes. A slave
axis can act as a master axis for another slave axis. The synchronized Motion
is based on commands. The commands of the synchronized Motion describe
the relationships between the axes.

ctrlX MOTION is used to define a calculation sequence for all synchronized
Motion axes. The positions of the master axes are calculated before the posi‐
tions of the slave axes. When creating a circular dependency of master and
slave axes, all axes (not just the commanded axes) are set to the error state
and stopped by their configured error reaction.
The difference between synchronized Motion commands and the synchroni‐
zation of Motion commands (SoMO) is that with synchronized Motion com‐
mands the axes move synchronously, whereas with the synchronization of
Motion commands a defined group of axes starts its motion at the same time.

Properties
Common features of synchronized Motion commands:
● Synchronized Motion commands are always commanded to the slave axis

● Synchronized Motion commands set the slave axis to the PLCopen state
  SYNCHRONIZED MOTION
● All synchronized Motion commands are endless and never reach the DONE
  state. This means that they can only be canceled with AxsAbort
● An error in the master axis has no effect on the slave axis. However, if the
  motion of the master axis stops due to an error, the slave axis also stops

Restrictions
The following restrictions apply to synchronized Motion commands:
● If a synchronized Motion command is active, the override has no influence
  on a slave axis that is involved in the synchronized Motion command. The
  override value is ignored
● All synchronized Motion commands are executed without dynamic limita‐
  tion
  – Functions based on dynamic limit values do not work. Examples
      of these functions are GetBrakingDistance and GetBrakingDistanceEx.
      These functions can only calculate an emergency braking distance
  – Setting the error level of a slave axis, part of a synchronized Motion
      command, set to LIGHT is automatically changed to SEVERE. As a result,
      the slave axis stops with the configured dynamic limits

Architecture
The entire functionality of the synchronized Motion is based on a flexible
mechanism/architecture of the calculation pipeline. Each Motion object of an
axis has a calculation pipeline manager. This manager contains calculation
pipelines. These calculation pipelines are specific to the respective axis. A
calculation pipeline is not shared by several axes. A calculation pipeline gener‐
ates command values for the slave axis based on the position, velocity, accel‐
eration and parameters of the master axis. A calculation pipeline contains
several calculation steps. See ⮫ Chapter Calculation pipeline on page 87 for
more information.

Available commands
The following commands are available for the synchronized Motion:
● ⮫ AxsGetSyncMotionState
● ⮫ AxsGearInPosCmd and AxsGearInPosCmdEx
● ⮫ AxsGearInVelCmd and AxsGearInVelCmdEx

Synchronized execution of Motion commands
All synchronized Motion commands execute the following basic command
sequence for each execution cycle of the Motion control.

                                      Start

                                  Determine
                               master axis values
                                                       master input

                                       Run
                               calculation pipeline   calculated slave
                                                          setpoint

                         No                           Yes
                                 Synchronized ?

                Dynamic                                    Monitor
             synchronization                            not exceeding
                                                          axis limits

                                           new slave setpoint

                               Write axis setpoint
                                 to slave axis

                                    Finished

Each synchronized Motion command consists of the following steps:
● Determine the reference values of the master axis, e.g. the interpolated
  position, etc.
● Execute the calculation pipeline to calculate the required command value
  for the slave axis (can be position, velocity, etc.). See ⮫ Chapter Calcula‐
  tion pipeline on page 87 for detailed information

 ● If the state of the slave axis is SYNCHRONIZED after the previous execu‐
   tion cycle of the Motion control with the master axis, the system checks
   whether the axis limits have been violated for the slave axis. If the axis
   limits of the slave axis are violated, there is an error reaction for the
   synchronized Motion, see ⮫ Chapter Error reaction on page 126.
   – If the slave axis state is SYNCHRONIZED with the master axis after the
       last update, the command value is written to the slave axis unless the
       axis limits are violated and the error reaction is not set to "ignore"
   – If the state of the slave axis is DYN_SYNCHRONIZING, dynamic syn‐
       chronization is executed. See ⮫ Chapter Dynamic synchronization
       on page 115 for more information. If dynamic synchronization results in
       the slave axis being synchronized with the master axis, the dynamic syn‐
       chronization functionality switches the state of the axis to SYNCHRON‐

       IZED
   – If the axis is in the SYNCHRONIZED state, the dynamic synchronization
       functionality copies the required command value of the slave axis to
       the slave axis, checks the dynamic limits of the slave axis and executes
       a configurable error reaction if the limits are exceeded. See ⮫ Chapter
       Error reaction on page 126 for more information

    Calculation pipeline
A so-called calculation pipeline is used to generate slave axis target values
based on the position or velocity of the master axis. All specific synchronized
Motion commands provide their own calculation pipeline and register the cal‐
culation pipeline in the calculation pipeline manager.
An application can use the calculation pipelines of certain synchronized
Motion commands as a template for application-defined calculation pipelines
(planned for a future version). From an application point-of-view, there is no
difference between integrated and application-defined calculation pipelines,
except that integrated calculation pipelines cannot be changed. Application-
defined calculation pipelines are part of the axis configuration, including
loading/saving.
The calculation pipeline contains the entire calculation of the new target com‐
mand value for the slave axis. The calculation pipeline consists of one or more
calculation steps, see ⮫ Chapter Calculation steps on page 91. The most
important features of a calculation pipeline are as follows:
 ● The order of the calculation steps can be configured
 ● Each calculation step can be configured, each step can have parameters
 The following image shows a simple calculation pipeline. The blue field is the
 input of the calculation step, the orange field is the type of the calculation
 step and the step ID, the white fields are the parameters of the calculation
 step and the green field is the output of the calculation step.

                                    Master 1
                                  (REF_POS)

                                        REF_POS = 12

                                   REF_POS
                        motion::sync::GearInPos (ID=17)
                              ratioNumerator = 4
                             ratioDenominator = 3
                                   REF_POS

                                        16

                                      16

Interface
The calculation pipeline has an abstract interface. This interface contains
methods for the following actions:
● Retrieving a list of all calculation steps (identifiers) that are part of the
    calculation pipeline
● Adding, inserting and removing calculation steps
● Setting and changing the parameters of an individual calculation step
● Read parameters of a single calculation step
● Validate the entire calculation pipeline
Adding or deleting calculation steps from the calculation pipeline and
updating internal structures are major changes to the calculation pipeline. A
calculation pipeline cannot be executed while such a change is implemented.
If the Motion object does not execute the calculation pipeline, the calculation
pipeline can be edited and changed. Only one instance can process the calcu‐
lation pipeline at a time.
Changing the parameters of a calculation step is a minor modification of
the calculation pipeline. It is therefore permissible to change the parameters
while the calculation pipeline is running.
You can only change user-defined calculation pipelines. The "built-in" calcula‐
tion pipelines cannot be changed.

Data Layer representation
"Variant" means that the data type can be a character string, an integer, a
float, an array or a complex structure, for example.

Table 4: Information on supported calculation steps (read-only)
URI                             Type                              Description
/motion/state/calculation-steps vector<struct>                    Provides information on all sup‐
                                                                  ported calculation steps
/motion/state/calculation-steps/ struct                           Provides information on a single
<calc-step-name>                                                  supported calculation step,
                                                                  specified by its type ID
/motion/state/calculation-steps/ string                           A line describing what the cal‐
<calc-step-name>/description                                      culation step does (could be a
                                                                  tooltip in an HMI)
/motion/state/calculation-steps/ string                           Reference to the documentation
<calc-step-name>/docu-ref                                         (page is displayed when F1 is

  pressed)
/motion/state/calculation-steps/ vector<enum>                     Vector of required input types
<calc-step-name>/inputs
/motion/state/calculation-steps/ vector<vector<vector<string>>> Contains groups of parameters
<calc-step-name>/mutex-param‐                                   (identified by their names) that
eter                                                            are optional and mutually exclu‐
sive
Example: GearIn stage with
fixed ratio or Data Layer path
® {{{"RatioNumerator", "Ratio‐
Denominator"}, {"DataLayer"}}}
/motion/state/calculation-steps/ vector<enum>                   Vector of required output types
<calc-step-name>/outputs
/motion/state/calculation-steps/ map<string,struct>             Provides information on the
<calc-step-name>/parameter                                      required parameters of the cal‐
culation step
/motion/state/calculation-steps/ struct                         Provides information about a
<calc-step-name>/parameter/                                     single required parameter of the
<par-name>                                                      calculation step
/motion/state/calculation-       string                         A line that describes what the
steps/<calc-step-name>/param‐                                   parameter of the calculation
eter/<par-name>/description                                     step does (could be a tooltip in
an HMI)
/motion/state/calculation-       bool                           Indicates whether the param‐
steps/<calc-step-name>/param‐                                   eter is mandatory or not
eter/<par-name>/mandatory
/motion/state/calculation-steps/ string                         Reference to the documentation
<calc-step-name>/parameter/                                     (page is displayed when F1 is
<par-name>/docu-ref                                             pressed)
/motion/state/calculation-steps/ enum                           Parameter type
<calc-step-name>/parameter/
<par-name>/type
/motion/state/calculation-steps/ enum                           Value of the unit type of the
<calc-step-name>/parameter/                                     parameter
<par-name>/unit

Table 5: Configuration of specific calculation pipelines (read and write, axis-specific)
URI                               Type                              Description
/motion/axs/<axsName>/cfg/        struct                            Configuration interface for a
functions/coupling/sync-                                            single calculation pipeline
motion/calculation-pipeline/
<calc-pipeline-name>
/motion/axs/<axsName>/cfg/        map<stepID, struct>               Configuration interface for all
functions/coupling/sync-                                            calculation steps of a single cal‐
motion/calculation-pipeline/                                        culation pipeline; is addressed
<calc-pipeline-name>/steps                                          by stepID. Name cannot be
                                                                    used because calcSteps can
                                                                    occur more than once
<calc-pipeline-name> e.g.
gear_in_pos                                                         The number is the step ID (is
                                                                    permanently assigned to the
                                                                    calculation step when it is cre‐
                                                                    ated; new steps are always at
                                                                    the end)
                                                                    CREATE, READ, WRITE and
                                                                    DELETE are supported
                                                                    To create or delete calculation
                                                                    steps, switch internally to the
                                                                    "Edit" function and release it
                                                                    again after the action
/motion/axs/<axsName>/cfg/        struct                            Configuration interface for a
functions/coupling/sync-                                            single calculation step of a
motion/calculation-pipeline/                                        pipeline; number is the number
<calc-pipeline-name>/steps/                                         of the stepID
<stepID>
/motion/axs/<axsName>/cfg/        string (read only)                Type ID of the calculation step
functions/coupling/sync-                                            (refers to "/motion/state/calcu‐
motion/calculation-pipeline/                                        lation-steps/<name>")
<calc-pipeline-name>/steps/                                         The type cannot be changed.
<stepID>/type                                                       Delete the step and create a
                                                                    new step with the new type;
                                                                    the type is required here for
                                                                    loading/saving
/motion/axs/<axsName>/cfg/        vector<string>                    Specifies the source for the
functions/coupling/sync-                                            inputs.
motion/calculation-pipeline/                                        Writing the inputs internally
<calc-pipeline-name>/steps/                                         switches to the function and
<stepID>/inputs                                                     releases it again after the action
/motion/axs/<axsName>/cfg/    map<string, variant>                  All parameter values of the calc‐
functions/coupling/sync-                                            Step
motion/calculation-pipeline/
<calc-pipeline-name>/steps/
<stepID>/parameter
/motion/axs/<axsName>/cfg/    variant                               Value of a
functions/coupling/sync-                                            single parameter (type
motion/calculation-pipeline/                                        refers to "/motion/state/calcu‐
<calc-pipeline-name>/steps/                                         lation-steps/<name>/parameter/
<stepID>/parameter/<par-name>                                       <name>/type")

URI                                 Type                           Description
/motion/axs/<axsName>/state/        double                         Current offset in the configured
functions/coupling/sync-                                           axis unit
motion/calculation-pipeline/
<calc-pipeline-name>/steps/
<stepID>/offset
/motion/axs/<axsName>/state/        double                         Remaining time in seconds until
functions/coupling/sync-                                           the interpolation for the target
motion/calculation-pipeline/                                       offset is completed
<calc-pipeline-name>/steps/
<stepID>/remain-ipo-time
/motion/axs/<axsName>/state/        uint64                         Information on whether the
functions/coupling/sync-                                           interpolation for the target

motion/calculation-pipeline/                                       offset has been completed (0
<calc-pipeline-name>/steps/                                        -> not completed OR 1 -> com‐
<stepID>/ipo-done                                                  pleted)

Table 6: Status of the configured pipelines (read-only)
URI                          Type                                  Description
/motion/axs/<axsName>/state/ struct                                State interface for a single cal‐
functions/coupling/sync-                                           culation pipeline
motion/calculation-pipeline/                                       Also supports a READ with
<calc-pipeline-name>                                               parameters (definition of all
                                                                   input values)
/motion/axs/<axsName>/state/ enum                                  EDIT, INVALID, VALID, RUN
functions/coupling/sync-
motion/calculation-pipeline/
<calc-pipeline-name>/state
/motion/axs/<axsName>/state/ vector<struct>                        During reading, a validation of
functions/coupling/sync-                                           the calculation pipeline is per‐
motion/calculation-pipeline/                                       formed and a vector of struc‐
<calc-pipeline-name>/validation                                    tures with { main diag code,
                                                                   detail diag code, uri, addInfo }
                                                                   is returned
/motion/axs/<axsName>/state/ bool                                  Returns TRUE if the calculation
functions/coupling/sync-                                           pipeline is an integrated calcu‐
motion/calculation-pipeline/                                       lation pipeline. An integrated
<calc-pipeline-name>/is-built-in                                   calculation pipeline cannot be
                                                                   changed
/motion/axs/<axsName>/state/ Input type: struct                    Input parameters for the run
functions/coupling/sync-                                           calculation pipeline (name of
motion/calculation-pipeline/                                       the master axis, syncMode and
<calc-pipeline-name>/runCalcu‐                                     inputs)
lationPipeline                 Output type: float                  Result of the calculation pipe‐
                                                                   line

Calculation steps
Introduction
A calculation pipeline for synchronized Motion contains a series of calculation
steps. Each calculation step receives its input parameters from the inputs of
the calculation pipeline or the outputs of other calculation steps and provides
an output for another calculation step or the output of the calculation pipe‐
line.

Each calculation step can have parameters for flexible use. Typical parame‐
ters:
● A value
● A reference to a Data Layer RT variable
● Switches (Boolean or enumeration value) which change the behavior of the
    calculation step
A Data Layer RT variable is referenced via an index. The index value starts at
0. The first 20 elements in the Data Layer RT are reserved for Motion.sync
commands, i.e. the indices 0 to 14. If an index of 1000 or higher is specified,
the global Motion real-time input is used. With an index value of 1000, this
means that index 0 of the global motion Data Layer RT is used. With an index
value of 1001, index 1 of the Global Motion Data Layer RT is used, etc. See
⮫ Chapter Change parameters in real time on page 103 for more information.
If varying values are used via Data Layer RT inputs, the calculation time for
a calculation step increases considerably. It is recommended to use constant
values if possible.
The following calculation steps are available and are listed in alphabetical
order:
●     Const
●     Derivative
●     Factor
●     FineAdjust
●     FirstOrderFilteredOffset
●     FirstOrderIpoOffset
●     GearIn
●     Offset
●     SecondOrderIpoOffset
●     Sum
●     TypeChange

Calculation step Const
The Const calculation step copies a constant input value to the output value.
The constant can either be specified by a constant value or determined by
reading the value from the Data Layer RT each time the calculation step is
evaluated.

                        y = Const

"y" is the output value of the calculation step, "Const" is the input value of the
calculation step.
Parameters:
The Const parameter can be defined as a constant value or as a Data Layer RT
input value.

● Const - The constant value of type double. This is used in the calculation
  step if the ConstDLIdx parameter is set to -1.
● ConstDLIdx - Determines the index of the real-time input if it is not nega‐
  tive. The type is Integer. The value of the constant is read in each execu‐
  tion cycle of the Motion control system using the index. See ⮫ Chapter
  Change parameters in real time on page 103 for more information.
To use the Const parameter as a constant value, set the ConstDLIdx param‐
eter to -1. To use the constant parameter as a variable during the execution
of a synchronized Motion command, assign a suitable index value in the Data
Layer RT to the ConstDLIdx parameter. Use the specified Data Layer RT index
to provide a variable value for the constant.
Select the correct input type for the calculation step. The output type is the
same as the input type. The following subtypes are defined for different input

types:
● Const_REF_POS - Constant step for position reference values
● Const_REF_VEL - Constant step for velocity reference values
● Const_REF_ACC - Constant step for acceleration reference values
Example
Task                     Constant                     Calculation result
Set constant parameter 0.0                            0.0
to 0.0
Read Data Layer RT input 1.0                          1.0
If the constant value is specified by a Data Layer RT index, the constant is
used as the position value.

Calculation step Derivation
The step for calculating the derivative calculates an approximation to the
derivative of the input. The approximation is realized using "Backward Euler",
whereby the difference of the input is taken over a time interval and this
value is divided by the size of the time interval. As a rule, the time interval
corresponds to two consecutive execution cycles of the Motion control so that
the size of the time interval is equal to cycleTime:

                                      x _ xprevious
                              y =
                                      cycleTime
                              xprevious = x

"y" is the output value of the calculation step, "x" is the input value of the
calculation step.
Select the correct input type for the calculation step. The output type is the
same as the input type. The following subtype is defined for the input type.
● Derivative_REF_POS_REF_VEL

Calculation step Factor
The factor calculation step multiplies a step input value by a factor. The factor
value can either be specified by a constant value or by reading the value from
the Data Layer RT each time the step is evaluated.

                         y =    x *     factor

"y" is the output value of the calculation step, "x" is the input value of the
calculation step.
Parameters:
The factor parameter can be defined as a constant value or as a Data Layer RT
input value.
● Factor - The constant value of the factor. Type is double. It is used in the
   calculation step if the FactorDLIdx parameter is set to -1
● FactorDLIdx - If not negative, the index of the real-time input. Type is
   integer. The value of the factor is read at each execution cycle of the
   Motion control using the index
To use the factor parameter as a constant value, set the FactorDLIdx param‐
eter to -1. To use the factor parameter as a variable when executing a
synchronized Motion command, assign a corresponding Data Layer RT index
value to FactorDLIdx. Subsequently, use the specified Data Layer RT index
to provide a variable value for the factor parameter. See ⮫ Chapter Change
parameters in real time on page 103 for more information.
Select the correct input type for the calculation step. The output type is the
same as the input type. The following subtypes are defined for different input
types.
● Factor_REF_POS - Factor step for position command values
● Factor_REF_VEL - Factor step for velocity command values
● Factor_REF_ACC - Factor step for acceleration command values
If the factor value is specified as a value via the real-time input and the factor
is applied to a position, the following special behavior occurs when the value
is changed.
● The specified factor is initially used directly as specified in the formula
   (SyncMode is set to SYNC_RELATIVE or SYNC_ABSOLUTE)
● If the factor changes, these changes only apply if the step input value
   changes. The result of the calculation step therefore does not change if the
   step input value does not change, even if the factor value is changed
Example
Assuming that the master axis is at position 100. The following table shows
the calculation result of the factor calculation step using the position of the
master axis as the step input value:
Task                        Input value step         Factor                   Calculation result
SyncMotion command          100                      0.5                      50
(originally)
Move master to 200          200                      0.5                      100
Change factor to 1.0        200                      1.0                      100
Move master to 100          100                      1.0                      100
Change factor to 1.5        100                      1.5                      100
Move master to 0            0                        1.5                      0

Calculation step FineAdjust
The fine adjustment step adjusts the input by a certain percentage in relation
to 100 %. The equation of the step can be written as follows:

                                            fineAdjust
             y =      x *       (1 +           100
                                                         )
"y" is the output value of the calculation step, "x" is the input value of the
calculation step, "fineAdjust" is the adjustment value in percent.

Parameters:
The FineAdjust parameter can be defined as a constant value or as a Data
Layer RT input value.
● FineAdjust - The constant value of the fine adjustment in percent, relative
   to 100 %. The type is double. It is used in the calculation step if the
   FineAdjustDLIdx parameter is set to -1
● FineAdjustDLIdx - If not negative, the index of the real-time input. Type is
   integer. The fine adjustment value is read at each execution cycle of the
   Motion control using the index
To use the FineAdjust parameter as a constant value, set the FineAdjustDLIdx
parameter to -1. To use the FineAdjust parameter as a variable during the
execution of a synchronized Motion command, assign a corresponding Data
Layer RT index value to FineAdjustDLIdx. See ⮫ Chapter Change parameters in
real time on page 103 for more information. Use the specified Data Layer RT
index to provide a variable value for the fine-tuning parameter.
Select the correct input type for the calculation step. The output type is the
same as the input type. The following subtypes are defined for different input
types.
● FineAdjust_REF_POS - Fine adjustment step for position command values
● FineAdjust_REF_VEL - Fine adjustment step for velocity command values
● FineAdjust_REF_ACC - Fine adjustment step for acceleration command
  values

Calculation step FirstOrderFilteredOffset
The step for calculating the first-order filtered offset adds or subtracts a low-
pass filtered offset value to or from the output of the calculation step. The
calculated offset value is the result of a low-pass filtered first-order offset
parameter with a time constant. The time constant is also specified as a
parameter. When the calculation step is executed for the first time, the offset
parameter is immediately applied to the output of the step. If this calculation
step is repeated later, any change to the offset parameter is applied after the
value has been filtered through the low-pass filter. The equation of the step
can be written as follows:

                                                                    _ cycleTime / timeConstant
        offs = offset(init) + ( offset _ offset(init) ) * ( 1 _ e                                )
              _ offs
        y = x +

"y" is the output value of the calculation step, "x" is the input value of the
calculation step, "offsetinit" is the offset value at the time at which the offset
parameter or the time constant is changed, "offset" is the current value of the
offset parameter, "cycleTime" is the time since the last change to the offset
parameter or the time constant.
Parameters:
The offset and timeConstant parameters can be defined as constant values or
as Data Layer RT input values:
● ArithmeticOperator - defines how the filtered first-order offset is applied to
   the step output. The offset can be added to or subtracted from the step
   input. Type is integer, value 0 means ADD, value 1 means SUBTRACT
● Offset - the constant value of the offset that is filtered. The type is double.
   It is used in the calculation step if the OffsetDLIdx parameter is set to -1.
   The unit is the configured unit for position, velocity, acceleration or jerk of
   the slave axis
● OffsetDLIdx - if not negative, the index of the Data Layer RT input. Type
   is integer. The offset value is read with each execution cycle of the Motion
   control using the index. See ⮫ Chapter Change parameters in real time
   on page 103 for more information. The offset value has to be specified in
   the configured unit for position, velocity, acceleration or jerk of the slave
   axis
● TimeConstant - the filter time constant. The unit is the configured unit for
   TIME of the axis. After this time, the change in offset has reached approxi‐
   mately 63.2% (1-e-1 ≈ 0.632). Type is double
● TimeConstantDlIdx - if not negative, the index of the Data Layer RT input.
   The type is an integer. The value of the time constant is read in each exe‐
   cution cycle of the Motion control using the index. See ⮫ Chapter Change
   parameters in real time on page 103 for more information
Select the correct input type for the calculation step. The output type is the
same as the input type. The following subtypes are defined for different input
types:
●  FirstOrderFiltered_REF_POS - Offset step for position command values
●  FirstOrderFiltered_REF_VEL - Offset step for velocity command values
●  FirstOrderFiltered_REF_ACC - Offset step for acceleration command values
●  FirstOrderFiltered_REF_JRK - Offset step for jerk reference values
Example
While this calculation step is active, the offset parameter is changed from 1 to
2 at time t=0.
This is shown in the green curve with a time constant of 1.0. The red curve
shows the currently used offset, which is the low-pass filtered value of the
command values change.

Calculation step FirstOrderIpoOffset
The first calculation step of the first-order interpolated offset calculation adds
or subtracts a velocity offset value to or from its input. This calculation step
only applies to one velocity value. The input of the calculation step has
to be a velocity value, and the output of the calculation step is a velocity
value. Changes in the target offset are linearly interpolated by a first-order
time-optimal velocity profile using maximum acceleration. This means that the
offset is limited to the restrictions of the specified maximum acceleration. The
maximum acceleration for the interpolation is specified by a parameter. When
the calculation step is executed for the first time by the synchronized Motion
command, the offset parameter is immediately applied to the input of the step
without any interpolation. The parameters for the offset and the maximum
acceleration can be specified as constant values that can be changed during
the execution of the synchronized or by Data Layer RT inputs. When using the
Data Layer, the parameter values are read during each execution cycle of the
motion controller, allowing the parameters to be updated while the synchron‐
ized Motion command is active. Any change to the target offset during the
execution of the synchronized Motion command is interpolated linearly from
the currently applied offset to the target offset. The equation of the step can
be written as follows.

               _
         y = x +   ( offset   (previous)   + interpolate ( offset(delta) , maxAcc )   )

"y" is the output value of the calculation step, "x" is the input value of the
calculation step, "offsetprevious" is the initial value of the target offset param‐
eter or the value before the parameter is changed, "offsetdelta" is the differ‐
ence between the new and the previous value of the target offset when it
is changed, "maxAcc" is the maximum acceleration when interpolating the
change in the target offset.
Parameters
The "Offset" and "maxAcc" parameters can be defined as a constant value or
as a Data Layer RT input value:
● ArithmeticOperator - defines how the interpolated second-order velocity
   offset is applied to the output of the calculation step. The offset can be
   added to or subtracted from the input of the calculation step. The type is
   an integer, the value 0 means ADD, the value 1 means SUBTRACT
● Offset - the constant offset value, which is the second order interpolated
   target velocity offset to be reached. This is linear (first order interpolation)
   from the currently applied offset value to this specific target offset. The
   type is “double”. It is used in the calculation step if the “OffsetDLIdx”
   parameter is set to -1. The unit is the configured unit for the position of the
   slave axis
● OffsetDLIdx - if not negative, the index of the Data Layer RT input. Type
   is integer. The offset value for the target velocity is read during each execu‐
   tion cycle of the Motion controller using the index. See ⮫ Chapter Change
   parameters in real time on page 103 for more information. The offset value
   has to be specified in the configured unit for the position of the slave axis
● OffsetAcc - maximum acceleration during the interpolation of the velocity
   offset. Type is double. It is used in the calculation step if the OffsetAcc‐
   DLIdx parameter is set to -1. The unit is the configured unit for the acceler‐
   ation of the slave axis
● OffsetAccDLIdx - if not negative, the index of the Data Layer RT input. Type
   is integer. The OffsetAcc value is read in each execution cycle of the Motion
   control using the index. See ⮫ Chapter Change parameters in real time
   on page 103 for more information. The offset value has to be specified in
   the configured unit for the acceleration of the slave axis
Select the correct input value for the calculation step. The input type is the
same as the output type. The following subordinate type is defined for the
input type:
● FirstOrderIpoOffset_REF_VEL - Offset step for velocity command values

−     Offset interpolation is only carried out if the maximum acceleration value
      is greater than zero. If the maximum acceleration is set to zero or negative,
      the interpolation is stopped immediately and the applied offset value no
      longer changes. As this behavior only applies when interpolation is active,
      this is only relevant if the maximum acceleration value is retrieved from
      the Data Layer RT
−     When this calculation step becomes active, i.e. when the synchronized
      Motion command starts, the offset value of the target is immediately
      applied as a step, even if the maximum acceleration is zero or negative

GearIn calculation step
The gear in the calculation step implements an electronic gear specified by a
constant ratio and a fine adjustment. The equation of the step can be written
as follows:

                       ratioNumerator                  fineAdjust
        y =   x *
                      ratioDenominator     *   (1 +       100
                                                                    )

"y" is the output value of the calculation step, "x" is the input value of the
calculation step, "ratioNumerator" is the numerator of the transmission ratio,
"ratioDenominator" is the denominator of the transmission ratio, "fineAdjust"
is the adjustment value in percent.

Parameters
● ratioNumerator - the numerator of the transmission ratio. The type is an
    integer
● ratioDenominator - the denominator of the transmission ratio. The type is
    an integer
● fineAdjust - The additional value of the fine adjustment in percent, related
    to 100 %. Type is double
If the master axis ratioDenominator completes full revolutions, the slave axis
ratioNumerator completes full revolutions (if the fine adjustment is 0). If one
of the ratio parameters is negative, the direction of motion of the slave axis is
opposite to the direction of motion of the master axis.
Very high values of relative accuracy can lead to a loss of accuracy.

Select the correct input type for the calculation step. The output type is the
same as the input type. The following subtypes are defined for different input
types.
● GearIn_REF_POS - GearIn step for position command values
● GearIn_REF_VEL - GearIn step for velocity command values

Offset calculation step
The offset calculation step applies an offset (term) to the step input value of
the calculation pipeline, whereby no filtering or interpolation takes place. The
offset can either be a step parameter that remains constant during execution,
or it can be read from the Data Layer RT each time the calculation step is
evaluated during execution.

                                   _ offset
                             y = x +

"y" is the output value of the calculation step, "x" is the input value of the
calculation step.
Parameters
The parameter offset can be defined as a constant value or as a Data Layer RT
input value:

● ArithmeticOperator - defines how the offset is applied to the step input.
   The offset can be added to or subtracted from the step input. The type is
   an integer, value 0 means ADD, value 1 means SUBTRACT.
● Offset - the constant offset value. Type is double. It is used in the calcula‐
   tion step if the OffsetDLIdx parameter is set to -1
● OffsetDLIdx - if not negative, the index of the Data Layer RT input. Type
   is integer. The offset value is read with each execution cycle of the Motion
   control using the index. See ⮫ Chapter Change parameters in real time
   on page 103 for more information. The offset value has to be specified in
   the configured unit for position, velocity, acceleration or jerk of the slave
   axis
To use the oOffset parameter as a constant value, set the OffsetDLIdx param‐
eter to -1. To use the offset parameter as a variable during the execution of
a synchronized Motion command, assign a corresponding Data Layer RT index
value to OffsetDLIdx. Then use the specified Data Layer RT index to provide a
variable value for the offset parameter.
Select the correct input type for the calculation step. The output type is the
same as the input type. The following subtypes are defined for different input
types:
●  Offset_REF_POS - Offset step for position command values
●  Offset_REF_VEL - Offset step for velocity command values
●  Offset_REF_ACC - Offset step for acceleration command values
●  Offset_REF_JRK - Offset step for jerk command values
How the offset (constant or real-time input) is applied depends on the value
of SyncMode:
● SYNC_ABSOLUTE
   The offset value is always added
● SYNC_RELATIVE
   If a synchronized Motion command is executed for the first time in the
   Motion control's execution cycle, the offset is not used. The offset is used
   in subsequent execution cycles of the Motion control, but only if the offset
   value has changed.
   Explanation:
   During the first execution cycle of the Motion control, the slave axis is
   synchronized to the master axis using the SYNC_RELATIVE SyncMode. The
   calculation pipeline determines an "internal offset" that causes the slave
   axis to follow the master axis without initial motion. This "internal offset"
   is retained, and when the master axis moves, the slave axis follows the
   master axis as defined by the calculation pipeline. However, if a different
   offset is specified after the first execution cycle of the Motion control, the
   difference between the previous offset and the new offset is applied.
Example:
Assuming that the position of the master axis is 10 and the position of the
slave axis is 4. A synchronized gearInPos command is issued with a transmis‐
sion ratio of 1:2 (the slave axis moves by a distance of 1 when the master axis
moves a by distance of 2) and by an offset of 3:

● If ABSOLUTE is specified in SyncMode, the slave axis executes a motion to
  position 8 ((10 * 1/2) + 3)
● If RELATIVE is specified in SyncMode, the slave axis does not move during
  the first execution cycle of the Motion control. An internal offset is calcu‐
  lated in the calculation pipeline, which means that the slave axis does not
  move. This internal offset is -4, the difference between the current position
  of the slave axis (4) and the position that corresponds to the result of the
  calculation pipeline if no internal offset is applied (8). So if the master axis
  moves to position 20 and the specified offset is 3 (no change), the slave
  axis moves to position 9 ((20 * 1/2) + 3 - 4). If the offset value is then
  changed to 8, the difference to the previous offset (8 - 3 = 5) is applied to
  the slave axis in the next execution cycle of the Motion control. So if the
  master axis moves to position 22, the slave axis moves to position 15 ((22

  * 1/2) + 3 - 4 + 5)

Calculation step SecondOrderIpoOffset
The second-order interpolated offset calculation step adds or subtracts a posi‐
tion offset to or from the output of the calculation step. Offset changes are
interpolated by a second-order time-optimal profile, "ramped offset", using a
maximum velocity and a maximum acceleration. This means that the offset is
limited to the restrictions of the maxVel and maxAcc parameters. When the
calculation step is executed for the first time, the offset parameter is applied
to the output of the step immediately and without interpolation. If this calcu‐
lation step is repeated later, each change to the offset parameter is applied as
a second-order interpolated offset. The equation of the step can be written as
follows:

              _
        y = x +   ( offset   (previous)   + interpolate ( offset(delta) , offsetVel , offsetAcc )   )

"y" is the output value of the calculation step, "x" is the input value of the
calculation step, "offsetprevious" is the initial value of the offset parameter or
the value before it was changed, and "offsetdelta" is the difference between the
new and the previous value of the offset when it is changed, "offsetVel" and
"offsetAcc" are the boundary conditions for the interpolation of the change in
the offset value.
Parameters
The parameters Offset, OffsetVel and OffsetAcc can be defined as constant
values or as Data Layer RT input values:
● ArithmeticOperator - defines how the interpolated second-order offset is
  applied to the step output. The offset can be added to or subtracted
  from the step input. Type is integer, value 0 means ADD, value 1 means
  SUBTRACT
● Offset - the constant offset value that is interpolated. Type is double. It is
  used in the calculation step if the OffsetDLIdx parameter is set to -1. The
  unit is the configured unit for the position of the slave axis
● OffsetDLIdx - if not negative, the index of the Data Layer RT input. Type is
  integer. The offset value is read during each execution cycle of the Motion
  control using the index. See ⮫ Chapter Change parameters in real time
  on page 103 for more information. The offset value has to be specified in
  the configured unit for the position of the slave axis

● OffsetVel - maximum velocity during the offset. Type is double. It is used in
   the calculation step if the OffsetVelDLIdx parameter is set to -1. The unit is
   the configured unit for the velocity of the slave axis
● OffsetVelDLIdx - if not negative, the index of the Data Layer RT input. Type
   is integer. The maximum velocity limit for second-order interpolation is
   read in each execution cycle of the Motion control using the index. See
   ⮫ Chapter Change parameters in real time on page 103 for more informa‐
   tion. The velocity value has to be specified in the configured unit for the
   velocity of the slave axis
● OffsetAcc - maximum acceleration during the interpolation of the second
   order offset. Type is double. It is used in the calculation step if the Offse‐
   tAccDLIdx parameter is set to -1. The unit is the configured unit for the
   acceleration of the slave axis
● OffsetAccDLIdx - if not negative, the index of the Data Layer RT input.
   The type is an integer. The maximum acceleration specification for the
   second-order interpolation is read in each execution cycle of the Motion
   control using the index. See ⮫ Chapter Change parameters in real time
   on page 103 for more information. The acceleration value has to be speci‐
   fied in the configured unit for the acceleration of the slave axis
Select the correct input type for the calculation step. The output type is the
same as the input type. The following subtype is defined for the input type:
● Offset_REF_POS - Offset step for position command values

Calculation step Sum
The sum calculation step adds up several input values. All input values have to
be of the same type.

                y =      x(1) +      x(2)    + ...

"y" is the output value of the calculation step, "x(n)" are the input values of the
calculation step.
You have to select the correct calculation step for the desired number of input
values and the desired input type. The output type is the same as the input
type. The following subtypes are defined for different input types and number
of inputs:
●   SUM2_REF_POS - Summation step for 2 position command values
●   SUM3_REF_POS - Summation step for 3 position command values
●   SUM4_REF_POS - Summation step for 4 position command values
●   SUM2_REF_VEL - Summation step for 2 velocity command values
●   SUM3_REF_VEL - Summation step for 3 velocity command values
●   SUM4_REF_VEL - Summation step for 4 velocity command values

TypeChange calculation step
The TypeChange calculation step changes the data type of its input without
changing the numerical value. In this way, calculation steps with non-matching
data types can be linked by an intermediate TypeChange calculation step.

                y =     x

"y" is the output data type of the calculation step, "x" is the input data type of
the calculation step.
Select the correct calculation step for the input data type and the desired
output data type. The following data type modifications are defined for var‐
ious input data types and output data types.
Table 7: Available data type modifications

Name                  Input data type                 Output data type
Type‐                 REF_POS                         REF_VEL
Change_REF_POS_REF_V
EL
Type‐                 REF_POS                         REF_ACC
Change_REF_POS_REF_A
CC
Type‐                 REF_VEL                         REF_POS
Change_REF_VEL_REF_P
OS
Type‐                 REF_VEL                         REF_ACC
Change_REF_VEL_REF_AC
C
Type‐                 REF_ACC                         REF_POS
Change_REF_ACC_REF_P
OS
Type‐                 REF_ACC                         REF_VEL
Change_REF_ACC_REF_V
EL

    Change parameters in real time
Many of the calculation steps can have dynamic parameters that can be
changed in a real-time context while the synchronous Motion command is
active. For example, a motion-synchronized PLC task or a real-time bundle.
Dynamic input is only possible with values that do not require validation.
Note that a calculation step can check the dynamic inputs, but this check is
performed in every execution cycle of the Motion control. Dynamic inputs can
be obtained via the Data Layer RT.
The input variables in the Data Layer RT are of type ARRAY_OF_DOUBLE, and
these variables are local for each individual axis Motion object.
In the calculation steps, you define the index in a Data Layer RT array to tell
the calculation step where the current value can be read. When the step is cal‐
culated, the value is read from the Data Layer RT and used in the calculation.
A single variable can be used in several calculation steps.
The number of dynamic input variables can be configured in setup mode in
the following Data Layer RT nodes:

● System-wide definition
   motion/cfg/realtime-inputs/double-array-size
   Standard size is 10 elements
● Per axis definition
   motion/axs/<axis-name>cfg/realtime-inputs/double-array-size
   Standard size is 20 elements
The array size of the Data Layer RT is limited to a minimum value of 20, which
guarantees the functionality of the motion.sync commands.
The values written by a real-time application can be read from the Data Layer
RT via the following paths:
● motion/cmd-input/double/data/in
● motion/axs/axis-name/cmd-input/double/data/in

                         Motion kernel
                                                          PLC application
             Axis X    Axis A3     Axis A6     Axis ...

         1                           3
                                                                   4
         double[20]   double[20]             double[10]

                  2      Data Layer RT

1 Data Layer RT elements are write-protected for one axis
2 The size of the array can be configured
3 An axis does not require dynamic parameters
4 A (real-time) PLC application can write values

Write synchronization
An application that writes data is responsible for synchronization with the
Motion kernel. Writing a single value is atomic, but if the application changes
multiple values as a group, the application has to ensure synchronization to
avoid a possible race condition in the calculation step.
Use in calculation steps
An index parameter is used to access a specific element in the array of dou‐
bles in the Data Layer RT. While a calculation step is active, it can use this
index to read parameter values:
● Indices in the range [0 ... 999] access elements in the Data Layer RT
   for the slave axis (motion/axs/<axis-name>/cmd-input/double/data/in). The
   first 20 elements are reserved for synchronized Motion parameters
● Indices from 1000 access elements in the global Data Layer RT at Motion
   system level (motion/cmd-input/double/data/in)
The parameters used in a calculation step can often be specified as a constant
value or as a dynamic value that is retrieved from the Data Layer RT. For
example, the offset value in the "Offset" calculation step can be specified as a
constant "Offset" or as a dynamic value that is retrieved from the Data Layer
RT via an index "offsetDlIdx" for each execution cycle of the Motion control. If
a constant offset is used, the index offsetDlIdx has to be set to -1.

    Handling Modulo axes
The modulo behavior is only applicable to position values and only is only
important for positions. In ctrlX MOTION there is no modulo definition for
velocity, for example. Each axis type can be a modulo axis. A rotary axis can
be a modulo axis, and a linear axis can also be a modulo axis. A mixture
of modulo axes and linear axes is supported. The modulo functionality is
activated by defining a modulo range. Valid values for a modulo axis have to
be in the interval range 0 £ position < moduloRange.

    Parameter of the command function

Introduction
A synchronized Motion command can have the following parameters for the

function:
● SyncMode - describes how the master axis and the slave axis has to reach
the synchronized state
– If the function is absolute, the generated values from the calculation
   pipeline are used as absolute values for the position of the slave
   axis. This can lead to a position jump between the calculated position
   and the current position of the slave axis when the execution of the
   synchronized command starts. In this situation, the dynamic synchroni‐
   zation function executes a Motion profile to reduce the position differ‐
   ence so that the dynamic restrictions are no longer violated
– If the function is relative, the generated values are interpreted as offsets
   that are added to the current position of the slave axis
The absolute and relative synchronization functions can be combined
with the KEEP_STATE function. The aim of KEEP_STATE is to continue a
synchronized Motion command correctly after an error.
See ⮫ Chapter Parameter of the command function on page 105 for more
information
● DynSyncDirection - Describes which master/slave axis relationship has to
be established if the slave axis is a modulo axis. If the function is absolute
and the slave axis is a modulo axis, there is a master/slave axis relation‐
ship for each modulo value. The dynamic synchronization functionality is
used to achieve the synchronized state. The dynamic synchronization direc‐
tion indicates the direction of motion when dynamic synchronization takes
place. See ⮫ Chapter Parameter of the command function on page 105 for
more information. Possible values:
– POSITIVE - the direction of motion is always positive, regardless of the
   current direction of motion
– NEGATIVE - the direction of motion is always negative, regardless of the
   current direction of motion
– SHORTEST_WAY - the direction of motion can be "POSITIVE" or "NEGA‐
   TIVE", depending on which direction represents the shortest distance
– DIRECT – The synchronized state (SYNCHRONIZED) is achieved directly,
   without dynamic synchronization.
   DIRECT should only be used if it is ensured that the slave axis can
   follow the master axis directly.
   Exception: If the calculation pipeline contains a calculation step that
   prevents the synchronized state from being reached directly. In this
   case, the behavior is as described for SHORTEST_WAY.
   The following calculation steps prevent the system from directly
   reaching the synchronized state: Derivation of calculation steps

● SyncSource - specifies whether the target position or the actual (encoder)
  position of the master axis is used as input for the calculation pipeline. The
  value can be:
  – SYNC_COMMAND VALUES - the interpolated command value of the
     master axis is used as input for the calculation pipeline
  – SYNC_ACTUAL - the actual command value of the master axis is used as
     input for the calculation pipeline
  – SYNC_ACTUAL_EXTRAPOLATED - the extrapolated command value of the
     master axis is used as input for the calculation pipeline

Synchronized command function
Different dependencies can exist between a master axis and a slave axis. This
relationship has an effect on how synchronized Motion commands and the
dry run functionality have to act. The SyncMode parameter defines how the
synchronized Motion commands and the dry-running functionality perform the
calculation type. Two switches are coded in SyncMode that define how the
first calculated command value of the slave axis from the calculation pipeline
is to be generated and used.
● Absolute or relative to the position of the slave axis at the start of the
  synchronized Motion command
● (Re-)initializing or retaining the internal state of the calculation pipeline.
  Retaining the state is relevant for the use of the continuous (linearized)
  position for modulo master axes
Both switches can be switched independently of each other.
Wherever the documentation refers to "Position" for synchronized Motion com‐
mands in position mode, e.g. gearInPos, you can also read "Velocity" for the
commands in velocity mode, e.g. gearInVel.

Absolute oder relative to the slave axis
The SyncMode parameter for the mode of the synchronization command can
be set to absolute or relative function:
● Functions for absolute synchronization
   – SYNC_ABSOLUTE
   – SYNC_ABSOLUTE_KEEP_STATE
● Functions of relative synchronization
   – SYNC_RELATIVE
   – SYNC_RELATIVE_KEEP_STATE
When a synchronized Motion command starts its execution, its pipeline is
evaluated in each execution cycle of the Motion control to generate a com‐
mand value for the slave axis. The absolute/relative switch determines how
the master/slave motion profile is "linked" to the start position of the slave
axis when the command is executed.

Function of the absolute synchronization
The generated command values are used directly by the slave axis. If the first
generated command value from the calculation pipeline is too far away from
the initial position of the slave axis, a jump would occur that violates the
limits defined for the axis, e.g. the maximum velocity. Instead of a jump, the
slave axis starts a motion in the direction of the generated command values
without violating the dynamic synchronization limits. This motion is known as
dynamic synchronization. The state of the synchronized Motion of the slave
axis changes to INITIAL_DYN_SYNCHRONIZING.
Situation 1: the master axis is stationary

           slave position
                                     DS
                                P1

                                P2

                0
                                               master position
                            0

The green line represents the commanded synchronized Motion function gear‐
InPos,posslave =posmaster * 1/2 + 0, which is the result of the calculation pipeline
of the gearInPos command.
The dashed red line represents the actual function of the master axis/
sequence axis when SYNC_ABSOLUTE is used.
When the synchronized Motion command starts to be executed at P1, the
slave axis has to be located at P2 in accordance with the gearInPos function
(master axis at 2 position units, slave axis at 1 position unit). As the distance
between the actual position P1 and position P2 is too large to be moved
within the dynamic limits of the slave axis in an execution cycle of the Motion
control, a dynamic synchronization motion [DS] to position P2 starts, which is
indicated by the blue arrow. The state of the synchronized Motion of the slave
axis becomes INITIAL_DYN_SYNCHRONIZING. Note that in this situation, even
if the master axis does not move, the slave axis executes a motion when the
gearInPos command is issued. The motion of the slave axis stops when the
axis is at position P2 and the state of the synchronized Motion of the slave
axis is SYNCHRONIZED.
Situation 2: the master axis is moving

           slave position
                                       DS

                                P1

                                            P3
                                P2

                0
                                               master position
                            0

The green line represents the commanded synchronized Motion function gear‐
InPos,posslave =posmaster * 1/2 + 0, which is the result of the calculation pipeline
of the gearInPos command.
The dashed red line represents the actual function of the master axis/
sequence axis when SYNC_ABSOLUTE is used.
When the synchronized Motion command starts to be executed at P1, the
slave axis has to be located at P2 in accordance with the gearInPos function
(master axis at 2 position units, slave axis at 1 position unit). As the distance
between the actual position P1 and position P2 is too large to move within
the axis limits of the slave axis in an execution cycle of the Motion control,
a dynamic synchronization movement [DS] to position P2 starts. The state
of the synchronized Motion of the slave axis becomes INITIAL_DYN_SYNCHRO‐
NIZING. However, as the master axis moves during the dynamic synchroniza‐
tion movement, the slave axis "chases" the calculated pipeline result, which
is indicated by the blue arrow. When the position of the slave axis finally
matches the calculated pipeline result, the state of the synchronized Motion
of the slave axis changes to SYNCHRONIZED. This is realized at position P3.

Function of the relative synchronization
When the synchronized Motion command starts its execution, the current
position of the slave axis is used to calculate an internal offset so that the
position of the slave axis does not change. As long as the result of the calcu‐
lation pipeline does not change (i.e. neither the position of the master axis
nor the offset), the slave axis does not move.

           slave position
                                P1

                                P2

                0
                                               master position
                            0

The green line represents the commanded synchronized Motion function gear‐
InPos,posslave =posmaster * 1/2 + 0, which is the result of the calculation pipeline
of the gearInPos command.
The dashed blue line represents the actual function of the master axis/
sequence axis when SYNC_RELATIVE is used.
The difference between the actual position of the slave axis P1 and the calcu‐
lated position P2 from the calculation pipeline is an offset that is added to
the calculated result of the calculation pipeline so that the initial position P1
of the slave axis matches the calculation result at the start of the synchron‐
ized Motion command. Thus, the synchronized motion starts at the current
position of the slave axis.
The following use cases are further examples of the use of the SYNC_ABSO‐
LUTE and SYNC_RELATIVE functions.
Use case 1
If you are performing position-related calculations (e.g. cam), you most likely
need the absolute function:
● Assuming you have a cam table with the user-defined relation of the master
    axis and the slave axis, which are specified as example points. This cam
    table defines a relationship between a master axis of 45° and a slave
    axis of 30°. If the master axis is at 45°, the slave axis should move to
    30°, regardless of its current position. You therefore need the SyncMode
    SYNC_ABSOLUTE
Use case 2
If you have a transmission ratio and do not care about the exact position of
the synchronized slave axis, you can use the SYNC_RELATIVE SyncMode. This
has the advantage that the slave axis is immediately synchronized with the
master axis (when both axes are at a standstill); no dynamic synchronization
motion is required:

● Assuming you have an electronic gearbox in your machine with a ratio of
  3:2 (two revolutions of the master axis correspond to 3 revolutions of the
  slave axis). Your master axis is in the 40° position, the slave axis in the 10°
  position
  – If you issue a gearInPos command with SyncMode SYNC_ABSOLUTE,
     ctrlX MOTION starts to move the slave axis from position 10° to 60°.
     This takes time, which is not desirable
  – If you issue the gearInPos command with SyncMode SYNC_RELATIVE,
     the slave axis is synchronized immediately. When subsequently moving
     the master axis, the slave axis moves with the correct transmission ratio

KEEP status
Sometimes it is necessary to continue an aborted Motion command in such
a way that the command continues its previously executed Motion profile
(master/slave synchronized Motion function). However, if the master axis is
a modulo axis, the position of the master axis can be ambiguous when con‐
tinuing the profile of a canceled Motion command. For example, consider the
following scenario:
● The master axis has a modulo range of 120
● The master axis is stationary at position 0
● A gearInPos command with a transmission ratio of 1:2 is started (slave axis
    moves by 1 when the master axis moves by 2)
● Slave axis moves to position 0 if the axis was not already there
● The master axis moves over a distance of 300 (2 times the modulo distance
    plus 60); the slave axis is at position 150
● The gearInPos command is aborted, e.g. due to an error
Although the position of the master axis is now actually 60 (300 mod 120
= 60), its cumulative (linearized) position during the gearInPos command is
300. If the original profile is to be continued by a new command of the
gearInPos command, the position of the slave axis at the current master axis
would be 60 60 * gear ratio = 30. However, the slave axis has to continue from
position 150. This is facilitated by retaining the state of the master axis in the
pipeline.
The information that the master axis moves by a multiple of its modulo
range is kept in the state of the calculation pipeline. To use this state, select
the KEEP_STATE function of the SYNC_ABSOLUTE_KEEP_STATE or SYNC_RELA‐
TIVE_KEEP_STATE command.
Only for modulo axes
The KEEP_STATE functions of SyncMode are used specifically for modulo axes.
If the application has a non-modular master axis, it is recommended to always
use the SYNC_RELATIVE or SYNC_ABSOLUTE functions of SyncMode.
Each calculation pipeline retains its own internal state
The internal state of the calculation pipeline is a property of the calculation
pipeline. Each calculation pipeline has its own internal state:
−   If the application cancels a synchronized Motion with calculation pipeline
    A and then uses a synchronized Motion with calculation pipeline B, the
    "keep state" refers to the internal state of calculation pipeline B, not to the
    calculation pipeline of A
−   If a calculation pipeline is not yet used by the system or another master
    axis is selected, the calculation pipeline does not have a valid status. Only
    the SYNC_RELATIVE and SYNC_ABSOLUTE functions initialize the internal
    state of the calculation pipeline. Do not use the KEEP_STATE function for a
    calculation pipeline when it is used for the first time

Hold the position of the master axis within its half modulo range after the
synchronized Motion command has been canceled
The original synchronized master/slave Motion profile can only be continued if
the master axis keeps its motion within half the modulo range from the posi‐
tion at which the synchronized Motion command was aborted. If the master
axis moves further, the original profile is offset. The linearized continuous
position of the master axis is retained in the calculation pipeline.

        Slave position

                     0°
                          0°   360°      720°                     1080°
                                                Master position

In Fig. 66, the modulo distance of the master axis is 360, and the gray area
represents the modulo range of the master axis that is held in the state of the
calculation pipeline when the synchronized Motion command is canceled at
position P1. The master axis is then moved to position P2. At position P2, the
same synchronized Motion command (i.e. using the same calculation pipeline)
is output with the selection KEEP_STATE in SyncMode:
● When SYNC_ABSOLUTE_KEEP_STATE is used, the absolute position of the
   slave axis from P3 to P2 is used. This continues the original Motion profile,
   indicated by the green line. Note that there is a dynamic synchronization
   motion from position P2 to P3, which is indicated by the blue line
● When SYNC_RELATIVE_KEEP_STATE is used, the slave axis is 'mapped' from
   P3 to position P2 (see Fig. 66), which results in the motion profile shown
   by the red dashed line
If the master axis has been offset by half its modulo distance or more,
the master axis becomes ambiguous for this shifted distance. The resulting
master/slave profile of the continued Motion profile appears to be offset over
the modulo range of the master axis. The chapter "Command function parame‐
ters" (see ⮫ Chapter Parameter of the command function on page 105) shows
what happens if the master axis moves more than half the modulo distance
away from the point at which a gearInPos command was canceled at position
P1.

       Slave position

                    0°
                         0°   360°            720°                     1080°
                                                     Master position

The green line represents the aborted synchronized Motion function gearInPos
dar, posslave = posmaster * 1/2 + 0.
The modulo distance of the master axis is 360, and the gray area represents
the modulo range of the master axis that is maintained in the state of the
calculation pipeline when the synchronized Motion command is aborted at
position P1. The master axis is then moved to position P2, which is more than
half of the master modulo distance. If the synchronized Motion command is
issued at position P2 and KEEP_STATE is selected in SyncMode, the position
of the master axis is "mapped" from P2 into the held modulo range. The
resulting synchronized master axis at P2 is P3. The original Motion profile
appears to be offset over a master axis modulo range:
● When SYNC_ABSOLUTE_KEEP_STATE is used, the absolute position of the
   slave axis from P3 to P2 is used, resulting in the Motion profile shown by
   the red dashed line. This also leads to a dynamic synchronization motion
   from P2 to P4, shown by the blue line
● When SYNC_RELATIVE_KEEP_STATE is used, the position of the slave axis
   P3 is "mapped" to P2, resulting in the Motion profile shown by the dashed
   blue line
As the master axis of the Motion of gearInPos is a straight line Fig. 67, it is
not clear how this Motion profile shifts in the direction of the master axis and
slave axis. The chapter "Parameters of the command function" (see ⮫ Chapter
Parameter of the command function on page 105) uses a more complex cal‐
culation pipeline function, e.g. a curve, to visualize the differences. In this
example, the master axis moves by 3/4 of its modulo range after the synchron‐
ized Motion command is aborted at position P1.

        Slave position

                     0°
                          0°   360°      720°           1080°
                                                Master position

The modulo distance of the master axis is 360, and the grey area represents
the modulo range of the master axis that is maintained in the state of the
calculation pipeline when the synchronized Motion command is aborted at
position P1. The master axis is then moved to position P2, which is more than
half of the master modulo distance. If the synchronized Motion command is
issued at position P2 and KEEP_STATE is selected in SyncMode, the position
of the master axis is "mapped" from P2 into the held modulo range. The
resulting synchronized master axis at P2 is P3. The original Motion profile
appears to be offset over a master axis modulo range:
● When SYNC_ABSOLUTE_KEEP_STATE is used, the absolute position of the
  slave axis from P3 to P2 is used, resulting in position P4. The resulting
  movement profile is shown by the dashed red line. There is a dynamic syn‐
  chronization movement from P2 to P4. Note that the resulting Motion pro‐
  file is no longer the original Motion profile. The Motion profile is modulo-
  offset via a master axis
● When SYNC_RELATIVE_KEEP_STATE is used, the resulting master/slave
  Motion profile, which would be the result of the SYNC_ABSOLUTE com‐
  mand, is offset in the "slave direction", resulting in the master/slave Motion
  profile shown by the dashed blue line. There is no dynamic synchronization
  motion, as the position P2 is now in the master axis of the Motion

Resuming after an error
Let us assume that the transmission ratio is 1:3 (3 revolutions of the master
axis correspond to 1 revolution of the slave axis) and that an error occurs in
the third revolution of the master axis at 120°. This is position 840°, refer to
Fig. 69. The error cancels the synchronized Motion command. The application
detects this error and stops the master axis motion. The stopping process
takes some time so that the master axis comes to a standstill at position 210°
in the third rotation, position 930° in the image.

                       360°
                       310°
                       280°

      Slave position                                                                      Stop
                                                                                  Error position
                       70°                                                       position
                       40°

                              0°   120°   210°   360°                     720°     840°   930°      1080°
                                                        Master position

Depending on the application, there are several options to continue:
● Continue in the current master axis rotation at the current master axis
   position.
   If the application reactivates the synchronized Motion command after the
   error has been corrected, the application has to retain the internal state. In
   this case, the slave axis moves to 310°, as this is the corresponding posi‐
   tion to the master axis of 210° in the third rotation (930° in the image). In
   this case, the application typically uses SYNC_ABSOLUTE_KEEP_STATE as
   the SyncMode
● Continue in the original master axis rotation at the error position.
   The application can also reset the position of the master axis in the third
   revolution to 120°, the position at which the error occurred, and then con‐
   tinue from there. In the command for the synchronized Motion command,
   select that the internal state is to be retained. Then the slave axis moves
   to 280° due to the dynamic synchronization, as this is the position that
   is related to the position of the master axis of 120° in the third rotation,
   840° in the image. In this case, the application typically uses SYNC_ABSO‐
   LUTE_KEEP_STATE as the SyncMode
● Restart in the first master axis rotation.
   If the application always has to start in the first revolution of the master
   axis, the application has to reset the internal state of the calculation pipe‐
   line. If the application selects SYNC_ABSOLUTE for the SyncMode and the
   master axis is at 210° (after stopping), the slave axis moves to 70° to
   be synchronized due to the dynamic synchronization. The application can
   also move the master axis back to the error position at 120° and activate
   the synchronized motion command with SYNC_ABSOLUTE. In this case, the
   slave axis moves to the 40° position
Restriction
The calculation pipeline tracks the rotations of the master axis as long as it is
used by a command. Therefore, calculations that use the inner state can only
work correctly if the application does not move the master axis more than half
of the modulo range.
Assume that the application has detected an error in the third rotation of
the master axis at the 100° position and has executed an error reaction. This
means that the internal state of the calculation pipeline is set to 100° in
the third revolution as the error reaction has switched off the synchronized
Motion coupling. The application then moves the master axis by 360°, i.e.
the master axis is back to position 100° in the fourth turn. If the applica‐

tion now commands a new synchronized Motion command with SYNC_ABSO‐
LUTE_KEEP_STATE, the calculation pipeline assumes that the master axis is
still in the third revolution and moves the slave axis to the associated axis
position for 100 of the third revolution of the master axis.

    Dynamic synchronization
Dynamic synchronization is the functionality that ensures that the master
axis and a slave axis move synchronously. Dynamic synchronization can occur
when a synchronized Motion is started or during the synchronized Motion
as the relationship between the master axis and the slave axis cannot be
maintained. The following table describes the dynamic synchronization states.
              Table 8: Dynamic synchronization states
                 State name                   Description

NO_SYNC_MOTION               No synchronized Motion function active
INITIAL_DYN_SYNCHRO‐         First occurrence of dynamic synchronization
NIZING                       after issuing a new synchronized Motion com‐
                             mand and violation of the axis limits
SYNCHRONIZED                 The slave axis is synchronized and uses the
                             calculated command value from the calculation
                             pipeline
DYN_SYNCHRONIZING            The slave axis synchronizes after the slave axis
                             no longer moves synchronously as the command
                             value from the calculation pipeline has violated
                             the axis limits of the slave axis
SYNC_ERROR                   Coupling error occurred

Before a master axis and a slave axis are moved in synchronization, the slave
axis has to execute a motion so that the velocity relationship or the velocity
and position reference between the master and slave axes can be achieved
and maintained. The motion has to be a uniform motion, which means that
the position reference has to be established at the end of the motion and the
velocity has to correspond to the reference. By default, when a synchronized
motion command is started, the synchronized motion state transitions are
always NO_SYNC_MOTION => INITIAL_DYN_SYNCHRONIZING => SYNCHRON‐
IZED.
The behavior of dynamic synchronization for a GearInPos command depends
on the following conditions:
●  Current position, velocity and acceleration of the slave axis
●  Calculated target position, velocity and acceleration
●  Axis type, modulo axis or non-modulo axis
●  Synchronization mode (SyncMode), SYNC_ABSOLUTE or SYNC_RELATIVE
●  Dynamic synchronization direction (DynSyncDirection), POSITIVE, NEGA‐
   TIVE, SHORTEST_WAY, DIRECT
● Dynamic synchronization limits of velocity, acceleration and jerk
The behavior of dynamic synchronization for a GearInVel command depends
on the following conditions:
● Current velocity and acceleration of the slave axis
● Calculated target velocity and acceleration
● Dynamic synchronization limits of velocity, acceleration and jerk
Two dynamic synchronization methods are available:
● 2-stage dynamic synchronization
● 1-stage dynamic synchronization

The type of the used dynamic synchronization method can be defined via
the axis configuration in the Data Layer. The dynamic 2-stage synchronization
method is the standard type used for dynamic synchronization.
URL                                 Type              Description
/motion/axs/<axsName>/cfg/          Enum              Selected dynamic synchronization method for
functions/coupling/sync-                              synchronized drive commands (TWO_STEP,
motion/ dyn-synchroniza‐                              ONE_STEP)
tion/method

2-stage dynamic synchronization
To synchronize a slave axis with a master axis, the slave axis moves towards
the command value in accordance with the dynamic synchronization motion.
The gap is closed in the following Motion controller cycles. Dynamic 2-step
synchronization defines 2 different steps to close the gap. In the first step, a
trajectory is calculated from the results of the calculation pipeline in order to
synchronize the velocity with a target command value of the slave. This step is
referred to as velocity synchronization. Once the velocity has been synchron‐
ized with the results of the calculation pipeline, a trajectory is calculated in
the second step in order to compensate for the difference between the actual
slave axis position and the command values of the slaves from the results of
the calculation pipeline. This step is referred to as phase synchronization.
If the selected dynamic synchronization method is 2-stage dynamic synchroni‐
zation, one or more steps are required for synchronization depending on the
synchronization mode.
● GearInPos and syncMode = SYNC_ABSOLUTE: Both steps
● GearInPos and syncMode = SYNC_RELATIVE: Only the first step
● GearInVel: Only the first step
The 2-stage dynamic synchronization behavior for GearInPos commands is
shown in ⮫ 2-stage dynamic synchronization on page 116. The diagram shows
the execution of a GearInPos command with the synchronization mode set to
SYNC_ABSOLUTE.

                       1       2

        position

                                                                         t
                   0       3                            4

SYNC_ABSOLUTE
The blue line represents the command values of the slave defined by the cal‐
culation pipeline. The dashed red line represents the actual slave positions.
Dynamic synchronization is active during the time span ➌. During the time
span ➍, the master and slave axes perform a synchronized motion.
● The GearInPos command starts the execution of a synchronized motion at
  t=0. The calculation pipeline generates command values of the slave so
  that the slave axis follows the master axis in each execution cycle of the
  Motion controller. Position P1 specifies the initial command value of the
  slave from the calculation pipeline. Position P2 shows the current initial
  position of a slave axis.
● Depending on the distance between the command value of the slave P1
  and the command value of the slave axis P2, two situations can occur. The
  initial state of the synchronized motion is always NO_SYNC_MOTION, which
  changes to INITIAL_DYN_SYNCHRONIZING.
  – The gap is too large to close in one execution cycle of the motion
      control system without violating the dynamic synchronization limits. If
      a violation of the dynamic synchronization limits occurs, dynamic syn‐
      chronization takes place. Dynamic synchronization generates a smooth
      motion from the current slave axis command value P2 to the slave target
      position P1.
  – The gap can be closed in one motion control execution cycle without
      violating the limits of dynamic synchronization. The initial state of the
      synchronized motion is always NO_SYNC_MOTION. The default behavior
      is a state transition to INITIAL_DYN_SYNCHRONIZING for at least one
      cycle of the motion control program. However, the state transition takes
      place from NO_SYNC_MOTION to SYNCHRONIZED if the dynamic syn‐
      chronization direction is DIRECT.

● During the INITIAL_DYN_SYNCHRONIZING state, the dynamic synchroniza‐
tion functionality attempts to follow the command values of the slaves
defined by the calculation pipeline, based on the master axis. As long as
the dynamic synchronization functionality is active, the first step of the
dynamic synchronization attempts to synchronize the target slave velocity
defined by the calculation pipeline. The first step of dynamic synchroniza‐
tion is indicated by the blue area ➊.
● If the velocity of the slave axis at P3 is equal to the target slave velocity
from the pipeline result at P4, the second step of dynamic synchronization
for phase synchronization of P3 starts. The second step of dynamic syn‐
chronization is indicated by the orange area ➋.
● In the second step of dynamic synchronization, it is tried to synchronize
the target position of the slave defined by the calculation pipeline. During
phase synchronization from P3 to P5, the gap between an actual slave
axis position and the target slave position is closed without exceeding the
configured dynamic synchronization limits of the slave axis. During phase
synchronization of P3, the velocity of the slave axis increases in order to
close the gap between the target slave position and the slave axis position.
The overshoot occurs at P5.
● At position P6, the slave axis corresponds to the target slave position from
the calculated pipeline result; the master and slave axes are synchronized.
The state of the synchronized motion changes to SYNCHRONIZED. If the
state of the synchronized motion is SYNCHRONIZED, the dynamic synchro‐
nization function copies the command value of the slave to the current
command value of the slave axis.
            slave position

                             2
                                                                6

                                              4

                                                  3
       1

                                              5

In Fig. 71, the blue line represents the result of the calculation pipeline based
on the motion of the master axis. ➊ is the modulo range of the slave posi‐
tion (0..360). The dashed lines represent the modulo intervals of the slave
position, based on the result of the calculation pipeline. ➋ stands for the
modulo distance of the slave. The large red dot indicates the time at which
the GearInPos function is started.
At this moment, the state of the synchronized motion changes from
NO_SYNC_MOTION to INITIAL_DYN_SYNCHRONIZING. However, if all axis
restrictions are met (calculated slave target velocity, acceleration and jerk
are within the dynamic synchronization slave limit values) and the dynamic
synchronization direction is DIRECT, the state of the synchronized motion
changes from NO_SYNC_MOTION to SYNCHRONIZED.
The bold dashed red line represents the actual motion of the slave axis. At

➌, the velocity of the slave axis corresponds to the velocity of the calculation
pipeline.
● If the synchronization mode is SYNC_RELATIVE, the slave axis is synchron‐
   ized with the master axis and the green line shows the positions of the
   slave axes.
● If the synchronization mode is SYNC_ABSOLUTE, phase synchronization
   (position synchronization) starts.
   – If the dynamic synchronization direction is POSITIVE, the position of the
      slave axis is synchronized to the red dashed line ➍. The resulting slave
      axis positions are shown by the red line.
   – If the dynamic synchronization direction is NEGATIVE, the position of
      the slave axis is synchronized to the purple dashed line ➎. The resulting
      positions of the slave axis are represented by the purple line.
   – If the dynamic synchronization direction is SHORTEST_WAY, the distance
      between the current interpolated position and the target position is cal‐
      culated and the shortest distance is selected. In Fig. 71, SHORTEST_WAY
      results in phase synchronization in the direction of the red dashed line
      ➍.
   – If the dynamic synchronization direction is DIRECT, the distance
      between the current interpolated position and the target position is
      calculated and the shortest path is selected (as SHORTEST_WAY), but
      the state of the synchronized motion is SYNCHRONIZED at the moment
      the synchronized motion command starts.
   – With ➏, the dynamic synchronization state is SYNCHRONIZED.
Even if POSITIVE or NEGATIVE was specified for DynSyncDirection, it
is possible that the dynamic synchronization uses SHORTEST_WAY. This
depends on the value of a position window called sync-window-modulo. This
parameter can be configured via motion/axs/<axis-name>/cfg/functions/cou‐
pling/sync-motion/dyn-synchronization/sync-window-modulo-extended. If the
position gap between the current interpolated position and the target posi‐
tion is smaller than the configured sync-window-modulo-extended value,
SHORTEST_WAY is selected. The position gap is checked when the dynamic
synchronization switches from velocity synchronization to position synchroni‐
zation, ➌ in Fig. 71.
In the previous software version, the parameter name was "sync-window-
modulo". This name is outdated and should no longer be used. Always use
"syncwindow-modulo-extended".
The DynSyncDirection parameter only applies to following modular axes and
"REF_POS" commands (see ⮫ Chapter Calculation steps on page 91), such as
GearInPos. The DynSyncDirection parameter values POSITIVE, NEGATIVE and
SHORTEST_WAY are valid in the INITIAL_DYN_SYNCHRONIZING and DYN_SYN‐
CHRONIZING states and behave identically for both states.

Data Layer representation
URI                                 Type         Description
/motion/axs/<axsName>/cfg/          double       User-defined synchronization window Modulo value
functions/coupling/sync-                         when moving the slave axis in the direction of the
motion/dyn-synchronisa‐                          shortest path (obsolete)
tion/sync-window-modulo
/motion/axs/<axsName>/cfg/          struct       Synchronization window moduleo of the dynamic
functions/coupling/sync-                         synchronization of this axis
motion/dyn-synchronisa‐
tion/sync-window-modulo-
extended
/motion/axs/<axsName>/cfg/          double       User-defined synchronization window Modulo value
functions/coupling/sync-                         when moving the slave axis in the direction of the
motion/dyn-synchronisa‐                          shortest path
tion/sync-window-modulo-
extended/sync-pos-window-
modulo
/motion/axs/<axsName>/cfg/          double       Position window for the "InSyncWindow" message
functions/coupling/sync-                         (in CyclicStatusData) for a position-controlled oper‐
motion/dyn-synchronisa‐                          ating mode or command
tion/sync-windows/position
/motion/axs/<axsName>/cfg/          double       Velocity window for the "InSyncWindow" message
functions/coupling/sync-                         (in CyclicStatusData) for a velocity window-con‐
motion/dyn-synchronisa‐                          trolled operation mode or command
tion/sync-windows/velocity

1-stage dynamic synchronization
Dynamic 1-step synchronization is an alternative method for synchronizing
a slave axis with a master axis. Compared to 2-stage dynamic synchroniza‐
tion and 1-stage dynamic synchronization, 1-stage dynamic synchronization
does not define two different steps for synchronization. Instead, with 1-stage
dynamic synchronization, the target position and the target velocity are taken
into account in each cycle of the Motion controller if position synchronization
is required. This change to the synchronization strategy can lead to faster
synchronization.
● The 1-stage dynamic synchronization only supports 2nd order profiles. The
    accelerations of the slave axis are not continuous in time and it is not
    possible to limit the jerk.
● Asymmetrical limit values are not supported with 1-stage dynamic synchro‐
    nization. Only the maximum velocity and the maximum acceleration are
    taken into account by the 1-stage dynamic synchronization algorithm.
● The GearInVel and GearInPos commands with RELATIVE mode cannot be
    used if 1-stage dynamic synchronization is selected. You have to use the
    2-step dynamic synchronization method.
If the slave loses synchronization and the dynamic synchronization synchro‐
nizes the velocity of the slave axis with the velocity of the master axis again,
there is a different position offset. If an application applies an offset, e.g. a
second order interpolated offset or a first order filtered offset that exceeds
the limits of the axis, the offset may not be fully applied as the slave axis only
synchronizes to the velocity of the master axis.
In the GearInPos functionality with the SYNC_ABSOLUTE synchronization com‐
mand mode, dynamic synchronization synchronizes the velocity and position
of the slave axis with the velocity and position of the master axis. The Dyn‐
SyncDirection command parameter specifies the direction of motion in which

position synchronization is performed. The possible values for DynSyncDirec‐
tion are listed at ⮫ Chapter Introduction on page 105. The direction of motion
is the direction that is selected during dynamic synchronization when velocity
synchronization has been achieved if 2-stage dynamic synchronization is used.
During position synchronization, the direction of motion is not changed after
velocity synchronization. As the velocity and position synchronization phases
are not separated in 1-stage dynamic synchronization, it is assumed that the
current target velocity remains constant. A future target position is determined
on the basis of the current target position, the current target velocity (which
is assumed to be constant up to the calculated future target position), the
current slave position, the current slave speed and a maximum acceleration
defined by the dynamic synchronization configuration of the slave axis. These
parameters are used to calculate a second-order profile from the current fol‐
lowing position and velocity to the calculated target position and velocity

in the future. This calculation is carried out in every cycle of the Motion
controller as long as dynamic synchronization is active.
In case of modulo slave axes, the calculated future target position also deter‐
mines how many modulo distances (revolutions) of the slave axis have to be
covered. This value is determined once at the start of synchronization and
remains the same during synchronization. This can lead to non-intuitive and
non-optimal behaviour when it comes to optimizing (minimizing) the number
of modulo rotations required during synchronization.
It is also possible that the axes move synchronously, but get out of synchro‐
nization for some reason. Depending on the configuration, dynamic synchroni‐
zation may attempt to synchronize the slave axis again. See ⮫ Chapter Error
reaction on page 126 for the various error reaction configurations for dynamic
synchronization.
● If an axis limit is violated at the start of the synchronized motion command,
  an initial dynamic synchronization always takes place.
● If an axis limit is violated while the state of the slave axis is SYNCHRON‐
  IZED, the "Limit exceeded" error is handled according to the configured
  error reaction for the synchronized motion. The following error reaction can
  be selected.
  – The violation is completely ignored, the new position of the slave axis is
      applied
  – Dynamic synchronization is initiated
  – Abort the synchronized traversing command and set the slave axis to an
      error state
See ⮫ Chapter Error reaction on page 126 for a detailed description of error
handling. Finally, dynamic synchronization ends when one of the following
cases occurs.
● The command for synchronized motion is aborted
● The dynamic synchronization status of the slave axis is SYNCHRONIZED
● A coupling error occurs, which results in the dynamic synchronization state
  SYNC_ERROR for the slave axis.

Status message "InSynchronization" and "InSyncWindow"
To determine whether a coupled slave axis is synchronized with its master
axis, the "InSynchronization" and "InSyncWindow" status signals are available
in the "cyclicStatusData" of the respective axis; see ⮫ Table on page 168.
The "cyclicStatusData" structure can be enabled via the axis's advanced set‐
tings (enable for axis real-time status data).
This is then also available in the PLC's MotionInterface (arAxisStatus[] struc‐
ture).

InSynchronization:
The status message is set when the linked slave command value of a synchro‐
nization command (e.g., GearInPos) has reached the master command value.
The synchronization status is then "SYNCHRONIZED" (value 1).
InSyncWindow:
The status message is set if, during a synchronization command (e.g., Gear‐
InPos), the difference between the master command value and the linked
slave command value is < for the respective configured window.
There is a separate window for position and velocity in the Data Layer for
configuration purposes. You can set different values for both windows; see
⮫ Data Layer representation on page 120.
The position window applies to position synchronization commands (Gear‐
InPos, FlexProfile).
The velocity window applies to velocity synchronization commands (Gear‐
InVel).
Depending on the selected command and the corresponding window, the
"InSyncWindow" message is set.
Use case:
If the actual value signals of master and slave are subject to significant noise,
a tolerance range can be defined using the respective windows to obtain a
more stable synchronization message. Since, in this case, the "InSynchroniza‐
tion" message can vary significantly.
Example of the "InSyncWindow" status message showing a position window
and the corresponding synchronization status:

Dynamic synchronization limits
Dynamic synchronization attempts to synchronize the slave axis. The system
attempts to synchronize so that the motion of the slave axis ultimately con‐
forms to the specified synchronized motion function. During dynamic synchro‐
nization, the configured dynamic synchronization limits are used while the
gap between the slave axis’s target command value and its current command
value is closed. The dynamic synchronization limits depend on the selected
dynamic synchronization method.

● 1-stage dynamic synchronization
  Asymmetrical limit values are not supported for dynamic synchronization in
  one step
  – Only the limit value for the dynamic synchronization velocity pos
     (velPos) is used. The limit value for the dynamic synchronization
     velocity neg (velNeg) is ignored. Thus, the dynamic synchronization
     velocity neg (velNeg) = velPos
  – Only the limit value for the dynamic synchronization acceleration (acc)
     is used. The limit value for the dynamic synchronization delay (dec) is
     ignored. Thus, the dynamic synchronization delay (dec) = acc
● 2-stage dynamic synchronization
  Asymmetrical limit values are supported for 2-stage dynamic synchroniza‐
  tion

  The dynamic synchronization velocity pos (velPos) and the dynamic syn‐
  chronization velocity neg (velNeg) are used during the synchronization
  phase
  – Dynamic synchronization velocity position limit = minimum value of
     (target velocity of slave axis + dynamic synchronization velocity position
     limit) and axis limit
  – Dynamic synchronization velocity neg. limit value = minimum value of
     (target velocity of slave axis - dynamic synchronization velocity neg.)
     and axis limit value
  – Dynamic synchronization acceleration limit = minimum value of the
     dynamic synchronization acceleration and axis limit
  – Dynamic synchronization delay limit = minimum value of the dynamic
     synchronization delay and axis limit
  – Dynamic jerk limit value for synchronization = minimum value of the
     dynamic jerk limit value for synchronization and the axis limit if the axis
     limit unequal to 0.
     Dynamic synchronization jerk acceleration limit value = dynamic synchro‐
     nization jerk acceleration limit value when the axis limit is 0
  – Dynamic synchronization jerk delay limit value = minimum value of the
     dynamic synchronization jerk delay limit value and the axis limit if the
     axis limit is not 0.
     Dynamic synchronization pressure delay limit = dynamic synchronization
     pressure delay when axis limit is 0

During the second step, phase synchronization, the slave axis is always in
the INITIAL_DYN_SYNCHRONIZING and DYN_SYNCHRONIZING states within
the bandwidth (target velocity - velPos) < Target velocity < (target velocity
+ velNeg).

                              350
                                                  velPos = 50

                                                  target velocity = 300
                              275
                                                  velNeg = 25

velocity of the master axis

                               –250
                                                     velPos = 50

                                                     target velocity = –300
                               –325
                                                     velNeg = 25

velocity of the master axis

The dynamic synchronization limits (for velocity, acceleration and jerk) are
limited by the axis limits. If the calculation result of the dynamic synchroniza‐
tion limit value (for velocity, acceleration or jerk) is higher than the axis limit,
the dynamic synchronization limit value (for velocity, acceleration or jerk) cor‐
responds to the axis limit. However, if the jerk limit value of the axis is 0,
the user-defined jerk limit value is used. Therefore, if the jerk limit value of
the axis is 0 and the dynamic synchronization jerk limit value defined via the
"Data Layer" node or in the axis configuration is greater than 0, the applied
dynamic synchronization jerk limit value is greater than 0 (as defined in the
"Data Layer" node or in the axis configuration).
The values for the target velocity, acceleration and jerk of the slave axis are
the result of the calculation pipeline and therefore the input for dynamic
synchronization.
The user-defined values for velocity, acceleration and jerk limit values are
defined in the synchronization axis configuration together with the axis limits.
These user-defined values for velocity, acceleration and jerk limit values can
also be configured asynchronously at any time via the Data Layer node. New
values are applied when a new synchronized Motion command is issued.
The user-defined value is checked when the synchronized Motion command
becomes active. If the user-defined value set by the application is higher than
the axis limit value, a warning is generated. In this case, the dynamic synchro‐
nization limits (for velocity, acceleration and jerk) are set to the axis limits
(for velocity, acceleration and jerk).
Negative values for the user-defined limit values are not permitted. If a nega‐
tive value is specified via the Data Layer, an error is generated. If a negative
value is specified in the configuration, this value is permitted when loading
the configuration, but the system is not booted.
Please note that the dynamic velocity limit also changes if the following
velocity changes, e.g. due to a new command to the master axis.
The dynamic velocity limit for synchronization only affects synchronized
Motion commands for position control. GearInVel commands are therefore not
affected.

If the slave axis cannot follow the master axis during GearInPos or GearInVel
functionality, the message "Warning: Axis limits exceeded" is reported and the
synchronization status changes to DYN_SYNCHRONIZING. The reasons for this
warning may be that the master axis is moving with a dynamic that is too high
or that the slave axis has initiated a step, for example due to an offset that is
too large.
Possible solutions to this problem are as follows:
−   Move the master axis more uniformly or more slowly
−   Do not change the parameters of the synchronized Motion calculation
    pipeline steps in such a way that the slave axis moves with excessive
    dynamics
− Increase the values for the axis limits that are violated by the slave axis to
    enable higher dynamics, e.g. its maximum axis acceleration.

Note that the slave axis does not necessarily leave the SYNCHRONIZED state
(and goes into the ERROR or DYN_SYNCHRONIZING state), or even ignores
the violation and remains SYNCHRONIZED. This would be the result of the
configuration of the error handling in the Motion synchronization for the slave
axis.

Data Layer representation
URI                            Type           Description
/Motion/axs/<axsName>/cfg/     struct         Complete configuration of the synchronized Motion
functions/coupling/sync-Motion                behaviour of this axis
/Motion/axs/<axsName>/cfg/     struct         Complete configuration of the dynamic synchroniza‐
functions/coupling/sync-                      tion of this axis
Motion/dyn-synchronization
/Motion/axs/<axsName>/cfg/     struct         All dynamic limits of the dynamic synchronization of
functions/coupling/sync-                      this axis
Motion/dyn-synchronization/lim
/Motion/axs/<axsName>/cfg/     double         User-defined velocity limit when the slave axis is
functions/coupling/sync-                      moved in positive direction
Motion/dyn-synchroniza‐
tion/lim/vel-pos
/Motion/axs/<axsName>/cfg/     double         User-defined velocity limit when the slave axis is
functions/coupling/sync-                      moved in negative direction
Motion/dyn-synchroniza‐
tion/lim/vel-neg
/Motion/axs/<axsName>/cfg/     double         User-defined acceleration limit
functions/coupling/sync-
Motion/dyn-synchroniza‐
tion/lim/acc
/Motion/axs/<axsName>/cfg/     double         User-defined deceleration limit
functions/coupling/sync-
Motion/dyn-synchroniza‐
tion/lim/dec
/Motion/axs/<axsName>/cfg/     double         User-defined jerk limit value during acceleration
functions/coupling/sync-
Motion/dyn-synchroniza‐
tion/lim/jrk-acc
/Motion/axs/<axsName>/cfg/     double         User-defined jerk limit value during deceleration
functions/coupling/sync-
Motion/dyn-synchroniza‐
tion/lim/jrk-dec

Value (object) *
{
  "limits":{
    "acc": 0,
    "dec": 0,
    "jrkAcc": 0,
    "jrkDec": 0,
    "velNeg": 10,
    "velPos": 10
  }
)

Error reaction
If the slave axis violates its limits during Motion with a synchronized Motion
command, an error reaction to the synchronized Motion follows. The following
error reactions can be configured:
● KEEP_SYNCHRONIZED - retains the SYNCHRONIZED state and sends the
   new values to the slave axis, even if they exceed the axis limits
● CREATE_ERROR - Generates an error in the slave axis and cancels the
   coupling. The slave axis stops as part of the standard reaction, the master
   axis is not affected.
● TRY_TO_RESYNC - leave the SYNCHRONIZED state and attempt to follow
   within the dynamic synchronization limits
CREATE_ERROR         always   generates     a   diagnostic    error.  For   the
KEEP_SYNCHRONIZED and TRY_TO_RESYNC error reactions, it is possible to
configure whether a diagnostic message or a warning is to be generated, with
details of which limit was exceeded and by how much.
● NONE - the reaction is muted (no message)
● WARNING - creating a diagnostic warning
● MESSAGE - creating a diagnostic message

Data Layer representation
URI                              Type            Description
/Motion/axs/<axsName>/cfg/       struct          Complete configuration of the synchronized Motion
functions/coupling/sync-Motion                   behaviour of this axis
/motion/axs/<axsName>/cfg/       struct          Overall configuration of the error reaction for
functions/coupling/sync-                         synchronized motion of this axis
motion/error-reaction
/motion/axs/<axsName>/cfg/       struct          Overall configuration if the limit values of the slave
functions/coupling/sync-                         axis are exceeded
motion/error-reaction/slave-
limits-exceeded
/motion/axs/<axsName>/cfg/       enum            Error reaction if the slave axis limits are
functions/coupling/sync-                         exceeded (KEEP_SYNCHRONIZED, CREATE_ERROR,
motion/error-reaction/slave-                     TRY_TO_RESYNC)
limits-exceeded/type
/motion/axs/<axsName>/cfg/       enum            Create a diagnostic message or warning (NONE,
functions/coupling/sync-                         MESSAGE, WARNING)?
motion/error-reaction/slave-lim‐
itsexceeded/type
Value (object) *
{
  "slaveLimitsExceeded":{
    "type": "KEEP_SYNCHRONIZED",

        "diagnosis": "WARNING"
    }
)

### 6.2.2 Cam tables for Flexprofiles and CamIn

Cam tables can be used for the "CamIn" and "Flexprofile" motion commands.
Using different "Segment-Law-Type" segment motion laws, different types of
cam tables can be used for the "Flexprofile" and "Cam-in" motion commands.
The following tables are available:
● POINTS_TABLE_AUTO (table with up to 1,024 points) default
● POINTS_TABLE_LIN (table with up to 100,000 points and linear interpola‐
   tion)

● POINTS_TABLE_SPLINE (table with up to 100,000 points and spline inter‐
   polation)
Tables of type "POINTS_TABLE_AUTO" do not need to be explicitly validated
before the command is executed.
Tables of type "POINTS_TABLE_LIN" and "POINTS_TABLE_SPLINE" has to be
validated before the command is executed.
(Cfg node->flexprofile->validate (with profile name) ).
                    POINTS_TABLE_AU POINTS_TABLE_LI POINTS_TABLE_SP
                    TO                   N                   LINE
Number of points Up to 1024              Up to 100,000       Up to 100,000
Interpolation       Spline up to 100 Linear                  Spline
                    points, then linear
Calculation         Uses pre-calcu‐      Simple linear cal‐ Uses pre-calcu‐
                    lated values (fixed- culation            lated values
                    size arrays)         (Arrays with vari‐ (Arrays with vari‐
                                         able size)          able size)
Configuration/vali‐ Does not need to The cam table has The cam table has
dation              be explicitly vali‐ to be validated      to be validated
                    dated                before it can be    before it can be
                                         used in the CamIn used in the CamIn
                                         or Flexprofile com‐ or Flexprofile com‐
                                         mand.               mand.
Cam tables of the "POINTS_TABLE_LIN" and "POINTS_TABLE_SPLINE" types
with a larger number of points require more memory. For point tables with
a large number of points (e.g., > 10,000 points), it is recommended to use
linear interpolation. Linear interpolation is sufficiently accurate when there are
a large number of points.
Cam tables can be created, opened, and edited using the "Cam Designer"
app. See "ctrlX Cam Designer App," Application Manual (R911430577), ⮫ .
Writing point tables via the PLC interface
CXA_MOTION library:
The "ML_AxsSetFlexProfileConfiguration()" function in the CXA_Motion PLC
library can be used to write the flexprofile configuration and, consequently, a
corresponding point table (using the FlexProfileSegment and LawType).
CXA_PLCOPEN library:
The function blocks "MB_WriteFlexProfile" and "MB_WriteFlexProfileType02"
are available for writing the Flexprofile configuration (using the "ProfileSeg‐
ments" and "LawType" structures).
.....
Validating point tables

Point tables of type 'POINTS_TABLE_AUTO' do not need to be explicitly vali‐
dated.
Point tables of the types 'POINTS_TABLE_LIN' and 'POINTS_TABLE_SPLINE'
has to be explicitly validated before using a CamIn command; otherwise, an
error message is displayed.
Maximum number of point tables
Motion App Version MOT                    Maximum cam tables
< MOT V 4.6                               99
From MOT V4.6                             250

Further information
For more information about the CamIn command, flexprofiles, and the Cam
Designer, click here:
● ⮫ Chapter 7.2.24 AxsCamIn, AxsCamInEx - Controlling a cam with a scaling
  factor on page 431
● ⮫ Chapter 7.2.28 AxsFlexprofile, AxsFlexprofile2, AxsFlexprofileEx, AxsFlex‐
  profileEx2 - Commanding an electronic cam (FlexProfile) on page 457
● ⮫

### 6.2.3 Electronic cam (FlexProfile)

Overview
The "Electronic cam (FlexProfile)" function is one of the position-based syn‐
chronization commands of ctrlX MOTION. This means that a slave axis is cou‐
pled to a master axis. The slave axis calculates a slave axis position based on
the master axis position and with the help of a calculation rule (see figure 1).
The synchronous command is commanded for the slave axis and processed in
its context.
The "Electronic cam (FlexProfile)" function consists of these parts:
● General basic functionality of a synchronous command
● Configuring the electronic cam disk
  – Profile
  – Points table
● FlexCmd command

axis
The "Electronic cam (FlexProfile)" function uses the same basic functions
as other synchronous commands. The slave axis position is calculated in a
calculation chain (see ⮫ Chapter 6.2.1 Synchronized Motion on page 84).
The FlexProfile command also contains the dynamic synchronization function
with the corresponding parameters (see ⮫ Chapter Dynamic synchronization
on page 115). The error reaction can also be configured here if the slave axis
cannot follow the calculated position within the scope of its dynamics (see
⮫ Chapter Error reaction on page 126).

The calculation rule for determining the slave axis position implements an
electronic cam. The configuration object of the electronic cam (profile)
defines what the slave axis position should be for certain master axis posi‐
tions. This can be done either on the basis of mathematical formulas (e.g.
5th degree polynomial) or with the help of a points table. Both variants can
also be combined in sections in one profile. The point tables are separate
configuration objects, which in turn are referenced in a profile by name. A
points table can therefore be used by several different profiles.
The AxsFlexprofile command uses the configuration of the profile during oper‐
ation to calculate the motion of the slave axis and traverse it accordingly. The
command has a parameter for this in which the name of the profile to be used
is specified.
The following chapters describe in detail which functions are supported

by the electronic cam (flex profiles) and how they are configured and com‐
manded:
● The description of the specific calculation chain can be found in chapter
  ⮫ Chapter General function on page 129
● All motion laws that can be used to define the profile are described in the
  chapter ⮫ Chapter Functional description on page 129. Extended functions
  of the FlexProfile (such as event status and control) can be found below
● The configuration of the profiles is described in the chapter ⮫ Chapter Gen‐
  eral function on page 129. This can either be done by writing directly to
  the Data Layer or generated with the CamDesigner. The CamDesigner is a
  convenient user interface with which profiles can be created and modified
  intuitively and easily. The CamDesigner can directly read the configuration
  and write the configuration in ctrlX MOTION
● All profiles and the points tables are stored as separate files in the file
  system (in the configuration data) and can be read and modified using a
  simple text editor. Details can be found in the chapter ⮫ Chapter Storage in
  the file system on page 149
● The description of the AxsFlexprofile command (prerequisites, parameters,
  interfaces) can be found in chapter ⮫ Chapter 7.2.28 AxsFlexprofile, Axs‐
  Flexprofile2, AxsFlexprofileEx, AxsFlexprofileEx2 - Commanding an elec‐
  tronic cam (FlexProfile) on page 457

    Functional description

General function
FlexProfiles belong to the group of electronic motion laws. These are
described as analytic functions by mathematical motion laws. The FlexProfile
has the following additional features:

● Time control
● Event control
● Width selection of motion laws, etc.

Basic structure of the “Flexprofile" synchronous operating modes
In the “Flexprofile" operation mode, there is a fixed relationship between a
specified master axis position and the slave axis. The main process chain for
this synchronization type also includes the gearbox and the FlexProfile, which
influence the relationship between the master and slave axis. All axis types
can be used as the master axis. In addition, there are several methods to
affect the signal flow.

These input values are calculated in two different ways in the calculation
chain:
● Interpolated offsetting (highlighted in yellow in the figure)
● Filtered offsetting (highlighted in blue in the figure)

                     c

   From version 3.6, the "SlaveAdjust" parameter has been added to the FlexPro‐
   file (gray "Profile" on the left).
   For compatibility reasons, there is a function without "SlaveAdjust" and a new
   function with "SlaveAdjust" in the "CXA_Motion" PLC library. In the PLC library
   CXA_PLCopen and in the CXA_MotionInterface, the previous function blocks
   and structures have been extended to be compatible.

   The FlexProfile can be started using the PLC function block ML_FlexProfile.

Configuring the profile
 When creating the Flexprofile, make sure that the individual motion steps are
 defined by a relative master axis section and a relative stroke (see figure). The
 motion sections defined in this manner are arranged successively. A profile

 created using this method no longer has an absolute reference. This can be
 restored by using a flex step.

   The master axis range can be either axis or time (time control). The duration
   for processing a motion step or an entire profile can be entered directly. The
   scaling of the master and slave axis is not restricted.

Time master
In order to allow time-controlled sequences in a MotionProfile, this section
shows how different master sources can be assigned to the individual motion
steps of a MotionProfile. For a cam profile, there is now no longer just a single
master axis for all motion steps, but a separate master source can be defined
for each step when creating the motion profile or motion plan. If we now
also consider time as a master source, time-controlled motions can also be
realized in this way. For steps with such a time reference signal, the execution
period does not depend on the master axis velocity.

   To restore an absolute master axis reference or to synchronize between dif‐
   ferent master axis encoders, a flex step (⮫ Flexstep , page 134,) has to be
   used.

Motion laws

Standard motion laws
The relationship between the master axis motion and the slave axis motion
in the individual motion steps is specified by motion laws based on different
standardized transfer functions.

According to VDI2143, the following four motion tasks can be defined in the
boundary points of a motion step, depending on velocity and acceleration:

Motion tasks according to VDI 2143
Table 9: Motion tasks according to VDI 2143
Motion task            Abbreviation           Velocity      Acceleration
Rest                        R                   v=0             a=0
Constant velocity           G                   v≠0             a=0
Reverse                     U                   v=0             a≠0

Various motion laws can be classified accordingly in terms of their function
courses possible boundary value adaptations. The following overview shows
the most common standardized motion laws:

Rest → Rest

Standstill

Simple sinoide (simple sine curve)

Bestehorn sinoide (inclined sine curve)

Acceleration-optimum inclined sinusoid

Torque-optimized inclined sine curve

Gutman sinusoid

Modified sinusoid

Modified acceleration trapezoid

Polynomial 5th order

7th order polynomial

Velocity → Velocity

Linear interpolation

Polynomial 5th order

Polynomial 7th order

Modified sinusoid

Rest → velocity

Polynomial 5th order

Polynomial 7th order

Velocity → rest

Polynomial 5th order

Polynomial 7th order

General motion

Polynomial 5th order

Polynomial 7th order

An overview of the motion laws can be found in the documentation "ctrlX Cam
Designer, Chapter 4.7 Motion laws" (see ⮫ link to web documentation).

Extended motion laws
Further special motion laws (interpolation) are shown here for use in Motion‐
Profiles. With different degrees of freedom, these laws facilitate an optimized
adjustment of the motion profile to the motion problem.

As a rule, the boundary conditions such as:

●   Stroke
●   Velocity
●   Acceleration
●   Jerk

are specified and result in the master axis section (see figure below).

Acceleration-limited motion (trapezoidal profile)

Acceleration-limited sinusoid

Jerk-limited motion

Polynomial 5th order, limited velocity

Overshooting-free polynomial 5th order

Acceleration-limited trapezoid

An overview of the motion laws can be found in the documentation "ctrlX Cam
Designer, Chapter 4.7 Motion laws" (see ⮫ link to web documentation).

Flexstep
If a motion step is marked as a flex step, it can be regarded as an active
motion step. Due to the boundary values specified previously, its motion path
is corrected and adapted at runtime. Among other things, flex steps are used
for synchronization between motion steps with different master axes (time
and positioning axes).

For a flex step, a slave axis target position to be reached in absolute terms
can also be specified instead of the stroke and a master axis end position
to be reached in absolute terms instead of the master encoder section (the
stroke and the master encoder section are then calculated at runtime, if nec‐
essary). The boundary values are adapted to avoid velocity jumps.

In principle, the following configurations can be implemented with the flex
step:

●   Flex step with relative stroke and relative master axis section
●   Flex step with absolute stroke and relative master axis section
●   Flex step with relative stroke and absolute master axis section
●   Flex step with absolute stroke and absolute master axis section

The flex step can only be configured with the following motion laws:
− General motion, polynomial 5th order
− General motion, polynomial 7th order
A flex step always has to be applied after a time step.

             Motion law boundary conditions

Transition and synchronization methods

Selecting the coordinate system
 The classification of the various profiles in the coordinate system can be
 either relative or absolute in relation to the respective master and slave axis.
 This makes it possible to combine the permitted setting options as required
 (see following figure).

  The red line symbolizes the current profile, the blue line symbolizes the pro‐
  file you want to change to.

Switching and synchronizing
After the assignment of profiles has been defined, both the switching char‐
acter (switching at angle or immediately) and the synchronization type (with
or without synchronization) can be selected. When switching to "Angle", the
system waits from the enable signal until the entered angle is reached, at
which point it switches to the other profile or starts the new profile in the
decoupled state. Immediate switching is executed simultaneously with the
input of a positive edge. When using this functionality, note the congruence of
the FlexProfiles. If this is ignored, command value jumps can occur in case of
some configurations.

  The following figures present some possible combinations for switching and
  synchronizing together with arbitrary coordinate systems.

The following figure shows switching to a different MotionProfile. The origin
of the first and second MotionProfile is congruent and is located in the zero
point of the coordinate system (absolute master axis position and absolute
slave axis position - case A). The MotionProfiles are not moved.

slave axis position

The following figure shows switching to a different MotionProfile. The origin
of the second MotionProfile is moved to the current master and slave axis
position of the first MotionProfile (relative master axis position and relative
slave axis position - case D).

axis position

The following figure shows switching to a different MotionProfile. The origin
of the second MotionProfile is moved to the current master axis position of
the first MotionProfile (relative master axis position and absolute slave axis
position – case B). The MotionProfile is not moved towards the slave axis.

axis position

The following figure shows switching to a different MotionProfile. The origin
of the second MotionProfile is moved to the current slave axis position of
the first MotionProfile (absolute master axis position and relative slave axis
position - case C). The MotionProfile is not moved towards the master axis.

axis position

The following figure shows switching to a different MotionProfile. The second
motion profile is moved to the current slave axis position of the first motion
profile and started (absolute master axis position and automatically deter‐
mined slave axis position (relative) - case E). The MotionProfile is not moved
towards the master axis.

position and automatically determined slave axis position (relative)

Processing type
It is distinguished between two types of processing (see the following figure):

● Continuous processing
● One-time processing (one shot)

During continuous processing, the active FlexProfile is executed cyclically.
Ensure that the final profile velocity of the last motion step is identical to the
initial velocity of the entire profile. If necessary, an error message is output.
With the one-time processing, the selected profile is only executed once. The
same profile can be started several times by commanding the FlexProfile sev‐
eral times.

Event control and status

Characteristics of the event control
In almost all the processing machines, several axes participate in the process.
The motion tasks to be carried out by the individual axes mostly depend on
one another and result from the application task.

Therefore, the motion of one axis often has to start at exactly the place where
another axis has reached a certain position or where another axis remained in
a motion step for a certain time. This is shown in the following picture.

Events are highly suitable to mark these points in the MotionProfile. These
points can then be responded to very conveniently within a PLC via the event
status. It is possible to start follow-up motions of other axes or to decide on
the further processing. The result is a dynamic "motion chain" that reflects the
dependencies of the machine in its realization within a PLC.

Events can be attached to the motion steps. One condition consists of a
trigger and an action.

The trigger is used to detect the states of the control variables. These are:

● Relative/absolute master axis position reached
  Describes the reaching of a relative/absolute position of the master axis.
  Similar to a programmable limit switch, the current position of a master
  source can be monitored. If it crosses a specified position in the current
  motion step, the event occurs.
● Relative/absolute slave axis position reached
  Describes the reaching of a relative/absolute position of the slave axis. The
  same concept can also be applied to the slave axis position.
● Event control
  The event can only be triggered by setting the corresponding bit in the
  event control.

● Time-controlled canceling
  The step itself is not time-controlled, i.e. it does not have a time master,
  but a master axis to which the motion should be synchronized. This can be
  achieved by linking an event that monitors the travel time since the start
  of the motion step and an action that causes the current motion step to be
  aborted. The resulting Motion profile can be used generically for different
  master axis velocities.
● Monitoring for time steps
  With regard to the time-master functionality, the events can also be used
  for the monitoring of different master sources. Depending on the motion
  task, for example, an event can be set so that the travel distance of the
  master axis is monitored during a motion step that is coupled to a time
  master. In this way, an error reaction could be carried out if the master
  axis has moved too far during this time. Different process states can be
  easily and comfortably buffered by the user with the help of the events. It
  is possible to react to this in a PLC.

The action is an active element responsible for the activation of certain varia‐
bles.

Possible actions are:

● Set bit immediately
  One of the available bits in the event status is set immediately.
● Set bit at the end of the motion step
  One of the available bits in the event status is set at the end of the motion
  step.
● Set bit at the end of the profile
  One of the available bits is set in the event status at the end of the profile.
● Set bit immediately and continue with the next motion step
  Causes the current motion step to be canceled immediately. This step is
  not processed completely, instead, the next motion step begins directly
  from the ongoing motion. If this is a flex motion step, this change can be
  made without shocks or jerks.

Mapping of events
Event status:
Whether an event has been triggered can be read out via the event status.
When configuring an event, you can specify which bit should are to be set in
this event status when the event is triggered.
Event control:
In addition to the option of triggering an event with a configured trigger, an
event can also be triggered directly via the event control. Which event is
triggered for which bit is specified via the configuration of the event, as with
the event status.
The user has 16 bits available for mapping the event status.

States
   There is various state information for a FlexProfile.

   AccessState
   An important piece of information is the accessState, which describes how
   the FlexProfile can currently be accessed. The diagram shows the different
   states and the possible transitions.

● LOCKED_FOR_RUN: The FlexProfile is executed (see ⮫ Chapter Com‐
  manding on page 151). This state is reached by commanding the FlexPro‐
  file command. The state is set to VALID when the FlexProfile command is
  completed and is no longer processed
● LOCKED_FOR_EDIT: The FlexProfile is edited (see ⮫ Chapter Configuration
  on page 147). This state is achieved by configuring the FlexProfile. The
  state is set to UNVALIDATED when writing the FlexProfile configuration has
  been completed
● IN_VALIDATION: The FlexProfile is validated (see ⮫ Chapter Validation
  on page 151). This status is achieved by starting the validation of the
  FlexProfile. The state is set to VALID when validation is complete and the
  FlexProfile configuration is valid. The state is set to INVALID when valida‐
  tion is complete and the FlexProfile configuration is invalid
● VALID: The FlexProfile is valid and ready for execution. This state is ach‐
  ieved by performing a validation of the FlexProfile with a valid FlexProfile
  configuration
● INVALID: The FlexProfile is invalid and has to be corrected. This state is
  achieved by performing a validation of the FlexProfile with an invalid Flex‐
  Profile configuration
● UNVALIDATED: The FlexProfile has not yet been validated. This state is
  reached after writing a FlexProfile configuration has been completed.

Event Condition
The functionality of the event conditions is explained in the chapter "Event
status and control" (⮫ Chapter Functional description on page 129).

Data Layer
Data Layer path     Type               Description
https://<ip-        Struct             FlexProfile state
addr>/automa‐
tion/api/v2/nodes/
motion/axs/[axs‐
Name]/state/
functions/cou‐
pling/sync-motion/
flexprofile/pro‐
files/[profileName]
https://<ip-        UInt64             Event state
addr>/automa‐

tion/api/v2/nodes/
motion/axs/[axs‐
Name]/state/
functions/cou‐
pling/sync-motion/
flexprofile/event-
condition/state
https://<ip-        UInt64             Trigger event directly
addr>/automa‐
tion/api/v2/nodes/
motion/axs/[axs‐
Name]/state/
functions/cou‐
pling/sync-motion/
flexprofile/event-
condition/control

Example of state information:

{
"type":"object","value":
{
  "profiles": [
     {
       "name": "0",                         /// name of the single
flexprofile
       "accessState": "UNVALIDATED"         /// access state
     }
  ],
  "events": {
     "conditionStatusMask": 0,              /// bit mask shows
triggered and signaled events
    "conditionControlMask": 0               /// bit mask with active
control events
  }
}

}

    Configuration
The following configuration options are available:
● Data Layer
● Storage in the file system

● CamDesigner
● PLC
● BundleIF
The functions for PLC, BundleIF and Data Layer are described here: ⮫ Chapter

### 7.2.28 AxsFlexprofile, AxsFlexprofile2, AxsFlexprofileEx, AxsFlexprofileEx2 -

Commanding an electronic cam (FlexProfile) on page 457.
To be able to command a FlexProfile, the following 2 steps are necessary:
● The FlexProfile has to be configured completely
● The configuration validation has to be completed successfully (see
    ⮫ Chapter Validation on page 151)
It is not possible to configure the FlexProfile in the following states:
● LOCKED_FOR_RUN: The FlexProfile is currently executed. Exit the command
   to be able to configure the FlexProfile
● IN_VALIDATION: The FlexProfile is currently validated. Wait until the valida‐
   tion is complete. The state then changes to VALID or INVALID
Flex profiles are configured for one axis and can only be used by this axis.
Four FlexProfiles (0 ... 3) are available. 64 segments and 64 events can be
created in each FlexProfile.
Point tables are configured for the entire Motion and can be used by all
FlexProfiles.

Data Layer
Data Layer path     Type                 Description
https://<ip-        Struct               Configuring a FlexProfile
addr>/automa‐
tion/api/v2/nodes/
motion/axs/
[axsName]/cfg/
functions/cou‐
pling/sync-motion/
flexprofile/pro‐
files/[profileName]
https://<ip-        Struct               Configuring a point table
addr>/automa‐
tion/api/v2/nodes/
motion/cfg/func‐
tions/sync-motion/
point-table/tables/
[tableName]
The configuration data is described in the documentation "ctrlX CORE, Data
Layer node" (see ⮫ link to web documentation). An example of the configura‐
tion data is described in the chapter "Configuration - Examples" (see ⮫ Exam‐
ples on page 149).
Please note:
● By writing the configuration in the Data Layer, the data is not yet stored
  remanently in the file system. Remanent saving is carried out when a
  "Create" command is carried out on the following Data Layer path.
URL: https://<ip-addr>/automation/api/v2/nodes/motion/admin/cfg/save

{
"type":"object","value":
{
  "configurationPath": "",

    "id": "",
    "phase": "save"
}
}

Storage in the file system
Json files in the file system
The configuration data of the flex profiles and the point tables are each stored
as separate files in the file system. They can be read and modified.
Data Layer path    Type               Description
https://<ip-       [profileName].json Configuring a FlexProfile
addr>/automa‐

tion/api/v2/nodes/
motion/Axis/[axis‐
Name]/Flexpro‐
files
https://<ip-       [tableName].json Configuring a point table
addr>/automa‐
tion/api/v2/nodes/
motion/System/
Pointtables
The configuration data is described in the chapter (see ⮫ link to web
documentation). An example of the configuration data is described in the
chapter "Configuration - Examples" (see ⮫ Examples on page 149).

Examples
1. Example: Configuring a FlexProfile with one segment and one event:
Configuring a FlexProfile:

{
"type":"object","value":
{
  "name": "0",
  "segments": [
    {
      "gain": 50,
      "range": 10,
      "v0": 0,
      "a0": 0,
      "j0": 0,
      "v1": 0,
      "a1": 0,
      "j1": 0,
      "limV": 0,
      "limA0": 0,
      "limA1": 0,
      "limJ0": 0,
      "limJ1": 0,
      "lambda": 0.5,
      "syncType": "SEG_DEFAULT",
      "lawType": "REST_IN_REST_POLYNOMIAL_5",
      "pointTableReference": "",
      "master": 0,
      "camBuilderSegmentData": ""
    }

    ],
    "events": [
       {
         "segmentNmb": 0,
         "triggerCondition": "SEG_TRIGGER_MASTER_REACHED_REL",
         "triggerValue": 5,
         "masterType": 0,
         "actionMode": "SEG_ACTION_EXTERNAL_INSTANT",
         "actionBit": 0,
         "segmentNmbFormula": 0,
         "valueFormula": ""
       }
    ],
    "masterAxsRefVel": 10,
    "camBuilderProfileData": ""
}
}

2. Example: Configuring a FlexProfile with a segment that uses a point table:
Configuring a FlexProfile:

{
"type":"object","value":
{
  "name": "0",
  "segments": [
     {
       "gain": 50,
       "range": 10,
       "v0": 0,
       "a0": 0,
       "j0": 0,
       "v1": 0,
       "a1": 0,
       "j1": 0,
       "limV": 0,
       "limA0": 0,
       "limA1": 0,
       "limJ0": 0,
       "limJ1": 0,
       "lambda": 0.5,
       "syncType": "SEG_DEFAULT",
       "lawType": " POINTS_TABLE_AUTO",
       "pointTableReference": " PointTable1",
       "master": 0,
       "camBuilderSegmentData": ""
     }
  ],
  "events": [],
  "masterAxsRefVel": 10,
  "camBuilderProfileData": ""
}

Configuration of the points table:
{
  "name": "PointTable1",
  "points": [
      11,

        42,
        45,
        6
    ],
    "interpolation": "DEFAULT",
    "camBuilderData": ""
}
}

ctrlX Cam Designer
See        documentation          for        the         ctrlX        Cam
Designer      ⮫        https://docs.automation.boschrexroth.com/iirds/cdp-
metadata.boschrexroth.de~iiDC~Product-ctrlX-Cam-Designer/.

    Validation
The configuration of the FlexProfile is checked during validation. This step is
required so that the FlexProfile can be commanded with valid data.
Validation is successful if:
● at least one segment is configured
● all configured segments contain valid values
● all configured events contain valid values
● the master axis reference velocity is valid
A FlexProfile can only be validated in the UNVALIDATED state, i.e. the Flex‐
Profile must currently not be executed or edited and must not be invalid.
If validation is successful, the state is set to VALID. If the configuration is
invalid and validation has therefore failed, the status is set to INVALID (see
⮫ AccessState on page 145).
If a FlexProfile is configured via the CamDesigner, validation is carried out
automatically when the configuration is written. If the FlexProfile is configured
using one of the other options, validation has to be carried out separately.

Data layer
Data Layer path      Type               Description
https://<ip-         String             Validating a FlexProfile
addr>/automa‐
tion/api/v2/nodes/
motion/axs/
[axsName]/cfg/
functions/cou‐
pling/sync-motion/
flexprofile/validate
Validation is performed for the corresponding FlexProfile when a "Create" is
performed on the Data Layer path with the FlexProfile name specified.

    Commanding
The FlexProfile command is a single-axis command and is commanded for
the slave axis. This command activates the FlexProfile functionality and (as
soon as the command is active) calculates it in the slave axis. The configured
motion laws (profiles) are used to determine the target position of the slave
axis and a motion is interpolated to this position.
Prerequisites:
● The slave axis is activated
● The profile is configured and (successfully) validated
● There is a master axis

The profile is specified in the command via a parameter. As soon as the com‐
mand is active, the profile is locked and can only be edited again once the
FlexProfile command has been completed.
The FlexProfile command does not end automatically, but has to be aborted
by another unbuffered command (such as AxsAbort or PosAbs).
The interfaces for commanding the FlexProfile functionality are described
in the Command electronic cam profiles (flex profiles) (see ⮫ Chapter

### 7.2.28 AxsFlexprofile, AxsFlexprofile2, AxsFlexprofileEx, AxsFlexprofileEx2 -

Commanding an electronic cam (FlexProfile) on page 457.

Further information
●   See chapter 4 "Introduction and overview"
●   ⮫ Chapter 6.2.3 Electronic cam (FlexProfile) on page 128
●   ⮫ Chapter 8.1.2 Window – “Axes” on page 795
●   ⮫ Chapter 8.1.3 Window – “Axis Profiles” on page 803
●   ⮫ Chapter 8.1.4 Window – “Coordinated Motion” on page 806

### 6.2.4 CamIn - Cam with scaling factor

A simplified FlexProfile command "CamIn" with an adjustable scaling factor
(stroke) and switching positions has been implemented for motion processes
that can only be mapped using point tables.
Features:
● 4 preconfigured profiles for the use of point tables with up to 100000
   interpolation points
● Switching between the points tables immediately or depending on the
   position
● Scaling factor for the points tables, with immediate or position-dependent
   effect
● Additional linear path with an adjustable reduction ratio for achieving
   linear motion between the master and slave
● Command parameters are validated for "default" type point tables or
   "POINTS_TABLE_AUTO" (implicit)
There are different types of point tables that can be used. Also refer to
⮫ Chapter 6.2.2 Cam tables for Flexprofiles and CamIn on page 127.
● POINTS_TABLE_AUTO or default (table with up to 1,024 points)
● POINTS_TABLE_LIN (table with up to 100,000 points and linear interpola‐
   tion)
● POINTS_TABLE_SPLINE (table with up to 100,000 points and spline inter‐
   polation)
Validating point tables (POINTS_TABLE_LIN, POINTS_TABLE_SPLINE with up
to 100,000 points):
These so-called "BigPoint tables" have to be validated before using the CamIn
command, just as with the Flexprofile command.
To do this, a "validate" function is available in the Data Layer below the corre‐
sponding axis and below the "cfg" folder. The state is stored in the Data Layer
below the corresponding axis and within the "state" folder for the selected
profile (0-3) as "acessState" (UNVALIDATED or VALIDATED).

If a profile contains an unvalidated point table of type "POINT_TABLE-LIN"
or If "POINTS_TABLE_SPLINE" is controlled using a CamIn command, the
error message "Error in the CamIn axis command" is displayed. "The refer‐
enced cam table does not exist in the validated profile" error was generated
(detailed diagnostics "0C550637").
A profile with an unvalidated points table of type "default" or
"POINTS_TABLE_AUTO" can be controlled using a CamIn command (implicit
validation).

The command's input values are processed in the calculation chain in two
different ways:
● Interpolated offsetting (highlighted in yellow in the figure)
● Filtered offsetting (highlighted in blue in the figure)

License
The license "{"SWL-XCx-MOT-CAMxxxxxxxxxxxx-NNNN", "1.0"};" is required for
the CamIn functionality.

Data Layer interface
A separate "cam-in" configuration node has been implemented. The configura‐
tion for the points tables can be read out there.
Data Layer configuration node
motion/axs/[axsName]/cfg/functions/coupling/sync-motion/cam-in
motion/axs/[axsName]/cfg/functions/coupling/sync-motion/cam-in/profiles
motion/axs/[axsName]/cfg/functions/coupling/sync-motion/cam-in/pro‐
files/[profileName]
motion/axs/[axsName]/cfg/functions/coupling/sync-motion/cam-in/validate
The status interface contains the active point table and the switches for
scaling factor and position.

State info of execution (active group)              axsStateCamInExecu‐
                                                    tion.fbs
motion/axs/[axsName]/state/functions/coupling/sync- string
motion/cam-in/execution-info/active-point-table
motion/axs/[axsName]/state/functions/coupling/sync-
motion/cam-in/execution-info/active-profile
motion/axs/[axsName]/state/functions/coupling/sync- bool
motion/cam-in/execution-info/single-execution-done
motion/axs/[axsName]/state/functions/coupling/sync- bool
motion/cam-in/execution-info/wait-for-switch
motion/axs/[axsName]/state/functions/coupling/sync- bool
motion/cam-in/execution-info/wait-for-switch-gain
Related profiles:
Profile                                                Name, PointTable‐
                                                       Name, AccessState
motion/axs/Axis_2/state/functions/coupling/sync-       "0", "PointTableName",
motion/cam-in/profiles/0                               "UNVALIDATED"
motion/axs/Axis_2/state/functions/coupling/sync-       "1", "PointTableName",
motion/cam-in/profiles/1                               "UNVALIDATED"
motion/axs/Axis_2/state/functions/coupling/sync-       "2", "PointTableName",
motion/cam-in/profiles/2                               "UNVALIDATED"
motion/axs/Axis_2/state/functions/coupling/sync-       "3", "PointTableName",
motion/cam-in/profiles/3                               "UNVALIDATED"

Further information
Further information on the CamIn command can be found at ⮫ Chapter 7.2.24
AxsCamIn, AxsCamInEx - Controlling a cam with a scaling factor on page 431.

### 6.2.5 Torque/force control

This command switches the drive's operation mode to “Torque/force control
with speed limitation" and controls the axis to the set torque using the speci‐
fied parameters.
Axis profile configuration
The configuration of the axis profile is described under ⮫ Chapter 5.4 Torque/
force control on page 49
Configuration in the drive
The operation mode "Torque/force control with speed limitation" is used in
the drive.

The scaling settings of the axis and the drive coupled via the axis profile have
to match.
In the ctrlX CORE control, the units for torque
●  "Nm"
●  "kNm"
●  "lbf ft (pound force feet)"
●  "lbf in (pound force inch)"
are supported.
The ctrlX CORE does not support percentage-based torque scaling as a torque
command value input.
Changing the drive's configuration settings requires rebooting the axis profile
so that the ctrlX control can detect these changes. To do this, the control
can be switched from the "Running" state to "Configuration" and then back to
"Running."
Data Layer configuration
There is an "in-trq" window for configuring the "in-torque message".
Data Layer path             Type                     Description
https://<ip-addr>/          double                   Window for creating the
automation/api/v2/                                   "in-torque" status.
nodes/motion/axs/                                    Value in the unit of the
<axs-name>/cfg/func‐                                 torque command value
tions/cyclic-status-data/
windows/in-trq
In-torque message
Data Layer path             Type                     Description
https://<ip-addr>/auto‐     bool8                    Torque message is in the
mation/api/v2/nodes/                                 window
motion/realtime/cyclic‐                              TRUE:
StatusData/data/axs/
                                                     Commanded torque - cur‐
<axs-name>/InTorque
                                                     rent torque < Window
                                                     ("in-trq")
https://<ip-addr>/auto‐     double                   current actual torque
mation/api/v2/nodes/                                 value
motion/realtime/cyclic‐
StatusData/data/axs/
<axs-name>/ActualTRQ
https://<ip-addr>/auto‐     double                   Current actual torque
mation/api/v2/nodes/                                 value in % (scaled
motion/realtime/cyclic‐                              by parameter S-0-00533
StatusData/data/axs/                                 "Rated torque/force of
<axs-name>/ActualTRQ‐                                the motor")
Percent                                              (ActualTRQ /rated
                                                     torque) + 100%)
Torque-Velocity-LimitStatus
Data Layer path             Type                     Description
https://<ip-addr>/auto‐     bool8                    High velocity limit is
mation/api/v2/nodes/                                 active.
motion/realtime/cyclic‐                              TRUE:
StatusData/data/axs/
                                                     Ve is at the positive
<axs-name>/TorqueCtrl‐
                                                     velocity limit (P-0-2249
PosVelLim
                                                     bit 1)

Data Layer path           Type                       Description
https://<ip-addr>/auto‐   bool8                      Low velocity limit is
mation/api/v2/nodes/                                 active.
motion/realtime/cyclic‐                              TRUE:
StatusData/data/axs/
                                                     Velocity is at the negative
<axs-name>/TorqueCtrl‐
                                                     velocity limit (P-0-2250
NegVelLim
                                                     bit 2).
p
During the motion, the PLCopen state of the axis is set to CONTIN‐
UOUS_MOTION. It is ensured that the configured dynamic limits of the axis
is complied with. If a velocity limit is specified that is greater than the con‐
figured maximum velocity or greater than the commanded dynamic limit, a

runtime error is generated and the axis switches to ERRORSTOP.
The ML_AxsGetPLCOpenState function block of the CXA_Motion library can be
used to determine the current PLC open state, for example.
Depending on the command parameters, interpolation to the target torque
takes place with or without jerk limitation (both jerk limit values in the com‐
manded dynamic limits are zero).
When the velocity limit is reached, the command continues to run endlessly at
a constant velocity until the specified torque is reached. The command status
remains ACTIVE. The command can be aborted with AxsAbort, see ⮫ Chapter
7.2.4 AxsAbort - Canceling the axis command on page 337. In this case the
command state changes to ABORTED. In this case, it is not the dynamic values
of the motion that apply, but rather the parameterized values of the drive.
In contrast to the position commands, the target velocity for this command is
adjusted using the velocity override.
Example: a target velocity of 500mm/min is commanded. If the override is
now set to 0.5, ctrlX MOTION performs an interpolation of the axis velocity to
250 mm/min (= 500 * 0.5).
The acceleration override has an impact on the acceleration limit value, analo‐
gously to the position command.
An AxsTorque command can be interrupted with an AxsInterrupt com‐
mand, see ⮫ Chapter 7.2.7 AxsInterrupt - Interrupting the axis command
on page 346. In this case, ctrlX MOTION generates a decelerating motion
(in compliance with all dynamic limit values) until it comes to a standstill.
The AxsTorque command remains active and the axis remains in the PLCopen
state CONTINUOUS_MOTION. If an AxsContinue command is issued at a later
point, the ctrlX MOTION interpolates back to the commanded velocity limit
and expects the set torque.
The axis interrupt command can only be sent as an unbuffered command.
Unbuffered commands are prepared within the framework of the execution.
They cancel the currently active command. In this case, the remaining com‐
mand buffer is deleted (all commands are assigned the state ABORTED,
when querying the state with ⮫ Chapter 7.8.7 GetCmdState - Command states
on page 787).
To be able to use the AxsTorque command, at least one drive firmware version
AXS-V-0504 is required for ctrlX DRIVE.
Switching between operation modes of the drive
You can switch between the different operation modes "Position control",
“Velocity control" and "Torque control with speed limitation" if the operation
mode (on-the-fly) is already activated.
The following transitions are possible:

Old state              New state              Behavior
Position control       Torque control         Interpolates Pos, Vel,
Acc with constant accel‐
eration, commands the
torque command value
simultaneously.
Start interpolation of the
torque after the oper‐
ating mode switching
from the last current
torque
Velocity control       Torque control         Interpolates Vel, Acc with
constant acceleration,
commands the torque
command value simulta‐
neously.
Start interpolation of the
torque after the oper‐
ating mode switching
from the last current
torque
Torque control         Torque control         No operating mode
switching.
Start interpolation of the
torque from the last
interpolated torque
Torque control         Position control       Commands the last inter‐
polated torque.
Extrapolates the position
based on the current
Pos, Vel , Acc assuming
constant acceleration.
Start interpolation of the
position after the opera‐
tion mode change from
extrapolated pos, Vel,
Acc
Torque control         Velocity control       Commands the last inter‐
polated torque.
Extrapolates the velocity
on the basis of the cur‐
rent Vel, Acc assuming
constant acceleration.
Start interpolation of the
velocity after the opera‐
tion mode change from
extrapolated Vel, Acc

Commands
The torque/force control mode is activated using the command ⮫ Chapter
7.2.10 AxsTorque - Torque axis on page 354.

If a command is already pending, the newly commanded command (in the
case of an "on-the-fly" change) has to be reported with the "non-buffered"
option.
When using the ctrlX Motion interface in the PLC, this is done implicitly and
automatically when commanding the corresponding operation modes with the
MB_AXIS_MODE_BITS (e.g. "MODE_AXS_VELOCITY".

### 6.2.6 Gantry coupling

The gantry function can be used to implement simple axis couplings. This can
be used to operate mechanically coupled axes via individual commands with
the Motion system.
The gantry is configured via the ctrlX OS Web UI or the ctrlX Data Layer in the
CONFIGURATION Motion system state. The actual coupling and uncoupling of

the gantry is then triggered by a command.
The gantry connection is also terminated in the event of a reset or an error.
Relevant commands:
● AddToGantry ⮫ Chapter 7.2.39 AxsAddToGantry - Adding the axis to the
  gantry on page 502
● RemoveFromGantry ⮫ Chapter 7.2.40 AxsRemoveFromGantry - Removing
  the axis from the gantry on page 505

Relevant configuration (Data Layer):
Data Layer path           Type                      Description
https://<ip-addr>/        bool                      Is this axis part of a
automation/api/v2/                                  gantry?
nodes/motion/axs/                                   TRUE: addToGantry and
<axs_name>/cfg/func‐                                removeFromGantry are
tions/coupling/gantry/                              allowed
member
                                                    If "TRUE" is set, the axis
                                                    cannot be moved as long
                                                    as it is not connected
https://<ip-addr>/        bool                      Allows to move an
automation/api/v2/                                  axis that is an uncon‐
nodes/motion/axs/                                   nected gantry member
<axs_name>/cfg/func‐                                (risk mode, e.g. for
tions/coupling/gantry/                              decoupling a gantry link
move-allowed                                        to ensure synchronous
                                                    run using a regular posi‐
                                                    tioning command)
https://<ip-addr>/auto‐ string                      NOT_GANTRY, UNCON‐
mation/api/v2/nodes/                                NECTED, CON‐
motion/axs/<axs_name>/                              NECTED_MASTER, CON‐
state/functions/coupling/                           NECTED_SLAVE, UNCON‐
gantry/state                                        NECTED_INDEP_MOVE_A
                                                    LLOWED
https://<ip-addr>/auto‐ string                      Specifies which axis is
mation/api/v2/nodes/                                the master for this slave
motion/axs/<axs_name>/
state/functions/coupling/
gantry/master-axis

Straightening can be realized in the application. The configuration "move-
allowed" is set to true for one (or both) gantry axes. If the gantry axes are
not coupled anymore, a regular positioning command (e.g. PositionAbsolute)
can be executed on this axis.
If the gantry axis is added to a kinematics, “move-allowed” does not have any
effect. The kinematics can only moved with a closed gantry.
                      If "move-allowed" is set to true, monitoring for gantry
       NOTICE         axis motion is disabled. In case of incorrect program‐
                      ming this can result in machine damage.
Error reaction:
● If a minor error is detected in one of the gantry axes (both gantry axes still
    comply with the command value input), it is decelerated to standstill from
    this cycle with the currently commanded dynamics.
● If a fatal error is detected in one of the gantry axes (an axis does not
    comply with the command value input anymore), it is decelerated to stand‐
    still from this cycle with the configured axis dynamics.
● If a ring dependency is established between two gantry axes, all axes are
    immediately stopped via their configured error reaction.
Reset of gantry axes:
If an error is pending, a reset always has to be commanded first for the slave
axis. The error is deleted and the gantry link is resolved. A reset can be
commanded for the master axis.
Background information: Errors are exchanged cyclically between slave and
master. If the reset command deletes the error in the master axis, it is copied
from the slave axis in the same cycle. Only after resolving the gantry coupling
it is possible to clear errors on both axes.

Different brake dynamics of the gantry axis

Introduction and overview
The function of the different gantry brake dynamics synchronizes the decelera‐
tion of the faulty and the fault-free axes in case one or several gantry axes fail
in order to reduce the error between the gantry axes and to prevent damage
to the machine.

If you want to use the function of the various gantry decelerating dynamics,
the parameters of the ctrlX DRIVE and the ctrlX MOTION has to be configured.
The function is available in the following version:
−  The firmware version of the ctrlX DRIVE is higher than FWA-XD1-AXS-
   V-0206
− ctrlX MOTION is greater than MOT-V-0112.0
This function is only supported in ctrlX DRIVE

ctrlX DRIVE Parameter
Table 10: ctrlX DRIVE Parameter
Name                          Description
S-0-0390                      Error diagnostic code
P-0-0117.0.0                  ctrlX DRIVE danger defense delay activation:
                              ● Bit 0 to 1: delayed reaction to slight errors
                              ● Bit 2 to 1: delayed reaction to an error in the field bus
                              ● Bit 3 to 1: delayed reaction to critical errors
P-0-0117.0.1                  Emergency stop delay for F2/3 errors
P-0-0117.0.2                  Emergency stop delay for F4/6/7 errors

Name                           Description
S-0-0429                       Delay of the drive in case of emergency stop
S-0-0138                       Bipolar acceleration limit value
S-0-0349                       Bipolar jerk limit value
P-0-0119                       Best possible standstill

Motion parameters
Motion parameters are set using the Data Layer.
● https://<ip-addr>/automation/api/v2/nodes/motion/axs/<axs_name>/cfg/
  functions/coupling/enable-multi-brake-dyn
  Activate the different brake dynamics of the gantry axis

● https://<ip-addr>/automation/api/v2/nodes/motion/axs/<axs_name>/cfg/
  error-reaction/light-error-reaction
  One of three emergency stop operations is caused by a slight device error
  – ESTOP_AXIS_LIMIT: Emergency stop with dynamic axis parameters
  – ESTOP_USER_LIMIT: Emergency stop with user-defined dynamic parame‐
     ters
  – ESTOP_TORQUE_FREE: Enable drive torque of the axis.
     (For MOT-V-0116 or older versions, the emergency stop with the best
     possible deceleration for ESTOP is implemented)
● https://<ip-addr>/automation/api/v2/nodes/motion/axs/<axs_name>/cfg/
  error-reaction/fieldbus-error-reaction
  Emergency stop type selection for emergency stop after a field bus error
● https://<ip-addr>/automation/api/v2/nodes/motion/axs/<axs_name>/cfg/
  error-reaction/critical-error-reaction
  Emergency stop type selection for emergency stop after a critical error
● https://<ip-addr>/automation/api/v2/nodes/motion/axs/<axs_name>/cfg/
  error-reaction/fatal-error-reaction
  Emergency stop type selection for emergency stop after a fatal error
● https://<ip-addr>/automation/api/v2/nodes/motion/axs/<axs_name>/cfg/
  error-reaction/stop-dec
  User-defined emergency stop acceleration
● https://<ip-addr>/automation/api/v2/nodes/motion/axs/<axs_name>/cfg/
  error-reaction/stop-jrk
  User-defined emergency stop jerk

Error classification and reaction principles
Different brake dynamics of the gantry axis in active state
Table 11: Error classes and possible reactions
Error type Error level       Emergency      Emergency stop in Description
                             stop in case case of fault-free
                             of faulty axes axes
F2/3       Minor error       Control        Control           ctrlX CORE continues to control all
                                                              axes and the gantry emergency stop
                                                              is control-guided.
                                                              The drive has to set a delay for
                                                              slight errors to ensure that the con‐
                                                              trol has sufficient time to complete
                                                              the emergency stop operation.
                                                              P-0-0117.0.0: bit0 to 1
                                                              P-0-0117.0.1: delay (e.g. 5000 ms)

Error type Error level      Emergency      Emergency stop in Description
stop in case case of fault-free
of faulty axes axes
F4           Field bus      Drive          Control           The control loses control over the
error                                           device in case of a faulty axis.
The faulty axis and all subsequent
axes are decelerated in a drive-
controlled way. Fault-free axes are
decelerated in a control-guided
way.
The drive has to set an emergency
stop delay time for bus errors
to ensure that the controller can
detect bus errors within the delay.
P-0-0117.0.0: Bit 2 to 1
P-0-0117.0.2: Mandatory delay time
6 ms
The drive and the Motion axes have
to set the same dynamic parame‐
ters for the delay
F6/7         Critical error Drive          Control           The control loses control over the
device in case of a faulty axis.
The faulty axis and all subsequent
axes are decelerated in a drive-
controlled way. Fault-free axes are
decelerated in a control-guided
way.
The drive has to set an emergency
stop delay time for bus errors
to ensure that the controller can
detect bus errors within the delay.
P-0-0117.0.0: Bit 3 to 1
P-0-0117.0.2: Mandatory delay time
6 ms
The drive and the Motion axes have
to set the same dynamic parame‐
ters for the delay
F8           Fatal error    Drive          Control           No configuration required

Use
Select the following settings to ensure the correct use of the different brake
dynamic functions of the gantry axis:

Delay time of the drive in case of emergency stop

Dynamic break parameter settings
The drive settings of all gantry link axes should be consistent.

The control is configured via the Data Layer. The settings of all gantry link
axes should be consistent.
● https://<ip-addr>/automation/api/v2/nodes/motion/axs/<axs_name>/cfg/e-
  stop is set to
  { "estopToNoDevErr": "ESTOP_USER_LIMIT",
  "estopToNoDeviceInfo": "ESTOP_USER_LIMIT",
  "estopToDevLightErr": "ESTOP_USER_LIMIT",
  "estopToFieldbusErr": "ESTOP_USER_LIMIT",
  "estopToDevCriticalErr": "ESTOP_USER_LIMIT",
  "estopToDevFatalErr": "ESTOP_AXIS_LIMIT" }
  set
● https://<ip-addr>/automation/api/v2/nodes/motion/axs/<axs_name>/cfg/
  error-reaction/stop-dec is set to the same deceleration rate as the
  drive. For example, if the value 500.00 mm/s² is set in the drive,
  the value has to be set to 0.500 m/s² in the control
● https://<ip-addr>/automation/api/v2/nodes/motion/axs/<axs_name>/cfg/
  error-reaction/stop-jrk is set to the same deceleration rate as the
  drive. For example, if the value 6000.00 mm/s³ is set in the drive,
  then the value has to be set to 6 m/s³ in the control

Axis profile setting
 Configuring S-0-0390 (error diagnostics code) using ctrlX I/O Engineering in
 the drive's PDO and the axis profile in ctrlX MOTION is required so that the
 motion control system can detect the error type and severity of the faulty
 drive.

  Enter the diagnostic error code in the axis profile.

Empiric parameter values
The value of parameter P-0-0117.0.2 significantly influences the result of the
gantry synchronous stop which is usually set to 12-14 ms. However, it is
recommended to test it on a real machine to achieve optimal results.
ctrlX DRIVE Engineering provides the test function.

CXA_GantryAlignment
GantryAlignMode (ENUM)
Name                          Initial    Comment
                              value
MoveSlaveToMaster             0          Positioning the slaves to the
                                         master position
MoveMasterToSlave                        Positioning the master to the slave
                                         position
MoveBothToMidPos                         Position the axes to the center
                                         position

MB_GantryAlignment

Interface description

Table 12: MB_GantryAlignment
Validity range Name                 Data type        Description
INPUT          Execute              BOOL             Start the motion at a rising edge

Validity range Name              Data type       Description
Tolerance‐        LREAL           Max. tolerance window. The axis does not
Window                            move as the offset between master and slave
                                  is less than the tolerance window
Mode              GantryAlignMode Gantry align strategy, default value MoveSla‐
                                  veToMaster
Velocity          LREAL           Maximum “velocity” value (does not necessa‐
                                  rily have to be reached)
Acceleration      LREAL           “Acceleration” value (always positive)
Deceleration      LREAL           “Deceleration” value (always positive)
Jerk              LREAL           “Jerk” value (always positive)
OUTPUT         DONE              BOOL            The commanded position was reached

ACTIVE            BOOL            In process
Error             BOOL            Indicates that an error occurred in the func‐
                                  tion block
ErrorID           ERROR_CODE      Error class
ErrorIdent        ERROR_STRUCT    Detailed error information
Inout Const    Master            AXIS_REF        Reference to the master axis
Slave             AXIS_REF        Reference to slave axis

      Brief description
      The MB_GantryAlignment function block aligns the gantry master and the
      slave axis prior to coupling of the gantry object.

      Functional description
      The master axis and the slave axis have to be in status STANDSTILL before
      starting the alignment.
      The function block sets the axis attribute "move-allowed" to TRUE before the
      axis is moved. The extended status of the master/slave is changed internally
      from UNCONNECTED to UNCONNECTED_INDEP_MOVE_ALLOWED. The gantry
      attribute “move-allowed” is reset to FALSE as soon as the axis has executed
      the motion.
      If the position offset between master and slave is smaller than the “Toleran‐
      ceWindow”, both axes do not move and the function block is directly set to
      DONE.
      If the alignment of the master axis and the slave axis is completed, the func‐
      tion block is set to DONE.
      ● During an alignment process in mode “MoveMasterToSlave” and “MoveSla‐
         veToMaster”, the target axis always has to be in status STANDSTILL while
         the other axis is moving
      ● During an alignment process in mode “MoveBothToMidPos”, an axis is
         stopped as soon as the motion of the other axis is canceled or changes
         to state ERRORSTOP
      The function block can be used in status ACTIVE. That means the current
      function block is executed.
      The function block is available as Open Source to all users.

                      −   The function block facilitates independent
      WARNING
                          motions of a gantry axis by internally set‐
                          ting the “motion/axs/[axis]/cfg/functions/coupling/
                          gantry/move-allowed“ axis attribute to TRUE
                      −   This can result in mechanical damage! Ensure the
                          safe use of the function.

Troubleshooting
The function block uses the error table CXA_TABLE.
It can generate the following error messages in Additional1/Additional2.
Table 13: MB_GantryAlignment
ErrorID    Additional1              Additional2        Comment
OTHER_ERRO 16#00000000              16#00000001        Master is not in standstill
R
OTHER_ERRO 16#00000000              16#00000002        Slave is not in standstill
R
OTHER_ERRO 16#00000000              16#00000003        Errors occur while the master is moving
R
OTHER_ERRO 16#00000000              16#00000004        Errors occur while the slave is moving
R

### 6.2.7 Axis status information

Information on the status of an axis is required in many applications. These
applications are provided by the ctrlX MOTION in each cycle in the Data Layer
and are available in the PLC or other applications.
As the cyclical provision of axis status data costs runtime, this function can
be activated individually for each axis. For the Standstill, InPosition,
InVelocity and InTorque status bits, a window can be set in the Data Layer
within which the value can fluctuate. The corresponding bit is only deleted
when the value leaves the window.

Function overview
The following status information is generated cyclically:
Category                   Name                      Data type                 Description
Status bits                DataValid                 bool                      The cyclical data is
                                                        valid
    Homed                     bool                      The axis is referenced
    Standstill                bool                      The axis does not move
                                                        within the standstill
                                                        window
    PowerReady                bool                      The drive is ready for
                                                        power up
    PowerOn                   bool                      The axis has power and
                                                        is actively controlled
    HasError                  bool                      An error is pending at
                                                        the axis
    HasWarning                bool                      A warning is displayed
                                                        on the axis
    AxisFollowCommand         bool                      The axis follows the
                                                        value settings of the
                                                        control

Category                     Name                  Data type              Description
InPosition            bool                   The axis is at the target
                                             position
In Velocity           bool                   The axis has reached
                                             the target velocity
InTorque              bool                   The target torque has
                                             been reached
InSyncWindow          bool                   Difference between the
                                             slave command value
                                             and the master com‐
                                             mand value. If it
                                             is within the config‐

                                             ured "InSync" position
                                             window, or "InSync” -
                                             velocity window
InSynchronization     bool                   The axis is following
                                             a master axis, and the
                                             slave command value
                                             has reached the master
                                             command value
OverrideIsZero        bool                   The velocity override is
                                             zero
TorqueCtrlPosVelLim   bool                   Torque Control, positive
                                             velocity limit reached
TorqueCtrlNegVelLim   bool                   Torque control, negative
                                             velocity limit reached
Actual values                ActualPos             double                 Current Location
ActualVel             double                 Current velocity
ActualTRQ             double                 Current torque
ActualTRQPercent      double                 Current torque in %
                                             (scaled by S-0-0533
                                             "Rated torque")
DriveStatusWord       uint16                 Status word of the drive
DriveError            uint32                 Diagnostic number of
                                             the drive
State machine                PlcOpenState          enum                   State of the PlcOpen
                                             state machine
Safety technology            ActualSafeMode        bool                   Safe operating mode
                                             active

Data Layer image
The status data is provided for each axis. These statuses are provided in real
time via a real-time Data Layer interface. The axis states are mapped in the
"motion/realtime/cyclicStatusData" node.

Relevant configuration (Data Layer):
Data Layer path                 Type                              Description
https://<ip-addr>/automa‐       bool                              Remanent activation of the
tion/api/v2/nodes/motion/axs/                                     cyclical data for the axis
[axsName]/cfg/functions/cyclic-                                   TRUE: cyclical data active
status-data/remanent

Data Layer path                 Type                                 Description
https://<ip-addr>/automa‐       double                               Standstill window
tion/api/v2/nodes/motion/axs/
[axsName]/cfg/functions/cyclic-
status-data/windows/standstill
https://<ip-addr>/automa‐       double                               Velocity window
tion/api/v2/nodes/motion/axs/
[axsName]/cfg/functions/cyclic-
status-data/windows/in-vel
https://<ip-addr>/automa‐       double                               Position window
tion/api/v2/nodes/motion/axs/
[axsName]/cfg/functions/cyclic-
status-data/windows/in-pos
https://<ip-addr>/automa‐       double                               Torque window
tion/api/v2/nodes/motion/axs/
[axsName]/cfg/functions/cyclic-
status-data/windows/in-trq
Whether the status for an axis is formed cyclically can be read out in the Data
Layer.
Data Layer path               Type                                   Description
https://<ip-addr>/automa‐     bool                                   Cyclical data for the axis active
tion/api/v2/nodes/motion/axs/
[axsName]/state/functions/
cyclic-status-data/active

Further information
⮫ Chapter 7.8.8 AxsSetRTStateEnabled - Enabling cyclic axis data on page 792

### 6.2.8 Measuring the maximum axis dynamics

This functionality facilitates determining the maximum dynamics of axes. The
user can use these values to optimize his machine. For example, it is pos‐
sible to determine which reserves are still available in order to increase the
dynamics of a kinematic system and thus achieve higher productivity.
The functionality can be enabled separately for each axis. For the axes with
activated measurement, the dynamic set values are determined in each Motion
cycle and the maximum values are saved.

Data Layer image
Data Layer path                    Type                              Description
motion/axs/[name]/cfg/func‐        bool                              Switching the maximum value
tions/max-value-monitoring                                           recording on or off. Only takes
                                              effect when switching from
                                              SETUP to OPERATING
motion/axs/[name]/state/       axsCfgLimits.fbs                      Recorded maximum values.
values/maxium-value-monitoring                                       Same data structure as for the
                                              configured limits
The recorded data is deleted when the configuration flag is switched from
"FALSE" to "TRUE". The configuration flag is part of the axis configuration and
is saved and loaded in it.
{
    "posMin": -67.600000000013,
    "posMax": 77.199999999987,
    "velPos": 5999.999999999131,

        "velNeg": 6000.000000000172,
        "acc": 2.000000000005,
        "dec": 2.000000000009,
        "jrkAcc": 666.708333322793,
        "jrkDec": 666.708333325883,
        "posMinUnit": "mm",
        "posMaxUnit": "mm",
        "velPosUnit": "mm/min",
        "velNegUnit": "mm/min",
        "accUnit": "m/s^2",
        "decUnit": "m/s^2",
        "jrkAccUnit": "m/s^3",
        "jrkDecUnit": "m/s^3"

}
Due to the additional CPU performance required for the measurement, the
functionality is switched off by default.
It is recommended to disable the function again after optimization.

### 6.2.9 Command value decoupling

If a machine is to be commissioned and all components (drives and controls)
are already configured correctly it is better if only certain machine parts are
moved when creating the application. Command value decoupling can be
used for this purpose.
Command value decoupling turns selected drive axes into virtual axes. A
virtual axis can be commanded in the same way as a normal axis and is
equipped with the same interfaces. There are only principle-related restric‐
tions for drive-related functions (such as probe measurement, travel to fixed
stop, ...). However, interaction between the virtual axes and other axes (Syn‐
cMotion) or kinematics (CoordinatedMotion) is possible.
There is a switch to switch all configured axes to virtual simultaneously and an
additional switch per axis to switch individual axes.
The switches can be switched at any time, but are only active when the con‐
trol is switched from SETUP to OPERATION.
Even if axes have been switched to virtual, the control system continues to
check during start-up whether all configured axis profiles are working cor‐
rectly. This means that the devices to which the axis profiles are assigned
have to be available and correctly configured and the axis profiles also have to
be configured correctly.

Configuration
Configuration is carried out via the Data Layer:
Data Layer node             Type                     Description
motion/cfg/func‐            bool                     TRUE: All configured axis
tions/ignore-axisprofiles                            profiles are ignored and
                                                     all axes are virtual axes.
                                                     FALSE: The set axis pro‐
                                                     files are active
motion/axs/<name>/cfg/ bool                          TRUE: The configured
functions/ignore-axispro‐                            axis profile of the corre‐
file                                                 sponding axis is ignored
                                                     and this axis becomes a
                                                     virtual axis.
                                                     FALSE: the configured
                                                     axis profile is active

### 6.2.10 Supporting devices in "Open Loop" mode with ctrlX

Positions are usually exchanged between the ctrlX Motion control and con‐
nected devices with associated axes. Furthermore, corresponding operation
modes with position control are expected. After an error or during initializa‐
tion start-up, a position operation mode is selected.
In order to also operate devices without feedback ("open loop"), a configura‐
tion option is provided for connected axes. In this case, velocity values are
exchanged and operation modes with velocity control are expected.
Open-loop axes are often driven by asynchronous motors or stepper motors.
Use:
● No great demands on accuracy
● Cost-effective
● Load torque is relatively constant

Configuring the open-loop device in ctrlX I/O Engineering
Only enter the control/status word and the velocity value.
S-0-0024 MDT
● S-0-0134 Master control word
● S-0-0036 Velocity command value
S-0-0016 AT
● S-0-0135 Drive status word
● S-0-0040 Actual velocity value
No position value must be entered in the cyclic data!

Optional setting via ⮫ Tab “General” on page 824.
Adjust start parameters for operation mode in ctrlX I/O Engineering

S-0-0032 Operation mode value "2" (velocity control)
No value must be entered for a position operating mode (value "11").

Relevant configuration (Data Layer):
There is one configuration parameter per axis:
● Boolean switch "open-loop" for setting the open-loop mode of the axis
Data Layer path           Type                      Description
https://<ip-addr>/        bool                      Setting the open loop
automation/api/v2/                                  mode
nodes/motion/axs/                                   TRUE: Open loop mode
<axs_name>/cfg/func‐                                active
tions/open-loop
Available commands
Axis commands for open loop            Operation mode
Velocity                               Velocity
GearinVel                              Velocity
SyncVelCmdGeneric                      Velocity
EStop                                  Velocity
Abort                                  Velocity

Axis commands for open loop             Operation mode
Reset                                   Velocity
Power                                   Velocity
The "driveVelMode" command parameter has to be set to "TRUE" for the
velocity command to be executed in velocity control mode. When using the
Motion interface within a PLC application, the "DriveVelControl" setting has to
be set in the "VelMode structure".
Error handling
If commands are used that require a position or a positioning mode (e.g.
"pos-abs"), a diagnostics is reported (e.g. "Device is not configured correctly
for positioning mode".
If such a command is issued in motion (e.g. velocity), an error reaction occurs.
Example of an error message when activating a position command with an
open loop device:

loop device

Drive parameterization
The device-specific parameterization of the open loop functionality has to
be carried out in the device manufacturer's engineering tool for the corre‐
sponding device.
For a Bosch Rexroth drive, parameterization is carried out in ctrlX DRIVE Engi‐
neering.
In particular, the parameterization of the motor parameters and the selection
of the motor control has to be adapted to the respective device hardware.

### 6.2.11 Axis decoupling from the axis profile

The "ignore-axisprofile" or "ignore-axisprofiles" node can be used to virtually
switch individual axes or all axes in an existing project without having to
make any changes to the IO or the Motion configuration. This ensures that the
physical axes set in this way cannot move on a finished machine, e.g. during
commissioning, and that the axis is treated as a virtual axis instead.
An axis set as virtual is decoupled from the command value.

                      As the virtual Motion axes behave exactly as if the
      WARNING         axis were real, it has be ensured that the virtually set
                      axes cannot cause a collision with other axes or obsta‐
                      cles. Example kinematics XYZ (real, real, virtual). In this
                      case, the real Z-axis would not move, although it is com‐
                      manded by the Motion.
                      Even in the case of a mechanical gantry link, it has to
                      be ensured that this setting cannot cause any damage
                      to the machine if, for example, only the gantry master
                      axis is moved and the gantry slave axis is set virtually.

Relevant configuration (Data Layer):
Data Layer path           Type                        Description
https://<ip-addr>/auto‐ bool                          TRUE: The axis is virtual,
mation/api/v2/nodes/                                  a real axis linked via the
motion/axs/<name>/cfg/                                axis profile is not moved,
functions/ignore-axispro‐                             the axis is virtual, decou‐
file                                                  pled from the command
                                                      value.
                                                      FALSE: The axis operates
                                                      as configured (if an axis
                                                      profile is set, it is used to
                                                      control the motion of the
                                                      actual drive)

https://<ip-addr>/          bool                      TRUE: All axes are vir‐
automation/api/v2/                                    tual, no real axis can
nodes/motion/cfg/func‐                                move, decoupled from
tions/ignore-axisprofiles                             the command value.
                                                      FALSE: The axes operate
                                                      as configured (if an axis
                                                      profile is set, it is used to
                                                      control the motion of the
                                                      actual drive)
The content of the node is saved remanently and is retained even after the
control is switched off.
A change to the node only becomes active when the Motion is booted (switch
from Configuration to Running).

### 6.2.12 Axis checksum

To reduce the switching time between configuration and runtime modes, a
checksum can be applied to the parameters for each axis. If this matches the
most recently transmitted configuration, the parameters do not need to be
rewritten during the switching process.
To enable this feature, set the use-checksum node to TRUE.
This feature is available only for ctrlX DRIVE starting with FW 5.2.
The following parameters are used:
−   S-0-0326 (CoE: 0x2B60:0E): Resulting checksum
−   S-0-0327 (CoE: 0x2B60:04): List of parameters for checksum calculation
−   S-0-0192 (CoE: 0x2B60:03): List of all parameters
The checksums are currently not stored permanently. That is why the first
startup takes longer after the control is switched on.

Relevant configuration (Data Layer):
The configuration interface uses the POST method.
Data Layer path             Type                      Description
../axisprofile/profiles/    bool                      TRUE: The checksum
<name>/cfg/device-app-                                should be verified during
data/use-checksum                                     axis startup.
                                                      FALSE: The checksum
                                                      should be ignored during
                                                      startup

Data Layer path            Type                      Description
../axisprofile/profiles/   bool                      TRUE: The checksum
system/use-checksum                                  should be verified for all
                                                     axes during startup.
                                                     FALSE: The configuration
                                                     for each axis is effective.
                                                     (See above.)
The status interface uses the GET method.
Data Layer path            Type                      Description
../axisprofile/profiles/   bool                      TRUE: The checksum
<name>/state/device-                                 is verified during axis
app-data/use-checksum                                startup.
                                                     FALSE: The checksum is
                                                     ignored during startup
../axisprofile/profiles/   bool                      TRUE: The checksum is
system/use-checksum                                  verified upon startup of
                                                     all axes.
                                                     FALSE: The configuration
                                                     for each axis is effective.
                                                     (See above.)
../axisprofile/profiles/ uint32                      Checksum value
<name>/state/device-
app-data/checksum-value
../axisprofile/profiles/ array of string             List of all parameters
<name>/state/device-                                 used to calculate the
app-data/checksum-list                               checksum
