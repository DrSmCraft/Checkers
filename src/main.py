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

# Initializing
pygame.init()


# Setting up Game Window
window = pygame.display.set_mode(constants.WINDOW_DIM)
pygame.display.set_caption(constants.WINDOW_NAME)
run = True
pause = False


# Setting up Game Board
board = util.Board(light_color=constants.LIGHT_COLOR, dark_color=constants.DARK_COLOR, surface=window, grid_dim=constants.GRID_DIM)
player1 = util.Player(color=constants.PLAYER_1_COLOR, board=board, start=(0,0))
player1.draw()

player2 = util.Player(color=constants.PLAYER_2_COLOR, board=board, start=(0, 6))
player2.draw()

# Main Game Loop
while run:
    # If not paused, draw all objects
    if not pause:
        board.draw()
        player1.draw()
        player2.draw()

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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 1 = LeftClick, 3 = RightClick
            if event.button  == 1:
                pass
            elif event.button == 3:
                pass