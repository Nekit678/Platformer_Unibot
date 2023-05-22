import pygame
from Live import LiveObject


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


class TestEnemy(Enemy):
    def __init__(self, x: int, y: int):
        super().__init__(img_a, x, y, 1)


img_a = pygame.Surface((20, 20))
img_a.fill("red")
