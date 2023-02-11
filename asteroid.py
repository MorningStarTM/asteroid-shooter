import pygame
import random
from animation import Explosion

#screen variable
WIDTH = 1820
HEIGHT = 1000

#green color
green = (0,255,0)
red = (255,0,0)

#score
score = 0

def pass_score():
    return score

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

    def sprite_groups():
        Asteroid_group = pygame.sprite.Group()
        return Asteroid_group
    




#class for big asteroid
class BigAsteroid(pygame.sprite.Sprite):
    def __init__(self, health, Explosion_group, SCREEN, BigAsteroid_group, Bullet_group, Missile_group, Nuclear_group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./image/asteroid_4.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH  - self.rect.width)
        self.rect.y = random.randrange(-150, -100)
        self.speed_y = random.randrange(1,3)
        #self.speed_x = random.randrange(-5,5)
        self.health_at_begining = health
        self.health_remaining = health
        self.time_astroid = 0
        self.Explosion_group = Explosion_group
        self.BigAsteroid_group = BigAsteroid_group
        self.SCREEN = SCREEN
        self.Nuclear_group = Nuclear_group
        self.Bullet_group = Bullet_group
        self.Missile_group = Missile_group
    
    def update(self):
        self.rect.y += self.speed_y 
        #self.rect.x +=  self.speed_x

        #draw the health bar to player
        pygame.draw.rect(self.SCREEN, red, (self.rect.x, (self.rect.top - 15), self.rect.width, 15))
        if self.health_remaining > 0:
            pygame.draw.rect(self.SCREEN, green, (self.rect.x, (self.rect.top - 15), int(self.rect.width * (self.health_remaining / self.health_at_begining)), 15))

        if pygame.sprite.spritecollide(self, self.Bullet_group, True):
            self.health_remaining -= 0.1
        elif pygame.sprite.spritecollide(self, self.Missile_group, True):
            self.health_remaining -= 0.5
        elif pygame.sprite.spritecollide(self, self.Nuclear_group, True):
            self.health_remaining -= 10
        
        if self.health_remaining <= 0:
            self.kill()

            #explosion = Explosion(self.rect.centerx, self.rect.centery, None)
            #self.Explosion_group.add(explosion)
            
            
        
        """elif self.rect.centery > 1200:
            if self.time_astroid % 10 == 0:
                bastroid = BigAsteroid(100)
                BigAsteroid_group.add(bastroid)"""
        
    def sprite_group():
        BigAsteroid_group = pygame.sprite.Group()
        return BigAsteroid_group
        
        
        #clock.tick(fps)      

