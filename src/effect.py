from mystruct import Vec2
from component import Component


class Effect(Component):
    def __init__(self, _owner, _pos, ani,_offset=Vec2(0,0)):
        super().__init__(_owner, _pos)
        self.offset = _offset
        self.pos_set = False

        # < Component >
        self.component = {}

        # ani
        self.ani = ani
        self.ani.owner = self

        self.component["ANI"] = self.ani

    def update(self):
        if not self.pos_set:
            self.pos = Vec2(self.owner.pos.x + self.offset.x, self.owner.pos.y + self.offset.y)

        # effect는 한번 재생하면 종료한다.
        if self.ani.cur_frame == self.ani.max_frame[self.ani.cur_ani]-1 : self.owner.delEffect()

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

    def resetFrame(self):
        self.ani.cur_frame = 0

    def setPos(self,_rhs):
        self.pos = _rhs
        self.pos_set = True # 위치고장
