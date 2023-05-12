import pygame
import sys

from Map import CommonBlock
from PhysicsEngine import PhysicsEngine
from Player import Player

FPS = 60
WIDTH = 1280
HEIGHT = 720


class Game:
    img_a = pygame.Surface((20, 20))
    img_a.fill("blue")

    player = Player(img_a, 100, 100, 1)

    enemies = []
    physics_objects = [player, *enemies]
    physics_map = [CommonBlock(100, 600), CommonBlock(132, 600), CommonBlock(164, 600),
                   CommonBlock(164, 568), CommonBlock(
                       196, 568), CommonBlock(228, 568),
                   CommonBlock(260, 568), CommonBlock(
                       196, 536), CommonBlock(196, 504),
                   CommonBlock(100, 500), CommonBlock(132, 500)]

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
pygame.display.set_caption("Platformer ALPHA")
clock = pygame.time.Clock()

game = Game()

def update():
    #! test gravity
    PhysicsEngine.gravity([game.player])
    PhysicsEngine.FrForceX([game.player])

    #! test collide
    PhysicsEngine.map_collision(game.physics_map, [game.player])

    game.player.update()

    for i in game.physics_map:
        i.render(screen)
    game.player.render(screen)


while True:
    screen.fill("black")

    clock.tick(FPS)

    game.event_control()
    game.player_control()

    update()
    pygame.display.update()
