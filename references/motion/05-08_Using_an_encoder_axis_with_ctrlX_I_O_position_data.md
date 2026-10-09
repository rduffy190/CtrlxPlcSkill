# 5.8 Using an encoder axis with ctrlX I/O position data

The encoder axis can process position data not only from the ctrlX DRIVE but
also via the ctrlX I/O device.
First, the I/O device should be configured in I/O Engineering.

                                                                                     Axis profile
Configuration in I/O Engineering
The configuration is then downloaded to ctrlX CORE.
Next, the required elements have to be assigned within the axis profile.
(Please note that there are two options for homing with ctrlX I/O. They have
different requirements for mapping of the elements.
                          Control-based             Device-based
Supports the "cyclic      No                        Yes
homed" flag
PDO requirement           Encoder position          Input mapping element:
                                                    io-encoder-referenced
                                                    position
                                                    Output mapping ele‐
                                                    ment:
                                                    io-encoder-set-reference
                                                    io-encoder-reference-
                                                    offset
In general, device-based homing triggers the homing function in the ctrlX I/O
device, thereby enabling the cyclic home state. However, this requires at least
4 PDO mapping elements.

Variable assignment of device-based homing
The control-based referencing method manages an offset between the device
and the axis. The value is managed by the Motion control. It is simpler and
requires only one PDO data mapping element, but it does not support cyclic
referencing.

Variable assignment for control-based referencing
Finally, link the encoder profile to an encoder axis — and you are all set.
