from pico2d import load_wav

from TimeMgr import TimeMgr
from mystruct import OBJ

from scene import scene
from scene_level_select import scene_level

from title_background import TitleBackground
from title_fence import TitleFence
from title_logo import TitleLogo


class scene_title(scene):
    bgm = None

    def __init__(self):
        super().__init__()
        self.obj[OBJ.kTitle_background.value].append(TitleBackground())
        self.obj[OBJ.kTitle_fence.value].append(TitleFence())
        self.obj[OBJ.kTitle_logo.value].append(TitleLogo())
        self.acc = 0.0
        if scene_title.bgm == None :
            scene_title.bgm = load_wav("resource/parrying_sound.wav")
    def updateKey(self):
        self.acc += TimeMgr.GetDt()
        if self.acc > 3.0 :
            self.sceneChange(scene_level(1))
            self.bgm.play()
            self.bgm.set_volume(64)
