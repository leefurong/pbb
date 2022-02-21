import sys
import pygame
from actor import Actor
import pymunk
import random
import pymunk.pygame_util
from peng import penglema
THECOLORS = {"lightgray": (79, 79, 79)}
# DANGONG_POS = (100, 400)
PIG_POS = (350, 200)
segment_bodies = []
pig_alive = True
def add_ball(space):
    mass = 50
    radius = 25
    body = pymunk.Body()  # 1
    x = random.randint(120, 300)
    body.position = x, 50  # 2
    shape = pymunk.Circle(body, radius)  # 3
    shape.elasticity = 0.9
    shape.mass = mass  # 4
    shape.friction = 0
    space.add(body, shape)  # 5
    return shape
def add_tianpin(space):
    mass = 5
    body = pymunk.Body()
    body2=pymunk.Body()
    body.position = (650, 550)
    ban = pymunk.Segment(body, (-150, 0), (150, 0), 5)  # 2

    ban.mass = mass  # 4
    ban.friction = 2
    spring1 = pymunk.constraints.DampedSpring(ban.body, di.body, (-150, 0), (500, 585), 15, 100, 3)
    spring2 = pymunk.constraints.DampedSpring(ban.body, di.body, (150, 0),
                                              (800, 585), 15, 100, 3)
    space.add(body, ban)  # 5spring1, spring2

    return ban
def add_segment(space, point_a, point_b):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)  # 1
    body.position = (0, 0)
    l1 = pymunk.Segment(body, point_a, point_b, 5)  # 2
    l1.friction = 0  # 3
    l1.elasticity = 0.6669
    space.add(body, l1)  # 4
    segment_bodies.append((body, l1, point_a, point_b))
    return l1
def add_rect(space, pos=(10, 10), weight=10, size=20):
    body = pymunk.Body()
    body.position = pos
    vertices = [(-size / 2, -size / 2), (size / 2, -size / 2),
                (size / 2, size / 2), (-size / 2, size / 2),
                ]
    shape = pymunk.Poly(body, vertices)
    shape.elasticity = 0.8
    shape.mass = 50
    shape.friction = 0.05
    space.add(body, shape)
    return shape

di=None
def add_frame(space):
    global di
    add_segment(space, (0, 0), (1200, 0))
    add_segment(space, (0,0), (0, 600))
    di = add_segment(space, (0,600), (1200, 600))
    add_segment(space, (1200, 0), (1200, 600))
def mouse_inside(mouse_pos, left, top, right, bottom):
    mx, my = mouse_pos
    return left<=mx<=right and top<=my<=bottom
def make_pig(space, x, y):
    pig_dot = add_tianpin(space)
    pig = Actor("pig.png", pig_dot, space)
    return pig
def make_fama(space,pos):
    bianchang = 50
    fang = add_rect(space,pos, 0.001, bianchang)
    a = Actor("fama.png", fang, space)
    a.bianchang = bianchang
    return a
def connect(space, pig_a):
    a= pig_a.body
    zhidian_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    c = pymunk.constraints.PivotJoint(a, zhidian_body, (650, 550))
    space.add(c)

def main():
    is_dragging=None
    pygame.init()
    screen = pygame.display.set_mode((1200, 600)) # pygame.FULLSCREEN
    # dangong_img = pygame.image.load("弹弓.png").convert_alpha()
    draw_options = pymunk.pygame_util.DrawOptions(screen)
    pygame.display.set_caption("Joints. Just wait and the L will tip over")
    clock = pygame.time.Clock()
    space = pymunk.Space()  #2
    space.gravity = (0.0, 1000.0)
    add_frame(space)
    pig = make_pig(space, 500, 300)
    famas = [make_fama(space,(100,100))]
    dots = []
    connect(space, pig)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)
            elif event.type==pygame.MOUSEBUTTONDOWN:
                for fama in famas:
                    l = fama.body.position[0]-fama.bianchang/2
                    r = fama.body.position[0]+fama.bianchang/2
                    t = fama.body.position[1] - fama.bianchang / 2
                    b = fama.body.position[1] + fama.bianchang / 2
                    if mouse_inside(pygame.mouse.get_pos(), l,t,r,b):
                        is_dragging=fama

            elif event.type==pygame.MOUSEBUTTONUP:
                if is_dragging:
                    is_dragging=None
                    space.gravity = (0.0, 1000.0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                famas.append(make_fama(space,pygame.mouse.get_pos()))
        left_holding = pygame.mouse.get_pressed()[0]
        global old_point, pig_alive
        screen.fill((255, 255, 255))
        if is_dragging:
            is_dragging.body.position=pygame.mouse.get_pos()
            space.gravity = (0.0, 0.0)
        space.debug_draw(draw_options)
        # screen.blit(dangong_img, DANGONG_POS)
        # fama.draw(screen)


        space.step(1 / 50.0)  #3

        pygame.display.flip()
        clock.tick(50)
if __name__ == '__main__':
    sys.exit(main())