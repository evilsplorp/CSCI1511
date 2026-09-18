def more_tunes():
    """asks if user wants to continue adding music"""
    while True: # 
        more_music = input("\nAdd more music? (yes/no): ").lower().strip()
        if more_music == 'yes' or more_music == 'y':
            return True
        elif more_music == 'no' or more_music == 'n':
            getting_songs = False
            return False
        else:
            print("Please enter yes or no.")