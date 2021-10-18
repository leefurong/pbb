import pgzrun,random
z=Actor("ccc")
b=Actor("bbb")
j=Actor("aaa")
WIDTH=j.width
HEIGHT=j.height
b.x=550
b.y=360
z.x=548
z.y=390
zz=-1
d=10
def update():
    global d,zz
    if keyboard.q and d==10:
        zz=1
    elif  keyboard.t and zz==1:
        zz=0
    if zz==1:
        z.angle=z.angle+10.13234575643567
    if zz==0:
        z.angle = z.angle + d
        d -= 0.3512345678900987654
        if d<=0:
            zz=-1
            d=10
def draw():
    j.draw()
    z.draw()
    b.draw()
pgzrun.go()