# 21 CXA_LoopControl

## 21.1 Introduction and overview

The CXA_LoopControl provides basic elements and controllers of the control
engineering.
The majority of the function blocks are available as time-discrete as well as
event-controlled version.
All function blocks are implemented irrespective of the hardware acc. to IEC
61131-3.
The CXA_CommonTypes and CXA_Utilities libraries are required.
Table 486: Areas of application and functions/function blocks of CXA_LoopControl
Area of application (folder in library)
Function blocks                                    Description
Controllers
⮫ Chapter 21.4.2 IL_PIDType01 on page 598          PID-controller with anti-reset windup integrator
                                                   and delimiter, time discrete
⮫ Chapter 21.4.3 IL_PIDType02 on page 602          PID-controller with anti-reset windup integrator
                                                   and delimiter, event-controlled
⮫ Chapter 21.4.4 IL_PIDType03 on page 605          2DOF (2 degree of freedom) PID-controller with
                                                   anti-reset windup integrator and delimiter, time
                                                   discrete
⮫ Chapter 21.4.5 IL_PIDType04 on page 610          2DOF (2 degree of freedom) PID-controller with
                                                   anti-reset windup integrator and delimiter, event-
                                                   controlled

⮫ Chapter 21.4.6 IL_PIType01 on page 614      PI-controller with smoothed “Feedback” input,
 analyzed control deviation, anti-reset windup
 integrator and delimiter at the output, time dis‐
 crete
⮫ Chapter 21.4.7 IL_PIType02 on page 618      PI-controller with smoothed “Feedback” input,
 analyzed control deviation, anti-reset windup
 integrator and delimiter at the output, event-
 controlled
Elements (basic elements)
⮫ Chapter 21.5.2 IL_DeadtimeType01            Dead time element (time-variable), time-discrete
on page 622

⮫ Chapter 21.5.3 IL_DeadtimeType02            Dead time element (time-variable), event-con‐
on page 625                                   trolled
⮫ Chapter 21.5.4 IL_DeviationResponseCurve    Evaluation graph
on page 628
⮫ Chapter 21.5.5 IL_DT1Type01 on page 630     Differential element with first order delay, time-
 discrete
⮫ Chapter 21.5.6 IL_DT1Type02 on page 632     Differential element with first order delay, event-
 controlled
⮫ Chapter 21.5.7 IL_PDT1Type01 on page 634    Digital filter to increase or decrease the transfer
 function starting from a certain frequency, time-
 discrete
⮫ Chapter 21.5.8 IL_PDT1Type02 on page 637    Digital filter to increase or decrease the transfer
 function starting from a certain frequency, event-
 controlled
⮫ Chapter 21.5.9 IL_PT1Type01 on page 641     First order delay element, time-discrete
⮫ Chapter 21.5.10 IL_PT1Type02 on page 643    First order delay element, event-controlled
⮫ Chapter 21.5.11 IL_TransportDelayType01     Dead time element (runtime-variable), time-dis‐
on page 645                                   crete
⮫ Chapter 21.5.12 IL_TransportDelayType02     Dead time element (runtime-variable), event-
on page 648                                   controlled
⮫ Chapter 21.5.13 IL_ValueLimit on page 651   Value limitation
⮫ Chapter 21.5.14 IL_ValueWindow on page 652 Value range check
Filters
⮫ Chapter 21.6.2 IL_FIRType01 on page 654    Digital FIR filter for high-pass, low-pass and
band-pass usage, time discrete
⮫ Chapter 21.6.3 IL_FIRType02 on page 656    Digital FIR filter for high-pass, low-pass and
band-pass usage, event-controlled
⮫ Chapter 21.6.4 IL_IIRType01 on page 659    Digital IIR filter for high-pass, low-pass and
band-pass usage, time discrete
⮫ Chapter 21.6.5 IL_IIRType02 on page 661    Digital IIR filter for high-pass, low-pass and
band-pass usage, event-controlled
⮫ Chapter 21.6.6 IL_StateVariableType01      IIR filter (Infinite Impulse Response) second
on page 663                                  order for high-pass, low-pass and band-pass use
and as band-stop filter, time discrete
⮫ Chapter 21.6.7 IL_StateVariableType02      IIR filter (Infinite Impulse Response) second
on page 665                                  order for high-pass, low-pass and band-pass use
and as band-stop filter, event-controlled
Generators
⮫ Chapter 21.7.2 IL_NoiseGeneratorType01     Pseudorandom number and noise generator,
on page 669                                  time discrete

⮫ Chapter 21.7.3 IL_NoiseGeneratorType02          Noise generator for white noise, time discrete
on page 671
⮫ Chapter 21.7.4 IL_PRBSGeneratorType01           Generator for pseudorandom binary numbers,
on page 672                                       time discrete
⮫ Chapter 21.7.5 IL_PRBSGeneratorType02         Generator for pseudorandom binary numbers,
on page 674                                     event-controlled
Signal generators (Generators/IL_Signalgenerator)
⮫ Chapter 21.7.6 IL_AngleGeneratorType01        Angle generator, time discrete
on page 676
⮫ Chapter 21.7.7 IL_AngleGeneratorType02        Angle generator, event-controlled
on page 677
⮫ Chapter 21.7.8 IL_PhaseController             Phase controller
on page 679
⮫ Chapter 21.7.9 IL_SignalGeneratorType01       Signal generator, time discrete
on page 681
⮫ Chapter 21.7.10 IL_SignalGeneratorType02      Signal generator, event-controlled
on page 685
⮫ Chapter 21.7.11 IL_AmplitudeController‐       Amplitude generator, time discrete
Type01 on page 689
⮫ Chapter 21.7.12 IL_AmplitudeController‐       Amplitude generator, event-controlled
Type02 on page 693
Statistics (Statistic function blocks)
⮫ Chapter 21.8.2 IL_HistogramType01             Sorts values into categories, time discrete
on page 698
⮫ Chapter 21.8.3 IL_HistogramType02             Sorts values into categories, event-controlled
on page 700
⮫ Chapter 21.8.4 IL_StatisticType01 on page 702 Detects floating mean value, minimum value and
maximum value, time discrete
⮫ Chapter 21.8.5 IL_StatisticType02 on page 704 Detects floating mean value, minimum value and
maximum value, event-controlled
⮫ Chapter 21.8.6 IL_SuppressionType01           Suppresses measured values with an excessive
on page 706                                     deviation to the mean value of the measured
values (1 limit), time discrete
⮫ Chapter 21.8.7 IL_SuppressionType02           Suppresses measured values with an excessive
on page 711                                     deviation to the mean value of the measured
values (1 limit), event-controlled
⮫ Chapter 21.8.8 IL_SuppressionType03           Suppresses measured values with an excessive
on page 715                                     deviation to the mean value of the measured
values (2 limits), time discrete
⮫ Chapter 21.8.9 IL_SuppressionType04           Suppresses measured values with an excessive
on page 721                                     deviation to the mean value of the measured
values (2 limits), event-controlled
Temperature controller (TemperatureController)
⮫ Chapter 21.9.2 IL_TempControl on page 727     Controller for the temperature-controlled system
with automatic online controller setting
TwoPosCtrl (two-position controller)
⮫ Chapter 21.10.1 IL_TwoPosCtrlType01           Two-position controller with hysteresis. It is suit‐
on page 740                                     able for simple controls
Utilities
IL_GetCurrentTimeUs                               Getting system time

## 21.2 Time-discrete function blocks

These function blocks compute a new value upon each call if the "Enable"
input is active. The time between two calls is measured and available at the
"ActScanTime" output. All computations refer to the cycle time measured.
Time-discrete function blocks should be called in a cyclic, or even better,
a Sercos-synchronous task. This can significantly affect the accuracy of the
output value.
The majority of function block inputs are applied immediately upon the next
call. It is thus possible to modify control parameters at runtime.
Set the "InPause” output to acknowledge an active "Pause" input. The output
values are frozen and there are no more internal computations. "ActScanTime"

is still updated when "Pause" is active.
A value at the "PresetValue" input is applied either to the "ControlValue" or to
the "OutputValue" output at a rising edge at "Preset". If applied successfully,
the "PresetAck" output becomes active. If "Preset" is active at the rising edge
at “Enable”, the value in "PresetValue" is also applied. An active Preset has a
higher priority than the "Pause" input.
Time-discrete function blocks can be directly linked to each other if all func‐
tion blocks are located within the same task. The "InOperation" output of the
preceding function block is connected to the "Enable" input of the following
function block. "InPause" is analogously transferred to "Pause" and "Output‐
Value” to "Value”. The sequence of the linkage has to be taken into account
for the sequence of the function block calls.

## 21.3 Event-controlled function blocks

These function blocks only compute one new value if the "Enable" input is
active and the value of the "Step" input changes. The last processed step
is available at the "ActStep" output. Connect the "ActStep" output of the
preceding function block to the "Step" input of the next function block to
cascade multiple event-controlled function blocks.
Inputs are only applied if the "Step" input changes. This ensures that an
already computed value cannot subsequently be modified. Thus, it can be par‐
ameterized at runtime. The "Preset" and "Pause" inputs are active irrespective
of a possible change at the “Step” input.
Set the "InPause” output to acknowledge an active "Pause" input. The output
values are frozen and there are no more internal computations. "ActStep" is
still updated when "Pause" is active.
A value at the "PresetValue" input is applied either to the "ControlValue" or to
the "OutputValue" output at a rising edge at "Preset". If applied successfully,
the "PresetAck" output becomes active. If "Preset" is active at the rising edge
at “Enable”, the value in "PresetValue" is also applied. An active Preset has a
higher priority than the "Pause" input.

Event-controlled function blocks can be linked directly to each other. The
"InOperation" output of the preceding function block is connected to the
"Enable" input of the following function block. "InPause" is analogously trans‐
ferred to "Pause", "ActStep" to "Step" and "OutputValue" to "Value”. Note the
sequence of the linkage for the sequence of the function block calls. This is
not mandatorily required as the unit of "ActStep" and "OutputValue" always
ensures a correct processing.

## 21.4 Controllers

### 21.4.1 Introduction and overview

The CXA_LoopControl provides the following controllers:
Table 487: CXA_LoopControl controller
Area of application (folder in library)
Function blocks                                      Description
Controllers
⮫ Chapter 21.4.2 IL_PIDType01 on page 598            PID-controller with anti-reset windup integrator
                                                     and delimiter, time discrete
⮫ Chapter 21.4.3 IL_PIDType02 on page 602            PID-controller with anti-reset windup integrator
                                                     and delimiter, event-controlled
⮫ Chapter 21.4.4 IL_PIDType03 on page 605            2DOF (2 degree of freedom) PID-controller with
                                                     anti-reset windup integrator and delimiter, time
                                                     discrete
⮫ Chapter 21.4.5 IL_PIDType04 on page 610            2DOF (2 degree of freedom) PID-controller with
                                                     anti-reset windup integrator and delimiter, event-
                                                     controlled
⮫ Chapter 21.4.6 IL_PIType01 on page 614             PI-controller with smoothed “Feedback” input,
                                                     analyzed control deviation, anti-reset windup
                                                     integrator and delimiter at the output, time dis‐
                                                     crete
⮫ Chapter 21.4.7 IL_PIType02 on page 618             PI-controller with smoothed “Feedback” input,
                                                     analyzed control deviation, anti-reset windup
                                                     integrator and delimiter at the output, event-
                                                     controlled

### 21.4.2 IL_PIDType01

Brief description
The PID-controller contains an anti-reset windup integrator and a delimiter at
the output. A preset value can also be set and the controller can be paused.
In this case, the controller output remains constant.

The PID-controller function block is to be called cyclically. As it is imple‐
mented as digital controller, there can be a significant effect on the accuracy
of the controller. The function block measures the time between the calls
(sampling time) and computes all controller parameters if the sampling time
deviates substantially or if the controller parameters change. The measured
sampling time is also available as output.

Interface description

Table 488: Interface variables of the IL_PIDType01 function block
              Name           Type             Comment
VAR_INPUT     Enable         BOOL             If TRUE, "ControlValue" is either set to the preset
                                              value of "PresetValue" (if there is a rising edge at
                                              "Preset") or to the computed value
              Pause          BOOL             If TRUE, the controller does not change the value of
                                              "ControlValue”.
              Preset         BOOL             At a rising edge at this input, the controller output is
                                              set to the parameterizable value in "PresetValue"
              Setpoint       LREAL            The requested "command value" for the controlled
                                              process
              Feedback       LREAL            The current actual process value
              Preset‐        LREAL            Preset value indicated at "ControlValue" at a rising
              Value                           edge at "Preset"
              HighLimit      LREAL            Upper limit of "ControlValue"
                                              If "ControlValue" exceeds this value, it is limited to
                                              this value
              LowLimit       LREAL            Lower limit of "ControlValue"
                                              If "ControlValue" falls below this value, it is limited to
                                              this value
              PControl       LREAL            Proportional value for the gaining value of the con‐
                                              troller.
              IControl       LTIME            Integration time "Tn" for the integration value of the
                                              controller.
              DControl       LTIME            Differential time "Tv" for the differential value of the
                                              controller
VAR_OUTPUT InOpera‐          BOOL             If TRUE, the PID-controller operates and the "Control‐
           tion                               Value" controller output is valid.
           Error             BOOL             Indicates that an error occurred in the function block

Name       Type          Comment
ErrorID    ⮫ ERROR_CODE  Error ID
ErrorIdent ⮫ ERROR_STRUC For the error structure with further error classification,
           T             see ⮫ Error codes on page 602
InPause    BOOL          "Pause" is active and the value at "ControlValue” is
                         frozen
PresetAck BOOL           Value applied at "PresetValue"
ActScan‐   LTIME         The time passed since the latest function block call
Time
HighLimi‐ BOOL           "ControlValue" reached upper limit
tAct
LowLimi‐ BOOL            "ControlValue" reached lower limit
tAct
Control‐   LREAL         Computed controller output value
Value

Table 489: Min./max. and default values of the IL_PIDType01 inputs
Name               Type            Min. value       Max. value   Default value    Applied
Enable             BOOL                                          FALSE            Continuous
Pause              BOOL                                          FALSE            Continuous
Preset             BOOL                                          FALSE            Continuous
Setpoint           LREAL           N. def.          N. def.      0.0              Continuous
Feedback           LREAL           N. def.          N. def.      0.0              Continuous
PresetValue        LREAL           N. def.          N. def.      0.0              Rising edge at "Preset"
HighLimit          LREAL           LowLimit         N. def.      0.0              Continuous
LowLimit           LREAL           N. def.          HighLimit    0.0              Continuous
PControl           LREAL           N. def.          N. def.      0.0              Continuous
IControl           LTIME           0s               n. def.      0s               Continuous
DControl           LTIME           0s               n. def.      0s               Continuous

      PID-controller configuration
      For the requested P-, I-, PI-, PD- or PID-response, assign the corresponding
      values for the "PControl", "IControl" and "DControl" inputs. The controller
      parameters can be changed “on-the-fly". Thus, the values are immediately
      applied when the controller is switched on. Use the following table to create
      the required control algorithm.
      A specific configuration is created if all three values for "PControl", "IControl"
      and "DControl" are set to 0. In this case, the controller is switched off (no
      P-, I- and D-value) and the "ControlValue" output is fixedly set to 0. However,
      the functionality for "Preset" and "Pause" remains. Thus, other values can be
      forced at the output using these inputs.

      Table 490: Configuration options of the PID-controller
      Controller type        PControl          IControl             DControl
      Switched off           0.0               0s                   0s
      P-controller           Valid value       0s                   0s
      I-controller           0.0               Valid value          0s
      PI-controller          Valid value       Valid value          0s
      PD-controller          Valid value       0s                   Valid value
      PID-controller         Valid value       Valid value          Valid value

The control algorithm can be displayed as the following block diagram:

Functional Description
Initialization
During the first action of the function block, the variables xd,k, xd,k-1, xd,k-2, yk
and yk-1 are initialized with the value "PresetValue". During the initialization,
assign valid values to the inputs "Setpoint" and "Feedback".
Preset value
For a trouble-free start of the controller output "ControlValue", set the
"Preset" input when "Enable" is activated. In this case, the PID-controller sets
the values

and

During this time, valid values have to be assigned to the inputs "Setpoint" and
"Feedback".
Checking upper/lower limit values is also still active to ensure that the "Con‐
trolValue" is limited if the preset value ("PresetValue") is beyond the limits of
"HighLimit" or "LowLimit".
"PresetAck" becomes TRUE when the value is applied at "PresetValue".
"Preset" has a higher priority than the "Pause" input.
Pause
The "Pause" input is only analyzed when the "Enable" input is active. In this
case, the control deviation ("Setpoint" – "Feedback") is set to 0. Thus, the
"ControlValue" is fixedly specified. It can be used for a constant and stable
output.
The "InPause" output is set when "Pause" is active.
The "ActScanTime" output is still updated.
Normal mode
If "ControlValue" exceeds or falls below the value of "HighLimit" or "Low‐
Limit", "ControlValue" is limited to the respective value. If the control has
an integration part, an Anti-Reset-Windup is executed additionally. Thus, the
integral value is not added up further. In this case, the "HighLimitAct" and
"LowLimitAct" outputs are set.
The controller coefficients are recomputed if controller parameters or sam‐
pling time change. Thus, the user can fine-tune by adjusting the controller
parameters. The sampling time is measured each time the function block is
called. If the sampling time deviates by more than 20% from the first one
measured, it is assumed that the sampling time changed and all coefficients
are recomputed. Use the function block only in a cyclic task, as the computa‐
tions are time-consuming.

Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:
Table 491: Generated error numbers of the IL_PIDType01 function block
ErrorID                             Additional1 Additional2 Description
INPUT_INVALID_ERROR                 16#0A0F0104 16#0C230001 "LowLimit" input value is greater than
                                                            the "HighLimit" input value
INPUT_INVALID_ERROR                 16#0A0F0104 16#0C230002 Controller type selection is not sup‐
                                                            ported. Check inputs for "PControl",
                                                            "IControl" and "DControl".
INPUT_RANGE_ERROR                   16#0A0F0104 16#0C230003 The "DControl" input is invalid.
INPUT_RANGE_ERROR                   16#0A0F0104 16#0C230004 The "IControl" input is invalid.
RESOURCE_ERROR                      16#0A0F0104 16#0C230005 Scan time is invalid for 5 cycles
STATE_MACHINE_ERROR                 16#0A0F0104 16#0C231000 Runtime error in function block:
                                                            Invalid state of the state machine.

### 21.4.3 IL_PIDType02

Brief description
The PID-controller contains an anti-reset windup integrator and a delimiter at
the output. A preset value can also be set and the controller can be paused.
In this case, the controller output remains constant.
The PID-controller function block is to be called cyclically. Only computed
if the value changes at the “Step” input. Keep the increment as constant as
possible. The last processed step is also available as output.

Interface description

Table 492: Interface variables of the IL_PIDType02 function block
                   Name         Type               Comment
VAR_INPUT          Enable       BOOL               If TRUE, "ControlValue" is either set to the preset
                                                   value of "PresetValue" (if there is a rising edge at
                                                   "Preset") or to the computed value.
                   Pause        BOOL               If TRUE, the controller does not change the value of
                                                   "ControlValue”.
                   Preset       BOOL               At a rising edge at this input, the controller output is
                                                   set to the parameterizable value in "PresetValue"

Name           Type   Comment
Step           UINT   Processing step
Setpoint       LREAL  The requested "command value" for the controlled
process
Feedback LREAL           The current actual process value
Preset‐    LREAL         Preset value displayed as "ControlValue" in case of a
Value                    rising edge at "Preset"
HighLimit LREAL          Upper limit of "ControlValue"
If "ControlValue" exceeds this value, it is limited to
this value

LowLimit LREAL           Lower limit of "ControlValue"
If "ControlValue" falls below this value, it is limited to
this value
PControl LREAL           Proportional value for the gaining value of the con‐
troller
IControl   LREAL         Integration constant Tn for the integration value of the
controller
DControl LREAL           Differential constant Tv for the differential value of the
controller
VAR_OUTPUT InOpera‐   BOOL          If TRUE, the PID-controller operates and the "Control‐
tion                     Value" controller output is valid
Error      BOOL          Indicates that an error occurred in the function block
ErrorID    ⮫ ERROR_CODE Error ID
ErrorIdent ⮫ ERROR_STRUC For the error structure with further error classification,
T             see ⮫ Error codes on page 605
InPause    BOOL          "Pause" is active and the value at "ControlValue” is
frozen
PresetAck BOOL           Value applied at "PresetValue"
ActStep    UINT          Last processed step
HighLimi‐ BOOL           "ControlValue" reached upper limit
tAct
LowLimi‐ BOOL            "ControlValue" reached lower limit
tAct
Control‐   LREAL         Computed controller output value
Value

Table 493: Min./max. and default values of the IL_PIDType02 inputs
Name           Type             Min. value   Max. value   Default value    Applied
Enable         BOOL                                       FALSE            Continuous
Pause          BOOL                                       FALSE            Continuous
Preset         BOOL                                       FALSE            Continuous
Step           UINT             0            65335        0                Continuous
Setpoint       LREAL            N. def.      N. def.      0.0              Continuous
Feedback       LREAL            N. def.      N. def.      0.0              Continuous
PresetValue    LREAL            N. def.      N. def.      0.0              Rising edge at "Preset"
HighLimit      LREAL            LowLimit     N. def.      0.0              Continuous
LowLimit       LREAL            N. def.      HighLimit    0.0              Continuous
PControl       LREAL            N. def.      N. def.      0.0              Continuous
IControl       LREAL            0.0          n. def.      0.0              Continuous

Name               Type           Min. value       Max. value     Default value Applied
DControl           LREAL          0.0              n. def.        0.0           Continuous

PID-controller configuration
For the requested P-, I-, PI-, PD- or PID-response, assign the corresponding
values for the "PControl", "IControl" and "DControl" inputs. The controller
parameters can be changed “on-the-fly". Thus, the values are immediately
applied when the controller is switched on. Use the following table to create
the required control algorithm.
A specific configuration is created if all three values for "PControl", "IControl"
and "DControl" are set to 0. In this case, the controller is switched off (no
P-, I- and D-value) and the "ControlValue" output is fixedly set to 0. However,
the functionality for "Preset" and "Pause" remains. Thus, other values can be
forced at the output using these inputs.

Table 494: Configuration options of the PID-controller
Controller type        PControl           IControl              DControl
Switched off           0.0                0.0                   0.0
P-controller           Valid value        0.0                   0.0
I-controller           0.0                Valid value           0.0
PI-controller          Valid value        Valid value           0.0
PD-controller          Valid value        0.0                   Valid value
PID-controller         Valid value        Valid value           Valid value

The control algorithm can be displayed as the following block diagram:

