"""
Name: main.py
Author: Sam O
Date: 3/19/18

Info:




"""


# Imports
import constants
import util
import pygame
import game_logic


def wait_for_input():
    print("Current Turn: " + str(logic.get_current_turn().get_name()))
    acceptable = False
    select.set_visible(False)
    right_click_coord = (0, 0)
    left_click_coord = (0, 0)

    while not acceptable:
        select.loc = board.get_square_raw_coord([left_click_coord[0], left_click_coord[1]])
        select.des = board.get_square_raw_coord([right_click_coord[0], right_click_coord[1]])

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
            # 1 = LeftClick, 3 = RightClick
                if event.button == 1:
                    #print("left")
                    left_click_coord = pygame.mouse.get_pos()
                    select.set_visible(True)

                elif event.button == 3:
                    #print("right")
                    right_click_coord = pygame.mouse.get_pos()
                    select.set_visible(True)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_INSERT:
                    select.set_visible(True)
                    move_valid = logic.check_player_move_valid(select.get_loc(), select.get_des())
                    if move_valid:
                        logic.move(select.get_loc(), select.get_des())
                    acceptable = move_valid
        draw(board, select)

    logic.switch_turn()








def debug_squares():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 1 = LeftClick, 3 = RightClick
                if event.button == 1:
                    left_click_coord = pygame.mouse.get_pos()
                    sq = board.get_square_raw_coord(left_click_coord)
                    #print(left_click_coord, board.get_square_raw_coord(left_click_coord).position)
                    print(sq)
                    print(logic.check_player_ownership(sq))

            # elif event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_SPACE:
            #         board.reset()


        draw(board)
def draw(*args):
    for obj in args:
        obj.draw()
    pygame.display.flip()

# Initializing
pygame.init()


# Setting up Game Window
window = pygame.display.set_mode(constants.WINDOW_DIM)
pygame.display.set_caption(constants.WINDOW_NAME)
run = True
pause = False
turn = True

# Setting up Game Board
board = util.Board(light_color=constants.LIGHT_COLOR, dark_color=constants.DARK_COLOR, surface=window, grid_dim=constants.GRID_DIM)
player1 = util.Player(window, constants.PLAYER_1_COLOR, board, constants.PLAYER_1_CHECKER_POSITIONS, name="Player Red")
player2 = util.Player(window, constants.PLAYER_2_COLOR, board, constants.PLAYER_2_CHECKER_POSITIONS, name="Player Blue")
select = util.Selector(surface=window, des_color=constants.DESTINATION_COLOR, loc_color=constants.LOCATION_COLOR)
logic = game_logic.GameLogic(player1=player1, player2=player2, board=board)


# Main Game Loop
while run:
    # If not paused, draw all util
    if not pause:
        draw(board, select)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pause:
                    pause = False
                elif not pause:
                    pause = True
            elif event.key == pygame.K_ESCAPE:
                run = False
        #debug_squares()
        wait_for_input()


