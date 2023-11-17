from pico2d import load_image

from src.mgr.TimeMgr import TimeMgr
from src.struct.struct import Vec2
from src.component.ani import Ani
from src.component.effect import Effect

from src.component.collider import Collider
from src.component.stateMachine import StatePlayer,Idle
from src.component.physic import Physic
from src.component.ui import UI

class Player:
    def __init__(self):
        self.pos = Vec2(200, 300)
        self.speed = 200
        self.dir = 1 # 양의 x축방향이 정면
        self.hp = 100

        # < Component >
        self.component = {}

        # animation
        self.cur_ani = 0
        self.ani_reset = False
        self.ani = Ani(self, self.pos, "Character.png", [8, 12, 7, 7], [128, 128, 200, 200], [130, 120, 203, 203]
                       , 0.15, Vec2(3, 3))
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
                                                         , 0.2, Vec2(1.5, 1.5),True)
                                      , Vec2 (-80,60))
        # < StateMachine >
        self.state = StatePlayer(self)

        # UI
        self.ui = UI(self,self.pos)
        self.component["UI"] = self.ui

    def render(self):
        self.state.render()
        for key, value in self.component.items():
            if value != None:
                value.render()

    def update(self):
        self.state.update()
        for key, value in self.component.items():
            if value != None:
               value.update()

    def getPos(self):
        return Vec2(self.pos.x, self.pos.y)

    def getCurState(self):
        return self.state.cur_state

    def get_bb(self):
        return self.component["COLLIDER"].get_bb()

    def processColl(self, _obj):  # 충돌처리
        # 피 흘림
        self.effect["BLOOD"].resetFrame()
        self.component["EFFECT"] = self.effect["BLOOD"]

        # 충격받음
        self.component["PHYSIC"].addForce(Vec2(-500, 0))
        if self.component["PHYSIC"].getAccel().y < 500:
            self.component["PHYSIC"].addForce(Vec2(0, 50))

    def delEffect(self):
        self.component["EFFECT"] = None

    def parrying(self):
        self.pos.x -= self.speed * TimeMgr.GetDt()  # 패링 반작용

        # 충격받음
        self.component["PHYSIC"].addForce(Vec2(-1000, 0))
        if self.component["PHYSIC"].getAccel().y < 500:
            self.component["PHYSIC"].addForce(Vec2(0, 250))
        self.attackRelease()

    def attackRelease(self):
        self.state.attackRelease()