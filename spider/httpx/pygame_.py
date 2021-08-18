"""
pygame，一个制作游戏的Python库。

不仅给开发人员提供了制作游戏的图形、声音库，还可以使用内置的模块来实现复杂的游戏逻辑。

下面我们使用pygame来制作一个小型的音乐播放器。

"""
from pygame import mixer
import pygame
import sys


pygame.display.set_mode([300, 300])

music = 'my_dream.app'
mixer.init()
mixer.music.load(music)
mixer.music.play()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()