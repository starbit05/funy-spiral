import turtle
jef = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")

jef.pensize(1.5)
jef.pencolor("white")
jef.speed(0)
for i in range(9999999999):
    jef.forward(1.5 * i)
    jef.left(91)


turtle.exitonclick()


