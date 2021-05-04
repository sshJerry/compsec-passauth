#include <ncurses.h>
#include <signal.h>
#include <unistd.h>

#include <stdio.h>
#include <string.h>

#define QUIT_KEY 'q'
static int is_running = 1;
// cd Downloads/VS\ CODE/c492-final/

static WINDOW *win;
//cd Downloads/VS\ CODE/CS355\ Final\ Project/Menu/

int main(int argc, char **argv)
{
    initscr();
    noecho();
    //cbreak();
    curs_set(0);

    int height = 0;
    int width = 0;
    getmaxyx(stdscr, height, width);

    //\\\\\\\\\\\\\\\\\\\\\\\\ - LOGIN WINDOW - \\\\\\\\\\\\\\\\

    WINDOW *menuwindow = newwin(height, width, 0, 0);
    box(menuwindow, 0, 0);
    refresh();
    wrefresh(menuwindow);

    keypad(menuwindow, true);

    char choices[3][13] = {"Login", "Unclassified", "Exit"};
    char username[10];
    char password[10];
    int choice;
    int highlight = 0;

    //wtimeout(menuwindow, 20);
    while (is_running)
    {
        for (int i = 0; i < 3; i++)
        {
            if (i == highlight)
                wattron(menuwindow, A_REVERSE);
            mvwprintw(menuwindow, i + (height / 2) - 2, (width / 4) - 2, choices[i]);
            wattroff(menuwindow, A_REVERSE);
        }

        choice = wgetch(menuwindow);
        switch (choice)
        {
        case KEY_UP:
            if (!(highlight <= 0))
            {
                highlight--;
            }
            break;
        case KEY_DOWN:
            if (!(highlight >= 2))
            {
                highlight++;
            }
            break;
        }
        // 10 refers to the "ENTER" key being pressed. The user wants to execute option
        if (choice == 10 && highlight == 2)
        {
            is_running = 0;
        }
        if (choice == 10 && highlight == 0)
        {
            break;
        }
    }
    //mvprintw((height / 2) - 2, (width / 2) - 2, "Username: ");
    //printw("Username: ");
    // move((height / 2) - 2, (width / 2) - 2);
    //mvwprintw(menuwindow, (height / 2) - 2, (width / 2) - 2, "Username: ");
    //printw("Username: ");
    //scanf("%s", username);
    delwin(menuwindow);

    //\\\\\\\\\\\\\\\\\\\\\\\\ - Sign in Window - \\\\\\\\\\\\\\\\

    WINDOW *loginwindow = newwin(height, width, 0, 0);
    box(loginwindow, 0, 0);
    refresh();
    wrefresh(loginwindow);

    while (is_running){
        refresh();
        mvwprintw(loginwindow, (height / 2) - 2, (width / 2) - 2, "Username: ");
        scanf("%s", username);
        mvwprintw(loginwindow, (height / 2), (width / 2) - 2, "Password: ");
    }

    mvprintw((height / 2) - 2, (width / 2) - 2, "Username: ");
    move((height / 2) - 2, (width / 2) - 2);
    refresh();
    scanf("%s", username);
    mvprintw((height / 2), (width / 2) - 2, "Password: ");

    

    getch();
    endwin();
    return 0;
}