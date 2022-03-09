from pygame import mixer
import time
mixer.init()
mixer.music.load('ex21.mp3')
mixer.music.play()
time.sleep(10)
print('Hahaha... top..')
