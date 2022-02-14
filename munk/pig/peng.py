def juli(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return (abs(x1-x2)**2+abs(y1-y2)**2)**(1/2)
def penglema(pos1, r1, pos2, r2):
    d=juli(pos1, pos2)
    print(d, r1+r2+15)
    return d<=r1+r2+15
if __name__=="__main__":
    print(penglema((10, 10), 10, (20, 20), 100)) # True
    print(penglema((10, 10), 2, (200, 200), 3))  # False