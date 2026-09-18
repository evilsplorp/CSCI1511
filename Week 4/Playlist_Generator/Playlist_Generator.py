"""
Playlist_Generator 1.7
Raymond Black
Creates a song playlist based on user input
<<<<<<< HEAD
Resources: used examples from the readings and from the lecture;
Google searches & 'Python for Kids' book to determine how to make 
some minor changes;
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