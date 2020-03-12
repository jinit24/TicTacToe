import curses
import time
# Draws the 3 x 3 grid on the terminal
def createGrid(h,w):
    for i in range(h):
        win.addstr(i,int(2*w/3),'|')
        win.addstr(i,int(w/3),'|')

    for j in range(w):
        win.addstr(int(h/3),j,'-')
        win.addstr(int(2*h/3),j,'-')

# Using the keyboard as input 
def printVal(next_key):
    global turn,arr
    if(turn%2==0):
        s = 'X'
    else:
        s = 'O'
    if (next_key == 55):
        win.addstr(int(h/6),int(w/6),s)
        arr[0][0]=turn%2

    elif (next_key == 56):
        win.addstr(int(h/6),int(w/2),s)
        arr[0][1]=turn%2

    elif (next_key == 57):
        win.addstr(int(h/6),int(5*w/6),s)
        arr[0][2]=turn%2

    elif (next_key == 52):
        win.addstr(int(h/2),int(w/6),s)
        arr[1][0]=turn%2

    elif (next_key == 53):
        win.addstr(int(h/2),int(w/2),s)
        arr[1][1]=turn%2

    elif (next_key == 54):
        win.addstr(int(h/2),int(5*w/6),s)
        arr[1][2]=turn%2

    elif (next_key == 49):
        win.addstr(int(5*h/6),int(w/6),s)
        arr[2][0]=turn%2

    elif (next_key == 50):
        win.addstr(int(5*h/6),int(w/2),s)
        arr[2][1]=turn%2

    elif (next_key == 51):
        win.addstr(int(5*h/6),int(5*w/6),s)
        arr[2][2]=turn%2
    turn = turn + 1

def printX(pair):
    x,y = pair
    if(x==0 and y==0):
        printVal(55)
    elif(x==0 and y==1):
        printVal(56)
    elif(x==0 and y==2):
        printVal(57)
    elif(x==1 and y==0):
        printVal(52)
    elif(x==1 and y==1):
        printVal(53)
    elif(x==1 and y==2):
        printVal(54)
    elif(x==2 and y==0):
        printVal(49)
    elif(x==2 and y==1):
        printVal(50)
    elif(x==2 and y==2):
        printVal(51)

def check():
    for i in range(3):
        # Checking if Rows are marked
        if((arr[i][0]!=-1) and (arr[i][0]==arr[i][1]) and (arr[i][1]==arr[i][2])):
            if(arr[i][0]==0):
                return [True,0]
            else:
                return [True,1]

        # Checking if Columns are marked
        if((arr[0][i]!=-1) and (arr[0][i]==arr[1][i]) and (arr[0][i]==arr[2][i])):
            if(arr[0][i]==0):
                return [True,0]
            else:
                return [True,1]

    # Checking if diagonals are marked
    if(arr[0][0]!=-1 and arr[0][0]==arr[1][1] and arr[1][1]==arr[2][2]):
        if(arr[0][0]==0):
            return [True,0]
        else:
            return [True,1]

    if(arr[2][0]!=-1 and arr[2][0]==arr[1][1] and arr[1][1]==arr[0][2]):
        if(arr[2][0]==0):
            return [True,0]
        else:
            return [True,1]

    # If all are marked, hence draw
    test=0
    for i in range(3):
        for j in range(3):
            if(arr[i][j]==-1):
                test=1

    if(test==0):
        return [True,-1]

    return [False,1]

def possibleMoves(arr):
    moves  = []
    for i in range(3):
        for j in range(3):
            if(arr[i][j]==-1):
                moves.append((i,j))
    return moves


def Comp(moves,cost):
    max_U = [cost for i in range(len(moves))]
    for i in range(len(moves)):
        x,y = moves[i]
        initial = arr[x][y]
        arr[x][y] = 1
        c,flag = check()
        if(c and flag==1):
            max_U[i] = max_U[i] + 20
        elif((c and flag!=-1) or not c):
            max_U[i]  = Hum(possibleMoves(arr),max_U[i]-1)
        else:
            max_U[i]  = max_U[i]

        arr[x][y] = initial

    max_i = 0
    max_e = -100000
    for i in range(len(moves)):
        if(max_U[i]>max_e):
            max_i = i
            max_e = max_U[i]

    global pair,Um
    if(len(max_U)>0):
        pair = moves[max_i]
        Um = max_U
        return max(max_U)

def Hum(moves,cost):
    min_U = [cost for i in range(len(moves))]
    for i in range(len(moves)):
        x,y = moves[i]
        initial = arr[x][y]
        arr[x][y] = 0
        c,flag = check()
        if(c and flag==0):
            min_U[i] = min_U[i]-20
        elif((c and flag!=-1) or not c):
            if(len(possibleMoves(arr))>0):
                min_U[i]  = Comp(possibleMoves(arr),min_U[i]-1)
        else:
            min_U[i]  = min_U[i]
        arr[x][y] = initial

    min_i = 0
    min_e = 0
    for i in range(len(moves)):
        if(min_U[i]<min_e):
            min_i = i
            min_e = min_U[i]
    return min(min_U)

###initialize screen
sc = curses.initscr()
h, w = sc.getmaxyx()
win = curses.newwin(h, w, 0, 0)
win.keypad(1)
curses.curs_set(0)
arr = [[-1 for i in range(3)] for j in range(3)]
cost =0
pair = (-1,-1)
Um = []
createGrid(h,w)
turn = 0
flag = -1

###Taking input from user through keyboard
while True:
    win.border(0)
    win.timeout(100)
    curses.noecho()

    next_key = win.getch()
    if(next_key != -1):
        if(next_key==27):
            break
        [c,flag] = check()
        if(c):
            break
        printVal(next_key)
        Comp(possibleMoves(arr),cost)
        printX(pair)
        [c,flag] = check()
        if(c):
            break

# Checking conditions for winning or losing or draw
if(flag==0):
    s = "You Won!"
elif(flag==1):
    s = "You Lost!"
elif(flag==-1):
    s = "Draw!"

# Outputting Result
sc.addstr(int(h/2),int(w/2),s)
sc.refresh()
time.sleep(2)
curses.endwin()
print(arr)
print(possibleMoves(arr))
