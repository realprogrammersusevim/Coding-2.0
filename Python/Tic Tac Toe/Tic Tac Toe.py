import variables

# This function will be called at the end of every move to display the current status of the board.


def show_board():
    print('  1   2   3')
    print('1 ' + variables.one_one + ' | ' +
          variables.two_one + ' | ' + variables.three_one)
    print('  --+---+--')
    print('2 ' + variables.one_two + ' | ' +
          variables.two_two + ' | ' + variables.three_two)
    print('  --+---+--')
    print('3 ' + variables.one_three + ' | ' +
          variables.two_three + ' | ' + variables.three_three)

# The point of this variable is to get where the player would like to go, and then change the correct variable.


def ask_for_move():
    variables.player_move_x = input(
        "Where would you like to go on the x axis? ")

    # Checks if the player gave the correct input
    # while config.player_move_x != '1' or '2' or '3':
    # config.player_move_x = input("Where would you like to go on the x axis? ")

    variables.player_move_y = input(
        "Where would you like to go on the y axis? ")
    # while config.player_move_y != '1' or '2' or '3':
    # config.player_move_y = input("Where would you like to go on the y axis? ")

    # TODO Check if the space is already occupied before declaring it a valid move.
    variables.player_move = (variables.player_move_x +
                             ', ' + variables.player_move_y)

    if variables.player_move == '1, 1':
        variables.one_one = 'o'
    elif variables.player_move == ' 2, 1':
        variables.two_one = 'o'
    elif variables.player_move == '3, 1':
        variables.three_one = 'o'
    elif variables.player_move == '1, 2':
        variables.one_two = 'o'
    elif variables.player_move == '2, 2':
        variables.two_two = 'o'
    elif variables.player_move == '3, 2':
        variables.three_two = 'o'
    elif variables.player_move == '1, 3':
        variables.one_three = 'o'
    elif variables.player_move == '2, 3':
        variables.two_three = 'o'
    elif variables.player_move == '3, 3':
        variables.three_three = 'o'

    show_board()


def computer_wins():
    show_board()
    print('The computer wins. Humanity is doomed.')
    # Eventually I'll start storing the win-tie record.


def tie():
    show_board()
    print('You tied up the game. Good job not-loser.')


# First int is x value second is y
print("1, 1")
show_board()


ask_for_move()
if variables.player_move == '2, 1':
    variables.two_two = 'x'
    print("2, 2")
    show_board()
    ask_for_move()

    if variables.player_move == '3, 1' or variables.player_move == '1, 2' or variables.player_move == '3, 2' or variables.player_move == '1, 3' or variables.player_move == '2, 3':
        variables.three_three = 'x'
        print('3, 3')
        computer_wins()
    elif variables.player_move == '3, 3':
        variables.one_three = 'x'
        print('1, 3')
        show_board()
        ask_for_move()

        if variables.player_move == '3, 1' or variables.player_move == '3, 2' or variables.player_move == '2, 3':
            variables.one_two = 'x'
            print('1, 2')
            computer_wins()
        elif variables.player_move == '1, 2':
            variables.three_one = 'x'
            print('3, 1')
            computer_wins()
elif variables.player_move == '3, 1':
    variables.one_three = 'x'
    print("1, 3")
    show_board()
    ask_for_move()

    if variables.player_move == '2, 1' or variables.player_move == '2, 2' or variables.player_move == '3, 2' or variables.player_move == '2, 3' or variables.player_move == '3, 3':
        variables.one_two = 'x'
        print('1, 2')
        computer_wins()

    elif variables.player_move == '1, 2':
        variables.three_three = 'x'
        print('3, 3')
        show_board()
        ask_for_move()

        if variables.player_move == '2, 1' or variables.player_move == '2, 2' or variables.player_move == '3, 2':
            variables.two_three = 'x'
            print('2, 3')
            computer_wins()

        elif variables.player_move == '2, 3':
            variables.two_two = 'x'
            print('2, 2')
            computer_wins()
