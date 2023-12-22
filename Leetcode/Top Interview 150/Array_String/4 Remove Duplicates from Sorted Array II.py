def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # if n == nums[i-2] -> i-2, i-1, i/n
    # i does not increment -> 3rd item is replaced by the next greatest value
    i = 0
    for x, n in enumerate(nums):
        if i < 2 or n > nums[i - 2]:
            nums[i] = n
            i += 1
    return i


removeDuplicates([1, 1, 2, 2, 2, 3, 3, 3, 3])
