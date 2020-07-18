#!/usr/bin/env python3
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C, MoveSteering
from ev3dev2.sensor.lego import TouchSensor, UltrasonicSensor,ColorSensor
from ev3dev2.sound import Sound
from ev3dev2.display import Display
from textwrap import wrap
from threading import Thread
#from ev3dev2.led import Leds
from time import sleep
#from ev3dev.ev3 import *
ts = TouchSensor()
cl = ColorSensor()
steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
steer_pair.on(steering=0, speed=20)

while not ts.is_pressed:
    if cl.color_name== 'Black':
       steer_pair.off()
    else:
        sleep(0.1)  
