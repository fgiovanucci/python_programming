def binary_search(my_list, x):
    '''
    this function adopts bisection/binary search to find the index of a given
    number in an ordered list
    my_list: an ordered list of numbers from smallest to largest
    x: a number
    returns the index of x if x is in my_list, None if not.
    '''
    first = 0
    last = len(my_list)-1
    found = False
	
    while first<=last and not found:
        midpoint = (first + last)//2
        if my_list[midpoint] == x:
	            found = True
        else:
            if x < my_list[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
	
	    return(found)

my_list = [1, 3, 5, 235425423, 23, 6, 0, -23, 6434]
my_list.sort()

print(binary_search(my_list, -23))
print(binary_search(my_list, 0))
print(binary_search(my_list, 235425423))
print(binary_search(my_list, 30))

# expected output
# 0
# 1
# 8
# None