import pygame, time
from sea import Sea
from actor import Actor
class Bomb(Actor):
    def __init__(self, ai):
        super().__init__(ai, ["bomb.png", "baozha.png"])
        self.baozha_time = 0

    def update(self):
        super().update()
        if self.face==0:
            self.rect.y += 8
        if self.ai.pengdao(self, Sea) and self.face==0:
            self.next_face()
            self.baozha_time = time.time()
        if self.face==1 and self.baozha_time+3 <= time.time():
            self.dead = True
