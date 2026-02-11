# Write a Python program that reads a number in octal format and converts its decimal value. The digits
# of the number should be kept in an array.
import math

digits = []

original_octal = input("Enter an octal number: ")
length = len(original_octal)

octal = int(original_octal)

for i in range(length):
    digit = octal % 10
    octal //= 10
    digits.append(digit)

sum = 0

for i in range(length):
    sum += digits[i] * math.pow(8, i)

print(f"{original_octal} in decimal: {int(sum)}")
