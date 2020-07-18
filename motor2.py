#!/usr/bin/env python3
from ev3dev2.motor import MediumMotor, OUTPUT_B
from time import sleep
mm = MediumMotor()
mm.on(speed=50, brake=True, block=False)
sleep(1)
mm.off()
sleep(1)
mm.on_for_seconds(speed=50, seconds=2, brake=True, block=True)
sleep(1)
mm.on_for_rotations(50,3)
sleep(1)
mm.on_for_degrees(50,90)
sleep(1)
mm.on_to_position(50,180)
sleep(1)