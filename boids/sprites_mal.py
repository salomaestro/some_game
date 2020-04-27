import pygame as pg
from settings import *
from random import randint, uniform, choice
vec = pg.math.Vector2

class Planet(pg.sprite.Sprite):
	def __init__(self, game):
		self.groups = game.all_sprites
		pg.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		self.choice = choice(self.game.img)
		self.image = self.choice
		self.rect = self.image.get_rect()

	def update(self, other_list):
		pass
