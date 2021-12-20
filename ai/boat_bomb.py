import plane
from bomb import Bomb
import time
class BoatBomb(Bomb):
    def update(self):
        if self.face == 0:
            self.forward(5)
        if self.face == 1 and self.baozha_time + 3 <= time.time():
            self.dead = True
        if self.ai.pengdao(self, plane.Plane) and self.face == 0:
            p = self.ai.find_actors_of_class(plane.Plane)[0]
            p.kouxue()
            self.next_face()
            self.baozha_time = time.time()
        if self.rect.y < 10:
            self.dead = True