from src.struct.struct import Vec2
from src.component.ani import Ani
from src.mgr.KeyMgr import GetKey,IsTapKey
from pico2d import SDLK_a,SDLK_d,SDLK_w,SDLK_s,SDLK_q,SDLK_e,get_time
from src.mgr.TimeMgr import TimeMgr

class Player:
    def __init__(self):
        self.pos = Vec2()
        self.speed = 500
        self.dir = Vec2()

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

    @staticmethod
    def exit(_instance):
        pass

class Run:

    @staticmethod
    def init(_instance):
        _instance.ani.cur_ani = 0
        _instance.ani.ani_reset = True
        if IsTapKey(SDLK_a) : _instance.dir.x -=1
        if IsTapKey(SDLK_d) : _instance.dir.x += 1
        if IsTapKey(SDLK_w) : _instance.dir.y += 1
        if IsTapKey(SDLK_s) : _instance.dir.y -= 1

    @staticmethod
    def update(_instance):
        _instance.ani.update()
        _instance.pos.x += 1
        pass

    @staticmethod
    def render(_instance):
        _instance.ani.render(_instance.pos)
        pass

    @staticmethod
    def exit(_instance):
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

    @staticmethod
    def exit(_instance):
        pass


class Attack_down:
    @staticmethod
    def init(_instance):
        _instance.ani.cur_ani = 2
        _instance.ani.ani_reset = True

    @staticmethod
    def update(_instance):
        _instance.ani.update()

    @staticmethod
    def render(_instance):
        _instance.ani.render(_instance.pos)
        pass

    @staticmethod
    def exit(_instance):
        pass


class StateMachine:
    def __init__(self,_instance):
        self.instance = _instance
        self.cur_state = Idle
        self.cur_state.init(self.instance)
        self.transition = {
            Idle : { SDLK_e :Attack_down, SDLK_q : Attack_up, SDLK_w : Run,SDLK_s:Run, SDLK_a : Run, SDLK_d : Run},
            Run : {SDLK_e : Attack_down, SDLK_q : Attack_up},
            Attack_up : { SDLK_e :Attack_down, SDLK_w : Run,SDLK_s:Run, SDLK_a : Run, SDLK_d : Run},
            Attack_down: {SDLK_q: Attack_up, SDLK_w: Run, SDLK_s: Run, SDLK_a: Run, SDLK_d: Run}
        }

    def update(self):
        self.cur_state.update(self.instance)
        self.update_key()
        self.change_state()


    def render(self):
        self.cur_state.render(self.instance)

    def change_state(self):
        for cur_key, next_state in self.transition[self.cur_state].items():
            if GetKey(cur_key) == "TAP" or GetKey(cur_key) == "HOLD":
                self.cur_state = next_state
                self.cur_state.init(self.instance)

    def update_key(self):
        pass
