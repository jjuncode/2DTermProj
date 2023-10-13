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

    def update(self):
        global dt
        self.cur_time = pico2d.get_time()
        dt = self.cur_time - self.prev_time
        self.prev_time = self.cur_time

    @staticmethod
    def GetDt():
        global dt
        return dt