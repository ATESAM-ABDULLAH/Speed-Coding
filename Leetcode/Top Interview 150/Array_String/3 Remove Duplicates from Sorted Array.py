def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    j = 1
    for i in range(1, len(nums)):
        print(j, i, nums)
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1

    return j


a = [1, 1, 1, 3, 3, 3, 4, 5, 5]
# print(a[len(a)-1])
print(removeDuplicates(a))
