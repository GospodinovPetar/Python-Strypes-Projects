import random
from computer import Computer
from player import Player

GAME_RUNNING = True

# Mapping card names to points.
deck_of_cards = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 11,
}


def count_points(hand: list) -> int:
    """
    Calculates the total points in a given hand based on card values.

    Special handling:
      - If a card is marked as 'A.' (indicating an Ace adjusted to avoid busting),
        it is counted as 1 point.
      - All other cards are evaluated using the deck_of_cards mapping.

    Parameters:
        hand (list of str): A list of card representations. Each card is a string that should be a key in the deck_of_cards dictionary.
                            Use 'A.' to denote an Ace counted as 1 point.

    Returns:
        int: The total point value calculated from the hand.

    Example:
        count_points(['A', '10'])
        21
    """

    points = 0
    ace_count = 0
    for card in hand:
        if card == "A.":  # Ace adjusted to 1
            points += 1
        elif card == "A":  # Ace as 11
            points += 11
        else:
            points += deck_of_cards[card]

    # If points exceed 21 and we have Aces, adjust Aces from 11 to 1
    while points > 21 and "A" in hand:
        points -= 10  # Adjust one Ace from 11 to 1
        hand.remove("A")  # Remove one 'A' from the hand (since it's counted as 11)
        hand.append("A.")  # Add 'A.' (Ace as 1)

    return points


def deal_card(entity: Player | Computer, role: str) -> str:
    """
    Deals a random card to an entity and updates its hand accordingly.

    The function randomly selects a card from the deck_of_cards.
    If the selected card is an Ace ('A') and adding its value would cause the entity's total points to exceed 21,
    the card is adjusted to 'A.' (to be counted as 1 point later). The card is then appended to the entity's hand,
    and the updated point total is printed along with the role (e.g., "Player" or "Computer").

    Parameters:
        entity: An object (such as an instance of Player or Computer) that has a 'hand' attribute (a list) and a 'points' attribute (an int).
        role (str): A string representing the role of the entity, used for printing messages.

    Returns:
       None
    """

    card: str = random.choice(list(deck_of_cards.keys()))
    if entity.points + deck_of_cards[card] > 21 and card == "A":
        card = "A."
    elif entity.points > 21:
        return f"{role} busts! Points exceeded 21."
    entity.hand.append(card)
    current: int = count_points(entity.hand)
    return f"{role} got {card}! Points: {current}"


def reset_points(comp: Computer, play: Player) -> None:
    """
    Resets the points and hands for both the computer and the player after a game round.

    This function sets the 'points' attribute of both entities to 0 and clears their hands.
    It then prints a confirmation message stating that the points and hands have been reset.

    Parameters:
        comp: An instance of Computer, which must have 'points' (int) and 'hand' (list) attributes.
        play: An instance of Player, which must have 'points' (int) and 'hand' (list) attributes.

    Returns:
       None
    """

    comp.points = 0
    play.points = 0
    comp.hand.clear()
    play.hand.clear()
    print("Points and hands have been reset!")


def game_outcome(betting_amount: float, computer: Computer, player: Player) -> str:
    """
    Determines the outcome of the game round based on the points of the player and the computer,
    and adjusts the player's money accordingly.

    The outcome conditions include:
      - Both entities bust (exceed 21 points): Declares a draw.
      - Only the player busts: Player loses and loses the bet amount.
      - Only the computer busts: Player wins and receives twice the bet amount.
      - Player reaches exactly 21 points: Player wins with a bonus (receives three times the bet amount).
      - Computer reaches exactly 21 points: Computer wins and the player loses the bet amount.

    After printing the outcome and updating the player's total money,
    the function resets the points and hands for both entities using the reset_points function.

    Parameters:
        player: The player object, which must have a 'points' attribute (an int) and a 'total_amount' attribute (an int).
        computer: Computer object, which must have a 'points' attribute (an int) and a 'hand' attribute (a list).
        betting_amount (int): The monetary amount bet for the current game round, used to update the player's total amount.

    Returns:
        None
    """
    if player.total_amount <= 0:
        return 'Player doesn\'t have enough money to play!'

    if betting_amount > player.total_amount:
        return 'Not enough money to make the bet!'

    if betting_amount <= 0:
        return 'Invalid amount. Please enter a positive number.'

    outcomes = {
        (True, True): "It's a draw",  # Both bust
        (True, False): "Player loses! Points exceeded 21.",  # Player busts
        (False, True): "Computer loses! Points exceeded 21.",  # Computer busts
        (False, False, True): "Player wins! Points equal 21.",  # Player wins with 21
        (False, False, False,): "Computer wins! Points equal 21."  # Computer wins with 21
    }

    # Check for game conditions
    player_bust = player.points > 21
    computer_bust = computer.points > 21
    player_21 = player.points == 21
    computer_21 = computer.points == 21

    if player_bust and computer_bust:
        reset_points(computer, player)
        return outcomes[(True, True)]

    elif player_bust:
        print(outcomes[(True, False)])
        player.total_amount -= betting_amount
        reset_points(computer, player)
        return f"Player's money: {player.total_amount}"
    elif computer_bust:
        print(outcomes[(False, True)])
        player.total_amount += betting_amount * 2
        reset_points(computer, player)
        return f"Player's money: {player.total_amount}"

    elif player_21:
        print(outcomes[(False, False, True)])
        player.total_amount += betting_amount * 3
        reset_points(computer, player)
        return f"Player's money: {player.total_amount}"

    elif computer_21:
        print(outcomes[(False, False, False)])
        player.total_amount -= betting_amount
        reset_points(computer, player)
        return f"Player's money: {player.total_amount}"

    return 'Invalid game outcome. Please try again.'


if __name__ == "__main__":
    total_amount: int = 0
    betting_amount: int = 0
    # Player's money
    while total_amount <= 0:
        total_amount: int = int(input("Enter the total amount you want to play with: "))
        if total_amount <= 0:
            print("Invalid amount. Please enter a positive number.")
    # The amount that the player wants to bet
    while betting_amount <= 0:
        betting_amount: int = int(input("Enter the betting amount of the player: "))
        if betting_amount <= 0:
            print("Invalid amount. Please enter a positive number.")

    player = Player(total_amount)
    computer = Computer()

    # Deal initial card to both.
    deal_card(player, "Player")
    deal_card(computer, "Computer")

    while GAME_RUNNING:

        if player.total_amount <= 0:
            print("Player doesn't have enough money to play!")
            break

        # Update current points.
        player.points = count_points(player.hand)
        computer.points = count_points(computer.hand)

        game_outcome(betting_amount, computer, player)
        player_choice: str = (
            input('Player chooses to "stand", "hit", "exit": ').strip().lower()
        )

        while player_choice not in ("stand", "hit", "exit"):
            print("Invalid input. Please choose 'stand', 'hit' or 'exit'.")
            player_choice: str = (
                input('Player chooses to "stand", "hit" or "exit": ').strip().lower()
            )

        if player_choice == "stand":
            deal_card(computer, "Computer")
            print(f"Player points: {player.points}")

        elif player_choice == "hit":
            deal_card(player, "Player")
            deal_card(computer, "Computer")

        elif player_choice == "exit":
            GAME_RUNNING = False
            break
