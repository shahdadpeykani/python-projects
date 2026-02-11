# Write a Python program that reads items of two vectors and applies the below given function over
# those vectors.
# 𝑓(𝑥, 𝑦) = 2x + 3y
x = []
y = []

size = int(input("Size of the vectors: "))

if size != 0:

    print("First vector (x): ")
    for i in range(size):
        vector_x = int(input())
        x.append(vector_x)

    print("Second vector (y): ")
    for i in range(size):
        vector_y = int(input())
        y.append(vector_y)

    def my_function(list1, list2):
        result = []
        for item in range(size):
            answer = 2 * list1[item] + 3 * list2[item]
            result.append(answer)
        return result


    print(f"Result: {my_function(x, y)}")
else:
    print("Bye!")
