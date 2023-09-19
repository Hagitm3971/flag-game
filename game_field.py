import consts
import pygame
import screen


def create_field_matrix():
    game_matrix = []
    for row in range(consts.BOARD_GRID_ROWS):
        matrix_row = []
        for col in range(consts.BOARD_GRID_COLS):
            matrix_row.append(0)
        game_matrix.append(matrix_row)
    return game_matrix


def draw_grid():
    screen.scrn.fill(consts.BLACK)
    for x in range(consts.WINDOW_WIDTH):
        for y in range(consts.WINDOW_LENGTH):
            rect = pygame.Rect(x * consts.GRID_SIZE, y * consts.GRID_SIZE, consts.GRID_SIZE, consts.GRID_SIZE)
            pygame.draw.rect(screen.scrn, consts.GREEN, rect, 1)
    pygame.display.flip()


def draw_flag(gamefield):
    screen.scrn.blit(consts.FLAG_IMG,
                     (consts.NEW_FLAG_WIDTH, consts.NEW_FLAG_LENGTH))
    gamefield[consts.NEW_FLAG_WIDTH][consts.NEW_FLAG_LENGTH] = consts.FLAG
    pygame.display.update()

# def create_mine():
#     pass
#
#
# def create_flag(game_matrix):
#     for i in range(len(game_matrix)):
#         for j in range(len(game_matrix[i])):
#             if (i, j) == consts.FLAG_LOCATION:
#                 game_matrix[j] = consts.FLAG
#     return game_matrix
#
#
# create_flag(create_field_matrix())


# def draw_text(text, font, text_col, x, y):
#     img = font.render(text, True, text_col)
#     screen.blit(img, (x, y))
