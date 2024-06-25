'''
    Pseudocode to find a key in boxes (recursively).

    Recursion is a function that calls itself. 
    Need a base-case to know when it's done, otherwise will loop until I run out of memoyr.

iterative approach:

def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile is not empty:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
            pile.append(item)
        elif item.is_a_key():
            print("found the key!")

recursive approach:

def look_for_key(box):
    for item in box:
        if item.is_a_box():
        look_for_key(item) # <--- recursive. This time use "item" as the argument
    elif item.is_a_key():
        print("found the key!")

'''

# def countdown(i):
#     print(i)
#     countdown(i-1)

# countdown(3)

# Python: "RecursionError: maximum recursion depth exceeded"
    # Need to be careful of this in programs like C or C++ though. Python has built-in handling for this, but don't count on that.


def countdown(i):
    print(i)
    if i <= 1: # base case (when it's considered to be "done")
        return
    else:
        countdown(i-1) # recursive case

countdown(3)