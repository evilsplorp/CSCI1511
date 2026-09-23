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
    """
    Get some player names
    """
    player1 = Player(input("Enter Player 1 name: "))
    player2 = Player(input("Enter Player 2 name: "))

    play = input("\nDo you want to toss a coin? (y/n))").strip().lower()

    while play == "y":
        print("Let\'s toss those coins!")

# toss coin for each player
    player1.toss_coin()
    player2.toss_coin()

# get result for each coin toss
    side1 = player1.get_coin_side()
    side2 = player2.get_coin_side()

# print name and who tossed what
    print(f"{player1} got {side1}\n")
    print(f"{player2} got {side2}")

# print winners
# If the sides match: Call the appropriate methods for the 
# winner to win_coin() and the loser to lose_coin(). 
# Print who won the round.
# If the sides do not match: Call the appropriate methods for 
# Player 2 to win_coin() and Player 1 to lose_coin(). 
# Print who won the round.

# update wallets
# Report the total coins for each player using get_wallet().


# if either player has an empty wallet, end the game
# otherwise, ask if they want to play again

# if empty wallet or end game selected, provide winner info

# call the function to start
main()