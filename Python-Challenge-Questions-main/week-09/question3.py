first_list = []
second_list = []

print("Enter first list: ")
for i in range(5):
    value = input()
    first_list.append(value)

print("Enter second list: ")
for i in range(5):
    value = input()
    second_list.append(value)

first_list.extend(second_list)
first_list.sort()

print(first_list)
