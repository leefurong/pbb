import pgzrun
import getpass
a=getpass.getpass()
b=getpass.getpass()
map = Actor("map")
az = Actor("a")
bz = Actor("b")
HEIGHT = map.height
WIDTH = map.width
qipan = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
next = 1
focus = None
def nengxia():
    count = 0
    for row in qipan:
        for cell in row:
            if cell!=0:
                count += 1
    return count<6
def xiazi(hang, lie):
    hang,lie=int(hang),int(lie)
    if qipan[hang][lie]==0:
        qipan[hang][lie] = next
        goNext()
def is_neighbor(a, b):
    return (a[0] == b[0] and abs(a[1] - b[1]) == 1) or (a[1] == b[1] and abs(a[0] - b[0]) == 1)
def move(move_from, move_to):
    if is_neighbor(move_from, move_to) and qipan[move_to[0]][move_to[1]]==0:
        from_color = qipan[move_from[0]][move_from[1]]
        qipan[move_to[0]][move_to[1]] = from_color
        qipan[move_from[0]][move_from[1]] = 0
def on_mouse_down(pos):
    global focus
    hang, lie = int(pos[1] / 203), int(pos[0] / 203)
    if nengxia():
        xiazi(hang, lie)
    else:
        if focus:
            move(focus, (hang,lie))
            focus = None
        else:
            focus = (hang,lie)
def goNext():
    global next
    if next == 1:
        next = 2
    else:
        next = 1
def draw():
    map.draw()
    for i in range(3):
        for j in range(3):
            status = qipan[i][j]
            x = (j+1) *203-101
            y = (i+1)*203-101
            if status==1:
                az.pos = (x, y)
                az.draw()
            if status == 2:
                bz.pos = (x, y)
                bz.draw()
clear_keys = set()
def update_keys(key):
    if len(clear_keys)==2:
        clear_keys

def update():
    global a,b,qipan
    if eval("keyboard."+a) and eval("keyboard."+b):
       qipan = [[0, 0, 0],[0, 0, 0],[0, 0, 0]] 
pgzrun.go()