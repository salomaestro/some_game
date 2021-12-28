import pygame as pg
from settings import *

class Magazine_on_ground(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = [game.pickable, game.all_sprites]
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        self.image = pg.Surface(vec(10, 27), pg.SRCALPHA)
        self.rect = self.image.get_rect(center = vec(700, 400))
        self.image.fill(YELLOW)
        self.image = pg.transform.rotate(self.image, 20)

    def update(self):
        pass