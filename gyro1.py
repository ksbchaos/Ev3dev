#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sound import Sound
from time import sleep
cl = ColorSensor() 
steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
sound = Sound()
while True:
    if cl.ambient_light_intensity > 20: #주변광이 20보다 크면 주행
       steer_pair.on(0,50)
       sleep(0.01)
    else:  # 그외의 조건이면 주행 멈춤
       steer_pair.off()
       sleep(0.01)    

