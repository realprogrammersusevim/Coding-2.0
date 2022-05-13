from time import sleep
import variables


# This function will be called at the end of every move to display the current
# status of the board.
def show_board():
    "Displays the board in a human-friendly format"
    print('  1   2   3')
    print(f'1 {variables.one_one} | {variables.two_one} | {variables.three_one}')
    print('  --+---+--')
    print(f'2 {variables.one_two} | {variables.two_two} | {variables.three_two}')
    print('  --+---+--')
    print(
        f'3 {variables.one_three} | {variables.two_three} | {variables.three_three}')

def ask_for_move():
    """
    Asks for where the player would like to go and changes the correct variable
    """

    variables.player_move_x = input(
        "Where would you like to go on the x axis? ")

    # Checks if the player gave the correct input
    variables.player_move_y = input(
        "Where would you like to go on the y axis? ")

    # TODO Check if the space is already occupied before declaring it a valid
    # move.
    variables.player_move = (variables.player_move_x +
                             ', ' + variables.player_move_y)

    match variables.player_move:
        case '1, 1':
            variables.one_one = 'o'
        case '2, 1':
            variables.two_one = 'o'
        case '3, 1':
            variables.three_one = 'o'
        case '1, 2':
            variables.one_two = 'o'
        case '2, 2':
            variables.two_two = 'o'
        case '3, 2':
            variables.three_two = 'o'
        case '1, 3':
            variables.one_three = 'o'
        case '2, 3':
            variables.two_three = 'o'
        case '3, 3':
            variables.three_three = 'o'

    sleep(0.2)
    show_board()


# TODO: Change the board to a matrix for better computer manipulation. Then I
# just need a good function to translate the matrix into a GUI and back again.


def computer_move(x_axis, y_axis):
    "Edits the np matrix board"
    variables.board[y_axis, x_axis] = 1
    show_board()


def computer_wins():
    show_board()
    print('The computer wins. Humanity is doomed.')
    # Eventually I'll start storing the win-tie record.


def tie():
    show_board()
    print('You tied up the game. Good job not-loser.')


# First int is x value second is y
computer_move(1, 1)
show_board()


