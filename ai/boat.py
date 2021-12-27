import pygame,time
from actor import Actor
from bomb import Bomb
import plane
from random import randint
from settings import Settings
from boat_bomb import BoatBomb
import random
WAVE = 5

def all_face_0(a, b):
    return a.face==0 and b.face==0
class Boat(Actor):
    sl = 1
    def __init__(self, ai, direction=1):
        def fire():
            if not self.is_sinking:
                self.fire()
        super().__init__(ai,
            ["boat_1.png",
             "boat_2.png",
              "boat_3.png",
               "boat_4.png"])
        if direction == 1:
            self.rect.left = ai.screen.get_rect().left
        else:
            self.rect.right = ai.screen.get_rect().right
        self.base_y = ai.screen.get_rect().bottom-376
        self.rect.y = self.base_y
        self.vy = -1
        self.is_sinking = False
        self.buzhi_loop(fire,0.28)
        self.direction=direction
    def fire(self):
        if self.ai.find_actors_of_class(plane.Plane):
            bomb = BoatBomb(self.ai)
            bomb.rect.midbottom = self.rect.midtop
            bomb.headingTo(plane.Plane)
            if random.randint(1,2)==1:
                bomb.rotate(random.randint(-90, 90))
            self.ai.add_actor(bomb)

    def update(self):
        super().update()
        if not self.is_sinking:
            self.rect.x += (self.direction * 3)
            self.rect.y += self.vy
            if self.vy<0 and self.rect.y<self.base_y-WAVE:
                self.vy = -1 * self.vy
            if self.vy > 0 and self.rect.y > self.base_y+WAVE:
                self.vy = -1 * self.vy

        bomb = self.ai.pengdao(self, Bomb, all_face_0)
        if self.rect.x>Settings.screen_width:
            self.direction=-1
        if self.rect.x<0:
            self.direction=1
        if bomb and bomb.face == 0:
            Boat.sl+=1
            if not self.is_sinking:
                def fanchuan():
                    self.next_face()
                def xc():
                    self.rect.y+=5
                def qusi():
                    self.dead = True
                def fachuan():
                    self.ai.add_actor(Boat(self.ai, self.direction * -1))
                self.buzhi(fanchuan, 0)
                self.buzhi(fanchuan, 0.5)
                self.buzhi(fanchuan, 1)
                self.buzhi(fachuan, randint(1,6)/10)
                for i in range(100):
                    self.buzhi(xc, i/10)
                self.buzhi(qusi, 10)
                self.is_sinking = True
