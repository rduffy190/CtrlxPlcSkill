# 5.2 Position control

The axis profile supports the position operating modes of the drive. This
feature is designed for closed-loop drivers. The target position of the drive is
set cyclically. The actual position is monitored and compared. This function is
used for all position-based motion commands.
Input
position        Position_feedback_value_1
statusword      Drive_status_word
Output
position        Position_command_value
controlword     Master_control_word

                                                                                     Axis profile
