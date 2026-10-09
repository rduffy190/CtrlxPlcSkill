# 4.3 System performance

The number of axes that can be used simultaneously, specified by ctrlX
MOTION is set to 128 axes for all controls. However, depending on the appli‐
cation and cycle time, this number of axes cannot be achieved.
When designing a machine, there is no getting around the question of overall
performance:
● How many axiss does the machine have?
● What cycle time is required for the application?
● What other tasks should the control system perform?
This chapter provides an overview of the performance of the ctrlX MOTION
on the various control systems. Various application scenarios are run through
here. The specified performance values should be seen as a rough guide. They
may vary depending on the field of application in practice.
All values given here are for a relatively unloaded control. If other applications
generate load, the values may be worse.

Handling application
This simple application only executes buffered commands. These buffered
commands can be positioning motions, for example.
The table shows the possible bus cycle time depending on the control and
the number of axes.
ctrlX     <= 4 axes <= 10        <= 25      <= 30       <= 50        <= 75     <= 100      <= 125
CORE                axes         axes       axes        axes         axes      axes        axes
x3        1000 µs 1000 µs        2000 µs    2000 µs     4000 µs
x5        500 µs    500 µs       500 µs     500 µs      1000 µs      2000 µs   2000 µs     2000 µs
x7        500 µs    500 µs       500 µs     500 µs      500 µs       500 µs    500 µs      500 µs

  Flexprofile application
  This application executes Flexprofiles on all axes. This application requires
  significantly more computing operations in the control and is therefore also
  slower.
  The table shows the possible bus cycle time depending on the control and
  the number of axes.
ctrlX          <= 4 axes <= 10       <= 25        <= 30     <= 50      <= 75       <= 100     <= 125
CORE                     axes        axes         axes      axes       axes        axes       axes
x3             2000 µs 2000 µs       4000 µs      4000 µs
x5             500 µs    500 µs      1000 µs      2000 µs   2000 µs    4000 µs     4000 µs    4000 µs
x7             500 µs    500 µs      500 µs       500 µs    500 µs     1000 µs     1000 µs    1000 µs
