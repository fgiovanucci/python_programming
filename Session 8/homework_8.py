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