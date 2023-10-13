from src.object.player import Player

class ObjMgr:
    mgr = None

    def __new__(cls):
        if cls.mgr == None:
            cls.mgr = super(ObjMgr,cls).__new__(cls)
            return cls.mgr

    def __init__(self):
        self.obj = []
        self.obj.append(Player())

    def update(self):
        for obj in self.obj:
            obj.update()

    def render(self):
        for obj in self.obj:
            obj.render()
