from typing import Literal
from Live import LiveObject
import pygame


class Player(LiveObject):
    def __init__(self, image: pygame.Surface, x: int, y: int, HP: int):
        super().__init__(image, x, y, HP)
        self.direction = "NULL"

    def set_direction(self, direction: Literal["LEFT", "RIGHT", "UP", "NULL"]):
        self.direction = direction

    def move(self):
        if self.direction == "LEFT":
            self.set_speed_x(-3)
        if self.direction == "RIGHT":
            self.set_speed_x(3)
        if self.direction == "UP":
            self.jump()

    def jump(self):
        if self.sp_y == 0:
            self.set_speed_y(-8)


img_a = pygame.Surface((20, 20))
img_a.fill("blue")
PLAYER = Player(img_a, 100, 100, 1)
