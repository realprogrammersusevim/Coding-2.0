from random import randint
import numpy as np


player_move = ''

player_move_x = ''
player_move_y = ''

rotation = randint(1, 4)
# This variable cotrols how much the board will be rotated to add randomness in
# the users perspective. 0 doesn't change it, 1 is 90 degrees, and so on.
computer_move = int

# These board representations are actually correct but the backslashes have to
# be excaped.
BOARD_X = """
\\  /
 \\/
 /\\
/  \\
      """
BOARD_O = """
/----\\
|    |
|    |
\\----/
"""
EMPTY = """




      """
HORIZONTAL_SEPARATOR = """
||
||
||
||
"""
VERTICAL_SEPARATOR = "======"

# This is the matrix that forms the real board
board = np.array([
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
])
