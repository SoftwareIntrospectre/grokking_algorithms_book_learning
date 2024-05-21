'''
4.4: Remember binary search from Chapter 1? It's a Divide & Conquer (D&C) algorithm too.
     Can you come up with the base case and recursive case for binary search?
'''

# My thought: Try to come up with the code for this, and that will force me to find the base case and recursive case.

# base case: when an element is found that's searched. So if guess == an element in the array.
    # example: search for 7. 7 is found. Return 7.   OR Array is empty, return None.

def recursive_binary_search(arr, search_item):

    found = None

    print("arr: ", arr)
    #print("search_item", search_item)

    if len(arr) == 1:
        if search_item == arr[0]:
            found = search_item
            return found
        
    elif len(arr) > 1:
        arr.pop()
        return recursive_binary_search(arr[1:], search_item)
    
    else:
        return None
    
recursive_binary_search([1,8,9,10,12], 99)
recursive_binary_search([1,8,9,10,12], 8)