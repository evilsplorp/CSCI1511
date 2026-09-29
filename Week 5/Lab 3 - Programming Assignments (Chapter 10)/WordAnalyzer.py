"""
WordAnalyzer Class for Word Counter
Raymond Black
Purpose: to count all the words in a file
and display how many times each word appears.

initial work used: 
code from example in reading. had it saved locally.
converted it to a Class
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
            punct_table = str.maketrans('', '', extended_punctuation)

            # handles the counting
            cleaned_contents = contents.translate(punct_table).lower()
            words = cleaned_contents.split()
            word_counts = Counter(words)

            # list all the words and their counts
            for word in sorted(word_counts):
                print(f"{word}: {word_counts[word]}")