"""
Search functions
- Searches JSON for songs that contain a search term
    - returns song title, artist, and album that contains the song
- Searches JSON for albums that contain a search term
    - returns album name, artist, and songs contained on the album
- Searches JSON for artists that contain a search term (partial searches, too)
    - returns albums on which the artist has a song and song titles
"""

class SearchDisplays:
    def __init__(self, utilities_instance):
        """
        Stores the utility reference so we can use its 
        formatting methods (like extract_track_order).
        """
        self.utilities = utilities_instance

    def song_search(self, query, matches):
        """
        Song search processing
        """
        if not matches:
            print(f"\nNo songs found containing '{query}'.")
            return

        sorting_pairs = []
        for s in matches:
            # v4.5 refactor update. added 'utilities.' for the function
            # v4.6 refactor update. added self for separate Class file
            clean_t = self.utilities.get_clean_string(s.get("Title")).lower()
            song_id = str(s.get("-id"))
            sorting_pairs.append((clean_t, song_id, s))

        sorting_pairs.sort()
        matches = [pair[2] for pair in sorting_pairs]
        
        print(f"\nFound {len(matches)} matching song(s):")

        for song in matches:
            album_info = song.get("Album", {})
            album_name = album_info.get("#text", "Unknown Album") if isinstance(album_info, dict) else "Unknown Album"

            # v4.2 version
            # v4.5 refactor update. added 'utilities.' for the function
            # v4.6 refactor update. added self for separate Class file
            fixed_order = self.utilities.extract_track_order(song)
            clean_song_title = self.utilities.get_clean_string(song.get("Title"), default = "No Song Name")

            print("")
            print(f"- Song Title: {clean_song_title}")
            print(f"Artist: {song.get('Artist')}")
            print(f"Album: {album_name}",)
            print(f"Track Number: {fixed_order}")

    def album_search(self, query, songs, matches):
        """
        Album search processing
        """
        if not matches:
            print(f"\nNo albums found containing '{query}'.")
            return
        
        print(f"\nFound {len(matches)} matching album(s):")

        for album in matches:
            album_id = album.get("-id")
            album_artist = album.get("AlbumArtist", "")
            # v4.5 refactor update. added 'utilities.' for the function
            # v4.6 refactor update. added self for separate Class file
            album_title = self.utilities.get_clean_string(album.get("Title"))

            song_info = []
            for s in songs:
                song_album = s.get("Album")
                if isinstance(song_album, dict) and song_album.get("-id") == album_id:
                    # v4.2 version
                    # v4.5 refactor update. added 'utilities.' for the function
                    # v4.6 refactor update. added self for separate Class file
                    fixed_order = self.utilities.extract_track_order(s)
                    track_artist = s.get("Artist", "Unknown Artist")
                    if isinstance(track_artist, dict):
                        track_artist = track_artist.get("#text", "Unknown Artist")

                    song_info.append({
                        "order": fixed_order,
                        # v4.5 refactor update. added 'utilities.' for the function
                        # v4.6 refactor update. added self for separate Class file
                        "title": self.utilities.get_clean_string(s.get("Title")),
                        "artist": str(track_artist)
                    })

            is_various = isinstance(album_artist, str) and album_artist.startswith("Various Artists - ")
            album_songs = []

            for s in song_info:
                if is_various:
                    album_songs.append(f"{s['order']}. {s['title']} by {s['artist']}\n")
                else:
                    album_songs.append(f"{s['order']}. {s['title']}\n")

            tracks_display = ''.join(album_songs) if album_songs else 'No tracks found'

            print("")
            print(f"- Album Title: {album_title}")
            print(f"Artist: {album.get('AlbumArtist')}")
            print(f"Songs:\n{tracks_display}")

    def artist_search(self, query, albums, songs, matches):
        if not matches:
            print(f"\nNo artists found containing '{query}'.")
            return

        print(f"\nFound {len(matches)} matching artist(s):")

        for artist in matches:
            artist_name = artist.get("Name")

            multiple_artist_albums = []
            for s in songs:
                song_artist = s.get("Artist", "")
                artists_list = [name.strip() for name in str(song_artist).split(";")] if song_artist else []

                if artist_name in artists_list and isinstance(s.get("Album"), dict):
                    compiled_id = s["Album"].get("-id")
                    if compiled_id and compiled_id not in multiple_artist_albums:
                        multiple_artist_albums.append(compiled_id)
            matching_albums = []

            for a in albums:
                is_main_artist = a.get("AlbumArtist") == artist_name
                is_compiliation_appeareance = a.get("-id") in multiple_artist_albums

                if is_main_artist or is_compiliation_appeareance:
                    matching_albums.append(a)

            print("")
            print(f"- Artist Name: {artist_name}")

            if not matching_albums:
                print("Albums: none")
                continue

            for album in matching_albums:
                album_id = album.get("-id")

                # v4.2 version
                # v4.5 refactor update. added 'utilities.' for the function
                # v4.6 refactor update. added self for separate Class file
                album_title = self.utilities.get_clean_string(album.get("Title"))

                song_info = []
                for s in songs:
                    song_album = s.get("Album")
                    song_artist = s.get("Artist", "")
                    track_artists = [name.strip() for name in str(song_artist).split(";")] if song_artist else []

                    if (
                        artist_name in track_artists
                        and isinstance(song_album, dict)
                        and song_album.get("-id") == album_id
                    ):
                        # V4.2 version
                        # v4.5 refactor update. added 'utilities.' for the function
                        # v4.6 refactor update. added self for separate Class file
                        fixed_order = self.utilities.extract_track_order(s)
                        song_info.append({
                            "order": fixed_order,
                            # v4.5 refactor update. added 'utilities.' for the function
                            # v4.6 refactor update. added self for separate Class file
                            "title": self.utilities.get_clean_string(s.get("Title"))
                        })

                artist_songs = [f"{s['order']}. {s['title']}\n" for s in song_info]

                tracks_display = ''.join(artist_songs) if artist_songs else 'No tracks found'
                print("")
                print(f"Album: {album_title}")
                print(f"Songs:\n{tracks_display}")