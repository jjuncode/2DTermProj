from mystruct import Vec2
from pico2d import load_image
from physic import Physic

class TitleLogo:
    def __init__(self):
        self.pos = Vec2(400,2000)
        self.cur_image = load_image('resource/title_logo.png')

        # < Component >
        self.component={}

        # physic
        self.physic = Physic(self,Vec2(self.pos.x,self.pos.y))
        self.physic.destn_y = 150
        self.component["PHYSIC"] = self.physic


    def render(self):
        self.cur_image.draw(self.pos.x,self.pos.y,400,400)
        for key, value in self.component.items():
            value.render()
        pass

    def update(self):
        for key, value in self.component.items():
            value.update()
