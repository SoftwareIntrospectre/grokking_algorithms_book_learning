"""
   Preparation: Import list of 128 names. Sort names alphabetically, output as an array.
"""


"""
    Exercise 1.1:

    Suppose you have a sorted list of 128 names, and you're searching through it using binary search.
    What's the maximum number of steps it would take?
"""

def is_flat_file(filepath):
    if not((filepath.endswith('.txt')) or (filepath.endswith('.csv'))) :
        print("Expecting '.txt' or '.csv' file extension. Please import a flat file.")
        return False
    
    else:
        print(f"'{filepath}' is a valid flat file. Continuing.")
        return True

def generate_sorted_names_array_from_textfile(textfile_filepath):
 
    if is_flat_file(textfile_filepath):
        names_array = []

        # reading the file in the specified directory
        with open(textfile_filepath, 'r') as names_file:
            names = names_file.read().split('\n')
            for name in names:
                names_array.append(name)

            # can only do binary search on a sorted array
            names_array.sort()

            return names_array
    else:
        return

def print_iterations(iterations):
    print("\n\n iterations: ", iterations)


def is_valid_array_for_binary_search(array, search_index):
    # empty array checks
    if (not(array)):
        return False
    
    # out of bounds checks
    elif (search_index > len(array) - 1) or (search_index < 0):
        return False
    
    else:
        return True


def binary_search(array, search_index):

    iterations = 0

    if is_valid_array_for_binary_search(array, search_index):

        search_index = array[search_index]

        low_index = 0
        hi_index = len(array) - 1

        while low_index <= hi_index:

            iterations += 1

            mid_index = (low_index + hi_index) // 2
            guess_index = array[mid_index]

            # if index is found, return it
            if guess_index == search_index:
                print_iterations(iterations)
                return array[mid_index]
            
            # if too high: decrement hi_index to before mid_index
            elif guess_index > search_index:
                hi_index = mid_index - 1

            # if too low: increment low_index to after mid_index
            else:
                low_index = mid_index + 1

        # index is not found
        print_iterations(iterations)
        return None
    
    else:
        print_iterations(iterations)
        return None
        
names_array1 = generate_sorted_names_array_from_textfile('chapter1/practice_problems/Ch1_Exercise1/128_Names.csv')

print(binary_search(names_array1, 99))
print(binary_search(names_array1, 137))
print(binary_search(names_array1, 80))
print(binary_search(names_array1, -1))
print(binary_search(names_array1, 0))

# The maximum number of steps for 128 names is 7 iterations.
# Confirmed to be correct (back of the book answer.)


"""
    Exercise 1.2:

    Suppose you double the size of the list. What's the maximum number of steps now?
"""

names_array2 = generate_sorted_names_array_from_textfile('chapter1/practice_problems/Ch1_Exercise1/256_Names.xls')

print(binary_search(names_array2, 199))
print(binary_search(names_array2, 258))
print(binary_search(names_array2, 128))
print(binary_search(names_array2, -1))
print(binary_search(names_array2, 0))


names_array2 = generate_sorted_names_array_from_textfile('chapter1/practice_problems/Ch1_Exercise1/256_Names.txt')

print(binary_search(names_array2, 199))
print(binary_search(names_array2, 258))
print(binary_search(names_array2, 128))
print(binary_search(names_array2, -1))
print(binary_search(names_array2, 0))

# The maximum number of steps for 128 names is 8 iterations.
# Confirmed to be correct (back of the book answer.)
