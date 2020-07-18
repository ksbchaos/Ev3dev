#!/usr/bin/env python3
from ev3dev2.motor import  OUTPUT_B, OUTPUT_C, MoveSteering
from ev3dev2.sensor.lego import TouchSensor
from time import sleep
ts = TouchSensor()
sound = Sound()
steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
steer_pair.on_for_rotations(steering=0, speed=50, rotations=4.5, brake=True, block=True)
sleep(1)
steer_pair.on_for_degrees(steering=100, speed=10, degrees=180, brake=True, block=True)
sleep(1)
steer_pair.on_for_rotations(steering=0, speed=50, rotations=3)
sleep(1)
steer_pair.on_for_degrees(steering=100, speed=10, degrees=180, brake=True, block=True)
sleep(1)
steer_pair.on_for_rotations(steering=0, speed=50, rotations=5)
sleep(1)
steer_pair.on_for_degrees(steering=100, speed=10, degrees=180, brake=True, block=True)
sleep(1)
steer_pair.on(steering=0, speed=50)
while not ts.is_pressed:  # while touch sensor is not pressed
    sleep(0.01)
tank_pair.off()
sleep(5)


