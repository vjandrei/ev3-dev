#!/usr/bin/env python3
from ev3dev.brickpi3 import *
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.led import Leds
from ev3dev2.sound import Sound

m = MediumMotor(OUTPUT_A)
m.run_forever(speed_sp=1000)
