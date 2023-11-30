from pico2d import load_music, load_wav

from TimeMgr import TimeMgr
from scene_result import scene_result
from mystruct import Vec2, OBJ
from ani import Ani

from collider import Collider
from stateMachine import *
from behavior_tree import BehaviorTree, Action, Sequence, Condition, Selector

from physic import Physic
from ui import UI
from effect import Effect


class Opponent:
    level1_bgm = None
    level2_bgm = None

    def __init__(self,_act_time, _parry_time,_level):
        self.pos = Vec2(600, 300)
        self.speed = 200
        self.dir = -1  # 음의 x축방향이 정면
        self.hp = 100

        self.acc_parry = 0.0
        self.can_parry = True
        self.cooltime_parry = _parry_time

        self.combo = False
        self.act_time = _act_time

        # < Component >
        self.component = {}

        # animation
        self.cur_ani = 0
        self.ani_reset = False

        if Opponent.level1_bgm == None :
            Opponent.level1_bgm = load_wav('resource/level_easy.wav')

        if Opponent.level2_bgm == None :
            Opponent.level2_bgm = load_wav('resource/level_hard.wav')

        if _level == 1 :
            self.ani = Ani(self, self.pos, "Opp1.png", [8, 12, 7, 7], [128, 128, 200, 200], [130, 120, 203, 203]
                           , self.act_time, Vec2(3, 3), True)
            Opponent.level1_bgm.repeat_play()
            Opponent.level1_bgm.set_volume(64)


        elif _level == 2 :
            self.ani = Ani(self, self.pos, "Opp2.png", [8, 12, 7, 7], [128, 128, 200, 200], [130, 120, 203, 203]
                           , self.act_time, Vec2(3, 3), True)
            Opponent.level2_bgm.repeat_play()
            Opponent.level2_bgm.set_volume(64)

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
                                      , Vec2(0, 60))

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

        if self.hp <0 : self.defeat()

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
        if self.component["PHYSIC"].getAccel().y < 500 and self.pos.y<250 : # 무콤방지
            self.component["PHYSIC"].addForce(Vec2(0, 50))

    def delEffect(self):
        self.component["EFFECT"] = None

    def addForce(self,_rhs):
        self.component["PHYSIC"].addForce(_rhs)

    def parrying(self):
        self.pos.x += self.speed * TimeMgr.GetDt()  # 패링 반작용

        # 충격받음
        self.component["PHYSIC"].addForce(Vec2(1000, 0))
        if self.component["PHYSIC"].getAccel().y < 500 and self.pos.y<250 :
            self.component["PHYSIC"].addForce(Vec2(0, 250))
        self.attackRelease()

        # 패링했는데 공격하면 콤보
        self.combo = True

    def attackRelease(self):
        self.state.attackRelease()

    def setGroggy(self):
        # 충격받음
        self.combo = False
        self.component["PHYSIC"].addForce(Vec2(1000, 0))
        if self.component["PHYSIC"].getAccel().y < 500 and self.pos.y<250 :
            self.component["PHYSIC"].addForce(Vec2(0, 250))

        self.changeEffect("POINT")
        self.state.change_state("GROGGY")

    def changeEffect(self, _effect):
        self.effect[_effect].resetFrame()
        self.component["EFFECT"] = self.effect[_effect]

    def build_behavior_tree(self):
        c_hp_more = Condition("플레이어보다 체력이 많거나 같은가", self.is_more_hp)
        c_hp_less = Condition("플레이어보다 체력이 적은가", self.is_less_hp)

        c_distn = Condition("일정거리 이내", self.is_near_player, 250)
        c_distn_parry = Condition ( "패링거리 이내 ", self.is_near_player, 400)
        c_is_attack = Condition("상대가 공격함", self.is_player_attack)
        c_is_idle = Condition("상대가 Idle", self.is_player_idle)
        c_can_parry = Condition("패링가능", self.is_can_parry)
        c_cur_parry = Condition("현재 자신이 패링중이 아닌가", self.is_not_parrying)
        c_combo= Condition("콤보가능한가", self.is_combo)
        c_is_cur_combo = Condition("지금 자신이 콤보중이 아닌가?", self.is_cur_not_combo)
        c_player_combo = Condition("플레이어가 콤보상태인가?", self.is_player_combo)

        a_combo = Action("콤보 전진",self.move_combo)
        a_move_forward = Action('전진', self.move_forward)  # action node 생성
        a_move_back = Action("후진", self.move_back)

        a_attack_down = Action("공격", self.attack_down)
        a_attack_parrying = Action("패링", self.attack_parrying)

        SEQ_move_by_combo = Sequence("앞으로 이동_by Combo",c_combo,a_combo)
        SEQ_move_by_idle = Sequence("앞으로 이동_by HP", c_cur_parry, c_hp_more, a_move_forward)
        SEQ_move_by_hp = Sequence("앞으로 이동_by IDLE", c_cur_parry, c_is_idle, a_move_forward)
        SEQ_move_froward = Selector("앞으로 이동", SEQ_move_by_hp, SEQ_move_by_idle)

        SEQ_move_back = Sequence("뒤로 이동", c_is_cur_combo,c_cur_parry, c_hp_less, a_move_back)

        SEQ_attack = Sequence("공격", c_player_combo,c_cur_parry, c_distn, a_attack_down)
        SEQ_parrying = Sequence("패링", c_player_combo,c_distn_parry, c_is_attack, c_can_parry, a_attack_parrying)

        root = Selector("콤보/패링/공격/이동/후퇴", SEQ_move_by_combo,SEQ_parrying, SEQ_attack, SEQ_move_froward, SEQ_move_back)

        self.bt = BehaviorTree(root)
        self.component["BT"] = self.bt

    # 플레이어보다 HP 많거나 같은지
    def is_more_hp(self):
        from SceneMgr import SceneMgr
        player = SceneMgr.getCurScene().getObj(OBJ.kPlayer)
        if self.hp >= player[0].hp:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL

    def is_less_hp(self):
        from SceneMgr import SceneMgr
        player = SceneMgr.getCurScene().getObj(OBJ.kPlayer)
        if self.hp < player[0].hp:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL

    def is_near_player(self, _distn):
        from SceneMgr import SceneMgr
        player = SceneMgr.getCurScene().getObj(OBJ.kPlayer)
        if self.pos.x - player[0].getPos().x < _distn:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL

    def is_player_attack(self):
        from SceneMgr import SceneMgr
        player = SceneMgr.getCurScene().getObj(OBJ.kPlayer)
        if player[0].getCurState() == Attack_down or player[0].getCurState() == Attack_up or player[0].getCurState() == Groggy:
            # rate=  random.randint(0,100)
            # if rate > 60 :
            return BehaviorTree.SUCCESS
        return BehaviorTree.FAIL

    def is_player_idle(self):
        from SceneMgr import SceneMgr
        player = SceneMgr.getCurScene().getObj(OBJ.kPlayer)
        if player[0].getCurState() == Idle:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL

    def is_can_parry(self):
        if self.can_parry:
            return BehaviorTree.SUCCESS
        return BehaviorTree.FAIL

    # 현재 자신이 패링중인지 ( 패링중이 아니라면 True )
    def is_not_parrying(self):
        if self.getCurState() == Attack_up_Opp:
            return False
        return True

    def is_combo(self):
        if self.combo : return BehaviorTree.SUCCESS
        return BehaviorTree.FAIL

    def is_cur_not_combo(self):     # 현재 자신이 콤보중이 아닌가 ( 콤보 중이라면 Fail )
        if self.component["PHYSIC"].getAccel().x < 0 : return BehaviorTree.FAIL
        return BehaviorTree.SUCCESS

    def is_player_combo(self): # 플레이어가 콤보 상태가 아닌가?
        from SceneMgr import SceneMgr
        player = SceneMgr.getCurScene().getObj(OBJ.kPlayer)
        if player[0].getAccel().x > 0 : return BehaviorTree.FAIL
        return BehaviorTree.SUCCESS

    def move_combo(self):
        self.addForce(Vec2(-3500,0))
        self.combo= False
        self.state.change_state("ATTACK_DOWN")

    def move_forward(self):
        if self.getCurState() != Front:
            self.state.change_state("FRONT")


    def move_back(self):
        if self.getCurState() != Back:
            self.state.change_state("BACK")

    def attack_down(self):
        if self.getCurState() != Attack_down_Opp:
            self.state.change_state("ATTACK_DOWN")

    def attack_parrying(self):
        if self.getCurState() != Attack_up_Opp:
            self.state.change_state("PARRYING")

    def defeat(self):
        from SceneMgr import SceneMgr
        SceneMgr.getCurScene().sceneChange(scene_result("WIN"))
        Opponent.level1_bgm = None
        Opponent.level2_bgm = None

    def delVolume(self):
        Opponent.level1_bgm = None
        Opponent.level2_bgm = None
