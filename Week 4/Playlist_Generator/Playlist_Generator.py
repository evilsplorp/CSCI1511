"""
Playlist_Generator 1.2
Raymond Black
Creates a song playlist based on user input
Resources: used examples from the readings and from the lecture on 2026-09-09;
did a Google search to figure out how to push the user back to the top (continue);
added a limit to the playlist (mostly so I could add a new if/else)
2026-09-11
"""

# I wanted the ability to randomize the tracks when it printed them out. 
import random

# empty list for playlist items. I didn't use a dictionary to allow duplicate artists / songs
playlist = []

print("--- Create a playlist ---")

# loop to get songs/artists
getting_songs = True
while getting_songs:

    # input artist and song; added the strip() to remove leading and trailing spaces.
    artist = input("\nEnter the artist name: ").strip()
    song_title = input("Enter the song title: ").strip()

    # added a catch to force at least once entry. This let me drop the last
    # if/else statement
    if not artist or not song_title:
        print("Please enter at least one artist and song title.")
        continue

    # make it a single value to put in the list
    track = f"{song_title} - {artist}"
    playlist.append(track)
    print(f"Added: '{track} to your playlist.")

    # Ask for more songs; added a limit 
    if len(playlist) == 5:
        print("There's a limit of 5 songs. Sorry about that.")
        getting_songs = False
    else:
        more_music = input("\nAdd more music? (yes/no): ").lower()

    # Adding more music or not?
    if more_music != 'yes' and more_music != 'y':
        getting_songs = False

# display the playlist

# will remove on next version. No longer needed as I added a catch, above
# make sure they entered some songs
# if len(playlist) == 0:
#     print("I think you forget to enter some songs.")
# else:

# shuffle
random.shuffle(playlist)
print("\nShuffled Playlist")
for current_track in playlist:
    print(f"🎵 {current_track}")


print(playlist)