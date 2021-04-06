import curses, time, copy, numpy as np
#Just to make a few calculations easier, you could it without numpy as well
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

    for i in range(n):
        # Checking if Rows are marked
        if(arr[i][0]!=-1):
            f = 0
            for j in range(n):
                if(arr[i][0] != arr[i][j]):
                    f = 1
                    break

            if(f == 0):
                return 1            

        # Checking if Columns are marked
        if(arr[0][i]!=-1):
            f = 0
            for j in range(n):
                if(arr[0][i] != arr[j][i]):
                    f = 1
                    break

            if(f == 0):
                return 1 

    # Checking if diagonals are marked
    if(arr[0][0]!=-1):
        f = 0
        for i in range(n):
            if(arr[0][0] != arr[i][i]):
                f = 1
                break

        if(f == 0):
            return 1


    if(arr[n-1][0]!=-1):
        f = 0
        for i in range(n):
            if(arr[n-1][0] != arr[i][n-i-1]):
                f = 1
                break

        if(f == 0):
            return 1
                

    # If all are marked, hence draw
    f = 0
    for i in range(n):
        for j in range(n):
            if(arr[i][j] == -1):
                f = 1 

    if(f == 0):
        return 0

    return -1

def possibleMoves(arr,n):

    moves  = []

    for i in range(n):
        for j in range(n):
            if(arr[i][j] == -1):
                moves.append((i,j))

    return moves


def similarStates(already_calc, current):

    rotated_arr = np.rot90(np.fliplr(current)).tolist()
    for i in already_calc:
        if(rotated_arr == i):
            return 1


    rotated_arr = np.rot90(np.fliplr(np.flip(current))).tolist()
    for i in already_calc:
        if(rotated_arr == i):
            return 1

    rotated_arr = np.flip(current, axis = 0).tolist()
    for i in already_calc:
        if(rotated_arr == i):
            return 1

    rotated_arr = np.flip(current, axis = 1).tolist()
    for i in already_calc:
        if(rotated_arr == i):
            return 1

    return 0


def NextWithPruning(turn, n, arr, alpha, beta):

    moves = possibleMoves(arr,n)

    # Minimizer
    if(turn == 0):

        best_val = [inf, -1, -1]
        for x,y in moves:

            arr[x][y] = 0

            # if(similarStates(already_calc, arr)):
            #     print(arr)
            #     arr[x][y] = -1
            #     continue

            c = check(arr,n)

            if(c == 1):
                val = -20
            elif(c == 0):
                val = 0
            else:
                val = NextWithPruning(1 - turn, n, arr, alpha, beta)[0]

            # already_calc.append(copy.deepcopy(arr))        
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



def NextMoveNaive(cost, turn, n, arr, depth = 0):

    global Last
    temp_cost = []
    moves  = possibleMoves(arr,n)

    if(turn == 0):

        for x,y in moves:

            arr[x][y] = 0
            c = check(arr,n)

            if(c == 1):
                temp_cost.append([cost-20, x, y])

            elif(c == 0):
                temp_cost.append([cost, x, y])
            
            else:
                val = NextMoveNaive(cost, 1 - turn, n, arr, depth + 1)[0]
                temp_cost.append([val,x,y])

            arr[x][y] = -1

        Last = temp_cost

        return min(temp_cost)

    else:

        for x,y in moves:

            arr[x][y] = 1
            c = check(arr,n)

            if(c == 1):
                temp_cost.append([cost+20,x,y])

            elif(c == 0):
                temp_cost.append([cost,x,y])

            else:
                temp_cost.append([NextMoveNaive(cost, 1 - turn, n, arr, depth + 1)[0],x,y])

            arr[x][y] = -1

        Last = temp_cost
        return max(temp_cost)

n = 3
# player = int(input("Enter 1 if you want to play as player 1 otherwise enter 2 : "))

# ##initialize screen
# sc = curses.initscr()
# h, w = sc.getmaxyx()
# win = curses.newwin(h, w, 0, 0)
# win.keypad(1)
# curses.curs_set(0)

# createGrid(h,w,n)
# curses.mousemask(1)

flag = -1
# played = 0

# if(player == 2):
#     played = 1

arr = [[-1]*n for i in range(n)]

start_time = time.time()
p = NextWithPruning(1, n, arr, -inf, inf)
print("--- %s seconds ---" % (time.time() - start_time))
print(p)


# while True:

#     win.border(0)
#     win.timeout(100)
#     curses.noecho()
#     next_key = win.getch()

#     if(next_key == curses.KEY_MOUSE and played == 0):
#         _, mx, my, _, _ = curses.getmouse()
#         arr_x = int((n)*my/h)
#         arr_y = int((n)*mx/w)
#         arr[arr_x][arr_y] = 0
#         win.addstr(int(((2*arr_x + 1)*h)/(2*n)),int(((2*arr_y + 1)*w)/(2*n)),'X')
#         played = 1

#     if(next_key == 55):
#         break

#     c = check(arr,n)
#     if(c == 0):
#         break

#     if(played == 1):
#         p = NextWithPruning(1, n, arr, -inf, inf)
#         arr[p[1]][p[2]] = 1
#         win.addstr(int(((2*p[1] + 1)*h)/(2*n)),int(((2*p[2] + 1)*w)/(2*n)),'0')
#         played = 0
#         c = check(arr,n)
#         if(c == 1):
#             flag = 0
#             break


## Checking conditions for winning or losing or draw
# if(flag==0):
#     s = "You Lost!"
# elif(flag==1):
#     s = "You Won!"
# elif(flag==-1):
#     s = "Draw!"

# ## Outputting Result
# sc.addstr(int(h/2),int(w/2),s)
# sc.refresh()
# time.sleep(2)
# curses.endwin()
