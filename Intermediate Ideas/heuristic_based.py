import curses, time, copy, UI_elements as UI
from checks_counts import *
from math import inf
from algo import *

def heuristic(arr, n, move, turn):

    x,y = move
    count, row, col, diag, adiag = 0, 0, 0, 0, 0

    # Along row
    for i in range(n):
        
        if(arr[x][i] == turn):
            row = row + 1
        elif(arr[x][i] == 1 - turn):
            row = 0
            break

    # Along col
    for i in range(n):

        if(arr[i][y] == turn):
            col = col + 1
        elif(arr[i][y] == 1 - turn):
            col = 0
            break

    # Diagonal
    if(x == y):
        for i in range(n):
            if(arr[i][i] == turn):
                diag = diag + 1
            elif(arr[i][i] == 1 - turn):
                diag = 0
                break

    if(x + y == n-1):

        for i in range(n):
            if(arr[i][n-i-1] == turn):
                adiag = adiag + 1
            elif(arr[i][n-i-1] == 1 - turn):
                adiag = 0
                break

    return row + col + diag + adiag


def count_moves(arr, n):

    count = 0
    for i in range(n):
        for j in range(n):
            if(arr[i][j] != -1):
                count = count + 1

    return count


def NextWithPruning(turn, n, arr, alpha, beta):

    limit = n
    if(n == 3):
        limit = 2

    if(count_moves(arr,n) < limit):
        for i in range(n):
            for j in range(n):
                if(arr[i][j] == -1):
                    arr[i][j] = turn
                    return [0, i, j]


    moves = possibleMoves(arr,n)
    moves.sort(reverse = True, key = lambda x : heuristic(arr, n, x, turn))

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

            if(val > best_val[0]):
                best_val = [val, x, y]

            if(best_val[0] >= beta):
                return best_val

            alpha = max(alpha, best_val[0])

        return best_val

n = int(input("Enter n for size of board : "))
player = int(input("Enter 1 if you want to play as player 1 otherwise enter 2 : "))
[sc, win, h, w ] = UI.initialise_screen(n)
flag = -1
played = 0

if(player == 2):
    played = 1

arr = [[-1]*n for i in range(n)]

# for i in range(1,12):
#     start_time = time.time()
#     p = NextWithPruning(i%2, n, arr, -inf, inf)
#     print("--- %s seconds ---" % (time.time() - start_time))
#     print(i%2, p)
#     arr[p[1]][p[2]] = i%2
# start_time = time.time()
# p = NextWithPruning(1, n, arr, -inf, inf)
# print("--- %s seconds ---" % (time.time() - start_time))
# print(p)


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


# Checking conditions for winning or losing or draw
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
