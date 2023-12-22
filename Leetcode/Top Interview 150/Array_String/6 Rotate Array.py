def rotate(nums, k):
    """
    Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    k = k % len(nums)  # remove full loops
    nums[:] = nums[-k:] + nums[:-k]  # [:] is necessary for inplace
    return nums


print(rotate([1, 3, 2, 1], 3))
