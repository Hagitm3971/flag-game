import pygame
import consts


def create_screen():
    pygame.init()
    size = (consts.BOARD_GRID_ROWS, consts.BOARD_GRID_COLS)
    screen = pygame.display.set_mode(size)
    screen.fill(consts.FIELD_COLOR)
    pygame.display.flip()


create_screen()
status = True
while (status):

    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for i in pygame.event.get():

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if i.type == pygame.QUIT:
            status = False

# deactivates the pygame library
pygame.quit()