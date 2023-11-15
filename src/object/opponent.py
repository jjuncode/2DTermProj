from src.mgr.TimeMgr import TimeMgr
from src.struct.struct import Vec2
from src.component.ani import Ani

from src.component.collider import Collider
from src.component.stateMachine import StateOpponent
from src.component.physic import Physic
from src.component.ui import UI
from src.component.effect import Effect

class Opponent:
    def __init__(self):
        self.pos = Vec2(600, 300)
        self.speed = 200
        self.dir = -1 # 음의 x축방향이 정면
        self.hp = 100

        # < Component >
        self.component = {}

        # animation
        self.cur_ani = 0
        self.ani_reset = False
        self.ani = Ani(self, self.pos, "Character.png", [8, 12, 7, 7], [128, 128, 200, 200], [130, 120, 203, 203]
                       , 0.15, Vec2(3, 3),True)
        self.component["ANI"] = self.ani

        # collider
        self.collider = Collider(self, Vec2(self.pos.x, self.pos.y), Vec2(40, 70))
        self.component["COLLIDER"] = self.collider

        # physic
        self.physic = Physic(self, Vec2(self.pos.x, self.pos.y))
        self.destn_y = 200
        self.physic.destn_y = self.destn_y
        self.component["PHYSIC"] = self.physic

        # effect
        self.effect = {}
        self.effect["BLOOD"] = Effect(self, self.pos,
                                      Ani(self, self.pos, "effect_blood.png", [4], [128], [171]
                                          , 0.2, Vec2(1.5, 1.5), True)
                                      , Vec2(-80, 60))
        # < StateMachine >
        self.state = StateOpponent(self)

        # UI
        self.ui = UI(self, self.pos)
        self.component["UI"] = self.ui

    def render(self):
        self.state.render()
        for key, value in self.component.items():
            value.render()

    def update(self):
        self.state.update()
        for key, value in self.component.items():
            value.update()

    def getPos(self):
        return Vec2(self.pos.x, self.pos.y)

    def getCurState(self):
        return self.state.cur_state

    def get_bb(self):
        return self.component["COLLIDER"].get_bb()

    def processColl(self, _obj):  # 충돌처리
        self.effect["BLOOD"].resetFrame()
        self.component["EFFECT"] = self.effect["BLOOD"]
        print("현재 체력 : ",self.hp)
        pass

    def delEffect(self):
        self.component["EFFECT"] = None