elif variables.player_move == '1, 2':
    variables.two_two = 'x'
    print("2, 2")
    show_board()
    ask_for_move()

    if variables.player_move == '2, 1' or variables.player_move == '3, 1' or variables.player_move == '3, 2' or variables.player_move == '1, 3' or variables.player_move == '2, 3':
        variables.three_three = 'x'
        print('3, 3')
        computer_wins()

    elif variables.player_move == '3, 3':
        variables.three_one = 'x'
        print('3, 1')
        show_board()
        ask_for_move()

        if variables.player_move == '3, 2' or variables.player_move == '1, 3' or variables.player_move == '2, 3':
            variables.two_one = 'x'
            print('2, 1')
            computer_wins()

        elif variables.player_move == '2, 1':
            variables.one_three = 'x'
            print('1, 3')
            computer_wins()
elif variables.player_move == '2, 2':
    variables.three_three = 'x'
    print("3, 3")
    show_board()
    ask_for_move()

    if variables.player_move == '2, 1':
        variables.two_three = 'x'
        print('2, 3')
        show_board()
        ask_for_move()

        if variables.player_move == '3, 1' or variables.player_move == '1, 2' or variables.player_move == '3, 2':
            variables.two_three = 'x'
            print('2, 3')
            computer_wins()
        elif variables.player_move == '1, 3':
            variables.three_one = 'x'
            print('3, 1')
            show_board()
            ask_for_move()

            if variables.player_move == '1, 2':
                variables.three_two = 'x'
                print('1, 2')
                computer_wins()
            elif variables.player_move == '3, 2':
                variables.one_two = 'x'
                print('1, 2')
                tie()
    elif variables.player_move == '3, 1':
        variables.one_three = 'x'
        print('1, 3')
        show_board()
        ask_for_move()

        if variables.player_move == '2, 1' or variables.player_move == '2, 3':
            variables.one_two = 'x'
            print('1, 2')
            computer_wins()
        elif variables.player_move == '1, 2' or variables.player_move == '3, 2':
            variables.two_three = 'x'
            print('2, 3')
            computer_wins()
    elif variables.player_move == '1, 2':
        variables.three_two = 'x'
        print('3, 2')
        show_board()
        ask_for_move()

        if variables.player_move == '2, 1' or variables.player_move == '1, 3' or variables.player_move == '2, 3':
            variables.three_two = 'x'
            print('3, 2')
            computer_wins()
        elif variables.player_move == '3, 1':
            variables.one_three = 'x'
            print('1, 3')
            show_board()
            ask_for_move()

            if variables.player_move == '2, 1':
                variables.two_three = 'x'
                print('2, 3')
                computer_wins()
            elif variables.player_move == '2, 3':
                variables.one_one = 'x'
                print('2, 1')
                tie()
    elif variables.player_move == '3, 2':
        variables.one_two = 'x'
        print('1, 2')
        show_board()
        ask_for_move()

        if variables.player_move == '2, 1' or variables.player_move == '3, 1' or variables.player_move == '2, 3':
            variables.one_three = 'x'
            print('1, 3')
            computer_wins()
        elif variables.player_move == '1, 3':
            variables.three_one = 'x'
            print('3, 1')
            show_board()
            ask_for_move()

            if variables.player_move == '2, 1':
                variables.two_three = 'x'
                print('2, 3')
                computer_wins()
            elif variables.player_move == '2, 3':
                variables.two_one = 'x'
                print('2, 1')
                computer_wins()
    elif variables.player_move == '1, 3':
        variables.three_one = 'x'
        print('3, 1')
        show_board()
        ask_for_move()

        if variables.player_move == '2, 1' or variables.player_move == '2, 3':
            variables.three_two = 'x'
            print('3, 2')
            computer_wins()
        elif variables.player_move == '1, 2' or variables.player_move == '2, 3':
            variables.two_one = 'x'
            print('2, 1')
            computer_wins()
    elif variables.player_move == '2, 3':
        variables.two_one = 'x'
        print('2, 1')
        show_board()
        ask_for_move()

        if variables.player_move == '1, 2' or variables.player_move == '3, 2' or variables.player_move == '1, 3':
            variables.three_one = 'x'
            print('3, 1')
            computer_wins()
        elif variables.player_move == '3, 1':
            variables.one_three = 'x'
            print('1, 3')
            show_board()
            ask_for_move()

            if variables.player_move == '1, 2':
                variables.three_two = 'x'
                print('3, 2')
                computer_wins()
            elif variables.player_move == '3, 2':
                variables.one_two = 'x'
                print('1, 2')
                tie()
