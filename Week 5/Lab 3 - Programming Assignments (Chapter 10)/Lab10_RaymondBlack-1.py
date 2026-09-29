"""
Word Counter
Raymond Black
Purpose: to count all the words in a file
and display how many times each word appears.

initial work used: 
code from Participation Activity 3 as a base
code from example in reading. had it saved locally.
more code from PA3 to ask to continue
"""

# required by instructions
from pathlib import Path
import string

# needed for the other code I borrowed
from collections import Counter

from WordAnalyzer import WordAnalyzer


class CountMore:
    """Do another book?"""
    def __init__(self):
        self.is_running = True

    def ask_to_continue(self):
        """Validates yes/no  and returns whether the loop should keep running."""
        while True:
            more = input("\nDo you want to select another book? (yes/no): ").lower().strip()
            if more in ['yes', 'y']:
                self.is_running = True
                return True
            elif more in ['no', 'n']:
                print("\nThanks! Have a great day!\n")
                self.is_running = False
                return False
            else:
                print("\nSorry, I didn't get that. Was that a yes or no?")

base_dir = Path(r"C:\\Users\\raymo\\OneDrive\\Documents\\CSCC  -Columbus State Community College\\Python Programming (26AU W04L) CSCI-1511-W04L-01965-AU-2026\\python_work\\GitByBit\\Week 5\\Lab 3 - Programming Assignments (Chapter 10)\\")

session = CountMore()
analyzer = WordAnalyzer()

while session.is_running:

    # changing to a menu-based option
    print("\n           Select a book")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("1. A Princess of Mars")
    print("2. Tarzan of the Apes")
    print("3. The Count of Monte Cristo")
    print("4. Treasure Island") 
    print("5. Exit")

    #menu option inputs
    selection = input("\nEnter selection: ").strip()

    if selection == "1":
       book = base_dir / "princess_mars.txt"
       analyzer.count_words(book)

    elif selection == "2":
       book = base_dir / "Tarzan.txt"
       analyzer.count_words(book)

    elif selection == "3":
       book = base_dir / "monte_cristo.txt"
       analyzer.count_words(book)

    elif selection == "4":
       book = base_dir / "treasure_island.txt"
       analyzer.count_words(book)

    elif selection == "5":
        print("\nThanks! Have a great day!\n")
        session.is_running = False
        break
    else:
        print("\nI think you mistyped. Please enter a number between 1 and 5.")
        continue

    session.ask_to_continue()