import pygame


class LiveObject(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface, x: int, y: int):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.sp_x = 0
        self.sp_y = 0
    
    def set_speed_x(self, sp_x:int):
        self.sp_x = sp_x

    def set_speed_y(self, sp_y:int):
        self.sp_y = sp_y

    def update(self):
        self.rect.x += self.sp_x
        self.rect.y += self.sp_y

    def render(self, master: pygame.Surface):
        master.blit(self.image, self.rect)
