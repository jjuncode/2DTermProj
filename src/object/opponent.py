from src.mgr.TimeMgr import TimeMgr
from src.struct.struct import Vec2, OBJ
from src.component.ani import Ani

from src.component.collider import Collider
from src.component.stateMachine import *
from src.component.behavior_tree import BehaviorTree, Action, Sequence, Condition, Selector

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
                                          , 0.2, Vec2(1.5, 1.5), False)
                                      , Vec2(80, 60))
        self.effect["POINT"] = Effect(self, self.pos,
                                      Ani(self, self.pos, "effect_point.png", [5], [80], [80]
                                                         , 0.2, Vec2(3, 3))
                                      , Vec2 (0,60))

        # < State >
        self.state = StateOpponent(self)

        # < Behavior Tree >
        self.build_behavior_tree()

        # UI
        self.ui = UI(self, self.pos)
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
        self.effect["BLOOD"].resetFrame()
        self.component["EFFECT"] = self.effect["BLOOD"]

        self.component["PHYSIC"].addForce(Vec2(500, 0))
        if self.component["PHYSIC"].getAccel().y < 500:
            self.component["PHYSIC"].addForce(Vec2(0, 50))

    def delEffect(self):
        self.component["EFFECT"] = None



    def parrying(self):
        self.pos.x -= self.speed * TimeMgr.GetDt()  # 패링 반작용

        # 충격받음
        self.component["PHYSIC"].addForce(Vec2(1000, 0))
        if self.component["PHYSIC"].getAccel().y < 500:
            self.component["PHYSIC"].addForce(Vec2(0, 250))
        self.attackRelease()

    def attackRelease(self):
        self.state.attackRelease()


    def setGroggy(self):
        self.changeEffect("POINT")
        self.state.change_state("GROGGY")

    def changeEffect(self,_effect):
        self.effect[_effect].resetFrame()
        self.component["EFFECT"] = self.effect[_effect]

    def build_behavior_tree(self):
        c1 = Condition("플레이어보다 체력이 많거나 같은가", self.is_more_hp)
        c2 = Condition("플레이어보다 체력이 적은가", self.is_less_hp)

        move_forward = Action('전진', self.move_forward)  # action node 생성
        move_back = Action("후진", self.move_back)

        SEQ_move_froward = Sequence("앞으로 이동",c1,move_forward)
        SEQ_move_back = Sequence("뒤로 이동",c2,move_back)

        root = Selector("이동/후퇴", SEQ_move_froward,SEQ_move_back)

        self.bt = BehaviorTree(root)
        self.component["BT"] = self.bt


    # 플레이어보다 HP 많거나 같은지
    def is_more_hp(self):
        from src.mgr.SceneMgr import SceneMgr
        player = SceneMgr.getCurScene().getObj(OBJ.kPlayer)
        if self.hp >= player[0].hp :
            return BehaviorTree.SUCCESS
        else :
            return BehaviorTree.FAIL

    def is_less_hp(self):
        from src.mgr.SceneMgr import SceneMgr
        player = SceneMgr.getCurScene().getObj(OBJ.kPlayer)
        if self.hp < player[0].hp:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL

    def move_forward(self):
        self.state.change_state(Front)

    def move_back(self):
        self.state.change_state(Back)
