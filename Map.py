import pygame
from PhysicsEngine import PhysicalMapSprite

class CommonBlock(PhysicalMapSprite):
    def __init__(self, x: int, y: int):
        img = pygame.Surface((50, 50))
        img.fill("gray")
        super().__init__(img, x, y)