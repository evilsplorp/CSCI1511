"""
Music Collection Manager 4.7
Raymond Black
A searchable JSON file of artists, albums, and songs;  
1.0 gets the JSON file and checks for errors. 
It only supports searching by song title.
2.0 adds searching by album title and shows the songs on that album.
3.0 added searching by artist name and shows the albums and songs for that artist.
3.1 added track numbers to the song list for each artist.
3.2 added error handling for missing album names.
3.3 added error handling for missing track numbers.
3.4 added track number info (along with error handling) to the song search results.
3.5 added temp fix for missing album names in the sub-menu. 
    added track numbers to the album search results (with error handling for missing track numbers).
    To Do: address issue with various artists being on the same album. Search for Bill & Ted for example - DONE
3.6 added support for various artists on an album. It now shows the artist for each track on the album.
    To Do: There's an issue with duplication of the track list when displaying albums with various artists. - DONE
           It shows the track list twice, once with the artist and once without. Need to fix that. - Done
3.7 fixed duplication of the track list when displaying albums with various artists. 
    Now shows the track list only once, with the artist for each track.
    added support for searching for albums with no title. The user can search for "none", "blank", or "no album name" to find albums with no title.
    To Do: add support for just hitting enter to find albums with no title. - DONE
    To Do: there's an issue with "various artists" albums not showing all the tracks for that album.
3.8 Fixed issue with hitting enter to find albums with no title.
    To Do: a single space still shows all albums. - DONE
3.9 Fixed issue with a single space showing all albums. Now it only shows albums with no title.
    To Do: correct search for albums (to start) so that searches are exact word matches - DONE
           ("an" returns only albums with "an" in the title, not "and" or "another", but not JUST the word "an").
4.0 Fixed issue with album search so that searches are exact word matches.
    Fixed issue with song search so that searches are exact word matches.
    Note: Not applying this to artists, as I want Tom to bring up Tom and Tommmy, for example.
    BUGFIX: multiple artists on a track are not showing in results, but are being counted separately. - DONE
    Addressed display formatting when multiple songs are displayed.
    To Do: Sort song search by Song Title - DONE
4.1 Song search now sorts alphabetically
    To Do: Extract functions to classes. 
    To Do: Add any helper functions that can be shared across the code.
4.2 Refactoring starts. 
    Added functions to convert fields to a string and deal with missing value, None, or {} AND
    Handle missing or empty track numbers, defaulting to '00'
    Updated menu to prevent invalid entries
4.3 Additional refactoring
    Consolidated punctuation stuff that was in both search_by_song and _album
4.4 Additional refactoring
    Consolidates the matching logic and blank value stuff for song and album
4.5 Additional refactoring
    Extracted helper functions to a separate Class file (search_utilities)
    Updated main app file to call the Class
4.6 Additional refactoring
    Extracted search functions to a separate Class file (search_displays)
    Updated main app file to call the Class
    Extracted menu to a separate Class file (menu)
    Updated main app to call the Class
4.7 Added option to select from different JSON files to show the try-except handling

Stretch goal 1:
Allow the user to add new artists, albums, and songs to the JSON file

Stretch goal 2:
Allow the user to delete artists, albums, and songs from the JSON file

2026-10-14
"""

from pathlib import Path
import json
from search_utilities import MusicUtilities
from search_displays import SearchDisplays
from menu import Menu

# v4.5 instance of the class
utilities = MusicUtilities()
# v4.6 instance of the class
displays = SearchDisplays(utilities)

def load_music_database(file_path):
    """
    Loads the JSON music database and check for errors.
    """
    if not file_path.exists():
        print(f"\nError: The music database file '{file_path}' does not exist.\n")
        return None
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
            return data.get("MusicDatabase", data)
        except json.JSONDecodeError:
            print(f"\nError: The music database file '{file_path}' is not a valid JSON.\n")
            return None

def search_by_song(db, query): 
    """
    Searches for songs in the database by title.
    """
    songs = db.get("Songs", {}).get("Song", [])

    # v4.4 refactor
    blank_keywords = ["none", "blank", "no song title"]
    # v4.5 refactor update. added 'utilities.' for the function
    matches = [s for s in songs if utilities.matches_query(s.get("Title"), query, blank_keywords)]

    return displays.song_search(query, matches)

def search_by_album(db, query):
    """
    Searches for albums in the database by title. 
    """

    albums = db.get("Albums", {}).get("Album", [])
    songs = db.get("Songs", {}).get("Song", [])

    # v4.4 refactor
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
    base_dir = Path(__file__).parent
    files_map = {
        "1": ("music.json", base_dir / "music.json"),
        "2": ("bad_music.json", base_dir / "bad_music.json"),
        "3": ("fake_music.json", base_dir / "fake_music.json")
    }

    # v4.7 addition: Prompt user for JSON file
    while True:
        print("\n--- Music File Selector ---")
        print("1. Load Option 1 (music.json)")
        print("2. Load Option 2 (bad_music.json)")
        print("3. Load Option 3 (fake_music.json)")
        file_choice = input("Select music database (1-3): ").strip()

        if file_choice in files_map:
            filename, chosen_path = files_map[file_choice]
            print(f"\nLoading music file: '{filename}'...")
            break
        print("Invalid choice. Please select option 1, 2, or 3.")

    # Execute your existing database load logic using the chosen path profile
    db = load_music_database(chosen_path)

    # Halt initialization if error-handling logic catches validation drops
    if db is None:
        print("Exiting program due to database load failure.\n")
        return

    # pre-v4.7 version
    # file_path = Path(__file__).parent / 'music.json'
    # db = load_music_database(file_path)
    # if db is None:
    #     print("Exiting program due to database load failure.\n")
    #     return

    # v4.6 sets up menu object
    menu = Menu(search_by_song, search_by_album, search_by_artist)

    # v4.6 refactor update. calling menu
    menu.mcm_menu(db)

if __name__ == "__main__":
    main()