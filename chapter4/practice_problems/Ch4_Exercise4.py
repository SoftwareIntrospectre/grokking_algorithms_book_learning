'''
4.4: Remember binary search from Chapter 1? It's a Divide & Conquer (D&C) algorithm too.
     Can you come up with the base case and recursive case for binary search?
'''

# My thought: Try to come up with the code for this, and that will force me to find the base case and recursive case.

# base case: when an element is found that's searched. So if guess == an element in the array.
    # example: search for 7. 7 is found. Return 7.   OR Array is empty, return None.

def recursive_binary_search(arr, item, low=0, high=None):

    # this only needs to be sorted once. No need to do this recursively
    #arr.sort()
    #print(arr)

    # initial value handling
    if high is None:
        high = len(arr) - 1

    if low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
  
        # base case 1: item is found, return
        if guess == item:
            print(guess)
            return guess
        
        # recursive case 1: guess is too high. Search up to to new high point (mid)
        elif guess > item:

            # defining new value for high, instead of storing as a variable
            return recursive_binary_search(arr, item, low, mid - 1)

        # recursive case 1: guess is too low. Search from new low point (mid + 1)
        else:
            # defining new value for low, instead of storing as a variable
            return recursive_binary_search(arr, item, mid + 1, high)

    # base case 2: No item is found, return None
    print(None)
    return None


array1 = sorted([1,8,9,10,12,99])
array2 = sorted([8,9,99,12])
array3 = sorted([8,9,99,12,1478,6])
array4 = sorted([8,9,99,12,1478,6])


recursive_binary_search(array1, 99)
recursive_binary_search(array2, 8)
recursive_binary_search(array3, 12)
recursive_binary_search(array4, 0)