"""
Geometry Calculator v1.3
Raymond Black
This application will calculate either the area and circumference of a circle
or the area and perimeter of a rectangle.

***** Modified for Participation Activity 3 *****

2026-09-24
"""

from circle import calc_area as cca, calc_circumference as cc
from rectangle import calc_area as rca, calc_perimeter as cp
# due to the replication of the calc_area function names,
# aliases were used to differentiate the circle and rectangle calculations

def get_positive_number(question):
    """validator function to eliminate repetition in the code"""
    while True:
        try:
            value = float(input(question))
            if value <= 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Please enter a positive number or positive decimal number.")

print("---===Welcome to the Geometry Calculator===---\n")

calculating = True
while calculating:
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
        calculating = False
        break
    else:
        print("\nI think you mistyped. Please enter a number between 1 and 7.")
        continue

    while True:
        more = input("\nDo you want to enter another shape? (yes/no)").lower()
        if more == 'yes' or more == 'y':
            calculating = True
            break
        elif more == 'no' or more == 'n':
            calculating = False
            break
        else:
            print("\nSorry, I didn't get that. Was that a yes or no?")

print("\n-=-=-=-=-=-=-=Have a great day!=-=-=-=-=-=-=-=-\n")