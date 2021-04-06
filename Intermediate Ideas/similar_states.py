import curses, time, copy, UI_elements as UI
from checks_counts import *
from math import inf
from algo import *

# Uses concept of similar states to prune search space
# But keeping track of moves made and checking for similarity is too expensive
# Hence symmetry test is done while generating possilble moves : possibleMoves(arr, n) in checks_counts.py

# Not used finally
# Intermediate idea
def similarStates(already_calc, current, to_mark, arr):

    # Rotation about main diagonal
    x = copy.deepcopy(arr)
    x[current[0]][current[1]] = to_mark

    rotated_arr = np.rot90(np.fliplr(x)).tolist()
    for i in already_calc:

        arr[i[0]][i[1]] = to_mark
        if(rotated_arr == arr):
            arr[i[0]][i[1]] = -1
            return 1

        arr[i[0]][i[1]] = -1

    # Rotation about other diagonal
    rotated_arr = np.rot90(np.fliplr(np.flip(x))).tolist()
    for i in already_calc:

        arr[i[0]][i[1]] = to_mark
        if(rotated_arr == arr):
            arr[i[0]][i[1]] = -1
            return 1

        arr[i[0]][i[1]] = -1


    # # Rotation horizontally and vertically

    rotated_arr = np.flip(x, axis = 0).tolist()
    for i in already_calc:

        arr[i[0]][i[1]] = to_mark
        if(rotated_arr == arr):
            arr[i[0]][i[1]] = -1
            return 1

        arr[i[0]][i[1]] = -1

    rotated_arr = np.flip(x, axis = 1).tolist()
    for i in already_calc:

        arr[i[0]][i[1]] = to_mark
        if(rotated_arr == arr):
            arr[i[0]][i[1]] = -1
            return 1

        arr[i[0]][i[1]] = -1

    return 0


def NextWithPruning(turn, n, arr, alpha, beta):

    moves = possibleMoves(arr,n)
    already_calc = []

    # Minimizer
    if(turn == 0):

        best_val = [inf, -1, -1]
        for x,y in moves:

            # if(similarStates(already_calc, (x,y), 0, arr)):
            #     continue

            arr[x][y] = 0
            c = check(arr,n)

            if(c == 1):
                val = -20
            elif(c == 0):
                val = 0
            else:
                val = NextWithPruning(1 - turn, n, arr, alpha, beta)[0]

            # already_calc.append((x,y))        
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


            # if(similarStates(already_calc, (x,y), 1, arr)):
            #     continue


            arr[x][y] = 1 
            c = check(arr,n)

            if(c == 1):
                val =  20
            elif(c == 0):
                val = 0
            else:
                val = NextWithPruning(1 - turn, n, arr, alpha, beta)[0]


            # already_calc.append((x,y))            
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


# for i in range(12):
#     start_time = time.time()
#     p = NextWithPruning(i%2, n, arr, -inf, inf)
#     print("--- %s seconds ---" % (time.time() - start_time))
#     print(i%2, p)
#     arr[p[1]][p[2]] = i%2


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
