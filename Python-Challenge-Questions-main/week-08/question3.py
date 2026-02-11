number = int(input("Enter a number: "))

factors = []
for i in range(number + 1):
    i += 1
    if number % i == 0:
        factors.append(i)


def display(length):
    if length > 2:
        print("Number's of factors are: ")
        print(factors)

    else:
        print("Number's of factors are: ")
        print(factors)
        print("It's a prime number.")


display(len(factors))
