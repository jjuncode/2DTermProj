from sdl2 import SDLK_SPACE

from ani import Ani
from effect import Effect
from TimeMgr import TimeMgr
from scene import scene
from background import BackGround
from mystruct import OBJ, Vec2
from KeyMgr import IsTapKey, SetKeyExcept


class scene_result(scene):

    def __init__(self, _result):
        super().__init__()
        # Background
        self.result = _result
        if _result == "DEFEAT" :
            background = BackGround("RESULT_DEFEAT")
            self.obj[OBJ.kBackground.value].append(background)
        elif _result == "WIN":
            background = BackGround("RESULT_WIN")
            self.obj[OBJ.kBackground.value].append(background)
        self.is_next = False
        self.acc = 0
        self.pos = Vec2(400,300)

        self.effect = {}
        self.effect["RESULT"] = Effect(self, self.pos,
                                      Ani(self, self.pos, "effect_result.png", [8], [320], [240]
                                          , 0.2 ,Vec2(3,3)))

    def updateKey(self):
        from scene_level_select import scene_level
        if IsTapKey(SDLK_SPACE) :
            SetKeyExcept(SDLK_SPACE)
            self.component["EFFECT"] = self.effect["RESULT"]
            self.is_next = True

        if self.is_next :
            self.acc += TimeMgr.GetDt()

            if self.acc > 1.4 :
                self.acc = 0

                if self.result == "DEFEAT":
                    self.sceneChange(scene_level(1))
                else :
                    self.sceneChange(scene_level(2))

    def delEffect(self):
        self.component["EFFECT"] = None
