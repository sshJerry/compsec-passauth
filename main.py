import curses
#import urwid
import time

menuGuest = ['Login', 'Unclassified', 'Exit']
menuUser = ['See Medium Level Files', 'Unclassified', 'Exit']
menuAdmin = ['See Admin Level Files', menuUser[0], menuUser[1], menuUser[2]]


# cd Downloads/VS\ CODE/pythonProject/ || python3 main.py

class User:
    def __init__(self, level, username, password, permission):
        self.level = level
        self.username = username
        self.password = password
        self.permission = permission

    def get_username(self):
        return self._username


def print_menu(stdscr, selected_option, access_request, name):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    stdscr.addstr(0, 0, ("Currently: " + str(name)))
    for i, row in enumerate(access_request):
        x = w // 2 - len(row) // 2
        y = h // 2 - len(access_request) // 2 + i
        if i == selected_option:
            stdscr.attron(curses.A_REVERSE)
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.A_REVERSE)
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()


def print_login(stdscr, u1, p1, u2, p2):
    stdscr.clear()
    curses.echo()
    stdscr.addstr(0, 0, "Username: ")
    stdscr.addstr(1, 0, "Password: ")
    stdscr.refresh()
    username = stdscr.getstr(0, 10, 15)
    password = stdscr.getstr(1, 10, 15)
    str(username)
    str(password)
    stdscr.addstr(5, 5, username)
    stdscr.addstr(6, 5, u1)
    stdscr.addstr(8, 5, password)
    stdscr.addstr(9, 5, p1)

    stdscr.addstr(5, 15, username)
    stdscr.addstr(6, 15, u2)
    stdscr.addstr(8, 15, password)
    stdscr.addstr(9, 15, p2)
    stdscr.refresh()
    if (str(username) == str(u1)) and (str(password) == str(p1)):
        return str(u1)
    elif username == u2:
        if password == p2:
            return u2.username
    else:
        return 'guest'


def unclassified_view(stdscr):
    pass


def main(stdscr):
    admin = User('Top', 'admin', '1', menuAdmin)
    worker = User('Medium', 'user', 'password2', menuUser)
    guest = User('Bottom', 'guest', '', menuGuest)
    curses.curs_set(0)

    highlight = 0
    print_menu(stdscr, highlight, guest.permission, guest.username)

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
                access = print_login(stdscr, admin.username, admin.password, worker.username, worker.password)
                stdscr.addstr(3, 3, access)

                stdscr.getch()
            stdscr.clear()
            stdscr.refresh()
            # stdscr.getch()
        print_menu(stdscr, highlight, User.get_username(access), access)
        stdscr.refresh()


curses.wrapper(main)
