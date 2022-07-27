# !/usr/bin/python
# -*- coding: utf-8 -*-
# Dino.py 
# Made by EarthlyEric6
import sys
import os
import pygame
import game_animation
from pygame.locals import QUIT
import object

# PyGame Init
pygame.init()

# Import Game Resource
background_image = pygame.image.load(os.path.join('resource/background/horizon.png'))

# Setup Game Settings
width, height = 1280,720
game_animation_speed = 20
screen = pygame.display.set_mode((width, height))
pygame.display.set_icon(pygame.image.load(os.path.join('dino.png')))
pygame.display.set_caption('Dino.py')
screen.fill((255,255,255))
GameClock = pygame.time.Clock()


# Game Event Loop
while True:
    # Update Game Screen 60 times per second.
    GameClock.tick(60) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    game_animation.background_animation()
    pygame.display.update()
   