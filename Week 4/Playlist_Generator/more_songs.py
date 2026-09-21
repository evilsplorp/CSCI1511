def more_tunes():
    """
    Playlist_Generator 1.7, add more songs function
    Raymond Black
    Asks if user wants to continue adding songs
    Requires yes/y to continue, no/n to end. 
    Anything other response asks user to reenter their input"""
    while True: # 
        more_music = input("\nAdd more music? (yes/no): ").lower().strip()
        if more_music == 'yes' or more_music == 'y':
            return True
        elif more_music == 'no' or more_music == 'n':
            getting_songs = False
            return False
        else:
            print("Please enter yes or no.")