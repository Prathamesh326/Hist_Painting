# import colorgram
#
# colors = colorgram.extract('spot_painting.jpg', 6)
#
# rgb_colors = []
#
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new_tuple = (r, g, b)
#     rgb_colors.append(new_tuple)

'''10*10   20_50_20'''
import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.speed('fastest')
screen = t.Screen()
tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
tim.hideturtle()
number_of_dots = 100
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

for i in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(50)
    tim.pendown()

    if i % 10 == 0:
        tim.penup()
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen.exitonclick()