ask_for_move()
match variables.player_move:
    case '2, 1':
        variables.two_two = 'x'
        print("2, 2")
        show_board()
        ask_for_move()

        match variables.player_move:
            case '3, 1' | '1, 2' | '3, 2' | '1, 3' | '2, 3':
                variables.three_three = 'x'
                print('3, 3')
                computer_wins()
            case '3,3':
                variables.one_three = 'x'
                print('1, 3')
                show_board()
                ask_for_move()

                match variables.player_move:
                    case '3, 1' | '3, 2' | '2, 3':
                        variables.one_two = 'x'
                        print('1, 2')
                        computer_wins()

                    case '1, 2':
                        variables.three_one = 'x'
                        print('3, 1')
                        computer_wins()
    case '3, 1':
        variables.one_three = 'x'
        print("1, 3")
        show_board()
        ask_for_move()

        match variables.player_move:
            case '2, 1' | '2, 2' | '3, 2' | '2, 3' | '3, 3':
                variables.one_two = 'x'
                print('1, 2')
                computer_wins()
            case '1, 2':
                variables.three_three = 'x'
                print('3, 3')
                show_board()
                ask_for_move()

                match variables.player_move:
                    case '2, 1' | '2, 2' | '3, 2':
                        variables.two_three = 'x'
                        print('2, 3')
                        computer_wins()
                    case '2, 3':
                        variables.two_two = 'x'
                        print('2, 2')
                        computer_wins()
    case '1, 2':
        variables.two_two = 'x'
        print("2, 2")
        show_board()
        ask_for_move()

        match variables.player_move:
            case '2, 1' | '3, 1' | '3, 2' | '1, 3' | '2, 3':
                variables.three_three = 'x'
                print('3, 3')
                computer_wins()

            case '3, 3':
                variables.three_one = 'x'
                print('3, 1')
                show_board()
                ask_for_move()

                match variables.player_move:
                    case '3, 2' | '1, 3' | '2, 3':
                        variables.two_one = 'x'
                        print('2, 1')
                        computer_wins()
                    case '2, 1':
                        variables.one_three = 'x'
                        print('1, 3')
                        computer_wins()
    case '2, 2':
        variables.three_three = 'x'
        print("3, 3")
        show_board()
        ask_for_move()

        match variables.player_move:
            case '2, 1':
                variables.two_three = 'x'
                print('2, 3')
                show_board()
                ask_for_move()

                match variables.player_move:
                    case '3, 1' | '1, 2' | '3, 2':
                        variables.two_three = 'x'
                        print('2, 3')
                        computer_wins()
                    case '1, 3':
                        variables.three_one = 'x'
                        print('3, 1')
                        show_board()
                        ask_for_move()

                        match variables.player_move:
                            case '1, 2':
                                variables.one_two = 'x'
                                print('1, 2')
                                computer_wins()
                            case '3, 2':
                                variables.one_two = 'x'
                                print('1, 2')
                                tie()
            case '3, 1':
                variables.one_three = 'x'
                print('1, 3')
                show_board()
                ask_for_move()

                match variables.player_move:
                    case '2, 3':
                        variables.one_two = 'x'
                        print('1, 2')
                        computer_wins()
                    case '1, 2' | '3, 2':
                        variables.two_three = 'x'
                        print('2, 3')
                        computer_wins()
            case '1, 2':
                variables.three_two = 'x'
                print('3, 2')
                show_board()
                ask_for_move()

                match variables.player_move:
                    case '2, 1' | '1, 3' | '2, 3':
                        variables.three_two = 'x'
                        print('3, 2')
                        computer_wins()
                    case '3, 1':
                        variables.one_three = 'x'
                        print('1, 3')
                        show_board()
                        ask_for_move()

                        match variables.player_move:
                            case '2, 1':
                                variables.two_three = 'x'
                                print('2, 3')
                                computer_wins()
                            case '2, 3':
                                variables.two_one = 'x'
                                print('2, 1')
                                tie()
            case '3, 2':
                variables.one_two = 'x'
                print('1, 2')
                show_board()
                ask_for_move()

                match variables.player_move:
                    case '2, 1' | '3, 1' | '2, 3':
                        variables.one_three = 'x'
                        print('1, 3')
                        computer_wins()
                    case '1, 3':
                        variables.three_one = 'x'
                        print('3, 1')
                        show_board()
                        ask_for_move()

                        match variables.player_move:
                            case '2, 1':
                                variables.two_three = 'x'
                                print('2, 3')
                                computer_wins()
                            case '2, 3':
                                variables.two_one = 'x'
                                print('2, 1')
                                computer_wins()
            case '1, 3':
                variables.three_one = 'x'
                print('3, 1')
                show_board()
                ask_for_move()

                match variables.player_move:
                    case '2, 1' | '2, 3':
                        variables.three_two = 'x'
                        print('3, 2')
                        computer_wins()
                    case '1, 2' | '2, 3' | '3, 2':
                        variables.two_one = 'x'
                        print('2, 1')
                        computer_wins()
            case '2, 3':
                variables.two_one = 'x'
                print('2, 1')
                show_board()
                ask_for_move()

                match variables.player_move:
                    case '1, 2' | '3, 2' | '1, 3':
                        variables.three_one = 'x'
                        print('3, 1')
                        computer_wins()
                    case '3, 1':
                        variables.one_three = 'x'
                        print('1, 3')
                        show_board()
                        ask_for_move()

                        match variables.player_move:
                            case '1, 2':
                                variables.three_two = 'x'
                                print('3, 2')
                                computer_wins()
                            case '3, 2':
                                variables.one_two = 'x'
                                print('1, 2')
                                tie()
    case '3,2':
        variables.two_two = 'x'
        print('2, 2')
        show_board()
        ask_for_move()

        match variables.player_move:
            case '2, 1' | '3, 1' | '1, 2' | '1, 3' | '2, 3':
                variables.three_three = 'x'
                print('3, 3')
                computer_wins()
            case '3, 3':
                variables.three_one = 'x'
                print('3, 1')
                show_board()
                ask_for_move()

                match variables.player_move:
                    case '1, 2' | '1, 3' | '2, 3':
                        variables.two_one = 'x'
                        print('2, 1')
                        computer_wins()
                    case '2, 1':
                        variables.one_three = 'x'
                        print('1, 3')
                        computer_wins()
    case '1, 3':
        variables.three_one = 'x'
        print('3, 1')
        show_board()
        ask_for_move()

        match variables.player_move:
            case '1, 2' | '2, 2' | '3, 2' | '2, 3' | '3, 3':
                variables.two_one = 'x'
                print('2, 1')
                computer_wins()
            case '2, 1':
                variables.three_three = 'x'
                print('3, 3')
                show_board()
                ask_for_move()

                match variables.player_move:
                    case '1, 2' | '2, 2' | '2, 3':
                        variables.three_two = 'x'
                        print('3, 2')
                        computer_wins()
                    case '3, 2':
                        variables.two_two = 'x'
                        print('2, 2')
                        computer_wins()
    case '2, 3':
        variables.two_two = 'x'
        print('2, 2')
        show_board()
        ask_for_move()

        match variables.player_move:
            case '2, 1' | '3, 1' | '1, 2' '3, 2' | '1, 3':
                variables.three_three = 'x'
                print('3, 3')
                computer_wins()
            case '3, 3':
                variables.one_three = 'x'
                print('1, 3')
                show_board()
                ask_for_move()

                match variables.player_move:
                    case '2, 1' | '3, 1':
                        variables.one_two = 'x'
                        print('1, 2')
                        computer_wins()
                    case '1, 2' | '3, 2':
                        variables.three_two = 'x'
                        print('3, 2')
                        computer_wins()
    case '3, 3':
        variables.three_one = 'x'
        print('3, 1')
        show_board()
        ask_for_move()

        match variables.player_move:
            case '1, 2' | '2, 2' | '3, 2' | '1, 3' | '2, 3':
                variables.two_one = 'x'
                print('2, 1')
                computer_wins()
            case '2, 1':
                variables.one_three = 'x'
                print('1, 3')
                show_board()
                ask_for_move()

                match variables.player_move:
                    case '2, 2' | '3, 2' | '2, 3':
                        variables.one_two = 'x'
                        print('1, 2')
                        computer_wins()
                    case '1, 2':
                        variables.two_two = 'x'
                        print('2, 2')
                        computer_wins()
