from src.object.player import Player
from src.object.background import BackGround

class ObjMgr:
    mgr = None

    def __new__(cls):
        if cls.mgr == None:
            cls.mgr = super(ObjMgr,cls).__new__(cls)
            return cls.mgr

    def __init__(self):
        self.obj = [[],[]]
        self.obj[1].append(Player())
        self.obj[0].append(BackGround())

    def update(self):
        for layer in self.obj:
            for obj in layer:
                obj.update()

    def render(self):
        for layer in self.obj:
            for obj in layer:
                obj.render()
