one_one = "x"
one_two = " "
one_three = " "
two_one = " "
two_two = " "
two_three = " "
three_one = " "
three_two = " "
three_three = " "

player_move = ''
# This function will be called at the end of every move to display the current status of the board.


def show_board():
    global one_one
    global two_one
    global three_one
    global one_two
    global two_two
    global two_three
    global one_three
    global two_three
    global three_three

    print('  1   2   3')
    print('1 ' + one_one + ' | ' + two_one + ' | ' + three_one)
    print('  --+---+--')
    print('2 ' + one_two + ' | ' + two_two + ' | ' + two_three)
    print('  --+---+--')
    print('3 ' + one_three + ' | ' + two_three + ' | ' + three_three)

# The point of this variable is to get where the player would like to go, and then change the correct variable.


def ask_for_move():
    global player_move_x
    player_move_x = input("Where would you like to go on the x axis? ")

    # Checks if the player gave the correct input
    # while player_move_x != '1' or '2' or '3':
    # player_move_x = input("Where would you like to go on the x axis? ")

    global player_move_y
    player_move_y = input("Where would you like to go on the y axis? ")
    # while player_move_y != '1' or '2' or '3':
    # player_move_y = input("Where would you like to go on the y axis? ")

    # TODO Check if the space is already occupied before declaring it a valid move.
    global player_move
    player_move = (player_move_x + ', ' + player_move_y)

    if player_move == '1, 1':
        global one_one
        one_one = 'o'
    elif player_move == ' 2, 1':
        global two_one
        two_one = 'o'
    elif player_move == '3, 1':
        global three_one
        three_one = 'o'
    elif player_move == '1, 2':
        global one_two
        one_two = 'o'
    elif player_move == '2, 2':
        global two_two
        two_two = 'o'
    elif player_move == '3, 2':
        global three_two
        three_two = 'o'
    elif player_move == '1, 3':
        global one_three
        one_three = 'o'
    elif player_move == '2, 3':
        global two_three
        two_three = 'o'
    elif player_move == '3, 3':
        global three_three
        three_three = 'o'

    show_board()


def computer_wins():
    print('The computer wins. Humanity is doomed.')
    # Eventually I'll start storing the win-tie record.


def tie():
    print('You tied up the game. Good job not-loser.')


# First int is x value second is y
print("1, 1")
show_board()


ask_for_move()
if player_move == '2, 1':
    two_two = 'x'
    print("2, 2")
    ask_for_move()

    if player_move == '3, 1' or '1, 2' or '3, 2' or '1, 3' or '2, 3':
        three_three = 'x'
        print('3, 3')
        computer_wins()
    elif player_move == '3, 3':
        one_three = 'x'
        print('1, 3')
        ask_for_move()

        if player_move == '3, 1' or '3, 2' or '2, 3':
            one_two = 'x'
            print('1, 2')
            computer_wins()
        elif player_move == '1, 2':
            three_one = 'x'
            print('3, 1')
            computer_wins()
elif player_move == '3, 1':
    one_three = 'x'
    print("1, 3")
    ask_for_move()

    if player_move == '2, 1' or '2, 2' or '3, 2' or '2, 3' or '3, 3':
        one_two = 'x'
        print('1, 2')
        computer_wins()

    elif player_move == '1, 2':
        three_three = 'x'
        print('3, 3')
        ask_for_move()

        if player_move == '2, 1' or '2, 2' or '3, 2':
            two_three = 'x'
            print('2, 3')
            computer_wins()

        elif player_move == '2, 3':
            two_two = 'x'
            print('2, 2')
            computer_wins()
elif player_move == '1, 2':
    two_two = 'x'
    print("2, 2")
    ask_for_move()

    if player_move == '2, 1' or '3, 1' or '3, 2' or '1, 3' or '2, 3':
        three_three = 'x'
        print('3, 3')
        computer_wins()

    elif player_move == '3, 3':
        three_one = 'x'
        print('3, 1')
        ask_for_move()

        if player_move == '3, 2' or '1, 3' or '2, 3':
            two_one = 'x'
            print('2, 1')
            computer_wins()

        elif player_move == '2, 1':
            one_three = 'x'
            print('1, 3')
            computer_wins()
