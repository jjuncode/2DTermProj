from pico2d import *
class KeyMgr:
    mgr = None
    key = { i:"NONE" for i in range(SDLK_a, SDLK_z+1)}

    def __new__(cls):
        if cls.mgr == None:
            cls.mgr = super(KeyMgr, cls).__new__(cls)
            return cls.mgr

    def __init__(self):
        self.key[SDLK_LSHIFT] = "NONE"
        pass
    def update(self):
        event = get_events()

        # 이벤트 처리
        for e in event:
            # AWAY -> NONE
            for _key,_value in self.key.items():
                if self.key[_key] == "AWAY":
                    self.key[_key] = "NONE"

            if e.type == SDL_KEYDOWN:
                if e.key not in self.key : self.key[e.key]="NONE"
                if self.key[e.key] == "NONE":
                    self.key[e.key] = "TAP" # TAP처리 됬으면 끝
                    continue
                print(self.key[e.key])

            elif e.type == SDL_KEYUP:
                self.key[e.key] = "AWAY"
                print(self.key[e.key])

            # HOLD 처리
            for _key,_value in self.key.items():
                if self.key[_key] == "TAP":
                    self.key[_key] = "HOLD"


def GetKey(_key):
    if _key not in KeyMgr.key: KeyMgr.key[_key] = "NONE"
    return KeyMgr.key[_key]

def IsKey(_key):
    if GetKey(_key) == "TAP" or GetKey(_key) == "HOLD" :
        return True
    return False

def IsTapKey(_key):
    if GetKey(_key) == "TAP" : return True
    return False

def IsHoldKey(_key):
    if GetKey(_key) == "HOLD" : return True
    return False

def IsAwayKey(_key):
    if GetKey(_key) == "AWAY" : return True
    return False

def isNoneKey(_key):
    for key in _key :
        if IsKey(key) : return False     # 들어온 키중 하나라도 입력되있으면 None상태가 아니다
    return True