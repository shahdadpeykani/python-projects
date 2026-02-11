class Complex:

    def __init__(self, real, image):
        self.a = real
        self.b = image

    def display(self):
        if self.b > 0:
            print(f"The complex number is: {self.a}+{self.b}i")
        else:
            print(f"The complex number is: {self.a}{self.b}i")


print("Enter a complex number: ")

a = float(input())
b = float(input())
obj = Complex(a, b)
obj.display()
