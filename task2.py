def tally(nums:list[int]) -> int:
    total = 0
    for num in nums:
        total = total + num           # Record each value of total and num at the end of the loop body.
                                    #For each each loop , the values are num = 4, total = 4; num = 9,
                                    # total = 13; num = 2, total = 15; num = 1, total = 16. and num at the end was 16
    return total

result = tally([4, 9, 2, 1])