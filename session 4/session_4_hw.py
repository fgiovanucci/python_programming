#Session 4 homework

import math

def quadratic(a, b, c):
    root = b**2 - 4*a*c
    if root < 0:
        root = abs(complex(root))
        j = complex( 0, 1)
        x1 = (-b + j + math.sqrt(root))/2*a
        x2 = (-b + j + math.sqrt(root))/2*a
        return x1, x2
    else:
        x1 = (-b+ math.sqrt(root))/2*a
        x2 = (-b + math.sqrt(root))/2*a
        return x1, x2

print(quadratic(1,2,3))

print(quadratic(1, 9, 4))

#did some research online

input()

