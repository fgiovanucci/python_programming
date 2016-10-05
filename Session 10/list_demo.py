# list_1 = [10, 20]

# AFC_east = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']

# a_nested_list = ['spam', 2.0, 5, [10, 20]]
# print(AFC_east)

# AFC_east[3] = 'New York Giants'
# print(AFC_east)

# print(AFC_east[0:2])
# print(AFC_east[2:4]) #after 2 but before 4

# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', ['Ruby', 'On Rail'], 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
# print(L[0][0])
# print(L[2][2])
# print(L[1][2][1])

# for team in AFC_east:
#     print(team)

# numbers = [2,0,1,6,9]

# for i in range(len(numbers)):
#     numbers[i] = numbers[i] * 2

# print(numbers)

# my_list = ['spam', 1, ['New England Patriots', \
#                        'Buffalo Bills', 'Miami Dolphins', \
#                        'New York Giants'], \
#            [1, 2, 3]]
# print(len(my_list))


# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# print(c)

# print([0] * 4)

# print(['Tom Brady', 'Bill Belichick']*3)

# t = ['a', 'b', 'c', 'd', 'e', 'f']
# #['b','c']
# print(t[1:3])


# t[1:3] = ['x', 'y']
# print(t)


# EXAMPLE FROM LINK ON BB
a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333), a.count(66.25), a.count('x'))
a.insert(2,-1)
a.append(333)
print(a)

def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res
print(only_upper('Happy'))

