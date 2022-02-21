import pygame

class Actor:
    def __init__(self, img_path, shape, space):
        self.img = pygame.image.load(img_path).convert_alpha()
        self.shape = shape
        self.alive = True
        self.space = space
        self.body=self.shape.body
    def draw(self,screen):
        if self.alive:
            pos = list(self.shape.body.position)
            pos[0] -= int(self.img.get_width()/2)
            pos[1] -= int(self.img.get_height()/2)
            screen.blit(self.img, pos)
    def update(self, event):
        print(event)

    def kill(self):
        self.alive=False
        self.space.remove(self.shape.body, self.shape)

    def position(self):
        return self.shape.body.position
