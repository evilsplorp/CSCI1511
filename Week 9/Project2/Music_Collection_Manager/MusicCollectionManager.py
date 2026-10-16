"""
Music Collection Manager 5.0
Raymond Black
Allows selecting a JSON file (checks for validity and existence),
then allows searching that file by artists, albums, and songs.
2026-10-16
"""

from pathlib import Path
from search_utilities import MusicUtilities
from search_displays import SearchDisplays
from menu import Menu

utilities = MusicUtilities()
displays = SearchDisplays(utilities)

def search_by_song(db, query): 
    """
    Searches for songs in the database by title.
    """
    songs = db.get("Songs", {}).get("Song", [])
    blank_keywords = ["none", "blank", "no song title"]
    matches = [s for s in songs if utilities.matches_query(s.get("Title"), query, blank_keywords)]
    return displays.song_search(query, matches)

def search_by_album(db, query):
    """
    Searches for albums in the database by title. 
    """
    albums = db.get("Albums", {}).get("Album", [])
    songs = db.get("Songs", {}).get("Song", [])
    blank_keywords = ["none", "blank", "no album name"]
    matches = [a for a in albums if utilities.matches_query(a.get("Title"), query, blank_keywords)]
    return displays.album_search(query, songs, matches)

def search_by_artist(db, query):
    """
    Searches for artists in the database by name.
    """
    artists = db.get("Artists", {}).get("Artist", [])
    albums = db.get("Albums", {}).get("Album", [])
    songs = db.get("Songs", {}).get("Song", [])
    matches = [a for a in artists if query in a.get("Name", "").lower()]
    return displays.artist_search(query, albums, songs, matches)

def main():
    """
    Main function to run the Music Collection Manager.    
    """

    menu = Menu(search_by_song, search_by_album, search_by_artist)
    db = menu.select_and_load_db()
    menu.mcm_menu(db)

if __name__ == "__main__":
    main()