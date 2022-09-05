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
for i in range(16):
    qipan.fapai()
# qipan.set()
# qipan.fapai()

def on_key_down(key):
    qipan.on_key_down(key)


def draw():
    screen.fill((128, 128, 128))
    qipan.draw(screen)

def update():
    pass
pgzrun.go()