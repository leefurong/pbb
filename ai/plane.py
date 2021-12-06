import pygame
from bomb import Bomb
class Plane:
    def __init__(self, ai):
        self.ai = ai
        self.image = pygame.image.load('images/plane.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.ai.screen.get_rect().midbottom
        self.rect.y = 10
        self.move_right = False
        self.move_left=False
        self.dead = False
    def fire(self):
        bomb = Bomb(self.ai)
        bomb.rect.midbottom = self.rect.midbottom
        self.ai.add_actor(bomb)

    def check_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.move_right = True
            if event.key == pygame.K_LEFT:
                self.move_left = True
            if event.key == pygame.K_SPACE:
                if not self.ai.find_actors_of_class_and_face(Bomb, 0):
                    self.fire()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.move_right = False
            if event.key == pygame.K_LEFT:
                self.move_left = False

    def update(self):
        if self.move_right and self.rect.right<self.ai.screen.get_rect().right:
            self.rect.x += 10
        if self.move_left and self.rect.left>self.ai.screen.get_rect().left:
            self.rect.x -= 10

    def blitme(self):
        self.ai.screen.blit(self.image, self.rect)
