class Player:
    def __init__(self, total_amount: int, points: int = 0):
        # Players points
        self.points: int = points
        # Players total amount of money
        self.total_amount: int = total_amount
        # Players hand
        self.hand: list = []
