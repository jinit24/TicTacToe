import curses, time, UI_elements as UI
from MCTS_node import node
from checks_counts import *

def get_move(turn, n, arr, iters = 1000):

	root = node(arr, turn, depth = 0)
	x = root.best_action(iters).parent_action
	return x

n = 3
arr = [[-1]*n for i in range(n)]
player = int(input("Enter 1 if you want to play as player 1 otherwise enter 2 : "))
[sc, win, h, w ] = UI.initialise_screen(n)
flag = -1
played = 0

if(player == 2):
    played = 1

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

    if(is_game_over(arr)):
        break

    if(played == 1):
        p = get_move(1, n, arr)
        arr[p[0]][p[1]] = 1
        win.addstr(int(((2*p[0] + 1)*h)/(2*n)),int(((2*p[1] + 1)*w)/(2*n)),'0')
        played = 0
        if(check(arr) == 1):
            flag = 0
            break

        if(is_game_over(arr)):
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


# 1 - 'X'
# 0 - 'O'
# root = node(arr, 1, depth = 0)

# for i in range(1,2):
#     start = time.time()
#     x = (root.best_action(1000).parent_action)
#     print(time.time() - start)

#     print("Move made by : ", x, i%2)
#     arr[x[0]][x[1]]= i%2

#     print()
#     for i in range(3):
#         print(arr[i])
#     print()


#     for c in root.children:
#         print("P",c.state,  c.parent_action, c._results, c.n(), len(c._untried_actions))
#         if(c.parent_action == x):
#         	root = c
#         	break
#         # for cc in c.children:
#         #     print(cc.state,  cc.parent_action, cc._results, cc.n(), len(cc._untried_actions))
#         # print()

#     # for child in root.children:
#     #     if(child.parent_action == x):
#     #         root = child
#     #         break


#     if(is_game_over(arr)):
#         break

