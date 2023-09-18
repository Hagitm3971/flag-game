import pygame
import consts
import random

def create_screen():
    #screen
    pygame.init()
    size = (consts.BOARD_GRID_ROWS, consts.BOARD_GRID_COLS)
    screen = pygame.display.set_mode(size)
    screen.fill(consts.FIELD_COLOR)
    pygame.display.update()

    #grass
    grass = pygame.image.load('grass.png')
    resized_grass_image = pygame.transform.scale(grass, (45, 30))
    for i in range(20):
        x = random.randint(0, 900)
        y = random.randint(0, 450)
        screen.blit(resized_grass_image, (x, y))

    #flag
    flag = pygame.image.load('flag.png')
    resized_flag_image = pygame.transform.scale(flag, (60, 50))
    screen.blit(resized_flag_image, (940,447))

    soldier = pygame.image.load('soldier.png')
    resized_soldier_image = pygame.transform.scale(soldier, (75, 68))
    screen.blit(resized_soldier_image, (0, 5))

    pygame.display.update()

    status = True
    while (status):
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                status = False
    pygame.quit()