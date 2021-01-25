# TODO: 拳击、脚踢， 多画一笔
# 拳击-1
# 脚踢-2
# 2秒拳击
# 3秒脚踢
# 近战最好， 用它不急
import pgzrun,pygame
import math
import pygame
import time,random
from gm import GM
aaa=input("A颜色")
bbb=input("B颜色")
ccccc=input("背景颜色")
grass=Actor("898")
m=GM(grass)
sss=1
b=300
azss=0
azcs=0
bzss=0
bzcs=0
bfcs=0
bfss=0
afcs=0
afss=0
aqss=0
aqcs=0
bqss=0
bqcs=0
btcs=0
btss=0
atcs=0
atss=0
z=0
y=0
o=20
p=20
c=1000
am=1
n=time.time()
bm=1
ee=10
oo=10
begin = None
HEIGHT=1000
WIDTH=1300
kt=time.time()
if random.randint(2,4)!=2:
    file='sounds/22.mp3'
else:
    file='sounds/1.mp3'
jitui=Actor("jitui")
knife=Actor("knife")
g=Actor("g")
nq=Actor("nq")
az=Actor("大子弹_1")
bz=Actor("大子弹_1")
af=Actor("qq")
bf=Actor("qq")
af.show=False
bf.show=False
bzs=[]
azs=[]
az.show=True
bz.show=True
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play(-1)
def getRect(shui):
    if (shui=='a'):
        return Rect((b-o,z-o),(2*o,2*o))
    else:
        return Rect((c-p,y-p),(2*p,2*p))
def pq(sh):
    return m.pm(getRect(sh))
def touch_edge(actor):
    if actor.center[1]>800 or actor.center[1]<0 or actor.center[0]>1300 or actor.center[0]<0:
        return True
    else:
        return False
def move(actor,b):
    actor.center=(actor.center[0]+b*math.cos(actor.angle*math.pi/180), actor.center[1]-b*math.sin(actor.angle*math.pi/180))
def jitui_update():
    global am,bm,n
    if jitui.colliderect(Rect((b-o, z-o), (2*o, 2*o))):
        am+=3
        jitui.center=(1000,1000)
        n=time.time()
    if jitui.colliderect(Rect((c-p, y-p), (2*p, 2*p))):
        bm+=3
        jitui.center=(1000,1000)
        n=time.time()
    if n+20<=time.time():
        jitui.center=(random.randint(10,1290),random.randint(10,790))
        n=time.time()
def knife_update():
    global am,bm,w
    if knife.colliderect(Rect((b-o, z-o), (2*o, 2*o))):
        am-=3
        knife.center=(1000,1000)
        w=time.time()
    if jitui.colliderect(Rect((c-p, y-p), (2*p, 2*p))):
        bm-=3
        knife.center=(1000,1000)
        w=time.time()
    if n+20<=time.time():
        knife.center=(random.randint(10,1290),random.randint(10,790))
        w=time.time()
def g_update():
    global am,bm,zz
    if g.colliderect(Rect((b-o, z-o), (2*o, 2*o))):
        am-=99
        g.center=(1000,1000)
        zz=time.time()
    if g.colliderect(Rect((c-p, y-p), (2*p, 2*p))):
        bm-=99
        g.center=(1000,1000)
        zz=time.time()
    if n+20<=time.time():
        g.center=(random.randint(10,1290),random.randint(10,790))
        zz=time.time()
def nq_update():
    global am,bm,ww
    if nq.colliderect(Rect((b-o, z-o), (2*o, 2*o))):
        am+=99
        knife.center=(1000,1000)
        ww=time.time()
    elif nq.colliderect(Rect((c-p, y-p), (2*p, 2*p))):
        bm+=99
        nq.center=(1000,1000)
        ww=time.time()
    if n+20<=time.time():
        nq.center=(random.randint(10,1290),random.randint(10,790))
        ww=time.time()
