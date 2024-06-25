phone_book = {}
phone_book["jenny"] = 8675309
phone_book["emergency"] = 911

print(phone_book["jenny"])
print(phone_book["emergency"])

"""
    Qeustion: Imagine if youhad to do this using an array instead. How would you do it?
"""

"""
    Answer: I'd make a 2D array. The problem is this is less intuitive than a hash table and doesn't scale as well.
"""
# define the rows and columns.
names, numbers = (2, 2)

# create the 2D array based on the names and columns
phone_book2 = [[0] * numbers] * names

# return the value at index [0][1] (coordinate)
phone_book2[0] = ["jenny", 8675309]
phone_book2[1] = ["emergency", 911]

print(phone_book2[0][1])
print(phone_book2[1][1])