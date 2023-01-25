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


bg = pygame.image.load('./image/bg.jpg')

""" Player  """
#player image load
player_img = pygame.image.load('./image/spaceship.png')
#position of player
player_x = 700
player_y = 650
playerX_change = 0
def player(x, y):
    SCREEN.blit(player_img, (x, y))


run = True
while run:

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN:
            #press left arrow key
            if event.key == pygame.K_LEFT:
                #decrease the value of position of player
                playerX_change = -0.4
            #press right arrow key
            if event.key == pygame.K_RIGHT:
                #increase the value of position of player
                playerX_change = 0.4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key ==  pygame.K_RIGHT:
                playerX_change = 0
    player_x += playerX_change
    SCREEN.blit(bg, (0,0))
    player(player_x, player_y)
    pygame.display.update()
