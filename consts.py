import pygame

MESSAGE = "Welcome to The Flag game. \n Have Fun!"
WIN_MSG = ""
LOSE_MSG = ""

GRID_SIZE = 20
BOARD_GRID_ROWS = 50 * GRID_SIZE
BOARD_GRID_COLS = 25 * GRID_SIZE

PLAYER_WIDTH = 2
PLAYER_LENGTH = 4
FLAG_WIDTH = 4
FLAG_LENGTH = 3
MINE_WIDTH = 3
MINE_LENGTH = 1

PLAYER_LOCATION = [0, 0]
FLAG_LOCATION = ((BOARD_GRID_ROWS - FLAG_WIDTH), (BOARD_GRID_COLS - FLAG_LENGTH))

PLAYER_IMG = pygame.image.load("bin/soldier.png")
MINE_IMG = pygame.image.load("bin/mine.png")
GRASS_IMG = pygame.image.load("bin/grass.png")
FLAG_IMG = pygame.image.load("bin/flag.png")

PLAYER_IMG = pygame.transform.scale(PLAYER_IMG, (PLAYER_WIDTH, PLAYER_LENGTH))

FIELD_COLOR = (46, 139, 87)
