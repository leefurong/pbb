b = []
d = []
def shuru():
    global b, d
    a=int(input())
    b=[]
    for i in range(a):
        b+=[input()]
    c=int(input())
    d=[]
    for i in range(c):
        d+= [input()]

e=[]
def f(sum):
    global e,b,d
    if len(b)!=0:
        h=b[0]
        b.remove(b[0])
        g=-1
        try:
            g=e.find(h)
        except ValueError:
            pass
        if g!=-1:
            aa=e[g:]
            aa.reverse()
            b=b+aa
    else:
        print("B win!")
        return
    if len(d) != 0:
        h = b[0]
        b.remove(b[0])
        g = -1
        try:
            g = e.find(h)
        except ValueError:
            pass
        if g != -1:
            bb = e[g:]
            bb.reverse()
            d = d + bb
    else:
        print("A win!")
        return

if __name__=="__main__":
    shuru()
    f()