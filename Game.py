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
f = pygame.font.Font(None, 150)
f.set_italic(True)
f.set_bold(True)
f.set_underline(True)

gameover_text = f.render("GAME OVER", True, "white")
complete_text = f.render("YOU WIN!", True, "white")

pygame.display.set_caption("Platformer ALPHA")
clock = pygame.time.Clock()


while True:
    screen.fill("black")
    clock.tick(FPS)

    complete, gameover, menu = GameEngine.get_status()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                GameEngine.menu = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if menu:
                    if Menu.check_collision(event.pos):
                        GameEngine.menu = False

    if menu:
        Menu.update()
        Menu.render(screen)
    else:
        GameEngine.player_control(pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP)
        GameEngine.update_game()
        GameEngine.render_game(screen, camera)

    if complete:
        GameEngine.menu = True
        GameEngine.complete = False
        screen.blit(complete_text, (350, 300))
        pygame.display.update()
        pygame.time.delay(2000)

    if gameover:
        GameEngine.gameover = False
        GameEngine.menu = True
        screen.blit(gameover_text, (300, 300))
        pygame.display.update()
        pygame.time.delay(2000)

    pygame.display.update()
