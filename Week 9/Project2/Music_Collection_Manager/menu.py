from pathlib import Path
import json

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

    def select_and_load_db(self):
        """
        Prompts the user for a JSON file, validates choices via try-except KeyError,
        and ensures a valid database state is loaded before proceeding.
        """
        base_dir = Path(__file__).parent
        files_map = {
            "1": ("music.json", base_dir / "music.json"),
            "2": ("bad_music.json", base_dir / "bad_music.json"),
            "3": ("fake_music.json", base_dir / "fake_music.json")
        }

        while True:
            print("\n--- Music File Selector ---")
            print("1. Load Option 1 (music.json)")
            print("2. Load Option 2 (bad_music.json)")
            print("3. Load Option 3 (fake_music.json)")
            file_choice = input("Select music database (1-3): ").strip()

            try:
                filename, chosen_path = files_map[file_choice]
                print(f"\nLoading music file: '{filename}'...")
            except KeyError:
                print("Invalid choice. Please select option 1, 2, or 3.")
                continue

            if not chosen_path.exists():
                print(f"\nError: The music database file '{chosen_path}' does not exist.\n")
                continue  

            with open(chosen_path, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                    return data.get("MusicDatabase", data)
                except json.JSONDecodeError:
                    print(f"\nError: The music database file '{chosen_path}' is not a valid JSON.\n")

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