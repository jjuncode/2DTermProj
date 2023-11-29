from mystruct import Vec2
from pico2d import load_image
from physic import Physic

class TitleFence:
    def __init__(self):
        self.pos = Vec2(400,900)
        self.cur_image = load_image('resource/title_fence.png')

        # < Component >
        self.component={}

        # physic
        self.physic = Physic(self,Vec2(self.pos.x,self.pos.y))
        self.physic.destn_y = 200
        self.component["PHYSIC"] = self.physic


    def render(self):
        self.cur_image.draw(self.pos.x,self.pos.y,800,600)
        for key, value in self.component.items():
            value.render()
        pass

    def update(self):
        for key, value in self.component.items():
            value.update()
