import pygame

from Level_Module.Level import Level
from PhysicsEngine_Module.PhysicsEngine import PhysicsEngine


class GameEngine:
    gameover = False
    complete = False
    menu = True

    # @staticmethod
    # def

    @staticmethod
    def get_status():
        return GameEngine.complete, GameEngine.gameover, GameEngine.menu

    @staticmethod
    def player_control(left_b: int, right_b: int, up_b: int):
        Level.get_player().reset_directions()
        keys = pygame.key.get_pressed()
        if keys[left_b]:
            Level.get_player().set_direction("LEFT")
        if keys[right_b]:
            Level.get_player().set_direction("RIGHT")
        if keys[up_b]:
            Level.get_player().set_direction("UP")

    @staticmethod
    def update_physics_engine():
        #! Optimization
        enemies = Level.get_enemies()
        player = Level.get_player()
        physics_map = []
        physics_effect_map = []
        complete_blocks = []

        for item in Level.get_physics_map():
            for live in [*enemies, player]:
                if pygame.Rect(live.get_rect().x, live.get_rect().y, 25, 28).colliderect(item.get_rect()):
                    physics_map.append(item)
                    break

        for item in Level.get_physics_effect_map():
            for live in [*enemies, player]:
                if pygame.Rect(live.get_rect().x, live.get_rect().y, 25, 28).colliderect(item.get_rect()):
                    physics_effect_map.append(item)
                    break

        for item in Level.get_complete_blocks():
            for live in [*enemies, player]:
                if pygame.Rect(live.get_rect().x, live.get_rect().y, 25, 28).colliderect(item.get_rect()):
                    complete_blocks.append(item)
                    break

        #! test gravity
        PhysicsEngine.gravity([player, *enemies])
        PhysicsEngine.FrForceX(
            [*physics_map, *physics_effect_map], [player])

        #! test collide
        PhysicsEngine.map_collision(
            [*physics_map, *physics_effect_map, *complete_blocks], [player, *enemies])

        #!test effect
        for item in physics_effect_map:
            if PhysicsEngine.check_bottom_collision(item, player):
                item.activate_effect(player)

        #!test collide player-enemy
        for en in enemies:
            if PhysicsEngine.check_rect_collision(en, player):
                if PhysicsEngine.check_bottom_collision(en, player) and player.get_speed_y() > 0:
                    en.damage(1)
                    player.set_speed_y(-10)
                else:
                    player.kill()

        #!test check fall objects
        for obj in [player, *enemies]:
            if PhysicsEngine.check_fall(obj):
                obj.kill()
        for bonus in Level.get_bonuses():
            if PhysicsEngine.check_fall(bonus):
                Level.get_bonuses().remove(bonus)

        #!test collide with CompleteBlock
        for item in complete_blocks:
            if PhysicsEngine.check_bottom_collision(item, player):
                GameEngine.complete = True

    @staticmethod
    def check_live_player():
        if Level.get_player().get_health() <= 0:
            GameEngine.gameover = True

    @staticmethod
    def check_live_enemies():
        for en in Level.get_enemies():
            if en.get_health() <= 0:
                Level.get_enemies().remove(en)

    @staticmethod
    def update_game():
        Level.get_player().move()
        for en in Level.get_enemies():
            en.move()

        GameEngine.update_physics_engine()
        GameEngine.check_live_player()
        GameEngine.check_live_enemies()

        for item in [Level.get_player(), *Level.get_enemies()]:
            item.update()

    @staticmethod
    def render_game(screen: pygame.Surface, camera: pygame.Rect):
        camera.x = Level.get_player().get_rect().x - camera.width/(13)
        camera.y = Level.get_player().get_rect().y-camera.height/(1.5)

        for i in [*Level.get_physics_map(), *Level.get_complete_blocks(), *Level.get_physics_effect_map(), Level.get_player(), *Level.get_enemies()]:
            i.render(screen, camera.x, camera.y)
