# !/usr/bin/python
# -*- coding: utf-8 -*-
# Dino.py 
# Made by EarthlyEric6
import sys
import os
import pygame
import object


# PyGame Init
pygame.init()

# Import Game Resource
background_image = pygame.image.load(os.path.join('resource/background/horizon.png'))

# Setup Game Settings
width, height = 1100,600
game_animation_speed = 10
screen = pygame.display.set_mode((width, height))
pygame.display.set_icon(pygame.image.load(os.path.join('dino.png')))
pygame.display.set_caption('Dino.py')

# Game Clock
GameClock = pygame.time.Clock()

# Background Animation
x_pos=0
y_pos=380
background_width=background_image.get_width()

# Dino
class Dino(pygame.sprite.Sprite):
    x_pos = 80
    y_pos = 310
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join("resource/Dino/DinoStart.png"))
        self.rect = self.image.get_rect()

def background_animation():
    global x_pos
    screen.fill((255,255,255))
    screen.blit(background_image,(x_pos,y_pos))
    screen.blit(background_image,(background_width+x_pos,y_pos))
    if x_pos<=-width:
        screen.blit(background_image,(background_width+x_pos,y_pos))
        x_pos=0
    x_pos-=game_animation_speed

def main():
    while True:
        # Update Game Screen 60 times per second.
        GameClock.tick(60) 
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()

def menu():
    # Menu Event Loop
    screen.fill((255,255,255))
    screen.blit(background_image,(0,380))
    screen.blit(pygame.image.load(os.path.join('dino.png')),(80,310))

    font=pygame.font.Font(os.path.join('resource/font/Minecraft.ttf'),144)
    screen.blit(font.render('DINO.PY', 0, (0,0,0), (255,255,255)),(250,70))
    while True:
        GameClock.tick(60)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()



menu()