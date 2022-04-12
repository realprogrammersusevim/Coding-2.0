from re import I
import central as cent

# First int is x value second is y
print("1, 1")


cent.ask_for_move()
if cent.player_move == '2, 1':
    two_two = 'x'
    print("2, 2")
    cent.ask_for_move()

    if cent.player_move == '3, 1' or '1, 2' or '3, 2' or '1, 3' or '2, 3':
        cent.three_three = 'x'
        print('3, 3')
        cent.computer_wins()
    elif cent.player_move == '3, 3':
        cent.one_three = 'x'
        print('1, 3')
        cent.ask_for_move()

        if cent.player_move == '3, 1' or '3, 2' or '2, 3':
            cent.one_two = 'x'
            print('1, 2')
            cent.computer_wins()
        elif cent.player_move == '1, 2':
            cent.three_one = 'x'
            print('3, 1')
            cent.computer_wins()
elif cent.player_move == '3, 1':
    cent.one_three = 'x'
    print("1, 3")
    cent.ask_for_move()

    if cent.player_move == '2, 1' or '2, 2' or '3, 2' or '2, 3' or '3, 3':
        cent.one_two = 'x'
        print('1, 2')
        cent.computer_wins()

    elif cent.player_move == '1, 2':
        cent.three_three = 'x'
        print('3, 3')
        cent.ask_for_move()

        if cent.player_move == '2, 1' or '2, 2' or '3, 2':
            cent.two_three = 'x'
            print('2, 3')
            cent.computer_wins()

        elif cent.player_move == '2, 3':
            cent.two_two = 'x'
            print('2, 2')
            cent.computer_wins()
elif cent.player_move == '1, 2':
    cent.two_two = 'x'
    print("2, 2")
    cent.ask_for_move()

    if cent.player_move == '2, 1' or '3, 1' or '3, 2' or '1, 3' or '2, 3':
        cent.three_three = 'x'
        print('3, 3')
        cent.computer_wins()

    elif cent.player_move == '3, 3':
        cent.three_one = 'x'
        print('3, 1')
        cent.ask_for_move()

        if cent.player_move == '3, 2' or '1, 3' or '2, 3':
            cent.two_one = 'x'
            print('2, 1')
            cent.computer_wins()

        elif cent.player_move == '2, 1':
            cent.one_three = 'x'
            print('1, 3')
            cent.computer_wins()
elif cent.player_move == '2 ,2':
    cent.three_three = 'x'
    print("3, 3")

    if cent.player_move == '2, 1':
        cent.two_three = 'x'
        print('2, 3')
        cent.ask_for_move()

        if cent.player_move == '3, 1' or '1, 2' or '3, 2':
            cent.two_three = 'x'
            print('2, 3')
            cent.computer_wins()
        elif cent.player_move == '1, 3':
            cent.three_one = 'x'
            print('3, 1')
            cent.ask_for_move()

            if cent.player_move == '1, 2':
                cent.three_two = 'x'
                print('1, 2')
                cent.computer_wins()
            elif cent.player_move == '3, 2':
                cent.one_two = 'x'
                print('1, 2')
                cent.tie()
    elif cent.player_move == '3, 1':
        cent.one_three = 'x'
        print('1, 3')
        cent.ask_for_move()

        if cent.player_move == '2, 1' or '2, 3':
            cent.one_two = 'x'
            print('1, 2')
            cent.computer_wins()
        elif cent.player_move == '1, 2' or '3, 2':
            cent.two_three = 'x'
            print('2, 3')
            cent.computer_wins()
    elif cent.player_move == '1, 2':
        cent.three_two = 'x'
        print('3, 2')
        cent.ask_for_move()

        if cent.player_move == '2, 1' or '1, 3' or '2, 3':
            cent.three_two = 'x'
            print('3, 2')
            cent.computer_wins()
        elif cent.player_move == '3, 1':
            cent.one_three
            print('1, 3')
            cent.ask_for_move()

            if cent.player_move == '2, 1':
                cent.two_three = 'x'
                print('2, 3')
                cent.computer_wins()
            elif cent.player_move == '2, 3':
                cent.two_one = 'x'
                print('2, 1')
                cent.tie()
    elif cent.player_move == '3, 2':
        cent. one_two = 'x'
        print('1, 2')
        cent.ask_for_move()

        if cent.player_move == '2, 1' or '3, 1' or '2, 3':
            cent.one_three = 'x'
            print(1, 3)
            cent.computer_wins()
        elif cent.player_move == '1, 3':
            cent.three_one = 'x'
            print('3, 1')
            cent.ask_for_move()

            if cent.player_move == '2, 1':
                cent.two_three = 'x'
                print('2, 3')
                cent.computer_wins()
            elif cent.player_move == '2, 3':
                cent.two_one = 'x'
                print('2, 1')
                cent.computer_wins()
    elif cent.player_move == '1, 3':
        cent.three_one = 'x'
        print('3, 1')
        cent.ask_for_move()

        if cent.player_move == '2, 1' or '2, 3':
            cent.three_two = 'x'
            print('3, 2')
            cent.computer_wins()
        elif cent.player_move == '1, 2' or '2, 3':
            cent.two_one = 'x'
            print('2, 1')
            cent.computer_wins()
    elif cent.player_move == '2, 3':
        cent.two_one = 'x'
        print('2, 1')
        cent.ask_for_move()

        if cent.player_move == '1, 2' or '3, 2' or '1, 3':
            cent.three_one = 'x'
            print('3, 1')
            cent.computer_wins()
        elif cent.player_move == '3, 1':
            cent.one_three = 'x'
            print('1, 3')
            cent.ask_for_move()

            if cent.player_move == '1, 2':
                cent.three_two = 'x'
                print('3, 2')
                cent.computer_wins()
            elif cent.player_move == '3, 2':
                cent.one_two = 'x'
                print('1, 2')
                cent.tie()
