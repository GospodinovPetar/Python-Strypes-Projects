from unittest.mock import patch
import pytest
from computer import Computer
from player import Player
from main import handle_game_round
from main import (
    count_points,
    reset_points,
    game_outcome,
    deal_card,
    player_input,
    get_valid_input,
    CARD_A,
    CARD_2,
    CARD_3,
    CARD_6,
    CARD_7,
    CARD_10,
    CARD_K,
    CARD_Q,
    game,
)

# ========================
# Tests for count_points()
# ========================


def test_counting_points_with_ace_as_11():
    """
    Test that counting points with an Ace (as 11) works correctly.

    This test verifies that an Ace is counted as 11 when it is part of a hand
    (in this case, combined with a '3') to give a total of 14 points.
    """
    hand = [CARD_A, CARD_3]
    result = count_points(hand)
    assert result == 14  # 11 (Ace) + 3 = 14


def test_counting_points_with_ace_and_other_cards():
    """
    Test that counting points with an Ace and other cards works correctly.

    This test verifies that an Ace is counted as 11 when combined with other
    cards, resulting in a correct total hand value (in this case, 14).
    """
    hand = [CARD_6, CARD_7, CARD_A]
    result = count_points(hand)
    assert result == 14  # 6 + 7 + 11 (Ace) = 14


# ==========================
# Tests for reset_points()
# ==========================


def test_reset_points():
    """
    Test that the reset_points function correctly resets the points of both the player and the computer.

    This test ensures that after resetting the points, both the computer's and player's points
    are set to 0, and their hands are cleared.
    """
    computer = Computer()
    player = Player(100)
    computer.points = 123
    player.points = 124
    reset_points(computer, player)
    assert computer.points == 0
    assert player.points == 0


# ================================
# Tests for game_outcome() logic
# ================================


def test_game_outcome_player_wins_with_blackjack():
    """
    Test that the player wins when they hit a Blackjack (21 points) while the computer has less than 21.

    This test verifies that when the player reaches 21 points and the computer has a lower point total,
    the player wins and their money is updated accordingly.
    """
    player = Player(100)
    computer = Computer()
    player.points = 21
    computer.points = 19
    result = game_outcome(10, computer, player)
    assert result == f"Player wins! Points equal 21. Players money: {100 + (10 * 3)}"


def test_game_outcome_computer_wins_with_blackjack():
    """
    Test that the computer wins when they hit a Blackjack (21 points) while the player has less than 21.

    This test ensures that when the computer reaches 21 points and the player has a lower point total,
    the computer wins and the player's money is updated accordingly.
    """
    player = Player(100)
    computer = Computer()
    player.points = 20
    computer.points = 21
    result = game_outcome(10, computer, player)
    assert result == f"Computer wins! Points equal 21. Players money: {100 - 10}"


def test_game_outcome_computer_busts():
    """
    Test that the computer loses when they bust (points exceed 21).

    This test ensures that when the computer's points exceed 21, they lose, and the player wins money.
    """
    player = Player(100)
    computer = Computer()
    player.points = 20
    computer.points = 23
    result = game_outcome(10, computer, player)
    assert (
        result == f"Computer loses! Points exceeded 21. Players money: {100 + (10 * 2)}"
    )


def test_game_outcome_player_busts():
    """
    Test that the player loses when they bust (points exceed 21).

    This test ensures that when the player's points exceed 21, they lose, and their money is reduced.
    """
    player = Player(100)
    computer = Computer()
    player.points = 23
    computer.points = 19
    result = game_outcome(10, computer, player)
    assert result == f"Player loses! Points exceeded 21. Players money: {100 - 10}"


def test_game_outcome_its_a_draw():
    """
    Test that the game results in a draw when both the player and computer bust.

    This test ensures that if both the player and the computer bust, the outcome is a draw.
    """
    player = Player(100)
    computer = Computer()
    player.points = 23
    computer.points = 24
    result = game_outcome(10, computer, player)
    assert result == "It's a draw"


# ===========================
# Tests for deal_card() logic
# ===========================


def test_deal_card_with_mocked_card():
    """
    Test that the deal_card function correctly deals a card and updates the player's points.

    This test ensures that when a card is dealt to the player, their hand is updated, and the correct points are returned.
    It mocks the random card choice to simulate specific scenarios.
    """
    player = Player(100)
    with patch("random.choice", return_value=CARD_A):
        result = deal_card(player, "Player")
        assert result == "Player got A! Points: 11"

    with patch("random.choice", return_value=CARD_10):
        result = deal_card(player, "Player")
        assert result == "Player got 10! Points: 21"

    with patch("random.choice", return_value=CARD_A):
        player.hand = [CARD_K, CARD_Q]
        result = deal_card(player, "Player")
        assert result == "Player got A! Points: 21"


# ===========================
# Tests for game continuation
# ===========================


def test_game_continues():
    """
    Test that the game continues when neither the player nor the computer wins or busts.

    This test verifies that if the points of both the player and computer are below 21,
    the game continues and no winner is declared.
    """
    player = Player(100)
    computer = Computer()
    player.points = 18
    computer.points = 19
    result = game_outcome(10, computer, player)
    assert result == "Game continues.."


# ========================
# Edge Case and Invalid Inputs
# ========================


def test_game_outcome_player_with_negative_money():
    """
    Test that the game correctly handles a player with negative money.

    This test ensures that the game will prevent a player with negative money from playing.
    """
    player = Player(-10)
    computer = Computer()
    player.points = 20
    computer.points = 19
    result = game_outcome(10, computer, player)
    assert result == "Player doesn't have enough money to play!"


