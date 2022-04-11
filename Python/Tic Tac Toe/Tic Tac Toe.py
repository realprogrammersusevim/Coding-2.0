# First int is x value second is y
print("1, 1")

oneone = "x"
onetwo = "x"
onethree = "nx"
twoone = "none"
twotwo = "none"
twothree = "none"
threeone = "none"
threetwo = "none"
threethree = "none"

x_won = False
o_won = False


def ask_for_move():
    opponent_move = input("Where would you like to go? ")


def check_for_win():
    if (oneone == 'x') and (twoone == 'x') and (threeone == 'x'):
        x_won = True
    elif (onetwo == 'x') and (twotwo == 'x') and (threetwo == 'x'):
        x_won = True
    elif (onethree == 'x') and (twothree == 'x') and (threethree == 'x'):
        x_won = True
    elif (oneone == 'o') and (twoone == 'o') and (threeone == 'o'):
        o_won = True
    elif (onetwo == 'o') and (twotwo == 'o') and (threetwo == 'o'):
        o_won = True
    elif (onethree == 'o') and (twothree == 'o') and (threethree == 'o'):
        o_won = True


check_for_win()
print(x_won)
