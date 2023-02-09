import pygame
import random

#screen variable
WIDTH = 1820
HEIGHT = 1000


class MissileAmmo(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./image/torpedo.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH  - self.rect.width)
        self.rect.y = random.randrange(-150, -100)
        self.speed_y = random.randint(1,8)


    def update(self):
        self.rect.y += self.speed_y
