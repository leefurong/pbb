import pymunk
import pymunk.pygame_util
import pygame

GRAY = (220, 220, 220)
space = pymunk.Space()
space.gravity = 0, -900
b0 = space.static_body

class Circle:
    def __init__(self, p0, radius=10, color=None):
        self.body = pymunk.Body()
        self.body.position = p0
        shape = pymunk.Circle(self.body, radius)
        shape.density = 0.01
        shape.elasticity = 0.5
        shape.friction = 0.5
        if color != None:
            shape.color = color
        App.current.space.add(self.body, shape)

class App:
    size = 700, 240
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.draw_options = pymunk.pygame_util.DrawOptions(self.screen)
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.image.save(self.screen, 'intro.png')

            self.screen.fill(GRAY)
            space.debug_draw(self.draw_options)
            pygame.display.update()
            space.step(0.01)

        pygame.quit()

if __name__ == '__main__':
    p0, p1 = (0, 0), (700, 0)
    segment = pymunk.Segment(b0, p0, p1, 4)
    segment.elasticity = 1

    body = pymunk.Body(mass=1, moment=10)
    body.position = (100, 200)

    circle = pymunk.Circle(body, radius=30)
    circle.elasticity = 0.95
    space.add(body, circle, segment)

    App().run()