import math

"""" Write a Python program that declares and initializes two double variables, radius (r) and height (h) of a cylinder,
and calculates the volume """


def volume(radius, height):
    pi = math.pi
    return pi * radius ** 2 * height


r = float(input("Enter the radius: "))
h = float(input("Enter the height: "))

result = round(volume(r, h), 3)

print(f"If the radius is {r} and the height is {h} then\nThe volume of the cylinder is {result}")
