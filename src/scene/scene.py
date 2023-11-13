from src.struct.struct import OBJ

class scene:
    def __init__(self):
        self.obj = [ [] for _ in range(0,OBJ.END.value)] # Obj Group으로 분류
        self.coll_group = {}

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


