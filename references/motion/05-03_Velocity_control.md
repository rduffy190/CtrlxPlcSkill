# 5.3 Velocity control

The axis profile supports the velocity mode of the drive. This function is
intended for drivers with a closed loop and is used to synchronize motions.
Switch to the OP mode only in AH and with the axis at standstill. This func‐
tion is used for the "axsVelocity" motion command, connected to ⮫ Chapter
7.2.9 AxsVelocity - Axis velocity on page 350.

Input
velocity        Velocity_Actual_Value
Output
velocity        Target_Velocity

SoE
Configuring the operation mode in the drive
The velocity control system has to be configured correctly. This can be done
once in the operating mode selection parameter in ctrlX DRIVE Engineering, or
via the startup parameters in ctrlX IO Engineering.

In this view, the default setting is retained. Second.op.mode 1 corresponds to
the velocity control.

Configuring the AT and MDT in the EtherCAT Master
Configure the cyclic data in ctrlX I/O Engineering to be able to access the
velocity Motion commands.

In this view, insert the parameter of the actual velocity value, S-0-0040, in the
AT PDO content.

In this view, the parameter of the velocity command value, S-0-0036, has to
be inserted into the MDT-PDO content.

Assigning the axis profile variables

                                                                                      Axis profile
You can add further axis profile variables via     under the “Variables” tab. In
the dialog, the velocity variable of the input and output can be assigned from
the cyclical value of the drive velocity.

CoE

Configuring the AT and MDT in the EtherCAT Master
After installing the device description file (XML file) in ctrlX I/O Engineering,
the cyclic data can access the velocity Motion commands in ctrlX I/O Engi‐
neering.

If the "Modes of Operation" and "Modes of Operation Display" are not directly
contained in the XML file, the following configuration should be added man‐
ually in ctrlX I/O Engineering:
Actual velocity value 606C, actual position value 6064 and status word 6041
have be added to the "Transmit PDO mapping parameter".

The target velocity value 60FF, the target position value 607A and the status
word 6040 have to be added to the "Receive PDO Mapping Parameter".

Assigning a PDO (Process Data Object) to an axis profile variable
A CoE axis profile should be created in ctrlX MOTION UI according to the sec‐
tion "CoE supports linear axes based on increments". The inputs and outputs
of the field bus device should then be assigned to the axis profile.

                                                                                   Axis profile
Scaling strategy assignment of the variables
See ⮫ Elements of the editor “Profile properties <Axis profile name>”
on page 830, “Scaling” tab.
Different third-party devices correspond to different values.