Functional Description
Initialization
During the first action of the function block, the variables xd,k, xd,k-1, xd,k-2, yk
and yk-1 are initialized with the value "PresetValue". During the initialization,
assign valid values to the inputs "Setpoint" and "Feedback".
Preset value
For a trouble-free start of the controller output ("ControlValue”), set the
"Preset" input when "Enable" is enabled. In this case, the PID-controller sets
the values

and
              .
During this time, valid values have to be assigned to the inputs "Setpoint" and
"Feedback".

Checking upper/lower limit values is also still active to ensure that the "Con‐
trolValue" is limited if the preset value ("PresetValue") is beyond the limits of
"HighLimit" or "LowLimit".
"PresetAck" becomes TRUE when the value is applied at "PresetValue".
"Preset" has a higher priority than the "Pause" input.
Pause
The "Pause" input is only analyzed when the "Enable" input is active. In this
case, the control deviation ("Setpoint" – "Feedback") is set to 0. Thus, the
"ControlValue" is fixedly specified. It can be used for a constant and stable
output.
The "InPause" output is set when "Pause" is active.

The "ActStep" output is still updated.
Normal mode
"ControlValue" is only computed if the "Step" input changes.
If "ControlValue" exceeds or falls below the value of "HighLimit" or "Low‐
Limit", "ControlValue" is limited to the respective value. If the control has
an integration part, an Anti-Reset-Windup is executed additionally. Thus, the
integral value is not added up further. In this case, the "HighLimitAct" and
"LowLimitAct" outputs are set.
The controller coefficients are recomputed if either the controller parameters
or the increment change. Thus, the user can fine-tune by adjusting the con‐
troller parameters. The increment is measured each time the "Step" input
changes. If the increment deviates by more than 20% from the first one meas‐
ured, all coefficients are recomputed. The function block should only be used
in a cyclic task, as the calculations are time-consuming.

Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:
Table 495: Generated error numbers of the IL_PIDType02 function block
ErrorID                       Additional1 Additional2 Description
INPUT_INVALID_ERROR           16#0A0F0104 16#0C230001 "LowLimit" input value is greater than
                                                      the "HighLimit" input value
INPUT_INVALID_ERROR           16#0A0F0104 16#0C230002 Controller type selection is not sup‐
                                                      ported. Check inputs for "PControl",
                                                      "IControl" and "DControl".
INPUT_RANGE_ERROR             16#0A0F0104 16#0C230003 The "DControl" input is invalid.
INPUT_RANGE_ERROR             16#0A0F0104 16#0C230004 The "IControl" input is invalid.
RESOURCE_ERROR                16#0A0F0104 16#0C230005 Scan time is invalid for 5 cycles.
STATE_MACHINE_ERROR           16#0A0F0104 16#0C230001 Runtime error in function block:
                                                      Invalid state of the state machine.

### 21.4.4 IL_PIDType03

Brief description
IL_PIDType03 is the 2DOF (2 degree of freedom) PID-controller.
The control difference is created separately for the proportional, integral and
differential value.
The command values for the proportional and differential value are each
scaled with the entered scaling factors "bControl" and "cControl". Thus,
disturbance and reference variable responses are individually specified. The
values "bControl" and "cControl" can be set from 0 to 1.

        If both (bControl and cControl) are set to "1.0", the controller responds like a
        classic 1DOF PID-controller (same response as IL_PIDType01).
        The controllers also contain an anti-reset windup integrator and a delimiter at
        the output. A preset value can also be set and the controller can be paused.
        In this case, the controller output remains constant.
        The PID-controller function block is to be called cyclically. As it is imple‐
        mented as digital controller, there can be a significant effect on the accuracy
        of the controller.
        The function block measures the time between the calls (scanning time) and
        calculates all controller parameters if the scanning time deviates substantially
        or if the controller parameters change. The measured sampling time is also
        available as output.
        The properties "PCorr", "ICorr" and "DCorr” can read the control coefficients
        (P-value, I-value and D-value).

        Interface description

Table 496: Interface variables of the IL_PIDType03 function block
                   Name         Type               Comment
VAR_INPUT          Enable       BOOL               If TRUE, "ControlValue" is either set to the preset
                                                   value of "PresetValue" (if there is a rising edge at
                                                   "Preset") or to the computed value
                   Pause        BOOL               If TRUE, the controller does not change the value of
                                                   "ControlValue”.
                   Preset       BOOL               At a rising edge at this input, the controller output is
                                                   set to the parameterizable value in "PresetValue"
                   Setpoint     LREAL              The requested "command value" for the controlled
                                                   process
                   Feedback     LREAL              The current actual process value
                   Preset‐      LREAL              Preset value indicated at "ControlValue" at a rising
                   Value                           edge at "Preset"
                   HighLimit    LREAL              Upper limit of "ControlValue"
                                                   If "ControlValue" exceeds this value, it is limited to
                                                   this value
                   LowLimit     LREAL              Lower limit of "ControlValue"
                                                   If "ControlValue" falls below this value, it is limited to
                                                   this value

Name           Type   Comment
PControl       LREAL  Proportional value for the gaining value of the con‐
               troller
IControl   LTIME         The integration time "Tn" for the integration value of
               the controller
DControl LTIME           Differential time "Tv" for the differential value of the
               controller
bControl LREAL           Scaling factor for P-value
cControl   LREAL         Scaling factor for D-value
VAR_OUTPUT InOpera‐   BOOL          If TRUE, the PID-controller operates and the "Control‐
tion                     Value" controller output is valid

Error      BOOL          Indicates that an error occurred in the function block
ErrorID    ⮫ ERROR_CODE Error ID
ErrorIdent ⮫ ERROR_STRUC For the error structure with further error classification,
 T             see ⮫ Error codes on page 609
InPause    BOOL          "Pause" is active and the value at "ControlValue” is
               frozen.
PresetAck BOOL           Value applied at "PresetValue”.
ActScan‐   LTIME         The time elapsed since the latest function block call.
Time
HighLimi‐ BOOL           "ControlValue" reached upper limit
tAct
LowLimi‐ BOOL            "ControlValue" reached lower limit
tAct
Control‐   LREAL         Computed controller output value
Value

Table 497: Min./max. and default values of the IL_PIDType03 inputs
Name           Type             Min. value   Max. value    Default value   Applied
Enable         BOOL                                        FALSE           Continuous
Pause          BOOL                                        FALSE           Continuous
Preset         BOOL                                        FALSE           Continuous
Setpoint       LREAL            N. def.      N. def.       0.0             Continuous
Feedback       LREAL            N. def.      N. def.       0.0             Continuous
PresetValue    LREAL            N. def.      N. def.       0.0             Rising edge at "Preset"
HighLimit      LREAL            LowLimit     N. def.       0.0             Continuous
LowLimit       LREAL            N. def.      HighLimit     0.0             Continuous
PControl       LREAL            N. def.      N. def.       0.0             Continuous
IControl       LTIME            0s           n. def.       0s              Continuous
DControl       LTIME            0s           n. def.       0s              Continuous
bControl       LREAL            0            1             1               Continuous
cControl       LREAL            0            1             1               Continuous

PID-controller configuration
For the requested P-, I-, PI-, PD- or PID-response, assign the corresponding
values for the "PControl", "IControl" and "DControl" inputs. The controller
parameters can be changed “on-the-fly". Thus, the values are immediately
applied when the controller is switched on. Use the following table to create
the required control algorithm.

A specific configuration is created if all three values for "PControl", "IControl"
and "DControl" are set to 0. In this case, the controller is switched off (no
P-, I- and D-value) and the "ControlValue" output is fixedly set to 0. However,
the functionality for "Preset" and "Pause" remains. Thus, other values can be
forced at the output using these inputs.

Table 498: Configuration options of the PID-controller
Controller type     PControl             IControl            DControl
Switched off        0.0                  0s                  0s
P-controller        Valid value          0s                  0s
I-controller        0.0                  Valid value         0s
PI-controller       Valid value          Valid value         0s
PD-controller       Valid value          0s                  Valid value
PID-controller      Valid value          Valid value         Valid value

The control algorithm can be displayed as the following block diagram:

Functional Description
Initialization
During the initialization, assign valid values to the inputs "Setpoint" and
"Feedback". If the "Preset" input is set to TRUE, the "ControlValue" output is
initialized with the "PresetValue" input. Otherwise, the "ControlValue" output
is initialized with "0".
Preset value
For a trouble-free start of the controller output "ControlValue", the "Preset"
input has to be set if "Enable" is activated. In this case, the "ControlValue"
applies the "PresetValue". During this time, valid values have to be assigned
to the inputs "Setpoint" and "Feedback".
Checking upper/lower limit values is also still active to ensure that the "Con‐
trolValue" is limited if the preset value ("PresetValue") is beyond the limits of
"HighLimit" or "LowLimit".
"PresetAck" becomes TRUE when the value is applied at "PresetValue".
"Preset" has a higher priority than the "Pause" input.
Pause
The "Pause" input is only evaluated when the "Enable" input is active. "Con‐
trolValue" is fixedly specified in this case. It can be used to keep the output
constant stable.
The "InPause" output is set when "Pause" is active.
The "ActScanTime" output is still updated.
Normal mode

If "ControlValue" exceeds or falls below the value of "HighLimit" or "Low‐
Limit", "ControlValue" is limited to the respective value. In this case, the
"HighLimitAct" and "LowLimitAct" outputs are set. If the control has an inte‐
gration part, an Anti-Reset-Windup is executed additionally. Thus, the integral
value is not added up further
The controller coefficients are recomputed if controller parameters or sam‐
pling time change. Thus, the user can fine-tune by adjusting the controller
parameters. The sampling time is measured each time the function block is
called. If the sampling time deviates by more than 20% from the first one
measured, it is assumed that the sampling time changed and all coefficients
are recomputed. The function block should only be used in a cyclic task, as
the calculations are time-consuming.

Example of the "bControl" selection
The following figure shows the step response of a PI-controller with a different
"bControl".
The reference behavior of the PI-controller can be changed using "bControl":

Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:
Table 499: Generated error numbers of the IL_PIDType03 function block
ErrorID                       Additional1 Additional2 Description
INPUT_INVALID_ERROR           16#0A0F0104 16#0C230001 "LowLimit" input value is greater than
                                                      the "HighLimit" input value
INPUT_INVALID_ERROR           16#0A0F0104 16#0C230002 Controller type selection is not sup‐
                                                      ported. Check inputs for "PControl",
                                                      "IControl" and "DControl".
INPUT_RANGE_ERROR             16#0A0F0104 16#0C230003 The "DControl" input is invalid
INPUT_RANGE_ERROR             16#0A0F0104 16#0C230004 The "IControl" input is invalid
RESOURCE_ERROR                16#0A0F0104 16#0C230005 Scan time is invalid for 5 cycles.
STATE_MACHINE_ERROR           16#0A0F0104 16#0C231000 Runtime error in function block:
                                                      Invalid state of the state machine.
INPUT_INVALID_ERROR           16#0A0F0104 16#0C230006 The "bControl" input is invalid
INPUT_INVALID_ERROR           16#0A0F0104 16#0C230007 The "cControl" input is invalid

### 21.4.5 IL_PIDType04

        Brief description
        IL_PIDType04 is the 2DOF (2 degree of freedom) PID-controller.
        The control difference is created separately for the proportional, integral and
        differential value of the controller.
        For the proportional and differential value, the command values are individu‐
        ally scaled by the factors "bControl" and "cControl". Thus, disturbance and
        reference variable responses are individually specified. The values "bControl"
        and "cControl" can be set from 0 to 1. If both (bControl and cControl) are
        set to "1.0", the controller responds like a classic 1DOF PID-controller (same
        response as IL_PIDType02).
        The controllers also contain an anti-reset windup integrator and a delimiter at
        the output. A preset value can also be set and the controller can be paused.
        In this case, the controller output remains constant.
        IL_PIDType04 is a step-dependent controller. The PID-controller function
        block has to be called cyclically. Only computed if the value changes at the
        “Step” input. Keep the increment as constant as possible. The last processed
        step is also available as output.
        The controller coefficients are recomputed if controller parameters or sam‐
        pling time change.

        Interface description

Table 500: Interface variables of the IL_PIDType02 function block
                   Name         Type               Comment
VAR_INPUT          Enable       BOOL               If TRUE, "ControlValue" is either set to the preset
                                                   value of "PresetValue" (if there is a rising edge at
                                                   "Preset") or to the computed value.
                   Pause        BOOL               If TRUE, the controller does not change the value of
                                                   "ControlValue”.
                   Preset       BOOL               At a rising edge at this input, the controller output is
                                                   set to the parameterizable value in "PresetValue”.
                   Step         UINT               Processing step
                   Setpoint     LREAL              The requested "command value" for the controlled
                                                   process.
                   Feedback     LREAL              The current actual value of the process.

Name           Type   Comment
Preset‐        LREAL  Preset value displayed as "ControlValue” if there is a
Value                 rising edge at "Preset".
HighLimit
LREAL         Upper limit for "ControlValue".
If "ControlValue" exceeds this value, it is limited to
this value.
LowLimit LREAL           Lower limit of "ControlValue".
If "ControlValue” falls below this value, it is limited to
this value.
PControl LREAL           Proportional value for the gaining value of the con‐
troller.

IControl   LREAL         Integration constant "Tn" for the integration value of
the controller.
DControl LREAL           Differential constant "Tv" for the differential value of
the controller.
bControl LREAL           Scaling factor for P-value.
cControl   LREAL         Scaling factor for D-value.
VAR_OUTPUT InOpera‐   BOOL          If TRUE, the PID-controller operates and the "Control‐
tion                     Value" controller output is valid.
Error      BOOL          Indicates that an error occurred in the function block.
ErrorID    ⮫ ERROR_CODE Error ID
ErrorIdent ⮫ ERROR_STRUC For the error structure with further error classification,
T             see ⮫ Error codes on page 613
InPause    BOOL          "Pause" is active and the value at "ControlValue” is
frozen.
PresetAck BOOL           Value applied at "PresetValue”.
ActStep    UINT          Last processed step.
HighLimi‐ BOOL           "ControlValue" reached upper limit
tAct
LowLimi‐ BOOL            "ControlValue" reached lower limit
tAct
Control‐   LREAL         Computed controller output value
Value

Table 501: Min./max. and default values of the IL_PIDType04 inputs
Name           Type             Min. value   Max. value   Default value    Applied
Enable         BOOL                                       FALSE            Continuous
Pause          BOOL                                       FALSE            Continuous
Preset         BOOL                                       FALSE            Continuous
Step           UINT             0            65335        0                Continuous
Setpoint       LREAL            N. def.      N. def.      0.0              Continuous
Feedback       LREAL            N. def.      N. def.      0.0              Continuous
PresetValue    LREAL            N. def.      N. def.      0.0              Rising edge at "Preset"
HighLimit      LREAL            LowLimit     N. def.      0.0              Continuous
LowLimit       LREAL            N. def.      HighLimit    0.0              Continuous
PControl       LREAL            N. def.      N. def.      0.0              Continuous
IControl       LREAL            0.0          n. def.      0.0              Continuous
DControl       LREAL            0.0          n. def.      0.0              Continuous
bControl       LREAL            0.0          1.0          1.0              Continuous

Name               Type           Min. value       Max. value   Default value Applied
cControl           LREAL          0.0              1.0          1.0           Continuous

PID-controller configuration
For the requested P-, I-, PI-, PD- or PID-response, assign the corresponding
values for the "PControl", "IControl" and "DControl" inputs. The controller
parameters can be changed “on-the-fly". Thus, the values are immediately
applied when the controller is switched on. The following table can be used
to create the required control algorithm.
There is a special configuration if all the three values for "PControl", "ICon‐
trol" and "DControl" are set to "0". In this case, the controller is switched
off (no P-, I- and D-value) and the "ControlValue" output is fixedly set to
0. However, the functionality for "Preset" and "Pause" remains. Thus, other
values can be forced at the output using these inputs.

Table 502: Configuration options of the PID-controller
Controller type        PControl          IControl            DControl
Switched off           0.0               0.0                 0.0
P-controller           Valid value       0.0                 0.0
I-controller           0.0               Valid value         0.0
PI-controller          Valid value       Valid value         0.0
PD-controller          Valid value       0.0                 Valid value
PID-controller         Valid value       Valid value         Valid value

The control algorithm can be displayed as the following block diagram:

Functional Description
Initialization

During the initialization, assign valid values to the inputs "Setpoint" and
"Feedback". If the "Preset" input is set to TRUE, the "ControlValue" output is
initialized with the "PresetValue" input. Otherwise, the "ControlValue" output
is initialized with "0".
Preset value
For a trouble-free start of the controller output "ControlValue", the "Preset"
input has to be set if "Enable" is activated. In this case, the "ControlValue"
applies the "PresetValue". During this time, valid values have to be assigned
to the inputs "Setpoint" and "Feedback". Checking upper/lower limit values is
also still active to ensure that the "ControlValue" is limited if the preset value
("PresetValue") is beyond the limits of "HighLimit" or "LowLimit".
"PresetAck" becomes TRUE when the value is applied at "PresetValue".
"Preset" has a higher priority than the "Pause" input.

Pause
The "Pause" input is only evaluated when the "Enable" input is active. "Con‐
trolValue" is fixedly specified in this case. It can be used to keep the output
constant stable. While pausing, the control coefficients are internally updated.
The "InPause" output is set when "Pause" is active.
The "ActStep" output is still updated.
Normal mode
"ControlValue" is only computed if the "Step" input changes. If "ControlValue"
exceeds or falls below the value of "HighLimit" or "LowLimit", "ControlValue"
is limited to the respective value. If the control has an integration part, an
Anti-Reset-Windup is executed additionally. Thus, the integral value is not

added up further. In this case, the "HighLimitAct" and "LowLimitAct" outputs
are set.
The controller coefficients are recomputed if either the controller parameters
or the increment change. Thus, the user can fine-tune by adjusting the con‐
troller parameters. The increment is measured each time the "Step" input
changes.

Example of the "bControl" selection
The following figure shows the step response of a PI-controller with a different
"bControl".
The reference behavior of the PI-controller can be changed using "bControl":

Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:
Table 503: Generated error numbers of the IL_PIDType04 function block
ErrorID                       Additional1 Additional2 Description
INPUT_INVALID_ERROR           16#0A0F0104 16#0C230001 "LowLimit" input value is greater than
                                                      the "HighLimit" input value
INPUT_INVALID_ERROR           16#0A0F0104 16#0C230002 Controller type selection is not sup‐
                                                      ported. Check inputs for "PControl",
                                                      "IControl" and "DControl".
INPUT_RANGE_ERROR             16#0A0F0104 16#0C230003 The "DControl" input is invalid
INPUT_RANGE_ERROR             16#0A0F0104 16#0C230004 The "IControl" input is invalid

ErrorID                             Additional1 Additional2 Description
RESOURCE_ERROR                      16#0A0F0104 16#0C230005 Scan time is invalid for 5 cycles.
STATE_MACHINE_ERROR                 16#0A0F0104 16#0C231000 Runtime error in function block:
                                         Invalid state of the state machine.
INPUT_INVALID_ERROR                 16#0A0F0104 16#0C230006 The "bControl" input is invalid
INPUT_INVALID_ERROR                 16#0A0F0104 16#0C230007 The "cControl" input is invalid

### 21.4.6 IL_PIType01

        Brief description
        The PI-controller contains an anti-reset windup integrator and a delimiter at
        the output. An adjustable PT1-element filters the actual value input. The dif‐
        ference between the command value and the actual value is analyzed by a
        command value curve (setpoint curve). A preset value can also be set and the
        controller can be paused. In this case, the controller output remains constant.
        The PI-controller function block should be called cyclically. As it is imple‐
        mented as digital controller, there can be a significant effect on the accuracy
        of the controller. The function block measures the time between the calls
        (scanning time) and calculates all controller parameters if the scanning time
        deviates substantially or if the controller parameters change. The measured
        sampling time is available as output.

        Interface description

Table 504: Interface variables of the IL_PIType01 function block
                   Name         Type               Comment
VAR_INPUT          Enable       BOOL               If TRUE, "ControlValue" is either set to the preset
                                                   value of "PresetValue" (if a rising edge is set at
                                                   "Preset") or to the computed value.
                   Pause        BOOL               If TRUE, the controller does not change the value of
                                                   "ControlValue”.
                   Preset       BOOL               At a rising edge at this input, the controller output is
                                                   set to the parameterizable value in "PresetValue”.
                   Setpoint     LREAL              The requested command or reference value for the
                                                   controlled process.
                   Feedback     LREAL              The current actual value of the process.
                   Preset‐      LREAL              Preset value indicated at "ControlValue" at a rising
                   Value                           edge at "Preset”.

Name           Type            Comment
HighLimit      LREAL           Upper limit for "ControlValue".
If "ControlValue" exceeds this value, it is limited to
this value.
LowLimit       LREAL           Lower limit of "ControlValue".
If "ControlValue” falls below this value, it is limited to
this value.
PControl       LREAL           Proportional value for the gaining value of the con‐
troller.
IControl       LTIME           Integration time "Tn" for the integration value of the
controller.

Feed‐     LTIME                   PT1 element filter time constant smoothing the actual
backTCon‐                         value input "Feedback".
trol
Response‐ ARRAY[0..3] OF          Command value curve to analyze the difference
Curve     ⮫ IL_COORD_TY           between the smoothed "Feedback" actual value and
PE01                    the "Setpoint" value.
VAR_OUTPUT InOpera‐  BOOL                    If TRUE, the PI-controller operates and the "Control‐
tion                              Value" controller output is valid
Error     BOOL                    Indicates that an error occurred in the function block
ErrorID   ⮫ ERROR_CODE            Error ID
ErrorIdent ⮫ ERROR_STRUC For the error structure with further error classification,
T             see ⮫ Error codes on page 617
InPause    BOOL          "Pause" is active and the value at "ControlValue” is
frozen.
PresetAck BOOL           Value at "PresetValue" was applied
ActScan‐   LTIME         The time passed since the latest function block call
Time
HighLimi‐ BOOL           "ControlValue" reached upper limit
tAct
LowLimi‐ BOOL            "ControlValue" reached lower limit
tAct
Control‐   LREAL         Computed controller output value
Value

Table 505: Min./max. and default values of the IL_PIType01 inputs
Name           Type             Min. value    Max. value      Default value   Applied
Enable         BOOL                                           FALSE           Continuous
Pause          BOOL                                           FALSE           Continuous
Preset         BOOL                                           FALSE           Continuous
Setpoint       LREAL            N. def.       N. def.         0.0             Continuous
Feedback       LREAL            N. def.       N. def.         0.0             Continuous
PresetValue    LREAL            N. def.       N. def.         0.0             Rising edge at Preset
HighLimit      LREAL            LowLimit      N. def.         0.0             Continuous
LowLimit       LREAL            N. def.       HighLimit       0.0             Continuous
PControl       LREAL            N. def.       N. def.         0.0             Continuous
IControl       LTIME            0s            n. def.         0s              Continuous
FeedbackT‐     LTIME            0s            n. def.         0s              Continuous
Control

Name               Type        Min. value          Max. value     Default value Applied
Response‐          ARRAY[0..3]                                    0             Rising edge at Enable
Curve              OF
IL_COORD_TY
PE01

Controller configuration
The signal at the "Feedback" input is smoothed by a first order delay element.
The respective filter time constant is set via "FeedbackTControl". If "Feed‐
backTControl" is 0 s, the filter is disabled. The difference signal from filtered
"Feedback" input and "Setpoint" is scaled by a characteristic curve given in
"ResponseCurve". The characteristic curve is point-symmetrical to the origin.
The x-values of the characteristic curve correspond to the differential signal.
The y-values correspond to the scaled difference signal. Up to four points
can be specified. The sections between the points are linearly interpolated. If
“ResponseCurve” is not created, there is no scaling.
For the requested P-, I-, PI-response, assign the corresponding values for the
"PControl" and "IControl" inputs. The control parameters can be changed "on
the fly". Thus, the values are immediately applied if the controller is switched
on. The following table can be used to create the required control algorithm.
0 is an invalid value, all other values are valid.
A specific configuration is produced if all three values for "PControl" and
"IControl" are set to 0 or 0 s. In this case, the controller is switched off (no
P-value and I-value) and the "ControlValue" output is fixedly set to 0. However,
the functionality for "Preset" and "Pause" remains. Thus, other values can be
forced at the output using these inputs.

Table 506: PI-controller configuration options
Controller type             PControl                    IControl
Switched off                0.0                         0s
P-controller                Valid value                 0s
I-controller                0.0                         Valid value
PI-controller               Valid value                 Valid value

The control algorithm can be displayed as the following block diagram:

Functional description
Initialization
During the first function block execution, the variables xd,k, xd,k-1, xd,k-2, yk and
yk-1 are initialized with the value "PresetValue". During the initialization, the
inputs "Setpoint" and "Feedback" have to have valid data.

If there is a rising edge at "Enable“, the delay element is initialized with the
value set at “Feedback”. Thus, "Feedback" is displayed immediately at the
outputs of the delay element.
Preset value
For a trouble-free start of the controller output "ControlValue", the "Preset"
input has to be set if "Enable" is activated. In this case, the internal inte‐
grators are initialized to the difference between "Setpoint" and "Feedback"
scaled by "ResponseCurve". The results is shown immediately at "Control‐
Value"
During this time, the inputs "Setpoint" and "Feedback" have to have valid
data.

Checking upper/lower limit values is also still active to ensure that the "Con‐
trolValue" is limited if the preset value "PresetValue" is beyond the limits of
"HighLimit" or "LowLimit".
"PresetAck" becomes TRUE when the value is applied at "PresetValue".
"Preset" has a higher priority than the "Pause" input.
Pause
The "Pause" input is only evaluated when the "Enable" input is active. In
this case, the control deviation ("Setpoint" – scaled "Feedback") is set to 0.
Thus, the "ControlValue" is fixedly specified. It can be used for a constant and
stable output.
The "InPause" output is set when "Pause" is active.
The "ActScanTime" output is still updated.
Normal mode
If "ControlValue" exceeds or falls below the value of "HighLimit" or "Low‐
Limit", "ControlValue" is limited to the respective value. If the control has
an integration part, an Anti-Reset-Windup is executed additionally. Thus, the
integral value is not added up further. In this case, the "HighLimitAct" and
"LowLimitAct" outputs are set.
The controller coefficients are recomputed if controller parameters or sam‐
pling time change. Thus, the user can fine-tune by adjusting the controller
parameters. The sampling time is measured each time the function block is
called. If the sampling time deviates by more than 20% from the first one
measured, it is assumed that the sampling time changed and all coefficients
are recomputed. Use the function block only in a cyclic task, as the computa‐
tions are time-consuming.

Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:
Table 507: Generated error numbers of the IL_PIType01 function block
ErrorID                       Additional1 Additional2 Description
INPUT_INVALID_ERROR           16#0A0F0104 16#0C230001 "LowLimit" input value is greater than
                                                      the "HighLimit" input value
INPUT_INVALID_ERROR           16#0A0F0104 16#0C230002 Controller type selection is not sup‐
                                                      ported. Check inputs for "PControl"
                                                      and "IControl".
INPUT_RANGE_ERROR             16#0A0F0104 16#0C230003 The "IControl" input is invalid
INPUT_RANGE_ERROR             16#0A0F0104 16#0C230017 The "FeedbackTControl" input is
                                                      invalid.
INPUT_INVALID_ERROR           16#0A0F0104 16#0C230008 The "PControl" input is invalid
INPUT_RANGE_ERROR             16#0A0F0104 16#0C230014 Negative x-value in "ResponseCurve"

ErrorID                             Additional1 Additional2 Description
INPUT_INVALID_ERROR                 16#0A0F0104 16#0C230015 X-value in "ResponseCurve" not in
                                         ascending order
INPUT_INVALID_ERROR                 16#0A0F0104 16#0C230016 More than one value for one x-position
                                         in "ResponseCurve"
STATE_MACHINE_ERROR                 16#0A0F0104 16#0C231000 Runtime error in function block:
                                         Invalid state of the state machine.

### 21.4.7 IL_PIType02

        Brief description
        The PI-controller contains an anti-reset wind-up integrator and a delimiter
        at the output. An adjustable PT1-element filters the actual value input. The
        difference between the command value and the actual value is analyzed by a
        command value curve (setpoint curve). A preset value can also be set and the
        controller can be paused. In this case, the controller output remains constant.
        It is only computed if the "Step" input changes. The last processed step is
        available as output.

        Interface description

Table 508: Interface variables of the IL_PIType02 function block
                   Name         Type               Comment
VAR_INPUT          Enable       BOOL               If TRUE, "ControlValue" is either set to the preset
                                                   value of "PresetValue" (if a rising edge is set at
                                                   "Preset") or to the computed value.
                   Pause        BOOL               If TRUE, the controller does not change the value of
                                                   "ControlValue”.
                   Preset       BOOL               At a rising edge at this input, the controller output is
                                                   set to the parameterizable value in "PresetValue”.
                   Setpoint     LREAL              The requested command value or command variable
                                                   for the controlled process.
                   Feedback     LREAL              The current actual value of the process.
                   Preset‐      LREAL              Preset value displayed at "ControlValue" at a rising
                   Value                           edge at "Preset”.
                   Step         UINT               Controller cycle step. The "ControlValue" is only com‐
                                                   puted if "Step" changes.
                   HighLimit    LREAL              Upper limit of "ControlValue"
                                                   If "ControlValue" exceeds this value, it is limited to
                                                   this value

Name           Type            Comment
LowLimit       LREAL           Lower limit of "ControlValue"
                              If "ControlValue" falls below this value, it is limited to
                              this value
PControl       LREAL           Proportional value for the gaining value of the con‐
                              troller
IControl       TIME            Integration time Tn for the integration value of the
                              controller
Feed‐     TIME                 PT1 element filter time constant smoothing the actual
backTCon‐                      value input "Feedback".
trol

Response‐ ARRAY[0..3] OF Command value curve to analyze the difference
Curve     ⮫ IL_COORD_TY between the smoothed "Feedback" actual value and
         PE01           the "Setpoint" value.

VAR_OUTPUT InOpera‐          BOOL      If TRUE, the PI-controller operates and the "Control‐
tion                        Value" controller output is valid.
Error         BOOL          Indicates that an error occurred in the function block.
ErrorID       ⮫ ERROR_CODE Error ID
ErrorIdent ⮫ ERROR_STRUC For the error structure with further error classification,
          T             see ⮫ Error codes on page 621
InPause    BOOL          "Pause" is active and the value at "ControlValue” is
                        frozen.
PresetAck BOOL           Value applied at "PresetValue".
ActStep    UINT          Step value to which "OutputValue" refers to.
HighLimi‐ BOOL           "ControlValue" reached upper limit
tAct
LowLimi‐ BOOL            "ControlValue" reached lower limit
tAct
Control‐   LREAL         The computed controller output value
Value

Table 509: Min./max. and default values of the IL_PIType02 inputs
Name           Type             Min. value    Max. value      Default value   Effective
Enable         BOOL                                           FALSE           continuous
Pause          BOOL                                           FALSE           continuous
Preset         BOOL                                           FALSE           continuous
Step           UINT             0             65335           0               continuous
Setpoint       LREAL            n. def.       n. def.         0.0             continuous
Feedback       LREAL            n. def.       n. def.         0.0             continuous
PresetValue    LREAL            n. def.       n. def.         0.0             rising edge at Preset
HighLimit      LREAL            LowLimit      n. def.         0.0             continuous
LowLimit       LREAL            n. def.       HighLimit       0.0             continuous
PControl       LREAL            n. def.       n. def.         0.0             continuous
IControl       LREAL            0.0           n. def.         0.0             continuous
FeedbackT‐     LREAL            0.0           n. def.         0.0             continuous
Control
Response‐      ARRAY[0..3]                                    0               rising edge at Enable
Curve          OF
               IL_COORD_TY
               PE01

Controller configuration
The signal at the "Feedback" input is smoothed by a first order delay element.
The respective filter time constant is set via "FeedbackTControl". If "Feed‐
backTControl" is 0 s, the filter is disabled. The difference signal from filtered
"Feedback" input and "Setpoint" is scaled by a characteristic curve given in
"ResponseCurve". The characteristic curve is point-symmetrical to the origin.
The x-values of the characteristic curve correspond to the differential signal.
The y-values correspond to the scaled difference signal. Up to four points
can be specified. The sections between the points are linearly interpolated. If
"ResponseCurve" is not created, there is no scaling.
For the requested P-, I-, PI-response, assign the corresponding values for the
"PControl" and "IControl" inputs. The control parameters can be changed "on
the fly". Thus, the values are immediately applied if the controller is switched
on. Use the following table to create the required control algorithm.
A specific configuration exists if all three values for "PControl" and "IControl"
are set to 0.0. In this case, the controller is switched off (no P-value and
I-value) and the "ControlValue" output is fixedly set to 0.0. However, the func‐
tionality for "Preset" and "Pause" remains. Thus, other values can be forced at
the output using these inputs.

Table 510: PI-controller configuration options
Controller type             PControl                    IControl
Switched off                0.0                         0.0
P-controller                Valid value                 0.0
I-controller                0.0                         Valid value
PI-controller               Valid value                 Valid value

The control algorithm can be displayed as the following block diagram:

Functional description
Initialization
During the first function block execution, the variables xd,k, xd,k-1, xd,k-2, yk and
yk-1 are initialized with the value "PresetValue". During the initialization, the
inputs "Setpoint" and "Feedback" have to have valid data.
If there is a rising edge at "Enable“, the delay element is initialized with the
value set at “Feedback”. Thus, "Feedback" is displayed immediately at the
outputs of the delay element.
The value of the "Step" input is copied to "ActStep".
Preset value
For a trouble-free start of the controller output "ControlValue", set the
"Preset" input when "Enable" is activated. In this case, the internal integrators
are initialized to the difference between "Setpoint" and "Feedback" scaled by
"ResponseCurve". The result is shown immediately at "ControlValue"

During this time, the inputs "Setpoint" and "Feedback" have to have valid
data.
Checking upper/lower limit values is also still active to ensure that the "Con‐
trolValue" is limited if the preset value "PresetValue" is beyond the limits of
"HighLimit" or "LowLimit".
"PresetAck" becomes TRUE when the value is applied at "PresetValue".
"Preset" has a higher priority than the "Pause" input.
Pause
The "Pause" input is only analyzed when the "Enable" input is active. In this
case, the control deviation ("Setpoint" – scaled "Feedback") is set to 0. Thus,
the "ControlValue" is fixedly specified. It can be used for a constant and

stable output.
The "InPause" output is set when "Pause" is active.
The "ActStep" output is still updated.
Normal mode
The controller computes only if the value changes at the "Step" input. The
step difference between two function block calls is included. "IControl" and
"FeedbackTControl" have steps as time base.
If "ControlValue" exceeds or falls below the value of "HighLimit" or "Low‐
Limit", "ControlValue" is limited to one of these values. If the control has
an integration part, an Anti-Reset-Windup is executed additionally. Thus, the
integral value is not added up further. In this case, the "HighLimitAct" and
"LowLimitAct" outputs are set.
The controller coefficients are computed again if the controller parameters
or the step difference change. Thus, the user can fine-tune by adjusting the
controller parameters. The step difference is measured each time the function
block is called. If the step difference deviates by more than 20% from the first
one measured and if it is not 0, all the coefficients are computed again.

Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:
Table 511: Generated error numbers of the IL_PIType02 function block
ErrorID                       Additional1 Additional2 Description
INPUT_INVALID_ERROR           16#0A0F0104 16#0C230001 "LowLimit" input value is greater than
                                                      the "HighLimit" input value
INPUT_INVALID_ERROR           16#0A0F0104 16#0C230002 Controller type selection is not sup‐
                                                      ported. Check inputs for "PControl"
                                                      and "IControl"
INPUT_RANGE_ERROR             16#0A0F0104 16#0C230004 The "IControl" input is invalid
INPUT_RANGE_ERROR             16#0A0F0104 16#0C230017 The "FeedbackTControl" input is
                                                      invalid
INPUT_INVALID_ERROR           16#0A0F0104 16#0C230008 The "PControl" input is invalid
INPUT_RANGE_ERROR             16#0A0F0104 16#0C230014 Negative x-value in "ResponseCurve"
INPUT_INVALID_ERROR           16#0A0F0104 16#0C230015 X-value in "ResponseCurve" not in
                                                      ascending order
INPUT_INVALID_ERROR           16#0A0F0104 16#0C230016 More than one value for one x-position
                                                      in "ResponseCurve"
STATE_MACHINE_ERROR           16#0A0F0104 16#0C231000 Runtime error in function block:
                                                      Invalid state of the state machine

## 21.5 Elements (basic elements)

### 21.5.1 Introduction and overview

The CXA_LoopControl provides the following basic elements from the control
engineering:
Table 512: CXA_LoopControl filter
           Time-discrete                  Event-controlled                   Description
⮫ Chapter 21.5.2 IL_Deadtime‐      ⮫ Chapter 21.5.3 IL_Deadtime‐   Dead time element (time-vari‐
Type01 on page 622                 Type02 on page 625              able)
⮫ Chapter 21.5.5 IL_DT1Type01 ⮫ Chapter 21.5.6 IL_DT1Type02 Differential element with first
on page 630                     on page 632                     order delay
⮫ Chapter 21.5.7                ⮫ Chapter 21.5.8                Digital filter to increase or
IL_PDT1Type01 on page 634       IL_PDT1Type02 on page 637       decrease the transfer function
                                                                starting from a certain frequency
⮫ Chapter 21.5.9 IL_PT1Type01 ⮫ Chapter 21.5.10                 First order delay element
on page 641                     IL_PT1Type02 on page 643
⮫ Chapter 21.5.11 IL_Transport‐ ⮫ Chapter 21.5.12 IL_Transport‐ Dead time element (runtime-var‐
DelayType01 on page 645         DelayType02 on page 648         iable)
    ⮫ Chapter 21.5.4 IL_DeviationResponseCurve on page 628         Evaluation graph
           ⮫ Chapter 21.5.13 IL_ValueLimit on page 651             Value limitation
          ⮫ Chapter 21.5.14 IL_ValueWindow on page 652             Value range check

### 21.5.2 IL_DeadtimeType01

Brief description
This function block implements a time-discrete dead time element with a
variable dead time. The dead time can be changed continuously. The actual
dead time is constantly adjusted to the preset value. The alignment to the
new dead time is based on the "variable time delay" schema.
Calle the dead time function block cyclically. As it is implemented as a digital
element, it can significantly affect the accuracy of the output. The function
block measures the time between the calls (sampling time) and updates the
resulting dead time if the scanning time of the preset dead time changes. The
measured sampling time is also available as output.

Interface description

Table 513: Interface variables of the IL_DeadtimeType01 function block
              Name           Type             Comment
VAR_INPUT     Enable         BOOL             At a rising edge, "OutputValue" is set to the preset
                                              value of "StartValue" and the function block is acti‐
                                              vated
              Pause      BOOL                 If TRUE, the value of "OutputValue" is not changed
              Value      LREAL                Input value to be output again, but delayed by "Delay"
              StartValue LREAL                A preset value indicated at the "OutputValue" at a
                                              rising edge at "Enable"
           Delay      LTIME                   Set dead time

BufferSize UINT                    Size of the buffer given in "Buffer" in elements
Buffer     POINTER TO              Value buffer
 LREAL
VAR_OUTPUT InOpera‐   BOOL                    If TRUE, the function block operates and the outputs
tion                               "OutputValue" and "ActDelay" are valid
Error      BOOL                    Indicates that an error occurred in the function block
ErrorID    ⮫ ERROR_CODE            Error ID
ErrorIdent ⮫ ERROR_STRUC For the error structure with further error classification,
    T             see ⮫ Error codes on page 624
InPause    BOOL          "Pause" is active and the values at "OutputValue" and
                  "ActDelay" are frozen
ActScan‐   LTIME         The passed time since the function block was called
Time                     the last time
Output‐    LREAL         Value delayed by "ActDelay"
Value
ActDelay   LTIME         Current delay

Table 514: Min./max. and default values of the IL_DeadtimeType01 inputs
Name           Type            Min. value      Max. value     Default value   Applied
Enable         BOOL                                           FALSE           Continuous
Pause          BOOL                                           FALSE           Continuous
Value          LREAL           N. def.         N. def.        0.0             Continuous
StartValue     LREAL           N. def.         N. def.        0.0             Rising edge at “Enable”
Delay          LTIME           0s              n. def.        0s              Continuous
BufferSize     UINT            0               4096           0               Rising edge at “Enable”
Buffer         POINTER TO                                     0               Rising edge at “Enable”
               LREAL

Functional description
Initialization

At a rising edge at "Enable", "BufferSize" and "Buffer” are checked and the
buffer is filled with the value of "StartValue". "ActDelay" is initialized with
0 s. "StartValue" is displayed immediately at the "OutputValue" output and
remains constant until "ActDelay" equals "Delay". The initial values of "Value"
are then displayed at the "OutputValue" output.
Normal mode
The function block is operating when the "Enable" input is active. With each
call, the time to the previous call is measured and returned at the "ActScan‐
Time" output. "ActScanTime" is also used to compute the buffer management.

At each call, the function block stores the value at "Value" and returns
this again delayed by "ActDelay" at "OutputValue". If the "BufferSize" of the
"Buffer" cannot buffer all values for the time given in "Delay", values are
omitted. This does not affect the resulting dead time.
The "ActDelay" output indicates the current delay of the value at "Output‐
Value". At a rising edge at "Enable" or if there is a change at "Delay", "Act‐
Delay" is constantly updated to the value in "Delay”. If "Delay“ changes while
the function block is active, the dead time is constantly adjusted based on
the variable time delay diagram. The dead time adjustment takes up to "Buf‐
ferSize" * "ActScanTime".

alignment. The packages are placed on a fixed point on the belt and removed
from the belt after the dead time. If the dead time changes, the point changes
at which the packages are taken from the belt.
Pause
The "Pause" input is only analyzed when the "Enable" input is active. The
function block can be stopped with "Pause". In this case, no further values are
stored and "OutputValue" and "ActDelay" remain constant.
The "InPause" output is set when "Pause" is active.
The "ActScanTime" output is still updated.

Configuration
The created buffer size in "Buffer" affects the accuracy of the output curve.
It is possible to create a smaller buffer than 4096 values at "Buffer". Ideally,
the buffer is larger than the maximum required delay divided by the call cycle
time of the function block. "BufferSize" can also be less than the delay. In this
case, there is not a new value at the "OutputValue" output during each cycle.
The time resolution decreases.
Required buffer size:
"BufferSize" = 1.4 * max("Delay")/required resolution
Adequate buffer size:
"BufferSize" = 1.4 * max("Delay")/ "ActScanTime"

Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:
Table 515: Generated error numbers of the IL_DeadtimeType01 function block
ErrorID                        Additional1 Additional2 Description
INPUT_INVALID_ERROR            16#0A0F0104 16#0C230011 The "Buffer" input is not assigned

ErrorID                         Additional1 Additional2 Description
INPUT_INVALID_ERROR             16#0A0F0104 16#0C230012 The "Delay" input is invalid
INPUT_RANGE_ERROR               16#0A0F0104 16#0C230013 The "BufferSize" input is too small
STATE_MACHINE_ERROR             16#0A0F0104 16#0C231000 Runtime error in function block:
                                   Invalid state of the state machine

### 21.5.3 IL_DeadtimeType02

Brief description
This function block implements an event-controlled dead time element with a
variable dead time. The dead time can be changed continuously. The actual

dead time steps are constantly adjusted to the preset value. The alignment to
the new dead time is based on the "variable time delay" schema.
The increment of the "Step” input should be as constant as possible. The last
processed step is also available as output.

Interface description

Table 516: Interface variables of the IL_DeadtimeType02 function block
              Name           Type            Comment
VAR_INPUT     Enable         BOOL            At a rising edge, "OutputValue" is set to the preset
                                             value of "StartValue" and the function block is acti‐
                                             vated
              Pause          BOOL            If TRUE, the value of "OutputValue" is not changed
              Step           UINT            Processing step
              Value          LREAL           Input value to be output again, but delayed by "Delay"
              StartValue     LREAL           A preset value indicated at the "OutputValue" at a
                                             rising edge at "Enable"
           Delay      UINT                   Number of steps to be delayed
           BufferSize UINT                   Size of the buffer given in "Buffer" in elements
           Buffer     POINTER TO             Value buffer
                      LREAL
VAR_OUTPUT InOpera‐   BOOL                   If TRUE, the function block operates and the outputs
           tion                              "OutputValue" and "ActDelay" are valid
           Error      BOOL                   Indicates that an error occurred in the function block
           ErrorID    ⮫ ERROR_CODE           Error ID
              ErrorIdent ⮫ ERROR_STRUC For the error structure with further error classification,
                         T             see ⮫ Error codes on page 627
              InPause    BOOL          "Pause" is active and the values at "OutputValue" and
                                       "ActDelay" are frozen

Name       Type               Comment
ActStep    UINT               Last processed step
Output‐    LREAL              Value delayed by "ActDelay"
Value
ActDelay   UINT               Actual delay in steps

Table 517: Min./max. and default values of the IL_DeadtimeType02 inputs
Name               Type          Min. value       Max. value     Default value   Applied
Enable             BOOL                                          FALSE           Continuous
Pause              BOOL                                          FALSE           Continuous
Step               UINT          0                65335          0               Continuous
Value              LREAL         N. def.          N. def.        0.0             Continuous
StartValue         LREAL         N. def.          N. def.        0.0             Rising edge at “Enable”
Delay              UINT          0                65335          0               Continuous
BufferSize         UINT          0                4096           0               Rising edge at “Enable”
Buffer             POINTER TO                                    0               Rising edge at “Enable”
                   LREAL

Functional description
Initialization
At a rising edge at "Enable", "BufferSize" and "Buffer” are checked and the
buffer is filled with the value of "StartValue". "ActDelay" is initialized with
0. "StartValue" is displayed immediately at the "OutputValue" output and
remains constant until "ActDelay" equals "Delay". The initial values of "Value"
are then displayed at the "OutputValue" output.
Normal mode
The function block is operating when the "Enable" input is active. "ActStep"
is updated to "Step” upon each call. It is only processed if the "Step" input
changes. The difference between the steps is also used for the buffer manage‐
ment.
Upon each call, the function block stores the value at "Value" and returns it
again at “OutputValue” but delayed by "ActDelay" steps. If the "BufferSize" of
the "Buffer" can buffer all values for the number of steps given in "Delay",
values are omitted. This does not affect the resulting dead time.
The "ActDelay" output indicates the current delay of the value at "Output‐
Value". At a rising edge at "Enable" or if there is a change at "Delay", "Act‐
Delay" is constantly updated to the value in "Delay". If "Delay“ changes while
the function block is active, the dead time is constantly adjusted based on
the variable time delay diagram. The dead time adjustment takes up to "Buf‐
ferSize" steps.

alignment. The packages are placed on a fixed point on the belt and removed
from the belt after the dead time. If the dead time changes, the point changes
at which the packages are taken from the belt.
Pause
The "Pause" input is only analyzed when the "Enable" input is active. The
function block can be stopped with "Pause". In this case, no further values are
stored and "OutputValue" and "ActDelay" remain constant.
The "InPause" output is set when "Pause" is active.
The "ActStep" output is still updated

Configuration
The created buffer size in "Buffer" affects the accuracy of the output curve.
It is possible to create a smaller buffer than 4096 values at "Buffer". Ideally,
the buffer is larger than the maximum required delay in steps. "BufferSize"
can also be less than the delay. In this case, there is not a new value at the
"OutputValue" output during each cycle. The resolution - based on the steps -
decreases.
Required buffer size:
"BufferSize" = 1.4 * max("Delay")/required resolution
Adequate buffer size:
"BufferSize" = 1.4 * max("Delay")

Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:
Table 518: Generated error numbers of the IL_DeadtimeType02 function block
ErrorID                       Additional1 Additional2 Description
INPUT_INVALID_ERROR           16#0A0F0104 16#0C230011 The "Buffer" input is not assigned
INPUT_INVALID_ERROR           16#0A0F0104 16#0C230012 The "Delay" input is invalid
INPUT_RANGE_ERROR             16#0A0F0104 16#0C230013 The "BufferSize" input is too small
INPUT_RANGE_ERROR             16#0A0F0104 16#0C231000 Runtime error in function block:
                                                      Invalid state of the state machine

### 21.5.4 IL_DeviationResponseCurve

      Brief description
      This function block converts an input signal point-symmetrically to the origin
      on a command value curve. The command value curve is given by up to 4
      points. It is linearly interpolated between the points. The first section goes
      from the origin to the first point. There is an increase of 1.0 from the last
      point onwards to infinity. The x-coordinates of the points have to increase in a
      positive direction and may not be smaller than 0.

      Interface description

Table 519: Interface variables of the IL_DeviationResponseCurve function block
                   Name        Type               Comment
VAR_INPUT          Enable      BOOL               If TRUE, the function block is active
                   Deviation   LREAL              Input value to be analyzed by the curve given in
                                                  "ResponseCurve"
           Response‐ ARRAY[0..3] OF               Command value curve consisting of value pairs
           Curve     ⮫ IL_COORD_TY
                     PE01
VAR_OUTPUT InOpera‐  BOOL                         The function block has completed its initialization and
           tion                                   "DeviationWeighted" is valid
           Error     BOOL                         Indicates that an error occurred in the function block
           ErrorID   ⮫ ERROR_CODE                 Error ID
                   ErrorIdent ⮫ ERROR_STRUC For the error structure with further error classification,
                              T             see ⮫ Error codes on page 629
                   Deviation‐ LREAL         Deviation scaled by "ResponseCurve"
                   Weighted

Table 520: Min./max. and default values of the IL_DeviationResponseCurve inputs
Name               Type        Min. value          Max. value     Default value Applied
Enable             BOOL                                           FALSE         Continuous
Deviation          LREAL       N. def.             N. def.        0.0           Continuous
Response‐          ARRAY[0..3]                                                  Rising edge at “Enable”
Curve              OF
                   IL_COORD_TY
                   PE01

      Functional description
      Initialization
      At a rising edge at "Enable", "ResponseCurve" is checked and set to “InOpera‐
      tion”. The value in "DeviationWeighted" is then valid.
      Normal mode

The function block is operating when the "Enable" input is active. With each
call, the value in "Deviation" is applied using the command value curve given
in "ResponseCurve" and issued at "DeviationWeighted".

Configuration
The characteristic curve defined in "ResponseCurve" consists of four points.
Negative deviations are processed by point reflection of the curve at the
origin. This results in a total of nine linear sections. The section s5 passes
the origin. The sections s1 and s9 have a slope of 1 and each run into positive
or negative infinity.

Points P1 to P4 are arranged in an array of IL_COORD_TYPE01. If less than
four points are required, the x-coordinates of the points not required (begin‐
ning with the last point) are set to 0. The x-values have to be positive and
increase in positive direction. The same point can be used twice.

Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:
Table 521: Generated error numbers of the IL_DeviationResponseCurve function block
ErrorID                       Additional1 Additional2 Description
INPUT_INVALID_ERROR           16#0A0F0104 16#0C230014 Negative x-value in “ResponseCurve"
INPUT_INVALID_ERROR           16#0A0F0104 16#0C230015 X-value in "ResponseCurve" not in
                                                      ascending order
INPUT_RANGE_ERROR             16#0A0F0104 16#0C230016 More than one value for one x-position
                                                      in "ResponseCurve"

### 21.5.5 IL_DT1Type01

Brief description
This function block implements a time-discrete differential element with first
order delay. It is computed continuously, that is upon each function call. Call
the function block cyclically for a most consistent computation possible. The
cycle time measured by the function block is also available as output.

Interface description

Table 522: Interface variables of the IL_DT1Type01 function block
                   Name      Type   Comment
VAR_INPUT          Enable    BOOL   If TRUE, "OutputValue" is set to the preset value of
                                    "StartValue" or to the computed value
           Pause      BOOL          If TRUE, the controller does not change the value of
                                    "OutputValue”
           Value      LREAL         The current actual process value
           DControl LTIME           Time constant Tn of the DT1 element
VAR_OUTPUT InOpera‐   BOOL          If TRUE, the DT1 element operates and the "Output‐
           tion                     Value" controller output is valid
           Error      BOOL          Indicates that an error occurred in the function block
           ErrorID    ⮫ ERROR_CODE Error ID
           ErrorIdent ⮫ ERROR_STRUC For the error structure with further error classification,
                      T             see ⮫ Error codes on page 631
           InPause    BOOL          "Pause" is active and the value at "ControlValue” is
                                    frozen
           ActScan‐   LTIME         The passed time since the function block was called
           Time                     the last time
           Output‐    LREAL         Computed controller output value
           Value

Table 523: Min./max. and default values of the IL_DT1Type01 inputs
Name               Type          Min. value     Max. value      Default value   Applied
Enable             BOOL                                         FALSE           Continuous
Pause              BOOL                                         FALSE           Continuous
Value              LREAL         N. def.        N. def.         0.0             Continuous
DControl           LTIME         0s             N. def.         1s              Continuous

Functional description
The function block outputs the computed value of the implemented DT1 func‐
tion at the "OutputValue" output. It is computed continuously when "Enable"
is set. The "Value" input value is applied at a rising edge at the "Enable"
input and provided for the internal computation. All inputs are continuously
processed.
During the function block initialization, the "Value" input variables and the
"DControl" time constant are applied. "OutputValue" is initialized with 0.0.
Pause
The "Pause" input is only evaluated when the "Enable" input is active. If TRUE
is present at "Pause", there is no computation and the "OutputValue" value is

not changed. The internal integrator is also frozen.
The "InPause" output is set when "Pause" is active.
The "ActScanTime" output is still updated.
Normal mode
The step response of a DT1 element is like a curve approximating 0.

The transfer function is:

"DControl" indicates the delay time constant. If "DControl" is 0.0, the DT1
element is disabled and the "OutputValue" output is set to 0.0.

Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:

Table 524: Generated error numbers of the IL_DT1Type01 function block
ErrorID                            Additional1 Additional2 Description
INPUT_RANGE_ERROR                  16#0A0F010 16#0C23001 The "DControl" input is invalid
                                   4           C
STATE_MACHINE_ERROR                16#0A0F010 16#0C23100 Runtime error in function block:
                                   4           0           Invalid state of the state machine

### 21.5.6 IL_DT1Type02

Brief description
This function block implements an event-controlled differential element with
first order delay. The computation is event-controlled, i.e. with each change at
the Step input. The last processed step is available as output.

Interface description

Table 525: Interface variables of the IL_DT1Type02 function block
                   Name      Type   Comment
VAR_INPUT          Enable    BOOL   If TRUE, "OutputValue" is set to the preset value of
                                    "StartValue" or to the computed value
           Pause      BOOL          If TRUE, the controller does not change the value of
                                    "OutputValue”
           Step       UINT          Processing step
           Value      LREAL         The current actual process value
           DControl LREAL           Time constant Tn of the DT1 element
VAR_OUTPUT InOpera‐   BOOL          If TRUE, the DT1 element operates and the "Output‐
           tion                     Value" controller output is valid
           Error      BOOL          Indicates that an error occurred in the function block
           ErrorID    ⮫ ERROR_CODE Error ID
           ErrorIdent ⮫ ERROR_STRUC For the error structure with further error classification,
                      T             see ⮫ Error codes on page 634
           InPause    BOOL          "Pause" is active and the value at "ControlValue” is
                                    frozen
           ActStep    UINT          Last processed step
           Output‐    LREAL         Computed controller output value
           Value

Table 526: Min./max. and default values of the IL_DT1Type02 inputs
Name               Type          Min. value     Max. value      Default value Applied
Enable             BOOL                                         FALSE         Continuous
Pause              BOOL                                         FALSE         Continuous

Name          Type            Min. value        Max. value   Default value   Applied
Step          UINT            0                 65335        0               Continuous
Value         LREAL           N. def.           N. def.      0.0             Continuous
DControl      LREAL           0.0               N. def.      1.0             Continuous

Functional description
The function block issues the calculated value of the implemented DT1 func‐
tion at the "OutputValue" output. It is computed when "Step" input changes
while "Enable" is set. The increment at the "Step" input is processed, i.e.
more than one step is computed if required. The "Value" input value is applied
at a rising edge at the "Enable" input and provided for the internal computa‐

tion. All inputs are continuously processed.
"Value" input variables and the "DControl" time constant are applied while the
function block is initialized. "OutputValue" is initialized with 0.0.
Pause
The "Pause" input is only evaluated when the "Enable" input is active. If TRUE
is present at "Pause", there is no computation and the "OutputValue" value is
not changed. The internal integrator is also frozen.
The "InPause" output is set when "Pause" is active.
The "ActStep" output is still updated.
Normal mode
The step response of a DT1 element is like a curve approximating 0.

The transfer function is:

"DControl" indicates the delay time constant. If "DControl" is 0.0, the DT1
element is disables and the "OutputValue" output is set to 0.0 each time the
"Step" input changes.

Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:
Table 527: Generated error numbers of the IL_DT1Type02 function block
ErrorID                               Additional1 Additional2 Description
INPUT_RANGE_ERROR                     16#0A0F010 16#0C23001 The "DControl" input is invalid
                                      4           C
STATE_MACHINE_ERROR                   16#0A0F010 16#0C23100 Runtime error in function block:
                                      4           0           Invalid state of the state machine

### 21.5.7 IL_PDT1Type01

Brief description
The IL_PDT1Type01 function block implements a time-discrete PDT1 filter. The
digital filter can be used to increase or decrease the transfer function starting
from a specific frequency.
It is computed continuously, that is upon each function call. Call the function
block cyclically for a most consistent computation possible. The cycle time
measured by the function block is also available as output.

Interface description

Table 528: Interface variables of the IL_PDT1Type01 function block
                   Name      Type   Comment
VAR_INPUT          Enable    BOOL   If TRUE, "OutputValue" is set to the value computed
                                    with "StartValue"
           Pause      BOOL          Enables the Pause mode if TRUE
           Value      LREAL         The current actual process value
           StartValue LREAL         The initial value applied at a rising edge at "Enable" at
                                    the "OutputValue" output
           TvControl LTIME          Derivative time constant
           T1Control LTIME          Time constant
VAR_OUTPUT InOpera‐   BOOL          If TRUE, the PT1 element operates and the "Output‐
           tion                     Value" controller output is valid
           Error      BOOL          Indicates that an error occurred in the function block
           ErrorID    ⮫ ERROR_CODE Error ID
           ErrorIdent ⮫ ERROR_STRUC For the error structure with further error classification,
                      T             see ⮫ Error codes on page 637
           InPause    BOOL          "Pause" is active and the value at "ControlValue” is
                                    frozen

Name           Type             Comment
ActScan‐       LTIME            The time passed since the latest function block call
Time
Output‐        LREAL            The computed filter value
Value

Table 529: Min./max. and default values of the IL_PDT1Type01 inputs
Name           Type             Min. value    Max. value     Default value   Applied
Enable         BOOL                                          FALSE           Continuous
Pause          BOOL                                          FALSE           Continuous

Value          LREAL            N. def.       N. def.        0.0             Continuous
StartValue     LREAL            N. def.       N. def.        0.0             Rising edge at “Enable”
TvControl      LTIME            0s            N. def.        1 ms            Continuous
T1Control      LTIME            0s            N. def.        1 ms            Continuous

Functional description
The IL_PDT1Type01 function block implements a time-discrete PDT1 filter. The
digital filter can be used to increase or decrease the transfer function starting
from a specific frequency. The function block operates time-discretely.
The response depends on the relation between the two time constants:
For Tv > T1: The signal is attenuated above Tv and T1.
For Tv < T1: The signal is amplified above Tv and T1.

Value, StartValue, OutputValue
The "Value" input contains the input value of the filter. This value is processed
at each call if "InOperation" is set. At a rising edge at "Enable", the value
in "StartValue" is applied to all internal registers. The result is output at the
"OutputValue" output.
TvControl, T1Control
These two inputs determine the filter response. "TvControl" is the derivative
time. The ratio of Tv/T1 is determined by the steepness of the dropping.

Pause

The "Pause" input is only evaluated when the "Enable" input is active. If
"Pause" is TRUE, it is not computed and the value of "OutputValue" is not
changed. The internal integrator is also frozen.
The "InPause" output is set when "Pause" is active.
The "ActScanTime" output is still updated.

Time response
The IL_PDT1Type01 function block operates asynchronously. After the start
due to a rising edge at the "Enable" input, it reads the "StartValue" input.
At each call, the function block reads a value from the inputs "Value", "TvCon‐
trol" and "T1Control" and computes a new value at the "OutputValue" output.

If the filter is active, the "InOperation" output is set. If an error occurs, the
"Error" output is set.

Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:
Table 530: Generated error numbers of the IL_PDT1Type01 function block
ErrorID                             Additional1 Additional2 Description
INPUT_RANGE_ERROR                   16#0A0F010 16#0C23001 The "TvControl" input is invalid
                                    4           8
INPUT_RANGE_ERROR                   16#0A0F010 16#0C23001 The "T1Control" input is invalid
                                    4           9
STATE_MACHINE_ERROR                 16#0A0F010 16#0C23100 Runtime error in function block:
                                    4           0           Invalid state of the state machine

### 21.5.8 IL_PDT1Type02

Brief description
The IL_PDT1Type02 function block implements an event-controlled PDT1 filter.
The digital filter can be used to increase or decrease the transfer function
starting from a specific frequency.
The calculation is event-controlled, that is to say at every change at the Step
input. The last processed step is available as output.

Interface description

Table 531: Interface variables of the IL_PDT1Type02 function block
              Name           Type              Comment
VAR_INPUT     Enable         BOOL              If TRUE, "OutputValue" is set to the value computed
                                               with "StartValue"
              Pause          BOOL              Enables the Pause mode if TRUE

Name         TypeComment
Step         UINTProcessing step
Value        LREAL
                 The current actual process value
StartValue   LREAL
                 The initial value applied at a rising edge at "Enable" at
                 the "OutputValue" output
TvControl LTIME          Derivative time constant
T1Control LTIME          Time constant
VAR_OUTPUT InOpera‐   BOOL          If TRUE, the PT1 element operates and the "Output‐
tion                     Value" controller output is valid
Error      BOOL          Indicates that an error occurred in the function block
ErrorID    ⮫ ERROR_CODE Error ID
ErrorIdent ⮫ ERROR_STRUC For the error structure with further error classification,
   T             see ⮫ Error codes on page 640
InPause    BOOL          "Pause" is active and the value at "ControlValue” is
                 frozen
ActStep    UINT          Step to which "OutputValue" refers
Output‐    LREAL         The computed filter value
Value

Table 532: Min./max. and default values of the IL_PDT1Type02 inputs
Name               Type            Min. value     Max. value     Default value   Applied
Enable             BOOL                                          FALSE           Continuous
Pause              BOOL                                          FALSE           Continuous
Step               UINT            0              65335          0               Continuous
Value              LREAL           N. def.        N. def.        0.0             Continuous
StartValue         LREAL           N. def.        N. def.        0.0             Rising edge at “Enable”
TvControl          LTIME           >0s            N. def.        1.0             Continuous
T1Control          LTIME           >0s            N. def.        1.0             Continuous

      Functional description
      The IL_PDT1Type02 function block implements a event-controlled PDT1 filter.
      The digital filter can be used to increase or decrease the transfer function
      starting from a specific frequency. The function block operates event-con‐
      trolled. Thus, a new value is processed when the "Step" input changes.
      The response depends on the relation between the two time constants:
      For Tv > T1: The signal is attenuated above Tv and T1.
      For Tv < T1: The signal is amplified above Tv and T1.

Value, StartValue, OutputValue
The "Value" input contains the input value of the filter. This value is processed
at each call if "InOperation" is set. At a rising edge at "Enable", the value
in "StartValue" is applied to all internal registers. The result is output at the
"OutputValue" output.
TvControl, T1Control

These two inputs determine the filter response. "TvControl" is the derivative
time. The ratio of Tv/T1 is determined by the steepness of the dropping.

Pause
The "Pause" input is only evaluated when the "Enable" input is active. If
"Pause" is TRUE, it is not computed and the value of "OutputValue" is not
changed. The internal integrator is also frozen.
The "InPause" output is set when "Pause" is active.
The "ActStep" output is still updated.

Time response
The IL_PDT1Type02 function block operates asynchronously. After the start
due to a rising edge at the "Enable" input, it reads the "StartValue" input.
At each call, the function block reads a value from the inputs "Value", "TvCon‐
trol" and "T1Control" and computes a new value at the "OutputValue" output.
If the filter is active, the "InOperation" output is set. If an error occurs, the
"Error" output is set.

Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:
Table 533: Generated error numbers of the IL_PDT1Type02 function block
ErrorID                            Additional1 Additional2 Description
INPUT_RANGE_ERROR                  16#0A0F010 16#0C23001 The "TvControl" input is invalid
                                   4           8
INPUT_RANGE_ERROR                  16#0A0F010 16#0C23001 The "T1Control" input is invalid
                                   4           9
STATE_MACHINE_ERROR                16#0A0F010 16#0C23100 Runtime error in function block:
                                   4           0           Invalid state of the state machine

### 21.5.9 IL_PT1Type01

Brief description
This function block implements a time-discrete first order delay element. The
calculation takes place continuously, that is to say each time the function
block is called. Call the function block cyclically for a most consistent compu‐
tation possible. The cycle time measured by the function block is also avail‐
able as output.

Interface description

Table 534: Interface variables of the IL_PT1Type01 function block
              Name           Type   Comment
VAR_INPUT     Enable         BOOL   If TRUE, "OutputValue" is set to the preset value of
                                    "StartValue" or to the computed value
           Pause      BOOL          If TRUE, the value at "OutputValue" remains constant
           Value      LREAL         The current actual process value
           StartValue LREAL         The initial value applied at a rising edge at "Enable" at
                                    the "OutputValue" output
           TControl   LTIME         Time constant Tn of the PT1 element
VAR_OUTPUT InOpera‐   BOOL          If TRUE, the PT1 element operates and the "Output‐
           tion                     Value" controller output is valid
           Error      BOOL          Indicates that an error occurred in the function block
           ErrorID    ⮫ ERROR_CODE Error ID
           ErrorIdent ⮫ ERROR_STRUC For the error structure with further error classification,
                      T             see ⮫ Error codes on page 643
           InPause    BOOL          "Pause" is active and the value at "ControlValue” is
                                    frozen
           ActScan‐   LTIME         The time passed since the latest function block call
           Time
           Output‐    LREAL         The computed output value
           Value

Table 535: Min./max. and default values of the IL_PT1Type01 inputs
Name           Type            Min. value    Max. value      Default value   Applied
Enable         BOOL                                          FALSE           Continuous
Pause          BOOL                                          FALSE           Continuous
Value          LREAL           N. def.       N. def.         0.0             Continuous
StartValue     LREAL           N. def.       N. def.         0.0             Rising edge at “Enable”
TControl       LTIME           0s            N. def.         1s              Continuous

Functional description
The function block outputs the computed value of the first order delay func‐
tion at the "OutputValue" output. It is computed continuously when the
"Enable" input is set. The "StartValue" input values are only applied at a rising
edge at the "Enable" input. It is present at "OutputValue" output and used
as initial value for the internal integrator. All other inputs are continuously
processed.
Starting value
An initial value of the function can optionally be applied to the function block
using the "StartValue" input variable. This value is applied along with the
other input variables, such as "Value“ and the time constant "TControl” while
the function block is initialized.
Pause
The "Pause" input is only evaluated when the "Enable" input is active. If TRUE
is present at "Pause", there is no computation and the "OutputValue" value is
not changed. The internal integrator is also frozen.
The "InPause" output is set when "Pause" is active.
The "ActScanTime" output is updated when "Pause" is active.
Normal mode
The step response of a PT1 element has the line of a curve similar to the
"Value" command value.

The transfer function is:

"TControl" indicates the delay time constant. If "TControl" is 0 s, the PT1
element is disabled and the "Value" input is copied directly to "OutputValue".
The "TControl" and "Value" inputs are applied upon each function block call
while "Enable" is set.

Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:
Table 536: Generated error numbers of the IL_PT1Type01 function block
ErrorID                            Additional1 Additional2 Description
INPUT_RANGE_ERROR                  16#0A0F010 16#0C23001 The "TControl" input is invalid
                                   4           7
STATE_MACHINE_ERROR                16#0A0F010 16#0C23100 Runtime error in function block:
                                   4           0           Invalid state of the state machine

### 21.5.10 IL_PT1Type02

Brief description
This function block implements an event-controlled first order delay element.
The calculation is event-controlled, that is with each change at the Step input.
The last processed step is available as output.

Interface description

Table 537: Interface variables of the IL_PT1Type02 function block
              Name           Type   Comment
VAR_INPUT     Enable         BOOL   If TRUE, "OutputValue" is set to the preset value of
                                    "StartValue" or to the computed value
           Pause      BOOL          If TRUE, the value at "OutputValue" remains constant
           Step       UINT          Processing step
           Value      LREAL         The current actual process value
           StartValue LREAL         The initial value applied at a rising edge at "Enable" at
                                    the "OutputValue" output
           TControl   LREAL         Time constant Tn of the PT1 element
VAR_OUTPUT InOpera‐   BOOL          If TRUE, the PT1 element operates and the "Output‐
           tion                     Value" controller output is valid
           Error      BOOL          Indicates that an error occurred in the function block
           ErrorID    ⮫ ERROR_CODE Error ID
           ErrorIdent ⮫ ERROR_STRUC For the error structure with further error classification,
                      T             see ⮫ Error codes on page 645
           InPause    BOOL          "Pause" is active and the value at "ControlValue” is
                                    frozen
           ActStep    UINT          Step to which "OutputValue" refers
           Output‐    LREAL         Computed controller output value
           Value

Table 538: Min./max. and default values of the IL_PT1Type02 inputs
Name               Type         Min. value     Max. value     Default value   Applied
Enable             BOOL                                       FALSE           Continuous
Pause              BOOL                                       FALSE           Continuous
Step               UINT         0              65335          0               Continuous
Value              LREAL        N. def.        N. def.        0.0             Continuous
StartValue         LREAL        N. def.        N. def.        0.0             Rising edge at “Enable”
TControl           LREAL        0.0            N. def.        1.0             Continuous

Functional description
The function block outputs the computed value of the implemented PT1 func‐
tion at the "OutputValue" output. It is computed when "Step" input changes
while "Enable" is set. The increment at the "Step" input is processed, i.e.
more than one step is computed if required. The "StartValue" input values
are only applied at a rising edge at the "Enable" input. It is present at "Output‐
Value" output and used as initial value for the internal integrator. All other
inputs are continuously processed.
Starting value
An initial value of the function can optionally be applied to the function block
using the "StartValue" input variable. This value is applied along with the
other input variables, such as "Value" and the time constant "TControl” when
the function block is initialized.
Pause
The "Pause" input is only evaluated when the "Enable" input is active. If TRUE
is present at "Pause", there is no computation and the "OutputValue" value is
not changed. The internal integrator is also frozen.
The "InPause" output is set when "Pause" is active.
The "ActStep" output is still updated.
Normal mode
The step response of a PT1 element has the line of a curve similar to the
"Value" command value.

The transfer function is:

"TControl" indicates the delay time constant. If "TControl" is 0.0, the PT1
element is disabled and the "Value" input is copied directly to "OutputValue"
upon each change at the "Step" input.
The "TControl" and "Value" inputs are applied upon each function block call
while "Enable" is set.

Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:
Table 539: Generated error numbers of the IL_PT1Type02 function block
ErrorID                            Additional1 Additional2 Description
INPUT_RANGE_ERROR                  16#0A0F010 16#0C23001 The "TControl" input is invalid
                                   4           7
STATE_MACHINE_ERROR                16#0A0F010 16#0C23100 Runtime error in function block:
                                   4           0           Invalid state of the state machine

### 21.5.11 IL_TransportDelayType01

Brief description
This function block implements a time-discrete dead time element with a
variable dead time. The dead time can be changed continuously. The actual
dead time is constantly adjusted to the preset value. The adjustment to the
new dead time is based on the "variable transport delay” schema.

      The dead time block should be called cyclically. As it is implemented as a dig‐
      ital element, it can significantly affect the accuracy of the output. The function
      block measures the time between the calls (sampling time) and updates the
      resulting dead time if the scanning time changes substantially or if the preset
      dead time changes. The measured sampling time is also available as output.

      Interface description

Table 540: Interface variables of the IL_TransportDelayType01 function block
                   Name       Type               Comment
VAR_INPUT          Enable     BOOL               At a rising edge, "OutputValue" is set to the preset
                                                 value of "StartValue”. If TRUE, the function block is
                                                 active
                   Pause      BOOL               If TRUE, the value of "OutputValue" is not changed
                   Value      LREAL              Input value to be output again, but delayed by "Delay"
                   StartValue LREAL              A preset value indicated at the "OutputValue" at a
                                                 rising edge at "Enable"
           Delay      TIME                       Set dead time
           BufferSize UINT                       Size of the buffer given in "Buffer" in elements
           Buffer     POINTER TO                 Value buffer
                      LREAL
VAR_OUTPUT InOpera‐   BOOL                       If TRUE, the function block operates and the outputs
           tion                                  "OutputValue" and "ActDelay" are valid
           Error      BOOL                       Indicates that an error occurred in the function block
           ErrorID    ⮫ ERROR_CODE               Error ID
                   ErrorIdent ⮫ ERROR_STRUC For the error structure with further error classification,
                              T             see ⮫ Error codes on page 648
                   InPause    BOOL          "Pause" is active and the values at "OutputValue" and
                                            "ActDelay" are frozen
                   ActScan‐   TIME          The passed time since the function block was called
                   Time                     the last time
                   Output‐    LREAL         Value delayed by "ActDelay"
                   Value
                   ActDelay   TIME          Actual delay

Table 541: Min./max. and default values of the IL_TransportDelayType01 inputs
Name               Type            Min. value     Max. value     Default value   Applied
Enable             BOOL                                          FALSE           Continuous
Pause              BOOL                                          FALSE           Continuous
Value              LREAL           N. def.        N. def.        0.0             Continuous

Name           Type            Min. value     Max. value     Default value   Applied
StartValue     LREAL           N. def.        N. def.        0.0             Rising edge at “Enable”
Delay          TIME            0s             n. def.        0s              Continuous
BufferSize     UINT            0              4096           0               Rising edge at “Enable”
Buffer         POINTER TO                                    0               Rising edge at “Enable”
LREAL

Functional description
Initialization
At a rising edge at "Enable", "BufferSize" and "Buffer” are checked and the

buffer is filled with the value of "StartValue". "ActDelay" is initialized with
"Delay". “StartValue" is displayed immediately at the "OutputValue" output
and remains until the specified time elapsed in "Delay". The initial values of
"Value" are then displayed at the "OutputValue" output.
Normal mode
The function block is operating when the "Enable" input is active. With each
call, the time to the previous call is measured and returned at the "ActScan‐
Time" output. "ActScanTime" is also used to compute the buffer management.
At each call, the function block stores the value at "Value" and returns
this again delayed by "ActDelay" at "OutputValue". If the "BufferSize" of the
"Buffer" cannot buffer all values for the time given in "Delay", values are
omitted. This does not affect the resulting dead time.
The "ActDelay" output indicates the current delay of the value at "Output‐
Value". If "Delay" changes, "ActDelay" is continuously updated to the value in
"Delay". If "Delay“ changes while the function block is active, the dead time is
constantly adjusted based on the variable transport delay diagram. The dead
time adjustment takes up to "BufferSize" * "ActScanTime".

alignment. The packages are placed on a fixed point on the belt and removed
from the belt after a specified period. The velocity of the belt set ensures that
every package remains on the belt for the length of the dead time. If the dead
time increases, the belt velocity is adjusted accordingly.
Pause
The "Pause" input is only analyzed when the "Enable" input is active. The
function block can be stopped with "Pause". In this case, no further values are
stored and "OutputValue" and "ActDelay" remain constant.
The "InPause" output is set when "Pause" is active.
The "ActScanTime" output is still updated.

Configuration
The created buffer size in "Buffer" affects the accuracy of the output curve.
It is possible to create a smaller buffer than 4096 values at "Buffer". Ideally,
the buffer is larger than the maximum required delay divided by the call cycle
time of the function block. "BufferSize" can also be less than the delay. In this
case, there is not a new value at the "OutputValue" output during each cycle.
The time resolution decreases.
Required buffer size:
"BufferSize" = max(“Delay”)/required resolution
Adequate buffer size:
"BufferSize" = max(“Delay”)/”ActScanTime”

Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:
Table 542: Generated error numbers of the IL_TransportDelayType01 function block
ErrorID                          Additional1 Additional2 Description
INPUT_INVALID_ERROR              16#0A0F0104 16#0C230011 The "Buffer" input is not assigned
INPUT_INVALID_ERROR              16#0A0F0104 16#0C230012 The "Delay" input is invalid
INPUT_RANGE_ERROR                16#0A0F0104 16#0C230013 The "BufferSize" input is too small
STATE_MACHINE_ERROR              16#0A0F0104 16#0C231000 Runtime error in function block:
                                                         Invalid state of the state machine

### 21.5.12 IL_TransportDelayType02

Brief description
This function block implements an event-controlled dead time element with a
variable dead time. The dead time can be changed continuously. The actual
dead time is constantly adjusted to the preset value. The adjustment to the
new dead time is based on the "variable transport delay” schema.
Call the dead time function block cyclically. The increment of the "Step” input
should be as constant as possible. The last processed step is also available as
output.

Interface description

Table 543: Interface variables of the IL_TransportDelayType02 function block
                   Name      Type               Comment
VAR_INPUT          Enable    BOOL               At a rising edge, "OutputValue" is set to the preset
                                                value of "StartValue”. If TRUE, the function block is
                                                active

Name           Type             Comment
Pause          BOOL             If TRUE, the value of "OutputValue" is not changed
Step           UINT             Processing step
Value          LREAL            Input value to be output again, but delayed by "Delay"
StartValue     LREAL            A preset value indicated at the "OutputValue" at a
                         rising edge at "Enable"
Delay      UINT                    Number of steps to be delayed
BufferSize UINT                    Size of the buffer given in "Buffer" in elements
Buffer     POINTER TO              Value buffer
 LREAL

VAR_OUTPUT InOpera‐   BOOL                    If TRUE, the function block operates and the outputs
tion                               "OutputValue" and "ActDelay" are valid
Error      BOOL                    Indicates that an error occurred in the function block
ErrorID    ⮫ ERROR_CODE            Error ID
ErrorIdent ⮫ ERROR_STRUC For the error structure with further error classification,
    T             see ⮫ Error codes on page 650
InPause    BOOL          "Pause" is active and the values at "OutputValue" and
                  "ActDelay" are frozen
ActStep    UINT          Last processed step
Output‐    LREAL         Value delayed by "ActDelay"
Value
ActDelay   UINT          Actual delay in steps

Table 544: Min./max. and default values of the IL_TransportDelayType02 inputs
Name           Type             Min. value     Max. value     Default value   Applied
Enable         BOOL                                           FALSE           Continuous
Pause          BOOL                                           FALSE           Continuous
Step           UINT             0              65335          0               Continuous
Value          LREAL            N. def.        N. def.        0.0             Continuous
StartValue     LREAL            N. def.        N. def.        0.0             Rising edge at “Enable”
Delay          UINT             0              65335          0               Continuous
BufferSize     UINT             0              4096           0               Rising edge at “Enable”
Buffer         POINTER TO                                     0               Rising edge at “Enable”
               LREAL

Functional description
Initialization
At a rising edge at "Enable", "BufferSize" and "Buffer” are checked and the
buffer is filled with the value of "StartValue". "ActDelay" is initialized with
"Delay". "StartValue" is displayed immediately at the "OutputValue" output
and remains constant until the number of steps given in "Delay" passed. The
initial values of "Value" are then displayed at the "OutputValue" output.
Normal mode
The function block is operating when the "Enable" input is active. "ActStep"
is updated to "Step” upon each call. It is only processed if the "Step" input
changes. The difference between the steps is also used for the buffer manage‐
ment.

Upon each call, the function block stores the value at "Value" and returns it
again at “OutputValue” but delayed by "ActDelay" steps. If the "BufferSize" of
the "Buffer" can buffer all values for the number of steps given in "Delay",
values are omitted. This does not affect the resulting dead time.
The "ActDelay" output indicates the current delay of the value at "Output‐
Value". If "Delay" changes, "ActDelay" is continuously updated to the value in
"Delay". If "Delay“ changes while the function block is active, the dead time is
constantly adjusted based on the variable transport delay diagram. The dead
time alignment takes up to "BufferSize" steps.

alignment. The packages are placed on a fixed point on the belt and removed
from the belt after a specified period. The velocity of the belt set ensures that
every package remains on the belt for the length of the dead time. If the dead
time increases, the belt velocity is adjusted accordingly.
Pause
The "Pause" input is only analyzed when the "Enable" input is active. The
function block can be stopped with "Pause". In this case, no further values are
stored and "OutputValue" and "ActDelay" remain constant.
The "InPause" output is set when "Pause" is active.
The "ActStep" output is still updated

Configuration
The created buffer size in "Buffer" affects the accuracy of the output curve.
It is possible to create a smaller buffer than 4096 values at "Buffer". Ideally,
the buffer is larger than the maximum required delay in steps. "BufferSize"
can also be less than the delay. In this case, there is not a new value at the
"OutputValue" output during each cycle. The resolution - based on the steps -
decreases.
Required buffer size:
"BufferSize" = max(“Delay”)/required resolution
Adequate buffer size:
"BufferSize" = max("Delay")

Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:
Table 545: Generated error numbers of the IL_TransportDelayType02 function block
ErrorID                        Additional1 Additional2 Description
INPUT_INVALID_ERROR            16#0A0F0104 16#0C230011 The "Buffer" input is not assigned

ErrorID                        Additional1 Additional2 Description
INPUT_INVALID_ERROR            16#0A0F0104 16#0C230012 The "Delay" input is invalid
INPUT_RANGE_ERROR              16#0A0F0104 16#0C230013 The "BufferSize" input is too small
STATE_MACHINE_ERROR            16#0A0F0104 16#0C231000 Runtime error in function block:
                                  Invalid state of the state machine

### 21.5.13 IL_ValueLimit

Brief description
This function block limits a value to the range within the limits.

Interface description

Table 546: Interface variables of the IL_ValueLimit function block
              Name           Type   Comment
VAR_INPUT     Enable         BOOL   If TRUE, the "Value" is checked for its "LowWindow"
                                    and "HighWindow" limits and the "LowWindowActive"
                                    and "HighWindowActive" outputs are set accordingly
           Pause      BOOL          If TRUE, "InWindow", "LowWindowActive" and "High‐
                                    WindowActive" remain constant
           Value      LREAL         The current actual process value
           LowLimit LREAL           Lower limit value
           HighLimit LREAL          Upper limit value
VAR_OUTPUT InOpera‐   BOOL          If TRUE, the function block operates and the
           tion                     "InWindow", "LowWindowActive" and "HighWindowAc‐
                                    tive" outputs are valid
           Error      BOOL          Indicates that an error occurred in the function block
           ErrorID    ⮫ ERROR_CODE Error ID
           ErrorIdent ⮫ ERROR_STRUC For the error structure with further error classification,
                      T             see ⮫ Error codes on page 652
           InPause    BOOL          "Pause" is active and the values at "InWindow", "Low‐
                                    WindowActive" and "HighWindowActive" are frozen
           Output‐    LREAL         A value limited to the range between "LowLimit" and
           Value                    "HighLimit"
           LowLimi‐ BOOL            Active if "Value" ≤ "LowLimit"
           tActive
           HighLimi‐ BOOL           Active if "Value" ≥ "HighLimit"
           tActive

Table 547: Min./max. and default values of the IL_ValueLimit inputs
Name               Type        Min. value      Max. value    Default value   Applied
Enable             BOOL                                      FALSE           Continuous
Pause              BOOL                                      FALSE           Continuous
Value              LREAL       N. def.         N. def.       0.0             Continuous
LowLimit           LREAL       N. def.         < HighLimit   -10.0           Continuous
HighLimit          LREAL       > LowLimit      N. def.       10.0            Continuous

Functional description
The function block IL_ValueLimit compares the value of the "Value" input
with the limit values given in "LowLimit" and "HighLimit" and issues the lim‐
ited value of "Value" at "OutputValue". It is checked continuously when the
"Enable" input is set. All inputs are continuously processed.
LowLimitActive, HighLimitActive
The "LowLimitActive" and "HighLimitActive" outputs are set as follows:
● "LowLimitActive is set if "Value" is lower than or equal to "LowLimit".
● "HighLimitActive" is set if "Value" is greater than or equal to "HighLimit".
Pause, InPause
The "Pause" input is only evaluated when the "Enable" input is active. If
"Pause" is set, there is no comparison and the "OutputValue", "LowLimitAc‐
tive" and "HighLimitActive" outputs are not changed.
The "InPause" output is set when "Pause" is active.

Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:
Table 548: Generated error numbers of the IL_ValueLimit function block
ErrorID                        Additional1 Additional2 Description
INPUT_INVALID_ERROR            16#0A0F0104 16#0C23001A "LowLimit" is higher than "HighLimit"
STATE_MACHINE_ERROR            16#0A0F0104 16#0C231000 Runtime error in function block:
                                                       Invalid state of the state machine

### 21.5.14 IL_ValueWindow

Brief description
This function block checks whether a value is within the limits and issues the
results of this check. The value is not modified.

Interface description

Table 549: Interface variables of the IL_ValueWindow function block
              Name           Type              Comment
VAR_INPUT     Enable         BOOL              If TRUE, the "Value" is checked for its "LowWindow"
                                               and "HighWindow" limits and the "LowWindowActive"
                                               and "HighWindowActive" outputs are set accordingly
              Pause          BOOL              If TRUE, "InWindow", "LowWindowActive" and "High‐
                                               WindowActive" remain constant
           Value             LREAL             The current actual process value
           Low‐              LREAL             Lower limit value
           Window
           High‐             LREAL             Upper limit value

Window
VAR_OUTPUT InOpera‐          BOOL      If TRUE, the function block operates and the
tion                        "InWindow", "LowWindowActive" and "HighWindowAc‐
                 tive" outputs are valid
Error      BOOL          Indicates that an error occurred in the function block
ErrorID    ⮫ ERROR_CODE Error ID
ErrorIdent ⮫ ERROR_STRUC For the error structure with further error classification,
   T             see ⮫ Error codes on page 654
InPause    BOOL          "Pause" is active and the values at "InWindow", "Low‐
                 WindowActive" and "HighWindowActive" are frozen
InWindow BOOL            Active if "LowWindow" < "Value" < "HighWindow"
LowWindo‐ BOOL           Active if "Value" ≤ "LowWindow"
wActive
HighWin‐ BOOL            Active if "Value" ≥ "HighWindow"
dowActive

Table 550: Min./max. and default values of the IL_ValueWindow inputs
Name           Type             Min. value     Max. value     Default value   Applied
Enable         BOOL                                           FALSE           Continuous
Pause          BOOL                                           FALSE           Continuous
Value          LREAL            N. def.     N. def.           0.0             Continuous
LowWindow      LREAL            N. def.     < High‐           -10.0           Continuous
                                            Window
HighWindow     LREAL            > LowWindow N. def.           10.0            Continuous

Functional description
The function block IL_ValueWindow compares the values of the "Value“ input
with the limit values given in "LowWindow“ and "HighWindow“. It is checked
continuously when the "Enable" input is set. All inputs are continuously proc‐
essed.
InWindow, LowWindowActive, HighWindowActive
The "InWindow", "LowWindowActive" and "HighWindowActive" outputs are set
as follows:
● "InWindow" is set if "Value" is higher than "LowWindow" and smaller than
  "HighWindow".
● "LowWindowActive" is set if "Value" is lower than or equal to "Low‐
  Window".
● "HighWindowActive" is set if "Value" is higher than or equal to "High‐
  Window".
Pause, InPause

The "Pause" input is only evaluated when the "Enable" input is active. If
"Pause" is set, there is no comparison and the "InWindow", "LowWindowAc‐
tive" and "HighWindowActive” outputs are not changed.
The "InPause" output is set when "Pause" is active.

Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:
Table 551: Generated error numbers of the IL_ValueWindow function block
ErrorID                 Additional1 Additional2 Description
INPUT_INVALID_ERROR,    16#0A0F0104 16#0C23001b "LowWindow" is higher than "High‐
16#0001                                         Window"
STATE_MACHINE_ERROR,16# 16#0A0F0104 16#0C231000 Runtime error in function block:
0005                                            Invalid state of the state machine

## 21.6 Filter

### 21.6.1 Introduction and overview

The CXA_LoopControl provides the following filter function blocks:
Table 552: CXA_LoopControl filter
           Time-discrete                  Event-controlled              Description
⮫ Chapter 21.6.2 IL_FIRType01 ⮫ Chapter 21.6.3 IL_FIRType02 Digital FIR filter for high-pass,
on page 654                   on page 656                   low-pass and band-pass usage
⮫ Chapter 21.6.4 IL_IIRType01      ⮫ Chapter 21.6.5 IL_IIRType02   Digital IIR filter for high-pass,
on page 659                        on page 661                     low-pass and band-pass usage
⮫ Chapter 21.6.6 IL_StateVaria‐ ⮫ Chapter 21.6.7 IL_StateVaria‐ IIR filter (Infinite Impulse
bleType01 on page 663           bleType02 on page 665           Response) second order for
                                                                high-pass, low-pass and band-
                                                                pass use and as band-stop filter

### 21.6.2 IL_FIRType01

Brief description
The IL_FIRType01 function block implements a general time-discrete FIR filter.
This digital filter can be used for different high-pass, low-pass and band-pass
filters. The function block operates time-discretely.

Interface description

Table 553: Interface variables of the IL_FIRType01 function block
               Name          Type    Comment
VAR_INPUT      Enable        BOOL    If TRUE, "OutputValue" is set to the value computed
                                     with "StartValue"
           Pause      BOOL           Enables the Pause mode if TRUE
           Value      LREAL          The current actual process value
           StartValue LREAL          The initial value applied at a rising edge at "Enable" at
                                     the "OutputValue" output
           Coeffi‐    ⮫ IL_FIR_COEFF Structure with filter coefficients
           cients

VAR_OUTPUT InOpera‐   BOOL           If TRUE, the filter is working and the "OutputValue"
tion                      output is valid
Error      BOOL           Indicates that an error occurred in the function block
ErrorID    ⮫ ERROR_CODE Error ID
ErrorIdent ⮫ ERROR_STRUC For the error structure with further error classification,
           T             see ⮫ Error codes on page 656
InPause    BOOL          "Pause" is active and the value at "OutputValue" is
                         frozen
ActScan‐   LTIME         The time passed since the latest function block call
Time
Output‐    LREAL         The computed filter value
Value

Table 554: Min./max. and default values of the IL_FIRType01 inputs
Name           Type         Min. value        Max. value      Default value   Applied
Enable         BOOL                                           FALSE           Continuous
Pause          BOOL                                           FALSE           Continuous
Value          LREAL        N. def.           N. def.         0.0             Continuous
StartValue     LREAL        N. def.           N. def.         0.0             Rising edge at “Enable”
Coefficients   IL_FIR_COEFF                                                   Rising edge at “Enable”

      Functional description
      The IL_FIRType01 function block implements a general time-discrete FIR filter.
      This digital filter can be used for different high-pass, low-pass and band-pass
      filters. The function block operates time-discretely.
      Value, StartValue, OutputValue
      The "Value" input contains the input value of the filter. This value is processed
      at each call if "InOperation" is set. At a rising edge at "Enable", the value in
      "StartValue" is applied to all internal registers. If "Enable" is set and "InPause"
      is not set, the result is output at the "OutputValue" output.
      Coefficients
      The filter response is defined using the "Coefficients" input. This data struc‐
      ture consists of the "NumberOfCoeffs" entry for the number of coefficients
      and the "Coeffs" array for the individual coefficients a0 to a15.

Pause, InPause
The "Pause" input is only analyzed when the "Enable" input is active. If
"Pause" is TRUE, it is not computed and the value of "OutputValue" is not
changed. The internal registers are also frozen.
The "InPause" output is set when "Pause" is active.
The "ActScanTime" output is still updated.

Time response
The IL_FIRType01 function block operates asynchronously. After the start due
to a rising edge at the "Enable" input, it reads the "Coefficients" input and
the internal registers are loaded with "StartValue". At each call, the function
block reads a value from the "Value" input and computes a new value at the
"OutputValue" output. If the filter is active, the "InOperation" output is set. If
an error occurs, the "Error" output is set.

Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:
Table 555: Generated error numbers of the IL_FIRType01 function block
ErrorID                        Additional1 Additional2 Description
INPUT_RANGE_ERROR              16#0A0F0104 16#0C230021 The "NumberOfCoeffs" entry of the
                                                       "Coefficients" input is invalid
STATE_MACHINE_ERROR            16#0A0F0104 16#0C231000 Runtime error in function block:
                                                       Invalid state of the state machine

### 21.6.3 IL_FIRType02

Brief description
The IL_FIRType02 function block implements a general event-controlled FIR
filter. This digital filter can be used for different high-pass, low-pass and band-
pass filters. This function block operates event-controlled. Thus, a new value
is processed when the "Step" input is changed.

      Interface description

Table 556: Interface variables of the IL_FIRType02 function block
               Name          Type    Comment
VAR_INPUT      Enable        BOOL    If TRUE, "OutputValue" is set to the value computed
                                     with "StartValue"
           Pause      BOOL           Enables the Pause mode if TRUE
           Step       UINT           Processing step. A change triggers the processing of a
                                     new signal value
           Value      LREAL          The current actual process value
           StartValue LREAL          The initial value applied at a rising edge at "Enable" at
                                     the "OutputValue" output
           Coeffi‐    ⮫ IL_FIR_COEFF Structure with filter coefficients
           cients
VAR_OUTPUT InOpera‐   BOOL           If TRUE, the filter is working and the "OutputValue"
           tion                      output is valid
           Error      BOOL           Indicates that an error occurred in the function block
           ErrorID    ⮫ ERROR_CODE Error ID
               ErrorIdent ⮫ ERROR_STRUC For the error structure with further error classification,
                          T             see ⮫ Error codes on page 658
               InPause    BOOL          "Pause" is active and the value at "OutputValue" is
                                        frozen
               ActStep    UINT          Latest step processed
               Output‐    LREAL         The computed filter value
               Value

Table 557: Min./max. and default values of the IL_FIRType02 inputs
Name           Type         Min. value        Max. value      Default value   Applied
Enable         BOOL                                           FALSE           Continuous
Pause          BOOL                                           FALSE           Continuous
Step           UINT         0                 65535           0               Continuous
Value          LREAL        N. def.           N. def.         0.0             Continuous
StartValue     LREAL        N. def.           N. def.         0.0             Rising edge at “Enable”
Coefficients   IL_FIR_COEFF                                                   Rising edge at “Enable”

      Functional description
      The IL_FIRType02 function block implements a general event-controlled FIR
      filter. This digital filter can be used for different high-pass, low-pass and band-
      pass filters. This function block operates event-controlled. Thus, a new value

is processed when the "Step" input is changed. The amount of value change
at the "Step" input is not important, since one filter iteration is executed each
time.
Value, StartValue, OutputValue
The "Value" input contains the input value of the filter. This value is processed
at each call if "InOperation" is set. At a rising edge at "Enable", the value in
"StartValue" is applied to all internal registers. If "Enable" is set and "InPause"
is not set, the result is output at the "OutputValue" output.
Coefficients
The filter response is defined using the "Coefficients" input. This data struc‐
ture consists of the "NumberOfCoeffs" entry for the number of coefficients
and the "Coeffs" array for the individual coefficients a0 to a15.

Pause, InPause
The "Pause" input is only analyzed when the "Enable" input is active. If
"Pause" is TRUE, it is not computed and the value of "OutputValue" is not
changed. The internal registers are also frozen.
The "InPause" output is set when "Pause" is active.
The "ActStep" output is still updated.

Time response
The IL_FIRType02 function block operates asynchronously. After the start due
to a rising edge at the "Enable" input, it reads the "Coefficients" input. With
each change at the "Step" input, the function block reads a new value from
the "Value" input and computes a new value at the "OutputValue" output. If
the signal generation is active, the "InOperation" output is set. If an error
occurs, the "Error" output is set.

Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:
Table 558: Generated error numbers of the IL_FIRType02 function block
ErrorID                        Additional1 Additional2 Description
INPUT_RANGE_ERROR              16#0A0F0104 16#0C230021 The "NumberOfCoeffs" entry of the
                                                       "Coefficients" input is invalid
STATE_MACHINE_ERROR            16#0A0F0104 16#0C231000 Runtime error in function block:
                                                       Invalid state of the state machine

### 21.6.4 IL_IIRType01

      Brief description
      The IL_IIRType01 function block implements a general time-discrete IIR filter
      (Infinite Impulse Response). This digital filter can be used for example for
      Chebyshev, Butterworth and Bessel filters. The function block operates time-
      discretely.

      Interface description

Table 559: Interface variables of the IL_IIRType01 function block
               Name          Type    Comment
VAR_INPUT      Enable        BOOL    If TRUE, "OutputValue" is set to the value computed
                                     with "StartValue"
           Pause      BOOL           Enables the Pause mode if TRUE
           Value      LREAL          The current actual process value
           StartValue LREAL          The initial value applied at a rising edge at "Enable" at
                                     the "OutputValue" output
           Coeffi‐    ⮫ IL_FIR_COEFF Structure with filter coefficients
           cients
VAR_OUTPUT InOpera‐   BOOL           If TRUE, the filter is working and the "OutputValue"
           tion                      output is valid
           Error      BOOL           Indicates that an error occurred in the function block
           ErrorID    ⮫ ERROR_CODE Error ID
               ErrorIdent ⮫ ERROR_STRUC For the error structure with further error classification,
                          T             see ⮫ Error codes on page 660
               InPause    BOOL          "Pause" is active and the value at "OutputValue" is
                                        frozen
               ActScan‐   LTIME         The time passed since the latest function block call
               Time
               Output‐    LREAL         The computed filter value
               Value

Table 560: Min./max. and default values of the IL_IIRType01 inputs
Name           Type         Min. value       Max. value      Default value   Applied
Enable         BOOL                                          FALSE           Continuous
Pause          BOOL                                          FALSE           Continuous
Value          LREAL        N. def.          N. def.         0.0             Continuous
StartValue     LREAL        N. def.          N. def.         0.0             Rising edge at “Enable”
Coefficients   IL_IIR_COEFF                                                  Rising edge at “Enable”

Functional description
The IL_IIRType01 function block implements a general time-discrete IIR filter.
This digital filter can be used for example for Chebyshev, Butterworth and
Bessel filters. The function block operates time-discretely.
Value, StartValue, OutputValue
The "Value" input contains the input value of the filter. This value is processed
at each call if "InOperation" is set. At a rising edge at "Enable", the value in
"StartValue" is applied to all internal registers. If "Enable" is set and "InPause"
is not set, the result is output at the "OutputValue" output.
Coefficients
The filter response is defined via the "Coefficients" input. This data structure
consists of the "NumberOfCoeffs" entry for the number of coefficients and
the "FowardCoeffs" a0 to a15 array and "BackwardCoeffs" b1 to b15 for the
individual coefficients. The "ForwardCoeffs" array contains one entry more
than the "BackwardCoeffs" array.

Pause, InPause
The "Pause" input is only analyzed when the "Enable" input is active. If
"Pause" is TRUE, it is not computed and the value of "OutputValue" is not
changed. The internal registers are also frozen.
The "InPause" output is set when "Pause" is active.
The "ActScanTime" output is still updated.

Time response
The IL_IIRType01 function block operates asynchronously. After the start due
to a rising edge at the "Enable" input, it reads the "Coefficients" input and
the internal registers are loaded with "StartValue". At each call, the function
block reads a value from the "Value" input and computes a new value at the
"OutputValue" output. If the filter is active, the "InOperation" output is set. If
an error occurs, the "Error" output is set.

Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:

Table 561: Generated error numbers of the IL_IIRType01 function block
ErrorID                        Additional1 Additional2 Description
INPUT_RANGE_ERROR              16#0A0F0104 16#0C230021 The "NumberOfCoeffs" entry of the
                                                       "Coefficients" input is invalid
STATE_MACHINE_ERROR            16#0A0F0104 16#0C231000 Runtime error in function block:
                                                       Invalid state of the state machine

### 21.6.5 IL_IIRType02

Brief description
The IL_IIRType02 function block implements a general event-controlled IIR

filter. This digital filter can be used for different high-pass, low-pass and band-
pass filters. This function block operates event-controlled. Thus, a new value
is processed when the "Step" input is changed.

Interface description

Table 562: Interface variables of the IL_IIRType02 function block
              Name           Type    Comment
VAR_INPUT     Enable         BOOL    If TRUE, "OutputValue" is set to the value computed
                                     with "StartValue"
           Pause      BOOL           Enables the Pause mode if TRUE
           Step       UINT           Processing step. A change triggers the processing of a
                                     new signal value
           Value      LREAL          The current actual process value
           StartValue LREAL          The initial value applied at a rising edge at "Enable" at
                                     the "OutputValue" output
           Coeffi‐    ⮫ IL_FIR_COEFF Structure with filter coefficients
           cients
VAR_OUTPUT InOpera‐   BOOL           If TRUE, the filter is working and the "OutputValue"
           tion                      output is valid
           Error      BOOL           Indicates that an error occurred in the function block
           ErrorID    ⮫ ERROR_CODE Error ID
              ErrorIdent ⮫ ERROR_STRUC For the error structure with further error classification,
                         T             see ⮫ Error codes on page 663
              InPause    BOOL          "Pause" is active and the value at "OutputValue" is
                                       frozen
              ActStep    UINT          Latest step processed
              Output‐    LREAL         The computed filter value
              Value

Table 563: Min./max. and default values of the IL_IIRType02 inputs
Name               Type         Min. value      Max. value      Default value   Applied
Enable             BOOL                                         FALSE           Continuous
Pause              BOOL                                         FALSE           Continuous
Step               UINT                                         0               Continuous
Value              LREAL        N. def.         N. def.         0.0             Continuous
StartValue         LREAL        N. def.         N. def.         0.0             Rising edge at “Enable”
Coefficients       IL_IIR_COEFF                                                 Rising edge at “Enable”

Functional description
The IL_IIRType02 function block implements a general event-controlled IIR
filter. This digital filter can be used for different high-pass, low-pass and band-
pass filters. This function block operates event-controlled. Thus, a new value
is processed when the "Step" input is changed. The amount of value change
at the "Step" input is not important, since one filter iteration is executed each
time.
Value, StartValue, OutputValue
The "Value" input contains the input value of the filter. This value is processed
at each call if "InOperation" is set. At a rising edge at "Enable", the value in
"StartValue" is applied to all internal registers. If "Enable" is set and "InPause"
is not set, the result is output at the "OutputValue" output.
Coefficients
The filter response is defined via the "Coefficients" input. This data structure
consists of the "NumberOfCoeffs" entry for the number of coefficients and
the "FowardCoeffs" a0 to a15 array and "BackwardCoeffs" b1 to b15 for the
individual coefficients. The "ForwardCoeffs" array contains one entry more
than the "BackwardCoeffs" array.

Pause, InPause
The "Pause" input is only analyzed when the "Enable" input is active. If
"Pause" is TRUE, it is not computed and the value of "OutputValue" is not
changed. The internal registers are also frozen.
The "InPause" output is set when "Pause" is active.

The "ActStep" output is still updated.

Time response
The IL_IIRType02 function block operates asynchronously. After the start due
to a rising edge at the "Enable" input, it reads the "Coefficients" input and
the internal registers are loaded with "StartValue". At each call, the function
block reads a value from the "Value" input and computes a new value at the
"OutputValue" output. If the filter is active, the "InOperation" output is set. If
an error occurs, the "Error" output is set.

Error codes

The function block uses the error table F_RELATED_TABLE, 16#0170.
It can generate the following error messages in Additional1/Additional2:
Table 564: Generated error numbers of the IL_IIRType02 function block
ErrorID                         Additional1 Additional2 Description
INPUT_RANGE_ERROR               16#0A0F0104 16#0C230021 The "NumberOfCoeffs" entry of the
                                                        "Coefficients" input is invalid.
STATE_MACHINE_ERROR             16#0A0F0104 16#0C231000 Runtime error in function block:
                                                        Invalid state of the state machine.

### 21.6.6 IL_StateVariableType01

Brief description
The IL_StateVariableType01 function block implements a special time-discrete
IIR filter (Infinite Impulse Response) of second order. This digital filter can be
used as high-pass, band-pass or band-stop filter. The function block operates
time-discretely.

Interface description

Table 565: Interface variables of the IL_StateVariableType01 function block
              Name           Type            Comment
VAR_INPUT     Enable         BOOL            If TRUE, "OutputValue" is set to the value computed
                                             with "StartValue"
              Pause      BOOL                Enables the Pause mode if TRUE
              Value      LREAL               The current actual process value
              StartValue LREAL               The initial value applied at a rising edge at "Enable" at
                                             the "OutputValue" output
              TControl       LTIME           Time constant
              Damping‐       LREAL           Damping factor
              Factor

Name       Type                        Comment
FilterType ⮫ IL_FILTER_TYP             Filter type
   E
VAR_OUTPUT InOpera‐   BOOL                        If TRUE, the filter is working and the "OutputValue"
tion                                   output is valid
Error      BOOL                        Indicates that an error occurred in the function block
ErrorID    ⮫ ERROR_CODE                Error ID
ErrorIdent ⮫ ERROR_STRUC For the error structure with further error classification,
           T             see ⮫ Error codes on page 665
InPause    BOOL          "Pause" is active and the value at "OutputValue" is
                         frozen
ActScan‐   LTIME         The time passed since the latest function block call
Time
Output‐    LREAL         The computed filter value
Value

Table 566: Min./max. and default values of the IL_StateVariableType01 inputs
Name               Type           Min. value       Max. value     Default value   Applied
Enable             BOOL                                           FALSE           Continuous
Pause              BOOL                                           FALSE           Continuous
Value              LREAL          N. def.          N. def.        0.0             Continuous
StartValue         LREAL          N. def.          N. def.        0.0             Rising edge at “Enable”
TControl           LTIME          >0s              N. def.        1 ms            Continuous
Damping‐           LREAL          0.0                             1.0             Continuous
Factor
FilterType         IL_FILTER_TY                                   IL_LOWPASS Rising edge at “Enable”
                   PE

      Functional description
  The IL_StateVariableType01 function block implements a special time-discrete
  IIR filter (Infinite Impulse Response) of second order. This digital filter can be
  used as high-pass, band-pass or band-stop filter. The function block operates
  time-discretely.
  Value, StartValue, OutputValue
  The "Value" input contains the input value of the filter. This value is processed
  upon each call if "InOperation" is set. The value in "StartValue" is applied
  to all internal registers at a rising edge at "Enable”. If "Enable" is set and
  "InPause" is not set, the result is output at the "OutputValue" output.
  TControl, DampingFactor, FilterType
  The "FilterType“ input indicates the filter to be computed. There are the
  following filter types: IL_LOWPASS, IL_HIGHPASS, IL_BANDPASS, IL_BANDRE‐
  JECT.
  Depending on the type of filter, the inputs "TControl“ and "Damping‐
  Factor“ are interpreted:
Table 567: Interpretation of the input values according to the filter type set
FilterType              1/TControl                                DampingFactor
IL_LOWPASS              Cut-off frequency suppressed above        DampingFactor<1: Overshooting,
                        the frequencies                           DampingFactor=1: Critical damping
IL_HIGHPASS             Cut-off frequency suppressed below        DampingFactor>1: No overshooting
                        the frequencies

FilterType           1/TControl                               DampingFactor
                                         Amplitude at cut-off frequency =
                                         damping factor0.5
IL_BANDPASS          Center frequency of the band pass        Amplitude at center frequency =
                                         damping factor0.5
IL_BANDREJECT        Center frequency of the band-stop        Cut-off frequency = center fre‐
filter                                   quency*(1±DampingFactor/2)
Pause
The "Pause" input is only evaluated when the "Enable" input is active. If
"Pause" is TRUE, it is not computed and the value of "OutputValue" is not
changed. The internal integrator is also frozen.

The "InPause" output is set when "Pause" is active.
The "ActScanTime" output is still updated.

Time response
The IL_StateVariableType01 function block operates asynchronously. After the
start due to a rising edge at the "Enable" input, it reads the "StartValue" input.
Upon each call, the function block reads a value from the inputs "Value",
"TControl" and "DampingFactor" and computes a new value at the "Output‐
Value" output. If the filter is active, the "InOperation" output is set. If an error
occurs, the "Error" output is set.

Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:

Generated error numbers of the IL_StateVariableType01 function block
Table 568: Generated error numbers of the IL_StateVariableType01 function block
ErrorID                        Additional1 Additional2 Description
INPUT_RANGE_ERROR              16#0A0F0104 16#0C230022 The value specified at the "FilterType"
                                                       input is invalid
INPUT_RANGE_ERROR              16#0A0F0104 16#0C230023 The "TControl" input is invalid
INPUT_RANGE_ERROR              16#0A0F0104 16#0C230024 The "DampingFactor" input is invalid
OTHER_ERROR                    16#0A0F0104 16#0C230025 The output is "Infinity" or "NaN"

### 21.6.7 IL_StateVariableType02

Brief description
The IL_StateVariableType02 function block implements a special event-con‐
trolled IIR filter (Infinite Impulse Response) of second order. This digital filter
can be used as high-pass, band-pass or band-stop filter. This function block
operates event-controlled. That means that a new value is processed when the
"Step" input is changed.

      Interface description

Table 569: Interface variables of the IL_StateVariableType02 function block
                   Name       Type               Comment
VAR_INPUT          Enable     BOOL               If TRUE, "OutputValue" is set to the value computed
                                                 with "StartValue"
                   Pause      BOOL               Enables the Pause mode if TRUE
                   Value      LREAL              The current actual process value
                   StartValue LREAL              The initial value applied at a rising edge at "Enable" at
                                                 the "OutputValue" output
           TControl   LREAL                      Time constant
           Damping‐ LREAL                        Damping factor
           Factor
           FilterType ⮫ IL_FILTER_TYP            Filter type
                      E
VAR_OUTPUT InOpera‐   BOOL                       If TRUE, the filter is working and the "OutputValue"
           tion                                  output is valid
           Error      BOOL                       Indicates that an error occurred in the function block
           ErrorID    ⮫ ERROR_CODE               Error ID
                   ErrorIdent ⮫ ERROR_STRUC For the error structure with further error classification,
                              T             see ⮫ Error codes on page 667
                   InPause    BOOL          "Pause" is active and the value at "OutputValue" is
                                            frozen
                   ActStep    UINT          Step to which "OutputValue" refers
                   Output‐    LREAL         The computed filter value
                   Value

Table 570: Min./max. and default values of the IL_StateVariableType02 inputs
Name               Type           Min. value      Max. value     Default value   Applied
Enable             BOOL                                          FALSE           Continuous
Pause              BOOL                                          FALSE           Continuous
Value              LREAL          N. def.         N. def.        0.0             Continuous
StartValue         LREAL          N. def.         N. def.        0.0             Rising edge at “Enable”
TControl           LREAL          > 0.0           N. def.        1               Continuous
Damping‐           LREAL          0.0                            1.0             Continuous
Factor
FilterType         IL_FILTER_TY                                  IL_LOWPASS Rising edge at “Enable”
                   PE

Functional description
The IL_StateVariableType02 function block implements a special event-con‐
trolled IIR filter (Infinite Impulse Response) of second order. This digital filter
can be used as high-pass, band-pass or band-stop filter. This function block
operates event-controlled. That means that a new value is processed when the
"Step" input is changed.
Value, StartValue, OutputValue
The "Value" input contains the input value of the filter. This value is processed
upon each call if "InOperation" is set. The value in "StartValue" is applied
to all internal registers at a rising edge at "Enable”. If "Enable" is set and
"InPause" is not set, the result is output at the "OutputValue" output.

TControl, DampingFactor, FilterType
The "FilterType“ input indicates the filter to be computed. There are the
following filter types: IL_LOWPASS, IL_HIGHPASS, IL_BANDPASS, IL_BANDRE‐
JECT.
Depending on the type of filter, the inputs "TControl“ and "Damping‐
Factor“ are interpreted:
Table 571: Interpretation of the input values according to the filter type set
FilterType           1/TControl                               DampingFactor
IL_LOWPASS           Cut-off frequency suppressed above       DampingFactor<1: Overshooting
                     the frequencies                          DampingFactor=1: Critical damping
IL_HIGHPASS          Cut-off frequency suppressed below       DampingFactor>1: No overshooting
                     the frequencies
IL_BANDPASS          Center frequency of the band pass        Band width = 2*DampingFactor/TCon‐
IL_BANDREJECT        Center frequency of the band-stop        trol
                     filter
                     Pause
                     The "Pause" input is only evaluated when the "Enable" input is active. If
                     "Pause" is TRUE, it is not computed and the value of "OutputValue" is not
                     changed. The internal integrator is also frozen.
                     The "InPause" output is set when "Pause" is active.
                     The "ActStep" output is still updated.

Time response
The IL_StateVariableType02 function block operates asynchronously. After the
start due to a rising edge at the "Enable" input, it reads the "StartValue" input.
At each "Step" input change, the function block reads a new value from the
inputs "Value", "TControl" and "DampingFactor" and computes a new value at
the "OutputValue" output. If the filter is active, the "InOperation" output is
set. If an error occurs, the "Error" output is set.

Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:

Table 572: Generated error numbers of the IL_StateVariableType02 function block
ErrorID                        Additional1 Additional2 Description
INPUT_RANGE_ERROR              16#0A0F0104 16#0C230022 The value specified at the "FilterType"
                                                       input is invalid
INPUT_RANGE_ERROR              16#0A0F0104 16#0C230023 The "TControl" input is invalid
INPUT_RANGE_ERROR              16#0A0F0104 16#0C230024 The "DampingFactor" input is invalid

ErrorID                          Additional1 Additional2 Description
OTHER_ERROR                      16#0A0F0104 16#0C230025 The output is "Infinity" or "NaN"

### 21.6.8 IL_FILTER_TYPE

The enumeration type IL_FILTER_TYPE defines several basic filter types.
Table 573: Elements of the IL_FILTER_TYPE enumeration type
Element                    Value                     Description
IL_LOWPASS                 1                         Low-pass
IL_HIGHPASS                2                         High-pass
IL_BANDPASS                3                         Band-pass
IL_BANDREJECT              4                         Band-stop filter

Used in
● ⮫ Chapter 21.6.6 IL_StateVariableType01 on page 663
● ⮫ Chapter 21.6.7 IL_StateVariableType02 on page 665

### 21.6.9 IL_FIR_COEFF

The IF_FIR_COEFF data type sets the filter coefficients.
Table 574: IL_FIR_COEFF data structure
Structural ele‐     Type                      Min.        Max.    Default    Description
ment                                          value       value
Coeffs              ARRAY[0..15] OF LREAL                         16(0.0)    Filter coefficients
NumberOfOeffs       UINT                  1               15      1          Number of filter coeffi‐
                                                                             cients

Used in
● ⮫ Chapter 21.6.2 IL_FIRType01 on page 654,
● ⮫ Chapter 21.6.3 IL_FIRType02 on page 656.

### 21.6.10 IL_IIR_COEFF

The IF_IIR_COEFF data type sets the filter coefficients.
Table 575: IL_IIR_COEFF data structure
Structural ele‐     Type                      Min.        Max.    Default    Description
ment                                          value       value
ForwardCoeffs       ARRAY[0..15] OF LREAL                         16(0.0)    Filter coefficients of the
                                                                             forward path
BackwardCoeffs ARRAY[1..15] OF LREAL                              15(0.0)    Filter coefficients of the
                                                                             feedback loop
NumberOfOeffs       UINT                      1           15      1          Number of filter coeffi‐
                                                                             cients

Used in
● ⮫ Chapter 21.6.4 IL_IIRType01 on page 659,
● ⮫ Chapter 21.6.5 IL_IIRType02 on page 661.

## 21.7 Generators

### 21.7.1 Introduction and overview

This section contains the signal generators of the CXA_LoopControl. Genera‐
tors are signal sources.

The CXA_LoopControl provides the following signal generators:
Table 576: CXA_LoopControl signal generators
         Time-discrete                   Event-controlled                   Description
                                           Generators
⮫ Chapter 21.7.2 IL_NoiseGe‐                                      Pseudorandom number and
neratorType01 on page 669                                         noise generator
⮫ Chapter 21.7.3 IL_NoiseGe‐                                      Noise generator for white noise
neratorType02 on page 671
⮫ Chapter 21.7.4 IL_PRBSGe‐       ⮫ Chapter 21.7.5 IL_PRBSGe‐     Generator for pseudorandom
neratorType01 on page 672         neratorType02 on page 674       binary numbers

              Generators/SignalGenerators
⮫ Chapter 21.7.6 IL_AngleGe‐      ⮫ Chapter 21.7.7 IL_AngleGe‐    Angle generator
neratorType01 on page 676         neratorType02 on page 677
⮫ Chapter 21.7.8 IL_PhaseController on page 679                   Phase controller
⮫ Chapter 21.7.9 IL_SignalGe‐     ⮫ Chapter 21.7.10 IL_SignalGe‐ Signal generator
neratorType01 on page 681         neratorType02 on page 685
⮫ Chapter 21.7.11                 ⮫ Chapter 21.7.12              Amplitude controller
IL_AmplitudeControllerType01      IL_AmplitudeControllerType02
on page 689                       on page 693
The     signal    generator   function   blocks    IL_NoiseGeneratorType01,
IL_NoiseGeneratorType02 and IL_PRBSGeneratorType0x are stand-alone func‐
tion blocks and can directly be used. They have an "OutputValue" output, but
no "Value" input.
The     function    blocks   IL_AngleGeneratorType0x,    IL_PhaseController,
IL_SignalGeneratorType0x and IL_AmplitudeControllerType0x belong together
and can be interconnected as follows:

### 21.7.2 IL_NoiseGeneratorType01

Brief description
This function block generates an equally-distributed noise signal with select‐
able amplitude based on a pseudorandom number.

      Interface description

Table 577: Interface variables of the IL_NoiseGeneratorType01 function block
           Name               Type                Comment
VAR_INPUT Enable              BOOL                Function block processing enabled
           Amplitude          LREAL               Amplitude of the noise signal
           Seed               UDINT               Initial value, 0 for CPU tick
VAR_OUTPUT InOpera‐           BOOL                The function block operates. The outputs are valid
           tion
           Error              BOOL          Indicates that an error occurred in the function block
           ErrorID            ⮫ ERROR_CODE Error ID
                   ErrorIdent ⮫ ERROR_STRUC For the error structure with further error classification,
                              T             see ⮫ Error codes on page 670
                   ActScan‐   LTIME         Measured call cycle time
                   Time
                   Output‐    LREAL         Generated pseudorandom number
                   Value

Table 578: Min./max. and default values of the IL_NoiseGeneratorType01 inputs
Name               Type           Min. value      Max. value     Default value   Applied
Enable             BOOL                                          FALSE           Continuous
Amplitude          LREAL          0.0             N. def.        1.0             Continuous
Seed               UDINT          0               232-1          0               Rising edge at Enable

      Functional description
      The IL_NoiseGeneratorType01 function block generates an equally-distributed
      noise signal based on pseudorandom numbers. At a rising edge at "Enable",
      the value is read at the "Seed" input. If "Seed" is 0, the current CPU counter
      is used for initialization purposes. All other values at "Seed" are directly used
      as initial value. If "InOperation" is set, the function block generates a new
      value between 0.0 and "Amplitude" at "OutputValue" upon each call. Call this
      function block cyclically. The measured call cycle is output in "ActScanTime".
      "OutputValue" contains the noise signal generated.
      The random numbers created are equally-distributed within the range
      between 0 and "Amplitude".
      It is processed continuously when the "Enable" input is set.

      Error codes
      The function block uses the error table CXA_TABLE, 16#0001.
      It can generate the following error messages in Additional1/Additional2:

Table 579: Generated error numbers of the IL_NoiseGeneratorType01 function block
ErrorID                          Additional1 Additional2 Description
INPUT_INVALID_ERROR              16#0A0F010 16#0C23003 "Amplitude" is smaller than 0.0
                                 4           1
STATE_MACHINE_ERROR              16#0A0F010 16#0C23100 Runtime error in function block:
                                 4           0           Invalid state of the state machine

### 21.7.3 IL_NoiseGeneratorType02

Brief description
The IL_NoiseGeneratorType02 function block generates a noise signal around

a specified mean value that is Gaussian-distributed in the amplitude. This
signal is a white noise, i.e. all frequencies are in the same amplitude. Addi‐
tionally, it is DC-free. This function block operates time-discretely.

Interface description

Table 580: Interface variables of the IL_NoiseGeneratorType02 function block
           Name              Type            Comment
VAR_INPUT Enable             BOOL            Function block processing enabled
           Amplitude         LREAL           Mean signal amplitude
           Sigma             LREAL           Default signal deviation
           Seed              UDINT           Initial value, 0 for CPU tick
VAR_OUTPUT InOpera‐          BOOL            The function block operates and the outputs are valid.
           tion
           Error             BOOL      Indicates that an error occurred in the function block
           ErrorID       ⮫ ERROR_CODE Error ID
              ErrorIdent ⮫ ERROR_STRUC For the error structure with further error classification,
                         T             see ⮫ Error codes on page 672
              ActScan‐   LTIME         Measured call cycle time.
              Time
              Output‐    LREAL         Generated noise signal.
              Value

Table 581: Min./max. and default values of the IL_NoiseGeneratorType02 inputs
Name           Type             Min. value   Max. value     Default value   Applied
Enable         BOOL                                         FALSE           Continuous
Amplitude      LREAL            0.0          N. def.        1.0             Rising edge at Enable
Sigma          LREAL            >0.0                        1.0             Rising edge at Enable
Seed           UDINT            0            232-1          0               Rising edge at Enable

Functional description
The IL_NoiseGeneratorType02 function block generates a noise signal that is
Gaussian-distributed in the amplitude. This signal is a white noise, i.e. all fre‐
quencies are in the same amplitude. Additionally, it is DC-free. This function
block operates time-discretely.
Amplitude, sigma:
The "Amplitude" input defines the mean amplitude of the generated signal
also called µ or expected value. The generated signal fluctuates around this
value. The "Sigma" input indicates the default variation, also called σ.
This results in the following value distribution:
68.3 % in the interval µ±σ
95.4 % in the interval µ±2σ
99.7 % in the interval µ±3σ
Seed:
This input is used as internal random seed. It can be generally omitted.
Time response:
The IL_NoiseGeneratorType02 function block operates asynchronously. It
reads the inputs "Amplitude", "Sigma" and "Seed” after the start due to a
rising edge at the "Enable" input. The function block generates a new value at
the "OutputValue" output upon each call. If the signal generation is active, the
"InOperation" output is set. If an error occurs, the "Error" output is set.

Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:
Table 582: Generated error numbers of the IL_NoiseGeneratorType02 function block
ErrorID                              Additional1 Additional2 Description
INPUT_INVALID_ERROR                  16#0A0F010 16#0C23003 "Sigma" input is smaller or equal to
                                     4           2           0.0
STATE_MACHINE_ERROR                  16#0A0F010 16#0C23100 Runtime error in function block:
                                     4           0           Invalid state of the state machine

### 21.7.4 IL_PRBSGeneratorType01

Brief description
The IL_PRBSGeneratorType01 function block generates a pseudo noise signal.
This signal is almost a white noise, i.e. all frequencies are of the same ampli‐
tude. Additionally, it is almost DC-free. This function block operates time-dis‐
cretely.

Interface description

Table 583: Interface variables of the IL_PRBSGeneratorType01 function block
           Name              Type             Comment
VAR_INPUT Enable             BOOL             Function block processing enabled
           Pause             BOOL             Aborts the signal generation
           Register‐         UINT             Length of the internal shift register
           Length
VAR_OUTPUT InOpera‐          BOOL             The function block operates. The outputs are valid
           tion
           Error             BOOL      Indicates that an error occurred in the function block
           ErrorID       ⮫ ERROR_CODE Error ID

ErrorIdent ⮫ ERROR_STRUC For the error structure with further error classification,
    T             see ⮫ Error codes on page 674
InPause    BOOL          Processing interrupted
ActScan‐   LTIME         Measured call cycle time
Time
Output‐    BOOL          Generated pseudorandom number
Value

Table 584: Min./max. and default values of the IL_PRBSGeneratorType01 inputs
Name           Type            Min. value      Max. value      Default value   Applied
Enable         BOOL                                            FALSE           Continuous
Pause          BOOL                                            FALSE           Continuous
Register‐      UINT            4               32              4               Rising edge at Enable
Length

Functional description
The IL_PRBSGeneratorType01 function block generates a pseudo noise signal.
This signal is almost a white noise, i.e. all frequencies are of the same ampli‐
tude. Additionally, it is almost DC-free. This function block operates time-dis‐
cretely.
The generated signal is repeated after n cycles. The number of cycles depends
on the register depth.
RegisterLength:
"RegisterLength" sets the depth of the internal shift register used for signal
generation. The register depth does not affect the signal quality generated. A
higher register depth generates a longer cycle before the signal is repeated.
The following table shows the signal period depending on the "Register‐
Length":
  RegisterLength          Period             RegisterLength          Period
                                                          17              131071
                 2                    3                   18              262143
                 3                    7                   19              524287
                 4                   15                   20            1048575
                 5                   31                   21            2097151
                 6                   63                   22            4194303
                 7                  127                   23            8388607
                 8                  255                   24           16777215
                 9                  511                   25           33554431
                10                 1023                   26           67108863

  RegisterLength          Period           RegisterLength           Period
               11                2047                   27           134217727
               12                4095                   28           268435455
               13                8191                   29           536870911
               14               16383                   30          1073741823
               15               32767                   31          2147483647
               16               65535                   32          4294967295
"RegisterLength" may only contain the values listed in the table.
Pause, InPause:
The function block processing can be temporarily paused with the "Pause"
input. If "Pause" is active, the "InPause" output is set. In this mode, no new
signal values are generated at the "OutputValue".
Time response:
The IL_PRBSGeneratorType01 function block operates asynchronously. After
the start due to a rising edge at the "Enable" input, it reads the "Register‐
Length" input. The function block generates a new value at the "OutputValue"
output upon each call. If the signal generation is active, the "InOperation"
output is set. If an error occurs, the "Error" output is set.

Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:
Table 585: Generated error numbers of the IL_PRBSGeneratorType01 function block
ErrorID                              Additional1 Additional2 Description
INPUT_INVALID_ERROR                  16#0A0F010 16#0C23003 The "RegisterLength" input is invalid
                                     4           3
STATE_MACHINE_ERROR                  16#0A0F010 16#0C23100 Runtime error in function block:
                                     4           0           Invalid state of the state machine

### 21.7.5 IL_PRBSGeneratorType02

Brief description
The IL_PRBSGeneratorType02 function block generates a pseudo noise signal.
This signal is almost a white noise which means that all frequencies are in
the same amplitude. Additionally, it is almost DC-free. This function block
operates event-controlled. That means that a new value is generated when the
"Step" input is changed.

Interface description

Table 586: Interface variables of the IL_PRBSGeneratorType02 function block
           Name              Type              Comment
VAR_INPUT Enable             BOOL              Function block processing enabled
           Pause             BOOL              Aborts the signal generation
           Step              UINT              Processing step. A change triggers a new signal value
           Register‐         UINT              Length of the internal shift register
           Length
VAR_OUTPUT InOpera‐          BOOL              The function block operates. The outputs are valid
           tion
           Error             BOOL      Indicates that an error occurred in the function block

ErrorID       ⮫ ERROR_CODE Error ID
ErrorIdent ⮫ ERROR_STRUC For the error structure with further error classification,
   T             see ⮫ Error codes on page 676
InPause    BOOL          Processing interrupted
ActStep    UINT          Latest step processed
Output‐    BOOL          Generated pseudo noise signal
Value

Table 587: Min./max. and default values of the IL_PRBSGeneratorType02 inputs
Name           Type            Min. value      Max. value      Default value Applied
Enable         BOOL                                            FALSE         Continuous
Pause          BOOL                                            FALSE         Continuous
                                                                             if "Enable" is set
Step           UINT            0               65535           0             Continuous
                                                                             if "Enable" is set
Register‐      UINT            4               32              4             Rising edge at Enable
Length

Functional description
The IL_PRBSGeneratorType02 function block generates a pseudo noise signal.
This signal is almost a white noise which means that all frequencies are in
the same amplitude. Additionally, it is almost DC-free. This function block
operates event-controlled. That means that a new value is generated when the
"Step" input is changed.
The generated signal is repeated after n cycles. The number of cycles depends
on the register depth.
RegisterLength:
"RegisterLength" sets the depth of the internal shift register used for signal
generation. The register depth does not affect the signal quality generated. A
higher register depth generates a longer cycle before the signal is repeated.
The following table shows the signal period depending on the "Register‐
Length":
  RegisterLength          Period            RegisterLength         Period
                                                         17             131071
                   2                 3                   18             262143
                   3                 7                   19             524287
                   4                15                   20           1048575
                   5                31                   21           2097151
                   6                63                   22           4194303

  RegisterLength          Period           RegisterLength         Period
                   7              127                   23           8388607
                   8              255                   24          16777215
                   9              511                   25          33554431
                  10             1023                   26          67108863
                  11             2047                   27         134217727
                  12             4095                   28         268435455
                  13             8191                   29         536870911
                  14            16383                   30        1073741823
                  15            32767                   31        2147483647
                  16            65535                   32        4294967295
"RegisterLength" may only contain the values listed in the table.
Pause, InPause:
The function block processing can be temporarily paused with the "Pause"
input. If "Pause" is active, the "InPause" output is set. In this mode, no new
signal values are generated at the "OutputValue".
Time response:
The IL_PRBSGeneratorType02 function block operates asynchronously. After
the start due to a rising edge at the "Enable" input, it reads the "Register‐
Length" input. The function block generates a new value at the "OutputValue"
output each time the "Step" input changes. If the signal generation is active,
the "InOperation" output is set. If an error occurs, the "Error" output is set.

Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:
Table 588: Generated error numbers of the IL_PRBSGeneratorType02 function block
ErrorID                              Additional1 Additional2 Description
INPUT_INVALID_ERROR                  16#0A0F010 16#0C23003 The "RegisterLength" input is invalid
                                     4           3
STATE_MACHINE_ERROR                  16#0A0F010 16#0C23100 Runtime error in function block:
                                     4           0           Invalid state of the state machine

### 21.7.6 IL_AngleGeneratorType01

Brief description
This function block generates an angle between 0.0 and 360.0 degree using
the specified frequency.

Interface description

Table 589: Interface variables of the IL_AngleGeneratorType01 function block
           Name              Type             Comment
VAR_INPUT Enable             BOOL             Function block processing enabled
           Pause             BOOL             Pauses processing
           Frequency         LREAL            Frequency in Hz
VAR_OUTPUT InOpera‐          BOOL             The function block operates and the outputs are valid.
           tion
           Error             BOOL      Indicates that an error occurred in the function block
           ErrorID       ⮫ ERROR_CODE Error ID
              ErrorIdent ⮫ ERROR_STRUC For the error structure with further error classification,

    T             see ⮫ Error codes on page 677
InPause    BOOL          Pauses processing active
Outpu‐     LREAL         Generated angle
tAngle
ActScan‐   LTIME         Measured call cycle time
Time

Table 590: Min./max. and default values of the IL_AngleGeneratorType01 inputs
Name           Type             Min. value     Max. value    Default value   Applied
Enable         BOOL                                          FALSE           Continuous
Pause          BOOL                                          FALSE           Continuous
Frequency      LREAL            0.0            1/(2*cycle    1.0             Continuous
                                               time)

Functional description
The IL_AngleGeneratorType01 function block generates an angle between 0
and 360 degrees with the frequency specified in Hz at the "Frequency" input.
If "InOperation" is set, the block generates a new value between 0.0 and
360.0 at "OutputAngle" with each call. This function block should be called
cyclically. The measured call cycle is output in "ActScanTime".
The created angular values are between 0 and 360 degrees.
Processing is carried out continuously when the "Enable" input is set. The
"Pause" input temporarily pauses the processing.

Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:
Table 591: Generated error numbers of the IL_AngleGeneratorType01 function block
ErrorID                            Additional1 Additional2 Description
INPUT_RANGE_ERROR                  16#0A0F010 16#0C23003 "Frequency" is smaller than 0.0 or
                                   4           4           greater than 1/(2*ActScanTime)
STATE_MACHINE_ERROR                16#0A0F010 16#0C23100 Runtime error in function block:
                                   4           0           Invalid state of the state machine

### 21.7.7 IL_AngleGeneratorType02

Brief description
This function block generates an angle between 0.0 and 360.0 degree using
the specified frequency.

      Interface description

Table 592: Interface variables of the IL_AngleGeneratorType02 function block
           Name               Type                Comment
VAR_INPUT Enable              BOOL                Function block processing enabled
           Pause              BOOL                Pauses processing
           Frequency          LREAL               Frequency in 1/steps
           Step               UINT                Processing step
VAR_OUTPUT InOpera‐           BOOL                The function block operates and the outputs are valid.
           tion
           Error              BOOL          Indicates that an error occurred in the function block
           ErrorID            ⮫ ERROR_CODE Error ID
                   ErrorIdent ⮫ ERROR_STRUC For the error structure with further error classification,
                              T             see ⮫ Error codes on page 678
                   InPause    BOOL          Pauses active processing
                   ActStep    UINT          Measured call cycle time.
                   Outpu‐     LREAL         Generated angle
                   tAngle

Table 593: Min./max. and default values of the IL_AngleGeneratorType02 inputs
Name               Type           Min. value      Max. value     Default value   Applied
Enable             BOOL                                          FALSE           Continuous
Pause              BOOL                                          FALSE           Continuous
Frequency          LREAL          0.0             0.5            0.1             Change at "Step"
Step               BOOL           0               65535          0               Continuous

      Functional description
      The IL_AngleGeneratorType01 function block generates an angle between 0
      and 360 degrees with the frequency specified in 1/Step at the "Frequency"
      input. If "InOperation" is set, the function block generates a new value
      between 0.0 and 360.0 at "OutputAngle" upon each call. This function block
      should be called cyclically. The frequency specified at the "Frequency" input
      does not refer to the steps at the "Step" input. Thus, it has to be lower than
      0.5. Only computed if the "Step" input changes.
      The created angular values are between 0 and 360 degrees.
      The “Step” input controls the processing when the "Enable" input is set. The
      "Pause" input temporarily pauses the processing.

      Error codes
      The function block uses the error table CXA_TABLE, 16#0001.

It can generate the following error messages in Additional1/Additional2:
Table 594: Generated error numbers of the IL_AngleGeneratorType02 function block
ErrorID                          Additional1 Additional2 Description
INPUT_RANGE_ERROR                16#0A0F010 16#0C23003 "Frequency" is smaller than 0.0 or
                                 4           4           greater than 0.5
STATE_MACHINE_ERROR              16#0A0F010 16#0C23100 Runtime error in function block:
                                 4           0           Invalid state of the state machine

### 21.7.8 IL_PhaseController

  Brief description

  This function block corrects the phase of an angle via a control loop.

  Interface description

Table 595: Interface variables of the IL_PhaseController function block
           Name              Type            Comment
VAR_INPUT  Enable            BOOL            Function block processing enabled
           Pause             BOOL            Pauses processing
           Angle             LREAL           Input angle
           Phase‐            LREAL           Reference variable for phase control
           ShiftSet‐
           point
           Phase‐            LREAL           Feedback value for control loop
           ShiftFeed‐
           back
           IControl          LREAL           I-value of the controller
           PControl          LREAL           P-value of the controller
           HighLimit         LREAL           Upper correction limit in degrees
           LowLimit          LREAL           Lower correction limit in degrees
           Window            LREAL           Control window
VAR_OUTPUT InOpera‐          BOOL            The function block operates and the outputs are valid
           tion
           Error             BOOL      Indicates that an error occurred in the function block
           ErrorID       ⮫ ERROR_CODE Error ID
              ErrorIdent ⮫ ERROR_STRUC For the error structure with further error classification,
                         T             see ⮫ Error codes on page 681
              InPause    BOOL          Processing pause active

Name      Type                Comment
Output‐   LREAL               Controlled angle
Value

Table 596: Min./max. and default values of the IL_PhaseController inputs
Name               Type          Min. value      Max. value      Default value   Applied
Enable             BOOL                                          FALSE           Continuous
Pause              BOOL                                          FALSE           Continuous
Angle              LREAL         0.0             360.0           0.0             Continuous
PhaseShift‐        LREAL                                         0.0             Continuous
Setpoint
PhaseShift‐        LREAL                                         0.0             Continuous
Feedback
IControl           LREAL         0.0                             0.0             Continuous
PControl           LREAL         0.0                             0.0             Continuous
HighLimit          LREAL         0.0             180.0           10.0            Continuous
LowLimit           LREAL         -180.0          0.0             -10.0           Continuous
Window             LREAL         0.0                             5.0             Continuous

Hidden outputs
To reduce the complexity of the function block, not all internal values are
available at the outputs. These values can be read directly at the function
block. Write-access is not possible.
Table 597: Internal values of the function block read via properties
Variable                 Data type    Description
ActAngle                 LREAL        Computed target zero line
IpartCorrection          LREAL        Correction value of the PI-controller
PhaseShift               LREAL        Computed phase offset

Functional Description
The IL_PhaseController function block shifts the input angle "Angle" by a cor‐
rection value and outputs it at "OutputAngle". The correction value is speci‐
fied by a PI-controller controlling once per cycle in the zero crossing when the
difference between "PhaseShiftSetPoint" and "PhaseShiftFeedback" is higher
than "Window". The correction value is limited to a value between "LowLimit"
and "HighLimit".
The control settings "PControl" and "IControl" refer to one cycle. One cycle
starts if the "Angle" input jumps from 360 to 0 degrees.
The created angular values are between 0 and 360 degrees.
It is processed continuously when the "Enable" input is set.

Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:
Table 598: Generated error numbers of the IL_PhaseController function block
ErrorID                            Additional1 Additional2 Description
INPUT_RANGE_ERROR                  16#0A0F010 16#0C23003 "Angle" is smaller than 0° or greater
                                   4           6           than 360°
INPUT_RANGE_ERROR                  16#0A0F010 16#0C23003 "PhaseShiftSetpoint" is smaller than
                                   4           7           -180 or greater than 180
INPUT_RANGE_ERROR                  16#0A0F010 16#0C23003 "PhaseShiftFeedback" is smaller than
                                   4           8           -180 or greater than 180
INPUT_RANGE_ERROR                  16#0A0F010 16#0C23003 "IControl" is negative
                                   4           9
INPUT_RANGE_ERROR                  16#0A0F010 16#0C23003 "PControl" is negative
                                   4           A
INPUT_RANGE_ERROR                  16#0A0F010 16#0C23003 "HighLimit" is smaller than "LowLimit"
                                   4           B
INPUT_RANGE_ERROR                  16#0A0F010 16#0C23003 "Window" is smaller than 0
                                   4           C
STATE_MACHINE_ERROR                16#0A0F010 16#0C23100 Runtime error in function block:
                                   4           0           Invalid state of the state machine

### 21.7.9 IL_SignalGeneratorType01

Brief description
This function block generates different signal shapes using an input angle.

       Interface description

Table 599: Interface variables of the IL_SignalGeneratorType01 function block
                   Name      Type           Comment
VAR_INPUT          Enable    BOOL           Function block processing enabled
                   Angle     LREAL          Angle
                   CurveType ⮫ IL_CURVETYPE Generated signal shape
                   Duty        LREAL              Duty factor in % (50=symmetric)
                                                  Permitted value range:
                                                  - Sinusoidal: 25-75
                                                  - Double_Sine: 10-90
                                                  - Triangular: 10-90
                   DutyRamp LREAL                 Changing the duty factor in %/ms
                   Rounding LREAL                 Rounding the signal in % (only active for the signal
                                                  shape "triangle")
           Rounding‐           LREAL              Changing the rounding in %/ms
           Ramp
VAR_OUTPUT InOpera‐            BOOL               The function block operates and the outputs are valid
           tion
           Error               BOOL         Indicates that an error occurred in the function block
           ErrorID            ⮫ ERROR_CODE Error ID
                   ErrorIdent ⮫ ERROR_STRUC For the error structure with further error classification,
                              T             see ⮫ Error codes on page 685
                   Output‐    LREAL         Generated signal shape
                   Value
                   ActScan‐   LTIME         Measured cycle time
                   Time

Table 600: Min./max. and default values of the IL_SignalGeneratorType01 inputs
Name               Type            Min. value      Max. value     Default value   Applied
Enable             BOOL                                           FALSE           Continuous
Angle              LREAL           0.0             360.0          0.0             Continuous
CurveType          IL_CURVE‐                                      SINUSOIDAL      Continuous
                   TYPE
Duty               LREAL           10.0            90.0           50.0            Continuous
DutyRamp           LREAL           0.0             100.0          0.0001          Continuous
Rounding           LREAL           0.0             100.0          0.0             Continuous
Rounding‐          LREAL           0.0             100.0          0.0001          Continuous
Ramp

Functional description
The IL_SignalGeneratorType01 function block generates the signal shape set
at the "CurveType" input. This shape is based on the angle applied at the
"Angle" input. Set the duty factor via the "Duty" input. If "InOperation” is
set, the function block generates a new value between -1.0 and 1.0 at the
"OutputValue" output.
It is processed continuously when the "Enable" input is set.
CurveType
The "CurveType" input determines the generated signal shape. The following
signal shapes are implemented:
● SINUSOIDAL: Function similar to sinusoidal with longest consistently

  increasing and decreasing sections possible

● DOUBLE_SINE: Double sine

● TRIANGULAR: Triangle signal

Duty, DutyRamp
The "Duty" input determines the duty factor of the signal. Actually, the 180°
mark is moved. With a duty factor of 50%, the signal is symmetric. Depending
on the signal shape, "Duty" is limited.
The "DutyRamp" input specifies the change rate of the duty factor in %/ms if
the value changes at the "Duty" input.
Rounding, RoundingRamp

The "Rounding" input is only enabled if the signal shape "TRIANGULAR" is
active. It indicates the rounding of the triangle in %. 0 means no rounding.
The "RoundingRamp" input specifies the change rate of the rounding in %/ms
if the "Rounding" input is changed.

Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:
Table 601: Generated error numbers of the IL_SignalGeneratorType01 function block
ErrorID                            Additional1 Additional2 Description
INPUT_RANGE_ERROR                  16#0A0F010 16#0C23005 "Angle" is smaller than 0.0° or greater
                                   4           1           than 360.0°
INPUT_RANGE_ERROR                  16#0A0F010 16#0C23005 "CurveType" is invalid
                                   4           2
INPUT_RANGE_ERROR                  16#0A0F010 16#0C23005 "Duty" is beyond the permitted range
                                   4           3
INPUT_RANGE_ERROR                  16#0A0F010 16#0C23005 "DutyRamp" is smaller than 0.0001
                                   4           4
INPUT_RANGE_ERROR                  16#0A0F010 16#0C23005 "Rounding" is negative or greater than
                                   4           5           100
INPUT_RANGE_ERROR                  16#0A0F010 16#0C23005 "RoundingRamp" is smaller than
                                   4           6           0.0001
STATE_MACHINE_ERROR                16#0A0F010 16#0C23100 Runtime error in function block:
                                   4           0           Invalid state of the state machine

### 21.7.10 IL_SignalGeneratorType02

Brief description
This function block generates different signal shapes using an input angle.

       Interface description

Table 602: Interface variables of the IL_SignalGeneratorType02 function block
                   Name      Type           Comment
VAR_INPUT          Enable    BOOL           Function block processing enabled
                   Angle     LREAL          Angle
                   CurveType ⮫ IL_CURVETYPE Generated signal shape
                   Duty        LREAL              Duty factor in % (50=symmetric)
                                                  - Sinusoidal: 25-75
                                                  - Double_Sine: 10-90
                                                  - Triangular: 10-90
                   DutyRamp LREAL                 Changing the duty factor in %/Step
                   Rounding LREAL                 Rounding the signal in % (only active for the signal
                                                  shape "triangle")
           Rounding‐           LREAL              Changing the rounding in %/Step
           Ramp
           Step                UINT               Processing step
VAR_OUTPUT InOpera‐            BOOL               The function block operates and the outputs are valid
           tion
           Error               BOOL         Indicates that an error occurred in the function block
           ErrorID            ⮫ ERROR_CODE Error ID
                   ErrorIdent ⮫ ERROR_STRUC For the error structure with further error classification,
                              T             see ⮫ Error codes on page 689
                   Output‐    LREAL         Generated signal shape
                   Value
                   ActStep    UINT          Latest executed processing step

Table 603: Min./max. and default values of the IL_SignalGeneratorType02 inputs
Name               Type            Min. value      Max. value     Default value   Applied
Enable             BOOL                                           FALSE           Continuous
Angle              LREAL           0.0             360.0          0.0             Change at "Step"
CurveType          IL_CURVE‐                                      SINUSOIDAL      Change at "Step"
                   TYPE
Duty               LREAL           10.0            90.0           50.0            Change at "Step"
DutyRamp           LREAL           0.0             100.0          0.0001          Change at "Step"
Rounding           LREAL           0.0             100.0          0.0             Change at "Step"
Rounding‐          LREAL           0.0             100.0          0.0001          Change at "Step"
Ramp

Functional description
The IL_SignalGeneratorType02 function block generates the signal shape set
at the "CurveType" input. This shape is based on the angle applied at the
"Angle" input. Set the duty factor via the "Duty" input. If "InOperation" is
set, the function block generates a new value between -1.0 and 1.0 at the
"OutputValue" output when "Step" is changed.
Processing is carried out continuously when the "Enable" input is set.
CurveType
The "CurveType" input determines the generated signal shape. The following
signal shapes are implemented:
● SINUSOIDAL: Function similar to sinusoidal with longest consistently

  increasing and decreasing sections possible

● DOUBLE_SINE: Double sine

● TRIANGULAR: Triangle signal

Duty, DutyRamp
The "Duty" input determines the duty factor of the signal. Actually, the 180°
mark is moved. With a duty factor of 50%, the signal is symmetric. Depending
on the signal shape, "Duty" is limited.
The "DutyRamp" input specifies the change rate of the duty factor in %/ms if
the value changes at the "Duty" input.
Rounding, RoundingRamp

The "Rounding" input is only enabled if the signal shape "TRIANGULAR" is
active. It indicates the rounding of the triangle in %. 0 means no rounding.
The "RoundingRamp" input specifies the change rate of the rounding in %/ms
if the "Rounding" input is changed.

Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:
Table 604: Generated error numbers of the IL_SignalGeneratorType02 function block
ErrorID                            Additional1 Additional2 Description
INPUT_RANGE_ERROR                  16#0A0F010 16#0C23005 "Angle" is smaller than 0.0° or greater
                                   4           1           than 360.0°
INPUT_RANGE_ERROR                  16#0A0F010 16#0C23005 "CurveType" is invalid
                                   4           2
INPUT_RANGE_ERROR                  16#0A0F010 16#0C23005 "Duty" is beyond the permitted range
                                   4           3
INPUT_RANGE_ERROR                  16#0A0F010 16#0C23005 "DutyRamp" is smaller than 0.0001
                                   4           4
INPUT_RANGE_ERROR                  16#0A0F010 16#0C23005 "Rounding" is negative or greater than
                                   4           5           100
INPUT_RANGE_ERROR                  16#0A0F010 16#0C23005 "RoundingRamp" is smaller than
                                   4           6           0.0001
STATE_MACHINE_ERROR                16#0A0F010 16#0C23100 Runtime error in function block:
                                   4           0           Invalid state of the state machine

### 21.7.11 IL_AmplitudeControllerType01

Brief description
This function block controls the amplitude and the zero line of a signal.

      Interface description

Table 605: Interface variables of the IL_AmplitudeControllerType01 function block
                   Name       Type               Comment
VAR_INPUT          Enable     BOOL               Function block processing enabled
                   Pause      BOOL               Pauses processing
                   Signal     LREAL              Input signal
                   Angle      LREAL              Input angle
                   Feedback   LREAL              Feedback value for control loop
                   AmpCon‐    ⮫ IL_AMP_CON‐      Settings of the amplitude controller
                   trol       TROL
                   Centerline‐ ⮫ IL_CENTER‐ Settings of the zero line controller
                   Control     LINE_CONTROL
VAR_OUTPUT InOpera‐           BOOL               The function block operates and the outputs are valid
           tion
           Error              BOOL          Indicates that an error occurred in the function block
           ErrorID            ⮫ ERROR_CODE Error ID
                   ErrorIdent ⮫ ERROR_STRUC For the error structure with further error classification,
                              T             see ⮫ Error codes on page 692
                   InPause    BOOL          Pauses active processing
                   ActScan‐   LTIME         Measured cycle time
                   Time
                   AmpSignal‐ LREAL         Amplitude-controlled signal
                   Corr
                   ActAmpli‐ LREAL          Latest measured amplitude
                   tude

Table 606: Min./max. and default values of the IL_AmplitudeControllerType01 inputs
Name               Type        Min. value        Max. value     Default value   Applied
Enable             BOOL                                         FALSE           Continuous
Pause              BOOL                                         FALSE           Continuous
Signal             LREAL       -1.0              1.0            0.0             Continuous
Angle              LREAL       0.0               360.0          0.0             Continuous
Feedback           LREAL                                        0.0             Continuous
AmpControl         IL_AMP_CON‐                                                  Continuous
                   TROL
Centerline‐        IL_CENTER‐                                                   Continuous
Control            LINE_CON‐
                   TROL

Hidden outputs
To reduce the complexity of the function block, not all internal values are
available at the outputs. These values can be read directly at the function
block. Write-access is not possible.
Table 607: Internal values of the function block read via properties
Variable                 Data type   Description
ActCenterline            LREAL       Computed target zero line
ActPhaseShift            LREAL       Latest determined phase deviation
AmpCorr                  LREAL       Correction value of the amplitude
AmpSignal                LREAL       Rectified signal without zero line correc‐

                                     tion
CenterlineCorr           LREAL       Controlled zero line
Strobe                   BOOL        New cycle detected

Functional Description
The IL_AmplitudeControllerType01 function block controls the amplitude and
the zero line of the signal applied at the "Signal" input.
AmpControl
The amplitude is corrected by a PI-controller controlling once per cycle in the
zero crossing when the difference between "AmpControl.Target" and the meas‐
ured amplitude of the "Signal" input is higher than "AmpControl.Window".
The correction value is limited to a value between "AmpControl.LowLimit" and
"AmpControl.HighLimit".
The control settings "AmpControl.PControl" and "AmpControl.IControl" refer
to one cycle. One cycle starts if the "Angle" input jumps from 360 to 0
degrees.
CenterlineControl
The zero crossing correction is corrected by a PI-controller controlling once
per cycle in the zero crossing when the difference between "CenterlineCon‐
trol.Target" and the measured mean value of the "Signal" input is higher than
"AmpControl.Window". The correction value is limited to a value between
"CenterlineControl.LowLimit" and "CenterlineControl.HighLimit".
The control settings "CenterlineControl.PControl" and "CenterlineCon‐
trol.IControl" refer to one cycle. One cycle starts if the "Angle" input jumps
from 360 to 0 degrees.

Processing is carried out continuously when the "Enable" input is set.

Error codes
The function block uses the error table CXA_TABLE, 16#0042.
It can generate the following error messages in Additional1/Additional2:
Table 608: Generated error numbers of the IL_AmplitudeControllerType01 function block
ErrorID                              Additional1 Additional2 Description
INPUT_RANGE_ERROR                    16#0A0F010 16#0C23004 "Signal" is smaller than -1.0 or greater
                                     4           1           than 1.0
INPUT_RANGE_ERROR                    16#0A0F010 16#0C23004 "Angle" is smaller than 0° or greater
                                     4           2           than 360°
INPUT_RANGE_ERROR                    16#0A0F010 16#0C23004 "AmpControl.Target" is negative
                                     4           3
INPUT_RANGE_ERROR                    16#0A0F010 16#0C23004 "AmpControl.Ramp" is smaller than
                                     4           4           0.0001
INPUT_RANGE_ERROR                    16#0A0F010 16#0C23004 "AmpControl.Init" is negative
                                     4           5
INPUT_RANGE_ERROR                    16#0A0F010 16#0C23004 "AmpControl.Window" is negative
                                     4           6
INPUT_RANGE_ERROR                    16#0A0F010 16#0C23004 "AmpControl.IControl" is negative
                                     4           7
INPUT_RANGE_ERROR                    16#0A0F010 16#0C23004 "AmpControl.PControl" is negative
                                     4           8
INPUT_RANGE_ERROR                    16#0A0F010 16#0C23004 "AmpControl.LowLimit" is higher than
                                     4           9           "AmpControl.HighLimit"
INPUT_RANGE_ERROR                    16#0A0F010 16#0C23004 "CenterlineControl.Ramp" is smaller
                                     4           A           than 0.0001
INPUT_RANGE_ERROR                    16#0A0F010 16#0C23004 "CenterlineControl.Window" is nega‐
                                     4           B           tive
INPUT_RANGE_ERROR                    16#0A0F010 16#0C23004 "CenterlineControl.IControl" is nega‐
                                     4           C           tive

ErrorID                          Additional1 Additional2 Description
INPUT_RANGE_ERROR                16#0A0F010 16#0C23004 "CenterlineControl.PControl" is nega‐
            4           D           tive
INPUT_RANGE_ERROR                16#0A0F010 16#0C23004 "CenterlineControl.LowLimit" is higher
            4           E           than "CenterlineControl.HighLimit"
INPUT_RANGE_ERROR                16#0A0F010 16#0C23004 "CenterlineControl.Init" is negative
            4           F
STATE_MACHINE_ERROR              16#0A0F010 16#0C23100 Runtime error in function block:
            4           0           Invalid state of the state machine

### 21.7.12 IL_AmplitudeControllerType02

Brief description
This function block controls the amplitude and the zero line of a signal.

Interface description

Table 609: Interface variables of the IL_AmplitudeControllerType02 function block
              Name           Type            Comment
VAR_INPUT     Enable         BOOL            Function block processing enabled
              Pause          BOOL            Pauses processing
              Step           UINT            Processing step
              Signal         LREAL           Input signal
              Angle          LREAL           Input angle
              Feedback       LREAL           Feedback value for control loop
              AmpCon‐        ⮫ IL_AMP_CON‐   Settings of the amplitude controller
              trol           TROL
              Centerline‐ ⮫ IL_CENTER‐ Settings of the zero line controller
              Control     LINE_CONTROL
VAR_OUTPUT InOpera‐          BOOL            The function block operates and the outputs are valid
           tion
           Error         BOOL         Indicates that an error occurred in the function block
           ErrorID       ERROR_CODE   Error ID
           ErrorIdent    ERROR_STRUCT For the error structure with further error classification,
                                      see ⮫ Error codes on page 695
              InPause    BOOL         Pauses active processing
              ActStep    UINT         Latest step processed
              AmpSignal‐ LREAL        Amplitude-controlled signal
              Corr

Name        Type              Comment
ActAmpli‐   LREAL             Latest measured amplitude
tude

Table 610: Min./max. and default values of the IL_AmplitudeControllerType02 inputs
Name               Type        Min. value        Max. value      Default value   Applied
Enable             BOOL                                          FALSE           Continuous
Pause              BOOL                                          FALSE           Continuous
Signal             LREAL       -1.0              1.0             0.0             Change at "Step"
Angle              LREAL       0.0               360.0           0.0             Change at "Step"
Feedback           LREAL                                         0.0             Change at "Step"
AmpControl         IL_AMP_CON‐                                                   Change at "Step"
                   TROL
Centerline‐        IL_CENTER‐                                                    Change at "Step"
Control            LINE_CON‐
                   TROL

Hidden outputs
To reduce the complexity of the function block, not all internal values are
available at the outputs. These values can be read directly at the function
block. Write-access is not possible.
Table 611: Internal values of the function block read via properties
 Variable                Data type    Description
 ActCenterline           LREAL        Computed target zero line
 ActPhaseShift           LREAL        Latest determined phase deviation
 AmpCorr                 LREAL        Correction value of the amplitude
 AmpSignal               LREAL        Rectified signal without zero line correc‐
                                      tion
 CenterlineCorr          LREAL        Controlled zero line
 Strobe                  BOOL         New cycle detected

Functional Description
The IL_AmplitudeControllerType02 function block controls the amplitude and
the zero line of the signal applied at the "Signal" input.
AmpControl
The amplitude is corrected by a PI-controller controlling once per cycle in the
zero crossing when the difference between "AmpControl.Target" and the meas‐
ured amplitude of the "Signal" input is higher than "AmpControl.Window".
The correction value is limited to a value between "AmpControl.LowLimit" and
"AmpControl.HighLimit".
The control settings "AmpControl.PControl" and "AmpControl.IControl" refer
to one cycle. One cycle starts if the "Angle" input jumps from 360 to 0
degrees.
CenterlineControl
The zero crossing correction is corrected by a PI-controller controlling once
per cycle in the zero crossing when the difference between "CenterlineCon‐
trol.Target" and the measured mean value of the "Signal" input is higher than
"AmpControl.Window". The correction value is limited to a value between
"CenterlineControl.LowLimit" and "CenterlineControl.HighLimit".

The control settings "CenterlineControl.PControl" and "CenterlineCon‐
trol.IControl" refer to one cycle. One cycle starts if the "Angle" input jumps
from 360 to 0 degrees.

A change at the “Step" input triggers the processing when the "Enable" input
is set.

Error codes
The function block uses the error table CXA_TABLE, 16#0042.
It can generate the following error messages in Additional1/Additional2:
Table 612: Generated error numbers of the IL_AmplitudeControllerType02 function block
ErrorID                            Additional1 Additional2 Description
INPUT_RANGE_ERROR                  16#0A0F010 16#0C23004 "Signal" is smaller than -1.0 or greater
                                   4           1           than 1.0
INPUT_RANGE_ERROR                  16#0A0F010 16#0C23004 "Angle" is smaller than 0° or greater
                                   4           2           than 360°
INPUT_RANGE_ERROR                  16#0A0F010 16#0C23004 "AmpControl.Target" is negative
                                   4           3
INPUT_RANGE_ERROR                  16#0A0F010 16#0C23004 "AmpControl.Ramp" is smaller than
                                   4           4           0.0001
INPUT_RANGE_ERROR                  16#0A0F010 16#0C23004 "AmpControl.Init" is negative
                                   4           5
INPUT_RANGE_ERROR                  16#0A0F010 16#0C23004 "AmpControl.Window" is negative
                                   4           6
INPUT_RANGE_ERROR                  16#0A0F010 16#0C23004 "AmpControl.IControl" is negative
                                   4           7
INPUT_RANGE_ERROR                  16#0A0F010 16#0C23004 "AmpControl.PControl" is negative
                                   4           8
INPUT_RANGE_ERROR                  16#0A0F010 16#0C23004 "AmpControl.LowLimit" is higher than
                                   4           9           "AmpControl.HighLimit"
INPUT_RANGE_ERROR                  16#0A0F010 16#0C23004 "CenterlineControl.Ramp" is smaller
                                   4           A           than 0.0001

ErrorID                            Additional1 Additional2 Description
INPUT_RANGE_ERROR                  16#0A0F010 16#0C23004 "CenterlineControl.Window" is nega‐
            4           B           tive
INPUT_RANGE_ERROR                  16#0A0F010 16#0C23004 "CenterlineControl.IControl" is nega‐
            4           C           tive
INPUT_RANGE_ERROR                  16#0A0F010 16#0C23004 "CenterlineControl.PControl" is nega‐
            4           D           tive
INPUT_RANGE_ERROR                  16#0A0F010 16#0C23004 "CenterlineControl.LowLimit" is higher
            4           E           than "CenterlineControl.HighLimit"
INPUT_RANGE_ERROR                  16#0A0F010 16#0C23004 "CenterlineControl.Init" is negative
            4           F
STATE_MACHINE_ERROR                16#0A0F010 16#0C23100 Runtime error in function block:
            4           0           Invalid state of the state machine

### 21.7.13 IL_CURVETYPE

Brief description
The IL_CURVETYPE enumeration type contains possible curve shapes of signal
generators.

Declaration of the IL_CURVETYPE structure

TYPE IL_CURVETYPE :
(
   SINUSOIDAL := 1,
   DOUBLE_SIN := 2,
   TRIANGULAR := 3,
);
END_TYPE

SINUSOIDAL: Function similar to sinusoidal with longest consistently
increasing and decreasing sections possible
DOUBLE_SINE: Double sine
TRIANGULAR: Triangle signal
Used in:
● ⮫ Chapter 21.7.9 IL_SignalGeneratorType01 on page 681
● ⮫ Chapter 21.7.10 IL_SignalGeneratorType02 on page 685

### 21.7.14 IL_CENTERLINE_CONTROL

Brief description
The IL_CENTERLINE_CONTROL structure contains information required for the
zero line correction.
The zero crossing correction is corrected by a PI-controller controlling once
per cycle in the zero crossing when the difference between "CenterlineCon‐
trol.Target" and the measured mean value of the "Signal" input is higher than
"AmpControl.Window". The correction value is limited to a value between
"CenterlineControl.LowLimit" and "CenterlineControl.HighLimit".
The control settings "CenterlineControl.PControl" and "CenterlineCon‐
trol.IControl" refer to one cycle. One cycle starts if the "Angle" input jumps
from 360 to 0 degrees.

Declaration of the IL_CENTERLINE_CONTROL structure

TYPE IL_CENTERLINE_CONTROL:
 STRUCT
  Target:    LREAL:= 0; // Centerline amplitude
  Ramp:      LREAL:= 0.0001; // Ramp for change centerline
value /s
  Init:      LREAL:= 0; // Start centerline
  Window:    LREAL:= 0; // Window centerlinecorrection
(outside this window correction is aktiv)
  IControl: LREAL:= 0; // Integration time Tn for the
integration fraction of the controller
  PControl: LREAL:= 0; // Proportional value for the gaining
fraction of the controller

  HighLimit: LREAL:= 1; // Upper limit of centerlinecorrection
  LowLimit: LREAL:= 0; // Lower limit of centerlinecorrection
 END_STRUCT
END_TYPE

Used in:
● ⮫ Chapter 21.7.11 IL_AmplitudeControllerType01 on page 689
● ⮫ Chapter 21.7.12 IL_AmplitudeControllerType02 on page 693

### 21.7.15 IL_AMP_CONTROL

Brief description
The IL_AMP_CONTROL structure contains information required for the ampli‐
tude correction.
The amplitude is corrected by a PI-controller controlling once per cycle in the
zero crossing when the difference between "AmpControl.Target" and the meas‐
ured amplitude of the "Signal" input is higher than "AmpControl.Window".
The correction value is limited to a value between "AmpControl.LowLimit" and
"AmpControl.HighLimit".

Declaration of the IL_AMP_CONTROL structure

TYPE IL_AMP_CONTROL:
 STRUCT
  Target:    LREAL:= 0; // target Amplitude
  Ramp:      LREAL:= 0.0001; // Ramp for change amplitude
value /s
  Init:      LREAL:= 0; // Start Amplitude
  Window:    LREAL:= 0; // Window amplitudecorrection (outside
this window correction is aktiv)
  IControl: LREAL:= 0; // Integration time Tn for the
