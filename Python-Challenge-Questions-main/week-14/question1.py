first_list = [8, 6, 4, 2]
second_list = [7, 5, 3, 1]
multiply = []

for i in range(4):
    sum = first_list[i] + second_list[i]
    multiply.append(sum)
    print(f"Number 1: {first_list[i]}+{second_list[i]}={sum}")

result = 1
for number in multiply:
    result *= number

print(f"Result = {result}")
