"""
Playlist_Generator 1.1
Raymond Black
Creates a song playlist based on user input
Resources: used examples from the readings and from the lecture on 2026-09-09
2026-09-10
"""

# I wanted the ability to randomize the tracks when it printed them out. 
import random

# empty list for playlist items
playlist = []

print("--- Create a playlist ---")

# loop to get songs/artists
getting_songs = True
while getting_songs:

    # input artist and song; added the strip() to remove leading and trailing spaces.
    artist = input("\nEnter the artist name: ").strip()
    song_title = input("Enter the song title: ").strip()

    # make it a single value to put in the list
    track = f"{song_title} - {artist}"
    playlist.append(track)
    print(f"Added: '{track} to your playlist.")

    # Ask for more songs
    more_music = input("\nAdd more music? (yes/no): ").lower()

    # Adding more music or not?
    if more_music != 'yes' and more_music != 'y':
        getting_songs = False

# display the playlist

# make sure they entered some songs
if len(playlist) == 0:
    print("I think you forget to enter some songs.")
else:
    # shuffle try 1
    random.shuffle(playlist)
    print("\nShuffled Playlist")
    for current_track in playlist:
        print(f"🎵 {current_track}")

# original code, to be removed before submitting project.
#     track_no = 1
#     for track in playlist:
#         print(f"{track_no}. {track}")
#         track_no += 1

# print("\n🎵 Here's your playlist! Enjoy! 🎵")



