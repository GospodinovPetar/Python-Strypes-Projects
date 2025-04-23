from unittest.mock import patch
from main import check_winner, move_checker, get_move, board


def test_check_winner_first_row_win():
    """
    Test for a winner on the first row.
    Simulates the first row being filled with "X" and asserts that "X wins!" is returned.
    """
    board = {
        "1,1": "X",
        "1,2": "X",
        "1,3": "X",
        "2,1": None,
        "2,2": None,
        "2,3": None,
        "3,1": None,
        "3,2": None,
        "3,3": None,
    }
    result = check_winner(board)
    assert result == "X wins!"


@patch("main.counter", 5)
def test_check_winner_second_row_win():
    """
    Test for a winner on the second row.
    Simulates the second row being filled with "O" and asserts that "O wins!" is returned.
    """
    board = {
        "1,1": None,
        "1,2": None,
        "1,3": None,
        "2,1": "O",
        "2,2": "O",
        "2,3": "O",
        "3,1": None,
        "3,2": None,
        "3,3": None,
    }

    result = check_winner(board)
    assert result == "O wins!", f"Expected 'O wins!', but got {result}"


def test_check_winner_third_row_win():
    """
    Test for a winner on the third row.
    Simulates the third row being filled with "X" and asserts that "X wins!" is returned.
    """
    board = {
        "1,1": None,
        "1,2": None,
        "1,3": None,
        "2,1": None,
        "2,2": None,
        "2,3": None,
        "3,1": "X",
        "3,2": "X",
        "3,3": "X",
    }
    result = check_winner(board)
    assert result == "X wins!"


def test_check_winner_first_column_win():
    """
    Test for a winner in the first column.
    Simulates the first column being filled with "X" and asserts that "X wins!" is returned.
    """
    board = {
        "1,1": "X",
        "2,1": "X",
        "3,1": "X",
        "1,2": None,
        "2,2": None,
        "3,2": None,
        "1,3": None,
        "2,3": None,
        "3,3": None,
    }
    result = check_winner(board)
    assert result == "X wins!"


def test_check_winner_second_column_win():
    """
    Test for a winner in the second column.
    Simulates the second column being filled with "X" and asserts that "X wins!" is returned.
    """
    board = {
        "1,1": None,
        "2,1": None,
        "3,1": None,
        "1,2": "X",
        "2,2": "X",
        "3,2": "X",
        "1,3": None,
        "2,3": None,
        "3,3": None,
    }
    result = check_winner(board)
    assert result == "X wins!"


def test_check_winner_third_column_win():
    """
    Test for a winner in the third column.
    Simulates the third column being filled with "X" and asserts that "X wins!" is returned.
    """
    board = {
        "1,1": None,
        "2,1": None,
        "3,1": None,
        "1,2": None,
        "2,2": None,
        "3,2": None,
        "1,3": "X",
        "2,3": "X",
        "3,3": "X",
    }
    result = check_winner(board)
    assert result == "X wins!"


def test_check_winner_left_diagonal_win():
    """
    Test for a winner on the left diagonal.
    Simulates the left diagonal being filled with "X" and asserts that "X wins!" is returned.
    """
    board = {
        "1,1": "X",
        "1,2": None,
        "1,3": None,
        "2,1": None,
        "2,2": "X",
        "2,3": None,
        "3,1": None,
        "3,2": None,
        "3,3": "X",
    }
    result = check_winner(board)
    assert result == "X wins!"


def test_check_winner_right_diagonal_win():
    """
    Test for a winner on the right diagonal.
    Simulates the right diagonal being filled with "X" and asserts that "X wins!" is returned.
    """
    board = {
        "1,1": None,
        "1,2": None,
        "1,3": "X",
        "2,1": None,
        "2,2": "X",
        "2,3": None,
        "3,1": "X",
        "3,2": None,
        "3,3": None,
    }
    result = check_winner(board)
    assert result == "X wins!"


def test_check_winner_no_winner_game_continues():
    """
    Test for a scenario where the game is ongoing and no winner yet.
    The board is partially filled, and no winner is detected.
    """
    board = {
        "1,1": "X",
        "1,2": "O",
        "1,3": None,
        "2,1": "O",
        "2,2": "X",
        "2,3": None,
        "3,1": None,
        "3,2": None,
        "3,3": None,
    }

    global counter
    counter = 5  # Not all moves have been made

    result = check_winner(board)
    assert result == "", "Expected no winner, but got a result."


@patch("main.counter", 9)
def test_draw():
    """
    Test for a draw condition when all cells are filled and no winner is detected.
    """
    board = {
        "1,1": "X",
        "1,2": "O",
        "1,3": "X",
        "2,1": "O",
        "2,2": "X",
        "2,3": "O",
        "3,1": "X",
        "3,2": "O",
        "3,3": "X",
    }

    result = check_winner(board)
    assert result == "It's a draw!", f"Expected 'It's a draw!', but got {result}"


def test_invalid_move_out_of_bounds():
    """
    Test for invalid moves that are outside the board.
    The function should return a message asking for a valid position.
    """
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

    with patch("builtins.input", side_effect=["4,1", "5,3"]):
        result = move_checker(get_move(), board)
        assert result == "Invalid move. Please enter a valid position."


def test_occupied_cell():
    """
    Test for a move being attempted on an already occupied cell.
    The function should ask the player to choose another cell.
    """
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
    """
    Test for the move input when it is player 'O's turn.
    Simulates the counter being even and asserts that the correct move is returned.
    """
    global counter
    counter = 0  # 'O' is expected to go first

    result = get_move()
    assert result == "1,1"


@patch("builtins.input", return_value="2,2")
def test_get_move_x_turn(mock_input: patch):
    """
    Test for the move input when it is player 'X's turn.
    Simulates the counter being odd and asserts that the correct move is returned.
    """
    global counter
    counter = 1  # 'X' is expected to go second

    result = get_move()
    assert result == "2,2"


@patch("builtins.input", return_value="1,1")
def test_player_output_on_board_o_turn(mock_input: patch):
    """
    Test the board output when player 'O' makes a valid move.
    Simulates player 'O' making a move and checks if the board updates correctly.
    """
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
def test_player_output_on_board_x_turn():
    """
    Test the board output when player 'X' makes a valid move.
    Simulates player 'X' making a move and checks if the board updates correctly.
    """
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
    with patch("builtins.input", return_value="1,1"):
        move_checker("1,1", board)

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
    assert board == expected_board


# Name                  Stmts   Miss  Cover
# -----------------------------------------
# main.py                  68      6    91%
# test_tic_tac_toe.py      80      0   100%
# -----------------------------------------
# TOTAL                   148      6    96%
