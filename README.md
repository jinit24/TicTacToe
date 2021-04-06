# Tic-Tac-Toe #
Tic Tac Toe game that never lets you win.

## Version 3 Features ##
1. Use of Heuristic for move ordering.
2. Idea of similar states is implemented to reduce search space.
3. Iterative deepening and depth-limited search is implemented using above 2.

## Libraries required ##
curses

## Playing the Game ## 

1. Type the following on the terminal
```
git clone https://github.com/jinit24/TicTacToe
cd TicTacToe
python3 iterative_deepening.py
```
2. Type the size of grid you want to play on then type 1 or 2 to select which player you want to play as.
3. Select using the mouse any sqaure that you want to mark. 

Iterative deepening has a time limit of 1 second for each move. Other implementations don't have a limit on time.

## Files ##
1. algo.py - Contains the heart of the algorithm : alpha-beta pruning and the naive version.
2. checks_counts.py - Contains the checking of board and generation of possible moves. (Similar states idea implemented in this)
3. UI_elements.py - Contains the making of the board using curses and variable initialization for the same.
4. Iterative_deepening.py and depth_limited_search.py - Contain the final move generation and adding time and depth limits. 

## Alternate C++ File ##
### Now in Intermediate Ideas ###
1. Here you can provide a testcase. The code will return the best move to be played. Example of a testcase :
```
X  
___  
___  
_XO  
```
Where the X on top is whose turn is to be played.
