from src.object.player import Player

class ObjMgr:
    def __init__(self):
        self.player = Player()

    def update(self):
        pass

    def render(self):
        self.player.render()