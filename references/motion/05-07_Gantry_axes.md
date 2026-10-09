# 5.7 Gantry axes

Adding the digital input module to the EtherCAT Master
To detect switching signals (e.g. reference switch, positive limit switch and
negative limit switch) when homing gantry axes (⮫ Chapter 7.2.41 AxsCtrlBa‐
sedGantryHoming - Control-based homing of gantry axes on page 507), add a
digital input module to ctrlX I/O Engineering.

In this view, the digital input module has to be included in the device list and
the actual switching signal is to be assigned to the user-defined digital input
channel.

Assigning an axis profile variable

In the variable assignment dialog, the variables switch-ref, switch-poslim and
switch-neglim can be assigned by the specified digital input channel.
