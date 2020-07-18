#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import TouchSensor, UltrasonicSensor
from time import sleep
steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
us = UltrasonicSensor()
ts = TouchSensor()
steer_pair.on(steering=0, speed=50)
while us.distance_centimeters > 10: #센서 거리가 10cm 보다 가까울 때까지 직진 
        sleep(0.01)
steer_pair.off() # 주행 멈춤