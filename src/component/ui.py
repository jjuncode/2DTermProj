from pico2d import load_image
from src.component.component import Component
from src.struct.struct import Vec2
from src.component.ani import CreatePath

class UI(Component):
    hp_bg = None
    hp_value = None

    def __init__(self, _owner, _pos):
        super().__init__(_owner, _pos)
        global hp_bg, hp_value
        hp_bg = load_image(CreatePath('health_bar.png'))
        hp_value = load_image(CreatePath('health_bar_value.png'))
        self.hp_bg = hp_bg
        self.hp_value = hp_value
        self.hp_bg_size = Vec2(590,144)
        self.hp_value_size = Vec2(560,100)

        self.ui_size = Vec2(0.25,0.2) # ui 비율값
        self.hp_per = _owner.hp / 100

    def render(self):
        self.hp_bg.draw(self.pos.x, self.pos.y,self.hp_bg_size.x * self.ui_size.x,self.hp_bg_size.y*self.ui_size.y)

        s = (self.hp_value_size.x - self.hp_value_size.x * self.hp_per)  # 깎인 가로값 계산
        move_x = s /2*self.ui_size.x
        self.hp_value.draw(self.pos.x-move_x, self.pos.y
                               ,self.hp_value_size.x * self.ui_size.x * self.hp_per
                               ,self.hp_value_size.y*self.ui_size.y)
        pass

    def update(self):
        # ui는 머리위에
        self.pos = Vec2(self.owner.pos.x, self.owner.pos.y + 100)
        self.hp_per = self.owner.hp / 100
