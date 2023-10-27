from src.struct.struct import Vec2
from src.component.ani import Ani

from src.component.Collider import Collider
from src.component.sword import Sword
from src.component.StateMachine import StateMachine
from src.component.Physic import Physic
class Player:
    def __init__(self):
        self.pos = Vec2(400,300)
        self.speed = 1

        # < Component >
        self.component={}

        # animation
        self.cur_ani = 0
        self.ani_reset = False
        self.ani = Ani(self,self.pos,"Character.png", [8,12,7,7], [128,128,200,200],[130,120,203,203]
                       ,0.15,Vec2(3,3))
        self.component["ANI"] = self.ani

        # collider
        self.collider = Collider(self,Vec2(self.pos.x,self.pos.y),Vec2(40,70))
        self.component["COLLIDER"] = self.collider

        # sword
        self.sword = Sword(self,Vec2(self.pos.x,self.pos.y))
        self.component["SWORD"] = self.sword

        # physic
        self.physic = Physic(self,Vec2(self.pos.x,self.pos.y))
        self.component["PHYSIC"] = self.physic

        # < StateMachine >
        self.state = StateMachine(self)

    def render(self):
        self.state.render()
        for key,value in self.component.items() :
            value.render()

    def update(self):
        for key, value in self.component.items():
            value.update()
        self.state.update()

    def getPos(self):
        return Vec2(self.pos.x,self.pos.y)

    def getCurState(self):
        return self.state.cur_state

