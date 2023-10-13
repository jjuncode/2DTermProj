from src.struct.struct import Pos
from src.component.ani import Ani
from src.mgr.KeyMgr import KeyMgr
from pico2d import SDLK_a,SDLK_d,SDLK_z


class Player:
    def __init__(self):
        self.pos = Pos()
        self.ani = Ani("Attacks.png", [])

    def render(self):
        self.ani.render()

    def update(self):
        self.ani.update()
        if KeyMgr.GetKey(SDLK_z) == "TAP": print(" Z : TAP")
        elif KeyMgr.GetKey(SDLK_z) == "HOLD" : print(" Z: HOLD")

