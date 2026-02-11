def function_f(numb1, numb2):
    result = (-2 * numb1 ** 2 + numb1 * numb2 - 4) / -numb1
    return result


def function_g(numb1):
    result = -numb1 ** 2 + 5
    return result


x = int(input("Enter integer x: "))
y = int(input("Enter integer y: "))
f = function_f(x, y)
g = function_g(x)

print(f"Here are declared and initialized variables: x = {x}, y = {y}")

print(f"Here are the output values of the functions: f({x}, {y}) = {f}, g({x}) = {g}")
