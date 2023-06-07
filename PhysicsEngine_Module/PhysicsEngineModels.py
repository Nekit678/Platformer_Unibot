import pygame
from Map_Module.MapEngine import MapSprite

# физические блоки карты (есть взаимодействие)
class PhysicalMapSprite(MapSprite):
    def __init__(self, image: pygame.Surface, x: int, y: int):
        super().__init__(image, x, y)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def get_rect(self):
        return self.rect

# нестатические физические объекты (по типу игрока, врагов и т.д)
class PhysicsObject(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface, x: int, y: int):
        super().__init__()
        self.image = pygame.transform.scale(image, (25, 25))
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

    def render(self, master: pygame.Surface, c_x: int, c_y: int):
        master.blit(self.image, (self.rect.x - c_x, self.rect.y - c_y))
