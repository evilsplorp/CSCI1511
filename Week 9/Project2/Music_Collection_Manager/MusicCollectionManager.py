"""
Music Collection Manager 4.1
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

# shared refactoring helpers v 4.2

def get_clean_string(value, default=""):
    """
    converts fields to a string. deals with missing value, None, or {}
    """
    if not value or value == {}:
        return default
    return value if isinstance(value, str) else str(value)

def extract_track_order(song):
    """
    handles missing or empty track numbers, defaulting to '00'
    """
    return get_clean_string(song.get("Order"), default = "00")

# search functions

def search_by_song(db, query): 
    """
    Searches for songs in the database by title.
    """
    # this looks at the JSON file for the Songs.Song information.
    songs = db.get("Songs", {}).get("Song", [])

    clean_query = query.strip().lower()
    is_query_blank = query == "" or query.isspace()

    # loops through all the songs looking for a match to the text the user entered.
    # matches = [s for s in songs if query in s.get("Title", "").lower()]

    matches = []
    for s in songs:
        title_value = s.get("Title", "")
        is_blank_title = not title_value or title_value == {}

        if is_blank_title and (clean_query in ["none", "blank", "no song title"] or is_query_blank):
            matches.append(s)

        elif not is_blank_title:
            if not is_query_blank:
                title_str = title_value if isinstance(title_value, str) else str(title_value)
                song_title_words = title_str.lower()

                # need to fix issue with partial matches, so that "an" 
                # doesn't match "and" or "another", but does match "an".

                # Visual Studio Code auto-generated the punctation list below
                for punctuation in [".", ",", "!", "?", ";", ":", "'", '"', "(", ")", "[", "]", "{", "}", "-", "_"]:
                    song_title_words = song_title_words.replace(punctuation, " ")

                song_words = song_title_words.split()
                query_words = clean_query.split()

                all_words_match = True
                for word in query_words:
                    if word not in song_words:
                        all_words_match = False
                        break
                if all_words_match:
                    matches.append(s)

    # no match, print a message and return
    if not matches:
        print(f"\nNo songs found containing '{query}'.")
        return

    # sorting songs by title.
    sorting_pairs = []

    # mapping everything out and checking for blanks, lowercase
    for s in matches:
        raw_t = s.get("Title", "")
        clean_t = "" if (not raw_t or raw_t == {}) else str(raw_t).lower()

        # in case multiple songs have the same name (they will)
        song_id = str(s.get("-id"))

        # title, song_id, original dictionary
        sorting_pairs.append((clean_t, song_id, s))

    # built in sorting
    sorting_pairs.sort()

    # builds the list
    matches = [pair[2] for pair in sorting_pairs]
    # end sorting songs by title
    
    # matches found, print the results (and give a count)
    print(f"\nFound {len(matches)} matching song(s):")

    # go through the Album section of the JSON file and get the Album name for each song.
    for song in matches:
        album_info = song.get("Album", {})

        # no match, use "Unknown Album" as the album name
        album_name = album_info.get("#text", "Unknown Album") if isinstance(album_info, dict) else "Unknown Album"

        # added track number PLUS error handling for missing track numbers, 
        # if there's no Order value, it displays 00, copied from below.


        # v4.2 version
        fixed_order = extract_track_order(song)
        clean_song_title = get_clean_string(song.get("Title"), default = "No Song Name")

        # old, pre-4.2 version
        # initial_order = song.get("Order", "0")
        # if not initial_order or initial_order == {}:
        #     fixed_order = "00"
        # else:
        #     fixed_order = initial_order if isinstance(initial_order, str) else str(initial_order)

        # raw_song_title = song.get('Title', "")
        # clean_song_title = "No Song Name" if not raw_song_title or raw_song_title == {} else raw_song_title

        # prints the song information
        print("") # Spacing line
        print(f"- Song Title: {clean_song_title}")
        print(f"Artist: {song.get('Artist')}")
        print(f"Album: {album_name}",)
        print(f"Track Number: {fixed_order}")

def search_by_album(db, query):
    """
    Searches for albums in the database by title. 
    """

    albums = db.get("Albums", {}).get("Album", [])
    songs = db.get("Songs", {}).get("Song", [])

    matches = []
    for a in albums:
        title_value = a.get("Title", "")
        is_blank_title = not title_value or title_value == {}

        clean_query = query.strip().lower()
        is_query_blank = query == "" or query.isspace()

        if is_blank_title and (clean_query in ["none", "blank", "no album name"] or is_query_blank):
            matches.append(a)

        elif not is_blank_title:
            if not is_query_blank:
                title_str = title_value if isinstance(title_value, str) else str(title_value)
                album_title_words = title_str.lower()

                # need to fix issue with partial matches, so that "an" 
                # doesn't match "and" or "another", but does match "an".

                # Visual Studio Code auto-generated the punctation list below
                for punctuation in [".", ",", "!", "?", ";", ":", "'", '"', "(", ")", "[", "]", "{", "}", "-", "_"]:
                    album_title_words = album_title_words.replace(punctuation, " ")

                album_words = album_title_words.split()
                query_words = clean_query.split()

                all_words_match = True
                for word in query_words:
                    if word not in album_words:
                        all_words_match = False
                        break
                if all_words_match:
                    matches.append(a)

                # if clean_query in title_str.lower():
                #     matches.append(a)

    if not matches:
        print(f"\nNo albums found containing '{query}'.")
        return
    
    print(f"\nFound {len(matches)} matching album(s):")

    for album in matches:

        album_id = album.get("-id")
        album_artist = album.get("AlbumArtist", "")


        # pre - v4.2 version
        # basic_title = album.get("Title", "")
        # if not basic_title or basic_title == {}:
        #     album_title = "" # blank album title
        # else:
        #     album_title = basic_title if isinstance(basic_title, str) else str(basic_title)

        album_title = get_clean_string(album.get("Title"))

        song_info = []
        for s in songs:
            song_album = s.get("Album")
            if isinstance(song_album, dict) and song_album.get("-id") == album_id:

                # v4.2 version
                fixed_order = extract_track_order(s)
                track_artist = s.get("Artist", "Unknown Artist")
                if isinstance(track_artist, dict):
                    track_artist = track_artist.get("#text", "Unknown Artist")

                song_info.append({
                    "order": fixed_order,
                    "title": get_clean_string(s.get("Title")),
                    "artist": str(track_artist)
                })

                # pre-v4.2 version
                # initial_order = s.get("Order", "0")
                # if not initial_order or initial_order == {}:
                #     fixed_order = "00"
                # else:
                #     fixed_order = initial_order if isinstance(initial_order, str) else str(initial_order)

                # track_artist = s.get("Artist", "Unknown Artist")
                # if isinstance(track_artist, dict):
                #     track_artist = track_artist.get("#text", "Unknown Artist")

                # song_info.append({
                #     "order": fixed_order,
                #     "title": s.get("Title") if isinstance(s.get("Title"), str) else str(s.get("Title", "")),
                #     "artist": str(track_artist)
                # })

        is_various = isinstance(album_artist, str) and album_artist.startswith("Various Artists - ")

        album_songs = []

        for s in song_info:
            if is_various:
                album_songs.append(f"{s['order']}. {s['title']} by {s['artist']}\n")
            else:
                album_songs.append(f"{s['order']}. {s['title']}\n")

        tracks_display = ''.join(album_songs) if album_songs else 'No tracks found'

        print("")  # Spacing line
        print(f"- Album Title: {album_title}")
        print(f"Artist: {album.get('AlbumArtist')}")
        print(f"Songs:\n{tracks_display}")

def search_by_artist(db, query):
    """
    Searches for artists in the database by name.
    """

    artists = db.get("Artists", {}).get("Artist", [])
    albums = db.get("Albums", {}).get("Album", [])
    songs = db.get("Songs", {}).get("Song", [])

    matches = [a for a in artists if query in a.get("Name", "").lower()]

    if not matches:
        print(f"\nNo artists found containing '{query}'.")
        return

    print(f"\nFound {len(matches)} matching artist(s):")

    for artist in matches:

        artist_name = artist.get("Name")

        # need to collect albums that have multiple artists and 
        # find ones with multiple artists on a single track

        # need an empty list
        multiple_artist_albums = []
        for s in songs:
            song_artist = s.get("Artist", "")

            # check the artist field and split on ; and strip trailing spaces
            artists_list = [name.strip() for name in str(song_artist).split(";")] if song_artist else []

            # check for matching artists in the search and connect it to the album

            if artist_name in artists_list and isinstance(s.get("Album"), dict):
                compiled_id = s["Album"].get("-id")
                if compiled_id and compiled_id not in multiple_artist_albums:
                    multiple_artist_albums.append(compiled_id)

        # matching_albums = [a for a in albums if a.get("AlbumArtist") == artist_name]

        # need an empty list
        matching_albums = []

        for a in albums:
            is_main_artist = a.get("AlbumArtist") == artist_name
            is_compiliation_appeareance = a.get("-id") in multiple_artist_albums

            if is_main_artist or is_compiliation_appeareance:
                matching_albums.append(a)

        print("")  # Spacing line for artist header
        print(f"- Artist Name: {artist_name}")

        if not matching_albums:
            print("Albums: none")
            continue


        for album in matching_albums:
            album_id = album.get("-id")


            # v4.2 version
            album_title = get_clean_string(album.get("Title"))

            # pre-v4.2 version
            basic_title = album.get("Title", "")
            # if not basic_title or basic_title == {}:
            #     album_title = "" 
            # else: 
            #     album_title = basic_title if isinstance(basic_title, str) else str(basic_title)

            song_info = []
            for s in songs:
                song_album = s.get("Album")
                song_artist = s.get("Artist", "")

                # split the track artists to get ones with multiple artists

                track_artists = [name.strip() for name in str(song_artist).split(";")] if song_artist else []

                # if the artist name shows up in the above and there's a matchiing song on the album...
                if (
                    artist_name in track_artists
                    and isinstance(song_album, dict)
                    and song_album.get("-id") == album_id
                ):


                    # V4.2 version
                    fixed_order = extract_track_order(s)
                    song_info.append({
                        "order": fixed_order,
                        "title": get_clean_string(s.get("Title"))
                    })

                    # pre-V4.2 version
                    # initial_order = s.get("Order", "0")
                    # if not initial_order or initial_order == {}:
                    #     fixed_order = "00"
                    # else:
                    #     fixed_order = initial_order if isinstance(initial_order, str) else str(initial_order)

                    # song_info.append({
                    #     "order": fixed_order,
                    #     "title": s.get("Title") if isinstance(s.get("Title"), str) else str(s.get("Title", ""))
                    # })

            artist_songs = [f"{s['order']}. {s['title']}\n" for s in song_info]

            tracks_display = ''.join(artist_songs) if artist_songs else 'No tracks found'
            print("")  # Spacing line
            # print(f"- Artist Name: {artist.get('Name')}")
            print(f"Album: {album_title}")
            print(f"Songs:\n{tracks_display}")

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
        # updated menu to prevent invalid selections
        print("\n--- Music Collection Manager ---")
        print("1. Search Database\n2. Exit")
        menu_option = input("Enter choice (1-2): ").strip()

        # quit if option 2
        if menu_option == '2':
            print("\nGoodbye!\n")
            break

        # sub-menu
        elif menu_option == '1':

            while True:
                print("\n-=-=-= Search Categories =-=-=-")
                print("\n1. Song, 2. Album (type 'none' for songs not on an album), 3. Artist\n")
                sub_menu = input("Select Category (1, 2, or 3): ").strip()

                if sub_menu in ['1', '2', '3']:
                    break
                else:
                    print("\nPlease choose 1, 2, or 3.")

            q = input("Enter query: ").strip().lower()
                
            if q and sub_menu == '1':
                search_by_song(db, q)
            elif sub_menu == '2': # removed the q check here to allow searching for albums with no title
                # but it broke the search result. It now displays ALL albums, not just the ones with no title. 
                # to be fixed above in the search_by_album function.
                search_by_album(db, q)
            elif q and sub_menu == '3':
                search_by_artist(db, q)
        else:
            print("\nPlease enter 1 or 2.")

if __name__ == "__main__":
    main()