import pico2d
from pico2d import load_image
from src.mgr.TimeMgr import TimeMgr

def CreatePath(_path):
    return "../../resource/" +_path

class Ani:
    def __init__(self,_path,_max_frame):
        self.cur_ani = 0
        self.cur_frame = 0
        self.max_frame = _max_frame
        self.image = load_image(CreatePath(_path))

        self.act_time = 0.1 # 프레임 건너는 시간

        self.acc_time =0.0  # 누적시간

    def render(self,pos):
        self.image.clip_draw(self.cur_frame*128,self.cur_ani*64,128,64,pos.x,pos.y, 500,400)

    def update(self):
        self.acc_time += TimeMgr.GetDt()

        if (self.acc_time > self.act_time ):
            self.acc_time = 0
            self.cur_frame = ( self.cur_frame +1 ) % 8
