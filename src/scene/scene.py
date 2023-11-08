from src.object.player import Player
from src.object.background import BackGround

def collide(a, b):
    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()

    if la > rb: return False
    if ra < lb: return False
    if ta < bb: return False
    if ba > tb: return False

    return True

class scene:
    def __init__(self):
        self.obj = [[],[],[]]
        self.coll_group = {}

    def update(self):
        for layer in self.obj:
            for obj in layer:
                obj.update()

    def render(self):
        for layer in self.obj:
            for obj in layer:
                obj.render()

    def updateKey(self):
        pass

    @staticmethod
    def sceneChange(_scene):
        from src.mgr.SceneMgr import SceneMgr
        SceneMgr.sceneChange(_scene)
        print(SceneMgr.mgr.cur_scene)


    def checkCollision(self):
        for group, pairs in self.coll_group.items():
            for a in pairs[0]:
                for b in pairs[1]:
                    if collide(a, b):
                        a.handle_collision(group, b)
                        b.handle_collision(group, a)

    def add_collision_pair(self, group, a=None, b=None):  # a와 b사이에 충돌검사가 필요하다는 점을 등록
        if group not in self.coll_group:
            print(f"New group {group} added...")
            self.coll_group[group] = [[], []]
        if a:
            self.coll_group[group][0].append(a)
        if b:
            self.coll_group[group][1].append(b)



