#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sound import Sound
from time import sleep
cl = ColorSensor() 
steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
sound = Sound()
while True: 
    if cl.color_name=='Green':
        steer_pair.on(0,50)
    elif cl.color_name=='Red':
        steer_pair.off()
        sleep(0.01)