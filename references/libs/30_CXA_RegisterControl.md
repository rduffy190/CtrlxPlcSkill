# 30 CXA_RegisterControl

## 30.1 Introduction and overview

Registration marks printed on a paper web or a paper sheet are detected
using a digital input and then read in by the register controller as a position
measuring value (position measurement). The position offset, velocity of the
drive or the master axis drive parameters are adjusted by the register con‐
troller function blocks.

a: Registration mark
b: Register touch probe sensor
c: Printing cylinders
d: Print φ

Measuring principle with web printing
The register controller controls the position of material in terms of the posi‐
tion of a reference axis. This can be the position of a sheet related to the
printing cylinder. The closed-loop control is conducted with the help of an
electrical input signal at the reference axis. The electrical input signal is pro‐
vided by the optical measurement of a registration mark on the material.

Function blocks of the CXA_RegisterControl library
Function block                           Description
⮫ MB_SetpointLockType01                  Component function block
⮫ MB_RegiMeasuringType01                 Component function block
⮫ MB_RegiMeasuringType02                 Component function block
⮫ MB_RegiRegulateType01                  Component function block
⮫ MB_RegiRegulateType02                  Component function block
⮫ MB_RegisterControllerType01 Main function block
⮫ MB_RegisterControllerSideTy Main function block

pe01

## 30.2 Data types

### 30.2.1 MB_CORRECTION_DATA (STRUCT)

Brief description
The data structure MB_CORRECTION_DATA describes the properties of the
correction window.

Table 807: MB_CORRECTION_DATA data structure
Name          Type                     Min.    Max.      Default    Effective       Description
                                       value   value     value
Correction‐   MB_CORRECTION_MODE       0       4         0          Continuous      Properties of the correction
Mode                                                                                window
Correction‐   LREAL                    0.0     n. def.   0.0        Continuous      Start of correction window
Start
CorrectionEnd LREAL                    0.0     n. def.   0.0        Continuous      End of correction window

### 30.2.2 MB_CORRECTION_MODE (ENUM)

Brief description
The enumeration type MB_CORRECTION_MODE contains possible variants of
the correction window for the function blocks ⮫ MB_RegiRegulateType01 and
⮫ MB_RegiRegulateType02.

Table 808: Data type MB_CORRECTION_MODE
Name                      Value   Description
CORR_WIN_DISA‐              0     Correction window is disabled
BLED
CORR_ABS                      1   Absolute correction window [CorrectionStart .. CorrectionEnd]
CORR_REL                      2   Relative correction window
                                  [Start = "RecordedPosition" + "CorrectionStart" ...
                                  End = "RecordedPosition" + "CorrectionEnd"]
CORR_REL_ABS                  3   Relative start correction window... absolute end correction
                                  window
                                  [Start = "RecordedPosition" + "CorrectionStart" ...
                                  End = "CorrectionEnd"]
