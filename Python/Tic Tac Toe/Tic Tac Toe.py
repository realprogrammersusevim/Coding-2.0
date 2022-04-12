import config

# This function will be called at the end of every move to display the current status of the board.


def show_board():
    print('  1   2   3')
    print('1 ' + config.one_one + ' | ' +
          config.two_one + ' | ' + config.three_one)
    print('  --+---+--')
    print('2 ' + config.one_two + ' | ' +
          config.two_two + ' | ' + config.three_two)
    print('  --+---+--')
    print('3 ' + config.one_three + ' | ' +
          config.two_three + ' | ' + config.three_three)

# The point of this variable is to get where the player would like to go, and then change the correct variable.


def ask_for_move():
    config.player_move_x = input("Where would you like to go on the x axis? ")

    # Checks if the player gave the correct input
    # while config.player_move_x != '1' or '2' or '3':
    # config.player_move_x = input("Where would you like to go on the x axis? ")

    config.player_move_y = input("Where would you like to go on the y axis? ")
    # while config.player_move_y != '1' or '2' or '3':
    # config.player_move_y = input("Where would you like to go on the y axis? ")

    # TODO Check if the space is already occupied before declaring it a valid move.
    config.player_move = (config.player_move_x + ', ' + config.player_move_y)

    if config.player_move == '1, 1':
        config.one_one = 'o'
    elif config.player_move == ' 2, 1':
        config.two_one = 'o'
    elif config.player_move == '3, 1':
        config.three_one = 'o'
    elif config.player_move == '1, 2':
        config.one_two = 'o'
    elif config.player_move == '2, 2':
        config.two_two = 'o'
    elif config.player_move == '3, 2':
        config.three_two = 'o'
    elif config.player_move == '1, 3':
        config.one_three = 'o'
    elif config.player_move == '2, 3':
        config.two_three = 'o'
    elif config.player_move == '3, 3':
        config.three_three = 'o'

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
if config.player_move == '2, 1':
    config.two_two = 'x'
    print("2, 2")
    show_board()
    ask_for_move()

    if config.player_move == '3, 1' or '1, 2' or '3, 2' or '1, 3' or '2, 3':
        config.three_three = 'x'
        print('3, 3')
        computer_wins()
    elif config.player_move == '3, 3':
        config.one_three = 'x'
        print('1, 3')
        show_board()
        ask_for_move()

        if config.player_move == '3, 1' or '3, 2' or '2, 3':
            config.one_two = 'x'
            print('1, 2')
            computer_wins()
        elif config.player_move == '1, 2':
            config.three_one = 'x'
            print('3, 1')
            computer_wins()
elif config.player_move == '3, 1':
    config.one_three = 'x'
    print("1, 3")
    show_board()
    ask_for_move()

    if config.player_move == '2, 1' or '2, 2' or '3, 2' or '2, 3' or '3, 3':
        config.one_two = 'x'
        print('1, 2')
        computer_wins()

    elif config.player_move == '1, 2':
        config.three_three = 'x'
        print('3, 3')
        show_board()
        ask_for_move()

        if config.player_move == '2, 1' or '2, 2' or '3, 2':
            config.two_three = 'x'
            print('2, 3')
            computer_wins()

        elif config.player_move == '2, 3':
            config.two_two = 'x'
            print('2, 2')
            computer_wins()
elif config.player_move == '1, 2':
    config.two_two = 'x'
    print("2, 2")
    show_board()
    ask_for_move()

    if config.player_move == '2, 1' or '3, 1' or '3, 2' or '1, 3' or '2, 3':
        config.three_three = 'x'
        print('3, 3')
        computer_wins()

    elif config.player_move == '3, 3':
        config.three_one = 'x'
        print('3, 1')
        show_board()
        ask_for_move()

        if config.player_move == '3, 2' or '1, 3' or '2, 3':
            config.two_one = 'x'
            print('2, 1')
            computer_wins()

        elif config.player_move == '2, 1':
            config.one_three = 'x'
            print('1, 3')
            computer_wins()
