import random
from computer import Computer
from player import Player

GAME_RUNNING = True

# Mapping card names to points.
deck_of_cards = {
    '2': 2, '3': 3, '4': 4, '5': 5,
    '6': 6, '7': 7, '8': 8, '9': 9,
    '10': 10, 'J': 10, 'Q': 10, 'K': 10,
    'A': 11
}


def count_points(hand) -> int:
    """"
    Function count_points:

    This function counts the number of points in a given hand.
    If the card is A. which is not in the deck, it's a made up card which indicated that
    either one of the players has drawn an Ace which will cause a bust, in that case
    we count the Ace as 1 instead of 11.
    """
    points = 0
    for card in hand:
        if card == 'A.':  # Ace adjusted value to 1
            points += 1
        else:
            points += deck_of_cards[card]
    return points



def deal_card(entity, role) -> None:
    """"
    Function deal_card:

    This function deals a random card to an entity (player or computer).
    If the card is an Ace and would cause a bust, it is marked as 'A.' and later counter as 1 instead of 11.
    """
    card : str = random.choice(list(deck_of_cards.keys()))
    if entity.points + deck_of_cards[card] > 21 and card == 'A':
        card = 'A.'
    entity.hand.append(card)
    current : int = count_points(entity.hand)
    print(f"{role} got {card}! Points: {current}")


def reset_points(comp, play) -> None:
    """"
    Function reset_points:

    This function resets the points of both players after the game has finished.
    """
    comp.points = 0
    play.points = 0
    comp.hand.clear()
    play.hand.clear()
    print("Points and hands have been reset!")


def game_outcome(betting_amount) -> None:
    """"
    Function game_outcome:

    This function is used to determine if the computer has won or lost.
    This is based on the points of the players
    """

    outcomes = {
        (True, True): "It's a draw",  # Both bust
        (True, False): "Player loses! Points exceeded 21.",  # Player busts
        (False, True): "Computer loses! Points exceeded 21.",  # Computer busts
        (False, False, True): "Player wins! Points equal 21.",  # Player wins with 21
        (False, False, False): "Computer wins! Points equal 21."  # Computer wins with 21
    }

    # Check for game conditions
    player_bust = player.points > 21
    computer_bust = computer.points > 21
    player_21 = player.points == 21
    computer_21 = computer.points == 21

    if player_bust and computer_bust:
        print(outcomes[(True, True)])
        reset_points(computer, player)
    elif player_bust:
        print(outcomes[(True, False)])
        player.total_amount -= betting_amount
        print(f"Player's money: {player.total_amount}")
        reset_points(computer, player)
    elif computer_bust:
        print(outcomes[(False, True)])
        player.total_amount += betting_amount * 2
        print(f"Player's money: {player.total_amount}")
        reset_points(computer, player)
    elif player_21:
        print(outcomes[(False, False, True)])
        player.total_amount += betting_amount * 3
        print(f"Player's money: {player.total_amount}")
        reset_points(computer, player)
    elif computer_21:
        print(outcomes[(False, False, False)])
        player.total_amount -= betting_amount
        print(f"Player's money: {player.total_amount}")
        reset_points(computer, player)


# Printing out the docstrings for each function
print(count_points.__doc__)
print(deal_card.__doc__)
print(reset_points.__doc__)
print(game_outcome.__doc__)

#Player's money
total_amount : int = int(input("Enter the total amount you want to play with: "))
#The amount that the player wants to bet
betting_amount : int = int(input("Enter the betting amount of the player: "))

player = Player(total_amount)
computer = Computer()

# Deal initial card to both.
deal_card(player, "Player")
deal_card(computer, "Computer")

while GAME_RUNNING:
    # Update current points.
    player.points = count_points(player.hand)
    computer.points = count_points(computer.hand)

    game_outcome(betting_amount)

    # End game if player runs out of money.
    if player.total_amount <= 0:
        print("Player doesn't have enough money to play!")
        break

    # Ask for player's decision: hit or stand (case-insensitive)
    player_choice : str = input('Player chooses to "stand" or "hit": ').strip().lower()

    while player_choice not in ('stand', 'hit'):
        print("Invalid input. Please choose 'stand' or 'hit'.")
        player_choice : str = input('Player chooses to "stand" or "hit": ').strip().lower()

    if player_choice == 'stand':
        deal_card(computer, "Computer")
        print(f'Player points: {player.points}')

    elif player_choice == 'hit':
        deal_card(player, "Player")
        deal_card(computer, "Computer")

