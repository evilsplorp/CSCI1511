import random

class Coin:
    """
    Match Coins Game
    Raymond Black
    A simple coin matching game. 2 players start with 20 points.
    If the coin is heads, one player gains a coin, the other loses
    a coin (and vice versa).
    This class handles the coin flipping functionality.
    2026-09-22
    """

    def __init__(self):
        """set default sides to Heads"""
        self.__sideup = random.choice(['Heads', 'Tails'])
        # initialize the attribute

    def toss(self):
        """Return and print a random number between 1 and the number of sides."""
        self.__sideup = random.randint(0, 1)
        if self.__sideup == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self):
        """Get the side of the coin that was returned"""
        return self.__sideup