integration fraction of the controller
  PControl: LREAL:= 0; // Proportional value for the gaining
fraction of the controller
  HighLimit: LREAL:= 1; // Upper limit of amplitudecorrection
  LowLimit: LREAL:= 0; // Lower limit of amplitudecorrection
 END_STRUCT
END_TYPE

Used in:
● ⮫ Chapter 21.7.11 IL_AmplitudeControllerType01 on page 689
● ⮫ Chapter 21.7.12 IL_AmplitudeControllerType02 on page 693

## 21.8 Statistics (Statistic function blocks)

### 21.8.1 Introduction and overview

This section contains the statistic function blocks of the CXA_LoopControl.
Statistic function blocks analyze a data signal and generate statistical values
The CXA_LoopControl provides the following statistic function blocks:
Table 613: CXA_LoopControl statistic function blocks
         Time-discrete                Event-controlled                    Description
⮫ Chapter 21.8.2 IL_Histogram‐ ⮫ Chapter 21.8.3 IL_Histogram‐ Sorts values into categories
Type01 on page 698             Type02 on page 700
⮫ Chapter 21.8.4 IL_Statistic‐ ⮫ Chapter 21.8.5 IL_Statistic‐ Detects floating mean value,
Type01 on page 702             Type02 on page 704             minimum value and maximum
                                                              value
