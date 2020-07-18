#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import TouchSensor, ColorSensor
from time import sleep
from ev3dev2.sound import Sound
ts = TouchSensor()
cl = ColorSensor()
steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C) # 스티어링 모드 설정
while not ts.is_pressed:  # 터치 센서를 클릭하면 멈춤
         if cl.reflected_light_intensity < 30:
              steer_pair.on(30,10) # 오른쪽 방향으로 10 속도로 주행
         else:
              steer_pair.on(-30,10) # 왼쪽 방향으로 10 속도로 주행  