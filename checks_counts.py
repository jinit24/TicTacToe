def get_legal_actions( arr):

    moves  = []
    n = len(arr[0])
    for i in range(n):
        for j in range(n):
            if(arr[i][j] == -1):
                moves.append((i,j))

    return moves


def is_game_over(state):

    if(check(state) == -1):
        return False

    return True


def check(arr, n = 3):

    # 1  - Win / Loss
    # 0  - Draw
    # -1 - Game is in progress

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


def imax(seq):

    ansi = 0
    vali = seq[0]
    for i in range(len(seq)):
        if (seq[i] > vali):
            ansi = i
            vali = seq[i]

    return ansi