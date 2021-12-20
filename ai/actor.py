import pygame
import time, math

def calcAngle(x1, y1, x2, y2):
    dy = y1-y2
    dx = x2-x1
    ans =  dx and 180 * math.atan(dy / dx)/math.pi or (dy>0 and 270 or 90)
    print("calcAngle(", x1, y1, x2, y2, "): ", ans)
    return ans+180


class Actor:
    def __init__(self, ai, img_paths):
        self.ai = ai
        self.images = [pygame.image.load("images/" + p) for p in img_paths]
        self.rect = self.images[0].get_rect()
        self.dead = False
        self.hide = False
        self.face = 0
        self.tasks = set()
        self.angle = 0

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

    def rotate(self, a):
        self.angle += a
        self.images = [pygame.transform.rotate(img, a) for img in self.images]

    def headingTo(self, actorClass):
        x1, y1 = self.rect.x, self.rect.y
        target = self.ai.find_actors_of_class_and_face(actorClass, 0)[0]
        x2, y2 = target.rect.x, target.rect.y
        angle = calcAngle(x1, y1, x2, y2)
        self.rotate(angle - self.angle)

    def forward(self, d):
        self.rect.x += d * math.cos(self.angle*math.pi/180)
        self.rect.y -= d * math.sin(self.angle*math.pi/180)

    def blitme(self):
        self.ai.screen.blit(self.images[self.face], self.rect)

    def buzhi(self, task, seconds):
        task_time = time.time() + seconds
        self.tasks.add((task, task_time))

    def buzhi_loop(self, task, every_seconds):
        def task_and_add_self():
            task()
            self.buzhi(task_and_add_self, every_seconds)

        self.buzhi(task_and_add_self, every_seconds)
