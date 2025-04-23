GAME_RUNNING: bool = True
counter: int = 0
board = {
    "1,1": None,
    "1,2": None,
    "1,3": None,
    "2,1": None,
    "2,2": None,
    "2,3": None,
    "3,1": None,
    "3,2": None,
    "3,3": None,
}


def print_board(board) -> str:
    """
    Returns the current state of the playing board as a string.

    The board is represented as a dictionary with keys for each cell (e.g., '1,1').
    For each row (1 to 3), the function returns the cell values separated by vertical bars.
    Empty cells (with a value of None) are represented by a blank space.

    Returns:
       str: The current board state as a string.
    """
    board_string = ""
    for row in range(1, 4):
        board_string += f"{board[f'{row},1'] or ' '} | {board[f'{row},2'] or ' '} | {board[f'{row},3'] or ' '}\n"
        if row < 3:
            board_string += "---------\n"
    return board_string.strip()


def move_checker(move: str, board: dict) -> str | None:
    """
    Processes the current move and updates the board with either 'X' or 'O'.

    The function checks whether the global move (a string representing the chosen cell)
    is valid (i.e., it exists in the board and the cell is empty). Based on the global counter,
    it assigns 'O' when the counter is even and 'X' when the counter is odd.

    If the move is invalid or the cell is already occupied, it prompts the user for a new move
    until a valid move is made.

    Returns:
        A message indicating whether the move was valid or not.
    """
    global counter
    while True:
        if move in board and board[move] is None:
            # Valid move
            if counter % 2 == 0:
                board[move] = "O"
            else:
                board[move] = "X"
            counter += 1
            return print_board(board)
        else:
            # Invalid move (either outside the board or cell is occupied)
            if move not in board:
                return "Invalid move. Please enter a valid position."
            else:
                return "Cell is occupied. Please choose another."


def check_winner(board: dict) -> bool | str | None:
    """
    Checks the board for a winning combination.

    The function examines rows, columns, and diagonals to determine whether there are
    three identical non-None values aligned. If such a combination is found, it indicates a win.

    Parameters:
        board (dict): A dictionary representing the playing board with keys like '1,1', '1,2', etc.,
                      and values that are either 'X', 'O', or None.

    Returns:
        bool: True if a winning combination is present, otherwise False.
    """
    global GAME_RUNNING

    # Check rows
    if board["1,1"] == board["1,2"] == board["1,3"] and board["1,1"] is not None:
        if counter != 9:
            GAME_RUNNING = False
            return f"{'X' if counter % 2 == 0 else 'O'} wins!"

    elif board["2,1"] == board["2,2"] == board["2,3"] and board["2,1"] is not None:
        if counter != 9:
            GAME_RUNNING = False
            return f"{'X' if counter % 2 == 0 else 'O'} wins!"

    elif board["3,1"] == board["3,2"] == board["3,3"] and board["3,1"] is not None:
        if counter != 9:
            GAME_RUNNING = False
            return f"{'X' if counter % 2 == 0 else 'O'} wins!"

    # Check columns
    elif board["1,1"] == board["2,1"] == board["3,1"] and board["1,1"] is not None:
        if counter != 9:
            GAME_RUNNING = False
            return f"{'X' if counter % 2 == 0 else 'O'} wins!"

    elif board["1,2"] == board["2,2"] == board["3,2"] and board["1,2"] is not None:
        if counter != 9:
            GAME_RUNNING = False
            return f"{'X' if counter % 2 == 0 else 'O'} wins!"

    elif board["1,3"] == board["2,3"] == board["3,3"] and board["1,3"] is not None:
        if counter != 9:
            GAME_RUNNING = False
            return f"{'X' if counter % 2 == 0 else 'O'} wins!"

    # Check diagonals
    elif board["1,1"] == board["2,2"] == board["3,3"] and board["1,1"] is not None:
        if counter != 9:
            GAME_RUNNING = False
            return f"{'X' if counter % 2 == 0 else 'O'} wins!"

    elif board["3,1"] == board["2,2"] == board["1,3"] and board["3,1"] is not None:
        if counter != 9:
            GAME_RUNNING = False
            return f"{'X' if counter % 2 == 0 else 'O'} wins!"

    if counter == 9:
        GAME_RUNNING = False
        return "It's a draw!"

    return ""


def get_move() -> str | None:
    """
    Prompts the current player to enter their move based on whose turn it is.

    The global counter is used to determine which player should make the move.
    If the counter is even, player 'O' is prompted; otherwise, player 'X' is prompted.

    Returns:
        str: The move input provided by the current player.
    """
    global counter
    if counter % 2 == 0:
        return input("O enters a move: ")
    else:
        return input("X enters a move: ")


if __name__ == "__main__":
    while GAME_RUNNING:
        move = get_move()
        result = move_checker(move, board)
        print(result)  # Print the result message of each move
        print(check_winner(board))