⮫ Chapter 21.8.6 IL_Suppres‐   ⮫ Chapter 21.8.7 IL_Suppres‐   Suppresses measured values
sionType01 on page 706         sionType02 on page 711         with an excessive deviation to
                                                              the mean value of the measured
                                                              values (1 limit)
⮫ Chapter 21.8.8 IL_Suppres‐   ⮫ Chapter 21.8.9 IL_Suppres‐   Suppresses measured values
sionType03 on page 715         sionType04 on page 721         with an excessive deviation to
                                                              the mean value of the measured
                                                              values (2 limits)

### 21.8.2 IL_HistogramType01

      Brief description
      This function block counts the occurrence of values into preset categories of
      the same size. This function block operates continuously.

      Interface description

Table 614: Interface variables of the IL_HistogramType01 function block
                   Name       Type              Comment
VAR_INPUT          Enable     BOOL              Function block processing enabled
                   Pause      BOOL              Temporary processing pause. The outputs are frozen
                   Reset      BOOL              Value reset in "HistogramData" and "ValueCount" at a
                                                rising edge
                   Value      LREAL             Value to be split into categories
                   MinValue   LREAL             Lower limit of classification
                   MaxValue   LREAL             Upper limit of collocation

Name       Type                 Comment
Category‐ USINT                 Number of categories into which "Value" should be
Count                           sub-divided
Histogram‐ POINTER TO           Address of an array with the values of the histogram
Data       UDINT                categories. The array has to have "CategoryCount" ele‐
                         ments
