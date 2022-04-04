import pymunk
from actor import Actor


class Block(Actor):
    def __init__(self, game, center):
        super().__init__(game, ["block.png"], center, pymunk.Body.STATIC)
