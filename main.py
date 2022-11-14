import turtle
import random
from turtle import Turtle, Screen

turtle.colormode(255)
color_list = [(234, 245, 239), (206, 159, 99), (233, 213, 102), (43, 104, 143), (131, 167, 193), (150, 79, 56),
              (201, 139, 162), (148, 65, 84), (22, 38, 55), (172, 158, 52), (203, 89, 69), (141, 179, 154),
              (194, 88, 118), (62, 117, 92), (21, 42, 33), (59, 40, 28), (224, 171, 187)]

timmy = Turtle()


def random_color():
    return random.choice(color_list)


timmy.hideturtle()
timmy.penup()
timmy.setheading(225)
timmy.forward(220)
timmy.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    timmy.color(random_color())
    timmy.dot(20)
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(0)
        timmy.back(500)
    print(timmy.position)

Screen().exitonclick()
