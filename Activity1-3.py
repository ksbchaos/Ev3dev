#!/usr/bin/env python3
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import TouchSensor, UltrasonicSensor
from ev3dev2.sound import Sound
from time import sleep
us = UltrasonicSensor() 
us.mode='US-DIST-CM'
ts = TouchSensor()
sound = Sound()
tank_pair = MoveTank(OUTPUT_B, OUTPUT_C)
#tank_pair.on(left_speed=30, right_speed=30)
tank_pair.on_for_seconds(left_speed=-50, right_speed=-25, seconds=1.6, brake=True, block=True)
tank_pair.on(left_speed=25, right_speed=50)
while True:
  Distance=us.value()/10
  if  Distance < 7:
    tank_pair.off(brake=True)
    sleep(1)
    sound.play_tone(440, 1)
    tank_pair.on_for_seconds(left_speed=-50, right_speed=-50, seconds=1, brake=True, block=True)
    break
  else:
    sleep(0.01)
