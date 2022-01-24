# implementation of the binary search pattern algorithm!

#  proving that binary search is faster than the normal(naive) search.

# where naive search : scans entire list and ask if it's equal to the target

# # if yes,return the index. else

# if no, then return -1

def naive_search(l, target):
    # example l = [1, 3, 10, 12]
    for i in range(len(l)):
        if l[i] == target:
            return i
        return -1

# binary search used the divide and conquer approach 
# we will leverage that our list is sorted.
def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) -1

    if high < low:
        return -1


    # example l = [ 1, 3, 5, 10, 12] should return 3
    midpoint = (len(l)) // 2 # 2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    else:
        # target > l[midpoint]
        return binary_search(l, target, midpoint+1, high)

if __name__==" __main__":
    l = [1, 3, 5, 10, 12]
    target = 10
    print(naive_search(l, target))
    print(binary_search(l, target)) 
