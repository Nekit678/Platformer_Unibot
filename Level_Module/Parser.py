
from Level_Module.EffectsMap import DamageBlock, GravityBlock, KillBlock, SlowBlock, SpeedBlock
from Level_Module.PhysicsMap import CommonBlock
from Level_Module.Player import Player


items = {
    0: Player,
    1: GravityBlock,
    2: SpeedBlock,
    3: SlowBlock,
    4: KillBlock,
    5: DamageBlock,
    6: CommonBlock
}


class Parser:
    @staticmethod
    def get_lvl_list():
        pass

    @staticmethod
    def load_level(lvl_pathname: str):
        s = "5 100 500"
        info = s.split(sep=" ")
        item_id = int(info[0])
        item_args = []
        for arg in info[1:]:
            item_args.append(int(arg))
        print(item_id)
        print(item_args)
        print(items[item_id](*item_args))
