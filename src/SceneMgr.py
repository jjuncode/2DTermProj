from scene_title import scene_title
from TimeMgr import TimeMgr


class SceneMgr:
    mgr = None

    def __new__(cls):
        if cls.mgr == None:
            cls.mgr = super(SceneMgr, cls).__new__(cls)
            return cls.mgr

    def __init__(self):
        # self.cur_scene = scene_play()
        self.cur_scene = scene_title()
        self.acc = 0

    def update(self):
        self.cur_scene.update()
        self.cur_scene.updateKey()

        self.acc += TimeMgr.GetDt()
        if self.acc > 1:
            self.acc = 0

    def render(self):
        self.cur_scene.render()

    @staticmethod
    def sceneChange(_scene):
        del SceneMgr.mgr.cur_scene
        SceneMgr.mgr.cur_scene = _scene

    @staticmethod
    def getCurScene():
        return SceneMgr.mgr.cur_scene
