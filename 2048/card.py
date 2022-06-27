from turtle import color
from pgzero import clock
from pygame import Rect
from functools import partial
from random import choice
clock=None
def r(a):
    l = a.left
    t = a.top
    w = a.width
    h = a.height
    return Rect(l, t, w, h)

def c(x):
    if x<=2:return ((234,222,210),(100,91,82))
    if x <= 4: return ((234, 219, 189), (100, 91, 82))
    if x<=8:return ((234,163,105),(247,244,238))
    if x <= 16: return ((241, 130, 82), (247, 244, 238))
    if x <= 32: return ((238,101,82), (247, 244, 238))
    if x <= 64: return ((243, 71, 46), (247, 244, 238))
    if x <= 128: return ((232,199,96), (247, 244, 238))
    if x<4096: return ((232,194,85), (247, 244, 238))
    return ((245,75,98), (247, 244, 238))


class Card:
    def __init__(self, Actor, clck):
        global clock
        clock = clck
        self.actor=Actor("gua", anchor=("left", "top"))
        self.actor.x=0
        self.actor.y=0
        self.tasks = set()
        self.n = 2


    def goto(self, x, y):
        self.actor.x=x
        self.actor.y=y
    def clear_tasks(self):
        self.tasks.clear()
    def slideTo(self, x=0, y=0, s=1):
        for i in range(s*50):
            xstep = (x-self.actor.x)/(s*50)
            ystep = (y - self.actor.y) / (s * 50)
            newx = self.actor.x+i*xstep
            newy = self.actor.y+i*ystep
            gt = partial(self.goto, newx, newy)
            self.tasks.add(gt)
            clock.schedule_unique(gt, 0.02*i)
        clock.schedule_unique(self.clear_tasks, s+0.01)
    def draw(self, screen):
        bg, fg = c(self.n)
        screen.draw.filled_rect(r(self.actor), color=bg)
        screen.draw.text(str(int(self.n)), center=self.actor.center,color=fg)
