from abc import ABC, abstractmethod
from typing import List, Literal
import pygame
from PhysicsEngine_Module.PhysicsEngineModels import PhysicalMapSprite, PhysicsObject


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

class Player(LiveObject):
    def __init__(self,image: pygame.Surface, x: int, y: int, HP: int):
        super().__init__(image, x, y, HP)
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

class Enemy(LiveObject):
    def __init__(self, image: pygame.Surface, x: int, y: int, HP: int):
        super().__init__(image, x, y, HP)
        self.last_sp_x = 0

    def move(self):
        if self.get_speed_x() == 0:
            if self.last_sp_x < 0:
                self.set_speed_x(1)
            else:
                self.set_speed_x(-1)

        self.last_sp_x = self.get_speed_x()


class PhysicalEffectMapSprite(PhysicalMapSprite, ABC):
    @abstractmethod
    def activate_effect(self, player: Player):
        pass