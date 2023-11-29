from mystruct import Vec2
from component import Component
from TimeMgr import TimeMgr

class Physic(Component):
    gravity = Vec2(0, -9. *18 )
    speed = 15  # 물리 적용 offset값

    def __init__(self, _owner, _pos):
        super().__init__(_owner, _pos)
        self.accel = Vec2(0, 0)
        self.velo = Vec2(0, 0)
        self.destn_y = 0  # 중력 어디까지 작용할건지
        self.fric = 0.9 # 마찰계수

    def update(self):
        dt = TimeMgr.GetDt() * Physic.speed
        if self.owner.pos.y > self.destn_y:  # 공중에 떠있을 때 중력 적용
            after_accel = Vec2(self.accel.x + Physic.gravity.x * dt, self.accel.y + Physic.gravity.y * dt)
            self.accel = after_accel

        else:  # 공중에 떠있지 않다면
            self.owner.pos.y = self.destn_y  # 땅에 고정
            self.accel.y = 0

        # 땅 뚫 방지
        if (self.owner.pos.y < self.destn_y):
            self.owner.pos.y = self.destn_y
            self.accel.y = 0

        # x방향 가속도가 있으면 점차 감소
        if self.accel.x > 0 or self.accel.x < 0 :
            self.accel.x *=  1 - self.fric * dt
            if abs(self.accel.x) < 10 : self.accel.x = 0 # 10보다 작으면 없는셈으로 친다.

        velo_after = Vec2(self.accel.x * dt, self.accel.y * dt)

        add_speed = Vec2(self.velo.x + velo_after.x, self.velo.y + velo_after.y)
        aver_speed = Vec2(add_speed.x / 2, add_speed.y / 2)
        result = Vec2(aver_speed.x * dt, aver_speed.y * dt)
        pos_after = Vec2(self.owner.pos.x + result.x, self.owner.pos.y + result.y)

        self.velo = velo_after
        self.owner.pos = pos_after

        # 화면 밖 안나가게 조절
        if self.owner.pos.x < 50 : self.owner.pos.x = 50
        elif self.owner.pos.x > 750 : self.owner.pos.x = 750



    def render(self):
        pass

    def addForce(self,_vec):
        self.accel.x += _vec.x
        if _vec.y > 0 :
            self.accel.y += _vec.y
            self.owner.pos.y +=1

    def getAccel(self):
        return self.accel