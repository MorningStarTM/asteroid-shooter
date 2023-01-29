import pygame
import random
import math

pygame.init()

#screen variable
WIDTH = 1820
HEIGHT = 1000

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
#title
pygame.display.set_caption("Asteroid Shooter")
#icon
icon = pygame.image.load('./image/asteroid.png')
pygame.display.set_icon(icon)

#background image
bg = pygame.image.load('./image/bg.jpg')


run = True
while run:

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        

    SCREEN.blit(bg, (0,0))
 
    pygame.display.update()

pygame.display.quit()