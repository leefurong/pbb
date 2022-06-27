"""Draw text to the screen."""
import pygame
from pygame.locals import *


RED = (255, 0, 0)


pygame.init()
screen = pygame.display.set_mode((640, 240))

sysfont = pygame.font.get_default_font()

font = pygame.font.SysFont(None, 48)
img = font.render(sysfont, True, RED)


# running = True
while True:
    # for event in pygame.event.get():
    #     if event.type == QUIT:
    #         running = False
    screen.blit(img, (20, 20))
    pygame.display.update()