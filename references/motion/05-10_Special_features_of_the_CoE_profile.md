# 5.10 Special features of the CoE profile

General information
CiA402 is a flexible protocol defining many optional objects for the object
directory. This result in the phenomena that different manufacturers imple‐
ment the same function with different objects. Specify more attributes to
support more brands of third party providers.
The ctrlX MOTION supports the following versions of the CiA402 protocol:
Document                                Version
CANopen device profile for drives and 4.0.0
Motion control, part 1: General defini‐
tions
CANopen device profile for drives       4.1.0
and Motion control, part 2: Operating
modes and application data
CANopen device profile for drives and 4.0.0
Motion control, part 3: PDO mapping
CANopen device profile for drives and 1.0.0
Motion control, part 4: Safety func‐
tionality
CANopen device profile for drives and 1.0.0
Motion control, part 5: PDO mapping
superset
CANopen device profile for drives and 1.0.0
Motion control, part 6: CANopen FD
PDO mapping
The ctrlX MOTION does not support all drive types. Please compare the list
of available CoE objects for the drive with the list under ⮫ Chapter 5.11
Overview of drive parameters on page 68.

Linear axes based on increments
This is a general CoE solution for the basic CoE function. The function can
easily be extended to adjust different third party drives.

1.    ScalingStrategy stands for the specific scaling strategy. The available
      value can be: SOE_STANDARD, COE_CALC_DRIVE, COE_CALC_CONTROL.
      The value depends on the profile type.
      ● SoE profile: SOE_STANDARD available.
      ● CoE profile: COE_CALC_DRIVE, COE_CALC_CONTROL available
      The COE_CALC_DRIVE strategy indicates that the scaling calculation is
      performed on the drive end.
      The COE_CALC_CONTROL strategy indicates that the scaling calculation
      is performed on the controller.
         Currently, COE_CALC_CONTROL is intended for drives of third party
      providers.
2.    ScalingType refers to the motion type of the axis: LINEAR or ROTARY
3.    Counter and denominator: Collectively define the scaling information
      (only available for the COE_CALC_CONTROL strategy)
4.    Resolution: corresponds to the encoder resolution (only available for the
      COE_CALC_CONTROL strategy)
Remarks:
1.    The scaling parameters (numerator and denominator) on the control
      should be exactly the same as on the drive end
2.    The scaling parameters (resolution) on the control should correspond to
      the actual encoder resolution
3.    The setting of the scaling parameters on the controller only become
      active if the COE_CALC_CONTROL strategy is selected
4.    The scaling strategy COE_CALC_CONTROL currently only supports the
      position mode.
5.    The axis profile Wittenstein/Inovance is supported. Other brands can
      also be supported but have to be tested for compatibility first.

Modulo axes
This is a general CoE solution for the basic CoE function. The function can be
easily extended to adapt various third-party drives. For third-party drives, all
module-related data conversions between the control and drive are performed
in ctrlX MOTION, therefore there are no special requirements and settings for
third-party drives. For the motion setting in ctrlX MOTION, an axis has to be
created or changed to the modulo type:

                                                                                     Axis profile
A compatible modulo value is also required:

1.    The modulo axis moves along the shortest path. The axis position should
      always be in the range between 0 and smaller modulo.
2.    To change the modulo value, the system first has to be switched to
      setup mode. The new modulo value becomes active when the system
      is switched back to operating mode.

Assigning multi-axis devices to axis profiles

Some CoE servo drives enable the connection of devices with multiple axes
with a single EtherCAT address. The second drive has a parameter offset com‐
pared to the first channel. Therefore, the main purpose of this function is to
solve application scenarios where a single EtherCAT address corresponds to
multiple axes.

Configuring AT and MDT in EtherCAT Master
After installing the device description file (XML file) in IO-Engineering, the
following figure shows the process data for several axes:

Assigning the PDO axis profile variable
Configuring the first axis:

                                                                                      Axis profile
Configuring the second axis:

Assigning the "ScalingStrategy" variable
Different third-party devices correspond to different values of scaling informa‐
tion.
Example of a linear axis:
If the resolution of the motor encoder is 8388608, connected to a lead
spindle with a pitch of 1 mm/rev. If the customer wants to set the output
of the lead spindle end to 1 mm/rev and the end resolution is 0.0001 mm/rev,
the numerator and denominator are calculated as follows:

The results should be configured as scaling information:
1.   Set scaling strategy to COE_CALC_CONTROL
2.   Set resolution to 8388608
3.   Set counter to 524288 (after reduction)
4.   Set denominator to 625 (after reduction)

                                                                                         Axis profile

Configuring the drive number:
The drive number of Profile_1 is 0, the drive number of Profile_2 is 1. If
only one axis is available, the value is 0, which corresponds to the default
value. If there is more than one axis, the drive number should be sequen‐

tially increased by 1. Figures ⮫ Assigning multi-axis devices to axis profiles
on page 63 and ⮫ Assigning multi-axis devices to axis profiles on page 63
show an example.
After configuring the axis profile, it should be added to the axis, see
⮫ Assigning multi-axis devices to axis profiles on page 63.
