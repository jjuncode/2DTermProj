from src.component.Collider import Collider
from src.struct.struct import Vec2
from src.component.Component import Component
from src.component.StateMachine import Idle, Run, Attack_down, Attack_up, Jump
from src.component.ani import Ani
from src.component.effect import Effect

origin_collider_size = Vec2(10, 10)


class Sword(Component):
    def __init__(self, _owner, _pos):
        super().__init__(_owner, _pos)

        # < Component >
        self.component = {}

        # collider
        self.collider = Collider(self, Vec2(self.pos.x, self.pos.y),
                                 Vec2(origin_collider_size.x, origin_collider_size.y))
        self.component["COLLIDER"] = self.collider

        # effect
        self.cur_effect = None
        self.effect ={}
        self.effect["EFFECT_ATTACK_UP"] = Effect(self, self.pos, Ani(self, self.pos, "spr_master_slash.png", [5], [123], [30]
                                                             , 0.15, Vec2(2, 5)))

        self.effect["EFFECT_ATTACK_DOWN"] = Effect(self,self.pos,Ani(self, self.pos, "spr_dragon_slash.png", [5], [94], [38]
                       ,0.15,Vec2(2,5)))

    def update(self):
        if self.owner.getCurState() == Idle or self.owner.getCurState() == Run or self.owner.getCurState()==Jump:
            self.pos = self.owner.pos
            self.component["COLLIDER"].scale.x = origin_collider_size.x
            self.component["COLLIDER"].scale.y = origin_collider_size.y

            if self.cur_effect == "EFFECT_ATTACK_UP" or self.cur_effect == "EFFECT_ATTACK_DOWN":
                self.effect[self.cur_effect].ani.cur_frame = 0

        elif self.owner.getCurState() == Attack_up:
            self.pos.x = self.owner.getPos().x + 25 * self.owner.ani.cur_frame
            self.component["COLLIDER"].scale.x = 10 + 10 * (self.owner.ani.cur_frame - 1)
            self.component["COLLIDER"].scale.y = 10 + 22 * (self.owner.ani.cur_frame - 1)
            self.cur_effect = "EFFECT_ATTACK_UP"

        elif self.owner.getCurState() == Attack_down:
            self.pos.x = self.owner.getPos().x + 25 * self.owner.ani.cur_frame
            self.component["COLLIDER"].scale.x = 10 + 15 * (self.owner.ani.cur_frame - 1)
            self.component["COLLIDER"].scale.y = 10 + 15 * (self.owner.ani.cur_frame - 1)
            self.cur_effect = "EFFECT_ATTACK_DOWN"

        # effect
        if self.cur_effect != None :
            self.component["EFFECT"] = self.effect[self.cur_effect]

        for key, value in self.component.items():
            value.update()

    def render(self):
        for key, value in self.component.items():
            value.render()

    def getPos(self):
        return self.pos
