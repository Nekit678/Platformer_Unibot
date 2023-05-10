import pygame
import sys

from Map import CommonBlock
from Player import Player

FPS = 60
WIDTH = 1280
HEIGHT = 720


class Game:
    img_a = pygame.Surface((20, 20))
    img_a.fill("blue")
    player = Player(img_a, 100, 100, 1)

    @staticmethod
    def player_control():
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            Game.player.set_speed_x(-3)
        if keys[pygame.K_RIGHT]:
            Game.player.set_speed_x(3)
        if keys[pygame.K_UP]:
            Game.player.jump()

    @staticmethod
    def event_control():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wall kickers ALPHA")
clock = pygame.time.Clock()

game = Game()


img_b = pygame.Surface((32, 32))
img_b.fill("red")

b = [CommonBlock(100, 650), CommonBlock(150, 650), CommonBlock(200, 650)]


def update():
    #! test gravity
    game.player.gravity(0.35)
    game.player.FrForceX()

    #! test collide
    game.player.check_collision(b)

    game.player.update()

    for i in b:
        i.render(screen)
    game.player.render(screen)


while True:
    screen.fill("black")

    clock.tick(FPS)

    game.event_control()
    game.player_control()

    update()
    pygame.display.update()
