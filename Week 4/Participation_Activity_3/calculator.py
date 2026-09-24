class Calculator:
    """Do we continue calculating shapes or not?"""
    def __init__(self):
        self.is_running = True

    def ask_to_continue(self):
        """Validates yes/no  and returns whether the loop should keep running."""
        while True:
            more = input("\nDo you want to enter another shape? (yes/no): ").lower().strip()
            if more in ['yes', 'y']:
                self.is_running = True
                return True
            elif more in ['no', 'n']:
                self.is_running = False
                return False
            else:
                print("\nSorry, I didn't get that. Was that a yes or no?")