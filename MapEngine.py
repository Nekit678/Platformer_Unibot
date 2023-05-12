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