def test_deal_card_after_busting():
    """
    Test that the deal_card function prevents further actions after the player busts.

    This test ensures that after a player busts (points exceed 21), no further cards are dealt, and the result reflects the bust.
    """
    player = Player(100)
    player.hand = [CARD_K, CARD_Q, CARD_2]
    result = deal_card(player, "Player")
    player.points = count_points(player.hand)
    assert result == "Player busts! Points exceeded 21."
    assert player.points == 22


# ===========================
# Tests for player_input logic
# ===========================

@patch("builtins.input", side_effect=["-34", "0", "100", "10"])
def test_player_input_invalid_total_amount(mock_input: patch,):
    """
    Test that the player input function handles invalid total amounts for the player.

    This test verifies that the function will keep prompting the player until a valid total amount is entered.
    """
    total_amount, betting_amount = player_input()
    assert total_amount == 100
    assert betting_amount == 10

@patch("builtins.input", side_effect=["100", "0", "10"])
def test_player_input_invalid_betting_amount(mock_input: patch,):
    """
    Test that the player input function handles invalid betting amounts.

    This test ensures that the function keeps prompting the player until a valid betting amount is entered.
    """

    total_amount, betting_amount = player_input()
    assert total_amount == 100
    assert betting_amount == 10

@patch("builtins.input", side_effect=["100", "10"])
def test_player_input_valid_inputs(mock_input: patch, ):
    """
    Test that the player input function correctly accepts valid inputs.

    This test verifies that the function accepts valid inputs for total and betting amounts.
    """
    total_amount, betting_amount = player_input()
    assert total_amount == 100
    assert betting_amount == 10

@patch("builtins.input", side_effect=["L", "L", "10"])
def test_invalid_input_key_instead_of_int(mock_input: patch):
    """
    Test that the player input function correctly handles invalid input types (e.g., non-numeric values).

    This test ensures that the function will reject non-numeric input and prompt the player again.
    """
    result = get_valid_input("Enter a positive number: ")
    assert result == 10


def test_betting_amount_higher_than_total_amount():
    """
    Test that the game correctly handles the scenario where the betting amount exceeds the player's total amount.

    This test ensures that the game will not allow a bet that is larger than the player's available funds.
    """
    player = Player(100)
    computer = Computer()
    result = game_outcome(203, computer, player)
    assert result == "Not enough money to make the bet!"


def test_betting_amount_lower_than_zero():
    """
    Test that the game correctly handles the scenario where the betting amount is less than or equal to zero.

    This test ensures that the game rejects invalid betting amounts (negative or zero) and prompts for a valid input.
    """
    player = Player(100)
    computer = Computer()
    result = game_outcome(-10, computer, player)
    assert result == "Invalid amount. Please enter a positive number."


# ========================
# Tests for invalid card input
# ========================


def test_count_points_invalid_card():
    """
    Test that the count_points function raises an error for invalid card inputs.

    This test ensures that if an invalid card (not in the deck) is passed to the function, a KeyError is raised.
    """
    with pytest.raises(KeyError):
        count_points(["Z"])


# ========================
# Tests for game()
# ========================

@patch("builtins.input", side_effect=["ne", "nqma kak", "hit", "exit"])
def test_invalid_player_input_stand_hit_exit(mock_input: patch):
    """
    Test that the game correctly handles invalid player input for choosing actions.

    This test ensures that if the player enters invalid input (not "stand", "hit", or "exit"),
    the game prompts the player again for a valid action. Invalid inputs are mocked as 'ne'
    and 'nqma kak' before the valid input 'hit' is provided.
    """
    player = Player(100)
    computer = Computer()
    betting_amount = 10  # Define betting amount
    result = game(player, computer, betting_amount)  # Run the game

    assert result == "GAME OVER"

@patch("builtins.input", side_effect = ["exit"])
def test_game_exit_if_player_says_exit(mock_input: patch):
    """
    Test that the game correctly exits when the player chooses to exit.

    This test ensures that if the player selects 'exit', the game ends and the appropriate message is returned.
    """
    player = Player(100)
    computer = Computer()
    betting_amount = 10  # Define betting amount

    result = game(player, computer, betting_amount)

    assert result == "GAME OVER"

@patch("builtins.input", return_value = ["hit"])
def test_game_busts_after_hit(mock_input: patch):
    """
    Test that the game correctly handles a bust after a player hits.

    This test ensures that if the player hits and their points exceed 21, the game correctly detects the bust.
    """
    player = Player(100)
    computer = Computer()

    # Mock a situation where the player busts after hitting
    player.hand = [CARD_10, CARD_10, CARD_2]  # 22
    computer.hand = [CARD_7, CARD_3]  # 10

    result = deal_card(player, "Player")  # The card will make the player bust

    assert result == "Player busts! Points exceeded 21."

def test_new_game():
    player = Player(100)
    computer = Computer()

    result = handle_game_round('test', player, computer)
    assert result == "New Game!"

# Name                                   Stmts   Miss  Cover
# ----------------------------------------------------------
# projects/blackjack/computer.py             4      0   100%
# projects/blackjack/main.py               122      9    93%
# projects/blackjack/player.py               5      0   100%
# projects/blackjack/test_blackjack.py     149      0   100%
# ----------------------------------------------------------
# TOTAL                                    280      9    97%
