from src.mgr.ObjMgr import ObjMgr
from pico2d import open_canvas, update_canvas

class Core:

    def __init__(self):
        open_canvas()
        self.obj = ObjMgr()
        pass

    def update(self):
        self.obj.update()

    def render(self):
        update_canvas()
        self.obj.render()

    def Quit(self):
        return True
