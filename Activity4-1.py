#!/usr/bin/env python3
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C, MoveSteering
from ev3dev2.sensor.lego import TouchSensor, UltrasonicSensor,ColorSensor
from ev3dev2.sound import Sound
from ev3dev2.display import Display
from textwrap import wrap
from threading import Thread
#from ev3dev2.led import Leds
from time import sleep
ts = TouchSensor()
cl = ColorSensor()
sound=Sound()
steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
steer_pair.on(steering=0, speed=20) 
while True:
    #steer_pair.on(steering=0, speed=20)  
    #while loop==True:
    if cl.color_name== 'Red':
       steer_pair.off()
       sleep(0.1)
    elif cl.color_name== 'Green':
       steer_pair.on(steering=0, speed=20) 
       sleep(0.1) 
    else:
       sleep(0.1)