"""
Circle calculator functions
Raymond Black
These functions will calculate the area 
and circumference of a circle.
Was necessary to import math to handle pi.
2026-09-16
"""

import math

def calc_area(radius):
    circle_area = math.pi * (radius ** 2)
    return circle_area

def calc_circumference(radius):
    circle_circumference = 2 * math.pi * radius
    return circle_circumference
