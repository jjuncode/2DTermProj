from src.component.Collider import Collider
from src.struct.struct import Vec2
from src.component.Component import Component
from src.component.StateMachine import Idle,Run,Attack_down,Attack_up
from src.mgr.TimeMgr import TimeMgr

class Sword(Component):
    def __init__(self,_owner,_pos):
        super().__init__(_owner, _pos)

        # < Component >
        self.component= {}
        self.collider = Collider(self,Vec2(self.pos.x,self.pos.y),Vec2(50,10))
        self.component["COLLIDER"] = self.collider

    def update(self):
        if self.owner.getCurState() == Idle or self.owner.getCurState() == Run:
            self.pos = self.owner.getPos()
        elif self.owner.getCurState() == Attack_up:
            self.pos.x += TimeMgr.GetDt() * 100
            pass
        elif self.owner.getCurState() == Attack_down:
            pass

        for key, value in self.component.items():
            value.update()
        pass

    def render(self):
        for key,value in self.component.items():
            value.render()

    def getPos(self):
        return self.pos