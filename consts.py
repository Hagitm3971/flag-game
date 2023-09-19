import pygame

MESSAGE = "Welcome to The Flag game. Have Fun!"
WIN_MSG = ""
LOSE_MSG = ""

FLAG = 1
MINE = 2
SOLIDER = 3

GRID_SIZE = 20
BOARD_GRID_ROWS = 50
BOARD_GRID_COLS = 25
WINDOW_WIDTH = BOARD_GRID_ROWS * GRID_SIZE  # 1000
WINDOW_LENGTH = BOARD_GRID_COLS * GRID_SIZE  # 500

PLAYER_WIDTH = 2 * GRID_SIZE  # 40
PLAYER_LENGTH = 4 * GRID_SIZE  # 80
FLAG_WIDTH = 4
FLAG_LENGTH = 3
MINE_WIDTH = 3 * GRID_SIZE  # 60
MINE_LENGTH = 1 * GRID_SIZE  # 20

NEW_FLAG_WIDTH = (BOARD_GRID_ROWS - FLAG_WIDTH)  # 46
NEW_FLAG_LENGTH = (BOARD_GRID_COLS - FLAG_LENGTH)  # 22

PLAYER_IMG = pygame.image.load("bin/soldier.png")
MINE_IMG = pygame.image.load("bin/mine.png")
GRASS_IMG = pygame.image.load("bin/grass.png")
FLAG_IMG = pygame.image.load("bin/flag.png")

MINE_IMG = pygame.transform.scale(MINE_IMG, (MINE_WIDTH, MINE_LENGTH))
FLAG_IMG = pygame.transform.scale(FLAG_IMG, (FLAG_WIDTH * GRID_SIZE, FLAG_LENGTH * GRID_SIZE))
GRASS_IMG = pygame.transform.scale(GRASS_IMG, (50, 50))
PLAYER_IMG = pygame.transform.scale(PLAYER_IMG, (PLAYER_WIDTH, PLAYER_LENGTH))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
FIELD_COLOR = (46, 139, 87)

RUNNING_STATE = 1
LOSE_STATE = 2
WIN_STATE = 3
