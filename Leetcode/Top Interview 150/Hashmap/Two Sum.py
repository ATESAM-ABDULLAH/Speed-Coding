def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for x in range(len(nums)):
        y = target - nums[x]
        if y in nums and nums.index(y) != x:
            return [x, nums.index(y)]
