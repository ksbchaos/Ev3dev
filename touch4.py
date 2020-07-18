#!/usr/bin/env python3
from ev3dev2.sensor import INPUT_1, INPUT_2
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from time import sleep
ts1 = TouchSensor(INPUT_1) # INPUT_1 포터에 ts1 터치센서 설정
ts2 = TouchSensor(INPUT_2) # INPUT_2 포터에 ts2 터치센서 설정
led = Leds()
led.all_off() # 모든 led 오프 
while True: # 무한 루프, 뒤로가기 버튼으로 정지.
    led.set_color('LEFT', ('GREEN',  'RED')[ts1.is_pressed]) # 터치1 클릭할때 왼쪽 LED 빨강
    led.set_color('RIGHT', ('GREEN', 'RED')[ts2.is_pressed]) # 터치2 클릭할때 오른쪽 LED 빨강
    sleep (0.01) 