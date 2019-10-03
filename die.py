import random

class Die:
    """
    A die
    """

    def __init__(self, min: int = 1, max: int= 6):
        self.min = min
        self.max = max

    def roll(self) -> int:
        """Roll the die"""
        return random.randint(self.min, self.max)

