import pico2d

class TimeMgr:
    mgr = None

    def __new__(cls):
        if cls.mgr == None:
            cls.mgr = super(TimeMgr, cls).__new__(cls)
            return cls.mgr

    def __init__(self):
        self.start_time = pico2d.get_time()
        self.prev_time = pico2d.get_time()
        global dt
        dt = 0

        self.cnt = 0
        self.acc = 0

    def update(self):
        global dt
        self.cur_time = pico2d.get_time()
        dt = self.cur_time - self.prev_time
        self.prev_time = self.cur_time

        self.cnt += 1
        self.acc += dt
        if self.acc >= 1 :
            self.acc = 0
            print("FPS : ",self.cnt)
            self.cnt =0

    @staticmethod
    def GetDt():
        global dt
        return dt