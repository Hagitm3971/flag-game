import pygame
import consts
import screen
import soldier
import game_field


state = {
    "is_window_open": True,
    "state": consts.RUNNING_STATE,
}


def main():
    pygame.init()
    scrn = screen.draw_screen()
    gamefield = game_field.create_field_matrix()
    game_field.draw_flag(gamefield)
    solider = soldier.draw_solider(gamefield)
    handle_user_events(gamefield)

    # while state["is_window_open"]:


def handle_user_events(gamefield, scrn, solider):
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_field.draw_grid()
                    game_field.draw_mine(gamefield)

                elif event.key == pygame.K_ESCAPE:
                    running = False

                elif event.key == pygame.K_LEFT:
                    soldier.move_left(scrn, solider)

                elif event.key == pygame.K_RIGHT:
                    soldier.move_right(scrn, solider)

                elif event.key == pygame.K_UP:
                    soldier.move_up(scrn, solider)

                elif event.key == pygame.K_DOWN:
                    soldier.move_down(scrn, solider)


if __name__ == '__main__':
    main()