import pygame
from asteroid import Asteroid
from main import asteroid_group, all_sprite


#game functions
def generate_asteroid():
    asteroid = Asteroid()
    asteroid_group.add(asteroid)
    all_sprite.add(asteroid)    

       
