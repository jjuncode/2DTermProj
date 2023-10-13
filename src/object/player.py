from src.struct.struct import Pos
from src.component.ani import Ani
from src.mgr.KeyMgr import GetKey
from pico2d import SDLK_a,SDLK_d,SDLK_w,SDLK_s,SDLK_1,SDLK_2,SDLK_3,SDLK_4
from src.mgr.TimeMgr import TimeMgr

class Player:
    def __init__(self):
        self.pos = Pos()
        self.speed = 500

        # animation
        self.cur_ani = 0
        self.ani_reset = False
        self.ani = Ani("Character.png", [8,12,7,7], [128,128,200,200],[120,120,210,210])

    def render(self):
        self.ani.render(self.pos)

    def update(self):
        if ( GetKey(SDLK_a) == "TAP" or GetKey(SDLK_a) ==  "HOLD"):
            self.pos.x -= TimeMgr.GetDt() * self.speed
            print(TimeMgr.GetDt() * 100)
        if GetKey(SDLK_w) == "TAP" or GetKey(SDLK_w) == "HOLD":
            self.pos.y += TimeMgr.GetDt() * self.speed
        if GetKey(SDLK_s) == "TAP" or GetKey(SDLK_s) == "HOLD":
            self.pos.y -=TimeMgr.GetDt() * self.speed
        if GetKey(SDLK_d) == "TAP" or GetKey(SDLK_d) == "HOLD":
            self.pos.x +=TimeMgr.GetDt() * self.speed

        if GetKey(SDLK_1) == "TAP":
            self.cur_ani = 0
            self.ani_reset = True
        if GetKey(SDLK_2) == "TAP":
            self.cur_ani = 1
            self.ani_reset = True
        if GetKey(SDLK_3) == "TAP":
            self.ani_reset = True
            self.cur_ani = 2
        if GetKey(SDLK_4) == "TAP":
            self.ani_reset = True
            self.cur_ani = 3

        self.ani.update(self.cur_ani,self.ani_reset)
        self.ani_reset = False

