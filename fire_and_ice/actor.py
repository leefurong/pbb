import pygame, pymunk
import time, math

def calcAngle(x1, y1, x2, y2):
    dy = y1-y2
    dx = x2-x1
    ans =  dx and 180 * math.atan(dy / dx)/math.pi or (dy>0 and 270 or 90)
    if x2<x1:
        ans += 180
    return ans

def make_rect_shape(space, rect, body_type=pymunk.Body.DYNAMIC):
    body = pymunk.Body(body_type=body_type)
    body.position = rect.center
    vertices = [
        (rect.left - rect.center[0], rect.top - rect.center[1]), # lt
        (rect.right - rect.center[0], rect.top - rect.center[1]), # tr
        (rect.right - rect.center[0], rect.bottom - rect.center[1]), # rb
        (rect.left - rect.center[0], rect.bottom - rect.center[1]), # bl
        #     lt            tr
        #
        #
        #     bl------------rb
    ]
    shape = pymunk.Poly(body, vertices)
    shape.elasticity = 0.8
    shape.mass = 50
    shape.friction = 0.05
    space.add(body, shape)
    return shape


class Actor:
    def __init__(self, game, img_paths, center, body_type=pymunk.Body.DYNAMIC):
        self.game = game
        self.images = [pygame.image.load("images/" + p) for p in img_paths]
        self.rect = self.images[0].get_rect()
        self.rect.center=center
        self.shape = make_rect_shape(game.space, self.rect, body_type=body_type)
        self.body = self.shape.body
        self.dead = False
        self.face = 0
        self.tasks = set()
        self.angle = 0
        self.visibility = True

        # self.space = game.space
        # self.body=self.shape.body
    def shouguangbo(self, s):
        pass
    def show(self):
        self.visibility=True
    def hide(self):
        self.visibility = False

    def set_face_number(self, x):
        self.face = x

    def next_face(self):
        self.face = (self.face + 1) % len(self.images)

    def update(self):
        to_delete = set()
        for t in self.tasks.copy():
            task, task_time = t
            if time.time() > task_time:
                task()
                to_delete.add(t)
        self.tasks = self.tasks - to_delete

    def check_event(self, event):
        pass

    def goto(self, x, y):
        self.body.position = x, y

    def setAngle(self, a):
        self.body.angle = a
        # TODO: 还要设置图片的angle
    def rotate(self, a):
        self.angle += a
        self.images = [pygame.transform.rotate(img, a) for img in self.images]

    def headingTo(self, actorClass):
        x1, y1 = self.rect.x, self.rect.y
        targets = self.game.find_actors_of_class_and_face(actorClass, 0)
        if targets:
            target = targets[0]
            x2, y2 = target.rect.x, target.rect.y
            angle = calcAngle(x1, y1, x2, y2)
            self.rotate(angle - self.angle)

    def forward(self, d):
        self.rect.x += d * math.cos(self.angle*math.pi/180)
        self.rect.y -= d * math.sin(self.angle*math.pi/180)

    def draw(self):
        if self.visibility:
            # TODO: convert body rect ==> pygame rect
            hw = self.rect.width/2
            hh = self.rect.height/2
            lt = (self.body.position[0]-hw, self.body.position[1]-hh)
            self.game.screen.blit(self.images[self.face], lt)

    def buzhi(self, task, seconds):
        task_time = time.time() + seconds
        self.tasks.add((task, task_time))

    def buzhi_loop(self, task, every_seconds):
        def task_and_add_self():
            task()
            self.buzhi(task_and_add_self, every_seconds)

        self.buzhi(task_and_add_self, every_seconds)

    def setVelocityX(self, vx):
        self.body.velocity = (vx, self.body.velocity[1])

    def setVelocityY(self, vy):
        self.body.velocity = (self.body.velocity[0], vy)
