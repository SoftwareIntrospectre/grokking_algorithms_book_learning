'''
    Write a recursive function to find the maximum number in a list
'''

'''
    input: [1,3,7,9,12]
    output: 12

    input: []
    output: None


    input: ['a', 'b', 0, 'c']
    output: 0


    Base case: When the array is 1 or None.
        - by definition the highest value of a single-value array is that single value
            largest number of [9] is 9
            largest number of ['a'] is None (no numbers)
            largest value of [] is None (nothing there)

                - base case: when there's only 1 number left, or there are no numbers left in a single-element array or an empty array

                - recursive case: compare the base case to the recursive case, return the higher number from recursive process


                [1,2,3]

'''

# my attempt, did not get it.
def find_max_number_in_list(list):

    #print(list)

    highest_number = 0
    
    if len(list) == 1:
        highest_number = list[0]
        return highest_number
    
    elif list is None:
        return highest_number
    
    else:
        if highest_number < list[0]:
            highest_number = list[0]
            return find_max_number_in_list(list[1:])


print(find_max_number_in_list([1,2,3]))
print(find_max_number_in_list([999999, 1,2,3,99,12,85,9999]))


# Correct Answer: I was on the right track, but couldn't accurately translate it into code.
# New ideas: 1. if len(list) == 2: base case is 2 elements, since this is a comparison.
#            2. make the return based on an if else

# Ideas I Was Onto: 1. divide the list from index 1 onward in recursive call
#                   2. Need to make a comparision between two elements
def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max


print(max([1,2,3]))
print(max([999999, 1,2,3,99,12,85,9999]))
