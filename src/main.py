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


def wait_for_input():
    while run:
        for event in pygame.event:
            if event.type == pygame.MOUSEBUTTONDOWN:
            # 1 = LeftClick, 3 = RightClick
                if event.button == 1:
                    left_click_coord = pygame.mouse.get_pos()
                    select.des = board.get_square_raw_coord((0, 0))
                    select.loc = board.get_square_raw_coord(left_click_coord)

                elif event.button == 3:
                    right_click_coord = pygame.mouse.get_pos()
                    select.loc = board.get_square_raw_coord((0, 0))
                    select.des = board.get_square_raw_coord(right_click_coord)
                select.set_visible(True)


def debug_squares():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 1 = LeftClick, 3 = RightClick
                if event.button == 1:
                    left_click_coord = pygame.mouse.get_pos()
                    print(board.get_square_raw_coord(left_click_coord))
        try:
            draw(board, select)
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
player1 = util.Player(color=constants.PLAYER_1_COLOR, board=board, start=(0,0))
player2 = util.Player(color=constants.PLAYER_2_COLOR, board=board, start=(0, 6))
select = util.Selector(surface=window, des_color=constants.DESTINATION_COLOR, loc_color=constants.LOCATION_COLOR)



# Main Game Loop
while run:
    # If not paused, draw all objects
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