def az_update(keyboard):
    global bm,ee,azcs
    if keyboard.x:
        if azss-azcs>=3:
            azcs=time.time()
            newaz=Actor("大子弹_1")
            newaz.center=(b,z)
            newaz.angle=newaz.angle_to([c,y])
            azs.append(newaz)
        else:
            pass
    else:
        for az in azs:
            if touch_edge(az):
                azs.remove(az)
    for az in azs:
        if az.colliderect(bf) and bf.show:
            azs.remove(az)
    for az in azs:
        move(az,ee)
        if m.bomb(az):
            azs.remove(az)
        if az.colliderect(Rect((c-p, y-p), (2*p, 2*p))):
            bm-=99
    if keyboard.z and azss-azcs>=3:
        ee+=1
    if keyboard.c:
        ee-=1
def bz_update(keyboard):
    global am,oo,bzcs
    if keyboard.o:
        if bzss-bzcs>=3:
            newbz=Actor("大子弹_1")
            newbz.center=(c,y)
            newbz.angle=newbz.angle_to([b,z])
            bzs.append(newbz)
            bzcs=time.time()
        else:
            pass
    else:
        for bz in bzs:
            if touch_edge(bz):
                bzs.remove(bz)
    for bz in bzs:
        if 1 in m.ps(bz):
            m.put(zzzz([bz.x, bz.y]), 0)
            bzs.remove(bz)
        if 2 in m.ps(bz):
            bzs.remove(bz)
        if bz.colliderect(af) and af.show:
            bzs.remove(bz)
    for bz in bzs:
        move(bz,oo)
        if bz.colliderect(Rect((b-o, z-o), (2*o, 2*o))):
            am-=99
    if keyboard.k and bzss-bzcs>=3:
        oo+=1
    if keyboard.l:
        oo-=1
def af_update(keyboard):
    global afcs
    if keyboard.f:
        if afss-afcs>=6:
            af.show=True
            afcs=time.time()
        else:
            if(time.time()-afcs>=3):
                af.show=False
            else:
                af.center=(b, z)
                af.angle+=2
    else:
        af.show=False
def bf_update(keyboard):
    global bfcs
    if keyboard.j:
        if bfss-bfcs>=6:
            bf.show=True
            bfcs=time.time()
        else:
            if(time.time()-bfcs>=3):
                bf.show=False
            else:
                bf.center=(c,y)
                bf.angle+=2
    else:
        bf.show=False
def aq(keyboard):
    global aqcs
    if keyboard.j:
        if aqss - aqcs >= 6:
            aq.show = True
            aqcs = time.time()
        else:
            if (time.time() - aqcs >= 2):
                aq.show = False
    else:
        aq.show = False
def zzzz(pixel_pos):
    return [int(x/16) for x in pixel_pos]
def make_line(beg, end):
    if abs(beg[1]-end[1])>abs(beg[0]-end[0]):
        if beg[1] > end[1]:  # guard
            return make_line(end, beg)
        dy = 16
        if (end[1] == beg[1]):
            dx = 0
        else:
            dx = 16 * (end[0] - beg[0]) / (end[1] - beg[1])

        x = beg[0]
        y = beg[1]
        result = []
        while y <= end[1]:
            result.append([x, y])
            x = x + dx
            y = y + dy
        return result
    else:
        if beg[0]>end[0]: # guard
            return make_line(end, beg)
        dx = 16
        if (end[0]==beg[0]):
            dy=0
        else:
            dy = 16 * (end[1]-beg[1])/(end[0]-beg[0])

        x = beg[0]
        y = beg[1]
        result = []
        while x<=end[0]:
            result.append([x, y])
            x = x+dx
            y = y+dy
        return result
def on_mouse_move(pos, rel, buttons):
    global begin
    if sss==3:
        return
    if sss!=5 and sss!=6 and sss!=4 and sss!=8:
        if sss==7:
            what=3
        else:
            what = sss
        positions = [pos]
        begin = None
    else:
        if begin==None:
            positions = make_line(pos, pos)
        else:
            positions = make_line(begin, pos)
        begin = pos
        if sss==5:
            what = 2
        elif sss==4:
            what = 1
        elif sss==6:
            what = 0
        elif sss == 8:
            what = 3
    for p in positions:
        m.put(zzzz(p), what)
