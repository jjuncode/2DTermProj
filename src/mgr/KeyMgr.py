from pico2d import *

class KeyMgr:
    mgr = None
    key = { i:0 for i in range(SDLK_a, SDLK_z+1)}

    def __new__(cls):
        if cls.mgr == None:
            cls.mgr = super(KeyMgr, cls).__new__(cls)
            return cls.mgr

    def __init__(self):
        temp = {i:0 for i in range(SDLK_RIGHT,SDLK_UP+1)}
        self.mgr.key.update(temp)
        pass
    def update(self):
        event = get_events()

        # 이벤트 처리
        for e in event:
            if e.type == SDL_KEYDOWN:
                self.mgr.key[e.key] = self.mgr.key[e.key] + 1
                print(self.mgr.key[e.key])
            elif e.type == SDL_KEYUP:
                self.mgr.key[e.key] -= 1

    @staticmethod
    def GetKey(_key):
        if KeyMgr.mgr.key[_key] == 0 :
            return "NONE"
        elif KeyMgr.mgr.key[_key] == 1 :
            return "TAP"
        elif KeyMgr.mgr.key[_key] > 1 :
            return "HOLD"
