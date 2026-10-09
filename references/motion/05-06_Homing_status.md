# 5.6 Homing status

To enable the display of the cyclic homing status in ctrlX Motion, the corre‐
sponding status word has to be defined in the axis profile (see ⮫ Chapter
6.2.7 Axis status information on page 168). If no cyclic homed signal is con‐
figured, the information is retrieved acyclically when the drive turns on the
power.

SoE
The configuration of S-0-0144 (signal status word) of the drive has to match
S-0-0403.0 (homing status: feedback value status).

In ctrlX I/O Engineering, the signal status word has to be set in the AT. This
must then be mapped to the axis profile.

    Input
    statusword   Drive_status_word
