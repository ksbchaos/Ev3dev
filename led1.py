#!/usr/bin/env python3
from ev3dev2.led import Leds
from time import sleep
led = Leds()
led.all_off() # 모든 led 오프 
sleep(1)
# 왼쪽 LED는 빨강, 오른쪽 LED는 노랑
led.set_color('LEFT', 'RED')
led.set_color('RIGHT', 'YELLOW')
sleep(3)
# RED 밝기와 GREEN 밝기 비율로 색을 만듬. 
#(RED밝기,GREEN 밝기) 100%는 1로 스케일 설정
led.set_color('LEFT', (1, 0)) # 밝은 RED
led.set_color('RIGHT', (0, 1)) # 밝은 GREEN.
sleep(3)