elif player_move == '2 ,2':
    three_three = 'x'
    print("3, 3")

    if player_move == '2, 1':
        two_three = 'x'
        print('2, 3')
        ask_for_move()

        if player_move == '3, 1' or '1, 2' or '3, 2':
            two_three = 'x'
            print('2, 3')
            computer_wins()
        elif player_move == '1, 3':
            three_one = 'x'
            print('3, 1')
            ask_for_move()

            if player_move == '1, 2':
                three_two = 'x'
                print('1, 2')
                computer_wins()
            elif player_move == '3, 2':
                one_two = 'x'
                print('1, 2')
                tie()
    elif player_move == '3, 1':
        one_three = 'x'
        print('1, 3')
        ask_for_move()

        if player_move == '2, 1' or '2, 3':
            one_two = 'x'
            print('1, 2')
            computer_wins()
        elif player_move == '1, 2' or '3, 2':
            two_three = 'x'
            print('2, 3')
            computer_wins()
    elif player_move == '1, 2':
        three_two = 'x'
        print('3, 2')
        ask_for_move()

        if player_move == '2, 1' or '1, 3' or '2, 3':
            three_two = 'x'
            print('3, 2')
            computer_wins()
        elif player_move == '3, 1':
            one_three
            print('1, 3')
            ask_for_move()

            if player_move == '2, 1':
                two_three = 'x'
                print('2, 3')
                computer_wins()
            elif player_move == '2, 3':
                two_one = 'x'
                print('2, 1')
                tie()
    elif player_move == '3, 2':
        one_two = 'x'
        print('1, 2')
        ask_for_move()

        if player_move == '2, 1' or '3, 1' or '2, 3':
            one_three = 'x'
            print(1, 3)
            computer_wins()
        elif player_move == '1, 3':
            three_one = 'x'
            print('3, 1')
            ask_for_move()

            if player_move == '2, 1':
                two_three = 'x'
                print('2, 3')
                computer_wins()
            elif player_move == '2, 3':
                two_one = 'x'
                print('2, 1')
                computer_wins()
    elif player_move == '1, 3':
        three_one = 'x'
        print('3, 1')
        ask_for_move()

        if player_move == '2, 1' or '2, 3':
            three_two = 'x'
            print('3, 2')
            computer_wins()
        elif player_move == '1, 2' or '2, 3':
            two_one = 'x'
            print('2, 1')
            computer_wins()
    elif player_move == '2, 3':
        two_one = 'x'
        print('2, 1')
        ask_for_move()

        if player_move == '1, 2' or '3, 2' or '1, 3':
            three_one = 'x'
            print('3, 1')
            computer_wins()
        elif player_move == '3, 1':
            one_three = 'x'
            print('1, 3')
            ask_for_move()

            if player_move == '1, 2':
                three_two = 'x'
                print('3, 2')
                computer_wins()
            elif player_move == '3, 2':
                one_two = 'x'
                print('1, 2')
                tie()
elif player_move == '3, 2':
    two_two = 'x'
    print('2, 2')
    ask_for_move()

    if player_move == '2, 1' or '3, 1' or '1, 2' or '1, 3' or '2, 3':
        three_three = 'x'
        print('3, 3')
        computer_wins()
    elif player_move == '3, 3':
        three_one = 'x'
        print('3, 1')
        ask_for_move()

        if player_move == '1, 2' or '1, 3' or '2, 3':
            two_one = 'x'
            print('2, 1')
            computer_wins()
        elif player_move == '2, 1':
            one_three = 'x'
            print('1, 3')
            computer_wins()
elif player_move == '1, 3':
    three_one = 'x'
    print('3, 1')
    ask_for_move()

    if player_move == '1, 2' or '2, 2' or '3, 2' or '2, 3' or '3, 3':
        two_one = 'x'
        print('2,1')
        computer_wins()
    elif player_move == '2, 1':
        three_three = 'x'
        print('3, 3')
        ask_for_move()

        if player_move == '1, 2' or '2, 2' or '2, 3':
            three_two = 'x'
            print('3, 2')
            computer_wins()
        elif player_move == '3, 2':
            two_two = 'x'
            print('2, 2')
            computer_wins()
elif player_move == '2, 3':
    two_two = 'x'
    print('2, 2')
    ask_for_move()

    if player_move == '2, 1' or '3, 1' or '1, 2' or '3, 2' or '1, 3':
        three_three = 'x'
        print('3, 3')
        computer_wins()
    elif player_move == '3, 3':
        one_three = 'x'
        print('1, 3')
        ask_for_move()

        if player_move == '2, 1' or '3, 1':
            one_two = 'x'
            print('1, 2')
            computer_wins()
        elif player_move == '1, 2' or '3, 2':
            three_two = 'x'
            print('3, 2')
            computer_wins()
elif player_move == '3, 3':
    three_one = 'x'
    print('3, 1')
    ask_for_move()

    if player_move == '1, 2' or '2, 2' or '3, 2' or '1, 3' or '2, 3':
        two_one = 'x'
        print('2, 1')
        computer_wins()
    elif player_move == '2, 1':
        one_three = 'x'
        print('1, 3')
        ask_for_move()

        if player_move == '2, 2' or '3, 2' or '2, 3':
            one_two = 'x'
            print('1, 2')
            computer_wins()
        elif player_move == '1, 2':
            two_two = 'x'
            print('2, 2')
            computer_wins()
