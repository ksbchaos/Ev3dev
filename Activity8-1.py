#!/usr/bin/env python3
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C, MoveSteering
from ev3dev2.sensor.lego import TouchSensor, UltrasonicSensor,ColorSensor
from ev3dev2.button import Button
from time import sleep
from ev3dev2.display import Display
from textwrap import wrap
from ev3dev2.sound import Sound
from threading import Thread
us = UltrasonicSensor() 
us.mode='US-DIST-CM'
ts = TouchSensor() 
cl = ColorSensor()
sound = Sound()
btn = Button()
steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
def WaitForBump():  # a 'bump' is a release of the touch sensor button
    PreviousState=0
    while True:
        CurrentState=ts.value()
        if PreviousState==1 and CurrentState==0: #button was released
            break     # button has just been released so exit loop
        PreviousState=CurrentState   # Ready for next loop
        sleep(0.01)  # don't read the sensor too frequently
def left(state):
    global color_list
    if state:
        sound.beep()
        color_list.append('Blue')
    else:
        sleep(0.01)
def right(state):  # neater use of 'if' follows:
    sound.beep()
    print(color_list.append('Green') if state else sleep(0.01))
def up(state):
     
    print('Up button pressed' if state else 'Up button released')
def down(state):
     
    print('Down button pressed' if state else 'Down button released')
def enter(state):
    
    print(color_list.append('Yellow') if state else sleep(0.01))
btn.on_left = left
btn.on_right = right
btn.on_up = up
btn.on_down = down
btn.on_enter = enter
color_list = []  # create empty list
sound.beep()
while ts.wait_for_bump() == False:
    btn.process()
    sleep(0.01)        
#for i in range(4):  # i=0 then 1 then 2 then 3
sound.beep()
ts.wait_for_bump()
#sound.play_file('/home/robot/sounds/Horn 2.wav')
for col in color_list:
    if col=='Blue':
       sound.beep()      # blue: turn the robot 90 degrees left
       steer_pair.on(steering=0,speed=10)
       sleep(1)
    elif col=='Green': 
       sound.beep()   # green: go straight forward for one wheel rotation
       steer_pair.on(steering=0,speed=30)
       sleep(1)
    elif col=='Yellow':  
       sound.beep()  # yellow: turn the robot 90 degrees right
       steer_pair.on(steering=30,speed=10)
       sleep(1)
