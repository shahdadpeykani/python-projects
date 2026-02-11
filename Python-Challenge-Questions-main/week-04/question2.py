# Write a java program to check if a number is divisible by the other. x is divisible by y, if there is no remainder
# left in the division operation.

numb1 = int(input("Input numbers: "))
numb2 = int(input())


def is_divisible(x, y):
    if y == 0:
        print("Division by zero is not allowed.")
    else:
        return x % y == 0


if is_divisible(numb1, numb2):
    print(f"{numb1} is divisible by {numb2}")
else:
    print(f"{numb1} is not divisible by {numb2}")
