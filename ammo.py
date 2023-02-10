import pygame
import random

#screen variable
WIDTH = 1820
HEIGHT = 1000


# Class for the asteroids
class MissileAmmo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./image/missile_pack.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH  - self.rect.width)
        self.rect.y = random.randrange(-150, -100)
        self.speed_y = random.randrange(5,10)
        self.speed_x = random.randrange(-5,5)
    

    def update(self):
        self.rect.y += self.speed_y    

    def sprite_groups():
        missile_ammo_group = pygame.sprite.Group()
        return missile_ammo_group
    