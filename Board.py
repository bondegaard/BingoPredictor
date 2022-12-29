import random

class Board:

    def __init__(self, id):
        self.id:int = id
        self.board:list = random.sample(range(1, 100), 15)


