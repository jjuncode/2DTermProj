from src.struct.struct import Pos
from src.component.ani import Ani
from src.mgr.KeyMgr import GetKey
from pico2d import SDLK_a,SDLK_d,SDLK_w,SDLK_s,SDLK_q,SDLK_e
from src.mgr.TimeMgr import TimeMgr

class Player:
    def __init__(self):
        self.pos = Pos()
        self.speed = 500

        self.state = StateMachine(self)

        # animation
        self.cur_ani = 0
        self.ani_reset = False
        self.ani = Ani("Character.png", [8,12,7,7], [128,128,200,200],[120,120,210,210])

    def UpdateKey(self):
        if (GetKey(SDLK_a) == "TAP" or GetKey(SDLK_a) == "HOLD"):
            self.pos.x -= TimeMgr.GetDt() * self.speed
        if GetKey(SDLK_w) == "TAP" or GetKey(SDLK_w) == "HOLD":
            self.pos.y += TimeMgr.GetDt() * self.speed
        if GetKey(SDLK_s) == "TAP" or GetKey(SDLK_s) == "HOLD":
            self.pos.y -= TimeMgr.GetDt() * self.speed
        if GetKey(SDLK_d) == "TAP" or GetKey(SDLK_d) == "HOLD":
            self.pos.x += TimeMgr.GetDt() * self.speed
        if GetKey(SDLK_q) == "TAP" or GetKey(SDLK_q) == "HOLD":
            self.ani.cur_ani = 2
            self.ani_reset = True
        if GetKey(SDLK_e) == "TAP" or GetKey(SDLK_e) == "HOLD":
            self.ani.cur_ani = 3
            self.ani_reset = True

    def render(self):
        self.ani.render(self.pos)

    def update(self):
        self.UpdateKey()
        self.ani.update()


class Idle:

    @staticmethod
    def init(_instance):
        _instance.ani.cur_ani = 0

    @staticmethod
    def update(_instance):
        _instance.ani.update(False)
        pass

    @staticmethod
    def render(_instance):
        _instance.ani.render(_instance.pos,_instance.dir)
        pass



class StateMachine:
    def __init__(self,_instance):
        self.instance = _instance
        self.cur_state = Idle

    def update(self):
        self.cur_state.update(self.instance)

    def render(self):
        self.cur_state.render(self.instance)
