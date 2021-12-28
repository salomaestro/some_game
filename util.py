import pygame as pg
from random import randint

vec = pg.math.Vector2

def randvec(min_x=-10, max_x=10, min_y=-10, max_y=10):
    """ Generates a random pygame.math.Vector2 vector """
    return vec(randint(min_x, max_x), randint(min_y, max_y))
