import curses

# Draws the n x n grid on the terminal
def createGrid(h, w, n, win):

    for j in range(1,n):
        for i in range(h):
            win.addstr(i,int(j*w/n),'|')

    for i in range(1,n):
        for j in range(w):
            win.addstr(i * int(h/n),j,'-')


def initialise_screen(n):

    sc = curses.initscr()
    h, w = sc.getmaxyx()
    win = curses.newwin(h, w, 0, 0)
    win.keypad(1)
    curses.curs_set(0)
    createGrid(h, w, n, win)
    curses.mousemask(1)

    return [sc, win, h, w]