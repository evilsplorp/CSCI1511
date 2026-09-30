"""
WordAnalyzer Class for Word Counter
Raymond Black
Purpose: to count all the words in a file
and display how many times each word appears.

initial work used: 
Code from example in reading. had it saved locally.
Converted it to a Class.
Code from Google search to determine how to start at a specific
location in the file (they all have boilerplate before
the real content starts)

refactor to follow instructions.
2026-09-29
"""

from pathlib import Path
import string

# remove this
from collections import Counter

# __init__(self, filepath): The initializer should take the filepath 
# (as a string) and store it as a private pathlibrary
# Path object. It should also initialize a private dictionary 
# to hold the word frequencies.
class WordAnalyzer:
    def __init__(self, filepath):
        """
        main function in class
        """
        self.__filepath = Path(filepath)
        self.__frequency = {}

    def process_file(self):
        """
        process_file(self): This method will contain the main logic.
        """
        # Use a try-except block to handle FileNotFoundError gracefully.
        # Use the pathlib.Path object's .exists() method to check for the file.
        try:
            if not self.__filepath.exists():
                raise FileNotFoundError
            
            # reusing the punctuation translation table
            punct_table = str.maketrans('', '', string.punctuation)

            # flag for the boilerplate text
            begin_count = False

            #Use the pathlib.Path object's .open() method to read the file line by line
            with self.__filepath.open('r', encoding='utf-8') as file:
                # converted to use the line by line
                for contents in file:
                    # Check for the Project Gutenberg boilterplate
                    if not begin_count:
                        if contents.startswith("*** START OF THE PROJECT GUTENBERG EBOOK"):
                            begin_count = True
                        continue  # Skip lines until the marker is passed
                    # updated character replacement stuff
                    contents = contents.replace('—', ' - ')
                    contents = contents.replace('“', '"')
                    contents = contents.replace('”', '"')
                    contents = contents.replace('‘', "'")
                    contents = contents.replace('’', "'")

                    fixed_contents = contents.translate(punct_table)

                    fixed_contents = fixed_contents.lower()

                    words = fixed_contents.split()

                    # using the new stuff from above
                    for word in words:
                        if word: # make sure it's not a blank
                            if word in self.__frequency: # if it's already recorded, increase the value
                                self.__frequency[word] += 1
                            else:
                                self.__frequency[word] = 1 # if it doesn't exist, start it with a 1

            return True # Done!

        # handling the error and updated variable call in the print statement
        except FileNotFoundError:
            print(f"Sorry, the file {self.__filepath} does not exist.")
            return False


# original version
    # def count_words(self, filename):
    #     """Count the approximate number of words in a file."""
    #     file_path = Path(filename)
    #     try:
    #         contents = file_path.read_text(encoding='utf-8')
    #     except FileNotFoundError:
    #         print(f"Sorry, the file {file_path} does not exist.")
    #         # to make it just ignore the failure, use pass
    #     else:
    #         # Count the approximate number of words in the file:

    #         # found code to start at specific location
    #         lines = contents.splitlines()
    #         start_index = 0
            
    #         for i, line in enumerate(lines):
    #             if line.startswith("*** START OF THE PROJECT GUTENBERG EBOOK"):
    #                 start_index = i + 1  # Begin on the line immediately after the marker
    #                 break
            
    #         # Rejoin only the text following the start marker
    #         valid_content = "\n".join(lines[start_index:])

    #         # Ran into another issues with em-dashes connecting words
    #         # punctuation code removal didn't work, so found an
    #         # alternative
    #         contents = valid_content.replace('—', ' - ')
    #         contents = contents.replace('“', '"')
    #         contents = contents.replace('”', '"')
    #         contents = contents.replace('‘', "'")
    #         contents = contents.replace('’', "'")

    #         # reusing the punctuation translation table
    #         punct_table = str.maketrans('', '', string.punctuation)

    #         # handles the counting
    #         cleaned_contents = contents.translate(punct_table).lower()
    #         words = cleaned_contents.split()
    #         word_counts = Counter(words)

# end original version

# print_report(self): This method should print the results.
    def print_report(self):
        # get keys from frequency dictionary & sort them alpha.
        sorted_content = sorted(self.__frequency.keys())

        # Print the word and its count in the specified format
        for word in sorted_content:
            print(f"{word} :: {self.__frequency[word]}")


# old version
            # # list all the words and their counts
            # for word in sorted(word_counts):
            #     print(f"{word}: {word_counts[word]}")