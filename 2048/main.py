from ast import With
from tkinter import Widget
import pgzrun
from functools import partial
from card import Card
from qipan import Qipan
from context import Context

# c2 = Card(Actor, clock)
# c2.slideTo(700, 200, 7)
# c3 = Card(Actor, clock)
# c3.slideTo(900, 400, 3)
size=4
HEIGHT=700
WIDTH=1250

def createContext():
    ctx = Context()
    ctx.Actor = Actor
    ctx.clock = clock
    ctx.keys = keys
    return ctx

ctx = createContext()

qipan = Qipan(size, (275, 1),700, ctx)
for i in range(2):
    qipan.fapai()
# qipan.fapai()

def on_key_down(key):
    qipan.on_key_down(key)


def draw():
    screen.fill((128, 128, 128))
    qipan.draw(screen)
    # for i in range(size+1):
    #     k = int(i * (600 / size))
    #     for j in range(k,k+width):
    #         screen.draw.line((j,100),(j,700),(200,200,200))
    # for i in range(size+1):
    #     k =1250- int(i * (600 / size))-width
    #     for j in range(k-width, k):
    #         screen.draw.line((j, 100), (j, 700), (200, 200, 200))
    # for i in range(size + 1):
    #     k = 700-int(i * (600 / size))
    #     for j in range(k, k+width):
    #         screen.draw.line((0,j), (1300, j), (200, 200, 200))
    #screen.draw.line((100, 101), (1000, 101), (0, 0, 0))
    #screen.draw.line((100, 102), (1000, 102), (0, 0, 0))
    #qipan.draw()
    pass

def update():
    pass
pgzrun.go()