from TimeMgr import TimeMgr
from mystruct import OBJ

from scene import scene
from scene_level_select import scene_level

from title_background import TitleBackground
from title_fence import TitleFence
from title_logo import TitleLogo


class scene_title(scene):

    def __init__(self):
        super().__init__()
        self.obj[OBJ.kTitle_background.value].append(TitleBackground())
        self.obj[OBJ.kTitle_fence.value].append(TitleFence())
        self.obj[OBJ.kTitle_logo.value].append(TitleLogo())
        self.acc = 0.0

    def updateKey(self):
        self.acc += TimeMgr.GetDt()
        if self.acc > 3.0 : self.sceneChange(scene_level(1))
