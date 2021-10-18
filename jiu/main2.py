import pgzrun
az=Actor("a")
bz=Actor("b")
map=Actor("map")
HEIGHT=map.height
WIDTH=map.width
ac=0
bc=0
cc=0
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0
p=0
def xz():
    global a,b,c,d,e,f,g,h,i,cc,ac,bc
    if p==1:
        if a==0:
            if cc==0:
                if ac >= 1:
                    ac += 1
                    ac = 0
                else:
                    ac += 1
                cc=1
                a=1
            else:
                if bc>=1:
                    bc += 1
                    bc=0
                else:
                    bc += 1
                cc=0
                a=2
    elif p==2:
        if b==0:
            if cc==0:
                if ac >= 1:
                    ac += 1
                    ac = 0
                else:
                    ac += 1
                cc=1
                b=1
            else:
                if bc>=1:
                    bc += 1
                    bc=0
                else:
                    bc += 1
                cc=0
                b=2
    elif p==3:
        if c==0:
            if cc==0:
                if ac >= 1:
                    ac += 1
                    ac = 0
                else:
                    ac += 1
                cc=1
                c=1
            else:
                if bc>=1:
                    bc += 1
                    bc=0
                else:
                    bc += 1
                cc=0
                c=2
    elif p==4:
        if d==0:
            if cc==0:
                if ac >= 1:
                    ac += 1
                    ac = 0
                else:
                    ac += 1
                cc=1
                d=1
            else:
                if bc>=1:
                    bc += 1
                    bc=0
                else:
                    bc += 1
                cc=0
                d=2
    elif p==5:
        if e==0:
            if cc==0:
                if ac >= 1:
                    ac += 1
                    ac = 0
                else:
                    ac += 1
                cc=1
                e=1
            else:
                if bc>=1:
                    bc += 1
                    bc=0
                else:
                    bc += 1
                cc=0
                e=2
    elif p==6:
        if f==0:
            if cc==0:
                if ac >= 1:
                    ac += 1
                    ac = 0
                else:
                    ac += 1
                cc=1
                f=1
            else:
                if bc>=1:
                    bc += 1
                    bc=0
                else:
                    bc += 1
                cc=0
                f=2
    elif p==7:
        if g==0:
            if cc==0:
                if ac >= 1:
                    ac += 1
                    ac = 0
                else:
                    ac += 1
                cc=1
                g=1
            else:
                if bc>=1:
                    bc += 1
                    bc=0
                else:
                    bc += 1
                cc=0
                g=2
    elif p==8:
        if h==0:
            if cc==0:
                if ac >= 1:
                    ac += 1
                    ac = 0
                else:
                    ac += 1
                cc=1
                h=1
            else:
                if bc>=1:
                    bc += 1
                    bc=0
                else:
                    bc += 1
                cc=0
                h=2
    elif p==9:
        if i == 0:
            if cc == 0:
                if ac >= 1:
                    ac += 1
                    ac = 0
                else:
                    ac += 1
                cc = 1
                i = 1
            else:
                if bc>=1:
                    bc += 1
                    bc=0
                else:
                    bc += 1
                cc = 0
                i = 2
def mo(pos):
    if(pos[0]>0*2 and pos[0]<=103*2 and pos[1]>0*2 and pos[1]<=103*2):
        return True
    return False
def mt(pos):
    if(pos[0]>0*2 and pos[0]<=103*2 and pos[1]>103*2 and pos[1]<=206*2):
        return True
    return False
def mh(pos):
    if(pos[0]>0*2 and pos[0]<=103*2 and pos[1]>206*2 and pos[1]<=309*2):
        return True
    return False
def mf(pos):
    if(pos[0]>103*2 and pos[0]<=206*2 and pos[1]>0*2 and pos[1]<=103*2):
        return True
    return False
def mi(pos):
    if(pos[0]>103*2 and pos[0]<=206*2 and pos[1]>103*2 and pos[1]<=206*2):
        return True
    return False
def ms(pos):
    if(pos[0]>103*2 and pos[0]<=206*2 and pos[1]>206*2 and pos[1]<=309*2):
        return True
    return False
def me(pos):
    if(pos[0]>206*2 and pos[0]<=309*2 and pos[1]>0*2 and pos[1]<=103*2):
        return True
    return False
def mg(pos):
    if(pos[0]>206*2 and pos[0]<=309*2 and pos[1]>103*2 and pos[1]<=206*2):
        return True
    return False
def mn(pos):
    if(pos[0]>206*2 and pos[0]<=309*2 and pos[1]>206*2 and pos[1]<=309*2):
        return True
    return False
