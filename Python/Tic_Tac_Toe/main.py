print('''
Welcome to the Tic Tac Toe game.
It was coded by Jonathan Milligan.
The computers strategy was invented by Randall Munroe in the xkcd comic 832.
Currently you can only play O and the computer can only play X.
''')

ready_to_continue = input("Are you ready to continue? (y/n) ")

if ready_to_continue == 'y':
    exec(open("tic_tac_toe.py").read())
