# 5.5 Multiple braking dynamics and diagnostic number

This function is used to activate the "Drive-Controlled Shutdown" drive func‐
tion. In this case, the deceleration ramp is not specified by the control but is
controlled by the drive. This feature is available only for ctrlX Drive.
Input
diagcode        Diagnostic_message_number

SoE
To be able to use the function “several brake dynamics” in dependency of the
drive error, configure the diagnostic message number in ctrlX I/O Engineering.

                                                                                     Axis profile
In this view, the parameter for diagnostic message number S-0-0390 have to
be inserted into the AT-PDO content.
