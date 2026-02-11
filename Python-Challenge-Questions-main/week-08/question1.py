# Write a complete Python program that takes a series of 10 integer numbers from the user, and determines and
# prints the smallest value of the numbers.

my_list = []

for i in range(10):
    number = int(input(f"{i + 1}. number: "))
    my_list.append(number)

min_numb = my_list[0]
for numb in my_list:
    if numb < min_numb:
        min_numb = numb

print(f"The smallest number is {min_numb}")
