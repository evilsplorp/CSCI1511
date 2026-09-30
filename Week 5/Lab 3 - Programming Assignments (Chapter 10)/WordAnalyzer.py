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
2026-09-29
"""

from pathlib import Path
import string

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
        try:
            if not self.__filepath.exists():
                raise FileNotFoundError
            
            punct_table = str.maketrans('', '', string.punctuation)

            begin_count = False

            with self.__filepath.open('r', encoding='utf-8') as file:
                for contents in file:
                    if not begin_count:
                        if contents.startswith("*** START OF THE PROJECT GUTENBERG EBOOK"):
                            begin_count = True
                        continue  
                    contents = contents.replace('—', ' - ')
                    contents = contents.replace('“', '"')
                    contents = contents.replace('”', '"')
                    contents = contents.replace('‘', "'")
                    contents = contents.replace('’', "'")

                    fixed_contents = contents.translate(punct_table)

                    fixed_contents = fixed_contents.lower()

                    words = fixed_contents.split()

                    for word in words:
                        if word: 
                            if word in self.__frequency: 
                                self.__frequency[word] += 1
                            else:
                                self.__frequency[word] = 1 

            return True

        except FileNotFoundError:
            print(f"Sorry, the file {self.__filepath} does not exist.")
            return False

    def print_report(self):
        sorted_content = sorted(self.__frequency.keys())

        for word in sorted_content:
            print(f"{word} :: {self.__frequency[word]}")