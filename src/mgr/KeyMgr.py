from pico2d import *

class KeyMgr:
    mgr = None

    def __new__(cls):
        if cls.mgr == None:
            cls.mgr = super(KeyMgr, cls).__new__(cls)
            return cls.mgr

    def __init__(self):
        pass

    def update(self):
        event = get_events()
        for e in event:
            if e.type == SDL_KEYDOWN and e.key == SDLK_a:
                print("a pressed")
