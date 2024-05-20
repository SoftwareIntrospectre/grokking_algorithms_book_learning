'''
    4.2: Write a recursive function to count the number of items in a list
'''

def count_items_in_list(list):

    #print(list)

    if not list:
        return 0
    
    return 1 + count_items_in_list(list[1:])

print(count_items_in_list([1,2,3,4,5]))
print(count_items_in_list([8,8,8,8,8,8,8,8,8,8,8,8,8]))
print(count_items_in_list([]))
print(count_items_in_list(['this', 'and', 'that']))


'''
    My intuition was correct. That's the answer.
'''