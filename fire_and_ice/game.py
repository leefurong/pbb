from ice import Ice
import pygame, sys, pymunk, pymunk.pygame_util



class Game:
    def __init__(self):
        self.space = pymunk.Space()  #2
        self.space.gravity = (0.0, 1000.0)
        self.screen = pygame.display.set_mode(
            (800, 800))
        self.draw_options = pymunk.pygame_util.DrawOptions(self.screen)
        self.actors = {"ice": Ice(self)}


    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def update(self):
        pass

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