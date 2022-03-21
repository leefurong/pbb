import pymunk
from actor import Actor
class Ice(Actor):
    def __init__(self, game):
        super().__init__(game, ["ice.png"], (0, 0))
