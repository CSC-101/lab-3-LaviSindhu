def check(n:int) -> bool:
    return n > 2                             # Record, in order of the calls, each value of n and
                                             # the corresponding return value.
                                    # The values of n are 0, 1, 2, 3, 4 in that order,
                                    # and it returns False, False, False, True, True.

answer = [x for x in range(5) if check(x)]   # What is the value of answer?
print()                                         # the answer is [3,4]