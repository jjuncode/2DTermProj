from src.struct.struct import Pos
from src.component.ani import Ani
from src.mgr.KeyMgr import GetKey
from pico2d import SDLK_a,SDLK_d,SDLK_w,SDLK_s,SDLK_q,SDLK_e
from src.mgr.TimeMgr import TimeMgr

class Player:
    def __init__(self):
        self.pos = Pos()
        self.speed = 500

        # animation
        self.cur_ani = 0
        self.ani_reset = False
        self.ani = Ani("Character.png", [8,12,7,7], [128,128,200,200],[120,120,203,203])

        self.state = StateMachine(self)

    def render(self):
        self.state.render()

    def update(self):
        self.state.update()


class Idle:

    @staticmethod
    def init(_instance):
        _instance.ani.cur_ani = 1
        _instance.ani.ani_reset = True

    @staticmethod
    def update(_instance):
        _instance.ani.update()
        pass

    @staticmethod
    def render(_instance):
        _instance.ani.render(_instance.pos)
        pass


class Run:

    @staticmethod
    def init(_instance):
        _instance.ani.cur_ani = 0
        _instance.ani.ani_reset = True

    @staticmethod
    def update(_instance):
        _instance.ani.update()
        pass

    @staticmethod
    def render(_instance):
        _instance.ani.render(_instance.pos)
        pass

class Attack_up:

    @staticmethod
    def init(_instance):
        _instance.ani.cur_ani = 3
        _instance.ani.ani_reset = True

    @staticmethod
    def update(_instance):
        _instance.ani.update()
        pass

    @staticmethod
    def render(_instance):
        _instance.ani.render(_instance.pos)
        pass


class Attack_down:
    @staticmethod
    def init(_instance):
        _instance.ani.cur_ani = 2
        _instance.ani.ani_reset = True

    @staticmethod
    def update(_instance):
        _instance.ani.update()
        pass

    @staticmethod
    def render(_instance):
        _instance.ani.render(_instance.pos)
        pass
class StateMachine:
    def __init__(self,_instance):
        self.instance = _instance
        self.cur_state = Idle
        self.cur_state.init(self.instance)

    def update_key(self):
        if (GetKey(SDLK_a) == "TAP" or GetKey(SDLK_a) == "HOLD"):
            self.instance.pos.x -= TimeMgr.GetDt() * self.instance.speed
            if self.cur_state != Run :
                self.cur_state = Run
                self.cur_state.init(self.instance)

        elif GetKey(SDLK_w) == "TAP" or GetKey(SDLK_w) == "HOLD":
            self.instance.pos.y += TimeMgr.GetDt() * self.instance.speed
            if self.cur_state != Run:
                self.cur_state = Run
                self.cur_state.init(self.instance)

        elif GetKey(SDLK_s) == "TAP" or GetKey(SDLK_s) == "HOLD":
            self.instance.pos.y -= TimeMgr.GetDt() * self.instance.speed
            if self.cur_state != Run:
                self.cur_state = Run
                self.cur_state.init(self.instance)

        elif GetKey(SDLK_d) == "TAP" or GetKey(SDLK_d) == "HOLD":
            self.instance.pos.x += TimeMgr.GetDt() * self.instance.speed
            if self.cur_state != Run:
                self.cur_state = Run
                self.cur_state.init(self.instance)

        elif GetKey(SDLK_q) == "TAP" or GetKey(SDLK_q) == "HOLD":
            if self.cur_state != Attack_down:
                self.cur_state = Attack_down
                self.cur_state.init(self.instance)

        elif GetKey(SDLK_e) == "TAP" or GetKey(SDLK_e) == "HOLD":
            if self.cur_state != Attack_up:
                self.cur_state = Attack_up
                self.cur_state.init(self.instance)

        else :
            if self.cur_state != Idle:
                self.cur_state = Idle
                self.cur_state.init(self.instance)

    def update(self):
        self.cur_state.update(self.instance)
        self.update_key()

    def render(self):
        self.cur_state.render(self.instance)

