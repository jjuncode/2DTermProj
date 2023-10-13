from src.mgr.ObjMgr import ObjMgr
from pico2d import open_canvas, update_canvas,clear_canvas
from src.mgr.TimeMgr import TimeMgr

class Core:

    def __init__(self):
        open_canvas()
        self.obj = ObjMgr()
        self.TimeMgr = TimeMgr()
        pass

    def update(self):
        self.obj.update()
        self.TimeMgr.update()

    def render(self):
        self.obj.render()
        update_canvas()
        clear_canvas()

    def Quit(self):
        return True
