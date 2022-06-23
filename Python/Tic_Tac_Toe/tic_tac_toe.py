from time import sleep

import numpy as np

import variables


# This function will be called at the end of every move to display the current
# status of the board.
def show_board():
    "Displays the board in a human-friendly format"
    player_board = np.rot90(variables.board, variables.rotation)
    count = 0

    for i in player_board:
        match variables.board.all():
            case 2:
                print('o', end=' ')
            case 1:
                print('x', end=' ')
            case 0:
                print('-', end=' ')
        count += 1
        if count == 3 or count == 6 or count == 9:
            print('\n')


# 0 means the space is unoccupied, 1 that it is an X and 2 that it's an O
def ask_for_move():
    """
    Asks for where the player would like to go and changes the correct variable
    """

    variables.player_move_x = input(
        "Where would you like to go on the x axis? ")

    variables.player_move_y = input(
        "Where would you like to go on the y axis? ")

    variables.player_move = (
        f'{variables.player_move_x}, {variables.player_move_y}')

    # This is the player board that is simply the real board that is rotated to
    # look different to the player
    player_board = np.rot90(variables.board, variables.rotation)

    # Checks that the player's move is valid before changing the board
    if player_board[int(variables.player_move_y), int(variables.player_move_x)] != 0:
        print('That space is already occupied. Try again.')
        ask_for_move()

    print(variables.player_move)

    # Remember that I use the Cartesian coordinate system (X then Y) while the
    # matrix uses Y first and X second
    player_board[int(variables.player_move_y),
                 int(variables.player_move_x)] = 2

    sleep(0.2)
    show_board()

    # This rotates the board back to what the computer sees after the player
    # has made their move
    rotate_back = 4 - variables.rotation
    variables.board = np.rot90(player_board, rotate_back)


# TODO: Change the board to a matrix for better computer manipulation. Then I
# just need a good function to translate the matrix into a GUI and back again.

def computer_move(x_axis, y_axis):
    "Edits the np matrix board"
    variables.board[int(y_axis), int(x_axis)] = 1
    print(f'{x_axis}, {y_axis}')
    show_board()


def computer_wins():
    show_board()
    print('The computer wins. Humanity is doomed.')
    # Eventually I'll start storing the win-tie record with Pickle.


def tie():
    show_board()
    print('You tied up the game. Good job not-loser.')


# First int is x value second is y
computer_move(1, 1)
show_board()


