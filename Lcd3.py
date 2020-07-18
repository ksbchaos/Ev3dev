#!/usr/bin/env python3
from ev3dev2.display import Display
from ev3dev2.sound import Sound
from time import sleep
lcd = Display()
sound = Sound()
# Try each of these different sets:
style = 'helvB'
#style = 'courB'
#style = 'lutBS'
y_value = 0
text = 'Hello World!'
for height in [10, 14, 18, 24]:
    lcd.text_pixels(text, False, 0, y_value, font=style+str(height))
    y_value += height+5   # short for  y_value = y_value+height+1
lcd.update()
sound.beep()
sleep(20) 
lcd.clear()  
    
