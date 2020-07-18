#!/usr/bin/env python3
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C, MoveSteering
from ev3dev2.sensor.lego import TouchSensor, UltrasonicSensor
from ev3dev2.sound import Sound
#from ev3dev2.led import Leds
from time import sleep
from ev3dev.ev3 import *

def WaitForBump():  # a 'bump' is a release of the touch sensor button
    PreviousState=0
    while True:
        CurrentState=ts.value()
        if PreviousState==1 and CurrentState==0: #button was released
            break     # button has just been released so exit loop
        PreviousState=CurrentState   # Ready for next loop
        sleep(0.01)  # don't read the sensor too frequently

us = UltrasonicSensor() 
us.mode='US-DIST-CM'
ts = TouchSensor()
sound = Sound()
leds = Leds()
steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
WaitForBump()
steer_pair.on(steering=0, speed=20)
while not ts.is_pressed:  # while touch sensor is not pressed
    sleep(0.01)
steer_pair.off()
sleep(1)
#leds.set_color('LEFT', 'RED')
#leds.animate_flash('AMBER', sleeptime=0.75, duration=10)
#leds.animate_police_lights('RED', 'GREEN', sleeptime=0.75, duration=5)
#leds.animate_police_lights('RED', 'GREEN', sleeptime=0.75)
leds.set(Leds.LEFT, brightness_pct=1, trigger='timer')
leds.set_color(Leds.LEFT, Leds.RED)
steer_pair.on_for_seconds(steering=0, speed=-20, seconds=3, brake=True, block=True)
