from ice import Ice
from fire import Fire
from block import Block
import pygame, sys, pymunk, pymunk.pygame_util
from game_data_loader import load
import json, time, os



class Game:
    def __init__(self):
        self.space = pymunk.Space()  #2
        self.space.gravity = (0.0, 400.0)
        self.screen = pygame.display.set_mode(
            (800, 600))
        self.draw_options = pymunk.pygame_util.DrawOptions(self.screen)
        self.actors={}
        _map = self.select_map()
        self.load_data(_map)
        self.pressing_key = set()
        self.click_add = None

    def select_map(self):
        maps = os.listdir("guanqia/")
        ans = self.ask(str(maps)+"\n请选择地图:  ")
        return ans

    def ask(self, question):
        return input(question)

    def load_data(self, filename):
        actor_confs = load(filename)
        for conf in actor_confs:
            self.add_actor_by_conf(conf)
    
    def save_data(self):
        confs = []
        for actor in self.actors:
            print("type of actor:", type(actor))
            conf = actor.export_conf()
            confs.append(conf)
        s = json.dumps(confs)
        filename = "guanqia/"+input("请输入地图名: ")+".json"
        with open(filename, "w") as f:
            f.write(s)


    def add_actor_by_conf(self, conf):
        id = conf["id"]
        pos = conf["pos"]
        _type = conf["type"]
        if _type=="block":
            self.add_block(id, pos)
        elif _type=="button":
            self.add_button(id, pos)
        elif _type=="door":
            self.add_door(id, pos, conf["controlled_by"])
        elif _type == "exit":
            self.add_exit(id, pos, conf["for"])
        elif _type=="ice":
            self.add_ice(id)
        elif _type=="fire":
            self.add_fire(id)

    def add_button(self, id, pos):
        pass

    def add_door(self, id, pos, controlled_by):
        pass

    def add_exit(self, id, pos, _for):
        pass

    def add_block(self, id, pos):
        self.actors[id] = Block(id, self, pos)

    def add_ice(self, id):
        self.actors[id] = Ice(id, self)
    
    def add_fire(self, id):
        self.actors[id] = Fire(id, self)


    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.pressing_key.add(event.key)
                if event.key == pygame.K_0:
                    self.click_add = None
                elif event.key == pygame.K_1:
                    self.click_add = "block"
                if event.key == pygame.K_s:
                    self.save_data()
            if event.type == pygame.KEYUP:
                self.pressing_key.remove(event.key)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.click_add:
                    _type = self.click_add
                    conf = {"id":str(time.time()), "type": _type, "pos": event.pos}
                    self.add_actor_by_conf(conf)
            for actor in self.actors.values():
                actor.check_event(event)
    def is_pressing(self, key):
        return key in self.pressing_key
    def update(self):
        for actor in self.actors.values():
            actor.update()

    def draw(self):
        self.screen.fill((230, 230, 230))
        self.space.debug_draw(self.draw_options)
        for actor in self.actors.values():
            actor.draw()
        pygame.display.flip()

    def run(self):
        while True:
            self.handleEvents()
            self.update()
            self.draw()
            self.space.step(1 / 50.0)