import turtle
import math
ex1 = turtle.Turtle()
print(ex1)
ex1.pensize(4)
ex1.hideturtle()


def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, length, n)

print(ex1)


circle(ex1, 80)




turtle.mainloop()


