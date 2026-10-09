# 5.11 Overview of drive parameters

Function           ctrlX DRIVE                             External drive
                   SoE                    CoE              CoE
Control/status     S-0-0134               0x6040           0x6040
word               S-0-0135               0x6041           0x6041
Signal status word S-0-0144               0x2C82:01
                   S-0-0026               0x2C82:02
                   S-0-0328               0x2C82:03

Function          ctrlX DRIVE                    External drive
                  SoE           CoE              CoE
Scaling           S-0-0044      0x60A8           0x60A8
                  S-0-0045      0x60A9           0x60A9
                  S-0-0046      0x60AA           0x60AA
                  S-0-0076      0x6076           0x6076
                  S-0-0077      0x2906:01
                  S-0-0078      0x2906:02
                  S-0-0079      0x2906:03
                  S-0-0086      0x6091:01
                  S-0-0093      0x6091:02

                                                                             Axis profile
                  S-0-0094      0x6092:01
                  S-0-0103
                  S-0-0121
                  S-0-0122
                  S-0-0123
                  S-0-0160
                  S-0-0161
                  S-0-0162
Operating mode    S-0-0032:     0x6060           0x6060
switching         S-0-0033:     0x6061           0x6061
                  S-0-0034
                  S-0-0035
                  S-0-0284
                  S-0-0285
                  S-0-0286
                  S-0-0287
Position control  S-0-0047:     0x607A           0x607A
                  S-0-0051      0x6064           0x6064
Velocity control  S-0-0036:     0x60FF           0x60FF
                  S-0-0040      0x606C           0x606C
Torque/force con‐ S-0-0080      0x6071           0x6071
trol              S-0-0084      0x6077           0x6077
Drive error diag‐ S-0-0390      0x1002:00        0x603F
nostics
Travel limits     S-0-0049      0x607B:01        0x607B:01
                  S-0-0050      0x607B:02        0x607B:02
                  S-0-0055
                  S-0-0038
                  S-0-0039
                  S-0-0091
                  S-0-0092
                  S-0-0138

Function            ctrlX DRIVE                External drive
                    SoE            CoE         CoE
Homing              S-0-0147       0x2505:02   0x607C
                    S-0-0148       0x2508:01   0x6098
                    S-0-0191       0x607C
                    S-0-0448       0x6098
                    S-0-0052/4
                    S-0-0150/1
Homed-Prüfung       S-0-0403       0x2508:01
Stillstandsprüfung S-0-0331        0x2212:04
Drive Halt          S-0-0115
Set absolute posi‐ S-0-0447        0x2500:01
tion                S-0-0227/115   0x2510:01
                    S-0-0052/4     0x2510:02
Positive stop drive S-0-0149
procedure           S-0-0530
                    S-0-0092
                    S-0-0533
Multiple-braking    P-0-0117
dynamics            P-0-0117.0.1
                    P-0-0117.0.2
                    P-0-0119
                    S-0-0138
                    S-0-0349
                    S-0-0372
                    S-0-0429
Touch probe drive S-0-0130         0x60B8      0x60BA
                    S-0-0131       0x60B9      0x60BB
                    S-0-0132       0x60BA      0x60BC
                    S-0-0133       0x60BB      0x60BD
                    S-0-0169       0x60BC
                    S-0-0170       0x60BD
                    S-0-0405       0x60D5
                    S-0-0406       0x60D6
                    S-0-0409       0x60D7
                    S-0-0410       0x60D8
                    S-0-0411
                    S-0-0412
                    S-0-0415
                    S-0-0426
                    S-0-0427
                    S-0-0524
                    S-0-0525
                    S-0-0526
                    S-0-0527
                    P-0-0200

Function            ctrlX DRIVE                              External drive
                    SoE                  CoE                 CoE
                    P-0-0201
                    P-0-0204
                    P-0-0205
                    P-0-0224
                    P-0-0225
                    P-0-0226
Touch probe con‐    P-0-2755
trol                P-0-0187
Parameter           S-0-0030             0x100A

checksum            S-0-0326             0x2B60:04
                    S-0-0327             0x2B60:0E
