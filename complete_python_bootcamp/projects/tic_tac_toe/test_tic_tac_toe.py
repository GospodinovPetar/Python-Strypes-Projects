from unittest.mock import patch
from main import check_winner, move_checker, get_move, board


def test_check_winner_on_first_row():
    # Simulate a winning condition where the first row has "X"
    board = {
        "1,1": "X",
        "1,2": "X",
        "1,3": "X",  # Winning row
        "2,1": "O",
        "2,2": "O",
        "2,3": None,
        "3,1": None,
        "3,2": None,
        "3,3": None,
    }

    result = check_winner(board)
    assert result == "X wins!"


def test_check_winner_on_first_column():
    # Simulate a winning condition where the first column has "X"
    board = {
        "1,1": "X",
        "2,1": "X",
        "3,1": "X",  # Winning column
        "1,2": "O",
        "2,2": "O",
        "3,2": None,
        "1,3": None,
        "2,3": None,
        "3,3": None,
    }

    result = check_winner(board)
    assert result == "X wins!"


def test_check_winner_on_diagonal():
    # Simulate a winning condition where the diagonal has "X"
    board = {
        "1,1": "X",
        "1,2": "O",
        "1,3": None,
        "2,1": None,
        "2,2": "X",
        "2,3": "O",
        "3,1": None,
        "3,2": None,
        "3,3": "X",  # Third row (winning diagonal)
    }

    result = check_winner(board)
    assert result == "X wins!", f"Expected 'X wins!', but got {result}"


@patch("main.counter", 9)  # Patching the counter value to simulate a draw
def test_draw():
    result = check_winner(board)
    assert result == "It's a draw!"


@patch("builtins.input", side_effect=["4,1", "5,3"])  # Mock input with invalid inputs
def test_invalid_move(mock_input: patch):
    """Test for invalid moves."""
    board = {
        "1,1": "O",
        "1,2": None,
        "1,3": None,
        "2,1": None,
        "2,2": None,
        "2,3": None,
        "3,1": None,
        "3,2": None,
        "3,3": None,
    }
    # First invalid move (4,1)
    result = move_checker(get_move(), board)
    assert result == "Invalid move. Please enter a valid position."

    # Second invalid move (5,3)
    result = move_checker(get_move(), board)
    assert result == "Invalid move. Please enter a valid position."


def test_occupied_cell():
    board = {
        "1,1": "O",
        "1,2": None,
        "1,3": None,
        "2,1": None,
        "2,2": None,
        "2,3": None,
        "3,1": None,
        "3,2": None,
        "3,3": None,
    }
    result = move_checker("1,1", board)
    assert result == "Cell is occupied. Please choose another."


@patch("builtins.input", return_value="1,1")
def test_get_move_o_turn(mock_input: patch):
    # Simulate the counter being even (player 'O's turn)
    global counter
    counter = 0  # 'O' is expected to go first

    result = get_move()

    # Assert that the correct prompt is shown for 'O' and the correct move is returned
    assert result == "1,1"  # TODO: works but I don't know why


@patch("builtins.input", return_value="2,2")
def test_get_move_x_turn(mock_input: patch):
    # Simulate the counter being odd (player 'X's turn)
    global counter
    counter = 1  # 'X' is expected to go second

    result = get_move()

    # Assert that the correct prompt is shown for 'X' and the correct move is returned
    assert result == "2,2"  # TODO: works but I don't know why


@patch("builtins.input", return_value="1,1")
def test_player_output_on_board_O_turn(mock_input: patch):
    """
    Tests a valid move for player 'O' (when the counter is even).
    Simulates player 'O' making a valid move and checks the updated board.
    """

    # The board before the move (empty)
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

    result = move_checker("1,1", board)

    # Expected updated board after player 'O' makes a move at "1,1"
    expected_board = {
        "1,1": "O",
        "1,2": None,
        "1,3": None,
        "2,1": None,
        "2,2": None,
        "2,3": None,
        "3,1": None,
        "3,2": None,
        "3,3": None,
    }

    assert board == expected_board

    expected_printed_output = "O |   |  \n---------\n  |   |  \n---------\n  |   |"

    captured = result.strip()
    assert captured == expected_printed_output


@patch("main.counter", 1)
def test_player_output_on_board_X_turn():
    """
    Tests a valid move for player 'O' (when the counter is even).
    Simulates player 'O' making a valid move and checks the updated board.
    """

    # The board before the move (empty)
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

    # Mock the input to simulate player 'X' choosing "1,1"
    with patch("builtins.input", return_value="1,1"):
        move_checker("1,1", board)

    # Expected updated board after player 'X' makes a move at "1,1"
    expected_board = {
        "1,1": "X",
        "1,2": None,
        "1,3": None,
        "2,1": None,
        "2,2": None,
        "2,3": None,
        "3,1": None,
        "3,2": None,
        "3,3": None,
    }

    # Check if the board is updated correctly
    assert board == expected_board


# Name                  Stmts   Miss  Cover   Missing
# ---------------------------------------------------
# main.py                  70     24    66%   79-81, 84-86, 95-97, 100-102, 111-113, 119, 135-137, 153-157
# test_tic_tac_toe.py      56      0   100%
# ---------------------------------------------------
# TOTAL                   126     24    81%
