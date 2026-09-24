from coin import Coin

class Player:
    """
    Match Coins Game
    Raymond Black
    A simple coin matching game. 2 players start with 20 points.
    If the coin is heads, one player gains a coin, the other loses
    a coin (and vice versa). 
    This class handles the player functionality.
    2026-09-22
    """
    def __init__(self, name):
        """Sets a name argument"""
        self.__name = name
        self.__wallet = 20
        self.__coin = Coin()

    def toss_coin(self):
        """
        Toss the player's coin
        """
        self.__coin.toss()

    def get_coin_side(self) -> str:
        """
        Gets the player's coin and returns the value
        """
        return self.__coin.get_sideup()

    def win_coin(self):
        """
        Add 1 to the wallet when they win
        """
        self.__wallet += 1

    def lose_coin(self):
        """
        Subtract 1 from the wallet when they lose
        """
        self.__wallet -= 1

    def get_wallet(self) -> int:
        """
        Shows the value of the wallet
        """
        return self.__wallet

    def get_name(self) -> str:
        """
        Returns the player's name
        """
        return self.__name

    def is_valid_name(self, other: Player | None = None):
        """
        Returns True if valid, or a reason why it was invalid otherwise.
        """
        if self.get_name() == "":
            return "Nothing was entered."
        if other != None and self.get_name() == other.get_name():
            return "Sorry, that name was already taken. "
        return True