import pygame


class MapSprite(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface, x: int, y: int):
        super().__init__()
        self.image = pygame.transform.scale(image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def render(self, master: pygame.Surface):
        master.blit(self.image, self.rect)


class PhysicalMapSprite(MapSprite):
    def __init__(self, image: pygame.Surface, x, y):
        super().__init__(image, x, y)
        
