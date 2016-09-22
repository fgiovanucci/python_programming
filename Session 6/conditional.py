'''
age = int(input("How old are you?"))
if age >= 21:
    print('your age is' + str(age) + '.')
    print('Yes, you can.')
elif age >= 6:
    print('Your age is', age)
    print('You are a teenager, no you cannot.')
else:
    print('Your age is', age)
    print('No, not allowed')


#sample
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')
'''

#Nested Conditions
x = 1
y = 2

if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        prnt('x is greater than y')
