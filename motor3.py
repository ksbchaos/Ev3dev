#!/usr/bin/env python3
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C
from time import sleep
tank_pair = MoveTank(OUTPUT_B, OUTPUT_C)
tank_pair.on(50, 50)
sleep(1)
tank_pair.off(brake=True)
sleep(1)
tank_pair.on_for_seconds(50, 50, 2)
sleep(1)
tank_pair.on_for_rotations(50, 50, -3)
sleep(1)
tank_pair.on_for_degrees(50, 50, 180)
sleep(1)