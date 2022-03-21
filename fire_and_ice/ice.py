import pymunk, pygame
from actor import Actor
class Ice(Actor):
    def __init__(self, game):
        super().__init__(game, ["ice.png"], (300, 300))
        self.shape.elasticity=0
        self.shape.friction=10
    def check_event(self, event):
        try:
            if event.key==pygame.K_RIGHT:
                print("right", event)
        except:
            pass
        if self.game.is_pressing(pygame.K_RIGHT):
            self.body.velocity = (60, self.body.velocity[1])
        elif self.game.is_pressing(pygame.K_LEFT):
            self.body.velocity = (-60, self.body.velocity[1])
        return super().check_event(event)
