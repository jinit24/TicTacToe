# Tic-Tac-Toe #
Tic Tac Toe game that never lets you win.

## Monte Carlo Tree Search ##
We are trying to find the best move for a given state. MCTS builds a tree through iterations, selecting and expanding nodes. 
At each leaf node simulates a game and backpropagates the information.  

It has 4 basic steps :
1. Selection 
2. Expansion
3. Simulation
4. Backpropagation

## Playing the Game ## 

1. Type the following on the terminal
```
git clone -b 'MCTS' https://github.com/jinit24/TicTacToe
cd TicTacToe
python3 monte.py
```
2. Type 1 or 2 to select which player you want to play as.
3. Select using the mouse any sqaure that you want to mark. 

## Files ##
1. MCTS_node.py - contains the node details and accompanying functions for it. (Important part is here)  
2. monte.py - final call of search and playing the game.

## References ##
For theory and idea - <a href = "https://medium.com/@quasimik/monte-carlo-tree-search-applied-to-letterpress-34f41c86e238">Explanation </a>  
For code- <a href = "https://ai-boson.github.io/mcts/">https://ai-boson.github.io/mcts/</a>
