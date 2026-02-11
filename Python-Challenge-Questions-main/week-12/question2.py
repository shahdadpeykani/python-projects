# warning!! this code is incompleted. I am still trying to figure it out.

operation = input("Enter the string of operations: ")

number = input("Enter the integer: ")
new_list = []
new_numb = []

if len(number) - len(operation) == 1:

    new_list = [letter for letter in operation]

    new_numb = [int(digit) for digit in number]
    print(new_list)
    print(new_numb)

else:
    print("The length of integer is inappropriate.")


def my_function(my_list, number_list):
    result = 0
    for i in my_list:
        for j in number_list:
            if i == "a":
                result = max(j, j+1)
            else:
                result = min(j, j+1)

    return result

print(my_function(new_list, new_numb))