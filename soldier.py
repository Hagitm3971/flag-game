import pygame
import consts
import screen
import game_field


def draw_solider(gamefield):
    soldier = {"x_val": 0, "y_val": 0}
    screen.scrn.blit(consts.PLAYER_IMG, (0, 0))
    gamefield[0][0] = consts.SOLIDER
    pygame.display.update()
    return soldier


def move_left(scrn, solider):
    solider["x_val"] += 1 * consts.GRID_SIZE
    scrn.blit(consts.PLAYER_IMG, (solider["x_val"] * consts.GRID_SIZE, solider["y_val"] * consts.GRID_SIZE))


def move_right(scrn, solider):
    solider["x_val"] -= 1 * consts.GRID_SIZE
    scrn.blit(consts.PLAYER_IMG, (solider["x_val"] * consts.GRID_SIZE, solider["y_val"] * consts.GRID_SIZE))


def move_up(scrn, solider):
    solider["y_val"] -= 1 * consts.GRID_SIZE
    scrn.blit(consts.PLAYER_IMG, (solider["x_val"] * consts.GRID_SIZE, solider["y_val"] * consts.GRID_SIZE))


def move_down(scrn, solider):
    solider["y_val"] += 1 * consts.GRID_SIZE
    scrn.blit(consts.PLAYER_IMG, (solider["x_val"] * consts.GRID_SIZE, solider["y_val"] * consts.GRID_SIZE))

