import pymunk, pygame
from actor import Actor
class Ice(Actor):
    def __init__(self, id, game):
        super().__init__(id, game, ["ice.png"], (300, 300))
        self.shape.elasticity=0
        self.shape.friction=5
        self.setMoveKeys(up=pygame.K_w, left=pygame.K_a, right=pygame.K_d)
        self.type = "ice"
