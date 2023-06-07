import pygame
import GameEngine_Module.GameEngineModels


class Player(GameEngine_Module.GameEngineModels.Player):
    def __init__(self, x: int, y: int, HP: int):
        super().__init__(player_img, x, y, HP)


player_img = pygame.Surface((20, 20))
player_img.fill("blue")
