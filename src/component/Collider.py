from pico2d import draw_rectangle
from src.component.Component import Component


class Collider(Component) :
    def __init__(self,_owner,_pos,_scale):
        super().__init__(_owner, _pos)
        self.scale = _scale
        self.collision_pair = [] # OBJ 충돌할거

    def update(self):
        self.pos = self.owner.pos
        self.checkColl()

    def render(self):
        draw_rectangle(self.pos.x - self.scale.x , self.pos.y + self.scale.y
                       , self.pos.x + self.scale.x , self.pos.y - self.scale.y )

    def setCollPair(self,rhs):
        self.collision_pair = rhs

    def get_bb(self): # lb rt
        return self.pos.x - self.scale.x , self.pos.y - self.scale.y , self.pos.x + self.scale.x, self.pos.y + self.scale.y

    def checkColl(self):
        for pair_value in self.collision_pair:
            from src.mgr.SceneMgr import SceneMgr
            obj_arr = SceneMgr.getCurScene().getObj(pair_value) # 충돌할 그룹의 obj를 가져온다.
            for obj in obj_arr :
                if collide(self.get_bb(),obj.get_bb()):         # 가져온 obj들과 충돌검사를 한다.
                    self.owner.processColl()
                    obj.processColl()
                    print("충돌객체 : ", type(self.owner))
                    print("충돌객체 : ", type(obj))


def collide(a, b):
    la, ba, ra, ta = a
    lb, bb, rb, tb = b

    if la > rb: return False
    if ra < lb: return False
    if ta < bb: return False
    if ba > tb: return False

    return True