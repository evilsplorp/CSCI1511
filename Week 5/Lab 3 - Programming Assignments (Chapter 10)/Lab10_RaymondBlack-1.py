"""
Word Counter
Raymond Black
Purpose: to count all the words in a file
and display how many times each word appears.

initial work used: 
code from Participation Activity 3 as a base

"""


while session.is_running:

    # changing to a menu-based option
    print("\n           Geometry Calculator")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("1. Calculate Circle Area")
    print("2. Calculate Circle Circumference")
    print("3. Calculate Both Circle Area and Circumference")
    print("4. Calculate Rectangle Area")
    print("5. Calculate Rectangle Perimeter")
    print("6. Calculate Both Rectangle Area and Perimeter")    
    print("7. Exit")

    #menu option inputs
    selection = input("\nEnter selection: ").strip()

    if selection in ["1", "2", "3"]:
        user_radius = get_positive_number("\nWhat's the radius of the circle? ")
        result_area = cca(user_radius)
        result_circumference = cc(user_radius)

        if selection == "1":
            print(f"\nThe area is {result_area:.2f}.")
        elif selection == "2":
            print(f"\nThe circumference is {result_circumference:.2f}.")
        elif selection == "3":
            print(f"\nThe area is {result_area:.2f} and the circumference is {result_circumference:.2f}.")

    elif selection in ["4", "5", "6"]:
        user_width = get_positive_number("\nWhat is the width of the rectangle? ")
        user_height = get_positive_number("What is the height of the rectangle? ")

        result_area = rca(user_width, user_height)
        result_perimeter = cp(user_width, user_height)

        square = "\nHey! You made a square! " if user_height == user_width else ""

        if selection == "4":
            print(f"\nThe area is {result_area:.2f}.")
        elif selection == "5":
            print(f"{square}The perimeter is {result_perimeter:.2f}.")
        elif selection =="6":
            print(f"{square}The area is {result_area:.2f} and the perimeter is {result_perimeter:.2f}.")

    elif selection == "7":
        # calculating = False
        session.is_running = False
        break
    else:
        print("\nI think you mistyped. Please enter a number between 1 and 7.")
        continue

    session.ask_to_continue()