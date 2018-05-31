"""
Name: main.py
Author: Sam O
Date: 3/19/18

Info:
This is the main driver file. It brings everything together.
"""


# Imports
import constants
import util
import pygame
import game_logic


# Function that waits for a player to move
# It also make sure move is valid using the GameLogic class
def wait_for_input():
    print("Current Turn: " + str(logic.get_current_turn().get_name()))
    acceptable = False
    select.set_visible(False)
    right_click_coord = (0, 0)
    left_click_coord = (0, 0)

    while not acceptable:
        select.loc = board.get_square_raw_coord([left_click_coord[0], left_click_coord[1]])
        select.des = board.get_square_raw_coord([right_click_coord[0], right_click_coord[1]])

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
            # 1 = LeftClick, 3 = RightClick
                if event.button == 1:
                    #print("left")
                    left_click_coord = pygame.mouse.get_pos()
                    select.set_visible(True)

                elif event.button == 3:
                    #print("right")
                    right_click_coord = pygame.mouse.get_pos()
                    select.set_visible(True)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    select.set_visible(True)
                    move_valid = logic.check_player_move_valid(select.get_loc(), select.get_des())
                    if move_valid:
                        logic.move(select.get_loc(), select.get_des())
                    acceptable = move_valid
        draw(board, select)

    logic.switch_turn()


# Function for debugging
def debug_squares():
    pygame.display.set_caption(constants.WINDOW_NAME + ": Debug")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 1 = LeftClick, 3 = RightClick
                if event.button == 1:
                    left_click_coord = pygame.mouse.get_pos()
                    sq = board.get_square_raw_coord(left_click_coord)
                    try:
                        sq.get_cargo().stack()
                    except:
                        pass
                    print(sq.get_cargo())
            # elif event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_SPACE:
            #         board.reset()


        draw(board)


# function to draw given arguments
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

instructions = ["Hello, Lets play Checkers!",
                "1 - Left Click on game piece that you want to move.",
                "2 - Then Right click on square you want to move.",
                "3 - Then press Enter on keyboard. That's it!", "FYI: Red goes first",
                "",
                "",
                "",
                "",
                "...Press any key to Play..."]

info_font = pygame.font.SysFont('Arial', 25)
y = 50
for string in instructions:
    window.blit(info_font.render(string, True, constants.INSTRUCTION_TEXT_COLOR), (20, y))
    y += 30
pygame.display.flip()

instructions_read = False

while not instructions_read:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            instructions_read = True

# Setting up Game Board
board = util.Board(light_color=constants.LIGHT_COLOR, dark_color=constants.DARK_COLOR, surface=window, grid_dim=constants.GRID_DIM)
player1 = util.Player(window, constants.PLAYER_1_COLOR, board, constants.PLAYER_1_CHECKER_POSITIONS, name="Player Red")
player2 = util.Player(window, constants.PLAYER_2_COLOR, board, constants.PLAYER_2_CHECKER_POSITIONS, name="Player Blue")
select = util.Selector(surface=window, des_color=constants.DESTINATION_COLOR, loc_color=constants.LOCATION_COLOR)
logic = game_logic.GameLogic(player1=player1, player2=player2, board=board)


# Main Game Loop
while run:
    # If not paused, draw all board and selector
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
        #debug_squares()
        wait_for_input()


