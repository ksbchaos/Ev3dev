#!/usr/bin/env python3
from ev3dev2.sound import Sound
from time import sleep
sound = Sound()
sound.play_file('Hello.wav') # Hello.wav 파일 재생
sound.beep()