import pygame
from asteroid import Asteroid


class GameFunction:
    def generate_asteroid(grp, all_sprite):
        asteroid = Asteroid()
        grp.add(asteroid)
        all_sprite.add(asteroid)  
