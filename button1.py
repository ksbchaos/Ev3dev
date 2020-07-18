#!/usr/bin/env python3
from ev3dev2.button import Button
from ev3dev2.display import Display
from ev3dev2.sound import Sound
btn = Button()
sound = Sound()
lcd = Display()
sound.beep()
while True:
     '''btn.wait_for_bump('left')
     lcd.text_pixels('left', x=40, y=50, font='courB24')
     lcd.update()
     sleep(1)
     sound.beep()'''
     '''btn.wait_for_pressed(['up', 'down'])
     lcd.text_pixels('up or down', x=40, y=50, font='courB24')
     lcd.update()
     sleep(1)
     sound.beep()'''
     btn.wait_for_bump('right')
     lcd.text_pixels('right', x=40, y=50, font='courB24')
     lcd.update()
     sleep(1)
     sound.beep()