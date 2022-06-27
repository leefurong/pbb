import pgzrun
from functools import partial
from card import Card
c1 = Card(Actor, clock)
c1.slideTo(500, 0, 5)

c2 = Card(Actor, clock)
c2.slideTo(700, 200, 7)
c3 = Card(Actor, clock)
c3.slideTo(900, 400, 3)


def draw():
    screen.fill((128, 128, 128))
    c1.draw(screen)
    c2.draw(screen)
    c3.draw(screen)
    pass

def update():
    pass
pgzrun.go()