import os
a=0
d=0
c=0
try:
    while a<1:
        print("如水师海谁？")
        b=input()
        if b=='日u':
            a=1
        else:
            a=0
    a=input("校有教，备长师名三么？A.霞 B.希 C.彬 D.群")
    if a=='r ong':
        d+=1
    else:
        c+=1
    p=input("家果外削何？ A.榴 B.卜 C.市 D.西")
    if p=='萝菠啊':
        d+=1
    else:
        c+=1
    o=input("家安如？ A.很 B.飞满 C.可 D.吱吱 ")
    if o=='PeI':
        d+=1
    else:
        c+=1
    e=input("家水谁？ A.g B.q C.l D.j")
    if e=='xiji':
        d+=1
    else:
        c+=1
    f=input("家所何？ A.苍 B.无 C.h D.chou ")
    if f=='n闻y':
        d+=1
    else:
        c+=1
    if d*20<60:
        while True:
            l=input("是否关机?")
            if l=='qQnLdGbTbGj':
                break
            elif l=='否':
                print("不，你要关机！！！")
            else:
                os.system("shutdown -s -t  10 ")
    else:
        print(d*20)
except KeyboardInterrupt:
    os.system("shutdown -s -t  3 ")