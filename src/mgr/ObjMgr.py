from src.object.player import Player

class ObjMgr:
    mgr = None

    def __new__(cls):
        if cls.mgr == None:
            cls.mgr = super(ObjMgr,cls).__new__(cls)
            return cls.mgr

    def __init__(self):
        self.player = Player()

    def update(self):
        self.player.update()

    def render(self):
        self.player.render()