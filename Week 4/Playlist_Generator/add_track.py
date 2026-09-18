def add_track(artist_input, song_title_input, playlist_list):
    """adds track to the playlist"""
    artist = artist_input
    song_title = song_title_input

    if not artist or not song_title:
        print("Please enter at least one artist and song title.")
        return False
    
    track = f"{song_title} - {artist}"
    playlist_list.append(track)
    print(f"Added: '{track}' to your playlist.")

    return True
