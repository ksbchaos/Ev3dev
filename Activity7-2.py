#!/usr/bin/env python3
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C, MoveSteering
from ev3dev2.sensor.lego import TouchSensor, UltrasonicSensor
from time import sleep
from ev3dev2.sound import Sound
from threading import Thread
us = UltrasonicSensor() 
us.mode='US-DIST-CM'
ts1 = TouchSensor('in1') 
ts2 = TouchSensor('in2')
sound = Sound()
steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
speed=0
def accel():
    global speed
    while loop==True: # repeat until 'loop' is set to False in the main thread.
        if  ts1.wait_for_bump() == True:
            speed+=10
            steer_pair.on(steering=0,speed=speed)
        else:
             sleep(0.01)
loop = True
# Start the play_sound thread.
t = Thread(target=accel)
t.start()
while True:
    if  ts2.wait_for_bump() == True:
        speed-=10
        steer_pair.on(steering=0,speed=speed)
    else:
        sleep(0.01)
