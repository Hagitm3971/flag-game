import pygame

MESSAGE = "Welcome to The Flag game. \n Have Fun!"
WIN_MSG = ""
LOSE_MSG = ""

BOARD_WIDTH = 25
BOARD_LENGTH = 50
PLAYER_WIDTH = 2
PLAYER_LENGTH = 4
FLAG_WIDTH = 4
FLAG_LENGTH = 3
MINE_WIDTH = 3
MINE_LENGTH = 1

PLAYER_LOCATION = [0, 0]
FLAG_LOCATION = ((BOARD_WIDTH - FLAG_WIDTH), (BOARD_LENGTH - FLAG_LENGTH))

PLAYER_IMG = pygame.image.load("bin/soldier.png")
MINE_IMG = pygame.image.load("bin/mine.png")
GRASS_IMG = pygame.image.load("bin/grass.png")
FLAG_IMG = pygame.image.load("bin/flag.png")

FIELD_COLOR = (46, 139, 87)
