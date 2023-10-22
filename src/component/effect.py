from src.component.Collider import Collider
from src.struct.struct import Vec2
from src.component.Component import Component
from src.component.StateMachine import Idle, Run, Attack_down, Attack_up
from src.component.ani import Ani

origin_collider_size = Vec2(10, 10)


class Effect(Component):
    def __init__(self, _owner, _pos):
        super().__init__(_owner, _pos)

        # < Component >
        self.component = {}

        # collider
        self.ani = Ani(self, self.pos, "spr_dragon_slash.png", [5], [94], [38]
                       ,0.15,Vec2(1,3))
        self.component["ANI"] = self.ani

    def update(self):
        self.pos = self.owner.pos

        for key, value in self.component.items():
            value.update()

    def render(self):
        if self.owner.owner.getCurState() == Attack_up or self.owner.owner.getCurState() == Attack_down:
            if self.owner.owner.ani.cur_frame ==0 :
                self.ani.cur_frame = 0
            for key, value in self.component.items():
                value.render()
        else:
            self.ani.cur_frame = 0

    def getPos(self):
        return self.pos
