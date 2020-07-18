#!/usr/bin/env python3
from ev3dev2.motor import  OUTPUT_B, OUTPUT_C, MoveSteering
from ev3dev2.sensor.lego import TouchSensor, UltrasonicSensor
from time import sleep
from ev3dev2.sound import Sound
from threading import Thread
from ev3dev2.display import Display
us = UltrasonicSensor() 
us.mode='US-DIST-CM'
ts = TouchSensor()
lcd = Display()
sound = Sound()
sound.beep()
while True:
    Distance=us.value()
    if  ts.is_pressed == True and Distance < 400:
        lcd.text_pixels('Motor Start& Idle', x=0, y=60, font='courB14')
        lcd.update()
        sound.beep()
        sleep(0.2) 
    else:
        sleep(0.01)

