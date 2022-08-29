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
        self.cards = [[None]*size for _ in range(size)]
        self.xinpai = xinpai
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
        card = Card(self.ctx, self.cell_width-10, v)
        card.goto(
            lie * self.cell_width + self.pos[0]+5,
            hang * self.cell_width + self.pos[1]+5,
        )
        self.cards[hang][lie] = card




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

    def fapai(self):
        # 怎样决定发在什么位置?
        empties = []
        for r in range(self.size):
            for  c in range(self.size):
                if not self.gezi[r][c]:
                    empties.append([r, c])
        weizhi = random.choice(empties)
        self.set(weizhi[0], weizhi[1], self.xinpai)
        print(self.gezi)



if __name__=="__main__":
    a = Qipan(4)
    a.set(0, 0, 2)
    a.set(0, 1, 4)
    a.set(0, 2, 0)
    a.set(0, 3, 4)
    print(a.movemovemove(0, 0, direction.right))

    # b = qipan(8)
    # b.print()
