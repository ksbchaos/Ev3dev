#!/usr/bin/env python3
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.display import Display
from ev3dev2.sound import Sound
from time import sleep
lcd = Display()
us = UltrasonicSensor()
sound = Sound()
sound.beep()
while True: 
    distance = us.distance_centimeters 
    lcd.text_pixels(str(distance) +' cm', x=40, y=50, font='courB24')
    lcd.update()
    sleep(0.1) 