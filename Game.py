import pygame
import sys

FPS = 60
WIDTH = 1280
HEIGHT = 720

class Game:
    pass


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wall kickers ALPHA")
clock = pygame.time.Clock()


def update():
    pass


while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    update()
    pygame.display.update()
