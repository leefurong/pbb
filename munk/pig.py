import sys
import pygame
from actor import Actor
import pymunk
import random
import pymunk.pygame_util
from peng import penglema
THECOLORS = {"lightgray": (79, 79, 79)}
DANGONG_POS = (100, 400)
PIG_POS = (350, 200)
segment_bodies = []
PIG_R = 50
is_dragging = False
pig_alive = True
def add_ball(space):
    mass = 3
    radius = 25
    body = pymunk.Body()  # 1
    x = random.randint(120, 300)
    body.position = x, 50  # 2
    shape = pymunk.Circle(body, radius)  # 3
    shape.elasticity = 0.9
    shape.mass = mass  # 4
    shape.friction = 3
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
    space.add(body, shape, )  # 5
    return shape
def add_static_L(space):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)  # 1
    body.position = (300, 300)
    l1 = pymunk.Segment(body, (50, 0), (455, 0), 5)  # 2
    l2 = pymunk.Segment(body, (50, 0), (50, -50), 5)
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
    l1.friction = 10  # 3
    l1.elasticity = 0.6669
    space.add(body, l1)  # 4
    segment_bodies.append((body, l1, point_a, point_b))
    return l1
old_point = None
def play_bgm():
    file='music1.mp3'
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(-1)
def play_fire():
    file = '鸟飞.wav'
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
def play_drag():
    file = '皮筋的声音.wav'
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()


def far_away(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    a = abs(x1-x2)
    b = abs(y1-y2)
    return a*a + b*b > 5
def add_frame(space):
    add_segment(space, (0, 0), (1200, 0))
    add_segment(space, (0,0), (0, 600))
    add_segment(space, (0,600), (1200, 600))
    add_segment(space, (1200, 0), (1200, 600))
def mouse_inside(mouse_pos, left, top, right, bottom):
    mx, my = mouse_pos
    return left<=mx<=right and top<=my<=bottom
def make_pig(space, x, y):
    pig_dot = add_dot(space, x, y, PIG_R)
    pig = Actor("pig.png", pig_dot, space)
    return pig
def make_bird(space):
    bird_dot = add_ball(space)
    bird = Actor("bird.png", bird_dot, space)
    return bird
def make_pigs(space):
    pigs=[]
    for i in range(1):
        pig = make_pig(space, 400, 200)
        pigs.append(pig)
    return pigs

def main():
    global is_dragging
    pygame.init()
    screen = pygame.display.set_mode((1200, 600)) # pygame.FULLSCREEN
    dangong_img = pygame.image.load("弹弓.png").convert_alpha()
    draw_options = pymunk.pygame_util.DrawOptions(screen)
    pygame.display.set_caption("Joints. Just wait and the L will tip over")
    clock = pygame.time.Clock()
    space = pymunk.Space()  #2
    space.gravity = (0.0, 1000.0)
    l1,l2 = add_static_L(space)
    add_frame(space)
    pigs = make_pigs(space)
    bird = make_bird(space)
    play_bgm()
    dots = []
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if not pigs:
                    pigs=make_pigs(space)
            elif event.type==pygame.MOUSEBUTTONDOWN\
                and\
                mouse_inside(pygame.mouse.get_pos(), 100, 400, 150, 450):
                is_dragging=True
                play_drag()
            elif event.type==pygame.MOUSEBUTTONUP:
                if is_dragging:
                    play_fire()
                    is_dragging=False
                    space.gravity = (0.0, 500.0)
                    x, y = pygame.mouse.get_pos()
                    x2, y2 = 130, 435
                    bird.body.velocity = (5*(x2 - x), 5*(y2 - y))
        left_holding = pygame.mouse.get_pressed()[0]
        global old_point, pig_alive
        screen.fill((255, 255, 255))
        if is_dragging:
            pygame.draw.line(screen, (0,0,0), pygame.mouse.get_pos(), (110, 435), 5)
            pygame.draw.line(screen, (0, 0, 0), pygame.mouse.get_pos(),
                             (150, 435), 5)
            bird.body.position=pygame.mouse.get_pos()
            space.gravity = (0.0, 0.0)
        space.debug_draw(draw_options)
        screen.blit(dangong_img, DANGONG_POS)
        bird.draw(screen)
        for pig in pigs:
            pig_pos = list(pig.position())
            if penglema(bird.body.position, 25,  pig_pos, PIG_R):
                if pig.alive:
                    pig.kill()
                    pigs.remove(pig)
            pig.draw(screen)


        space.step(1 / 50.0)  #3

        pygame.display.flip()
        clock.tick(50)
if __name__ == '__main__':
    sys.exit(main())