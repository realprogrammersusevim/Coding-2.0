one_one = "x"
one_two = "none"
one_three = "none"
two_one = "none"
two_two = "none"
two_three = "none"
three_one = "none"
three_two = "none"
three_three = "none"


def ask_for_move():
    player_move_x = input("Where would you like to go on the x axis? ")
    while player_move_x != '1' or '2' or '3':
        player_move_x = input("Where would you like to go on the x axis? ")

    player_move_y = input("Where would you like to go on the y axis? ")
    while player_move_y != '1' or '2' or '3':
        player_move_y = input("Where would you like to go on the y axis? ")

    player_move = (player_move_x, player_move_y)
    if player_move == '1, 1':
        one_one = 'o'
    elif player_move == ' 2, 1':
        two_one = 'o'
    elif player_move == '3, 1':
        three_one = 'o'
    elif player_move == '1, 2':
        one_two = 'o'
    elif player_move == '2, 2':
        two_two = 'o'
    elif player_move == '3, 2':
        three_two = 'o'
    elif player_move == '1, 3':
        one_three = 'o'
    elif player_move == '2, 3':
        two_three = 'o'
    elif player_move == '3, 3':
        three_three = 'o'


def computer_wins():
    print('The computer wins. Humanity is doomed.')
    # Eventually I'll start storing the win-tie record.


def tie():
    print('You tied up the game. Good job not-loser.')


def show_board():
    if one_one == 'x' and two_one == 'x' and three_one == 'x':
        print('''
              \  /      \  /        \  /
               \         \           \
             /  \       /  \        /  \
              ''')
