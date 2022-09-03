from time import sleep
import numpy as np
import variables as var
import logging


# This function will be called at the end of every move to display the current
# status of the board.
def show_board():
    "Displays the board in a human-friendly format"
    player_board = np.rot90(var.board, var.rotation)
    count = 0

    logging.debug("Showing the board")
    for row in player_board:
        for cell in row:
            match cell:
                case 2:
                    print("o", end="")
                case 1:
                    print("x", end="")
                case 0:
                    print(" ", end="")
            count += 1
            match count:
                case 3 | 6:
                    print("")
                    print("--+---+--")
                case 9:
                    print("\n")
                case _:
                    print(" | ", end="")


# 0 means the space is unoccupied, 1 that it is an X and 2 that it's an O
def ask_for_move():
    "Asks for where the player would like to go and changes the correct variable"

    logging.debug("Asking for move")
    # var.player_move_x = input("Where would you like to go on the x axis? ")

    # var.player_move_y = input("Where would you like to go on the y axis? ")

    # var.player_move = f"{var.player_move_x}, {var.player_move_y}"
    old_move = var.player_move
    while True:
        if old_move != var.player_move:
            break
        else:
            sleep(0.5)
    logging.debug("Got move, rotating it for computer")
    # Rotates the player's move to match the computer's perspective
    rotate_player_move = np.zeros((3, 3), dtype=int)
    rotate_player_move[int(var.player_move_y) - 1, int(var.player_move_x) - 1] = 1
    rotate_player_move = np.rot90(rotate_player_move, -(var.rotation))
    var.rotated_player_move = np.where(rotate_player_move == 1)
    np.concatenate(var.rotated_player_move).tolist()
    var.rotated_player_move = (
        f"{var.rotated_player_move[1] + 1}, {var.rotated_player_move[0] + 1}"
    )
    var.rotated_player_move = var.rotated_player_move.replace("[", "")
    var.rotated_player_move = var.rotated_player_move.replace("]", "")
    logging.debug(f"Finished move rotation, move is {var.rotated_player_move}")

    # This is the player board that is simply the real board that is rotated to
    # look different to the player
    logging.debug("Getting player board")
    player_board = np.rot90(var.board, var.rotation)

    # Checks that the player's move is valid before changing the board
    logging.debug("Checking if player move is valid")
    # if (
    #     player_board[int(var.player_move_y) - 1, int(var.player_move_x) - 1]
    #     != 0
    # ):
    #     print("That space is already occupied. Try again.")
    #     ask_for_move()

    # Remember that I use the Cartesian coordinate system (X then Y) while the
    # matrix uses Y first and X second
    logging.debug("Editing player board")
    player_board[int(var.player_move_y) - 1, int(var.player_move_x) - 1] = 2

    # show_board()

    # This rotates the board back to what the computer sees after the player
    # has made their move
    rotate_back = 4 - var.rotation
    var.board = np.rot90(player_board, rotate_back)


def computer_move(x_axis, y_axis):
    "Edits the np matrix board"
    logging.debug("Computer editing board")
    # var.board[int(y_axis) - 1, int(x_axis) - 1] = 1
    # show_board()
    var.computer_move_x = x_axis
    var.computer_move_y = y_axis
    var.computer_has_moved = True


def computer_wins():
    "Called when the computer wins."
    show_board()
    print("The computer wins. Humanity is doomed.")
    # Eventually I'll start storing the win-tie record with Pickle.


def tie():
    "This function will be called when the board is full and no one has won."
    show_board()
    print("You tied up the game. Good job not-loser.")


