def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print (n)
        countdown(n-1)

countdown(5)

# ALWAYS HAVE AN ENDING POINT (if and then the return)

def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)
print_n('Hello', 3)