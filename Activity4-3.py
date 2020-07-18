#!/usr/bin/env python3
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C, MoveSteering
from ev3dev2.sensor.lego import TouchSensor, UltrasonicSensor,ColorSensor
from ev3dev2.sound import Sound
from ev3dev2.display import Display
from textwrap import wrap
from threading import Thread
from time import sleep
ts = TouchSensor()
cl = ColorSensor()
steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
while True:
    #steer_pair.on(steering=0, speed=20)  
    #while loop==True:
    if cl.color_name== 'Red':
       steer_pair.off()
       sleep(0.1)
       while True:
             if cl.color_name== 'Green':
                break 
             else:
                sleep(0.1)
    else:
       if cl.reflected_light_intensity<30:   # weak reflection so over black line
        # medium turn right
        steer_pair.on(steering=30, speed=10)
       else:   # strong reflection (>=30) so over white surface
        # medium turn left
        steer_pair.on(steering=-30, speed=10)
 
        
    
