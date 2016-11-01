class Time():       #you do not need () it is the same as Time:
    '''
    Represents the time of day

    attributes: hour, minute, second
    '''
    def print_time(self):
        '''Prints a string representation of the time'''
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))


    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

    def increment(self, seconds):
       seconds += self.time_to_int()
       return int_to_time(seconds)
       
       

def int_to_time(seconds):
    """Makes a new Time object.
    seconds: int seconds since midnight.
    """
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
    
# def print_time(t):
#     print('%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second))
#with this one you use print_time(start) function package   calling function to do something for me

start = Time()
start.hour = 9
start.minute = 45
start.second = 0
# start.print_time()    #OOP with def indented and (start)  calling the object to do something for me 
print(start.time_to_int())   # time to int function print 

end = start.increment(2000)
end.print_time()
print(end.is_after(start))



