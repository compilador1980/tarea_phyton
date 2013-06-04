import pygame
import os
import sys
import pygame.mixer
import pygame.cdrom

from pygame import time as pytime  
from pygame.locals import *  
      
pygame.mixer.init()
reload(sys)
sys.setdefaultencoding("utf-8")

pygame.mixer.music.load(os.path.join('C:\Users\Public\Music\Sample Music\\Kalimba.mp3'))  
pygame.mixer.music.set_volume(1.0)  
pygame.mixer.music.play()  
exit(0)  


