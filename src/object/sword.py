from src.component.Collider import Collider
from src.struct.struct import Vec2
from src.component.Component import Component
from src.component.StateMachine import Idle, Run, Attack_down, Attack_up, Jump
from src.component.ani import Ani
from src.component.effect import Effect
from src.struct.struct import OBJ

origin_collider_size = Vec2(10, 10)

class Sword(Component):
    def __init__(self, _owner, _pos):
        super().__init__(_owner, _pos)

        # < Component >
        self.component = {}

        # collider
        self.collider = Collider(self, Vec2(self.pos.x, self.pos.y),
                                 Vec2(origin_collider_size.x, origin_collider_size.y))
        from src.object.player import Player
        from src.object.opponent import Opponent
        print(type(_owner))
        if type(_owner) == Player:
            self.collider.setCollPair([OBJ.kOpponent,OBJ.kOpponent_sword])     # 플레이어 -> 적 몸체와 충돌체크, 적 칼과 충돌체크
        elif type(_owner) == Opponent:
            self.collider.setCollPair([OBJ.kPlayer,OBJ.kPlayer_sword])         # 적 -> 플레이어 몸체와 충돌체크, 플레이어 칼과 충돌체크

        self.component["COLLIDER"] = self.collider

        # effect
        self.effect ={}

        # player effect
        if type(_owner) == Player:
            self.effect["EFFECT_ATTACK_UP"] = Effect(self, self.pos
                                                     , Ani(self, self.pos, "parring_purple.png", [5], [123], [30] , 0.15, Vec2(2, 5))
                                                     , Vec2 (0,30))

            self.effect["EFFECT_ATTACK_DOWN"] = Effect(self,self.pos
                                                       ,Ani(self, self.pos, "slash_purple.png", [5], [94], [38],0.15,Vec2(2,5))
                                                       , Vec2 (0,30))
        # opponent effect
        elif type(_owner) == Opponent:
            self.effect["EFFECT_ATTACK_UP"] = Effect(self, self.pos,
                                                     Ani(self, self.pos, "spr_master_slash.png", [5], [123], [30], 0.15, Vec2(2, 5),True)
                                                     , Vec2 (0,30))

            self.effect["EFFECT_ATTACK_DOWN"] = Effect(self, self.pos,
                                                       Ani(self, self.pos, "spr_dragon_slash.png", [5], [94], [38], 0.15, Vec2(2, 5),True)
                                                       , Vec2 (0,30))
    def update(self):
        if self.owner.getCurState() == Idle or self.owner.getCurState() == Run or self.owner.getCurState()==Jump:
            self.pos = self.owner.pos
            self.component["COLLIDER"].scale.x = origin_collider_size.x
            self.component["COLLIDER"].scale.y = origin_collider_size.y

        elif self.owner.getCurState() == Attack_up:
            self.pos.x = self.owner.getPos().x + 25 * self.owner.ani.cur_frame * self.owner.dir
            self.component["COLLIDER"].scale.x = 10 + 10 * (self.owner.ani.cur_frame-1)
            self.component["COLLIDER"].scale.y = 10 + 22 * (self.owner.ani.cur_frame-1)
            self.component["EFFECT"] = self.effect["EFFECT_ATTACK_UP"]

        elif self.owner.getCurState() == Attack_down:
            self.pos.x = self.owner.getPos().x + 25 * self.owner.ani.cur_frame* self.owner.dir
            self.component["COLLIDER"].scale.x = 10 + 15 * (self.owner.ani.cur_frame-1 )
            self.component["COLLIDER"].scale.y = 10 + 15 * (self.owner.ani.cur_frame-1 )
            self.component["EFFECT"] = self.effect["EFFECT_ATTACK_DOWN"]

        for key, value in self.component.items():
            if value != None:
                value.update()

    def render(self):
        for key, value in self.component.items():
            if value != None:
                value.render()

    def getPos(self):
        return self.pos

    def get_bb(self):
        return self.component["COLLIDER"].get_bb()

    def processColl(self):
        pass

    def delEffect(self):
        self.component["EFFECT"] = None
