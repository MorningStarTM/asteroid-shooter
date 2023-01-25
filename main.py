import pygame
import random
import math

pygame.init()

#screen variable
WIDTH = 1500
HEIGHT = 800

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
#title
pygame.display.set_caption("Asteroid Shooter")
#icon
icon = pygame.image.load('./image/asteroid.png')
pygame.display.set_icon(icon)

#background image
bg = pygame.image.load('./image/bg.jpg')




"""     Player  """
#player image load
player_img = pygame.image.load('./image/spaceship.png')

#position of player
player_x = 700
player_y = 700
playerX_change = 0

#draw the player on screen
def player(x, y):
    SCREEN.blit(player_img, (x, y))


"""     Asteroid    """
#asteroid image load
asteroidImg = pygame.image.load('./image/asteroid_1.png')
#random position of asteroid
asteroidX = random.randint(0,1436)
asteroidY = random.randint(50, 150)
#velocity of asteroid
asteroidVel = 0.3

#draw the asteroid on screen
def asteroid(x, y):
    SCREEN.blit(asteroidImg, (asteroidX, asteroidY))


"""     Bullet      """
#bullet image load
bulletImg = pygame.image.load('./image/bullet.png')
#position of bullet
bulletX = 0
bulletY = 700
#velocity of bullet
asteroidVel = 0.3
bullet_state = "active"
bulletX_change = 0
bulletY_change = 2

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    SCREEN.blit(bulletImg, (x+24, y+10))


run = True
while run:

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        #when key pressed
        if event.type == pygame.KEYDOWN:
            #press left arrow key
            if event.key == pygame.K_LEFT:
                #decrease the value of position of player
                playerX_change = -0.5
            #press right arrow key
            if event.key == pygame.K_RIGHT:
                #increase the value of position of player
                playerX_change = 0.5
            if event.key == pygame.K_SPACE:
                bulletX = player_x
                fire_bullet(bulletX, bulletY)
                
        #when key released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key ==  pygame.K_RIGHT:
                playerX_change = 0

    player_x += playerX_change

    #set up the player into the screen when moving outside of screen
    if player_x <= 0:
        player_x = 0
    #player size 64x64, 1500-64=1436
    if player_x >= 1436:
        player_x = 1436

    #bullet movement
    if bulletY <= 0:
        bulletY = 700
        bullet_state = "active" 
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
        print(bullet_state)


    SCREEN.blit(bg, (0,0))
    SCREEN.blit(bulletImg, (bulletX+24, bulletY+10))
    player(player_x, player_y)
    asteroid(asteroidX, asteroidY)
    #move y direction
    asteroidY += asteroidVel
    pygame.display.update()
