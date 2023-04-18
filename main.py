import turtle
from random import randrange

turtle.Screen().colormode(255)
turtle.hideturtle()


def square():
    turtle.pendown()
    x1, y1 = turtle.position()
    random_x = randrange(-150, 150)
    random_y = randrange(-150, 150)
    turtle.goto(random_x, y1)
    change_pen()
    turtle.goto(random_x, random_y)
    change_pen()
    turtle.goto(x1, random_y)
    change_pen()
    turtle.goto(x1, y1)
    turtle.penup()


def triangle():
    first_cor = turtle.pos()
    turtle.pendown()
    cor1 = randrange(-250, 250), randrange(-250, 250)
    cor2 = randrange(-250, 250), randrange(-250, 250)
    turtle.goto(cor1)
    change_pen()
    turtle.goto(cor2)
    change_pen()
    turtle.goto(first_cor)
    turtle.penup()


def change_pen():
    turtle.pensize(randrange(1, 10))
    turtle.pencolor(randrange(256), randrange(256), randrange(256))


turtle.speed(0)
turtle.penup()
for i in range(20):
    turtle.speed(10)
    q = randrange(4)
    turtle.penup() if q else turtle.pendown()
    change_pen()
    turtle.goto(randrange(-250, 251), randrange(-250, 251))
    if q:
        var = randrange(6)
        if var in (0, 1, 2):
            turtle.dot(randrange(50))
        elif var == 3:
            triangle()
        elif var == 4:
            square()
        else:
            turtle.speed(0)
            turtle.pendown()
            turtle.circle(randrange(30))
            turtle.penup()
print()
turtle.done()
