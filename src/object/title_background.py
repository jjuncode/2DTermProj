from src.struct.struct import Vec2
from pico2d import load_image
from src.component.ani import CreatePath
import pico2d

class TitleBackground:
    def __init__(self):
        self.pos = Vec2(400,300)
        self.cur_image = load_image(CreatePath('title_background.png'))

    def render(self):
        self.cur_image.draw(self.pos.x,self.pos.y,800,600)
        pass

    def update(self):
        pass
