from sdl2 import SDLK_SPACE,SDLK_DOWN
from pico2d import draw_rectangle
from src.struct.struct import OBJ

from src.scene.scene import scene
from src.scene.scene_play import scene_play

from src.object.background.level_background import LevelBackground
from src.object.background.level_select import LevelSelect
from src.mgr.KeyMgr import IsTapKey, SetKeyExcept


class scene_level(scene):

    def __init__(self):
        super().__init__()
        self.obj[OBJ.kLevel_background.value].append(LevelBackground())
        self.obj[OBJ.kLevel_level.value].append(LevelSelect())

    def updateKey(self):
        if IsTapKey(SDLK_SPACE) :
            self.sceneChange(scene_play())
            SetKeyExcept(SDLK_SPACE)

