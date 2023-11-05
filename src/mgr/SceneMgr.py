import pico2d
from src.scene.scene_play import scene_play

class SceneMgr:
    mgr = None

    def __new__(cls):
        if cls.mgr == None:
            cls.mgr = super(SceneMgr, cls).__new__(cls)
            return cls.mgr

    def __init__(self):
        self.cur_scene = scene_play()

    def update(self):
        self.cur_scene.update()

    def render(self):
        self.cur_scene.render()