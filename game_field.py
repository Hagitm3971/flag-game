# מודול לניהול לוח המשחק.
# מודול זה יחזיק מטריצה שתייצג את לוח המשחק בעזרת סימונים למשבצת ריקה, דגל,
# ומוקשים.
# בנוסף, הוא יכיל את מתודה ליצירת המוקשים במיקום אקראי, ויצירת הדגל, ומתודות נוספות
# הקשורות במוקשים ודגל.
import pygame
import consts


screen = pygame.display.set_mode((consts.BOARD_GRID_ROWS, consts.BOARD_GRID_COLS))
pygame.display.set_caption("Pixel to Square")
pygame.display.flip()

