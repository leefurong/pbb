from ice import Ice
from fire import Fire
from floor import Floor
import pygame, sys, pymunk, pymunk.pygame_util



class Game:
    def __init__(self):
        self.space = pymunk.Space()  #2
        self.space.gravity = (0.0, 400.0)
        self.screen = pygame.display.set_mode(
            (800, 600))
        self.draw_options = pymunk.pygame_util.DrawOptions(self.screen)
        self.actors = {
            "ice": Ice(self),
            "fire": Fire(self)
        }
        self.addFloor()
        self.pressing_key = set()
    def addFloor(self):
        y = 600
        x = 0
        for i in range(20):
            k = "floor"+str(i)
            self.actors[k] = Floor(self, (x, y))
            x += 60
    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.pressing_key.add(event.key)
            if event.type == pygame.KEYUP:
                self.pressing_key.remove(event.key)
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