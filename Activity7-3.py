#!/usr/bin/env python3
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C, MoveSteering
from ev3dev2.sensor.lego import TouchSensor, UltrasonicSensor
from time import sleep
from ev3dev2.display import Display
from textwrap import wrap
from ev3dev2.sound import Sound
from threading import Thread
us = UltrasonicSensor() 
us.mode='US-DIST-CM'
ts1 = TouchSensor('in1') 
ts2 = TouchSensor('in2')
sound = Sound()
lcd = Display()
steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
speed=0
def show_text(string, font_name='courB24', font_width=15, font_height=24):
    lcd.clear()
    strings = wrap(string, width=int(180/font_width))
    for i in range(len(strings)):
        x_val = 89-font_width/2*len(strings[i])
        y_val = 63-(font_height+1)*(len(strings)/2-i)
        lcd.text_pixels(strings[i], False, x_val, y_val, font=font_name)
    lcd.update()
def accel():
    global speed
    while loop==True: # repeat until 'loop' is set to False in the main thread.
        if  ts1.wait_for_bump() == True:
            speed+=10
            steer_pair.on(steering=0,speed=speed)
        else:
             sleep(0.01)
def decel():
    global speed
    while loop==True: # repeat until 'loop' is set to False in the main thread.
        if  ts2.wait_for_bump() == True:
            speed-=10
            steer_pair.on(steering=0,speed=speed)
        else:
             sleep(0.01)             
loop = True
# Start the play_sound thread.
t = Thread(target=accel)
t.start()
t1 = Thread(target=decel)
t1.start()
while True:
    text = 'speed='+str(speed)
    show_text(text)
    #sleep(0.1)
