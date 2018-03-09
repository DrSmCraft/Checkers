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
    def __init__(self, coord=(0, 0), color=constants.LIGHT_COLOR, surface=None):
        self.coord = coord
        self.color = color
        self.surface = surface

    def draw(self):
        rect = (self.coord[0] * constants.SQUARE_SIZE,
                self.coord[1] * constants.SQUARE_SIZE,
                constants.SQUARE_SIZE,
                constants.SQUARE_SIZE)
        pygame.draw.rect(self.surface, self.color, rect)


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
        pygame.draw.circle(self.surface, self.color, (coordx, coordy), self.size)

# Payer Class
class Player():
    def __init__(self, color=constants.PLAYER_1_COLOR):
        self.color = color
        self.checkers = []
        # TODO place all checker pieces down in correct order
        for x in range(constants.GRID_DIM[0]):
            #self.checkers.append(Checker(color=self.color, coord=))
            pass

# Board Class
class Board():
    def __init__(self, light_color=constants.LIGHT_COLOR, dark_color=constants.DARK_COLOR, surface=None, grid_dim=constants.GRID_DIM):
        self.light_color = light_color
        self.dark_color = dark_color
        self.surface = surface
        self.grid_dim = grid_dim
        self.grid = []

        col = self.light_color
        for y in range(0, grid_dim[0]+1):
            lst = []
            for x in range(0, grid_dim[1]+1):
                lst.append(Square(coord=(y,x), surface=self.surface, color=col))
                if col == self.light_color:
                    col = self.dark_color
                elif col == self.dark_color:
                    col = self.light_color
            self.grid.append(lst)

    def draw(self):
        for y in self.grid:
            for x in y:
                x.draw()








