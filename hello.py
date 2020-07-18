#!/usr/bin/env python3
from ev3dev.ev3 import *
import os
os.system('setfont Lat15-TerminusBold14')
print('Hello World!')
Sound.speak('Hello World!').wait()