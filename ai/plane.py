import pygame
from bomb import Bomb
import boat_bomb
from actor import Actor

def boat_bomb_is_active(_, boatbomb):
    return boatbomb.face==0
class Plane(Actor):
    def __init__(self, ai):
        super().__init__(ai,["plane.png"])
        self.move_right = False
        self.move_left=False
        self.hp = 10
    def fire(self):
        bomb = Bomb(self.ai)
        bomb.rect.midbottom = self.rect.midbottom
        self.ai.add_actor(bomb)
    def kouxue(self):
        self.hp -=1
        print(self.hp)
        if self.hp ==0:
            self.dead = True

    def check_event(self, event):
        super().check_event(event)
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
        super().update()
        if self.move_right and self.rect.right<self.ai.screen.get_rect().right:
            self.rect.x += 10
        if self.move_left and self.rect.left>self.ai.screen.get_rect().left:
            self.rect.x -= 10
