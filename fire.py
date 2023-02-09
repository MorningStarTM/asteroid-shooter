#class for nuclear
import pygame
import random
import time
from animation import Explosion
from game_funtion import GameFunction
from asteroid import Asteroid


class Nuclear(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./image/nuclear.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.rect.y -= 5
        if self.rect.bottom < 0:
            self.kill()

    def sprite_groups():
        Nuclear_group = pygame.sprite.Group()
        return Nuclear_group




#class for missile
class Missile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./image/missile.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.rect.y -= 5
        if self.rect.bottom < 0:
            self.kill()  

    def sprite_groups():
        Missile_group = pygame.sprite.Group()
        return Missile_group 



#class for Bullet
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, all_sprite, asteroid_groups, explosion_group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./image/bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.all_sprite = all_sprite
        self.asteroid_groups = asteroid_groups
        self.explosion_group = explosion_group

    def update(self):
        self.rect.y -= 5
        if pygame.sprite.spritecollide(self, self.asteroid_groups, True):
            self.kill()
            GameFunction.generate_asteroid(self.asteroid_groups, self.all_sprite)
            explosion = Explosion(self.rect.centerx, self.rect.centery, 2)
            self.explosion_group.add(explosion)

    def sprite_groups():
        Bullet_group = pygame.sprite.Group()
        return Bullet_group