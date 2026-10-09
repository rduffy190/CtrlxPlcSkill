# 15 CXA_MBus

## 15.1 Introduction and overview

### 15.1.1 Overview

M-Bus (meter bus) used to read meter devices (e.g. water, gas, electrical or
consumption meters) acc. to the European standard EN 13757-2 Physical and
link layer, EN 13757-3 Application layer.
Use the CXA_MBus library with the ctrlX I/O XI531001 1Ch. M-Bus master
(R911423593). The ctrlX I/O XI531001 can be operated either locally on a
ctrlX CORE or decentrally with a bus coupler.
With the ctrlX I/O XI531001 1Ch. M-Bus master can communicate with up to
50 M-bus devices.

The CXA_MBus library contains the fundamental basic services for the M-Bus
start. There is also an extended part, that is an M-Bus SDK, a toolbox to use
existing function blocks or to create own solutions for own M-Bus devices.
The M-Bus basic services include raw data communication, bus scanning and
addressing. The module transmits data transparently between the communica‐
tion devices (M-Bus slaves) and the control.

Based on CXA_MBus, Bosch Rexroth provides a Software Development Kit
(SDK) with the CXA_MBusSDK library. The SDK provides specific function
blocks for M-Bus devices and is open source. The library contains a function
block template "IH_MBUS_SDK" (including comments) used to create own
function blocks. The template includes a standardized "state machine", error
handling and M-Bus communication handling. The library is to be continuously
extended with further M-Bus device-specific function blocks. Function blocks
are already included for some M-Bus-specific devices. These function blocks
are used to guide through SDK and to create own function blocks.
The following function blocks are for example available:
● KDK1-45AM-12 (KDK-Dornscheidt) - IH_MBUS_KDK1_45AM_12
● PadPulsM1 (Relay GmbH) - IH_MBUS_REL_PadPulsM1
Please contact Bosch Rexroth or your contact person if you would like to
use or contribute to the library and provide your function blocks to Bosch
Rexroth.

Table 259: Function blocks of the CXA_MBus library
Function block     Description
IH_XIMBUSClient    Master function block that ensures the communication
                   with the M-Bus master module and provides the commu‐
                   nication handle “IH_XI_MBUS_LINK” for the other function
                   blocks.
IH_XIMBUS_Raw‐     Sending and receiving RAW M-Bus data telegrams
Data               Enables communication with:
                 ● Short Frame
                 ● Control Frame
                 ● Long Frame
IH_XIMBUS_Scan Scanning and retrieving M-Bus device information
IH_XIMBUS_SetAd‐ Setting or changing M-Bus device address
dress

Examples
The examples show the wiring of the IH_XIMBUS_RawData function block.
The resulting M-Bus request telegram and response telegram are also dis‐
played.
The first example shows the reading of a counter value from an M-Bus device
with the address 8.

The second example shows the writing/sending of a Long Frame to an M-Bus
device with address 8. Hier wird exemplarisch der Zählerwert auf 0 zurück
gesetzt.

### 15.1.2 General information on signal processing

                                                              Process Data
                             TX Handling
                                              TX Buffer            from
                              (asynch.)
                                                                EtherCAT
                                               511 Byte        1 .. 30 Byte

        M-Bus Interface

                                                              Process Data
                             RX Handling
                                              RX Buffer              to
                              (asynch.)
                                                                EtherCAT
                                               511 Byte        1 .. 30 Byte

On the EtherCAT side, the process data image has a data width of 30 bytes
in both the send and receive directions. A handshake mechanism is used to
signal that new data is available.
Between the M-Bus interface and the EtherCAT bus interface is a buffer of 511
bytes each for send and receive data.

If the data cannot be sent fast enough, the respective buffer fills up and data
is lost. This can result in the sending direction if the data rate of the interface
is lower than the data rate of the data transmitted via EtherCAT. In receive
direction, this can result if the data rate of the interface is higher than that of
the data transmitted via EtherCAT.

Possible transmission rates
 An EtherCAT process data image contains 30 bytes of payload in the send and
 receive direction. In every second EtherCAT cycle, it is possible to send or
 receive up to 30 bytes:
● In the first cycle, data is transferred in the process data.
● In the second cycle, the remote station acknowledges data reception.

With a cycle time of 10 ms, 30 bytes per second can be transferred 50 times.
If the data format "8E1" is set, each transmitted byte is composed as follows:
●   1 starting bit
●   8 data bits
●   1 parity bit
●   1 stop bit
This corresponds to 11 bits for each byte of process data to be transferred.
The above settings result in a continuous transmission rate of:
50[1/s] × 30[byte] × 11[bit] = 16500baud(bit/s)
The maximum M-bus transmission is 38,400 baud. The next lowest M-Bus
standard transmission rate is 9,600 baud. With a cycle time of 10 ms, con‐
tinuous transmission with up to 9,600 baud can be guaranteed. Use the
engineering tool to configure the transmission rate in the module. It is not
possible with the PLC function block.
If the control cannot retrieve the data from the module quickly enough, the
data is temporarily stored in the receive buffer of the module. If the receive
buffer is full, all further data is lost. There is also a buffer for the sending
data. If the buffer is full, all further data is lost.
Continuous data transmission results in the following maximum data rates:
Cycle time           Computed data rate          Standard data rate
1 ms                 165.000 bit/s               38,400 baud
5 ms                 33.000 bit/s                38,400 baud
10 ms                16.500 bit/s                9,600 baud
20 ms                8.250 bit/s                 4,800 baud
30 ms                5.500 bit/s                 4,800 baud
50 ms                3.300 bit/s                 2,400 baud
100 ms               1.650 bit/s                 600 baud

