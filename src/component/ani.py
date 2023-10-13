import pico2d
from pico2d import load_image
from src.mgr.TimeMgr import TimeMgr

def CreatePath(_path):
    return "../../resource/" +_path

class Ani:
    def __init__(self,_path,_max_frame,_offset_x,_offset_y):
        self.cur_ani = 0
        self.cur_frame = 0
        self.offset_x = _offset_x
        self.offset_y = _offset_y

        self.max_frame = _max_frame
        self.image = load_image(CreatePath(_path))

        self.act_time = 0.1 # 프레임 건너는 시간

        self.acc_time =0.0  # 누적시간
        self.ani_reset =False

    def render(self,pos):
            self.image.clip_draw(self.cur_frame*self.offset_x[self.cur_ani] # x
                             ,sum(self.offset_y[:self.cur_ani])         # y
                             ,self.offset_x[self.cur_ani],self.offset_y[self.cur_ani]    # offset
                             ,pos.x,pos.y   # pos
                             ,self.offset_x[self.cur_ani] * 4       # size_x
                             ,self.offset_y[self.cur_ani] * 4)      # size_y

    def update(self):
        self.acc_time += TimeMgr.GetDt()
        if (self.ani_reset) :
            self.cur_frame = 0
            self.ani_reset = False

        if (self.acc_time > self.act_time ):
            self.acc_time = 0
            self.cur_frame = ( self.cur_frame +1 ) % self.max_frame[self.cur_ani]
