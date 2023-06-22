from typing import List

from GameEngine_Module.GameEngineModels import Enemy, PhysicalEffectMapSprite
from PhysicsEngine_Module.PhysicsEngineModels import PhysicalMapSprite
from Map_Module.MapEngine import MapSprite
from Level_Module.Player import Player


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
    def set_player(player: Player):
        Level.player = player

    @staticmethod
    def add_enemy(enemy: Enemy):
        Level.enemies.append(enemy)

    @staticmethod
    def add_bonus(bonus):
        Level.bonuses.append(bonus)

    @staticmethod
    def add_complete_block(block: PhysicalMapSprite):
        Level.complete_blocks.append(block)

    @staticmethod
    def add_edge_block(block: PhysicalMapSprite):
        Level.edge_blocks.append(block)

    @staticmethod
    def add_map_sprite_block(block: MapSprite):
        Level.map_sprite.append(block)

    @staticmethod
    def add_physics_map_block(block: PhysicalMapSprite):
        Level.physics_map.append(block)

    @staticmethod
    def add_physics_effect_map_block(block: PhysicalEffectMapSprite):
        Level.physics_effect_map.append(block)

    @staticmethod
    def clear_level():
        Level.player = None
        Level.enemies = []
        Level.bonuses = []
        Level.complete_blocks = []
        Level.edge_blocks = []
        Level.map_sprite = []
        Level.physics_map = []
        Level.physics_effect_map = []

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
