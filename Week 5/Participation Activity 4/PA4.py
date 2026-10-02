"""
Participation Activity 4
Raymond Black
Purpose: To show an example of an AssertionError and
to use a try-except to catch the error.

2026-10-01
"""

# optionally, lines 2 through 8 can be uncommented and 
# lines 10 through 16 can be commented to test this directly
# print("Enter 4 numbers. The first pair should have the first number smaller than the second. \n"
# "The second pair should have the first number larger than the second.")

# number1 = float(input("Give me your first number. \n"))
# number2 = float(input("Give me your second number, but make it larger than the first one. \n"))
# number3 = float(input("Give me your third number. \n"))
# number4 = float(input("Give me your fourth number, but make it larger than the third one. \n"))

print("\nThe code handles basic division and tests an AssertionError. \n"
      "The assertion requires that the numerator is smaller than the denominator. \n"
      "Instead, the second pair of numbers reverses that to force an error.\n")

number1 = 5
number2 = 10
number3 = 10
number4 = 5

print(f"First pair: {number1}, {number2}\nSecond pair: {number3}, {number4}\n")

try:
    assert number1 <= number2

    result = float(number1 / number2)
    print(f"First division: {result}\n")

    assert number3 <= number4

    result2 = float(number3 / number4)
    print(f"Second division: {result2}\n")

    assert 5 / 10 < 1 
    print("Pass")

except AssertionError:
    print("AssertionError caught, as the code requires a denominator larger than the numerator.\n")