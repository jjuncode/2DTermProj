from pico2d import draw_rectangle
from src.component.Component import Component

class Collider(Component) :
    def __init__(self,_owner,_pos,_scale):
        self.pos = _pos
        self.scale = _scale
        self.owner = _owner

    def update(self):
        self.pos = self.owner.getPos()


    def render(self):
        draw_rectangle(self.pos.x - self.scale.x , self.pos.y + self.scale.y
                       , self.pos.x + self.scale.x , self.pos.y - self.scale.y )
