import curses
# import urwid
import time

menu = ['Login', 'Unclassified', 'Exit']


# cd Downloads/VS\ CODE/pythonProject/ || python3 main.py

class User:
    def __init__(self, level, username, password):
        self.level = level
        self.username = username
        self.password = password


def print_menu(stdscr, selected_option):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for i, row in enumerate(menu):
        x = w // 2 - len(row) // 2
        y = h // 2 - len(menu) // 2 + i
        if i == selected_option:
            stdscr.attron(curses.A_REVERSE)
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.A_REVERSE)
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()


def print_login(stdscr):
    stdscr.clear()
    curses.echo()
    stdscr.addstr(0, 0, "Username: ")
    stdscr.addstr(1, 0, "Password: ")
    stdscr.refresh()
    username = stdscr.getstr(0, 10, 15)
    password = stdscr.getstr(1, 10, 15)
    pass


def unclassified_view(stdscr):
    pass


def main(stdscr):
    admin = User('Top', 'admin', 'password1')
    worker = User('Medium', 'user', 'password2')
    guest = User('Bottom', 'guest', 'password3')
    curses.curs_set(0)

    highlight = 0
    print_menu(stdscr, highlight)

    # stdscr.clear()
    while True:
        key = stdscr.getch()
        stdscr.clear()
        if key == curses.KEY_UP and not (highlight <= 0):
            highlight -= 1
        elif key == curses.KEY_DOWN and not (highlight >= 2):
            highlight += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if highlight == 0:
                print_login(stdscr)
            # curses.nocbreak()
            # stdscr.keypad(False)
            # curses.echo()
            stdscr.clear()
            stdscr.addstr(0, 0, "Pressed {}".format(menu[highlight]))
            stdscr.refresh()
            # stdscr.getch()
        print_menu(stdscr, highlight)
        stdscr.refresh()


curses.wrapper(main)
