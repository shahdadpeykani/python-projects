# The program should keep asking for integers to the user until ‘q’ character is entered. Then, the following
# equation should be calculated using the minimum and maximum entered integers.
import math

numbers = []

is_over = True

while is_over:

    numb = input("Enter a number: ")
    numbers.append(numb)

    if numb == "q":
        is_over = False

numbers.pop()
new_list = [int(numb) for numb in numbers]

max_numb = max(new_list)
min_numb = min(new_list)

result = math.sqrt(max_numb + 1) ** math.sqrt(max_numb ** min_numb)
print(f"Result: {result}")
