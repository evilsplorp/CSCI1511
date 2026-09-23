"""
Match Coins Game
Raymond Black
A simple coin matching game. 2 players start with 20 points.
If the coin is heads, one player gains a coin, the other loses
a coin (and vice versa).
This is the application itself. In progress, non-functional.
2026-09-23
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
        print(f"{player1.get_name()} got {side1}\n")
        print(f"{player2.get_name()} got {side2}")

    # print winners
    # If the sides match: Call the appropriate methods for 
    # Player1 to win_coin() and the loser to lose_coin(). 
    # update wallet
    # Print who won the round.
        if side1 == side2:
            player1.win_coin()
            player2.lose_coin()
            print(f"We've got a match! {player1.get_name()} wins!")
    # If the sides do not match: Call the appropriate methods for 
    # Player 2 to win_coin() and Player 1 to lose_coin(). 
    # update wallet
    # Print who won the round.        
        else:
            player1.lose_coin()
            player2.win_coin()
            print(f"No match! {player2.get_name()} wins!")

    # Report the total coins for each player using get_wallet().
        print(f"{player1.get_name()} has {player1.get_wallet()} coins.")
        print(f"{player2.get_name()} has {player2.get_wallet()} coins.")
        total1 = int(player1.get_wallet())
        total2 = int(player2.get_wallet())

    # if either player has an empty wallet, end the game
        if total1 <= 0:
            print(f"{player1.get_name()} is out of coins! {player2.get_name()} wins!")
            break
        elif total2 <= 0:
            print(f"{player2.get_name()} is out of coins! {player1.get_name()} wins!")
            break
    # otherwise, ask if they want to play again
        play = input("\nDo you want to toss a coin? (y/n))").strip().lower()

    print("-=-=-=-=-=-=-=GAME OVER=-=-=-=-=-=-=-\n")
    wallet1 = player1.get_wallet()
    wallet2 = player2.get_wallet()

    if wallet1 > wallet2:
        print(f"{player1.get_name()} wins!\n")
        print(f"{wallet1} to {wallet2}\n")
    elif wallet1 < wallet2:
        print(f"{player2.get_name()} wins!\n")
        print(f"{wallet2} to {wallet1}\n")
    else:
        print("It's a tie!\n")
        print(f"{wallet1} to {wallet2}\n")
   

    # if empty wallet or end game selected, provide winner info

    # call the function to start
main()