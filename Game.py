import pygame
import sys

from GameEngine_Module.GameEngine import GameEngine
from Menu_Module.Menu import Menu


FPS = 60
WIDTH = 1280
HEIGHT = 720

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
camera = pygame.Rect(0, 0, WIDTH, HEIGHT)

pygame.display.set_caption("Platformer ALPHA")
clock = pygame.time.Clock()


while True:
    screen.fill("black")
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    complete, gameover, menu = GameEngine.get_status()

    if menu:
        Menu.update()
        Menu.check_collision()
        Menu.render(screen)
    else:
        GameEngine.player_control(pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP)
        GameEngine.update_game()
        GameEngine.render_game(screen, camera)

    if gameover:
        pygame.quit()
        sys.exit()

    pygame.display.update()