# First int is x value second is y
computer_move(1, 1)
ask_for_move()
match var.rotated_player_move:
    case "2, 1":
        computer_move(2, 1)
        ask_for_move()

        match var.rotated_player_move:
            case "3, 1" | "1, 2" | "3, 2" | "1, 3" | "2, 3":
                computer_move(3, 3)
                computer_wins()
            case "3, 3":
                computer_move(1, 3)
                ask_for_move()

                match var.rotated_player_move:
                    case "3, 1" | "3, 2" | "2, 3":
                        computer_move(1, 2)
                        computer_wins()
                    case "1, 2":
                        computer_move(3, 1)
                        computer_wins()
                    case _:
                        print("No match")
            case _:
                print("No match")
    case "3, 1":
        computer_move(1, 3)
        ask_for_move()

        match var.rotated_player_move:
            case "2, 1" | "2, 2" | "3, 2" | "2, 3" | "3, 3":
                computer_move(1, 2)
                computer_wins()
            case "1, 2":
                computer_move(3, 3)
                ask_for_move()

                match var.rotated_player_move:
                    case "2, 1" | "2, 2" | "3, 2":
                        computer_move(2, 3)
                        computer_wins()
                    case "2, 3":
                        computer_move(2, 2)
                        computer_wins()
                    case _:
                        print("No match")
            case _:
                print("No match")
    case "1, 2":
        computer_move(2, 2)
        ask_for_move()

        match var.rotated_player_move:
            case "2, 1" | "3, 1" | "3, 2" | "1, 3" | "2, 3":
                computer_move(3, 3)
                computer_wins()

            case "3, 3":
                computer_move(3, 1)
                ask_for_move()

                match var.rotated_player_move:
                    case "3, 2" | "1, 3" | "2, 3":
                        computer_move(2, 1)
                        computer_wins()
                    case "2, 1":
                        computer_move(1, 3)
                        computer_wins()
                    case _:
                        print("No match")
            case _:
                print("No match")
    case "2, 2":
        computer_move(3, 3)
        ask_for_move()

        match var.rotated_player_move:
            case "2, 1":
                computer_move(2, 3)
                ask_for_move()

                match var.rotated_player_move:
                    case "3, 1" | "1, 2" | "3, 2":
                        computer_move(2, 3)
                        computer_wins()
                    case "1, 3":
                        computer_move(3, 1)
                        ask_for_move()

                        match var.rotated_player_move:
                            case "1, 2":
                                computer_move(1, 2)
                                computer_wins()
                            case "3, 2":
                                computer_move(1, 2)
                                tie()
                            case _:
                                print("No match")
                    case _:
                        print("No match")
            case "3, 1":
                computer_move(1, 3)
                ask_for_move()

                match var.rotated_player_move:
                    case "2, 3":
                        computer_move(1, 2)
                        computer_wins()
                    case "1, 2" | "3, 2":
                        computer_move(2, 3)
                        computer_wins()
                    case _:
                        print("No match")
            case "1, 2":
                computer_move(3, 2)
                ask_for_move()

                match var.rotated_player_move:
                    case "2, 1" | "1, 3" | "2, 3":
                        computer_move(3, 1)
                        computer_wins()
                    case "3, 1":
                        computer_move(1, 3)
                        ask_for_move()

                        match var.rotated_player_move:
                            case "2, 1":
                                computer_move(2, 3)
                                computer_wins()
                            case "2, 3":
                                computer_move(2, 1)
                                tie()
                            case _:
                                print("No match")
                    case _:
                        print("No match")
            case "3, 2":
                computer_move(1, 2)
                ask_for_move()

                match var.rotated_player_move:
                    case "2, 1" | "3, 1" | "2, 3":
                        computer_move(1, 3)
                        computer_wins()
                    case "1, 3":
                        computer_move(3, 1)
                        ask_for_move()

                        match var.rotated_player_move:
                            case "2, 1":
                                computer_move(2, 3)
                                computer_wins()
                            case "2, 3":
                                computer_move(2, 1)
                                computer_wins()
                            case _:
                                print("No match")
                    case _:
                        print("No match")
            case "1, 3":
                computer_move(3, 1)
                ask_for_move()

                match var.rotated_player_move:
                    case "2, 1" | "2, 3":
                        computer_move(3, 2)
                        computer_wins()
                    case "1, 2" | "2, 3" | "3, 2":
                        computer_move(2, 1)
                        computer_wins()
                    case _:
                        print("No match")
            case "2, 3":
                computer_move(2, 1)
                ask_for_move()

                match var.rotated_player_move:
                    case "1, 2" | "3, 2" | "1, 3":
                        computer_move(3, 1)
                        computer_wins()
                    case "3, 1":
                        computer_move(1, 3)
                        ask_for_move()

                        match var.rotated_player_move:
                            case "1, 2":
                                computer_move(3, 2)
                                computer_wins()
                            case "3, 2":
                                computer_move(1, 2)
                                tie()
                            case _:
                                print("No match")
                    case _:
                        print("No match")
            case _:
                print("No match")
    case "3,2":
        computer_move(2, 2)
        ask_for_move()

        match var.rotated_player_move:
            case "2, 1" | "3, 1" | "1, 2" | "1, 3" | "2, 3":
                computer_move(3, 3)
                computer_wins()
            case "3, 3":
                computer_move(3, 1)
                ask_for_move()

                match var.rotated_player_move:
                    case "1, 2" | "1, 3" | "2, 3":
                        computer_move(2, 1)
                        computer_wins()
                    case "2, 1":
                        computer_move(1, 3)
                        computer_wins()
                    case _:
                        print("No match")
            case _:
                print("No match")
    case "1, 3":
        computer_move(3, 1)
        ask_for_move()

        match var.rotated_player_move:
            case "1, 2" | "2, 2" | "3, 2" | "2, 3" | "3, 3":
                computer_move(2, 1)
                computer_wins()
            case "2, 1":
                computer_move(3, 3)
                ask_for_move()

                match var.rotated_player_move:
                    case "1, 2" | "2, 2" | "2, 3":
                        computer_move(3, 2)
                        computer_wins()
                    case "3, 2":
                        computer_move(2, 2)
                        computer_wins()
                    case _:
                        print("No match")
            case _:
                print("No match")
    case "2, 3":
        computer_move(2, 2)
        ask_for_move()

        match var.rotated_player_move:
            case "2, 1" | "3, 1" | "1, 2" "3, 2" | "1, 3":
                computer_move(3, 3)
                computer_wins()
            case "3, 3":
                computer_move(1, 3)
                ask_for_move()

                match var.rotated_player_move:
                    case "2, 1" | "3, 1":
                        computer_move(1, 2)
                        computer_wins()
                    case "1, 2" | "3, 2":
                        computer_move(3, 2)
                        computer_wins()
                    case _:
                        print("No match")
            case _:
                print("No match")
    case "3, 3":
        computer_move(3, 1)
        ask_for_move()

        match var.rotated_player_move:
            case "1, 2" | "2, 2" | "3, 2" | "1, 3" | "2, 3":
                computer_move(2, 1)
                computer_wins()
            case "2, 1":
                computer_move(1, 3)
                ask_for_move()

                match var.rotated_player_move:
                    case "2, 2" | "3, 2" | "2, 3":
                        computer_move(1, 2)
                        computer_wins()
                    case "1, 2":
                        computer_move(2, 2)
                        computer_wins()
                    case _:
                        print("No match")
            case _:
                print("No match")
    case _:
        print("No match")
