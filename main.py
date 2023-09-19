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
    solider = soldier.draw_solider(gamefield)
    game_field.draw_flag(gamefield)
    handle_user_events()

    # while state["is_window_open"]:


def handle_user_events():
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_field.draw_grid()

                elif event.key == pygame.K_ESCAPE:
                    running = False

                elif event.key == pygame.K_LEFT:
                    soldier.move_left()

                elif event.key == pygame.K_RIGHT:
                    soldier.move_right()

                elif event.key == pygame.K_UP:
                    soldier.move_up()

                elif event.key == pygame.K_DOWN:
                    soldier.move_down()


if __name__ == '__main__':
    main()