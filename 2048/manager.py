from qipan import qipan
class manager:
    def __init__(self, Actor, clock):
        self.Actor = Actor
        self.clock = clock
        self.q = qipan()
        pass
    def up(self):
        for i in range(self.q.size):
            for j in range(1, self.q.size):
                pass
    def down(self):
        pass
    def left(self):
        pass
    def right(self):
        pass
    def fapai(self):
        card = Card(self.Actor, self.clock)
        card.moveto()
