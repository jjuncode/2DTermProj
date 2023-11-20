from sdl2 import SDLK_SPACE
from src.struct.struct import OBJ

from src.scene.scene import scene
from src.scene.scene_play import scene_play

from src.object.background.level_background import LevelBackground
from src.mgr.KeyMgr import IsTapKey
class scene_level(scene):

    def __init__(self):
        super().__init__()
        self.obj[OBJ.kLevel_background.value].append(LevelBackground())

    def updateKey(self):
        if IsTapKey(SDLK_SPACE) :
            self.sceneChange(scene_play())
