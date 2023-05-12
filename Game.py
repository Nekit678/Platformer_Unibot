import pygame
import sys
from Level import Level

from PhysicsEngine import PhysicsEngine
from Player import PLAYER

FPS = 60
WIDTH = 1280
HEIGHT = 720


class Game:
    player = PLAYER
    level = Level
    level.physics_objects.append(player)

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


screen = pygame.display.set_mode((WIDTH, HEIGHT))

camera = pygame.Rect(0, 0, WIDTH, HEIGHT)

pygame.display.set_caption("Platformer ALPHA")
clock = pygame.time.Clock()

game = Game()


def update():
    #! test gravity
    PhysicsEngine.gravity(game.level.physics_objects)
    PhysicsEngine.FrForceX(game.level.physics_objects)

    #! test collide
    PhysicsEngine.map_collision(game.level.physics_map, [game.player])

    #!test effect
    PhysicsEngine.effect_collision(game.level.physics_effect_map, game.player)

    game.player.update()

    #!test
    camera.x = game.player.get_rect().x - WIDTH/(13)
    camera.y = game.player.get_rect().y-HEIGHT/(1.5)

    for i in game.level.physics_map:
        i.render(screen, camera.x, camera.y)
    for i in game.level.physics_objects:
        i.render(screen, camera.x, camera.y)


while True:
    screen.fill("black")

    clock.tick(FPS)

    game.event_control()
    game.player_control()

    update()
    pygame.display.update()
