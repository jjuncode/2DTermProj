from src.scene.scene import scene
from src.object.player import Player
from src.object.background import BackGround

class scene_play(scene):

    def __init__(self):
        super().__init__()
        self.obj[1].append(Player())
        self.obj[0].append(BackGround())