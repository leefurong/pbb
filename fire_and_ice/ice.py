import pymunk, pygame
from actor import Actor
class Ice(Actor):
    def __init__(self, game):
        super().__init__(game, ["ice.png"], (300, 300))
        self.shape.elasticity=0
        self.shape.friction=5
    def check_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            self.setVelocityY(-300)
        return super().check_event(event)
    def update(self):
        self.setAngle(0)
        if self.game.is_pressing(pygame.K_RIGHT):
            self.body.velocity = (60, self.body.velocity[1])
        elif self.game.is_pressing(pygame.K_LEFT):
            self.body.velocity = (-60, self.body.velocity[1])
        return super().update()