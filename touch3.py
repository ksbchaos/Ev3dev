#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import TouchSensor
from time import sleep
ts = TouchSensor()
steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C) # 스티어링 모드 설정
steer_pair.on(0,50) # 직진 스팅어링으로 속도 50% 무한 주행
while not ts.is_pressed:  # 터치센서가 온이 될 때 까지 무한 루프
    sleep(0.01)
steer_pair.on(0,-50) # 직진 스팅어링으로 반대 방향으로 속도 50% 무한 주행
sleep(5)