from sdl2 import SDLK_SPACE

from src.scene.scene import scene
from src.scene.scene_play import scene_play

from src.object.background.title_background import TitleBackground
from src.object.background.title_fence import TitleFence
from src.object.background.title_logo import TitleLogo
from src.mgr.KeyMgr import IsTapKey

class scene_title(scene):

    def __init__(self):
        super().__init__()
        self.obj[0].append(TitleBackground())
        self.obj[1].append(TitleFence())
        self.obj[2].append(TitleLogo())

    def updateKey(self):
        if IsTapKey(SDLK_SPACE) :
            self.sceneChange(scene_play)
