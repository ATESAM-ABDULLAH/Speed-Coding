def canJump(nums):
    """
    You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
    Return true if you can reach the last index, or false otherwise
    :type nums: List[int]
    :rtype: bool
    """
    last_pos = len(nums) - 1
    for i in range(
        len(nums) - 2, -1, -1
    ):  # loop from 2nd last to first item in reverse
        if i + nums[i] >= last_pos:  # if pos reachable from previous idx
            last_pos = i  # update pos
    return last_pos == 0  # True if 1st item is reachable


print(canJump([2, 3, 1, 0, 0]))
