#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import (
    Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (
    Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

from ev3dev2.motor import (MoveJoystick, MoveSteering, OUTPUT_A)

import struct

# Declare motors
main_motor = Motor(Port.A)

aBtn = 304
bBtn = 305
xBtn = 307
yBtn = 308

# left pad center value 128
# left pad center max left value 0
# left pad center max right value 255
# left pad center max top value 0
# left pad center max bottom value 255
lPadrTl = 0
lPadtTb = 1

# right pad center value 128
# right pad center max left value 0
# right pad center max right value 255
# right pad center max top value 0
# right pad center max bottom value 255
rPadrTl = 2
rPadtTb = 5

# Initialize variables.
# Assuming sticks are in the middle when starting.
rPad_x = 128
rPad_y = 128

# A helper function for converting stick values (0 - 255)
# to more usable numbers (-100 - 100)


def scale(val, src, dst):
    """
    Scale the given value from the scale of src to the scale of dst.

    val: float or int
    src: tuple
    dst: tuple

    example: print(scale(99, (0.0, 99.0), (-1.0, +1.0)))
    """
    return (float(val - src[0]) / (src[1] - src[0])) * (dst[1] - dst[0]) + dst[0]


# Find the 8BitDo Gamepad:
# /dev/input/event2 is the usual file handler for the gamepad.
infile_path = "/dev/input/event2"

# open file in binary mode
in_file = open(infile_path, "rb")

# Read from the file
# long int, long int, unsigned short, unsigned short, unsigned int
FORMAT = 'llHHI'
EVENT_SIZE = struct.calcsize(FORMAT)
event = in_file.read(EVENT_SIZE)

while event:
    (tv_sec, tv_usec, ev_type, code, value) = struct.unpack(FORMAT, event)

    if ev_type == 3 and code == 0:
        rPad_x = value
    if ev_type == 3 and code == 1:
        rPad_y = value

    # Scale stick positions to -100,100

    right = scale(rPad_x, (0, 255), (100, -100))
    left = scale(rPad_x, (0, 255), (100, -100))
    # Set motor voltages. If we're steering left, the left motor
    # must run backwards so it has a -left component
    # It has a forward component for going forward too.
    # steer_motor.dc=(45-steer_motor.angle())
    # main_motor.angle(45)
    right = round(right, 1)

    main_motor.dc(right - left)
    main_motor.dc(right + left)

    # Finally, read another event
    event = in_file.read(EVENT_SIZE)

in_file.close()

# evdev takes care of polling the controller in a loop
for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        if event.value == 1:
            if event.code == yBtn:
                print("Y")
            elif event.code == bBtn:
                print("B")
                # mA.run_forever(speed_sp=1000)
            elif event.code == aBtn:
                print("A")
                # mA.stop()
            elif event.code == xBtn:
                print("X")
            elif event.code == lPadrTl:
                print("left pad")
