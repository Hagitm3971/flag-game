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
    block_size = 20
    for x in range(0, consts.WINDOW_WIDTH, block_size):
        for y in range(0, consts.WINDOW_LENGTH, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(screen.scrn, consts.WHITE, rect, 1)
    pygame.display.flip()

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
