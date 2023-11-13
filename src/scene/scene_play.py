from src.scene.scene import scene
from src.object.player import Player
from src.object.background.background import BackGround
from src.object.sword import Sword
from src.struct.struct import Vec2
from src.object.opponent import Opponent
from src.struct.struct import OBJ

class scene_play(scene):

    def __init__(self):
        super().__init__()
        # Background
        background = BackGround()

        # Player
        player = Player()
        sword_player = Sword(player, Vec2(player.pos.x, player.pos.y))

        # Opponent
        opponent = Opponent()
        sword_opponent = Sword(opponent, Vec2(opponent.pos.x, opponent.pos.y))

        self.obj[OBJ.kPlayer.value].append(player)
        self.obj[OBJ.kPlayer_sword.value].append(sword_player)

        self.obj[OBJ.kOpponent.value].append(opponent)
        self.obj[OBJ.kOpponent_sword.value].append(sword_opponent)

        self.obj[OBJ.kBackground.value].append(background)