### 15.1.3 Meter bus (M-bus)

General information
 The M-Bus (meter bus) is a bus system to network and remotely read supply
 meters, e.g. to measure gas or water consumption.
 A general overview is provided in the following.
For further details, refer to the official website ⮫ https://m-bus.com/.

    Telegram types
The data is generally transmitted in the following telegram types:
Single character (Single Short frame (Short   Control frame (Control Long frame (Long
Character)               Frame)               Frame)                 Frame)
E5h                     Start 10 h            Start character 68h   Start character 68h
                        C-field               L-field = 3           L-field
                        A-field               L-field = 3           L-field
                        Checksum              Start character 68h   Start character 68h
                        Stop character 16h    C-field               C-field
                                              A-field               A-field
                                              CI field              CI field

                                              Checksum              User data
                                                                    0 to 252 bytes
                                              Stop character 16h    Checksum
                                                                    Stop character 16h

    Telegram description
● The Single Character E5hex is used to confirm correctly received messages.
● The Short Frame always consists of five characters. The start character
  is "10h". The checksum results from adding the fields C and A without
  transferring these fields. The stop character is "16h", as for the Control and
  Long Frame.
● Nine characters are always transmitted with the Control Frame. "68h" is
  used as start character. The L-field (length field) always has the value three.
  The checksum is created using the fields C, A and CI.
● The difference between the Long Frame and the Control Frame is that
  payload can be transmitted after the CI field. The length of the telegram
  and the content of the L-field - created from the number of payload plus
  three - vary accordingly.

Field-(byte) description
● 4Byte Header: 1byte 0x68, 2x 1byte L-field is the length field that specifies
  the size of the payload and 1byte 0x68
● C-field: The C-field, control or function field indicates which function is
  executed, in which direction it is communicated and whether it is a request
  or a response.
● A-field: Address field, addresses from 1 to 250 can be assigned. M-Bus
  devices not yet configured have the primary address 0. The address 254
  (FEhex) is used as broadcast to address all M-Bus devices.
● CI field: The control information field is part of the application and con‐
  tains commands.
● 1Byte: 1Byte checksum (bytes added after the header)
● 1Byte stop character: 1Byte 0x16

Example
Request

Short Frame        Read           Address             Checksum            Stop character

0x10               0x5B           0x01                0x5C                0x16

Response (Long Frame)

Header                            C-field   A-field   CI field   User data Checksu   Stop
                                                                          m          character

0x68      0x1B     0x1B    0x68   0x08      0x01      0x72       24Byte   e.g. 0x29 0x16
          (len)    (len)

## 15.2 Troubleshooting

Troubleshooting
The function blocks of the library use the error codes ADD1: 16#0A0F.011C
and ADD2, to be found in:
● CXA_MBus CXA_MBus_ErrorAdd
● CXA_EthercatMaster ErrorCodes
For the MBus error codes, refer to the Global Variable List
CXA_MBus_ErrorAdd of the library CXA_EthercatMaster.
For the CXA_EthercatMaster error codes, refer to the Global Variable List
ErrorCodes in the library CXA_EthercatMaster.

It following error messages can be created in Additional2:

Table 260: CXA_MBus error codes
ErrorID                 Additonal2   Description
INPUT_INVALID_RAN       16#0001      The input in "TimeOut" is invalid (5s - 60s).
GE
INPUT_INVALID_RAN       16#0002      The input in "SizeOfUserData" is invalid (1 - 252 bytes).
GE
INPUT_INVALID_RAN       16#0003      The input in "RequestType" is invalid.
GE
INPUT_INVALID_RAN       16#0004      The input in "Control_C_Field" is invalid.
GE
INPUT_INVALID_RAN       16#0005      The input in "ControlInfo_CI_Field" is invalid.
GE

INPUT_INVALID_RAN       16#0006      The input in "OldAddress" is invalid (0 - 250).
GE
INPUT_INVALID_RAN       16#0007      The input in "NewAddress" is invalid (0 - 250).
GE
INPUT_INVALID_ERR       16#0065      The input in "MBUSLink" is invalid (Invalid Pointer Addr).
OR
INPUT_INVALID_ERR       16#0066      The input in "UserDataAdr" is invalid (Invalid Pointer Addr).
OR
INPUT_INVALID_ERR       16#0067      The input in "InProcData" is invalid (Invalid Reference).
OR
INPUT_INVALID_ERR       16#0068      The input in "OutProcData" is invalid (Invalid Reference).
OR
INPUT_INVALID_ERR       16#0069      Client token not available or invalid. Check the connection
OR                                   with the function block IH_XIMBUSClient.
DEVICE_ERROR            16#0191      Time error. The device does not respond.
DEVICE_ERROR            16#0192      Function block IH_XIMBUSClient is busy.
DEVICE_ERROR            16#0193      Telegram error - collision, reported by the ctrlX I/O MBus
module.
DEVICE_ERROR            16#0194      Overcurrent, reported by the ctrlX I/O MBus module.
DEVICE_ERROR            16#0195      Setting "NewAddress" failed. Check that the correct "OldAd‐
dress" is entered.
STATEMA‐                16#012D      Internal state machine function block error
CHINE_ERROR
