"""
Music Collection Manager 1.0
Raymond Black
A searchable JSON file of artists, albums, and songs; 
1.0 gets the JSON file and checks for errors. 
It only supports searching by song title.

Stretch goal 1:
Allow the user to add new artists, albums, and songs to the JSON file

Stretch goal 2:
Allow the user to delete artists, albums, and songs from the JSON file

2026-10-05
"""

from pathlib import Path
import json

def load_music_database(file_path):
    """
    Loads the JSON music database and check for errors.
    """
    if not file_path.exists():
        # exit the program if the file does not exist
        print(f"\nError: The music database file '{file_path}' does not exist.\n")
        return None
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
            return data.get("MusicDatabase", data)
        except json.JSONDecodeError:
            # exit the program if the file is not a valid JSON
            print(f"\nError: The music database file '{file_path}' is not a valid JSON.\n")
            return None

def search_by_song(db, query): 
    """
    Searches for songs in the database by title.
    """
    # this function looks at the JSON file for the Songs.Song information.
    songs = db.get("Songs", {}).get("Song", [])

    # loops through all the songs looking for a match to the text the user entered.
    matches = [s for s in songs if query in s.get("Title", "").lower()]

    # no match, print a message and return
    if not matches:
        print(f"\nNo songs found containing '{query}'.")
        return
    # matches found, print the results (and give a count)
    print(f"\nFound {len(matches)} matching song(s):")

    # go through the Album section of the JSON file and get the Album name for each song.
    for song in matches:
        album_info = song.get("Album", {})

        # no match, use "Unknown Album" as the album name
        album_name = album_info.get("#text", "Unknown Album") if isinstance(album_info, dict) else "Unknown Album"

        # prints the song information
        print("") # Spacing line
        print(f"- Song Title: {song.get('Title')}")
        print(f"Artist:     {song.get('Artist')}")
        print(f"Album:      {album_name}",)


def main():
    """
    Main function to run the Music Collection Manager.    
    """

    # file location
    file_path = Path(__file__).parent / 'music.json'

    # run the load_music_database function to get the database
    db = load_music_database(file_path)

    # if there's no file or the format isn't JSON, exit the program with a message
    if db is None:
        print("Exiting program due to database load failure.\n")
        return

    while True:

        # simple menu for the user to select options
        print("--- Music Collection Manager ---")
        print("1. Search Database\n2. Exit")
        menu_option = input("Enter choice (1-2): ").strip()

        # quit if option 2
        if menu_option == '2':
            print("Goodbye!")
            break

        # sub-menu
        elif menu_option == '1':
            sub_menu = input("\n1. Song, 2. Album, 3. Artist\nSelect category: ").strip()
            q = input("Enter query: ").strip().lower()
            if q and sub_menu == '1':
                search_by_song(db, q)
            elif q and sub_menu == '2':
                search_by_album(db, q)
            elif q and sub_menu == '3':
                search_by_artist(db, q)

if __name__ == "__main__":
    main()