elif config.player_move == '2, 2':
    config.three_three = 'x'
    print("3, 3")
    show_board()
    ask_for_move()

    if config.player_move == '2, 1':
        config.two_three = 'x'
        print('2, 3')
        show_board()
        ask_for_move()

        if config.player_move == '3, 1' or '1, 2' or '3, 2':
            config.two_three = 'x'
            print('2, 3')
            computer_wins()
        elif config.player_move == '1, 3':
            config.three_one = 'x'
            print('3, 1')
            show_board()
            ask_for_move()

            if config.player_move == '1, 2':
                config.three_two = 'x'
                print('1, 2')
                computer_wins()
            elif config.player_move == '3, 2':
                config.one_two = 'x'
                print('1, 2')
                tie()
    elif config.player_move == '3, 1':
        config.one_three = 'x'
        print('1, 3')
        show_board()
        ask_for_move()

        if config.player_move == '2, 1' or '2, 3':
            config.one_two = 'x'
            print('1, 2')
            computer_wins()
        elif config.player_move == '1, 2' or '3, 2':
            config.two_three = 'x'
            print('2, 3')
            computer_wins()
    elif config.player_move == '1, 2':
        config.three_two = 'x'
        print('3, 2')
        show_board()
        ask_for_move()

        if config.player_move == '2, 1' or '1, 3' or '2, 3':
            config.three_two = 'x'
            print('3, 2')
            computer_wins()
        elif config.player_move == '3, 1':
            config.one_three
            print('1, 3')
            show_board()
            ask_for_move()

            if config.player_move == '2, 1':
                config.two_three = 'x'
                print('2, 3')
                computer_wins()
            elif config.player_move == '2, 3':
                config.one_one = 'x'
                print('2, 1')
                tie()
    elif config.player_move == '3, 2':
        config.one_two = 'x'
        print('1, 2')
        show_board()
        ask_for_move()

        if config.player_move == '2, 1' or '3, 1' or '2, 3':
            config.one_three = 'x'
            print('1, 3')
            computer_wins()
        elif config.player_move == '1, 3':
            config.three_one = 'x'
            print('3, 1')
            show_board()
            ask_for_move()

            if config.player_move == '2, 1':
                config.two_three = 'x'
                print('2, 3')
                computer_wins()
            elif config.player_move == '2, 3':
                config.two_one = 'x'
                print('2, 1')
                computer_wins()
    elif config.player_move == '1, 3':
        config.three_one = 'x'
        print('3, 1')
        show_board()
        ask_for_move()

        if config.player_move == '2, 1' or '2, 3':
            config.three_two = 'x'
            print('3, 2')
            computer_wins()
        elif config.player_move == '1, 2' or '2, 3':
            config.two_one = 'x'
            print('2, 1')
            computer_wins()
    elif config.player_move == '2, 3':
        config.one_one = 'x'
        print('2, 1')
        show_board()
        ask_for_move()

        if config.player_move == '1, 2' or '3, 2' or '1, 3':
            config.three_one = 'x'
            print('3, 1')
            computer_wins()
        elif config.player_move == '3, 1':
            config.one_three = 'x'
            print('1, 3')
            show_board()
            ask_for_move()

            if config.player_move == '1, 2':
                config.three_two = 'x'
                print('3, 2')
                computer_wins()
            elif config.player_move == '3, 2':
                config.one_two = 'x'
                print('1, 2')
                tie()
elif config.player_move == '3, 2':
    config.two_two = 'x'
    print('2, 2')
    show_board()
    ask_for_move()

    if config.player_move == '2, 1' or '3, 1' or '1, 2' or '1, 3' or '2, 3':
        config.three_three = 'x'
        print('3, 3')
        computer_wins()
    elif config.player_move == '3, 3':
        config.three_one = 'x'
        print('3, 1')
        show_board()
        ask_for_move()

        if config.player_move == '1, 2' or '1, 3' or '2, 3':
            config.two_one = 'x'
            print('2, 1')
            computer_wins()
        elif config.player_move == '2, 1':
            config.one_three = 'x'
            print('1, 3')
            computer_wins()
elif config.player_move == '1, 3':
    config.three_one = 'x'
    print('3, 1')
    show_board()
    ask_for_move()

    if config.player_move == '1, 2' or '2, 2' or '3, 2' or '2, 3' or '3, 3':
        config.two_one = 'x'
        print('2,1')
        computer_wins()
    elif config.player_move == '2, 1':
        config.three_three = 'x'
        print('3, 3')
        show_board()
        ask_for_move()

        if config.player_move == '1, 2' or '2, 2' or '2, 3':
            config.three_two = 'x'
            print('3, 2')
            computer_wins()
        elif config.player_move == '3, 2':
            config.two_two = 'x'
            print('2, 2')
            computer_wins()
elif config.player_move == '2, 3':
    config.two_two = 'x'
    print('2, 2')
    show_board()
    ask_for_move()

    if config.player_move == '2, 1' or '3, 1' or '1, 2' or '3, 2' or '1, 3':
        config.three_three = 'x'
        print('3, 3')
        computer_wins()
    elif config.player_move == '3, 3':
        config.one_three = 'x'
        print('1, 3')
        show_board()
        ask_for_move()

        if config.player_move == '2, 1' or '3, 1':
            config.one_two = 'x'
            print('1, 2')
            computer_wins()
        elif config.player_move == '1, 2' or '3, 2':
            config.three_two = 'x'
            print('3, 2')
            computer_wins()
elif config.player_move == '3, 3':
    config.three_one = 'x'
    print('3, 1')
    show_board()
    ask_for_move()

    if config.player_move == '1, 2' or '2, 2' or '3, 2' or '1, 3' or '2, 3':
        config.two_one = 'x'
        print('2, 1')
        computer_wins()
    elif config.player_move == '2, 1':
        config.one_three = 'x'
        print('1, 3')
        show_board()
        ask_for_move()

        if config.player_move == '2, 2' or '3, 2' or '2, 3':
            config.one_two = 'x'
            print('1, 2')
            computer_wins()
        elif config.player_move == '1, 2':
            config.two_two = 'x'
            print('2, 2')
            computer_wins()
