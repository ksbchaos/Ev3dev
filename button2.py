#!/usr/bin/env python3
from ev3dev2.button import Button
from ev3dev2.display import Display
from time import sleep
btn = Button()
lcd = Display()
# Do something when state of any button changes:
def left(state): # left 이벤트 함수
    if state: # 왼쪽 버튼 눌림
        lcd.text_pixels('Left button pressed', x=0, y=50, font='courB14')
        lcd.update()
        sleep(0.2)
    else: # 왼쪽 버튼 땜
        lcd.text_pixels('Left button released', x=0, y=50, font='courB14')
        lcd.update()
        sleep(0.2)
def right(state): # right 이벤트 함수
    if state:  # 오른쪽 버튼 눌림
        lcd.text_pixels('Right button pressed', x=0, y=50, font='courB14')
        lcd.update()
        sleep(0.2)
    else: # 오른쪽 버튼 땜
        lcd.text_pixels('Right button released', x=0, y=50, font='courB14')
        lcd.update()
        sleep(0.2)
def up(state): # up 이벤트 함수
    if state: # 위 버튼 눌림
        lcd.text_pixels('Up button pressed', x=0, y=50, font='courB14')
        lcd.update()
        sleep(0.2)
    else: # 위 버튼 땜
        lcd.text_pixels('Up button released', x=0, y=50, font='courB14')
        lcd.update()
        sleep(0.2)
def down(state): # down 이벤트 함수
    if state: #  아래 버튼 눌림
        lcd.text_pixels('Down button pressed', x=0, y=50, font='courB14')
        lcd.update()
        sleep(0.2)
    else: # 아래 버튼 뗌
        lcd.text_pixels('Down button released', x=0, y=50, font='courB14')
        lcd.update()
        sleep(0.2)
def enter(state): # enter 이벤트 함수
    if state:  #  엔터 버튼 눌림
        lcd.text_pixels('Enter button pressed', x=0, y=50, font='courB14')
        lcd.update()
        sleep(0.2)
    else: #  엔터 버튼 뗌
        lcd.text_pixels('Enter button released', x=0, y=50, font='courB14')
        lcd.update()
        sleep(0.2)
btn.on_left = left   #왼쪽 버튼 이벤트 함수를 left 함수로 등록
btn.on_right = right #오른쪽 버튼 이벤트 함수를 right 함수로 등록
btn.on_up = up #위쪽 버튼 이벤트 함수를 up 함수로 등록
btn.on_down = down  #아래쪽 버튼 이벤트 함수를 down 함수로 등록
btn.on_enter = enter  #엔터 버튼 이벤트 함수를 enter 함수로 등록
while True:
    btn.process() # 버튼 이벤트 상태를 감지 함
    sleep(0.01)
