import pytest
from computer import Computer
from player import Player
from unittest.mock import patch
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
    hand = [CARD_A, CARD_3]
    result = count_points(hand)
    assert result == 14  # 11 (Ace) + 3 = 14


def test_counting_points_with_ace_and_other_cards():
    hand = [CARD_6, CARD_7, CARD_A]
    result = count_points(hand)
    assert result == 14  # 6 + 7 + 11 (Ace) = 14


# ==========================
# Tests for reset_points()
# ==========================


def test_reset_points():
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
    player = Player(100)
    computer = Computer()
    player.points = 21
    computer.points = 19
    result = game_outcome(10, computer, player)
    assert result == f"Player wins! Points equal 21. Players money: {100 + (10 * 3)}"


def test_game_outcome_computer_wins_with_blackjack():
    player = Player(100)
    computer = Computer()
    player.points = 20
    computer.points = 21
    result = game_outcome(10, computer, player)
    assert result == f"Computer wins! Points equal 21. Players money: {100 - 10}"


def test_game_outcome_computer_busts():
    player = Player(100)
    computer = Computer()
    player.points = 20
    computer.points = 23
    result = game_outcome(10, computer, player)
    assert (
        result == f"Computer loses! Points exceeded 21. Players money: {100 + (10 * 2)}"
    )


def test_game_outcome_player_busts():
    player = Player(100)
    computer = Computer()
    player.points = 23
    computer.points = 19
    result = game_outcome(10, computer, player)
    assert result == f"Player loses! Points exceeded 21. Players money: {100 - 10}"


def test_game_outcome_its_a_draw():
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
    player = Player(-10)
    computer = Computer()
    player.points = 20
    computer.points = 19
    result = game_outcome(10, computer, player)
    assert result == "Player doesn't have enough money to play!"


def test_deal_card_after_busting():
    player = Player(100)
    computer = Computer()
    player.hand = [CARD_K, CARD_Q, CARD_2]
    result = deal_card(player, "Player")
    player.points = count_points(player.hand)
    assert result == "Player busts! Points exceeded 21."
    assert player.points == 22


# ===========================
# Tests for player_input logic
# ===========================


def test_player_input_invalid_total_amount():
    with patch("builtins.input", side_effect=["-34", "0", "100", "10"]):
        total_amount, betting_amount = player_input()
        assert total_amount == 100
        assert betting_amount == 10


def test_player_input_invalid_betting_amount():
    with patch("builtins.input", side_effect=["100", "0", "0", "10"]):
        total_amount, betting_amount = player_input()
        assert total_amount == 100
        assert betting_amount == 10


def test_player_input_valid_inputs():
    with patch("builtins.input", side_effect=["100", "10"]):
        total_amount, betting_amount = player_input()
        assert total_amount == 100
        assert betting_amount == 10


def test_invalid_input_key_instead_of_int():
    with patch("builtins.input", side_effect=["L", "L", "10"]):
        result = get_valid_input("Enter a positive number: ")
        assert result == 10


def test_betting_amount_higher_than_total_amount():
    player = Player(100)
    computer = Computer()
    result = game_outcome(203, computer, player)
    assert result == "Not enough money to make the bet!"


def test_betting_amount_lower_than_zero():
    player = Player(100)
    computer = Computer()
    result = game_outcome(-10, computer, player)
    assert result == "Invalid amount. Please enter a positive number."


# ========================
# Tests for invalid card input
# ========================


def test_count_points_invalid_card():
    with pytest.raises(KeyError):
        count_points(["Z"])


# ========================
# Tests for game()
# ========================


def test_invalid_player_input_stand_hit_exit():
    player = Player(100)
    computer = Computer()
    betting_amount = 10  # Define betting amount
    with patch("builtins.input", return_value="No"):  # Mock invalid input
        result = game(player, computer, betting_amount)  # Run the game

    assert result == "Invalid input. Please choose 'stand', 'hit' or 'exit'."


def test_game_exit_if_player_says_exit():
    player = Player(100)
    computer = Computer()
    betting_amount = 10  # Define betting amount

    # Mock the input to exit the game
    with patch("builtins.input", return_value="exit"):
        result = game(player, computer, betting_amount)

    assert result == "GAME OVER"


def test_game_busts_after_hit():
    player = Player(100)
    computer = Computer()

    # Mock a situation where the player busts after hitting
    player.hand = [CARD_10, CARD_10, CARD_2]  # 22
    computer.hand = [CARD_7, CARD_3]  # 10

    # Mock the card that will push the player's total over 21 (busting)
    with patch("builtins.input", return_value="hit"):
        result = deal_card(player, "Player")  # The card will make the player bust

    assert result == "Player busts! Points exceeded 21."


# Name                                   Stmts   Miss  Cover
# ----------------------------------------------------------
# projects/blackjack/computer.py             4      0   100%
# projects/blackjack/main.py               119     15    87%
# projects/blackjack/player.py               5      0   100%
# projects/blackjack/test_blackjack.py     144      0   100%
# ----------------------------------------------------------
# TOTAL                                    272     15    94%