CORR_ABS_REL                  4   Absolute start correction window... relative end correction
                                  window
                                  [Start = "CorrectionStart" .. End = "RecordedPosition" + "Correc‐
                                  tionEnd"]

### 30.2.3 MB_CORRECTION_TYPE (ENUM)

Brief description
The enumeration type MB_CORRECTION_TYPE contains possible variants of
the correction type. Only CORR_POSITION is currently available.

Table 809: MB_CORRECTION_MODE enumeration type
Name                     Value       Description
CORR_POSITION              0         Correction mode: Additive position for use in ProcessCtrl.offset

### 30.2.4 MB_PICONTROL_DATA (STRUCT)

Brief description
The data structure MB_PICONTROL_DATA describes the properties of the PI
controller.

Table 810: MB_PICONTROL_DATA data structure
Name          Type           Min.        Max.      Default    Effective     Description
                             value       value     value
PControl      LREAL          0           4         1.0        Continuous    Proportional value for the
                                                                            gaining value of the con‐
                                                                            troller
IControl      LREAL          0.0         n. def.   0.0        Continuous    Integration time Tn for the
                                                                            integration value of the
                                                                            controller
FeedbackT‐ LREAL             0.0         n. def.   0.0        Continuous    PT1 element filter time
Control                                                                     constant smoothing the
                                                                            actual value input "Feed‐
                                                                            back"
Response‐ ARRAY [0..3]                                        Continuous    Command value curve
Curve     OF                                                                to analyze the difference
          IL_COORD_T                                                        between the smoothed
          YPE01                                                             "Feedback" actual value
                                                                            and the "Setpoint" value
HighLimit     LREAL          >Low‐                 10000000 Continuous      Upper limit of "Control‐
                             Limit                 00.0                     Value"
                                                                            If "ControlValue" exceeds
                                                                            this value, it is limited to
                                                                            this value.
LowLimit      LREAL                      <High‐    -10000000 Continuous     Lower limit of "Control‐
                                         Limit     00.0                     Value"
                                                                            If "ControlValue” falls
                                                                            below this value, it is lim‐
                                                                            ited to this value.

## 30.3 Function blocks

### 30.3.1 MB_RegiSetpointLockType01

Brief description
The MB_RegiSetpointLockType01 function block is used to lock a value for a
register controller.

      Interface description

Table 811: Interface variables of the MB_RegiSetpointLockType01 function block
I/O type       Name                 Data type            Description
VAR_INPUT      Execute              BOOL                 The register setpoint lock function block
                                                         becomes active at a rising edge
               RecordedPosition     LREAL                The applied position is copied to the "Set‐
                                                         point" input when "SetpointLock" changes
               SetPointLock         UDINT                The value has to increase if the value is
                                                         applied to "RecordedPosition". If 2^32-1,
                                                         the value becomes 0 (value of modulo
                                                         type). Typically, an "actStep" output of a
                                                         technology function block is used as input
VAR_OUTPUT Active                   BOOL                 Function block is active
           Done                     BOOL                 Function block is completed
           Error                    BOOL                 Processing completed with error
           ErrorID                  ⮫ ERROR_CODE         Diagnostic description in case of error
               ErrorIdent           ⮫ ERROR_STRUCT Detailed diagnostics
VAR_IN_OUT     SetPoint             LREAL          Setpoint

Table 812: Min./max. and default values of the inputs of the MB_RegiSetpointLockType01 function
block
Name          Type              Min. value      Max. value        Default value   Effective
Execute       BOOL                                                FALSE           Continuous
RecordedPosi‐ LREAL                                               0.0             Change at "Set‐
tion                                                                              pointLock"
SetpointLock UDINT              0               2^32-1            0               Continuous. Initial‐
                                                                                  ized at a rising
                                                                                  edge of "Execute"

      Functional description
      The function block sets "Setpoint" to the next value at the "RecordedPosi‐
      tion" input. The next occurrence is detected when the "SetpointLock" input
      changes. This can be used for example to set a new command value for a
      register controller.

### 30.3.2 MB_RegiMeasuringType01

      Brief description
      The MB_RegiMeasuringType01 function block processes the measured touch
      probe signal.

       Interface description

Table 813: Interface variables of the MB_RegiMeasuringType01 function block
I/O type           Name                 Data type            Description
VAR_INPUT          Enable               BOOL                 Enables the function block when set to
                                                             TRUE
                   Pause                BOOL                 The "Pause" input is only analyzed when
                                                             the "Enable" input is active
                   Step                 UDINT                New values are calculated when the "Step"
                                                             input changes
           Setpoint                     LREAL                Command value
           Feedback                     LREAL                Measured value
           ModuloValue                  LREAL                Modulo value of the measured axis
VAR_OUTPUT InOperation                  BOOL                 Measuring function block is operating
           Error                        BOOL                 Processing completed with error
           ErrorID                      ⮫ ERROR_CODE         Diagnostic description in case of error
                   ErrorIdent           ⮫ ERROR_STRUCT Detailed diagnostics
                   InPause              BOOL           "Pause" is active; the "Deviation" output
                                                       maintains its value
                   ActStep              UDINT          Step value, incrementing with every new
                                                       value on the output "Deviation"
                   Deviation            LREAL          "Setpoint" - "Feedback"

Table 814: Min./max. and default values of the inputs of the MB_RegiMeasuringType01 function
block
Name                Type            Min. value      Max. value      Default value   Effective
Enable              BOOL                                            FALSE           Continuous
Pause               BOOL                                            FALSE           Continuous
Step                UDINT           0               2^32-1          0               Continuous, starts
                                                                                    at a rising edge
                                                                                    at "Enable" and at
                                                                                    a falling edge at
                                                                                    "Pause"
Setpoint            LREAL           0               ModuloValue     0.0             Change of "Step"
Feedback            LREAL           0               ModuloValue     0.0             Change of "Step"

       Functional description
       The MB_RegiMeasuringType01 function block subtracts the "Setpoint" and
       "Feedback" inputs from each other ("Setpoint" - "Feedback"). The result of
       the subtraction is the value of the "Deviation" output.
       Pause
       The "Pause" input is only analyzed when the "Enable" input is active. The
       "ActStep" output is updated even if the "Pause" input is active. While "Pause"
       is active, the "InPause" output is TRUE and the "Deviation" output maintains
       its value.
       Normal mode

       The RegiRegulateType02 function block only calculates a new value if the
       "Step" input changes. The controlled and the measured axis have to be
       modulo axes.

### 30.3.3 MB_RegiMeasuringType02

       Brief description
       The MB_RegiMeasuringType02 function block processes the measured touch
       probe signal.

       Interface description

Table 815: Interface variables of the MB_RegiMeasuringType02 function block
I/O type       Name                 Data type           Description
VAR_INPUT      Enable               BOOL                Enables the function block when set to
                                                        TRUE
               Pause                BOOL                The "Pause" input is only analyzed when
                                                        the "Enable" input is active
               Preset               BOOL                The "Preset" input is only analyzed when
                                                        "Enable" is TRUE. A positive edge of this
                                                        input forces the shift register memory to
                                                        "0"
               Step                 UDINT               New values are calculated when the "Step"
                                                        input changes
               Setpoint             LREAL               Command value
               Feedback             LREAL               Measured value
               ModuloValue          LREAL               Modulo value of the measured axis
               ProbeDistance        UDINT               The distance between the mark sensor and
                                                        the measuring axis in master axis revolu‐
                                                        tions (format lengths)

I/O type           Name                 Data type            Description
MissedMarksCnt       UDINT                Counter for marker failures if an expecta‐
                                          tion window is used
MarkGating                   UDINT                Every nth mark is used for registration
VAR_OUTPUT InOperation                  BOOL                 Measuring function block is operating
Error                        BOOL                 Processing completed with error
ErrorID                      ⮫ ERROR_CODE         Diagnostic description in case of error
ErrorIdent           ⮫ ERROR_STRUCT Detailed diagnostics
InPause              BOOL           "Pause" is active; the "Deviation" output
                                    maintains its value
PresetAck            BOOL           "Preset" function is completed
ActStep              UDINT          Step value, incrementing with every new
                                    value on the output "Deviation"
Deviation            LREAL          "Setpoint" - "Feedback" delayed if shift reg‐
                                    ister is active

Table 816: Min./max. and default values of the inputs of the MB_RegiMeasuringType02 function
block
Name               Type             Min. value      Max. value        Default value   Effective
Enable             BOOL                                               FALSE           Continuous
Pause              BOOL                                               FALSE           Continuous
Preset             BOOL                                               FALSE           "Enable" TRUE
                                                                                      (continuous)
Step               UDINT            0               2^32-1            0               Continuous, starts
                                                                                      at a rising edge
                                                                                      at "Enable" and at
                                                                                      a falling edge at
                                                                                      "Pause"
Setpoint           LREAL            0               ModuloValue       0.0             Change of "Step"
Feedback           LREAL            0               ModuloValue       0.0             Continuous
ModuloValue        LREAL            0               n. def.           0.0             Rising edge at
                                                                                      "Enable"
ProbeDistance UDINT                 0               60                0               Continuous
Missed‐       UDINT                 0               2^32-1            0               Continuous
MarksCnt
MarkGating    UDINT                 0               2^32-1            1               Rising edge at
                                                                                      "Enable", "0" dis‐
                                                                                      ables MarkGating
                                                                                      (identical to "1")

     Functional description
     The MB_RegiMeasuringType02 function block subtracts the "Setpoint" and
     "Feedback" inputs from each other ("Setpoint" - "Feedback"). The result of
     the subtraction is the value of the "Deviation" output when the shift register
     is disabled. When the shift register is enabled, it is delayed by the number of
     "ProbeDistance". Only every nth mark is intended for the registration with the
     MarkGating function of the function block.
     Pause

The "Pause" input is only analyzed when the "Enable" input is active. The
"ActStep" output is updated even if the "Pause" input is active. While "Pause"
is active, the "InPause" output is TRUE and the "Deviation" output maintains
its value.
Preset
The "Preset" input can be written in advance to the shift register. To write on
the shift register memory in advance, "Enable" has to be active. A zero value is
written to the memory at the rising edge of the "Preset" input when "Enable"
is active. If successful, the "PresetAck" output is set to TRUE.
ProbeDistance
The "ProbeDistance" input is the distance between the mark sensor and the

measuring (= controlled) axis in master axis revolutions (format lengths). The
maximum format length is 60. If "ProbeDistance" is 0, the shift register is
disabled. The "Deviation" output is set to "Setpoint" – "Feedback".
If "ProbeDistance" is unequal to 0, the shift register is enabled. This means
that the values at the "Deviation" output are delayed by the number of master
axis revolutions (format lengths) at the "ProbeDistance" input.

MissedMarkCnt
This is the marker failure monitoring counter of the touch probe function
when the expectation window is active. If a mark is missing, zero is written
to the shift register if it is enabled. In case of a disabled shift register, zero is
written to the "Deviation" output.
MarkGating
This function allows the user to control the registration only every nth mark
by gating invalid marks. This can be used for example if the marks on the web
were printed with a printing plate where the printed image is shown several
times. In this case, the mark distances between subsequent marks is not
constant. However, the mark distances between every nth consecutive mark
are constant. The RegiMeasuring function block only uses every nth mark for
the register control.

                 Valid marks                                  Controlled
                 Hidden (invalid marks)                         axis

                                                               ü = 1:1
                N master axis revolutions                       el

### 30.3.4 MB_RegiRegulateType01

     Brief description
     The MB_RegiRegulateType01 function block is used to calculate a control vari‐
     able.

     Interface description

Table 817: Interface variables of the MB_RegiRegulateType01 function block
I/O type           Name               Data type          Description
VAR_INPUT          Enable             BOOL               The register setpoint lock function block
                                                         becomes active at a rising edge
                   Pause              BOOL               The "Pause" input is only analyzed when
                                                         the "Enable" input is active
                   Preset             BOOL               The "Preset" input is only analyzed when
                                                         "Enable" is TRUE. A positive edge of this
                                                         input forces "ParameterControlValue" to
                                                         "PresetValue"
                   Step               UDINT              Processing step
                   PresetValue        LREAL              Value applied to the "ParameterControl‐
                                                         Value" output at a rising edge of the
                                                         "Preset" input
                   ControlPolarity    BOOL               The polarity of the control value is inverted
                                                         when this input is TRUE
                   ControlValue       LREAL              Calculated control value from IL_PIType02
                                                         for example
                   ControlType        MB_CORREC‐         Enum of the correction type, supports only
                                      TION_TYPE          position
           ModuloValue                LREAL              Modulo value of the measured axis
VAR_OUTPUT InOperation                BOOL               Function block is operating
           Error                      BOOL               Processing completed with error
           ErrorID                    ⮫ ERROR_CODE       Diagnostic description in case of error
                   ErrorIdent         ⮫ ERROR_STRUCT Detailed diagnostics
                   InPause            BOOL           "Pause" is active; the "ParameterControl‐
                                                     Value" output maintains its value
                   PresetAck          BOOL           "Preset" is completed, the "Preset" value
                                                     is copied to the "ParameterControlValue"
                                                     output
                   ActStep            UDINT          Step value, incrementing with every new
                                                     value at the output "ParameterControl‐
                                                     Value"

I/O type       Name              Data type                 Description
ParameterControl‐ LREAL                     The register controller function block calcu‐
Value                                       lates a value based on the selected param‐
                                      eter in the input "ControlType" and stores
                                      the result in the output "ParameterControl‐
                                      Value"
VAR_IN_OUT     ControlledAxis       ⮫ AXIS_REF             Reference to the controlled axis

Table 818: Min./max. and default values of the inputs of the MB_RegiRegulateType01 function
block
Name            Type            Min. value       Max. value         Default value    Effective

Enable          BOOL                                                FALSE            Continuous
Pause           BOOL                                                FALSE            Continuous
Preset          BOOL                                                FALSE            Continuous
Step            UDINT           0                2^32-1             0                Continuous, starts
                                                                at a rising edge
                                                                at "Enable" and at
                                                                a falling edge at
                                                                "Pause"
PresetValue     LREAL           n. def.          n. def.            0.0              Rising edge at
                                                                "Preset"
ControlPolarity BOOL                                                FALSE            Continuous
ControlType     MB_CORREC‐      n. def.          n. def.            0                Rising edge at
TION_TYPE                                                            "Enable"
ControlValue LREAL              n. def.          n. def.            0.0              Continuous
ModuloValue LREAL               0.0              n. def.            0.0              Rising edge at
                                                                "Enable"

Functional description
The function block writes control values to a parameter in an axis. Depending
on the target parameter "ControlledType", the function block includes an
integration of the "ParameterControlValue" input. Only the position mode is
supported.

Pause
The "Pause" input is only analyzed when the "Enable" input is active. The "Act‐
Step" output is updated even if the "Pause" input is active. While "Pause" is
active, the "InPause" output is TRUE and the "ParameterControlValue" output
maintains its value.

Preset
The "PresetAck" output is active when the value at "PresetValue" is taken into
account. The "Preset" input has a higher priority than the "Pause" input. The
value of "PresetValue" is taken into account at a rising edge of "Preset" when
the "Enable" input is active. If successful, the "PresetAck" output is set to
TRUE and the value of "PresetValue" is written to the controlled parameter.

Normal mode
The RegiRegulateType02 function block only calculates a new value if the
"Step" input changes. The controlled and the measured axis have to be
modulo axes.

### 30.3.5 MB_RegiRegulateType02

       Brief description
       The MB_RegiRegulateType02 function block is used to calculate a control vari‐
       able. If the correction window is active, the control deviations are corrected in
       one parameterized correction window.

       Interface description

Table 819: Interface variables of the MB_RegiRegulateType02 function block
I/O type           Name                  Data type           Description
VAR_INPUT          Enable                BOOL                The register setpoint lock function block
                                                             becomes active at a rising edge
                   Pause                 BOOL                The "Pause" input is only analyzed when
                                                             the "Enable" input is active
                   Preset                BOOL                The "Preset" input is only analyzed when
                                                             "Enable" is TRUE. A positive edge of this
                                                             input forces "ParameterControlValue" to
                                                             "PresetValue"
                   Step                  UDINT               The approached position is copied to
                                                             the "Setpoint" input when "SetpointLock"
                                                             changes
                   PresetValue           LREAL               Value applied to the "ParameterControl‐
                                                             Value" output at a rising edge of the
                                                             "Preset" input
                   ControlPolarity       BOOL                The polarity of the control value is inverted
                                                             when this input is TRUE
                   ControlValue          LREAL               Calculated control value from IL_PIType02
                                                             for example
                   ControlType           MB_CORREC‐          Enum of the correction type, supports only
                                         TION_TYPE           position
                   CorrectionData        MB_CORREC‐          Properties of the correction window
                                         TION_DATA
           RecordedPosition              LREAL               Measured value
           ModuloValue                   LREAL               Modulo value of the measured axis
VAR_OUTPUT InOperation                   BOOL                Function block is operating
           Error                         BOOL                Processing completed with error
           ErrorID                       ⮫ ERROR_CODE        Diagnostic description in case of error
                   ErrorIdent            ⮫ ERROR_STRUCT Detailed diagnostics

I/O type       Name                 Data type              Description
InPause              BOOL                   "Pause" is active; the "ParameterControl‐
                                            Value" output maintains its value
PresetAck            BOOL                   "Preset" is completed, the "Preset" value
                                            is copied to the "ParameterControlValue"
                                            output
ActStep              UDINT                  Step value, incrementing with every new
                                            value at the output "ParameterControl‐
                                            Value"
ParameterControl‐ LREAL                     The register controller function block calcu‐

Value                                       lates a value based on the selected param‐
                                            eter in the input "ControlType" and stores
                                            the result in the output "ParameterControl‐
                                            Value".
VAR_IN_OUT     MeasuredAxis         ⮫ AXIS_REF             Reference to the measured axis

Table 820: Min./max. and default values of the inputs of the MB_RegiRegulateType02 function
block
Name            Type            Min. value       Max. value         Default value    Effective
Enable          BOOL                                                FALSE            Continuous
Pause           BOOL                                                FALSE            Continuous
Preset          BOOL                                                FALSE            Continuous
Step            UDINT           0                2^32-1             0                Continuous, starts
                                                                                     at a rising edge
                                                                                     at "Enable" and at
                                                                                     a falling edge at
                                                                                     "Pause"
PresetValue     LREAL           n. def.          n. def.            0.0              Rising edge at
                                                                                     "Preset"
ControlPolarity BOOL                                                FALSE            Continuous
ControlType     MB_CORREC‐                                          0                Rising edge at
                TION_TYPE                                                            "Enable"
ControlValue LREAL              n. def.          n. def.            0.0              Continuous
CorrectionData MB_CORREC‐                                                            Continuous
                TION_DATA
RecordedPosi‐ LREAL             0.0              ModuloValue        0.0              Changing the
tion                                                                                 "Step" input
ModuloValue LREAL               0.0              n. def.            0.0              Rising edge at
                                                                                     "Enable"

      Functional description
      The function block writes control variables to a parameter in an axis.
      Depending on the target parameter, "ControlType", the function block
      includes an integration of the "ParameterControlValue" input. Only the posi‐
      tion mode is supported.
      Pause
      The "Pause" input is only analyzed when the "Enable" input is active. The "Act‐
      Step" output is updated even if the "Pause" input is active. While "Pause" is
      active, the "InPause" output is TRUE and the "ParameterControlValue" output
      maintains its value.
      Preset

The "PresetAck" output is active when the value at "PresetValue" is taken into
account. The "Preset" input has a higher priority than the "Pause" input. The
value of "PresetValue" is taken into account at a rising edge of "Preset" when
the "Enable" input is active. If successful, the "PresetAck" output is set to
TRUE and the value of "PresetValue" is written to the controlled parameter.
Correction window
The correction window is an angular range relating to the measuring axis.
The register controller controls the control deviations within this window. The
position and size of the correction window are set using the following inputs:
The "CorrectionMode" input sets the correction window either absolute or
relative. If "CorrectionMode" is set to CORR_WIN_DISABLED, the correction
window is inactive.
The "CorrectionStart" input defines the start of the correction window.
The "CorrectionEnd" input defines the end of the correction window.
The correction window supports only a positive modulo range (e.g., 0...+360
degrees) of the measuring axis.

                                                 d

              b                                                   a

                                          c

a: Start correction window
b: End correction window
c: Correction window
d: Expectation window

                                                  a

                                                      d

                                                          c

                                                      b

a: Start correction window = measuring end
b: Relative end of correction window to measuring end
c: Correction window
d: Expectation window

                                                               a

                                                      d

            b

                                     c

a: Start correction window = measuring end
b: End of correction window = perm. angle
c: Correction window
d: Expectation window
Normal mode

The MB_RegiRegulateType02 function block only calculates a new value if the
"Step" input changes. The controlled axis and the measured axis have to be
modulo axes.

### 30.3.6 MB_RegisterControllerType01

Brief description
The register controller function block MB_RegisterControllerType01 supports
the following functionality:
● Calculation of a correction value based on the measured value and the
  command value using a P- or PI-control loop
● Preset function
● Pause function
● Min./max. limitation of the calculated control value
● Correction window function
● Shift register
● Dead band Kp characteristic curve
● PT1 element
● Apply command value (Lock setpoint on demand)
● Mark gating function

Interface description

Table 821: Interface variables of the MB_RegisterControllerType01 function block
I/O type           Name                 Data type          Description
VAR_INPUT          Enable               BOOL               The register setpoint lock function block
                                                           becomes active at a rising edge
                   Pause                BOOL               The "Pause" input is only analyzed when
                                                           the "Enable" input is active. The "Control‐
                                                           Value" and "ParameterControlValue" out‐
                                                           puts are constant when "Pause" is active
                   Preset               BOOL               The "Preset" input is only analyzed when
                                                           "Enable" is TRUE. A positive edge of this
                                                           input forces the control loop to "Preset‐
                                                           Value". In addition, the "Preset" input sets
                                                           the "ParameterControlValue" value to the
                                                           "PresetValue" value
                   Step                 UDINT              Processing step

I/O type       Name               Data type         Description
PresetValue        LREAL             Value applied to the outputs "ControlValue"
                                     and "ParameterControlValue" at a rising
                                     edge of the "Preset" input
SetpointLock       BOOL              Enables command value application (set‐
                                     point lock). If TRUE, the next measured
                                     mark is latched
ClearMeasValMem BOOL                 Clear the memory for the measured values
                                     used by the "Touch probe distance" func‐
                                     tion

ControlPolarity    BOOL              The polarity of the control value is inverted
                                     when this input is TRUE
ControlType        ⮫ MB_CORREC‐      Structure of the correction type
                   TION_TYPE
PIControlData      ⮫ MB_PICON‐       Structure of the PI-controller
                   TROL_DATA
CorrectionData     ⮫ MB_CORREC‐      Structure of the correction window
                   TION_DATA
ModuloValue        LREAL             Modulo value of the measured axis
RecordedPosition   LREAL             Position where edge occurred
ProbeDistance      UDINT             The distance between the mark sensor and
                                     controlled axis in format lengths (master
                                     axis revolutions, formats)
MissedMarksCnt     UDINT             Missed mark counter when using an expect‐
                                     ation window
MarkGating             UDINT             Every nth mark is used for the register
VAR_OUTPUT InOperation            BOOL              Register controller is operating
Error                  BOOL              Processing completed with error
ErrorID                ⮫ ERROR_CODE      Diagnostic description in case of error
ErrorIdent         ⮫ ERROR_STRUCT Detailed diagnostics
InPause            BOOL           "Pause" is active. The "ControlValue" and
                                  "ParameterControlValue" outputs maintain
                                  their values
PresetAck          BOOL           "Preset" is completed. The "Preset" value is
                                  copied to the "ControlValue" and "Parame‐
                                  terControlValue" outputs
ActStep            UDINT          Step value, incrementing with every new
                                  value at the "ControlValue" output
SetpointLockAck    BOOL           "Setpoint" applied. Current value in
                                  "RecordedPosition" is copied to "Setpoint"
ClearMeasValMe‐    BOOL           Clearing the memory of the measured
mAck                              values completed
HighLimitActive    BOOL           Upper limit is active. "ControlValue" would
                                  be higher, but is limited to "HighLimit"
LowLimitActive     BOOL           Lower limit is active. "ControlValue" would
                                  be lower, but is limited to "LowLimit"
ControlValue       LREAL          Control value calculated by the register
                                  controller

I/O type           Name                Data type              Description
CurrentValue        LREAL                  Current value used in the register con‐
                                           troller. It is equal to the input "RecordedPo‐
                                           sition" if "ProbeDistance" and "MarkGating"
                                           are disabled
Deviation           LREAL                  "Deviation" = ("Setpoint" - "CurrentValue")
                                           of the register controller
ParameterControl‐ LREAL                    The register controller calculates a value
Value                                      based on the selected parameter in the
                                           "ControlType" input and stores the result in
                                           the "ParameterControlValue" output
VAR_IN_OUT         Setpoint            LREAL                  Command value
MeasuredAxis        ⮫ AXIS_REF             Reference to the measured axis

Table 822: Min./max. and default values of the inputs of the MB_RegisterControllerType01
function block
Name               Type            Min. value       Max. value         Default value   Effective
Enable             BOOL                                                FALSE           Continuous
Pause              BOOL                                                FALSE           Continuous
Preset             BOOL                                                FALSE           "Enable" TRUE
                                                                                       (continuous)
Step               UDINT           0                2^32 - 1           0               Continuous. Starts
                                                                                       at a rising edge
                                                                                       at "Enable" and at
                                                                                       a falling edge at
                                                                                       "Pause"
SetpointLock       BOOL                                                FALSE           Continuous
ClearMeas‐         BOOL                                                FALSE           Continuous
ValMem
PresetValue        LREAL           n. def.          n. def.            0.0             Rising edge at
                                                                                       "Preset"
ControlPolarity BOOL                                                   FALSE           Continuous
ControlType     MB_CORREC‐                                                             Rising edge at
                TION_TYPE                                                              "Enable"
Setpoint        LREAL              n. def.          n. def.            0.0             Change of "Step"
ModuloValue LREAL                  0.0              n. def.            0.0             Rising edge at
                                                                                       "Enable"
CorrectionData MB_CORREC‐                                              CORR_DIS‐       Continuous
               TION_DATA                                               ABLE
RecordedPosi‐ LREAL                n. def.          n. def.            0.0             Change of "Step"
tion
ProbeDistance UDINT                0                30                 0               Continuous
Missed‐        UDINT               0                2^32 -1            0               Continuous. Initial‐
MarksCnt                                                                               ization at a rising
                                                                                       edge at "Enable"
                                                                                       and at falling edge
                                                                                       at "Pause"
MarkGating         UDINT           0                2^32 -1            1               Rising edge at
                                                                                       "Enable". "0" disa‐
                                                                                       bles mark gating
                                                                                       (identical to "1")

Functional description
A sensor detects marks, perforations, cuts or pasted joints on the material and
provides a (binary) signal to the control.
The register controller calculates the control deviation between the measured
and command value positions and determines the required correction value
once a new edge of the sensor signal is detected.
Changes in the correction value become active via the trapezoidal profile,
velocity ramp, PT1-filter or instantaneously depending on the selected control
parameter ("ControlType") input of the function block.
Initialization

During the initialization, the inputs "Setpoint" and "RecordedPosition" have to
contain valid data.
PresetValue
For a trouble-free start of the controller outputs "ControlValue" and "Parame‐
terControlValue", set the "Preset" input before activating the "Enable" input.
During this period, the "Setpoint" and "RecordedPosition" inputs have to have
valid data. In addition, the upper limits and lower limits are monitored to
ensure a limitation of the "ControlValue" output if the current value for "Pre‐
setValue" is beyond the valid range of "PIControlData.HighLimit" or "PICon‐
trolData.LowLimit".
The "PresetAck" output is active when the value at the "PresetValue" input
is copied to the outputs "ControlValue" and "ParameterControlValue". The
"Preset" input has a higher priority than the "Pause" input. The value in "Pre‐
setValue" is copied to the respective outputs at a rising edge at the "Preset"
input if "Enable" is active. If successful, the "PresetAck" output is set to TRUE.
Pause
The "Pause" input is only analyzed when the "Enable" input is active. In this
case, the deviation ("Setpoint" – "RecordedPosition") is set to 0. Therefore,
the outputs "ControlValue" and "ParameterControlValue" do not change any‐
more. This can be used to maintain the values of the outputs "ControlValue"
and "ParameterControlValue". The "ActStep" output is refreshed even if the
"Pause" input is active. As long as the "Pause" input is active, the "InPause"
output is TRUE.
Command value application Setpoint lock
A mode change from Manual to Automatic is achieved by engaging at the next
detected register marks. For example, if a new paper web is brought into
position and the register mark is detected, the "SetpointLock" input is set to
TRUE. The value in "Setpoint" is overwritten with the value in "RecordedPosi‐
tion" as soon as the "Step" input is changed.
Correction window
The correction window is an angular range relating to the measuring axis.
The register controller controls the control deviations within this window. The
position and size of the correction window are set using the following inputs:
The "CorrectionMode" input sets the correction window either absolute or
relative. If "CorrectionMode" is set to CORR_WIN_DISABLED, the correction
window is inactive.
The "CorrectionStart" input defines the start of the correction window.
The "CorrectionEnd" input defines the end of the correction window.
The correction window supports only a positive modulo range (e.g., 0...+360
degrees) of the measuring axis.

                                               d

              b                                                a

                                        c

a: Start correction window
b: End correction window
c: Correction window
d: Expectation window

                                                   a

                                                       d

                                                           c

                                                       b

a: Start correction window = measuring end
b: Relative end of correction window to measuring end
c: Correction window
d: Expectation window

                                                                  a

                                                        d

             b

                                      c

a: Start correction window = measuring end
b: End of correction window = perm. angle
c: Correction window
d: Expectation window
Smoothing
The "TControl" input is the attenuation constant for the "RecordedPosition"
input. If set to 0, smoothing is inactive.
ProbeDistance
In the simplest case, the measuring axis is a format cylinder and the distance
of the sensor to the measuring axis is less than the format length. Meas‐
urement and correction relate to the same product. It is often required to
mount the mark reader (sensor) further away from the measuring axis, e.g.,
hazardous areas in printing facilities. If the distance is greater than the format
length, the measured register error cannot be corrected until the product has
reached the format cylinder. The correction has to be delayed by as many
formats as there are formats between the controlled axis and the sensor. The
"ProbeDistance" input is the distance between the mark reader (sensor) and
the controlled axis in format lengths (master axis revolutions, formats). If set
to 0, the distance of the sensor to the measuring axis is less than the format
length.

Clearing the internal memory of measured values
The "Touch probe distance" function contains an internal memory that stores
measured values (like a shift register). This internal memory can be cleared
(set to "0") using the "ClearMeasValMem" input.
ResponseCurve
Using the "ResponseCurve" input, the control deviation can be scaled. Use
this functionality to specify a smaller scaling of the control deviation for
smaller control deviations. This results in a lower proportional gain and thus
causes a smoother control behavior in a steady state.
When parameterizing the input, the controller parameters should first be
set without evaluation. Subsequently, a lower scaling should be specified.
This allows to globally set the controller parameters first using the system
dynamics, and then, a local optimization is ensured (e.g. for the steady state).
The local optimization is parameterized with a characteristic curve with up
to four data points. Negative deviations are processed by point reflection of
the curve at the origin. This results in a total of nine linear sections. The
section s5 passes the origin. The sections s1 and s9 have a slope of 1 and
each run into positive or negative infinity. If the input is not assigned, a 1-to-1
characteristic curve is used as default value. That means that it is not scaled.

Points P1 to P4 are stored in an array of IL_COORD_TYPE01. If less than four
points are required, the x-coordinates of the points not required (beginning
with the last point) are set to 0. The x-values have to be positive and increase
in positive direction. The same point can be stored twice.
MarkGating
This function allows the user to control the registration only every nth mark
by gating invalid marks. This can be used for example if the marks on the web
were printed with a printing plate where the printed image is shown several

times. In this case, the mark distances between subsequent marks is not
constant. However, the mark distances between every nth consecutive mark
are constant. The RegiMeasuring function block only uses every nth mark for
the register control.

                Valid marks                                Controlled
                Hidden (invalid marks)                       axis

                                                           ü = 1:1

               N master axis revolutions                     el

Normal mode
The RegisterController only calculates a new value if the "Step" input changes.
The "PControl" and "IControl" controller parameters can be changed perma‐
nently.
If the value in the "ControlValue" output exceeds or falls below the values of
the outputs "HighLimit" or "LowLimit", "ControlValue" is limited to one of the
following limit values.
● If the value in "ControlValue" is positive, the value in "HighLimit" is used.
● If the value in "ControlValue" is negative, the value in "LowLimit" is used.
If the register controller has an integral action time, an anti-reset wind-up is
carried out and the integral action is no longer summed up. In this case, the
"HighLimitActive" and "LowLimitActive" outputs are set to TRUE.

### 30.3.7 MB_RegisterControllerSideType01

Brief description
The register controller function block MB_RegisterControllerSideType01 sup‐
ports the following functionality:

● Calculation of a correction value based on the measured values and the
  command values using a P- or PI-control loop
● Preset function
● Pause function
● Min./max. limitation of the calculated control value
● Command value application (setpoint lock) function
● Dead band KP characteristic curve
● PT1 element

     Interface description

Table 823: Interface variables of the MB_RegisterControllerSideType01 function block
I/O type           Name               Data type        Description
VAR_INPUT          Enable             BOOL             The register setpoint lock function block
                                                       becomes active at a rising edge
                   Pause              BOOL             The "Pause" input is only analyzed when
                                                       the "Enable" input is active. The "Control‐
                                                       Value" and "CommandPosition" outputs are
                                                       constant while "Pause" is active
                   Preset             BOOL             The "Preset" input is only analyzed when
                                                       "Enable" is TRUE. A positive edge of this
                                                       input forces the control loop to "Preset‐
                                                       Value"
                   Step               UDINT            Processing step
                   PresetValue        LREAL            Value applied to the "ControlValue" output
                                                       at the rising edge at the "Preset" input
                   SetpointLock       BOOL             Enables command value application (set‐
                                                       point lock). If TRUE, the next measured
                                                       mark is latched
                   ControlPolarity    BOOL             The polarity of the control value is inverted
                                                       when this input is TRUE
                   RecordedPosition‐ LREAL             Width of the measured mark
                   Width
                   PIControlData     MB_PICON‐         Structure of the PI-controller
                                     TROL_DATA
                   ControlType       MB_CORREC‐        Structure of the correction type
                                     TION_TYPE
                   TriangleTangent   LREAL             Value of tan α = (opposite leg length/adja‐
                                                       cent leg length )
VAR_OUTPUT InOperation                BOOL             Side register controller is operating
           Error                      BOOL             Indicates an error
                                                       Clear error with "Enable" = FALSE
                   ErrorID            ⮫ ERROR_CODE     Diagnostic description in case of error
                   ErrorIdent         ⮫ ERROR_STRUCT Detailed diagnostics
                   InPause            BOOL           "Pause" is active. The "ControlValue" and
                                                     "ParameterControlValue" outputs maintain
                                                     their values

I/O type       Name                  Data type              Description
PresetAck             BOOL                   "Preset" is completed. The "Preset" value is
                                             copied to the "ControlValue" and "Parame‐
                                             terControlValue" outputs
ActStep               UDINT                  Step value, incrementing with every new
                                             value at the "ControlValue" output
SetpointLockAck       BOOL                   "Setpoint" applied. Current value in
                                             "RecordedPosition" is copied to "Setpoint"
HighLimitActive       BOOL                   Upper limit is active. "ControlValue" would
                                             be higher, but is limited to "HighLimit"

LowLimitActive        BOOL                   Lower limit is active. "ControlValue" would
                                             be lower, but it is limited to "LowLimit"
ControlValue          LREAL                  Control value calculated by the register
                                             controller
CurrentValue          LREAL                  Recorded position currently used in the
                                             register controller side.
                                             Note: Converted "RecordedPositionWidth"
                                             value
Deviation             LREAL                  Difference of the command value side (con‐
                                             verted "SetpointWidth") - "CurrentValue" of
                                             the side register controller (mm)
CommandPosition LREAL                        Calculated command position for the drive
VAR_IN_OUT     SetpointWidth   LREAL                        Command value (setpoint) width value (in
                                             technical units)
ControlledAxis        ⮫ AXIS_REF             Reference to the controlled axis

Table 824: Min./max. and default values of the inputs of the MB_RegisterControllerSideType01
function block
Name            Type             Min. value       Max. value        Default value    Effective
Enable          BOOL                                                FALSE            Continuous
Pause           BOOL                                                FALSE            Continuous
Preset          BOOL                                                FALSE            "Enable" TRUE
                                                                                     (continuous)
Step            UDINT            0                2^32 -1           0                Continuous. Starts
                                                                                     at a rising edge
                                                                                     at "Enable" and at
                                                                                     a falling edge at
                                                                                     "Pause"
PresetValue     LREAL            n. def.          n. def.           0.0              Rising edge at
                                                                                     "Preset"
SetpointLock BOOL                n. def.          n. def.           FALSE            Continuous
ControlPolarity BOOL                                                FALSE            Continuous
ControlType     MB_CORREC‐       n. def.          n. def.           0                Rising edge at
                TION_TYPE                                                            "Enable"
PIControlData MB_PICON‐                                                              Continuous
                TROL_DATA
RecordedPosi‐ LREAL              n. def.          n. def.           0.0              Change of "Step"
tionWidth
TriangleTan‐    LREAL            0.0              n. def.           1.0              Rising edge at
gent                                                                                 "Enable"

Functional description
Initialization
During initialization, the "SetpointWidth" and "RecordedPositionWidth" inputs
have to have valid data.
PresetValue
For a trouble-free start of the controller outputs "ControlValue" and "Com‐
mandPosition", set the "Preset" input before activating the "Enable" input.
During this period, the "SetpointWidth" and "RecordedPositionWidth" inputs
have to have valid data. In addition, the upper limits and lower limits are
monitored to ensure a limitation of the "ControlValue" output if the current
value for "PresetValue" is beyond the valid range of "HighLimit" or "LowLimit".
The "PresetAck" output is active when the value at "PresetValue" input is
copied to the "ControlValue" output. The "Preset" input has a higher priority
than the "Pause" input. The value in "PresetValue" is copied to the respec‐
tive output at the rising edge at the "Preset" input if "Enable" is active. If
successful, the "PresetAck" output is set to TRUE.
Pause
The "Pause" input is only analyzed when the "Enable" input is active. In this
case, the deviation ("SetpointWidth" – "RecordedPositionWidth") is set to 0.
Therefore, the outputs "ControlValue" and "CommandPosition" do not change
anymore. This can be used to maintain the values of the "ControlValue" and
"CommandPosition" outputs. The "ActStep" output is updated even if the
"Pause" input is active. As long as the "Pause" input is active, the "InPause"
output is TRUE.
Smoothing
The "TControl" input is the attenuation constant for the "RecordedPosition‐
Width" input. If this input set to 0, smoothing is inactive.
ResponseCurve
To scaled the control deviation, use the "ResponseCurve" input. Use this
functionality to specify a smaller scaling of the control deviation for smaller
control deviations. This results in a lower proportional gain and thus causes a
smoother control behavior in a steady state.
When parameterizing the input, the controller parameters should first be
set without evaluation. Subsequently, a lower scaling should be specified.
This allows to globally set the controller parameters first using the system
dynamics, and then, a local optimization is ensured (e.g. for the steady state).
The local optimization is parameterized with a characteristic curve with up
to four data points. Negative deviations are processed by point reflection of
the curve at the origin. This results in a total of nine linear sections. The
section s5 passes the origin. The sections s1 and s9 have a slope of 1 and
each run into positive or negative infinity. If the input is not assigned, a 1-to-1
characteristic curve is used as default value. That means that it is not scaled.

Points P1 to P4 are stored in an array of IL_COORD_TYPE01. If less than four
points are required, the x-coordinates of the points not required (beginning
with the last point) are set to 0. The x-values have to be positive and increase
in positive direction. The same point can be stored twice.
TriangleTangent
The length of the marks between opposite leg and adjacent leg (tan α).

Normal mode
The register controller side only calculates a new value when the "Step" input
changes. The "PControl" and "IControl" and "TControl" controller parameters
can be changed permanently.
If the value in the "ControlValue" output exceeds or falls below the values of
the outputs "HighLimit" or "LowLimit", "ControlValue" is limited to one of the
following limit values.
● If the value in "ControlValue" is positive, the value in "HighLimit" is used
● If the value in "ControlValue" is negative, the value in "LowLimit" is used
If the register controller side has an integral action time, an anti-reset wind-up
is carried out and the integral action is no longer summed up. In this case, the
"HighLimitActive" and "LowLimitActive" outputs are set to TRUE.

## 30.4 Error codes of the CXA_RegisterControl

ErrorID            Additional1               Additional2          Description
INPUT_INVALID_ERRO 16#0A0F0116               16#0C230001          Correction path < Correction
R                                                                 start hysteresis (0.25% of modulo
                                             value)
INPUT_INVALID_ERRO 16#0A0F0116               16#0C230002          Correction start < 0
R
INPUT_INVALID_ERRO 16#0A0F0116               16#0C230003          Correction end < 0
R

ErrorID            Additional1   Additional2       Description
INPUT_INVALID_ERRO 16#0A0F0116   16#0C230004       ModuloValue < 0
R
INPUT_INVALID_ERRO 16#0A0F0116   16#0C230005       RecordedPosition < 0
R
INPUT_INVALID_ERRO 16#0A0F0116   16#0C230006       "CorrectionStart" > "ModuloValue"
R
INPUT_INVALID_ERRO 16#0A0F0116   16#0C230007       "CorrectionEnd" > "ModuloValue"
R
INPUT_INVALID_ERRO 16#0A0F0116   16#0C230008       "RecordedPosition" > "Modulo‐

R                                                  Value"
INPUT_INVALID_ERRO 16#0A0F0116   16#0C230009       Correction path > "ModuloValue"
R
INPUT_INVALID_ERRO 16#0A0F0116   16#0C230010       Invalid correction mode
R
INPUT_INVALID_ERRO 16#0A0F0116   16#0C230011       Correction start = Correction end
R
INPUT_INVALID_ERRO 16#0A0F0116   16#0C230012       Axis format is absolute
R
INPUT_INVALID_ERRO 16#0A0F0116   16#0C230013       ProbeDistance < 0 or
R                                                  > CONST_SHIFT_REGISTER
INPUT_INVALID_ERRO 16#0A0F0116   16#0C230014       Setpoint > ModuloValue
R
INPUT_INVALID_ERRO 16#0A0F0116   16#0C230015       Setpoint < 0
R
INPUT_INVALID_ERRO 16#0A0F0116   16#0C230016       Feedback > ModuloValue
R
INPUT_INVALID_ERRO 16#0A0F0116   16#0C230017       Feedback < 0
R
INPUT_INVALID_ERRO 16#0A0F0116   16#0C230018       ModuloValue < 0
R
INPUT_INVALID_ERRO 16#0A0F0116   16#0C230019       MarkGating < 0
R
INPUT_INVALID_ERRO 16#0A0F0116   16#0C230020       HighLimit < LowLimit
R
INPUT_INVALID_ERRO 16#0A0F0116   16#0C230021       PControl < 0
R
INPUT_INVALID_ERRO 16#0A0F0116   16#0C230022       Axis for axis command was not
R                                                  found
INPUT_INVALID_ERRO 16#0A0F0116   16#0C230023       Input "SetpointWidth" < 0
R
INPUT_INVALID_ERRO 16#0A0F0116   16#0C230024       "RecordedPositionWidth" < 0
R
INPUT_INVALID_ERRO 16#0A0F0116   16#0C230025       Input "TriangleTangent" beyond
R                                                  the range
INPUT_INVALID_ERRO 16#0A0F0116   16#0C230026       Input "FormatLength" beyond the
R                                                  range
