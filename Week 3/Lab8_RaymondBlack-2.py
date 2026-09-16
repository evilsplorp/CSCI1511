"""
Geometry Calculator v1.2
Raymond Black
This application will calculate either the area and circumference of a circle
or the area and perimeter of a rectangle.

2026-09-16
"""

from circle import calc_area as cca, calc_circumference as cc
from rectangle import calc_area as rca, calc_perimeter as cp
# due to the replication of the calc_area function names,
# aliases were used to differentiate the circle and rectangle calculations

# I need to learn to read through the whole instructions. Refactor time...

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

    #menu option input
    selection = input("\nEnter selection: ").strip()

    if selection == "1":
        user_radius = get_positive_number("\nWhat's the radius of the circle? ")
        result_area = cca(user_radius)
        print(f"\nThe area is {result_area:.2f}.")

    elif selection == "2":
        user_radius = get_positive_number("\nWhat's the radius of the circle? ")
        result_circumference = cc(user_radius)
        print(f"\nThe circumference is {result_circumference:.2f}.")

    elif selection == "3":
        user_radius = get_positive_number("\nWhat's the radius of the circle? ")
        result_area = cca(user_radius)
        result_circumference = cc(user_radius)
        print(f"\nThe area is {result_area:.2f} and the circumference is {result_circumference:.2f}.")

    elif selection == "4":
        user_width = get_positive_number("\nWhat is the width of the rectangle? ")
        user_height = get_positive_number("\nWhat is the height of the rectangle? ")
        result_area = rca(user_width, user_height)
        print(f"\nThe area is {result_area:.2f}.")

    elif selection == "5":
        user_width = get_positive_number("\nWhat is the width of the rectangle? ")
        user_height = get_positive_number("\nWhat is the height of the rectangle? ")
        result_perimeter = cp(user_width, user_height)
        if user_height == user_width:
            print(f"\nHey! You made a square! The perimeter is {result_perimeter:.2f}.")
        else:
            print(f"\nThe perimeter is {result_perimeter:.2f}.")

    elif selection == "6":
        user_width = get_positive_number("\nWhat is the width of the rectangle? ")
        user_height = get_positive_number("\nWhat is the height of the rectangle? ")
        result_area = rca(user_width, user_height)
        result_perimeter = cp(user_width, user_height)
        if user_height == user_width:
            print(f"\nHey! You made a square! The area is {result_area:.2f} and the perimeter is {result_perimeter:.2f}.")
        else:
            print(f"\nThe area is {result_area:.2f} and the perimeter is {result_perimeter:.2f}.")
    elif selection == "7":
        calculating = False
        break
    else:
        print("\nI think you mistyped. Please enter a number between 1 and 7.")
        continue

#    shape = input("\nDo you want to calculate information for a circle or rectangle? (q to quit)").lower()
    # if shape == "circle" or shape == 'c':
    #     user_radius = get_positive_number("\nWhat's the radius of the circle? ")
    #     while True:
    #         which_circle_calc = input("\nDid you want to calculate the circumference, the area, or both for the circle? (c/a/b)").lower()
    #         if which_circle_calc == 'circumference' or which_circle_calc == 'c':
    #             result_circumference = cc(user_radius)
    #             print(f"The circumference is {result_circumference:.2f}.")
    #             calculating = False
    #             break
    #         elif which_circle_calc == 'area' or which_circle_calc == 'a':
    #             result_area = cca(user_radius)
    #             print(f"The area is {result_area:.2f}.")
    #             calculating = False
    #             break
    #         elif which_circle_calc == 'both' or which_circle_calc == 'b':
    #             result_area = cca(user_radius)
    #             result_circumference = cc(user_radius)
    #             print(f"The area is {result_area:.2f} and the circumference is {result_circumference:.2f}.")
    #             calculating = False
    #             break
    #         else:
    #             print("I think you mistyped. ")

    # elif shape == "rectangle" or shape == 'r':
    #     user_height = get_positive_number("\nWhat is the height of the rectangle? ")
    #     user_width = get_positive_number("\nWhat is the width of the rectangle? ")

    #     while True:
    #         which_rectangle_calc = input("\nDid you want to calculate the area, the perimeter, or both for the rectangle? (a/p/b)").lower()
    #         if which_rectangle_calc == 'area' or which_rectangle_calc == 'a':
    #             result_area = rca(user_height, user_width) 
    #             print(f"The area is {result_area:.2f}.")
    #             calculating = False
    #             break
    #         elif which_rectangle_calc == 'perimeter' or which_rectangle_calc == 'p':
    #             result_perimeter = cp(user_height, user_width)
    #             if user_height == user_width:
    #                 print(f"Hey! You made a square! The perimeter is {result_perimeter:.2f}.")
    #             else:
    #                 print(f"The perimeter is {result_perimeter:.2f}.")
    #             calculating = False
    #             break
    #         elif which_rectangle_calc == 'both' or which_rectangle_calc == 'b':
    #             result_area = rca(user_height, user_width)
    #             result_perimeter = cp(user_height, user_width)
    #             if user_height == user_width:
    #                 print(f"Hey! You made a square! The area is {result_area:.2f} and the perimeter is {result_perimeter:.2f}.")
    #             else:
    #                 print(f"The area is {result_area:.2f} and the perimeter is {result_perimeter:.2f}.")
    #             calculating = False
    #             break
    #         else:
    #             print("I think you mistyped.")

    # elif shape == "q" or shape == 'quit':
    #     calculating = False
    #     break

    # else:
    #     print("We can only calculate values for a circle or rectangle.")
    #     continue

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

print("\nHave a great day!")