from src.mgr.ObjMgr import ObjMgr
from pico2d import open_canvas, update_canvas,clear_canvas,SDLK_ESCAPE
from src.mgr.TimeMgr import TimeMgr
from src.mgr.KeyMgr import KeyMgr

class Core:
    mgr = None
    quit = False

    def __new__(cls):
        if cls.mgr == None:
            cls.mgr = super(Core,cls).__new__(cls)
            return cls.mgr

    def __init__(self):
        open_canvas()
        self.objMgr = ObjMgr()
        self.TimeMgr = TimeMgr()
        self.KeyMgr = KeyMgr()

    def update(self):
        self.objMgr.update()
        self.TimeMgr.update()
        self.KeyMgr.update()

        if KeyMgr.GetKey(SDLK_ESCAPE) == "TAP":
            self.quit = True


    def render(self):
        self.objMgr.render()
        update_canvas()
        clear_canvas()

    def Quit(self):
        return not self.quit
