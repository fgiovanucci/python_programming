import math
import random

power_of_two = [3,7,15,31,63]

pile = random.randrange(10, 101)
turn = random.randrange(0, 2)
strategy = random.randrange(0, 2)

print('The pile size at the start has %s marbles' %(pile))
def nim():
    if strategy == 0:
        print('Human Wins')
    else:
        print('Computer Wins')

    while pile > 2:
        if turn == 0:
            print('Computers Turn')
            if strategy == 0 or turn in power_of_two:
                computer_takes = random.randrange(1, pile // 2+1)
            else:
                for p in power_of_two:
                    if(pile // 2 >= pile - p) and (pile - p >0):
                      computer_takes = pile - p  
                      break
            pile -= computer_takes
            print('The Computer chose %2 from the pile.  There are %d remaining' %(computer_takes, pile))
            going_first = 1
        else:
            if pile == 2:
                break
            print('It is your turn now')
            human_turn = 0
            while human_turn < 1 or human_turn > pile // 2:
                human_turn = int(input('Please enter a number between 1 and %d: ' %(pile // 2)))
            pile -= human_turn
            print('There are now only %d marbles remaining' %(pile))
            going_first = 0
    if going_first == 0:
        print('You have lost')
        return False
    else:
        print('Congrats! you have won')

    

            