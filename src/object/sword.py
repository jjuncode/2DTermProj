from src.component.collider import Collider
from src.mgr.TimeMgr import TimeMgr
from src.struct.struct import Vec2
from src.component.component import Component
from src.component.stateMachine import Idle, Run, Attack_down, Attack_up, Jump, Groggy, Attack_up_Opp, Attack_down_Opp, \
    Front, Back
from src.component.ani import Ani
from src.component.effect import Effect
from src.struct.struct import OBJ

origin_collider_size = Vec2(0, 0)


class Sword(Component):
    def __init__(self, _owner, _pos):
        super().__init__(_owner, _pos)

        self.damage = 2
        self.is_paryying = False

        # < Component >
        self.component = {}

        # collider
        self.collider = Collider(self, Vec2(self.pos.x, self.pos.y),
                                 Vec2(origin_collider_size.x, origin_collider_size.y))
        from src.object.player import Player
        from src.object.opponent import Opponent
        print(type(_owner))
        if type(_owner) == Player:
            self.collider.setCollPair([OBJ.kOpponent, OBJ.kOpponent_sword])  # 플레이어 -> 적 몸체와 충돌체크, 적 칼과 충돌체크
        elif type(_owner) == Opponent:
            self.collider.setCollPair([OBJ.kPlayer, OBJ.kPlayer_sword])  # 적 -> 플레이어 몸체와 충돌체크, 플레이어 칼과 충돌체크

        self.component["COLLIDER"] = self.collider

        # effect
        self.effect = {}

        # parrying effect
        self.effect["EFFECT_PARRYING"] = Effect(self, self.pos
                                                , Ani(self, self.pos, "spark.png", [5], [70], [64], 0.15, Vec2(7, 7))
                                                , Vec2(0, 30))
        # player effect
        if type(_owner) == Player:
            self.effect["EFFECT_ATTACK_UP"] = Effect(self, self.pos
                                                     , Ani(self, self.pos, "parring_purple.png", [5], [123], [30], 0.15,
                                                           Vec2(2, 5))
                                                     , Vec2(0, 30))

            self.effect["EFFECT_ATTACK_DOWN"] = Effect(self, self.pos
                                                       , Ani(self, self.pos, "slash_purple.png", [5], [94], [38], 0.15,
                                                             Vec2(2, 5))
                                                       , Vec2(0, 30))
        # opponent effect
        elif type(_owner) == Opponent:
            self.effect["EFFECT_ATTACK_UP"] = Effect(self, self.pos,
                                                     Ani(self, self.pos, "spr_master_slash.png", [5], [123], [30], 0.15,
                                                         Vec2(2, 5), True)
                                                     , Vec2(0, 30))

            self.effect["EFFECT_ATTACK_DOWN"] = Effect(self, self.pos,
                                                       Ani(self, self.pos, "spr_dragon_slash.png", [5], [94], [38],
                                                           0.15, Vec2(2, 5), True)
                                                       , Vec2(0, 30))

        # 기본 이펙트는 공통분모인 패링 이펙트
        self.component["EFFECT"] = self.effect["EFFECT_PARRYING"]

    def update(self):
        self.is_paryying = False  # 패링 해제

        for key, value in self.component.items():
            if value != None:
                value.update()

        if self.owner.getCurState() == Idle or self.owner.getCurState() == Run or self.owner.getCurState() == Jump or self.owner.getCurState() == Groggy \
                or self.owner.getCurState() == Front or self.owner.getCurState() == Back:
            self.pos = self.owner.pos
            self.component["COLLIDER"].scale.x = origin_collider_size.x
            self.component["COLLIDER"].scale.y = origin_collider_size.y

        # 패링 -> 흠..
        if self.is_paryying:
            self.component["COLLIDER"].pos = self.owner.pos
            self.component["COLLIDER"].scale.x = origin_collider_size.x
            self.component["COLLIDER"].scale.y = origin_collider_size.y

        # 패링중일 때는 공격이펙트 안나옴
        else:
            if self.owner.getCurState() == Attack_up or self.owner.getCurState() == Attack_up_Opp:
                self.pos.x = self.owner.getPos().x + 25 * self.owner.ani.cur_frame * self.owner.dir
                self.component["COLLIDER"].scale.x = 10 + 10 * (self.owner.ani.cur_frame - 1)
                self.component["COLLIDER"].scale.y = 10 + 22 * (self.owner.ani.cur_frame - 1)
                self.component["EFFECT"] = self.effect["EFFECT_ATTACK_UP"]

            elif self.owner.getCurState() == Attack_down or self.owner.getCurState() == Attack_down_Opp:
                self.pos.x = self.owner.getPos().x + 25 * self.owner.ani.cur_frame * self.owner.dir
                self.component["COLLIDER"].scale.x = 10 + 15 * (self.owner.ani.cur_frame - 1)
                self.component["COLLIDER"].scale.y = 10 + 15 * (self.owner.ani.cur_frame - 1)
                self.component["EFFECT"] = self.effect["EFFECT_ATTACK_DOWN"]

    def render(self):
        for key, value in self.component.items():
            if value != None:
                value.render()

    def getPos(self):
        return self.pos

    def get_bb(self):
        return self.component["COLLIDER"].get_bb()

    def processColl(self, _obj):
        # 데미지 입히기
        if hasattr(_obj, "hp"):  # 몸체끼리
            _obj.hp -= self.damage  # 데미지 입힘
        else:  # 칼끼리
            if self.owner.getCurState() == Attack_up or self.owner.getCurState() == Attack_up_Opp:
                # 내가 Up 공격일 때
                # 내가 Up공격일 때 Down 공격을 막는다.
                # 내가 Up공격일 때 상대가 Up 공격이라면 둘다 그로기, 패링
                if _obj.owner.getCurState() == Attack_up or _obj.owner.getCurState() == Attack_up_Opp:
                    self.owner.setGroggy()
                    _obj.owner.parrying()

                self.owner.parrying()  # 주인장은 패링
                _obj.owner.setGroggy()  # 상대방은 그로기

                self.is_paryying = True

                # 패링 이펙트
                self.effect["EFFECT_PARRYING"].resetFrame()
                self.component["EFFECT"] = self.effect["EFFECT_PARRYING"]
                self.component["EFFECT"].setPos(Vec2(self.pos.x + (_obj.pos.x - self.pos.x) / 2,
                                                     self.pos.y + (_obj.pos.y - self.pos.y) / 2))  # 충돌위치의 중간 ㄷ

        # 내가 Down공격일 때 안막는다.

    def delEffect(self):
        self.component["EFFECT"] = None

    def setDamage(self, _rhs):
        self.damage = _rhs
