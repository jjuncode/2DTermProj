from src.struct.struct import OBJ

class scene:
    def __init__(self):
        self.obj = [ [] for _ in range(0,OBJ.END.value)] # Obj Group으로 분류
        self.coll_group = {}

        # < Component >
        self.component = {}

    def update(self):
        for layer in self.obj:
            for obj in layer:
                obj.update()

        for key, value in self.component.items():
            if value != None:
                value.update()

    def render(self):
        for layer in self.obj:
            for obj in layer:
                obj.render()

        for key, value in self.component.items():
            if value != None:
                value.render()
    def updateKey(self):
        pass

    @staticmethod
    def sceneChange(_scene):
        from src.mgr.SceneMgr import SceneMgr
        SceneMgr.sceneChange(_scene)

    def getObj(self, _OBJ):
        return self.obj[_OBJ.value]
