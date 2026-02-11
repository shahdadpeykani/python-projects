# Write a Python program to decide larger of two input numbers. It takes two numbers as input, and prints the
# larger one.

numb1 = int(input("Input numbers: "))
numb2 = int(input())

max_numb = numb1

if numb2 > numb1:
    max_numb = numb2

print(f"The larger number is: {max_numb}")
