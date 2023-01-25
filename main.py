import pygame
import math

pygame.init()

#screen variable
WIDTH = 1500
HEIGHT = 750

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
#title
pygame.display.set_caption("Asteroid Shooter")
#icon
icon = pygame.image.load('./image/asteroid.png')
pygame.display.set_icon(icon)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
