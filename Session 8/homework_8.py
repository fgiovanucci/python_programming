#exercise 2
team = 'New England Patriots'
new_team = team.upper()
print(new_team)

index = team.find('a')
print(index)
print(team.find('En'))

def character_count(my_string, a):
    result = 0
    for letter in my_string:
        if letter == a:
            result += 1
    return result        
print(character_count)


# def word_value(word):
#     total = 0
#     for letter in word:
#         total += ord(letter) - 96
#     return float(total)

# def receipt(my_list):
#     max_length = 0
#     for word in my_list:
#         if len(word) > max_length:
#             max_length = len(word)
#     grand_total = 0
#     for word in my_list:
#         print('{:{align}{width}}'.format(word, align='<', width=str(max_length+4))+'{:{align}{width}}'.format('$'+ str(word_value(word))+'0', align='>', width='5'))
#         grand_total += word_value(word)
#     print('--------------------------')
#     print('{:{align}{width}}'.format('Total', align='<', width=str(max_length+4))+'{:{align}{width}}'.format('$'+ str(grand_total)+'0', align='>', width='5'))

# item_list = ['bananas', 'rice', 'paprika', 'potato chips', 'stuff', 'other stuff']

# receipt(item_list)

# def rotate_word(my_word, rotate):
    # final_string = ''
    # for char in my_word:
    #     if char.isalpha():
    #         new_letter = chr((ord(char.lower()) - 97 + rotate) % 26 + 97)
    #         final_string += new_letter
    #     else:
    #         final_string += char
    # return final_string