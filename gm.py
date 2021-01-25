from pygame import Rect
WIDTH=50
HEIGHT=85
def make_row(n, v):
    return [v]*n
def m_e(w,h,v):
    result = []
    for _ in range(w):
        result.append(make_row(h, v))
    return result
class GM:
    def __init__(self, grass):
        self.sz=m_e(WIDTH,HEIGHT,0)
        self.grass=grass
    def clear(self,aaa):
        self.sz=m_e(WIDTH, HEIGHT, aaa)
    def draw(self, screen):
        for row in range(len(self.sz)):
            for col in range(len(self.sz[0])):
                x = col*16
                y = row*16
                rect = Rect(x, y, 16, 16)
                if self.sz[row][col]==1:
                    screen.draw.filled_rect(rect,'brown')
                elif self.sz[row][col]==2:
                    screen.draw.filled_rect(rect,'grey')
                elif self.sz[row][col]==3:
                    self.grass.x=rect.x+8
                    self.grass.y=rect.y+8
                    self.grass.draw()
    def put(self, pos, what):
        try:
            self.sz[pos[1]][pos[0]]=what
        except IndexError:
            print(self.sz[pos[1]][pos[0]])
    def pm(self, fw):
        ps = self.ps(fw)
        return 1 in ps or 2 in ps
    def bomb(self, fw):
        bombed = False
        try:
            left, top, width, height = (int(fw[0] / 16), int(fw[1] / 16),int(fw[2] / 16), int(fw[3] / 16))
        except TypeError:
            left = int(fw.x / 16)
            top = int(fw.y / 16)
            width = int(fw.width / 16)
            height = int(fw.height / 16)
        for row in range(top, top+height+1):
            for col in range(left,left+width):
                try:
                    if self.sz[row][col] in [1,2]:
                        bombed = True
                    if self.sz[row][col]==1:
                        self.sz[row][col]=0
                except IndexError:
                    pass
        return bombed
                

    def ps(self,fw):
        result = set()
        try:
            left,top,width,height=(int(fw[0]/16), int(fw[1]/16), int(fw[2]/16), int(fw[3]/16))
        except TypeError:
            left = int(fw.x/16)
            top = int(fw.y/16)
            width=int(fw.width/16)
            height = int(fw.height/16)
        for row in range(top, top+height+1):
            for col in range(left,left+width):
                try:
                    result.add(self.sz[row][col])
                except IndexError:
                    pass
        return result