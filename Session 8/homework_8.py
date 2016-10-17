#exercise 2
# team = 'New England Patriots'
# new_team = team.upper()
# print(new_team)

# index = team.find('a')
# print(index)
# print(team.find('En'))

# #exercise 4
# def character_count(my_string, a):
#     result = 0
#     for letter in my_string:
#         if letter == a:
#             result += 1
#     return result        
# print(character_count)



# def word_value(word):
#     total = 0
#     for letter in word:
#         total += ord(letter) - 96
#     return float(total)



#     print(receipt(item_list))

# def rotate_word(my_word, rotate):
#     final_string = ''
#     for char in my_word:
#         if char.isalpha():
#             new_letter = chr((ord(char.lower()) - 97 + rotate) % 26 + 97)
#             final_string += new_letter
#         else:
#             final_string += char
#     return final_string

#exercise 5
str_1 = 'iPAD'
str_2 = 'Babson'
str_3 = 'python'


def any_lowercase1(s):
    for c in s:
        if c.islower():                #if the word starts with a  lower case letter print true
            return True
        else:
            return False
print('1')
print(any_lowercase1(str_1))
print(any_lowercase1(str_2))  
print(any_lowercase1(str_3))     

#2 same as #1
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
print('2')
print(any_lowercase1(str_1))
print(any_lowercase1(str_2))  
print(any_lowercase1(str_3))

#3
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag
print('3')
print(any_lowercase1(str_1))
print(any_lowercase1(str_2))  
print(any_lowercase1(str_3))
def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag
print('4')
print(any_lowercase1(str_1))
print(any_lowercase1(str_2))  
print(any_lowercase1(str_3))
def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
print('5')
print(any_lowercase1(str_1))
print(any_lowercase1(str_2))  
print(any_lowercase1(str_3))