import pymunk
from actor import Actor


class Floor(Actor):
    def __init__(self, game, center):
        super().__init__(game, ["floor.png"], center, pymunk.Body.STATIC)
