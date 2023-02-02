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
asteroid_img =pygame.image.load('./image/asteroid_1.png')

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
        speed = 8
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
        
        #when ctrl pressed missile will be released
        if key[pygame.K_LCTRL] and time_now - self.last_shot > cooldown:
            missile = Missile(self.rect.centerx, self.rect.top)
            Missile_group.add(missile)
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


#class for missile
class Missile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./image/missile.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.rect.y -= 5
        if self.rect.bottom < 200:
            self.kill()

# Class for the asteroids
class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = asteroid_img
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
    
    

#game functions
def generate_asteroid():
    asteroid = Asteroid()
    asteroid_group.add(asteroid)
    all_sprite.add(asteroid)    

       



#sprite group
Spaceship_group = pygame.sprite.Group()
Bullet_group = pygame.sprite.Group()
Missile_group = pygame.sprite.Group()

all_sprite = pygame.sprite.Group()
asteroid_group = pygame.sprite.Group()


#player
spaceship = Spaceship(int(WIDTH/2), int(HEIGHT - 100), 5)
Spaceship_group.add(spaceship)

time_now = pygame.time.get_ticks()
time_released = 0

for i in range(9):        
    generate_asteroid()

run = True
while run:

    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        
    #screen background
    SCREEN.blit(bg, (0,0))
    
    #bullet movement
    Bullet_group.draw(SCREEN)

    #missile movement
    Missile_group.draw(SCREEN)

    #draw the player
    Spaceship_group.draw(SCREEN)

    #draw the asteroid
    asteroid_group.draw(SCREEN)

    #player movement
    spaceship.update()

    #bullet movement
    Bullet_group.update()

    #missile movement
    Missile_group.update()

    #asteroid movement
    asteroid_group.update()

    #collision detect
    asteroid_collision = pygame.sprite.spritecollide(spaceship, asteroid_group, False)
    if asteroid_collision:
        run = False
    
    bullet_collision = pygame.sprite.groupcollide(Bullet_group, asteroid_group, True, True)
    if bullet_collision:
        generate_asteroid()
    pygame.display.update()

pygame.display.quit()