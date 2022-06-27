d = {"mao": 148, "li": 0, "zhang": 34, "lijiayi": 1}

def remove_odd(d):
    dd={}
    for i in d:
        if d[i]%2!=0:
            dd[i]=d[i]
    return dd

if __name__=="__main__":
    assert(remove_odd(d)=={"lijiayi": 1})