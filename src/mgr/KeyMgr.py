from pico2d import *
import ctypes

def is_key_pressed(key_code):
    return ctypes.windll.user32.GetAsyncKeyState(key_code) != 0
class KeyMgr:
    mgr = None
    key = { i:"NONE" for i in range(SDLK_a, SDLK_z+1)}

    def __new__(cls):
        if cls.mgr == None:
            cls.mgr = super(KeyMgr, cls).__new__(cls)
            return cls.mgr

    def __init__(self):
        pass
    def update(self):
        event = get_events()

        # 이벤트 처리
        for e in event:

            if e.type == SDL_KEYDOWN:
                if e.key not in self.key : self.key[e.key]="NONE"
                if self.key[e.key] == "NONE":
                    self.key[e.key] = "TAP" # TAP처리 됬으면 끝
                    continue


            elif e.type == SDL_KEYUP:
                self.key[e.key] = "NONE"
                print(self.key[e.key])
                print("key up!!!!!!!!!!!!!!!!!!!!!!")

            # HOLD 처리
            for _key,_value in self.key.items():
                if self.key[_key] == "TAP":
                    self.key[_key] = "HOLD"


    @staticmethod
    def GetKey(_key):
        return KeyMgr.key[_key]
