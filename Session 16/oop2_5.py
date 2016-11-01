#Exercise 5
#1

class datetime.date:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
# 2    
class datetime.date(year,month,day):
    MINYEAR <= year <= MAXYEAR
    1 <= month <= 12
    1 <= day <= month
    input(print('Please input your Birthday here: (mm/dd/yyyy)') month, day, year)
    return(month, day, year)

#I tried number 3 but I know I was very far off.
