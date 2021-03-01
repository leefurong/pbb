import pygame
pygame.init()
pygame.mixer.init()
firstSound = pygame.mixer.music('sounds/ha.wav')
secondSound = pygame.mixer.music('sounds/hzy.wav')
firstSound.play()
secondSound.play()
