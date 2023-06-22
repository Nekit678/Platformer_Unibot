from typing import List, Tuple
import pygame

from Level_Module.Parser import Parser


class MenuButton(pygame.Surface):
    def __init__(self, lvl_number, lvl_pathname, x, y):
        super().__init__((70, 70))
        self.fill("blue")
        self.rect = self.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.lvl_pathname = lvl_pathname

        lvl = pygame.font.Font(None, 40).render(
            lvl_number, True, (255, 255, 255))
        self.blit(lvl, (10, 10))

    def check_collision(self, pos: Tuple[int, int]):
        if self.rect.collidepoint(pos):
            Parser.load_level(self.lvl_pathname)
            return True
        return False

    def render(self, master: pygame.Surface):
        master.blit(self, (0, 0))


class Menu():
    surf = pygame.Surface((1280, 720), pygame.SRCALPHA, 32)
    buttons: List[MenuButton] = []

    @staticmethod
    def update():
        Menu.buttons = []
        count = 1
        row = 1
        col = 0

        for file in Parser.get_lvl_list():
            Menu.buttons.append(MenuButton(
                str(count), file, 50 + col*100, row*100))
            count += 1
            col += 1
            if col == 12:
                row += 1
                col = 0

        Menu.surf.fill("black")
        for b in Menu.buttons:
            Menu.surf.blit(b, b.rect)

    @staticmethod
    def check_collision(pos: Tuple[int, int]):
        for b in Menu.buttons:
            if b.check_collision(pos):
                return True
        return False

    @staticmethod
    def render(master: pygame.Surface):
        master.blit(Menu.surf, (0, 0))
