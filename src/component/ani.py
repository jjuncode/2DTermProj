import pico2d
from pico2d import load_image

def CreatePath(_path):
    return "../../resource/" +_path

class Ani:
    def __init__(self,_path,_max_frame):
        self.cur_ani = 0
        self.cur_frame = 0
        self.max_frame = _max_frame
        self.image = load_image(CreatePath(_path))

    def render(self):
        self.image.draw(50,50)