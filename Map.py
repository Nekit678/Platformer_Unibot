import pygame
from PhysicsEngine import PhysicalMapSprite, PhysicalEffectMapSprite
from Player import PLAYER

#обычный блок (ничего не делает)
class CommonBlock(PhysicalMapSprite):
    def __init__(self, x: int, y: int):
        img = pygame.Surface((50, 50))
        img.fill("gray")
        super().__init__(img, x, y)


#поддталкивает игрока вверх
class JumpBlock(PhysicalEffectMapSprite):
    def __init__(self, x: int, y: int):
        img = pygame.Surface((50, 50))
        img.fill("green")
        super().__init__(img, x, y)

    def activate_effect(self):
        PLAYER.set_speed_y(-15)

#притягивает игрока (нельзя прыгнуть)
class GravityBlock(PhysicalEffectMapSprite):
    def __init__(self, x: int, y: int):
        img = pygame.Surface((50, 50))
        img.fill("blue")
        super().__init__(img, x, y)

    def activate_effect(self):
        PLAYER.set_speed_y(0)