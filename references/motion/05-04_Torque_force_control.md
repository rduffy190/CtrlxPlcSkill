# 5.4 Torque/force control

In torque/force control mode, a target force or a target torque is specified.
The control loop is based on force control. The maximum feed rate is limited
by the appropriate limits. This function is used for the motion command
axsTorque (⮫ Chapter 7.2.10 AxsTorque - Torque axis on page 354). Further
information: ⮫ Chapter 6.2.5 Torque/force control on page 155.
The following input and output variables have to be used:
Input
torque-force   Torque_Force_Torque_actual_value

torque limit     Torque_force_control_Torque_limitation_status
status
Output
torque-force     Torque_force_control_Target_torque
torque-high-     Torque_force_control_High_velocity_limit_value
velocity-limit
torque-low-      Torque_force_control_Low_velocity_limit_value
velocity-limit

SoE
The "Torque/force control with speed limitation" operation mode has to be
configured in a secondary operation mode in the drive. e.g. secondary oper‐
ating mode 2 value "0x8101 hex" or "33025 decimal".

This can be realized by a one-off parameterization in the drive or by config‐
uring the start parameters in the IO project.
Due to the automatic adjustment of the operation mode, it is not important
which operating mode was selected as velocity or torque/force control mode.
If the velocity control or torque/force control operation modes is displayed in
this list, the drive can detect these operating modes.
Configure the corresponding cyclic data in ctrlX I/O Engineering to be able to
access the torque/force Motion commands.

                                                                                        Axis profile
In this view, the parameter of the current actual torque/force value, S-0-0084,
has be added to the list of Acknowledge Data Telegram (AT) PDOs.

In this view, the parameter of the current torque/force command value
S-0-0080 has to be added to the list of the Master Data Telegram (MDT)
PDOs.
Parameter IDN Description
MDT
S-0-0080          Torque/force target torque
P-0-2249          Torque/force high velocity limit
(P-0-0421.0.3 in
EIDN format in
ctrlX Drive Engi‐
neering)

P-0-2250          Torque/force low velocity limit
(P-0-0421.0.4 in
EIDN format in
ctrlX Drive Engi‐
neering)
AT:
S-0-0084          Torque/Force: Actual torque value
P-0-2251          Torque/force control: Torque limitation status
(P-0-0421.0.7 in
EIDN format in
ctrlX Drive Engi‐
neering)
Only 16-bit parameters can be applied as cyclic data. (e.g. P-0-2249, the
associated 32-bit parameter in EIDN format P-0-421.0.3 cannot be applied
cyclically).

CoE
The operation mode "cyclic sync torque mode" is used.

For drives with COE connection, it is required to set the speed limitation for
torque mode once.
To do this, the value "4" has to be entered in the parameter object 0x60CA
"Torque/force control Torque limitation option code".
Otherwise, an error message is reported when the torque command is acti‐
vated.
CAN-IDN      Description

0x6071       Torque/force target torque
0x60C9       Torque/force high velocity limit
0x60C8       Torque/force low velocity limit

0x6077       Torque/force: Actual torque value
0x60CC       Torque/force control: Torque limitation status
