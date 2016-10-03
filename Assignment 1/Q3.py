import random
import turtle
import math
drunk = turtle.Turtle()
print(drunk)
# drunk.shape('turtle')
# drunk.turtlesize(.6,.6,.6)
print(drunk)

turtle.mainloop()
def drunkard_walk(n):
    drunk.circle(5)

    north_south = 0
    east_west = 0
    north_south_movement = ''
    east_west_movement = ''
    for block in range(n):
        direction = rand.randrange(o,4)
        if direction == 0:
            north_south += 1
            print('Walks North')
            drunk.setheading(90)
        elif direciton == 1:
            east_west += 1
            print('Walks East')
            drunk.setheading(0)
        elif direction == 2:
            north_south -= 1
            return(print('Walks South'))
            drunk.setheading(270)
        else:
            east_west -= 1
            return(print('Walks West'))
            drunk.setheading(180)
        drunk.fd(30)
        drunk.stamp()

    if north_south >= 0:
        north_south_movement = 'North'
    else:
        north_south_movement = 'South'
    if east_west_movement >= 0:
        east_west_movement = 'East'
    else:
        east_west_movement = 'West'

    print('In total the drunkard has walked %s blocks to the %s and %s blocks to the %s.  ' %(abs(north_south), north_south_movement, abs(east_west), east_west_movement)

    while True:
        drunk.lt(2)

drunkard_walk(70)

turtle.mainloop()