from actor import Actor

class Sea(Actor):
    def __init__(self, ai):
        super().__init__(ai, ["sea.png"])
        self.rect.bottom = ai.screen.get_rect().bottom