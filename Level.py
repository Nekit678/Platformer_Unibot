from Map import CommonBlock, JumpBlock, SpeedBlock


class Level:
    map_sprite = []

    enemies = []
    bonuses = []
    physics_effect_map = []

    physics_objects = []
    physics_map = []

    physics_effect_map = []

    physics_objects = []
    physics_map = []

    @staticmethod
    def create_level():
        # Level.enemies.append()
        # Level.bonuses.append()

        Level.physics_effect_map.append(JumpBlock(32*4, 500-32))
        Level.physics_effect_map.append(JumpBlock(0, 0))
        for i in range(32*7, 32*15, 32):
            Level.physics_effect_map.append(SpeedBlock(i, 500-32))

        for i in range(0, 10000, 32):
            Level.physics_map.append(CommonBlock(i, 500))

        Level.physics_objects = [*Level.enemies, *Level.bonuses]
        Level.physics_map = [*Level.physics_map, *Level.physics_effect_map]


Level.create_level()