def update():
    global azss,bzss,afss,bfss,sss
    azss=time.time()
    bzss=time.time()
    afss=time.time()
    bfss=time.time()
    jitui_update()
    knife_update()
    g_update()
    nq_update()
    az_update(keyboard)
    bz_update(keyboard)
    af_update(keyboard)
    bf_update(keyboard)
    aq_update(keyboard)
    at_update(keyboard)
    bq_update(keyboard)
    bt_update(keyboard)
    global b,c,y,z,o,p,am,bm
    if keyboard.k_1:
        sss=1
    if keyboard.k_2:
        sss = 2
    if keyboard.k_3:
        sss = 0
    if keyboard.k_4:
        sss = 3
    if keyboard.k_5:
        sss=4
    if keyboard.k_6:
        sss=5
    if keyboard.k_7:
        sss = 6
    if keyboard.k_8:
        sss = 7
    if keyboard.k_9:
        sss = 8
    if keyboard.k_0 and keyboard.k_3:
        m.clear(0)
    if keyboard.k_0 and keyboard.k_2:
        m.clear(2)
    if keyboard.k_0 and keyboard.k_1:
        m.clear(1)
    if keyboard.k_0 and keyboard.k_8:
        m.clear(3)
    if z>=700:
        pass
    else:
        z+=4.6
        if pq('a'):
            z -= 4.6
    if y>=700:
        pass
    else:
        y+=4.6
        if pq('b'):
            y -= 4.6
    if keyboard.UP:
        if y<=20:
            pass
        else:
            y-=30
            if pq('b'):
                y += 30
    if keyboard.w:
        if z<=20:
            pass
        else:
            z-=30
            if pq('a'):
                z+= 30
    if b>=c-5 and b<=c+5:
        if z>y-5 and z<y:
            bm-=1
        elif y>z-5 and y<z:
            am-=1
    if bm<=0:
        print("ay")
        exit()
    if am<=0:
        print("by")
        exit()
    if keyboard.DOWN:
        y=700
    if keyboard.s:
        z=700
    if keyboard.d:
        if b>=1280:
            pass
        else:
            b+=10
            if pq('a'):
                b-=10
    if keyboard.a:
        if b<=20:
            pass
        else:
            b-=10
            if pq('a'):
                b += 10
    if keyboard.RIGHT:
        if c>=1280:
            pass
        else:
            c+=10
            if pq('b'):
                c -= 10
    if keyboard.LEFT:
        if c<=20:
            pass
        else:
            c-=10
            if pq('b'):
                c+= 10
    if keyboard.q:
        if o<20:
            o+=1
    if keyboard.e:
        if o>1:
            o-=1
    if keyboard.i:
        if p<20:
            p+=1
    if keyboard.p:
        if p>1:
            p-=1
def draw():
    screen.fill('#'+ccccc)

    screen.draw.filled_circle((b,z),o,'#'+aaa)
    screen.draw.filled_circle((c,y),p,'#'+bbb)
    jitui.draw()
    knife.draw()
    nq.draw()
    g.draw()
    for bz in bzs:
        bz.draw()
    for az in azs:
        az.draw()
    af.show and af.draw()
    bf.show and bf.draw()
    m.draw(screen)
    screen.draw.text("am:"+str(am)+" "+"bm:"+str(bm), (1170, 0),color="black")
    screen.draw.text("q,i-big e,p-small z,k-faster c,l-slower r,u-hit v,m-kick f,j-no hurt x,o-pong!",(200,10),color="black")
    screen.draw.text("1:onebrick 2:oneiron 3:oneclear 4:move 5:manybricks 6:manyirons 7:manyclear 8:onegrass 9:manygrass 0:clear all", (200, 0),color="black")
pgzrun.go()