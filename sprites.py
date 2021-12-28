import pygame as pg

from settings import *
from text import draw_text

vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game, width, height):
        self.groups = [game.friendly_sprites, game.all_sprites]
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.width, self.height = width, height
        self.image = pg.Surface(vec(self.width, self.height), pg.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = vec(CENTERSCREEN)
        self.vel = vec(0, 0)
        self.pos = self.rect.center
        self.radius = self.width // 2
        self.score = 0
        self.player_alive = True

        # hitbox
        # pg.draw.rect(self.image, GREEN, [0, 0, self.width, self.height])

        # player circle
        circle_center = vec(self.width//2, self.height//2)
        pg.draw.circle(self.image, OLIVE, circle_center, self.radius)

        # magasine
        self.in_magazine = MAGAZINE_SIZE

    def update(self):
        self.boundaries()
        direction = self.move()
        self.pos += direction * MOVE_SPD * self.game.dt
        self.rect.center = self.pos

    def boundaries(self):
        # not good boundaries, still possible to get out
        if self.rect.left <= 0:
            self.pos.x = self.radius
        if self.rect.right >= WIDTH:
            self.pos.x = WIDTH - self.radius
        if self.rect.top <= 0:
            self.pos.y = self.radius
        if self.rect.bottom >= HEIGHT:
            self.pos.y = HEIGHT - self.radius

    def move(self):
        keys = pg.key.get_pressed()
        dir = vec(0, 0)
        if keys[pg.K_a]:
            dir += vec(-1, 0)
        if keys[pg.K_d]:
            dir += vec(1, 0)
        if keys[pg.K_w]:
            dir += vec(0, -1)
        if keys[pg.K_s]:
            dir += vec(0, 1)
        return dir

    def shoot(self):
        if self.in_magazine > 0:
            direction = self.pos - vec(pg.mouse.get_pos())
            Bullet(self.game, direction, self.pos)
            self.in_magazine -= 1

class Bullet(pg.sprite.Sprite):
    def __init__(self, game, direction, pos):
        self.groups = [game.projectiles, game.all_sprites]
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.width, self.height = BULLET_WIDTH, BULLET_HEIGHT
        self.img = pg.Surface(vec(self.width, self.height), pg.SRCALPHA)
        self.rect = self.img.get_rect()
        self.rect.center = vec(pos)
        self.vel = (-direction).normalize() * BULLET_SPD
        self.pos = self.rect.center

        # drawing the bullet
        pg.draw.rect(self.img, BRASS, [0, 0, self.width, self.height])

        # rotation
        self.rot = ORIGIN.angle_to(direction) + 90

    def update(self):
        self.image = pg.transform.rotate(self.img, -self.rot)
        new_rect = self.image.get_rect(center=self.img.get_rect().center)

        self.pos += self.vel * self.game.dt
        new_rect.center = self.pos
        self.rect = new_rect
        
class Enemy(pg.sprite.Sprite):
    def __init__(self, game, pos):
        self.groups = [game.enemy_sprites, game.all_sprites]
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.width, self.height = ENEMY_WIDTH, ENEMY_HEIGHT
        self.image = pg.Surface(vec(self.width, self.height), pg.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = vec(pos)
        self.vel = vec(0, 0)
        self.pos = self.rect.center
        self.radius = self.width // 2

        # hitbox
        # pg.draw.rect(self.image, GREEN, [0, 0, self.width, self.height])

        # player circle
        circle_center = vec(self.width//2, self.height//2)
        pg.draw.circle(self.image, RED, circle_center, self.radius)

    # def update(self):