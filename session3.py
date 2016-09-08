import math
print(math.pi)

import time
print(time.time())
#time gives you time in seconds
seconds = time.time()
print('seconds = ',seconds)

minutes = (seconds// 60)
print('minutes = ',(seconds// 60))


hours = (minutes / 60)
print('hours = ', (minutes // 60))


days = (hours /24)
print('days = ', (hours // 24))

years = (days / 365)
print('years = ', (days // 365))


input()







