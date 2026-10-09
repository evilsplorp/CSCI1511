"""
Helper Class that contains multiple functions
- Converts fields to a string and deals with missing value, None, or {}
- Handles missing or empty track numbers, defaulting to '00'
- Consolidates punctuation stuff that was in both search_by_song and _album
- Consolidates the matching logic and blank value stuff for song and album
"""

class MusicUtilities:
    def __init__(self):
        """
        Initialization.
        """
        pass

    def get_clean_string(self, value, default=""):
        """
        Converts fields to a string. Deals with missing value, None, or {}.
        """
        if not value or value == {}:
            return default
        return value if isinstance(value, str) else str(value)

    def extract_track_order(self, song):
        """
        Handles missing or empty track numbers, defaulting to '00'.
        """
        return self.get_clean_string(song.get("Order"), default="00")

    def normalize_and_tokenize(self, text):
        """
        Removes punctuation and splits text into a lowercase word list to handle whole-word matches.
        """
        text_lower = text.lower()
        punctuations = [".", ",", "!", "?", ";", ":", "'", '"', "(", ")", "[", "]", "{", "}", "-", "_"]
        for punctuation in punctuations:
            text_lower = text_lower.replace(punctuation, " ")
        return text_lower.split()

    def matches_query(self, item_title, query, blank_keywords):
        """
        Consolidates full-word match logic and handles blank keyword rules.
        """
        clean_query = query.strip().lower()
        is_query_blank = query == "" or query.isspace()
        is_blank_title = not item_title or item_title == {}

        if is_blank_title:
            return (clean_query in blank_keywords) or is_query_blank

        if not is_query_blank:
            title_str = self.get_clean_string(item_title)
            title_words = self.normalize_and_tokenize(title_str)
            query_words = clean_query.split()
            return all(word in title_words for word in query_words)

        return False
