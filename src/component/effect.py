from src.component.Collider import Collider
from src.struct.struct import Vec2
from src.component.Component import Component
from src.component.StateMachine import Idle, Run, Attack_down, Attack_up
from src.component.ani import Ani


class Effect(Component):
    def __init__(self, _owner, _pos, ani,_offset=Vec2(0,0)):
        super().__init__(_owner, _pos)
        self.offset = _offset

        # < Component >
        self.component = {}

        # ani
        self.ani = ani
        self.ani.owner = self

        self.component["ANI"] = self.ani

    def update(self):
        self.pos = Vec2(self.owner.pos.x + self.offset.x, self.owner.pos.y + self.offset.y)

        for key, value in self.component.items():
            value.update()

    def render(self):
        # if self.owner.owner.getCurState() == Attack_up or self.owner.owner.getCurState() == Attack_down:
        #     if self.owner.owner.ani.cur_frame == 0:
        #         self.ani.cur_frame = 0
            for key, value in self.component.items():
                value.render()
        # else:
        #     self.ani.cur_frame = 0

    def getPos(self):
        return self.pos
