import pymunk
from actor import Actor


class Block(Actor):
    def __init__(self, id, game, center):
        super().__init__(id, game, ["block.png"], center, pymunk.Body.STATIC)
        self.type="block"
