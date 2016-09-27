
def crazy_about_9(a, b):
    if a == 9:
        return(True)
    elif (a - b == 9):  
        return(True)
    elif (b - a == 9):
        return (True)
    elif (a + b == 9):
        return(True)  
    else:
        return(False)

print(crazy_about_9(2, 9))
print(crazy_about_9(4, 5))
print(crazy_about_9(3, 8))

#2
def leap_year(year):
    if n%4==0 and n%100!=0:
       elif n%400==0:
            print(n,' is a leap year.'))
    elif n%4!=0:
        print(n, " is not a leap year.")

print(leap_year(1900))
print(leap_year(2016))
print(leap_year(2017))
print(leap_year(2000))

   
    