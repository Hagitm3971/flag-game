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


def move_left(solider):
    solider["x_val"] -= 1 * consts.GRID_SIZE
    screen.scrn.blit(consts.PLAYER_IMG, (solider["x_val"], solider["y_val"]))


def move_right(solider):
    solider["x_val"] += 1 * consts.GRID_SIZE
    screen.scrn.blit(consts.PLAYER_IMG, (solider["x_val"], solider["y_val"]))


def move_up(solider):
    solider["y_val"] -= 1 * consts.GRID_SIZE
    screen.scrn.blit(consts.PLAYER_IMG, (solider["x_val"], solider["y_val"]))


def move_down(solider):
    solider["y_val"] += 1 * consts.GRID_SIZE
    screen.scrn.blit(consts.PLAYER_IMG, (solider["x_val"], solider["y_val"]))

