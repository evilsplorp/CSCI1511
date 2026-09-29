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
"""

from pathlib import Path
import string
from collections import Counter

class WordAnalyzer:
    def __init__(self):
                self.is_running = True
    def count_words(self, filename):
        """Count the approximate number of words in a file."""
        file_path = Path(filename)
        try:
            contents = file_path.read_text(encoding='utf-8')
        except FileNotFoundError:
            print(f"Sorry, the file {file_path} does not exist.")
            # to make it just ignore the failure, use pass
        else:
            # Count the approximate number of words in the file:

            # found code to start at specific location
            lines = contents.splitlines()
            start_index = 0
            
            for i, line in enumerate(lines):
                if line.startswith("*** START OF THE PROJECT GUTENBERG EBOOK"):
                    start_index = i + 1  # Begin on the line immediately after the marker
                    break
            
            # Rejoin only the text following the start marker
            valid_content = "\n".join(lines[start_index:])

            # Ran into another issues with em-dashes connecting words
            # punctuation code removal didn't work, so found an
            # alternative
            contents = valid_content.replace('—', ' - ')
            contents = contents.replace('“', '"')
            contents = contents.replace('”', '"')
            contents = contents.replace('‘', "'")
            contents = contents.replace('’', "'")

            # replaces the above characters with nothing.
            punct_table = str.maketrans('', '', string.punctuation)

            # handles the counting
            cleaned_contents = contents.translate(punct_table).lower()
            words = cleaned_contents.split()
            word_counts = Counter(words)

            # list all the words and their counts
            for word in sorted(word_counts):
                print(f"{word}: {word_counts[word]}")