def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    i = 0
    for x in nums:
        if x != val:
            nums[i] = x
            i += 1
    print(nums)
    return i


print(removeElement([0, 1, 3, 2, 3], 2))
