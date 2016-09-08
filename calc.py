print(46+37+38)
print(2016-1996)
print(15/3)
print(5*5)
print(2**6)

#Session 2 assigment
# 1
print((4/3)*(3.14*(5**3)))
#2
OGbookprice = 24.95

storediscount = OGbookprice*.4

ship1 = 3
ship2 = .75
totalorder= (storediscount + 3) + (storediscount *.75)*59

#3
seconds = 1
minutes = 60
hours = 60 * minutes
leaveat = 6 * hours + 52 * minutes
slow_pace = 2* (8 * minutes + 15 *seconds)
fast_pace = 3 * (7 * minutes + 12 * seconds)
full_run = slow_pace + fast_pace + leaveat

time = full_run // hours

timeratio = full_run % hours
time_minutess = timeratio // minutes
time_seconds = timeratio % minutes
print( 'Total Run : [], Hours: [], Minutes: [], Seconds: []'. format(full_run, time, time_minutes, time_seconds))

#4
grade= ((89-82)/82)*100
print('Grade: %.1f%%' % grade)

