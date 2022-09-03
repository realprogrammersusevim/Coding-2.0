import sys
from streamlit import cli as stcli
import curses
from curses import wrapper

screen = curses.initscr()


def main(screen):
    curses.curs_set(0)
    num_rows, num_cols = screen.getmaxyx()
    middle_column = int(num_cols / 2)
    middle_row = int(num_rows / 2)
    half_length_of_message = int(num_cols / 2)
    x_position = middle_column - half_length_of_message

    message = """
Welcome to the Tic Tac Toe game.
It was coded by Jonathan Milligan.
The computers strategy was invented by Randall Munroe in the xkcd comic 832.
"""
    while True:
        screen.addstr(middle_row, x_position, message)
        screen.refresh()
        key = screen.getch()
        if key == ord("q"):
            curses.endwin()
            break
        elif key != curses.ERR:
            curses.endwin()
            sys.argv = ["streamlit", "run", "ttt.py"]
            sys.exit(stcli.main())
            import tic_tac_toe


wrapper(main)