def draw():
    map.draw()
    if a==1:
        az.pos=(51*2,51*2)
        az.draw()
    elif a==2:
        bz.pos = (51*2, 51*2)
        bz.draw()
    if b==1:
        az.pos = (51 * 2, 154 * 2)
        az.draw()
    elif b==2:
        bz.pos = (51 * 2, 154 * 2)
        bz.draw()
    if c==1:
        az.pos = (51 * 2, 257 * 2)
        az.draw()
    elif c==2:
        bz.pos = (51 * 2, 257 * 2)
        bz.draw()
    if d==1:
        az.pos = (154 * 2, 51 * 2)
        az.draw()
    elif d==2:
        bz.pos = (154 * 2, 51 * 2)
        bz.draw()
    if e==1:
        az.pos = (154 * 2, 154 * 2)
        az.draw()
    elif e==2:
        bz.pos = (154 * 2, 154 * 2)
        bz.draw()
    if f==1:
        az.pos = (154 * 2, 257 * 2)
        az.draw()
    elif f==2:
        bz.pos = (154 * 2, 257 * 2)
        bz.draw()
    if g==1:
        az.pos = (257 * 2, 51 * 2)
        az.draw()
    elif g==2:
        bz.pos = (257 * 2, 51 * 2)
        bz.draw()
    if h==1:
        az.pos = ( 257* 2, 154 * 2)
        az.draw()
    elif h==2:
        bz.pos = (257 * 2, 154 * 2)
        bz.draw()
    if i==1:
        az.pos = (257 * 2, 257 * 2)
        az.draw()
    elif i==2:
        bz.pos = (257 * 2, 257 * 2)
        bz.draw()
def on_mouse_down(pos,button):
    global a,b,c,d,e,f,g,h,i,p,cc
    if(button==mouse.LEFT):
        if mo(pos):
            p=1
            xz()
        elif mt(pos):
            p=2
            xz()
        elif mh(pos):
            p=3
            xz()
        elif mf(pos):
            p=4
            xz()
        elif mi(pos):
            p=5
            xz()
        elif ms(pos):
            p=6
            xz()
        elif me(pos):
            p=7
            xz()
        elif mg(pos):
            p=8
            xz()
        elif mn(pos):
            p=9
            xz()
    else:
        a=0
        b=0
        c=0
        d=0
        e=0
        f=0
        g=0
        h=0
        i=0
        cc=0
# def on_key_down():
#     global a,b,c,d,e,f,g,h,i,ac,bc
#     if ac==0 and cc==0:
#         if p==1:
#             if keyboard.DOWN:
#                 b=0
#             if keyboard.RIGHT:
#                 d=0
#         if p==2:
#             if keyboard.UP:
#                 a=0
#             if keyboard.DOWN:
#                 c=0
#             if keyboard.RIGHT:
#                 e=0
#         if p==3:
#             if keyboard.UP:
#                 b=0
#             if keyboard.RIGHT:
#                 f=0
#         if p==4:
#             if keyboard.DOWN:
#                 e=0
#             if keyboard.LEFT:
#                 a=0
#             if keyboard.RIGHT:
#                 g=0
#         if p==5:
#             if keyboard.UP:
#                 d=0
#             if keyboard.DOWN:
#                 f=0
#             if keyboard.LEFT:
#                 b=0
#             if keyboard.RIGHT:
#                 h=0
#         if p==6:
#             if keyboard.UP:
#                 e=0
#             if keyboard.LEFT:
#                 c=0
#             if keyboard.RIGHT:
#                 i=0
#         if p==7:
#             if keyboard.DOWN:
#                 h=0
#             if keyboard.LEFT:
#                 d=0
#         if p==8:
#             if keyboard.UP:
#                 g=0
#             if keyboard.DOWN:
#                 i=0
#             if keyboard.LEFT:
#                 e=0
#         if p==9:
#             if keyboard.UP:
#                 h=0
#             if keyboard.LEFT:
#                 f=0
#         ac=1
#     elif bc==0 and cc==1:
#         if p == 1:
#             if keyboard.DOWN:
#                 b = 0
#             if keyboard.RIGHT:
#                 d = 0
#         if p == 2:
#             if keyboard.UP:
#                 a = 0
#             if keyboard.DOWN:
#                 c = 0
#             if keyboard.RIGHT:
#                 e = 0
#         if p == 3:
#             if keyboard.UP:
#                 b = 0
#             if keyboard.RIGHT:
#                 f = 0
#         if p == 4:
#             if keyboard.DOWN:
#                 e = 0
#             if keyboard.LEFT:
#                 a = 0
#             if keyboard.RIGHT:
#                 g = 0
#         if p == 5:
#             if keyboard.UP:
#                 d = 0
#             if keyboard.DOWN:
#                 f = 0
#             if keyboard.LEFT:
#                 b = 0
#             if keyboard.RIGHT:
#                 h = 0
#         if p == 6:
#             if keyboard.UP:
#                 e = 0
#             if keyboard.LEFT:
#                 c = 0
#             if keyboard.RIGHT:
#                 i = 0
#         if p == 7:
#             if keyboard.DOWN:
#                 h = 0
#             if keyboard.LEFT:
#                 d = 0
#         if p == 8:
#             if keyboard.UP:
#                 g = 0
#             if keyboard.DOWN:
#                 i = 0
#             if keyboard.LEFT:
#                 e = 0
#         if p == 9:
#             if keyboard.UP:
#                 h = 0
#             if keyboard.LEFT:
#                 f = 0
#         bc=1
pgzrun.go()