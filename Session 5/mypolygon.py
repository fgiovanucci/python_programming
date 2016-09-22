import turtle
jerry = turtle.Turtle()

'''
print(jerry)
jerry.fd(100)
jerry.lt(90)
jerry.fd(100)
jerry.lt(90)
jerry.fd(100)
jerry.lt(90)
jerry.fd(100)

def square(t, length):
    t.fd(length)
    t.lt(90)
    t.fd(length)
    t.lt(90)
    t.fd(length)
    t.lt(90)
    t.fd(length)
    t.lt(90)
   #print(t)
 
#exercise 2.2
def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
'''
#exercise 2.3
def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)


jerry = turtle.Turtle()
#square(jerry, 100)
#polygon(jerry, 50, 12)

#polygon(jerry, n=7, length =70)
#identify or follow the order above (t, length, n) or (t, n=, length =)


#exercise 2.4
import math


def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, length, n)

def yin(radius):
    circle(jerry, radius/2)
    circle(jerry, radius)

yin(80)







turtle.mainloop()