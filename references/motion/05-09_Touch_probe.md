# 5.9 Touch probe

Configuration
To configure the function, the following steps are required:
●   Adding probe-related parameters to the cyclic data
●   Assigning probe-related signals to the axis profile
●   Connecting the probe to the corresponding input of the drive
●   Setting the probe parameters in the Data Layer

SoE
To use the touch probe function, first configure the drive. Connect the probe
hardware (I/O) to the drive and set the drive parameter S-0-0401 to probe 1
and S-0-0402 to probe 2 as described in the following steps:
Probe1 IDN          Probe2 IDN           Description        Data type
S-0-0401            S-0-0402             Probe status       UINT
S-0-0130            S-0-0132             Probe value, posi‐ DINT
                                         tive edge
S-0-0131            S-0-0133             Probe value, nega‐ DINT
                                         tive edge
S-0-0409            S-0-0411             Touch probe, posi‐ UINT
                                         tively recorded
S-0-0410            S-0-0412             Touch probe, neg‐ UINT
                                         atively detected
P-0-0202            P-0-0203             Difference of      DINT
                                         measured values
                                         S-0-0130 to
                                         S-0-0131 or
                                         S-0-0132 to
                                         S-0-0133
P-0-0224            P-0-0225             Number of marker UINT
                                         failures
Please configure the I/Os as described in the following four steps:

Axis profile

After configuration in drive and ctrlX I/O Engineering, the following AT entries
should be mapped to the axis profile in ctrlX MOTION UI (⮫ Chapter 8.1.3
Window – “Axis Profiles” on page 803):

CoE
The touch probe function has to be configured in the CoE drive. The engi‐
neering software of the drive should be used. Connect the probe hardware
(I/O) to the input for the probe of the drive.

                                                                                      Axis profile
Configure the signal selection of the probe in the drive.

The touch probe-related parameters has to be configured in ctrlX I/O Engi‐
neering. The user can only configure probe 1 or probe 2. If the push-button
function only requires one positive (negative) edge, the other, negative (posi‐
tive) edge, can be ignored. The following table shows the required parameters
for the respective probe:

Probe1 IDN          Probe2 IDN          Description        Data type
0x60BA              0x60BC              Probe value, posi‐ DINT
                                        tive edge
0x60BB              0x60BD              Probe value, nega‐ DINT
                                        tive edge
0x60D5              0x60D7              Touch probe, posi‐ UINT
                                        tively recorded
0x60D6              0x60D8              Touch probe, neg‐ UINT
                                        atively detected
Once all settings have been selected, you can load the PDO configuration into
the EtherCAT bus.

After configuration in drive and ctrlX I/O Engineering, the following AT entries
should be mapped to the axis profile in ctrlX MOTION UI:

                                                                                    Axis profile
Related topics
● ⮫ Chapter 6.1.3 Measuring probe on page 76
● ⮫ Chapter Synchronizing Motion objects on page 79
