"""
Word Counter
Raymond Black
Purpose: to count all the words in a file
and display how many times each word appears.

initial work used: 
code from Participation Activity 3 as a base
code from example in reading. had it saved locally.

"""

def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
        # to make it just ignore the failure, use pass
    else:
        # Count the approximate number of words in the file:
        words = contents.split()
        word_counts = Counter(words)
        for word in sorted(word_counts):
            print(f"{word}: {word_counts[word]}")

running = True
while True:

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



    if selection == 1:
       filename = "C:\\Users\\raymo\\OneDrive\\Documents\\CSCC  -Columbus State Community College\\Python Programming (26AU W04L) CSCI-1511-W04L-01965-AU-2026\\python_work\\GitByBit\\Week 5\\Lab 3 - Programming Assignments (Chapter 10)\\princess_mars.txt"
       count_words()




    elif selection == "6":
        # calculating = False
        session.is_running = False
        break
    else:
        print("\nI think you mistyped. Please enter a number between 1 and 7.")
        continue

    session.ask_to_continue()