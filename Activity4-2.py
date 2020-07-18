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
while not ts.is_pressed:    # exit loop when any button pressed
    if cl.reflected_light_intensity<30:   # weak reflection so over black line
        # medium turn right
        steer_pair.on(steering=30, speed=10)
    else:   # strong reflection (>=30) so over white surface
        # medium turn left
        steer_pair.on(steering=-30, speed=10)
