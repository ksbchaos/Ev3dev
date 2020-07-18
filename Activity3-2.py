#!/usr/bin/env python3
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C, MoveSteering
from ev3dev2.sensor.lego import TouchSensor, UltrasonicSensor
from ev3dev2.sound import Sound
from ev3dev2.display import Display
from ev3dev2.sensor.lego import ColorSensor
from textwrap import wrap
from threading import Thread
#from ev3dev2.led import Leds
from time import sleep
from ev3dev.ev3 import *
ts = TouchSensor()
lcd = Display()
def show_text(string, font_name='courB24', font_width=15, font_height=24):
    lcd.clear()
    strings = wrap(string, width=int(180/font_width))
    for i in range(len(strings)):
        x_val = 89-font_width/2*len(strings[i])
        y_val = 63-(font_height+1)*(len(strings)/2-i)
        lcd.text_pixels(strings[i], False, x_val, y_val, font=font_name)
    lcd.update()

def WaitForBump():  # a 'bump' is a release of the touch sensor button
    PreviousState=0
    while True:
        CurrentState=ts.value()
        if PreviousState==1 and CurrentState==0: #button was released
            break     # button has just been released so exit loop
        PreviousState=CurrentState   # Ready for next loop
        sleep(0.01)  # don't read the sensor too frequently

cl = ColorSensor()
def auto():
  while loop==True:
    if cl.reflected_light_intensity < 15:
        show_text('Light On')
    else:
        show_text('Light Off')  
loop = True
t = Thread(target=auto)
t.start()  
WaitForBump()
loop = False
show_text('          ') 
show_text('Light On')
while not ts.is_pressed:
    sleep(0.1)
show_text('Light OFF')
sleep(5)