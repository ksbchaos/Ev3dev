#!/usr/bin/env python3
from ev3dev2.display import Display
from time import sleep
from PIL import Image
lcd = Display()
heart = Image.open('Heart.bmp') # Heart.bmp 파일 불러오기
lcd.image.paste(heart, (0,0)) # 0,0위치에 이미지 출력
lcd.update()
sleep(5)