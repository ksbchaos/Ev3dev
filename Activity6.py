#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_B, OUTPUT_C, MoveSteering
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
def play_welcome():
    global Distance
    while loop==True: # repeat until 'loop' is set to False in the main thread.       
       Distance=us.value()
       if Distance < 400: 
          lcd.text_pixels('Welcome', x=40, y=50, font='courB24')
          lcd.update()
          sleep(0.2) 
       else:
          sleep(0.1) 
loop = True
t = Thread(target=play_welcome)
t.start()
sound.beep()
while True:
    
    if  ts.is_pressed == True:
        lcd.text_pixels('Ignition', x=40, y=70, font='courB24')
        lcd.update()
        sleep(0.2) 
        sleep(1)
    else:
        sleep(0.01)

