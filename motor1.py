#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor
from time import sleep
lm = LargeMotor()
lm.on(speed=50, brake=True, block=False)
sleep(1)
lm.off()
sleep(1)
lm.on_for_seconds(speed=50, seconds=2, brake=True, block=True)
sleep(1)
lm.on_for_rotations(50,3)
sleep(1)
lm.on_for_degrees(50,90)
sleep(1)
lm.on_to_position(50,180)
sleep(1)