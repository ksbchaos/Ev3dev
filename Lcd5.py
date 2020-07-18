#!/usr/bin/env python3
from ev3dev2.display import Display
from time import sleep
lcd = Display()
# Draw a rectangle where the top left corner is at (x1, y1)
# and the bottom right corner is at (x2, y2). 
lcd.rectangle(False, x1=10, y1=10, x2=170, y2=120, fill_color='grey')
# Draw a circle of ‘radius’ centered at (x, y)
lcd.circle(clear_screen=False, x=89, y=64, radius=50, fill_color='white')
# Draw a line from (x1, y1) to (x2, y2)
lcd.line(False, x1=0, y1=0, x2=177, y2=127, line_color='white', width=4)
# Draw a single pixel at (x, y)
lcd.point(False, x=65, y=45, point_color='white')
lcd.update()
sleep(10)