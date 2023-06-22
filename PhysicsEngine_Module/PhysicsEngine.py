from typing import List

from PhysicsEngine_Module.PhysicsEngineModels import PhysicalMapSprite, PhysicsObject



class PhysicsEngine:  # базовый физический движок
    GRAVITY = 0.35
    FrForceKoef = 0.3

    @staticmethod
    def check_fall(obj: PhysicsObject) -> bool:
        y = obj.get_rect().y
        if y > 200:
            return True
        return False
        

    @staticmethod
    def check_bottom_collision(obj, player: PhysicsObject):
        if (obj.get_rect().collidepoint(player.get_rect().bottomleft) or obj.get_rect().collidepoint(player.get_rect().bottomright)):
            return True
        return False

    @staticmethod
    def check_rect_collision(obj, player: PhysicsObject):
        if obj.get_rect().colliderect(player.get_rect()):
            return True
        return False

    @staticmethod
    def gravity(obj_items: List[PhysicsObject]):  # гравитация
        for obj in obj_items:
            if obj.get_speed_y() < 15:
                obj.set_speed_y(obj.get_speed_y() + PhysicsEngine.GRAVITY)

    @staticmethod
    # сила трения
    def FrForceX(map_items: List[PhysicalMapSprite], obj_items: List[PhysicsObject]):
        for obj in obj_items:
            for item in map_items:
                if (item.get_rect().collidepoint(obj.get_rect().bottomleft) and item.get_rect().collidepoint(obj.get_rect().bottomright)):
                    if obj.get_speed_x() < 0:
                        obj.set_speed_x(obj.get_speed_x() +
                                        PhysicsEngine.FrForceKoef)
                        if obj.get_speed_x() > 0:
                            obj.set_speed_x(0)

                    elif obj.get_speed_x() > 0:
                        obj.set_speed_x(obj.get_speed_x() -
                                        PhysicsEngine.FrForceKoef)
                        if obj.get_speed_x() < 0:
                            obj.set_speed_x(0)
                    break

    @staticmethod  # базовая физика столкновений
    def phys_obj_phys_map_item_collision(item: PhysicalMapSprite, obj: PhysicsObject):
        if (item.get_rect().collidepoint(obj.get_rect().bottomleft) and item.get_rect().collidepoint(obj.get_rect().bottomright)):
            if obj.get_speed_y() > 0:
                obj.get_rect().bottom = item.get_rect().top
                obj.set_speed_y(0)
        elif (item.get_rect().collidepoint(obj.get_rect().topleft) and item.get_rect().collidepoint(obj.get_rect().topright)):
            if obj.get_speed_y() < 0:
                obj.get_rect().top = item.get_rect().bottom
                obj.set_speed_y(1)
        elif (item.get_rect().collidepoint(obj.get_rect().topleft) and item.get_rect().collidepoint(obj.get_rect().bottomleft)):
            obj.get_rect().left = item.get_rect().right + 1
            obj.set_speed_x(0)
        elif (item.get_rect().collidepoint(obj.get_rect().topright) and item.get_rect().collidepoint(obj.get_rect().bottomright)):
            obj.get_rect().right = item.get_rect().left - 1
            obj.set_speed_x(0)

        elif (item.get_rect().collidepoint(obj.get_rect().bottomleft)):
            if abs(obj.get_rect().bottomleft[1] - item.get_rect().top) < 7 and abs(obj.get_rect().bottomleft[0] - item.get_rect().right) > 2:
                if obj.get_speed_y() > 0:
                    obj.get_rect().bottom = item.get_rect().top
                    obj.set_speed_y(0)

            if abs(obj.get_rect().bottomleft[1] - item.get_rect().top) >= 7:
                if obj.get_speed_x() < 0:
                    obj.get_rect().left = item.get_rect().right + 1
                    obj.set_speed_x(0)

        elif (item.get_rect().collidepoint(obj.get_rect().bottomright)):
            if abs(obj.get_rect().bottomright[1] - item.get_rect().top) < 7 and abs(obj.get_rect().bottomright[0] - item.get_rect().left) > 2:
                if obj.get_speed_y() > 0:
                    obj.get_rect().bottom = item.get_rect().top
                    obj.set_speed_y(0)

            if abs(obj.get_rect().bottomright[1] - item.get_rect().top) >= 7:
                if obj.get_speed_x() > 0:
                    obj.get_rect().right = item.get_rect().left - 1
                    obj.set_speed_x(0)

        elif (item.get_rect().collidepoint(obj.get_rect().topleft)):
            if abs(obj.get_rect().topleft[1] - item.get_rect().bottom) < 7:
                if obj.get_speed_y() < 0:
                    obj.get_rect().top = item.get_rect().bottom
                    obj.set_speed_y(1)

            if abs(obj.get_rect().topleft[1] - item.get_rect().bottom) >= 7:
                if obj.get_speed_x() < 0:
                    obj.get_rect().left = item.get_rect().right + 1
                    obj.set_speed_x(0)

        elif (item.get_rect().collidepoint(obj.get_rect().topright)):
            if abs(obj.get_rect().topright[1] - item.get_rect().bottom) < 7:
                if obj.get_speed_y() < 0:
                    obj.get_rect().top = item.get_rect().bottom
                    obj.set_speed_y(1)

            if abs(obj.get_rect().topright[1] - item.get_rect().bottom) >= 7:
                if obj.get_speed_x() > 0:
                    obj.get_rect().right = item.get_rect().left - 1
                    obj.set_speed_x(0)

    @staticmethod
    # базовая физика столкновений
    def map_collision(map_items: List[PhysicalMapSprite], obj_items: List[PhysicsObject]):
        for obj in obj_items:
            for item in map_items:
                PhysicsEngine.phys_obj_phys_map_item_collision(item, obj)
