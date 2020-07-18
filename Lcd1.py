#!/usr/bin/env python3
from time import sleep
import os
#os.system('setfont Lat15-TerminusBold14')
os.system('setfont Lat15-TerminusBold32x16')  # Try this larger font
print('Hello World!')
print()  # print a blank line
print('Hi Everybody!')  # comma means continue on same line
# print() has a parameter 'end' which by
# default is the new line character:
print('Hi',end=' ')    # A new line will be started after this
print('Susan!')
sleep(20)  # display the text long enough for it to be seen

