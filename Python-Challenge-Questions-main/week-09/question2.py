# Write a Python program that finds if an integer list is a palindrome.


size = int(input("Please enter the capacity of the list: "))

my_list = []

for i in range(size):
    numb = int(input(f"Please enter the element {i + 1} of the list:"))
    my_list.append(numb)

print(my_list)

length = len(my_list)
palindrome = True

for i in range(length // 2):
    if my_list[i] != my_list[length - 1 - i]:
        palindrome = False
        break

if palindrome:
    print("This list is a Palindrome.")
else:
    print("This list is not a Palindrome.")
