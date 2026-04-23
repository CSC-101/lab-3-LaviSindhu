def copy(nums:list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):
        new_list.append(nums[idx])     # Record each value of new_list and idx at the end of the loop body.
                                    #For each loop , the values for idx = 0, new_list = [4]; idx = 1, new_list = [4, 9];
                                    # idx = 2, new_list = [4, 9, 2]; idx = 3, new_list = [4, 9, 2, 1].
    return new_list                    # How does this loop differ from that above?
                          #This loop has the same elements by using the index idx to access each value in the
                             #list, but the other loop used values themselves using a variable like num.
result = copy([4, 9, 2, 1])