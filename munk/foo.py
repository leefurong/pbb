import sys
import pygame
import pymunk  #1
import random
import pymunk.pygame_util

THECOLORS = {"lightgray": (79, 79, 79)}
segment_bodies = []

def add_ball(space):
    mass = 3
    radius = 25
    body = pymunk.Body()  # 1
    x = random.randint(120, 300)
    body.position = x, 50  # 2
    shape = pymunk.Circle(body, radius)  # 3
    shape.elasticity = 0.9999
    shape.mass = mass  # 4
    shape.friction = 10
    space.add(body, shape)  # 5
    return shape

def add_dot(space, x, y, r):
    mass = 3
    radius = 25
    body = pymunk.Body()  # 1
    body.position = x, y  # 2
    shape = pymunk.Circle(body, r)  # 3
    shape.mass = mass  # 4
    shape.friction = 0.6
    space.add(body, shape)  # 5
    return shape


def add_static_L(space):
    body = pymunk.Body()  # 1
    body.position = (300, 300)
    l1 = pymunk.Segment(body, (-150, 0), (255, 0), 5)  # 2
    l2 = pymunk.Segment(body, (-150, 0), (-150, -50), 5)
    l1.friction = 10  # 3
    l2.friction = 10
    l1.elasticity = 0.999
    l2.elasticity = 0.999

    space.add(body, l1, l2)  # 4
    return l1, l2

def add_segment(space, point_a, point_b):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)  # 1
    body.position = (0, 0)
    l1 = pymunk.Segment(body, point_a, point_b, 5)  # 2
    l1.friction = 1  # 3

    space.add(body, l1)  # 4
    segment_bodies.append((body, l1, point_a, point_b))
    return l1


old_point = None

def far_away(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    a = abs(x1-x2)
    b = abs(y1-y2)
    return a*a + b*b > 5


def rebuild_segments(space):
    """构造一条完整的弧线（由小线段组成）"""
    # body = pymunk.Body()  # 1
    # body.position = (0, 0)
    # lines=[body]
    # for (_, _, a, b) in segment_bodies[0:1]:
    #     l1 = pymunk.Segment(body, a, b, 5)  # 2
    #     l1.friction = 1  # 3
    #     lines.append(l1)
    # space.add(*lines)  # 4


def activate_segments(space):
    for (body, shape,_,_) in segment_bodies:
        space.remove(body, shape)
    rebuild_segments(space)
    segment_bodies.clear()
def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    draw_options = pymunk.pygame_util.DrawOptions(screen)
    pygame.display.set_caption("Joints. Just wait and the L will tip over")
    clock = pygame.time.Clock()

    space = pymunk.Space()  #2
    space.gravity = (0.0, 1000.0)

    balls = []
    for i in range(3):
        balls.append(add_ball(space))
    l1,l2 = add_static_L(space)

    dots = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)
        left_holding = pygame.mouse.get_pressed()[0]
        global old_point
        if left_holding:
            x, y = pygame.mouse.get_pos()
            if old_point and far_away((x,y), old_point):
                add_segment(space, old_point, (x, y))
            old_point = (x, y)
        else:
            if old_point:
                activate_segments(space)
            old_point=None
        screen.fill((255, 255, 255))

        space.step(1 / 50.0)  #3

        # for ball in balls:
        #     draw_ball(screen, ball)
        # draw_lines(screen, [l1, l2])
        space.debug_draw(draw_options)

        pygame.display.flip()
        clock.tick(50)


if __name__ == '__main__':
    sys.exit(main())