from src.struct.struct import Pos
from src.component.ani import Ani

class Player:
    def __init__(self):
        self.pos = Pos()
        self.ani = Ani("Attacks.png", [])

    def render(self):
        self.ani.render()