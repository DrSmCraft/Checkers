"""
Name: constants.py
Author: Sam O
Date:3/19/28

Info:
This is where game constants and settings are defined.



"""


# Window Settings
WINDOW_NAME = "Play Checkers!" # "Play Checkers!"
WINDOW_DIM = (500, 500) # (1000, 1000)

# Board Settings
LIGHT_COLOR = (255, 255, 255)  # (255, 255, 255)
DARK_COLOR = (0, 0, 0)  # (0, 0, 0)
GRID_DIM = (10, 10)  # (10, 10)
SQUARE_SIZE = WINDOW_DIM[0]//GRID_DIM[0]  # 100

# Player Settings
PLAYER_1_COLOR = (200, 0, 0)  # (200, 200, 200)
PLAYER_2_COLOR = (0, 0, 200)  # (100, 100, 100)
PLAYER_1_CHECKER_POSITIONS = [[(0, 1), (0, 3), (0, 5), (0, 7), (0, 9)],
                              [(1, 0), (1, 2), (1, 4), (1, 6), (1, 8)],
                              [(2, 1), (2, 3), (2, 5), (2, 7), (2, 9)],
                              [(3, 0), (3, 2), (3, 4), (3, 6), (3, 8)]]

PLAYER_2_CHECKER_POSITIONS = [[(9, 0), (9, 2), (9, 4), (9, 6), (9, 8)],
                              [(8, 1), (8, 3), (8, 5), (8, 7), (8, 9)],
                              [(7, 0), (7, 2), (7, 4), (7, 6), (7, 8)],
                              [(6, 1), (6, 3), (6, 5), (6, 7), (6, 9)]]

# Checker Settings
CHECKER_SIZE = SQUARE_SIZE // 2  # 50

# Selector color
LOCATION_COLOR = (0, 100, 0)  # (0, 100, 0)
DESTINATION_COLOR = (0, 200, 0)  # (0, 200, 0)
