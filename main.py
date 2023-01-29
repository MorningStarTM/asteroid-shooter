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

clock = pygame.time.Clock()

#background image
bg = pygame.image.load('./image/bg.jpg')

#green color
green = (0,255,0)
red = (255,0,0)


#class for spaceship
class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y, health):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./image/spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.health_at_begining = health
        self.health_remaining = health
        self.last_shot = pygame.time.get_ticks()

    def update(self):
        #movement speed
        speed = 5
        #cooldown time
        cooldown = 100 #milliseconds

        #get pressed key
        key = pygame.key.get_pressed()
        #when left arrow pressed
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= speed
        #when right key pressed 
        if key[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += speed

        #recored current time
        time_now = pygame.time.get_ticks()
        #when space bar pressed, shoot
        if key[pygame.K_SPACE] and time_now - self.last_shot > cooldown:
            bullet = Bullet(self.rect.centerx, self.rect.top)
            Bullet_group.add(bullet)
            self.last_shot = time_now

        #draw the health bar to player
        pygame.draw.rect(SCREEN, red, (self.rect.x, (self.rect.bottom + 10), self.rect.width, 15))
        if self.health_remaining > 0:
            pygame.draw.rect(SCREEN, green, (self.rect.x, (self.rect.bottom + 10), int(self.rect.width * (self.health_remaining / self.health_at_begining)), 15))



#class for spaceship
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./image/bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.rect.y -= 5
        if self.rect.bottom < 200:
            self.kill()




#class for Asteroid
class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./image/asteroid_" + str(random.randint(1,3)) + ".png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.rect.y += 1
        #clock.tick(60)
        



#sprite group
Spaceship_group = pygame.sprite.Group()
Bullet_group = pygame.sprite.Group()
Asteroid_group = pygame.sprite.Group()

#player
spaceship = Spaceship(int(WIDTH/2), int(HEIGHT - 100), 5)
Spaceship_group.add(spaceship)

#Asteroid
for i in range(5):
    astroid = Asteroid(random.randint(32,768), 10)
    Asteroid_group.add(astroid)


run = True
while run:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        
    #screen background
    SCREEN.blit(bg, (0,0))
    
    #bullet movement
    Bullet_group.draw(SCREEN)

    #draw the player
    Spaceship_group.draw(SCREEN)

    #draw the asteroid
    Asteroid_group.draw(SCREEN)

    #player movement
    spaceship.update()

    #bullet movement
    Bullet_group.update()

    #asteroid movement
    Asteroid_group.update()
 
    pygame.display.update()

pygame.display.quit()