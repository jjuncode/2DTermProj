from src.struct.struct import Pos
from src.component.ani import Ani
from src.mgr.KeyMgr import KeyMgr
from pico2d import SDLK_a,SDLK_d,SDLK_w,SDLK_s
from src.mgr.TimeMgr import TimeMgr

class Player:
    def __init__(self):
        self.pos = Pos()
        self.speed = 500

        self.ani = Ani("Character.png", [7], 200,200)

    def render(self):
        self.ani.render(self.pos)

    def update(self):
        self.ani.update()
        if ( KeyMgr.key[SDLK_a] == "TAP" or KeyMgr.key[SDLK_a] ==  "HOLD"):
            self.pos.x -= TimeMgr.GetDt() * self.speed
            print(TimeMgr.GetDt() * 100)
        if KeyMgr.key[SDLK_w] == "TAP" or KeyMgr.key[SDLK_w] == "HOLD":
            self.pos.y += TimeMgr.GetDt() * self.speed
        if KeyMgr.key[SDLK_s] == "TAP" or KeyMgr.key[SDLK_s] == "HOLD":
            self.pos.y -=TimeMgr.GetDt() * self.speed
        if KeyMgr.key[SDLK_d] == "TAP" or KeyMgr.key[SDLK_d] == "HOLD":
            self.pos.x +=TimeMgr.GetDt() * self.speed

