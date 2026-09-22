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
        """set default sides to Heads"""
        self.__name = name
        self.__wallet = 20
        self.__coin = Coin()

    @property
    def name(self):
        """Allows main.py to use 'player.name' instead of 'player.get_name()'"""
        return self.__name    

    def toss_coin(self):
        """
        Tells the player's coin to toss itself.
        """
        self.__coin.toss()

    def get_coin_side(self) -> str:
        """
        Gets the side of the player's coin and returns its value.
        """
        return self.__coin.get_sideup()

    def win_coin(self):
        """
        Adds 1 to the wallet.
        """
        self.__wallet += 1

    def lose_coin(self):
        """
        Subtracts 1 from the wallet.
        """
        self.__wallet -= 1

    def get_wallet(self) -> int:
        """
        Returns the current value of the wallet.
        """
        return self.__wallet

    def get_name(self) -> str:
        """
        Returns the value of the player's name.
        """
        return self.__name


