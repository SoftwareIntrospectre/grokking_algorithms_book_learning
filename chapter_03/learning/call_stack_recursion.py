def fact(x):
    if x == 1:
        print(x)
        return 1
    
    else:
        x = x * fact(x-1)
        print(x)
        return x
    

# fact(7)

''''

Operations: Get to the base case

A. fact(7)
   x = 7
    7 != 1
    so x = (7- 1) --> 6

    call fact(6)

B. fact(6)
    x = 6
    6 != 1
    so x = (6 - 1) --> 5

    call fact(5)


C. fact(5)
    x = 5
    5 != 1
    so x = (5- 1) --> 4

    call fact(4)
    

D. fact(4)
    x = 4
    4 != 1
    so x = (4 - 1) --> 3

    call fact(3)


E. fact(3)
    x = 3
    3 != 1
    so x = (3 - 1) --> 2

    call fact(1)

F. fact(2)
    x = 2
    2 != 1
    so x = (2 - 1) --> 1

    call fact(1)

G. fact(1)
    x = 1
    1 == 1
    
    return x
    
Operations: Return the resulting values from the call stack.

G. fact(1)
    return 1 * (1) = 1 --> (1 * 1) --> 1
        return 1 to fact(2)

F. fact(2) 
    return 2 * (1) --> 2
        return 2 to fact(3)

E. fact(3) 
    return 3 * (2) --> 6
        return 6 to fact(4)

D. fact(4) 
    return 4 * (6) -- > 24
        return 24 to fact(5)

C. fact(5) 
    return 5 * (24) --> 120
        return 120 to fact(6)

B. fact(6)
    return 6 * (120) --> 720
    return 720 to fact(7)

A. fact(7)
    return 7 * (720) ---> 5040
    return 5040 (done)

    (*) prediction: if the initial function call was fact(8) instead: return 5040 to fact(8)

    fact(8)
        return 8 * (5040) --> 40,320
            return 40320 (done) 
'''

fact(8) # yes, I got it correct! Woo!

# This works because the function call has 2 different values for x: 
    # The x of the function call itself. fact(8) has x = 8, and the result of the previous call stack result.
    # Second x (fact(x-1)) is 5040. Even though variable is the same, there's more than one in each function call.