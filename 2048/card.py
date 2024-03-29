from turtle import color
from pgzero import clock
from pygame import Rect
from functools import partial
from random import choice
import time
clock=None


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
    def __init__(self, ctx, size, n=2):
        global clock
        clock = ctx.clock
        self.x=0
        self.y=0
        self.tasks = set()
        self.n = n
        self.size = size


    def r(self):
        return Rect(self.x, self.y, self.size, self.size)

    def goto(self, x, y):
        self.x=x
        self.y=y
    def clear_tasks(self):
        self.tasks.clear()
    def goto_future(self, x1, y1, x2, y2, beg_time, end_time):
        now = time.time()
        rate = (now-beg_time)/(end_time-beg_time)
        x = x1 + (x2-x1)*rate
        y = y1 + (y2-y1)* rate
        self.goto(x, y)
        
    def slideTo(self, x=0, y=0, s=1):
        now = time.time()
        for i in range(int(s*50)):
            gt = partial(self.goto_future, self.x, self.y, x, y, now, now+s)
            self.tasks.add(gt)
            clock.schedule_unique(gt, 0.02*i)
        clock.schedule_unique(self.clear_tasks, s+0.01)
    def getCenter(self):
        return [self.x+self.size/2, self.y+self.size/2]
    def draw(self, screen):
        if not self.n: return
        bg, fg = c(self.n)
        screen.draw.filled_rect(self.r(), color=bg)
        screen.draw.text(str(int(self.n)), center=self.getCenter(),color=fg)
