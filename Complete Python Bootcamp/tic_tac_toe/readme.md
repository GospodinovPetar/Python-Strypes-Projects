# Milestone Project I: <br> Tic-Tac-Toe Game: Player vs Player

This Python script implements a console-based Tic-Tac-Toe game where two players (X and O) take turns to make their moves on a 3x3 board. The game continues until either one of the players wins or the game ends in a draw.

## Requirements

There are no external libraries required for this script, so no additional installation is needed. It is a simple Python script that runs directly in the terminal or command line.

## Script Functionality

### `print_board()`
This function prints the current state of the Tic-Tac-Toe board to the console. The board is displayed in a 3x3 grid format with 'X' and 'O' representing the players' moves.

### `move_checker()`
This function checks if the player's move is valid. It ensures that:
- The move corresponds to a valid position on the board.
- The cell is not already occupied.
The function uses recursion to prompt the player again if the move is invalid.

### `check_winner(board)`
This function checks if there is a winner on the board. It evaluates all possible winning conditions (rows, columns, and diagonals) and returns `True` if a player has won.

### `get_move()`
This function prompts the current player to enter their move (either 'X' or 'O'). It alternates between players by checking the global counter, which tracks the number of moves made.

## Game Flow

1. The game starts with an empty 3x3 board, and the players alternate between 'X' and 'O'.
2. The `get_move()` function asks the current player to enter their move in the format of row and column (e.g., "1,1" for the top-left corner).
3. The `move_checker()` function ensures the move is valid (i.e., the cell is unoccupied and within the board).
4. After each valid move, the board is printed
