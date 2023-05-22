from typing import List
from Enemies import Enemy, TestEnemy
from Map.EffectsMap import PhysicalEffectMapSprite, SpeedBlock
from Map.MapEngine import MapSprite
from Map.PhysicsMap import CommonBlock
from PhysicsEngine import PhysicalMapSprite

from Player import Player


class Level:
    player: Player
    enemies: List[Enemy] = []
    bonuses = []
    complete_blocks: List[PhysicalMapSprite] = []
    edge_blocks: List[PhysicalMapSprite] = []
    map_sprite: List[MapSprite] = []
    physics_map: List[PhysicalMapSprite] = []
    physics_effect_map: List[PhysicalEffectMapSprite] = []

    @staticmethod
    #!тут будет парсинг файла с уровнем
    def create_level(lvl_file_path: str):
        # with open(lvl_file_path, 'r', encoding="UTF-8") as lvl_file:
        #     for line in lvl_file:
        #         param = line.split(sep=" ")


        Level.enemies.append(TestEnemy(640, 350))
        # Level.bonuses.append()
        Level.player = Player(100, 100, 1)

        # Level.physics_effect_map.append(JumpBlock(32*4, 500-32))
        # Level.physics_effect_map.append(JumpBlock(0, 0))
        for i in range(32*7, 32*15, 32):
            Level.physics_effect_map.append(SpeedBlock(i, 500-32))

        for i in range(32*20, 32*24, 32):
            Level.physics_effect_map.append(SpeedBlock(i, 500-32))

        for i in range(0, 10000, 32):
            Level.physics_map.append(CommonBlock(i, 500))

        # for i in range(32*30, 32*40, 32):
        #     Level.physics_effect_map.append(SpeedBlock(i, 500-32))

    @staticmethod
    def get_enemies():
        return Level.enemies

    @staticmethod
    def get_player():
        return Level.player

    @staticmethod
    def get_bonuses():
        return Level.bonuses

    @staticmethod
    def get_map_sprite():
        return Level.map_sprite

    @staticmethod
    def get_physics_map():
        return Level.physics_map

    @staticmethod
    def get_physics_effect_map():
        return Level.physics_effect_map

    @staticmethod
    def get_complete_blocks():
        return Level.complete_blocks

    @staticmethod
    def get_edge_blocks():
        return Level.edge_blocks


Level.create_level("")
