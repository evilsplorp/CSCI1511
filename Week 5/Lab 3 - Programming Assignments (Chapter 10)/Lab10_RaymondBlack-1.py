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
2026-09-30
"""

from pathlib import Path
from WordAnalyzer import WordAnalyzer

def main():
    '''
    Runs the main menu for the application
    Gives a list of books (with an exit option) from
    which the user can select,
    Analyzation is handled by the WordAnalzer class.
    Input validation is handled here as well.
    '''
    base_dir = Path(__file__).parent

    files_menu = {
        "1": base_dir / "princess_mars.txt",
        "2": base_dir / "Tarzan.txt",
        "3": base_dir / "monte_cristo.txt",
        "4": base_dir / "treasure_island.txt"
    }

    while True:

        print("\n                 Select a book")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

        for key, filepath in files_menu.items():

            clean_name = filepath.stem.replace('_', ' ').title()
            # if statements to provide correct names of the books
            if clean_name == "Princess Mars":
                clean_name = "A Princess of Mars"
            elif clean_name == "Tarzan":
                clean_name = "Tarzan of the Apes"
            elif clean_name == "Monte Cristo":
                clean_name = "The Count of Monte Cristo"                
            else:
                clean_name = clean_name

            print(f"{key}. {clean_name}")
        print 
        print("5. Exit")
        selection = input("\nEnter selection: ").strip()

        if selection == "5":
            print("\nThanks! Have a great day!\n")
            break

        if selection not in files_menu:
            print("\nI think you mistyped. Please enter a number between 1 and 5.")
            continue

        selected_file = files_menu[selection]

        analyzer = WordAnalyzer(str(selected_file))

        if analyzer.process_file():
            analyzer.print_report()

if __name__ == "__main__":
    main()