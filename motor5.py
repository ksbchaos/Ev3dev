#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, OUTPUT_B, OUTPUT_C
from time import sleep
steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C) # 스티어링 모드 설정
steer_pair.on(0,50) # 직진 스팅어링으로 속도 50% 무한 주행
sleep(1)
steer_pair.off(brake=True) # 주행 멈춤
sleep(1)
steer_pair.on_for_seconds(30,50, 2) # 좌회전 스팅어링으로 속도 50% 2초 주행
sleep(1)
# 직진 스팅어링으로 속도 50% 반대방향 3회전 주행
steer_pair.on_for_rotations(0,50, -3)  
sleep(1)
steer_pair.on_for_degrees(0,50, 180)  # 직진 스팅어링으로 속도 50% 180도 주행
sleep(1)
