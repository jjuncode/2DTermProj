from src.scene.scene import scene
from src.object.player import Player
from src.object.background.background import BackGround
from src.object.sword import Sword
from src.struct.struct import Vec2

class scene_play(scene):

    def __init__(self):
        super().__init__()
        player = Player()
        background = BackGround()

        # player sword
        sword_player = Sword(player, Vec2(player.pos.x, player.pos.y))
        player.setSword(sword_player)

        self.obj[1].append(player)
        self.obj[0].append(background)

        self.add_collision_pair("PLAYER:OPP_SWORD",player,None)        # 적 플레이어 타격
        self.add_collision_pair("PLAYER_SWORD:OPP",sword_player,None)       # 플레이어 적 타격
        self.add_collision_pair("PLAYER_SWORD:OPP_SWORD",sword_player,None) # 패링

