def inc(m:int) -> int:
    return m + 1                             # Record, in order of the calls, each value of m and
                                             # the corresponding return value.
                                    # it calls m = 3 and 4, and it returns 4 and 5.

def check(n:int) -> bool:
    return n > 2                             # Record, in order of the calls, each value of n and
                                             # the corresponding return value.
                                        # The values of n are 0, 1, 2, 3, 4, and it returns False, False, False, True, True

answer = [inc(x) for x in range(5) if check(x)]   # What is the value of answer?
                                            # The answer is [4, 5] because only the values 3 and 4 pass
                                            #  the check, and then 1 is added to each of them.
print()