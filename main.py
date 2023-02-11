import pygame
import random
import math
import time
from fire import Nuclear, Missile, Bullet, display_score
from asteroid import Asteroid, BigAsteroid
from animation import Explosion
from game_funtion import GameFunction
from ammo import MissileAmmo, NuclearAmmo

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

#font
my_font = pygame.font.Font("./font/ostrich-regular.ttf", 90)
ammo_font = pygame.font.Font("./font/ostrich-regular.ttf", 50)
#green color
green = (0,255,0)
red = (255,0,0)

#score
score = display_score()

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
        self.Mammo = []
        self.Nammo = []
    
    def ammo(self):
        return len(self.Mammo), len(self.Nammo)

    def update(self):
        #movement speed
        speed = 8
        #cooldown time
        cooldown = 100 #milliseconds

        #mask
        self.mask = pygame.mask.from_surface(self.image)

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
            bullet = Bullet(self.rect.centerx, self.rect.top, all_sprite, asteroid_group, Explosion_group)
            Bullet_group.add(bullet)
            self.last_shot = time_now
        
        #when ctrl pressed missile will be released
        if key[pygame.K_LCTRL] and time_now - self.last_shot > cooldown:
            if len(self.Mammo) != 0:
                missile = Missile(self.rect.centerx, self.rect.top, asteroid_group, Explosion_group)
                Missile_group.add(missile)
                self.last_shot = time_now
                self.Mammo.pop()
        
        #when ctrl pressed missile will be released
        if key[pygame.K_q] and time_now - self.last_shot > cooldown:
            if len(self.Nammo) != 0:
                nuclear = Nuclear(self.rect.centerx, self.rect.top, asteroid_group, Explosion_group)
                Nuclear_group.add(nuclear)
                self.last_shot = time_now
                self.Nammo.pop()

        #check collision of missile ammo
        if pygame.sprite.spritecollide(self, missileAmmo_group, True):
            self.Mammo.append(1)
        
        #check collsion of nuclear ammo
        if pygame.sprite.spritecollide(self, nuclearAmmo_group, True):
            self.Nammo.append(1)



        #draw the health bar to player
        pygame.draw.rect(SCREEN, red, (self.rect.x, (self.rect.bottom + 10), self.rect.width, 15))
        if self.health_remaining > 0:
            pygame.draw.rect(SCREEN, green, (self.rect.x, (self.rect.bottom + 10), int(self.rect.width * (self.health_remaining / self.health_at_begining)), 15))



#sprite group
Spaceship_group = pygame.sprite.Group()
Bullet_group = Bullet.sprite_groups()
Missile_group = Missile.sprite_groups()
Nuclear_group = Nuclear.sprite_groups()
Explosion_group = Explosion.sprite_groups()
missileAmmo_group = MissileAmmo.sprite_groups()
nuclearAmmo_group = NuclearAmmo.sprite_groups()


all_sprite = pygame.sprite.Group()
asteroid_group = Asteroid.sprite_groups()
BigAsteroid_group = BigAsteroid.sprite_group()



#player
spaceship = Spaceship(int(WIDTH/2), int(HEIGHT - 100), 5)
Spaceship_group.add(spaceship)

#get the starting time of asteroid
start_time_big_asteroid = time.time()

last_destroyed_time = time.time()
last_catridge_time = time.time()
last_nuclear_catridge_time = time.time()

#generate asteroid
for i in range(9):
    GameFunction.generate_asteroid(asteroid_group,all_sprite)


#function for display the score
def display_score_on_screen(score):
    text = my_font.render(f'Score: {str(score)}', True, (211,211,211))
    SCREEN.blit(text, [10, 10])

def display_ammo():
    missile_count, nuclear_count = Spaceship.ammo(spaceship)
    missile_info = ammo_font.render(f'Missile-{str(missile_count)}', True, 'gray')
    nuclear_info = ammo_font.render(f'Nuclear-{str(nuclear_count)}', True, 'gray')
    SCREEN.blit(missile_info, [10, 950])
    SCREEN.blit(nuclear_info, [10, 900])

#score
score = 0

run = True
while run:
    


    clock.tick(60)
    
    current_time = time.time()
    time_since_last_destroyed = current_time - last_destroyed_time
    time_since_last_catridge = current_time - last_catridge_time
    time_last_nuclear_catridge = current_time - last_nuclear_catridge_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        
    #screen background
    SCREEN.blit(bg, (0,0))
    
    #draw bullet
    Bullet_group.draw(SCREEN)

    #draw missile
    Missile_group.draw(SCREEN)

    #draw nuclear missile 
    Nuclear_group.draw(SCREEN)

    #draw the player
    Spaceship_group.draw(SCREEN)

    #draw the asteroid
    asteroid_group.draw(SCREEN)

    #draw the big asteroid
    BigAsteroid_group.draw(SCREEN)      
        
    #draw the explosion
    Explosion_group.draw(SCREEN)

    #draw Ammo
    missileAmmo_group.draw(SCREEN)
    nuclearAmmo_group.draw(SCREEN)


    #Ammo movement
    missileAmmo_group.update()
    nuclearAmmo_group.update()

    #player movement
    spaceship.update()

    #bullet movement
    Bullet_group.update()

    #missile movement
    Missile_group.update()

    #nuclear missile movement
    Nuclear_group.update()

    #asteroid movement
    asteroid_group.update()

    #big asteroid movement
    BigAsteroid_group.update()  

    #explosion movement
    Explosion_group.update()

    #collision detect
    asteroid_collision = pygame.sprite.spritecollide(spaceship, asteroid_group, False, pygame.sprite.collide_mask)
    if asteroid_collision:
        run = False
    
    """bullet_collision = pygame.sprite.groupcollide(Bullet_group, asteroid_group, True, True, pygame.sprite.collide_mask)
    if bullet_collision:
        explosion = Explosion(asteroid_group.)
        generate_asteroid()"""
    
    #generate missile ammo
    if int(time_since_last_catridge) % 15 == 0 and int(time_since_last_catridge) != 0:
        missileAmmo = MissileAmmo()
        missileAmmo_group.add(missileAmmo)
        all_sprite.add(missileAmmo)
        last_catridge_time = current_time

    #generate nuclear ammo
    if (int(time_last_nuclear_catridge)) % 2 == 0 and int(time_last_nuclear_catridge) != 0:
        nuclearAmmo = NuclearAmmo()
        nuclearAmmo_group.add(nuclearAmmo)
        all_sprite.add(nuclearAmmo)
        last_nuclear_catridge_time = current_time
    

    if int(time_since_last_destroyed) % 20 == 0 and int(time_since_last_destroyed) != 0:
        #generate the big asteroid at particular time
        GameFunction.generate_bigAsteroid(BigAsteroid_group, all_sprite, Explosion_group, SCREEN, Bullet_group, Missile_group, Nuclear_group)

        # Update the last_destroyed_time with the current time
        last_destroyed_time = current_time
    

    score = display_score()
    display_score_on_screen(score)

    display_ammo()
    pygame.display.update()

pygame.display.quit()