'''
    It's important for hash functions to consistently return the same output for the same input.
    If they don't, you won't be able to find your item after you put it in the hash table!

    Which one of these hash functions is consistent?
'''

# 5.1: f(x) = 1 

# 5.2: f(x) = random.random()

# 5.3: f(x) = next_empty_slot()

# 5.4: f(x) = len(x) 

import random

def hash_function1(x):
    return 1

def hash_function2(x):
    return random.random()

# def hash_function3(x):
   #return next_empty_slot()
    # not consistent, because the next empty slot can vary

def hash_function4(x):
    return len(x)


hashtable = {"Apples": 1, "Bananas": 7, "Grapes": 2}
hashtable2 = {"Apples": 1, "Bananas": 7, "Grapes": 2, "Mangoes": 3, "Papayas": 19}

print("hash function 1: test 1A: ", hash_function1(hashtable))
print("hash function 1: test 1B: ", hash_function1(hashtable))
print("hash function 1: test 1C: ", hash_function1(hashtable))
print("hash function 1: test 1D: ", hash_function1(hashtable))


print("hash function 1: test 2A: ", hash_function1(hashtable2))
print("hash function 1: test 2B: ", hash_function1(hashtable2))
print("hash function 1: test 2C: ", hash_function1(hashtable2))
print("hash function 1: test 2D: ", hash_function1(hashtable2))


print("hash function 2: test 1A: ", hash_function2(hashtable))
print("hash function 2: test 1B: ", hash_function2(hashtable))
print("hash function 2: test 1C: ", hash_function2(hashtable))
print("hash function 2: test 1D: ", hash_function2(hashtable))

print("hash function 2: test 2A: ", hash_function2(hashtable2))
print("hash function 2: test 2B: ", hash_function2(hashtable2))
print("hash function 2: test 2C: ", hash_function2(hashtable2))
print("hash function 2: test 2D: ", hash_function2(hashtable2))


print("hash function 4: test 1A: ", hash_function4(hashtable))
print("hash function 4: test 1B: ", hash_function4(hashtable))
print("hash function 4: test 1C: ", hash_function4(hashtable))
print("hash function 4: test 1D: ", hash_function4(hashtable))

print("hash function 4: test 2A: ", hash_function4(hashtable2))
print("hash function 4: test 2B: ", hash_function4(hashtable2))
print("hash function 4: test 2C: ", hash_function4(hashtable2))
print("hash function 4: test 2D: ", hash_function4(hashtable2))


# Answer: 1 and 4 are consistent.