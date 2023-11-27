from src.component.component import Component
from pico2d import load_image
from src.mgr.TimeMgr import TimeMgr

def CreatePath(_path):
    return "../../resource/" +_path
class Ani(Component):
    def __init__(self,_owner,_pos,_path,_max_frame,_offset_x,_offset_y,_acc_time,draw_size, _composite=False):
        super().__init__(_owner,_pos)
        self.cur_ani = 0
        self.cur_frame = 0
        self.offset_x = _offset_x
        self.offset_y = _offset_y

        self.max_frame = _max_frame
        self.image = load_image(CreatePath(_path))

        self.act_time = _acc_time # 프레임 건너는 시간

        self.acc_time =0.0  # 누적시간
        self.ani_reset =False
        self.draw_size = draw_size
        self.composite = _composite # 이미지 반전여부

    def render(self):
            if (self.composite ):
                self.image.clip_composite_draw(self.cur_frame * self.offset_x[self.cur_ani]  # x
                                     , sum(self.offset_y[:self.cur_ani])  # y
                                     , self.offset_x[self.cur_ani], self.offset_y[self.cur_ani]  # offset
                                     ,0 , 'h'   # 반전
                                     , self.owner.pos.x, self.owner.pos.y  # pos
                                     , self.offset_x[self.cur_ani] * self.draw_size.x  # size_x
                                     , self.offset_y[self.cur_ani] * self.draw_size.y)  # size_y
            else:
                self.image.clip_draw(self.cur_frame*self.offset_x[self.cur_ani] # x
                                 ,sum(self.offset_y[:self.cur_ani])         # y
                                 ,self.offset_x[self.cur_ani],self.offset_y[self.cur_ani]    # offset
                                 ,self.owner.pos.x,self.owner.pos.y   # pos
                                 ,self.offset_x[self.cur_ani] * self.draw_size.x       # size_x
                                 ,self.offset_y[self.cur_ani] * self.draw_size.y)      # size_y

    def update(self):
        self.pos = self.owner.pos

        self.acc_time += TimeMgr.GetDt()
        if (self.ani_reset) :
            self.cur_frame = 0
            self.ani_reset = False

        if (self.acc_time > self.act_time ):
            self.acc_time = 0
            self.cur_frame = ( self.cur_frame +1 ) % self.max_frame[self.cur_ani]

    def setAni(self,_rhs):
        self.cur_ani= _rhs

    def resetAni(self):
        self.ani_reset = True