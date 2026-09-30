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
the real content starts).

refactor to follow instructions.
2026-09-30
"""

from pathlib import Path
import string

class WordAnalyzer:
    '''
    optionally filters out specific words
    removes punctuation
    provides a count for each word in the selected document
    '''
    def __init__(self, filepath):
        """
        provides an initial file path
        empty frequency dictionary 
        """
        self.__filepath = Path(filepath)
        self.__frequency = {}

    def process_file(self):
        """
        reads and reviews selected document
        asks user if they want any words to be ignored
        cleans punctuation
        changes text to lowercase
        counts frequency of each unique word
        """
        try:
            if not self.__filepath.exists():
                raise FileNotFoundError

            clean_punctuation = string.punctuation.replace("'", "")
            
            punct_table = str.maketrans('', '', clean_punctuation)

            discard_list = self.ignore_words()

            begin_count = False

            with self.__filepath.open('r', encoding='utf-8') as file:
                for contents in file:
                    if not begin_count:
                        if contents.startswith("*** START OF THE PROJECT GUTENBERG EBOOK"):
                            begin_count = True
                        continue
                    # also saw this in the list. added a catch to stop when the book ends.
                    if contents.startswith("*** END OF THE PROJECT GUTENBERG EBOOK"):
                        break

                    contents = contents.replace('—', ' - ')
                    # happened to catch another weird thing in Treasure Island
                    # I added the below to separate words that were combined with a double --
                    contents = contents.replace('--', ' - ')
                    contents = contents.replace('“', '"')
                    contents = contents.replace('”', '"')
                    contents = contents.replace('‘', "'")
                    contents = contents.replace('’', "'")

                    fixed_contents = contents.translate(punct_table)

                    fixed_contents = fixed_contents.lower()

                    words = fixed_contents.split()

                    for word in words:
                        # handling the discard list
                        if word and word not in discard_list: 
                            if word in self.__frequency: 
                                self.__frequency[word] += 1
                            else:
                                self.__frequency[word] = 1 

            return True

        except FileNotFoundError:
            print(f"Sorry, the file {self.__filepath} does not exist.")
            return False

    def ignore_words(self):
        """
        asks user for optional words to ignore
        enter with no content ends the loop
        returns the list of words to be ignored
        """
        ignore = []
        while True:
            denied = input("\nDo you want to skip any words? Type a word or press Enter to finish: ").strip()
            if not denied:
                break
            ignore.append(denied)
        return ignore

    def print_report(self):
        '''
        prints the results for the selected book
        alphabetical list with a count for each word
        '''
        sorted_content = sorted(self.__frequency.keys())
        line_count = 0

        for word in sorted_content:
            print(f"{word} :: {self.__frequency[word]}")
            line_count += 1

            if line_count == 1000:
                keep_displaying = input("\nWow, that's a lot of words. Let's take a break.\n OK, hit ENTER to continue or type q to stop.\n").strip().lower()
                if keep_displaying == 'q':
                    print("\n Back to the main menu")
                    break
                line_count = 0