#!/usr/bin/env python3
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C, MoveSteering
from ev3dev2.sensor.lego import TouchSensor, UltrasonicSensor
from ev3dev2.sound import Sound
from ev3dev2.display import Display
from textwrap import wrap
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

lcd = Display()
def show_text(string, font_name='courB24', font_width=15, font_height=24):
    lcd.clear()
    strings = wrap(string, width=int(180/font_width))
    for i in range(len(strings)):
        x_val = 89-font_width/2*len(strings[i])
        y_val = 63-(font_height+1)*(len(strings)/2-i)
        lcd.text_pixels(strings[i], False, x_val, y_val, font=font_name)
    lcd.update()
us = UltrasonicSensor() 
us.mode='US-DIST-CM'
ts = TouchSensor()
sound = Sound()
leds = Leds()
steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
WaitForBump()
show_text('FORWARD')
steer_pair.on(steering=0, speed=20)
while not ts.is_pressed:  # while touch sensor is not pressed
    sleep(0.01)
show_text('BACKWARD')
steer_pair.off()
sleep(1)
#leds.set_color('LEFT', 'RED')
#leds.animate_flash('AMBER', sleeptime=0.75, duration=10)
#leds.animate_police_lights('RED', 'GREEN', sleeptime=0.75, duration=5)
#leds.animate_police_lights('RED', 'GREEN', sleeptime=0.75)
leds.set(Leds.LEFT, brightness_pct=1, trigger='timer')
leds.set_color(Leds.LEFT, Leds.RED)
steer_pair.on_for_seconds(steering=0, speed=-20, seconds=3, brake=True, block=True)
