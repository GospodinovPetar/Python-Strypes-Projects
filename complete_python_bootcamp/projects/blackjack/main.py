import random
from computer import Computer
from player import Player

# Defining constants for the cards
CARD_2 = '2'
CARD_3 = '3'
CARD_4 = '4'
CARD_5 = '5'
CARD_6 = '6'
CARD_7 = '7'
CARD_8 = '8'
CARD_9 = '9'
CARD_10 = '10'
CARD_J = 'J'
CARD_Q = 'Q'
CARD_K = 'K'
CARD_A = 'A'

# Mapping card names to points.
deck_of_cards = {
    CARD_2: 2,
    CARD_3: 3,
    CARD_4: 4,
    CARD_5: 5,
    CARD_6: 6,
    CARD_7: 7,
    CARD_8: 8,
    CARD_9: 9,
    CARD_10: 10,
    CARD_J: 10,
    CARD_Q: 10,
    CARD_K: 10,
    CARD_A: 11,
}

global GAME_RUNNING

def count_points(hand: list) -> int:
    """
    Calculates the total points in a given hand based on card values.

    Special handling:
      - If a card is marked as 'A.' (indicating an Ace adjusted to avoid busting),
        it is counted as 1 point.
      - All other cards are evaluated using the deck_of_cards mapping.

    Parameters:
        hand (list of str): A list of card representations. Each card is a string that should be a key in the deck_of_cards dictionary.
                            Use 'A.' to denote an Ace counted as 1 point later.

    Returns:
        int: The total point value calculated from the hand.

    Example:
        count_points([CARD_A, CARD_10])
        21
    """

    points = 0
    for card in hand:
        points += deck_of_cards[card]

    # If points exceed 21, and we have Aces, adjust Aces from 11 to 1
    while points > 21 and CARD_A in hand:
        points -= 10  # Adjust one Ace from 11 to 1

    return points


def deal_card(entity: Player | Computer, role: str) -> str:
    """
    Deals a random card to an entity and updates its hand accordingly.
    """
    current: int = count_points(entity.hand)
    if current > 21:
        return f"{role} busts! Points exceeded 21."

    card: str = random.choice(list(deck_of_cards.keys()))

    entity.hand.append(card)
    current: int = count_points(entity.hand)  # Recalculate points after a card is added

    return f"{role} got {card}! Points: {current}"


def reset_points(comp: Computer, play: Player) -> None:
    """
    Resets the points and hands for both the computer and the player after a game round.
    """
    comp.points = 0
    play.points = 0
    comp.hand.clear()
    play.hand.clear()
    print("Points and hands have been reset!")


def game_outcome(betting_amount: float, computer: Computer, player: Player) -> str:
    if player.total_amount <= 0:
        return "Player doesn't have enough money to play!"

    if betting_amount > player.total_amount:
        return "Not enough money to make the bet!"

    if betting_amount <= 0:
        return "Invalid amount. Please enter a positive number."

    # Check for game conditions
    player_bust = player.points > 21
    computer_bust = computer.points > 21
    player_21 = player.points == 21
    computer_21 = computer.points == 21

    if player_bust and computer_bust:
        reset_points(computer, player)
        return "It's a draw"

    elif player_bust:
        player.total_amount -= betting_amount
        reset_points(computer, player)
        return f"Player loses! Points exceeded 21. Players money: {player.total_amount}"

    elif computer_bust:
        player.total_amount += betting_amount * 2
        reset_points(computer, player)
        return f"Computer loses! Points exceeded 21. Players money: {player.total_amount}"

    elif player_21:
        player.total_amount += betting_amount * 3
        reset_points(computer, player)
        return f"Player wins! Points equal 21. Players money: {player.total_amount}"

    elif computer_21:
        player.total_amount -= betting_amount
        reset_points(computer, player)
        return f"Computer wins! Points equal 21. Players money: {player.total_amount}"

    return "Game continues.."




def get_valid_input(prompt: str) -> int:
    """
    Helper function to get a valid positive number as input.
    """
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Invalid amount. Please enter a positive number.")
        except ValueError:
            print("Invalid amount. Please enter a positive number.")


def player_input():
    """
    Gets valid total amount and betting amount from the player.
    """
    total_amount = get_valid_input("Enter the total amount you want to play with: ")
    betting_amount = get_valid_input("Enter the betting amount of the player: ")

    return total_amount, betting_amount


def game():
    GAME_RUNNING = True
    while GAME_RUNNING:

        if player.total_amount <= 0:
            print("Player doesn't have enough money to play!")
            break

        # Update current points.
        player.points = count_points(player.hand)
        computer.points = count_points(computer.hand)

        result = game_outcome(betting_amount, computer, player)
        print(result)

        if result == "Game continues..":
            player_choice: str = (
                input('Player chooses to "stand", "hit", "exit": ').strip().lower()
            )
        else:
            print(f"\nNew Game!")
            print(deal_card(player, "Player"))
            print(deal_card(computer, "Computer"))
            continue

        while player_choice not in ("stand", "hit", "exit"):
            print("Invalid input. Please choose 'stand', 'hit' or 'exit'.")
            player_choice: str = (
                input('Player chooses to "stand", "hit" or "exit": ').strip().lower()
            )

        if player_choice == "stand":
            print(deal_card(computer, "Computer"))
            print(f"Player points: {player.points}")

        elif player_choice == "hit":
            print(deal_card(player, "Player"))
            print(deal_card(computer, "Computer"))

        elif player_choice == "exit":
            GAME_RUNNING = False
            break


if __name__ == "__main__":
    total_amount, betting_amount = player_input()
    player = Player(total_amount)
    computer = Computer()

    # Deal initial card to both.
    print(deal_card(player, "Player"))
    print(deal_card(computer, "Computer"))

    game()