VAR_OUTPUT InOpera‐          BOOL             The function block operates. The outputs are valid
tion
Error             BOOL      Indicates that an error occurred in the function block
ErrorID       ⮫ ERROR_CODE Error ID
ErrorIdent ⮫ ERROR_STRUC For the error structure with further error classification,

    T             see ⮫ Error codes on page 699
InPause    BOOL          The analysis was paused. The values in "Histogram‐
                  Data" and "ValueCount" do not change
Value‐     UDINT         Number of the values already sorted in "Histogram‐
Count                    Data"

Table 615: Min./max. and default values of the IL_HistogramType01 inputs
Name           Type            Min. value     Max. value     Default value   Applied
Enable         BOOL                                          FALSE           Continuous
Pause          BOOL                                          FALSE           Continuous
Reset          BOOL                                          FALSE           Continuous
Value          LREAL           N. def.        N. def.        0.0             Continuous
MinValue       LREAL           N. def.        < MaxValue     0.0             Rising edge at Enable
MaxValue       LREAL           > MinValue     N. def.        1.0             Rising edge at Enable
Category‐      USINT           1              255            10              Rising edge at Enable
Count
Histogram‐     POINTER TO      0              N. def.        0               Rising edge at Enable
Data           UDINT

Functional description
The IL_HistogramType01 function block sorts the values at "Value" between
"MinValue" and "MaxValue" into one of the "CategoryCount" categories. Each
category is of the same size and covers a specific non-overlapping interval.
The interval range is uniquely defined by ("MaxValue"-"MinValue")/ "Category‐
Count". Each category counts its "Value" values. The total number of already
values applied is output in "ValueCount".
"HistogramData points" to an array of UDINTs. The array has to have "Cate‐
goryCount" elements of the type UDINT. Each element of the array forms a
category and counts the occurrence of "Value" within the category.
Processing is carried out continuously when the "Enable" input is set.
Pause, InPause
If "Pause" is set, the current state is frozen. "InPause" is set and "Value" not
analyzed further.
Reset
At a rising edge at "Reset", all array elements at "HistogramData" are set to 0
and the "ValueCount" output is deleted.

Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:

