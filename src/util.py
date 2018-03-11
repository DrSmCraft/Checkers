"""
Name:
Author:
Date:

Info:




"""


# Imports
import constants
import pygame




# Square Class
class Square():
    def __init__(self, coord=(0, 0), color=constants.LIGHT_COLOR, surface=None, dark=False, contains=None):
        self.coord = coord
        self.color = color
        self.surface = surface
        self.dark = dark
        self.contains = contains

    def draw(self):
        rect = (self.coord[0] * constants.SQUARE_SIZE,
                self.coord[1] * constants.SQUARE_SIZE,
                constants.SQUARE_SIZE,
                constants.SQUARE_SIZE)
        pygame.draw.rect(self.surface, self.color, rect)

    def is_dark(self):
        return self.dark


# Checker Class
class Checker():
    def __init__(self, player=None, color=constants.PLAYER_1_COLOR, coord=(1, 1), size=constants.CHECKER_SIZE, surface=None):
        self.player = player
        self.color = color
        self.surface = surface
        self.coord = coord
        self.size = size

    def draw(self):
        coordy = (self.coord[0] * constants.SQUARE_SIZE) - constants.SQUARE_SIZE / 2
        coordx = (self.coord[1] * constants.SQUARE_SIZE) - constants.SQUARE_SIZE / 2
        pygame.draw.circle(self.surface, self.color, (int(coordx), int(coordy)), self.size)

# Payer Class
class Player():
    def __init__(self, color=constants.PLAYER_1_COLOR, board=None, start=(0,0)):
        self.color = color
        self.checkers = []
        self.board = board
        self.start = start
        self.reset()


    def draw(self):
        for x in self.checkers:
            x.draw()

    def reset(self):
        # TODO place all checker pieces down in correct order
        self.checkers = []
        col = 0 + self.start[0]
        row = 0 + self.start[1]
        for num in range(4 * constants.GRID_DIM[0]):
            col += 1
            if num % constants.GRID_DIM[0] == 0:
                row += 1
                col = 1
            if self.board.get_square((row, col)).is_dark():
                self.checkers.append(Checker(surface=self.board.surface, color=self.color, coord=(row, col)))

# Board Class
class Board():
    def __init__(self, light_color=constants.LIGHT_COLOR, dark_color=constants.DARK_COLOR, surface=None, grid_dim=constants.GRID_DIM, player1=None, player2=None):
        self.light_color = light_color
        self.dark_color = dark_color
        self.surface = surface
        self.player1 = player1
        self.player2 = player2
        self.grid_dim = grid_dim
        self.grid = []

        self.create_grid()


    def draw(self):
        for y in self.grid:
            for x in y:
                x.draw()

    def get_square(self, coord):
        return self.grid[coord[0]][coord[1]]

    def reset(self):
        self.player1.reset()
        self.player2.reset()

    def create_grid(self):
        col = self.light_color
        for y in range(0, self.grid_dim[0]+1):
            lst = []
            for x in range(0, self.grid_dim[1]+1):
                if col == self.light_color:
                    lst.append(Square(coord=(y, x), surface=self.surface, color=col, dark=False))
                    col = self.dark_color
                elif col == self.dark_color:
                    lst.append(Square(coord=(y, x), surface=self.surface, color=col, dark=True))
                    col = self.light_color
            self.grid.append(lst)







