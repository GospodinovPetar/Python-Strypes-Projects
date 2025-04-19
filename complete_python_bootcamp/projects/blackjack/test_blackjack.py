import pytest

from projects.blackjack.computer import Computer
from projects.blackjack.main import count_points, reset_points
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

# TODO: test game_outcome

    