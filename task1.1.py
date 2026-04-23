def square(n:int) -> int:
    return n * n                           # Record, in order of the calls, each value of n and
                                           # the corresponding return value.
                                    #The values of n  are = 1, 2, 3, 4, and the
                                    #corresponding return values are 1, 4, 9, and 16.
squares = [square(x) for x in [1,2,3,4]]   # What is the value of squares and how does this relate to the
print()                                     # values recorded above?
                                    #The list squares is [1, 4, 9, 16], which is formed by
                     #applying the function square(x) = x² to each element of the list [1, 2, 3, 4].
