#!/usr/bin/env python3
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C, MoveSteering
from ev3dev2.sensor.lego import TouchSensor, UltrasonicSensor
from time import sleep
from ev3dev2.sound import Sound
from threading import Thread
us = UltrasonicSensor() 
us.mode='US-DIST-CM'
ts = TouchSensor()
sound = Sound()
steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
def play_sound():
    global Distance
    while loop==True: # repeat until 'loop' is set to False in the main thread.       
       Distance=us.value()
       if Distance < 300: 
          sound.play_tone(440, Distance/1000)
          #sleep(0.1)
       else:
          sleep(0.1) 
loop = True
t = Thread(target=play_sound)
t.start()
steer_pair.on(steering=0,speed=10)
while True:
    
    steer_pair.on(steering=0,speed=Distance/10)
    if  Distance < 40:
        steer_pair.off(brake=True)
        loop = False
        sleep(1)
    else:
        loop = True
        sleep(0.01)

