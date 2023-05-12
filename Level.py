from Map import CommonBlock, JumpBlock


class Level:
    enemies = []
    bonuses = []
    physics_effect_map = [JumpBlock(32*4, 500-32), JumpBlock(0, 0)]

    physics_objects = [*enemies]
    physics_map = [*physics_effect_map]
    for i in range(0, 10000, 32):
        physics_map.append(CommonBlock(i, 500))