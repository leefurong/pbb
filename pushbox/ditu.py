REN = 1
KONGQI = 0
XIANGZI = 2
QIANG = 3
MUDIDI = 4

ditu1 = [
    [0, 0, 0, 0, 0],
    [3, 3, 3, 3, 3],
    [3, 1, 2, 0, 4],
    [3, 3, 3, 3, 3],
    [0, 0, 0, 0, 0],
]

def get_ren(ditu):
    for i in range(len(ditu)):
        for j in range(len(ditu[0])):
            if(ditu[i][j]==REN):
                return i,j


def move(ditu, dx, dy):
    x, y = get_ren(ditu)
    newx = x+dx
    newy = y+dy
    ditu[x][y] = KONGQI
    ditu[newx][newy] = REN
    return ditu


if __name__=="__main__":
    print(get_ren(ditu1)) #