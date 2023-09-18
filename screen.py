import pygame
import consts

def create_screen():
    pygame.init()
    size = (consts.BOARD_GRID_ROWS, consts.BOARD_GRID_COLS)
    screen = pygame.display.set_mode(size)
    while True:
        screen.fill(consts.FIELD_COLOR)
        pygame.display.flip()


