import pygame as pg
import sys
from os import path
from sprites import *
from settings import *

class Game:
	def __init__(self):
		self.screen = pg.display.set_mode((WIDTH, HEIGHT))
		# pg.display.set_caption(TITLE)
		self.clock = pg.time.Clock()
		pg.key.set_repeat(500, 100)
		self.load_data()

	def load_data(self):
		game_folder = path.dirname(__file__)
		img_folder = path.join(game_folder, 'img')
		self.img = pg.image.load(path.join(img_folder, 'name.png')).convert_alpha()

	def new(self):
		self.start_time = pg.time.get_ticks()
		self.all_sprites = pg.sprite.Group()

		#self.multiple_obj = [obj(self) for i in range(NUMBER_OF_OBJ)]

	def run(self):
		#gameloop - self.playing = False => game over
		self.playing = True
		while self.playing:
			self.dt = self.clock.tick(FPS) / 1000
			self.events()
			self.start = pg.time.get_ticks()
			self.update()
			self.draw()

	def quit(self):
		pg.quit()
		sys.exit()

	def update(self):
        self.all_sprites.update()

	def draw(self):
		# show FPS
		pg.display.set_caption('{:.2f}'.format(self.clock.get_fps()))

		self.screen.fill(50)
		self.all_sprites.draw(self.screen)

		pg.display.flip()

	def events(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				self.quit()
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					self.quit()

g = Game()
while True:
	g.new()
	g.run()
