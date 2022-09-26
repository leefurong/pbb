from pickle import TRUE
import copy
from pprint import PrettyPrinter
from pygame import Rect
import random
from card import Card
dlie=[0,0,-1,1]
dhang=[-1,1,0,0]

class direction:
    up=0
    down=1
    left=2
    right=3
class Qipan:
    def __init__(self, size, pos, edge_len, ctx, xinpai=2):
        self.ctx = ctx
        self.size=size
        self.cell_width = edge_len/size
        self.pos = pos
        self.gezi = [[0]*size for _ in range(size)]
        self.cards = [[Card(self.ctx, self.cell_width-10, 0) for _ in range(size)] for _ in range(size)]
        self.xinpai = xinpai
        self.isMoving = False
        self.dead = False
    def inside(self , hang, lie):
        return 0<=hang<self.size and self.size>lie>=0
    def hasMate(self , hang, lie):
        sum=self.gezi[hang][lie]
        if hang<self.size-1 and self.gezi[hang+1][lie]==sum:return True
        if lie<self.size-1 and self.gezi[hang][lie+1]==sum:return True
        return False

    def print(self):
        print(self.gezi)

    def set(self, hang, lie, v):
        self.gezi[hang][lie] = v

    def refresh_cards(self):
        for hang in range(self.size):
            for lie in range(self.size):
                card = self.cards[hang][lie]
                card.goto(
                    lie * self.cell_width + self.pos[0]+5,
                    hang * self.cell_width + self.pos[1]+5,
                )
                card.n = self.gezi[hang][lie]
# 2
# 0
# -4
    def detect(self, y, x, num):
        if x<0 or x>=self.size or y<0 or y>=self.size or \
            self.gezi[y][x]<0 or self.gezi[y][x]!=0 and self.gezi[y][x]!=num:
            return -1
        if self.gezi[y][x]:
            return num*-2
        return num
    def move(self, dx, dy, real=True):
        gezi_bak = copy.deepcopy(self.gezi)

        rangedict = {-1: range(self.size),
                      0: range(self.size),
                      1: range(self.size-1, -1, -1)}
        range_x = rangedict[dx]
        range_y = rangedict[dy]
        for row in range_y:
            for col in range_x:
                if self.gezi[row][col]==0:continue
                x=col
                y=row
                while True:
                    sum=self.detect(y+dy, x+dx, self.gezi[y][x])
                    if sum==-1:break
                    self.set(y, x, 0)
                    y+=dy
                    x+=dx
                    self.set(y, x, sum)
                if real:
                    self.cards[row][col].slideTo(
                        x * self.cell_width + self.pos[0] + 5,
                        y * self.cell_width + self.pos[1] + 5,
                        0.5
                    )

        for row in range_y:
            for col in range_x:
                self.gezi[row][col] = abs(self.gezi[row][col])
        self.isMoving = True
        self.ctx.clock.schedule_unique(self.moveEnd, 0.5)

        changed = self.gezi != gezi_bak
        if not real:
            self.gezi = gezi_bak
        return changed

    def moveEnd(self):
        self.isMoving = False

    def on_key_down(self, key):
        if self.isMoving:
            pass
        else:
            if key == self.ctx.keys.LEFT:
                self.move(-1, 0)
            if key == self.ctx.keys.RIGHT:
                self.move(1, 0)
            if key == self.ctx.keys.UP:
                self.move(0, -1)
            if key == self.ctx.keys.DOWN:
                self.move(0, 1)
            self.ctx.clock.schedule_unique(self.refresh_cards, 0.5)
            self.ctx.clock.schedule_unique(self.fapai_n, 0.5)





    def isAlive(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.gezi[i][j] == 0 or self.hasMate(i, j):
                    return True
        return False

    def canMoveTo(self,v,hang2, lie2):
        return self.inside(hang2, lie2) and self.gezi[hang2][lie2]==0 or self.gezi[hang2][lie2]==v

    def movemovemove(self, hang, lie, direction):
        me = self.what(hang, lie)
        newhang = hang+dhang[direction]
        newlie = lie+dlie[direction]
        while self.inside(newhang, newlie) and self.what(newhang, newlie) == 0:
            newhang  += dhang[direction]
            newlie  += dlie[direction]
        if self.inside(newhang, newlie) and me == self.what(newhang, newlie):
            return newhang,newlie
        else:
            return newhang - dhang[direction], newlie - dlie[direction]

    def what(self, hang, lie):
        return self.gezi[hang][lie]

    def draw_bg_cell(self, screen, row, col):
        line_color = (200, 200, 200)
        r = Rect((self.pos[0] + col * self.cell_width+4,
                  self.pos[1] + row * self.cell_width+4),
                   (self.cell_width-8, self.cell_width-8))
        screen.draw.filled_rect(r, line_color)
    def draw_bg(self, screen):
        for row in range(self.size):
            for col in range(self.size):
                self.draw_bg_cell(screen, row, col)
    def draw_cards(self, screen):
        for row in range(self.size):
            for col in range(self.size):
                self.cards[row][col] and self.cards[row][col].draw(screen)


    def draw(self, screen):
        self.draw_bg(screen)
        self.draw_cards(screen)
        if self.dead:
            screen.draw.text("You are dead!!!",
                             center=(200, 200),
                             color=(0, 0, 0))

    def fapai(self):
        # 怎样决定发在什么位置?
        empties = []
        for r in range(self.size):
            for  c in range(self.size):
                if not self.gezi[r][c]:
                    empties.append([r, c])
        if len(empties):
            weizhi = random.choice(empties)
            self.set(weizhi[0], weizhi[1], self.xinpai)
            self.refresh_cards()

    def fapai_n(self, n=2):
        for i in range(n): self.fapai()
        if self.sile():
            self.dead = True

    def sile(self):
        canMove = self.move(1, 0, False) or self.move(-1, 0, False) or self.move(0, 1, False) or self.move(0, -1, False)
        return not canMove





if __name__=="__main__":
    a = Qipan(4)
    a.set(0, 0, 2)
    a.set(0, 1, 4)
    a.set(0, 2, 0)
    a.set(0, 3, 4)
    print(a.movemovemove(0, 0, direction.right))

    # b = qipan(8)
    # b.print()
