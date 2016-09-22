#Factorial
def factorial(n):
    result = 1
    if n == 1:
        return 1
    print(n)
    result = n * factorial(n-1)
    return result

print(factorial(1))
print(factorial(3))

#Fibonacci

def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(3))

print(fib(10))

#GCD
def gcd(a,b):
    while b != 0:
        c = b
        b = a % b
        a = c 
    return a
print(gcd(5,10))

#Hanoi
def move(n, source, bridge, destination):
    if n >= 1:
        move(n - 1, source, bridge, destination)
        print(source, destination)
        move(n - 1, destination, source, bridge)

move(3, 'A', 'B', 'C')


