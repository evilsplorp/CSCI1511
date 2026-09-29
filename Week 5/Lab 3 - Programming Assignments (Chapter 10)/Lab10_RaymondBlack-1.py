"""
Word Counter
Raymond Black
Purpose: to count all the words in a file
and display how many times each word appears.

initial work used: 
code from Participation Activity 3 as a base
code from example in reading. had it saved locally.
code from the internet: how to remove characters
that the maketrans wasn't catching
more code from PA3 to ask to continue
"""

# required by instructions
from pathlib import Path
import string

# needed for the other code I borrower
from collections import Counter

# not sure I need this, but keeping for now
import re

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
                self.is_running = False
                return False
            else:
                print("\nSorry, I didn't get that. Was that a yes or no?")

def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
        # to make it just ignore the failure, use pass
    else:
        # Count the approximate number of words in the file:
        
        # ran into a problem when I tried to ignore punctuation. 
        # this is my second runthrough, tested locally. the 
        # curved double and single quotes weren't being removed,
        # so I Googled how to exlude them and got this
        extended_punctuation = string.punctuation + "“”‘’"

        # replaces the normal, and the extra punctuation, with nothing
        punct_table = str.maketrans("", "", extended_punctuation)

        # handles the counting
        cleaned_contents = contents.translate(punct_table).lower()
        words = cleaned_contents.split()
        word_counts = Counter(words)

        # list all the words and their counts
        for word in sorted(word_counts):
            print(f"{word}: {word_counts[word]}")

# random trouble with the path to the files not working
cwd = Path.cwd()
print(f"Path: {cwd}")

session = CountMore()
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

    filenames = ["C:\\Users\\raymo\\OneDrive\\Documents\\CSCC  -Columbus State Community College\\Python Programming (26AU W04L) CSCI-1511-W04L-01965-AU-2026\\python_work\\GitByBit\\Week 5\\Lab 3 - Programming Assignments (Chapter 10)\\treasure_island.txt", 
                 "C:\\Users\\raymo\\OneDrive\\Documents\\CSCC  -Columbus State Community College\\Python Programming (26AU W04L) CSCI-1511-W04L-01965-AU-2026\\python_work\\GitByBit\\Week 5\\Lab 3 - Programming Assignments (Chapter 10)\\Tarzan.txt", 
                 "C:\\Users\\raymo\\OneDrive\\Documents\\CSCC  -Columbus State Community College\\Python Programming (26AU W04L) CSCI-1511-W04L-01965-AU-2026\\python_work\\GitByBit\\Week 5\\Lab 3 - Programming Assignments (Chapter 10)\\monte_cristo.txt", 
                 "C:\\Users\\raymo\\OneDrive\\Documents\\CSCC  -Columbus State Community College\\Python Programming (26AU W04L) CSCI-1511-W04L-01965-AU-2026\\python_work\\GitByBit\\Week 5\\Lab 3 - Programming Assignments (Chapter 10)\\treasure_island.txt"]
    for filename in filenames:
        path = Path(filename)
        count_words(path)

    if selection == "1":
       book = "C:\\Users\\raymo\\OneDrive\\Documents\\CSCC  -Columbus State Community College\\Python Programming (26AU W04L) CSCI-1511-W04L-01965-AU-2026\\python_work\\GitByBit\\Week 5\\Lab 3 - Programming Assignments (Chapter 10)\\treasure_island.txt"
       count_words(book)

    if selection == "2":
       book = "C:\\Users\\raymo\\OneDrive\\Documents\\CSCC  -Columbus State Community College\\Python Programming (26AU W04L) CSCI-1511-W04L-01965-AU-2026\\python_work\\GitByBit\\Week 5\\Lab 3 - Programming Assignments (Chapter 10)\\Tarzan.txt"
       count_words(book)

    if selection == "3":
       book = "C:\\Users\\raymo\\OneDrive\\Documents\\CSCC  -Columbus State Community College\\Python Programming (26AU W04L) CSCI-1511-W04L-01965-AU-2026\\python_work\\GitByBit\\Week 5\\Lab 3 - Programming Assignments (Chapter 10)\\monte_cristo.txt"
       count_words(book)

    if selection == "4":
       book = "C:\\Users\\raymo\\OneDrive\\Documents\\CSCC  -Columbus State Community College\\Python Programming (26AU W04L) CSCI-1511-W04L-01965-AU-2026\\python_work\\GitByBit\\Week 5\\Lab 3 - Programming Assignments (Chapter 10)\\treasure_island.txt"
       count_words(book)

    elif selection == "5":
        # calculating = False
        session.is_running = False
        break
    else:
        print("\nI think you mistyped. Please enter a number between 1 and 5.")
        continue

    session.ask_to_continue()