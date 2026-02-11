# import colorgram
import turtle
from turtle import Turtle, Screen
import random
# rgb_colors =[]
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     r = color.rgb.g
#     g = color.rgb.r
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
turtle.colormode(255)
color_list = [(252, 235, 243), (13, 198, 32), (236, 248, 25), (76, 40, 188), (247, 244, 253), (216, 39, 69),
              (227, 238, 5),
              (159, 227, 49), (40, 29, 154), (76, 212, 15), (153, 17, 17), (36, 241, 161), (16, 195, 12),
              (21, 223, 120),
              (10, 68, 31),
              (15, 61, 8), (141, 223, 206), (97, 11, 62), (159, 219, 11), (209, 54, 229), (21, 19, 49), (157, 238, 216),
              (74, 79, 212),
              (228, 10, 238), (212, 73, 168), (233, 93, 198), (231, 65, 239), (88, 217, 51)]

timmy = Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)
    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen = Screen()
screen.exitonclick()