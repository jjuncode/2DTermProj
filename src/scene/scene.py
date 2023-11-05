from src.object.player import Player
from src.object.background import BackGround

class scene:
    def __init__(self):
        self.obj = [[],[],[]]

    def update(self):
        for layer in self.obj:
            for obj in layer:
                obj.update()

    def render(self):
        for layer in self.obj:
            for obj in layer:
                obj.render()

    def updateKey(self):
        pass

    @staticmethod
    def sceneChange(_scene):
        from src.mgr.SceneMgr import SceneMgr
        SceneMgr.sceneChange(_scene)
        print(SceneMgr.mgr.cur_scene)
