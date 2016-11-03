class Time():       #you do not need () it is the same as Time:
    '''
    Represents the time of day

    attributes: hour, minute, second
    '''
    def __init__(self, hour=0, minute=0, second=0):       # initialization method
        self.hour = hour
        self.minute = minute
        self.second = second



    def print_time(self):
        '''Prints a string representation of the time'''
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))


    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

    def is_as_expected(self, duration, arrival):
        return self.time_to_int() + duration.time_to_int() == arrival.time_to_int()
     
    def increment(self, seconds):
       seconds += self.time_to_int()
       return int_to_time(seconds)

       

def int_to_time(seconds):
    """Makes a new Time object.
    seconds: int seconds since midnight.
    """
    
    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    return Time(hour, minute, second)
    
# def print_time(t):
#     print('%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second))
#with this one you use print_time(start) function package   calling function to do something for me

start = Time(9, 45, 0)
# start.hour = 9
# start.minute = 45
# start.second = 0
# start.print_time()    #OOP with def indented and (start)  calling the object to do something for me 
print(start.time_to_int())   # time to int function print 

end = start.increment(2000)         #first one was 9:45 then we add 2000 secs and get 10:18
end.print_time()
print(end.is_after(start))  #is end after start

traffic = Time(0, 30, 0)
# traffic.hour = 0
# traffic.minute = 30
# traffic.second = 0

expected_time = Time(10, 15, 0)
# expected_time.hour = 10
# expected_time.minute = 15
# expected_time.second = 0

traffic.print_time()
expected_time.print_time()
print(start.is_as_expected(traffic, expected_time))  #when we call this method we only need two times

default_time = Time()
default_time.print_time()



