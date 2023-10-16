from src.component.Collider import Collider
from src.struct.struct import Vec2
from src.component.Component import Component

class Sword(Component):
    def __init__(self,_owner):
        self.owner = _owner
        self.pos = _owner.getPos()
        self.collider = Collider(self,self.pos,Vec2(50,10))

    def update(self):
        self.pos = self.owner.getPos()

    def render(self):
        self.collider.render()
