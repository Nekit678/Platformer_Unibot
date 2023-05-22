from typing import List, Literal
from Live import LiveObject
import pygame


class Player(LiveObject):
    def __init__(self, x: int, y: int, HP: int):
        super().__init__(player_img, x, y, HP)
        self.directions: List[Literal["LEFT", "RIGHT", "UP"]] = []

    def set_direction(self, direction: Literal["LEFT", "RIGHT", "UP"]):
        self.directions.append(direction)
    
    def reset_directions(self):
        self.directions = []

    def get_directions(self):
        return self.directions

    def move(self):
        for direction in self.directions:
            if direction == "LEFT":
                if self.get_speed_x() > -3:
                    self.set_speed_x(self.get_speed_x()-0.4)
            if direction == "RIGHT":
                if self.get_speed_x() < 3:
                    self.set_speed_x(self.get_speed_x()+0.4)
            if direction == "UP":
                self.jump()

    def jump(self):
        if self.get_speed_y() == 0:
            self.set_speed_y(-8)


player_img = pygame.Surface((20, 20))
player_img.fill("blue")
