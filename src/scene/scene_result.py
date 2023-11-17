from src.scene.scene import scene
from src.object.background.background import BackGround
from src.struct.struct import OBJ


class scene_result(scene):

    def __init__(self):
        super().__init__()
        # Background
        background = BackGround("RESULT_DEFEAT")
        self.obj[OBJ.kBackground.value].append(background)

