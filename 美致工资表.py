import os
def callback():
    pass
def shi():
    print("太少了！！你的电脑将在10秒后关机！")
    os.system("sudo shutdown -h now")
def fou():
    print("还敢不涨！！你的电脑将在10秒后关机！")
    os.system("sudo shutdown -h now")
def tankuang():
    import tkinter as tk
    window = tk.Tk()
    window.attributes("-fullscreen",True)
    l = tk.Label(window, 
        text='给李老师加1亿比特币的工资， 是否同意？',
        bg='brown', font=('Arial', 12), width=600, height=10)
    l.pack() 
    b = tk.Button(window, 
        text='是',     
        width=300, height=17, 
        command=shi)     
    b.pack()  
    c = tk.Button(window, 
        text='否',     
        width=300, height=17, 
        command=fou)     
    c.pack()  
    window.protocol("WM_DELETE_WINDOW", callback)
    window.mainloop()
tankuang()