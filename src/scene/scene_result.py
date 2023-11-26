from sdl2 import SDLK_SPACE

from src.scene.scene import scene
from src.object.background.background import BackGround
from src.struct.struct import OBJ
from src.mgr.KeyMgr import IsTapKey, SetKeyExcept


class scene_result(scene):

    def __init__(self, _result):
        super().__init__()
        # Background
        if _result == "DEFEAT" :
            background = BackGround("RESULT_DEFEAT")
            self.obj[OBJ.kBackground.value].append(background)
        elif _result == "WIN":
            background = BackGround("RESULT_WIN")
            self.obj[OBJ.kBackground.value].append(background)

    def updateKey(self):
        from src.scene.scene_level_select import scene_level
        if IsTapKey(SDLK_SPACE):
            self.sceneChange(scene_level())
            SetKeyExcept(SDLK_SPACE)
