import pygame


class MapSprite(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface, x: int, y: int):
        super().__init__()
        self.image = pygame.transform.scale(image, (32, 32))
        self.x = x
        self.y = y

    def render(self, master: pygame.Surface):
        master.blit(self.image, (self.x, self.y))


##########################################################################


class PhysicalMapSprite(MapSprite):
    def __init__(self, image: pygame.Surface, x: int, y: int):
        super().__init__(image, x, y)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def get_rect(self):
        return self.rect


class CommonBlock(PhysicalMapSprite):
    def __init__(self, x: int, y: int):
        img = pygame.Surface((50, 50))
        img.fill("gray")
        super().__init__(img, x, y)
