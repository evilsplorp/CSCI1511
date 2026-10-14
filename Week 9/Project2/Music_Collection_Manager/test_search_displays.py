import pytest
from search_utilities import MusicUtilities
from search_displays import SearchDisplays

@pytest.fixture
def displays():
    """
    Provides a clean SearchDisplays instance.
    """
    utils = MusicUtilities()
    return SearchDisplays(utils)

@pytest.fixture
def mock_db():
    """
    Build a clean mock database fixture before each test.
    This is an extract from the actual JSON file.
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
        "Artists": {
            "Artist": [
                {
                    "-id": "Artist_957", "Name": "The Beatles"
                }
            ]

        }
    }

def test_song_search_execution(displays, mock_db):
    """
    Test that song_search runs without raising any exceptions.
    """
    try:
        song_list = mock_db.get("Songs", {}).get("Song", [])
        displays.song_search(query="come", matches=song_list)
        success = True
    except Exception as e:
        success = False
        print(f"song_search crashed: {e}")
        
    assert success is True

def test_album_search_execution(displays, mock_db):
    """
    Test that album_search runs without raising any exceptions.
    """
    try:
        song_list = mock_db.get("Songs", {}).get("Song", [])
        album_list = mock_db.get("Albums", {}).get("Album", [])
        
        displays.album_search(
            query="abbey", 
            songs=song_list, 
            matches=album_list
        )
        success = True
    except Exception as e:
        success = False
        print(f"album_search crashed: {e}")
        
    assert success is True

def test_artist_search_execution(displays, mock_db):
    """
    Test that artist_search runs without raising any exceptions.
    """
    try:
        artist_list = mock_db.get("Artists", {}).get("Artist", [])
        album_list = mock_db.get("Albums", {}).get("Album", [])
        song_list = mock_db.get("Songs", {}).get("Song", [])

        displays.artist_search(
            query="beatles", 
            albums=album_list, 
            songs=song_list, 
            matches=artist_list
        )
        success = True
    except Exception as e:
        success = False
        print(f"artist_search crashed: {e}")
        
    assert success is True

def test_search_with_no_matches_execution(displays):
    """
    Test that functions gracefully handle empty search matches without crashing.
    """
    try:
        displays.song_search(query="Missing", matches=[])
        displays.album_search(query="Missing", songs=[], matches=[])
        displays.artist_search(query="Missing", albums=[], songs=[], matches=[])
        success = True
    except Exception:
        success = False
        
    assert success is True