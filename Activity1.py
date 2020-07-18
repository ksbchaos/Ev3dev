#!/usr/bin/env python3
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import TouchSensor
from time import sleep
from ev3dev.ev3 import *
ts = TouchSensor()
tank_pair = MoveTank(OUTPUT_B, OUTPUT_C)
#tank_pair.on(left_speed=30, right_speed=30)
tank_pair.on_for_seconds(left_speed=50, right_speed=25, seconds=1.6, brake=True, block=True)
tank_pair.on_for_seconds(left_speed=-25, right_speed=-50, seconds=1.2, brake=True, block=True)
tank_pair.on_for_seconds(left_speed=50, right_speed=50, seconds=1, brake=True, block=True)
while not ts.is_pressed:  # while touch sensor is not pressed
    sleep(0.01)
tank_pair.off()
sleep(5)