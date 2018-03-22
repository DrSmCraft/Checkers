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
        # Check if loc_square is empty
        if loc_square is not None:
            if loc_square.contains_obj() in self.players[self.turn].checkers:
                loc_acceptable = True
            else:
                loc_acceptable = False
        else:
            loc_acceptable = False
        print("Loc_Acc " + str(loc_acceptable))

        # Check if des square is acceptable
        if des_square.contains_obj() is not None:
            print(des_square.contains_obj())
            if des_square.contains_obj() in self.players[self.turn].checkers:
                des_acceptable = False
            elif des_square.contains_obj() in self.players[self.turn - 1].checkers:
                des_acceptable = True
        else:
            print("dez is empty")
            des_acceptable = True
        print("Des_Acc " + str(des_acceptable))

        return des_acceptable and loc_acceptable


    def check_player_ownership(self, item):
        if type(item) is util.Square:
            return item.contains_obj() in self.players[self.turn].checkers
        elif type(item) is util.Checker:
            return item in self.players[self.turn].checkers

    def get_current_turn(self):
        return self.players[self.turn]

    def switch_turn(self):
        if self.turn == 0:
            self.turn = 1
        elif self.turn == 1:
            self.turn = 0

    def set_turn(self, id):
        self.turn = id

    def move(self, checker_square, target_square):
        target_square.clear_cargo()

        target_square.set_cargo(checker_square.get_cargo())
        checker_square.clear_cargo()
        print(target_square)



def show_checks(surface, board):
    num = 0

    for y in board.grid:
        for x in y:
            if x.contains_obj() is not None:

                coord = (x.contains_obj().coord[0] * 100 + 50, x.contains_obj().coord[1] * 100 + 50)
                pygame.draw.circle(surface, (255, 0, 255), coord, 5)
                num += 1