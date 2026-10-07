"""
Music Collection Manager 3.9
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
    To Do: a single space still shows all albums.
3.9 Fixed issue with a single space showing all albums. Now it only shows albums with no title.
    To Do: correct search for albums (to start) so that searches are exact word matches 
           ("an" returns only albums with "an" in the title, not "and" or "another", but not JUST the word "an").

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

        # added track number PLUS error handling for missing track numbers, 
        # if there's no Order value, it displays 00, copied from below.
        initial_order = song.get("Order", "0")
        if not initial_order or initial_order == {}:
            fixed_order = "00"
        else:
            fixed_order = initial_order if isinstance(initial_order, str) else str(initial_order)

        # prints the song information
        print("") # Spacing line
        print(f"- Song Title: {song.get('Title')}")
        print(f"Artist: {song.get('Artist')}")
        print(f"Album: {album_name}",)
        print(f"Track Number: {fixed_order}")

def search_by_album(db, query):
    """
    Searches for albums in the database by title.
    """

    # this looks at the JSON file for the Songs.Song information and Albums.Album information.

    albums = db.get("Albums", {}).get("Album", [])
    songs = db.get("Songs", {}).get("Song", [])

    # loops through all the albums looking for a match to the text the user entered.
    # matches = [
    #     a for a in albums 
    #     if query.lower() in (
    #         a.get("Title", "") if isinstance(a.get("Title"), str) 
    #         else str(a.get("Title", ""))
    #     ).lower()
    # ]

    # trying to correctly handle albums with no title, so that they can be searched for by the user.

    matches = []
    for a in albums:
        title_value = a.get("Title", "")
        is_blank_title = not title_value or title_value == {}

        clean_query = query.strip().lower()

        is_query_blank = query == "" or query.isspace()

        if is_blank_title and (clean_query in ["none", "blank", "no album name", ""] or is_query_blank):
            matches.append(a)
            # fixed the issue with searching for albums with no title, 
            # but it now displays ALL albums, not just the ones with no title when using a single space.
        elif not is_blank_title:
            if not is_query_blank:

            # if query.strip() != "":
                title_str = title_value if isinstance(title_value, str) else str(title_value)
                if clean_query in title_str.lower():

                # if query.lower() in title_str.lower():
                    matches.append(a)

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

        # trying to refactor to handle various artists on an album
        album_artist = album.get("AlbumArtist", "")

        # needed to modify this as part of the blank album title support
        basic_title = album.get("Title", "")
        if not basic_title or basic_title == {}:
            album_title = "" # blank album title
        else:
            album_title = basic_title if isinstance(basic_title, str) else str(basic_title)

        # similar code as that under the artist selection
        song_info = []
        for s in songs:
            song_album = s.get("Album")
            if isinstance(song_album, dict) and song_album.get("-id") == album_id:
                initial_order = s.get("Order", "0")
                if not initial_order or initial_order == {}:
                    fixed_order = "00"
                else:
                    fixed_order = initial_order if isinstance(initial_order, str) else str(initial_order)

                # grab the artist for each track for "various artists" albums
                track_artist = s.get("Artist", "Unknown Artist")
                if isinstance(track_artist, dict):
                    track_artist = track_artist.get("#text", "Unknown Artist")

                song_info.append({
                    "order": fixed_order,
                    "title": s.get("Title") if isinstance(s.get("Title"), str) else str(s.get("Title", "")),
                    # save the artist for each track for "various artists" albums
                    "artist": str(track_artist)
                })

        # startwith "Various Artists - " to get the albums with various artists
        is_various = isinstance(album_artist, str) and album_artist.startswith("Various Artists - ")

        # this was causing the duplication of the track list when displaying albums with various artists.
        # it now shows the track list only once, with the artist for each track.
        # album_songs = [f"{s['order']}. {s['title']}" for s in song_info]

        album_songs = []

        for s in song_info:
            if is_various:
                album_songs.append(f"{s['order']}. {s['title']} by {s['artist']}")
            else:
                album_songs.append(f"{s['order']}. {s['title']}")

        tracks_display = ', '.join(album_songs) if album_songs else 'No tracks found'

        # prints the album information
        print("")  # Spacing line
        print(f"- Album Title: {album_title}")
        print(f"Artist: {album.get('AlbumArtist')}")
        print(f"Songs: {tracks_display}")

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
                album_title = "" # blank album title
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

                    # If there's no Order value, it now displays 00

                    initial_order = s.get("Order", "0")
                    if not initial_order or initial_order == {}:
                        fixed_order = "00"
                    else:
                        fixed_order = initial_order if isinstance(initial_order, str) else str(initial_order)

                    song_info.append({
                        "order": fixed_order,
                        "title": s.get("Title") if isinstance(s.get("Title"), str) else str(s.get("Title", ""))
                    })

            artist_songs = [f"{s['order']}. {s['title']}" for s in song_info]

            tracks_display = ', '.join(artist_songs) if artist_songs else 'No tracks found'
            print("")  # Spacing line
            # prints the artist, album, and song information
            print(f"- Artist Name: {artist.get('Name')}")
            print(f"Album: {album_title}")
            print(f"Songs: {tracks_display}")

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
        print("\n--- Music Collection Manager ---")
        print("1. Search Database\n2. Exit")
        menu_option = input("Enter choice (1-2): ").strip()

        # quit if option 2
        if menu_option == '2':
            print("\nGoodbye!\n")
            break

        # sub-menu
        elif menu_option == '1':
            sub_menu = input("\n1. Song, 2. Album (type 'none' for songs not on an album), 3. Artist\nSelect category: ").strip()
            q = input("Enter query: ").strip().lower()
            if q and sub_menu == '1':
                search_by_song(db, q)
            elif sub_menu == '2': # removed the q check here to allow searching for albums with no title
                # but it broke the search result. It now displays ALL albums, not just the ones with no title. 
                # to be fixed above in the search_by_album function.
                search_by_album(db, q)
            elif q and sub_menu == '3':
                search_by_artist(db, q)

if __name__ == "__main__":
    main()