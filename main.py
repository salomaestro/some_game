import pygame as pg
import sys
import os
from sprites import *
from static_objects import *
from settings import *
from text import *
from util import *

class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_CROSSHAIR))

    def new(self):
        self.start_time = pg.time.get_ticks()
        self.all_sprites = pg.sprite.Group()
        self.friendly_sprites = pg.sprite.Group()
        self.projectiles = pg.sprite.Group()
        self.pickable = pg.sprite.Group()
        self.enemy_sprites = pg.sprite.Group()

        self.p1 = Player(self, 30, 30)
        mag1 = Magazine_on_ground(self)

        self.enemy = [Enemy(self, randvec(0, WIDTH, 0, HEIGHT)) for _ in range(3)]

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()
            self.collide()
            if len(self.enemy_sprites) < 1:
                [Enemy(self, randvec(0, WIDTH, 0, HEIGHT)) for _ in range(randint(1, 4))]

    def collide(self):
        self.item_interaction()
        self.enemy_hit()
        self.player_hit()

    def player_hit(self):
        collision = pg.sprite.groupcollide(self.friendly_sprites, self.enemy_sprites, dokilla=True, dokillb=False)
        if collision:
            self.p1.player_alive = False

    def item_interaction(self):
        collision = pg.sprite.spritecollide(self.p1, self.pickable, True)
        if collision:
            for item in collision:
                self.p1.in_magazine += 30

    def enemy_hit(self):
        collision = pg.sprite.groupcollide(self.projectiles, self.enemy_sprites, dokilla=True, dokillb=True)

        if collision:
            for enemy in collision:
                self.p1.score += 1

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        self.all_sprites.update()
        self.pickable.update()
    
    def draw(self):
        # show FPS
        pg.display.set_caption('{:.2f}'.format(self.clock.get_fps()))

        if self.p1.player_alive:
            self.screen.fill((0, 2, 46))

            self.all_sprites.draw(self.screen)

            self.text()
        else:
            self.screen.fill(BLACK)

            self.end_screen()

        pg.display.flip()

    def text(self):
        draw_text(self.screen, f"{self.p1.in_magazine}", 32, WIDTH * .05, HEIGHT * .05, WHITE, True)
        draw_text(self.screen, f"Score: {self.p1.score}", 28, WIDTH * .05, HEIGHT * .1, WHITE, True)

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()

            if event.type == pg.MOUSEBUTTONDOWN and self.p1.player_alive:
                self.p1.shoot()

    def end_screen(self):
        draw_text(self.screen, "Game Over", 76, WIDTH // 2, HEIGHT * 0.45, RED, True)
        draw_text(self.screen, f"Score: {self.p1.score}", 46, WIDTH // 2, HEIGHT * 0.6, RED, True)

g = Game()
while True:
    g.new()
    g.run()
