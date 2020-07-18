#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.display import Display
from PIL import Image
from time import sleep
ts = TouchSensor()
lcd = Display()
Angry = Image.open('Angry.bmp') 
Winking = Image.open('Winking.bmp')
lcd.image.paste(Angry, (0,0)) # 0,0위치에 이미지 출력
lcd.update()
#steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C) # 스티어링 모드 설정
#steer_pair.on(0,50) # 직진 스팅어링으로 속도 50% 무한 주행
while not ts.is_pressed:  # while touch sensor is not pressed
    sleep(0.01)
lcd.image.paste(Winking, (0,0)) # 0,0위치에 이미지 출력
lcd.update()
sleep(5)
