# !/usr/bin/python
# -*- coding: utf-8 -*-
# Dino.py 
# Made by EarthlyEric6
# Version 1.0
# Date: 2021-09-25
# Updated 01: 2024-5-5
import sys
import os
import pygame

# PyGame Initialization
pygame.init()
pygame.mixer.init()

# Import Game Image Resource, Sound, Font
FONT=os.path.join('resource/font/Minecraft.ttf')

background_image = pygame.image.load(os.path.join('resource/background/horizon.png'))
dino_image=pygame.image.load(os.path.join('dino.png'))
dino_running_image=[pygame.image.load(os.path.join('resource/Dino/DinoRun1.png')),
                    pygame.image.load(os.path.join('resource/Dino/DinoRun2.png'))]
dino_jumping_image=pygame.image.load(os.path.join('resource/Dino/DinoJump.png'))
dino_ducking_image=[pygame.image.load(os.path.join('resource/Dino/DinoDuck1.png ')),
                    pygame.image.load(os.path.join('resource/Dino/DinoDuck2.png'))]

point_sound=pygame.mixer.Sound(os.path.join('resource/sound/point.wav'))
jump_sound=pygame.mixer.Sound(os.path.join('resource/sound/jump.wav'))

# Setup Game Settings 
width, height = 1100,600 
game_animation_speed = 10
screen = pygame.display.set_mode((width, height))
pygame.display.set_icon(pygame.image.load(os.path.join('dino.png')))
pygame.display.set_caption('Dino.py')

# Set up Game Clocks
GameClock = pygame.time.Clock()

# Background Animation
x_pos=0
y_pos=380
background_width=background_image.get_width()

# Build Dino
class Dino:
    x_pos=80
    y_pos=310
    y_pos_ducking=340
    jump_v=7
    def __init__(self):
        self.dino_duck=False
        self.dino_run=True
        self.dino_jump=False
        self.step=0  
        self.jump_vel = self.jump_v
        self.jumping=dino_jumping_image
        self.running=dino_running_image
        self.ducking=dino_ducking_image
        self.image=self.running[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos

    def run(self):
        self.image=self.running[self.step//5]
        self.dino_rect=self.image.get_rect()
        self.dino_rect.x=self.x_pos
        self.dino_rect.y=self.y_pos
        self.step+=1

    def duck(self):
        self.image=self.ducking[self.step//5]
        self.dino_rect=self.image.get_rect()
        self.dino_rect.x=self.x_pos
        self.dino_rect.y=self.y_pos
        self.step=self.step+1

    def jump(self):
        self.image = self.jumping
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.5  
        if self.jump_vel < - self.jump_v:
            self.dino_jump = False
            self.jump_vel = self.jump_v
        pygame.mixer.Sound.play(jump_sound)

    def update(self,input:pygame.key):
        if input[pygame.K_SPACE] and not self.dino_jump:
            self.dino_run=False
            self.dino_duck=False
            self.dino_jump=True
        elif input[pygame.K_c] and not self.dino_jump:
            self.dino_run=False
            self.dino_duck=True
            self.dino_jump=False
        elif not (self.dino_jump or input[pygame.K_c]):
            self.dino_run=True
            self.dino_duck=False
            self.dino_jump=False

        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()
        if self.dino_duck:
            self.duck()
        if self.step >= 10:
            self.step = 0

    def draw(self,screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
# Point System
class Point():
    x_pos=950
    y_pos=30
    def __init__(self):
        self.font=pygame.font.Font(FONT,24)
        self.point=0
        self.x=self.x_pos
        self.y=self.y_pos

    def update(self):
        global game_animation_speed
        self.point=self.point+1
        if self.point % 200 == 0:
            game_animation_speed=game_animation_speed+1
            pygame.mixer.Sound.play(point_sound)

    def draw(self,screen):
        po=self.font.render(f'{self.point}',True,(0,0,0),(255,255,255))
        screen.blit(po,(self.x,self.y))

def background_animation():
    screen.fill((255,255,255))
    global x_pos
    image_width = background_image.get_width()
    screen.blit(background_image, (x_pos, y_pos))
    screen.blit(background_image, (image_width + x_pos, y_pos))
    x_pos -= game_animation_speed  # make background moving
    if x_pos <= -image_width:
        screen.blit(background_image, (image_width + x_pos, y_pos))
        x_pos = 0

def main():
    screen.fill((255,255,255))
    dino=Dino()
    point=Point()
    while True:
    # Update Game Screen 60 times per second.
        # Background
        background_animation()

        input=pygame.key.get_pressed()
        dino.update(input)
        dino.draw(screen)
        
        point.update()
        point.draw(screen)
        GameClock.tick(60)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        

def menu():
    screen.fill((255,255,255))
    screen.blit(background_image,(0,380))
    screen.blit(dino_image,(80,310))

    font_size_big=pygame.font.Font(FONT,144)
    font_size_small=pygame.font.Font(FONT,36)
    title=font_size_big.render('Dino.py',True,(0,0,0),(255,255,255))
    text=font_size_small.render('Plese Press Space Key to Start The Game !',True,(0,0,0),(255,255,255))
    screen.blit(text,(250,310))
    screen.blit(title,(250,70))
    
    run = True
    while run:
        pygame.display.update()
        GameClock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()
                elif event.key == pygame.K_ESCAPE:
                    run = False     
menu()