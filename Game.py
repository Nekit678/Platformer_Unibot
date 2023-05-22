import pygame
import sys
from Level import Level

from PhysicsEngine import PhysicsEngine


FPS = 60
WIDTH = 1280
HEIGHT = 720


class Game:
    gameover = False
    complete = False
    show_lvl_menu = False

    @staticmethod
    def player_control():
        Level.get_player().reset_directions()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            Level.get_player().set_direction("LEFT")
        if keys[pygame.K_RIGHT]:
            Level.get_player().set_direction("RIGHT")
        if keys[pygame.K_UP]:
            Level.get_player().set_direction("UP")

    @staticmethod
    def event_control():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    @staticmethod
    def check_live_player():
        if Level.get_player().get_health() <= 0:
            Game.gameover = True

    @staticmethod
    def check_live_enemies():
        for en in Level.get_enemies():
            if en.get_health() <= 0:
                Level.get_enemies().remove(en)

    @staticmethod
    def update_physics_engine():
        #! test gravity
        PhysicsEngine.gravity([Level.get_player(), *Level.get_enemies()])
        PhysicsEngine.FrForceX(
            [*Level.get_physics_map(), *Level.get_physics_effect_map()], [Level.get_player()])

        #! test collide
        PhysicsEngine.map_collision(
            [*Level.get_physics_map(), *Level.get_physics_effect_map()], [Level.get_player(), *Level.get_enemies()])

        #!test effect
        for item in Level.get_physics_effect_map():
            if PhysicsEngine.check_bottom_collision(item, Level.get_player()):
                item.activate_effect(Level.get_player())

        #!test collide player-enemy
        for en in Level.get_enemies():
            if PhysicsEngine.check_rect_collision(en, Level.get_player()):
                if PhysicsEngine.check_bottom_collision(en, Level.get_player()) and Level.get_player().get_speed_y() > 0:
                    en.damage(1)
                    Level.get_player().set_speed_y(-10)
                else:
                    Level.get_player().kill()

    @staticmethod
    def check_complete_level():
        for item in Level.get_complete_blocks():
            if PhysicsEngine.check_bottom_collision(item, Level.get_player()):
                Game.complete = True

    @staticmethod
    def check_edge():
        for item in Level.get_edge_blocks():
            if PhysicsEngine.check_rect_collision(item, Level.get_player()):
                Level.get_player().kill()
            for en in Level.get_enemies():
                if PhysicsEngine.check_rect_collision(item, en):
                    en.kill()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
camera = pygame.Rect(0, 0, WIDTH, HEIGHT)

pygame.display.set_caption("Platformer ALPHA")
clock = pygame.time.Clock()


def update_game():
    Level.get_player().move()
    for en in Level.get_enemies():
        en.move()

    Game.update_physics_engine()
    Game.check_live_player()
    Game.check_live_enemies()

    for item in [Level.get_player(), *Level.get_enemies()]:
        item.update()

    #!test
    camera.x = Level.get_player().get_rect().x - WIDTH/(13)
    camera.y = Level.get_player().get_rect().y-HEIGHT/(1.5)

    for i in [*Level.get_physics_map(), *Level.get_physics_effect_map(), Level.get_player(), *Level.get_enemies()]:
        i.render(screen, camera.x, camera.y)

    if Game.gameover:  # !!!!!!
        Game.show_lvl_menu = True


while True:
    screen.fill("black")
    clock.tick(FPS)

    Game.event_control()

    if Game.show_lvl_menu:
        pass
    else:

        Game.player_control()

        update_game()

    pygame.display.update()
