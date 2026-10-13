class Menu:
    """
    Maintains the menu structure for selecting search types
    """
    def __init__(self, search_song_func, search_album_func, search_artist_func):
        """
        Stores references to the search functions.
        """
        self.search_song = search_song_func
        self.search_album = search_album_func
        self.search_artist = search_artist_func

    def mcm_menu(self, db):
        while True:
            print("\n--- Music Collection Manager ---")
            print("1. Search Database\n2. Exit")
            menu_option = input("Enter choice (1-2): ").strip()

            if menu_option == '2':
                print("\nGoodbye!\n")
                break

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
                    self.search_song(db, q)
                elif sub_menu == '2':
                    self.search_album(db, q)
                elif q and sub_menu == '3':
                    self.search_artist(db, q)
            else:
                print("\nPlease enter 1 or 2.")