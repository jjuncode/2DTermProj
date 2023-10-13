from src.mgr.ObjMgr import ObjMgr
from pico2d import open_canvas, update_canvas,clear_canvas
from src.mgr.TimeMgr import TimeMgr

class Core:
    mgr = None

    def __new__(cls):
        if cls.mgr == None:
            cls.mgr = super(Core,cls).__new__(cls)
            return cls.mgr

    def __init__(self):
        open_canvas()
        self.objMgr = ObjMgr()
        self.TimeMgr = TimeMgr()

    def update(self):
        self.objMgr.update()
        self.TimeMgr.update()

    def render(self):
        self.objMgr.render()
        update_canvas()
        clear_canvas()

    def Quit(self):
        return True
