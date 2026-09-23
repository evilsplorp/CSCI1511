"""
Match Coins Game
Raymond Black
A simple coin matching game. 2 players start with 20 points.
If the coin is heads, one player gains a coin, the other loses
a coin (and vice versa).
This is the application itself.
2026-09-23
 """
from player import Player

def main():
    """
    Get player names for coin game. Toss coins, compare coins, determine
    a winner. print scores and ask if they want to continue (unless one
    of them has a coin total of 0 or less)
    """
    player1 = Player(input("Enter Player 1 name: "))
    player2 = Player(input("Enter Player 2 name: "))

    play = input("\nDo you want to toss a coin? (y/n))").strip().lower()
    if play == 'n':
        print("\nI guess you don't want to play.\n")
    elif play == "y":

        while play == "y":
            print("Let\'s toss those coins!")

            player1.toss_coin()
            player2.toss_coin()

            side1 = player1.get_coin_side()
            side2 = player2.get_coin_side()

            print(f"{player1.get_name()} got {side1}\n")
            print(f"{player2.get_name()} got {side2}")

            if side1 == side2:
                player1.win_coin()
                player2.lose_coin()
                print(f"We've got a match! {player1.get_name()} wins!")    
            else:
                player1.lose_coin()
                player2.win_coin()
                print(f"No match! {player2.get_name()} wins!")

            print(f"{player1.get_name()} has {player1.get_wallet()} coins.")
            print(f"{player2.get_name()} has {player2.get_wallet()} coins.")
            total1 = int(player1.get_wallet())
            total2 = int(player2.get_wallet())

            if total1 <= 0:
                print(f"{player1.get_name()} is out of coins! {player2.get_name()} wins!")
                break
            elif total2 <= 0:
                print(f"{player2.get_name()} is out of coins! {player1.get_name()} wins!")
                break
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
    else:
        print("Please enter y or n.")
        continue

main()