import pygame as pg
from random import randint
import numpy as np
from PIL import Image
from os.path import join, dirname

vec = pg.math.Vector2

def randvec(min_x=-10, max_x=10, min_y=-10, max_y=10):
    """ Generates a random pygame.math.Vector2 vector """
    return vec(randint(min_x, max_x), randint(min_y, max_y))

def get_pix_of_img(imgname) -> np.ndarray:
    with Image.open(imgname) as im:
        data = np.array(im)
    return data
    