from src.component.Collider import Collider
from src.struct.struct import Vec2
from src.component.Component import Component
from src.component.StateMachine import Idle, Run, Attack_down, Attack_up
from src.component.ani import Ani

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

        # ani
        self.ani = Ani(self,self.pos,"Character.png", [8,12,7,7], [128,128,200,200],[130,120,203,203])

    def update(self):
        if self.owner.getCurState() == Idle or self.owner.getCurState() == Run:
            self.pos = self.owner.getPos()
            self.component["COLLIDER"].scale.x = origin_collider_size.x
            self.component["COLLIDER"].scale.y = origin_collider_size.y

        elif self.owner.getCurState() == Attack_up:
            self.pos.x = self.owner.getPos().x + 25 * self.owner.ani.cur_frame
            self.component["COLLIDER"].scale.x = 10 + 10 * (self.owner.ani.cur_frame - 1)
            self.component["COLLIDER"].scale.y = 10 + 22 * (self.owner.ani.cur_frame - 1)


        elif self.owner.getCurState() == Attack_down:
            self.pos.x = self.owner.getPos().x + 25 * self.owner.ani.cur_frame
            self.component["COLLIDER"].scale.x = 10 + 15 * (self.owner.ani.cur_frame - 1)
            self.component["COLLIDER"].scale.y = 10 + 15 * (self.owner.ani.cur_frame - 1)

        for key, value in self.component.items():
            value.update()
        pass

    def render(self):
        for key, value in self.component.items():
            value.render()

    def getPos(self):
        return self.pos
