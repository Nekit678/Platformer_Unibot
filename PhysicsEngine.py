import pygame
from typing import List
from Map import PhysicalMapSprite


class PhysicsObject(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface, x: int, y: int):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.sp_x = 0
        self.sp_y = 0

    def set_speed_x(self, sp_x: int):
        self.sp_x = sp_x

    def get_rect(self):
        return self.rect

    def set_speed_y(self, sp_y: int):
        self.sp_y = sp_y

    def gravity(self, koef: float):
        self.sp_y += koef

    def FrForceX(self):
        if self.sp_x < 0:
            self.sp_x += 0.3
        if self.sp_x > 0:
            self.sp_x -= 0.3

    def check_collision(self, items: List[PhysicalMapSprite]):
        for item in items:
            if item.get_rect().colliderect(self.rect) and self.sp_y > 0:
                self.rect.bottom = item.rect.top+1
                self.sp_y = 0

    def update(self):
        self.rect.x += self.sp_x
        self.rect.y += self.sp_y

    def render(self, master: pygame.Surface):
        master.blit(self.image, self.rect)