Table 616: Generated error numbers of the IL_HistogramType01 function block
ErrorID                            Additional1 Additional2 Description
INPUT_INVALID_ERROR                16#0A0F0104 16#0C230061 "MinValue" is greater than "MaxValue"
INPUT_RANGE_ERROR                  16#0A0F0104 16#0C230062 "CategoryCount" is 0
INPUT_INVALID_ERROR                16#0A0F0104 16#0C230063 "HistogramData" is 0
STATE_MACHINE_ERROR                16#0A0F0104 16#0C231000 Runtime error in function block:
                                                           Invalid state of the state machine

### 21.8.3 IL_HistogramType02

       Brief description
       This function block counts the occurrence of values into preset categories of
       the same size. This function block only operates when there is a change at the
       "Step" input.

       Interface description

Table 617: Interface variables of the IL_HistogramType02 function block
                   Name        Type               Comment
VAR_INPUT          Enable      BOOL               Function block processing enabled
                   Pause       BOOL               Temporary processing pause. The outputs are frozen
                   Reset       BOOL               Value reset in "HistogramData" and "ValueCount" at a
                                                  rising edge
                   Step        UINT               Current processing step. A new value at "Value" is only
                                                  processed when "Step” changes
                   Value      LREAL               Value to be split into categories
                   MinValue LREAL                 Lower limit of classification
                   MaxValue LREAL                 Upper limit of collocation
                   Category‐ USINT                Number of categories into which "Value" should be
                   Count                          sub-divided
                   Histogram‐ POINTER TO          Address of an array with the values of the histogram
                   Data       UDINT               categories. The array has to have "CategoryCount" ele‐
                                                  ments
VAR_OUTPUT InOpera‐            BOOL               The function block operates. The outputs are valid
           tion
           Error               BOOL         Indicates that an error occurred in the function block
           ErrorID             ⮫ ERROR_CODE Error ID

Name       Type          Comment
ErrorIdent ⮫ ERROR_STRUC For the error structure with further error classification,
    T             see ⮫ Error codes on page 701
InPause    BOOL          The analysis was paused. The values in "Histogram‐
                  Data" and "ValueCount" do not change
ActStep    UINT          Last processed step
Value‐     UDINT         Number of the values already sorted in "Histogram‐
Count                    Data"

Table 618: Min./max. and default values of the IL_HistogramType02 inputs
Name           Type           Min. value      Max. value     Default value   Applied

Enable         BOOL                                          FALSE           Continuous
Pause          BOOL                                          FALSE           Continuous
Reset          BOOL                                          FALSE           Continuous
Step           UINT           0               65335          0               Continuous
Value          LREAL          N. def.         N. def.        0.0             When there is a change
                                                        at Step
MinValue       LREAL          N. def.         < MaxValue     0.0             Rising edge at Enable
MaxValue       LREAL          > MinValue      N. def.        1.0             Rising edge at Enable
Category‐      USINT          1               255            10              Rising edge at Enable
Count
Histogram‐     POINTER TO     0               N. def.        0               Rising edge at Enable
Data           UDINT

Functional description
The IL_HistogramType02 function block sorts the values at "Value" between
"MinValue" and "MaxValue" into one of the "CategoryCount" categories. Each
category is of the same size and covers a specific non-overlapping interval.
The interval range is uniquely defined by ("MaxValue"-"MinValue")/ "Category‐
Count". Each category counts its "Value" values. The total number of already
applied values is output in "ValueCount". "Value" is only analyzed if the Step
input has changed.
"HistogramData points" to an array of UDINTs. The array has to have "Cate‐
goryCount" elements of the type UDINT. Each element of the array forms a
category and counts the occurrence of "Value" within the category.
It is only processed when the value at the "Step" input changes.
Pause, InPause
If "Pause" is set, the current state is frozen. "InPause" is set and "Value" not
analyzed further.
Reset
At a rising edge at "Reset", all array elements at "HistogramData" are set to 0
and the "ValueCount" output is deleted.

Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:
Table 619: Generated error numbers of the IL_HistogramType02 function block
ErrorID                       Additional1 Additional2 Description
INPUT_INVALID_ERROR           16#0A0F0104 16#0C230061 "MinValue" is greater than "MaxValue"
INPUT_RANGE_ERROR             16#0A0F0104 16#0C230062 "CategoryCount" is 0

ErrorID                          Additional1 Additional2 Description
INPUT_INVALID_ERROR              16#0A0F0104 16#0C230063 "HistogramData" is 0
STATE_MACHINE_ERROR              16#0A0F0104 16#0C231000 Runtime error in function block:
                                      Invalid state of the state machine

### 21.8.4 IL_StatisticType01

   Brief description
   The function block identifies time-discrete statistic characteristics of meas‐
   ured values or control deviations.
   Characteristics identified:
   ● Mean value (exponentially floating mean value)
   ● Variance (exponentially floating variance)
   ● Minimum/Maximum values (exponentially falling, that means that the
     values age)

   Interface description

Table 620: Interface variables of the IL_StatisticType01 function block
                   Name                   Type          Comment
VAR_INPUT          Enable                 BOOL          Calculation of data in each cycle when
                                                        "Enable" = TRUE
                   Pause                  BOOL          The output data is not changed when
                                                        Pause = TRUE
                   MeanFilterTCon‐        LTIME         The constant "Tn" of the exponentially
                   trol                                 floating calculation
                   Value                  LREAL         Input value; its statistical characteristic
                                                        variable can be identified
                   StartMeanValue         LREAL         The starting value applied at a rising edge
                                                        at "Enable" at the "MeanValue" output
VAR_OUTPUT         InOperation            BOOL          Processing is running, outputs are valid
                   Error                  BOOL          Error (see ErrorID and ErrorIdent)
                   ErrorID                ⮫ ERROR_CODE Error description
                   ErrorIdent             ⮫ ERROR_STRUC For a detailed error description, see
                                          T             ⮫ Error codes on page 704
                   InPause                BOOL          Indicates that the "Pause" input is active
                                                        and the values in "MeanValue", "Variance",
                                                        "MinValue" and "MaxValue" do not change

Name                Type                 Comment
ActScanTime         LTIME                The time difference since the function
                                      block was called last
MeanValue           LREAL                Mean value of "Value" (exponentially
                                      floating computation)
Variance            LREAL                Variance of "Value" (exponentially floating
                                      computation)
MinValue            LREAL                Minimum value of "Value" (exponentially
                                      floating computation)
MaxValue            LREAL                Maximum value of "Value" (exponentially
                                      floating computation)

Table 621: Min./max. and default values of the IL_StatisticType01 inputs
Name           Type             Min. value     Max. value      Default value Applied
Enable         BOOL                                               FALSE      Continuous
Pause          BOOL                                               FALSE      Continuous
MeanFilterT‐   LTIME           (2 x ActScan‐     N. def.         100 ms      Continuous
Control                            Time)
Value          LREAL              N. def.        N. def.            0.0       Continuous
StartMean‐     LREAL              N. def.        N. def.            0.0       Rising edge at Enable
Value

Functional description
The function block identifies the statistic characteristics of the "Value" input
value. The characteristic variables can, for example, be used to show the
mean value, variance and minimum/maximum values during the control proc‐
esses.
"MeanValue" and "Variance"
The computation includes older input values to a lesser extent than newer
input values (so-called exponentially floating computation). This ensures that
the characteristics do not fully include all measured values since the activa‐
tion of the function block, but also include the changes of the characteristic
variables of the input. For example, a step change of the mean value of the
"Value" input variable to a new mean value of the variable is quickly displayed
at the "MeanValue" output without older input values distorting the new mean
value. The variance is computed analogously.
The averaging depends on the "MeanFilterTControl" input. Higher values
include older data to a greater extent to determine the statistical character‐
istic variables. The higher the value, the slower the outputs responses to
changes to the characteristic variables of the input signal and the more con‐
stant the characteristic values identified.
"MinValue" and "MaxValue"
The outputs show the tendency of the minimum and maximum values that
occur. As with the mean value and the variance, not all input values are
analyzed since the function block activation, but the minimum and maximum
values are identified in a floating manner. This means that a minimum or
maximum value becomes older and is overwritten by newer (possibly lower)
values. The function can be compared with a drag indicator applied immedi‐
ately with a new higher input value, which then falls again with a large time
constant.
The "MeanFilterTControl" input also shows the time-lag of the output with
regard to the lowering of the "MinValue" and "MaxValue values".

   Error codes
   The function block uses the error table CXA_TABLE, 16#0001.
   It can generate the following error messages in Additional1/Additional2:
Table 622: Generated error numbers of the IL_StatisticType01 function block
ErrorID                          Additional1 Additional2 Description
STATE_MACHINE_ERROR             16#0A0F0104 16#0C231000 Invalid function block state
INPUT_RANGE_ERROR               16#0A0F0104 16#0C230064 MeanFilterTControl value < (2 x "ActS‐
                                                         canTime")

### 21.8.5 IL_StatisticType02

   Brief description
   The function block identifies event-controlled statistical characteristics of
   measured values or control deviations.
   Characteristics identified:
   ● Mean value (exponentially floating mean value)
   ● Variance (exponentially floating variance)
   ● Minimum/Maximum values (exponentially falling, that means that the
     values age)

   Interface description

Table 623: Interface variables of the IL_StatisticType02 function block
                   Name                   Type           Comment
VAR_INPUT          Enable                 BOOL           Data computed each time "Step" changes
                                                         if Enable = TRUE
                   Pause                  BOOL           The OutputValue data is not changed
                                                         when "Pause" = TRUE. If the "Step" input
                                                         increments in the meantime, the step cur‐
                                                         rently present at the "ActStep" output is
                                                         issued
                   Step                   UINT           Current computation step
                   MeanFilterTCon‐        LREAL          The constant "Tn" of the exponentially
                   trol                                  floating computation related to "Step"
                   Value                  LREAL          Input value; its statistical characteristic
                                                         variable can be identified
                   StartMeanValue         LREAL          The starting value applied at a rising edge
                                                         at "Enable" at the "MeanValue" output

Name                Type          Comment
VAR_OUTPUT        InOperation         BOOL          Processing without errors, output data is
                                  valid
Error               BOOL          Error (see ErrorID and ErrorIdent)
ErrorID             ⮫ ERROR_CODE Error description
ErrorIdent          ⮫ ERROR_STRUC For a detailed error description, see
                    T             ⮫ Error codes on page 706
InPause             BOOL          Indicates that the "Pause" input is active
                                  and that the values do not change in
                                  "MeanValue", "Variance", "MinValue" and
                                  "MaxValue”

ActStep             UINT          "Step” value to which "OutputValue" refers
                                  to. "ActStep" is initialized with the "Step"
                                  value at a rising edge at "Enable"
MeanValue           LREAL         Mean value of "Value" (exponentially
                                  floating computation)
Variance            LREAL         Variance of "Value" (exponentially floating
                                  computation)
MinValue            LREAL         Minimum value of "Value" (exponentially
                                  floating computation)
MaxValue            LREAL         Maximum value of "Value" (exponentially
                                  floating computation)

