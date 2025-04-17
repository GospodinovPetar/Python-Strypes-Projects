<h1 align="center">Milestone Project II <br> Blackjack Game: Player vs. Computer</h1>

This is a simple Python implementation of a Blackjack game where a player competes against a computer. The player can choose to "hit" (draw a card) or "stand" (keep their current hand). The game simulates the process of card dealing, point calculation, and determining the outcome based on the players' scores.

## Overview

The game logic is designed for a two-player setup: one player is a human (the player), and the other is the computer. The deck consists of cards with values from 2 to Ace (Ace can be 11 or 1 depending on the situation). The goal is to achieve a hand value of 21 or as close as possible without exceeding it.

## Components

- **Player and Computer Classes**: These classes represent the entities (player and computer) and track their respective hands, points, and total money.
- **Card Deck**: The deck is represented as a dictionary with card names as keys and their corresponding point values as values.
- **Game Logic**: The game includes functions for dealing cards, counting points, and determining the outcome of each round.

## Functions

### `count_points(hand)`
This function counts the total points of the cards in a given hand. If an Ace would cause the total to exceed 21, it is counted as 1 instead of 11.

### `deal_card(entity, role)`
This function deals a random card to the given entity (either player or computer). If the card is an Ace that would cause a bust, it is counted as 'A.' (Ace counted as 1).

### `reset_points(comp, play)`
This function resets the hands and points of both the player and the computer after each round.

### `game_outcome(betting_amount)`
This function checks the points of both players and determines the winner or if there is a bust. It also adjusts the player's total money based on the outcome:
- If the player busts, they lose their bet.
- If the computer busts, the player wins the bet.
- If either player reaches 21 points, they win.
- The game can also result in a draw.

## Game Flow

1. **Initialization**: The player is prompted to enter the starting amount of money and their betting amount.
2. **Card Dealing**: Initially, both the player and the computer are dealt one card each.
3. **Game Loop**: The player chooses to "hit" (draw another card) or "stand" (keep their current hand). The computer automatically draws cards based on the game rules.
4. **Outcome**: The winner is determined based on the points of the player and the computer, with money being adjusted accordingly.

## Example

```bash
Enter the total amount you want to play with: 1000
Enter the betting amount of the player: 500
Player got J! Points: 10
Computer got 3! Points: 3
Player chooses to "stand", "hit", "exit": hit
Player got J! Points: 20
Computer got 9! Points: 12
Player chooses to "stand", "hit", "exit": stand
Computer got 4! Points: 16
Player points: 20
Player chooses to "stand", "hit", "exit": stand
Computer got 8! Points: 24
Player points: 20
Computer loses! Points exceeded 21.
Players money: 2000
Points and hands have been reset!
Player chooses to "stand", "hit", "exit": exit
