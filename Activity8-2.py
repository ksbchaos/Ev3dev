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
#def change(changed_buttons):   # changed_buttons is a list of 
# tuples of changed button names and their states.
#    if ('left', True) in changed_buttons:
#        sound.beep()
#        color_list.append('Blue')
def left(state):
    global color_list
    if state:
        #sound.beep()
        color_list.append('Blue')
    else:
        print('left button released')
def right(state):  # neater use of 'if' follows:
    #sound.beep()
    print(color_list.append('Green') if state else 'right button released')
def up(state):
     
    print(color_list.append('Yellow') if state else 'Up button released')
def down(state):
     
    print(color_list.append('Red') if state else 'Down button released')
def enter(state):
  if state:
     for col in color_list:
        if col=='Blue':
           sound.beep()      # blue: turn the robot 90 degrees left
           steer_pair.on(steering=-30,speed=20)
           sleep(1)
        elif col=='Green': 
          sound.beep()   # green: go straight forward for one wheel rotation
          steer_pair.on(steering=30,speed=20)
          sleep(1)
        elif col=='Yellow':  
          sound.beep()  # yellow: turn the robot 90 degrees right
          steer_pair.on(steering=0,speed=20)
          sleep(1)
        elif col=='Red':  
          sound.beep()  # yellow: turn the robot 90 degrees right
          steer_pair.on(steering=0,speed=-20)
          sleep(1)
        else:
          print('enter button released')
  else:
     steer_pair.off() 
     print('enter button released')   
#btn.on_change = change
btn.on_left = left
btn.on_right = right
btn.on_up = up
btn.on_down = down
btn.on_enter = enter
color_list = []  # create empty list
sound.beep()
while  True:
    btn.process()
    sleep(0.01)        
