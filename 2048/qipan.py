class qipan:
    def __init__(self, size):
        self.size=size
        self.gezi = [[0]*size for _ in range(size)]

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

if __name__=="__main__":
    a = qipan(2)
    a.set(0, 1, 26)
    a.set(1, 1, 2048)
    a.set(1, 0, 12)
    a.set(0, 0, 2048)
    print(a.isAlive())

    # b = qipan(8)
    # b.print()
