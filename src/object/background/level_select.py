from sdl2 import SDLK_DOWN, SDLK_UP

from src.struct.struct import Vec2
from pico2d import load_image
from src.component.ani import CreatePath
from src.mgr.KeyMgr import IsTapKey, SetKeyNone


class LevelSelect:
    level1 = None
    level2 = None

    def __init__(self,_max_level):
        self.pos = Vec2(400,450)
        self.max_level = _max_level

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

        if self.max_level == 2 :
            # max level이 2일 때
            # 2레벨까지 선택가능
            if self.cur_level % 2 == 0 : self.cur_image = LevelSelect.level2
            else: self.cur_image = LevelSelect.level1

        elif self.max_level == 1 :
            # max level이 1일때 
            # 1레벨만 선택가능
            self.cur_image = LevelSelect.level1