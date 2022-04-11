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
        oneone = 'o'


def show_board():
    if one_one == 'x' and two_one == 'x' and three_one == 'x':
        print('''
              \  /      \  /        \  /
               \         \           \
             /  \       /  \        /  \
              ''')
