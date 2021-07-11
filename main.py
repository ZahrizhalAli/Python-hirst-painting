from turtle import Turtle, Screen, colormode
from random import choice
# colormode
colormode(255)
color_list = [(212, 149, 95), (215, 80, 62), (47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40), (155, 73, 60), (122, 167, 195), (40, 22, 29), (39, 19, 15), (209, 70, 89), (192, 140, 159), (39, 131, 91), (125, 179, 141), (75, 164, 96), (229, 169, 183), (15, 31, 22), (51, 55, 102), (233, 220, 12), (159, 177, 54), (99, 44, 63), (35, 164, 196), (234, 171, 162), (105, 44, 39), (164, 209, 187), (151, 206, 220)]

max = Turtle()
num_dots = 100

max.speed(0)
max.hideturtle()
max.setheading(225)
max.penup()
max.forward(320)
max.setheading(0)

for dots in range(1, num_dots+1):
    max.dot(20, choice(color_list))
    max.penup()
    max.forward(50)
    if dots % 10 == 0:
        max.setheading(90)
        max.forward(50)
        max.setheading(180)
        max.forward(500)
        max.setheading(0)


screen = Screen()

screen.exitonclick()