elif variables.player_move == '3, 2':
    variables.two_two = 'x'
    print('2, 2')
    show_board()
    ask_for_move()

    if variables.player_move == '2, 1' or variables.player_move == '3, 1' or variables.player_move == '1, 2' or variables.player_move == '1, 3' or variables.player_move == '2, 3':
        variables.three_three = 'x'
        print('3, 3')
        computer_wins()
    elif variables.player_move == '3, 3':
        variables.three_one = 'x'
        print('3, 1')
        show_board()
        ask_for_move()

        if variables.player_move == '1, 2' or variables.player_move == '1, 3' or variables.player_move == '2, 3':
            variables.two_one = 'x'
            print('2, 1')
            computer_wins()
        elif variables.player_move == '2, 1':
            variables.one_three = 'x'
            print('1, 3')
            computer_wins()
elif variables.player_move == '1, 3':
    variables.three_one = 'x'
    print('3, 1')
    show_board()
    ask_for_move()

    if variables.player_move == '1, 2' or variables.player_move == '2, 2' or variables.player_move == '3, 2' or variables.player_move == '2, 3' or variables.player_move == '3, 3':
        variables.two_one = 'x'
        print('2,1')
        computer_wins()
    elif variables.player_move == '2, 1':
        variables.three_three = 'x'
        print('3, 3')
        show_board()
        ask_for_move()

        if variables.player_move == '1, 2' or variables.player_move == '2, 2' or variables.player_move == '2, 3':
            variables.three_two = 'x'
            print('3, 2')
            computer_wins()
        elif variables.player_move == '3, 2':
            variables.two_two = 'x'
            print('2, 2')
            computer_wins()
elif variables.player_move == '2, 3':
    variables.two_two = 'x'
    print('2, 2')
    show_board()
    ask_for_move()

    if variables.player_move == '2, 1' or variables.player_move == '3, 1' or variables.player_move == '1, 2' or variables.player_move == '3, 2' or variables.player_move == '1, 3':
        variables.three_three = 'x'
        print('3, 3')
        computer_wins()
    elif variables.player_move == '3, 3':
        variables.one_three = 'x'
        print('1, 3')
        show_board()
        ask_for_move()

        if variables.player_move == '2, 1' or variables.player_move == '3, 1':
            variables.one_two = 'x'
            print('1, 2')
            computer_wins()
        elif variables.player_move == '1, 2' or variables.player_move == '3, 2':
            variables.three_two = 'x'
            print('3, 2')
            computer_wins()
elif variables.player_move == '3, 3':
    variables.three_one = 'x'
    print('3, 1')
    show_board()
    ask_for_move()

    if variables.player_move == '1, 2' or variables.player_move == '2, 2' or variables.player_move == '3, 2' or variables.player_move == '1, 3' or variables.player_move == '2, 3':
        variables.two_one = 'x'
        print('2, 1')
        computer_wins()
    elif variables.player_move == '2, 1':
        variables.one_three = 'x'
        print('1, 3')
        show_board()
        ask_for_move()

        if variables.player_move == '2, 2' or variables.player_move == '3, 2' or variables.player_move == '2, 3':
            variables.one_two = 'x'
            print('1, 2')
            computer_wins()
        elif variables.player_move == '1, 2':
            variables.two_two = 'x'
            print('2, 2')
            computer_wins()
