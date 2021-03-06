from typing import Set
import pygame, sys, time
from settings import Settings
from plane import Plane
from bbb import BBB
from bomb import Bomb
from boat import Boat
from sea import Sea
from blood import Blood
from bb import BB
class AlienInvasion:
    def __init__(self):
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        self.actors = []
        self.actors.append(Sea(self))
        self.actors.append(BBB(self))
        self.actors.append(Boat(self))
        self.makeplane()
        self.actors.append(Blood(self))
        self.yuyi_memory = {}
    def makeplane(self):
        self.actors.append(Plane(self))
    def add_actor(self, actor):
        self.actors.append(actor)
    def _pengdao(self, a, b):
        return a.rect.colliderect(b.rect)
    def find_actors(self, f):
        return [a for a in self.actors if f(a)]
    def find_actors_of_class_and_face(self, cls, face):
        """找到符合类要求，及编号要求的角色"""
        f = lambda a: type(a) == cls and a.face == face
        return self.find_actors(f)

    def find_actors_of_class(self, cls):
        """找到符合类要求，及编号要求的角色"""
        f = lambda a: type(a) == cls
        return self.find_actors(f)
    def pengdao(self, actor_a, cls, f=lambda _,__:True):
        """Return whatever the first one I am colliding. """
        def oneOfCls(actor):
            return type(actor) == cls
        for actor_b in filter(oneOfCls, self.actors):
            if self._pengdao(actor_a, actor_b) and f(actor_a, actor_b):
                return actor_b
    def yuyi(self, t, f):
        now = time.time()
        if now-self.yuyi_memory.get(f, 0) >= t:
            self.yuyi_memory[f] = now
            f()
    def delete(self,cls):
        for i in cls:
            self.actors.remove(i)
    def faguangbo(self, s):
        actors = self.actors.copy()
        for actor in actors:
            actor.shouguangbo(s)
    def run_game(self):
        while True:
            # 事件检测、处理
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                for actor in self.actors:
                    actor.check_event(event)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r and not self.find_actors_of_class(Plane):
                        self.makeplane()

            # 刷新各个角色的状态
            for actor in self.actors:
                actor.update()

            # 绘制屏幕
            self.screen.fill(self.settings.bg_color)
            for actor in self.actors:
                actor.blitme()
            pygame.display.flip()

            self.actors = [a for a in self.actors if not a.dead]
