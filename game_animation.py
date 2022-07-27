from main import screen,background_image,game_animation_speed
import pygame
pygame.init()

def background_animation():
    x_pos,y_pos = 0
    image_w = 2404
    screen.blit(background_image,(x_pos,y_pos))
    screen.blit(background_animation, (image_w + x_pos, y_pos))
    if x_pos <= -image_w:
        screen.blit(background_image, (image_w + x_pos, y_pos))
        x_pos = 0
    x_pos -= game_animation_speed

