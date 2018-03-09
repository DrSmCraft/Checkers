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


# Main Game Loop
while run:
    # If not paused, draw all objects
    if not pause:
        board.draw()

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
            if event.button  == 4:
                print(4)
            elif event.button == 5:
                print(5)