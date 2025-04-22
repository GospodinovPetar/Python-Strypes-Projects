import random
from computer import Computer
from player import Player

# Declare GAME_RUNNING as a global variable at the top of the code
GAME_RUNNING = True

# Defining constants for the cards
CARD_2 = "2"
CARD_3 = "3"
CARD_4 = "4"
CARD_5 = "5"
CARD_6 = "6"
CARD_7 = "7"
CARD_8 = "8"
CARD_9 = "9"
CARD_10 = "10"
CARD_J = "J"
CARD_Q = "Q"
CARD_K = "K"
CARD_A = "A"

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

    Special handling:
      - If the entity's points exceed 21 after receiving the card, it results in a bust (the entity loses).
      - The function selects a card at random from the deck and adds it to the entity's hand.

    Parameters:
        entity (Player | Computer): The entity (either a Player or Computer) receiving the card. The entity must have a `hand` attribute that is a list representing its current cards.
        role (str): A string representing the role of the entity (e.g., "Player" or "Computer") used in the response message.

    Returns:
        str: A message indicating the card dealt to the entity and its updated point total, or a bust message if the total exceeds 21.

    Example:
        deal_card(player, "Player")
        "Player got 10! Points: 15"
    """

    current: int = count_points(entity.hand)
    if current > 21:
        return f"{role} busts! Points exceeded 21."

    card: str = random.choice(list(deck_of_cards.keys()))

    entity.hand.append(card)
    current: int = count_points(entity.hand)  # Recalculate points after a card is added

    return f"{role} got {card}! Points: {current}"


def reset_points(comp: Computer, play: Player) -> str:
    """
    Resets the points and hands for both the computer and the player after a game round.

    Special handling:
      - The points for both the computer and player are reset to 0.
      - The hands of both the computer and player are cleared (emptied) to start a new round.

    Parameters:
        comp (Computer): The computer entity whose points and hand are being reset.
        play (Player): The player entity whose points and hand are being reset.

    Returns:
        str: A message indicating that the points and hands have been successfully reset for both entities.

    Example:
        reset_points(computer, player)
        "Points and hands have been reset!"
    """

    comp.points = 0
    play.points = 0
    comp.hand.clear()
    play.hand.clear()
    return "Points and hands have been reset!"


def game_outcome(betting_amount: float, computer: Computer, player: Player) -> str:
    """
    Determines the outcome of a game round, updates the player's total amount of money, and resets the points and hands.

    Special handling:
      - If the player doesn't have enough money to make the bet, the game can't proceed.
      - If the player or computer exceeds 21 points, the respective entity loses.
      - If the player or computer hits 21 points, special outcomes are applied (with corresponding changes to the player's money).
      - The game continues if no player or computer busts or hits 21.

    Parameters:
        betting_amount (float): The amount the player is betting on this round.
        computer (Computer): The computer entity, whose points and game status are checked.
        player (Player): The player entity, whose points and game status are checked.

    Returns:
        str: A message indicating the outcome of the round (e.g., whether the player or computer wins, loses, or if the game continues).

    Example:
        game_outcome(100, computer, player)
        "Player wins! Points equal 21. Players money: 500"
    """

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
        return (
            f"Computer loses! Points exceeded 21. Players money: {player.total_amount}"
        )

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
    Helper function to get a valid positive number as input from the user.

    Special handling:
      - Continuously prompts the user until a valid positive integer is entered.
      - If the user enters a non-integer or a non-positive number, an error message is displayed and the input is requested again.

    Parameters:
        prompt (str): The message to be displayed to the user, prompting for input.

    Returns:
        int: A valid positive integer input by the user.

    Example:
        get_valid_input("Enter a positive number: ")
        50
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


def player_input() -> tuple[float, float]:
    """
    Gets valid total amount and betting amount from the player.

    Special handling:
      - Prompts the player for a valid total amount they want to play with and a valid betting amount.
      - Uses the `get_valid_input` function to ensure that the amounts entered are positive numbers.
      - Returns the total amount and the betting amount as a tuple.

    Returns:
        tuple[float, float]: A tuple containing the player's total amount and betting amount.

    Example:
        player_input()
        (500, 100)
    """

    total : float = get_valid_input("Enter the total amount you want to play with: ")
    betting : float = get_valid_input("Enter the betting amount of the player: ")

    return total, betting

def game(player: Player, computer: Computer, betting_amount: float) -> str:

    """
    Runs the game loop where the player competes against the computer, managing rounds and actions.

    Special handling:
      - The game continues as long as the player has money and chooses to play.
      - The player can choose to "stand", "hit", or "exit" during their turn.
      - If the player or computer busts or hits 21, the game outcome is determined and the round ends.
      - The game loops, prompting the player for decisions and updating the hands, points, and outcome after each round.

    Parameters:
        player (Player): The player entity who participates in the game.
        computer (Computer): The computer entity, which competes against the player.
        betting_amount (float): The amount the player is betting for the current round.

    Returns:
        str: A message indicating the game outcome or "GAME OVER" if the game ends.

    Example:
        game(player, computer, 100)
        "Player wins! Points equal 21. Player's money: 500"
    """

    global GAME_RUNNING  # Declare GAME_RUNNING as global before using it

    while GAME_RUNNING:
        if player.total_amount <= 0:
            return "Player doesn't have enough money to play!"

        # Update current points for both player and computer
        player.points = count_points(player.hand)
        computer.points = count_points(computer.hand)

        # Determine the outcome of the game round
        result = game_outcome(betting_amount, computer, player)
        print(result)

        if result != "Game continues..":
            print(f"\nNew Game!")
            print(deal_card(player, "Player"))
            print(deal_card(computer, "Computer"))
            continue

        # If the game continues, ask the player for their action (hit, stand, or exit)
        player_choice: str = (
            input('Player chooses to "stand", "hit", "exit": ').strip().lower()
        )

        while player_choice not in ("stand", "hit", "exit"):
            print("Invalid input. Please choose 'stand', 'hit' or 'exit'.")
            player_choice = (
                input('Player chooses to "stand", "hit" or "exit": ').strip().lower()
            )

            if player_choice not in ("stand", "hit", "exit"):
                return "Invalid input. Please choose 'stand', 'hit' or 'exit'."  # Stop the game on invalid input

        if player_choice == "stand":
            print(deal_card(computer, "Computer"))
            print(f"Player points: {player.points}")
        elif player_choice == "hit":
            print(deal_card(player, "Player"))
            print(deal_card(computer, "Computer"))
        elif player_choice == "exit":
            GAME_RUNNING = False
            break

    return "GAME OVER"


if __name__ == "__main__":
    total_amount, betting_amount = player_input()
    player = Player(total_amount)
    computer = Computer()

    # Deal initial card to both.
    print(deal_card(player, "Player"))
    print(deal_card(computer, "Computer"))
    game(player, computer, betting_amount)