elif cent.player_move == '3, 2':
    cent.two_two = 'x'
    print('2, 2')
    cent.ask_for_move()

    if cent.player_move == '2, 1' or '3, 1' or '1, 2' or '1, 3' or '2, 3':
        cent.three_three = 'x'
        print('3, 3')
        cent.computer_wins()
    elif cent.player_move == '3, 3':
        cent.three_one = 'x'
        print('3, 1')
        cent.ask_for_move()

        if cent.player_move == '1, 2' or '1, 3' or '2, 3':
            cent.two_one = 'x'
            print('2, 1')
            cent.computer_wins()
        elif cent.player_move == '2, 1':
            cent.one_three = 'x'
            print('1, 3')
            cent.computer_wins()
elif cent.player_move == '1, 3':
    cent.three_one = 'x'
    print('3, 1')
    cent.ask_for_move()

    if cent.player_move == '1, 2' or '2, 2' or '3, 2' or '2, 3' or '3, 3':
        cent.two_one = 'x'
        print('2,1')
        cent.computer_wins()
    elif cent.player_move == '2, 1':
        cent.three_three = 'x'
        print('3, 3')
        cent.ask_for_move()

        if cent.player_move == '1, 2' or '2, 2' or '2, 3':
            cent.three_two = 'x'
            print('3, 2')
            cent.computer_wins()
        elif cent.player_move == '3, 2':
            cent.two_two = 'x'
            print('2, 2')
            cent.computer_wins()
elif cent.player_move == '2, 3':
    cent.two_two = 'x'
    print('2, 2')
    cent.ask_for_move()

    if cent.player_move == '2, 1' or '3, 1' or '1, 2' or '3, 2' or '1, 3':
        cent.three_three = 'x'
        print('3, 3')
        cent.computer_wins()
    elif cent.player_move == '3, 3':
        cent.one_three = 'x'
        print('1, 3')
        cent.ask_for_move()

        if cent.player_move == '2, 1' or '3, 1':
            cent.one_two = 'x'
            print('1, 2')
            cent.computer_wins()
        elif cent.player_move == '1, 2' or '3, 2':
            cent.three_two = 'x'
            print('3, 2')
            cent.computer_wins()
elif cent.player_move == '3, 3':
    cent.three_one = 'x'
    print('3, 1')
    cent.ask_for_move()

    if cent.player_move == '1, 2' or '2, 2' or '3, 2' or '1, 3' or '2, 3':
        cent.two_one = 'x'
        print('2, 1')
        cent.computer_wins()
    elif cent.player_move == '2, 1':
        cent.one_three = 'x'
        print('1, 3')
        cent.ask_for_move()

        if cent.player_move == '2, 2' or '3, 2' or '2, 3':
            cent.one_two = 'x'
            print('1, 2')
            cent.computer_wins()
        elif cent.player_move == '1, 2':
            cent.two_two = 'x'
            print('2, 2')
            cent.computer_wins()
