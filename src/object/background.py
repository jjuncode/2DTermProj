from src.component.ani import CreatePath
from src.struct.struct import Vec2
from pico2d import load_image

class BackGround:
    image_background = None
    image_defeat = None
    image_win = None

    def __init__(self,_type):
        self.pos = Vec2(400,300)

        if BackGround.image_defeat == None :
            BackGround.image_defeat = load_image(CreatePath('bg_result_defeat.jpg'))

        if BackGround.image_background == None :
            BackGround.image_background = load_image(CreatePath('bg_streetFighter2.png'))

        if BackGround.image_win == None:
            BackGround.image_win = load_image(CreatePath('bg_result_win.jpg'))

        if _type == "BACKGROUND" : self.cur_image = BackGround.image_background
        elif _type == "RESULT_DEFEAT" : self.cur_image = BackGround.image_defeat
        elif _type == "RESULT_WIN" : self.cur_image = BackGround.image_win

    def render(self):
        self.cur_image.draw(self.pos.x,self.pos.y,800,600)
        pass

    def update(self):
        pass
