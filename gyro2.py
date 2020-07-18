#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_B, OUTPUT_C, MoveSteering
from ev3dev2.sensor.lego import GyroSensor
from time import sleep
gyro = GyroSensor()
steering_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
steering_pair.on(40,30) # 오른쪽 방향 주행모드
gyro.wait_until_angle_changed_by(45) # 자이로 센서 기울기가 45도 될때까지 기다림.
steering_pair.on(0,50) # 직진 주행 모드
sleep(3)
