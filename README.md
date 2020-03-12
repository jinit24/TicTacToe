# TicTacToe
Tic Tac Toe game that never lets you win as first player.
Uses minimax algorithm to generate moves and python curses to enter data

Software Required:
Python3

Libraries reuqired:
curses

Input:
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                             |                             |                             │
│                             |                             |                             │
│                             |                             |                             │
│             7               |             8               |                9            │
│                             |                             |                             │
│                             |                             |                             │
│                             |                             |                             │
│-----------------------------------------------------------------------------------------│
│                             |                             |                             │
│                             |                             |                             │
│                             |                             |                             │
│             4               |             5               |               6             │
│                             |                             |                             │
│                             |                             |                             │
│                             |                             |                             │
│-----------------------------------------------------------------------------------------│
│                             |                             |                             │
│                             |                             |                             │
│             1               |             2               |                3            │
│                             |                             |                             │
│                             |                             |                             │
│                             |                             |                             │
└─────────────────────────────────────────────────────────────────────────────────────────┘

Use the following numbers to enter into that specific location:


Sample Game:
1.User enters 7
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                             |                             |                             │
│                             |                             |                             │
│                             |                             |                             │
│              X              |                             |                             │
│                             |                             |                             │
│                             |                             |                             │
│                             |                             |                             │
│-----------------------------------------------------------------------------------------│
│                             |                             |                             │
│                             |                             |                             │
│                             |                             |                             │
│                             |              O              |                             │
│                             |                             |                             │
│                             |                             |                             │
│                             |                             |                             │
│-----------------------------------------------------------------------------------------│
│                             |                             |                             │
│                             |                             |                             │
│                             |                             |                             │
│                             |                             |                             │
│                             |                             |                             │
│                             |                             |                             │
└─────────────────────────────────────────────────────────────────────────────────────────┘
2. User enters 4
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                             |                             |                             │
│                             |                             |                             │
│                             |                             |                             │
│              X              |                             |                             │
│                             |                             |                             │
│                             |                             |                             │
│                             |                             |                             │
│-----------------------------------------------------------------------------------------│
│                             |                             |                             │
│                             |                             |                             │
│                             |                             |                             │
│              X              |              O              |                             │
│                             |                             |                             │
│                             |                             |                             │
│                             |                             |                             │
│-----------------------------------------------------------------------------------------│
│                             |                             |                             │
│                             |                             |                             │
│                             |                             |                             │
│              O              |                             |                             │
│                             |                             |                             │
│                             |                             |                             │
└─────────────────────────────────────────────────────────────────────────────────────────┘
3. User enters 9
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                             |                             |                             │
│                             |                             |                             │
│                             |                             |                             │
│              X              |              O              |              X              │
│                             |                             |                             │
│                             |                             |                             │
│                             |                             |                             │
│-----------------------------------------------------------------------------------------│
│                             |                             |                             │
│                             |                             |                             │
│                             |                             |                             │
│              X              |              O              |                             │
│                             |                             |                             │
│                             |                             |                             │
│                             |                             |                             │
│-----------------------------------------------------------------------------------------│
│                             |                             |                             │
│                             |                             |                             │
│                             |                             |                             │
│              O              |                             |                             │
│                             |                             |                             │
│                             |                             |                             │
└─────────────────────────────────────────────────────────────────────────────────────────┘
4. User enters 3
You lose!



