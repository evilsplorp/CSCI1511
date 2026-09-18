"""
Playlist_Generator 1.5
Raymond Black
Creates a song playlist based on user input
Resources: used examples from the readings and from the lecture on 2026-09-09 v1.0;
did a Google search to figure out how to push the user back to the top (continue) v1.2;
added a limit to the playlist (mostly so I could add a new if/else) v1.2;
found a way to add numbers to the song list when it prints v1.3;
added notations indicating what version added a feature v1.3
correct playlist creation limit if statement v1.4
updated creation limit, more music if statement with a while loop v1.5
extracted adding tracks to a function and put in separate file v1.6
extracting yes/no to add more to a separate function file v1.7
2026-09-18
"""

import random
from add_track import add_track
from more_songs import more_tunes

playlist = []

print("--- Create a playlist of up to 5 artists and songs ---")

getting_songs = True
while getting_songs:

    artist = input("\nEnter the artist name: ").strip()
    song_title = input("Enter the song title: ").strip()

    if not add_track(artist, song_title, playlist):
        continue
    if len(playlist) < 5:
         if not more_tunes():
              getting_songs = False
    else:
            print("\nThat's 5 songs!")
            getting_songs = False

random.shuffle(playlist)
print("\nShuffled Playlist")
for number, current_track in enumerate(playlist, start=1):# add numbers to the tracks v1.3
    print(f"{number}. 🎵 {current_track}")