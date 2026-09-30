"""
Word Counter
Raymond Black
Purpose: to count all the words in a file
and display how many times each word appears.

initial work used: 
code from Participation Activity 3 as a base
code from example in reading. had it saved locally.
more code from PA3 to ask to continue

refactor to follow instructions
2026-09-29
"""

# required by instructions
from pathlib import Path
from WordAnalyzer import WordAnalyzer

# no longer needed
import string

# no longer needed
from collections import Counter

def main():
    # base directory
    base_dir = Path(__file__).parent

# removing? will try and restore it
# class CountMore:
#     """Do another book?"""
#     def __init__(self):
#         self.is_running = True

#     def ask_to_continue(self):
#         """Validates yes/no  and returns whether the loop should keep running."""
#         while True:
#             more = input("\nDo you want to select another book? (yes/no): ").lower().strip()
#             if more in ['yes', 'y']:
#                 self.is_running = True
#                 return True
#             elif more in ['no', 'n']:
#                 print("\nThanks! Have a great day!\n")
#                 self.is_running = False
#                 return False
#             else:
#                 print("\nSorry, I didn't get that. Was that a yes or no?")
# end remove

# removing?
# session = CountMore()
# end removing


    files_menu = {
        "1": base_dir / "princess_mars.txt",
        "2": base_dir / "Tarzan.txt",
        "3": base_dir / "monte_cristo.txt",
        "4": base_dir / "treasure_island.txt"
    }


# got rid of session variable, for now.
# while session.is_running:

    while True:

        # menu
        print("\n           Select a book")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

        for key, filepath in files_menu.items():

            clean_name = filepath.stem.replace('_', ' ').title()
            print(f"{key}. {clean_name}")
        print("5. Exit")

        #menu option inputs
        selection = input("\nEnter selection: ").strip()

        if selection == "5":
            print("\nThanks! Have a great day!\n")
            break

        if selection not in files_menu:
            print("\nI think you mistyped. Please enter a number between 1 and 5.")
            continue

        selected_file = files_menu[selection]

        # moved and modified
        analyzer = WordAnalyzer(str(selected_file))

        if analyzer.process_file():
            analyzer.print_report()

if __name__ == "__main__":
    main()

    # original code
        # print("1. A Princess of Mars")
        # print("2. Tarzan of the Apes")
        # print("3. The Count of Monte Cristo")
        # print("4. Treasure Island") 
        # print("5. Exit")

        # #menu option inputs
        # selection = input("\nEnter selection: ").strip()

        # if selection == "1":
        # book = base_dir / "princess_mars.txt"
        # analyzer.count_words(book)

        # elif selection == "2":
        # book = base_dir / "Tarzan.txt"
        # analyzer.count_words(book)

        # elif selection == "3":
        # book = base_dir / "monte_cristo.txt"
        # analyzer.count_words(book)

        # elif selection == "4":
        # book = base_dir / "treasure_island.txt"
        # analyzer.count_words(book)

        # elif selection == "5":
        #     print("\nThanks! Have a great day!\n")
        #     session.is_running = False
        #     break
        # else:
        #     print("\nI think you mistyped. Please enter a number between 1 and 5.")
        #     continue

# session gone
    # session.ask_to_continue()