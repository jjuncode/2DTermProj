from src.scene.scene import scene
from src.object.background.background import BackGround
from src.struct.struct import OBJ


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
