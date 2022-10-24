import pgzrun
import time
import random
pp=0
b=0
c=0
COLORS={"grey": "灰",
       "green":"绿",
       "red":"红",
       "orange": "橙",
       "yellow":"黄",
       "blue":"蓝",
       "purple":"紫"}
WIDTH = 600
HEIGHT = 600
gezi=[[0,0,0,0],
      [0,0,0,0],
      [0,0,0,0],
      [0,0,0,0]]
def run_session(items):
    global gezi
    gezi = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for item in items:
        c=random.randint(0,3)
        d=random.randint(0,3)
        while gezi[c][d]!=0:
            c = random.randint(0,3)
            d = random.randint(0,3)
        gezi[c][d] = item

def get_rgb(c):
    return {
        "grey": (50, 50, 50),
        "green": (0, 255, 0),
        "red": (255, 0, 0),
        "orange": (250, 132, 43),
        "yellow": (245, 255, 0),
        "blue": (0, 0, 255),
        "purple": (135, 115, 161)
    }[c]
def draw():
    screen.fill("#818479")
    cell_w = WIDTH / len(gezi)
    for i in range(len(gezi)):
        for j in range(len(gezi[0])):
            if gezi[i][j]:
                x = j*cell_w
                y = i*cell_w
                r = Rect((x, y), (cell_w, cell_w))
                color = get_rgb(gezi[i][j][0])
                screen.draw.filled_rect(r,color)
                x+=cell_w/2
                y+=cell_w/2
                text = gezi[i][j][1]
                text_color="white"
                if gezi[i][j][0] in ["green", "yellow"]:
                    text_color="black"
                screen.draw.text(text, (x-10, y-10),
                                 color=text_color)


def begin_game(a, b):
    d=[]
    c = list(COLORS.keys())
    jishu=0
    for i in range(a):
        if jishu<b:
            choice1 = random.choice(c)
            choice2 = random.choice(c)
            while choice1==choice2:
                choice1 = random.choice(c)
                choice2 = random.choice(c)
            d.append((choice1, choice2))
        else:
            choice1 = random.choice(c)
            d.append((choice1,choice1))
        jishu+=1
    run_session(d)
def rand_game():
    a=int(random.randint(4,8))
    pp=int(random.randint(1,a))
    begin_game(a, pp)
def is_success():
    for i in gezi:
        for j in i:
            if j and j[0]!=j[1]:
                return False
    return True

def update():
    global b,c
    a=time.time()
    if keyboard.SPACE:
        b=time.time()
        rand_game()
    if is_success():  
        if c!=0:
            print(c,a-b)
            if a-b<=pp+5:
                print("合格")
            else:
                print("不合格")
        b=time.time()
        rand_game()
        c+=1
def on_mouse_down(pos):
    gezi_w = WIDTH/len(gezi)
    j = int(pos[0]//gezi_w)
    i = int(pos[1] // gezi_w)
    if gezi[i][j] and (gezi[i][j][0]!=gezi[i][j][1]):
        gezi[i][j] = 0
pgzrun.go()