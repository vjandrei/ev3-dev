#!/usr/bin/env python3
from ev3dev.brickpi3 import *
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound
from evdev import InputDevice, categorize, ecodes

# https://www.youtube.com/watch?v=F5-dV6ULeg8&t=602s
# https://core-electronics.com.au/tutorials/using-usb-and-bluetooth-controllers-with-python.html
# use dinput in 8bitdo
# ssh as robot@ see the ip on the ev3 device (ssh robot@192.168.1.139)
# cat /dev/input/eventx(2)
#

gamepad = InputDevice('/dev/input/event2')
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


sound = Sound()
mA = MediumMotor(OUTPUT_A)
mB = MediumMotor(OUTPUT_B)
# TODO: Add code here

# evdev takes care of polling the controller in a loop
for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        if event.value == 1:
            if event.code == yBtn:
                print("Y")
                sound.speak('Autobots, roll out!')
                sound.play_file('autobot.wav')
            elif event.code == bBtn:
                print("B")
                mA.run_forever(speed_sp=1000)
            elif event.code == aBtn:
                print("A")
                mA.stop()
            elif event.code == xBtn:
                print("X")
