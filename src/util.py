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

    # Draw the Square
    def draw(self):
        rect = self.get_bounds()
        pygame.draw.rect(self.surface, self.color, rect)

    # return true if square is a dark square ---> if checker pieces can move onto it
    def is_dark(self):
        return self.dark

    # Return whatever is in the square
    def contains_obj(self):
        return self.contains()

    # Put an object into square
    def put_obj(self, obj):
        self.contains = obj

    def get_bounds(self):
        return (self.coord[0] * constants.SQUARE_SIZE,
                self.coord[1] * constants.SQUARE_SIZE,
                constants.SQUARE_SIZE,
                constants.SQUARE_SIZE)


# Checker Class
class Checker():
    def __init__(self, player=None, color=constants.PLAYER_1_COLOR, coord=(1, 1), size=constants.CHECKER_SIZE, surface=None):
        self.player = player
        self.color = color
        self.surface = surface
        self.coord = coord
        self.size = size

    # Draw the checker piece
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

    # Draw all the checkers that player has
    def draw(self):
        for x in self.checkers:
            x.draw()

    # Reset Board to starting position ---> called when player is created
    def reset(self):
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

    # Draw the Board
    def draw(self):
        for y in self.grid:
            for x in y:
                x.draw()

    # return the square at coord
    def get_square(self, coord):
        return self.grid[coord[0]][coord[1]]

    # return the square at raw screen coords
    def get_square_raw_coord(self, coord):
        return self.get_square((coord[0]//(constants.WINDOW_DIM[0]//self.grid_dim[0]), coord[1]//(constants.WINDOW_DIM[1]//self.grid_dim[1])))

    # Reset the board
    def reset(self):
        self.player1.reset()
        self.player2.reset()

    # creates a 2-dim list of squares ---> called when Board is created
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

# Selector class
# Used for Selecting Game Pieces
class Selector():
    def __init__(self, loc_color=constants.LOCATION_COLOR, des_color=constants.DESTINATION_COLOR, loc=None, des=None, surface=None):
        self.loc_color = loc_color
        self.loc = loc

        self.des_color = des_color
        self.des = des

        self.visible = False
        self.surface = surface
        self.thickness = 6

    def is_visible(self):
        return self.visible

    def set_visible(self, arg):
        self.visible = arg

    def draw(self):
        if self.visible:
            # Draw loc selector
            pygame.draw.rect(self.surface, self.loc_color, self.loc.get_bounds(), self.thickness)
            # Draw dest selector
            pygame.draw.rect(self.surface, self.des_color, self.des.get_bounds(), self.thickness)

    def get_des(self):
        return self.des

    def get_loc(self):
        return self.loc

    def set_des(self, obj):
        self.des = obj

    def set_loc(self, obj):
        self.loc = obj