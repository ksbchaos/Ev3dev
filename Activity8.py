#!/usr/bin/env python3
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C, MoveSteering
from ev3dev2.sensor.lego import TouchSensor, UltrasonicSensor,ColorSensor
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
steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
def WaitForBump():  # a 'bump' is a release of the touch sensor button
    PreviousState=0
    while True:
        CurrentState=ts.value()
        if PreviousState==1 and CurrentState==0: #button was released
            break     # button has just been released so exit loop
        PreviousState=CurrentState   # Ready for next loop
        sleep(0.01)  # don't read the sensor too frequently
color = []
'''Colors=[]  # create empty list
for i in range(0, 4):  # i=0 then 1 then 2 then 3
    sound.beep()
    WaitForBump()
    while True:   # Wait for a valid color to be detected
        ColorCode=cl.color_name
        if ColorCode==2 or ColorCode==3 or ColorCode==4:
        # blue,green,yellow
            Colors.append(ColorCode)
            break   # exit the loop
        sleep(0.01)  # don't read the sensor too frequently
sound.beep()
for k in range(0, 4):     # k=0 then 1 then 2 then 3
    if Colors[k]==2:      # blue
        steer_pair.on(steering=0,speed=10)
    elif Colors[k]==3:    # green
        steer_pair.on(steering=0,speed=30)
    elif Colors[k]==4:    # yellow
        steer_pair.on(steering=30,speed=10)
    sleep(3)  # give enough time for the motors to finish moving
'''

def get_color():
    while True:   # Wait for a valid color to be detected
        color = cl.color_name
        if color in ('Blue', 'Green', 'Yellow'):
            color_list.append(color)
            break   # exit the loop
        sleep(0.01)
color_list = []  # create empty list
for i in range(4):  # i=0 then 1 then 2 then 3
    sound.beep()
    ts.wait_for_bump()
    get_color()
sound.beep()
#sound.play_file('/home/robot/sounds/Horn 2.wav')
for col in color_list:
    if col=='Blue':      # blue: turn the robot 90 degrees left
       steer_pair.on(steering=0,speed=10)
       sleep(1)
    elif col=='Green':    # green: go straight forward for one wheel rotation
       steer_pair.on(steering=0,speed=30)
       sleep(1)
    elif col=='Yellow':    # yellow: turn the robot 90 degrees right
       steer_pair.on(steering=30,speed=10)
       sleep(1)
