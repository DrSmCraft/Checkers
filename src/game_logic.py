"""
Name: game_logic.py
Author: Sam O
Date: March 12, 2018

Info:
This is the file that defines gamerules and checks whether actions done by players are acceptable.

"""


# Imports
import util
import constants
import pygame


# This is the class for Game Logic and Gamerules
class GameLogic():
    def __init__(self, board=None, player1=None, player2=None):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.players = [player1, player2]
        self.turn = 0

    # See if move is valid
    def check_player_move_valid(self, loc_square, des_square):
        loc_acceptable = False
        des_acceptable = False

        # Check if loc_square is valid
        if self.check_player_ownership(loc_square):
            loc_acceptable = True

        # Check if des square is valid
        if des_square.get_dark():
            if self.check_move(loc_square, des_square):
                if des_square.get_cargo() is not None:
                    if self.check_player_ownership(des_square):
                        des_acceptable = False
                    elif self.check_other_player_ownership(des_square):
                        des_acceptable = True
                else:
                    des_acceptable = True

        return des_acceptable and loc_acceptable

    # Check if player has ownership of square
    def check_player_ownership(self, item):
        if item.get_cargo() is None:
            return False
        elif type(item) is util.Square:
            for row in self.players[self.turn].get_game_pieces():
                if item.get_cargo() in row:
                    return True
        return False

    # Check if other player has ownership of square
    def check_other_player_ownership(self, item):
        if item.get_cargo() is None:
            return False
        elif type(item) is util.Square:
            for row in self.players[self.turn - 1].get_game_pieces():
                if item.get_cargo() in row:
                    return True
        return False

    # Check if move distance and direction is allowed
    def check_move(self, loc_square, des_square):
        distance_acceptable = False
        direction_acceptable = False
        loc_pos = loc_square.get_position()
        des_pos = des_square.get_position()

        if loc_pos[0] != des_pos[0] or loc_pos[1] != des_pos[1]:
            direction_acceptable = True
        if abs(des_pos[0] - loc_pos[0]) == 1 or abs(des_pos[1] - loc_pos[1]) == 1:
            distance_acceptable = True
        return distance_acceptable and direction_acceptable

    # return which player has current turn
    def get_current_turn(self):
        return self.players[self.turn]

    # Switch turn to other player
    def switch_turn(self):
        if self.turn == 0:
            self.turn = 1
        elif self.turn == 1:
            self.turn = 0

    def set_turn(self, id):
        self.turn = id

    # Move Game Piece from checker_square to target_square
    def move(self, checker_square, target_square):
        target_square.clear_cargo()
        target_square.set_cargo(checker_square.get_cargo())
        checker_square.clear_cargo()