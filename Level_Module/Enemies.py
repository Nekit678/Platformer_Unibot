import pygame
from GameEngine_Module.GameEngineModels import Enemy



class TestEnemy(Enemy):
    def __init__(self, x: int, y: int):
        super().__init__(img_a, x, y, 1)


img_a = pygame.Surface((20, 20))
img_a.fill("red")
