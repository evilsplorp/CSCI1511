import pytest
from search_utilities import MusicUtilities

@pytest.fixture
def utilities():
    """
    Provides a clean MusicUtilities instance to all tests.
    (This replaces the unittest setUp method)
    """
    return MusicUtilities()

def test_get_clean_string_with_dict(utilities):
    """
    Test that an empty dictionary {} returns the default fallback string.
    """
    result = utilities.get_clean_string({}, default="No Name")
    assert result == "No Name"

def test_extract_track_order_empty(utilities):
    """
    Test that a track missing an order index safely defaults to '00'.
    """
    song = {"Title": "Under Pressure"}
    result = utilities.extract_track_order(song)
    assert result == "00"

def test_normalize_and_tokenize_punctuation(utilities):
    """
    Test that punctuation is completely stripped out and lowercased.
    """
    dirty_title = "Help! (A Night... At The Opera?)"
    expected_words = ["help", "a", "night", "at", "the", "opera"]
    
    result = utilities.normalize_and_tokenize(dirty_title)
    assert result == expected_words
