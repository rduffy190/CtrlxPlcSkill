# 5.1 Overview

The axis profile serves as the link between the axes of the ctrlX MOTION and
the drives on the field bus. For the EtherCAT field bus, it supports the SoE
and CoE profiles. The axis profile thus abstracts the hardware of the axis. This
allows for hardware-independent programming of the Motion application. An
axis of the ctrlX MOTION can be created as a logic axis without hardware and
later connected to a physically existing drive via the axis profile.
In ctrlX I/O Engineering (see documentation EtherCAT Master App chapter
⮫ EtherCAT Configuring field bus devices) EtherCAT devices (e.g. drives) are
manually added or added via scan and transmitted to the control at the
EtherCAT bus master.

  An “IndraDrive” is configured at EtherCAT Master in this view. The Ethercat
  address of IndraDrive is "1003". To create an axis profile for this drive, an axis
  profile with the device address 1003 has to be created in the configuration
  and the variables of this drive have to be linked to e.g. the variables of the
  axis profile (see also documentation EtherCAT Master App ⮫ Window - Status).

The I/O parameters of the EtherCAT I/O image are contained in the IndraDrive
properties apart from the address. These specifications are contained in the
tab of the configured drive.
When assigning the axis profile, the system also attempts to map all config‐

                                                                                     Axis profile
ured variables of the drive/encoder to the corresponding variables in the axis
profile. This assignment can be checked and adjusted in the following dialog.
At the same time, further axis profile variables can be assigned to the
EtherCAT drive variables here. These drive variables have to be configured
accordingly in the I/O configuration.
If the "Expert settings" are enabled in the "General" tab of the EtherCAT drive,
a "Process data expert mode" tab is displayed in which further data can be
configured in the cyclic communication channel.

 Configuring the velocity command value in the cyclic communication
