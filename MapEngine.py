import pygame


class MapSprite(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface, x: int, y: int):
        super().__init__()
        self.image = pygame.transform.scale(image, (32, 32))
        self.x = x
        self.y = y

    def render(self, master: pygame.Surface, c_x: int, c_y: int):
        master.blit(self.image, (self.x - c_x, self.y - c_y))
