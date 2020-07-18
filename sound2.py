#!/usr/bin/env python3
from ev3dev2.sound import Sound
sound = Sound()
sound.beep() # 비프 음 재생#!/usr/bin/env python3
from ev3dev2.sound import Sound
sound = Sound()
sound.play_tone(700, 1) #700Hz 주파수 1초간 재생