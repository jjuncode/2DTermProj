from pico2d import load_wav
from sdl2 import SDLK_SPACE
from mystruct import OBJ

from scene import scene
from scene_play import scene_play

from level_background import LevelBackground
from level_select import LevelSelect
from KeyMgr import IsTapKey, SetKeyExcept


class scene_level(scene):
    bgm = None

    def __init__(self, _max_level):
        super().__init__()
        if scene_level.bgm == None :
            scene_level.bgm = load_wav('resource/bgm_title.wav')
            scene_level.bgm.repeat_play()

        scene_level.bgm.set_volume(64)

        self.obj[OBJ.kLevel_background.value].append(LevelBackground())
        self.obj[OBJ.kLevel_level.value].append(LevelSelect(_max_level))


    def updateKey(self):
        if IsTapKey(SDLK_SPACE) :
            level = LevelSelect.getCurLevel()
            self.sceneChange(scene_play(level))
            SetKeyExcept(SDLK_SPACE)
            scene_level.bgm = None

