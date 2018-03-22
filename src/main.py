"""
Name: main.py
Author: Sam O
Date: 3/19/18

Info:




"""


# Imports
import pygame
import constants
import util



"""
Name:
Author:
Date:

Info:




"""


# Imports
import constants
import util
import pygame
import game_logic

def wait_for_input():
    right_click_coord = (0, 0)
    left_click_coord = (0, 0)
    select.set_visible(True)

    while run:
        select.loc = board.get_square_raw_coord([left_click_coord[0], left_click_coord[1]])
        select.des = board.get_square_raw_coord([right_click_coord[0], right_click_coord[1]])
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
            # 1 = LeftClick, 3 = RightClick
                if event.button == 1:
                    #print("left")
                    left_click_coord = pygame.mouse.get_pos()

                elif event.button == 3:
                    #print("right")
                    right_click_coord = pygame.mouse.get_pos()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_INSERT:
                    logic.move(select.des, select.loc)


        draw(board, select)





def debug_squares():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 1 = LeftClick, 3 = RightClick
                if event.button == 1:
                    left_click_coord = pygame.mouse.get_pos()
                    sq = board.get_square_raw_coord(left_click_coord)
                    #print(left_click_coord, board.get_square_raw_coord(left_click_coord).position)
                    print(sq, sq.cargo)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    board.reset()

                #elif event.key == pygame.K_BACKSPACE:
                    #board.player1.reset()
        try:
            draw(select, board)
        except AttributeError:
            pass

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
player1 = util.Player(window, constants.PLAYER_1_COLOR, board, constants.PLAYER_1_CHECKER_POSITIONS)
player2 = util.Player(window, constants.PLAYER_2_COLOR, board, constants.PLAYER_2_CHECKER_POSITIONS)
select = util.Selector(surface=window, des_color=constants.DESTINATION_COLOR, loc_color=constants.LOCATION_COLOR)
logic = game_logic.GameLogic()


print(player1.game_pieces)
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
        debug_squares()
        #wait_for_input()


