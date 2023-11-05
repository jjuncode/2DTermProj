import pico2d
from src.scene.scene_play import scene_play
from src.scene.scene_title import scene_title
from src.mgr.TimeMgr import TimeMgr

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
        if self.acc >1 :
            self.acc = 0

    def render(self):
        self.cur_scene.render()

    @staticmethod
    def sceneChange(_scene):
        SceneMgr.mgr.cur_scene = _scene()
