import json
def load(filename):
    filename = "guanqia/"+filename
    f=open(filename)
    s=f.read()
    return json.loads(s)

if __name__=="__main__":
    print(load("guanqia1.json"))