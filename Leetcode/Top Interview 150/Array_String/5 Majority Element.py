def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # majority =  occurence > n/2 . Thus must occupy atleast 50% of the array
    # left:0 - n/2, middle:n/4 - 3n/4, right: n/2 - 0
    # n//2 is the common factor
    # only works with numeric data
    nums.sort()
    return nums[len(nums) // 2]


print(majorityElement([3, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1]))
