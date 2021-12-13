from plane import Plane
from bomb import Bomb
import time
class BoatBomb(Bomb):
    def update(self):
        super().update()
        if self.face == 0:
            self.forward(5)
        if self.rect.y<=10 and self.face == 0:
            self.next_face()
            self.baozha_time = time.time()
        if self.face == 1 and self.baozha_time + 3 <= time.time():
            self.dead = True