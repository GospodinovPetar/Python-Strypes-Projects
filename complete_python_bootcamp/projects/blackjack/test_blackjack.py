import pytest

from projects.blackjack.computer import Computer
from projects.blackjack.main import count_points, reset_points, game_outcome, deal_card
from projects.blackjack.player import Player


def test_counting_points():
    hand = ["A", "3"]
    result = count_points(hand)

    assert result == 14


def test_counting_points_with_ace_counted_as_one():
    hand = ["A.", "2"]
    result = count_points(hand)

    assert result == 3


def test_counting_ace_as_one():
    hand = ["6", "7", "A"]

    assert count_points(hand) == 14


def test_reset_points():
    computer = Computer()
    player = Player(100)
    computer.points = 123
    player.points = 124

    reset_points(computer, player)

    assert computer.points == 0
    assert player.points == 0


def test_game_outcome_player_wins_with_a_blackjack():
    player = Player(100)
    computer = Computer()
    player.points = 21
    computer.points = 19
    game_outcome(10, computer, player)
    # Player got a blackjack so the betting amount is tripled
    assert player.total_amount == 130

def test_game_outcome_computer_gets_a_blackjack():
    player = Player(100)
    computer = Computer()
    player.points = 20
    computer.points = 21
    game_outcome(10, computer, player)
    assert player.total_amount == 90

def test_game_outcome_computer_busts():
    player = Player(100)
    computer = Computer()
    player.points = 20
    computer.points = 23
    game_outcome(10, computer, player)
    assert player.total_amount == 120

def test_game_outcome_player_busts():
    player = Player(100)
    computer = Computer()
    player.points = 23
    computer.points = 19
    game_outcome(10, computer, player)
    assert player.total_amount == 90

def test_game_outcome_its_a_draw():
    player = Player(100)
    computer = Computer()
    player.points = 23
    computer.points = 24
    game_outcome(10, computer, player)
    assert player.total_amount == 100

def test_player_total_amount_zero():
    player = Player(0)  # Player starts with no money
    computer = Computer()
    player.points = 21
    computer.points = 19
    result = game_outcome(10, computer, player)
    # Player shouldn't have enough money to make a bet
    assert result == 'Player doesn\'t have enough money to play!'  # Make sure the game doesn't allow betting when out of money

def test_player_betting_amount_zero():
    player = Player(100)  # Player starts with no money
    computer = Computer()
    player.points = 21
    computer.points = 19
    result = game_outcome(0, computer, player)
    # Player shouldn't have enough money to make a bet
    assert result == 'Invalid amount. Please enter a positive number.'  # Make sure the game doesn't allow betting when out of money

def test_player_betting_amount_higher_than_total_amount():
    player = Player(100)
    computer = Computer()
    player.points = 21
    computer.points = 19
    result = game_outcome(110, computer, player)
    assert result == 'Not enough money to make the bet!'

def test_deal_card_while_not_busting():
    player = Player(100)
    computer = Computer()

    deal_card(player, "Player")
    assert player.points <= 21  # Ensure that the points do not exceed 21

def test_deal_card_while_busting():
    player = Player(100)
    computer = Computer()

    player.points = 22
    result = deal_card(player, "Player")
    assert result == f"Player busts! Points exceeded 21." # Points should not change because a card wasn't dealt

# Name                                   Stmts   Miss  Cover
# ----------------------------------------------------------
# projects/blackjack/computer.py             4      0   100%
# projects/blackjack/main.py               104     35    66%
# projects/blackjack/player.py               5      0   100%
# projects/blackjack/test_blackjack.py      90      0   100%
# ----------------------------------------------------------
# TOTAL                                    203     35    83%