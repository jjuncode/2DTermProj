from sdl2 import SDLK_BACKSPACE

from KeyMgr import IsTapKey
from level_select import LevelSelect
from scene import scene
from player import Player
from background import BackGround
from sword import Sword
from mystruct import Vec2
from opponent import Opponent
from mystruct import OBJ

class scene_play(scene):

    def __init__(self,_level):
        super().__init__()
        # Background
        background = BackGround("BACKGROUND")

        # Player
        player = Player()
        sword_player = Sword(player, Vec2(player.pos.x, player.pos.y))
        sword_player.setDamage(0.5)

        # Opponent
        if _level == 1 :
            opponent = Opponent(0.15,3,_level)
            sword_opponent = Sword(opponent, Vec2(opponent.pos.x, opponent.pos.y))
            sword_opponent.setDamage(1)
        elif _level == 2 :
            opponent = Opponent(0.1125, 1.5,_level)
            sword_opponent = Sword(opponent, Vec2(opponent.pos.x, opponent.pos.y))
            sword_opponent.setDamage(2)

        self.obj[OBJ.kPlayer.value].append(player)
        self.obj[OBJ.kPlayer_sword.value].append(sword_player)

        self.obj[OBJ.kOpponent.value].append(opponent)
        self.obj[OBJ.kOpponent_sword.value].append(sword_opponent)

        self.obj[OBJ.kBackground.value].append(background)

    def updateKey(self):
        from scene_level_select import scene_level
        if IsTapKey(SDLK_BACKSPACE):
            level = LevelSelect.getMaxLevel()
            self.sceneChange(scene_level(level))
