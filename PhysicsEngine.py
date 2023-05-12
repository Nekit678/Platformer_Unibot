import pygame
from typing import List

from MapEngine import MapSprite


class PhysicalMapSprite(MapSprite):
    def __init__(self, image: pygame.Surface, x: int, y: int):
        super().__init__(image, x, y)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def get_rect(self):
        return self.rect


class PhysicsObject(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface, x: int, y: int):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.sp_x = 0.0
        self.sp_y = 0.0

    def get_rect(self) -> pygame.Rect:
        return self.rect

    def get_speed_x(self) -> float:
        return self.sp_x

    def get_speed_y(self) -> float:
        return self.sp_y

    def set_speed_x(self, sp_x: float) -> None:
        self.sp_x = sp_x

    def set_speed_y(self, sp_y: float) -> None:
        self.sp_y = sp_y

    def update(self):
        self.rect.x += self.sp_x
        self.rect.y += self.sp_y

    def render(self, master: pygame.Surface):
        master.blit(self.image, self.rect)


class PhysicsEngine:
    GRAVITY = 0.35
    FrForceKoef = 0.3

    @staticmethod
    def gravity(obj_items: List[PhysicsObject]):
        for obj in obj_items:
            obj.set_speed_y(obj.get_speed_y() + PhysicsEngine.GRAVITY)

    @staticmethod
    def FrForceX(obj_items: List[PhysicsObject]):
        for obj in obj_items:
            if obj.get_speed_x() < 0:
                obj.set_speed_x(obj.get_speed_x() + PhysicsEngine.FrForceKoef)

            if obj.get_speed_x() > 0:
                obj.set_speed_x(obj.get_speed_x() - PhysicsEngine.FrForceKoef)

    @staticmethod
    def map_collision(map_items: List[PhysicalMapSprite], obj_items: List[PhysicsObject]):
        for obj in obj_items:
            for item in map_items:
                if (item.get_rect().collidepoint(obj.get_rect().bottomleft) and item.get_rect().collidepoint(obj.get_rect().bottomright)):
                    if obj.get_speed_y() > 0:
                        obj.get_rect().bottom = item.get_rect().top
                        obj.set_speed_y(0)
                elif (item.get_rect().collidepoint(obj.get_rect().topleft) and item.get_rect().collidepoint(obj.get_rect().topright)):
                    if obj.get_speed_y() < 0:
                        obj.get_rect().top = item.get_rect().bottom
                        obj.set_speed_y(1)
                elif (item.get_rect().collidepoint(obj.get_rect().topleft) and item.get_rect().collidepoint(obj.get_rect().bottomleft)):
                    obj.get_rect().left = item.get_rect().right + 1
                    obj.set_speed_x(0)
                elif (item.get_rect().collidepoint(obj.get_rect().topright) and item.get_rect().collidepoint(obj.get_rect().bottomright)):
                    obj.get_rect().right = item.get_rect().left - 1
                    obj.set_speed_x(0)

                elif (item.get_rect().collidepoint(obj.get_rect().bottomleft)):
                    if abs(obj.get_rect().bottomleft[1] - item.get_rect().top) < 7 and abs(obj.get_rect().bottomleft[0] - item.get_rect().right) > 2:
                        if obj.get_speed_y() > 0:
                            obj.get_rect().bottom = item.get_rect().top
                            obj.set_speed_y(0)

                    if abs(obj.get_rect().bottomleft[1] - item.get_rect().top) > 7:
                        if obj.get_speed_x() < 0:
                            obj.get_rect().left = item.get_rect().right + 1
                            obj.set_speed_x(0)

                elif (item.get_rect().collidepoint(obj.get_rect().bottomright)):
                    if abs(obj.get_rect().bottomright[1] - item.get_rect().top) < 7 and abs(obj.get_rect().bottomright[0] - item.get_rect().left) > 2:
                        if obj.get_speed_y() > 0:
                            obj.get_rect().bottom = item.get_rect().top
                            obj.set_speed_y(0)

                    if abs(obj.get_rect().bottomright[1] - item.get_rect().top) > 7:
                        if obj.get_speed_x() > 0:
                            obj.get_rect().right = item.get_rect().left - 1
                            obj.set_speed_x(0)

                elif (item.get_rect().collidepoint(obj.get_rect().topleft)):
                    if abs(obj.get_rect().topleft[1] - item.get_rect().bottom) < 7:
                        if obj.get_speed_y() < 0:
                            obj.get_rect().top = item.get_rect().bottom
                            obj.set_speed_y(1)

                    if abs(obj.get_rect().topleft[1] - item.get_rect().bottom) > 7:
                        if obj.get_speed_x() < 0:
                            obj.get_rect().left = item.get_rect().right + 1
                            obj.set_speed_x(0)

                elif (item.get_rect().collidepoint(obj.get_rect().topright)):
                    if abs(obj.get_rect().topright[1] - item.get_rect().bottom) < 7:
                        if obj.get_speed_y() < 0:
                            obj.get_rect().top = item.get_rect().bottom
                            obj.set_speed_y(1)

                    if abs(obj.get_rect().topright[1] - item.get_rect().bottom) > 7:
                        if obj.get_speed_x() > 0:
                            obj.get_rect().right = item.get_rect().left - 1
                            obj.set_speed_x(0)
