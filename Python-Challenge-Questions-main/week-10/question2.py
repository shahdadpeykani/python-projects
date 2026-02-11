class Box:

    def __init__(self, width, length, height):

        self.width = width
        self.length = length
        self.height = height

    def volume(self):

        volume = self.width * self.length * self.height
        print(f"The volume of box: {volume}")
        if self.width == self.length == self.height:
            print("It is a Cube")
        else:
            print("It is a  Cuboid")


print("Enter box dimensions: ")

a = int(input())
b = int(input())
c = int(input())

box = Box(a, b, c)
box.volume()
