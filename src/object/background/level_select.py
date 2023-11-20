from sdl2 import SDLK_DOWN, SDLK_UP

from src.struct.struct import Vec2
from pico2d import load_image
from src.component.ani import CreatePath
from src.mgr.KeyMgr import IsTapKey, SetKeyNone


class LevelSelect:
    level1 = None
    level2 = None

    def __init__(self):
        self.pos = Vec2(400,450)
        if LevelSelect.level1 == None:
           LevelSelect.level1  = load_image(CreatePath('level.png'))
        if LevelSelect.level2 == None:
            LevelSelect.level2  = load_image(CreatePath('level2.png'))
        self.cur_image = LevelSelect.level1
        self.cur_level = 1

    def render(self):
        self.cur_image.draw(self.pos.x,self.pos.y,250,250)

    def update(self):
        if IsTapKey(SDLK_DOWN) :
            self.cur_level += 1
            SetKeyNone(SDLK_DOWN)
        elif IsTapKey(SDLK_UP) :
            self.cur_level -=1
            SetKeyNone(SDLK_UP)

        if self.cur_level % 2 == 0 : self.cur_image = LevelSelect.level2
        else : self.cur_image = LevelSelect.level1