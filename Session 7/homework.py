import math
a = 4
x = 3
y = (x + a/x) / 2
print(y)

x = y
y = (x + a/x) / 2
print(y)

from math import sqrt

while True:
    print(x)
    y = (x + a/x) / 2
    if y == x:
        break
def mysqrt(a):
    x = a/2
    while True:
        y = (x + a/x) / 2
        if y == x:
            break
        x = y
    return x

#in class answers
epsilon = 1e-15
