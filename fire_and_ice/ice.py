import pymunk, pygame
from actor import Actor
class Ice(Actor):
    def __init__(self, game):
        super().__init__(game, ["ice.png"], (300, 300))
        self.shape.elasticity=0
        self.shape.friction=5
        self.setMoveKeys(up=pygame.K_UP, left=pygame.K_LEFT, right=pygame.K_RIGHT)
