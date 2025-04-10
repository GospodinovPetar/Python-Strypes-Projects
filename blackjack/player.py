class Player:
    def __init__(self, total_amount : int, points : int = 0):
        self.points : int = points
        self.total_amount : int = total_amount
        self.hand : list = []
