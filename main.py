# Dino.py 
# Made by EarthlyEric6
import sys
import os
import pygame
from pygame.locals import QUIT
import object

# PyGame Init
pygame.init()

width, height = 640, 360
screen = pygame.display.set_mode((width, height))
pygame.display.set_icon(pygame.image.load(os.path.join("dino.png")))
pygame.display.set_caption("Dino.py")

GameClock = pygame.time.Clock() 

# Game Event Loop
while True:
    # Update Game Screen 60 times per second.
    GameClock.tick(60) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update() 
   