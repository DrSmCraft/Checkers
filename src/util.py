# """
# Name: objects.py
# Author: Sam O
# Date: 3/19/18
#
# Info:
#
#
#
#
# """
#
#
# # Imports
import pygame
import constants
#
#

#
#

#
#



class Board():
    def __init__(self, surface, grid_dim, light_color=constants.LIGHT_COLOR, dark_color=constants.DARK_COLOR):
        self.surface = surface
        self.light_color = light_color
        self.dark_color = dark_color
        self.grid_dim = grid_dim
        self.matrix = []
        self.reset()



    def reset(self):
        self.matrix = []
        self.create_matrix()

    def create_matrix(self):
        col = self.light_color
        for y in range(0, self.grid_dim[0]+1):
            lst = []
            for x in range(0, self.grid_dim[1]+1):
                if col == self.light_color:
                    lst.append(Square(self.surface, (y, x), col, dark=False))
                    col = self.dark_color
                elif col == self.dark_color:
                    lst.append(Square(self.surface, (y, x), color=col, dark=True))
                    col = self.light_color
            self.matrix.append(lst)
    def get_square(self, coord):
        return self.matrix[coord[0]][coord[1]]

    # return the square at raw screen coords
    def get_square_raw_coord(self, coord):
        return self.get_square((coord[0]//(constants.WINDOW_DIM[0]//self.grid_dim[0]), coord[1]//(constants.WINDOW_DIM[1]//self.grid_dim[1])))

    def __repr__(self):
        return str(self.matrix)

    def draw(self):
        for row in self.matrix:
            for entry in row:
                entry.draw()


class Player():
    def __init__(self, surface, color, board, positions):
        self.surface = surface
        self.color = color
        self.board = board
        self.positions = positions
        self.game_pieces = [[None for row in range(self.board.grid_dim[0])] for col in range(self.board.grid_dim[1])]
        self.reset()

    def reset(self):
        for row in self.positions:
            for pos in row:
                #square = self.board.get_square(pos)
                self.add_checker(pos)
        # for row in rows:
            # for col in range(10):
                # square = self.board.get_square((row, col))
                # if square.get_dark():
                    # self.add_checker((row-1, col-1))
                # if square.get_dark():
                #     check = Checker(self.surface, self, self.color, square)
                #     square.clear_cargo()
                #     square.set_cargo(check)
                #     self.game_pieces.append(check)

        # for row in [4]:
        #     for col in range(10 + 1):
        #         square = self.board.get_square((row, col))
        #         square.clear_cargo()

    def draw(self):
        #print(self.game_pieces)
        for obj in self.game_pieces:
            obj.draw()

    def add_checker(self, position):
        self.game_pieces[position[0]][position[1]] = Checker(self.surface, self, self.color, self.board.get_square(position))












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


class Square():
    def __init__(self, surface, position, color, dark=False, cargo=None):
        self.surface = surface
        self.position = position
        self.coord = (self.position[0] * constants.SQUARE_SIZE,
                     self.position[1] * constants.SQUARE_SIZE)
        self.color = color
        self.dark = dark
        self.cargo = cargo

    def get_position(self):
        return self.position

    def get_cargo(self):
        return self.cargo

    def set_cargo(self, new_cargo):
        self.cargo = new_cargo
        self.cargo.set_square(self)

    def clear_cargo(self):
        self.cargo = None

    def set_dark(self, is_dark):
        self.dark = is_dark

    def get_dark(self):
        return self.dark

    def get_bounds(self):
        return (self.position[0] * constants.SQUARE_SIZE,
                self.position[1] * constants.SQUARE_SIZE,
                constants.SQUARE_SIZE,
                constants.SQUARE_SIZE)

    def draw(self):
        rect = self.get_bounds()
        pygame.draw.rect(self.surface, self.color, rect)
        try:
            self.cargo.draw()
        except:
            #print(self.cargo)
            pass

    def get_info(self):
        return {"surface": self.surface,
                "position": self.position,
                "color": self.color,
                "dark": self.dark,
                "cargo": self.cargo}

    def __str__(self):
        return "Square at position " + str(self.position) + " of color " + str(self.color) + " containing " + str(self.cargo)

    def __repr__(self):
        return self.__str__()

class Checker():
    def __init__(self, surface, player, color, square, size=constants.CHECKER_SIZE):
        self.surface = surface
        self.player = player
        self.color = color
        self.square = square
        self.square.set_cargo(self)
        self.size = size

    def get_player(self):
        return self.player

    def set_player(self, new_player):
        self.player = new_player

    def get_color(self):
        return self.color

    def set_color(self, new_color):
        self.color = new_color

    def get_square(self):
        return self.square

    def set_square(self, new_square):
        self.square = new_square

    def draw(self):
        coordy = ((self.square.position[0] + 1) * constants.SQUARE_SIZE) - (constants.SQUARE_SIZE // 2)
        coordx = ((self.square.position[1] + 1) * constants.SQUARE_SIZE) - (constants.SQUARE_SIZE // 2)
        pygame.draw.circle(self.surface, self.color, (int(coordy), int(coordx)), self.size)

    def __str__(self):
        return "Checker of " + str(self.color) + " at " + str(self.square.get_position())