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


#class for spaceship
class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./image/spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        #movement speed
        speed = 5

        #get pressed key
        key = pygame.key.get_pressed()
        #when left arrow pressed
        if key[pygame.K_LEFT]:
            self.rect.x -= speed
        #when right key pressed
        if key[pygame.K_RIGHT]:
            self.rect.x += speed

#sprite group
Spaceship_group = pygame.sprite.Group()

#player
spaceship = Spaceship(int(WIDTH/2), int(HEIGHT - 100))
Spaceship_group.add(spaceship)

run = True
while run:

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        

    SCREEN.blit(bg, (0,0))
    spaceship.update()
    Spaceship_group.draw(SCREEN)
 
    pygame.display.update()

pygame.display.quit()