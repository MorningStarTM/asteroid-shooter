import pygame
from asteroid import Asteroid, BigAsteroid


class GameFunction:
    def generate_asteroid(grp, all_sprite):
        asteroid = Asteroid()
        grp.add(asteroid)
        all_sprite.add(asteroid)  

    def generate_bigAsteroid(grp, all_sprite, Explosion_group, SCREEN, Bullet_group, Missile_group, Nuclear_group):
        big_asteroid = BigAsteroid(10, Explosion_group, SCREEN, grp, Bullet_group, Missile_group, Nuclear_group)
        grp.add(big_asteroid)
        all_sprite.add(big_asteroid)