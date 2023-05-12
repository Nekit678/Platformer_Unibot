import pygame

from PhysicsEngine import PhysicsObject

class LiveObject(PhysicsObject):
    def __init__(self, image: pygame.Surface, x: int, y: int, HP: int):
        super().__init__(image, x, y)
        self.health = HP


