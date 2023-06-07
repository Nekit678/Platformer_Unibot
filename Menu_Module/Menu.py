import pygame

from Level_Module.Parser import Parser


class MenuButton(pygame.Surface):
    def __init__(self, lvl_number,lvl_pathname, x, y):
        super().__init__((70, 70))
        self.fill("blue")
        self.rect = self.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.lvl_pathname = lvl_pathname

        lvl = pygame.font.Font(None, 40).render(
            lvl_number, True, (255, 255, 255))
        self.blit(lvl, (10, 10))

    def render(self, master: pygame.Surface):
        master.blit(self, (0, 0))


class Menu():
    surf = pygame.Surface((1280, 720), pygame.SRCALPHA, 32)
    buttons = []

    @staticmethod
    def update():
        Menu.buttons = []
        count = 1
        row = 1
        col = 0
        for i in range(0, 26):
            Menu.buttons.append(MenuButton(str(count), "", 50 + col*100, row*100))
            count += 1
            col += 1
            if col == 12:
                row += 1
                col = 0

        for b in Menu.buttons:
            Menu.surf.blit(b, b.rect)

    @staticmethod
    def check_collision():
        pos = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()
        for b in Menu.buttons:
            if b.rect.collidepoint(pos):
                if pressed[0]:
                    Parser.load_level(b.lvl_pathname)

    @staticmethod
    def render(master: pygame.Surface):
        master.blit(Menu.surf, (0, 0))
