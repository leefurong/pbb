from actor import Actor
from plane import Plane
class Blood(Actor):
    def __init__(self, ai):
        super().__init__(ai, [
            "0.png",
            "1.png",
            "2.png",
            "3.png",
            "4.png",
            "5.png",
            "6.png",
            "7.png",
            "8.png",
            "9.png",
            "10.png",
        ])
        self.rect.x=20
        self.rect.y = 20
    def update(self):
        super().update()
        planes = self.ai.find_actors_of_class(Plane)
        if planes:
            plane = planes[0]
            self.face = plane.hp
        else:
            self.face=0