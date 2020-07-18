#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import UltrasonicSensor
from time import sleep
steering_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
us = UltrasonicSensor()
while True:    
    distance = us.distance_centimeters
    if distance > 5 and distance < 15: # 센서거리가 5보다 크고 15보다 가까우면 주행
        steering_pair.on(0,50)
    else: # 그외의 센서 거리는 주행 멈춤
        steering_pair.off()
    sleep(0.1)