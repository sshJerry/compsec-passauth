import curses
# import urwid
import time

menu = ['Login', 'Unclassified', 'Exit']


# cd Downloads/VS\ CODE/pythonProject/ || python3 main.py


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


def main(stdscr):
    curses.curs_set(0)

    highlight = 0
    print_menu(stdscr, highlight)

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
                stdscr.getch()
            stdscr.clear()
            stdscr.refresh()
            # stdscr.getch()
        print_menu(stdscr, highlight)
        stdscr.refresh()


curses.wrapper(main)
