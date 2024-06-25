def binary_search(arr, item):
    low = 0 # pointer to the first earliest index in the array
    high = len(arr) - 1 # pointer to the final index index in the array

    while low <= high: # condition: these two pointers are different indeces in the array.
        mid = (low + high) // 2 # rounding down to the nearest whole number. Check the middle element.
        guess = arr[mid]

        if guess == item: # found the item
            return mid
        
        elif guess > item: # guess was to high
            high = mid - 1 # decrement high to before mid

        else:  # guess was too low1
            low = mid + 1 # increment low to after mid

    return None # item does not exist in the array


my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))