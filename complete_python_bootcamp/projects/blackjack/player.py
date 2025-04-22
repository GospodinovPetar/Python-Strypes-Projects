class Player:
    def __init__(self, total_amount: float, points: int = 0):
        # Player points
        self.points: int = points
        # Players total amount of money
        self.total_amount: float = total_amount
        # Player hand
        self.hand: list = []
