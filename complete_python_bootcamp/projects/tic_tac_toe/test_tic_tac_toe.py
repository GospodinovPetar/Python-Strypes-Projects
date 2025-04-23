from unittest.mock import patch
from main import check_winner, move_checker, get_move, board


def test_check_winner_on_first_row():
    board["1,1"] = "X"
    board["1,2"] = "X"
    board["1,3"] = "X"
    assert check_winner(board) == "X wins!"


def test_check_winner_on_second_row():
    board["2,1"] = "X"
    board["2,2"] = "X"
    board["2,3"] = "X"
    assert check_winner(board) == "X wins!"


def test_check_winner_on_third_row():
    board["3,1"] = "X"
    board["3,2"] = "X"
    board["3,3"] = "X"
    assert check_winner(board) == "X wins!"


def test_check_winner_on_first_column():
    board["1,1"] = "X"
    board["2,1"] = "X"
    board["3,1"] = "X"
    assert check_winner(board) == "X wins!"


def test_check_winner_on_second_column():
    board["1,2"] = "X"
    board["2,2"] = "X"
    board["3,2"] = "X"
    assert check_winner(board) == "X wins!"


def test_check_winner_on_third_column():
    board["1,3"] = "X"
    board["2,3"] = "X"
    board["3,3"] = "X"
    assert check_winner(board) == "X wins!"


def test_check_winner_on_diagonal():
    board["1,1"] = "X"
    board["2,2"] = "X"
    board["3,3"] = "X"
    assert check_winner(board) == "X wins!"


@patch("main.counter", 9)  # Patching the counter value to simulate a draw
def test_draw():
    result = check_winner(board)
    assert result == "It's a draw!"


@patch("builtins.input", side_effect=["4,1", "5,3"])  # Mock input with invalid inputs
def test_invalid_move(mock_input: patch):
    """Test for invalid moves."""
    # First invalid move (4,1)
    result = move_checker(get_move())
    assert (
        result == "Invalid move. Please enter a valid position."
    )  # Assert the message returned

    # Second invalid move (5,3)
    result = move_checker(get_move())
    assert result == "Invalid move. Please enter a valid position."


# Name                  Stmts   Miss  Cover   Missing
# ---------------------------------------------------
# main.py                  58     35    40%   16-21, 43-48, 54, 78-100, 110, 126-128, 144-148
# test_tic_tac_toe.py      47      0   100%
# ---------------------------------------------------
# TOTAL                   105     35    67%
