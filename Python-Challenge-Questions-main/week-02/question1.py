# Write a simple Java program EvaluateFunction.java that reads three integer variables 𝑥, 𝑦, and 𝑧 from the
# user and evaluates the outputs of 𝑓(𝑥, 𝑦) and 𝑔(𝑥, 𝑦, 𝑧) for given values.

x = int(input("Enter integer x: "))
y = int(input("Enter integer y: "))
z = int(input("Enter integer z: "))


def function_f(num1, num2):
    result = ((num1 - num2) / (num1 + num2)) + 3 * num1 * num2
    return round(result)


def function_g(num1, num2, num3):
    result = ((num1 ** 2 - num2 ** 2) / (num1 + num3)) + ((num1 ** 2 + num3 ** 2) / (num2 - num3))
    return round(result)


print(f"f({x},{y}) = {function_f(x, y)}")

print(f"g({x},{y},{z}) = {function_g(x, y, z)}")