ask_for_move()
match variables.player_move:
    case '2, 1':
        computer_move(2, 1)
        ask_for_move()

        match variables.player_move:
            case '3, 1' | '1, 2' | '3, 2' | '1, 3' | '2, 3':
                computer_move(3, 3)
                computer_wins()
            case '3, 3':
                computer_move(1, 3)
                ask_for_move()

                match variables.player_move:
                    case '3, 1' | '3, 2' | '2, 3':
                        computer_move(1, 2)
                        computer_wins()
                    case '1, 2':
                        computer_move(3, 1)
                        computer_wins()
    case '3, 1':
        computer_move(1, 3)
        ask_for_move()

        match variables.player_move:
            case '2, 1' | '2, 2' | '3, 2' | '2, 3' | '3, 3':
                computer_move(1, 2)
                computer_wins()
            case '1, 2':
                computer_move(3, 3)
                ask_for_move()

                match variables.player_move:
                    case '2, 1' | '2, 2' | '3, 2':
                        computer_move(2, 3)
                        computer_wins()
                    case '2, 3':
                        computer_move(2, 2)
                        computer_wins()
    case '1, 2':
        computer_move(2, 2)
        ask_for_move()

        match variables.player_move:
            case '2, 1' | '3, 1' | '3, 2' | '1, 3' | '2, 3':
                computer_move(3, 3)
                computer_wins()

            case '3, 3':
                computer_move(3, 1)
                ask_for_move()

                match variables.player_move:
                    case '3, 2' | '1, 3' | '2, 3':
                        computer_move(2, 1)
                        computer_wins()
                    case '2, 1':
                        computer_move(1, 3)
                        computer_wins()
    case '2, 2':
        computer_move(3, 3)
        ask_for_move()

        match variables.player_move:
            case '2, 1':
                computer_move(2, 3)
                ask_for_move()

                match variables.player_move:
                    case '3, 1' | '1, 2' | '3, 2':
                        computer_move(2, 3)
                        computer_wins()
                    case '1, 3':
                        computer_move(3, 1)
                        ask_for_move()

                        match variables.player_move:
                            case '1, 2':
                                computer_move(1, 2)
                                computer_wins()
                            case '3, 2':
                                computer_move(1, 2)
                                tie()
            case '3, 1':
                computer_move(1, 3)
                ask_for_move()

                match variables.player_move:
                    case '2, 3':
                        computer_move(1, 2)
                        computer_wins()
                    case '1, 2' | '3, 2':
                        computer_move(2, 3)
                        computer_wins()
            case '1, 2':
                computer_move(3, 2)
                ask_for_move()

                match variables.player_move:
                    case '2, 1' | '1, 3' | '2, 3':
                        computer_move(3, 1)
                        computer_wins()
                    case '3, 1':
                        computer_move(1, 3)
                        ask_for_move()

                        match variables.player_move:
                            case '2, 1':
                                computer_move(2, 3)
                                computer_wins()
                            case '2, 3':
                                computer_move(2, 1)
                                tie()
            case '3, 2':
                computer_move(1, 2)
                ask_for_move()

                match variables.player_move:
                    case '2, 1' | '3, 1' | '2, 3':
                        computer_move(1, 3)
                        computer_wins()
                    case '1, 3':
                        computer_move(3, 1)
                        ask_for_move()

                        match variables.player_move:
                            case '2, 1':
                                computer_move(2, 3)
                                computer_wins()
                            case '2, 3':
                                computer_move(2, 1)
                                computer_wins()
            case '1, 3':
                computer_move(3, 1)
                ask_for_move()

                match variables.player_move:
                    case '2, 1' | '2, 3':
                        computer_move(3, 2)
                        computer_wins()
                    case '1, 2' | '2, 3' | '3, 2':
                        computer_move(2, 1)
                        computer_wins()
            case '2, 3':
                computer_move(2, 1)
                ask_for_move()

                match variables.player_move:
                    case '1, 2' | '3, 2' | '1, 3':
                        computer_move(3, 1)
                        computer_wins()
                    case '3, 1':
                        computer_move(1, 3)
                        ask_for_move()

                        match variables.player_move:
                            case '1, 2':
                                computer_move(3, 2)
                                computer_wins()
                            case '3, 2':
                                computer_move(1, 2)
                                tie()
    case '3,2':
        computer_move(2, 2)
        ask_for_move()

        match variables.player_move:
            case '2, 1' | '3, 1' | '1, 2' | '1, 3' | '2, 3':
                computer_move(3, 3)
                computer_wins()
            case '3, 3':
                computer_move(3, 1)
                ask_for_move()

                match variables.player_move:
                    case '1, 2' | '1, 3' | '2, 3':
                        computer_move(2, 1)
                        computer_wins()
                    case '2, 1':
                        computer_move(1, 3)
                        computer_wins()
    case '1, 3':
        computer_move(3, 1)
        ask_for_move()

        match variables.player_move:
            case '1, 2' | '2, 2' | '3, 2' | '2, 3' | '3, 3':
                computer_move(2, 1)
                computer_wins()
            case '2, 1':
                computer_move(3, 3)
                ask_for_move()

                match variables.player_move:
                    case '1, 2' | '2, 2' | '2, 3':
                        computer_move(3, 2)
                        computer_wins()
                    case '3, 2':
                        computer_move(2, 2)
                        computer_wins()
    case '2, 3':
        computer_move(2, 2)
        ask_for_move()

        match variables.player_move:
            case '2, 1' | '3, 1' | '1, 2' '3, 2' | '1, 3':
                computer_move(3, 3)
                computer_wins()
            case '3, 3':
                computer_move(1, 3)
                ask_for_move()

                match variables.player_move:
                    case '2, 1' | '3, 1':
                        computer_move(1, 2)
                        computer_wins()
                    case '1, 2' | '3, 2':
                        computer_move(3, 2)
                        computer_wins()
    case '3, 3':
        computer_move(3, 1)
        ask_for_move()

        match variables.player_move:
            case '1, 2' | '2, 2' | '3, 2' | '1, 3' | '2, 3':
                computer_move(2, 1)
                computer_wins()
            case '2, 1':
                computer_move(1, 3)
                ask_for_move()

                match variables.player_move:
                    case '2, 2' | '3, 2' | '2, 3':
                        computer_move(1, 2)
                        computer_wins()
                    case '1, 2':
                        computer_move(2, 2)
                        computer_wins()
