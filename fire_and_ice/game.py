from ice import Ice
import pygame, sys

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(
            (800, 800))
        self.actors = {"ice": Ice(self)}

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def update(self):
        pass

    def draw(self):
        self.screen.fill((230, 230, 230))
        for actor in self.actors.values():
            actor.draw()
        pygame.display.flip()

    def run(self):
        while True:
            self.handleEvents()
            self.update()
            self.draw()