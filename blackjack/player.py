class Player:
    def __init__(self, total_amount : int, points : int = 0):
        #Player points
        self.points : int = points
        #Player total amount of money
        self.total_amount : int = total_amount
        #Player hand
        self.hand : list = []
