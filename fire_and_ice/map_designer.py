import json
from random import randint
def rand_pos():
    return (randint(-100, 900), randint(0, 600))

def make_random():
    ans = []
    for i in range(50):
        pos = rand_pos()
        id = "block"+str(i)
        item = {"pos": pos, "id": id, "type": "block"}
        ans.append(item)
    ice_conf={"id": "ice", "type": "ice", "pos": rand_pos()}
    ans.append(ice_conf)
    fire_conf = {"id": "fire", "type": "fire", "pos": rand_pos()}
    ans.append(fire_conf)
    return ans

if __name__=="__main__":
    _map = make_random()
    s = json.dumps(_map)
    f = open("guanqia/map1.json", "w")
    f.write(s)