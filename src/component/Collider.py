from pico2d import draw_rectangle
from src.component.Component import Component

class Collider(Component) :
    def __init__(self,_owner,_pos,_scale):
        super().__init__(_owner, _pos)
        self.scale = _scale

    def update(self):
        self.pos = self.owner.pos

    def render(self):
        draw_rectangle(self.pos.x - self.scale.x , self.pos.y + self.scale.y
                       , self.pos.x + self.scale.x , self.pos.y - self.scale.y )

    def get_bb(self): # lb rt
        return self.pos.x - self.scale.x , self.pos.y - self.scale.y , self.pos.x + self.scale.x, self.pos.y + self.scale.y

def collide(a, b):
    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()

    if la > rb: return False
    if ra < lb: return False
    if ta < bb: return False
    if ba > tb: return False

    return True