import pygame

from PhysicsEngine_Module.PhysicsEngineModels import PhysicalMapSprite


# обычный блок (ничего не делает)
class CommonBlock(PhysicalMapSprite):
    def __init__(self, x: int, y: int):
        super().__init__(common_block_img, x, y)

###################### особые блоки ###########################


class CompleteBlock(PhysicalMapSprite):
    def __init__(self, x: int, y: int):
        super().__init__(complete_block_img, x, y)


class EdgeBlock(PhysicalMapSprite):
    def __init__(self, x: int, y: int):
        super().__init__(complete_block_img, x, y)


complete_block_img = pygame.image.load("images/complete_block.png")
common_block_img = pygame.image.load("images/common_block.png")
