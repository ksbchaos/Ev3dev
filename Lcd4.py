#!/usr/bin/env python3
from ev3dev2.display import Display
from textwrap import wrap
from time import sleep
lcd = Display()
lcd.clear()
style = 'lutBS24'
string = 'What a wonderful world! Is it good day? Cool Okey'
strings = wrap(string, width=12)
y_value = 0
for i in range(len(strings)):
        lcd.text_pixels(strings[i], False, 0, y_value, font=style)
        y_value+=24
lcd.update()
lcd.update()
sleep(20) 
lcd.clear()  
