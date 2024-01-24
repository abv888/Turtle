# import colorgram
import turtle
import random

# colors = colorgram.extract('pic.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
# print(rgb_colors)

rgb_colors = [(13, 103, 154), (215, 152, 98), (144, 75, 97), (130, 162, 182), (143, 79, 64), (199, 94, 76),
              (170, 138, 63), (178, 85, 103), (193, 139, 149), (3, 63, 108), (236, 195, 126), (2, 86, 101),
              (149, 169, 166), (57, 116, 83), (5, 100, 90), (51, 150, 176), (223, 175, 182), (74, 49, 47),
              (87, 149, 123), (2, 74, 69), (29, 65, 112), (179, 199, 190), (76, 41, 43), (79, 55, 53), (86, 50, 57),
              (215, 180, 175)]

tim = turtle.Turtle()
tim.penup()
tim.hideturtle()
tim.speed('fastest')
turtle.colormode(255)
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(rgb_colors))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle.Screen()
screen.exitonclick()