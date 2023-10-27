from src.mgr.KeyMgr import GetKey,IsKey,isNoneKey, SetKeyExcept,SetKeyTap,IsTapKey
from pico2d import SDLK_a,SDLK_d,SDLK_w,SDLK_s,SDLK_q,SDLK_e,SDLK_SPACE
class Idle:

    @staticmethod
    def init(_instance):
        _instance.ani.cur_ani = 1
        _instance.ani.ani_reset = True

    @staticmethod
    def update(_instance):
        _instance.ani.update()
        pass

    @staticmethod
    def render(_instance):
        _instance.ani.render()
        pass

    @staticmethod
    def exit(_instance):
        pass

class Run:

    @staticmethod
    def init(_instance):
        _instance.ani.cur_ani = 0
        _instance.ani.ani_reset = True

    @staticmethod
    def update(_instance):
        _instance.ani.update()
        Run.update_key(_instance)

    @staticmethod
    def render(_instance):
        _instance.ani.render()
        pass

    @staticmethod
    def exit(_instance):
        pass

    @staticmethod
    def update_key(_instance):
        if IsKey(SDLK_d): _instance.pos.x += +_instance.speed
        if IsKey(SDLK_a): _instance.pos.x -= +_instance.speed
        if IsKey(SDLK_w): _instance.pos.y += +_instance.speed
        if IsKey(SDLK_s): _instance.pos.y -= +_instance.speed

        if isNoneKey((SDLK_a,SDLK_d,SDLK_w,SDLK_s)):
            _instance.state.change_state("KEY_NONE")

class Jump:
    @staticmethod
    def init(_instance):
        _instance.ani.cur_ani = 0
        _instance.ani.ani_reset = True

    @staticmethod
    def update(_instance):
        _instance.ani.update()
        Jump.update_key(_instance)

    @staticmethod
    def render(_instance):
        _instance.ani.render()
        pass

    @staticmethod
    def exit(_instance):
        pass
    @staticmethod
    def update_key(_instance):
        if IsKey(SDLK_SPACE):
            if _instance.pos.y <= 50 + 180:
                if _instance.component["PHYSIC"].accel.y <= 1000:
                    _instance.component["PHYSIC"].accel.y += 250
        if _instance.pos.y <= 0 + 180:
            _instance.state.change_state("GROUND")

class Attack_up:
    @staticmethod
    def init(_instance):
        _instance.ani.cur_ani = 3
        _instance.ani.ani_reset = True

    @staticmethod
    def update(_instance):
        _instance.ani.update()
        Attack_up.update_key(_instance)

    @staticmethod
    def render(_instance):
        _instance.ani.render()
        pass

    @staticmethod
    def exit(_instance):
        pass

    @staticmethod
    def update_key(_instance):

        # 공격상태에서 이동키가 동시에 눌릴경우
        # 이동 취소
        if IsKey(SDLK_d):
            SetKeyExcept(SDLK_d)
        if IsKey(SDLK_a) :
            SetKeyExcept(SDLK_a)

            # SetKeyNone(SDLK_a)
            # SetKeyNone(SDLK_d)

        if isNoneKey((SDLK_e,SDLK_q)) :
            _instance.state.change_state("KEY_NONE")

            # key holding 중이면 Tap처리해준다.
            if GetKey(SDLK_d) == "EXCEPT": SetKeyTap(SDLK_d)
            if GetKey(SDLK_a) == "EXCEPT": SetKeyTap(SDLK_a)

class Attack_down:
    @staticmethod
    def init(_instance):
        _instance.ani.cur_ani = 2
        _instance.ani.ani_reset = True

    @staticmethod
    def update(_instance):
        _instance.ani.update()
        Attack_down.update_key(_instance)

    @staticmethod
    def render(_instance):
        _instance.ani.render()
        pass

    @staticmethod
    def exit(_instance):
        pass

    @staticmethod
    def update_key(_instance):
        if IsKey(SDLK_d) or IsKey(SDLK_a):
            # 공격상태에서 이동키가 동시에 눌릴경우
            # 이동 취소
            if IsKey(SDLK_d):
                SetKeyExcept(SDLK_d)
            if IsKey(SDLK_a):
                SetKeyExcept(SDLK_a)

        if isNoneKey((SDLK_e,SDLK_q)) :
            _instance.state.change_state("KEY_NONE")

            # key holding 중이면 Tap처리해준다.
            if GetKey(SDLK_d) == "EXCEPT": SetKeyTap(SDLK_d)
            if GetKey(SDLK_a) == "EXCEPT": SetKeyTap(SDLK_a)
class StateMachine:
    def __init__(self,_instance):
        self.instance = _instance
        self.cur_state = Idle
        self.cur_state.init(self.instance)
        self.transition = {
            Idle : { SDLK_e :Attack_down, SDLK_q : Attack_up, SDLK_w : Run,SDLK_s:Run, SDLK_a : Run, SDLK_d : Run,SDLK_SPACE : Jump},
            Run : {SDLK_e : Attack_down, SDLK_q : Attack_up,"KEY_NONE":Idle,SDLK_SPACE : Jump},
            Attack_up : { SDLK_e :Attack_down, SDLK_w : Run,SDLK_s:Run, SDLK_a : Run, SDLK_d : Run, "KEY_NONE":Idle,SDLK_SPACE : Jump},
            Attack_down: {SDLK_q: Attack_up, SDLK_w: Run, SDLK_s: Run, SDLK_a: Run, SDLK_d: Run, "KEY_NONE":Idle,SDLK_SPACE : Jump},
            Jump : {"GROUND" : Idle, SDLK_w : Run,SDLK_s:Run, SDLK_a : Run, SDLK_d : Run}
        }

    def update(self):
        self.cur_state.update(self.instance)
        self.update_key()
        self.change_state(None)


    def render(self):
        self.cur_state.render(self.instance)

    def change_state(self,extra):
        for cur_event, next_state in self.transition[self.cur_state].items():
            if GetKey(cur_event) == "TAP" or GetKey(cur_event) == "HOLD":
                self.cur_state.exit(self.instance)
                self.cur_state = next_state
                self.cur_state.init(self.instance)
            elif extra == cur_event :
                self.cur_state.exit(self.instance)
                self.cur_state = next_state
                self.cur_state.init(self.instance)

    def update_key(self):
        pass
