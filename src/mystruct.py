from enum import Enum

class Vec2:
    def __init__(self,_x,_y):
        self.x = _x
        self.y = _y
    #
    # def __add__(self, other):
    #     if isinstance(other, Vec2):
    #         # 두 객체를 더하고 새로운 객체를 반환
    #         return Vec2(self.x + other.x,self.y + other.y)
    #
    # def __div__(self, other):
    #     if isinstance(other, int):
    #         if other != 0 :
    #             # 두 객체를 나누고 새로운 객체를 반환
    #             return Vec2(self.x / other, self.y / other)
    #
    # def __mul__(self, other):
    #     if isinstance(other, Vec2):
    #         # 두 객체를 곱하고 새로운 객체를 반환
    #         return Vec2(self.x * other.x,self.y*other.y)

class OBJ(Enum):
    kBackground = 0
    kOpponent = 1
    kOpponent_sword = 2
    kPlayer = 3
    kPlayer_sword = 4

    kTitle_background = 5
    kTitle_fence = 6
    kTitle_logo = 7

    kLevel_level = 8
    kLevel_background = 9
    END = 10
