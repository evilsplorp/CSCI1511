"""
Playlist_Generator 1.4
Raymond Black
Creates a song playlist based on user input
Resources: used examples from the readings and from the lecture on 2026-09-09 v1.0;
did a Google search to figure out how to push the user back to the top (continue) v1.2;
added a limit to the playlist (mostly so I could add a new if/else) v1.2;
found a way to add numbers to the song list when it prints v1.3;
added notations indicating what version added a feature v1.3
correct playlist creation limit if statement v1.4
2026-09-11
"""

# I wanted the ability to randomize the tracks when it printed them out v1.1. 
import random

# empty list for playlist items. I didn't use a dictionary to allow duplicate artists / songs v1.0
playlist = []

print("--- Create a playlist of up to 5 artists and songs ---")

# loop to get songs/artists v1.0
getting_songs = True
while getting_songs:

    # input artist and song; added the strip() to remove leading and trailing spaces v1.1.
    artist = input("\nEnter the artist name: ").strip()
    song_title = input("Enter the song title: ").strip()

    # added a catch to force at least once entry. This let me drop the last
    # if/else statement v1.2
    if not artist or not song_title:
        print("Please enter at least one artist and song title.")
        continue

    # make it a single value to put in the list v1.0
    track = f"{song_title} - {artist}"
    playlist.append(track)
    print(f"Added: '{track} to your playlist.")

    # Ask for more songs; added a limit v1.2
    # refactored, as the print statement would never print
    if len(playlist) < 5:
        more_music = input("\nAdd more music? (yes/no): ").lower()
    else:
        getting_songs = False

    # Adding more music or not? anything other than yes or y is a no v1.0
    if more_music != 'yes' and more_music != 'y':
        getting_songs = False

# display the playlist v1.0

# shuffle the songs v1.1
random.shuffle(playlist)
print("\nShuffled Playlist")
for number, current_track in enumerate(playlist, start=1):# add numbers to the tracks v1.3
    print(f"{number}. 🎵 {current_track}")