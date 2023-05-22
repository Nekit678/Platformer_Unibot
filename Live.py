import pygame
from PhysicsEngine import PhysicsObject


class LiveObject(PhysicsObject):
    def __init__(self, image: pygame.Surface, x: int, y: int, HP: int):
        super().__init__(image, x, y)
        self.health = HP

    def damage(self, dmg: int):
        self.health -= dmg

    def kill(self):
        self.health = 0

    def get_health(self):
        return self.health
