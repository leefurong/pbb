import pygame
import time

class Actor:
    def __init__(self, ai, img_paths):
        self.ai = ai
        self.images = [pygame.image.load("images/"+p) for p in img_paths]
        self.rect = self.images[0].get_rect()
        self.dead = False
        self.hide = False
        self.face = 0
        self.tasks = set()

    def set_face_number(self, x):
        self.face = x
    def next_face(self):
        self.face = (self.face+1)%len(self.images)

    def update(self):
        to_delete = set()
        for t in self.tasks.copy():
            task, task_time = t
            if time.time()>task_time:
                task()
                to_delete.add(t)
        self.tasks = self.tasks - to_delete

    def check_event(self, event):
        pass

    def blitme(self):
        self.ai.screen.blit(self.images[self.face], self.rect)
    def buzhi(self, task, seconds):
        task_time = time.time()+seconds
        self.tasks.add((task, task_time))
    def buzhi_loop(self, task, every_seconds):
        def task_and_add_self():
            task()
            self.buzhi(task_and_add_self, every_seconds)

        self.buzhi(task_and_add_self, every_seconds)
