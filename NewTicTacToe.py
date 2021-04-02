import curses
import time
#Just to make a few calculations easier, you could it without numpy as well
import numpy as np
from math import inf

# Draws the n x n grid on the terminal
def createGrid(h,w,n):
    # global col
    # global row
    col = []
    row = []
    for j in range(1,n):
        for i in range(h):
            win.addstr(i,int(j*w/n),'|')
        # col.append(int(j*w/n))

    for i in range(1,n):
        for j in range(w):
            win.addstr(i * int(h/n),j,'-')
        # row.append(i * int(h/n))

def check(arr, n):

    # Checking if Rows are marked
    for i in range(n):
        if(np.min(arr[i]) == 0 and np.max(arr[i]) == 0):
            return 1
        if(np.min(arr[i])==1 and np.max(arr[i])==1):
            return 1

    # Checking if Columns are marked
    temp = np.array(arr).T
    for i in range(n):
        if(np.min(temp[i]) == 0 and np.max(temp[i]) == 0):
            return 1
        if(np.min(temp[i])==1 and np.max(temp[i])==1):
            return 1


    # Checking if diagonals are marked
    temp = np.diagonal(arr)
    if(np.min(temp) == 0 and np.max(temp) == 0):
        return 1
    if(np.min(temp)==1 and np.max(temp)==1):
        return 1


    temp = np.diagonal(np.flip(arr,axis=1))
    if(np.min(temp) == 0 and np.max(temp) == 0):
        return 1
    if(np.min(temp)==1 and np.max(temp)==1):
        return 1


    # If all are marked, hence draw
    if(np.min(arr)!=-1):
        return 0


    return -1

def possibleMoves(arr,n):

    moves  = []

    for i in range(n):
        for j in range(n):
            if(arr[i][j]==-1):
                moves.append((i,j))

    return moves

def NextWithPruning(turn, n, arr, alpha, beta):

    global U
    temp_cost = []
    moves = possibleMoves(arr,n)

    # Minimizer
    if(turn == 0):

        best_val = [inf, -1, -1]
        for x,y in moves:

            arr[x][y] = 0
            c = check(arr,n)

            if(c == 1):
                val = -20
            elif(c == 0):
                val = 0
            else:
                val = NextWithPruning(1 - turn, n, arr, alpha, beta)[0]
            
            arr[x][y] = -1
            temp_cost.append([val,x,y])

            if(val < best_val[0]):
                best_val = [val, x, y]

            if(best_val[0] <= alpha):
                return best_val

            beta = min(beta, best_val[0])

        return best_val

    else:

        best_val = [-inf, -1, -1]

        for x,y in moves:

            arr[x][y] = 1 
            c = check(arr,n)

            if(c == 1):
                val =  20
            elif(c == 0):
                val = 0
            else:
                val = NextWithPruning(1 - turn, n, arr, alpha, beta)[0]

            arr[x][y] = -1
            temp_cost.append([val, x, y])

            if(val > best_val[0]):
                best_val = [val, x, y]

            if(best_val[0] >= beta):
                return best_val

            alpha = max(alpha, best_val[0])

        return best_val

n = 3


player = int(input("Enter 1 if you want to play as player 1 otherwise enter 2 : "))

##initialize screen
sc = curses.initscr()
h, w = sc.getmaxyx()
win = curses.newwin(h, w, 0, 0)
win.keypad(1)
curses.curs_set(0)

createGrid(h,w,n)
curses.mousemask(1)

flag = -1
played = 0

if(player == 2):
    played = 1

arr = [[-1]*n for i in range(n)]

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
        p = NextWithPruning(1, n, arr, -inf, inf)
        arr[p[1]][p[2]] = 1
        win.addstr(int(((2*p[1] + 1)*h)/(2*n)),int(((2*p[2] + 1)*w)/(2*n)),'0')
        played = 0
        c = check(arr,n)
        if(c == 1):
            flag = 0
            break


## Checking conditions for winning or losing or draw
if(flag==0):
    s = "You Lost!"
elif(flag==1):
    s = "You Won!"
elif(flag==-1):
    s = "Draw!"

## Outputting Result
sc.addstr(int(h/2),int(w/2),s)
sc.refresh()
time.sleep(2)
curses.endwin()
