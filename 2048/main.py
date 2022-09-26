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
size=int(input("您想玩多大？"))
n = int(input("您想发多大?"))
num = int(input("每次发几张牌?"))
HEIGHT=700
WIDTH=1250

def createContext():
    ctx = Context()
    ctx.Actor = Actor
    ctx.clock = clock
    ctx.keys = keys
    return ctx

ctx = createContext()

qipan = None
def beg():
    global qipan
    qipan = Qipan(size, (275, 1),700, ctx, n, num)
    qipan.fapai_n()
    qipan.refresh_cards()
    # qipan.set()
    # qipan.fapai()

def on_key_down(key):
    if key==ctx.keys.SPACE:
        beg()
    qipan.on_key_down(key)



def draw():
    screen.fill((128, 128, 128))
    qipan.draw(screen)

def update():
    pass

beg()
pgzrun.go()