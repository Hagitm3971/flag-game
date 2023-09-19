import pygame
import consts
import random

scrn = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_LENGTH))


def draw_screen():
    scrn.fill(consts.FIELD_COLOR)
    for i in range(20):
        x = random.randint(0, consts.WINDOW_WIDTH)
        y = random.randint(0, consts.WINDOW_LENGTH)
        scrn.blit(consts.GRASS_IMG, (x, y))
    scrn.blit(consts.FLAG_IMG,
                     (consts.NEW_FLAG_WIDTH * consts.GRID_SIZE, consts.NEW_FLAG_LENGTH * consts.GRID_SIZE))
    pygame.display.update()
