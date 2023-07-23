import pygame
from GameEngine_Module.GameEngineModels import Enemy



class TestEnemy(Enemy):
    def __init__(self, x: int, y: int):
        super().__init__(test_enemy, x, y, 1)


test_enemy = pygame.image.load("images/test_enemy.png")
