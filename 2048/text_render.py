import pygame, sys

screen = pygame.display.set_mode((1920, 1080), pygame.RESIZABLE)
while True:
    # 事件检测、处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0,230,230))
    # 绘制屏幕

    font = pygame.font.SysFont(None, 24)
    # img = font.render('hello', True, (255, 221, 85))
    # screen.blit(img, (20, 20))
    # 更新绘制到屏幕上
    pygame.display.update()
