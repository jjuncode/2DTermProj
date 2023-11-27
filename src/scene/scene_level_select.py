from sdl2 import SDLK_SPACE
from src.struct.struct import OBJ

from src.scene.scene import scene
from src.scene.scene_play import scene_play

from src.object.level_background import LevelBackground
from src.object.level_select import LevelSelect
from src.mgr.KeyMgr import IsTapKey, SetKeyExcept


class scene_level(scene):

    def __init__(self, _max_level):
        super().__init__()
        self.obj[OBJ.kLevel_background.value].append(LevelBackground())
        self.obj[OBJ.kLevel_level.value].append(LevelSelect(_max_level))

    def updateKey(self):
        if IsTapKey(SDLK_SPACE) :
            level = LevelSelect.getCurLevel()
            self.sceneChange(scene_play(level))
            SetKeyExcept(SDLK_SPACE)

