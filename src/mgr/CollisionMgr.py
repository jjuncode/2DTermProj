import pico2d
from src.mgr.TimeMgr import TimeMgr

class CollisionMgr:
    mgr = None

    def __new__(cls):
        if cls.mgr == None:
            cls.mgr = super(CollisionMgr, cls).__new__(cls)
            return cls.mgr

    def __init__(self):
        self.coll_pair = {}
        pass

    def checkCollision(self):
        for group, pairs in self.coll_pair.items():
            for a in pairs[0]:
                for b in pairs[1]:
                    if CollisionMgr.mgr.collide(a, b):
                        a.handle_collision(group, b)
                        b.handle_collision(group, a)

    @staticmethod
    def add_collision_pair(group, a=None, b=None):  # a와 b사이에 충돌검사가 필요하다는 점을 등록
        if group not in CollisionMgr.mgr.coll_pair:
            print(f"New group {group} added...")
            CollisionMgr.mgr.coll_pair[group] = [[], []]
        if a:
            CollisionMgr.mgr.coll_pair[group][0].append(a)
        if b:
            CollisionMgr.mgr.coll_pair[group][1].append(b)

    def collide(self, a, b):
        la, ba, ra, ta = a.get_bb()
        lb, bb, rb, tb = b.get_bb()

        if la > rb: return False
        if ra < lb: return False
        if ta < bb: return False
        if ba > tb: return False

        return True

