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
)


# ========================
# Tests for count_points()
# ========================


def test_counting_points_with_ace_as_11():
    # Test: Hand has an Ace and a 3. The Ace counts as 11.
    hand = [CARD_A, CARD_3]
    result = count_points(hand)
    assert result == 14  # 11 (Ace) + 3 = 14


def test_counting_points_with_ace_and_other_cards():
    # Test: Hand has a 6, a 7, and an Ace. The Ace counts as 11.
    hand = [CARD_6, CARD_7, CARD_A]
    result = count_points(hand)
    assert result == 14  # 6 + 7 + 11 (Ace) = 14


# ==========================
# Tests for reset_points()
# ==========================


def test_reset_points():
    # Test: Reset points for both player and computer
    computer = Computer()
    player = Player(100)
    computer.points = 123
    player.points = 124
    reset_points(computer, player)
    assert computer.points == 0  # Computer's points should be reset
    assert player.points == 0  # Player's points should be reset


# ================================
# Tests for game_outcome() logic
# ================================


def test_game_outcome_player_wins_with_blackjack():
    # Test: Player wins with a Blackjack (21 points)
    player = Player(100)
    computer = Computer()
    player.points = 21  # Player has Blackjack
    computer.points = 19
    result = game_outcome(10, computer, player)
    assert result == f"Player wins! Points equal 21. Players money: {100 + (10 * 3)}"


def test_game_outcome_computer_wins_with_blackjack():
    # Test: Computer wins with a Blackjack (21 points)
    player = Player(100)
    computer = Computer()
    player.points = 20
    computer.points = 21  # Computer has Blackjack
    result = game_outcome(10, computer, player)
    assert result == f"Computer wins! Points equal 21. Players money: {100 - 10}"


def test_game_outcome_computer_busts():
    # Test: Computer exceeds 21 points (busts), player wins
    player = Player(100)
    computer = Computer()
    player.points = 20
    computer.points = 23  # Computer busts
    result = game_outcome(10, computer, player)
    assert (
        result == f"Computer loses! Points exceeded 21. Players money: {100 + (10 * 2)}"
    )


def test_game_outcome_player_busts():
    # Test: Player exceeds 21 points (busts), player loses
    player = Player(100)
    computer = Computer()
    player.points = 23  # Player busts
    computer.points = 19
    result = game_outcome(10, computer, player)
    assert result == f"Player loses! Points exceeded 21. Players money: {100 - 10}"


def test_game_outcome_its_a_draw():
    # Test: Both player and computer bust, it's a draw
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
    # Test: Deal card with mocked values
    player = Player(100)

    # Mock 'A' to always be drawn
    with patch("random.choice", return_value=CARD_A):
        result = deal_card(player, "Player")
        assert result == "Player got A! Points: 11"  # Ace counts as 11 initially

    # Mock '10' to always be drawn
    with patch("random.choice", return_value=CARD_10):
        result = deal_card(player, "Player")
        assert result == "Player got 10! Points: 21"  # Now points should be 21

    # Mock Ace adjusted to 1
    with patch("random.choice", return_value=CARD_A):
        player.hand = [CARD_K, CARD_Q]
        result = deal_card(player, "Player")
        assert result == "Player got A! Points: 21"  # Ace counts as 1


# ===========================
# Tests for game continuation
# ===========================


def test_game_continues():
    # Test: Game continues if neither player busts
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
    # Test: Player starts with negative money
    player = Player(-10)  # Player starts with negative money
    computer = Computer()
    player.points = 20
    computer.points = 19
    result = game_outcome(10, computer, player)
    assert result == "Player doesn't have enough money to play!"


def test_deal_card_after_busting():
    # Test: Deal card after player busts
    player = Player(100)
    computer = Computer()
    player.hand = [CARD_K, CARD_Q, CARD_2]  # The player is already busted
    result = deal_card(player, "Player")
    player.points = count_points(player.hand)
    assert result == "Player busts! Points exceeded 21."  # No card should be dealt
    assert player.points == 22  # Ensure points haven't changed


# ===========================
# Tests for player_input logic
# ===========================


def test_player_input_invalid_total_amount():
    # Test: Invalid total amount input, then a valid one (100)
    with patch("builtins.input", side_effect=["-34", "0", "100", "10"]):
        total_amount, betting_amount = player_input()
        assert total_amount == 100
        assert betting_amount == 10


def test_player_input_invalid_betting_amount():
    # Test: Invalid betting amount input, then a valid one (10)
    with patch("builtins.input", side_effect=["100", "0", "0", "10"]):
        total_amount, betting_amount = player_input()
        assert total_amount == 100
        assert betting_amount == 10


def test_player_input_valid_inputs():
    # Test: Valid inputs for both total amount and betting amount
    with patch("builtins.input", side_effect=["100", "10"]):
        total_amount, betting_amount = player_input()
        assert total_amount == 100
        assert betting_amount == 10


def test_invalid_input_key_instead_of_int():
    # Test: Invalid input ('L') followed by valid input ('10')
    with patch("builtins.input", side_effect=["L", "L", "10"]):
        result = get_valid_input("Enter a positive number: ")
        assert (
            result == 10
        )  # Should return the valid number entered after invalid attempts


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
    # Test: Invalid card input should raise a KeyError
    with pytest.raises(KeyError):
        count_points(["Z"])  # Invalid card 'Z' should raise KeyError

# Name                                   Stmts   Miss  Cover   Missing
# --------------------------------------------------------------------
# projects/blackjack/computer.py             4      0   100%
# projects/blackjack/main.py               117     33    72%   169-209, 213-221
# projects/blackjack/player.py               5      0   100%
# projects/blackjack/test_blackjack.py     122      0   100%
# --------------------------------------------------------------------
# TOTAL                                    248     33    87%