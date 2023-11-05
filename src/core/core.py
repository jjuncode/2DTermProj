from src.mgr.SceneMgr import SceneMgr
from pico2d import open_canvas, update_canvas,clear_canvas,SDLK_ESCAPE
from src.mgr.TimeMgr import TimeMgr
from src.mgr.KeyMgr import GetKey,KeyMgr

class Core:
    mgr = None
    quit = False

    def __new__(cls):
        if cls.mgr == None:
            cls.mgr = super(Core,cls).__new__(cls)
            return cls.mgr

    def __init__(self):
        open_canvas()
        self.SceneMgr = SceneMgr()
        self.TimeMgr = TimeMgr()
        self.KeyMgr = KeyMgr()

    def update(self):
        self.SceneMgr.update()
        self.TimeMgr.update()
        self.KeyMgr.update()

        if GetKey(SDLK_ESCAPE) == "TAP":
            self.quit = True


    def render(self):
        self.SceneMgr.render()
        update_canvas()
        clear_canvas()

    def Quit(self):
        return not self.quit
