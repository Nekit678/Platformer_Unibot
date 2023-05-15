import pygame
from PhysicsEngine import PhysicalMapSprite, PhysicalEffectMapSprite
from Player import PLAYER


# обычный блок (ничего не делает)
class CommonBlock(PhysicalMapSprite):
    def __init__(self, x: int, y: int):
        super().__init__(common_block_img, x, y)


# поддталкивает игрока вверх
class JumpBlock(PhysicalEffectMapSprite):
    def __init__(self, x: int, y: int):
        super().__init__(jump_block_img, x, y)

    def activate_effect(self):
        PLAYER.set_speed_y(-15)


# притягивает игрока (нельзя прыгнуть)
class GravityBlock(PhysicalEffectMapSprite):
    def __init__(self, x: int, y: int):
        super().__init__(gravity_block_img, x, y)

    def activate_effect(self):
        PLAYER.set_speed_y(0)


# толкает игрока в сторону движения
class SpeedBlock(PhysicalEffectMapSprite):
    def __init__(self, x: int, y: int):
        super().__init__(speed_block_img, x, y)

    def activate_effect(self):
        if PLAYER.get_speed_x() > 0:
            PLAYER.set_speed_x(7)
        elif PLAYER.get_speed_x() < 0:
            PLAYER.set_speed_x(-7)


common_block_img = pygame.Surface((50, 50))
common_block_img.fill("gray")

jump_block_img = pygame.Surface((50, 50))
jump_block_img.fill("green")

gravity_block_img = pygame.Surface((50, 50))
gravity_block_img.fill("blue")

speed_block_img = pygame.Surface((50, 50))
speed_block_img.fill("orange")
