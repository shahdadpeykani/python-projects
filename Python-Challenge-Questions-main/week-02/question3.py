number = int(input("Enter a 4 digit number: "))

digit = []
term = ["Thousands", "Hundreds", "Tens", "Units"]

for i in range(4):
    digit.append(int(number % 10))
    number /= 10

digit.reverse()

for i in range(4):
    print(f"{term[i]}: {digit[i]}")
