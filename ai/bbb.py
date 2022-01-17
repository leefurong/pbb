# 敌方的老板， 负责发船相关的逻辑
from actor import Actor
from boat import Boat
from random import randint

class BBB(Actor):
    def __init__(self, ai):
        super().__init__(ai, ["baozha.png"])
        self.visibility=False
        self.buzhi_loop(self.fachuan,0)
        self.fa = True
    def shouguangbo(self, s):
        if s=="核爆炸":
            self.fa=False
        if s=="核爆结束":
            self.fa=True
    def fachuan(self):
        if self.fa and not self.ai.find_actors_of_class_and_face(Boat, 0):
            dir=randint(1,2)
            self.ai.add_actor(Boat(self.ai, dir))