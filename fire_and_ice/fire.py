import pymunk, pygame
from actor import Actor
class Fire(Actor):
    def __init__(self, id, game):
        super().__init__(id, game, ["fire.png"], (300, 300))
        self.shape.elasticity=0
        self.shape.friction=5
        self.setMoveKeys(up=pygame.K_UP, left=pygame.K_LEFT, right=pygame.K_RIGHT)
        self.type = "fire"