Table 624: Min./max. and default values of the IL_StatisticType02 inputs
Name           Type             Min. value     Max. value    Default value Applied
Enable         BOOL                                             FALSE      Continuous
Pause          BOOL                                             FALSE      Continuous
Step           UINT                  0          16#FFFF           0        Continuous
MeanFilterT‐   LREAL                2.0          N. def.        100.0      Continuous
Control
Value          LREAL              N. def.        N. def.          0.0       Continuous
StartMean‐     LREAL              N. def.        N. def.          0.0       Rising edge at Enable
Value

   Functional description
   The function block identifies the statistic characteristics of the "Value" input
   value. The characteristic variables can, for example, be used to show the
   mean value, variance and minimum/maximum values during the control proc‐
   esses.
   "MeanValue" and "Variance"
   The computation includes older input values to a lesser extent than newer
   input values (so-called exponentially floating computation). This ensures that
   the characteristics do not fully include all measured values since the activa‐
   tion of the function block, but also include the changes of the characteristic
   variables of the input. For example, a step change of the mean value of the
   "Value" input variable to a new mean value of the variable is quickly displayed
   at the "MeanValue" output without older input values distorting the new mean
   value. The variance is computed analogously.

The averaging depends on the "MeanFilterTControl" input. Higher values
include older data to a greater extent to determine the statistical character‐
istic variables. The higher the value, the slower the outputs responses to
changes to the characteristic variables of the input signal and the more con‐
stant the characteristic values identified.
"MinValue" and "MaxValue"
The outputs show the tendency of the minimum and maximum values that
occur. As with the mean value and the variance, not all input values are
analyzed since the function block activation, but the minimum and maximum
values are identified in a floating manner. This means that a minimum or
maximum value becomes older and is overwritten by newer (possibly lower)
values. The function can be compared with a drag indicator applied immedi‐
ately with a new higher input value, which then falls again with a large time
constant.
The "MeanFilterTControl" input also shows the time-lag of the output with
regard to the lowering of the "MinValue" and "MaxValue values".

Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:
Table 625: Generated error numbers of the IL_StatisticType02 function block
ErrorID                          Additional1 Additional2 Description
STATE_MACHINE_ERROR             16#0A0F0104 16#0C231000 Invalid function block state
INPUT_RANGE_ERROR               16#0A0F0104 16#0C230064 "MeanFilterTControl" value has to be
                                                         greater or equal to 2.0

### 21.8.6 IL_SuppressionType01

Brief description
This time-discreet function block suppresses measured values with an exces‐
sive deviation to the mean value of the measured values. The measured values
beyond the parameterizable threshold values are not transmitted, but output
as filtered value.

Interface description

Table 626: Interface variables of the IL_SuppressionType01 function block
                  Name               Type        Comment
VAR_INPUT         Enable             BOOL        Computation of data in each cycle when
                                                 "Enable" = TRUE
                  Pause            BOOL          The output data is not changed when
                                                 Pause = TRUE
                  MeanFilterTCon‐  LTIME         The constant "Tn" of the (PT1) mean value
                  trol                           filter
                  SuppressionMode ⮫ IL_SUPPRES‐ Describes the function of the inputs "Sup‐
                                   SION_MODE     pressionLimitLow" and "SuppressionLimi‐
                                                 tHigh"

SuppressionLimi‐ REAL          Upper value of the suppression window
tHigh                          (added to the mean value)
SuppressionLimi‐ REAL          Lower value of the suppression window
tLow                           (is subtracted from the mean value)
Value            REAL          The current actual process value
StartValue       REAL          The initial value applied at a rising edge at
                               "Enable" at the "OutputValue" output
VAR_OUTPUT        InOperation      BOOL          Processing without errors, output data is
                               valid
Error            BOOL          Error (see ErrorID and ErrorIdent)
ErrorID          ⮫ ERROR_CODE Error description
ErrorIdent       ⮫ ERROR_STRUC For a detailed error description, see
                 T             ⮫ Error codes on page 710
InPause          BOOL          Indicates that the "Pause" input is active
                               and the output values do not change
ActScanTime      LTIME         The time difference since the function
                               block was called last
MeanValue        REAL          Filtered mean value compared to "Value"
OutputValue      REAL          The computed output value
InLimitActive    BOOL          Indicates that the suppression window is
                               active
