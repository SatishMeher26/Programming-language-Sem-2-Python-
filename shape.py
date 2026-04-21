import math 

def area_circle(radius):
    if radius <= 0:
        raise ValueError("Radius cannot be negative or Zero.")
    return math.pi * radius ** 2

def area_rectangle(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width cannot be negative or Zero.")
    return length * width

def area_triangle(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height cannot be negative or Zero.")
    return 0.5 * base * height

