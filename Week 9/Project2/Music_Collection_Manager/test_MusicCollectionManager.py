import pytest
from MusicCollectionManager import search_by_song, search_by_album, search_by_artist

@pytest.fixture
def mock_db():
    """
    Build a clean mock database fixture before each test.
    """
    return {
        "Songs": {
            "Song": [
                {"-id": "Song_3618", "Title": "Come Together", "Artist": "The Beatles", "Album": {
                 "-id": "Album_1489", "#text": "Abbey Road"
                 },
                 "Order": "01",
                 "AlbumArtist": "The Beatles"
                 },
                {"-id": "Song_3708", "Title": "Let It Be", "Artist": "The Beatles", "Album": {
                 "-id": "Album_1497", "#text": "Let It Be"
                 },
                 "Order": "6",
                 "AlbumArtist": "The Beatles"}
            ]
        },
        "Albums": {
            "Album": [
                {"-id": "Album_1497", "AlbumArtist": "The Beatles", "Title": "Let It Be"},
                {"-id": "Album_1491", "AlbumArtist": "The Beatles2", "Title": "Abbey Road"}
            ]
        },
        "Artist": {
            "Artist": [
                {
                    "-id": "Artist_957", "Name": "The Beatles"
                }
            ]

        }
    }

def test_search_by_song_passing(mock_db):
    """
    Test that searching for a valid keyword routes 
    and processes smoothly for songs.
    ."""
    try:
        search_by_song(mock_db, "together")
        search_is_successful = True
    except Exception:
        search_is_successful = False
        
    assert search_is_successful is True

def test_search_by_album_passing(mock_db):
    """
    Test that searching for a valid keyword routes 
    and processes smoothly for albums.
    """
    try:
        search_by_album(mock_db, "abbey")
        search_is_successful = True
    except Exception:
        search_is_successful = False
        
    assert search_is_successful is True

def test_search_by_artist_passing(mock_db):
    """
    Test that searching for a valid keyword 
    routes and processes smoothly for artists.
    """
    try:
        search_by_artist(mock_db, "beatles")
        search_is_successful = True
    except Exception:
        search_is_successful = False
        
    assert search_is_successful is True