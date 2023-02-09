import pygame
import random

#screen variable
WIDTH = 1820
HEIGHT = 1000


# Class for the asteroids
class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./image/asteroid_' + str(random.randrange(1,3)) + '.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH  - self.rect.width)
        self.rect.y = random.randrange(-150, -100)
        self.speed_y = random.randrange(2,8)
        self.speed_x = random.randrange(-5,5)
    
    def spawn_new_asteroid(self):
        self.rect.x = random.randrange(0, WIDTH  - self.rect.width)
        self.rect.y = random.randrange(-150, -100)
        self.speed_y = random.randrange(2,8)
        self.speed_x = random.randrange(-5,5)

    def boundary(self):
        if self.rect.left > WIDTH + 16 or self.rect.right < -16 or self.rect.top > WIDTH + 16:
            self.spawn_new_asteroid()

    def update(self):
        self.rect.y += self.speed_y 
        self.rect.x +=  self.speed_x
        self.boundary()
        #clock.tick(fps)
