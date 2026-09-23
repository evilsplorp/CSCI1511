"""
Match Coins Game
Raymond Black
A simple coin matching game. 2 players start with 20 points.
If the coin is heads, player 1 gains a coin and player 2 loses
a coin (and vice versa). Play continues until stopped or one
player has zero coins.
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

    while True:

        play = input("\nDo you want to toss a coin? (y/n) ").strip().lower()

        if play == "n":
            print("\nI guess you don't want to play.\n")
            break

        elif play == "y":

            player1 = Player(input("We need names. First player? "))
            print(f"{player1.get_name()}")
            while player1.get_name() == "":
                player1 = Player(input("Please enter a name, Player 1: "))
                if player1.get_name() == "":
                    continue
                else:
                    break

            player2 = Player(input("Second player? "))
            while player2.get_name() == "":
                player2 = Player(input("Please enter a name, Player 2: "))
                if player2.get_name() == "":
                    continue
                elif player2.get_name() == player1.get_name():
                    player2 = Player(input("Sorry, that name is taken. Choose another? "))
                    continue
                else:
                    break

            print(f"\nWelcome {player1.get_name()} and {player2.get_name()}! You both start with 20 coints.")
            while play == "y":
                print("🪙 🪙 🪙   Let\'s toss those coins! 🪙 🪙 🪙\n")
               
                player1.toss_coin()
                player2.toss_coin()

                side1 = player1.get_coin_side()
                side2 = player2.get_coin_side()

                print(f"{player1.get_name()} got {side1}")
                print(f"{player2.get_name()} got {side2}\n")

                if side1 == side2:
                    player1.win_coin()
                    player2.lose_coin()
                    print(f"We've got a match! {player1.get_name()} wins a coin 🪙  this round!")    
                else:
                    player1.lose_coin()
                    player2.win_coin()
                    print(f"No match! {player2.get_name()} wins a coin 🪙  this round!\n")

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

                play = input("\nDo you want to toss another coin? (y/n))\n").strip().lower()
                if play == "y":
                    continue
                elif play == "n":
                    break
                else:
                    print("Please enter y or n.")
                    play = input("\nDo you want to toss another coin? (y/n))\n").strip().lower()
                    continue

            print("-=-=-=-=-=-=-=GAME OVER=-=-=-=-=-=-=-\n")

            wallet1 = player1.get_wallet()
            wallet2 = player2.get_wallet()

            if wallet1 > wallet2:
                print(f"{player1.get_name()} wins!\n")
                print(f"The score is {wallet1} coins to {wallet2} coins.\n")
            elif wallet1 < wallet2:
                print(f"{player2.get_name()} wins!\n")
                print(f"The score is {wallet2} coins to {wallet1} coins.\n")
            else:
                print("It's a tie!\n")
                print(f"{wallet1} to {wallet2}\n")
            break
        else:
            print("Please enter y or n.")
            continue

main()