import random

ROSTER = {"Beshansky": 0,
          "Collins": 0,
          "Fischer": 1,
          "Giovanucci": 0,
          "Jain": 0,
          "Kim": 0,
          "Lauture": 0,
          "Lee": 0,
          "Maddox": 0,
          "Martinez": 0,
          "Mendez": 0,
          "Oh": 0,
          "Petrone": 1,
          "Posada": 0,
          "Rule": 1,
          "Schilb": 0,
          "Tariq": 0,
          "Wang": 0,
          "Wolf": 0}


def call(roster):
    """
    Among the names that are called least times,
    return one name
    roster: a dict of names and integers

    TO-DO: update dict after every call
    TO-DO: save dict to files
    """
    #dict roster key value, temp is the new dict(), only those key values where value is min 
    # min(roster.values) and then random.choice(in the import random function)
    value_list = roster.values()
    min_value = min(value_list)

    # temp_dict = dict()        # you could also do temp_dict = {} to create a new dictionary 
    names = []          # only use names because we don't care about the number
    for name, number in roster.items():             #roster.item returns the pairs 
        if number == min_value:
            names.append(name)
    return random.choice(names)
    

print(call(ROSTER))