import pygame,time
from actor import Actor
from bomb import Bomb
from random import randint
from settings import Settings
from boat_bomb import BoatBomb
WAVE = 5

def all_face_0(a, b):
    return a.face==0 and b.face==0
class Boat(Actor):
    def __init__(self, ai):
        def fire():
            self.fire()
        super().__init__(ai,
            ["boat_1.png",
             "boat_2.png",
              "boat_3.png",
               "boat_4.png"])
        self.rect.left = ai.screen.get_rect().left
        self.base_y = ai.screen.get_rect().bottom-376
        self.rect.y = self.base_y
        self.vy = -1
        self.is_sinking = False
        self.buzhi_loop(fire, 2)
    def fire(self):
        print("fire!")

    def update(self):
        super().update()
        if not self.is_sinking:
            self.rect.x += 3
            self.rect.y += self.vy
            if self.vy<0 and self.rect.y<self.base_y-WAVE:
                self.vy = -1 * self.vy
            if self.vy > 0 and self.rect.y > self.base_y+WAVE:
                self.vy = -1 * self.vy

        bomb = self.ai.pengdao(self, Bomb, all_face_0)
        if bomb and bomb.face == 0 or self.rect.x>Settings.screen_width:
            if not self.is_sinking:
                def fanchuan():
                    self.next_face()
                def xc():
                    self.rect.y+=5
                def qusi():
                    self.dead = True
                def fachuan():
                    self.ai.add_actor(Boat(self.ai))
                self.buzhi(fanchuan, 0)
                self.buzhi(fanchuan, 0.5)
                self.buzhi(fanchuan, 1)
                self.buzhi(fachuan, randint(1,6)/10)
                for i in range(100):
                    self.buzhi(xc, i/10)
                self.buzhi(qusi, 10)
                self.is_sinking = True
