import math

# Checking if game is over or not
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


def check_symmetry_about_maind(arr, n):

    for i in range(n):
        for j in range(n):
            if(arr[i][j] != arr[j][i]):
                return 0

    return 1


def check_symmetry_about_otherd(arr, n):

    for i in range(n):
        for j in range(n):
            if(arr[i][j] != arr[n-j-1][n-i-1]):
                return 0

    return 1


def check_symmetry_about_midrow(arr, n):

    for i in range(n):
        for j in range(n):
            if(arr[i][j] != arr[n-i-1][j]):
                return 0

    return 1


def check_symmetry_about_midcol(arr, n):

    for i in range(n):
        for j in range(n):
            if(arr[i][j] != arr[i][n-j-1]):
                return 0

    return 1


def count_moves(arr, n):

    count = 0
    for i in range(n):
        for j in range(n):
            if(arr[i][j] != -1):
                count = count + 1

    return count


def possibleMoves(arr,n):

    moves  = []
    maind = 0; otherd = 0; midrow = 0; midcol = 0

    # Removing sub-trees which have a similar move
    if(check_symmetry_about_maind(arr, n)):
        maind = 1

    if(check_symmetry_about_midrow(arr, n)):
        midrow = 1

    if(check_symmetry_about_midcol(arr, n)):
        midcol = 1

    row_lim = n
    if(midrow):
        row_lim = math.ceil(n/2)

    col_lim = n
    if(midcol):
        col_lim = math.ceil(n/2)

    for i in range(row_lim):

        col_start = 0
        if(maind):
            col_start = i

        for j in range(col_start, col_lim):
            if(arr[i][j] == -1):
                moves.append((i,j))

    return moves
