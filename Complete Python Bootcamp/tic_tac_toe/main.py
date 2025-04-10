GAME_RUNNING : bool = True
counter : int = 0

def print_board() -> None:
    """"
    Function print_board is used for printing the playing board.
    """
    global board
    for row in range(1, 4):
        print(f"{board[f'{row},1'] or ' '} | {board[f'{row},2'] or ' '} | {board[f'{row},3'] or ' '}")
        if row < 3:
            print("---------")


def move_checker() -> None:
    """"
    Move checker function is used for populating the playing board with either X or O.
    We use the global counter which tells us which player (X, O) is answering the console query.
    We use recursion when the input is incorrect.
    """
    global counter
    global move
    if move in board and board[move] is None:
        if counter % 2 == 0:
            board[move] = 'O'
        else:
            board[move] = 'X'
        counter += 1
    else:
        if move not in board:
            print('Invalid move. Please enter a valid position.')
            move = get_move()
            move_checker()
        else:
            print('Cell is occupied. Please choose another.')
            move = get_move()
            move_checker()

def check_winner(board) -> bool:
    """"
    Function check_winner is used for checking if we have a winning combination on the board.
    """
    # Check rows
    if board['1,1'] == board['1,2'] == board['1,3'] and board['1,1'] is not None:
        return True
    elif board['2,1'] == board['2,2'] == board['2,3'] and board['2,1'] is not None:
        return True
    elif board['3,1'] == board['3,2'] == board['3,3'] and board['3,1'] is not None:
        return True

    # Check columns
    elif board['1,1'] == board['2,1'] == board['3,1'] and board['1,1'] is not None:
        return True
    elif board['1,2'] == board['2,2'] == board['3,2'] and board['1,2'] is not None:
        return True
    elif board['1,3'] == board['2,3'] == board['3,3'] and board['1,3'] is not None:
        return True

    # Check diagonals
    elif board['1,1'] == board['2,2'] == board['3,3'] and board['1,1'] is not None:
        return True
    elif board['3,1'] == board['2,2'] == board['1,3'] and board['3,1'] is not None:
        return True

    return False


def get_move() -> str|None:
    """""
    Get Move function is used for getting the right player for answering the console query.
    We use the global counter.
    """
    global counter
    if counter % 2 == 0:
        return input("O enters a move: ")
    elif counter % 2 == 1 or counter == 1:
        return input("X enters a move: ")


board = {
    '1,1': None, '1,2': None, '1,3': None,
    '2,1': None, '2,2': None, '2,3': None,
    '3,1': None, '3,2': None, '3,3': None
}


while GAME_RUNNING:

    move = get_move()

    move_checker()

    print_board()

    if check_winner(board):
        print(f"{'X' if counter % 2 == 0 else 'O'} wins!")
        GAME_RUNNING = False

    elif counter == 9:
        print("It's a draw!")
        GAME_RUNNING = False
