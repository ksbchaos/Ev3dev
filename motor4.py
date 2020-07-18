#!/usr/bin/env python3
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import TouchSensor
from time import sleep
ts = TouchSensor()
tank_pair = MoveTank(OUTPUT_B, OUTPUT_C)
tank_pair.on(50,50)
while not ts.is_pressed:  # while touch sensor is not pressed
    sleep(0.01)
tank_pair.off()
sleep(5)