dlie=[0,0,-1,1]
dhang=[-1,1,0,0]

class direction:
    up=0
    down=1
    left=2
    right=3
class qipan:
    def __init__(self, size):
        self.size=size
        self.gezi = [[0]*size for _ in range(size)]
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

if __name__=="__main__":
    a = qipan(4)
    a.set(0, 0, 2)
    a.set(0, 1, 4)
    a.set(0, 2, 0)
    a.set(0, 3, 4)
    print(a.movemovemove(0, 0, direction.right))

    # b = qipan(8)
    # b.print()
