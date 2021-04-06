import curses, time, copy, numpy as np, math, UI_elements as UI
from checks_counts import *
from math import inf
from algo import *

def get_move(turn, n, arr, depth_limit):

    alpha = -inf
    beta  =  inf

    # Time limit set to 1 second per move
    start_time = time.time()
    for i in range(1,depth_limit+1):

        prev = NextWithPruning(turn, n, arr, alpha, beta, 0, i, 1, start_time)
        if(time.time() - start_time > 1):
            break
        p = prev


    return p

n = int(input("Enter n for size of board : "))
player = int(input("Enter 1 if you want to play as player 1 otherwise enter 2 : "))
[sc, win, h, w ] = UI.initialise_screen(n)
flag = -1
played = 0

if(player == 2):
    played = 1

arr = [[-1]*n for i in range(n)]

# for i in range(n*n):
#     start_time = time.time()
#     # p = NextWithPruning(i%2, n, arr, alpha, beta, 0, 6)
#     p = get_move(i%2, n, arr, 6)
#     arr[p[1]][p[2]] = i%2
#     print(i%2, p)
#     print("--- %s seconds ---" % (time.time() - start_time))


while True:

    win.border(0)
    win.timeout(100)
    curses.noecho()
    next_key = win.getch()

    if(next_key == curses.KEY_MOUSE and played == 0):
        _, mx, my, _, _ = curses.getmouse()
        arr_x = int((n)*my/h)
        arr_y = int((n)*mx/w)
        arr[arr_x][arr_y] = 0
        win.addstr(int(((2*arr_x + 1)*h)/(2*n)),int(((2*arr_y + 1)*w)/(2*n)),'X')
        played = 1

    if(next_key == 55):
        break

    c = check(arr,n)
    if(c == 0):
        break

    if(played == 1):
        p = get_move(1, n, arr, 6)
        arr[p[1]][p[2]] = 1
        win.addstr(int(((2*p[1] + 1)*h)/(2*n)),int(((2*p[2] + 1)*w)/(2*n)),'0')
        played = 0
        c = check(arr,n)
        if(c == 1):
            flag = 0
            break

# Checking conditions for winning or losing or draw
if(flag == 0):
    s = "You Lost!"
elif(flag == 1):
    s = "You Won!"
elif(flag == -1):
    s = "Draw!"

## Outputting Result
sc.addstr(int(h/2),int(w/2),s)
sc.refresh()
time.sleep(2)
curses.endwin()
