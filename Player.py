from Live import LiveObject
import pygame


class Player(LiveObject):
    def __init__(self, image: pygame.Surface, x: int, y: int, HP: int):
        super().__init__(image, x, y, HP)
        #####

    def jump(self):
        if self.sp_y == 0:
            self.set_speed_y(-8)
