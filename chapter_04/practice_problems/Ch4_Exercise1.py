
'''
    4.1: Write out the code for the earlier sum function
'''


'''
    1. Figure out what the Base Case is.

    2. Divide or decrease the problem until it becomes the base case.


    Goal is to take all numbers from the input array and add them together, so base case is if there is 0 or 1 elements in the array
'''


'''my first attempt (incorrect)

Why this does NOT work: The base case is only valid if the result is 0, not if the array is empty. Wrong base case. The idea of separating the current_index from the rest of the array is an OK idea, but I did not separate it from the array itself.

Example:
    1 + [1,2,3,4] --> not valid.
'''
# def recursive_sum(arr):
#     print(arr)

#     if (len(arr)) < 1:
#         return 0
    
#     else:
#         current_index = arr[0]
#         arr.pop(current_index)
#         current_index + recursive_sum(arr)

'''correct answer

# Why this works: The base case is an empty array. The recursive case is summing the first element with the rest of the array, then returning it. If this is returned, the array will reduce in size each time.
# Then once I get to the base case, all of the returned values will add together.


recursive_sum([1,2,3,4])
    return [1] + [2, 3, 4]
        return [2] + [3, 4]
            return 3 + [4]
                return []
            return 7
        return 2 + 7 = 9
    return 1 + 9
return 10
'''

def recursive_sum(arr):
    if arr == []:
        return 0
    return arr[0] + sum(arr[1:])

print(sum([1,2,3,4]))
print(recursive_sum([1,2,3,4]))

'''What I learned: Each step needs to build on the previous one, and the algorithm will scale. Need to think in these terms.'''