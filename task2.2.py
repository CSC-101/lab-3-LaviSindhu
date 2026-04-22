def increment_all(nums:list[int]) -> list[int]:
    new_list = []
    for value in nums:
        new_list.append(value + 1)     # Record each value of new_list and value at the end of the loop body.
                                    #the values are: value = 4, new_list = [5]; value = 9, new_list = [5, 10];
                                    #value = 2, new_list = [5, 10, 3]; value = 1, new_list = [5, 10, 3, 2].
    return new_list

result = increment_all([4, 9, 2, 1])