import central as cent

# First int is x value second is y
print("1, 1")

x_won = False
o_won = False

cent.ask_for_move()
if cent.player_move == '2, 1':
    two_two = 'x'
    print("2, 2")
elif cent.player_move == '3, 1':
    cent.one_three = 'x'
    print("1, 3")
elif cent.player_move == "1, 2":
    cent.two_two = 'x'
    print("2, 2")
elif cent.player_move == "2 ,2":
    cent.three_three = 'x'
    print("3, 3")
