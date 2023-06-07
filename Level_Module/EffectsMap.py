import pygame
from GameEngine_Module.GameEngineModels import PhysicalEffectMapSprite


class JumpBlock(PhysicalEffectMapSprite):
    def __init__(self, x: int, y: int):
        super().__init__(jump_block_img, x, y)

    def activate_effect(self, player):
        player.set_speed_y(-15)


# притягивает игрока (нельзя прыгнуть)
class GravityBlock(PhysicalEffectMapSprite):
    def __init__(self, x: int, y: int):
        super().__init__(gravity_block_img, x, y)

    def activate_effect(self, player):
        player.set_speed_y(0)


# ускоряет игрока в сторону движения
class SpeedBlock(PhysicalEffectMapSprite):
    def __init__(self, x: int, y: int):
        super().__init__(speed_block_img, x, y)

    def activate_effect(self, player):
        for direction in player.get_directions():
            if direction == "RIGHT":
                player.set_speed_x(7)
            elif direction == "LEFT":
                player.set_speed_x(-7)


# замедляет игрока в сторону движения
class SlowBlock(PhysicalEffectMapSprite):
    def __init__(self, x: int, y: int):
        super().__init__(slow_block_img, x, y)

    def activate_effect(self, player):
        for direction in player.get_directions():
            if direction == "RIGHT":
                player.set_speed_x(1)
            elif direction == "LEFT":
                player.set_speed_x(-1)


class KillBlock(PhysicalEffectMapSprite):
    def __init__(self, x: int, y: int):
        super().__init__(slow_block_img, x, y)

    def activate_effect(self, player):
        player.kill()


class DamageBlock(PhysicalEffectMapSprite):
    def __init__(self, x: int, y: int):
        super().__init__(slow_block_img, x, y)
        self.count = 1

    def activate_effect(self, player):
        if self.count == 1:
            player.damage(1)
            self.count = 0


jump_block_img = pygame.Surface((50, 50))
jump_block_img.fill("green")

gravity_block_img = pygame.Surface((50, 50))
gravity_block_img.fill("blue")

speed_block_img = pygame.Surface((50, 50))
speed_block_img.fill("orange")

slow_block_img = pygame.Surface((50, 50))
slow_block_img.fill("orange")

edge_block_img = pygame.Surface((50, 50))
edge_block_img.fill("red")