SuppressionTime LTIME          Time counter counting how long the meas‐
                               ured values were suppressed. The value is
                               deleted at a rising edge at "Enable" (T#0s)
                               and increments in case of an active sup‐
                               pression. When there is again an unsup‐
                               pressed input value, the output is deleted
                               again. In case of an overflow, the counter
                               automatically returns to "0"
SuppressionRatio REAL          Percentage rate of all suppressed values
                               (0-100%)

Table 627: Min./max. and default values of the IL_SuppressionType01 inputs
Name                 Type           Min.      Max.        Default value     Applied
                                    value     value
Enable               BOOL                                    FALSE          Continuous
Pause                BOOL                                    FALSE          Continuous
MeanFilterTCon‐      LTIME           0.0     N. def.         100 ms         Continuous
trol

Name                  Type             Min.        Max.      Default value   Applied
                 value       value
SuppressionMode IL_SUPPRES‐                                  IL_SUPPRES‐     Rising edge at Enable
SION_MODE                                     SION_PER‐
                                         CENTAGE
SuppressionLimi‐      REAL               0.0       N. def.       20.0        Continuous
tHigh
SuppressionLimi‐      REAL               0.0       N. def.       20.0        Continuous
tLow
Value                 REAL             N. def.     N. def.       0.0         Continuous
StartValue            REAL             N. def.     N. def.       0.0         Rising edge at Enable

Functional description
When controlling, it is often required that the measured values with an obvi‐
ously strong deviation from the expected value are filtered (suppressed).
Therefore, a suppression window is implemented in the function block that
moves along with the mean value of the value to be filtered and generates
a tolerance window around this mean value. Each measured value "Value" is
compared to the filtered measured value (filtering of the measured value with
a PT1 filter). If the respective measured value is not within the suppression
window around the mean value (tolerance window defined by "Suppression‐
LimitLow" or "SuppressionLimitHigh"), it is not output at the function block
output "OutputValue", but suppressed. Thus, the mean value is output instead
of “Value” at the "OutputValue" output.

Internal function block structure
The function block consists of an mean value filter and a block suppressing
the measured values. A PT1 element filters the mean value. The filter time
constant should be higher than the process time constant to allow a correct
mean value filtering. To diagnose the filtered mean value, use the "MeanValue"
output.

Window-cutting modes
In case of window-cutting, the upper threshold ("SuppressionLimitHigh") and
the lower threshold ("SuppressionLimitLow") can be configured separately.
There are two modes:
● Related to the mean value in percent (IL_SUPPRESSION_PERCENTAGE):
  The window width is specified by the percentage rate of the mean value.
  That means that "SuppressionLimitHigh" specifies a percentage rate (from
  the absolute value of the mean value) that is added to the mean value
  to maintain the upper threshold. "SuppressionLimitLow" specifies a per‐
  centage rate (from the absolute value of the mean value) that is subtracted
  from the mean value for the lower threshold. Note that the window size
  might become very small if the amount of the mean value becomes very
  small.
● Absolute window related to the mean value (IL_SUPPRESSION_ABSO‐
  LUTE_VALUE: The values at the inputs "SuppressionLimitLow" and "Sup‐
  pressionLimitHigh" directly specify the window size around the mean value.

mean value"
Diagnostics of the window-cutting
Observe the window-cutting function for diagnostic purposes using the out‐
puts "SuppressionTime" and "SuppressionRatio". "SuppressionTime" is a time
counter that counts the suppression period of the measured values. It incre‐
ments if the suppression is active and reset to "0" if there is an input value
that is not suppressed. It is also reset to “0” at a rising edge at "Enable" as
well as in case of an overflow. "SuppressionRatio" is the percentage rate of
time of all suppressed values.

Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:

Table 628: Generated error numbers of the IL_SuppressionType01 function block
ErrorID                         Additional1 Additional2 Description
STATE_MACHINE_ERROR            16#0A0F0104 16#0C231000 Invalid function block state
INPUT_INVALID_ERROR            16#0A0F0104 16#0C230065 "SuppressionLimitHigh" value is lower
                                                        than 0.0
INPUT_INVALID_ERROR            16#0A0F0104 16#0C230066 "SuppressionLimitLow" value is lower
                                                        than 0.0
INPUT_INVALID_ERROR            16#0A0F0104 16#0C230067 "MeanFilterTControl" value is lower
                                                        than 0.0

### 21.8.7 IL_SuppressionType02

   Brief description
   This event-controlled function block suppresses measured values with an
   excessive deviation to the mean value of the measured values. The measured
   values beyond the parameterizable threshold values are not transmitted, but
   output as filtered value.

   Interface description

Table 629: Interface variables of the IL_SuppressionType02 function block
                  Name                   Type          Comment
VAR_INPUT         Enable                 BOOL          Computation of data in each cycle (step)
                                                       while "Enable" = TRUE
                  Pause                  BOOL          The output data is not changed when
                                                       "Pause" = TRUE. If the “Step” input incre‐
                                                       ments in the meantime, the step at the
                                                       "ActSteps" output is issued
                  Step            UINT                 Current calculation step
                  MeanFilterTCon‐ LREAL                The constant "Tn" of the mean value filter
                  trol                                 element related to "Step"
                  SuppressionMode ⮫ IL_SUPPRES‐        Describes the function of the inputs "Sup‐
                                  SION_MODE            pressionLimitLow" and "SuppressionLimi‐
                                                       tHigh"
                  SuppressionLimi‐       LREAL         Upper value of the suppression window
                  tHigh                                (added to the mean value)
                  SuppressionLimi‐       LREAL         Lower value of the suppression window
                  tLow                                 (is subtracted from the mean value)
                  Value                  LREAL         The current actual process value

Name                 Type      Comment
StartValue           LREAL     The initial value applied at a rising edge at
                               "Enable" at the "OutputValue" output
VAR_OUTPUT         InOperation      BOOL          Processing without errors, output data is
                               valid
Error            BOOL          Error (see ErrorID and ErrorIdent)
ErrorID          ⮫ ERROR_CODE Error description
ErrorIdent       ⮫ ERROR_STRUC For a detailed error description, see
                 T             ⮫ Error codes on page 715
InPause          BOOL          Indicates that the "Pause" input is active
                               and the output values do not change
ActStep          UINT          Step value to which "OutputValue" refers
                               to. "ActStep" is initialized with the "Step"
                               value at a rising edge at "Enable"
MeanValue        LREAL         Filtered mean value compared to "Value"
OutputValue      LREAL         The computed output value
InLimitActive    BOOL          Indicates that the suppression window is
                               active
SuppressionCount UINT          Counter for the number of suppressed
                               values. The value is deleted at a rising
                               edge at "Enable" and counts up when
                               the suppression is active. When there is
                               again an unsuppressed input value, the
                               output is deleted again. In case of an over‐
                               flow (16xFFFF), the counter automatically
                               returns to "0"
SuppressionRatio LREAL         Percentage rate of all suppressed values
                               (0-100%)

Table 630: Min./max. and default values of the IL_SuppressionType02 inputs
Name                  Type             Min.         Max.      Default value   Effective
                                       value        value
Enable                BOOL                                      FALSE         Continuous
Pause                 BOOL                                      FALSE         Continuous
Step                  UINT                0        16#FFFF        0           Continuous
MeanFilterTCon‐       LTIME              0.0        N. def.     100 ms        Continuous
trol
SuppressionMode       IL_SUPPRES‐                             IL_SUPPRES‐     Rising edge at "Enable"
                      SION_MODE                                SION_PER‐
                                                                CENTAGE
SuppressionLimi‐      LREAL              0.0       N. def.        20.0        Continuous
tHigh
SuppressionLimi‐      LREAL              0.0       N. def.        20.0        Continuous
tLow
Value                 LREAL            N. def.     N. def.        0.0         Continuous
StartValue            LREAL            N. def.     N. def.        0.0         Rising edge at "Enable"

   Functional description
   When controlling, it is often required that the measured values with an obvi‐
   ously strong deviation from the expected value are filtered (suppressed).
   Therefore, a suppression window is implemented in the function block that
   moves along with the mean value of the value to be filtered and generates

a tolerance window around this mean value. Each measured value "Value" is
compared to the filtered measured value (filtering of the measured value with
a PT1 filter). If the respective measured value is not within the suppression
window around the mean value (tolerance window defined by "Suppression‐
LimitLow" or "SuppressionLimitHigh"), it is not output at the function block
output "OutputValue", but suppressed. Thus, the mean value is output instead
of “Value” at the "OutputValue" output.

Internal function block structure
The function block consists of an mean value filter and a block suppressing
the measured values. A PT1 element filters the mean value. The filter time
constant should be higher than the process time constant to allow a correct
mean value filtering. To diagnose the filtered mean value, use the "MeanValue"
output.

Window-cutting modes

In case of window-cutting, the upper threshold ("SuppressionLimitHigh") and
the lower threshold ("SuppressionLimitLow") can be configured separately.
There are two modes:
● Related to the mean value in percent (IL_SUPPRESSION_PERCENTAGE):
  The window width is specified by the percentage rate of the mean value.
  Thus, "SuppressionLimitHigh" specifies a percentage rate (from the abso‐
  lute value of the mean value) that is added to the mean value to main‐
  tain the upper threshold. "SuppressionLimitLow" specifies a percentage
  rate (from the absolute value of the mean value) that is subtracted from
  the mean value for the lower threshold. Note that the window size might
  become very small if the amount of the mean value becomes very small.
● Absolute window related to the mean value (IL_SUPPRESSION_ABSO‐
  LUTE_VALUE): The values at the inputs "SuppressionLimitLow" and "Sup‐
  pressionLimitHigh" directly specify the window size around the mean value.

mean value"
Diagnostics of the window-cutting
Observe the window-cutting function for diagnostic purposes using the out‐
puts "SuppressionCount" and "SuppressionRatio". "SuppressionCount" is a
counter that counts the suppression period of the measured values. It incre‐
ments if the suppression is active and reset to "0” if there is an input value
that is not suppressed. It is also reset to “0” at a rising edge at "Enable" as
well as in case of an overflow. "SuppressionRatio" is the percentage rate of
time of all suppressed values.

Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:
Table 631: Generated error numbers of the IL_SuppressionType02 function block
ErrorID                         Additional1 Additional2 Description
STATE_MACHINE_ERROR            16#0A0F0104 16#0C231000 Invalid function block state
INPUT_INVALID_ERROR            16#0A0F0104 16#0C230065 "SuppressionLimitHigh" value is lower
                                                        than 0.0
INPUT_INVALID_ERROR            16#0A0F0104 16#0C230066 "SuppressionLimitLow" value is lower
                                                        than 0.0
INPUT_INVALID_ERROR            16#0A0F0104 16#0C230067 "MeanFilterTControl" value is lower
                                                        than 0.0

### 21.8.8 IL_SuppressionType03

Brief description
This time-discreet function block suppresses measured values with an exces‐
sive deviation to the mean value of the measured values. The measured values
outside the threshold values that can be parameterized are not transferred,
but output as filtered value. The IL_SuppressionType03 is provided with func‐

   tional extensions compared to Type01. Two of the extensions are the two
   switchable limits for the suppression window as well as an additional sup‐
   pression function.

   Interface description

Table 632: Interface variables of the IL_SuppressionType03 function block
                   Name                 Type            Comment
VAR_INPUT          Enable               BOOL            Computation of data in each cycle when
                                                        "Enable" = TRUE
                   Pause                BOOL            The output data is not changed when
                                                        Pause = TRUE
                   MeanFilterTCon‐ LTIME                The constant "Tn" of the (PT1) mean value
                   trol                                 filter
                   SuppressionMode ⮫ IL_SUPPRES‐        Describes the function of the inputs "Sup‐
                                   SION_MODE            pressionLimitLow" and "SuppressionLimi‐
                                                        tHigh":
                                                        ● IL_SUPPRESSION_PERCENTAGE
                                                        ● IL_SUPPRESSION_ABSOLUTE_VALUE
                                                        ● IL_SUPPRESSION_STATISTICAL
                   SuppressionLimits ⮫ IL_SUPPRES‐      Selection of the active suppression
                                     SION_LIMITS        window:
                                                        ● IL_SUPPRESSION_OFF
                                                        ● IL_SUPPRESSION_LIMIT_1
                                                        ● IL_SUPPRESSION_LIMIT_2
                   Suppression‐         LREAL           Lower value of the suppression window #1
                   Limit1High
                   Suppression‐         LREAL           Upper value of suppression window #1
                   Limit1Low
                   Suppression‐         LREAL           Lower value of the suppression window #2
                   Limit2High
                   Suppression‐         LREAL           Upper value of suppression window #2
                   Limit2Low
                   Value                LREAL           The current actual process value
                   StartValue           LREAL           The initial value applied at a rising edge at
                                                        "Enable" at the "OutputValue" output
VAR_OUTPUT         InOperation          BOOL            Processing without errors, output data is
                                                        valid

Name                Type          Comment
Error               BOOL          Error (see ErrorID and ErrorIdent)
ErrorID             ⮫ ERROR_CODE Error description
ErrorIdent          ⮫ ERROR_STRUC For a detailed error description, see
                    T             ⮫ Error codes on page 720
InPause             BOOL          Indicates that the "Pause" input is active
                                  and the output values do not change
ActScanTime         LTIME         The time difference since the function
                                  block was called last
MeanValue           LREAL         Filtered mean value compared to "Value"

OutputValue         LREAL         The computed output value
InLimit1Active      BOOL          Indicates that suppression window #1 is
                                  active
InLimit2Active      BOOL          Indicates that suppression window #2 is
                                  active
SuppressionTime     LTIME         Time counter counting how long the meas‐
                                  ured values were suppressed. The value is
                                  deleted at a rising edge at "Enable" (T#0s)
                                  and increments in case of an active sup‐
                                  pression. When there is again an unsup‐
                                  pressed input value, the output is deleted
                                  again. In case of an overflow, the counter
                                  automatically returns to "0"
SuppressionRatio    LREAL         Percentage rate of all suppressed values
                                  (0-100%)

Table 633: Min./max. and default values of the IL_SuppressionType03 inputs
Name                 Type             Min.      Max.         Default value    Applied
                                      value     value
Enable               BOOL                                       FALSE         Continuous
Pause                BOOL                                       FALSE         Continuous
MeanFilterTCon‐      LTIME             0.0      N. def.         100 ms        Continuous
trol
SuppressionMode      IL_SUPPRES‐                             IL_SUPPRES‐      Rising edge at Enable
                     SION_MODE                                SION_PER‐
                                                               CENTAGE
SuppressionLimit     IL_SUPPRES‐                             IL_SUPPRES‐      Continuous
                     SION_LIMITS                             SION_LIMIT_1
Suppression‐         LREAL             0.0      N. def.           5.0         Continuous
Limit1High
Suppression‐         LREAL             0.0      N. def.           5.0         Continuous
Limit1Low
Suppression‐         LREAL             0.0      N. def.          20.0         Continuous
Limit2High
Suppression‐         LREAL             0.0      N. def.          20.0         Continuous
Limit2Low
Value                LREAL            N. def.   N. def.           0.0         Continuous
StartValue           LREAL            N. def.   N. def.           0.0         Rising edge at Enable

Functional description
When controlling, it is often required that the measured values with an obvi‐
ously strong deviation from the expected value are filtered (suppressed).
Therefore, a suppression window is implemented in the function block that
moves along with the mean value of the value to be filtered and generates
a tolerance window around this mean value. Each measured value "Value" is
compared to the filtered measured value (filtering of the measured value with
a PT1 filter). If the respective measured value is not within the suppression
window around the mean value (tolerance window defined by "Suppression‐
Limit1/2Low" or "SuppressionLimit1/2High"), it is not output at the function
block output "OutputValue", but suppressed instead. Thus, the mean value is
output instead of “Value" at the "OutputValue" output.
The function is provided with two different windows between which can be
switched. Additionally, the suppression function is deactivated. This can be
used to increase the suppression window for a short period if operated with
great deviations (e.g. in case of transient processes).

Internal function block structure
The function block consists of an mean value filter and a block suppressing
the measured values. A PT1 element filters the mean value. The filter time
constant should be higher than the process time constant to allow a correct
mean value filtering. The filtered mean value can be diagnosed via the "Mean‐
Value" output.

Window-cutting modes
In case of window-cutting, the upper threshold ("SuppressionLimit1/2High")
and the lower threshold ("SuppressionLimit1/2Low") can be configured sepa‐
rately. There are three modes:
● Related to the mean value in percent (IL_SUPPRESSION_PERCENTAGE):
  The window width is specified by the percentage rate of the mean value.
  Thus, "SuppressionLimitHigh" specifies a percentage rate (from the abso‐
  lute value of the mean value) that is added to the mean value to main‐
  tain the upper threshold. "SuppressionLimitLow" specifies a percentage
  rate (from the absolute value of the mean value) that is subtracted from
  the mean value for the lower threshold. Note that the window size might
  become very small if the amount of the mean value becomes very small.
● Absolute window related to the mean value (IL_SUPPRESSION_ABSO‐
  LUTE_VALUE: The values at the inputs "SuppressionLimitLow" and "Sup‐
  pressionLimitHigh" directly specify the window size around the mean value.
● Related to the statistic deviations of the input signals (IL_SUPPRES‐
  SION_STATISTICAL): The window width is related to the standard devia‐
  tion σ of the measurement signal. That means that the standard deviation
  σ of the measurement signal with the values of the inputs “Suppression‐
  Limit1/2Low” and “SuppressionLimit1/2High” is multiplied and results in
  the window size. (To determine the standard deviation, an exponentially
  floating computation is used with the "MeanFilterTControl" as time con‐
  stant)

mean value"
Diagnostics of the window-cutting
Observe the window-cutting function for diagnostic purposes using the out‐
puts "SuppressionTime" and "SuppressionRatio". "SuppressionTime" is a time
counter that counts the suppression period of the measured values. It incre‐
ments if the suppression is active and reset to "0" if there is an input value
that is not suppressed. It is also reset to “0” at a rising edge at "Enable" as
well as in case of an overflow. "SuppressionRatio" is the percentage rate of
time of all suppressed values.

Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:

Table 634: Generated error numbers of the IL_SuppressionType03 function block
ErrorID                         Additional1 Additional2 Description
STATE_MACHINE_ERROR            16#0A0F0104 16#0C231000 Invalid function block state
INPUT_INVALID_ERROR            16#0A0F0104 16#0C230065 "SuppressionLimit1/2High" value is
                                                        lower than 0.0
INPUT_INVALID_ERROR            16#0A0F0104 16#0C230066 "SuppressionLimit1/2Low" value is
                                                        lower than 0.0
INPUT_INVALID_ERROR            16#0A0F0104 16#0C230067 "MeanFilterTControl" value is lower
                                                        than 0.0
INPUT_INVALID_ERROR            16#0A0F0104 16#0C230068 "MeanFilterTControl" value is lower
                                                        than (2 x "ActScanTime"); only relevant

                                      in "Statistical" mode

### 21.8.9 IL_SuppressionType04

   Brief description
   This event-controlled function block suppresses measured values with an
   excessive deviation to the mean value of the measured values. The measured
   values outside the threshold values that can be parameterized are not trans‐
   ferred, but output as filtered value. The IL_SuppressionType04 is provided
   with functional extensions compared to Type02. Two of the extensions are the
   two switchable limits for the suppression window as well as an additional
   suppression function.

   Interface description

Table 635: Interface variables of the IL_SuppressionType04 function block
                  Name                   Type          Comment
VAR_INPUT         Enable                 BOOL          Computation of data in each cycle (step)
                                                       while "Enable" = TRUE
                  Pause                  BOOL          The output data is not changed when
                                                       "Pause" = TRUE. If the “Step” input incre‐
                                                       ments in the meantime, the step at the
                                                       "ActSteps" output is issued.
                  Step                   UINT          Current computation step
                  MeanFilterTCon‐        LREAL         The constant "Tn" of the mean value filter
                  trol                                 element related to "Step"

Name            Type               Comment
SuppressionMode ⮫ IL_SUPPRES‐      Describes the function of the inputs "Sup‐
                SION_MODE          pressionLimitLow" and "SuppressionLimi‐
                                   tHigh":
                                   ● IL_SUPPRESSION_PERCENTAGE
                                   ● IL_SUPPRESSION_ABSOLUTE_VALUE
                                   ● IL_SUPPRESSION_STATISTICAL
SuppressionLimits ⮫ IL_SUPPRES‐    Selection of the active suppression
                  SION_LIMITS      window:
                                   ● IL_SUPPRESSION_OFF
                                   ● IL_SUPPRESSION_LIMIT_1
                                   ● IL_SUPPRESSION_LIMIT_2
Suppression‐         LREAL         Lower value of the suppression window #1
Limit1High
Suppression‐         LREAL         Upper value of suppression window #1
Limit1Low
Suppression‐         LREAL         Lower value of the suppression window #2
Limit2High
Suppression‐         LREAL         Upper value of suppression window #2
Limit2Low
Value                LREAL     The current actual process value
StartValue           LREAL     The initial value applied at a rising edge at
                               "Enable" at the "OutputValue" output
VAR_OUTPUT         InOperation      BOOL          Processing without errors, output data is
                               valid
Error            BOOL          Error (see ErrorID and ErrorIdent)
ErrorID          ⮫ ERROR_CODE Error description
ErrorIdent       ⮫ ERROR_STRUC For a detailed error description, see
                 T             ⮫ Error codes on page 726
InPause          BOOL          Indicates that the "Pause" input is active
                               and the output values do not change
ActStep          UINT          Step value to which "OutputValue" refers.
                               "ActStep" is initialized with the "Step"
                               value at a rising edge at "Enable"
MeanValue        LREAL         Filtered mean value compared to "Value"
OutputValue      LREAL         The computed output value
InLimit1Active   BOOL          Indicates that suppression window #1 is
                               active
InLimit2Active   BOOL          Indicates that suppression window #2 is
                               active
SuppressionCount UINT          Counter for the number of suppressed
                               values. The value is deleted at a rising
                               edge at "Enable" and counts up when
                               the suppression is active. When there is
                               again an unsuppressed input value, the
                               output is deleted again. In case of an over‐
                               flow (16xFFFF), the counter automatically
                               returns to "0"
SuppressionRatio LREAL         Percentage rate of all suppressed values
                               (0-100%)

Table 636: Min./max. and default values of the IL_SuppressionType04 inputs
Name                 Type            Min.      Max.         Default value    Applied
                                     value     value
Enable               BOOL                                      FALSE         Continuous
Pause                BOOL                                      FALSE         Continuous
Step                 UINT              0      16#FFFF            0           Continuous
MeanFilterTCon‐      LTIME            0.0      N. def.         100 ms        Continuous
trol
SuppressionMode      IL_SUPPRES‐                            IL_SUPPRES‐      Rising edge at Enable
                     SION_MODE                               SION_PER‐
                                                              CENTAGE

SuppressionLimit     IL_SUPPRES‐                            IL_SUPPRES‐      Continuous
SION_LIMITS                            SION_LIMIT_1
Suppression‐         LREAL            0.0     N. def.            5.0         Continuous
Limit1High
Suppression‐         LREAL            0.0     N. def.            5.0         Continuous
Limit1Low
Suppression‐         LREAL            0.0     N. def.           20.0         Continuous
Limit2High
Suppression‐         LREAL            0.0     N. def.           20.0         Continuous
Limit2Low
Value                LREAL          N. def.   N. def.            0.0         Continuous
StartValue           LREAL          N. def.   N. def.            0.0         Rising edge at Enable

Functional description
When controlling, it is often required that the measured values with an obvi‐
ously strong deviation from the expected value are filtered (suppressed).
Therefore, a suppression window is implemented in the function block that
moves along with the mean value of the value to be filtered and generates
a tolerance window around this mean value. Each measured value "Value" is
compared to the filtered measured value (filtering of the measured value with
a PT1 filter). If the respective measured value is not within the suppression
window around the mean value (tolerance window defined by "Suppression‐
Limit1/2Low" or "SuppressionLimit1/2High"), it is not output at the function
block output "OutputValue", but suppressed instead. Thus, the mean value is
output instead of “Value" at the "OutputValue" output.
The function is provided with two different windows between which can be
switched. Additionally, the suppression function is deactivated. This can be
used to increase the suppression window for a short period if operated with
great deviations (e.g. in case of transient processes).

Internal function block structure
The function block consists of an mean value filter and a block suppressing
the measured values. A PT1 element filters the mean value. The filter time
constant should be higher than the process time constant to allow a correct
mean value filtering. To diagnose the filtered mean value, use the "MeanValue"
output.

Window-cutting modes
In case of window-cutting, the upper threshold ("SuppressionLimit1/2High")
and the lower threshold ("SuppressionLimit1/2Low") can be configured sepa‐
rately. There are three modes:

● Related to the mean value in percent (IL_SUPPRESSION_PERCENTAGE):
The window width is specified by the percentage rate of the mean value.
Thus, "SuppressionLimitHigh" specifies a percentage rate (from the abso‐
lute value of the mean value) that is added to the mean value to main‐
tain the upper threshold. "SuppressionLimitLow" specifies a percentage
rate (from the absolute value of the mean value) that is subtracted from
the mean value for the lower threshold. Note that the window size might
become very small if the amount of the mean value becomes very small.
● Absolute window related to the mean value (IL_SUPPRESSION_ABSO‐
LUTE_VALUE: The values at the inputs "SuppressionLimitLow" and "Sup‐
pressionLimitHigh" directly specify the window size around the mean value.
● Related to the statistic deviations of the input signals (IL_SUPPRES‐

SION_STATISTICAL): The window width is related to the standard devia‐
tion σ of the measurement signal. That means that the standard deviation
σ of the measurement signal with the values of the inputs “Suppression‐
Limit1/2Low” and “SuppressionLimit1/2High” is multiplied and results in
the window size. (To determine the standard deviation, an exponentially
floating computation is used with the "MeanFilterTControl" as time con‐
stant)

mean value"
Diagnostics of the window-cutting
Observe the window-cutting function for diagnostic purposes using the out‐
puts "SuppressionCount" and "SuppressionRatio". "SuppressionCount" is a
counter that counts the suppression period of the measured values. It incre‐
ments if the suppression is active and reset to "0” if there is an input value
that is not suppressed. It is also reset to “0” at a rising edge at "Enable" as
well as in case of an overflow. "SuppressionRatio" is the percentage rate of
time of all suppressed values.

Error codes
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:
Table 637: Generated error numbers of the IL_SuppressionType04 function block
ErrorID                          Additional1 Additional2 Description
STATE_MACHINE_ERROR             16#0A0F0104 16#0C231000 Invalid function block state
INPUT_INVALID_ERROR             16#0A0F0104 16#0C230065 "MeanFilterTControl" value is lower
                                                         than 0.0
INPUT_INVALID_ERROR             16#0A0F0104 16#0C230066 "SuppressionLimit1/2High" value is
                                                         lower than 0.0
INPUT_INVALID_ERROR             16#0A0F0104 16#0C230067 "SuppressionLimit1/2Low" value is
                                                         lower than 0.0
INPUT_INVALID_ERROR             16#0A0F0104 16#0C230068 The "MeanFilterTControl" value has to
                                                         be twice the difference of two (dif‐
                                                         ferent) sequent "Step" values (only in
                                                         "Statistical" mode)

## 21.9 Temperature controller

### 21.9.1 Introduction and overview

The following function blocks control temperature-controlled systems.
Table 638: Temperature controller function blocks of the CXA_LoopControl
Area of application (folder in library)
Function blocks                                Description
Temperature controller (TemperatureController)
⮫ Chapter 21.9.2 IL_TempControl on page 727    Controller for the temperature-controlled system
                                               with automatic offline controller setting

### 21.9.2 IL_TempControl

Brief description
The IL_TempControl function block controls the temperature. It can determine
the controller parameters either independently or using specifications.
Advantages of the two variants:
●   Shorter identification period (StartAutoTune)
●   Changed controller parameterization (Preset)
●   Changed fine controller adjustment (DampingFactor)
●   Input/output of the controlled system parameters (ModelParam)
●   Individual controller design (ControlMode)

Interface description

Table 639: Interface variables of the IL_TempControl function block
I/O type       Name                Data type          Description
VAR_INPUT      Enable              BOOL               The function block is enabled if this input
                                                      is "TRUE". The function block outputs are
                                                      reset to their default value with a falling
                                                      edge.
               Preset              BOOL               A rising edge at this input applies the con‐
                                                      troller or controlled system parameters of
                                                      the structures "ContrParam" and/or "Mod‐
                                                      elParam"

I/O type           Name               Data type      Description
StartAutoTune      BOOL           A rising edge at this input starts the auto-
                                  tuning. If this input is set together with
                                  "Enable", the controller parameters do not
                                  have to be specified
SetPoint           LREAL          Command temperature.
                                  Unit [u]*
SetPointGradient   LREAL          Maximum change of the "Setpoint" param‐
                                  eter
                                  Unit [u/s]
Feedback           LREAL          Actual temperature.
                                  Unit [u]
Pause              BOOL           This input "freezes" the control variable
                                  and the controller computation
ControlMode        ⮫ IL_TEMP‐     Selection of the control loop response.
                   CONTROL_CON‐   Either the open-loop control in the open
                   TROL_MODE      control loop or the closed-loop control
                                  optimize the command value response or
                                  the disturbance response in the closed con‐
                                  trol loop
ManContrValue      LREAL          This input specifies the control variable
                                  when controlling manually.
                                  Unit [%]
DampingFactor      LREAL          This input affects the control loop
                                  response. It can be selected without step
                                  between a slow aperiodic and a fast oscil‐
                                  lating response.
                                  Unit [-]
AutoTuneMax‐       LREAL          Control variable limitation at the beginning
Power                             of the auto-tuning.
                                  Unit [%]
OutputPowerMax     LREAL          Limitation of the controller output. If a
                                  control signal limitation in the controlled
                                  system is smaller than the limitation of the
                                  controller output, the anti-windup function
                                  of the controller can be restricted.
                                  Unit [%]
StartUpTemp        LREAL          Startup temperature. Only active if a value
                                  unequal to 0 is assigned to the "StartUp‐
                                  Time" input.
                                  Unit [u]
StartUpTime        LTIME          Startup time, i.e. the period during which
                                  the startup temperature ("StartUpTemp") is
                                  not changed until the "normal" closed-loop
                                  control is started. The preset value is T#0s
                                  (not active)
ExtendedSettings   ⮫ IL_TEMPCON‐  Structure with the extended setting options
                   TROL_EXTENDED_ of the auto-tuning. The default settings are
                   SETTINGS       sufficient for the common controlled sys‐
                                  tems

I/O type        Name                  Data type      Description
Limits                ⮫ IL_TEMPCON‐  Structure  with the alarm limits in [u]
                      TROL_ LIMITS   (units).
                                     Unit [u]
VAR_OUTPUT InOperation                BOOL           This output is set if "Enable" is set and if
                                     the function block is active
Error                 BOOL           An error occurred at runtime. The control
                                     variable is set to 0[%]
ErrorID               ⮫ ERROR_CODE   If the "Error" output is set, it contains a
                                     broad error classification

ErrorIdent            ⮫ ERROR_STRUCT If the "Error" output is set, this output con‐
                                     tains detailed error information
                               ⮫ Troubleshooting on page 735
InPause         BOOL           The "ControlValueAnalog" output is frozen
                               and the "ControlValuePWM" output remains
                               active with this value
AutoTuneActive  BOOL           Auto-tuning is active
AutoTuneDone    BOOL           Auto-tuning was completed successfully
ControlValueA‐  LREAL          Analog value of the control variable.
nalog                          Unit [%]
ControlValuePWM BOOL           Digital, pulse width-modulated control vari‐
                               able value.
                               Unit [-]
SetPointReached BOOL           Status output whether the actual
                               value is within the limits (Setpoint
                               " + Limits.UpperAtSetpoint) >=
                               Actual value >= (Setpoint -
                               Limits.LowerAtSetpoint)
VAR_IN_OUT      ContrParam      ⮫ IL_TEMPCON‐  This structure contains the current parame‐
                TROL_ CONTR_PA ters KP , KI and KD of the controller as well
                RAM            as the dead time Tt
ModelParam            ⮫ IL_TEMPCON‐  This structure contains the parameters KS
                      TROL_ MODEL_PA and TS of the controlled system
                      RAM
        ● * The unit [u] means unit. This can be any unit such as [°C] or [°F]. Ensure
          that the selected unit is always used.

    The following table lists the min./max. and default values as well as the
    application response of the function block inputs:
Table 640: Min./max. and default values as well as the application response of the inputs of the
function block IL_TempControl
Name            Type               Min. value      Max. value      Default value   Applied
Enable          BOOL               FALSE           TRUE            FALSE           Cyclic
Preset          BOOL               FALSE           TRUE            FALSE           Cyclic
StartAutoTune   BOOL               FALSE           TRUE            FALSE           Cyclic
SetPoint        LREAL              N. def.         N. def.         0               Cyclic
SetPointGra‐    LREAL              0               N. def.         0               Cyclic
dient
Feedback        LREAL              N. def.         N. def.         0               Cyclic
Pause           BOOL               FALSE           TRUE            FALSE           Cyclic

Name               Type            Min. value    Max. value       Default value   Applied
ControlMode        IL_TEMPCON‐     CON‐          CON‐             CON‐            Cyclic
TROL_ CON‐      TROL_TEMP‐    TROL_TEMP‐       TROL_TEMP‐
TROL_MODE       MODE_         MODE_            MODE_
                MANUAL        ONLY_DIS‐        ONLY_DIS‐
                              TURBANCE         TURBANCE
ManContr‐     LREAL                0             100              0               Cyclic
Value
DampingFactor LREAL                20            200              100             Cyclic
AutoTuneMax‐ LREAL                 >0            100              80              At a rising edge at
Power                                                                             "StartAutoTune"
OutputPo‐     LREAL                >0            100              100             Cyclic
werMax
StartUpTemp LREAL                  N. def.       N. def.          0               At a rising edge at
                                                               "Enable"
StartUpTime        LTIME           LTIME#0s      N. def.          LTIME#0s        At a rising edge at
                                                               "Enable"
ExtendedSet‐       IL_TEMPCON‐     See "Data     See "Data        See "Data       See "Data struc‐
tings              TROL_           structure"    structure"       structure"      ture"
EXTENDED_
SETTINGS
Limits             IL_TEMPCON‐     See "Data     See "Data        See "Data       See "Data struc‐
TROL_ LIMITS    structure"    structure"       structure"      ture"
ContrParam         IL_TEMPCON‐     See "Data     See "Data        See "Data       See "Data struc‐
TROL_           structure"    structure"       structure"      ture"
CONTR_PARA
M
ModelParam         IL_TEMPCON‐     See "Data     See "Data        See "Data       See "Data struc‐
TROL_           structure"    structure"       structure"      ture"
MODEL_PARA
M

   Functional description
   The function block can be operated at the ctrlX system. The actual tempera‐
   ture to be controlled can be determined using Inline temperature modules (IL
   TEMP 2 RTD) or provided differently via a field bus connection for example).
   The internal PID-controller can either be parameterized as P-, PI-, PD- or PID-
   controller or the function block can automatically determine "StartAutoTune"
   controller parameters via an auto-tuning.

   Controller/controlled system parameters
   The identification of the auto-tuning temperature controller function block
   IL_TempControl was designed to ensure that the control loop is now closed
   when starting the auto-tuning and that the controller parameters continuously
   follow the currently identified controlled system parameters.
   For this functionality, set the "StartAutoTune" input with the controller design
   procedure "ControlMode".
   Auto-tuning is not required for known controller or controlled system parame‐
   ters. In this case, the values are specified via the inputs "ContrParam" and/or
   "ModelParam" and applied with a rising edge at the "Preset" input.
   A PT1-filter continuously smoothes the actual temperature value "Feedback" in
   the function block to reduce disturbances. The time constant of the filter is
   nearly 20 times higher than the cycle time (TFilt=20*TTask).

Due to this and further secondary delays caused by the process, the temper‐
ature controlled system can be assumed as non-oscillating PT2 controlled sys‐
tems with a dominant compensation constant Ts and a secondary delay Tt.

The following step response of a temperature-controlled system is an example
assuming that the controlled system parameter shows Ks = 1°C/%, Ts=10 s

and Tt = 1 s.

In case of an auto-tuning, the control loop is directly closed with a P-con‐
troller with a rising edge at the "StartAutoTune" input to cause a controlled
system reaction. The initial, proportional controller parameter KP is used
either from the "ContrParam" structure, computed from the present controlled
system parameters (Ks,Ts,Tt) or pre-assigned with a positive and internally
stored value. While the actual value approximates the command value, the
controlled system response is continuously identified and the controller set‐
tings follow the controlled system information. After the identification, the
"AutoTuning" is automatically completed and the determined controller and
controlled system parameters are applied to the "ModelParam" (Ks,Ts) and
"ContrParam" (KP,KI,KD,Tt) structures.

Cooling
If there is a cooling, the KP input has to be pre-assigned with a negative value
to initiate the system for the first time. Due to the control signal limitation and
the controller adaptation, KP=-10000 can be specified for the initial identifica‐
tion.

Control signal limitation
If the actual value is changed by 20 % of the command value change, there
is already sufficient information on the dynamic controlled system response
to calculate the controller parameters. Thus, at this point in time, the control

signal limitation "AutoTuneMaxPower" of the automatically set PI-controller is
increased to the maximum controller output "OutputPowerMax" to achieve
the fastest correction time possible.

Preset; controller parameter
The internal PID-controller can also be used as P-controller, PI-controller, PD-
controller or PID-controller if individual controller values are set to zero. The
controller parameterization as purely integrating I-controller is not supported
with regard to the expected controlled system response.

Preset; controlled system parameter
In addition to the controller parameterization using the specified controller
parameters, specified controlled system parameters can also be used for
parameterization purposes. If all controller parameters (KP, KI and KD) of the
"ContrParam" structure are zero when there is a rising edge at the "Preset"
input, it is checked internally whether all controlled system parameters (Ks, Ts
and Tt) are present in the "ModelParam" and "ContrParam" structures. After
the plausibility check of these controlled system parameters, a PI-controller
is designed on this basis. The advantage of this controller parameterization
is that the set controller can be switched between the disturbance and com‐
mand value response and that the controller can be re-adjusted using the
"DampingFactor".

controlled system parameters
To ensure known controlled system and/or controller parameters, back them
up in the retain area.
The structures "ContrParam" and/or "ModelParam” containing the controller
and/or controlled system parameters can be created as retain variables (VAR
RETAIN).

AutoTuneMaxPower
Due to the dominant time constant Ts and a secondary delay time Tt, a step
response without control signal limitation results up to the point in time
t~Ts/3. An IT1 system can also write to the step response. To determine con‐
troller parameters at this early stage of the self-adjustment (up to a change of
20% of the actual value), it might be required to limit the controller output
signal additionally ("AutoTuneMaxPower"). Whether this is required depends
on the relation of the controlled system constants. Thus, the transient of the
delay time Tt can already be completed at this point in time (20% of the
actual value change) even at a low quotient of the time constants Ts/Tt<10.
This results in sufficient information for a controller design.

DampingFactor
This input can be used to re-adjust the determined controller parameters
either automatically via "StartAutoTune" or manually via "Preset" using the
specification of the controlled system parameters Ks, Ts, Tt). Changing and
deviating parameters not covered in a fast and slow control-loop response for

ideal controlled system parameters can thus also be included. Therefore, the
linear interpolation of the controller parameters was extended between an
oscillating and aperiodic transient using an extrapolation.
For ideal controlled system parameters, a "DampingFactor" of 100 corre‐
sponds exactly to an aperiodic boundary case and a "DampingFactor" of 120
corresponds to an transient oscillation with approximately 20% of overshoot.
Thus, the control loop response can be decelerated accordingly with a "Damp‐
ingFactor" of up to 20 or accelerated with a "DampingFactor" of up to 200. If
there are controlled system parameters or a system response deviating from
the LREAL behavior, the requested dynamic control loop response can be
corrected using this input.

StartUpTemp/StartUpTime
If a process prior to the actual temperature control requires a pause at a cer‐
tain temperature for a certain period (startup ramp), this function is available
via the inputs "StartUpTemp" and "StartUpTime".
First, the controller controls until the startup temperature "StartUpTemp".
If this temperature is reached, the startup time "StartUpTime" expires and
the controller keeps the startup temperature constant. After the startup time
"StartUpTime" elapsed, the startup ramp is completed and the controller
shows its normal behavior. The startup ramp is executed once at each rising
edge at the "Enable" input.

Limits
Alarm and status limits can be created for process monitoring purposes.
The "Limits" structure contains the values "UpperAlarm" and "LowerAlarm".
When exceeding the alarm limits, an error is generated. The monitoring func‐
tion is only enabled, when the current process temperature ranges between
"UpperAlarm" and "LowerAlarm” to avoid an error during process start. These
values are absolute values.
The "Limits“ structure also contains the values "UpperAtSetPoint" and
"LowerAtSetPoint". The "SetPointReached" is set when the condition
(Setpoint – Limits.LowerAtSetPoint) ≤ Feedback ≤ (Setpoint +
Limits.UpperAtSetPoint) is met.
These values are relative values referring to the "Setpoint". The "Set‐
point" can thus be modified without changing "Limits.LowerAtSetPoint" and
"Limits.UpperAtSetPoint". Based on this status display, it can be determined
whether the requested temperature has already been reached.

Pause
The closed-loop control can be paused via the "Pause" input. The control vari‐
able remains constant and the controller as well as all its values are frozen.
After the "Pause" input is reset, the closed-loop control continues. A jump can
result if the actual value has changed significantly in the meantime.

SetPointGradient
The function block can limit the increase of the command value. This reduces
the overshoot width and prevents the unit from damages. For each new spec‐
ification of the "SetPoint" input, the command value is internally changed in
ramps (not in steps) until the requested command value is reached.
"SetPointGradient" is entered into [rps]

ControlMode
Use this input to select between a control in the open control loop and
a closed-loop control (optimized to the command value or disturbance
response) in a closed control loop.
The manual control variable "ManContrValue" can for example be used before
an auto-tuning to control the controlled variable in the operating point or
when an error occurs in the actual value detection.
In           the           default           setting            ControlMode:=
CONTROL_TEMPMODE_ONLY_DISTURBANCE, a fast and robust distance identifica‐
tion is implemented. In this mode, it is explicitly optimized to disturbance
reaction (due to optimizations). Accordingly, it cannot be changed to another
optimization method without another auto-tuning.
Furthermore, a failed identification due to an insufficient distance reaction is
signaled in this mode by the controller and distance parameters NULL.

Control loop monitoring
The function block is provided with a gradient monitoring of the actual value
reporting in case of very high deviations. There can be deviations for example
if the sensor displays an error code and if this error code is not detected/
evaluated by the user. The gradient is set to [10 rms]. A one-time exceedance
is tolerated before an error is generated.

Task interval/PWM
The pulse-width modulation (PWM) is based on the task interval, i.e. the task
interval is the smallest possible time slice which can be set to "ON" or "OFF"
during the PWM. One PWM period is 20 times longer than the task interval.
Thus, control variables can be modulated in steps of 5 % with a resolution
between 0 % to 100 %.
Set the task interval/cycle time with regard to the control element and the
controlled system to ensure that the PWM does not cause any visible tempera‐
ture changes in one PWM period (20*task interval). Thus, if the temperature
gradient changes noticeably between the switched-on and switched-off state
of the PWM period due to the control variable, the selected task interval is
too high.
Do not use a task interval that is too small, since the control element (e.g.
relay module) is subject to an increased load.
Furthermore, the sampling time is monitored function block-internally. This
sampling time generates an error if it exceeds/falls below by more than 20 %
and sets the "Error" output to TRUE.

Auto-tuning
Note the following for the best auto-tuning possible:

● Temperature-controlled systems are mostly not linear over a wide range.
  Thus, if there is an identical temperature change, the following applies:
  The higher the temperature, the higher the control signal change required
  and vice versa. Thus, a controller requires temperature-dependent settings.
  Thus, perform the identification in a temperature range in which the con‐
  troller is used later on.
● At runtime, the auto-tuning can be started again at a rising edge at the
  "StartAutoTune“ input. This can for example be reasonable for a level
  change or if there are any other modifications at the controlled system.
  Ensure a sufficient system initiation (actual value change) for an optimum
  identification.
● Auto-tuning can only be executed if the command value is higher than the

  actual temperature for a heating and if the actual temperature is higher
  than the command value for a cooling.

Special influencing variables of the auto-tuning
In special cases, the following measures can improve the "AutoTuning":
● The "ExtendedSettings.IdentAccuracy” input can affect the abort criteria.
  It is aborted either when reaching this change rate or at double the correc‐
  tion time with this limit. This depends on which criterion is met first.
● Use the "ExtendedSettings.OblivionFactor" input to include changeable
  controlled system parameters in the "AutoTuning". For controlled system
  parameters varying in time, a reduction of this input is reasonable. For
  controlled system parameters not varying in time, an increase of this input
  is reasonable.
● The "ExtendedSettings.MinDelayTime" input specifies a minimum delay
  time Tt as a priori information. This value is used for the "AutoTuning" if no
  value is specified at the "ContrParam.Tt" input. This value corresponds to
  the minimum controlled system delay time possible which cannot be lower
  than the sum of all secondary transport, delay and filter time constants.

Troubleshooting
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1/Additional2:
Table 641: Error codes of the IL_TempControl function block
ErrorID           Additional1              Additional2    Description
STATE_MACHINE_ERR 16#0A0F0104              16#0C2300+Cur‐ Error in the state machine; invalid
OR                                         rent state     state
INPUT_RANGE_ERROR 16#0A0F0104              16#0C230071    Input values for maximum output
                                                          value ("OutputPowerMax") beyond the
                                                          valid range. Value has to be higher
                                                          than 0 [%] up to max. 100 [%]
INPUT_RANGE_ERROR 16#0A0F0104              16#0C230072    Input values invalid for alarm limits.
                                                             (Condition: Limits.UpperAlarm >
                                                             Limits.LowerAlarm)
INPUT_RANGE_ERROR 16#0A0F0104              16#0C230073       Input value for manual control variable
                                                             ("ManContrValue") invalid. Value has
                                                             to be between 0[%] and 100[%]
INPUT_RANGE_ERROR 16#0A0F0104              16#0C230074       Controller parameter invalid. There are
                                                             either no controller parameters or the
                                                             controller parameters are invalid

ErrorID           Additional1          Additional2    Description
INPUT_RANGE_ERROR 16#0A0F0104          16#0C230075    Controlled system constant is invalid.
Either the time constant "Model‐
Param.Ts" or "ContrParam.Tt" is
invalid
INPUT_RANGE_ERROR 16#0A0F0104          16#0C230076    Input value "OblivionFactor" is invalid.
Value has to be between 0.9 and 1
INPUT_RANGE_ERROR 16#0A0F0104          16#0C230077    Input value "MinDelayTime" is invalid.
Value has to be higher than T#0s
INPUT_RANGE_ERROR 16#0A0F0104          16#0C230078    Input value "IdentAccuracy" is invalid.
Value has to be higher than 0 [%/s]
INPUT_RANGE_ERROR 16#0A0F0104          16#0C230079    Input value "DampingFactor" is invalid.
Value has to be between 20 and 200
INPUT_RANGE_ERROR 16#0A0F0104          16#0C23007A    Input value "SetPointGradient" is
invalid. Value has to be higher than 0
[u/s]
INPUT_RANGE_ERROR 16#0A0F0104          16#0C23007B    Input values invalid for status limits
(Condition: (Setpoint
+ Limits.UpperAtSetpoint)
> (Setpoint -
Limits.LowerAtSetpoint)
INPUT_RANGE_ERROR 16#0A0F0104          16#0C23007C    Input value "ContrMode" is invalid
INPUT_RANGE_ERROR 16#0A0F0104          16#0C23007D    Input value "AutoTuneMaxPower" is
invalid. Value has to be between 0[%]
and 100[%]
INPUT_RANGE_ERROR 16#0A0F0104          16#0C23007E    Input value "ExtendedSettings.Control‐
Type" is invalid.
INPUT_RANGE_ERROR 16#0A0F0104          16#0C23007F    Input value "ExtendedSettings.bCon‐
trol" is invalid. Value has to be
between 0[-] and 1[-]
INPUT_RANGE_ERROR 16#0A0F0104          16#0C230081    Input value "ExtendedSettings.cCon‐
trol" is invalid. Value has to be
between 0[-] and 1[-]
SYSTEM_ERROR             16#0A0F0104   16#0C23+Sam‐   Jittering the sampling time > 20[%].
pling time     Error becomes only active after two
successive timeouts
SYSTEM_ERROR             16#0A0F0104   16#0C230082    Gradient of the actual value is too
high. Sensor fault possible
CALCULATION_ERROR 16#0A0F0104          16#0C230083    Identified controlled system parame‐
ters are invalid, self-identification of
the controlled system failed
DEVICE_ERROR             16#0A0F0104   16#0C23+Tem‐   Temperature error limit exceeded.
perature       Temperature beyond error limits

Information on specific errors
● "Controller parameter invalid"
(Additional1 = 16#0A0F0104; Additional2 = 16#0C230074):
Cause: Either there are no controller parameters or the controller param‐
eters created in the input/output structure "ContrParam" are incorrect.
To ensure that the temperature controller can create a reasonable con‐
trol signal either in the operation mode CONTROL_TEMPMODE_OPT_COMMAND
or CONTROL_TEMPMODE_OPT_DISTURBANCE, at least one proportional con‐
troller with a Kp unequal to zero is required. Its number depends on the
control direction (positive = heating and negative = cooling.
Troubleshooting: The temperature controller can either determine the con‐

trolled system and controller parameters. Controller parameters can be
specified or the controller can determine the controller parameters using
the controlled system parameters. For the auto-tuning without specified
controller parameters, it is required to start the auto-tuning at a rising edge
at "StartAutoTune". To specify the controller parameters, use the requested
controller parameters at the input/output structure "ContrParam" and
apply them with a rising edge at the "Preset" input. To specify the con‐
trolled system parameters, set the proportional controller parameter ("Con‐
trParam.KP") to zero in the input/output structures "ModelParam" and
"ContrParam", use the controlled system parameters ("ModelParam.Ks",
"ModelParam.Ts" and "ContrParam.Tt") and start the controller computa‐
tion with a rising edge at the "Preset" input
● "Identified controlled system parameters are invalid, self-identification of
the controlled system failed"
(Additional1 = 16#0A0F0104; Additional2 = 16#0C230075):
The identification of the controlled system response and the resulting con‐
troller parameterization failed.
– "ControlMode:= CONTROL_TEMPMODE_ONLY_DISTURBANCE":
   Cause: The "AutoTuneMaxPower" input is too large for the existing con‐
   trolled system. Consequently, the distinctive controlled system reaction
   could not be detected within the first half of the actual value change.
   Troubleshooting: Reduction of the input "AutoTuneMaxPower".
– "ControlMode:= CONTROL_TEMPMODE_OPT_xxxxx":
   Cause: Identification failure can cause a unfavorable specified con‐
   trolled system delay time "ContrParam.Tt", a task interval that is too
   high, a controlled system that is not sufficiently transient at the identifi‐
   cation point in time, a controlled system initiation that is too low or an
   incorrect actual value detection (sensor not connected).
   Troubleshooting: If the auto-tuning failed due to an incorrect sampling
   time, a rough estimation of the controlled system delay time can be
   specified as information on the auto-tuning at the "ContrParam.Tt" input
   and/or the task interval can be reduced. If the auto-tuning of the tem‐
   perature controller failed due to the controlled system not being suffi‐
   ciently transient, the repeat the auto-tuning with a stationary transient
   controlled system. If the auto-tuning failed due to an insufficient con‐
   trolled system initiation, repeat the auto-tuning with a bigger command
   value change. If the temperature detection is defective, the error has to
   be recovered

### 21.9.3 IL_TEMPCONTROL_CONTROL_TYPE

The enumeration type IL_TEMPCONTROL_CONTROL_TYPE is used to select a
specific controller type (PI or PID) used as basis for the internal controller
parameterization ("Autotune" or "Preset") with the distance parameters.

        Depending on this “Autotuning" setting, the internal PID controller can be
        parameterized as P-, PI- or PID-controller via a “Preset" of the respective
        controller parameters.
Table 642: IL_TEMPCONTROL_CONTROL_TYPE enumeration type
Enumeration element            Number Description
CONTROL_TYPE_PI                1      Parameterization of a PI-controller using the controlled system
                                      parameters
CONTROL_TYPE_PID               2      Parameterization of a PID-controller using the controlled
                                      system parameters

### 21.9.4 IL_TEMPCONTROL_CONTROL_MODE

        The enumeration type IL_TEMPCONTROL_CONTROL_MODE selects the con‐
        trol loop response:

Either the open-loop control in the open control loop or the closed-loop con‐
trol optimize the command value response or the disturbance response in the
closed control loop
Table 643: IL_TEMPCONTROL_CONTROL_MODE enumeration type
Enumeration element Number              Description
CONTROL_TEMP‐       1                   The function block controls the actual controlled system value
MODE_MANUAL                             using the value specified at the "ManContrValue" input
CONTROL_TEMP‐       2                   The function block optimizes the command value response of
MODE_OPT_COMMAND                        the "Feedback" value to the "Setpoint" value
CONTROL_TEMP‐       3                   The function block optimizes the disturbance response of the
MODE_OPT_DISTURB‐                       "Feedback" value to the "Setpoint" value
ANCE
CONTROL_TEMP‐       4                   The function block optimizes the disturbance response of the
MODE_ONLY_DISTURB‐                      "Feedback" value to the "Setpoint" value.
ANCE                                    Fast and robust auto-tuning explicitly for interference reaction
                                        at the same time.
                                        (Default)

### 21.9.5 IL_TEMPCONTROL_EXTENDED_SETTINGS

 The    structure    IL_TEMPCONTROL_EXTENDED_SETTINGS            contains           the
 extended setting options of the auto-tuning.
 The default settings are sufficient for the common controlled systems.
Table 644: Structural description of the IL_TEMPCONTROL_EXTENDED_SETTINGS
Name               Type         Min. value Max. value Default    Applied         Description
                                                      value
IdentAc‐           LREAL        >0         N. def     3.0        Cyclic          Abort criterion of the
curacy                                                                           identification
Oblivion‐          LREAL        0.9        1.0         0.98      Cyclic          Oblivion factor for
Factor                                                                           changeable controlled
                                                                                 systems
MinDelay‐          LTIME        >LTIME#0s N. def
                                         LTIME#1 At a rising                     Minimum delay of the
Time                                     s       edge of "Star‐                  controlled system
                                                 tAutoTune"
ControlType ⮫ IL_TEMP‐ CON‐     CON‐     CON‐    Cyclic                          Controller type (PI- or
            CON‐       TROL_TYP TROL_TYP TROL_TY                                 PID-controller)
            TROL_CON E_PI       E_PID    PE_PI
            TROL_TYP
            E

Name           Type           Min. value Max. value Default      Applied           Description
                              value
bControl       LREAL          0          1.0        1.0          Cyclic            Scaling factor for P-
                                                             value
cControl       LREAL          0            1.0        1.0        Cyclic            Scaling factor for D-
                                                             value

### 21.9.6 IL_TEMPCONTROL_MODEL_PARAM

The structure IL_TEMPCONTROL_MODEL_PARAM contains the parameters KS
and TS of the controlled system.
Table 645: Structural description of the IL_TEMPCONTROL_MODEL_PARAM

Name       Type       Min.        Max.      Default    Applied                         Description
value       value     value
Ks         LREAL      N. def      N. def    0        At a rising edge at        Gain of the con‐
                               "Preset", "StartAutoTune" trolled system
                               or a change in the con‐
                               troller setting ("Damping‐
                               Factor", "ControlMode")
Ts         LTIME      LTIME#0 N. def        LTIME#0s Rising edge at "Preset“,   Compensation time
s                              "StartAutoTune“ or a       constant of the con‐
                               change in the controller trolled system
                               setting ("DampingFactor“,
                               "ControlMode“)

### 21.9.7 IL_TEMPCONTROL_CONTR_PARAM

The structure IL_TEMPCONTROL_CONTR_PARAM contains the current parame‐
ters KP , KI and KD of the controller as well as the dead time Tt
Table 646: Structural description of the IL_TEMPCONTROL_ CONTR_PARAM
Name       Type       Min. value Max. value Default         Applied                Description
                                            value
KP         LREAL      N. def     N. def     10000        At a rising edge at    Proportional gain of
                                                         "Preset" or "StartAu‐ the controller
                                                         toTune"
KI         LREAL      N. def       N. def        0       At a rising edge at    Integration constant of
                                                         "Preset"               the controller
KD         LREAL      N. def       N. def        0       At a rising edge at    Differentiation con‐
                                                         "Preset"               stant of the controller
Tt         LTIME      LTIME#0s     N. def        LTIME#0 At a rising edge at    Delay of the controlled
                                                 s       "Preset", "StartAuto‐ system
                                                         Tune" or a change in
                                                         the controller setting
                                                         ("DampingFactor",
                                                         "ControlMode")

### 21.9.8 IL_TEMPCONTROL_LIMITS

The structure IL_TEMPCONTROL_LIMITS contains the alarm limits in [u]
(units). Initial value is 0u (not active).
If values are assigned to the structure,
Limits.UpperAlarm > Limits.LowerAlarm
and
(Setpoint    +    Limits.UpperAtSetpoint)                   >=       (Setpoint       -
Limits.LowerAtSetpoint)

an error is generated.
Table 647: Structural description of the IL_TEMPCONTROL_LIMITS
Name               Type        Min. value Max. value Default   Applied        Description
                                                     value
UpperAlarm         LREAL       N. def     N. def     0         Cyclic         Upper actual value
                                                                              limit when an alarm is
                                                                              triggered (absolute)
LowerAlarm         LREAL       N. def         N. def   0       Cyclic         Lower actual value
                                                                              limit when the alarm is
                                                                              triggered (absolute)
UpperAtSet‐        LREAL       N. def         N. def   0       Cyclic         Upper actual limit for
point                                                                         SetpointReached (rela‐
                                                                              tive)
LowerAtSet‐        LREAL       N. def         N. def   0       Cyclic         Lower actual limit for
point                                                                         SetpointReached (rela‐
                                                                              tive)

## 21.10 Two-position controller

### 21.10.1 IL_TwoPosCtrlType01

Brief description
The function block IL_TwoPosCtrlType01 implements a two-position controller
with hysteresis and is suitable for simple closed-loop controls.

Interface description

Table 648: Interface variables of the IL_TwoPosCtrlType01 function block
I/O type       Name                    Data type      Description
VAR_INPUT      Enable                  BOOL           Processing enabled of the function block
                                                      (cyclic, state-controlled)
           InitValue                   BOOL           Specified value for the control variable y
           SetPoint                    LREAL          Reference variable w (command value)
           ActValue                    LREAL          Controlled variable x (actual value)
           HysteresisHi                LREAL          Upper response threshold of the hysteresis
           HysteresisLo                LREAL          Lower response threshold of the hysteresis
VAR_OUTPUT InOperation                 BOOL           Computation of the control variable y com‐

                               pleted without error. Output variable "Con‐
                               trolValue" valid
Error                   BOOL           Computation of the control variable "Con‐
                               trolValue" completed with error. Output
                               variable "ErrorIdent" valid
ErrorID                 ⮫ ERROR_CODE   If the "Error" output is set, it contains a
                               broad error classification
ErrorIdent              ⮫ ERROR_STRUCT Diagnostic description in case of error
                               ⮫ Troubleshooting on page 742
ControlValue            BOOL           Controller output value – control variable y
ActScanTime             LTIME          Controller cycle time [ms]

Specification
The properties of the function block IL_TwoPosCtrlType01 can be modified
using the following input variables:
"HysteresisHi":
● The input has to be preset with a positive value or zero. Zero switches off
   the positive hysteresis.
"HysteresisLo":
● The input has to be preset with a negative value or zero. Zero switches off
   the negative hysteresis.
When computing the control variable "ControlValue", FALSE is dominant.
Thus, with "HysteresisLo" == "HysteresisHi" == zero with a control difference
of zero ("SetPoint" == "ActualValue"), the output "ControlValue" is always
"FALSE".

Functional Description
After the function block has been enabled for processing, the function block
IL_TwoPosCtrlType01 uses "Enable" to preset the internal controller state in
the first controller cycle as well as the controller output to the preset value
given at the "InitValue" input and it cyclically computes the control variable
"ControlValue" in the following cycles.
If there are no errors during the function block processing, the validity of the
control variable is signaled by the "InOperation" output and the elements of
the output structures "ErrorID" and "ErrorIdent "are not updated.

If an error occurs during the function block processing, the error is signaled
by the "Error" output and specified by the elements of the output structures
"ErrorID" and "ErrorIdent" which are updated in this case. The outputs "Con‐
trolValue" and "ActScanTime" are not updated in case of an error.

Troubleshooting
The function block uses the error table CXA_TABLE, 16#0001.
It can generate the following error messages in Additional1 and Additional2:
Table 649: Error codes of the IL_TwoPosCtrlType01 function block
ErrorID                                  Additional1 Additional2 Description
INPUT_RANGE_ERROR                        16#0A0F0104 16#0C230085 The inputs "HysteresisHi" or
                                                                 "HysteresisLo" are invalid
STATE_MACHINE_ERROR                      16#0A0F0104 16#0C231000 Invalid state of the state
                                                                 machine
                                                                 xx indicates the invalid state

## 21.11 Utilities

### 21.11.1 IL_SUPPRESSION_LIMITS

IL_SUPPRESSION_LIMITS is an enumeration type and enables the suppression
window with the following allocation:
Table 650: Structure of the enumeration type IL_SUPPRESSION_LIMITS
Element                                  Description
IL_SUPPRESSION_OFF                       Suppression is disabled and all values return unchanged
                                         at the output.
IL_SUPPRESSION_LIMIT_1                   Suppression window #1 active ("SuppressionLimit1Low"
                                         and "SuppressionLimit1High")
IL_SUPPRESSION_LIMIT_2                   Suppression window #2 active ("SuppressionLimit2Low"
                                         and "SuppressionLimit2High")

Used in
● ⮫ Chapter 21.8.8 IL_SuppressionType03 on page 715
● ⮫ Chapter 21.8.9 IL_SuppressionType04 on page 721

### 21.11.2 IL_SUPPRESSION_MODE

IL_SUPPRESSION_MODE is an enumeration type and describes the function
of the inputs "SuppressionLimitLow*" and "SuppressionLimitHigh*" with the
following allocation:

Table 651: Structure of the enumeration type IL_SUPPRESSION_MODE
Element                                 Description
IL_SUPPRESSION_PERCENTAGE               Values are on a percentage rate to the averaged input
                                        value
IL_SUPPRESSION_ABSOLUTE_VALUE           Values are absolute values to the averaged input value
IL_SUPPRESSION_STATISTICAL              Value are statistical to the default deviation σ of the input
                                        value (e.g. 0.5 • σ, 1.0 • σ, 4.0 • σ,...)

Used in
●   ⮫ Chapter 21.8.6 IL_SuppressionType01 on page 706
●   ⮫ Chapter 21.8.7 IL_SuppressionType02 on page 711

●   ⮫ Chapter 21.8.8 IL_SuppressionType03 on page 715
●   ⮫ Chapter 21.8.9 IL_SuppressionType04 on page 721

### 21.11.3 IL_COORD_TYPE01

This data structure defines a two-dimensional coordinate with REAL values of
X and Y.

TYPE IL_COORD_TYPE01 :
STRUCT
  X: LREAL;     // X coord
  Y: LREAL;     // Y coord
END_STRUCT
END_TYPE

Used in
● ⮫ Chapter 21.5.4 IL_DeviationResponseCurve on page 628,
● ⮫ Chapter 21.4.6 IL_PIType01 on page 614,
● ⮫ Chapter 21.4.7 IL_PIType02 on page 618,
