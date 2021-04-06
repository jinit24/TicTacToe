from checks_counts import *
from math import inf
import time

def NextMoveNaive(cost, turn, n, arr, depth = 0):

    # global Last
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

        # Last = temp_cost

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

        # Last = temp_cost
        return max(temp_cost)


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


def removing_initial_moves(arr, n):

    if(n>3 and count_moves(arr, n) < 2*n-3):
        return 1

    return 0


def NextWithPruning(turn, n, arr, alpha, beta, current_depth, depth_limit, time_limit = inf, start_time = inf):

    moves = possibleMoves(arr,n)
    moves.sort(reverse = True, key = lambda x : heuristic(arr, n, x, turn))

    if(time_limit != inf and time.time() - start_time > time_limit):
        return [0, moves[0][0], moves[0][1]]

    if(removing_initial_moves(arr, n)):
        return [0, moves[0][0], moves[0][1]]

    # Minimizer
    if(turn == 0):

        best_val = [inf, -1, -1]
        if(current_depth == depth_limit):
            return [0, moves[0][0], moves[0][1]]

        for x,y in moves:

            arr[x][y] = 0
            c = check(arr,n)

            if(c == 1):
                val = -20
            elif(c == 0):
                val = 0
            else:
                val = NextWithPruning(1 - turn, n, arr, alpha, beta, current_depth + 1, depth_limit, time_limit, start_time)[0]

            arr[x][y] = -1

            if(val < best_val[0]):
                best_val = [val, x, y]

            if(best_val[0] <= alpha):
                return best_val

            beta = min(beta, best_val[0])

        return best_val

    else:

        best_val = [-inf, -1, -1]

        if(current_depth == depth_limit):
            return [0, moves[0][0], moves[0][1]]

        for x,y in moves:

            arr[x][y] = 1 
            c = check(arr,n)

            if(c == 1):
                val =  20
            elif(c == 0):
                val = 0
            else:
                val = NextWithPruning(1 - turn, n, arr, alpha, beta, current_depth + 1, depth_limit, time_limit, start_time)[0]

            arr[x][y] = -1

            if(val > best_val[0]):
                best_val = [val, x, y]

            if(best_val[0] >= beta):
                return best_val

            alpha = max(alpha, best_val[0])

            # print(x,y, current_depth, c, best_val[0])
        return best_val
