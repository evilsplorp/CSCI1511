"""
Music Collection Manager 3.1
Raymond Black
A searchable JSON file of artists, albums, and songs; 
1.0 gets the JSON file and checks for errors. 
It only supports searching by song title.
2.0 adds searching by album title and shows the songs on that album.
3.0 added searching by artist name and shows the albums and songs for that artist.
3.1 added track numbers to the song list for each artist.
3.2 added error handling for missing album names.

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
    # this looks at the JSON file for the Songs.Song information.
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

def search_by_album(db, query):
    """
    Searches for albums in the database by title.
    """

    # this looks at the JSON file for the Songs.Song information and Albums.Album information.

    albums = db.get("Albums", {}).get("Album", [])
    songs = db.get("Songs", {}).get("Song", [])

    # loops through all the albums looking for a match to the text the user entered.
    matches = [
        a for a in albums 
        if query.lower() in (
            a.get("Title", "") if isinstance(a.get("Title"), str) 
            else str(a.get("Title", ""))
        ).lower()
    ]

    # no match, print a message and return
    if not matches:
        print(f"\nNo albums found containing '{query}'.")
        return
    
    # prints how many matches were found
    print(f"\nFound {len(matches)} matching album(s):")

    for album in matches:

        # grabs the unique album ID and title, then finds all songs that 
        # belong to that album by matching the album ID.
        album_id = album.get("-id")
        album_title = album.get("Title")
        album_songs = [
            s.get("Title") for s in songs
            if isinstance(s.get("Album"), dict) and s["Album"].get("-id") == album_id
        ]

        # prints the album information
        print("")  # Spacing line
        print(f"- Album Title: {album.get('Title')}")
        print(f"Artist:      {album.get('AlbumArtist')}")
        print(f"Songs:  {', '.join(album_songs) if album_songs else 'No tracks found'}")

def search_by_artist(db, query):
    """
    Searches for artists in the database by name.
    """

    # this looks at the JSON file for the Artists.Artist information,
    # Albums.Album information, and Songs.Song information.
    artists = db.get("Artists", {}).get("Artist", [])
    albums = db.get("Albums", {}).get("Album", [])
    songs = db.get("Songs", {}).get("Song", [])

    # loops through all the artists looking for a match to the text the user entered.
    matches = [a for a in artists if query in a.get("Name", "").lower()]

    # no match, print a message and return
    if not matches:
        print(f"\nNo artists found containing '{query}'.")
        return

    # prints how many matches were found
    print(f"\nFound {len(matches)} matching artist(s):")

    for artist in matches:
        # grabs the artist name, then finds all albums and songs that 
        # belong to that artist by matching the artist name.
        artist_name = artist.get("Name")

        # grab the full Album info to grab the album ID for matching songs
        matching_albums = [a for a in albums if a.get("AlbumArtist") == artist_name]

        # artist_albums = [a.get("Title") for a in albums if a.get("AlbumArtist") == artist_name]

        # I wanted to add track numbers to the song list 
        # also wanted to make sure that the songs were correctly
        # associated with the album

        for album in matching_albums:
            # grab the ID of the album to match with songs
            album_id = album.get("-id")

            basic_title = album.get("Title", "")
            # some albums have no title, so we need a default value
            if not basic_title or basic_title == {}:
                album_title = "No Album Name"
            else: 
                album_title = basic_title if isinstance(basic_title, str) else str(basic_title)

            song_info = []
            for s in songs:
                song_album = s.get("Album")
                
                # Make sure the Album is a dictionary AND actually has a valid, matching -id
                if (
                    s.get("Artist") == artist_name 
                    and isinstance(song_album, dict) 
                    and song_album.get("-id") == album_id
                ):

                    # something broken about here. If there's no Order, it displays {}                    
                    song_info.append({
                        "order": s.get("Order", "0"),
                        "title": s.get("Title") if isinstance(s.get("Title"), str) else str(s.get("Title", ""))
                    })


        # song_info = [
        #     {
        #         # order is the track number, title is the song title
        #         "order": s.get("Order", "0"),
        #         "title": s.get("Title") if isinstance(s.get("Title"), str) else str(s.get("Title", ""))
        #     }
        #     for s in songs if s.get("Artist") == artist_name
        # ]

            artist_songs = [f"{s['order']}. {s['title']}" for s in song_info]

            # artist_songs = [s.get("Title") for s in songs if s.get("Artist") == artist_name]

            tracks_display = ', '.join(artist_songs) if artist_songs else 'No tracks found'
            print("")  # Spacing line
            # prints the artist, album, and song information
            print(f"- Artist Name: {artist.get('Name')}")
            print(f"Albums:      {album_title}")
            print(f"Songs:       {tracks_display}")

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
            print("\nGoodbye!\n")
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