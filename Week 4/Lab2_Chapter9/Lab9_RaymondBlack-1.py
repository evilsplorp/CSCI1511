"""
Match Coins Game
Raymond Black
A simple coin matching game. 2 players start with 20 points.
If the coin is heads, one player gains a coin, the other loses
a coin (and vice versa).
This is the application itself. In progress, non-functional.
2026-09-22
 """
from player import Player


def main():
    player1 = Player(input("Enter Player 1 name: "))
    player2 = Player(input("Enter Player 2 name: "))
    # return player1, player2

    play = input("\nDo you want to toss a coin? (y/n))").strip().lower()

    while play == "y":
        print("Let\'s toss those coins!")

# toss coin for each player

# get result for each coin toss

# print name and who tossed what

# print winner

# update wallets

# if either player has an empty wallet, end the game
# otherwise, ask if they want to play again

# empty wallet or end game, provide winner info

# call the function?