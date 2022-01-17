import pygame, time
from sea import Sea
from actor import Actor


class BB(Actor):
    def __init__(self, ai):
        super().__init__(ai, ["bb.png", "爆炸.png"])
        self.baozha_time = 0

    def update(self):
        super().update()
        if self.face == 0:
            self.rect.y += 8
        if self.ai.pengdao(self, Sea) and self.face == 0:
            self.next_face()
            self.rect.center = (self.ai.screen.get_rect().center[0]-400, self.ai.screen.get_rect().center[1]-300)
            self.ai.faguangbo("核爆炸")
            self.baozha_time = time.time()
        if self.face == 1 and self.baozha_time + 5<= time.time():
            self.dead = True
